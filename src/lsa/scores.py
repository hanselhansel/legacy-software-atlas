"""Five-part opportunity scores per category (plan 3, lane O).

The parts and their evidence are exactly ``configs/rubric.toml`` (spec
section 8): size is market value (buyer-universe buyers x segment spend
from ``research/criticality.csv``, binned on ``value_bins_usd``) and falls
back to the buyer-count midpoint on ``buyer_bins`` when a category has no
spend data; ai_fit is the share-weighted mean of the ``tasks-ai-fit`` Jev
pass over ``research/tasks.csv``. Pain, lock-in and crowding are the lane O
means of sub-scores computed by ``lsa.measures``: each sub-score is a raw
measurement ranked across the categories into quintiles 1..5 (or a direct
score for the S3 grade and regulator approval), and the part is the
rounded mean of the available sub-scores (half up, like ``ai_fit``) with
every sub-score, its raw value and its input count in the detail.

Every part scores 1 to 5. The opportunity total is the weighted
``size + pain + ai_fit - lockin - crowding`` rescaled to 0..100 over the
range the present parts can reach. When the ``tasks-ai-fit`` pass is
missing, ``ai_fit`` is None, the total is computed without it and the
score carries the ``ai_fit_missing`` flag.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from lsa import estimates, market, measures
from lsa.rubric import Rubric, load_rubric
from lsa.score_inputs import AI_FIT_PASS, ScoreInputs

AI_FIT_FLAG = "ai_fit_missing"


@dataclass(frozen=True)
class ScorePart:
    score: int | None
    detail: dict
    evidence: tuple[str, ...]


@dataclass(frozen=True)
class CategoryScore:
    slug: str
    parts: dict[str, ScorePart]
    total_raw: float
    total: float
    flags: tuple[str, ...] = ()


def size_part(
    estimate: estimates.CategoryEstimate,
    rubric: Rubric,
    universe_mid: float | None = None,
    market_view: market.MarketValue | None = None,
) -> ScorePart:
    """Market value: buyers x segment spend, binned on ``value_bins_usd``.

    ``market_view`` comes from ``market.market_value``. When the category
    has no spend data the score falls back to the buyer-universe midpoint
    (or the companies-using midpoint) binned on ``buyer_bins``, the old
    behaviour.
    """
    users_mid = estimate.midpoint()
    detail: dict = {"users_midpoint": users_mid}
    if market_view is not None and market_view.has_spend:
        mid = market_view.value_mid
        bins = rubric.value_bins_usd
        detail["basis"] = "market_value"
        detail["buyers_mid"] = market_view.buyers_mid
        detail["value_usd"] = {
            "low": market_view.value_low,
            "mid": market_view.value_mid,
            "high": market_view.value_high,
        }
        evidence = [
            (
                f"market value ${mid:,.0f} mid "
                f"({market_view.buyers_mid:g} buyers x segment spend)"
            )
        ]
    else:
        mid = universe_mid if universe_mid else users_mid
        bins = rubric.buyer_bins
        detail["basis"] = (
            "buyer_universe" if universe_mid else "companies_using"
        )
        evidence = [
            f"possible buyers {mid:g} (buyer universe)" if universe_mid
            else f"estimates: region midpoints sum to {mid:g} companies using"
        ]
        if market_view is not None:
            evidence.append("no spend data; buyer-count bins used")
    detail["midpoint"] = mid
    detail["bins"] = list(bins)
    if market_view is not None and market_view.notes:
        detail["notes"] = list(market_view.notes)
    score = 1 + sum(1 for b in bins if mid >= b)
    for region, s in estimate.regions.items():
        evidence.append(
            f"{region}: {s.companies_low}-{s.companies_high} grade {s.grade}"
        )
        evidence.extend(s.sources)
    return ScorePart(score, detail, tuple(evidence))


def measure_part(subs: list[measures.SubScore] | None) -> ScorePart:
    """Round-half-up mean of available sub-scores for one lane O part.

    The detail lists every sub-score with its raw value, input count ``n``
    and quintile (None when the sub-score had no usable data); ``mean``
    is the unrounded mean of the available scores. Evidence is one line
    per sub-score that contributed. ``int(mean + 0.5)`` matches the
    round-half-up convention ``ai_fit_part`` uses.
    """
    subs = subs or []
    detail: dict = {
        "sub_scores": {
            s.name: {"raw": s.raw, "n": s.n, "score": s.score}
            for s in subs
        }
    }
    available = [s for s in subs if s.score is not None]
    if not available:
        detail["status"] = "no sub-scores with data"
        return ScorePart(None, detail, ())
    mean = sum(s.score for s in available) / len(available)
    detail["mean"] = mean
    evidence = [
        f"{s.name}: raw {s.raw} (n={s.n}) -> {s.score}"
        for s in available
    ]
    return ScorePart(int(mean + 0.5), detail, tuple(evidence))


def ai_fit_part(
    tasks: list[dict],
    answers: dict[str, dict],
    slug: str,
    rubric: Rubric,
    *,
    pass_present: bool,
) -> ScorePart:
    """Share-weighted mean Jev score over the category's tasks, rounded.

    ``tasks`` are research/tasks.csv rows (category, task, share);
    ``answers`` maps task item ids to their ``ai_fit`` answer row. A task
    answers when its id is ``task:<slug>:<slugified task>``, ``<slug>:<task>``
    or the bare task text; unanswerable ids are noted.
    """
    rows = [t for t in tasks if t.get("category") == slug]
    ev = [f"jev pass {AI_FIT_PASS}: question ai_fit, research/tasks.csv"]
    if not pass_present or not rows:
        reason = (
            "pass missing" if not pass_present else "no tasks for category"
        )
        return ScorePart(
            None, {"status": reason, "tasks": len(rows)}, tuple(ev)
        )

    def cand(task: str, t: dict) -> list[str]:
        slugified = re.sub(r"[^a-z0-9]+", "-", task.lower()).strip("-")
        return [
            str(t.get("task_id", "")),
            f"task:{slug}:{slugified}",
            f"{slug}:{task}",
            task,
        ]

    num = den = 0.0
    missing: list[str] = []
    for t in rows:
        row = next(
            (answers[c] for c in cand(t.get("task", ""), t) if c in answers),
            None,
        )
        if row is None or row.get("score") is None:
            missing.append(t.get("task", ""))
            continue
        w = rubric.share_weights.get(str(t.get("share", "")).lower(), 1.0)
        # Jev returns the score on a 0..4 scale (docs/reports/jev-audit.md); shift to 1..5.
        num += (float(row["score"]) + AI_FIT_SCORE_OFFSET) * w
        den += w
    if den == 0:
        return ScorePart(
            None,
            {"status": "no answered tasks", "tasks": len(rows)},
            tuple(ev),
        )
    mean = num / den
    score = max(1, min(5, int(mean + 0.5)))
    return ScorePart(
        score,
        {
            "mean": mean,
            "answered": len(rows) - len(missing),
            "unanswered": missing,
            "tasks": len(rows),
        },
        tuple(ev),
    )


def combine(
    parts: dict[str, ScorePart], weights: dict[str, float]
) -> tuple[float, float, tuple[str, ...]]:
    """Weighted total rescaled to 0..100 over the present parts' range."""
    flags: list[str] = []
    present = [
        p for p in ("size", "pain", "ai_fit", "lockin", "crowding")
        if parts[p].score is not None
    ]
    if "ai_fit" not in present:
        flags.append(AI_FIT_FLAG)
    w = {p: weights.get(p, 1.0) for p in present}
    raw = (
        w.get("size", 0) * (parts["size"].score or 0)
        + w.get("pain", 0) * (parts["pain"].score or 0)
        + w.get("ai_fit", 0) * (parts["ai_fit"].score or 0)
        - w.get("lockin", 0) * (parts["lockin"].score or 0)
        - w.get("crowding", 0) * (parts["crowding"].score or 0)
    )
    lo = (
        w.get("size", 0) + w.get("pain", 0) + w.get("ai_fit", 0)
        - 5 * w.get("lockin", 0) - 5 * w.get("crowding", 0)
    )
    hi = (
        5 * w.get("size", 0) + 5 * w.get("pain", 0) + 5 * w.get("ai_fit", 0)
        - w.get("lockin", 0) - w.get("crowding", 0)
    )
    scaled = 0.0 if hi == lo else 100.0 * (raw - lo) / (hi - lo)
    return raw, round(scaled, 1), tuple(flags)


AI_FIT_SCORE_OFFSET = 1.0


def score_category(
    slug: str, inp: ScoreInputs, rubric: Rubric | None = None
) -> CategoryScore:
    """All five parts plus the rescaled opportunity total."""
    rubric = rubric or load_rubric()
    subs = inp.measures or {}
    parts = {
        "size": size_part(
            inp.estimate, rubric, inp.universe_mid, inp.market
        ),
        "pain": measure_part(subs.get("pain")),
        "ai_fit": ai_fit_part(
            inp.tasks, inp.ai_answers, slug, rubric,
            pass_present=inp.ai_pass_present,
        ),
        "lockin": measure_part(subs.get("lockin")),
        "crowding": measure_part(subs.get("crowding")),
    }
    raw, scaled, flags = combine(parts, rubric.weights)
    return CategoryScore(
        slug=slug, parts=parts, total_raw=raw, total=scaled, flags=flags
    )
