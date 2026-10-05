"""vendor/integrator fetcher: sitemap story pages are the items."""

from __future__ import annotations

from lsa.contracts import CountRecord
from lsa.fetch import stories

ROBOTS_ALLOW = "User-agent: *\nDisallow:\n"
SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://acme.test/stories/bank-modernization</loc></url>
  <url><loc>https://acme.test/blog/news-item</loc></url>
</urlset>"""
STORY = (
    "<html><body><h1>bank modernization</h1>"
    "<p>acme moved the bank off the mainframe</p></body></html>"
)


def _sites_csv(tmp_path):
    path = tmp_path / "vendor_sites.csv"
    path.write_text(
        "vendor,domain,story_path_regex,categories\n"
        "Acme,acme.test,/stories/,core-banking\n"
        "Other,other.test,/cases/,core-banking\n"
    )
    return path


def _record(method="sitemap-url-count", category="core-banking", domain="acme.test"):
    return CountRecord(
        source=domain,
        family="vendor",
        region="US",
        category=category,
        system="Acme",
        query="/stories/",
        count=1,
        method=method,
        counted_at="T",
    )


def _handler(requests):
    from httpx import Response

    def handler(request):
        requests.append(str(request.url))
        if request.url.path == "/robots.txt":
            return Response(200, text=ROBOTS_ALLOW)
        if request.url.path == "/sitemap.xml":
            return Response(200, text=SITEMAP)
        if request.url.path == "/stories/bank-modernization":
            return Response(200, text=STORY)
        return Response(404, text="nope")

    return handler


def test_plan_rows_keeps_only_sitemap_counts():
    rows = [
        _record(),
        _record("robots-unavailable"),
        _record("no-sitemap"),
        _record("http-500"),
    ]
    planned = stories.plan_rows(rows)
    assert len(planned) == 1
    assert planned[0].method == "sitemap-url-count"


def test_fetch_yields_story_pages_only(mock_client, no_sleep, tmp_path):
    requests = []
    client = mock_client(_handler(requests))
    produced = list(
        stories.fetch(
            [_record()],
            client,
            sites_path=_sites_csv(tmp_path),
            log=None,
        )
    )
    assert len(produced) == 1
    p = produced[0]
    assert p.item.url == "https://acme.test/stories/bank-modernization"
    assert "off the mainframe" in p.item.text
    assert p.source == "acme.test"
    assert p.category_hint == "core-banking"
    # the /blog URL never matched the story regex, so it was never fetched
    assert not any("/blog/" in u for u in requests)


def test_fetch_dedupes_pages_across_category_rows(mock_client, no_sleep, tmp_path):
    """Two category rows for one domain share the sitemap and the story;
    the page is produced once with the first row's category hint."""
    requests = []
    client = mock_client(_handler(requests))
    rows = [_record(category="core-banking"), _record(category="payroll-hr")]
    produced = list(
        stories.fetch(
            rows, client,
            sites_path=_sites_csv(tmp_path), log=None,
        )
    )
    story_fetches = [u for u in requests if "/stories/" in u]
    assert len(produced) == 1
    assert len(story_fetches) == 1
    assert produced[0].category_hint == "core-banking"
    assert produced[0].region == ""


def test_fetch_skips_unknown_domains(mock_client, no_sleep, tmp_path):
    client = mock_client(_handler([]))
    logs = []
    produced = list(
        stories.fetch(
            [_record(domain="ghost.test")],
            client,
            sites_path=_sites_csv(tmp_path),
            log=logs.append,
        )
    )
    assert produced == []
    assert any("ghost.test" in m for m in logs)


def test_fetch_respects_robots_on_story_pages(mock_client, no_sleep, tmp_path):
    from httpx import Response

    def handler(request):
        if request.url.path == "/robots.txt":
            return Response(
                200, text="User-agent: *\nDisallow: /stories/\n"
            )
        if request.url.path == "/sitemap.xml":
            return Response(200, text=SITEMAP)
        return Response(200, text=STORY)

    client = mock_client(handler)
    produced = list(
        stories.fetch(
            [_record()],
            client,
            sites_path=_sites_csv(tmp_path),
            log=None,
        )
    )
    assert produced == []
