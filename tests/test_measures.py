import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from lsa import measures

TH = measures.Thresholds(
    pain_min_awards=3,
    min_reviews=3,
    min_apps=2,
    min_cases=2,
    failure_yes=0.7,
    lockin_min_awards=3,
)


def _ans(item_id, **q):
    return item_id, q


def test_keep_alive_share():
    answers = dict(
        [
            _ans("a1", action={"choice": "maintain"}, category={"choice": "x"}),
            _ans("a2", action={"choice": "extend"}, category={"choice": "x"}),
            _ans("a3", action={"choice": "replace"}, category={"choice": "x"}),
            _ans("a4", action={"choice": "consult"}, category={"choice": "x"}),
            _ans("b1", action={"choice": "maintain"}, category={"choice": "y"}),
            _ans("b2", action={"choice": "extend"}, category={"choice": "y"}),
            _ans("u1", action={"choice": "maintain"}, category={"choice": "unclear"}),
            _ans("n1", action={"choice": "maintain"}),  # no category answer
        ]
    )
    out = measures.keep_alive_shares(answers)
    assert out["x"] == (pytest.approx(2 / 3), 3)
    assert out["y"] == (1.0, 2)
    assert "unclear" not in out and "n1" not in "".join(out)


def test_backend_failure_share_threshold_and_min():
    cats = {f"r{i}": "x" for i in range(4)} | {"r9": "y"}
    answers = {
        "r0": {"backend_failure": {"probability": 0.8}},
        "r1": {"backend_failure": {"probability": 0.7}},   # boundary = yes
        "r2": {"backend_failure": {"probability": 0.69}},
        "r3": {"backend_failure": {"probability": None}},  # skipped
        "r9": {"backend_failure": {"probability": 0.9}},
    }
    out = measures.backend_failure_shares(cats, answers, TH)
    assert out["x"] == (pytest.approx(2 / 3), 3)
    assert out["y"] == (1.0, 1)
    # min applied downstream in collect; raw layer returns all shares


def _app_row(cat, apple_id, rating, status="ok"):
    return {
        "category": cat,
        "apple_id": apple_id,
        "rating": rating,
        "status": status,
    }


def test_app_rating_means_per_app():
    apps = [
        _app_row("x", "1", 4.0),
        _app_row("x", "1", 3.0),   # second storefront, same app
        _app_row("x", "2", 5.0),
        _app_row("x", "3", None),          # unrated, skipped
        _app_row("x", "4", 1.0, "error"),  # failed lookup, skipped
    ]
    out = measures.app_rating_means(apps)
    # per-app means: app1 -> 3.5, app2 -> 5.0; category mean 4.25 over 2 apps
    assert out["x"] == (pytest.approx(4.25), 2)


def test_failed_rate_and_replacement_duration():
    cases = [
        {"category": "x", "outcome": "cancelled_or_rolled_back", "duration_months": "30"},
        {"category": "x", "outcome": "completed_late_or_over", "duration_months": "48"},
        {"category": "x", "outcome": "completed_on_time", "duration_months": "18"},
        {"category": "x", "outcome": "ongoing", "duration_months": ""},
        {"category": "y", "outcome": "cancelled_or_rolled_back", "duration_months": ""},
    ]
    rate = measures.failed_rates(cases)
    assert rate["x"] == (0.5, 4)
    assert rate["y"] == (1.0, 1)
    dur = measures.replacement_durations(cases)
    assert dur["x"] == (30.0, 3)   # median of 18, 30, 48
    assert "y" not in dur          # no non-empty durations


def test_s3_and_regulator_direct_scores():
    assert measures.s3_score("strong", TH) == 5
    assert measures.s3_score("weak", TH) == 3
    assert measures.s3_score("not_met", TH) == 1
    assert measures.s3_score("surprise", TH) == 1
    assert measures.regulator_score(True, TH) == 5
    assert measures.regulator_score(False, TH) == 1


def test_award_duration_and_noncompetitive():
    awards = [
        {"award_id": "a1", "duration_months": 12.0, "procedure": "open"},
        {"award_id": "a2", "duration_months": 24.0, "procedure": "direct"},
        {"award_id": "a3", "duration_months": 60.0, "procedure": "negotiated_no_competition"},
        {"award_id": "a4", "duration_months": None, "procedure": "unknown"},
        {"award_id": "a5", "duration_months": 36.0, "procedure": "restricted"},
    ]
    answers = {
        i: {"category": {"choice": "x"}}
        for i in ("a1", "a2", "a3", "a4", "a5")
    }
    dur = measures.award_durations(awards, answers)
    assert dur["x"] == (30.0, 4)  # median of 12,24,36,60
    nc = measures.noncompetitive_shares(awards, answers, TH)
    assert nc["x"] == (0.5, 4)    # 2 noncompetitive over 4 known procedures
    # an award with no category answer never joins
    out = measures.award_durations(awards, {"a1": {"category": {"choice": "x"}}})
    assert out["x"] == (12.0, 1)


def test_traction_counts():
    rows = {
        "x": [
            {"company": "c1", "ai_native": "True", "status": "traction"},
            {"company": "c2", "ai_native": "True", "status": "early"},
            {"company": "c3", "ai_native": "False", "status": "traction"},
            {"company": "c4", "ai_native": "True", "status": "traction"},
        ],
        "y": [],
    }
    out = measures.traction_counts(rows, TH)
    assert out["x"] == (2.0, 2)
    assert out["y"] == (0.0, 0)


