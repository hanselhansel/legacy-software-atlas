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
    assert seen["body"]["filters"]["keywords"] == ["mainframe"]
    # Same FY2025 window the sources.csv live test verified.
    assert seen["body"]["filters"]["time_period"] == [
        {"start_date": "2024-10-01", "end_date": "2025-09-30"}
    ]


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
