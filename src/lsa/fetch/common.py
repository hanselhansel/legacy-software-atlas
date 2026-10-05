"""Shared plumbing for the fetchers (plan 2, task 1).

``counted_rows`` reads a counts parquet (written by ``lsa count``) and
returns one family's rows in parquet order. ``fetchable`` is the shared
skip rule the API families use: a row annotated by the sanity guard
(``; rejected by sanity guard``) or dropped at review (``; dropped: ...``)
is never paged again, and neither is an empty (match-all) query.

``collect_items`` dedupes produced items on URL or source id, cuts each
item's text to the family's pass window, writes one JSON per item under
``data/raw/<family>/`` and returns the ``items.parquet`` rows.
``append_items`` upserts on ``item_id`` so a rerun replaces rather than
duplicates, mirroring ``count.append_counts``.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from pathlib import Path

from lsa import estimate as est
from lsa.contracts import CountRecord, SourceItem

# Same words-to-tokens proxy the estimators use (cli.py, hn.py).
WORDS_TO_TOKENS = 1.33
# Passes without a measured tokens_per_item fall back to the estimator's
# stated default (estimate.estimate default_tokens_per_item).
DEFAULT_TOKENS_PER_ITEM = 400

_UPSERT_KEY = ("source", "region", "category", "query")


@dataclass(frozen=True)
class Produced:
    """A source item tied to the counted row that surfaced it."""

    item: SourceItem
    source: str
    region: str
    category_hint: str
    query: str


@dataclass(frozen=True)
class ItemRow:
    """One ``data/derived/items.parquet`` row."""

    item_id: str
    family: str
    source: str
    region: str
    category_hint: str
    url: str
    fetched_at: str
    text_sha256: str


def counted_rows(counts_path: Path, family: str) -> list[CountRecord]:
    """CountRecord rows for ``family`` in parquet order, deduped on the
    count upsert key."""
    seen: set[tuple[str, ...]] = set()
    rows = []
    for rec in est.read_counts(counts_path):
        if rec.family != family:
            continue
        key = tuple(getattr(rec, k) for k in _UPSERT_KEY)
        if key in seen:
            continue
        seen.add(key)
        rows.append(rec)
    return rows


def fetchable(row: CountRecord) -> bool:
    """Shared skip rule: annotated rows (rejected by the sanity guard or
    dropped at review, both carry a ``;`` suffix in ``method``) and empty
    match-all queries are never paged."""
    return bool(row.query.strip()) and ";" not in row.method


def plan_rows(
    rows: list[CountRecord], *, fetchable=fetchable
) -> list[CountRecord]:
    """The counted rows a family will page: fetchable ones, order kept."""
    return [r for r in rows if fetchable(r)]


def window_words(passes_path: Path, family: str) -> int:
    """Words kept per item: the family's largest ``tokens_per_item``
    converted at WORDS_TO_TOKENS, so the raw window covers every pass."""
    tokens = max(
        (
            p.tokens_per_item
            for p in est.load_passes(passes_path)
            if p.family == family and p.tokens_per_item is not None
        ),
        default=None,
    )
    if tokens is None:
        tokens = DEFAULT_TOKENS_PER_ITEM
    return max(1, int(tokens / WORDS_TO_TOKENS))


def window_text(text: str, max_words: int) -> str:
    """The text cut to at most ``max_words`` whitespace-separated words."""
    return " ".join(text.split()[:max_words])


def item_id(source: str, item: SourceItem) -> str:
    """Stable id: ``source:native-id``, or ``source:<url/text hash>`` for
    items with no native id."""
    if item.source_id:
        return f"{source}:{item.source_id}"
    digest = hashlib.sha256(
        f"{item.url}\n{item.text[:200]}".encode()
    ).hexdigest()[:16]
    return f"{source}:{digest}"


def safe_name(item_id: str) -> str:
    """Filesystem-safe file stem for an item id, plus a short hash so two
    ids that slug alike still map to different files."""
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "-", item_id).strip("-")[:110]
    digest = hashlib.sha256(item_id.encode()).hexdigest()[:10]
    return f"{slug}-{digest}"


def collect_items(
    family: str,
    produced: Iterable[Produced],
    *,
    raw_dir: Path,
    max_words: int,
    fetched_at: str,
    limit: int | None = None,
) -> list[ItemRow]:
    """Dedupe, window and write produced items; return the parquet rows.

    Dedupe is on URL or source id (plan 2, task 1): an item already seen
    under another query or page never reaches the raw store or the parquet
    twice. Items with no text after windowing are dropped. ``limit`` caps
    the kept items; because ``produced`` is lazy, hitting the cap stops the
    source's paging mid-flight.
    """
    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    rows = []
    for p in produced:
        if limit is not None and len(rows) >= limit:
            break
        if not p.item.source_id and not p.item.url:
            continue
        iid = item_id(p.source, p.item)
        if iid in seen_ids or (p.item.url and p.item.url in seen_urls):
            continue
        text = window_text(p.item.text, max_words)
        if not text:
            continue
        seen_ids.add(iid)
        if p.item.url:
            seen_urls.add(p.item.url)
        raw_dir.mkdir(parents=True, exist_ok=True)
        (raw_dir / f"{safe_name(iid)}.json").write_text(
            json.dumps(
                {
                    "item_id": iid,
                    "source": p.source,
                    "url": p.item.url,
                    "query": p.query,
                    "fetched_at": fetched_at,
                    "text": text,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        rows.append(
            ItemRow(
                item_id=iid,
                family=family,
                source=p.source,
                region=p.region,
                category_hint=p.category_hint,
                url=p.item.url,
                fetched_at=fetched_at,
                text_sha256=hashlib.sha256(text.encode()).hexdigest(),
            )
        )
    return rows


def _items_schema():
    import pyarrow as pa

    return pa.schema(
        [
            ("item_id", pa.string()),
            ("family", pa.string()),
            ("source", pa.string()),
            ("region", pa.string()),
            ("category_hint", pa.string()),
            ("url", pa.string()),
            ("fetched_at", pa.string()),
            ("text_sha256", pa.string()),
        ]
    )


def append_items(rows: list[ItemRow], path: Path | None = None) -> Path:
    """Upsert ItemRows into the items parquet; returns the path written."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    from lsa import paths

    path = Path(path) if path is not None else paths.DERIVED / "items.parquet"
    fresh = {r.item_id for r in rows}
    existing = []
    if path.exists():
        existing = [
            row
            for row in pq.read_table(path).to_pylist()
            if row["item_id"] not in fresh
        ]
    existing.extend(asdict(r) for r in rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(
        pa.Table.from_pylist(existing, schema=_items_schema()), path
    )
    return path
