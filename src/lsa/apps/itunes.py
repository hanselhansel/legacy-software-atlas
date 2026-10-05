"""iTunes lookup and customer-reviews RSS collectors (plan 3, lane M).

Two keyless GET endpoints on itunes.apple.com:

- ``lookup``: one app's storefront facts (rating, rating count, version,
  version date): ``GET /lookup?id=<apple_id>&country=<cc>``.
- ``reviews``: one RSS page of customer reviews:
  ``GET /<cc>/rss/customerreviews/page=<n>/id=<apple_id>/sortby=<sort>/json``.

Live findings 2026-10-05 (recorded during the lane M build): the review
feed is degraded. ``sortby=mostrecent`` returns an empty ``feed.entry``
for every app and storefront tried (US, GB, SG). ``sortby=mosthelpful``
returns at most the first page of 50 reviews, and only for a subset of
apps. ``reviews`` keeps the lane's documented ``mostrecent`` default;
``lsa apps --sort mosthelpful`` collects what the feed currently serves.

robots.txt note: itunes.apple.com declares ``Disallow: /*/rss/*`` and
``Disallow: /*/lookup?`` for ``User-agent: *``. Those are RFC 9309
wildcards that urllib.robotparser reads as literal prefixes, so the
repo's robots gate permits both endpoints. Under wildcard semantics the
root ``/lookup`` path is not matched by ``/*/lookup?``, but ``/*/rss/*``
does match the reviews feed; the lane keeps the gate anyway so a
stricter parser or a tighter robots file stops collection cleanly.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from datetime import UTC, datetime

import httpx

from lsa.sources import http, robots

SOURCE = "itunes"
FAMILY = "app_reviews"

_HOST = "https://itunes.apple.com"
MAX_PAGES = 10
# Reviews kept per the lane contract: text window of the first 80 words.
TEXT_WINDOW_WORDS = 80
SORTS = ("mostrecent", "mosthelpful")


class RobotsDenied(RuntimeError):
    """robots.txt disallows the URL under the repo's parser rules."""


@dataclass(frozen=True)
class AppLookup:
    """Storefront facts for one app, from ``/lookup``."""

    track_name: str | None
    rating: float | None
    rating_count: int | None
    version: str | None
    version_date: str | None
    store_url: str | None


@dataclass(frozen=True)
class Review:
    """One customer review: id, rating, date, title, text window."""

    review_id: str
    rating: int | None
    date: str
    title: str
    text: str
    url: str


def _get(url: str, client: httpx.Client, get_kwargs: dict | None) -> httpx.Response:
    """robots-gated GET through the shared pacing/backoff wrapper."""
    kwargs = dict(get_kwargs or {})
    if not robots.allowed(url, client, get_kwargs=kwargs):
        raise RobotsDenied(f"robots.txt disallows {url}")
    return http.get_with_backoff(client, url, **kwargs)


def lookup(
    apple_id: str,
    country: str,
    client: httpx.Client,
    *,
    get_kwargs: dict | None = None,
) -> AppLookup | None:
    """Storefront facts for ``apple_id`` in ``country``, or None when the
    app is not listed in that storefront."""
    url = f"{_HOST}/lookup?id={apple_id}&country={country.lower()}"
    response = _get(url, client, get_kwargs)
    response.raise_for_status()
    results = response.json().get("results") or []
    if not results:
        return None
    app = results[0]
    rating = app.get("averageUserRating")
    count = app.get("userRatingCount")
    return AppLookup(
        track_name=app.get("trackName"),
        rating=float(rating) if isinstance(rating, int | float) else None,
        rating_count=int(count) if isinstance(count, int | float) else None,
        version=app.get("version"),
        version_date=app.get("currentVersionReleaseDate")
        or app.get("releaseDate"),
        store_url=app.get("trackViewUrl"),
    )


def _feed_url(apple_id: str, country: str, page: int, sort: str) -> str:
    cc = country.lower()
    return (
        f"{_HOST}/{cc}/rss/customerreviews/page={page}"
        f"/id={apple_id}/sortby={sort}/json"
    )


def _label(node: object) -> str:
    """The ``label`` string of an RSS field, or ""."""
    if isinstance(node, dict):
        value = node.get("label")
        return str(value) if value is not None else ""
    return ""


def _link_href(node: object) -> str:
    """First ``link.attributes.href``; ``link`` is a dict or a list."""
    links = node if isinstance(node, list) else [node]
    for link in links:
        if not isinstance(link, dict):
            continue
        href = (link.get("attributes") or {}).get("href")
        if href:
            return str(href)
    return ""


def _parse_date(raw: str) -> datetime | None:
    """RSS ``updated`` labels are ISO 8601 with an offset."""
    try:
        parsed = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed


def _entry(entry: dict, page_url: str) -> Review | None:
    """One review entry, or None for non-review entries (the feed's app
    metadata row carries no ``im:rating``)."""
    if not isinstance(entry, dict) or "im:rating" not in entry:
        return None
    body = entry.get("content")
    if isinstance(body, list):
        body = next(
            (c for c in body if isinstance(c, dict) and c.get("label")),
            {},
        )
    text = " ".join(_label(body).split()[:TEXT_WINDOW_WORDS])
    raw_rating = _label(entry.get("im:rating"))
    try:
        rating = int(raw_rating)
    except ValueError:
        rating = None
    return Review(
        review_id=_label(entry.get("id")),
        rating=rating,
        date=_label(entry.get("updated")),
        title=_label(entry.get("title")),
        text=text,
        url=_link_href(entry.get("link")) or page_url,
    )


def _entries(payload: dict) -> list[dict]:
    """``feed.entry`` as a list; the feed emits a dict for a lone entry."""
    entries = (payload.get("feed") or {}).get("entry") or []
    if isinstance(entries, dict):
        entries = [entries]
    return [e for e in entries if isinstance(e, dict)]


def reviews(
    apple_id: str,
    country: str,
    client: httpx.Client,
    *,
    sort: str = "mostrecent",
    max_pages: int = MAX_PAGES,
    cutoff: datetime | None = None,
    get_kwargs: dict | None = None,
) -> Iterator[Review]:
    """Page the customer-reviews RSS feed; yields reviews dated on or
    after ``cutoff``.

    Stops on an empty page, a non-200 page, a page with no parseable
    reviews, or a page where every review predates the cutoff (feeds
    are ordered, so deeper pages only get older or less relevant).
    ``cutoff`` of None keeps everything.
    """
    if sort not in SORTS:
        raise ValueError(f"sort must be one of {SORTS}, got {sort!r}")
    for page in range(1, max_pages + 1):
        url = _feed_url(apple_id, country, page, sort)
        response = _get(url, client, get_kwargs)
        if response.status_code != 200:
            return
        entries = _entries(response.json())
        if not entries:
            return
        seen = 0
        stale = 0
        for entry in entries:
            review = _entry(entry, url)
            if review is None:
                continue
            seen += 1
            when = _parse_date(review.date)
            if cutoff is not None and (when is None or when < cutoff):
                stale += 1
                continue
            yield review
        if seen == 0 or stale == seen:
            return
