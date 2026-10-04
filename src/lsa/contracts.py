"""Data contracts shared by collectors, estimation, and exports.

CountRecord is one row per (source, query) count run; its count is None when the
source gives no total, never 0. EvidenceRow is one row per fetched item kept as
evidence; its excerpt is at most 30 words. Both validate on construction.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

# Regions in scope (spec section 4): ISO alpha-2 codes, with "EU" for EU-level sources.
REGIONS = frozenset(
    {"US", "EU", "UK", "SG", "IN", "ID", "VN", "MY", "TH", "PH", "AU"}
)

MAX_EXCERPT_WORDS = 30

Lane = Literal["count", "depth"]


def _check_region(region: str) -> None:
    if region not in REGIONS:
        raise ValueError(f"unknown region code: {region!r}")


@dataclass(frozen=True)
class CountRecord:
    source: str
    family: str
    region: str
    category: str
    system: str
    query: str
    count: int | None
    method: str
    counted_at: str

    def __post_init__(self) -> None:
        _check_region(self.region)
        if self.count is not None and self.count < 0:
            raise ValueError("count must be None or a non-negative int")


@dataclass(frozen=True)
class EvidenceRow:
    source: str
    family: str
    url: str
    fetched_at: str
    region: str
    category: str
    system: str
    org: str
    excerpt: str
    lane: Lane

    def __post_init__(self) -> None:
        _check_region(self.region)
        if self.lane not in ("count", "depth"):
            raise ValueError(f"lane must be 'count' or 'depth', got {self.lane!r}")
        words = len(self.excerpt.split())
        if words > MAX_EXCERPT_WORDS:
            raise ValueError(
                f"excerpt is {words} words; max is {MAX_EXCERPT_WORDS}"
            )
