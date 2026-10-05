"""Tests for the MyCareersFuture counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import httpx

from lsa.sources import mycareersfuture


def test_count_reads_total(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"total": 23, "results": []})

    client = mock_client(handler)
    assert mycareersfuture.count("cobol", "SG", client) == 23
    assert seen["params"]["search"] == '"cobol"'
    assert seen["params"]["limit"] == "1"


def test_count_sends_quoted_phrase(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"total": 151})

    client = mock_client(handler)
    mycareersfuture.count("core banking", "SG", client)
    assert seen["params"]["search"] == '"core banking"'


def test_count_quotes_special_chars(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"total": 0})

    client = mock_client(handler)
    mycareersfuture.count("z/TPF d'art", "SG", client)
    assert seen["params"]["search"] == '"z/TPF d\'art"'


def test_count_empty_query_omits_search(mock_client, no_sleep):
    """Empty query is the match-all probe: no search filter."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"total": 40000})

    client = mock_client(handler)
    assert mycareersfuture.count("", "SG", client) == 40000
    assert "search" not in seen["params"]


def test_count_missing_total_returns_none(mock_client, no_sleep):
    client = mock_client(lambda r: httpx.Response(200, json={}))
    assert mycareersfuture.count("cobol", "SG", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"total": 18})

    client = mock_client(handler)
    assert mycareersfuture.count("mainframe", "SG", client) == 18
    assert len(calls) == 2


def test_search_pages_results_and_maps_items(mock_client, no_sleep):
    pages = []

    def handler(request: httpx.Request) -> httpx.Response:
        page = int(dict(request.url.params)["page"])
        pages.append(page)
        results = (
            [
                {
                    "uuid": f"uuid-{i}",
                    "title": "cobol developer",
                    "postedCompany": {"name": "acme bank"},
                    "description": "<p>maintain the <b>core</b> ledger</p>",
                    "metadata": {"jobPostId": "MCF-2026-000001"},
                }
                for i in range(mycareersfuture._PAGE)
            ]
            if page == 0
            else []
        )
        return httpx.Response(200, json={"total": 51, "results": results})

    client = mock_client(handler)
    items = list(mycareersfuture.search("cobol", "SG", client))
    assert pages == [0, 1]
    item = items[0]
    assert item.source_id == "uuid-0"
    # jobPostId beats uuid for the public detail URL.
    assert item.url == "https://www.mycareersfuture.gov.sg/job/mcf-2026-000001"
    assert "cobol developer" in item.text
    assert "acme bank" in item.text
    # description HTML is stripped to visible text
    assert "<p>" not in item.text
    assert "maintain the core ledger" in item.text


def test_search_falls_back_to_uuid_url(mock_client, no_sleep):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "total": 1,
                "results": [{"uuid": "abc123", "title": "as400 op"}],
            },
        )

    client = mock_client(handler)
    items = list(mycareersfuture.search("as400", "SG", client))
    assert items[0].url == "https://www.mycareersfuture.gov.sg/job/abc123"


def test_search_empty_results_stops(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(200, json={"total": 0, "results": []})

    client = mock_client(handler)
    assert list(mycareersfuture.search("zzz", "SG", client)) == []
    assert len(calls) == 1
