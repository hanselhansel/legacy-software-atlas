import json
import sys
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from lsa import estimate as est
from lsa.cli import main
from lsa.contracts import CountRecord

ROOT = Path(__file__).resolve().parents[1]


def _record(**over):
    kw = {
        "source": "usaspending",
        "family": "procurement",
        "region": "US",
        "category": "core-banking",
        "system": "cobol-mainframe",
        "query": "cobol",
        "count": 10,
        "method": "api-total",
        "counted_at": "2026-10-05T00:00:00Z",
    }
    kw.update(over)
    return CountRecord(**kw)


def _pass(**over):
    kw = {
        "name": "jobs",
        "family": "jobs",
        "prefilter_keep": 1.0,
        "tokens_per_item": 200,
        "items_per_call": 5,
        "overhead_tokens_per_call": 120,
    }
    kw.update(over)
    return est.Pass(**kw)


def test_estimate_arithmetic_fixed_counts():
    counts = [
        _record(family="jobs", source="indeed", count=100),
        _record(family="jobs", source="seek", count=50),
    ]
    out = est.estimate(counts, [_pass()], price_usd_per_million=0.042)
    pe = out.passes[0]
    assert pe.name == "jobs"
    assert pe.items_counted == 150
    assert pe.items_sent == 150
    assert pe.calls == 30
    assert pe.input_tokens == 150 * 200 + 30 * 120
    assert pe.input_tokens == 33600
    assert pe.usd == pytest.approx(0.0014112, abs=1e-9)
    assert f"{pe.usd:.6f}" == "0.001411"
    assert pe.tokens_measured is True
    assert out.total_usd == pytest.approx(0.0014112, abs=1e-9)
    assert out.target_usd == 25.0
    assert out.within_target is True


def test_packing_ceil():
    counts = [_record(family="jobs", count=9)]
    out = est.estimate(
        counts,
        [_pass(items_per_call=4, tokens_per_item=10)],
        price_usd_per_million=1.0,
    )
    pe = out.passes[0]
    assert pe.items_sent == 9
    assert pe.calls == 3
    assert pe.input_tokens == 9 * 10 + 3 * 120
    assert pe.usd == pytest.approx(450 / 1e6)


def test_prefilter_keep_ceil():
    counts = [_record(family="jobs", count=9)]
    out = est.estimate(
        counts, [_pass(prefilter_keep=0.5)], price_usd_per_million=1.0
    )
    pe = out.passes[0]
    assert pe.items_counted == 9
    assert pe.items_sent == 5
    assert pe.calls == 1


def test_none_counts_reported_uncounted_not_zero():
    counts = [
        _record(family="jobs", source="jobstreet", count=None),
        _record(family="jobs", source="mycareersfuture", count=None),
        _record(family="jobs", source="jobstreet", count=None),
        _record(family="jobs", source="seek", count=7),
    ]
    out = est.estimate(counts, [_pass()], price_usd_per_million=1.0)
    assert out.passes[0].items_counted == 7
    assert out.uncounted_sources == ("jobstreet", "mycareersfuture")


def test_default_tokens_flagged_when_unmeasured():
    counts = [_record(family="jobs", count=10)]
    out = est.estimate(
        counts,
        [_pass(tokens_per_item=None)],
        price_usd_per_million=1.0,
        default_tokens_per_item=400,
    )
    pe = out.passes[0]
    assert pe.tokens_measured is False
    assert pe.input_tokens == 10 * 400 + 2 * 120


def test_family_filtering():
    counts = [
        _record(family="jobs", source="seek", count=3),
        _record(family="reviews", source="g2", count=999),
    ]
    out = est.estimate(counts, [_pass()], price_usd_per_million=1.0)
    assert out.passes[0].items_counted == 3


def test_over_target_flagged():
    counts = [_record(family="jobs", count=10_000_000)]
    out = est.estimate(
        counts,
        [_pass(tokens_per_item=100)],
        price_usd_per_million=0.042,
        target_usd=25.0,
    )
    assert out.total_usd > 25.0
    assert out.within_target is False


