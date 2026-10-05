"""Tests for the TED notice counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import json

import httpx

from lsa.sources import ted


def test_count_reads_total_notice_count(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["body"] = json.loads(request.read())
        return httpx.Response(
            200, json={"totalNoticeCount": 44, "notices": []}
        )

    client = mock_client(handler)
    assert ted.count("core banking", "EU", client) == 44
    assert seen["url"] == "https://api.ted.europa.eu/v3/notices/search"
    assert seen["body"]["query"] == 'FT~"core banking"'
    assert seen["body"]["limit"] == 1


def test_count_missing_total_returns_none(mock_client, no_sleep):
    client = mock_client(
        lambda r: httpx.Response(200, json={"totalNoticeCount": None})
    )
    assert ted.count("cobol", "EU", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"totalNoticeCount": 7})

    client = mock_client(handler)
    assert ted.count("cobol", "EU", client) == 7
    assert len(calls) == 2
