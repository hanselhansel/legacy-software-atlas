import httpx

from lsa.workflows_labour import net, onet

CSV = """O*NET-SOC Code,Title,Task ID,Task,Task Type,Incumbents Responding,Date,Domain Source
43-4051.00,Customer Service Representatives,101,"Confer with customers by telephone or in person.",Core,10,08/2023,Incumbent
43-4051.00,Customer Service Representatives,102,"Keep records of customer interactions.",Core,10,08/2023,Incumbent
13-2011.00,Accountants and Auditors,201,"Review accounts for discrepancies and reconcile differences.",Core,9,08/2023,Incumbent
13-2011.00,Accountants and Auditors,202,"Prepare adjusting journal entries.",Core,9,08/2023,Incumbent
"""


def _tasks(tmp_path):
    path = tmp_path / "task_statements.csv"
    path.write_text(CSV)
    return onet.load_tasks(path)


def test_load_tasks_parses_csv(tmp_path):
    tasks = _tasks(tmp_path)
    assert len(tasks) == 4
    t = tasks[0]
    assert (t.soc, t.onet_soc, t.task_id) == ("43-4051", "43-4051.00", "101")
    assert t.norm == "confer with customers by telephone or in person"


def test_soc_base_and_split():
    assert onet.soc_base("13-2099.04") == "13-2099"
    assert onet.soc_base("43-4051") == "43-4051"
    assert onet.split_tasks("Do a thing. | Do another. |") == [
        "Do a thing.",
        "Do another.",
    ]


def test_match_exact_normalized_overlap_and_unmatched(tmp_path):
    tasks = _tasks(tmp_path)
    rows = [
        {
            "workflow_id": "wf1",
            "soc_code": "43-4051",
            "onet_tasks": (
                "Confer with customers by telephone or in person."
                " | keep records of customer interactions"
                " | Telephone or otherwise confer with all customers in person."
                " | Knit sweaters for penguins."
            ),
        }
    ]
    m = onet.match_tasks(rows, tasks)
    assert [x.quality for x in m] == [
        "exact",
        "normalized",
        "overlap",
        "unmatched",
    ]
    assert m[0].task_id == "101"
    assert m[1].task_id == "102"
    assert m[2].task_id == "101"
    assert 0 < m[2].score < 1
    assert m[3].task_id is None


def test_normalized_match_stays_within_soc(tmp_path):
    tasks = _tasks(tmp_path)
    # "Review accounts..." exists under 13-2011 but not 43-4051; the
    # casing change defeats the global exact match, and normalised and
    # overlap matching only see same-SOC candidates.
    rows = [
        {
            "workflow_id": "wf1",
            "soc_code": "43-4051",
            "onet_tasks": "review accounts for discrepancies and reconcile differences.",
        }
    ]
    (m,) = onet.match_tasks(rows, tasks)
    assert m.quality == "unmatched"
    assert m.task_id is None


def test_exact_match_can_cross_soc(tmp_path):
    tasks = _tasks(tmp_path)
    # Same raw text listed under a different soc still exact-matches.
    tasks.append(
        onet.OnetTask(
            "99-9999", "99-9999.00", "999",
            "Confer with customers by telephone or in person.",
            "", frozenset(),
        )
    )
    rows = [
        {
            "workflow_id": "wf1",
            "soc_code": "43-4051",
            "onet_tasks": "Confer with customers by telephone or in person.",
        }
    ]
    (m,) = onet.match_tasks(rows, tasks)
    assert m.quality == "exact"
    assert m.task_id == "101"  # same-SOC hit preferred


def test_task_file_uses_cache(tmp_path):
    raw = tmp_path / "onet"
    raw.mkdir()
    dest = raw / "task_statements.csv"
    dest.write_text(CSV)
    assert onet.task_file(raw) == dest


def test_task_file_downloads_first_working_url(tmp_path):
    raw = tmp_path / "onet"
    seen = []

    def handler(request):
        seen.append(request.url.path)
        if "db_31_0" in request.url.path:
            return httpx.Response(200, text=CSV)
        return httpx.Response(404)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    out = onet.task_file(raw, client=client)
    assert out == raw / "task_statements.csv"
    assert out.read_text() == CSV
    assert any("task_statements.csv" in p for p in seen)


def test_task_file_returns_none_when_all_fail(tmp_path):
    def handler(request):
        return httpx.Response(404)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    assert onet.task_file(tmp_path / "onet", client=client) is None


def test_download_discards_partial_file(tmp_path):
    dest = tmp_path / "x.bin"

    def handler(request):
        return httpx.Response(500)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    try:
        net.download(client, "https://example.test/x", dest)
        assert False, "expected raise"
    except httpx.HTTPStatusError:
        pass
    assert not dest.exists()
    assert not (tmp_path / "x.bin.part").exists()
