"""Reddit public-search gating: disallowed means never fetched."""

import httpx

from lsa.sources import http, reddit

DENY_ALL = "User-agent: *\nDisallow: /\n"
ALLOW_ALL = "User-agent: *\nDisallow:\n"


def _client(handler):
    return http.make_client(transport=httpx.MockTransport(handler))


def test_robots_disallow_never_fetches_search(no_sleep):
    requested = []

    def handler(request):
        requested.append(request.url.path)
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text=DENY_ALL)
        return httpx.Response(200, json={"data": {"children": [1, 2]}})

    client = _client(handler)
    assert reddit.count("cobol", "US", client, get_kwargs=no_sleep) is None
    assert requested == ["/robots.txt"]


def test_search_json_counted_when_allowed(no_sleep):
    def handler(request):
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text=ALLOW_ALL)
        return httpx.Response(
            200, json={"data": {"children": [{"id": 1}, {"id": 2}, {"id": 3}]}}
        )

    client = _client(handler)
    assert reddit.count("cobol", "US", client, get_kwargs=no_sleep) == 3


def test_bad_json_returns_none(no_sleep):
    def handler(request):
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text=ALLOW_ALL)
        return httpx.Response(200, text="<html>blocked</html>")

    client = _client(handler)
    assert reddit.count("cobol", "US", client, get_kwargs=no_sleep) is None


def test_skipped_documents_reason():
    assert "reddit.com" in reddit.SKIPPED
    assert "robots" in reddit.SKIPPED["reddit.com"]
