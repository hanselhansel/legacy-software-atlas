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
