"""Market value per category and the build-vs-buy lens (plan 2, task 7).

``research/criticality.csv`` says what a buyer in each segment spends per
year (``criticality.load_criticality``); ``research/buyer_universe.csv``
rows carry ``seg_<segment>`` share columns saying which share of a
register's buyers sits in each segment (about 1 in total, blank when
unknown).

``market_value`` prices each buyer-universe row's buyers at the
share-weighted segment spend, giving value_low/mid/high per category,
region and segment. Rows without shares attribute all buyers to the
category's best-documented segment; segments without spend add no value.
Every assumption lands in ``notes``.
"""

from __future__ import annotations

import math

from dataclasses import dataclass

from lsa import catconfig, criticality, estimates, parse_counts
from lsa.criticality import Criticality

SEGMENT_ORDER = ("enterprise", "mid_market", "smb", "government")

_SHARE_SLACK = 0.05  # row shares may sum to 1 +/- this before we note it


def _shares(row: dict) -> dict[str, float]:
    """Non-empty ``seg_<segment>`` share columns on a buyer-universe row."""
    out: dict[str, float] = {}
    for seg in SEGMENT_ORDER:
        raw = (row.get(f"seg_{seg}") or "").strip()
        if not raw:
            continue
        try:
            out[seg] = float(raw)
        except ValueError:
            continue
    return out


def _best_segment(crit: Criticality | None) -> str | None:
    """The category's best-documented segment for share-less rows.

    ``best_icp`` wins when it names a segment the category documents;
    otherwise the row with the most sources, then longest evidence, in
    SEGMENT_ORDER order.
    """
    if crit is None or not crit.segments:
        return None
    icp = criticality.norm_seg(crit.best_icp)
    if icp in crit.segments:
        return icp

    def doc_key(item: tuple[str, criticality.SegmentSpend]) -> tuple:
        seg, s = item
        order = (
            SEGMENT_ORDER.index(seg)
            if seg in SEGMENT_ORDER
            else len(SEGMENT_ORDER)
        )
        return (-len(s.sources), -len(s.evidence), order)

    return min(crit.segments.items(), key=doc_key)[0]


@dataclass(frozen=True)
class SegmentMarket:
    buyers: float
    value_low: float
    value_mid: float
    value_high: float
    build_in_house: str | None
    buyable: bool
    evidence: str
    sources: tuple[str, ...]


@dataclass(frozen=True)
class RegionMarket:
    buyers_low: float
    buyers_high: float
    value_low: float | None
    value_mid: float | None
    value_high: float | None

    @property
    def buyers_mid(self) -> float:
        return (self.buyers_low + self.buyers_high) / 2


@dataclass(frozen=True)
class MarketValue:
    """Buyers times segment spend for one kept category."""

    slug: str
    buyers_low: float
    buyers_high: float
    has_spend: bool
    value_low: float | None
    value_mid: float | None
    value_high: float | None
    buyable_value: float | None
    criticality: Criticality | None
    segments: dict[str, SegmentMarket]
    regions: dict[str, RegionMarket]
    notes: tuple[str, ...]

    @property
    def buyers_mid(self) -> float:
        return (self.buyers_low + self.buyers_high) / 2


