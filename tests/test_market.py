import pytest

from lsa import criticality, estimates, market, scores
from lsa.rubric import Rubric

RUBRIC = Rubric(
    weights={"size": 1.0, "pain": 1.0, "ai_fit": 1.0, "lockin": 1.0, "crowding": 1.0},
    value_bins_usd=(100e6, 1e9, 5e9, 20e9),
    buyer_bins=(100.0, 1000.0, 10000.0, 100000.0),
    s3_strong=2.0,
    s3_weak=1.0,
    hn_pain_min_comments=5,
    legacy_in_use_share=0.30,
    share_weights={"high": 3.0, "medium": 2.0, "low": 1.0},
    s2_strong=2.0,
    s2_weak=1.0,
    s4_strong=1.0,
    regulation_reason=1.0,
    count_bins=(2.0, 5.0, 9.0),
    funding_usd_over=500_000_000.0,
)


def _crit_row(
    segment,
    level="critical",
    why="runs the money",
    icp="enterprise",
    bih="rare",
    low="100000",
    high="200000",
    evidence="survey says",
    sources="https://a.test; https://b.test",
):
    return {
        "category": "x",
        "criticality": level,
        "criticality_why": why,
        "best_icp": icp,
        "segment": segment,
        "build_in_house": bih,
        "spend_low": low,
        "spend_high": high,
        "evidence": evidence,
        "sources": sources,
    }


def _bu_row(region="US", low=1000, high=1200, shares=None, register="reg"):
    row = {
        "category": "x",
        "region": region,
        "register": register,
        "approx_count": "",
        "source": "https://s.test",
        "unit": "organisations",
        "buyers_low": str(low),
        "buyers_high": str(high),
    }
    for seg, share in (shares or {}).items():
        row[f"seg_{seg}"] = str(share)
    return row


def _crit(rows):
    return criticality.criticality_map(rows)["x"]


def _mv(value_mid, buyers=1100.0):
    return market.MarketValue(
        slug="x",
        buyers_low=buyers * 10 / 11,
        buyers_high=buyers * 12 / 11,
        has_spend=True,
        value_low=value_mid / 2,
        value_mid=value_mid,
        value_high=value_mid * 2,
        buyable_value=value_mid,
        criticality=None,
        segments={},
        regions={},
        notes=(),
    )


def _est(midpoints):
    return estimates.CategoryEstimate(
        slug="x",
        regions={
            f"r{i}": estimates.SliceEstimate(
                key=f"r{i}",
                companies_low=low,
                companies_high=high,
                grade="C",
                families=(),
                notes=(),
                sources=(),
            )
            for i, (low, high) in enumerate(midpoints)
        },
        segments={},
        notes=(),
    )


def test_criticality_map_parses_spend_and_sources():
    crit = _crit(
        [
            _crit_row("Mid Market", low="$40k", high="1.2M"),
            _crit_row("enterprise", bih="some"),
        ]
    )
    assert crit.level == "critical"
    assert crit.best_icp == "enterprise"
    mm = crit.segments["mid_market"]
    assert mm.spend_low == 40_000
    assert mm.spend_high == 1_200_000
    assert mm.bounds() == (40_000, 1_200_000)
    assert mm.sources == ("https://a.test", "https://b.test")
    assert mm.build_in_house == "rare"
    assert crit.segments["enterprise"].build_in_house == "some"


def test_criticality_map_blank_spend_is_none():
    crit = _crit([_crit_row("smb", low="", high="")])
    assert crit.segments["smb"].bounds() is None


def test_value_arithmetic_with_shares_and_spends():
    crit = _crit(
        [
            _crit_row("enterprise", low="100000", high="200000"),
            _crit_row("smb", low="10000", high="20000"),
        ]
    )
    rows = [_bu_row(shares={"enterprise": 0.5, "smb": 0.5})]
    mv = market.market_value("x", rows, crit)
    assert mv.buyers_low == 1000 and mv.buyers_high == 1200
    assert mv.buyers_mid == 1100
    # low: 1000 x (0.5x100k + 0.5x10k) = 55M; mid: 1100 x 82.5k = 90.75M
    # high: 1200 x (0.5x200k + 0.5x20k) = 132M
    assert mv.value_low == 55_000_000
    assert mv.value_mid == 90_750_000
    assert mv.value_high == 132_000_000
    assert mv.segments["enterprise"].buyers == 550
    assert mv.segments["enterprise"].value_mid == 82_500_000
    assert mv.segments["smb"].value_mid == 8_250_000
    assert mv.regions["US"].value_mid == 90_750_000


