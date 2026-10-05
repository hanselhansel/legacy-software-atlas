"""Lane M driver: apps.csv rows to apps.parquet plus app_reviews items.

``load_apps`` reads the research CSV (``category, region, app_name,
country, apple_id``; ``country`` is the storefront code). For each row,
``iter_collection`` yields one ``AppRecord`` (the apps.parquet row:
lookup facts plus a ``status`` of "ok", "missing", "robots-denied" or
"error") followed by one ``common.Produced`` per kept review. Only
reviews dated inside the last ``REVIEW_MONTHS`` months reach the item
stream, per the lane contract; the item's text is ``title (rating/5)
body`` and ``collect_items`` cuts it to the 80-word window.

``append_apps`` upserts on (apple_id, country): apps.parquet holds one
row per app x storefront, so a rerun replaces rather than duplicates.
"""

from __future__ import annotations

import csv
from collections.abc import Callable, Iterator
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path

import httpx

from lsa import paths
from lsa.apps import itunes
from lsa.contracts import REGIONS, SourceItem
from lsa.fetch import common

FAMILY = itunes.FAMILY
REVIEW_MONTHS = 24
_UPSERT_KEY = ("apple_id", "country")
_REQUIRED = ("category", "region", "app_name", "country", "apple_id")


@dataclass(frozen=True)
class AppRow:
    """One ``research/apps.csv`` row."""

    category: str
    region: str
    app_name: str
    country: str
    apple_id: str


@dataclass(frozen=True)
class AppRecord:
    """One ``data/derived/apps.parquet`` row: app x storefront."""

    source: str
    category: str
    region: str
    app_name: str
    country: str
    apple_id: str
    rating: float | None
    rating_count: int | None
    version: str | None
    version_date: str | None
    collected_at: str
    status: str


def load_apps(path: Path) -> list[AppRow]:
    """``AppRow`` list from the apps CSV; blank apple_ids are skipped."""
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in _REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(
                f"{path}: missing columns {missing} (need {_REQUIRED})"
            )
        return [
            AppRow(
                row["category"].strip(),
                row["region"].strip(),
                row["app_name"].strip(),
                row["country"].strip().lower(),
                row["apple_id"].strip(),
            )
            for row in reader
            if (row.get("apple_id") or "").strip()
        ]


def _months_ago(now: datetime, months: int) -> datetime:
    """``now`` shifted back ``months`` calendar months."""
    years, rem = divmod(months, 12)
    year = now.year - years
    month = now.month - rem
    if month <= 0:
        year -= 1
        month += 12
    try:
        return now.replace(year=year, month=month)
    except ValueError:  # e.g. Mar 31 -> Sep 31: clamp to the 28th
        return now.replace(year=year, month=month, day=28)


def _item_text(review: itunes.Review) -> str:
    """Title plus rating plus body; Jev sees the score with the words."""
    stars = f" ({review.rating}/5)" if review.rating is not None else ""
    return f"{review.title}{stars} {review.text}".strip()


def _record_for(
    row: AppRow,
    client: httpx.Client,
    *,
    collected_at: str,
    log: Callable[[str], None],
) -> AppRecord:
    """The apps.parquet row for one app x storefront."""
    base = {
        "source": itunes.SOURCE,
        "category": row.category,
        "region": row.region,
        "app_name": row.app_name,
        "country": row.country,
        "apple_id": row.apple_id,
        "rating": None,
        "rating_count": None,
        "version": None,
        "version_date": None,
        "collected_at": collected_at,
    }
    try:
        info = itunes.lookup(row.apple_id, row.country, client)
    except itunes.RobotsDenied as exc:
        log(f"lookup {row.apple_id} {row.country}: {exc}")
        return AppRecord(**base, status="robots-denied")
    except Exception as exc:  # noqa: BLE001 - a bad row never stops a run
        log(f"lookup {row.apple_id} {row.country}: {exc}")
        return AppRecord(**base, status="error")
    if info is None:
        return AppRecord(**base, status="missing")
    return AppRecord(
        **base
        | {
            "rating": info.rating,
            "rating_count": info.rating_count,
            "version": info.version,
            "version_date": info.version_date,
        },
        status="ok",
    )


def iter_collection(
    rows: list[AppRow],
    client: httpx.Client,
    *,
    sort: str = "mostrecent",
    max_pages: int = itunes.MAX_PAGES,
    now: datetime | None = None,
    collected_at: str | None = None,
    log: Callable[[str], None] | None = print,
) -> Iterator[AppRecord | common.Produced]:
    """Per app row: its AppRecord, then Produced items for fresh reviews.

    A row whose lookup is not "ok" yields only its record; a storefront
    without the app has no reviews to page. Rows with unknown region
    codes are logged and skipped, like ``count.run_api_counts``.
    """
    log = log or (lambda _m: None)
    now = now or datetime.now(UTC)
    cutoff = _months_ago(now, REVIEW_MONTHS)
    collected_at = collected_at or now.strftime("%Y-%m-%dT%H:%M:%SZ")
    for row in rows:
        if row.region not in REGIONS:
            log(f"skip {row.region} {row.app_name!r}: unknown region code")
            continue
        record = _record_for(row, client, collected_at=collected_at, log=log)
        yield record
        if record.status != "ok":
            continue
        try:
            for rev in itunes.reviews(
                row.apple_id,
                row.country,
                client,
                sort=sort,
                max_pages=max_pages,
                cutoff=cutoff,
            ):
                yield common.Produced(
                    SourceItem(rev.review_id, rev.url, _item_text(rev)),
                    itunes.SOURCE,
                    row.region,
                    row.category,
                    row.app_name,
                    query_count=record.rating_count,
                )
        except Exception as exc:  # noqa: BLE001 - skip the row, not the run
            log(f"reviews {row.apple_id} {row.country}: {exc}")


def _schema():
    import pyarrow as pa

    return pa.schema(
        [
            ("source", pa.string()),
            ("category", pa.string()),
            ("region", pa.string()),
            ("app_name", pa.string()),
            ("country", pa.string()),
            ("apple_id", pa.string()),
            ("rating", pa.float64()),
            ("rating_count", pa.int64()),
            ("version", pa.string()),
            ("version_date", pa.string()),
            ("collected_at", pa.string()),
            ("status", pa.string()),
        ]
    )


def append_apps(records: list[AppRecord], path: Path | None = None) -> Path:
    """Upsert AppRecords into apps.parquet; returns the path written."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    path = Path(path) if path is not None else paths.DERIVED / "apps.parquet"
    fresh = {tuple(getattr(r, k) for k in _UPSERT_KEY) for r in records}
    rows = []
    if path.exists():
        rows = [
            row
            for row in pq.read_table(path).to_pylist()
            if tuple(row[k] for k in _UPSERT_KEY) not in fresh
        ]
    rows.extend(asdict(r) for r in records)
    path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(pa.Table.from_pylist(rows, schema=_schema()), path)
    return path
