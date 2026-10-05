"""Tests for the award collection driver (plan 3, lane L)."""

from __future__ import annotations

from types import SimpleNamespace

import pyarrow.parquet as pq

from lsa.awards import collect
from lsa.awards.common import AwardRow, QueryRow


def _row(award_id, source="stub-us", region="US", query="mainframe"):
    return AwardRow(
        award_id=award_id,
        source=source,
        region=region,
        category_hint="core-banking",
        query=query,
        buyer="Agency",
        title="Title",
        text="maintain the legacy system",
        value=100.0,
        currency="USD",
        start_date="2025-01-01",
        end_date="2026-01-01",
        duration_months=None,
        procedure="open",
        cpv_or_psc="",
        url="https://example.com/a",
    )


def _stub(sources, regions, rows_by_query, calls):
    def _collect(rows, client, *, per_query, log=None):
        calls.append([r.query for r in rows])
        for r in rows:
            yield from rows_by_query.get(r.query, [])

    return SimpleNamespace(
        SOURCES=sources, REGIONS=regions, collect=_collect
    )


def test_plan_routes_rows_to_region_collectors():
    queries = [
        QueryRow("core-banking", "US", "mainframe"),
        QueryRow("core-banking", "EU", "core banking"),
        QueryRow("core-banking", "UK", "erp"),
        QueryRow("core-banking", "AU", "mainframe"),
        QueryRow("core-banking", "SG", "erp"),
        QueryRow("core-banking", "XX", "unmatched"),
    ]
    by_region = {r.region: mods for r, mods in collect.plan(queries)}
    assert [m.SOURCE for m in by_region["US"]] == ["usaspending"]
    assert [m.SOURCE for m in by_region["EU"]] == ["ted"]
    assert by_region["UK"][0].SOURCES == ("find-tender", "contracts-finder")
    assert [m.SOURCE for m in by_region["AU"]] == ["austender"]
    assert [m.SOURCE for m in by_region["SG"]] == ["gebiz"]
    assert by_region["XX"] == []


def test_run_dedupes_across_collectors(tmp_path):
    calls = []
    stub_a = _stub(("a",), ("US",), {"mainframe": [_row("a:1"), _row("a:1")]}, calls)
    stub_b = _stub(("b",), ("US",), {"mainframe": [_row("a:1"), _row("b:2")]}, calls)
    kept = collect.run(
        [QueryRow("core-banking", "US", "mainframe")],
        object(),  # stubs never touch the client
        per_query=None,
        limit=None,
        awards_path=tmp_path / "awards.parquet",
        items_path=tmp_path / "items.parquet",
        raw_dir=tmp_path / "raw",
        rates={"USD": 1.0},
        fetched_at="2026-10-05T00:00:00Z",
        log=None,
        collectors=(stub_a, stub_b),
    )
    assert [r.award_id for r in kept] == ["a:1", "b:2"]
    table = pq.read_table(tmp_path / "awards.parquet")
    assert table.num_rows == 2
    items = pq.read_table(tmp_path / "items.parquet").to_pylist()
    assert {i["family"] for i in items} == {"awards"}
    assert len(list((tmp_path / "raw").glob("*.json"))) == 2


def test_run_limit_stops_collection(tmp_path):
    calls = []
    stub = _stub(
        ("a",),
        ("US",),
        {"mainframe": [_row(f"a:{i}") for i in range(5)]},
        calls,
    )
    kept = collect.run(
        [QueryRow("core-banking", "US", "mainframe")],
        object(),
        per_query=None,
        limit=2,
        awards_path=tmp_path / "awards.parquet",
        items_path=tmp_path / "items.parquet",
        raw_dir=tmp_path / "raw",
        rates={"USD": 1.0},
        fetched_at="2026-10-05T00:00:00Z",
        log=None,
        collectors=(stub,),
    )
    assert len(kept) == 2


def test_run_filters_regions_per_collector(tmp_path):
    calls = []
    stub_us = _stub(("us",), ("US",), {}, calls)
    stub_sg = _stub(("sg",), ("SG",), {}, calls)
    collect.run(
        [
            QueryRow("core-banking", "US", "mainframe"),
            QueryRow("core-banking", "SG", "erp"),
            QueryRow("core-banking", "XX", "none"),
        ],
        object(),
        per_query=None,
        limit=None,
        awards_path=tmp_path / "awards.parquet",
        items_path=tmp_path / "items.parquet",
        raw_dir=tmp_path / "raw",
        rates={"USD": 1.0},
        fetched_at="2026-10-05T00:00:00Z",
        log=None,
        collectors=(stub_us, stub_sg),
    )
    assert calls == [["mainframe"], ["erp"]]
