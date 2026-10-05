"""Tests for counts.parquet upserts and the `lsa count` CLI (task 3)."""

from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

import pyarrow.parquet as pq
import pytest

from lsa import count as cnt
from lsa.cli import main
from lsa.contracts import CountRecord
from tests.sources.test_hn import TERMS, make_comments_parquet

FIXTURE_TERMS_CSV = (
    Path(__file__).resolve().parent / "fixtures" / "search_terms.csv"
)
FIXTURE_QUERIES_CSV = (
    Path(__file__).resolve().parent / "fixtures" / "count_queries.csv"
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


def test_format_table_lists_counts():
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
            "pages",
            "--terms",
            str(FIXTURE_TERMS_CSV),
        ],
    )
    with pytest.raises(SystemExit):
        main()


def _stub_source(
    source,
    regions,
    result=None,
    raises=False,
    nonsense=0,
    match_all=10_000,
    probe_raises=False,
):
    """Fake source module: constants plus a ``count`` callable.

    ``count`` returns ``nonsense`` for the sanity-guard nonsense query and
    ``match_all`` for the empty match-all query, so stubbed runs model a
    sane API. ``calls`` records every query the guard or run sent.
    """
    stub = SimpleNamespace(SOURCE=source, FAMILY="procurement", REGIONS=regions)
    calls = []

    def count(query, region, client):
        calls.append(query)
        probes = (cnt.NONSENSE_QUERY, cnt.MATCH_ALL_QUERY)
        if raises or (probe_raises and query in probes):
            raise RuntimeError(f"{source} exploded")
        if query == cnt.NONSENSE_QUERY:
            return nonsense
        if query == cnt.MATCH_ALL_QUERY:
            return match_all
        return result

    stub.count = count
    stub.calls = calls
    return stub


def _queries_csv(tmp_path, rows):
    path = tmp_path / "queries.csv"
    path.write_text(
        "category,region,query,lang\n"
        + "\n".join(",".join(r) for r in rows)
        + "\n"
    )
    return path


def test_load_queries_reads_fixture_rows():
    rows = cnt.load_queries(FIXTURE_QUERIES_CSV)
    for expected in (
        cnt.QueryRow("core-banking", "US", "mainframe", "en"),
        cnt.QueryRow("core-banking", "EU", "core banking", "en"),
        cnt.QueryRow("erp", "SG", "sap", "en"),
    ):
        assert expected in rows


def test_planned_calls_routes_rows_to_region_sources(monkeypatch):
    us = _stub_source("us-src", ("US",))
    eu = _stub_source("eu-src", ("EU",))
    monkeypatch.setattr(
        cnt, "API_SOURCES", {"procurement": (us, eu)}
    )
    queries = [
        cnt.QueryRow("c", "US", "q1", "en"),
        cnt.QueryRow("c", "EU", "q2", "en"),
        cnt.QueryRow("c", "SG", "q3", "en"),
    ]
    calls = cnt.planned_calls(queries, "procurement")
    assert [(row.query, mod.SOURCE) for row, mod in calls] == [
        ("q1", "us-src"),
        ("q2", "eu-src"),
    ]


def test_run_api_counts_builds_records_and_skips_errors(monkeypatch):
    ok = _stub_source("ok-src", ("US",), result=7)
    bad = _stub_source("bad-src", ("US",), raises=True)
    monkeypatch.setattr(
        cnt, "API_SOURCES", {"procurement": (ok, bad)}
    )
    logs: list[str] = []
    records = cnt.run_api_counts(
        [cnt.QueryRow("cat", "US", "q", "en")],
        "procurement",
        client=None,
        log=logs.append,
    )
    assert len(records) == 1
    rec = records[0]
    assert rec.source == "ok-src"
    assert rec.family == "procurement"
    assert rec.region == "US"
    assert rec.category == "cat"
    assert rec.system == ""
    assert rec.query == "q"
    assert rec.count == 7
    assert rec.method == "ok-src api total"
    assert any("bad-src" in line for line in logs)