def market_value(
    slug: str,
    buyer_universe_rows: list[dict],
    crit: Criticality | None = None,
    cfg: catconfig.CategoryConfig | None = None,
) -> MarketValue:
    """Buyers x share-weighted segment spend, per region and segment.

    ``buyer_universe_rows`` are research/buyer_universe.csv dicts; the
    same register/region/unit/override rules as the usage estimate apply
    via :func:`estimates._universe_rows`.
    """
    cfg = cfg or catconfig.CategoryConfig(slug=slug)
    recs, notes = estimates._universe_rows(slug, buyer_universe_rows, cfg)
    notes = list(notes)
    seg_buyers: dict[str, float] = {}
    seg_val: dict[str, list[float]] = {}  # seg -> [low, mid, high]
    reg: dict[str, dict[str, float]] = {}
    fallback_counts: dict[str, int] = {}
    unsegmented = odd_shares = 0
    no_spend: set[str] = set()
    buyers_low = buyers_high = 0.0
    for r in recs:
        low, high = r["low"], r["high"]
        mid = (low + high) / 2
        buyers_low += low
        buyers_high += high
        shares = _shares(r["row"])
        if not shares:
            seg = _best_segment(crit)
            if seg is None:
                unsegmented += 1
            else:
                shares = {seg: 1.0}
                fallback_counts[seg] = fallback_counts.get(seg, 0) + 1
        elif not 1 - _SHARE_SLACK <= sum(shares.values()) <= 1 + _SHARE_SLACK:
            odd_shares += 1
        ra = reg.setdefault(
            r["region"],
            {"blow": 0.0, "bhigh": 0.0, "vlow": 0.0, "vmid": 0.0, "vhigh": 0.0},
        )
        ra["blow"] += low
        ra["bhigh"] += high
        for seg, share in shares.items():
            sp = crit.segments.get(seg) if crit else None
            bounds = sp.bounds() if sp else None
            if bounds is None:
                if share:
                    no_spend.add(seg)
                s_low = s_mid = s_high = 0.0
            else:
                s_low, s_high = bounds
                # Spend ranges span orders of magnitude, so the typical buyer
                # sits at the geometric mean, not the arithmetic one.
                s_mid = math.sqrt(s_low * s_high) if s_low > 0 else s_high / 10
            seg_buyers[seg] = seg_buyers.get(seg, 0.0) + mid * share
            sv = seg_val.setdefault(seg, [0.0, 0.0, 0.0])
            sv[0] += low * share * s_low
            sv[1] += mid * share * s_mid
            sv[2] += high * share * s_high
            ra["vlow"] += low * share * s_low
            ra["vmid"] += mid * share * s_mid
            ra["vhigh"] += high * share * s_high
    for seg, n in sorted(fallback_counts.items()):
        notes.append(
            f"{n} buyer-universe rows have no segment shares; "
            f"buyers counted as {seg} (best-documented segment)"
        )
    if unsegmented:
        notes.append(
            f"{unsegmented} buyer-universe rows have no segment shares and "
            "the category has no best-documented segment; buyers only"
        )
    if no_spend:
        notes.append(
            "no spend data for segment(s) "
            + ", ".join(sorted(no_spend))
            + "; those shares add no value"
        )
    if odd_shares:
        notes.append(
            f"{odd_shares} buyer-universe rows have segment shares "
            "not summing to 1; used as given"
        )
    has_spend = bool(
        crit and any(s.bounds() for s in crit.segments.values())
    )
    if crit is None:
        notes.append(f"no criticality.csv rows for {slug}; size uses buyer count")
    elif not has_spend:
        notes.append(
            f"criticality.csv has no spend for {slug}; size uses buyer count"
        )
    segs: dict[str, SegmentMarket] = {}
    for seg in set(seg_buyers) | set(crit.segments if crit else ()):
        sp = crit.segments.get(seg) if crit else None
        bih = sp.build_in_house if sp else None
        vals = seg_val.get(seg, [0.0, 0.0, 0.0])
        segs[seg] = SegmentMarket(
            buyers=seg_buyers.get(seg, 0.0),
            value_low=vals[0],
            value_mid=vals[1],
            value_high=vals[2],
            build_in_house=bih or None,
            buyable=bih != "common",
            evidence=sp.evidence if sp else "",
            sources=sp.sources if sp else (),
        )
    regions = {
        region: RegionMarket(
            buyers_low=ra["blow"],
            buyers_high=ra["bhigh"],
            value_low=ra["vlow"] if has_spend else None,
            value_mid=ra["vmid"] if has_spend else None,
            value_high=ra["vhigh"] if has_spend else None,
        )
        for region, ra in reg.items()
    }
    return MarketValue(
        slug=slug,
        buyers_low=buyers_low,
        buyers_high=buyers_high,
        has_spend=has_spend,
        value_low=(
            sum(ra["vlow"] for ra in reg.values()) if has_spend else None
        ),
        value_mid=(
            sum(ra["vmid"] for ra in reg.values()) if has_spend else None
        ),
        value_high=(
            sum(ra["vhigh"] for ra in reg.values()) if has_spend else None
        ),
        buyable_value=(
            sum(sv.value_mid for sv in segs.values() if sv.buyable)
            if has_spend
            else None
        ),
        criticality=crit,
        segments=segs,
        regions=regions,
        notes=tuple(notes),
    )


