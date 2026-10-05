"""Usage estimates per category, region and segment (plan 2, task 5).

For each region with evidence, ``estimate_category`` triangulates three
source families:

- ``buyer_universe``: ``research/buyer_universe.csv`` registers for the
  category and region. ``approx_count`` is parsed by
  :func:`parse_counts.parse_sum_or_range` (ranges give low/high, summed
  counts give one figure); unparseable cells are skipped and noted.
- ``vendor_disclosed``: ``research/vendors.csv`` rows for the category. The
  first guarded number in ``disclosed_customers`` is the row's count; the
  free-text ``regions`` cell maps to study regions. Rows naming more than
  one study region land in the ``global`` bucket so their count is used
  once at category level (``multi_region_policy = "each"`` spreads them).
- ``confirmed_signals``: Jev-confirmed tenders (v2 category match) and job
  posts showing the legacy system in use (v2 ``legacy_in_use``). Each
  confirmed item counts as one distinct organisation for the floor, and
  its ``query_count / sampled`` weight scales it to the counted universe.

Per region:

- ``low = max(vendor-disclosed sum, distinct confirmed organisations)``
- ``high = min(buyer universe high, low x config multiplier)``; without a
  parsed universe the multiplier alone bounds the top.
- grade A when 3+ source families' point estimates agree within
  ``agree_within`` x, B when 2 agree, else C (rough).

Family point estimates: vendor sum, weighted confirmed / detection_rate,
and universe midpoint x penetration. All defaults live in
``configs/categories/<slug>.toml``.

Segment slices use confirmed signals only (job posts carry a v2 segment;
tenders do not), so they are always single-family grade C.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

from lsa import catconfig, labels, parse_counts, paths

FAM_UNIVERSE = "buyer_universe"
FAM_VENDOR = "vendor_disclosed"
FAM_CONFIRMED = "confirmed_signals"


@dataclass(frozen=True)
class SliceEstimate:
    key: str
    companies_low: int
    companies_high: int
    grade: str  # A / B / C per spec section 6
    families: tuple[str, ...]
    notes: tuple[str, ...]
    sources: tuple[str, ...]


@dataclass(frozen=True)
class CategoryEstimate:
    slug: str
    regions: dict[str, SliceEstimate]
    segments: dict[str, SliceEstimate]
    notes: tuple[str, ...]

    def midpoint(self) -> float:
        """Sum of (low + high) / 2 over the region slices."""
        return sum(
            (s.companies_low + s.companies_high) / 2
            for s in self.regions.values()
        )


def load_csv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _universe(
    slug: str, rows: list[dict], cfg: catconfig.CategoryConfig
) -> tuple[dict[str, dict], list[str]]:
    """Per-region buyer universe ``{region: {low, high, sources, detail}}``."""
    per: dict[str, dict] = {}
    notes: list[str] = []
    for row in rows:
        if row["category"] != slug:
            continue
        register = row.get("register", "")
        if any(s in register for s in cfg.universe_skip):
            notes.append(f"universe skip: {register}")
            continue
        region = parse_counts.norm_universe_region(row.get("region", ""))
        low, high, pnotes = parse_counts.parse_sum_or_range(
            row.get("approx_count", "")
        )
        if region in cfg.universe_overrides:
            low, high = cfg.universe_overrides[region]
            pnotes = ["override"]
        if low is None:
            notes.append(
                f"universe unparsed ({region} {register}): "
                + "; ".join(pnotes)
            )
            continue
        ent = per.setdefault(
            region, {"low": 0.0, "high": 0.0, "sources": [], "detail": []}
        )
        ent["low"] += low
        ent["high"] += high if high is not None else low
        if row.get("source"):
            ent["sources"].append(row["source"])
        ent["detail"].append(f"{register}: " + "; ".join(pnotes))
    return per, notes


def _vendor_sums(
    slug: str, rows: list[dict], cfg: catconfig.CategoryConfig
) -> tuple[dict[str, dict], list[str]]:
    """Per-region vendor-disclosed sums ``{region: {sum, sources, detail}}``."""
    per: dict[str, dict] = {}
    notes: list[str] = []
    for row in rows:
        if row["category"] != slug:
            continue
        if any(s in row.get("product", "") for s in cfg.vendor_exclude):
            notes.append(f"vendor skip: {row['vendor']} {row['product']}")
            continue
        key = f"{row['vendor']} | {row['product']}"
        year = parse_counts.parse_year(row.get("disclosed_customers", ""))
        if key in cfg.vendor_overrides:
            count, pnotes = cfg.vendor_overrides[key], ["override"]
        else:
            count, pnotes = parse_counts.parse_first_count(
                row.get("disclosed_customers", "")
            )
        regions, rnotes = parse_counts.resolve_regions(
            row.get("regions", "")
        )
        if cfg.multi_region_policy == "global" and len(regions) > 1:
            regions = {parse_counts.GLOBAL}
            rnotes = rnotes + ["multi-region row counted once as global"]
        if not regions:
            notes.append(
                f"vendor unmapped ({key}): " + "; ".join(rnotes or pnotes)
            )
            continue
        if count is None:
            notes.append(f"vendor unparsed ({key}): " + "; ".join(pnotes))
            continue
        tag = f"{key} {count:g}" + (f" ({year})" if year else "")
        for region in regions:
            ent = per.setdefault(
                region, {"sum": 0.0, "sources": [], "detail": []}
            )
            ent["sum"] += count
            if row.get("source"):
                ent["sources"].append(row["source"])
            ent["detail"].append(tag)
    return per, notes


def _grade(estimates: dict[str, float], agree_within: float) -> str:
    """A: 3+ families pairwise within ``agree_within``; B: 2; else C."""
    vals = {k: v for k, v in estimates.items() if v > 0}
    best = 1 if vals else 0
    for a, b in combinations(vals, 2):
        if max(vals[a], vals[b]) / min(vals[a], vals[b]) <= agree_within:
            best = max(best, 2)
    if len(vals) >= 3:
        ok = all(
            max(vals[a], vals[b]) / min(vals[a], vals[b]) <= agree_within
            for a, b in combinations(vals, 2)
        )
        if ok:
            best = 3
    return {3: "A", 2: "B"}.get(best, "C")


def _slice(
    key: str,
    low: float,
    universe_high: float | None,
    family_est: dict[str, float],
    cfg: catconfig.CategoryConfig,
    notes: list[str],
    sources: list[str],
) -> SliceEstimate:
    low_i = round(low)
    cap = low_i * cfg.multiplier
    if universe_high is not None:
        cap = min(universe_high, cap)
    high_i = round(cap)
    if high_i < low_i:
        notes.append("high floored at low: bound below the floor estimate")
        high_i = low_i
    grade = _grade(family_est, cfg.agree_within)
    if grade == "C":
        notes.append("grade C: rough, fewer than two agreeing families")
    return SliceEstimate(
        key=key,
        companies_low=low_i,
        companies_high=high_i,
        grade=grade,
        families=tuple(family_est),
        notes=tuple(notes),
        sources=tuple(dict.fromkeys(sources)),
    )


def estimate_category(
    slug: str,
    *,
    items: list[labels.LabelledItem] | None = None,
    buyer_universe: list[dict] | None = None,
    vendors: list[dict] | None = None,
    config: catconfig.CategoryConfig | None = None,
) -> CategoryEstimate:
    """Per-region and per-segment usage estimate for one category."""
    if items is None:
        items = labels.load_labels()
    if buyer_universe is None:
        buyer_universe = load_csv(paths.RESEARCH / "buyer_universe.csv")
    if vendors is None:
        vendors = load_csv(paths.RESEARCH / "vendors.csv")
    cfg = config or catconfig.load_config(slug)

    uni, uni_notes = _universe(slug, buyer_universe, cfg)
    vend, vend_notes = _vendor_sums(slug, vendors, cfg)
    conf = labels.confirmed(
        items,
        slug,
        job_in_use_choices=frozenset(cfg.job_in_use_choices),
        tender_require_status=frozenset(cfg.tender_require_status),
        tender_question_set=cfg.tender_question_set,
        job_question_sets=frozenset(cfg.job_question_sets),
    )
    by_region: dict[str, list] = {}
    for it in conf:
        by_region.setdefault(it.region or "unknown", []).append(it)

    regions: dict[str, SliceEstimate] = {}
    cat_notes: list[str] = list(uni_notes) + list(vend_notes)
    for region in sorted(set(uni) | set(vend) | set(by_region)):
        u = uni.get(region)
        v = vend.get(region)
        citems = by_region.get(region, [])
        v_sum = v["sum"] if v else 0.0
        distinct = len(citems)
        weighted = sum(i.weight for i in citems)
        low = max(v_sum, distinct)
        if low <= 0:
            cat_notes.append(
                f"{region}: universe only, no usage evidence; skipped"
            )
            continue
        family_est: dict[str, float] = {}
        if v_sum > 0:
            family_est[FAM_VENDOR] = v_sum
        if distinct:
            family_est[FAM_CONFIRMED] = weighted / cfg.detection_rate
        u_high = None
        if u:
            u_high = u["high"]
            family_est[FAM_UNIVERSE] = (
                (u["low"] + u["high"]) / 2 * cfg.penetration
            )
        notes = [
            (
                f"vendor sum {v_sum:g}, confirmed {distinct} items "
                f"(weighted {weighted:g})"
            )
        ]
        if u:
            notes.append(
                f"universe {u['low']:g}-{u['high']:g}: "
                + " | ".join(u["detail"])
            )
        else:
            notes.append("no buyer universe bound")
        if v:
            notes.append("vendor detail: " + " | ".join(v["detail"]))
        family_txt = ", ".join(
            f"{k}={v:g}" for k, v in family_est.items()
        )
        if family_txt:
            notes.append(f"family estimates: {family_txt}")
        regions[region] = _slice(
            region,
            low,
            u_high,
            family_est,
            cfg,
            notes,
            (v["sources"] if v else []) + (u["sources"] if u else []),
        )

    segments: dict[str, SliceEstimate] = {}
    seg_groups: dict[str, list] = {}
    unseg = 0
    for it in conf:
        if it.segment in labels.SEGMENTS:
            seg_groups.setdefault(it.segment, []).append(it)
        else:
            unseg += 1
    for seg in sorted(seg_groups):
        citems = seg_groups[seg]
        distinct = len(citems)
        weighted = sum(i.weight for i in citems)
        notes = [
            f"confirmed {distinct} items (weighted {weighted:g})",
            "single family (confirmed signals); rough",
        ]
        segments[seg] = _slice(
            seg,
            distinct,
            None,
            {FAM_CONFIRMED: weighted / cfg.detection_rate},
            cfg,
            notes,
            [],
        )
    if unseg:
        cat_notes.append(f"{unseg} confirmed items have no segment label")

    return CategoryEstimate(
        slug=slug,
        regions=regions,
        segments=segments,
        notes=tuple(cat_notes),
    )