def test_missing_shares_fall_back_to_best_icp():
    crit = _crit(
        [
            _crit_row("enterprise", icp="mid_market", low="100", high="100"),
            _crit_row("mid_market", icp="mid_market", low="50", high="50"),
        ]
    )
    mv = market.market_value("x", [_bu_row()], crit)
    assert mv.segments["mid_market"].buyers == 1100
    assert mv.value_mid == 1100 * 50
    assert any(
        "no segment shares" in n and "mid_market" in n for n in mv.notes
    )


def test_missing_spend_segment_contributes_zero_and_is_noted():
    crit = _crit([_crit_row("enterprise")])
    rows = [_bu_row(shares={"enterprise": 0.8, "government": 0.2})]
    mv = market.market_value("x", rows, crit)
    assert mv.segments["government"].value_mid == 0
    assert mv.value_mid == pytest.approx(1100 * 0.8 * 150_000)
    assert any("no spend data for segment(s) government" in n for n in mv.notes)


def test_no_criticality_falls_back_to_buyer_count():
    mv = market.market_value("x", [_bu_row()], None)
    assert not mv.has_spend
    assert mv.value_mid is None
    assert mv.buyers_mid == 1100
    assert any("size uses buyer count" in n for n in mv.notes)


def test_criticality_without_spend_falls_back():
    crit = _crit([_crit_row("enterprise", low="", high="")])
    mv = market.market_value("x", [_bu_row()], crit)
    assert not mv.has_spend
    assert mv.value_mid is None
    assert any("no spend" in n for n in mv.notes)


def test_non_buyer_units_are_skipped():
    crit = _crit([_crit_row("enterprise")])
    rows = [
        {
            "category": "x",
            "region": "US",
            "register": "loans",
            "approx_count": "36,000,000 loans",
            "source": "",
            "unit": "accounts_or_loans",
            "buyers_low": "",
            "buyers_high": "",
        },
        _bu_row(),
    ]
    mv = market.market_value("x", rows, crit)
    assert mv.buyers_mid == 1100
    assert any("not buyers" in n for n in mv.notes)


def test_shares_not_summing_to_one_noted():
    crit = _crit([_crit_row("enterprise")])
    mv = market.market_value(
        "x", [_bu_row(shares={"enterprise": 0.4})], crit
    )
    assert any("not summing to 1" in n for n in mv.notes)


@pytest.mark.parametrize(
    "value,score",
    [
        (0, 1),
        (99e6, 1),
        (100e6, 2),
        (999e6, 2),
        (1e9, 3),
        (4.9e9, 3),
        (5e9, 4),
        (19.9e9, 4),
        (20e9, 5),
        (500e9, 5),
    ],
)
def test_value_bins(value, score):
    part = scores.size_part(_est([(10, 20)]), RUBRIC, market_view=_mv(value))
    assert part.score == score
    assert part.detail["basis"] == "market_value"
    assert part.detail["value_usd"]["mid"] == value


def test_size_part_falls_back_to_buyer_bins_without_spend():
    mv = market.market_value("x", [_bu_row()], None)
    part = scores.size_part(
        _est([(10, 20)]), RUBRIC, universe_mid=mv.buyers_mid, market_view=mv
    )
    assert part.detail["basis"] == "buyer_universe"
    assert part.detail["midpoint"] == 1100
    assert part.score == 3  # 1100 >= 1000 bin
    assert any("no spend data" in e for e in part.evidence)


def test_size_part_falls_back_to_companies_using():
    part = scores.size_part(_est([(50, 150)]), RUBRIC)
    assert part.detail["basis"] == "companies_using"
    assert part.detail["midpoint"] == 100
    assert part.score == 2


def test_buyable_logic_and_buyable_value():
    crit = _crit(
        [
            _crit_row("enterprise", bih="common", low="100", high="100"),
            _crit_row("mid_market", bih="some", low="50", high="50"),
            _crit_row("smb", bih="rare", low="10", high="10"),
            _crit_row("government", bih="common", low="1", high="1"),
        ]
    )
    rows = [
        _bu_row(
            shares={
                "enterprise": 0.5,
                "mid_market": 0.3,
                "smb": 0.2,
            }
        )
    ]
    mv = market.market_value("x", rows, crit)
    assert mv.segments["enterprise"].buyable is False
    assert mv.segments["mid_market"].buyable is True
    assert mv.segments["smb"].buyable is True
    # government is in the lens with 0 attributed buyers
    assert mv.segments["government"].buyable is False
    # buyable value: mid_market 1100x0.3x50 + smb 1100x0.2x10
    assert mv.buyable_value == 1100 * 0.3 * 50 + 1100 * 0.2 * 10
    assert mv.value_mid == pytest.approx(
        1100 * (0.5 * 100 + 0.3 * 50 + 0.2 * 10)
    )


