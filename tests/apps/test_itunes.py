"""Tests for the iTunes lookup and reviews collectors (plan 3, lane M)."""

from __future__ import annotations

import re
from datetime import UTC, datetime

import httpx
import pytest

from lsa.apps import itunes

LOOKUP = {
    "resultCount": 1,
    "results": [
        {
            "trackId": 42,
            "trackName": "BankApp",
            "averageUserRating": 3.5,
            "userRatingCount": 4200,
            "version": "7.1.2",
            "currentVersionReleaseDate": "2026-09-01T10:00:00Z",
            "releaseDate": "2015-01-01T00:00:00Z",
            "trackViewUrl": "https://apps.apple.com/gb/app/bankapp/id42",
            "sellerName": "Bank Co",
        }
    ],
}

RSS_RE = re.compile(
    r"^/([a-z]{2})/rss/customerreviews/page=(\d+)/id=(\d+)"
    r"/sortby=(\w+)/json$"
)


def _review(rid, rating, date, title, body):
    return {
        "id": {"label": rid},
        "im:rating": {"label": str(rating)},
        "updated": {"label": date},
        "title": {"label": title},
        "content": {"label": body, "attributes": {"type": "text"}},
        "link": {
            "attributes": {
                "href": f"https://itunes.apple.com/gb/review?rid={rid}"
            }
        },
    }


METADATA_ENTRY = {
    "im:name": {"label": "BankApp"},
    "id": {"label": "42"},
    "link": {"attributes": {"href": "https://apps.apple.com/gb/app/id42"}},
}


def _handler(*, lookup_payload=None, pages=None, robots_body=None):
    def handler(request: httpx.Request) -> httpx.Response:
        path = request.url.path
        if path == "/robots.txt":
            if robots_body is None:
                return httpx.Response(404)
            return httpx.Response(200, text=robots_body)
        if path == "/lookup":
            return httpx.Response(200, json=lookup_payload or {})
        match = RSS_RE.match(path)
        if match:
            entries = (pages or {}).get(int(match.group(2)), [])
            return httpx.Response(200, json={"feed": {"entry": entries}})
        return httpx.Response(404)

    return handler


