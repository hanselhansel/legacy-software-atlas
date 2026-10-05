"""Tests for the GeBIZ data.gov.sg counter (plan 1, task 3, lane B)."""

from __future__ import annotations

import httpx

from lsa.sources import gebiz


def test_count_reads_result_total(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["params"] = dict(request.url.params)
        return httpx.Response(
            200, json={"success": True, "result": {"total": 31, "records": []}}
        )

    client = mock_client(handler)
    assert gebiz.count("core banking", "SG", client) == 31
    assert seen["params"]["resource_id"] == gebiz.RESOURCE_ID
    assert seen["params"]["q"] == "core banking"
    assert seen["params"]["limit"] == "1"


def test_count_missing_total_returns_none(mock_client, no_sleep):
    client = mock_client(
        lambda r: httpx.Response(200, json={"result": {"records": []}})
    )
    assert gebiz.count("cobol", "SG", client) is None


def test_count_429_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"result": {"total": 31}})

    client = mock_client(handler)
    assert gebiz.count("cobol", "SG", client) == 31
    assert len(calls) == 2
