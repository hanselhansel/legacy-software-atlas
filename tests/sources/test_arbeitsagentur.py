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
    assert seen["params"]["was"] == '"cobol"'
    assert seen["params"]["size"] == "1"
    assert seen["api_key"] == "jobboerse-jobsuche"


def test_count_sends_quoted_phrase(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"maxErgebnisse": 5})

    client = mock_client(handler)
    arbeitsagentur.count("COBOL Entwickler", "EU", client)
    assert seen["params"]["was"] == '"COBOL Entwickler"'


def test_count_escapes_lucene_specials_inside_quotes(mock_client, no_sleep):
    """A bare '/' splits the query into OR terms even inside quotes."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"maxErgebnisse": 0})

    client = mock_client(handler)
    arbeitsagentur.count("z/TPF", "EU", client)
    assert seen["params"]["was"] == '"z\\/TPF"'


def test_count_quotes_apostrophe_verbatim(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"maxErgebnisse": 0})

    client = mock_client(handler)
    arbeitsagentur.count("d'art système", "EU", client)
    assert seen["params"]["was"] == '"d\'art système"'


def test_count_empty_query_omits_was(mock_client, no_sleep):
    """Empty query is the match-all probe: no was filter."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(200, json={"maxErgebnisse": 1016017})

    client = mock_client(handler)
    assert arbeitsagentur.count("", "EU", client) == 1016017
    assert "was" not in seen["params"]


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


def test_search_pages_stellenangebote_and_maps_items(mock_client, no_sleep):
    pages = []

    def handler(request: httpx.Request) -> httpx.Response:
        params = dict(request.url.params)
        pages.append(params["page"])
        jobs = (
            [
                {
                    "hashId": "10000-1198581490-S",
                    "refnr": "10000-1198581490-S",
                    "titel": "COBOL Entwickler",
                    "arbeitgeber": "bank ag",
                    "arbeitsort": {"ort": "Frankfurt"},
                    "aktuelleVeroeffentlichungsdatum": "2026-01-01",
                }
                for _ in range(arbeitsagentur._PAGE)
            ]
            if params["page"] == "1"
            else []
        )
        return httpx.Response(
            200, json={"maxErgebnisse": 51, "stellenangebote": jobs}
        )

    client = mock_client(handler)
    items = list(arbeitsagentur.search("cobol", "EU", client))
    assert pages == ["1", "2"]
    item = items[0]
    assert item.source_id == "10000-1198581490-S"
    assert item.url == (
        "https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1198581490-S"
    )
    assert "COBOL Entwickler" in item.text
    assert "bank ag" in item.text
    assert "Frankfurt" in item.text


def test_search_sends_key_and_escaped_phrase(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        seen["api_key"] = request.headers.get("x-api-key")
        return httpx.Response(
            200, json={"maxErgebnisse": 0, "stellenangebote": []}
        )

    client = mock_client(handler)
    assert list(arbeitsagentur.search("z/TPF", "EU", client)) == []
    assert seen["params"]["was"] == '"z\\/TPF"'
    assert seen["params"]["page"] == "1"
    assert seen["api_key"] == "jobboerse-jobsuche"
