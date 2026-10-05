"""The five-part score rubric from ``configs/rubric.toml`` (spec section 8).

Each part scores 1 to 5; lockin and crowding are penalties. The opportunity
total is ``size + pain + ai_fit - lockin - crowding`` weighted by
``[weights]`` and rescaled to 0..100 over the range the present parts can
reach.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

from lsa import paths


@dataclass(frozen=True)
class Rubric:
    weights: dict[str, float]
    size_bins: tuple[float, ...]
    s3_strong: float
    s3_weak: float
    hn_pain_min_comments: int
    legacy_in_use_share: float
    share_weights: dict[str, float]
    s2_strong: float
    s2_weak: float
    s4_strong: float
    regulation_reason: float
    count_bins: tuple[float, ...]
    funding_usd_over: float


def load_rubric(path: Path | None = None) -> Rubric:
    data = tomllib.loads(
        Path(path or paths.ROOT / "configs" / "rubric.toml").read_text(
            encoding="utf-8"
        )
    )
    pain, lockin, crowd = data["pain"], data["lockin"], data["crowding"]
    return Rubric(
        weights={k: float(v) for k, v in data["weights"].items()},
        size_bins=tuple(float(b) for b in data["size"]["bins"]),
        s3_strong=float(pain["s3_strong"]),
        s3_weak=float(pain["s3_weak"]),
        hn_pain_min_comments=int(pain["hn_pain_min_comments"]),
        legacy_in_use_share=float(pain["legacy_in_use_share"]),
        share_weights={
            k: float(v) for k, v in data["ai_fit"]["share_weights"].items()
        },
        s2_strong=float(lockin["s2_strong"]),
        s2_weak=float(lockin["s2_weak"]),
        s4_strong=float(lockin["s4_strong"]),
        regulation_reason=float(lockin["regulation_reason"]),
        count_bins=tuple(float(b) for b in crowd["count_bins"]),
        funding_usd_over=float(crowd["funding_usd_over"]),
    )
