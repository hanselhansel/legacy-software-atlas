"""Calibrate bottom-up market value to the top-down legacy spend.

Bottom-up value (buyers x spend per buyer) inflates when a register counts
millions of small businesses, so the category total comes from
``research/market_size.csv``: global annual spend times the share still on
legacy systems. Bottom-up figures keep their role as the split: each
region's and segment's share of the bottom-up total is applied to the
top-down total.
"""

from __future__ import annotations

import csv
import math
from dataclasses import replace
from pathlib import Path

from lsa import paths
from lsa.market import MarketValue


def load(path: Path | None = None) -> dict[str, dict]:
    p = Path(path or paths.RESEARCH / "market_size.csv")
    if not p.exists():
        return {}
    with open(p, newline="", encoding="utf-8") as f:
        return {r["category"]: r for r in csv.DictReader(f)}


def calibrate(mv: MarketValue, row: dict | None) -> MarketValue:
    """Top-down total with the bottom-up regional and segment split."""
    if not row or not row.get("legacy_low_usd"):
        return mv
    low, high = float(row["legacy_low_usd"]), float(row["legacy_high_usd"])
    mid = math.sqrt(low * high)
    bu = mv.value_mid or 0.0
    k = mid / bu if bu else 0.0
    note = (
        f"total from top-down legacy spend ${low / 1e9:.1f}B to ${high / 1e9:.1f}B "
        f"(research/market_size.csv); bottom-up ${bu / 1e9:.1f}B used only for the split"
    )
    segs = {
        s: replace(v, value_low=v.value_low * k, value_mid=v.value_mid * k, value_high=v.value_high * k)
        for s, v in mv.segments.items()
    }
    regs = {
        r: replace(
            v,
            value_low=None if v.value_low is None else v.value_low * k,
            value_mid=None if v.value_mid is None else v.value_mid * k,
            value_high=None if v.value_high is None else v.value_high * k,
        )
        for r, v in mv.regions.items()
    }
    buyable = sum(s.value_mid for s in segs.values() if s.buyable) if bu else None
    return replace(
        mv,
        has_spend=True,
        value_low=low,
        value_mid=mid,
        value_high=high,
        buyable_value=buyable,
        segments=segs,
        regions=regs,
        notes=mv.notes + (note,),
    )
