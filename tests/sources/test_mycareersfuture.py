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
    assert seen["params"]["search"] == "cobol"
    assert seen["params"]["limit"] == "1"


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
