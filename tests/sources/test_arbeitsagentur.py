"""Tests for the Arbeitsagentur jobsuche counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import httpx

from lsa.sources import arbeitsagentur


def test_count_reads_max_ergebnisse_and_sends_key(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        seen["api_key"] = request.headers.get("x-api-key")
        return httpx.Response(
            200, json={"maxErgebnisse": 49, "stellenangebote": []}
        )

    client = mock_client(handler)
    assert arbeitsagentur.count("cobol", "EU", client) == 49
    assert seen["params"]["was"] == "cobol"
    assert seen["params"]["size"] == "1"
    assert seen["api_key"] == "jobboerse-jobsuche"


def test_count_string_max_ergebnisse_coerces(mock_client, no_sleep):
    """The bund.dev spec types maxErgebnisse as string; coerce to int."""
    client = mock_client(
        lambda r: httpx.Response(200, json={"maxErgebnisse": "49"})
    )
    assert arbeitsagentur.count("cobol", "EU", client) == 49


def test_count_missing_max_ergebnisse_returns_none(mock_client, no_sleep):
    client = mock_client(lambda r: httpx.Response(200, json={}))
    assert arbeitsagentur.count("cobol", "EU", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"maxErgebnisse": 12})

    client = mock_client(handler)
    assert arbeitsagentur.count("as400", "EU", client) == 12
    assert len(calls) == 2
