import csv
import json
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from lsa import export

RUBRIC_TOML = """
[weights]
size = 1.0
pain = 1.0
ai_fit = 1.0
lockin = 1.0
crowding = 1.0

[size]
value_bins_usd = [100000000, 1000000000, 5000000000, 20000000000]
buyer_bins = [100, 1000, 10000, 100000]

[pain]
s3_strong = 2.0
s3_weak = 1.0
hn_pain_min_comments = 5
legacy_in_use_share = 0.30

[ai_fit]
[ai_fit.share_weights]
high = 3.0
medium = 2.0
low = 1.0

[lockin]
s2_strong = 2.0
s2_weak = 1.0
s4_strong = 1.0
regulation_reason = 1.0

[crowding]
count_bins = [2, 5, 9]
funding_usd_over = 500000000
"""

ITEM_SCHEMA = {
    "item_id": "x:1",
    "family": "jobs",
    "source": "job-api",
    "region": "US",
    "category_hint": "core-banking",
    "url": "https://example.test/job/1",
    "fetched_at": "2026-10-05T00:00:00Z",
    "text_sha256": "abc",
    "query_count": 10,
    "sampled": 5,
}


def _research_dir(tmp_path: Path) -> Path:
    r = tmp_path / "research"
    (r / "raw").mkdir(parents=True)
    cats = [
        {
            "slug": "core-banking",
            "name": "Core banking",
            "s1": "strong",
            "s2": "strong",
            "s3": "weak",
            "s4": "strong",
            "strong": "2",
            "weak": "1",
            "legacy_score": "3.5",
            "kept": "True",
            "reason": "kept",
            "differentiator": "diff",
        },
        {
            "slug": "dropped",
            "name": "Dropped",
            "s1": "weak",
            "s2": "not_met",
            "s3": "not_met",
            "s4": "not_met",
            "strong": "0",
            "weak": "1",
            "legacy_score": "0.5",
            "kept": "False",
            "reason": "thin",
            "differentiator": "",
        },
    ]
    with open(r / "categories.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(cats[0]))
        w.writeheader()
        w.writerows(cats)
    desk = {
        "categories": [
            {
                "slug": "core-banking",
                "name": "Core banking",
                "systems": ["Sys A", "Sys B"],
                "vendors": [],
                "s1_pre_cloud_core": {"met": True, "evidence": "x"},
                "s2_slow_to_replace": {"met": True, "evidence": "x"},
                "s3_workarounds": {"met": False, "evidence": "x"},
                "s4_shrinking_skills": {"met": True, "evidence": "x"},
                "buyer_universe": [],
                "segments": "text",
                "reasons_to_stay": [
                    "Regulators require certified cores",
                    "Migration risk is existential",
                ],
                "search_terms": [],
                "challengers": [],
                "notes": "",
                "check": {},
            }
        ],
        "sources": [],
        "gaps": [],
    }
    (r / "raw" / export.DESK).write_text(json.dumps(desk))
    regrade = [
        {
            "slug": "core-banking",
            "s1": {"grade": "strong", "why": "why1", "source": "https://a"},
            "s2": {"grade": "strong", "why": "why2", "source": "https://b"},
            "s3": {"grade": "weak", "why": "why3", "source": "https://c"},
            "s4": {"grade": "strong", "why": "why4", "source": "https://d"},
        }
    ]
    (r / "raw" / export.REGRADE).write_text(json.dumps(regrade))
    with open(r / "challengers.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "category",
                "company",
                "founded",
                "hq",
                "funding_usd",
                "strategy",
                "traction",
                "source",
            ],
        )
        w.writeheader()
        w.writerows(
            [
                {
                    "category": "core-banking",
                    "company": "Ch1",
                    "founded": "2020",
                    "hq": "SG",
                    "funding_usd": "$10M",
                    "strategy": "overlay",
                    "traction": "t",
                    "source": "https://e",
                }
            ]
        )
    with open(r / "buyer_universe.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["category", "region", "register", "approx_count", "source"],
        )
        w.writeheader()
        w.writerows(
            [
                {
                    "category": "core-banking",
                    "region": "US",
                    "register": "reg",
                    "approx_count": "4,000 to 5,000",
                    "source": "https://f",
                }
            ]
        )
    with open(r / "vendors.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "category",
                "vendor",
                "product",
                "first_shipped",
                "disclosed_customers",
                "regions",
                "source",
            ],
        )
        w.writeheader()
        w.writerows(
            [
                {
                    "category": "core-banking",
                    "vendor": "V",
                    "product": "P",
                    "first_shipped": "1980",
                    "disclosed_customers": "120 banks (FY2025)",
                    "regions": "US",
                    "source": "https://g",
                }
            ]
        )
    return r


def _items_parquet(tmp_path: Path) -> Path:
    rows = [
        dict(ITEM_SCHEMA),
        dict(ITEM_SCHEMA, item_id="x:2", url="https://example.test/job/2"),
    ]
    path = tmp_path / "items.parquet"
    pq.write_table(
        pa.Table.from_pylist(
            rows,
            schema=pa.schema(
                [
                    ("item_id", pa.string()),
                    ("family", pa.string()),
                    ("source", pa.string()),
                    ("region", pa.string()),
                    ("category_hint", pa.string()),
                    ("url", pa.string()),
                    ("fetched_at", pa.string()),
                    ("text_sha256", pa.string()),
                    ("query_count", pa.int64()),
                    ("sampled", pa.int64()),
                ]
            ),
        ),
        path,
    )
    return path


