"""Command-line entry point: `uv run lsa <command>`."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from lsa import paths


def _not_implemented(_args: argparse.Namespace) -> None:
    print("not implemented")


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

    sub.add_parser("count").set_defaults(func=_not_implemented)

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
