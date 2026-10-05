"""Tests for the BOAMP opendatasoft counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import httpx

from lsa.sources import boamp


def test_count_reads_total_count(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(
            200, json={"total_count": 4726, "results": []}
        )

    client = mock_client(handler)
    assert boamp.count("progiciel", "EU", client) == 4726
    assert seen["params"]["where"] == 'search("progiciel")'
    assert seen["params"]["limit"] == "0"


def test_count_escapes_quotes_in_where(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"total_count": 1})

    client = mock_client(handler)
    boamp.count('say "hi"', "EU", client)
    assert seen["params"]["where"] == 'search("say \\"hi\\"")'


def test_count_missing_total_returns_none(mock_client, no_sleep):
    client = mock_client(lambda r: httpx.Response(200, json={}))
    assert boamp.count("progiciel", "EU", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"total_count": 9})

    client = mock_client(handler)
    assert boamp.count("progiciel", "EU", client) == 9
    assert len(calls) == 2
