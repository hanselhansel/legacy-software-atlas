"""Tests for the lane M driver and apps.parquet writer."""

from __future__ import annotations

from datetime import UTC, datetime

import httpx
import pytest

from lsa.apps import collect
from lsa.fetch import common

CSV_HEADER = "category,region,app_name,country,apple_id\n"


def _csv(tmp_path, *rows):
    path = tmp_path / "apps.csv"
    lines = [CSV_HEADER] + [",".join(r) + "\n" for r in rows]
    path.write_text("".join(lines), encoding="utf-8")
    return path


def _row(**over):
    base = {
        "category": "core-banking",
        "region": "SG",
        "app_name": "BankApp",
        "country": "sg",
        "apple_id": "42",
    }
    base.update(over)
    return collect.AppRow(**base)


def _review(rid, rating, date, title="t", body="b"):
    return {
        "id": {"label": rid},
        "im:rating": {"label": str(rating)},
        "updated": {"label": date},
        "title": {"label": title},
        "content": {"label": body, "attributes": {"type": "text"}},
        "link": {"attributes": {"href": f"https://x.test/rev/{rid}"}},
    }


def _lookup(aid, rating=4.0, count=100):
    return {
        "resultCount": 1,
        "results": [
            {
                "trackName": f"App{aid}",
                "averageUserRating": rating,
                "userRatingCount": count,
                "version": "1.0",
                "currentVersionReleaseDate": "2026-09-01T00:00:00Z",
            }
        ],
    }


def _handler(*, lookups=None, pages=None):
    def handler(request: httpx.Request) -> httpx.Response:
        path = request.url.path
        if path == "/robots.txt":
            return httpx.Response(404)
        if path == "/lookup":
            aid = request.url.params["id"]
            payload = (lookups or {}).get(aid, {"resultCount": 0, "results": []})
            return httpx.Response(200, json=payload)
        if "/rss/" in path:
            aid = path.split("/id=")[1].split("/")[0]
            page_n = int(path.split("/page=")[1].split("/")[0])
            entries = (pages or {}).get(aid, {}).get(page_n, [])
            return httpx.Response(200, json={"feed": {"entry": entries}})
        return httpx.Response(404)

    return handler


def test_load_apps_parses_rows(tmp_path):
    path = _csv(
        tmp_path,
        ("core-banking", "SG", "BankApp", "SG", "42"),
        ("ehr-hospital", "US", "ChartApp", "us", "43"),
        ("payroll-hr", "US", "Skipped", "us", ""),
    )
    rows = collect.load_apps(path)
    assert [r.apple_id for r in rows] == ["42", "43"]
    assert rows[0] == collect.AppRow(
        "core-banking", "SG", "BankApp", "sg", "42"
    )


def test_load_apps_missing_column_raises(tmp_path):
    path = tmp_path / "apps.csv"
    path.write_text("category,region,app_name,apple_id\nx,SG,y,42\n")
    with pytest.raises(ValueError, match="missing columns"):
        collect.load_apps(path)


def test_iter_collection_records_then_items(mock_client, no_sleep):
    rows = [
        _row(),
        _row(app_name="Ghost", apple_id="99", region="US", country="us"),
    ]
    lookups = {"42": _lookup("42", rating=3.25, count=777)}
    pages = {
        "42": {
            1: [
                _review("r1", 5, "2026-06-01T00:00:00-07:00", "Good", "works"),
                _review("r2", 1, "2020-01-01T00:00:00-07:00", "Old", "stale"),
            ],
            2: [],
        }
    }
    client = mock_client(_handler(lookups=lookups, pages=pages))
    now = datetime(2026, 10, 5, tzinfo=UTC)
    events = list(collect.iter_collection(rows, client, now=now, log=None))

    records = [e for e in events if isinstance(e, collect.AppRecord)]
    produced = [e for e in events if isinstance(e, common.Produced)]
    assert len(records) == 2 and records[0] is events[0]
    assert records[0].status == "ok"
    assert records[0].rating == 3.25 and records[0].rating_count == 777
    assert records[0].version_date == "2026-09-01T00:00:00Z"
    assert records[1].status == "missing"

    # only the in-window review, after its app's record
    assert len(produced) == 1
    p = produced[0]
    assert p.item.source_id == "r1"
    assert p.item.text == "Good (5/5) works"
    assert (p.source, p.region, p.category_hint) == (
        "itunes", "SG", "core-banking"
    )
    assert p.query == "BankApp"
    assert p.query_count == 777


def test_iter_collection_skips_unknown_region(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(str(request.url))
        return httpx.Response(404)

    rows = [_row(region="XX")]
    logs = []
    events = list(
        collect.iter_collection(rows, mock_client(handler), log=logs.append)
    )
    assert events == []
    assert calls == []  # no lookups attempted
    assert any("unknown region" in m for m in logs)


def test_iter_collection_records_errors_without_stopping(
    mock_client, no_sleep
):
    """A lookup that 500s through its retries is an "error" row."""

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        if request.url.path == "/lookup":
            return httpx.Response(500)
        return httpx.Response(404)

    rows = [_row()]
    events = list(
        collect.iter_collection(rows, mock_client(handler), log=None)
    )
    assert [type(e) for e in events] == [collect.AppRecord]
    assert events[0].status == "error"


def test_append_apps_upserts_on_apple_id_country(tmp_path):
    rec = collect.AppRecord(
        source="itunes",
        category="core-banking",
        region="SG",
        app_name="BankApp",
        country="sg",
        apple_id="42",
        rating=4.0,
        rating_count=100,
        version="1.0",
        version_date="2026-01-01",
        collected_at="T1",
        status="ok",
    )
    path = collect.append_apps([rec], tmp_path / "apps.parquet")
    import pyarrow.parquet as pq

    rows = pq.read_table(path).to_pylist()
    assert len(rows) == 1 and rows[0]["rating"] == 4.0

    # a rerun replaces the storefront row, it does not duplicate
    rec2 = collect.AppRecord(
        **{**rec.__dict__, "rating": 4.5, "collected_at": "T2"}
    )
    collect.append_apps([rec2], path)
    rows = pq.read_table(path).to_pylist()
    assert len(rows) == 1 and rows[0]["rating"] == 4.5


def test_months_ago_clamps_to_28th():
    now = datetime(2026, 3, 31, tzinfo=UTC)
    assert collect._months_ago(now, 6) == datetime(2025, 9, 28, tzinfo=UTC)
    assert collect._months_ago(now, 24) == datetime(2024, 3, 31, tzinfo=UTC)
