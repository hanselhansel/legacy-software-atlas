"""Tests for the USAspending award collector (plan 3, lane L)."""

from __future__ import annotations

import json

import httpx

from lsa.awards import usaspending
from lsa.awards.common import QueryRow


def _search_row(**over):
    row = {
        "internal_id": 353863805,
        "generated_internal_id": "CONT_AWD_FA830725FB166_9700_X_4732",
        "Award ID": "FA830725FB166",
        "Recipient Name": "M2 TECHNOLOGY, INC.",
        "Awarding Agency": "Department of Defense",
        "Award Amount": 60272.0,
        "Start Date": "2025-11-24",
        "End Date": "2030-11-23",
        "Description": "POWERVAULT ME5012 mainframe storage refresh",
        "PSC": {"code": "7B21", "description": "IT AND TELECOM - MAINFRAME"},
    }
    row.update(over)
    return row


def _detail(**contract_over):
    contract = {
        "extent_competed": "A",
        "extent_competed_description": "FULL AND OPEN COMPETITION",
        "other_than_full_and_open": None,
        "other_than_full_and_open_description": None,
    }
    contract.update(contract_over)
    return {
        "piid": "FA830725FB166",
        "description": "POWERVAULT ME5012 mainframe storage refresh",
        "total_obligation": 60272.0,
        "awarding_agency": {"name": "Department of Defense"},
        "period_of_performance": {
            "start_date": "2025-11-24",
            "end_date": "2026-11-23",
            "potential_end_date": "2030-11-23 00:00:00",
        },
        "latest_transaction_contract_data": contract,
    }


def _handler(search_rows, detail=None, detail_status=200):
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        if request.url.path == "/api/v2/search/spending_by_award/":
            return httpx.Response(
                200,
                json={
                    "results": list(search_rows),
                    "page_metadata": {"hasNext": False},
                },
            )
        if request.url.path.startswith("/api/v2/awards/"):
            if detail is None:
                return httpx.Response(detail_status)
            return httpx.Response(200, json=detail)
        return httpx.Response(404)

    return handler, seen


def test_collect_maps_search_and_detail_fields(mock_client, no_sleep):
    handler, _ = _handler([_search_row()], detail=_detail())
    rows = list(
        usaspending.collect(
            [QueryRow("core-banking", "US", "mainframe")],
            mock_client(handler),
            per_query=10,
            log=None,
        )
    )
    assert len(rows) == 1
    row = rows[0]
    assert row.award_id == "usaspending:CONT_AWD_FA830725FB166_9700_X_4732"
    assert row.buyer == "Department of Defense"
    assert row.title == "FA830725FB166"
    assert "POWERVAULT" in row.text
    assert row.value == 60272.0
    assert row.currency == "USD"
    assert row.start_date == "2025-11-24"
    # Potential end date (full length incl options), not the current end.
    assert row.end_date == "2030-11-23"
    assert row.procedure == "open"
    assert row.cpv_or_psc == "7B21"
    assert row.url.endswith("/award/CONT_AWD_FA830725FB166_9700_X_4732")


def test_collect_posts_contracts_only_with_keyword(mock_client, no_sleep):
    bodies = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        if request.url.path == "/api/v2/search/spending_by_award/":
            bodies.append(json.loads(request.read()))
            return httpx.Response(
                200, json={"results": [], "page_metadata": {"hasNext": False}}
            )
        return httpx.Response(404)

    client = mock_client(handler)
    list(
        usaspending.collect(
            [QueryRow("core-banking", "US", "core banking")],
            client,
            per_query=None,
            log=None,
        )
    )
    assert len(bodies) == 1
    filters = bodies[0]["filters"]
    assert filters["award_type_codes"] == ["A", "B", "C", "D"]
    assert filters["keywords"] == ['"core banking"']
    assert filters["time_period"]


def test_collect_maps_extent_competed_descriptions(mock_client, no_sleep):
    cases = [
        ("FULL AND OPEN COMPETITION", "open"),
        ("FULL AND OPEN COMPETITION AFTER EXCLUSION OF SOURCES", "restricted"),
        ("COMPETED UNDER SIMPLIFIED ACQUISITION PROCEDURES", "restricted"),
        ("OTHER THAN FULL AND OPEN COMPETITION", "negotiated_no_competition"),
        ("FOLLOW ON TO COMPETED ACTION", "negotiated_no_competition"),
        ("NOT COMPETED", "direct"),
        ("NOT COMPETED UNDER SIMPLIFIED ACQUISITION PROCEDURES", "direct"),
        ("NOT AVAILABLE FOR COMPETITION", "direct"),
        (None, "unknown"),
        ("SOMETHING NEW", "unknown"),
    ]
    for desc, expected in cases:
        detail = _detail(extent_competed_description=desc)
        handler, _ = _handler([_search_row()], detail=detail)
        rows = list(
            usaspending.collect(
                [QueryRow("core-banking", "US", "mainframe")],
                mock_client(handler),
                per_query=1,
                log=None,
            )
        )
        assert rows[0].procedure == expected, desc


def test_collect_detail_failure_yields_unknown_procedure(mock_client, no_sleep):
    handler, _ = _handler([_search_row()], detail=None, detail_status=500)
    rows = list(
        usaspending.collect(
            [QueryRow("core-banking", "US", "mainframe")],
            mock_client(handler),
            per_query=1,
            log=None,
        )
    )
    assert len(rows) == 1
    assert rows[0].procedure == "unknown"
    # Falls back to the search row's fields.
    assert rows[0].end_date == "2030-11-23"


def test_collect_per_query_stops_detail_calls(mock_client, no_sleep):
    search_rows = [
        _search_row(generated_internal_id=f"CONT_AWD_{i}", **{"Award ID": f"PIID{i}"})
        for i in range(5)
    ]
    detail_calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        if request.url.path == "/api/v2/search/spending_by_award/":
            return httpx.Response(
                200,
                json={
                    "results": search_rows,
                    "page_metadata": {"hasNext": False},
                },
            )
        if request.url.path.startswith("/api/v2/awards/"):
            detail_calls.append(1)
            return httpx.Response(200, json=_detail())
        return httpx.Response(404)

    client = mock_client(handler)
    rows = list(
        usaspending.collect(
            [QueryRow("core-banking", "US", "mainframe")],
            client,
            per_query=2,
            log=None,
        )
    )
    assert len(rows) == 2
    assert len(detail_calls) == 2


def test_collect_other_regions_skipped(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(str(request.url))
        return httpx.Response(404)

    client = mock_client(handler)
    rows = list(
        usaspending.collect(
            [QueryRow("core-banking", "EU", "sap")],
            client,
            per_query=None,
            log=None,
        )
    )
    assert rows == []
    assert calls == []


def test_collect_robots_disallowed_skips(mock_client, no_sleep):
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text="User-agent: *\nDisallow: /\n")
        return httpx.Response(404)

    logs = []
    rows = list(
        usaspending.collect(
            [QueryRow("core-banking", "US", "mainframe")],
            mock_client(handler),
            per_query=None,
            log=logs.append,
        )
    )
    assert rows == []
    assert logs
