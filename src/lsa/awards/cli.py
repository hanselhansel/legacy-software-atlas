"""`lsa awards` command registration (plan 3, lane L).

``lsa awards --queries research/award_queries.csv [--per-query N]
[--limit N] [--dry-run]`` collects public contract awards from the six
regional sources, dedupes on ``award_id``, and writes
``data/derived/awards.parquet`` plus ``data/raw/awards/*.json`` and
``items.parquet`` rows under family ``awards``.
"""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

from lsa import paths


def _stamp() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _awards(args: argparse.Namespace) -> None:
    from lsa.awards import collect
    from lsa.awards import common as aw

    if not args.queries.exists():
        raise SystemExit(f"queries csv not found: {args.queries}")
    if args.per_query < 1:
        raise SystemExit("--per-query must be a positive integer")
    rows = aw.load_queries(args.queries)
    if args.dry_run:
        planned = collect.plan(rows)
        for row, mods in planned:
            sources = (
                ",".join(s for m in mods for s in m.SOURCES)
                if mods
                else "(no source)"
            )
            print(
                f"{sources:<32} {row.region}  "
                f"{row.category:<20} {row.query}"
            )
        print(
            f"dry run: {len(rows)} queries, "
            f"{sum(1 for _, m in planned if m)} routed, nothing written"
        )
        return
    from lsa.sources import http

    fx_path = paths.ROOT / "configs" / "fx.toml"
    _as_of, rates = aw.load_fx(fx_path)
    with http.make_client() as client:
        collect.run(
            rows,
            client,
            per_query=args.per_query,
            limit=args.limit,
            awards_path=args.awards or paths.DERIVED / "awards.parquet",
            items_path=args.items or paths.DERIVED / "items.parquet",
            raw_dir=paths.RAW / "awards",
            rates=rates,
            fetched_at=_stamp(),
            log=print,
        )


def register(sub: argparse._SubParsersAction) -> None:
    """Attach the ``awards`` subcommand, same pattern as ``jev.cli``."""
    p = sub.add_parser(
        "awards",
        help="collect public contract awards into awards.parquet + items",
    )
    p.add_argument(
        "--queries",
        type=Path,
        default=paths.RESEARCH / "award_queries.csv",
        help="category,region,query csv of award searches",
    )
    p.add_argument(
        "--per-query",
        type=int,
        default=200,
        help="keep at most N awards per query (default: %(default)s)",
    )
    p.add_argument(
        "--limit",
        type=int,
        default=None,
        help="cap kept awards to N (smoke runs; stops collecting early)",
    )
    p.add_argument(
        "--awards",
        type=Path,
        default=None,
        help="awards parquet to upsert (default: data/derived/awards.parquet)",
    )
    p.add_argument(
        "--items",
        type=Path,
        default=None,
        help="items parquet to upsert (default: data/derived/items.parquet)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="print the query-to-source routing; no collect, no writes",
    )
    p.set_defaults(func=_awards)