def test_pass_validation():
    with pytest.raises(ValueError):
        _pass(prefilter_keep=0.0)
    with pytest.raises(ValueError):
        _pass(prefilter_keep=1.5)
    with pytest.raises(ValueError):
        _pass(items_per_call=0)
    with pytest.raises(ValueError):
        _pass(tokens_per_item=0)
    with pytest.raises(ValueError):
        _pass(overhead_tokens_per_call=-1)


def test_load_passes_reads_repo_config():
    """The gate config: every counted family has a pass with a measured window."""
    passes = est.load_passes(ROOT / "configs" / "passes.toml")
    families = {p.family for p in passes}
    assert {"procurement", "jobs", "jobs-pages", "vendor", "integrator", "hn"} <= families
    for p in passes:
        assert p.tokens_per_item is not None
        assert 0.0 < p.prefilter_keep <= 1.0


def test_load_passes_optional_fields(tmp_path):
    cfg = tmp_path / "passes.toml"
    cfg.write_text(
        "[[pass]]\n"
        'name = "hn-pain"\n'
        'family = "hn"\n'
        "prefilter_keep = 0.25\n"
        "tokens_per_item = 850\n"
        "items_per_call = 10\n"
        "overhead_tokens_per_call = 90\n",
        encoding="utf-8",
    )
    (p,) = est.load_passes(cfg)
    assert p.name == "hn-pain"
    assert p.prefilter_keep == 0.25
    assert p.tokens_per_item == 850
    assert p.items_per_call == 10
    assert p.overhead_tokens_per_call == 90


def _write_counts_parquet(path: Path, rows: list[dict]) -> None:
    cols = [
        "source",
        "family",
        "region",
        "category",
        "system",
        "query",
        "count",
        "method",
        "counted_at",
    ]
    table = pa.table({c: [r.get(c) for r in rows] for c in cols})
    pq.write_table(table, path)


def test_cli_estimate_json(tmp_path, monkeypatch, capsys):
    rows = [
        {
            "source": "seek",
            "family": "jobs",
            "region": "AU",
            "category": "core-banking",
            "system": "cobol-mainframe",
            "query": "cobol",
            "count": 40,
            "method": "search-total",
            "counted_at": "2026-10-05T00:00:00Z",
        },
        {
            "source": "naukri",
            "family": "jobs",
            "region": "IN",
            "category": "core-banking",
            "system": "cobol-mainframe",
            "query": "cobol",
            "count": 60,
            "method": "search-total",
            "counted_at": "2026-10-05T00:00:00Z",
        },
        {
            "source": "jobstreet",
            "family": "jobs",
            "region": "SG",
            "category": "core-banking",
            "system": "cobol-mainframe",
            "query": "cobol",
            "count": None,
            "method": "search-total",
            "counted_at": "2026-10-05T00:00:00Z",
        },
        {
            "source": "g2",
            "family": "reviews",
            "region": "US",
            "category": "core-banking",
            "system": "cobol-mainframe",
            "query": "as/400",
            "count": 5,
            "method": "search-total",
            "counted_at": "2026-10-05T00:00:00Z",
        },
    ]
    counts_path = tmp_path / "counts.parquet"
    _write_counts_parquet(counts_path, rows)
    passes_path = tmp_path / "passes.toml"
    passes_path.write_text(
        "[[pass]]\n"
        'name = "jobs"\n'
        'family = "jobs"\n'
        "prefilter_keep = 1.0\n"
        "tokens_per_item = 100\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "lsa",
            "estimate",
            "--counts",
            str(counts_path),
            "--passes",
            str(passes_path),
            "--json",
        ],
    )
    main()
    data = json.loads(capsys.readouterr().out)
    (pe,) = data["passes"]
    assert pe["name"] == "jobs"
    assert pe["items_counted"] == 100
    assert pe["items_sent"] == 100
    assert pe["calls"] == 20
    assert pe["input_tokens"] == 12400
    assert pe["usd"] == pytest.approx(0.0005208)
    assert pe["tokens_measured"] is True
    assert data["total_usd"] == pytest.approx(0.0005208)
    assert data["target_usd"] == 25.0
    assert data["within_target"] is True
    assert data["uncounted_sources"] == ["jobstreet"]
