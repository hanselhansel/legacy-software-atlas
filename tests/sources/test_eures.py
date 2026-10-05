"""Tests for the EURES counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import json

import httpx

from lsa.sources import eures


def test_count_reads_number_records(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"numberRecords": 2314})

    client = mock_client(handler)
    assert eures.count("cobol", "EU", client) == 2314
    assert seen["url"] == (
        "https://europa.eu/eures/api/jv-searchengine"
        "/public/jv-search/search"
    )
    keywords = seen["body"]["keywords"]
    assert keywords == [{"keyword": '"cobol"', "specificSearchCode": "EVERYWHERE"}]
    assert seen["body"]["resultsPerPage"] == 1


def test_count_sends_quoted_phrase_keyword(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"numberRecords": 0})

    client = mock_client(handler)
    eures.count("core banking", "EU", client)
    assert seen["body"]["keywords"] == [
        {"keyword": '"core banking"', "specificSearchCode": "EVERYWHERE"}
    ]


def test_count_quotes_special_chars(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"numberRecords": 0})

    client = mock_client(handler)
    eures.count("système d'information de laboratoire", "EU", client)
    assert seen["body"]["keywords"][0]["keyword"] == (
        '"système d\'information de laboratoire"'
    )


def test_count_empty_query_sends_empty_keywords(mock_client, no_sleep):
    """Empty query is the match-all probe: empty keywords array."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"numberRecords": 1932139})

    client = mock_client(handler)
    assert eures.count("", "EU", client) == 1932139
    assert seen["body"]["keywords"] == []


def test_count_missing_number_records_returns_none(mock_client, no_sleep):
    client = mock_client(lambda r: httpx.Response(200, json={}))
    assert eures.count("cobol", "EU", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"numberRecords": 42})

    client = mock_client(handler)
    assert eures.count("as400", "EU", client) == 42
    assert len(calls) == 2


def test_search_pages_jvs_and_maps_items(mock_client, no_sleep):
    pages = []

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.read())
        pages.append(body["page"])
        jvs = (
            [
                {
                    "id": "MjQ1MjkyNyAxOA",
                    "title": "cobol developer",
                    "employer": {"name": "bank of eu"},
                    "description": "maintain the ledger",
                }
                for _ in range(eures._PAGE)
            ]
            if body["page"] == 1
            else []
        )
        return httpx.Response(200, json={"numberRecords": 99, "jvs": jvs})

    client = mock_client(handler)
    items = list(eures.search("cobol", "EU", client))
    assert pages == [1, 2]
    item = items[0]
    assert item.source_id == "MjQ1MjkyNyAxOA"
    assert item.url == (
        "https://europa.eu/eures/portal/jv-se/jv-details/MjQ1MjkyNyAxOA"
    )
    assert "cobol developer" in item.text
    assert "bank of eu" in item.text


def test_search_keeps_quoted_keyword_and_page(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"numberRecords": 0, "jvs": []})

    client = mock_client(handler)
    assert list(eures.search("core banking", "EU", client)) == []
    assert seen["body"]["keywords"] == [
        {"keyword": '"core banking"', "specificSearchCode": "EVERYWHERE"}
    ]
    assert seen["body"]["resultsPerPage"] == eures._PAGE
    assert seen["body"]["page"] == 1
