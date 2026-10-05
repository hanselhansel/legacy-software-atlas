"""``lsa apps`` wiring: dry-run, end-to-end with a mock client."""

from __future__ import annotations

from argparse import Namespace

import httpx

from lsa.apps import cli as apps_cli


def _csv(tmp_path, *rows):
    path = tmp_path / "apps.csv"
    header = "category,region,app_name,country,apple_id\n"
    path.write_text(header + "".join(",".join(r) + "\n" for r in rows))
    return path


def _args(apps_path, tmp_path, **over):
    base = {
        "apps": apps_path,
        "sort": "mostrecent",
        "limit": None,
        "dry_run": False,
        "out": tmp_path / "apps.parquet",
        "items": tmp_path / "items.parquet",
        "raw_dir": tmp_path / "raw" / "app_reviews",
        "passes": None,
    }
    base.update(over)
    return Namespace(**base)


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


LOOKUP = {
    "resultCount": 1,
    "results": [
        {
            "trackName": "BankApp",
            "averageUserRating": 4.25,
            "userRatingCount": 900,
            "version": "2.0",
            "currentVersionReleaseDate": "2026-08-01T00:00:00Z",
        }
    ],
}


def _review(rid, rating, date, body):
    return {
        "id": {"label": rid},
        "im:rating": {"label": str(rating)},
        "updated": {"label": date},
        "title": {"label": "Title" + rid},
        "content": {"label": body, "attributes": {"type": "text"}},
        "link": {"attributes": {"href": f"https://x.test/rev/{rid}"}},
    }


def test_dry_run_lists_rows_writes_nothing(tmp_path, capsys):
    apps = _csv(
        tmp_path,
        ("core-banking", "SG", "BankApp", "sg", "42"),
        ("ehr-hospital", "US", "ChartApp", "us", "43"),
    )
    apps_cli._apps(_args(apps, tmp_path, dry_run=True))
    out = capsys.readouterr().out
    assert "BankApp" in out and "ChartApp" in out and "dry run" in out
    assert not (tmp_path / "apps.parquet").exists()


def test_missing_csv_exits(tmp_path):
    import pytest

    args = _args(tmp_path / "nope.csv", tmp_path)
    with pytest.raises(SystemExit):
        apps_cli._apps(args)


def test_end_to_end(tmp_path, mock_client, no_sleep, capsys):
    apps = _csv(
        tmp_path,
        ("core-banking", "SG", "BankApp", "sg", "42"),
        ("ehr-hospital", "US", "GhostApp", "us", "43"),
    )
    pages = {
        "42": {
            1: [_review("r1", 5, "2026-06-01T00:00:00-07:00", "solid app")],
            2: [],
        }
    }
    client = mock_client(_handler(lookups={"42": LOOKUP}, pages=pages))
    apps_cli._apps(_args(apps, tmp_path), client)
    out = capsys.readouterr().out
    assert "status=ok" in out and "status=missing" in out
    assert "wrote 2 app rows" in out and "wrote 1 items" in out

    import json

    import pyarrow.parquet as pq

    app_rows = pq.read_table(tmp_path / "apps.parquet").to_pylist()
    assert len(app_rows) == 2
    assert app_rows[0]["rating"] == 4.25
    item_rows = pq.read_table(tmp_path / "items.parquet").to_pylist()
    assert len(item_rows) == 1
    row = item_rows[0]
    assert (row["family"], row["source"], row["region"]) == (
        "app_reviews",
        "itunes",
        "SG",
    )
    assert row["category_hint"] == "core-banking"
    assert row["query_count"] == 900 and row["sampled"] == 1

    raws = list((tmp_path / "raw" / "app_reviews").glob("*.json"))
    assert len(raws) == 1
    raw = json.loads(raws[0].read_text())
    assert raw["text"] == "Titler1 (5/5) solid app"
    assert row["item_id"] == "itunes:r1"


def test_limit_caps_rows(tmp_path, capsys):
    apps = _csv(
        tmp_path,
        ("core-banking", "SG", "BankApp", "sg", "42"),
        ("ehr-hospital", "US", "ChartApp", "us", "43"),
    )
    apps_cli._apps(_args(apps, tmp_path, dry_run=True, limit=1))
    out = capsys.readouterr().out
    assert "BankApp" in out and "ChartApp" not in out


def test_sort_mosthelpful_reaches_feed(tmp_path, mock_client, no_sleep):
    apps = _csv(tmp_path, ("core-banking", "SG", "BankApp", "sg", "42"))
    seen = []
    base = _handler(lookups={"42": LOOKUP}, pages={})

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return base(request)

    apps_cli._apps(
        _args(apps, tmp_path, sort="mosthelpful"), mock_client(handler)
    )
    assert any("sortby=mosthelpful" in u for u in seen)
