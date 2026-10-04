import pytest

from lsa import contracts as c


def _count_record(**over):
    kw = {
        "source": "usaspending",
        "family": "procurement",
        "region": "US",
        "category": "core-banking",
        "system": "cobol-mainframe",
        "query": "cobol",
        "count": 42,
        "method": "api-total",
        "counted_at": "2026-10-05T00:00:00Z",
    }
    kw.update(over)
    return c.CountRecord(**kw)


def _evidence_row(**over):
    kw = {
        "source": "g2",
        "family": "reviews",
        "url": "https://example.com/r1",
        "fetched_at": "2026-10-05T00:00:00Z",
        "region": "US",
        "category": "core-banking",
        "system": "cobol-mainframe",
        "org": "Example Bank",
        "excerpt": "still re-keying records into spreadsheets",
        "lane": "count",
    }
    kw.update(over)
    return c.EvidenceRow(**kw)


def test_excerpt_over_30_words_raises():
    _evidence_row(excerpt=" ".join(["w"] * 30))
    with pytest.raises(ValueError):
        _evidence_row(excerpt=" ".join(["w"] * 31))


def test_count_none_allowed():
    rec = _count_record(count=None)
    assert rec.count is None
    assert _count_record(count=0).count == 0


def test_region_must_be_known_code():
    for region in sorted(c.REGIONS):
        _count_record(region=region)
        _evidence_row(region=region)
    with pytest.raises(ValueError):
        _count_record(region="XX")
    with pytest.raises(ValueError):
        _evidence_row(region="XX")
