"""Tests for the GeBIZ datastore award collector (plan 3, lane L)."""

from __future__ import annotations

import httpx

from lsa.awards import gebiz
from lsa.awards.common import QueryRow


def _record(**over):
    record = {
        "_id": 1,
        "tender_no": "ACR000ETT21000001",
        "tender_description": (
            "MAINTENANCE OF CORE BANKING PLATFORM WITH OPTION FOR "
            "ENHANCEMENT SERVICES"
        ),
        "agency": "Accounting And Corporate Regulatory Authority",
        "award_date": "6/9/2021",
        "tender_detail_status": "Awarded to Suppliers",
        "supplier_name": "ALPHA ZETTA PTE. LTD.",
        "awarded_amt": "2321600",
    }
    record.update(over)
    return record


def _handler(pages):
    """pages: list of records lists served as consecutive offset pages."""
    state = {"i": 0}
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        seen.append(request.url)
        idx = min(state["i"], len(pages) - 1)
        state["i"] += 1
        records = pages[idx]
        # Pretend the whole set fits one page: total = len(records).
        return httpx.Response(
            200,
            json={
                "result": {
                    "total": len(pages) * len(records) if len(pages) > 1 else len(records),
                    "records": records,
                }
            },
        )

    return handler, seen


def test_collect_maps_record_fields(mock_client, no_sleep):
    handler, seen = _handler([[_record()]])
    rows = list(
        gebiz.collect(
            [QueryRow("core-banking", "SG", "core banking")],
            mock_client(handler),
            per_query=10,
            log=None,
        )
    )
    assert len(rows) == 1
    row = rows[0]
    assert row.award_id.startswith("gebiz:ACR000ETT21000001")
    assert row.source == "gebiz"
    assert row.buyer == "Accounting And Corporate Regulatory Authority"
    assert "CORE BANKING" in row.text
    assert row.value == 2321600.0
    assert row.currency == "SGD"
    assert row.start_date == "2021-09-06"
    assert row.end_date == ""
    assert row.procedure == "open"  # ETT is an open e-tender
    assert row.url
    # q param carries the raw query as the loose candidate filter.
    assert seen[0].params.get("q") == "core banking"


def test_collect_phrase_filters_records(mock_client, no_sleep):
    other = _record(
        _id=2,
        tender_no="MOE000ETT21000002",
        tender_description="SCHOOL DINNER CATERING SERVICES",
        supplier_name="CATERS PTE LTD",
    )
    handler, _ = _handler([[_record(), other]])
    rows = list(
        gebiz.collect(
            [QueryRow("core-banking", "SG", "core banking")],
            mock_client(handler),
            per_query=None,
            log=None,
        )
    )
    assert len(rows) == 1
    assert rows[0].award_id.startswith("gebiz:ACR000ETT21000001")


def test_collect_procedure_from_tender_code(mock_client, no_sleep):
    def rec(code, i):
        return _record(_id=i, tender_no=f"MOE000{code}21000007")

    handler, _ = _handler(
        [[rec("ETT", 1), rec("SVP", 2), rec("RIT", 3)]]
    )
    rows = list(
        gebiz.collect(
            [QueryRow("core-banking", "SG", "core banking")],
            mock_client(handler),
            per_query=None,
            log=None,
        )
    )
    procs = {r.award_id: r.procedure for r in rows}
    assert procs["gebiz:MOE000ETT21000007-ALPHA ZETTA PTE. LTD."] == "open"
    assert procs["gebiz:MOE000SVP21000007-ALPHA ZETTA PTE. LTD."] == "direct"
    assert procs["gebiz:MOE000RIT21000007-ALPHA ZETTA PTE. LTD."] == "restricted"


def test_collect_skips_not_awarded(mock_client, no_sleep):
    record = _record(tender_detail_status="Awarded to No Suppliers")
    handler, _ = _handler([[record]])
    rows = list(
        gebiz.collect(
            [QueryRow("core-banking", "SG", "core banking")],
            mock_client(handler),
            per_query=None,
            log=None,
        )
    )
    assert rows == []


def test_collect_pages_candidates(mock_client, no_sleep):
    """Offset paging walks all candidate pages of the q filter."""
    handler, seen = _handler([[_record(_id=1)], [_record(_id=2, supplier_name="B PTE")]])
    rows = list(
        gebiz.collect(
            [QueryRow("core-banking", "SG", "core banking")],
            mock_client(handler),
            per_query=None,
            log=None,
        )
    )
    assert len(rows) == 2
    assert seen[0].params.get("offset") == "0"
    assert seen[1].params.get("offset") == "1"


def test_collect_per_query_cap(mock_client, no_sleep):
    records = [_record(_id=i, supplier_name=f"S{i}") for i in range(5)]
    handler, _ = _handler([records])
    rows = list(
        gebiz.collect(
            [QueryRow("core-banking", "SG", "core banking")],
            mock_client(handler),
            per_query=2,
            log=None,
        )
    )
    assert len(rows) == 2
