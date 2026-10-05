"""The API-family driver maps counted rows to source search() calls."""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from lsa import count as cnt
from lsa.contracts import CountRecord, SourceItem
from lsa.fetch import api


def _record(
    source: str = "fakesrc", query: str = "cobol", region: str = "US"
) -> CountRecord:
    return CountRecord(
        source=source,
        family="fakefam",
        region=region,
        category="legacy-erp",
        system="",
        query=query,
        count=5,
        method="fakesrc api total",
        counted_at="T",
    )


@pytest.fixture
def fake_source(monkeypatch):
    """A source module stub registered for the ``fakefam`` family."""
    calls = []

    def search(query, region, client):
        calls.append((query, region, client))
        yield SourceItem("i1", "https://x.test/1", "some text")

    mod = SimpleNamespace(SOURCE="fakesrc", search=search)
    monkeypatch.setitem(cnt.API_SOURCES, "fakefam", (mod,))
    yield calls
    cnt.API_SOURCES.pop("fakefam", None)


def test_fetch_calls_search_with_row_query_and_region(fake_source):
    produced = list(api.fetch("fakefam", [_record()], client=None, log=None))
    assert fake_source == [("cobol", "US", None)]
    item = produced[0]
    assert item.item.source_id == "i1"
    assert (item.source, item.region, item.category_hint) == (
        "fakesrc",
        "US",
        "legacy-erp",
    )
    assert item.query == "cobol"


def test_fetch_skips_unknown_sources_and_search_errors(monkeypatch):
    def boom(query, region, client):
        raise RuntimeError("api down")
        yield  # pragma: no cover - keeps the signature a generator

    broken = SimpleNamespace(SOURCE="broken", search=boom)
    logs = []
    monkeypatch.setitem(cnt.API_SOURCES, "fakefam", (broken,))
    rows = [_record("nosuch"), _record("broken")]
    produced = list(api.fetch("fakefam", rows, client=None, log=logs.append))
    assert produced == []
    assert any("nosuch" in m for m in logs)
    assert any("broken" in m and "api down" in m for m in logs)
    cnt.API_SOURCES.pop("fakefam", None)
