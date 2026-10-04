"""Counts parquet writer and term loading (plan 1, task 3).

``append_counts`` upserts CountRecord rows on (source, region, category,
query): rerunning a count replaces the previous row for the same key instead
of duplicating it, so a count run stays idempotent.
"""

from __future__ import annotations

import csv
from dataclasses import asdict
from pathlib import Path

from lsa import paths
from lsa.contracts import CountRecord

UPSERT_KEY = ("source", "region", "category", "query")


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
