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
    assert seen["body"]["searchCriteria"]["keyword"] == '"mainframe"'


def test_count_sends_quoted_phrase_keyword(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"hitCount": 846})

    client = mock_client(handler)
    contracts_finder.count("mortgage servicing platform", "UK", client)
    assert seen["body"]["searchCriteria"]["keyword"] == (
        '"mortgage servicing platform"'
    )


def test_count_quotes_special_chars(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"hitCount": 0})

    client = mock_client(handler)
    contracts_finder.count("z/TPF d'art", "UK", client)
    assert seen["body"]["searchCriteria"]["keyword"] == '"z/TPF d\'art"'


def test_count_empty_query_sends_empty_criteria(mock_client, no_sleep):
    """Empty query is the match-all probe: no keyword filter."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"hitCount": 612724})

    client = mock_client(handler)
    assert contracts_finder.count("", "UK", client) == 612724
    assert "keyword" not in seen["body"]["searchCriteria"]
    assert "queryString" not in seen["body"]["searchCriteria"]


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


def test_search_pages_notice_list(mock_client, no_sleep):
    pages = []

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.read())
        pages.append(body.get("page"))
        notices = (
            [
                {
                    "id": f"notice-{i}",
                    "title": "mainframe support",
                    "description": "keep the lights on",
                    "organisationName": "DVLA",
                    "publishedDate": "2025-03-01",
                }
                for i in range(contracts_finder._PAGE)
            ]
            if body.get("page") == 1
            else []
        )
        return httpx.Response(
            200, json={"hitCount": 200, "noticeList": notices}
        )

    client = mock_client(handler)
    items = list(contracts_finder.search("mainframe", "UK", client))
    assert pages == [1, 2]
    assert len(items) == contracts_finder._PAGE
    item = items[0]
    assert item.source_id == "notice-0"
    assert item.url == (
        "https://www.contractsfinder.service.gov.uk/notice/notice-0"
    )
    assert "mainframe support" in item.text
    assert "DVLA" in item.text


def test_search_sends_keyword_page_and_size(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.read())
        return httpx.Response(200, json={"hitCount": 0, "noticeList": []})

    client = mock_client(handler)
    assert list(contracts_finder.search("as400", "UK", client)) == []
    assert seen["body"]["searchCriteria"]["keyword"] == '"as400"'
    assert seen["body"]["page"] == 1
    assert seen["body"]["size"] == contracts_finder._PAGE
