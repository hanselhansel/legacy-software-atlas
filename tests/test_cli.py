"""CLI wiring: new families, dry-run, and limit."""

from argparse import Namespace
from pathlib import Path

from lsa import cli, paths

FIXTURES = Path(__file__).parent / "fixtures"


def _args(family, **overrides):
    base = {
        "family": family,
        "terms": FIXTURES / "search_terms.csv",
        "queries": FIXTURES / "count_queries.csv",
        "sites": paths.RESEARCH / "vendor_sites.csv",
        "counts": None,
        "snapshot": None,
        "dry_run": False,
        "limit": None,
    }
    base.update(overrides)
    return Namespace(**base)


def test_dry_run_jobs_pages_plans_without_client(capsys):
    args = _args("jobs-pages", dry_run=True, limit=2)
    records = cli._count_jobs_pages(args)  # client=None -> plan only
    # Two VN rows x three VN sites.
    assert len(records) == 6
    assert all(r.count is None and r.method == "dry-run" for r in records)
    assert {r.source for r in records} == {"topcv", "itviec", "careerviet"}
    assert all(r.family == "jobs-pages" for r in records)


def test_dry_run_jobs_pages_limit(capsys):
    args = _args("jobs-pages", limit=1)
    records = cli._count_jobs_pages(args)
    assert len(records) == 3  # one VN row -> three sites


def test_dry_run_vendor(tmp_path):
    csv_path = tmp_path / "sites.csv"
    csv_path.write_text(
        "vendor,domain,story_path_regex,categories\n"
        "Acme,acme.test,^/stories/,core-banking;payroll-hr\n"
        "Solo,solo.test,^/cases/,\n"
    )
    args = _args("vendor", sites=csv_path)
    records = cli._count_vendor(args)
    assert [r.category for r in records] == ["core-banking", "payroll-hr", ""]
    assert all(r.count is None and r.method == "dry-run" for r in records)
    assert {r.family for r in records} == {"vendor"}
    assert all(r.system in {"Acme", "Solo"} for r in records)


def test_dry_run_reddit():
    args = _args("reddit", limit=2)
    records = cli._count_reddit(args)
    assert len(records) == 2
    assert all(r.source == "reddit" for r in records)


def test_count_writes_parquet(tmp_path):
    """_count with dry_run prints a plan and writes nothing."""
    out = tmp_path / "counts.parquet"
    args = _args("jobs-pages", dry_run=True, limit=1, counts=out)
    cli._count(args)
    assert not out.exists()


def test_unknown_family_exits():
    import pytest

    args = _args("nope")
    with pytest.raises(SystemExit):
        cli._count(args)


def test_sample_tokens_word_count():
    html = (
        "<html><head><title>x</title><style>css{}</style></head>"
        "<body><h1>Hello world</h1><script>var x=1;</script>"
        "<p>one two three</p></body></html>"
    )
    # title + h1 + p visible; script and style dropped, head dropped too.
    assert cli._word_count(html) == 5


def _fetch_args(family, **overrides):
    base = {
        "family": family,
        "counts": None,
        "items": None,
        "sites": paths.RESEARCH / "vendor_sites.csv",
        "passes": paths.ROOT / "configs" / "passes.toml",
        "snapshot": None,
        "dry_run": False,
        "limit": None,
    }
    base.update(overrides)
    return Namespace(**base)


def _count_rec(source, family, method="x api total", query="cobol", count=5):
    from lsa.contracts import CountRecord

    return CountRecord(
        source=source,
        family=family,
        region="US",
        category="mainframe-cobol",
        system="",
        query=query,
        count=count,
        method=method,
        counted_at="T",
    )


def test_fetch_dry_run_lists_plan_writes_nothing(tmp_path, capsys):
    from lsa import count as cnt

    counts = tmp_path / "counts.parquet"
    cnt.append_counts(
        [
            _count_rec("usaspending", "procurement"),
            _count_rec(
                "kalibrr", "jobs",
                method="kalibrr api total; rejected by sanity guard",
            ),
            _count_rec("hn-snapshot", "hn", method="local snapshot regex"),
        ],
        counts,
    )
    items = tmp_path / "items.parquet"
    args = _fetch_args(
        "procurement", counts=counts, items=items, dry_run=True
    )
    cli._fetch(args)
    out = capsys.readouterr().out
    assert "usaspending" in out and "cobol" in out
    assert "kalibrr" not in out
    assert "dry run" in out
    assert not items.exists()


def test_fetch_unknown_family_exits(tmp_path):
    import pytest

    args = _fetch_args("nope", counts=tmp_path / "c.parquet")
    with pytest.raises(SystemExit):
        cli._fetch(args)


def test_fetch_missing_counts_exits(tmp_path):
    import pytest

    args = _fetch_args("procurement", counts=tmp_path / "nope.parquet")
    with pytest.raises(SystemExit):
        cli._fetch(args)


def test_fetch_end_to_end_with_fake_source(tmp_path, monkeypatch, capsys):
    """A fake API source flows through fetch -> raw -> items.parquet."""
    from types import SimpleNamespace

    from lsa import count as cnt
    from lsa.contracts import SourceItem

    def search(query, region, client):
        yield SourceItem("id1", "https://x.test/1", "alpha beta gamma")
        yield SourceItem("id2", "https://x.test/2", "delta epsilon")

    fake = SimpleNamespace(SOURCE="fakesrc", search=search)
    monkeypatch.setitem(cnt.API_SOURCES, "procurement", (fake,))
    monkeypatch.setattr(paths, "RAW", tmp_path / "raw")

    counts = tmp_path / "counts.parquet"
    cnt.append_counts([_count_rec("fakesrc", "procurement")], counts)
    items = tmp_path / "items.parquet"
    args = _fetch_args("procurement", counts=counts, items=items, limit=1)
    cli._fetch(args)

    import pyarrow.parquet as pq

    rows = pq.read_table(items).to_pylist()
    assert len(rows) == 1  # limit honoured
    assert rows[0]["item_id"] == "fakesrc:id1"
    assert rows[0]["family"] == "procurement"
    assert rows[0]["category_hint"] == "mainframe-cobol"
    raw_files = list((tmp_path / "raw" / "procurement").glob("*.json"))
    assert len(raw_files) == 1
    cnt.API_SOURCES.pop("procurement", None)
