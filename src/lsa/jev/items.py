"""Item loading for a Jev pass: items.parquet rows plus raw text windows.

The fetcher lane (plan 2, task 1) writes ``data/derived/items.parquet``
(``item_id, family, source, region, category_hint, url, fetched_at,
text_sha256``) and one ``data/raw/<family>/<item_id>.json`` per item holding
the text window Jev sees. This loader joins the two and yields
``{item_id, text, source, region, category_hint, url}`` dicts. An item whose
raw file is absent or unreadable fails the whole load: silently skipping would
undercover the pass and skew its estimates.
"""

from __future__ import annotations

import json
from pathlib import Path

from lsa import paths
from lsa.fetch.common import safe_name

_TEXT_KEYS = ("text", "text_window", "window")


def _raw_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, str):
        return data
    if isinstance(data, dict):
        for key in _TEXT_KEYS:
            if isinstance(data.get(key), str):
                return data[key]
    raise ValueError(f"{path}: no text field (one of {_TEXT_KEYS})")


def load_items(
    family: str,
    items_path: Path | None = None,
    raw_root: Path | None = None,
) -> list[dict]:
    """All items for a count family, in items.parquet order."""
    import pyarrow.parquet as pq

    ip = Path(items_path) if items_path is not None else paths.DERIVED / "items.parquet"
    rr = Path(raw_root) if raw_root is not None else paths.RAW
    if not ip.exists():
        raise FileNotFoundError(
            f"items parquet not found: {ip} (run the fetchers first)"
        )
    items: list[dict] = []
    missing: list[str] = []
    for row in pq.read_table(ip).to_pylist():
        if row.get("family") != family:
            continue
        item_id = str(row["item_id"])
        try:
            text = _raw_text(rr / family / f"{safe_name(item_id)}.json")
        except FileNotFoundError:
            missing.append(item_id)
            continue
        items.append(
            {
                "item_id": item_id,
                "text": text,
                "source": row.get("source"),
                "region": row.get("region"),
                "category_hint": row.get("category_hint"),
                "url": row.get("url"),
            }
        )
    if missing:
        raise FileNotFoundError(
            f"{len(missing)} of {len(items) + len(missing)} {family} items "
            f"lack raw text under {rr / family} (first: {missing[:5]})"
        )
    return items
