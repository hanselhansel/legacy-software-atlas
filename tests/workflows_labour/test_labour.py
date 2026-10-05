import pyarrow.parquet as pq
import pytest

from lsa.workflows_labour import labour, oews, onet

WORKFLOWS = [
    {
        "category": "cat-a",
        "workflow_id": "cat-a:wf1",
        "workflow": "WF one",
        "description": "d",
        "touches_core": "False",
    },
    {
        "category": "cat-a",
        "workflow_id": "cat-a:wf2",
        "workflow": "WF two",
        "description": "d",
        "touches_core": "False",
    },
]

OCCS = [
    {"workflow_id": "cat-a:wf1", "soc_code": "43-4051", "title": "CSR",
     "time_share": "0.5",
     "onet_tasks": "Confer with customers. | Keep records."},
    {"workflow_id": "cat-a:wf1", "soc_code": "13-2011", "title": "Acct",
     "time_share": "0.25",
     "onet_tasks": "Review accounts. | Keep records."},
    {"workflow_id": "cat-a:wf2", "soc_code": "99-9999", "title": "Nope",
     "time_share": "1.0",
     "onet_tasks": "Fly to the moon."},
]

MATCHES = [
    onet.TaskMatch("cat-a:wf1", "43-4051", "Confer with customers.", "1", "exact", 1.0),
    onet.TaskMatch("cat-a:wf1", "43-4051", "Keep records.", "2", "exact", 1.0),
    onet.TaskMatch("cat-a:wf1", "13-2011", "Review accounts.", "3", "normalized", 1.0),
    onet.TaskMatch("cat-a:wf1", "13-2011", "Keep records.", None, "unmatched", 0.2),
    onet.TaskMatch("cat-a:wf2", "99-9999", "Fly to the moon.", None, "unmatched", None),
]

WAGES = {
    "434051": oews.OewsRow(
        "434051", employment=1000.0, annual_mean_wage=50000.0,
        emp_soc="434051", wage_soc="434051",
    ),
    "132011": oews.OewsRow(
        "132011", employment=2000.0, annual_mean_wage=60000.0,
        emp_soc="132010", wage_soc="132011",
    ),
}

USAGE = {"1": 0.2, "3": 0.4}


def test_workflow_rows_maths_and_notes():
    rows = labour.workflow_rows(WORKFLOWS, OCCS, MATCHES, WAGES, USAGE)
    assert len(rows) == 2
    r1, r2 = rows

    assert r1["labour_value_usd"] == 1000 * 50000 * 0.5 + 2000 * 60000 * 0.25
    assert r1["employment_share_sum"] == 1000 * 0.5 + 2000 * 0.25
    # tasks 1, 2, 3 matched; shares only for 1 and 3 (0.2, 0.4)
    assert r1["ai_usage"] == pytest.approx(0.3)
    assert r1["n_tasks"] == 3  # distinct texts; "Keep records." dedupes
    assert r1["n_tasks_matched"] == 3  # matched under any listing counts
    assert "13-2011 via broad 13-2010" in r1["notes"]

    assert r2["labour_value_usd"] is None
    assert r2["ai_usage"] is None
    assert r2["n_tasks"] == 1
    assert r2["n_tasks_matched"] == 0
    assert "99-9999 no oews" in r2["notes"]
    assert "1/1 tasks unmatched" in r2["notes"]


def test_workflow_rows_global_notes_and_null_share():
    rows = labour.workflow_rows(
        WORKFLOWS, OCCS, MATCHES, WAGES, {"1": None, "2": None, "3": None},
        global_notes=["ai usage file unavailable"],
    )
    assert rows[0]["ai_usage"] is None
    assert "ai usage file unavailable" in rows[0]["notes"]


def test_write_parquet_round_trip(tmp_path):
    rows = labour.workflow_rows(WORKFLOWS, OCCS, MATCHES, WAGES, USAGE)
    out = labour.write_parquet(rows, tmp_path / "workflows.parquet")
    back = pq.read_table(out).to_pylist()
    assert [r["workflow_id"] for r in back] == ["cat-a:wf1", "cat-a:wf2"]
    assert back[0]["region"] == "US"
    assert back[0]["category"] == "cat-a"
    assert back[0]["n_tasks"] == 3
    assert back[1]["labour_value_usd"] is None
