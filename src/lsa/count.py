"""Counts parquet writer, term loading, and API count runs (plan 1, task 3).

``append_counts`` upserts CountRecord rows on (source, region, category,
query): rerunning a count replaces the previous row for the same key instead
of duplicating it, so a count run stays idempotent.

``run_api_counts`` drives the keyless API collectors: for each
``category, region, query, lang`` row it calls every source module whose
``REGIONS`` contains the row's region, turns the result into a CountRecord
(``method`` is ``"<source> api total"``), and skips-and-logs any source that
raises after its own retries, so one bad source never crashes the run.
"""

from __future__ import annotations

import csv
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING

from lsa import paths
from lsa.contracts import REGIONS, CountRecord

if TYPE_CHECKING:
    from collections.abc import Callable

    import httpx

UPSERT_KEY = ("source", "region", "category", "query")

API_SOURCES: dict[str, tuple[ModuleType, ...]] = {}


@dataclass(frozen=True)
class QueryRow:
    """One row of a ``category,region,query,lang`` count-queries CSV."""

    category: str
    region: str
    query: str
    lang: str


def api_sources(family: str) -> tuple[ModuleType, ...]:
    """Counter modules for a family, lazily imported on first use.

    Populates the module-level ``API_SOURCES`` dict; tests replace the dict
    directly, so a non-empty value is returned untouched.
    """
    if not API_SOURCES:
        from lsa.sources import (
            arbeitsagentur,
            boamp,
            contracts_finder,
            eures,
            gebiz,
            kalibrr,
            mycareersfuture,
            ted,
            usaspending,
        )

        API_SOURCES.update(
            {
                "procurement": (
                    usaspending,
                    ted,
                    contracts_finder,
                    gebiz,
                    boamp,
                ),
                "jobs": (
                    mycareersfuture,
                    kalibrr,
                    eures,
                    arbeitsagentur,
                ),
            }
        )
    return API_SOURCES[family]


def load_queries(path: Path) -> list[QueryRow]:
    """``QueryRow`` list from a ``category,region,query,lang`` CSV."""
    with open(path, newline="", encoding="utf-8") as f:
        return [
            QueryRow(row["category"], row["region"], row["query"], row["lang"])
            for row in csv.DictReader(f)
        ]


def planned_calls(
    queries: list[QueryRow], family: str
) -> list[tuple[QueryRow, ModuleType]]:
    """(row, source) pairs a run would make: valid regions, source covers it."""
    return [
        (row, mod)
        for row in queries
        if row.region in REGIONS
        for mod in api_sources(family)
        if row.region in mod.REGIONS
    ]


def run_api_counts(
    queries: list[QueryRow],
    family: str,
    client: httpx.Client,
    log: Callable[[str], None] = print,
) -> list[CountRecord]:
    """Count every planned (row, source) pair into CountRecords.

    A row whose region is not a known code, or a source that raises, is
    logged and skipped; the run never stops.
    """
    counted_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    records = []
    for row in queries:
        if row.region not in REGIONS:
            log(f"skip {row.region} {row.query!r}: unknown region code")
            continue
        for mod in api_sources(family):
            if row.region not in mod.REGIONS:
                continue
            try:
                total = mod.count(row.query, row.region, client)
            except Exception as exc:  # noqa: BLE001 - any source error skips, never crashes
                log(f"skip {mod.SOURCE} {row.region} {row.query!r}: {exc}")
                continue
            records.append(
                CountRecord(
                    source=mod.SOURCE,
                    family=mod.FAMILY,
                    region=row.region,
                    category=row.category,
                    system="",
                    query=row.query,
                    count=total,
                    method=f"{mod.SOURCE} api total",
                    counted_at=counted_at,
                )
            )
    return records


def _schema():
    import pyarrow as pa

    return pa.schema(
        [
            ("source", pa.string()),
            ("family", pa.string()),
            ("region", pa.string()),
            ("category", pa.string()),
            ("system", pa.string()),
            ("query", pa.string()),
            ("count", pa.int64()),
            ("method", pa.string()),
            ("counted_at", pa.string()),
        ]
    )


def load_terms(path: Path) -> list[tuple[str, str]]:
    """``(category, term)`` pairs from a ``category,region,term`` CSV."""
    with open(path, newline="", encoding="utf-8") as f:
        return [(row["category"], row["term"]) for row in csv.DictReader(f)]


def append_counts(
    records: list[CountRecord], path: Path | None = None
) -> Path:
    """Upsert records into the counts parquet; returns the path written."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    path = Path(path) if path is not None else paths.DERIVED / "counts.parquet"
    fresh = {tuple(getattr(r, k) for k in UPSERT_KEY) for r in records}
    rows = []
    if path.exists():
        rows = [
            row
            for row in pq.read_table(path).to_pylist()
            if tuple(row[k] for k in UPSERT_KEY) not in fresh
        ]
    rows.extend(asdict(r) for r in records)
    path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(pa.Table.from_pylist(rows, schema=_schema()), path)
    return path


def format_table(records: list[CountRecord]) -> str:
    """One line per record: category, count, query."""
    lines = [f"{'category':<20}{'count':>8}  query"]
    for r in records:
        count = "-" if r.count is None else str(r.count)
        lines.append(f"{r.category:<20}{count:>8}  {r.query}")
    return "\n".join(lines)
