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
    # '=' is the exact-match operator; '~' stems multilingual fields.
    assert seen["body"]["query"] == 'FT="core banking"'
    assert seen["body"]["limit"] == 1


def test_count_quotes_special_chars(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"totalNoticeCount": 0})

    client = mock_client(handler)
    ted.count("z/TPF d'art", "EU", client)
    assert seen["body"]["query"] == 'FT="z/TPF d\'art"'


def test_count_empty_query_is_match_all(mock_client, no_sleep):
    """Empty query maps to a publication-date match-all for the guard."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"totalNoticeCount": 7063501})

    client = mock_client(handler)
    assert ted.count("", "EU", client) == 7063501
    assert seen["body"]["query"] == "publication-date >= 20000101"


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


def test_search_pages_notices_and_flattens_multilingual(mock_client, no_sleep):
    pages = []

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.read())
        pages.append(body["page"])
        if body["page"] == 1:
            notices = [
                {
                    "publication-number": f"000{i}-2026",
                    "notice-title": {"eng": "core banking refresh"},
                    "organisation-name-buyer": {"eng": "bank of test"},
                    "description-lot": {"eng": "replace the ledger"},
                }
                for i in range(ted._PAGE)
            ]
        else:
            notices = []
        return httpx.Response(
            200, json={"notices": notices, "totalNoticeCount": 5}
        )

    client = mock_client(handler)
    items = list(ted.search("core banking", "EU", client))
    assert pages == [1, 2]
    item = items[0]
    assert item.source_id == "0000-2026"
    assert item.url == "https://ted.europa.eu/en/notice/-/detail/0000-2026"
    assert "core banking refresh" in item.text
    assert "bank of test" in item.text


def test_search_sends_query_fields_and_page(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"notices": []})

    client = mock_client(handler)
    assert list(ted.search("core banking", "EU", client)) == []
    assert seen["body"]["query"] == 'FT="core banking"'
    assert seen["body"]["limit"] == ted._PAGE
    assert seen["body"]["page"] == 1
    assert "publication-number" in seen["body"]["fields"]
    assert "notice-title" in seen["body"]["fields"]
    # only TED's enumerated field names; the live API rejects anything else
    assert set(seen["body"]["fields"]) == set(ted._ITEM_FIELDS)
