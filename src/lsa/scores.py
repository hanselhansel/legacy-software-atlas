"""Five-part opportunity scores per category (plan 2, task 6).

The parts and their evidence are exactly ``configs/rubric.toml`` (spec
section 8): size from the estimate midpoints summed over regions; pain from
the S3 grade, HN firsthand-pain comments at p >= 0.7 and the weighted share
of job posts showing the legacy system in use; ai_fit the share-weighted
mean of the ``tasks-ai-fit`` Jev pass over ``research/tasks.csv``; lockin
from the S2 and S4 grades plus a regulation/certification reason to stay;
crowding from the challenger count and disclosed funding.

Every part scores 1 to 5. The opportunity total is the weighted
``size + pain + ai_fit - lockin - crowding`` rescaled to 0..100 over the
range the present parts can reach. When the ``tasks-ai-fit`` pass is
missing, ``ai_fit`` is None, the total is computed without it and the
score carries the ``ai_fit_missing`` flag.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path

from lsa import catconfig, estimates, labels, parse_counts, paths
from lsa.rubric import Rubric, load_rubric

AI_FIT_PASS = "tasks-ai-fit"
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


def _cap5(x: float) -> int:
    return max(1, min(5, round(x)))


def size_part(
    estimate: estimates.CategoryEstimate,
    rubric: Rubric,
    universe_mid: float | None = None,
) -> ScorePart:
    """Possible buyers: the buyer-universe midpoint summed over regions, binned.

    Vendor disclosures are too sparse to count users (many name one customer),
    so size measures the organisations a challenger could sell to. Falls back
    to the companies-using midpoint when no universe row exists."""
    users_mid = estimate.midpoint()
    mid = universe_mid if universe_mid else users_mid
    score = 1 + sum(1 for b in rubric.size_bins if mid >= b)
    evidence = [
        f"possible buyers {mid:g} (buyer universe)" if universe_mid
        else f"estimates: region midpoints sum to {mid:g} companies using"
    ]
    for region, s in estimate.regions.items():
        evidence.append(
            f"{region}: {s.companies_low}-{s.companies_high} grade {s.grade}"
        )
        evidence.extend(s.sources)
    return ScorePart(score, {"midpoint": mid, "users_midpoint": users_mid, "basis": "buyer_universe" if universe_mid else "companies_using", "bins": list(rubric.size_bins)}, tuple(evidence))


def pain_part(
    s3: str,
    hn_pain_comments: int,
    in_use_share: float | None,
    labelled_share: float | None,
    rubric: Rubric,
    evidence: list[str] | None = None,
) -> ScorePart:
    """1 + S3 points + HN pain bonus + in-use share bonus, capped at 5."""
    pts = {"strong": rubric.s3_strong, "weak": rubric.s3_weak}.get(s3, 0.0)
    hn_hit = hn_pain_comments >= rubric.hn_pain_min_comments
    share_hit = (
        in_use_share is not None
        and in_use_share >= rubric.legacy_in_use_share
    )
    score = _cap5(1 + pts + hn_hit + share_hit)
    ev = list(evidence or [])
    ev.append(
        f"hn firsthand pain >= {labels.HN_PAIN_YES}: {hn_pain_comments} "
        f"comments (need {rubric.hn_pain_min_comments})"
    )
    ev.append(
        "job posts legacy in use, weighted share "
        f"{in_use_share if in_use_share is not None else 'n/a'} "
        f"(unweighted {labelled_share if labelled_share is not None else 'n/a'}, "
        f"need {rubric.legacy_in_use_share})"
    )
    return ScorePart(
        score,
        {
            "s3": s3,
            "s3_points": pts,
            "hn_pain_comments": hn_pain_comments,
            "in_use_share": in_use_share,
            "in_use_share_unweighted": labelled_share,
        },
        tuple(ev),
    )


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


def lockin_part(
    s2: str,
    s4: str,
    reasons_to_stay: list[str],
    regulation_patterns: tuple[str, ...],
    rubric: Rubric,
    evidence: list[str] | None = None,
) -> ScorePart:
    """1 + S2 points + S4-strong point + regulation reason point, cap 5."""
    pts = {"strong": rubric.s2_strong, "weak": rubric.s2_weak}.get(s2, 0.0)
    s4_hit = s4 == "strong"
    hits = [
        r
        for r in reasons_to_stay
        if any(p.lower() in r.lower() for p in regulation_patterns)
    ]
    reg_hit = bool(hits)
    score = _cap5(
        1 + pts + s4_hit * rubric.s4_strong + reg_hit * rubric.regulation_reason
    )
    ev = list(evidence or [])
    if reg_hit:
        ev.append(f"regulation reason to stay: {hits[0]}")
    return ScorePart(
        score,
        {
            "s2": s2,
            "s2_points": pts,
            "s4": s4,
            "s4_hit": s4_hit,
            "regulation_reason_hit": reg_hit,
        },
        tuple(ev),
    )


def crowding_part(
    rows: list[dict],
    funding_overrides: dict[str, float],
    exclude: tuple[str, ...],
    rubric: Rubric,
) -> ScorePart:
    """Challenger-count bin plus a funding bonus, capped at 5."""
    kept = [
        r
        for r in rows
        if not any(e in r.get("company", "") for e in exclude)
    ]
    n = len(kept)
    score = 1 + sum(1 for b in rubric.count_bins if n >= b)
    parsed: dict[str, float] = {}
    unparsed: list[str] = []
    for r in kept:
        company = r.get("company", "")
        if company in funding_overrides:
            parsed[company] = funding_overrides[company]
            continue
        usd = parse_counts.parse_usd(r.get("funding_usd", ""))
        if usd is None:
            unparsed.append(company)
        else:
            parsed[company] = usd
    funding = sum(parsed.values())
    funded = funding > rubric.funding_usd_over
    score = _cap5(score + funded)
    ev = [r["source"] for r in kept if r.get("source")]
    if unparsed:
        ev.append("funding unparsed: " + ", ".join(unparsed))
    return ScorePart(
        score,
        {
            "challengers": n,
            "funding_usd": funding,
            "funding_over": rubric.funding_usd_over,
            "unparsed": unparsed,
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


def load_task_answers(jev_root: Path | None = None) -> dict[str, dict]:
    """``{item_id: answer row}`` for the ``ai_fit`` question, or {} when the
    pass has not run."""
    import pyarrow.parquet as pq

    root = Path(jev_root or paths.DERIVED / "jev") / AI_FIT_PASS / "answers"
    out: dict[str, dict] = {}
    if not root.exists():
        return out
    for part in sorted(root.glob("part-*.parquet")):
        for row in pq.read_table(part).to_pylist():
            if row.get("question_id") == "ai_fit":
                out[row["item_id"]] = row
    return out


def load_tasks(path: Path | None = None) -> list[dict]:
    p = Path(path or paths.RESEARCH / "tasks.csv")
    if not p.exists():
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@dataclass
class ScoreInputs:
    """Everything ``score_category`` needs, so callers load it once."""

    estimate: estimates.CategoryEstimate
    signs: dict[str, str] = field(default_factory=dict)  # s1..s4 grades
    sign_evidence: dict[str, str] = field(default_factory=dict)
    reasons_to_stay: list[str] = field(default_factory=list)
    challengers: list[dict] = field(default_factory=list)
    hn_pain_comments: int = 0
    in_use_share: float | None = None
    labelled_share: float | None = None
    tasks: list[dict] = field(default_factory=list)
    ai_answers: dict[str, dict] = field(default_factory=dict)
    ai_pass_present: bool = False
    config: catconfig.CategoryConfig | None = None
    universe_mid: float | None = None


def score_category(
    slug: str, inp: ScoreInputs, rubric: Rubric | None = None
) -> CategoryScore:
    """All five parts plus the rescaled opportunity total."""
    rubric = rubric or load_rubric()
    cfg = inp.config or catconfig.CategoryConfig(slug=slug)
    parts = {
        "size": size_part(inp.estimate, rubric, inp.universe_mid),
        "pain": pain_part(
            inp.signs.get("s3", "not_met"),
            inp.hn_pain_comments,
            inp.in_use_share,
            inp.labelled_share,
            rubric,
            [inp.sign_evidence["s3"]] if inp.sign_evidence.get("s3") else [],
        ),
        "ai_fit": ai_fit_part(
            inp.tasks, inp.ai_answers, slug, rubric,
            pass_present=inp.ai_pass_present,
        ),
        "lockin": lockin_part(
            inp.signs.get("s2", "not_met"),
            inp.signs.get("s4", "not_met"),
            inp.reasons_to_stay,
            cfg.regulation_patterns,
            rubric,
            [
                inp.sign_evidence[k]
                for k in ("s2", "s4")
                if inp.sign_evidence.get(k)
            ],
        ),
        "crowding": crowding_part(
            inp.challengers,
            cfg.funding_overrides,
            cfg.challenger_exclude,
            rubric,
        ),
    }
    raw, scaled, flags = combine(parts, rubric.weights)
    return CategoryScore(
        slug=slug, parts=parts, total_raw=raw, total=scaled, flags=flags
    )


def job_in_use_share(
    items: list[labels.LabelledItem], slug: str
) -> tuple[float | None, float | None]:
    """``(weighted, unweighted)`` share of labelled job posts in use."""
    posts = labels.labelled_job_posts(items, slug)
    if not posts:
        return None, None
    w_in = sum(i.weight for i in posts if i.status == "in_use")
    w_all = sum(i.weight for i in posts)
    n_in = sum(1 for i in posts if i.status == "in_use")
    return (
        w_in / w_all if w_all else None,
        n_in / len(posts),
    )


def hn_pain_comments(items: list[labels.LabelledItem], slug: str) -> int:
    """HN firsthand-pain comments for the category at p >= 0.7."""
    return sum(
        1
        for i in items
        if i.family == "hn"
        and i.category == slug
        and i.pain is not None
        and i.pain >= labels.HN_PAIN_YES
    )
