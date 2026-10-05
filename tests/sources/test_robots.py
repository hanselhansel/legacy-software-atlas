"""robots.txt allow/deny and per-host caching."""

import httpx

from lsa.sources import http, robots


def _client(handler):
    return http.make_client(transport=httpx.MockTransport(handler))


def _robot_paths(handler):
    requested = []

    def wrapped(request):
        requested.append(request.url.path)
        return handler(request)

    return wrapped, requested


def test_disallowed_path_denied():
    def handler(request):
        return httpx.Response(
            200, text="User-agent: *\nDisallow: /private/\n"
        )

    client = _client(handler)
    assert not robots.allowed("https://x.test/private/page", client)
    assert robots.allowed("https://x.test/public/page", client)


def test_missing_robots_allows_all():
    def handler(request):
        return httpx.Response(404)

    client = _client(handler)
    assert robots.allowed("https://x.test/anything", client)


def test_server_error_denies_all(no_sleep):
    def handler(request):
        return httpx.Response(503)

    client = _client(handler)
    assert not robots.allowed(
        "https://x.test/anything", client, get_kwargs=no_sleep
    )


def test_robots_fetched_once_per_host():
    def handler(request):
        return httpx.Response(200, text="User-agent: *\nDisallow: /x\n")

    client = _client(handler)
    wrapped, requested = _robot_paths(handler)
    client = _client(wrapped)
    for path in ("/a", "/b", "/c"):
        robots.allowed(f"https://x.test{path}", client)
    assert requested.count("/robots.txt") == 1


def test_declared_sitemaps():
    def handler(request):
        return httpx.Response(
            200,
            text=(
                "User-agent: *\nDisallow:\n"
                "Sitemap: https://x.test/maps/main.xml\n"
            ),
        )

    client = _client(handler)
    rules = robots.rules_for("https://x.test/", client)
    assert rules.sitemaps() == ["https://x.test/maps/main.xml"]
