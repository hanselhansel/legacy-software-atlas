"""The runner reads raw text from the file names the fetchers write."""

import json

import pyarrow as pa
import pyarrow.parquet as pq

from lsa.fetch.common import safe_name
from lsa.jev.items import load_items


def test_load_items_reads_fetcher_file_names(tmp_path):
    item_id = "hn-snapshot:9000000001"
    pq.write_table(
        pa.Table.from_pylist([{"item_id": item_id, "family": "hn", "source": "hn-snapshot"}]),
        tmp_path / "items.parquet",
    )
    raw = tmp_path / "raw" / "hn"
    raw.mkdir(parents=True)
    (raw / f"{safe_name(item_id)}.json").write_text(json.dumps({"item_id": item_id, "text": "synthetic"}))
    items = load_items("hn", tmp_path / "items.parquet", tmp_path / "raw")
    assert [i["text"] for i in items] == ["synthetic"]