def _usd(value: float | None) -> int | None:
    return round(value) if value is not None else None


def _seg_key(seg: str) -> tuple[int, str]:
    return (
        SEGMENT_ORDER.index(seg)
        if seg in SEGMENT_ORDER
        else len(SEGMENT_ORDER),
        seg,
    )


def market_json(mv: MarketValue) -> dict:
    """categories.json block: possible buyers and market value."""
    return {
        "buyers_low": mv.buyers_low,
        "buyers_high": mv.buyers_high,
        "buyers_mid": mv.buyers_mid,
        "value_low_usd": _usd(mv.value_low),
        "value_mid_usd": _usd(mv.value_mid),
        "value_high_usd": _usd(mv.value_high),
        "basis": "market_value" if mv.has_spend else "buyer_count",
        "notes": list(mv.notes),
    }


def lens_json(mv: MarketValue) -> dict:
    """Build-vs-buy lens block; never feeds the opportunity total."""
    crit = mv.criticality
    segments = {}
    for seg in sorted(mv.segments, key=_seg_key):
        sv = mv.segments[seg]
        segments[seg] = {
            "buyers": round(sv.buyers, 1),
            "value_usd": _usd(sv.value_mid),
            "value_low_usd": _usd(sv.value_low),
            "value_high_usd": _usd(sv.value_high),
            "build_in_house": sv.build_in_house,
            "buyable": sv.buyable,
            "evidence": sv.evidence,
            "sources": list(sv.sources),
        }
    return {
        "criticality": (crit.level or None) if crit else None,
        "criticality_why": crit.why if crit else "",
        "best_icp": (crit.best_icp or None) if crit else None,
        "buyable_value_usd": _usd(mv.buyable_value),
        "segments": segments,
    }


def regions_view(
    data: list[tuple[str, estimates.CategoryEstimate, MarketValue]],
) -> dict:
    """``exports/site/regions.json``: every region x kept category.

    A cell's ``evidence`` is ``usage`` when the category has a usage
    estimate there, ``buyers only`` when only buyer-universe rows exist,
    else ``none``. Each region carries a summary of categories with usage
    evidence and the total market value.
    """
    regions = set(parse_counts.STUDY_REGIONS)
    for _, est, mv in data:
        regions.update(est.regions)
        regions.update(mv.regions)
    out: dict[str, dict] = {}
    for region in sorted(regions):
        cells: dict[str, dict] = {}
        n_usage = n_buyers = 0
        total = 0.0
        any_value = False
        for slug, est, mv in data:
            rm = mv.regions.get(region)
            usage = est.regions.get(region)
            n_usage += usage is not None
            n_buyers += rm is not None
            if rm and rm.value_mid is not None:
                total += rm.value_mid
                any_value = True
            cells[slug] = {
                "buyers": (
                    {
                        "low": rm.buyers_low,
                        "high": rm.buyers_high,
                        "mid": rm.buyers_mid,
                    }
                    if rm
                    else None
                ),
                "value_usd": (
                    {
                        "low": _usd(rm.value_low),
                        "mid": _usd(rm.value_mid),
                        "high": _usd(rm.value_high),
                    }
                    if rm and rm.value_mid is not None
                    else None
                ),
                "usage": (
                    {
                        "companies_low": usage.companies_low,
                        "companies_high": usage.companies_high,
                        "grade": usage.grade,
                    }
                    if usage
                    else None
                ),
                "evidence": (
                    "usage" if usage else ("buyers only" if rm else "none")
                ),
            }
        out[region] = {
            "summary": {
                "categories_with_usage": n_usage,
                "categories_with_buyers": n_buyers,
                "total_value_usd": _usd(total) if any_value else None,
            },
            "categories": cells,
        }
    return {"regions": out}