def test_run_api_counts_skips_unknown_region():
    logs: list[str] = []
    records = cnt.run_api_counts(
        [cnt.QueryRow("cat", "XX", "q", "en")],
        "procurement",
        client=None,
        log=logs.append,
    )
    assert records == []
    assert logs


def test_run_api_counts_skips_bad_count_values(monkeypatch):
    """A source returning an invalid count is skipped, not fatal."""
    neg = _stub_source("neg-src", ("US",), result=-1)
    text = _stub_source("text-src", ("US",), result="lots")
    ok = _stub_source("ok-src", ("US",), result=3)
    monkeypatch.setattr(
        cnt, "API_SOURCES", {"procurement": (neg, text, ok)}
    )
    logs: list[str] = []
    records = cnt.run_api_counts(
        [cnt.QueryRow("cat", "US", "q", "en")],
        "procurement",
        client=None,
        log=logs.append,
    )
    assert [r.source for r in records] == ["ok-src"]
    assert len(logs) == 2


def test_run_api_counts_none_count_survives_to_parquet(
    monkeypatch, tmp_path
):
    none_src = _stub_source("none-src", ("US",), result=None)
    monkeypatch.setattr(cnt, "API_SOURCES", {"procurement": (none_src,)})
    records = cnt.run_api_counts(
        [cnt.QueryRow("cat", "US", "q", "en")],
        "procurement",
        client=None,
        log=lambda m: None,
    )
    assert len(records) == 1
    assert records[0].count is None
    out = cnt.append_counts(records, tmp_path / "counts.parquet")
    assert pq.read_table(out).to_pylist()[0]["count"] is None


def test_run_api_counts_rejects_source_with_nonsense_hits(monkeypatch):
    """A nonsense probe returning >0 means the source's counts are junk."""
    flaky = _stub_source("flaky-src", ("US",), result=7, nonsense=5)
    monkeypatch.setattr(cnt, "API_SOURCES", {"procurement": (flaky,)})
    records = cnt.run_api_counts(
        [cnt.QueryRow("cat", "US", "q", "en")],
        "procurement",
        client=None,
        log=lambda m: None,
    )
    assert len(records) == 1
    rec = records[0]
    assert rec.count is None
    assert rec.method.endswith("; rejected by sanity guard")
    # A poisoned source needs no match-all probe.
    assert flaky.calls == [cnt.NONSENSE_QUERY, "q"]


def test_run_api_counts_rejects_count_dominating_match_all(monkeypatch):
    big = _stub_source("big-src", ("US",), result=2000, match_all=10_000)
    monkeypatch.setattr(cnt, "API_SOURCES", {"procurement": (big,)})
    records = cnt.run_api_counts(
        [cnt.QueryRow("cat", "US", "q", "en")],
        "procurement",
        client=None,
        log=lambda m: None,
    )
    assert records[0].count is None
    assert records[0].method.endswith("; rejected by sanity guard")


def test_run_api_counts_keeps_count_below_share_threshold(monkeypatch):
    ok = _stub_source("ok-src", ("US",), result=1999, match_all=10_000)
    monkeypatch.setattr(cnt, "API_SOURCES", {"procurement": (ok,)})
    records = cnt.run_api_counts(
        [cnt.QueryRow("cat", "US", "q", "en")],
        "procurement",
        client=None,
        log=lambda m: None,
    )
    assert records[0].count == 1999
    assert records[0].method == "ok-src api total"


