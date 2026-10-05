"""Tests for the GeBIZ data.gov.sg counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import httpx

from lsa.sources import gebiz


def test_count_filters_candidates_to_exact_phrase(mock_client, no_sleep):
    """q is a loose candidate filter; the count is the exact-phrase subset."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(
            200,
            json={
                "success": True,
                "result": {
                    "total": 3,
                    "records": [
                        {"tender_description": "core banking system refresh"},
                        {"tender_description": "core sampling, banking hours"},
                        {"tender_description": "CORE BANKING upgrade", "_id": 3},
                    ],
                },
            },
        )

    client = mock_client(handler)
    assert gebiz.count("core banking", "SG", client) == 2
    # The validator rejects quotes, so q carries the raw words.
    assert seen["params"]["resource_id"] == gebiz.RESOURCE_ID
    assert seen["params"]["q"] == "core banking"


def test_count_matches_phrase_with_special_chars(mock_client, no_sleep):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "result": {
                    "total": 2,
                    "records": [
                        {"tender_description": "z/TPF interface licence"},
                        {"tender_description": "z TPF adapter"},
                    ],
                }
            },
        )

    client = mock_client(handler)
    assert gebiz.count("z/TPF", "SG", client) == 1


def test_count_matches_phrase_across_fields(mock_client, no_sleep):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "result": {
                    "total": 2,
                    "records": [
                        {
                            "tender_description": "hardware refresh",
                            "supplier_name": "d'art systems",
                        },
                        {"tender_description": "unrelated", "agency": "PUB"},
                    ],
                }
            },
        )

    client = mock_client(handler)
    assert gebiz.count("d'art", "SG", client) == 1


def test_count_paginates_candidate_records(mock_client, no_sleep):
    pages = []

    def handler(request: httpx.Request) -> httpx.Response:
        pages.append(dict(request.url.params).get("offset", "0"))
        first = len(pages) == 1
        records = [{"tender_description": "core banking"}] if first else [
            {"tender_description": "other"},
            {"tender_description": "core banking"},
        ]
        return httpx.Response(
            200, json={"result": {"total": 3, "records": records}}
        )

    client = mock_client(handler)
    assert gebiz.count("core banking", "SG", client) == 2
    assert len(pages) == 2


def test_count_empty_query_returns_dataset_total(mock_client, no_sleep):
    """Empty query is the match-all probe: unfiltered result.total."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(
            200, json={"result": {"total": 18464, "records": []}}
        )

    client = mock_client(handler)
    assert gebiz.count("", "SG", client) == 18464
    assert "q" not in seen["params"]


def test_count_no_matching_records_is_zero(mock_client, no_sleep):
    client = mock_client(
        lambda r: httpx.Response(
            200, json={"result": {"total": 2, "records": [
                {"tender_description": "soil and core samples"},
                {"tender_description": "banking hours"},
            ]}}
        )
    )
    assert gebiz.count("core banking", "SG", client) == 0


def test_calls_stay_under_datagovsg_rate_limit(mock_client, no_sleep):
    """datastore_search allows 4 calls per 10 s; calls must wait >=2.5 s."""
    client = mock_client(
        lambda r: httpx.Response(200, json={"result": {"total": 1}})
    )
    gebiz.count("a", "SG", client)
    gebiz.count("b", "SG", client)
    assert no_sleep and no_sleep[0] > 2.0


def test_count_missing_result_returns_none(mock_client, no_sleep):
    client = mock_client(lambda r: httpx.Response(200, json={}))
    assert gebiz.count("cobol", "SG", client) is None


def test_count_missing_total_returns_none(mock_client, no_sleep):
    client = mock_client(
        lambda r: httpx.Response(200, json={"result": {}})
    )
    assert gebiz.count("cobol", "SG", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(
            200,
            json={
                "result": {
                    "total": 1,
                    "records": [{"tender_description": "cobol refresh"}],
                }
            },
        )

    client = mock_client(handler)
    assert gebiz.count("cobol", "SG", client) == 1
    assert len(calls) == 2


def test_search_yields_exact_phrase_records_as_items(mock_client, no_sleep):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "success": True,
                "result": {
                    "total": 3,
                    "records": [
                        {
                            "tender_no": "AGO000ETT21000001",
                            "tender_description": "core banking system refresh",
                            "agency": "MHA",
                            "supplier_name": "acme bank tech",
                            "awarded_amt": "100000.00",
                            "award_date": "2024-05-01",
                        },
                        {"tender_description": "core sampling"},
                        {
                            "tender_description": "CORE BANKING upgrade",
                            "_id": 42,
                        },
                    ],
                },
            },
        )

    client = mock_client(handler)
    items = list(gebiz.search("core banking", "SG", client))
    assert [i.source_id for i in items] == ["AGO000ETT21000001", "42"]
    first = items[0]
    assert "core banking system refresh" in first.text
    assert "MHA" in first.text
    assert "acme bank tech" in first.text
    assert "data.gov.sg" in first.url


def test_search_empty_query_yields_nothing(mock_client, no_sleep):
    """The match-all probe stays a count-only path; fetching it would
    stream the whole dataset."""
    client = mock_client(lambda r: httpx.Response(500))
    assert list(gebiz.search("", "SG", client)) == []
