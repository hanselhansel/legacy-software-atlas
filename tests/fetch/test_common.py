"""Counted-row loading, dedupe, windowing and items.parquet writes."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from pathlib import Path

import pyarrow.parquet as pq

from lsa import count as cnt
from lsa.contracts import CountRecord, SourceItem
from lsa.fetch import common


def _record(**over):
    kw = {
        "source": "usaspending",
        "family": "procurement",
        "region": "US",
        "category": "core-banking",
        "system": "",
        "query": "mainframe",
        "count": 3,
        "method": "usaspending api total",
        "counted_at": "2026-10-05T00:00:00Z",
    }
    kw.update(over)
    return CountRecord(**kw)


def _counts(tmp_path: Path, records) -> Path:
    path = tmp_path / "counts.parquet"
    cnt.append_counts(records, path)
    return path


def test_counted_rows_filters_family_keeps_parquet_order(tmp_path):
    path = _counts(
        tmp_path,
        [
            _record(query="mainframe"),
            _record(query="cobol"),
            _record(source="ted", region="EU", method="ted api total"),
            _record(
                source="hn-snapshot",
                family="hn",
                method="local snapshot regex",
            ),
        ],
    )
    rows = common.counted_rows(path, "procurement")
    assert [(r.source, r.query) for r in rows] == [
        ("usaspending", "mainframe"),
        ("usaspending", "cobol"),
        ("ted", "mainframe"),
    ]


def test_counted_rows_skips_rejected_and_dropped(tmp_path):
    """Rows the sanity guard or a reviewer marked stay out of the plan."""
    path = _counts(
        tmp_path,
        [
            _record(
                source="kalibrr",
                query="fuzzy",
                method="kalibrr api total; rejected by sanity guard",
            ),
            _record(
                source="ted",
                region="EU",
                query="Maximo",
                method="ted api total; dropped: Maximo matches the "
                "Romance-language word for maximum",
            ),
            _record(),
        ],
    )
    rows = common.counted_rows(path, "procurement")
    kept = [r for r in rows if common.fetchable(r)]
    assert [r.method for r in kept] == ["usaspending api total"]
    assert len(rows) == 3


def test_counted_rows_skips_empty_query(tmp_path):
    path = _counts(tmp_path, [_record(query=""), _record()])
    rows = common.counted_rows(path, "procurement")
    assert [common.fetchable(r) for r in rows] == [False, True]


def test_window_words_uses_largest_pass_for_family(tmp_path):
    toml = tmp_path / "passes.toml"
    toml.write_text(
        '[[pass]]\nname = "a"\nfamily = "jobs"\n'
        "prefilter_keep = 1.0\ntokens_per_item = 300\n"
        '[[pass]]\nname = "b"\nfamily = "jobs"\n'
        "prefilter_keep = 1.0\ntokens_per_item = 200\n"
        '[[pass]]\nname = "c"\nfamily = "hn"\n'
        "prefilter_keep = 1.0\ntokens_per_item = 190\n"
    )
    # 300 tokens at 1.33 tokens/word -> 225 words; smaller pass must not win.
    assert common.window_words(toml, "jobs") == 225
    assert common.window_words(toml, "hn") == 142
    # No pass for the family: stated default of 400 tokens -> 300 words.
    assert common.window_words(toml, "unknown-family") == 300


def test_item_id_prefers_source_id_and_hashes_url():
    item = SourceItem("abc-1", "https://x.test/a", "text")
    assert common.item_id("ted", item) == "ted:abc-1"
    page = SourceItem("", "https://x.test/b", "text")
    iid = common.item_id("seek-au", page)
    assert iid.startswith("seek-au:")
    assert "https" not in iid


def test_collect_items_dedupes_windows_and_writes_raw(tmp_path):
    raw = tmp_path / "raw" / "jobs"
    produced = iter(
        [
            common.Produced(
                SourceItem("a1", "https://x.test/1", "one two three four"),
                "src", "US", "cat", "q1",
            ),
            common.Produced(
                SourceItem("a1", "https://x.test/2", "dup by id"),
                "src", "US", "cat", "q1",
            ),
            common.Produced(
                SourceItem("zz", "https://x.test/1", "dup by url"),
                "src", "US", "cat", "q2",
            ),
            common.Produced(
                SourceItem("", "", "no id no url"),
                "src", "US", "cat", "q2",
            ),
            common.Produced(
                SourceItem("b1", "https://x.test/3", "five six"),
                "src", "US", "cat2", "q2",
            ),
        ]
    )
    rows = common.collect_items(
        "jobs", produced, raw_dir=raw, max_words=3, fetched_at="T0"
    )
    assert [r.item_id for r in rows] == ["src:a1", "src:b1"]
    first = rows[0]
    assert (first.family, first.source, first.region) == ("jobs", "src", "US")
    assert first.category_hint == "cat"
    assert first.url == "https://x.test/1"
    assert first.fetched_at == "T0"
    assert first.text_sha256 == hashlib.sha256(b"one two three").hexdigest()
    written = json.loads(
        (raw / f"{common.safe_name('src:a1')}.json").read_text()
    )
    assert written == {
        "item_id": "src:a1",
        "source": "src",
        "url": "https://x.test/1",
        "query": "q1",
        "fetched_at": "T0",
        "text": "one two three",
    }


def test_collect_items_skips_empty_text(tmp_path):
    produced = iter(
        [common.Produced(SourceItem("e1", "https://x.test/e", "  "), "s", "US", "c", "q")]
    )
    rows = common.collect_items(
        "jobs", produced, raw_dir=tmp_path / "raw",
        max_words=5, fetched_at="T",
    )
    assert rows == []


def test_append_items_creates_and_upserts(tmp_path):
    out = tmp_path / "items.parquet"
    row = common.ItemRow(
        "src:a1", "jobs", "src", "US", "cat", "https://x/1", "T0", "sha0"
    )
    common.append_items([row], out)
    newer = common.ItemRow(
        "src:a1", "jobs", "src", "US", "cat", "https://x/1", "T1", "sha1"
    )
    other = common.ItemRow(
        "src:b2", "jobs", "src", "SG", "cat", "https://x/2", "T1", "sha2"
    )
    common.append_items([newer, other], out)
    rows = pq.read_table(out).to_pylist()
    assert len(rows) == 2
    by_id = {r["item_id"]: r for r in rows}
    assert by_id["src:a1"]["fetched_at"] == "T1"
    assert by_id["src:a1"]["text_sha256"] == "sha1"
    assert by_id["src:b2"]["region"] == "SG"
    assert list(rows[0]) == [
        "item_id", "family", "source", "region",
        "category_hint", "url", "fetched_at", "text_sha256",
    ]
    assert asdict(newer) == by_id["src:a1"]
