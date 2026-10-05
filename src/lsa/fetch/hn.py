"""hn fetcher: matched snapshot comments become items (no network).

Each counted row's ``query`` is the category's terms joined by ``" | "``;
``fetch`` rebuilds the same regex the counter used and streams matching
comments out of the local parquet with duckdb. The item's text is the
comment's ``text`` column when the snapshot has one, else ``text_norm``.
The ``_any`` summary row covers the same union of comments, so
``plan_rows`` drops it rather than fetching everything twice.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from pathlib import Path

from lsa.contracts import CountRecord, SourceItem
from lsa.fetch import common
from lsa.sources import hn

_ITEM_URL = "https://news.ycombinator.com/item?id="


def plan_rows(rows: list[CountRecord]) -> list[CountRecord]:
    return [
        r
        for r in rows
        if r.method == hn.METHOD and r.category != "_any" and r.query.strip()
    ]


def _text_column(con, comments_sql: str) -> str:
    cols = {
        row[0]
        for row in con.execute(
            f"DESCRIBE SELECT * FROM {comments_sql}"
        ).fetchall()
    }
    return "text" if "text" in cols else "text_norm"


def fetch(
    rows: list[CountRecord],
    client=None,
    *,
    snapshot: Path | None = None,
    log: Callable[[str], None] | None = print,
    **_unused,
) -> Iterator[common.Produced]:
    """``client`` is unused: the HN source is a local parquet snapshot."""
    import duckdb

    log = log or (lambda _m: None)
    path = Path(snapshot) if snapshot is not None else hn.snapshot_path()
    comments = hn._comments_sql(path)
    con = duckdb.connect()
    try:
        col = _text_column(con, comments)
        for row in rows:
            terms = [t.strip() for t in row.query.split(" | ") if t.strip()]
            if not terms:
                continue
            try:
                result = con.execute(
                    f"SELECT id, {col} FROM {comments} "
                    f"WHERE {hn._ELIGIBLE} AND regexp_matches(text_norm, ?)",
                    [hn._pattern(terms)],
                )
            except Exception as exc:  # noqa: BLE001 - a bad row never stops
                log(f"fetch hn {row.category}: {exc}")
                continue
            for cid, body in result.fetchall():
                yield common.Produced(
                    SourceItem(
                        str(cid), f"{_ITEM_URL}{cid}", str(body or "")
                    ),
                    hn.SOURCE,
                    row.region,
                    row.category,
                    row.query,
                )
    finally:
        con.close()
    log(f"fetch hn: done ({path.name})")
