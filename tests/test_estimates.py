from lsa import catconfig, estimates, labels


def _item(**over):
    kw = {
        "item_id": "src:1",
        "family": "jobs",
        "url": "https://example.test/1",
        "weight": 1.0,
        "region": "US",
        "category": "core-banking",
        "segment": "enterprise",
        "industry": "banking_finance",
        "status": "in_use",
        "pain": None,
        "reason": None,
        "sets": frozenset({"job-apis-industry-segment-legacy-in-use@v2"}),
    }
    kw.update(over)
    return labels.LabelledItem(**kw)


def _bu_row(region="US", approx_count="1,000", register="reg", slug="core-banking"):
    return {
        "category": slug,
        "region": region,
        "register": register,
        "approx_count": approx_count,
        "source": "https://example.test/reg",
    }


def _vendor_row(
    regions="US", disclosed="100", slug="core-banking", product="P"
):
    return {
        "category": slug,
        "vendor": "V",
        "product": product,
        "first_shipped": "1980",
        "disclosed_customers": disclosed,
        "regions": regions,
        "source": "https://example.test/v",
    }


CFG = catconfig.CategoryConfig(slug="core-banking")


def test_weight_of():
    assert labels.weight_of({"query_count": 36, "sampled": 30}) == 1.2
    assert labels.weight_of({"query_count": None, "sampled": None}) == 1.0
    assert labels.weight_of({"query_count": 10, "sampled": 0}) == 1.0
    assert labels.weight_of({}) == 1.0


def test_confirmed_requires_matching_question_set():
    items = [
        _item(item_id="j:1", status="in_use"),
        _item(
            item_id="j:2",
            status="in_use",
            sets=frozenset({"job-apis-industry-segment-legacy-in-use@v1"}),
        ),
        _item(item_id="j:3", status="neither"),
        _item(item_id="j:4", status="being_replaced"),
        _item(
            item_id="t:1",
            family="procurement",
            sets=frozenset({"tenders-which-category@v2"}),
            status="neither",
        ),
        _item(
            item_id="t:2",
            family="procurement",
            sets=frozenset({"tenders-which-category@v1"}),
        ),
    ]
    got = {i.item_id for i in labels.confirmed(items, "core-banking")}
    assert got == {"j:1", "t:1"}
    strict = {
        i.item_id
        for i in labels.confirmed(
            items,
            "core-banking",
            tender_require_status=frozenset({"in_use", "being_replaced"}),
        )
    }
    assert strict == {"j:1"}


def test_estimate_low_is_max_of_vendor_and_confirmed():
    est = estimates.estimate_category(
        "core-banking",
        items=[_item(), _item(item_id="src:2")],
        buyer_universe=[_bu_row()],
        vendors=[_vendor_row(disclosed="500 banks")],
        config=CFG,
    )
    s = est.regions["US"]
    # low = max(500, 2), high = min(1000, 500*3)
    assert s.companies_low == 500
    assert s.companies_high == 1000


def test_estimate_confirmed_floor_and_weighting():
    est = estimates.estimate_category(
        "core-banking",
        items=[
            _item(item_id="a", weight=10.0),
            _item(item_id="b", weight=10.0),
            _item(item_id="c", weight=10.0),
        ],
        buyer_universe=[_bu_row(approx_count="10,000")],
        vendors=[],
        config=CFG,
    )
    s = est.regions["US"]
    assert s.companies_low == 3
    assert s.companies_high == 9  # min(10,000 universe, 3 x default 3)
    assert "weighted 30" in "; ".join(s.notes)


def test_grade_a_three_agreeing_families():
    # vendor 800, confirmed weighted 1000/1.0=1000 -> ratio 1.25;
    # universe mid 1000 x 1.0 = 1000; all within 2x -> A
    est = estimates.estimate_category(
        "core-banking",
        items=[_item(item_id=str(i), weight=250.0) for i in range(4)],
        buyer_universe=[_bu_row(approx_count="1,000")],
        vendors=[_vendor_row(disclosed="800 banks")],
        config=CFG,
    )
    s = est.regions["US"]
    assert s.companies_low == 800
    assert s.companies_high == 1000
    assert s.grade == "A"
    assert set(s.families) == {
        estimates.FAM_UNIVERSE,
        estimates.FAM_VENDOR,
        estimates.FAM_CONFIRMED,
    }


def test_grade_b_two_agreeing_families():
    # vendor 100 vs confirmed 100 agree; universe mid 5000 is off by >2x.
    est = estimates.estimate_category(
        "core-banking",
        items=[_item(item_id=str(i), weight=100.0) for i in range(1)],
        buyer_universe=[_bu_row(approx_count="10,000")],
        vendors=[_vendor_row(disclosed="50 banks")],
        config=CFG,
    )
    s = est.regions["US"]
    assert s.grade == "B"


def test_grade_c_single_family():
    est = estimates.estimate_category(
        "core-banking",
        items=[_item(item_id="a", weight=5.0)],
        buyer_universe=[_bu_row()],
        vendors=[],
        config=CFG,
    )
    s = est.regions["US"]
    assert s.grade == "C"
    assert s.families == (
        estimates.FAM_CONFIRMED,
        estimates.FAM_UNIVERSE,
    ) or set(s.families) >= {estimates.FAM_CONFIRMED}


