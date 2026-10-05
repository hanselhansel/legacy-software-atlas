"""``lsa apps`` (plan 3, lane M): app ratings plus review windows.

Reads ``--apps`` (default research/apps.csv), writes one apps.parquet
row per app x storefront, and streams each app's recent reviews through
the shared ``collect_items`` plumbing into ``data/raw/app_reviews/`` and
``items.parquet`` (family ``app_reviews``). ``--dry-run`` prints the
rows without fetching or writing; ``--limit`` caps input rows for smoke
runs. ``--sort`` selects the feed ordering: the lane's documented
``mostrecent`` currently returns empty feeds (see ``lsa.apps.itunes``),
so ``mosthelpful`` is the working fallback.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import httpx

from lsa import paths
from lsa.apps import collect, itunes
from lsa.fetch import common


def _stamp() -> str:
    from datetime import UTC, datetime

    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _run(args: argparse.Namespace, rows: list, client: httpx.Client) -> None:
    stamp = _stamp()
    records: list[collect.AppRecord] = []

    def _produced():
        for event in collect.iter_collection(
            rows, client, sort=args.sort, collected_at=stamp, log=print
        ):
            if isinstance(event, collect.AppRecord):
                records.append(event)
            else:
                yield event

    raw_dir = args.raw_dir or paths.RAW / collect.FAMILY
    item_rows = common.collect_items(
        collect.FAMILY,
        _produced(),
        raw_dir=raw_dir,
        max_words=_window_words(args),
        fetched_at=stamp,
    )
    for r in records:
        rating = "-" if r.rating is None else f"{r.rating:.2f}"
        count = "-" if r.rating_count is None else str(r.rating_count)
        print(
            f"{r.app_name:<30} {r.country}  rating={rating:<6} "
            f"count={count:<9} status={r.status}"
        )
    out = collect.append_apps(records, args.out)
    print(f"wrote {len(records)} app rows to {out}")
    items_path = args.items or paths.DERIVED / "items.parquet"
    if item_rows:
        out = common.append_items(item_rows, items_path)
        print(f"wrote {len(item_rows)} items to {out}")
    else:
        print("no items; items parquet unchanged")


def _window_words(args: argparse.Namespace) -> int:
    """The lane's 80-word review window, or passes.toml when a pass
    config for ``app_reviews`` is supplied."""
    if args.passes is None:
        return itunes.TEXT_WINDOW_WORDS
    return common.window_words(args.passes, collect.FAMILY)


def _apps(args: argparse.Namespace, client: httpx.Client | None = None) -> None:
    if not args.apps.exists():
        raise SystemExit(f"apps csv not found: {args.apps}")
    rows = collect.load_apps(args.apps)
    if args.limit:
        rows = rows[: args.limit]
    if args.dry_run:
        for r in rows:
            print(
                f"{r.category:<24} {r.region}  {r.app_name:<30} "
                f"{r.country}  {r.apple_id}"
            )
        print(f"dry run: {len(rows)} app rows, nothing written")
        return
    if client is not None:
        _run(args, rows, client)
        return
    from lsa.sources import http

    with http.make_client() as real_client:
        _run(args, rows, real_client)


def register(sub) -> None:
    p_apps = sub.add_parser(
        "apps",
        help="app store ratings and review windows (plan 3, lane M)",
    )
    p_apps.add_argument(
        "--apps",
        type=Path,
        default=paths.RESEARCH / "apps.csv",
        help="category,region,app_name,country,apple_id csv",
    )
    p_apps.add_argument(
        "--sort",
        default="mostrecent",
        choices=list(itunes.SORTS),
        help=(
            "feed ordering; mostrecent is the lane contract but currently "
            "returns empty feeds, mosthelpful is the working fallback"
        ),
    )
    p_apps.add_argument(
        "--limit",
        type=int,
        default=None,
        help="cap app rows to the first N (smoke runs)",
    )
    p_apps.add_argument(
        "--dry-run",
        action="store_true",
        help="print planned app rows; no fetch, no writes",
    )
    p_apps.add_argument(
        "--out",
        type=Path,
        default=None,
        help="apps parquet to upsert (default: data/derived/apps.parquet)",
    )
    p_apps.add_argument(
        "--items",
        type=Path,
        default=None,
        help="items parquet to upsert (default: data/derived/items.parquet)",
    )
    p_apps.add_argument(
        "--raw-dir",
        type=Path,
        default=None,
        help="raw item dir (default: data/raw/app_reviews)",
    )
    p_apps.add_argument(
        "--passes",
        type=Path,
        default=None,
        help=(
            "pass config for the review text window; default keeps the "
            "lane's fixed 80-word window"
        ),
    )
    p_apps.set_defaults(func=_apps)
