"""Tests for the AusTender OCDS award collector (plan 3, lane L)."""

from __future__ import annotations

import httpx

from lsa.awards import austender
from lsa.awards.common import QueryRow

_BASE = httpx.URL(austender.URL).host


def _release(**over):
    release = {
        "ocid": "prod-65f4a315a47a4a62aa475c59e1944949",
        "id": "prod-65f4a315a47a4a62aa475c59e1944949-bc1c09",
        "tag": ["contract"],
        "initiationType": "tender",
        "tender": {
            "id": "ATM-2026-0001",
            "procurementMethod": "limited",
            "procurementMethodDetails": "Limited tender exemption",
        },
        "parties": [
            {
                "id": "abc123",
                "name": "Munupi Aboriginal Corporation",
                "roles": ["supplier"],
            },
            {
                "id": "def456",
                "name": "National Indigenous Australians Agency",
                "roles": ["procuringEntity"],
            },
        ],
        "awards": [
            {
                "id": "CN4280221-da775ca26c734f5eb2c07b501f71fb5c",
                "suppliers": [{"id": "abc123", "name": "Munupi Aboriginal Corporation"}],
                "status": "active",
            }
        ],
        "contracts": [
            {
                "id": "CN4280221",
                "awardID": "CN4280221-da775ca26c734f5eb2c07b501f71fb5c",
                "title": "NCD11811",
                "description": "Core banking platform maintenance services",
                "dateSigned": "2026-10-01T23:51:13Z",
                "status": "active",
                "period": {
                    "startDate": "2026-09-22T14:00:00Z",
                    "endDate": "2027-06-29T14:00:00Z",
                },
                "value": {"amount": "44490.60", "currency": "AUD"},
                "items": [
                    {
                        "id": "80101504-da77",
                        "classification": {"id": "80101504", "scheme": "UNSPSC"},
                    }
                ],
            }
        ],
    }
    release.update(over)
    return release


def _handler(pages_by_date):
    """pages_by_date: list of pages (release lists) served in order."""
    state = {"page": 0}
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        seen.append(request.url)
        idx = min(state["page"], len(pages_by_date) - 1)
        links = {}
        if idx + 1 < len(pages_by_date):
            links["next"] = str(request.url) + "?cursor=next"
            state["page"] += 1
        return httpx.Response(
            200,
            json={
                "releases": pages_by_date[idx],
                "uri": str(request.url),
                "links": links,
            },
        )

    return handler, seen


def test_collect_maps_contract_fields(mock_client, no_sleep):
    handler, seen = _handler([[_release()]])
    rows = list(
        austender.collect(
            [QueryRow("core-banking", "AU", "core banking")],
            mock_client(handler),
            per_query=10,
            log=None,
        )
    )
    assert len(rows) == 1
    row = rows[0]
    assert row.award_id == "austender:CN4280221"
    assert row.source == "austender"
    assert row.buyer == "National Indigenous Australians Agency"
    assert row.title == "NCD11811"
    assert "Core banking platform" in row.text
    assert row.value == 44490.60
    assert row.currency == "AUD"
    assert row.start_date == "2026-09-22"
    assert row.end_date == "2027-06-29"
    assert row.procedure == "negotiated_no_competition"
    assert row.cpv_or_psc == "80101504"
    assert "CN4280221" in row.url
    assert "/ocds/findByDates/" in str(seen[0])


def test_collect_open_tender_maps_open(mock_client, no_sleep):
    release = _release()
    release["tender"]["procurementMethod"] = "open"
    release["tender"]["procurementMethodDetails"] = "Open tender"
    handler, _ = _handler([[release]])
    rows = list(
        austender.collect(
            [QueryRow("core-banking", "AU", "core banking")],
            mock_client(handler),
            per_query=1,
            log=None,
        )
    )
    assert rows[0].procedure == "open"


def test_collect_filters_locally_by_keyword(mock_client, no_sleep):
    other = _release()
    other["contracts"] = [
        {**other["contracts"][0], "id": "CN999",
         "description": "School catering services"}
    ]
    other["ocid"] = "prod-other"
    handler, _ = _handler([[_release(), other]])
    rows = list(
        austender.collect(
            [QueryRow("core-banking", "AU", "core banking")],
            mock_client(handler),
            per_query=None,
            log=None,
        )
    )
    assert [r.award_id for r in rows] == ["austender:CN4280221"]


def test_collect_follows_links_next(mock_client, no_sleep):
    """A second page via links.next is fetched; repeat CNs dedupe."""
    handler, seen = _handler([[_release()], [_release()]])
    rows = list(
        austender.collect(
            [QueryRow("core-banking", "AU", "core banking")],
            mock_client(handler),
            per_query=None,
            log=None,
        )
    )
    assert len(rows) == 1
    assert len(seen) >= 2


def test_collect_multiple_contracts_in_release(mock_client, no_sleep):
    release = _release()
    release["contracts"] = [
        release["contracts"][0],
        {
            **release["contracts"][0],
            "id": "CN4280222",
            "description": "Core banking platform integration",
            "value": {"amount": "1000", "currency": "AUD"},
        },
    ]
    handler, _ = _handler([[release]])
    rows = list(
        austender.collect(
            [QueryRow("core-banking", "AU", "core banking")],
            mock_client(handler),
            per_query=10,
            log=None,
        )
    )
    assert {r.award_id for r in rows} == {
        "austender:CN4280221",
        "austender:CN4280222",
    }
