import json

import httpx
import pyarrow.parquet as pq

from lsa import yc


def _company(**kw):
    base = {
        "id": 1,
        "name": "Acme Ledger",
        "slug": "acme-ledger",
        "one_liner": "Banking ops copilot",
        "long_description": "We automate the core ledger.",
        "batch": "Winter 2025",
        "status": "Active",
        "url": "https://www.ycombinator.com/companies/acme-ledger",
        "website": "https://acme.test",
    }
    return base | kw


def test_batch_year_parses_season_and_short_forms():
    assert yc.batch_year("Winter 2012") == 2012
    assert yc.batch_year("Summer 2024") == 2024
    assert yc.batch_year("Fall 2025") == 2025
    assert yc.batch_year("W24") == 2024
    assert yc.batch_year("S23") == 2023
    assert yc.batch_year("") is None
    assert yc.batch_year(None) is None


def test_company_rows_keeps_2024_onward():
    rows = yc.company_rows(
        [
            _company(id=1, batch="Winter 2024"),
            _company(id=2, batch="Summer 2023"),
            _company(id=3, batch="W25"),
            _company(id=4, batch=""),
        ]
    )
    assert [r["item_id"] for r in rows] == ["yc:1", "yc:3"]


def test_item_text_one_liner_plus_description_capped_120_words():
    c = _company(
        one_liner=" ".join(["liner"] * 100),
        long_description=" ".join(["deep"] * 100),
    )
    words = yc.item_text(c).split()
    assert len(words) == 120
    assert words[0] == "liner"
    assert words[-1] == "deep"


def test_fetch_all_reads_cache_without_client(tmp_path):
    cache = tmp_path / "all.json"
    cache.write_text(json.dumps([_company()]))
    assert yc.fetch_all(cache) == [_company()]


def test_fetch_all_downloads_and_caches(tmp_path):
    cache = tmp_path / "all.json"

    def handler(request):
        return httpx.Response(200, json=[_company(id=9, batch="Spring 2025")])

    client = httpx.Client(transport=httpx.MockTransport(handler))
    rows = yc.fetch_all(cache, client=client)
    assert rows[0]["id"] == 9
    assert json.loads(cache.read_text())[0]["id"] == 9


def test_run_writes_yc_parquet_items_and_raw(tmp_path):
    src = tmp_path / "all.json"
    src.write_text(
        json.dumps(
            [
                _company(id=1, batch="Winter 2024"),
                _company(id=2, batch="Summer 2020"),
            ]
        )
    )
    raw_dir = tmp_path / "raw" / "yc"
    items_path = tmp_path / "items.parquet"
    out_path = tmp_path / "yc.parquet"
    rows = yc.run(
        input_path=src,
        raw_dir=raw_dir,
        items_path=items_path,
        out_path=out_path,
        fetched_at="2026-10-05T00:00:00Z",
    )
    assert [r["item_id"] for r in rows] == ["yc:1"]

    yc_rows = pq.read_table(out_path).to_pylist()
    assert yc_rows[0]["item_id"] == "yc:1"
    assert yc_rows[0]["name"] == "Acme Ledger"
    assert yc_rows[0]["batch"] == "Winter 2024"
    assert yc_rows[0]["status"] == "Active"

    items = pq.read_table(items_path).to_pylist()
    assert items[0]["family"] == "yc"
    assert items[0]["item_id"] == "yc:1"
    assert items[0]["source"] == "yc-oss"

    raw = json.loads(next(raw_dir.glob("*.json")).read_text())
    assert raw["text"].startswith("Banking ops copilot")
    assert "core ledger" in raw["text"]