def test_lookup_parses_storefront_fields(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        seen["url"] = str(request.url)
        return httpx.Response(200, json=LOOKUP)

    info = itunes.lookup("42", "GB", mock_client(handler))
    assert seen["url"] == "https://itunes.apple.com/lookup?id=42&country=gb"
    assert info == itunes.AppLookup(
        track_name="BankApp",
        rating=3.5,
        rating_count=4200,
        version="7.1.2",
        version_date="2026-09-01T10:00:00Z",
        store_url="https://apps.apple.com/gb/app/bankapp/id42",
    )


def test_lookup_missing_app_returns_none(mock_client, no_sleep):
    client = mock_client(
        _handler(lookup_payload={"resultCount": 0, "results": []})
    )
    assert itunes.lookup("99", "us", client) is None


def test_lookup_falls_back_to_release_date(mock_client, no_sleep):
    payload = {
        "resultCount": 1,
        "results": [
            {
                "trackName": "OldApp",
                "version": "1.0",
                "releaseDate": "2015-01-01T00:00:00Z",
            }
        ],
    }
    info = itunes.lookup("7", "us", mock_client(_handler(lookup_payload=payload)))
    assert info.version_date == "2015-01-01T00:00:00Z"
    assert info.rating is None and info.rating_count is None


def test_robots_denied_raises(mock_client, no_sleep):
    client = mock_client(
        _handler(robots_body="User-agent: *\nDisallow: /")
    )
    with pytest.raises(itunes.RobotsDenied):
        itunes.lookup("42", "us", client)
    with pytest.raises(itunes.RobotsDenied):
        list(itunes.reviews("42", "us", client))


def test_reviews_parses_entries(mock_client, no_sleep):
    body = " ".join(f"w{i}" for i in range(100))
    pages = {
        1: [
            METADATA_ENTRY,
            _review("r1", 5, "2026-06-01T10:00:00-07:00", "Crashes", body),
            _review("r2", 1, "2026-05-02T10:00:00-07:00", "Down again", "offline"),
        ],
        2: [],
    }
    seen = []
    base = _handler(pages=pages)

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return base(request)

    client = mock_client(handler)
    result = list(itunes.reviews("42", "gb", client))
    assert [r.review_id for r in result] == ["r1", "r2"]
    first = result[0]
    assert first.rating == 5
    assert first.date == "2026-06-01T10:00:00-07:00"
    assert first.title == "Crashes"
    assert len(first.text.split()) == itunes.TEXT_WINDOW_WORDS
    assert first.url == "https://itunes.apple.com/gb/review?rid=r1"
    feed_urls = [u for u in seen if "/rss/" in u]
    assert (
        feed_urls[0]
        == "https://itunes.apple.com/gb/rss/customerreviews/page=1"
        "/id=42/sortby=mostrecent/json"
    )
    # page 2 came back empty, so page 3 was never requested
    assert not any("page=3" in u for u in feed_urls)


def test_reviews_stops_after_all_stale_page(mock_client, no_sleep):
    pages = {
        1: [
            _review("r1", 5, "2026-02-01T00:00:00-07:00", "ok", "fine"),
            _review("r2", 3, "2025-01-01T00:00:00-07:00", "old", "stale"),
        ],
        2: [_review("r3", 4, "2024-01-01T00:00:00-07:00", "older", "stale")],
        3: [_review("r4", 1, "2026-09-01T00:00:00-07:00", "never", "seen")],
    }
    seen = []
    base = _handler(pages=pages)

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return base(request)

    client = mock_client(handler)
    cutoff = datetime(2026, 1, 1, tzinfo=UTC)
    result = list(itunes.reviews("42", "us", client, cutoff=cutoff))
    assert [r.review_id for r in result] == ["r1"]
    assert not any("page=3" in u for u in seen)


def test_reviews_no_cutoff_keeps_everything(mock_client, no_sleep):
    pages = {
        1: [_review("r1", 5, "2020-01-01T00:00:00-07:00", "old", "kept")],
        2: [],
    }
    client = mock_client(_handler(pages=pages))
    assert len(list(itunes.reviews("42", "us", client))) == 1


def test_reviews_caps_pages(mock_client, no_sleep):
    pages = {
        n: [_review(f"r{n}", 5, "2026-06-01T00:00:00-07:00", "t", "b")]
        for n in range(1, 12)
    }
    client = mock_client(_handler(pages=pages))
    result = list(itunes.reviews("42", "us", client))
    assert len(result) == itunes.MAX_PAGES
    result = list(itunes.reviews("42", "us", client, max_pages=3))
    assert len(result) == 3


def test_reviews_sort_param_and_validation(mock_client, no_sleep):
    seen = []
    base = _handler(pages={1: []})

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return base(request)

    client = mock_client(handler)
    assert list(itunes.reviews("42", "us", client, sort="mosthelpful")) == []
    assert any("sortby=mosthelpful" in u for u in seen)
    with pytest.raises(ValueError, match="sort"):
        list(itunes.reviews("42", "us", client, sort="newest"))


def test_reviews_single_entry_dict_feed(mock_client, no_sleep):
    """The feed emits a bare dict, not a list, for a lone review."""
    entry = _review("r1", 4, "2026-06-01T00:00:00-07:00", "Solo", "only one")
    base = _handler()

    def handler(request: httpx.Request) -> httpx.Response:
        if "/rss/" in request.url.path:
            entries = entry if "page=1" in request.url.path else []
            return httpx.Response(200, json={"feed": {"entry": entries}})
        return base(request)

    client = mock_client(handler)
    result = list(itunes.reviews("42", "us", client))
    assert [r.review_id for r in result] == ["r1"]


def test_reviews_content_list_picks_text(mock_client, no_sleep):
    entry = _review("r1", 3, "2026-06-01T00:00:00-07:00", "Mixed", "")
    entry["content"] = [
        {"label": "", "attributes": {"type": "text/html"}},
        {"label": "real words here", "attributes": {"type": "text"}},
    ]
    client = mock_client(_handler(pages={1: [entry], 2: []}))
    result = list(itunes.reviews("42", "us", client))
    assert result[0].text == "real words here"