def test_market_json_and_lens_json_shapes():
    crit = _crit(
        [
            _crit_row("enterprise", bih="common"),
            _crit_row("smb", low="5000", high="10000"),
        ]
    )
    mv = market.market_value(
        "x", [_bu_row(shares={"enterprise": 0.5, "smb": 0.5})], crit
    )
    mj = market.market_json(mv)
    assert mj["basis"] == "market_value"
    assert mj["value_mid_usd"] == round(mv.value_mid)
    assert mj["buyers_mid"] == 1100
    lens = market.lens_json(mv)
    assert lens["criticality"] == "critical"
    assert lens["criticality_why"] == "runs the money"
    assert lens["best_icp"] == "enterprise"
    assert set(lens["segments"]) == {"enterprise", "smb"}
    ent = lens["segments"]["enterprise"]
    assert ent["build_in_house"] == "common"
    assert ent["buyable"] is False
    assert ent["sources"] == ["https://a.test", "https://b.test"]
    assert lens["buyable_value_usd"] == round(
        mv.segments["smb"].value_mid
    )


def test_regions_view_evidence_levels():
    crit = _crit([_crit_row("enterprise")])
    rows = [
        _bu_row(region="US", shares={"enterprise": 1.0}),
        _bu_row(region="UK", low=10, high=10, shares={"enterprise": 1.0}),
    ]
    mv = market.market_value("x", rows, crit)
    est = _est([(10, 20)])  # region key r0, not a study region
    usage_est = estimates.CategoryEstimate(
        slug="x",
        regions={
            "US": estimates.SliceEstimate(
                key="US",
                companies_low=10,
                companies_high=20,
                grade="B",
                families=("vendor_disclosed",),
                notes=(),
                sources=(),
            )
        },
        segments={},
        notes=(),
    )
    data = [("x", usage_est, mv), ("y", est, market.market_value("y", [], None))]
    view = market.regions_view(data)["regions"]
    us = view["US"]["categories"]["x"]
    assert us["evidence"] == "usage"
    assert us["usage"]["companies_low"] == 10
    assert us["usage"]["grade"] == "B"
    assert us["buyers"]["mid"] == 1100
    assert us["value_usd"]["mid"] == round(mv.regions["US"].value_mid)
    uk = view["UK"]["categories"]["x"]
    assert uk["evidence"] == "buyers only"
    assert uk["usage"] is None
    assert uk["buyers"]["mid"] == 10
    none_cell = view["IN"]["categories"]["x"]
    assert none_cell["evidence"] == "none"
    assert none_cell["buyers"] is None
    # second category has no data anywhere
    assert view["US"]["categories"]["y"]["evidence"] == "none"
    # observed non-study region (r0) is included too
    assert "r0" in view
    summary = view["US"]["summary"]
    assert summary["categories_with_usage"] == 1
    assert summary["categories_with_buyers"] == 1
    assert summary["total_value_usd"] == round(mv.regions["US"].value_mid)
    assert view["IN"]["summary"]["categories_with_usage"] == 0


def test_best_segment_prefers_most_documented_without_icp():
    crit = _crit(
        [
            _crit_row("smb", icp="not-a-segment", sources=""),
            _crit_row("enterprise", icp="not-a-segment", evidence="long evidence text here"),
        ]
    )
    assert market._best_segment(crit) == "enterprise"


def test_load_criticality_reads_csv(tmp_path):
    p = tmp_path / "criticality.csv"
    import csv

    with open(p, "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "category",
                "criticality",
                "criticality_why",
                "best_icp",
                "segment",
                "build_in_house",
                "spend_low",
                "spend_high",
                "evidence",
                "sources",
            ],
        )
        w.writeheader()
        w.writerow(_crit_row("enterprise"))
        w.writerow(_crit_row("smb", low="", high=""))
    got = criticality.load_criticality(p)
    assert set(got["x"].segments) == {"enterprise", "smb"}
    assert criticality.load_criticality(tmp_path / "none.csv") == {}
