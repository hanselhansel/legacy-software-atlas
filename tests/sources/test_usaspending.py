"""Tests for the USAspending counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import json

import httpx

from lsa.sources import usaspending

RESULTS = {
    "contracts": 3682,
    "idvs": 136,
    "grants": 5,
    "loans": 0,
    "direct_payments": 0,
    "other": 0,
}


def test_count_sums_procurement_award_groups(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"results": dict(RESULTS)})

    client = mock_client(handler)
    total = usaspending.count("mainframe", "US", client)
    # Procurement instruments only: contracts + idvs, assistance excluded.
    assert total == 3818
    assert seen["url"] == (
        "https://api.usaspending.gov/api/v2/search/spending_by_award_count/"
    )
    assert seen["body"]["filters"]["keywords"] == ['"mainframe"']
    # Same FY2025 window the sources.csv live test verified.
    assert seen["body"]["filters"]["time_period"] == [
        {"start_date": "2024-10-01", "end_date": "2025-09-30"}
    ]


def test_count_sends_quoted_phrase_keywords(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"results": dict(RESULTS)})

    client = mock_client(handler)
    usaspending.count("core banking", "US", client)
    assert seen["body"]["filters"]["keywords"] == ['"core banking"']


def test_count_quotes_special_chars(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"results": dict(RESULTS)})

    client = mock_client(handler)
    usaspending.count("z/TPF d'art", "US", client)
    assert seen["body"]["filters"]["keywords"] == ['"z/TPF d\'art"']


def test_count_empty_query_omits_keywords(mock_client, no_sleep):
    """Empty query is the match-all probe: no keywords filter at all."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"results": dict(RESULTS)})

    client = mock_client(handler)
    usaspending.count("", "US", client)
    assert "keywords" not in seen["body"]["filters"]
    assert seen["body"]["filters"]["time_period"]


def test_count_missing_results_returns_none(mock_client, no_sleep):
    client = mock_client(lambda r: httpx.Response(200, json={}))
    assert usaspending.count("mainframe", "US", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"results": dict(RESULTS)})

    client = mock_client(handler)
    assert usaspending.count("mainframe", "US", client) == 3818
    assert len(calls) == 2


def test_search_pages_awards_until_has_next_false(mock_client, no_sleep):
    pages = []
    row = {
        "internal_id": 1,
        "generated_internal_id": "CONT_AWD_9",
        "Award ID": "FA999",
        "Recipient Name": "acme systems",
        "Awarding Agency": "DoD",
        "Description": "mainframe refresh",
        "Start Date": "2025-01-01",
    }

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.read())
        pages.append(body["page"])
        results = [row] if body["page"] == 1 else [{**row, "internal_id": 2}]
        return httpx.Response(
            200,
            json={
                "results": results,
                "page_metadata": {"hasNext": body["page"] == 1},
            },
        )

    client = mock_client(handler)
    items = list(usaspending.search("mainframe", "US", client))
    assert pages == [1, 2]
    assert len(items) == 2
    item = items[0]
    assert item.source_id == "CONT_AWD_9"
    assert item.url == "https://www.usaspending.gov/award/CONT_AWD_9"
    assert "mainframe refresh" in item.text
    assert "acme systems" in item.text


def test_search_posts_to_award_search_not_count(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["body"] = json.loads(request.read())
        return httpx.Response(
            200, json={"results": [], "page_metadata": {"hasNext": False}}
        )

    client = mock_client(handler)
    assert list(usaspending.search("core banking", "US", client)) == []
    assert seen["url"].endswith("/search/spending_by_award/")
    assert seen["body"]["filters"]["keywords"] == ['"core banking"']
    assert seen["body"]["filters"]["time_period"] == usaspending._TIME_PERIOD
    # Procurement instruments only: contracts A-D plus the IDV family.
    assert "A" in seen["body"]["filters"]["award_type_codes"]
    assert "IDV_E" in seen["body"]["filters"]["award_type_codes"]
    assert "Award ID" in seen["body"]["fields"]