def test_run_api_counts_caches_probe_per_source(monkeypatch):
    src = _stub_source("cached-src", ("US",), result=3)
    monkeypatch.setattr(cnt, "API_SOURCES", {"procurement": (src,)})
    rows = [
        cnt.QueryRow("a", "US", "q1", "en"),
        cnt.QueryRow("b", "US", "q2", "en"),
    ]
    records = cnt.run_api_counts(
        rows, "procurement", client=None, log=lambda m: None
    )
    assert src.calls == [cnt.NONSENSE_QUERY, cnt.MATCH_ALL_QUERY, "q1", "q2"]
    assert [r.count for r in records] == [3, 3]


def test_run_api_counts_probe_failure_does_not_reject(monkeypatch):
    """When both probes fail, the guard has no evidence; counts pass."""
    src = _stub_source("probe-fail", ("US",), result=4, probe_raises=True)
    monkeypatch.setattr(cnt, "API_SOURCES", {"procurement": (src,)})
    records = cnt.run_api_counts(
        [cnt.QueryRow("cat", "US", "q", "en")],
        "procurement",
        client=None,
        log=lambda m: None,
    )
    assert records[0].count == 4
    assert records[0].method == "probe-fail api total"


def test_cli_count_api_family_writes_counts(tmp_path, monkeypatch, capsys):
    queries_csv = _queries_csv(
        tmp_path,
        [
            ("core-banking", "US", "mainframe", "en"),
            ("erp", "EU", "sap", "en"),
        ],
    )
    out = tmp_path / "counts.parquet"
    us = _stub_source("us-src", ("US",), result=10)
    eu = _stub_source("eu-src", ("EU",), result=20)
    monkeypatch.setattr(
        cnt, "API_SOURCES", {"procurement": (us, eu)}
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "lsa",
            "count",
            "--family",
            "procurement",
            "--queries",
            str(queries_csv),
            "--counts",
            str(out),
        ],
    )
    main()
    printed = capsys.readouterr().out
    assert "mainframe" in printed
    rows = pq.read_table(out).to_pylist()
    assert len(rows) == 2
    by_source = {r["source"]: r for r in rows}
    assert by_source["us-src"]["count"] == 10
    assert by_source["us-src"]["method"] == "us-src api total"
    assert by_source["us-src"]["system"] == ""
    assert by_source["eu-src"]["count"] == 20
    assert by_source["eu-src"]["category"] == "erp"

    # A rerun upserts rather than duplicating rows.
    main()
    assert len(pq.read_table(out).to_pylist()) == 2


def test_cli_count_dry_run_prints_plan_without_writing(
    tmp_path, monkeypatch, capsys
):
    queries_csv = _queries_csv(
        tmp_path,
        [
            ("core-banking", "US", "mainframe", "en"),
            ("erp", "EU", "sap", "en"),
        ],
    )
    out = tmp_path / "counts.parquet"
    us = _stub_source("us-src", ("US",), result=10)
    monkeypatch.setattr(cnt, "API_SOURCES", {"procurement": (us,)})
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "lsa",
            "count",
            "--family",
            "procurement",
            "--queries",
            str(queries_csv),
            "--counts",
            str(out),
            "--dry-run",
        ],
    )
    main()
    printed = capsys.readouterr().out
    assert "us-src" in printed
    assert "mainframe" in printed
    assert "no source" in printed  # the EU row has no matching stub
    assert not out.exists()


def test_cli_count_limit_runs_first_rows_only(tmp_path, monkeypatch):
    queries_csv = _queries_csv(
        tmp_path,
        [
            ("core-banking", "US", "mainframe", "en"),
            ("erp", "US", "sap", "en"),
        ],
    )
    out = tmp_path / "counts.parquet"
    us = _stub_source("us-src", ("US",), result=10)
    monkeypatch.setattr(cnt, "API_SOURCES", {"procurement": (us,)})
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "lsa",
            "count",
            "--family",
            "procurement",
            "--queries",
            str(queries_csv),
            "--counts",
            str(out),
            "--limit",
            "1",
        ],
    )
    main()
    rows = pq.read_table(out).to_pylist()
    assert [r["query"] for r in rows] == ["mainframe"]
