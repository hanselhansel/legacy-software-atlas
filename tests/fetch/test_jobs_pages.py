"""jobs-pages fetcher: the counted listing page is the item."""

from __future__ import annotations

from lsa.contracts import CountRecord
from lsa.fetch import jobs_pages

ROBOTS_ALLOW = "User-agent: *\nDisallow:\n"
ROBOTS_DENY = "User-agent: *\nDisallow: /\n"
PAGE = (
    "<html><head><title>results</title></head><body>"
    "<h1>cobol jobs</h1><p>1200 jobs at acme bank</p>"
    "<script>var x=1;</script></body></html>"
)


def _record(method: str, query: str = "cobol", source: str = "seek-au"):
    return CountRecord(
        source=source,
        family="jobs-pages",
        region="AU",
        category="mainframe-cobol",
        system="",
        query=query,
        count=1234 if method == "search-result-total" else None,
        method=method,
        counted_at="T",
    )


def test_plan_rows_keeps_only_loaded_pages():
    rows = [
        _record("search-result-total"),
        _record("http-403"),
        _record("robots-disallowed"),
        _record("no-total-in-page"),
        _record("search-result-total", query=""),
        _record("search-result-total; rejected by sanity guard"),
    ]
    planned = jobs_pages.plan_rows(rows)
    assert [r.method for r in planned] == ["search-result-total"]
    assert len(planned) == 1


def test_fetch_yields_listing_page_text(mock_client, no_sleep):
    requested = []

    def handler(request):
        requested.append(request.url.path)
        if request.url.path == "/robots.txt":
            from httpx import Response

            return Response(200, text=ROBOTS_ALLOW)
        from httpx import Response

        return Response(200, text=PAGE)

    client = mock_client(handler)
    rows = jobs_pages.plan_rows([_record("search-result-total")])
    produced = list(jobs_pages.fetch(rows, client, log=None))
    assert len(produced) == 1
    item = produced[0].item
    assert item.source_id == ""
    assert item.url == "https://www.seek.com.au/jobs?keywords=cobol"
    assert "cobol jobs" in item.text
    assert "<script>" not in item.text
    assert produced[0].category_hint == "mainframe-cobol"
    assert produced[0].region == "AU"


def test_fetch_respects_robots_deny(mock_client, no_sleep):
    requested = []

    def handler(request):
        requested.append(request.url.path)
        from httpx import Response

        if request.url.path == "/robots.txt":
            return Response(200, text=ROBOTS_DENY)
        return Response(200, text=PAGE)

    client = mock_client(handler)
    rows = jobs_pages.plan_rows([_record("search-result-total")])
    produced = list(jobs_pages.fetch(rows, client, log=None))
    assert produced == []
    # robots.txt was consulted; the listing page was never fetched.
    assert "/robots.txt" in requested
    assert "/jobs" not in requested


def test_fetch_logs_and_skips_http_errors(mock_client, no_sleep):
    from httpx import Response

    def handler(request):
        if request.url.path == "/robots.txt":
            return Response(200, text=ROBOTS_ALLOW)
        return Response(503, text="down")

    client = mock_client(handler)
    logs = []
    produced = list(
        jobs_pages.fetch(
            jobs_pages.plan_rows([_record("search-result-total")]),
            client,
            log=logs.append,
        )
    )
    assert produced == []
    assert any("503" in m for m in logs)
