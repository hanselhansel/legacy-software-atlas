import pytest

from lsa import estimates, labels, scores
from lsa.rubric import Rubric

RUBRIC = Rubric(
    weights={"size": 1.0, "pain": 1.0, "ai_fit": 1.0, "lockin": 1.0, "crowding": 1.0},
    value_bins_usd=(100e6, 1e9, 5e9, 20e9),
    buyer_bins=(100.0, 1000.0, 10000.0, 100000.0),
    s3_strong=2.0,
    s3_weak=1.0,
    hn_pain_min_comments=5,
    legacy_in_use_share=0.30,
    share_weights={"high": 3.0, "medium": 2.0, "low": 1.0},
    s2_strong=2.0,
    s2_weak=1.0,
    s4_strong=1.0,
    regulation_reason=1.0,
    count_bins=(2.0, 5.0, 9.0),
    funding_usd_over=500_000_000.0,
)


def _est(midpoints):
    regions = {
        f"r{i}": estimates.SliceEstimate(
            key=f"r{i}",
            companies_low=low,
            companies_high=high,
            grade="C",
            families=(),
            notes=(),
            sources=(),
        )
        for i, (low, high) in enumerate(midpoints)
    }
    return estimates.CategoryEstimate(
        slug="x", regions=regions, segments={}, notes=()
    )


@pytest.mark.parametrize(
    "mid,score",
    [(0, 1), (99, 1), (100, 2), (999, 2), (1000, 3), (9999, 3),
     (10000, 4), (99999, 4), (100000, 5), (10**9, 5)],
)
def test_size_bins(mid, score):
    est = _est([(mid, mid)])
    assert scores.size_part(est, RUBRIC).score == score


def test_size_sums_regions():
    est = _est([(100, 200), (300, 400)])  # midpoints 150 + 350 = 500
    assert scores.size_part(est, RUBRIC).score == 2
    assert scores.size_part(est, RUBRIC).detail["midpoint"] == 500


@pytest.mark.parametrize(
    "s3,hn,share,expected",
    [
        ("not_met", 0, 0.0, 1),
        ("weak", 0, 0.0, 2),
        ("strong", 0, 0.0, 3),
        ("not_met", 5, 0.0, 2),
        ("not_met", 4, 0.0, 1),
        ("not_met", 0, 0.30, 2),
        ("not_met", 0, 0.29, 1),
        ("strong", 5, 0.5, 5),
        ("strong", 4, 0.29, 3),
        ("weak", 5, 0.30, 4),
        ("not_met", 100, 0.9, 3),  # capped
    ],
)
def test_pain_rules(s3, hn, share, expected):
    part = scores.pain_part(s3, hn, share, share, RUBRIC)
    assert part.score == expected


def test_pain_no_share_data():
    part = scores.pain_part("weak", 0, None, None, RUBRIC)
    assert part.score == 2


@pytest.mark.parametrize(
    "s2,s4,reasons,expected",
    [
        ("not_met", "not_met", [], 1),
        ("weak", "not_met", [], 2),
        ("strong", "not_met", [], 3),
        ("not_met", "strong", [], 2),
        ("not_met", "not_met", ["Regulators require certified systems"], 2),
        ("strong", "strong", ["regulation demands it", "cost"], 5),
        ("strong", "strong", [], 4),
        ("not_met", "not_met", ["certification is mandatory"], 2),
        ("not_met", "not_met", ["expensive to leave"], 1),
    ],
)
def test_lockin_rules(s2, s4, reasons, expected):
    part = scores.lockin_part(
        s2, s4, reasons, ("regulat", "certif"), RUBRIC
    )
    assert part.score == expected


def test_lockin_pattern_config():
    part = scores.lockin_part(
        "not_met", "not_met", ["audit requirements bind"], ("audit",), RUBRIC
    )
    assert part.score == 2


def _challenger(company, funding="", source="https://example.test/c"):
    return {
        "category": "x",
        "company": company,
        "founded": "2020",
        "hq": "nowhere",
        "funding_usd": funding,
        "strategy": "overlay",
        "traction": "some",
        "source": source,
    }


@pytest.mark.parametrize(
    "n,funding_each,expected",
    [
        (0, "", 1),
        (1, "", 1),
        (2, "", 2),
        (4, "", 2),
        (5, "", 3),
        (8, "", 3),
        (9, "", 4),
        (12, "", 4),
        (1, "$600M", 2),   # 1 challenger + funding bonus
        (8, "$600M", 4),
        (9, "$600M", 5),
    ],
)
def test_crowding_bins_and_funding(n, funding_each, expected):
    rows = [
        _challenger(f"c{i}", funding_each) for i in range(n)
    ]
    part = scores.crowding_part(rows, {}, (), RUBRIC)
    assert part.score == expected


