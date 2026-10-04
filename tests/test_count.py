"""Tests for counts.parquet upserts and the `lsa count` CLI (task 3)."""

from __future__ import annotations

import sys
from pathlib import Path

import pyarrow.parquet as pq
import pytest

from lsa import count as cnt
from lsa.cli import main
from lsa.contracts import CountRecord
from tests.sources.test_hn import TERMS, make_comments_parquet

FIXTURE_TERMS_CSV = (
    Path(__file__).resolve().parent / "fixtures" / "search_terms.csv"
)


def _record(**over):
    kw = {
        "source": "hn-snapshot",
        "family": "hn",
        "region": "US",
        "category": "core-banking",
        "system": "",
        "query": "cobol",
        "count": 1,
        "method": "local snapshot regex",
        "counted_at": "2026-10-05T00:00:00Z",
    }
    kw.update(over)
    return CountRecord(**kw)


def test_append_counts_creates_file(tmp_path):
    out = tmp_path / "derived" / "counts.parquet"
    cnt.append_counts([_record()], out)
    rows = pq.read_table(out).to_pylist()
    assert len(rows) == 1
    assert rows[0]["count"] == 1


def test_append_counts_upsert_replaces_not_duplicates(tmp_path):
    out = tmp_path / "counts.parquet"
    cnt.append_counts(
        [_record(count=1, counted_at="2026-10-05T00:00:00Z")], out
    )
    cnt.append_counts(
        [_record(count=7, counted_at="2026-10-05T01:00:00Z")], out
    )
    rows = pq.read_table(out).to_pylist()
    assert len(rows) == 1
    assert rows[0]["count"] == 7
    assert rows[0]["counted_at"] == "2026-10-05T01:00:00Z"


def test_append_counts_keeps_rows_with_other_keys(tmp_path):
    out = tmp_path / "counts.parquet"
    cnt.append_counts(
        [_record(category="a", query="qa"), _record(category="b", query="qb")],
        out,
    )
    cnt.append_counts([_record(category="a", query="qa", count=9)], out)
    rows = pq.read_table(out).to_pylist()
    assert len(rows) == 2
    by_cat = {r["category"]: r for r in rows}
    assert by_cat["a"]["count"] == 9
    assert by_cat["b"]["count"] == 1


def test_load_terms_reads_category_term_pairs():
    terms = cnt.load_terms(FIXTURE_TERMS_CSV)
    assert terms == TERMS


def test_format_table_lists_counts(tmp_path):
    out = cnt.format_table([_record(count=5), _record(category="_any", count=9)])
    assert "core-banking" in out
    assert "_any" in out


def test_cli_count_hn_writes_counts_and_prints_proxy(
    tmp_path, monkeypatch, capsys
):
    snap = make_comments_parquet(tmp_path / "comments.parquet")
    out = tmp_path / "counts.parquet"
    monkeypatch.setenv("LSA_HN_SNAPSHOT", str(snap))
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "lsa",
            "count",
            "--family",
            "hn",
            "--terms",
            str(FIXTURE_TERMS_CSV),
            "--counts",
            str(out),
        ],
    )
    main()
    printed = capsys.readouterr().out
    assert "core-banking" in printed
    assert "token proxy" in printed
    rows = pq.read_table(out).to_pylist()
    assert len(rows) == 3
    by_cat = {r["category"]: r for r in rows}
    assert by_cat["core-banking"]["count"] == 3
    assert by_cat["erp"]["count"] == 2
    assert by_cat["_any"]["count"] == 4

    # A rerun upserts rather than duplicating rows.
    main()
    assert len(pq.read_table(out).to_pylist()) == 3


def test_cli_count_unknown_family_exits(tmp_path, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "lsa",
            "count",
            "--family",
            "jobs",
            "--terms",
            str(FIXTURE_TERMS_CSV),
        ],
    )
    with pytest.raises(SystemExit):
        main()
