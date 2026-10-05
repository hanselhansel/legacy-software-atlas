"""Per-site total parsing and robots-first behaviour for job pages."""

from pathlib import Path

import httpx
import pytest

from lsa.sources import http, jobpages

FIXTURES = Path(__file__).parent.parent / "fixtures" / "jobpages"

ROBOTS_ALLOW = "User-agent: *\nDisallow:\n"
ROBOTS_DENY = "User-agent: *\nDisallow: /\n"


def _client(handler):
    return http.make_client(transport=httpx.MockTransport(handler))


def _fixture(name: str) -> str:
    return (FIXTURES / name).read_text()


@pytest.mark.parametrize(
    ("site_key", "fixture", "expected"),
    [
        ("seek-au", "seek.html", 1234),
        ("jobsdb-th", "jobsdb.html", 62),
        ("jobthai", "jobthai.html", 56),
        ("itviec", "itviec.html", 42),
        ("careerviet", "careerviet.html", 3102),
        ("topcv", "topcv.html", 789),
        ("careersgov-sg", "careersgov.html", 64),
        ("indeed-au", "indeed.html", 1205),
    ],
)
def test_parse_total_per_site(site_key, fixture, expected):
    site = next(s for s in jobpages.SITES if s.key == site_key)
    assert site.parse_total(_fixture(fixture)) == expected


def test_parse_total_missing_returns_none():
    site = next(s for s in jobpages.SITES if s.key == "seek-au")
    assert site.parse_total(_fixture("no_total.html")) is None


def test_robots_disallow_never_fetches(no_sleep):
    requested = []

    def handler(request):
        requested.append(request.url.path)
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text=ROBOTS_DENY)
        return httpx.Response(200, text=_fixture("seek.html"))

    client = _client(handler)
    site = jobpages.SITES[0]
    value, method = jobpages.count_site(
        site, "cobol", client, get_kwargs=no_sleep
    )
    assert value is None
    assert method == "robots-disallowed"
    assert "/robots.txt" in requested
    assert all(path == "/robots.txt" for path in requested)


def test_count_site_parses_fixture(no_sleep):
    def handler(request):
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text=ROBOTS_ALLOW)
        return httpx.Response(200, text=_fixture("seek.html"))

    client = _client(handler)
    site = next(s for s in jobpages.SITES if s.key == "seek-au")
    value, method = jobpages.count_site(
        site, "cobol", client, get_kwargs=no_sleep
    )
    assert value == 1234
    assert method == "search-result-total"


def test_http_error_returns_none(no_sleep):
    def handler(request):
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text=ROBOTS_ALLOW)
        return httpx.Response(403, text="challenge")

    client = _client(handler)
    site = jobpages.SITES[0]
    value, method = jobpages.count_site(
        site, "cobol", client, get_kwargs=no_sleep
    )
    assert value is None
    assert method == "http-403"


def test_count_picks_max_across_region(monkeypatch):
    """VN query: every site returns its own total; count() takes the max."""
    totals = {"topcv": 789, "itviec": 42, "careerviet": 3102}

    def fake_count_site(site, query, client, *, get_kwargs=None):
        return totals[site.key], "search-result-total"

    monkeypatch.setattr(jobpages, "count_site", fake_count_site)
    assert jobpages.count("core banking", "VN", None) == 3102


def test_count_none_when_all_sites_fail(monkeypatch):
    monkeypatch.setattr(
        jobpages,
        "count_site",
        lambda site, query, client, *, get_kwargs=None: (None, "http-403"),
    )
    assert jobpages.count("core banking", "VN", None) is None


def test_skipped_lists_naukri_and_glints():
    assert "naukri.com" in jobpages.SKIPPED
    assert "glints.com" in jobpages.SKIPPED
    assert all(jobpages.SKIPPED.values())
