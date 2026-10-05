"""The five-part score rubric from ``configs/rubric.toml`` (spec section 8).

Each part scores 1 to 5; lockin and crowding are penalties. The opportunity
total is ``size + pain + ai_fit - lockin - crowding`` weighted by
``[weights]`` and rescaled to 0..100 over the range the present parts can
reach. The ``measures`` field holds the lane O sub-score minima and
thresholds from the ``[pain]``, ``[lockin]`` and ``[crowding]`` sections.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path

from lsa import paths
from lsa.measures import Thresholds


@dataclass(frozen=True)
class Rubric:
    weights: dict[str, float]
    value_bins_usd: tuple[float, ...]
    buyer_bins: tuple[float, ...]
    share_weights: dict[str, float]
    measures: Thresholds = field(default_factory=Thresholds)


def load_rubric(path: Path | None = None) -> Rubric:
    data = tomllib.loads(
        Path(path or paths.ROOT / "configs" / "rubric.toml").read_text(
            encoding="utf-8"
        )
    )
    pain, lockin, crowd = data["pain"], data["lockin"], data["crowding"]
    thresholds = Thresholds(
        pain_min_awards=int(pain["min_awards"]),
        min_reviews=int(pain["min_reviews"]),
        min_apps=int(pain["min_apps"]),
        pain_min_cases=int(pain["min_cases"]),
        failure_yes=float(pain["failure_yes"]),
        s3_strong=float(pain["s3_strong"]),
        s3_weak=float(pain["s3_weak"]),
        s3_other=float(pain["s3_other"]),
        lockin_min_awards=int(lockin["min_awards"]),
        lockin_min_cases=int(lockin["min_cases"]),
        noncompetitive=tuple(lockin["noncompetitive"]),
        regulator_true=float(lockin["regulator_true"]),
        regulator_false=float(lockin["regulator_false"]),
        traction_status=str(crowd["traction_status"]),
    )
    return Rubric(
        weights={k: float(v) for k, v in data["weights"].items()},
        value_bins_usd=tuple(
            float(b) for b in data["size"].get("value_bins_usd", ())
        ),
        buyer_bins=tuple(
            float(b)
            for b in data["size"].get("buyer_bins", data["size"].get("bins", ()))
        ),
        share_weights={
            k: float(v) for k, v in data["ai_fit"]["share_weights"].items()
        },
        measures=thresholds,
    )
