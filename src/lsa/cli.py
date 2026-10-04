"""Command-line entry point: `uv run lsa <command>`."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from lsa import paths


def _count(args: argparse.Namespace) -> None:
    from lsa import count as cnt

    if args.family != "hn":
        raise SystemExit(
            f"family {args.family!r} has no counter yet (implemented: hn)"
        )
    if not args.terms.exists():
        raise SystemExit(f"terms csv not found: {args.terms}")
    from lsa.sources import hn

    snapshot = args.snapshot or hn.snapshot_path()
    if not snapshot.exists():
        raise SystemExit(f"snapshot not found: {snapshot}")
    terms = cnt.load_terms(args.terms)
    records = hn.count_terms(snapshot, terms)
    out = cnt.append_counts(records, args.counts)
    proxy = hn.sample_token_lengths(snapshot, terms)
    print(cnt.format_table(records))
    print(f"token proxy: {proxy:.1f} tokens/comment (word_count x 1.33)")
    print(f"wrote {len(records)} rows to {out}")


def _estimate(args: argparse.Namespace) -> None:
    from lsa import estimate as est

    if not args.counts.exists():
        raise SystemExit(f"counts parquet not found: {args.counts}")
    counts = est.read_counts(args.counts)
    passes = est.load_passes(args.passes)
    price = est.input_price(args.prices, args.model)
    out = est.estimate(counts, passes, price, target_usd=args.target)
    if args.json:
        print(json.dumps(asdict(out), indent=2))
    else:
        print(est.format_table(out))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lsa")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_count = sub.add_parser(
        "count", help="count items per source and upsert counts.parquet"
    )
    p_count.add_argument("--family", required=True, help="count family to run")
    p_count.add_argument(
        "--terms",
        type=Path,
        default=paths.RESEARCH / "search_terms.csv",
        help="category,region,term csv of search terms",
    )
    p_count.add_argument(
        "--counts",
        type=Path,
        default=None,
        help="counts parquet to upsert (default: data/derived/counts.parquet)",
    )
    p_count.add_argument(
        "--snapshot",
        type=Path,
        default=None,
        help="override LSA_HN_SNAPSHOT / the default HN snapshot path",
    )
    p_count.set_defaults(func=_count)

    p_est = sub.add_parser(
        "estimate", help="print a Jev cost estimate from counted items"
    )
    p_est.add_argument(
        "--counts",
        type=Path,
        default=paths.DERIVED / "counts.parquet",
        help="parquet of CountRecord rows from the collectors",
    )
    p_est.add_argument(
        "--passes",
        type=Path,
        default=paths.ROOT / "configs" / "passes.toml",
    )
    p_est.add_argument(
        "--prices",
        type=Path,
        default=paths.ROOT / "configs" / "prices.toml",
    )
    p_est.add_argument("--model", default="jev-1.13.0")
    p_est.add_argument("--target", type=float, default=25.0)
    p_est.add_argument("--json", action="store_true")
    p_est.set_defaults(func=_estimate)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
