import httpx

from lsa.workflows_labour import aiuse

SIBLINGS = [
    "README.md",
    "labor_market_impacts/job_exposure.csv",
    "labor_market_impacts/task_penetration.csv",
    "release_2025_02_10/onet_task_statements.csv",
    "release_2025_02_10/onet_task_mappings.csv",
    "release_2025_09_15/data/input/task_pct_v1.csv",
    "release_2025_09_15/data/input/task_pct_v2.csv",
    "release_2025_03_27/automation_vs_augmentation_by_task.csv",
]


def test_choose_file_prefers_task_penetration():
    assert (
        aiuse.choose_file(SIBLINGS)
        == "labor_market_impacts/task_penetration.csv"
    )


def test_choose_file_falls_back_to_task_pct():
    names = [n for n in SIBLINGS if "penetration" not in n]
    pick = aiuse.choose_file(names)
    assert pick is not None
    assert "task_pct" in pick
    assert "v2" in pick or "v1" in pick


def test_choose_file_none_without_usage_files():
    assert aiuse.choose_file(["README.md", "x/onet_task_statements.csv"]) is None


def test_usage_shares_normalizes_and_dedupes(tmp_path):
    path = tmp_path / "task_penetration.csv"
    path.write_text(
        "task,penetration\n"
        '"Keep records of customer interactions.",0.42\n'
        '"keep records of customer interactions",0.5\n'
        "Unparseable row,\n"
        "Do a thing.,not-a-number\n"
    )
    shares = aiuse.usage_shares(path)
    assert shares == {"keep records of customer interactions": 0.5}


def test_usage_shares_rejects_bad_columns(tmp_path):
    path = tmp_path / "x.csv"
    path.write_text("foo,bar\n1,2\n")
    try:
        aiuse.usage_shares(path)
        assert False, "expected ValueError"
    except ValueError:
        pass


def _client(search_ids, files):
    def handler(request):
        url = str(request.url)
        if "datasets?search" in url:
            return httpx.Response(
                200, json=[{"id": i} for i in search_ids]
            )
        if "/api/datasets/" in url:
            return httpx.Response(
                200, json={"siblings": [{"rfilename": f} for f in files]}
            )
        if "/resolve/" in url:
            return httpx.Response(
                200, text="task,penetration\nDo a thing.,0.1\n"
            )
        return httpx.Response(404)

    return httpx.Client(transport=httpx.MockTransport(handler))


def test_usage_file_discovers_and_downloads(tmp_path):
    client = _client(["other/EconomicIndex", "Anthropic/EconomicIndex"], SIBLINGS)
    out = aiuse.usage_file(tmp_path / "aiuse", client=client)
    assert out is not None
    assert out.name == "task_penetration.csv"
    assert out.exists()
    # second call serves the cache
    assert aiuse.usage_file(tmp_path / "aiuse", client=client) == out


def test_usage_file_none_when_repo_missing(tmp_path):
    client = _client(["someone/unrelated"], [])
    assert aiuse.usage_file(tmp_path / "aiuse", client=client) is None
