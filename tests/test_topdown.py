"""Top-down calibration keeps the bottom-up split and replaces the total."""

import math

import pytest

from lsa import market, topdown
from lsa.market import MarketValue, RegionMarket, SegmentMarket


def _mv():
    seg = lambda v, b: SegmentMarket(1, v, v, v, "rare" if b else "common", b, "", ())
    return MarketValue(
        slug="x", buyers_low=1, buyers_high=1, has_spend=True,
        value_low=100.0, value_mid=100.0, value_high=100.0, buyable_value=75.0,
        criticality=None,
        segments={"smb": seg(75.0, True), "enterprise": seg(25.0, False)},
        regions={"US": RegionMarket(1, 1, 60.0, 60.0, 60.0), "EU": RegionMarket(1, 1, 40.0, 40.0, 40.0)},
        notes=(),
    )


def test_calibrate_uses_top_down_total_and_bottom_up_split():
    out = topdown.calibrate(_mv(), {"legacy_low_usd": "1e9", "legacy_high_usd": "4e9"})
    mid = math.sqrt(1e9 * 4e9)
    assert out.value_mid == pytest.approx(mid)
    assert out.value_low == 1e9 and out.value_high == 4e9
    assert out.regions["US"].value_mid == pytest.approx(0.6 * mid)
    assert out.buyable_value == pytest.approx(0.75 * mid)
    assert any("top-down" in n for n in out.notes)


def test_calibrate_without_row_is_unchanged():
    mv = _mv()
    assert topdown.calibrate(mv, None) is mv
    assert market.MarketValue is MarketValue