def test_crowding_funding_threshold_and_overrides():
    rows = [_challenger("a", "$400M"), _challenger("b", "undisclosed")]
    part = scores.crowding_part(rows, {}, (), RUBRIC)
    assert part.detail["funding_usd"] == 400e6
    assert part.score == 2  # 2 challengers, funding under 500M
    part = scores.crowding_part(
        rows, {"b": 200e6}, (), RUBRIC
    )
    assert part.detail["funding_usd"] == 600e6
    assert part.score == 3
    part = scores.crowding_part(rows + [_challenger("c", "$10M")], {}, ("c",), RUBRIC)
    assert part.detail["challengers"] == 2


def test_ai_fit_weighted_mean():
    tasks = [
        {"category": "x", "task": "a", "share": "high"},
        {"category": "x", "task": "b", "share": "low"},
        {"category": "x", "task": "c", "share": "medium"},
    ]
    answers = {
        "task:x:a": {"score": 4, "question_id": "ai_fit"},
        "x:b": {"score": 0, "question_id": "ai_fit"},
        "task:x:c": {"score": 2, "question_id": "ai_fit"},
    }
    # Jev scores are 0..4 and shift by +1: (5*3 + 1*1 + 3*2) / (3+1+2) = 22/6 = 3.667 -> 4
    part = scores.ai_fit_part(tasks, answers, "x", RUBRIC, pass_present=True)
    assert part.score == 4
    assert part.detail["mean"] == pytest.approx(22 / 6)


def test_ai_fit_matches_task_id_column():
    tasks = [{"category": "x", "task_id": "task:x:00", "task": "a", "share": "high"}]
    answers = {"task:x:00": {"score": 3.4, "question_id": "ai_fit"}}
    part = scores.ai_fit_part(tasks, answers, "x", RUBRIC, pass_present=True)
    assert part.score == 4


def test_ai_fit_missing_pass():
    part = scores.ai_fit_part([], {}, "x", RUBRIC, pass_present=False)
    assert part.score is None


def test_combine_with_and_without_ai_fit():
    def part(s):
        return scores.ScorePart(s, {}, ())
    parts = {
        "size": part(5), "pain": part(5), "ai_fit": part(5),
        "lockin": part(1), "crowding": part(1),
    }
    raw, scaled, flags = scores.combine(parts, RUBRIC.weights)
    assert raw == 13
    assert scaled == 100.0
    parts["ai_fit"] = part(None)
    raw, scaled, flags = scores.combine(parts, RUBRIC.weights)
    # present parts: size+pain-lockin-crowding = 8; range -8..8 -> 100
    assert scaled == 100.0
    assert flags == (scores.AI_FIT_FLAG,)
    parts["size"] = part(1)
    raw, scaled, flags = scores.combine(parts, RUBRIC.weights)
    # 1+5-1-1 = 4 over -8..8 -> 75
    assert raw == 4
    assert scaled == 75.0


def test_combine_weights():
    def part(s):
        return scores.ScorePart(s, {}, ())
    parts = {
        "size": part(5), "pain": part(1), "ai_fit": part(None),
        "lockin": part(1), "crowding": part(1),
    }
    w = {"size": 2.0, "pain": 1.0, "ai_fit": 1.0, "lockin": 1.0, "crowding": 1.0}
    raw, scaled, _ = scores.combine(parts, w)
    # raw = 2*5 + 1 - 1 - 1 = 9; lo = 2*1+1 -5 -5 = -7; hi = 10+5 -1 -1 = 13
    assert raw == 9
    assert scaled == pytest.approx(100 * (9 + 7) / 20, abs=0.15)


def test_job_in_use_share_and_hn_count():
    items = [
        labels.LabelledItem(
            item_id="j1", family="jobs", url="u", weight=2.0, region="SG",
            category="x", segment="smb", industry=None, status="in_use",
            pain=None, reason=None,
        ),
        labels.LabelledItem(
            item_id="j2", family="jobs-pages", url="u", weight=1.0,
            region="VN", category="x", segment="smb", industry=None,
            status="neither", pain=None, reason=None,
        ),
        labels.LabelledItem(
            item_id="h1", family="hn", url="u", weight=1.0, region="US",
            category="x", segment=None, industry=None, status=None,
            pain=0.8, reason=None,
        ),
        labels.LabelledItem(
            item_id="h2", family="hn", url="u", weight=1.0, region="US",
            category="x", segment=None, industry=None, status=None,
            pain=0.69, reason=None,
        ),
        labels.LabelledItem(
            item_id="h3", family="hn", url="u", weight=1.0, region="US",
            category="y", segment=None, industry=None, status=None,
            pain=0.9, reason=None,
        ),
    ]
    w, u = scores.job_in_use_share(items, "x")
    assert w == pytest.approx(2 / 3)
    assert u == pytest.approx(1 / 2)
    assert scores.hn_pain_comments(items, "x") == 1