def _jev_root(tmp_path: Path) -> Path:
    """Two v2 job answers marking both items in_use, segment enterprise."""
    answers_dir = (
        tmp_path
        / "jev"
        / "job-apis-industry-segment-legacy-in-use"
        / "answers"
    )
    answers_dir.mkdir(parents=True)
    qs = "job-apis-industry-segment-legacy-in-use@v2"
    rows = []
    for item_id in ("x:1", "x:2"):
        for qid, choice in (
            ("legacy_in_use", "in_use"),
            ("segment", "enterprise"),
        ):
            rows.append(
                {
                    "run_id": "test",
                    "item_id": item_id,
                    "question_set": qs,
                    "question_id": qid,
                    "qtype": "choice",
                    "probability": None,
                    "choice": choice,
                    "score": None,
                    "probabilities_json": "{}",
                    "confidence": 0.9,
                    "model_returned": "test",
                    "request_id": "r",
                    "logical_call_id": "l",
                }
            )
    pq.write_table(
        pa.Table.from_pylist(
            rows,
            schema=pa.schema(
                [
                    ("run_id", pa.string()),
                    ("item_id", pa.string()),
                    ("question_set", pa.string()),
                    ("question_id", pa.string()),
                    ("qtype", pa.string()),
                    ("probability", pa.float64()),
                    ("choice", pa.string()),
                    ("score", pa.float64()),
                    ("probabilities_json", pa.string()),
                    ("confidence", pa.float64()),
                    ("model_returned", pa.string()),
                    ("request_id", pa.string()),
                    ("logical_call_id", pa.string()),
                ]
            ),
        ),
        answers_dir / "part-000.parquet",
    )
    return tmp_path / "jev"


def test_export_shape(tmp_path):
    research = _research_dir(tmp_path)
    items = _items_parquet(tmp_path)
    rubric = tmp_path / "rubric.toml"
    rubric.write_text(RUBRIC_TOML)
    configs = tmp_path / "configs"
    out = tmp_path / "exports"

    result = export.run_export(
        out,
        research_dir=research,
        configs_dir=configs,
        rubric_path=rubric,
        items_path=items,
        jev_root=_jev_root(tmp_path),
    )

    cat_path = result["categories"]
    sco_path = result["scores"]
    assert cat_path.name == "categories.json"
    assert cat_path.parent.name == "site"
    cats = json.loads(cat_path.read_text())
    scores_list = json.loads(sco_path.read_text())

    assert len(cats) == 1  # dropped category excluded
    cat = cats[0]
    assert cat["slug"] == "core-banking"
    assert cat["name"] == "Core banking"
    assert cat["systems"] == ["Sys A", "Sys B"]
    assert cat["signs"]["s1"]["grade"] == "strong"
    assert cat["signs"]["s1"]["source"] == "https://a"
    assert cat["signs"]["s3"]["why"] == "why3"
    assert "Regulators require certified cores" in cat["reasons_to_stay"]

    assert cat["regions"] == ["US"]
    us = cat["estimates"]["regions"]["US"]
    assert us["companies_low"] == 120  # max(120 vendor, 2 confirmed)
    assert us["companies_high"] == 360  # min(5000 universe, 120*3)
    assert us["grade"] in ("A", "B", "C")
    assert set(us["families"]) == {
        "buyer_universe",
        "vendor_disclosed",
        "confirmed_signals",
    }
    assert us["notes"]
    assert cat["segments"] == ["enterprise"]
    assert cat["estimates"]["segments"]["enterprise"]["companies_low"] == 2
    assert cat["challengers"][0]["company"] == "Ch1"

    sco = cat["scores"]
    assert set(sco["parts"]) == {
        "size",
        "pain",
        "ai_fit",
        "lockin",
        "crowding",
    }
    for part in sco["parts"].values():
        assert set(part) == {"score", "detail", "evidence"}
    assert sco["parts"]["ai_fit"]["score"] is None
    assert "ai_fit_missing" in sco["flags"]
    # pain: 1 + s3 weak 1 + in-use share 1.0 (>= 0.30) + 0 hn = 3
    assert sco["parts"]["pain"]["score"] == 3
    # lockin: 1 + s2 strong 2 + s4 strong 1 + regulation reason 1 = 5
    assert sco["parts"]["lockin"]["score"] == 5
    # crowding: 1 challenger -> 1
    assert sco["parts"]["crowding"]["score"] == 1
    assert 0 <= sco["total"] <= 100

    assert len(scores_list) == 1
    assert scores_list[0]["slug"] == "core-banking"
    assert scores_list[0]["flags"] == sco["flags"]

    cfg = configs / "core-banking.toml"
    assert cfg.exists()
    assert "multiplier = 3.0" in cfg.read_text()


def test_export_config_not_overwritten(tmp_path):
    research = _research_dir(tmp_path)
    items = _items_parquet(tmp_path)
    rubric = tmp_path / "rubric.toml"
    rubric.write_text(RUBRIC_TOML)
    configs = tmp_path / "configs"
    configs.mkdir()
    cfg = configs / "core-banking.toml"
    cfg.write_text(
        'slug = "core-banking"\n[estimate]\nmultiplier = 10.0\n'
    )
    export.run_export(
        tmp_path / "out",
        research_dir=research,
        configs_dir=configs,
        rubric_path=rubric,
        items_path=items,
        jev_root=tmp_path / "jev",
    )
    assert "multiplier = 10.0" in cfg.read_text()
    cats = json.loads(
        (tmp_path / "out" / "site" / "categories.json").read_text()
    )
    # multiplier 10: high = min(5000, 120*10) = 1200
    assert cats[0]["estimates"]["regions"]["US"]["companies_high"] == 1200
