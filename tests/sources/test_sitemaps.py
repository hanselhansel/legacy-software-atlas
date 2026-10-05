"""Sitemap index walking, gzip, regex filtering, and CountRecord output."""

import gzip
from pathlib import Path

import httpx

from lsa.sources import http, sitemaps

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sitemaps"

SITE = sitemaps.VendorSite(
    vendor="Test Vendor",
    domain="test.vendor",
    story_path_regex=r"^/customer-stories/[\w-]+/?$",
    categories=("core-banking", "wealth-portfolio-accounting"),
)

ROBOTS_DECLARED = (
    "User-agent: *\nDisallow:\nSitemap: https://test.vendor/sitemap-index.xml\n"
)
ROBOTS_PLAIN = "User-agent: *\nDisallow:\n"
ROBOTS_DENY = "User-agent: *\nDisallow: /\n"


def _client(handler):
    return http.make_client(transport=httpx.MockTransport(handler))


def _body(name: str) -> bytes:
    return (FIXTURES / name).read_bytes()


def _handler_with_index(request):
    path = request.url.path
    if path == "/robots.txt":
        return httpx.Response(200, text=ROBOTS_DECLARED)
    if path == "/sitemap-index.xml":
        return httpx.Response(200, content=_body("index.xml"))
    if path == "/pages-1.xml":
        return httpx.Response(200, content=_body("pages-1.xml"))
    if path == "/pages-2.xml.gz":
        return httpx.Response(200, content=gzip.compress(_body("pages-2.xml")))
    return httpx.Response(404)


def test_index_gzip_and_regex_filter(no_sleep):
    client = _client(_handler_with_index)
    urls, method = sitemaps.story_urls(SITE, client, get_kwargs=no_sleep)
    assert method == "ok"
    assert urls == [
        "https://test.vendor/customer-stories/acme-bank",
        "https://test.vendor/customer-stories/globex-insurance/",
        "https://test.vendor/customer-stories/initech-retail",
    ]


def test_records_per_category(no_sleep):
    client = _client(_handler_with_index)
    records = sitemaps.records_for_site(SITE, client, "2026-01-01T00:00:00Z", get_kwargs=no_sleep)
    assert [r.category for r in records] == [
        "core-banking",
        "wealth-portfolio-accounting",
    ]
    assert all(r.count == 3 for r in records)
    assert all(r.family == "vendor" for r in records)
    assert all(r.region == "US" for r in records)
    assert all(r.query == SITE.story_path_regex for r in records)
    assert all(r.method == "sitemap-url-count" for r in records)


def test_fallback_sitemap_when_robots_declares_none(no_sleep):
    def handler(request):
        path = request.url.path
        if path == "/robots.txt":
            return httpx.Response(200, text=ROBOTS_PLAIN)
        if path == "/sitemap.xml":
            return httpx.Response(200, content=_body("pages-1.xml"))
        return httpx.Response(404)

    client = _client(handler)
    urls, method = sitemaps.page_urls(SITE, client, get_kwargs=no_sleep)
    assert method == "ok"
    assert len(urls) == 3


def test_robots_deny_all_returns_none_without_fetches(no_sleep):
    requested = []

    def handler(request):
        requested.append(request.url.path)
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text=ROBOTS_DENY)
        return httpx.Response(200, content=_body("pages-1.xml"))

    client = _client(handler)
    urls, method = sitemaps.page_urls(SITE, client, get_kwargs=no_sleep)
    assert urls is None
    assert method == "robots-disallowed"
    assert all(path == "/robots.txt" for path in requested)


def test_no_sitemap_returns_none(no_sleep):
    def handler(request):
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text=ROBOTS_PLAIN)
        return httpx.Response(404)

    client = _client(handler)
    urls, method = sitemaps.page_urls(SITE, client, get_kwargs=no_sleep)
    assert urls is None
    assert method == "http-404"

    records = sitemaps.records_for_site(
        SITE, client, "2026-01-01T00:00:00Z", get_kwargs=no_sleep
    )
    assert all(r.count is None for r in records)


def test_load_sites_csv(tmp_path):
    csv_path = tmp_path / "vendor_sites.csv"
    csv_path.write_text(
        "vendor,domain,story_path_regex,categories\n"
        "Acme,acme.test,^/stories/,core-banking;payroll-hr\n"
        "Solo,solo.test,^/cases/,\n"
    )
    sites = sitemaps.load_sites(csv_path)
    assert sites[0].vendor == "Acme"
    assert sites[0].categories == ("core-banking", "payroll-hr")
    assert sites[0].family == "vendor"
    assert sites[1].categories == ()


def test_integrator_family():
    site = sitemaps.VendorSite(
        vendor="TCS", domain="tcs.com", story_path_regex="x", categories=()
    )
    assert site.family == "integrator"
