"""Tests for the TED v3 award collector (plan 3, lane L)."""

from __future__ import annotations

import json

import httpx

from lsa.awards import ted
from lsa.awards.common import QueryRow


def _notice(**over):
    notice = {
        "publication-number": "543210-2026",
        "notice-title": {"eng": "Core banking maintenance"},
        "organisation-name-buyer": {"eng": "Ministry of Finance", "deu": "Finanzministerium"},
        "description-lot": {"eng": "Maintenance and support for the core banking platform."},
        "procedure-type": "neg-wout-call",
        "classification-cpv": ["72260000", "72262000"],
        "estimated-value-lot": 1200000.0,
        "estimated-value-cur-lot": "EUR",
        "tender-value": 1100000.0,
        "tender-value-cur": "EUR",
        "duration-period-value-lot": 36,
        "duration-period-unit-lot": "month",
        "contract-duration-start-date-lot": "2026-01-01+01:00",
        "contract-duration-end-date-lot": "2029-01-01+01:00",
        "winner-name": "ACME Banking Systems",
        "publication-date": "2026-09-01+02:00",
    }
    notice.update(over)
    return notice


def _handler(notices, total_pages=1):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        body = json.loads(request.read())
        calls.append(body)
        page = body.get("page", 1)
        chunk = notices if page <= total_pages else []
        return httpx.Response(
            200, json={"notices": chunk, "totalNoticeCount": len(notices)}
        )

    return handler, calls


def test_collect_maps_notice_fields(mock_client, no_sleep):
    handler, calls = _handler([_notice()])
    rows = list(
        ted.collect(
            [QueryRow("core-banking", "EU", "core banking")],
            mock_client(handler),
            per_query=10,
            log=None,
        )
    )
    assert len(rows) == 1
    row = rows[0]
    assert row.award_id == "ted:543210-2026"
    assert row.source == "ted"
    assert row.buyer == "Ministry of Finance"
    assert row.title == "Core banking maintenance"
    assert "core banking platform" in row.text
    assert row.value == 1100000.0
    assert row.currency == "EUR"
    assert row.start_date == "2026-01-01"
    assert row.end_date == "2029-01-01"
    assert row.procedure == "negotiated_no_competition"
    assert row.cpv_or_psc == "72260000;72262000"
    assert row.url.endswith("/543210-2026")


def test_collect_posts_expert_query(mock_client, no_sleep):
    handler, calls = _handler([])
    client = mock_client(handler)
    list(
        ted.collect(
            [QueryRow("core-banking", "EU", "core banking")],
            client,
            per_query=None,
            log=None,
        )
    )
    body = calls[0]
    assert body["query"] == 'FT="core banking"'
    assert "procedure-type" in body["fields"]
    assert "classification-cpv" in body["fields"]


def test_collect_prefers_awarded_over_estimated(mock_client, no_sleep):
    handler, _ = _handler([_notice(**{"tender-value": 500.0, "estimated-value-lot": 999.0})])
    rows = list(
        ted.collect(
            [QueryRow("core-banking", "EU", "x")],
            mock_client(handler),
            per_query=1,
            log=None,
        )
    )
    assert rows[0].value == 500.0


def test_collect_falls_back_to_estimated(mock_client, no_sleep):
    notice = _notice(**{"tender-value": None, "result-value-lot": None})
    handler, _ = _handler([notice])
    rows = list(
        ted.collect(
            [QueryRow("core-banking", "EU", "x")],
            mock_client(handler),
            per_query=1,
            log=None,
        )
    )
    assert rows[0].value == 1200000.0
    assert rows[0].currency == "EUR"


def test_collect_duration_from_period_fields(mock_client, no_sleep):
    """No contract dates: duration_months comes straight from the lot."""
    notice = _notice(
        **{
            "contract-duration-start-date-lot": None,
            "contract-duration-end-date-lot": None,
            "duration-period-value-lot": 2,
            "duration-period-unit-lot": "year",
        }
    )
    handler, _ = _handler([notice])
    rows = list(
        ted.collect(
            [QueryRow("core-banking", "EU", "x")],
            mock_client(handler),
            per_query=1,
            log=None,
        )
    )
    assert rows[0].duration_months == 24.0
    assert rows[0].start_date == ""


def test_collect_list_valued_fields(mock_client, no_sleep):
    notice = _notice(
        **{
            "procedure-type": ["restricted"],
            "organisation-name-buyer": ["Ministry"],
            "tender-value": ["42.5"],
            "tender-value-cur": ["EUR"],
        }
    )
    handler, _ = _handler([notice])
    rows = list(
        ted.collect(
            [QueryRow("core-banking", "EU", "x")],
            mock_client(handler),
            per_query=1,
            log=None,
        )
    )
    assert rows[0].procedure == "restricted"
    assert rows[0].buyer == "Ministry"
    assert rows[0].value == 42.5


def test_collect_stops_after_short_page(mock_client, no_sleep):
    """A page shorter than the limit is the last page (count-lane rule)."""
    handler, calls = _handler([_notice()])
    client = mock_client(handler)
    list(
        ted.collect(
            [QueryRow("core-banking", "EU", "x")],
            client,
            per_query=None,
            log=None,
        )
    )
    assert len(calls) == 1
