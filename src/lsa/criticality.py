"""``research/criticality.csv``: how much each segment spends and builds.

One row per (category, segment): a ``criticality`` level repeated on
every row of the category (critical / important / supporting), the
best-documented buyer segment (``best_icp``), a ``build_in_house`` class
(common / some / rare) and the annual USD a buyer in the segment spends
on the category (``spend_low`` / ``spend_high``, blank when the segment
does not buy). ``evidence`` and ``sources`` trace each row.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path

from lsa import paths

_SPEND = re.compile(
    r"^\$?\s*([\d,]*\.?\d+)\s*(k|m|b|bn|thousand|million|billion)?$",
    re.IGNORECASE,
)
_SCALE = {
    "k": 1e3, "thousand": 1e3,
    "m": 1e6, "million": 1e6,
    "b": 1e9, "bn": 1e9, "billion": 1e9,
}


def norm_seg(text: str) -> str:
    """``Mid Market`` / ``mid-market`` -> ``mid_market``."""
    return re.sub(r"[\s\-]+", "_", (text or "").strip().lower())


def _spend_num(text: str) -> float | None:
    """USD figure like ``$1.2M`` or ``50,000``; blank/unparseable -> None."""
    m = _SPEND.match((text or "").strip())
    if not m:
        return None
    return float(m.group(1).replace(",", "")) * _SCALE.get(
        (m.group(2) or "").lower(), 1.0
    )


def _source_list(text: str) -> tuple[str, ...]:
    return tuple(
        s for s in (p.strip() for p in re.split(r"[;|]", text or "")) if s
    )


@dataclass(frozen=True)
class SegmentSpend:
    """One (category, segment) row of criticality.csv."""

    build_in_house: str
    spend_low: float | None
    spend_high: float | None
    evidence: str
    sources: tuple[str, ...]

    def bounds(self) -> tuple[float, float] | None:
        """(low, high) spend, cross-filling a missing side; None if neither."""
        if self.spend_low is None and self.spend_high is None:
            return None
        low = (
            self.spend_low if self.spend_low is not None else self.spend_high
        )
        high = (
            self.spend_high if self.spend_high is not None else self.spend_low
        )
        return low, high


@dataclass(frozen=True)
class Criticality:
    level: str
    why: str
    best_icp: str
    segments: dict[str, SegmentSpend]


def criticality_map(rows: list[dict]) -> dict[str, Criticality]:
    """``{slug: Criticality}`` from criticality.csv row dicts."""
    meta: dict[str, dict] = {}
    for row in rows:
        slug = (row.get("category") or "").strip()
        seg = norm_seg(row.get("segment") or "")
        if not slug or not seg:
            continue
        ent = meta.setdefault(
            slug, {"level": "", "why": "", "icp": "", "segs": {}}
        )
        for key, col in (
            ("level", "criticality"),
            ("why", "criticality_why"),
            ("icp", "best_icp"),
        ):
            if not ent[key] and (row.get(col) or "").strip():
                ent[key] = row[col].strip()
        ent["segs"][seg] = SegmentSpend(
            build_in_house=(row.get("build_in_house") or "").strip(),
            spend_low=_spend_num(row.get("spend_low")),
            spend_high=_spend_num(row.get("spend_high")),
            evidence=(row.get("evidence") or "").strip(),
            sources=_source_list(row.get("sources") or ""),
        )
    return {
        slug: Criticality(ent["level"], ent["why"], ent["icp"], ent["segs"])
        for slug, ent in meta.items()
    }


def load_criticality(path: Path | None = None) -> dict[str, Criticality]:
    p = Path(path or paths.RESEARCH / "criticality.csv")
    if not p.exists():
        return {}
    with open(p, newline="", encoding="utf-8") as f:
        return criticality_map(list(csv.DictReader(f)))
