"""Shared plumbing for the award collectors (plan 3, lane L).

``QueryRow`` is one ``category,region,query`` row of
``research/award_queries.csv``. ``AwardRow`` is one collected award as the
source emitted it: raw fields only. ``write_awards`` derives the parquet
columns — ``text_window`` (first ``MAX_WINDOW_WORDS`` words of ``text``),
``value_usd`` (``value`` converted at the dated ``configs/fx.toml`` rates)
and ``duration_months`` (source-given, else computed from start/end) —
and upserts on ``award_id`` so a rerun replaces rather than duplicates,
mirroring ``count.append_counts``.

``write_items`` writes each kept award's ``text_window`` to
``data/raw/awards/<safe_name>.json`` under key ``text`` and upserts an
``items.parquet`` row with family ``awards`` so the Jev runner can label
it (see ``src/lsa/jev/items.py``). Rows with an empty window have nothing
to label and are skipped on the items side only.
"""

from __future__ import annotations

import csv
import hashlib
import json
import tomllib
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, replace
from datetime import date
from pathlib import Path

from lsa.fetch import common as fcommon

MAX_WINDOW_WORDS = 120

PROCEDURES = (
    "open",
    "restricted",
    "negotiated_no_competition",
    "direct",
    "other",
    "unknown",
)

# OCDS tender.procurementMethod -> study procedure. Shared by the two UK
# endpoints and AusTender, all OCDS publishers.
_OCDS_PROCEDURE = {
    "open": "open",
    "selective": "restricted",
    "limited": "negotiated_no_competition",
    "direct": "direct",
}


@dataclass(frozen=True)
class QueryRow:
    """One ``category,region,query`` award-queries CSV row."""

    category: str
    region: str
    query: str


@dataclass(frozen=True)
class AwardRow:
    """One collected award, as the source emitted it.

    ``award_id`` is ``"<source>:<native id>"`` so it is unique across
    sources. ``text`` is the full description before windowing; ``value``
    is in ``currency``; ``duration_months`` is only set when the source
    states a duration directly (otherwise the writer derives it from the
    dates). Dates are ISO ``YYYY-MM-DD`` strings or "".
    """

    award_id: str
    source: str
    region: str
    category_hint: str
    query: str
    buyer: str
    title: str
    text: str
    value: float | None
    currency: str
    start_date: str
    end_date: str
    duration_months: float | None
    procedure: str
    cpv_or_psc: str
    url: str


def load_queries(path: Path) -> list[QueryRow]:
    """``QueryRow`` list from a ``category,region,query`` CSV."""
    with open(path, newline="", encoding="utf-8") as f:
        return [
            QueryRow(row["category"], row["region"], row["query"])
            for row in csv.DictReader(f)
        ]


def load_fx(path: Path) -> tuple[str, dict[str, float]]:
    """``(as_of, rates)`` from the dated fx.toml."""
    data = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    rates = {k.upper(): float(v) for k, v in (data.get("rates") or {}).items()}
    return str(data.get("as_of", "")), rates


def to_usd(
    amount: float | None, currency: str, rates: dict[str, float]
) -> float | None:
    """``amount`` in ``currency`` at the fixed rate, or None when unknown."""
    if amount is None:
        return None
    rate = rates.get((currency or "").upper())
    return amount * rate if rate is not None else None


def _parse_date(value: str) -> date | None:
    """Best-effort ISO date parse: YYYY-MM-DD or the date part of a datetime."""
    text = (value or "").strip()[:10]
    if len(text) < 10:
        return None
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def months_between(start: str, end: str) -> float | None:
    """Calendar months from ``start`` to ``end``, None on missing/reversed."""
    s, e = _parse_date(start), _parse_date(end)
    if s is None or e is None or e < s:
        return None
    months = (e.year - s.year) * 12 + (e.month - s.month)
    return round(months + (e.day - s.day) / 30.4375, 1)


