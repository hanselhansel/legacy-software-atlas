"""`--per-query` sampling: per-row caps, seeded sitemap picks, weight columns."""

from __future__ import annotations

from argparse import Namespace
from types import SimpleNamespace

import pyarrow.parquet as pq
import pytest

from lsa import cli, paths
from lsa import count as cnt
from lsa.contracts import CountRecord, SourceItem
from lsa.fetch import common, stories

SEED = 20261005


def _count_rec(**over):
    kw = {
        "source": "fakesrc",
        "family": "procurement",
        "region": "US",
        "category": "mainframe-cobol",
        "system": "",
        "query": "cobol",
        "count": 5,
        "method": "fakesrc api total",
        "counted_at": "T",
    }
    kw.update(over)
    return CountRecord(**kw)


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
        "per_query": None,
        "seed": SEED,
    }
    base.update(overrides)
    return Namespace(**base)


@pytest.fixture
def fake_search(monkeypatch):
    """A procurement source yielding 5 items per query, in id order."""

    def search(query, region, client):
        for i in range(5):
            yield SourceItem(
                f"{query}-{i}",
                f"https://x.test/{query}/{i}",
                f"{query} word {i}",
            )

    fake = SimpleNamespace(SOURCE="fakesrc", search=search)
    monkeypatch.setitem(cnt.API_SOURCES, "procurement", (fake,))
    yield
    cnt.API_SOURCES.pop("procurement", None)


def test_per_query_caps_items_per_count_row(tmp_path, monkeypatch, fake_search):
    monkeypatch.setattr(paths, "RAW", tmp_path / "raw")
    counts = tmp_path / "counts.parquet"
    cnt.append_counts(
        [
            _count_rec(query="cobol", count=5),
            _count_rec(query="as400", category="ibm-i", count=9),
        ],
        counts,
    )
    items = tmp_path / "items.parquet"
    cli._fetch(
        _fetch_args("procurement", counts=counts, items=items, per_query=2)
    )
    rows = pq.read_table(items).to_pylist()
    assert [r["item_id"] for r in rows] == [
        "fakesrc:cobol-0",
        "fakesrc:cobol-1",
        "fakesrc:as400-0",
        "fakesrc:as400-1",
    ]
    by_hint = {r["category_hint"]: r for r in rows}
    assert by_hint["mainframe-cobol"]["query_count"] == 5
    assert by_hint["mainframe-cobol"]["sampled"] == 2
    assert by_hint["ibm-i"]["query_count"] == 9
    assert by_hint["ibm-i"]["sampled"] == 2


def test_collect_items_enforces_cap_and_stamps_weights(tmp_path):
    """The kept-per-row cap holds even if a producer over-yields."""
    produced = (
        common.Produced(
            SourceItem(f"id{i}", f"https://x.test/{i}", "some words"),
            "src",
            "US",
            "cat",
            "q",
            query_count=10,
        )
        for i in range(4)
    )
    rows = common.collect_items(
        "jobs",
        produced,
        raw_dir=tmp_path / "raw",
        max_words=5,
        fetched_at="T",
        per_query=2,
    )
    assert [r.item_id for r in rows] == ["src:id0", "src:id1"]
    assert all(r.query_count == 10 and r.sampled == 2 for r in rows)


def test_fetch_without_per_query_keeps_everything(
    tmp_path, monkeypatch, fake_search
):
    """No cap: every produced item lands, weights document a full take."""
    monkeypatch.setattr(paths, "RAW", tmp_path / "raw")
    counts = tmp_path / "counts.parquet"
    cnt.append_counts([_count_rec(query="cobol", count=5)], counts)
    items = tmp_path / "items.parquet"
    cli._fetch(_fetch_args("procurement", counts=counts, items=items))
    rows = pq.read_table(items).to_pylist()
    assert len(rows) == 5
    assert all(r["query_count"] == 5 and r["sampled"] == 5 for r in rows)


def test_per_query_must_be_positive(tmp_path, fake_search):
    counts = tmp_path / "counts.parquet"
    cnt.append_counts([_count_rec()], counts)
    args = _fetch_args(
        "procurement",
        counts=counts,
        items=tmp_path / "items.parquet",
        per_query=0,
    )
    with pytest.raises(SystemExit):
        cli._fetch(args)


STORY_URLS = [f"https://acme.test/stories/s{i}" for i in range(8)]
SITEMAP = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    + "".join(f"<url><loc>{u}</loc></url>" for u in STORY_URLS)
    + "<url><loc>https://acme.test/blog/news</loc></url>"
    + "</urlset>"
)


def _sites_csv(tmp_path):
    path = tmp_path / "vendor_sites.csv"
    path.write_text(
        "vendor,domain,story_path_regex,categories\n"
        "Acme,acme.test,/stories/,core-banking\n"
    )
    return path


def _story_handler(requests):
    from httpx import Response

    def handler(request):
        requests.append(str(request.url))
        if request.url.path == "/robots.txt":
            return Response(200, text="User-agent: *\nDisallow:\n")
        if request.url.path == "/sitemap.xml":
            return Response(200, text=SITEMAP)
        if request.url.path.startswith("/stories/"):
            return Response(200, text="<html><body><p>a story</p></body></html>")
        return Response(404, text="nope")

    return handler


def test_seeded_sitemap_sample_is_deterministic(
    mock_client, no_sleep, tmp_path
):
    requests = []
    client = mock_client(_story_handler(requests))
    sites = _sites_csv(tmp_path)
    row = _count_rec(
        source="acme.test",
        family="vendor",
        query="/stories/",
        method="sitemap-url-count",
        count=8,
    )
    first = list(
        stories.fetch(
            [row], client, sites_path=sites, per_query=3, seed=7, log=None
        )
    )
    second = list(
        stories.fetch(
            [row], client, sites_path=sites, per_query=3, seed=7, log=None
        )
    )
    urls = [p.item.url for p in first]
    assert urls == [p.item.url for p in second]
    assert len(urls) == 3
    assert set(urls) <= set(STORY_URLS)
    assert all(p.query_count == 8 for p in first)

    other = list(
        stories.fetch(
            [row], client, sites_path=sites, per_query=3, seed=99, log=None
        )
    )
    assert [p.item.url for p in other] != urls
    # Only sampled pages are fetched, never the whole sitemap.
    story_gets = [u for u in requests if "/stories/" in u]
    assert len(story_gets) == 9


def test_sitemap_sample_covers_full_set_when_cap_exceeds_urls(
    mock_client, no_sleep, tmp_path
):
    requests = []
    client = mock_client(_story_handler(requests))
    row = _count_rec(
        source="acme.test",
        family="vendor",
        query="/stories/",
        method="sitemap-url-count",
        count=8,
    )
    produced = list(
        stories.fetch(
            [row],
            client,
            sites_path=_sites_csv(tmp_path),
            per_query=50,
            seed=7,
            log=None,
        )
    )
    assert [p.item.url for p in produced] == STORY_URLS
