"""jobs-pages fetcher: the counted search-listing page is the item.

The count row exists only when the listing page loaded and showed a total
(``search-result-total``); ``plan_rows`` keeps exactly those rows. ``fetch``
rebuilds the same URL the counter used, re-checks robots.txt, GETs the page
through the shared pacing helper, and yields the page's visible text.
Listing pages carry the job titles and employer names Jev needs; chasing
individual job-detail pages is deliberately out of scope for the count-run
unit (and would multiply requests against boards that already 403).
"""

from __future__ import annotations

from collections.abc import Callable, Iterator

import httpx

from lsa.contracts import CountRecord, SourceItem
from lsa.fetch import common
from lsa.sources import http, jobpages, robots, text

_LOADED = "search-result-total"


def plan_rows(rows: list[CountRecord]) -> list[CountRecord]:
    """Rows whose listing page actually loaded for the count."""
    return [
        r for r in rows if r.method == _LOADED and r.query.strip()
    ]


def fetch(
    rows: list[CountRecord],
    client: httpx.Client,
    *,
    get_kwargs: dict | None = None,
    per_query: int | None = None,
    log: Callable[[str], None] | None = print,
    **_unused,
) -> Iterator[common.Produced]:
    kwargs = get_kwargs or {}
    log = log or (lambda _m: None)
    sites = {s.key: s for s in jobpages.SITES}
    for row in rows:
        if per_query is not None and per_query <= 0:
            continue
        site = sites.get(row.source)
        if site is None:
            log(f"fetch jobs-pages: no site for source {row.source}")
            continue
        url = site.url(row.query)
        if not robots.allowed(url, client, get_kwargs=kwargs):
            log(f"fetch {site.key}: robots disallows {url}")
            continue
        try:
            response = http.get_with_backoff(client, url, **kwargs)
        except httpx.TransportError as exc:
            log(f"fetch {site.key} {url}: {exc}")
            continue
        if response.status_code != 200:
            log(f"fetch {site.key} {url} -> HTTP {response.status_code}")
            continue
        yield common.Produced(
            SourceItem("", url, text.html_to_text(response.text)),
            site.key,
            row.region,
            row.category,
            row.query,
            query_count=row.count,
        )
