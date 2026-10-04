"""Tests for the HN snapshot counter (plan 1, task 3, lane C).

Synthetic fixture comments only; ids start at 9,000,000,000. No real HN text
or usernames ever enter the repo.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from lsa.sources import hn

FIXTURE_TERMS_CSV = (
    Path(__file__).resolve().parents[1] / "fixtures" / "search_terms.csv"
)

TERMS = [
    ("core-banking", "cobol"),
    ("core-banking", "as/400"),
    ("erp", "sap"),
]


def make_comments_parquet(path: Path) -> Path:
    """Tiny synthetic comment snapshot with the columns the counter reads."""
    rows = [
        # (id, text_norm, word_count, eligible, in_window)
        (9_000_000_001, "still running cobol on the mainframe", 10, True, True),
        (9_000_000_002, "we still operate an AS/400 box", 20, True, True),
        (9_000_000_003, "the sapling grew quickly", 5, True, True),
        (9_000_000_004, "SAP runs our ledger", 30, True, True),
        (9_000_000_005, "COBOL and SAP both linger here", 40, True, True),
        (9_000_000_006, "cobol but not eligible", 10, False, True),
        (9_000_000_007, "cobol outside the window", 10, True, False),
        (9_000_000_008, "python and django chat", 10, True, True),
    ]
    table = pa.table(
        {
            "id": [r[0] for r in rows],
            "story_id": [9_000_000_100 for _ in rows],
            "created_at": ["2026-01-01T00:00:00Z" for _ in rows],
            "text_norm": [r[1] for r in rows],
            "word_count": [r[2] for r in rows],
            "eligible": [r[3] for r in rows],
            "in_window": [r[4] for r in rows],
        }
    )
    pq.write_table(table, path)
    return path


def _by_category(records):
    return {r.category: r for r in records}


def test_count_terms_one_record_per_category(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    records = hn.count_terms(snap, TERMS)
    by_cat = _by_category(records)
    # core-banking: ids 1 (cobol), 2 (as/400), 5 (both terms across categories)
    assert by_cat["core-banking"].count == 3
    # erp: ids 4 and 5; id 3 "sapling" must not match "sap"
    assert by_cat["erp"].count == 2


def test_word_boundary_blocks_substring_match(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    record = hn.count_terms(snap, [("erp", "sap")])[0]
    assert record.count == 2


def test_match_is_case_insensitive(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    upper = hn.count_terms(snap, [("c", "COBOL")])[0].count
    lower = hn.count_terms(snap, [("c", "cobol")])[0].count
    # ids 1 and 5 in any case; 6 and 7 excluded by flags
    assert upper == lower == 2


def test_comment_matching_two_terms_counts_once(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    # id 5 holds both cobol and sap; one category holding both terms still
    # counts the comment a single time.
    record = hn.count_terms(snap, [("c", "cobol"), ("c", "sap")])[0]
    assert record.count == 3


def test_ineligible_and_out_of_window_excluded(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    record = hn.count_terms(snap, [("c", "cobol")])[0]
    assert record.count == 2


def test_any_row_counts_distinct_across_all_terms(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    records = hn.count_terms(snap, TERMS)
    any_rec = records[-1]
    assert any_rec.category == "_any"
    # ids 1, 2, 4, 5 across every term; id 5 counted once
    assert any_rec.count == 4


def test_record_fields(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    records = hn.count_terms(snap, TERMS)
    first, last = records[0], records[-1]
    assert first.source == "hn-snapshot"
    assert first.family == "hn"
    assert first.region == "US"
    assert first.system == ""
    assert first.query == "cobol | as/400"
    assert first.method == "local snapshot regex"
    assert last.query == "cobol | as/400 | sap"
    parsed = datetime.strptime(first.counted_at, "%Y-%m-%dT%H:%M:%S%z")
    assert parsed.utcoffset() == timedelta(0)


def test_empty_terms_rejected(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    with pytest.raises(ValueError):
        hn.count_terms(snap, [])


def test_snapshot_path_env_override(tmp_path, monkeypatch):
    monkeypatch.setenv("LSA_HN_SNAPSHOT", str(tmp_path / "x.parquet"))
    assert hn.snapshot_path() == tmp_path / "x.parquet"


def test_snapshot_path_default_expands(monkeypatch):
    monkeypatch.delenv("LSA_HN_SNAPSHOT", raising=False)
    path = hn.snapshot_path()
    assert "~" not in str(path)
    assert path.name == "comments.parquet"
    assert "jev-opportunity-atlas" in str(path)


def test_sample_token_lengths_mean(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    # matching ids 1, 2, 4, 5 with word_count 10, 20, 30, 40: mean 25 * 1.33
    assert hn.sample_token_lengths(snap, TERMS) == pytest.approx(33.25)


def test_sample_token_lengths_seeded(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    a = hn.sample_token_lengths(snap, TERMS, n=2, seed=0)
    b = hn.sample_token_lengths(snap, TERMS, n=2, seed=0)
    assert a == b
    pairs = {10, 20, 30, 40}
    means = {(x + y) / 2 * 1.33 for x in pairs for y in pairs if x < y}
    assert any(a == pytest.approx(m) for m in means)


def test_sample_token_lengths_no_matches(tmp_path):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    assert hn.sample_token_lengths(snap, [("c", "zzzznothing")]) == 0.0
