"""Tests for the awards shared plumbing: queries, fx, windowing, writes."""

from __future__ import annotations

import json
from pathlib import Path

import pyarrow.parquet as pq

from lsa.awards import common
from lsa.fetch import common as fcommon

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"


def _row(**over) -> common.AwardRow:
    kw = {
        "award_id": "src:a1",
        "source": "src",
        "region": "UK",
        "category_hint": "erp-distribution",
        "query": "sap",
        "buyer": "Department of Work",
        "title": "ERP renewal",
        "text": " ".join(["w"] * 200),
        "value": 1000.0,
        "currency": "GBP",
        "start_date": "2025-01-01",
        "end_date": "2026-01-01",
        "duration_months": None,
        "procedure": "open",
        "cpv_or_psc": "72000000",
        "url": "https://example.test/a1",
    }
    kw.update(over)
    return common.AwardRow(**kw)


def test_load_queries(tmp_path):
    rows = common.load_queries(FIXTURES / "award_queries.csv")
    assert len(rows) == 5
    first = rows[0]
    assert (first.category, first.region, first.query) == (
        "core-banking",
        "US",
        "core banking",
    )
    assert rows[3].region == "AU"


def test_load_fx_returns_dated_rates(tmp_path):
    fx = tmp_path / "fx.toml"
    fx.write_text(
        'as_of = "2026-10-05"\n\n[rates]\nUSD = 1.0\nGBP = 1.34\n', "utf-8"
    )
    as_of, rates = common.load_fx(fx)
    assert as_of == "2026-10-05"
    assert rates["GBP"] == 1.34


def test_to_usd_converts_known_currency():
    rates = {"USD": 1.0, "EUR": 1.17, "GBP": 1.34}
    assert common.to_usd(100.0, "GBP", rates) == 134.0
    assert common.to_usd(50.0, "USD", rates) == 50.0


def test_to_usd_missing_rate_or_amount_is_none():
    assert common.to_usd(100.0, "JPY", {"USD": 1.0}) is None
    assert common.to_usd(None, "GBP", {"GBP": 1.34}) is None


def test_months_between_dates():
    assert common.months_between("2025-01-01", "2026-01-01") == 12.0
    assert common.months_between("2026-08-20", "2028-08-19") == 24.0


def test_months_between_iso_datetime_and_bad_input():
    assert (
        common.months_between("2025-01-01T00:00:00+01:00", "2025-07-01") == 6.0
    )
    assert common.months_between("", "2025-07-01") is None
    assert common.months_between("2026-01-01", "2025-01-01") is None
    assert common.months_between("garbage", "2025-01-01") is None


def test_window_cuts_at_120_words():
    text = " ".join(f"w{i}" for i in range(200))
    out = common.window(text)
    assert len(out.split()) == 120
    assert out.endswith("w119")


def test_ocds_procedure_map():
    assert common.ocds_procedure("open") == "open"
    assert common.ocds_procedure("selective") == "restricted"
    assert common.ocds_procedure("limited") == "negotiated_no_competition"
    assert common.ocds_procedure("direct") == "direct"
    assert common.ocds_procedure(None) == "unknown"
    assert common.ocds_procedure("weird") == "other"


def test_write_awards_schema_and_derived(tmp_path):
    path = tmp_path / "awards.parquet"
    common.write_awards([_row()], path, rates={"USD": 1.0, "GBP": 1.34})
    rows = pq.read_table(path).to_pylist()
    assert len(rows) == 1
    row = rows[0]
    assert row["award_id"] == "src:a1"
    assert row["value_usd"] == 1340.0
    assert row["duration_months"] == 12.0
    assert len(row["text_window"].split()) == 120
    assert row["procedure"] == "open"
    assert set(row) == {
        "award_id",
        "source",
        "region",
        "category_hint",
        "query",
        "buyer",
        "title",
        "text_window",
        "value_usd",
        "start_date",
        "end_date",
        "duration_months",
        "procedure",
        "cpv_or_psc",
        "url",
    }


def test_write_awards_upserts_on_award_id(tmp_path):
    path = tmp_path / "awards.parquet"
    rates = {"GBP": 1.34}
    common.write_awards([_row(title="v1"), _row(title="other")], path, rates=rates)
    # Rerun: same award_id replaces, a new one appends.
    common.write_awards(
        [_row(title="v2"), _row(award_id="src:b2")], path, rates=rates
    )
    rows = pq.read_table(path).to_pylist()
    assert len(rows) == 2
    titles = {r["award_id"]: r["title"] for r in rows}
    assert titles["src:a1"] == "v2"
    assert "src:b2" in titles


def test_write_items_writes_raw_json_and_item_rows(tmp_path):
    raw_dir = tmp_path / "raw" / "awards"
    items_path = tmp_path / "items.parquet"
    rows = [_row(), _row(award_id="src:b2", text="short")]
    item_rows = common.write_items(
        rows, raw_dir, items_path, fetched_at="2026-10-05T00:00:00Z"
    )
    assert len(item_rows) == 2
    raw_file = raw_dir / f"{fcommon.safe_name('src:a1')}.json"
    data = json.loads(raw_file.read_text("utf-8"))
    assert len(data["text"].split()) == 120
    stored = pq.read_table(items_path).to_pylist()
    assert len(stored) == 2
    first = next(r for r in stored if r["item_id"] == "src:a1")
    assert first["family"] == "awards"
    assert first["source"] == "src"
    assert first["region"] == "UK"
    # Both rows share the same (source,region,category,query) key.
    assert first["sampled"] == 2


def test_write_items_skips_empty_text(tmp_path):
    """Awards keep a parquet row even with empty description, but an empty
    text_window has nothing for Jev to label, so no item row is written."""
    raw_dir = tmp_path / "raw" / "awards"
    items_path = tmp_path / "items.parquet"
    item_rows = common.write_items(
        [_row(text=""), _row(award_id="src:b2", text="has text")],
        raw_dir,
        items_path,
        fetched_at="t",
    )
    assert [r.item_id for r in item_rows] == ["src:b2"]


def test_query_row_repr(tmp_path):
    rows = common.load_queries(FIXTURES / "award_queries.csv")
    assert {r.category for r in rows} == {
        "core-banking",
        "erp-distribution",
        "ehr-hospital",
        "mainframe-cobol-general",
    }