def window(text: str, max_words: int = MAX_WINDOW_WORDS) -> str:
    """The text cut to at most ``max_words`` whitespace-separated words."""
    return " ".join((text or "").split()[:max_words])


def ocds_procedure(method: str | None) -> str:
    """OCDS procurementMethod code -> study procedure label."""
    if method is None:
        return "unknown"
    return _OCDS_PROCEDURE.get(method, "other")


def finalize(row: AwardRow, rates: dict[str, float]) -> dict:
    """The awards.parquet dict for one row: derived columns computed."""
    return {
        "award_id": row.award_id,
        "source": row.source,
        "region": row.region,
        "category_hint": row.category_hint,
        "query": row.query,
        "buyer": row.buyer,
        "title": row.title,
        "text_window": window(row.text),
        "value_usd": to_usd(row.value, row.currency, rates),
        "start_date": row.start_date,
        "end_date": row.end_date,
        "duration_months": (
            row.duration_months
            if row.duration_months is not None
            else months_between(row.start_date, row.end_date)
        ),
        "procedure": (
            row.procedure if row.procedure in PROCEDURES else "unknown"
        ),
        "cpv_or_psc": row.cpv_or_psc,
        "url": row.url,
    }


def _schema():
    import pyarrow as pa

    return pa.schema(
        [
            ("award_id", pa.string()),
            ("source", pa.string()),
            ("region", pa.string()),
            ("category_hint", pa.string()),
            ("query", pa.string()),
            ("buyer", pa.string()),
            ("title", pa.string()),
            ("text_window", pa.string()),
            ("value_usd", pa.float64()),
            ("start_date", pa.string()),
            ("end_date", pa.string()),
            ("duration_months", pa.float64()),
            ("procedure", pa.string()),
            ("cpv_or_psc", pa.string()),
            ("url", pa.string()),
        ]
    )


def write_awards(
    rows: Iterable[AwardRow],
    path: Path,
    *,
    rates: dict[str, float],
) -> Path:
    """Upsert finalized rows into awards.parquet on ``award_id``."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    fresh: dict[str, dict] = {}
    for row in rows:
        fresh.setdefault(row.award_id, finalize(row, rates))
    existing = []
    if path.exists():
        existing = [
            r
            for r in pq.read_table(path).to_pylist()
            if r["award_id"] not in fresh
        ]
    existing.extend(fresh.values())
    path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(pa.Table.from_pylist(existing, schema=_schema()), path)
    return path


def write_items(
    rows: Iterable[AwardRow],
    raw_dir: Path,
    items_path: Path,
    *,
    fetched_at: str,
) -> list[fcommon.ItemRow]:
    """Raw text_window JSON per row plus items.parquet rows (family awards).

    Rows with an empty text window are skipped: there is nothing for Jev
    to label.
    """
    kept: Counter[tuple[str, ...]] = Counter()
    pending = []
    for row in rows:
        text = window(row.text)
        if not text:
            continue
        iid = row.award_id
        raw_dir.mkdir(parents=True, exist_ok=True)
        (raw_dir / f"{fcommon.safe_name(iid)}.json").write_text(
            json.dumps(
                {
                    "item_id": iid,
                    "source": row.source,
                    "url": row.url,
                    "query": row.query,
                    "fetched_at": fetched_at,
                    "text": text,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        key = (row.source, row.region, row.category_hint, row.query)
        kept[key] += 1
        pending.append(
            (
                key,
                fcommon.ItemRow(
                    item_id=iid,
                    family="awards",
                    source=row.source,
                    region=row.region,
                    category_hint=row.category_hint,
                    url=row.url,
                    fetched_at=fetched_at,
                    text_sha256=hashlib.sha256(text.encode()).hexdigest(),
                    query_count=None,
                ),
            )
        )
    item_rows = [replace(item, sampled=kept[key]) for key, item in pending]
    if item_rows:
        fcommon.append_items(item_rows, items_path)
    return item_rows
