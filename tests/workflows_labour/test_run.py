import json

import httpx
import pyarrow.parquet as pq
import pytest

from lsa.workflows_labour import labour, oews

ONET_CSV = """O*NET-SOC Code,Title,Task ID,Task,Task Type,Incumbents Responding,Date,Domain Source
43-4051.00,Customer Service Representatives,101,"Confer with customers.",Core,10,08/2023,Incumbent
43-4051.00,Customer Service Representatives,102,"Keep records.",Core,10,08/2023,Incumbent
"""


def _write_inputs(tmp_path):
    wf = tmp_path / "workflows.csv"
    wf.write_text(
        "category,workflow_id,workflow,description,touches_core\n"
        "cat-a,cat-a:wf1,WF one,d,False\n"
    )
    occ = tmp_path / "occupations.csv"
    occ.write_text(
        "workflow_id,soc_code,title,time_share,onet_tasks\n"
        'cat-a:wf1,43-4051,CSR,0.5,"Confer with customers. | Keep records."\n'
    )
    onet_csv = tmp_path / "task_statements.csv"
    onet_csv.write_text(ONET_CSV)
    oews_cache = tmp_path / "api.json"
    oews_cache.write_text(
        json.dumps(
            {
                oews.series_id("434051", oews.EMPLOYMENT): 1000.0,
                oews.series_id("434051", oews.ANNUAL_MEAN_WAGE): 50000.0,
            }
        )
    )
    aiuse_csv = tmp_path / "task_penetration.csv"
    aiuse_csv.write_text(
        "task,penetration\n"
        '"Confer with customers.",0.3\n'
        '"Keep records.",0.1\n'
    )
    return wf, occ, onet_csv, oews_cache, aiuse_csv


def test_run_end_to_end_offline(tmp_path):
    wf, occ, onet_csv, oews_cache, aiuse_csv = _write_inputs(tmp_path)

    def boom(request):
        raise RuntimeError("network must not be touched")

    client = httpx.Client(transport=httpx.MockTransport(boom))
    out = tmp_path / "workflows.parquet"
    rows = labour.run(
        workflows_path=wf,
        occ_path=occ,
        out_path=out,
        raw_dir=tmp_path / "raw",
        onet_path=onet_csv,
        oews_cache=oews_cache,
        aiuse_path=aiuse_csv,
        client=client,
    )
    (r,) = rows
    assert r["labour_value_usd"] == 1000 * 50000 * 0.5
    assert r["employment_share_sum"] == 500.0
    assert r["ai_usage"] == pytest.approx(0.2)
    assert r["n_tasks"] == 2 and r["n_tasks_matched"] == 2
    assert r["region"] == "US"

    back = pq.read_table(out).to_pylist()
    assert len(back) == 1
    assert back[0]["workflow_id"] == "cat-a:wf1"


def test_run_notes_when_sources_missing(tmp_path):
    wf, occ, _o, _c, _a = _write_inputs(tmp_path)

    def boom(request):
        raise RuntimeError("network must not be touched")

    client = httpx.Client(transport=httpx.MockTransport(boom))
    rows = labour.run(
        workflows_path=wf,
        occ_path=occ,
        out_path=tmp_path / "workflows.parquet",
        raw_dir=tmp_path / "raw",
        client=client,
    )
    (r,) = rows
    assert r["labour_value_usd"] is None
    assert r["ai_usage"] is None
    assert r["n_tasks_matched"] == 0
    for want in (
        "onet task file unavailable",
        "oews unavailable",
        "ai usage file unavailable",
        "43-4051 no oews",
    ):
        assert want in r["notes"]
