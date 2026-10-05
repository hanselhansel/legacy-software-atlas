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
min_awards = 3
min_reviews = 2
min_apps = 2
min_cases = 2
failure_yes = 0.7
s3_strong = 5
s3_weak = 3
s3_other = 1

[ai_fit]
[ai_fit.share_weights]
high = 3.0
medium = 2.0
low = 1.0

[lockin]
min_awards = 3
min_cases = 2
noncompetitive = ["negotiated_no_competition", "direct"]
regulator_true = 5
regulator_false = 1

[crowding]
traction_status = "traction"
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
                "ai_native",
                "status",
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
                    "ai_native": "True",
                    "status": "traction",
                }
            ]
        )
    with open(r / "replacement_cases.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "category",
                "buyer",
                "region",
                "system_from",
                "system_to",
                "start_year",
                "end_year",
                "duration_months",
                "cost_usd",
                "outcome",
                "source",
            ],
        )
        w.writeheader()
        w.writerows(
            [
                {
                    "category": "core-banking",
                    "duration_months": "30",
                    "outcome": "cancelled_or_rolled_back",
                },
                {
                    "category": "core-banking",
                    "duration_months": "20",
                    "outcome": "completed_on_time",
                },
            ]
        )
    with open(r / "regulator_approval.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["category", "regulator_approval_required", "note"],
        )
        w.writeheader()
        w.writerows(
            [
                {
                    "category": "core-banking",
                    "regulator_approval_required": "True",
                    "note": "license required",
                }
            ]
        )
    with open(r / "ai_native_rounds_24m.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "category",
                "company",
                "hq",
                "date",
                "amount_usd",
                "round",
                "workflow_id",
                "source",
            ],
        )
        w.writeheader()
        w.writerows(
            [
                {
                    "category": "core-banking",
                    "company": "Ch1",
                    "amount_usd": "10000000",
                    "workflow_id": "core-banking:wf_a",
                }
            ]
        )
    with open(r / "workflows.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "category",
                "workflow_id",
                "workflow",
                "description",
                "touches_core",
            ],
        )
        w.writeheader()
        w.writerows(
            [
                {
                    "category": "core-banking",
                    "workflow_id": "core-banking:wf_a",
                    "workflow": "Reconciliation",
                    "description": "match ledgers",
                    "touches_core": "False",
                },
                {
                    "category": "core-banking",
                    "workflow_id": "core-banking:wf_core",
                    "workflow": "Posting",
                    "description": "post to the ledger",
                    "touches_core": "True",
                },
            ]
        )
    with open(r / "buyer_universe.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "category",
                "region",
                "register",
                "approx_count",
                "source",
                "seg_enterprise",
                "seg_mid_market",
                "seg_smb",
                "seg_government",
            ],
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
                    "seg_enterprise": "0.5",
                    "seg_mid_market": "0.5",
                },
                {
                    "category": "core-banking",
                    "region": "UK",
                    "register": "reg-uk",
                    "approx_count": "100",
                    "source": "https://uk",
                    "seg_enterprise": "1.0",
                },
            ]
        )
    with open(r / "criticality.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "category",
                "criticality",
                "criticality_why",
                "best_icp",
                "segment",
                "build_in_house",
                "spend_low",
                "spend_high",
                "evidence",
                "sources",
            ],
        )
        w.writeheader()
        w.writerows(
            [
                {
                    "category": "core-banking",
                    "criticality": "critical",
                    "criticality_why": "runs the ledger",
                    "best_icp": "mid_market",
                    "segment": "enterprise",
                    "build_in_house": "common",
                    "spend_low": "100000",
                    "spend_high": "200000",
                    "evidence": "bank IT budgets",
                    "sources": "https://a; https://b",
                },
                {
                    "category": "core-banking",
                    "criticality": "critical",
                    "criticality_why": "runs the ledger",
                    "best_icp": "mid_market",
                    "segment": "mid_market",
                    "build_in_house": "rare",
                    "spend_low": "20000",
                    "spend_high": "40000",
                    "evidence": "smaller budgets",
                    "sources": "https://c",
                },
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
        dict(
            ITEM_SCHEMA,
            item_id="rev:1",
            family="app_reviews",
            url="https://example.test/rev/1",
        ),
        dict(
            ITEM_SCHEMA,
            item_id="rev:2",
            family="app_reviews",
            url="https://example.test/rev/2",
        ),
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


_ANSWER_SCHEMA = pa.schema(
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
)


def _ans_row(item_id, question_set, question_id, choice=None, probability=None, score=None):
    return {
        "run_id": "test",
        "item_id": item_id,
        "question_set": question_set,
        "question_id": question_id,
        "qtype": "choice",
        "probability": probability,
        "choice": choice,
        "score": score,
        "probabilities_json": "{}",
        "confidence": 0.9,
        "model_returned": "test",
        "request_id": "r",
        "logical_call_id": "l",
    }


def _jev_root(tmp_path: Path) -> Path:
    """v2 job answers (in_use, enterprise) plus the lane O award and
    app-review pass answers."""
    qs = "job-apis-industry-segment-legacy-in-use@v2"
    rows = []
    for item_id in ("x:1", "x:2"):
        for qid, choice in (
            ("legacy_in_use", "in_use"),
            ("segment", "enterprise"),
        ):
            rows.append(_ans_row(item_id, qs, qid, choice=choice))
    answers_dir = (
        tmp_path
        / "jev"
        / "job-apis-industry-segment-legacy-in-use"
        / "answers"
    )
    answers_dir.mkdir(parents=True)
    pq.write_table(
        pa.Table.from_pylist(rows, schema=_ANSWER_SCHEMA),
        answers_dir / "part-000.parquet",
    )

    awards_qs = "awards-keep-alive-or-replace@v1"
    award_rows = []
    actions = {"aw:1": "maintain", "aw:2": "extend", "aw:3": "replace", "aw:4": "maintain"}
    for aid, action in actions.items():
        award_rows.append(
            _ans_row(aid, awards_qs, "action", choice=action)
        )
        award_rows.append(
            _ans_row(aid, awards_qs, "category", choice="core-banking")
        )
    adir = tmp_path / "jev" / "awards-keep-alive-or-replace" / "answers"
    adir.mkdir(parents=True)
    pq.write_table(
        pa.Table.from_pylist(award_rows, schema=_ANSWER_SCHEMA),
        adir / "part-000.parquet",
    )

    reviews_qs = "app-reviews-backend-failure@v1"
    review_rows = [
        _ans_row("rev:1", reviews_qs, "backend_failure", probability=0.9),
        _ans_row("rev:2", reviews_qs, "backend_failure", probability=0.2),
    ]
    rdir = tmp_path / "jev" / "app-reviews-backend-failure" / "answers"
    rdir.mkdir(parents=True)
    pq.write_table(
        pa.Table.from_pylist(review_rows, schema=_ANSWER_SCHEMA),
        rdir / "part-000.parquet",
    )
    return tmp_path / "jev"


def _derived_dir(tmp_path: Path) -> Path:
    d = tmp_path / "derived"
    d.mkdir()
    pq.write_table(
        pa.Table.from_pylist(
            [
                {
                    "award_id": "aw:1",
                    "duration_months": 12.0,
                    "procedure": "open",
                },
                {
                    "award_id": "aw:2",
                    "duration_months": 24.0,
                    "procedure": "direct",
                },
                {
                    "award_id": "aw:3",
                    "duration_months": 48.0,
                    "procedure": "negotiated_no_competition",
                },
                {
                    "award_id": "aw:4",
                    "duration_months": 36.0,
                    "procedure": "restricted",
                },
            ]
        ),
        d / "awards.parquet",
    )
    pq.write_table(
        pa.Table.from_pylist(
            [
                {"category": "core-banking", "apple_id": "1", "rating": 2.0, "status": "ok"},
                {"category": "core-banking", "apple_id": "1", "rating": 4.0, "status": "ok"},
                {"category": "core-banking", "apple_id": "2", "rating": 3.0, "status": "ok"},
            ]
        ),
        d / "apps.parquet",
    )
    return d


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
        derived_dir=_derived_dir(tmp_path),
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

    # Lane O parts: one kept category -> every ranked sub-score is quintile 1.
    pain_subs = sco["parts"]["pain"]["detail"]["sub_scores"]
    assert set(pain_subs) == {
        "keep_alive_share",
        "backend_failure_share",
        "app_rating_inverted",
        "failed_rate",
        "s3_grade",
    }
    assert pain_subs["s3_grade"] == {"raw": "weak", "n": 1, "score": 3}
    assert pain_subs["keep_alive_share"]["raw"] == 0.75  # 3 keep / 4 counted
    assert pain_subs["failed_rate"] == {"raw": 0.5, "n": 2, "score": 1}
    # pain = round(mean(1, 1, 1, 1, 3)) = 1
    assert sco["parts"]["pain"]["score"] == 1
    assert sco["parts"]["pain"]["detail"]["mean"] == 1.4

    lockin_subs = sco["parts"]["lockin"]["detail"]["sub_scores"]
    assert set(lockin_subs) == {
        "award_duration_months",
        "noncompetitive_share",
        "replacement_duration_months",
        "regulator_approval",
    }
    assert lockin_subs["regulator_approval"] == {
        "raw": True, "n": 1, "score": 5
    }
    assert lockin_subs["award_duration_months"]["raw"] == 30.0
    assert lockin_subs["noncompetitive_share"]["raw"] == 0.5
    assert lockin_subs["replacement_duration_months"]["raw"] == 25.0
    # lockin = round(mean(1, 1, 1, 5)) = 2
    assert sco["parts"]["lockin"]["score"] == 2

    crowd_subs = sco["parts"]["crowding"]["detail"]["sub_scores"]
    assert set(crowd_subs) == {
        "ai_native_traction",
        "funding_per_billion",
        "yc_2024_plus",
    }
    assert crowd_subs["ai_native_traction"]["raw"] == 1.0
    # no market_size.csv in the fixture -> funding cannot be normalized
    assert crowd_subs["funding_per_billion"]["score"] is None
    # no yc-category pass -> no data
    assert crowd_subs["yc_2024_plus"]["score"] is None
    assert sco["parts"]["crowding"]["score"] == 1
    assert 0 <= sco["total"] <= 100

    assert len(scores_list) == 1
    assert scores_list[0]["slug"] == "core-banking"
    assert scores_list[0]["flags"] == sco["flags"]

    # workflows.json: sorted by opportunity index desc; wf_a has the round
    # crowding, wf_core carries the touches_core penalty; they tie at -1.
    wf_path = result["workflows"]
    assert wf_path.name == "workflows.json"
    wf = json.loads(wf_path.read_text())
    assert [w["workflow_id"] for w in wf] == [
        "core-banking:wf_a",
        "core-banking:wf_core",
    ]
    assert wf[0]["crowding"] == 1
    assert wf[1]["crowding"] == 0
    assert wf[0]["pain"] == 1  # category pain part score
    assert wf[0]["touches_core"] is False
    assert wf[1]["touches_core"] is True
    idx = [w["opportunity_index"] for w in wf]
    assert idx == sorted(idx, reverse=True)

    # market value: US 4500 buyers x (0.5x150k + 0.5x30k) + UK 100 x 150k
    mk = cat["market"]
    assert mk["basis"] == "market_value"
    assert mk["buyers_mid"] == 4600
    assert mk["value_mid_usd"] == 395_979_797  # geometric-mean spend midpoints
    assert mk["value_low_usd"] == 250_000_000
    assert mk["value_high_usd"] == 620_000_000
    assert sco["parts"]["size"]["detail"]["basis"] == "market_value"
    assert sco["parts"]["size"]["score"] == 2  # 420M >= 100M bin

    lens = cat["build_vs_buy"]
    assert lens["criticality"] == "critical"
    assert lens["best_icp"] == "mid_market"
    assert lens["segments"]["enterprise"]["build_in_house"] == "common"
    assert lens["segments"]["enterprise"]["buyable"] is False
    assert lens["segments"]["enterprise"]["buyers"] == 2350
    assert lens["segments"]["mid_market"]["buyable"] is True
    # only mid_market is buyable: 4500 x 0.5 x 30k
    assert lens["buyable_value_usd"] == 63_639_610  # geometric-mean spend midpoints

    regions = json.loads(result["regions"].read_text())["regions"]
    assert regions["US"]["categories"]["core-banking"]["evidence"] == "usage"
    uk = regions["UK"]["categories"]["core-banking"]
    assert uk["evidence"] == "buyers only"
    assert uk["buyers"]["mid"] == 100
    assert regions["EU"]["categories"]["core-banking"]["evidence"] == "none"
    assert regions["US"]["summary"] == {
        "categories_with_usage": 1,
        "categories_with_buyers": 1,
        "total_value_usd": 381_837_662,
    }

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
        derived_dir=tmp_path / "derived",
    )
    assert "multiplier = 10.0" in cfg.read_text()
    cats = json.loads(
        (tmp_path / "out" / "site" / "categories.json").read_text()
    )
    # multiplier 10: high = min(5000, 120*10) = 1200
    assert cats[0]["estimates"]["regions"]["US"]["companies_high"] == 1200
