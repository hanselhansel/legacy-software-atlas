"""Tests for the Contracts Finder counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import json

import httpx

from lsa.sources import contracts_finder


def test_count_reads_hit_count(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["body"] = json.loads(request.read())
        return httpx.Response(
            200, json={"hitCount": 71, "noticeList": []}
        )

    client = mock_client(handler)
    assert contracts_finder.count("mainframe", "UK", client) == 71
    assert seen["url"] == (
        "https://www.contractsfinder.service.gov.uk"
        "/api/rest/2/search_notices/json"
    )
    assert seen["body"]["searchCriteria"]["keyword"] == "mainframe"


def test_count_missing_hit_count_returns_none(mock_client, no_sleep):
    client = mock_client(lambda r: httpx.Response(200, json={}))
    assert contracts_finder.count("mainframe", "UK", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"hitCount": 71})

    client = mock_client(handler)
    assert contracts_finder.count("mainframe", "UK", client) == 71
    assert len(calls) == 2
