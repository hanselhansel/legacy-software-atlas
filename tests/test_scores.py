import pytest

from lsa import estimates, measures, score_inputs, scores
from lsa.rubric import Rubric

RUBRIC = Rubric(
    weights={"size": 1.0, "pain": 1.0, "ai_fit": 1.0, "lockin": 1.0, "crowding": 1.0},
    value_bins_usd=(100e6, 1e9, 5e9, 20e9),
    buyer_bins=(100.0, 1000.0, 10000.0, 100000.0),
    share_weights={"high": 3.0, "medium": 2.0, "low": 1.0},
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


def _sub(name, score, raw=None, n=0):
    return measures.SubScore(name=name, raw=raw, n=n, score=score)


def test_measure_part_rounds_mean_of_available():
    subs = [
        _sub("a", 4, 0.6, 12),
        _sub("b", 2, 0.4, 60),
        _sub("c", None),           # no data, excluded from the mean
        _sub("d", 3, "weak", 1),
    ]
    part = scores.measure_part(subs)
    assert part.detail["mean"] == pytest.approx(3.0)
    assert part.score == 3


def test_measure_part_rounds_half_up():
    subs = [_sub("a", 4, 1.0, 1), _sub("b", 3, 2.0, 1)]
    assert scores.measure_part(subs).score == 4  # 3.5 -> 4
    subs = [_sub("a", 4, 1.0, 1), _sub("b", 1, 2.0, 1)]
    assert scores.measure_part(subs).score == 3  # 2.5 -> 3 (half up)


def test_measure_part_detail_lists_every_sub_score():
    subs = [
        _sub("keep_alive_share", 4, 0.6, 12),
        _sub("s3_grade", 3, "weak", 1),
        _sub("failed_rate", None, 0.5, 2),
    ]
    detail = scores.measure_part(subs).detail["sub_scores"]
    assert detail["keep_alive_share"] == {"raw": 0.6, "n": 12, "score": 4}
    assert detail["s3_grade"] == {"raw": "weak", "n": 1, "score": 3}
    assert detail["failed_rate"] == {"raw": 0.5, "n": 2, "score": None}
    # sub-scores with data contribute an evidence line
    part = scores.measure_part(subs)
    assert len(part.evidence) == 2
    assert "keep_alive_share" in part.evidence[0]


def test_measure_part_no_data_is_none():
    part = scores.measure_part([_sub("a", None), _sub("b", None)])
    assert part.score is None
    assert part.detail["status"] == "no sub-scores with data"
    assert scores.measure_part(None).score is None
    assert scores.measure_part([]).score is None


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


def test_score_category_uses_sub_scores():
    subs = {
        "pain": [_sub("s3_grade", 5, "strong", 1)],
        "lockin": [_sub("regulator_approval", 1, False, 1)],
        "crowding": [_sub("ai_native_traction", 3, 2.0, 2)],
    }
    inp = score_inputs.ScoreInputs(estimate=_est([(100, 100)]), measures=subs)
    sc = scores.score_category("x", inp, RUBRIC)
    assert sc.parts["pain"].score == 5
    assert sc.parts["lockin"].score == 1
    assert sc.parts["crowding"].score == 3
    assert sc.parts["ai_fit"].score is None
    assert "ai_fit_missing" in sc.flags
    # raw = size 2 + pain 5 + lockin -1 - crowding 3 = 3
    assert sc.total_raw == 3
