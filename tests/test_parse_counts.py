import pytest

from lsa import parse_counts as pc


@pytest.mark.parametrize(
    "text,low,high",
    [
        ("4,238 FDIC-insured institutions (Q2 2026)", 4238, 4238),
        ("4,000 to 5,000 banks", 4000, 5000),
        ("between 1,200 and 1,500 firms", 1200, 1500),
        (
            (
                "About 250+ banks, 44 building societies and about 380 "
                "credit unions (September 2026 lists, counts approximate)"
            ),
            674,
            674,
        ),
        (
            (
                "6 local banks, 10 qualifying full banks, 20 full banks, "
                "95 wholesale banks, 21 merchant banks, 3 finance companies"
            ),
            155,
            155,
        ),
        (
            (
                "114 significant entities directly supervised by the ECB "
                "(cut-off 1 Jan 2025). Search snippets put less significant "
                "institutions at about 1,800, but I did not verify that "
                "from an opened page"
            ),
            1914,
            1914,
        ),
        ("105 commercial banks (bank umum), 1,339 BPR, about 174 BPRS", 1618, 1618),
    ],
)
def test_sum_or_range(text, low, high):
    assert pc.parse_sum_or_range(text)[:2] == (low, high)


@pytest.mark.parametrize(
    "text",
    [
        "",
        "not verified from an opened page",
        "unknown",
        "no register gives a total",
    ],
)
def test_sum_or_range_unparseable(text):
    low, high, notes = pc.parse_sum_or_range(text)
    assert low is None and high is None
    assert notes


def test_sum_or_range_ignores_small_dash_fragments():
    # "3-to-5-year" is a duration, not a count range; hyphen-glued
    # numbers do not parse, so only the trailing count lands.
    low, high, _ = pc.parse_sum_or_range("3-to-5-year terms at 44 banks")
    assert (low, high) == (44, 44)


@pytest.mark.parametrize(
    "text,count",
    [
        ("520 banks with assets from $1B to over $55B (FY2025 10-K)", 520),
        ("About 715 credit unions, $20M to $33B assets", 715),
        ("Over 170 banks, de novo to $2B assets (FY2025 10-K)", 170),
        ("over 950 core banking clients and 600 digital banking clients", 950),
        ("500+ customers, 400+ in cloud (April 2023)", 500),
        ("110+ operators in 80+ countries", 110),
        ("2,100+ properties in 2003", 2100),
        ("27 million electricity customers", 27e6),
        ("322 bank locations, 93 countries, 15 million transactions", 322),
    ],
)
def test_first_count(text, count):
    got, _ = pc.parse_first_count(text)
    assert got == count


@pytest.mark.parametrize(
    "text",
    [
        "Not disclosed at product level",
        "No vendor-disclosed count found",
        "unknown",
        "",
    ],
)
def test_first_count_unparseable(text):
    got, notes = pc.parse_first_count(text)
    assert got is None
    assert notes


def test_first_count_skips_years_and_forms():
    got, _ = pc.parse_first_count("(FY2025 10-K) 260 banks")
    assert got == 260


def test_parse_year():
    assert pc.parse_year("520 banks (FY2025 10-K)") == "FY2025"
    assert pc.parse_year("500+ customers (April 2023)") == "2023"
    assert pc.parse_year("not dated") is None


@pytest.mark.parametrize(
    "text,usd",
    [
        ("About $510M+ across Series A-D ($160M Series D, $2.7B valuation)", 510e6),
        ("Series E EUR235M (about $266M)", 266e6),
        ("Acquired by Visa for $1B all cash", 1e9),
        ("$45M in Jan 2024", 45e6),
        ("EUR387M raised in total", None),
        ("amount undisclosed", None),
    ],
)
def test_parse_usd(text, usd):
    assert pc.parse_usd(text) == usd


@pytest.mark.parametrize(
    "text,expected",
    [
        ("US", {"US"}),
        ("US, Canada", {"US"}),
        ("EU (Germany)", {"EU"}),
        ("Indonesia", {"ID"}),
        ("Vietnam", {"VN"}),
        ("IN, Middle East, SE Asia", {"IN", "SG", "ID", "VN", "MY", "TH", "PH"}),
        (
            "Global: US, UK, APAC incl. Australia",
            {"US", "UK", "SG", "IN", "ID", "VN", "MY", "TH", "PH", "AU"},
        ),
        ("Global, 70+ countries", {"global"}),
        ("Global (all 11 study regions)", {"global"}),
        ("UK, Ireland", {"UK", "EU"}),
        ("Australia, NZ", {"AU"}),
        ("Singapore", {"SG"}),
        ("DE, AT, CH and other EU", {"EU"}),
    ],
)
def test_resolve_regions(text, expected):
    got, _ = pc.resolve_regions(text)
    assert got == expected


def test_resolve_regions_no_match():
    got, notes = pc.resolve_regions("Same as above")
    assert got == set()
    assert notes


@pytest.mark.parametrize(
    "raw,code",
    [
        ("US", "US"),
        ("EU (EEA)", "EU"),
        ("EU/EEA", "EU"),
        ("SG (composite)", "SG"),
        ("US (local)", "US"),
        ("Global (cross-check)", "global"),
        ("IN (health)", "IN"),
    ],
)
def test_norm_universe_region(raw, code):
    assert pc.norm_universe_region(raw) == code
