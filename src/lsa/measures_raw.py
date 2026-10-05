"""Lane O raw sub-score computations (plan 3).

Each function maps raw inputs to ``{category_slug: (raw_value, n)}``; the
``n`` counts the inputs behind the value (awards, reviews, apps, cases,
rounds). Minimum-count filtering and quintile assignment happen in
``lsa.measures``; this module only extracts.

Category attribution comes from Jev answer maps in the
``{item_id: {question_id: row}}`` shape produced by
``measures.load_pass_answers``; a choice in ``NO_CATEGORY`` is treated as
unattributed and dropped.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from statistics import median
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lsa.measures import Thresholds

KEEP_ALIVE = frozenset({"maintain", "extend"})
COUNTED_ACTIONS = frozenset({"maintain", "extend", "replace"})
FAILED_OUTCOMES = frozenset(
    {"cancelled_or_rolled_back", "completed_late_or_over"}
)
UNKNOWN_PROCEDURES = frozenset({"", "unknown"})
NO_CATEGORY = frozenset({"", "unclear", "other", "none"})


def _cat_choice(ans: dict) -> str:
    row = ans.get("category") or {}
    return str(row.get("choice") or "")


def keep_alive_shares(
    award_answers: dict,
) -> dict[str, tuple[float, int]]:
    """{slug: (keep_alive / counted, n_counted)} over the v1 answers."""
    keep: Counter[str] = Counter()
    denom: Counter[str] = Counter()
    for ans in award_answers.values():
        cat = _cat_choice(ans)
        action = str((ans.get("action") or {}).get("choice") or "")
        if cat in NO_CATEGORY or action not in COUNTED_ACTIONS:
            continue
        denom[cat] += 1
        keep[cat] += action in KEEP_ALIVE
    return {s: (keep[s] / denom[s], denom[s]) for s in denom}


def backend_failure_shares(
    review_categories: dict, review_answers: dict, th: Thresholds
) -> dict[str, tuple[float, int]]:
    """{slug: (share at p >= failure_yes, n_answered)} per category_hint."""
    yes: Counter[str] = Counter()
    n: Counter[str] = Counter()
    for item_id, ans in review_answers.items():
        cat = review_categories.get(item_id) or ""
        prob = (ans.get("backend_failure") or {}).get("probability")
        if not cat or cat in NO_CATEGORY or prob is None:
            continue
        n[cat] += 1
        yes[cat] += prob >= th.failure_yes
    return {s: (yes[s] / n[s], n[s]) for s in n}


def app_rating_means(apps: list[dict]) -> dict[str, tuple[float, int]]:
    """{slug: (mean of per-app mean ratings, n_apps)} over ok rows."""
    per_app: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for r in apps:
        if r.get("status") != "ok" or r.get("rating") is None:
            continue
        cat = str(r.get("category") or "")
        per_app[cat][str(r.get("apple_id") or "")].append(
            float(r["rating"])
        )
    out = {}
    for slug, ratings in per_app.items():
        means = [sum(v) / len(v) for v in ratings.values()]
        out[slug] = (sum(means) / len(means), len(means))
    return out


def failed_rates(cases: list[dict]) -> dict[str, tuple[float, int]]:
    """{slug: (failed / all cases, n_cases)}."""
    by: dict[str, list[dict]] = defaultdict(list)
    for c in cases:
        by[(c.get("category") or "").strip()].append(c)
    out = {}
    for slug, rows in by.items():
        if not slug:
            continue
        failed = sum(
            1 for r in rows if (r.get("outcome") or "") in FAILED_OUTCOMES
        )
        out[slug] = (failed / len(rows), len(rows))
    return out


def s3_score(grade: str, th: Thresholds) -> int:
    """Direct sub-score: strong -> 5, weak -> 3, anything else -> 1."""
    if grade == "strong":
        return int(th.s3_strong)
    if grade == "weak":
        return int(th.s3_weak)
    return int(th.s3_other)


def award_durations(
    awards: list[dict], award_answers: dict
) -> dict[str, tuple[float, int]]:
    """{slug: (median duration_months, n)} over v1-categorized awards."""
    cat_of = {
        iid: c for iid, a in award_answers.items()
        if (c := _cat_choice(a)) not in NO_CATEGORY
    }
    durs: dict[str, list[float]] = defaultdict(list)
    for r in awards:
        cat = cat_of.get(str(r.get("award_id") or ""))
        d = r.get("duration_months")
        if cat is None or d is None:
            continue
        durs[cat].append(float(d))
    return {s: (median(v), len(v)) for s, v in durs.items()}


def noncompetitive_shares(
    awards: list[dict], award_answers: dict, th: Thresholds
) -> dict[str, tuple[float, int]]:
    """{slug: (noncompetitive / known-procedure awards, n)}."""
    cat_of = {
        iid: c for iid, a in award_answers.items()
        if (c := _cat_choice(a)) not in NO_CATEGORY
    }
    non: Counter[str] = Counter()
    known: Counter[str] = Counter()
    for r in awards:
        cat = cat_of.get(str(r.get("award_id") or ""))
        proc = str(r.get("procedure") or "")
        if cat is None or proc in UNKNOWN_PROCEDURES:
            continue
        known[cat] += 1
        non[cat] += proc in th.noncompetitive
    return {s: (non[s] / known[s], known[s]) for s in known}


def replacement_durations(cases: list[dict]) -> dict[str, tuple[float, int]]:
    """{slug: (median duration_months, n)} over cases with a duration."""
    durs: dict[str, list[float]] = defaultdict(list)
    for c in cases:
        slug = (c.get("category") or "").strip()
        raw = (c.get("duration_months") or "").strip()
        if not slug or not raw:
            continue
        try:
            durs[slug].append(float(raw))
        except ValueError:
            continue
    return {s: (median(v), len(v)) for s, v in durs.items()}


def regulator_score(required: bool, th: Thresholds) -> int:
    """Direct sub-score: required -> 5, not required -> 1."""
    return int(th.regulator_true if required else th.regulator_false)


def traction_counts(
    challengers: dict[str, list[dict]], th: Thresholds
) -> dict[str, tuple[float, int]]:
    """{slug: (n AI-native challengers at status traction, same n)}."""
    out = {}
    for slug, rows in challengers.items():
        n = sum(
            1
            for r in rows
            if str(r.get("ai_native")) == "True"
            and str(r.get("status")) == th.traction_status
        )
        out[slug] = (float(n), n)
    return out


def funding_per_billion(
    rounds: list[dict], legacy_mid: dict[str, float]
) -> dict[str, tuple[float | None, int]]:
    """{slug: (sum amount_usd per $1B legacy mid, n_rounds)}.

    A category with no legacy midpoint gets raw None (cannot normalize);
    rounds exist but the sum can still be 0 when amounts are blank.
    """
    total: Counter[str] = Counter()
    n: Counter[str] = Counter()
    for r in rounds:
        slug = (r.get("category") or "").strip()
        if not slug:
            continue
        # Horizontal companies (general AI agents, foundation models) and
        # exits are not money aimed at this category (research column scope).
        if (r.get("scope") or "category_specific") != "category_specific":
            continue
        n[slug] += 1
        try:
            total[slug] += float(r.get("amount_usd") or 0)
        except ValueError:
            continue
    slugs = set(legacy_mid) | set(n)
    out = {}
    for slug in slugs:
        mid = legacy_mid.get(slug)
        raw = None if not mid else total[slug] / (mid / 1e9)
        out[slug] = (raw, n[slug])
    return out


def yc_counts(yc_answers: dict) -> dict[str, tuple[float, int]]:
    """{slug: (n yc items whose category answer is the slug, same n)}."""
    n: Counter[str] = Counter()
    for ans in yc_answers.values():
        cat = _cat_choice(ans)
        if cat not in NO_CATEGORY:
            n[cat] += 1
    return {s: (float(n[s]), n[s]) for s in n}
