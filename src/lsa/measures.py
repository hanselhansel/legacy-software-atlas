"""Lane O measures: the pain, lock-in and crowding sub-scores (plan 3).

Each sub-score produces a raw value per category plus a count ``n`` of the
inputs behind it. ``collect`` then ranks every quintiled sub-score across
the categories into 1..5 (``quintiles``: rank = 1 + count of strictly
smaller raw values, quintile = ``1 + 5*rank_less // n``, so ties share the
lower quintile and a category under the sub-score's minimum count stays
None). Two sub-scores score directly without ranking: the S3 grade
(strong 5, weak 3, not_met 1) and regulator approval (true 5, false 1).

Sources per sub-score (``configs/rubric.toml`` holds the minima):

- pain ``keep_alive_share``: awards Jev pass ``awards-keep-alive-or-replace@v1``,
  (maintain + extend) / (maintain + extend + replace) over awards whose v1
  category answer is the category; min ``pain_min_awards``.
- pain ``backend_failure_share``: app review answers at probability >=
  ``failure_yes`` over the item's ``category_hint``; min ``min_reviews``.
- pain ``app_rating_inverted``: mean of per-app mean ratings from
  apps.parquet, ranked inverted (low rating = high pain); min ``min_apps``.
- pain ``failed_rate``: replacement cases with outcome
  cancelled_or_rolled_back or completed_late_or_over over all cases;
  min ``min_cases``.
- lockin ``award_duration_months``: median award duration over the v1
  category answer; min ``lockin_min_awards``.
- lockin ``noncompetitive_share``: share of categorized awards whose
  procedure is negotiated_no_competition or direct, over awards with a
  known procedure; min ``lockin_min_awards``.
- lockin ``replacement_duration_months``: median case duration;
  min ``min_cases``.
- crowding ``ai_native_traction``: challengers.csv rows with ai_native and
  status ``traction``.
- crowding ``funding_per_billion``: ai_native_rounds_24m amount_usd sum per
  $1B of legacy spend midpoint (sqrt of low x high, as topdown.calibrate).
- crowding ``yc_2024_plus``: yc-category@v1 answers naming the category.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass, field
from pathlib import Path

from lsa.measures_raw import (
    app_rating_means,
    award_durations,
    backend_failure_shares,
    failed_rates,
    funding_per_billion,
    keep_alive_shares,
    noncompetitive_shares,
    regulator_score,
    replacement_durations,
    s3_score,
    traction_counts,
    yc_counts,
)

__all__ = [
    "AWARDS_SET",
    "REVIEWS_SET",
    "YC_SET",
    "MeasureData",
    "SubScore",
    "Thresholds",
    "app_rating_means",
    "award_durations",
    "backend_failure_shares",
    "collect",
    "failed_rates",
    "funding_per_billion",
    "item_categories",
    "keep_alive_shares",
    "legacy_midpoints",
    "load_csv",
    "load_parquet",
    "load_pass_answers",
    "noncompetitive_shares",
    "quintiles",
    "regulator_map",
    "regulator_score",
    "replacement_durations",
    "s3_score",
    "traction_counts",
    "yc_counts",
]

AWARDS_SET = "awards-keep-alive-or-replace@v1"
REVIEWS_SET = "app-reviews-backend-failure@v1"
YC_SET = "yc-category@v2"  # reworded after the blind audit (docs/reports/jev-audit.md)


@dataclass(frozen=True)
class Thresholds:
    """Rubric minima and direct-score maps; parsed from rubric.toml."""

    pain_min_awards: int = 10
    min_reviews: int = 50
    min_apps: int = 3
    pain_min_cases: int = 3
    failure_yes: float = 0.7
    s3_strong: float = 5.0
    s3_weak: float = 3.0
    s3_other: float = 1.0
    lockin_min_awards: int = 10
    lockin_min_cases: int = 3
    noncompetitive: tuple[str, ...] = ("negotiated_no_competition", "direct")
    regulator_true: float = 5.0
    regulator_false: float = 1.0
    traction_status: str = "traction"


@dataclass(frozen=True)
class SubScore:
    """One sub-score for one category: raw value, input count, 1..5 score."""

    name: str
    raw: float | str | bool | None
    n: int
    score: int | None


@dataclass
class MeasureData:
    """Everything ``collect`` needs, loaded once by the caller.

    ``None`` marks an absent source (missing file or Jev pass): the
    sub-scores it feeds all come out as no-data. Empty containers are real
    data: a category with zero AI-native challengers scores, not skips.
    """

    s3: dict[str, str] = field(default_factory=dict)
    awards: list[dict] | None = None
    award_answers: dict | None = None
    review_categories: dict | None = None
    review_answers: dict | None = None
    apps: list[dict] | None = None
    cases: list[dict] | None = None
    regulator: dict[str, bool] = field(default_factory=dict)
    challengers: dict[str, list[dict]] | None = None
    rounds: list[dict] | None = None
    legacy_mid: dict[str, float] = field(default_factory=dict)
    yc_answers: dict | None = None


def load_csv(path: Path) -> list[dict] | None:
    """CSV rows as dicts, or None when the file is absent."""
    p = Path(path)
    if not p.exists():
        return None
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_parquet(path: Path) -> list[dict] | None:
    """Parquet rows as dicts, or None when the file is absent."""
    import pyarrow.parquet as pq

    p = Path(path)
    if not p.exists():
        return None
    return pq.read_table(p).to_pylist()


def load_pass_answers(
    jev_root: Path, set_label: str
) -> dict[str, dict[str, dict]] | None:
    """``{item_id: {question_id: row}}`` for one set label, or None when the
    pass directory is absent (the pass never ran)."""
    import pyarrow.parquet as pq

    answers_dir = (
        Path(jev_root) / set_label.split("@", 1)[0] / "answers"
    )
    if not answers_dir.exists():
        return None
    out: dict[str, dict[str, dict]] = {}
    for part in sorted(answers_dir.glob("part-*.parquet")):
        for row in pq.read_table(part).to_pylist():
            if row.get("question_set") != set_label:
                continue
            out.setdefault(str(row["item_id"]), {})[
                row["question_id"]
            ] = row
    return out


def item_categories(items_path: Path, family: str) -> dict[str, str]:
    """``{item_id: category_hint}`` for one family in items.parquet."""
    rows = load_parquet(items_path) or []
    return {
        str(r["item_id"]): str(r.get("category_hint") or "")
        for r in rows
        if r.get("family") == family
    }


def regulator_map(rows: list[dict] | None) -> dict[str, bool]:
    """``{slug: regulator_approval_required}`` from regulator_approval.csv."""
    out: dict[str, bool] = {}
    for r in rows or []:
        cat = (r.get("category") or "").strip()
        if cat:
            out[cat] = (r.get("regulator_approval_required") or "") == "True"
    return out


def legacy_midpoints(rows: list[dict] | None) -> dict[str, float]:
    """``{slug: sqrt(legacy_low x legacy_high)}`` from market_size.csv."""
    out: dict[str, float] = {}
    for r in rows or []:
        cat = (r.get("category") or "").strip()
        try:
            low = float(r.get("legacy_low_usd") or 0)
            high = float(r.get("legacy_high_usd") or 0)
        except ValueError:
            continue
        if cat and low > 0 and high > 0:
            out[cat] = math.sqrt(low * high)
    return out


def quintiles(
    raws: dict[str, float | None], *, invert: bool = False
) -> dict[str, int | None]:
    """Rank raw values into 1..5: ``1 + 5 * count_less // n``.

    ``invert`` flips the order (lower raw = higher quintile). Ties share
    the lower quintile because every tied value has the same count_less.
    None raw -> None.
    """
    vals = {
        s: (-v if invert else v)
        for s, v in raws.items()
        if v is not None
    }
    n = len(vals)
    out: dict[str, int | None] = {}
    for s, raw in raws.items():
        if raw is None or s not in vals:
            out[s] = None
            continue
        less = sum(1 for o in vals.values() if o < vals[s])
        out[s] = 1 + (5 * less) // n
    return out


def _under_min(
    raws: dict[str, tuple[float | None, int]], min_n: int
) -> dict[str, tuple[float | None, int]]:
    """Blank the raw when the input count is below the sub-score minimum."""
    return {
        s: (raw if raw is not None and n >= min_n else None, n)
        for s, (raw, n) in raws.items()
    }


# Sub-score -> (part, invert, zero_fill). zero_fill marks count sub-scores
# where a category missing from the raw map is a real zero (the source file
# or pass exists and simply found nothing), not absent data.
_SUB_SCORES: tuple[tuple[str, str, bool, bool], ...] = (
    ("pain", "keep_alive_share", False, False),
    ("pain", "backend_failure_share", False, False),
    ("pain", "app_rating_inverted", True, False),
    ("pain", "failed_rate", False, False),
    ("lockin", "award_duration_months", False, False),
    ("lockin", "noncompetitive_share", False, False),
    ("lockin", "replacement_duration_months", False, False),
    ("crowding", "ai_native_traction", False, True),
    ("crowding", "funding_per_billion", False, False),
    ("crowding", "yc_2024_plus", False, True),
)


def _raw_sub_scores(
    data: MeasureData, th: Thresholds
) -> dict[str, dict[str, tuple[float | None, int]] | None]:
    """``{sub_score: {slug: (raw, n)}}``; None marks an absent source."""
    award_ok = data.award_answers is not None
    return {
        "keep_alive_share": (
            _under_min(
                keep_alive_shares(data.award_answers), th.pain_min_awards
            )
            if award_ok
            else None
        ),
        "backend_failure_share": (
            _under_min(
                backend_failure_shares(
                    data.review_categories or {}, data.review_answers, th
                ),
                th.min_reviews,
            )
            if data.review_answers is not None
            else None
        ),
        "app_rating_inverted": (
            _under_min(app_rating_means(data.apps), th.min_apps)
            if data.apps is not None
            else None
        ),
        "failed_rate": (
            _under_min(failed_rates(data.cases), th.pain_min_cases)
            if data.cases is not None
            else None
        ),
        "award_duration_months": (
            _under_min(
                award_durations(data.awards or [], data.award_answers),
                th.lockin_min_awards,
            )
            if award_ok
            else None
        ),
        "noncompetitive_share": (
            _under_min(
                noncompetitive_shares(
                    data.awards or [], data.award_answers, th
                ),
                th.lockin_min_awards,
            )
            if award_ok
            else None
        ),
        "replacement_duration_months": (
            _under_min(replacement_durations(data.cases), th.lockin_min_cases)
            if data.cases is not None
            else None
        ),
        "ai_native_traction": (
            traction_counts(data.challengers, th)
            if data.challengers is not None
            else None
        ),
        "funding_per_billion": (
            funding_per_billion(data.rounds, data.legacy_mid)
            if data.rounds is not None
            else None
        ),
        "yc_2024_plus": (
            yc_counts(data.yc_answers)
            if data.yc_answers is not None
            else None
        ),
    }


def collect(
    slugs: list[str] | tuple[str, ...], data: MeasureData, th: Thresholds
) -> dict[str, dict[str, list[SubScore]]]:
    """``{slug: {part: [SubScore]}}`` with quintiles assigned across slugs."""
    slugs = list(slugs)
    raws = _raw_sub_scores(data, th)
    assigned: dict[str, dict[str, int | None]] = {}
    for _, name, invert, zero_fill in _SUB_SCORES:
        r = raws[name]
        default = (0.0, 0) if zero_fill else (None, 0)
        flat = {
            s: (r.get(s, default)[0] if r is not None else None)
            for s in slugs
        }
        assigned[name] = quintiles(flat, invert=invert)
    out: dict[str, dict[str, list[SubScore]]] = {}
    for slug in slugs:
        subs: dict[str, list[SubScore]] = {
            "pain": [], "lockin": [], "crowding": []
        }
        for part, name, _, zero_fill in _SUB_SCORES:
            r = raws[name]
            default = (0.0, 0) if zero_fill else (None, 0)
            raw, n = r.get(slug, default) if r is not None else (None, 0)
            subs[part].append(SubScore(name, raw, n, assigned[name][slug]))
        grade = data.s3.get(slug)
        subs["pain"].append(
            SubScore(
                "s3_grade",
                grade or None,
                1 if grade else 0,
                s3_score(grade, th) if grade else None,
            )
        )
        reg = data.regulator.get(slug)
        subs["lockin"].append(
            SubScore(
                "regulator_approval",
                reg if reg is not None else None,
                1 if reg is not None else 0,
                regulator_score(reg, th) if reg is not None else None,
            )
        )
        out[slug] = subs
    return out
