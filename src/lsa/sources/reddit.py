"""Public Reddit search counts, robots/terms-gated (plan 1, task 3).

Only unauthenticated access is in scope: no OAuth, no credentials. The
collector checks robots.txt for the public ``/search.json`` URL before any
fetch. Reddit's live robots.txt disallows every path for ``User-agent: *``,
so count() returns None and the target is never fetched; ``SKIPPED`` records
why.
"""

from __future__ import annotations

import logging

import httpx

from lsa.sources import http, robots

log = logging.getLogger(__name__)

SKIPPED: dict[str, str] = {
    "reddit.com": (
        "robots.txt disallows /search.json for User-agent: *; "
        "authenticated API terms are out of scope"
    ),
}

_SEARCH = "https://www.reddit.com/search.json?q={q}&limit=1"


def count(
    query: str,
    region: str,
    client: httpx.Client,
    *,
    get_kwargs: dict | None = None,
) -> int | None:
    """Total posts matching ``query`` from public search JSON, or None."""
    kwargs = get_kwargs or {}
    url = _SEARCH.format(q=httpx.QueryParams({"q": query})["q"])
    if not robots.allowed(url, client, get_kwargs=kwargs):
        log.info("robots disallows %s", url)
        return None
    try:
        response = http.get_with_backoff(client, url, **kwargs)
    except httpx.TransportError as exc:
        log.warning("transport error %s: %s", url, exc)
        return None
    if response.status_code != 200:
        log.warning("%s -> HTTP %s", url, response.status_code)
        return None
    try:
        payload = response.json()
        children = payload["data"]["children"]
    except (ValueError, KeyError, TypeError):
        return None
    return len(children)


def record_for_query(
    query: str,
    region: str,
    category: str,
    client: httpx.Client,
    counted_at: str,
    *,
    get_kwargs: dict | None = None,
):
    """One CountRecord; count is None whenever the fetch is barred."""
    from lsa.contracts import CountRecord

    value = count(query, region, client, get_kwargs=get_kwargs)
    return CountRecord(
        source="reddit",
        family="reddit",
        region=region,
        category=category,
        system="",
        query=query,
        count=value,
        method="public-search-json" if value is not None else "robots-disallowed",
        counted_at=counted_at,
    )
