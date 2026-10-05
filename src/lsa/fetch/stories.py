"""vendor/integrator fetcher: sitemap story pages are the items.

Counted rows hold ``method == "sitemap-url-count"`` when the site's
sitemap parse worked. ``fetch`` groups rows by source domain so each site's
sitemap walk runs once, filters page URLs through the site's own story
regex (reusing ``sitemaps.story_urls``), checks robots on every story page,
and yields the page's visible text. A page is fetched once even when
several category rows cover the domain; the item is yielded once per row
so its ``category_hint`` reflects that row, and ``collect_items``'s URL
dedupe keeps a single raw copy.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator

import httpx

from lsa.contracts import CountRecord, SourceItem
from lsa.fetch import common
from lsa.sources import http, robots, sitemaps, text


def plan_rows(rows: list[CountRecord]) -> list[CountRecord]:
    """Rows whose sitemap walk produced a story-url count."""
    return [r for r in rows if r.method == "sitemap-url-count"]


def fetch(
    rows: list[CountRecord],
    client: httpx.Client,
    *,
    sites_path=None,
    get_kwargs: dict | None = None,
    log: Callable[[str], None] | None = print,
    **_unused,
) -> Iterator[common.Produced]:
    from lsa import paths

    kwargs = get_kwargs or {}
    log = log or (lambda _m: None)
    sites = sitemaps.load_sites(sites_path or paths.RESEARCH / "vendor_sites.csv")
    by_domain = {s.domain: s for s in sites}

    by_source: dict[str, list[CountRecord]] = {}
    for row in rows:
        by_source.setdefault(row.source, []).append(row)

    for domain, domain_rows in by_source.items():
        site = by_domain.get(domain)
        if site is None:
            log(f"fetch stories: no site config for {domain}")
            continue
        urls, method = sitemaps.story_urls(site, client, get_kwargs=kwargs)
        if urls is None:
            log(f"fetch {domain}: sitemap walk failed ({method})")
            continue
        bodies: dict[str, str] = {}
        for url in urls:
            if not robots.allowed(url, client, get_kwargs=kwargs):
                continue
            try:
                response = http.get_with_backoff(client, url, **kwargs)
            except httpx.TransportError as exc:
                log(f"fetch {domain} {url}: {exc}")
                continue
            if response.status_code != 200:
                log(f"fetch {domain} {url} -> HTTP {response.status_code}")
                continue
            bodies[url] = text.html_to_text(response.text)
        for row in domain_rows:
            for url, body in bodies.items():
                yield common.Produced(
                    SourceItem("", url, body),
                    domain,
                    row.region,
                    row.category,
                    row.query,
                )
