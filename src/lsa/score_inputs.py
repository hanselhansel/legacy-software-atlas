"""Inputs to ``scores.score_category``: market value, tasks and lane O measures.

Kept beside ``scores`` so callers (``export``) load everything once per
category and pass it in. ``ScoreInputs.market`` is the buyers x
segment-spend computation from ``market.market_value``; ``measures`` is the
``{part: [SubScore]}`` map from ``measures.collect`` for the category.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path

from lsa import estimates, market, measures, paths

AI_FIT_PASS = "tasks-ai-fit"


@dataclass
class ScoreInputs:
    """Everything ``score_category`` needs, so callers load it once."""

    estimate: estimates.CategoryEstimate
    tasks: list[dict] = field(default_factory=list)
    ai_answers: dict[str, dict] = field(default_factory=dict)
    ai_pass_present: bool = False
    universe_mid: float | None = None
    market: market.MarketValue | None = None
    measures: dict[str, list[measures.SubScore]] | None = None


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
