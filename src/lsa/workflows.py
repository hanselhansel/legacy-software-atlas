"""Lane O workflow scores (plan 3): the opportunity index per workflow.

For every row of ``research/workflows.csv`` the index combines the
workflow's own data with its category's scores:

``index = rank(labour_value) + rank(ai_usage or category ai_fit)
        + rank(pain) - rank(crowding)
        - (touches_core ? 1 : 0) * rank_spread``

Ranks ascend by value (``rank = 1 + count of strictly smaller values``;
ties share the lower rank, a missing value ranks 0) across the workflows
in the set, so labour value, AI usage and pain pull a workflow up and
crowding pushes it down. ``rank_spread = max(base) - min(base)`` of the
base index before the core penalty, so a workflow that touches the core
lands below every one that does not. ``touches_core`` is the lock-in
proxy: false means low lock-in for that work.

Inputs: ``research/workflows.csv`` (workflow_id, category, touches_core),
``data/derived/workflows.parquet`` when present (labour_value_usd,
ai_usage per workflow_id), ``research/ai_native_rounds_24m.csv`` (crowding
= rounds mapped to the workflow), and the category pain and ai_fit part
scores from the export.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


def load_workflows(path: Path) -> list[dict]:
    """``research/workflows.csv`` rows, or [] when absent."""
    p = Path(path)
    if not p.exists():
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_metrics(path: Path) -> dict[str, dict]:
    """``{workflow_id: {labour_value_usd, ai_usage}}`` from the lane N
    parquet, or {} when absent."""

    def f(v):
        try:
            return None if v is None else float(v)
        except (TypeError, ValueError):
            return None

    rows = _load_parquet(path)
    return {
        str(r["workflow_id"]): {
            "labour_value_usd": f(r.get("labour_value_usd")),
            "ai_usage": f(r.get("ai_usage")),
        }
        for r in rows
        if r.get("workflow_id")
    }


def _load_parquet(path: Path) -> list[dict]:
    import pyarrow.parquet as pq

    p = Path(path)
    if not p.exists():
        return []
    return pq.read_table(p).to_pylist()


def rounds_by_workflow(rounds: list[dict]) -> dict[str, int]:
    """``{workflow_id: n AI-native rounds}`` from ai_native_rounds_24m."""
    return dict(
        Counter(
            (r.get("workflow_id") or "").strip()
            for r in rounds
            if (r.get("workflow_id") or "").strip()
        )
    )


def _touches(value) -> bool:
    return value is True or str(value).strip().lower() == "true"


def _ranks(values: list[float | None]) -> list[int]:
    """Ascending rank per position: 1 + count_less; None ranks 0."""
    present = [v for v in values if v is not None]
    return [
        0 if v is None else 1 + sum(1 for o in present if o < v)
        for v in values
    ]


def score_workflows(
    rows: list[dict],
    metrics: dict[str, dict],
    rounds: dict[str, int],
    pain: dict[str, int | None],
    ai_fit: dict[str, int | None],
) -> list[dict]:
    """Score every workflow row and return them sorted by index desc."""
    labour, ai, pn, crowd = [], [], [], []
    for r in rows:
        m = metrics.get(str(r.get("workflow_id") or "")) or {}
        labour.append(m.get("labour_value_usd"))
        ai.append(m.get("ai_usage"))
        pn.append(pain.get(r.get("category")))
        crowd.append(float(rounds.get(str(r.get("workflow_id") or ""), 0)))
    # ai_usage falls back to the category's ai_fit score when absent.
    ai = [
        v if v is not None else ai_fit.get(rows[i].get("category"))
        for i, v in enumerate(ai)
    ]
    rl, ra, rp, rc = (
        _ranks(labour), _ranks(ai), _ranks(pn), _ranks(crowd)
    )
    base = [rl[i] + ra[i] + rp[i] - rc[i] for i in range(len(rows))]
    spread = (max(base) - min(base)) if base else 0
    out = []
    for i, r in enumerate(rows):
        ai_src = (
            "workflow"
            if (metrics.get(str(r.get("workflow_id") or "")) or {}).get(
                "ai_usage"
            )
            is not None
            else "category"
        )
        touches = _touches(r.get("touches_core"))
        out.append(
            {
                "workflow_id": r.get("workflow_id"),
                "category": r.get("category"),
                "workflow": r.get("workflow"),
                "description": r.get("description"),
                "labour_value_usd": labour[i],
                "ai_usage": ai[i],
                "ai_source": ai_src,
                "touches_core": touches,
                "pain": pn[i],
                "crowding": int(crowd[i]),
                "base_index": base[i],
                "opportunity_index": base[i] - spread * touches,
            }
        )
    out.sort(
        key=lambda w: (-w["opportunity_index"], w["workflow_id"] or "")
    )
    return out
