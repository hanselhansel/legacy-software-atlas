import pyarrow as pa
import pyarrow.parquet as pq

from lsa import workflows


def _wf(wf_id, cat="x", touches="False", name="w"):
    return {
        "workflow_id": wf_id,
        "category": cat,
        "workflow": name,
        "description": "",
        "touches_core": touches,
    }


def test_opportunity_index_ordering():
    rows = [
        _wf("w-low", touches="False"),
        _wf("w-high", touches="False"),
        _wf("w-core", touches="True"),
    ]
    metrics = {
        "w-low": {"labour_value_usd": 100.0, "ai_usage": 0.1},
        "w-high": {"labour_value_usd": 900.0, "ai_usage": 0.9},
        "w-core": {"labour_value_usd": 500.0, "ai_usage": 0.5},
    }
    pain = {"x": 5}
    ai_fit = {"x": None}
    crowd = {"w-core": 3}  # core is also the most crowded
    out = workflows.score_workflows(rows, metrics, crowd, pain, ai_fit)
    # ranks: labour w-high 3, w-core 2, w-low 1; ai the same; pain tied -> 1;
    # crowding: w-low/w-high tied at 0 -> 1, w-core -> 3.
    # base: low 1+1+1-1=2, high 3+3+1-1=6, core 2+2+1-3=2; spread 4.
    # index: low 2, high 6, core 2-4=-2.
    assert [w["workflow_id"] for w in out] == ["w-high", "w-low", "w-core"]
    assert out[0]["opportunity_index"] == 6
    assert out[2]["opportunity_index"] == -2
    assert out[2]["touches_core"] is True


def test_ai_usage_falls_back_to_category_ai_fit():
    rows = [_wf("a"), _wf("b")]
    metrics = {"a": {"labour_value_usd": 10.0, "ai_usage": None}}
    # a's ai_usage is missing -> category ai_fit 4; b has no metric row at
    # all -> same fallback, but b also lacks labour value.
    out = workflows.score_workflows(
        rows, metrics, {}, {"x": 2}, {"x": 4}
    )
    a, b = out
    assert a["workflow_id"] == "a"
    assert a["ai_usage"] == 4
    assert a["ai_source"] == "category"
    assert b["ai_usage"] == 4
    assert b["labour_value_usd"] is None
    assert a["opportunity_index"] > b["opportunity_index"]


def test_missing_pain_and_crowding_rank_zero():
    rows = [_wf("a", cat="ghost")]
    metrics = {"a": {"labour_value_usd": 10.0, "ai_usage": 0.5}}
    out = workflows.score_workflows(rows, metrics, {}, {}, {})
    # only labour and ai contribute (rank 1 each); pain and crowding are 0
    assert out[0]["opportunity_index"] == 1 + 1 + 0 - 1
    assert out[0]["pain"] is None


def test_touches_core_penalty_only_when_true():
    rows = [_wf("core", touches="True"), _wf("edge", touches="False")]
    metrics = {
        "core": {"labour_value_usd": 50.0, "ai_usage": 0.5},
        "edge": {"labour_value_usd": 50.0, "ai_usage": 0.5},
    }
    out = workflows.score_workflows(rows, metrics, {}, {"x": 3}, {"x": None})
    # identical inputs: both base 1+1+1-1=2, spread 0 -> the penalty lands 0
    assert {w["workflow_id"] for w in out} == {"core", "edge"}
    # with unequal spread the core row drops below the edge row
    metrics["edge"]["labour_value_usd"] = 500.0
    out = workflows.score_workflows(rows, metrics, {}, {"x": 3}, {"x": None})
    assert out[-1]["workflow_id"] == "core"


def test_load_metrics_from_parquet(tmp_path):
    p = tmp_path / "workflows.parquet"
    pq.write_table(
        pa.Table.from_pylist(
            [
                {
                    "workflow_id": "w1",
                    "labour_value_usd": 1.5e9,
                    "ai_usage": 0.42,
                },
                {"workflow_id": "w2", "labour_value_usd": None, "ai_usage": 0.0},
                {"workflow_id": None, "labour_value_usd": 5.0, "ai_usage": 1.0},
            ]
        ),
        p,
    )
    out = workflows.load_metrics(p)
    assert out == {
        "w1": {"labour_value_usd": 1.5e9, "ai_usage": 0.42},
        "w2": {"labour_value_usd": None, "ai_usage": 0.0},
    }
    assert workflows.load_metrics(tmp_path / "nope.parquet") == {}


def test_rounds_by_workflow():
    rounds = [
        {"workflow_id": "w1"},
        {"workflow_id": "w1"},
        {"workflow_id": "w2"},
        {"workflow_id": ""},
        {},
    ]
    assert workflows.rounds_by_workflow(rounds) == {"w1": 2, "w2": 1}
