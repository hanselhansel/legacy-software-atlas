"""hn fetcher: matched snapshot comments become items, no network."""

from __future__ import annotations

import pyarrow as pa
import pyarrow.parquet as pq

from lsa.contracts import CountRecord
from lsa.fetch import hn as fetch_hn


def _snapshot(path):
    rows = [
        (9_000_000_001, "still running cobol on the mainframe", True, True),
        (9_000_000_002, "the sapling grew quickly", True, True),
        (9_000_000_003, "SAP runs our ledger", True, True),
        (9_000_000_004, "cobol but not eligible", False, True),
        (9_000_000_005, "cobol outside the window", True, False),
    ]
    table = pa.table(
        {
            "id": [r[0] for r in rows],
            "story_id": [9_000_000_100 for _ in rows],
            "created_at": ["2026-01-01T00:00:00Z" for _ in rows],
            "text_norm": [r[1] for r in rows],
            "word_count": [10 for _ in rows],
            "eligible": [r[2] for r in rows],
            "in_window": [r[3] for r in rows],
        }
    )
    pq.write_table(table, path)
    return path


def _record(
    category="mainframe-cobol",
    query="cobol | as/400",
    method="local snapshot regex",
):
    return CountRecord(
        source="hn-snapshot",
        family="hn",
        region="US",
        category=category,
        system="",
        query=query,
        count=3,
        method=method,
        counted_at="T",
    )


def test_plan_rows_skips_any_summary_row():
    rows = [_record(), _record(category="_any"), _record(method="http-500")]
    planned = fetch_hn.plan_rows(rows)
    assert [r.category for r in planned] == ["mainframe-cobol"]


def test_fetch_reads_matching_comments(tmp_path):
    snap = _snapshot(tmp_path / "comments.parquet")
    produced = list(
        fetch_hn.fetch([_record()], client=None, snapshot=snap, log=None)
    )
    ids = {p.item.source_id for p in produced}
    # cobol matches 001; 002 (sapling) is excluded by the term boundaries;
    # 003 SAP matches the "as/400"? no - the query is cobol | as/400, so SAP
    # alone must not match. 004/005 are ineligible or out of window.
    assert ids == {"9000000001"}
    item = produced[0].item
    assert item.url == "https://news.ycombinator.com/item?id=9000000001"
    assert "cobol" in item.text
    assert produced[0].source == "hn-snapshot"
    assert produced[0].region == "US"
    assert produced[0].category_hint == "mainframe-cobol"


def test_fetch_prefers_text_column_when_present(tmp_path):
    """Snapshots with a raw ``text`` column use it over ``text_norm``."""
    path = tmp_path / "comments.parquet"
    pq.write_table(
        pa.table(
            {
                "id": [1],
                "story_id": [2],
                "created_at": ["2026-01-01T00:00:00Z"],
                "text": ["We still run COBOL at the bank."],
                "text_norm": ["we still run cobol at the bank."],
                "word_count": [8],
                "eligible": [True],
                "in_window": [True],
            }
        ),
        path,
    )
    produced = list(
        fetch_hn.fetch([_record()], client=None, snapshot=path, log=None)
    )
    assert produced[0].item.text == "We still run COBOL at the bank."