def test_funding_per_billion():
    rounds = [
        {"category": "x", "amount_usd": "20000000"},
        {"category": "x", "amount_usd": ""},
        {"category": "x", "amount_usd": "10000000"},
        {"category": "y", "amount_usd": "5000000"},
    ]
    mids = {"x": 2.0e9, "y": 0.0, "w": 5e8}
    out = measures.funding_per_billion(rounds, mids)
    assert out["x"] == (pytest.approx(15.0e6), 3)  # $30M / $2B legacy
    assert out["y"][0] is None                   # no legacy midpoint
    assert out["y"][1] == 1
    assert out["w"] == (0.0, 0)   # midpoint but no rounds -> real zero
    assert "z" not in out         # no midpoint and no rounds -> absent


def test_yc_counts():
    answers = {
        "yc:1": {"category": {"choice": "x"}},
        "yc:2": {"category": {"choice": "x"}},
        "yc:3": {"category": {"choice": "y"}},
        "yc:4": {"category": {"choice": "none"}},
    }
    out = measures.yc_counts(answers)
    assert out["x"] == (2.0, 2)
    assert out["y"] == (1.0, 1)
    assert "none" not in out


def test_quintiles_spread_and_ties():
    raws = {f"c{i}": float(i) for i in range(10)}  # 0..9
    q = measures.quintiles(raws)
    assert q["c0"] == 1 and q["c9"] == 5
    # n=10: count_less 0,1 -> 1; 2,3 -> 2; 4,5 -> 3; 6,7 -> 4; 8,9 -> 5
    assert [q[f"c{i}"] for i in range(10)] == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]


def test_quintiles_ties_share_lower():
    # tie group at count_less 2 straddles the 1/2 boundary; all get 1
    raws = {"a": 1.0, "b": 2.0, "c": 2.0, "d": 3.0, "e": 4.0}
    q = measures.quintiles(raws)
    assert q["b"] == q["c"]
    assert q["b"] == 1 + (5 * 1) // 5


def test_quintiles_all_tied_get_one_and_none_passthrough():
    q = measures.quintiles({"a": 1.0, "b": 1.0, "c": None})
    assert q == {"a": 1, "b": 1, "c": None}


def test_quintiles_invert():
    # n=3: the lowest rating is most painful; 1+5*2//3 = 4 (a 3-point
    # sample cannot fill all five quintiles)
    q = measures.quintiles({"low": 1.0, "high": 9.0, "mid": 5.0}, invert=True)
    assert q["low"] == 4 and q["mid"] == 2 and q["high"] == 1


def test_load_pass_answers(tmp_path):
    adir = tmp_path / "jev" / "yc-category" / "answers"
    adir.mkdir(parents=True)
    rows = [
        {
            "item_id": "yc:1",
            "question_set": "yc-category@v1",
            "question_id": "category",
            "choice": "core-banking",
        },
        {
            "item_id": "yc:1",
            "question_set": "other-set@v9",
            "question_id": "category",
            "choice": "x",
        },
    ]
    pq.write_table(pa.Table.from_pylist(rows), adir / "part-1.parquet")
    out = measures.load_pass_answers(tmp_path / "jev", measures.YC_SET)
    assert out["yc:1"]["category"]["choice"] == "core-banking"
    assert len(out["yc:1"]) == 1   # the other-set row is filtered out
    assert measures.load_pass_answers(tmp_path / "jev", "nope@v1") is None


def test_collect_assembles_parts(tmp_path):
    data = measures.MeasureData(
        s3={"x": "weak"},
        regulator={"x": True},
        challengers={
            "x": [{"company": "c", "ai_native": "True", "status": "traction"}]
        },
        rounds=[],
        legacy_mid={"x": 1e9},
        yc_answers={"yc:1": {"category": {"choice": "x"}}},
    )
    out = measures.collect(["x", "y"], data, TH)
    pain = {s.name: s for s in out["x"]["pain"]}
    assert pain["s3_grade"].score == 3
    assert pain["s3_grade"].raw == "weak"
    assert pain["keep_alive_share"].score is None   # no awards pass data
    lockin = {s.name: s for s in out["x"]["lockin"]}
    assert lockin["regulator_approval"].score == 5
    crowd = {s.name: s for s in out["x"]["crowding"]}
    assert crowd["ai_native_traction"].score == 3   # x=1 > y=0, n=2 -> 3
    assert crowd["yc_2024_plus"].score == 3
    assert crowd["funding_per_billion"].score == 1  # x=0 rounds, mid exists
    crowd_y = {s.name: s for s in out["y"]["crowding"]}
    # challengers source exists, so y having no rows is a real zero
    assert crowd_y["ai_native_traction"].score == 1
    assert crowd_y["funding_per_billion"].score is None  # no mid for y
    # min counts: 1 award-borne data point is below pain_min_awards
    data2 = measures.MeasureData(
        award_answers={
            "a1": {"action": {"choice": "maintain"}, "category": {"choice": "x"}}
        },
        s3={},
    )
    out2 = measures.collect(["x"], data2, TH)
    ka = {s.name: s for s in out2["x"]["pain"]}["keep_alive_share"]
    assert ka.score is None and ka.n == 1 and ka.raw is None
    s3x = {s.name: s for s in out2["x"]["pain"]}["s3_grade"]
    assert s3x.score is None   # no s3 row for x -> no data