def test_region_without_usage_evidence_skipped():
    est = estimates.estimate_category(
        "core-banking",
        items=[],
        buyer_universe=[_bu_row()],
        vendors=[],
        config=CFG,
    )
    assert est.regions == {}
    assert any("no usage evidence" in n for n in est.notes)


def test_multi_region_vendor_row_goes_global():
    est = estimates.estimate_category(
        "core-banking",
        items=[],
        buyer_universe=[],
        vendors=[_vendor_row(regions="US, UK, EU", disclosed="300 banks")],
        config=CFG,
    )
    assert "US" not in est.regions
    g = est.regions["global"]
    assert g.companies_low == 300
    assert g.companies_high == 900


def test_multi_region_policy_each():
    cfg = catconfig.CategoryConfig(
        slug="core-banking", multi_region_policy="each"
    )
    est = estimates.estimate_category(
        "core-banking",
        items=[],
        buyer_universe=[],
        vendors=[_vendor_row(regions="US, UK", disclosed="300 banks")],
        config=cfg,
    )
    assert est.regions["US"].companies_low == 300
    assert est.regions["UK"].companies_low == 300


def test_universe_and_vendor_overrides_and_skips():
    cfg = catconfig.CategoryConfig(
        slug="core-banking",
        universe_skip=("bad reg",),
        universe_overrides={"US": (2000.0, 2000.0)},
        vendor_exclude=("Old P",),
        vendor_overrides={"V | P": 700.0},
    )
    est = estimates.estimate_category(
        "core-banking",
        items=[],
        buyer_universe=[
            _bu_row(register="good reg"),
            _bu_row(register="bad reg", approx_count="9,999"),
        ],
        vendors=[
            _vendor_row(disclosed="unknown"),
            _vendor_row(regions="UK", disclosed="50 banks", product="Q"),
            _vendor_row(
                regions="US", disclosed="9,999 banks", product="Old P"
            ),
        ],
        config=cfg,
    )
    assert est.regions["US"].companies_high == 2000
    assert est.regions["US"].companies_low == 700
    assert est.regions["UK"].companies_low == 50


def test_unparseable_universe_is_noted_and_skipped():
    est = estimates.estimate_category(
        "core-banking",
        items=[_item()],
        buyer_universe=[_bu_row(approx_count="not verified")],
        vendors=[],
        config=CFG,
    )
    assert "US" in est.regions
    assert any("unparsed" in n for n in est.notes)
    assert "no buyer universe bound" in "; ".join(est.regions["US"].notes)


def test_segments_from_confirmed_jobs_only():
    est = estimates.estimate_category(
        "core-banking",
        items=[
            _item(item_id="a", segment="smb"),
            _item(item_id="b", segment="smb"),
            _item(item_id="c", segment="government"),
            _item(item_id="d", segment="unclear"),
            _item(
                item_id="t",
                family="procurement",
                segment=None,
                sets=frozenset({"tenders-which-category@v2"}),
            ),
        ],
        buyer_universe=[],
        vendors=[],
        config=CFG,
    )
    assert set(est.segments) == {"government", "smb"}
    assert est.segments["smb"].companies_low == 2
    assert est.segments["smb"].grade == "C"
    assert any("no segment label" in n for n in est.notes)


def test_load_config_roundtrip(tmp_path):
    path = catconfig.ensure_config("x-cat", "X Cat", tmp_path)
    cfg = catconfig.load_config("x-cat", path)
    assert cfg.multiplier == 3.0
    assert cfg.tender_question_set == "tenders-which-category@v2"
    assert cfg.job_in_use_choices == ("in_use",)


def test_load_config_overrides(tmp_path):
    p = tmp_path / "x.toml"
    p.write_text(
        'slug = "x"\n'
        "[estimate]\nmultiplier = 5.0\ndetection_rate = 2.0\n"
        'agree_within = 1.5\n'
        "[vendors]\nmulti_region_policy = \"each\"\n"
    )
    cfg = catconfig.load_config("x", p)
    assert cfg.multiplier == 5.0
    assert cfg.detection_rate == 2.0
    assert cfg.agree_within == 1.5
    assert cfg.multi_region_policy == "each"


def test_universe_skips_non_buyer_units_and_uses_classified_counts():
    cfg = catconfig.CategoryConfig(slug="x")
    rows = [
        {"category": "x", "region": "US", "register": "loans", "approx_count": "36,000,000 loans", "unit": "accounts_or_loans", "buyers_low": "", "buyers_high": ""},
        {"category": "x", "region": "US", "register": "banks", "approx_count": "about 4,000", "unit": "organisations", "buyers_low": "4000", "buyers_high": "4200"},
    ]
    per, notes = estimates._universe("x", rows, cfg)
    assert per["US"]["low"] == 4000 and per["US"]["high"] == 4200
    assert any("not buyers" in n for n in notes)


def test_slice_caps_low_at_buyer_universe():
    notes: list[str] = []
    cfg = catconfig.CategoryConfig(slug="x")
    sl = estimates._slice("AU", 2_600_000, 8, {"buyer_universe": 8}, cfg, notes, [])
    assert sl.companies_low == 8 and sl.companies_high == 8
    assert any("capped at buyer universe" in n for n in notes)
