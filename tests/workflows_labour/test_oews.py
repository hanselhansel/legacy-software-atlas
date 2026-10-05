import json

import httpx

from lsa.workflows_labour import oews


def _api_client(payloads):
    """MockTransport returning canned v2 bodies for each POST chunk."""

    def handler(request):
        body = json.loads(request.content)
        out = {"status": "REQUEST_SUCCEEDED", "message": [], "Results": {"series": []}}
        for sid in body["seriesid"]:
            value = payloads.get(sid)
            data = (
                [{"year": "2025", "period": "A01", "value": str(value), "latest": "true"}]
                if value is not None
                else []
            )
            out["Results"]["series"].append({"seriesID": sid, "data": data})
        return httpx.Response(200, json=out)

    return httpx.Client(transport=httpx.MockTransport(handler))


def test_soc6_and_candidates():
    assert oews.soc6("13-2099.04") == "132099"
    assert oews.soc6("13-1021") == "131021"
    assert oews.candidates("13-1021") == ["131021", "131020", "131000", "130000"]
    assert oews.candidates("43-4000") == ["434000", "430000"]
    assert oews.candidates("13-0000") == ["130000"]
    assert oews.candidates("xx") == []


def test_series_id_format():
    sid = oews.series_id("131021", oews.EMPLOYMENT)
    assert sid == "OEUN000000000000013102101"
    assert len(sid) == 25


def test_level_name():
    assert oews.level_name("131021", "131021") == "exact"
    assert oews.level_name("131021", "131020") == "broad"
    assert oews.level_name("131021", "131000") == "minor"
    assert oews.level_name("131021", "130000") == "major"


def test_fetch_values_batches_and_caches(tmp_path):
    payloads = {
        oews.series_id("131021", "01"): 491430,
        oews.series_id("131021", "04"): 83770,
    }
    client = _api_client(payloads)
    cache = tmp_path / "api.json"
    series = list(payloads) + [oews.series_id("999999", "01")]
    vals = oews.fetch_values(series, client, cache)
    assert vals[oews.series_id("131021", "01")] == 491430.0
    assert vals[oews.series_id("131021", "04")] == 83770.0
    assert vals[oews.series_id("999999", "01")] is None
    assert cache.exists()

    def boom(request):
        raise AssertionError("cache should have answered")

    dead = httpx.Client(transport=httpx.MockTransport(boom))
    again = oews.fetch_values(series, dead, cache)
    assert again[oews.series_id("131021", "01")] == 491430.0


def test_wages_for_resolves_broad_group(tmp_path):
    payloads = {
        # exact 13-1021 missing; broad 13-1020 answers
        oews.series_id("131020", "01"): 491430,
        oews.series_id("131020", "04"): 83770,
        # 43-4051 answers at exact level
        oews.series_id("434051", "01"): 2800000,
        oews.series_id("434051", "04"): 45000,
    }
    client = _api_client(payloads)
    rows = oews.wages_for(
        {"13-1021", "43-4051"}, client, tmp_path / "api.json"
    )
    r = rows["131021"]
    assert r.employment == 491430.0 and r.annual_mean_wage == 83770.0
    assert r.emp_soc == "131020"
    assert oews.level_name("131021", r.emp_soc) == "broad"
    r2 = rows["434051"]
    assert r2.emp_soc == "434051"
    assert r2.annual_mean_wage == 45000.0


def test_wages_for_marks_missing(tmp_path):
    client = _api_client({})
    rows = oews.wages_for({"13-1021"}, client, tmp_path / "api.json")
    r = rows["131021"]
    assert r.employment is None and r.annual_mean_wage is None
    assert r.emp_soc is None


def test_wages_for_partial_per_datatype(tmp_path):
    # employment exact, wage only at broad level
    payloads = {
        oews.series_id("131021", "01"): 100,
        oews.series_id("131020", "04"): 70000,
    }
    client = _api_client(payloads)
    rows = oews.wages_for({"13-1021"}, client, tmp_path / "api.json")
    r = rows["131021"]
    assert r.employment == 100.0
    assert r.emp_soc == "131021"
    assert r.annual_mean_wage == 70000.0
    assert r.wage_soc == "131020"
