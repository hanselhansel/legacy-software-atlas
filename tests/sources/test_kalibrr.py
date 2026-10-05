"""Tests for the Kalibrr counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import httpx

from lsa.sources import kalibrr


def test_count_reads_count_and_maps_country(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"count": 95, "jobs": []})

    client = mock_client(handler)
    assert kalibrr.count("core banking", "ID", client) == 95
    assert seen["params"]["country"] == "Indonesia"
    assert seen["params"]["text"] == '"core banking"'


def test_count_quotes_special_chars(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"count": 0})

    client = mock_client(handler)
    kalibrr.count("z/TPF d'art", "ID", client)
    assert seen["params"]["text"] == '"z/TPF d\'art"'


def test_count_empty_query_omits_text(mock_client, no_sleep):
    """Empty query is the match-all probe: no text filter."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"count": 50000})

    client = mock_client(handler)
    assert kalibrr.count("", "ID", client) == 50000
    assert "text" not in seen["params"]
    assert seen["params"]["country"] == "Indonesia"


def test_count_ph_maps_to_philippines(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"count": 90})

    client = mock_client(handler)
    assert kalibrr.count("core banking", "PH", client) == 90
    assert seen["params"]["country"] == "Philippines"


def test_count_from_alternative_returns_none(mock_client, no_sleep):
    """from_alternative means the total is a fuzzy fallback, not this query."""
    client = mock_client(
        lambda r: httpx.Response(
            200, json={"count": 795, "from_alternative": True}
        )
    )
    assert kalibrr.count("mainframe", "PH", client) is None


def test_count_missing_count_returns_none(mock_client, no_sleep):
    client = mock_client(lambda r: httpx.Response(200, json={}))
    assert kalibrr.count("cobol", "ID", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"count": 2})

    client = mock_client(handler)
    assert kalibrr.count("as400", "ID", client) == 2
    assert len(calls) == 2


def test_search_returns_no_items_when_from_alternative(mock_client, no_sleep):
    """A fuzzy fallback page would feed Jev the wrong query's items."""
    client = mock_client(
        lambda r: httpx.Response(
            200,
            json={
                "count": 795,
                "from_alternative": True,
                "jobs": [{"id": 1, "name": "unrelated"}],
            },
        )
    )
    assert list(kalibrr.search("mainframe", "PH", client)) == []


def test_search_maps_jobs_and_pages(mock_client, no_sleep):
    offsets = []

    def handler(request: httpx.Request) -> httpx.Response:
        offsets.append(dict(request.url.params)["offset"])
        jobs = (
            [
                {
                    "id": 270874 + i,
                    "name": "cobol programmer",
                    "company": {"name": "Monde Nissin", "code": "monde-nissin"},
                    "description": "AS400 batch work",
                }
                for i in range(kalibrr._PAGE)
            ]
            if dict(request.url.params)["offset"] == "0"
            else []
        )
        return httpx.Response(200, json={"count": 99, "jobs": jobs})

    client = mock_client(handler)
    items = list(kalibrr.search("cobol", "PH", client))
    assert offsets == ["0", str(kalibrr._PAGE)]
    item = items[0]
    assert item.source_id == "270874"
    assert item.url == (
        "https://www.kalibrr.com/c/monde-nissin/jobs/270874"
    )
    assert "cobol programmer" in item.text
    assert "Monde Nissin" in item.text


def test_search_url_without_company_code(mock_client, no_sleep):
    client = mock_client(
        lambda r: httpx.Response(
            200,
            json={
                "count": 1,
                "jobs": [{"id": 7, "name": "as400 operator"}],
            },
        )
    )
    items = list(kalibrr.search("as400", "ID", client))
    assert items[0].url == "https://www.kalibrr.com/job-board/7"
