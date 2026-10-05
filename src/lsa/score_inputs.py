"""Inputs to ``scores.score_category``: labelled data, tasks, market value.

Kept beside ``scores`` so callers (``export``) load everything once per
category and pass it in. ``ScoreInputs.market`` is the buyers x
segment-spend computation from ``market.market_value``.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path

from lsa import catconfig, estimates, labels, market, paths

AI_FIT_PASS = "tasks-ai-fit"


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
    market: market.MarketValue | None = None


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
