"""Award collection driver (plan 3, lane L).

``plan`` shows the dry-run routing: each query row and the collector
modules whose ``REGIONS`` cover it. ``run`` streams rows through the
collectors over one shared client, dedupes on ``award_id`` (an award
surfacing under two queries or endpoints is kept once), applies the
total ``limit`` and hands the kept rows to ``write_awards`` /
``write_items``.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from pathlib import Path
from types import ModuleType

import httpx

from lsa import awards
from lsa.awards.common import (
    AwardRow,
    QueryRow,
    write_awards,
    write_items,
)


def plan(
    rows: list[QueryRow],
    collectors: tuple[ModuleType, ...] | None = None,
) -> list[tuple[QueryRow, list[ModuleType]]]:
    """Each query row with the modules that collect its region."""
    modules = collectors if collectors is not None else awards.collectors()
    return [
        (row, [m for m in modules if row.region in m.REGIONS])
        for row in rows
    ]


def _stream(
    rows: list[QueryRow],
    client: httpx.Client,
    *,
    per_query: int | None,
    log: Callable[[str], None],
    collectors: tuple[ModuleType, ...],
) -> Iterator[AwardRow]:
    for mod in collectors:
        own = [r for r in rows if r.region in mod.REGIONS]
        if own:
            yield from mod.collect(
                own, client, per_query=per_query, log=log
            )


def run(
    rows: list[QueryRow],
    client: httpx.Client,
    *,
    per_query: int | None,
    limit: int | None,
    awards_path: Path,
    items_path: Path,
    raw_dir: Path,
    rates: dict[str, float],
    fetched_at: str,
    log: Callable[[str], None] | None = print,
    collectors: tuple[ModuleType, ...] | None = None,
) -> list[AwardRow]:
    """Collect, dedupe and persist; returns the kept award rows."""
    log = log or (lambda _m: None)
    modules = collectors if collectors is not None else awards.collectors()
    seen: set[str] = set()
    kept: list[AwardRow] = []
    for row in _stream(
        rows,
        client,
        per_query=per_query,
        log=log,
        collectors=modules,
    ):
        if row.award_id in seen:
            continue
        seen.add(row.award_id)
        kept.append(row)
        if limit is not None and len(kept) >= limit:
            break
    write_awards(kept, awards_path, rates=rates)
    items = write_items(kept, raw_dir, items_path, fetched_at=fetched_at)
    log(
        f"awards: kept {len(kept)} rows, wrote {awards_path} "
        f"and {len(items)} items"
    )
    return kept
