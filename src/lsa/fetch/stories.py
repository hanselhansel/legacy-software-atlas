"""vendor/integrator fetcher: sitemap story pages are the items.

Counted rows hold ``method == "sitemap-url-count"`` when the site's
sitemap parse worked. ``fetch`` groups rows by source domain so each site's
sitemap walk runs once, filters page URLs through the site's own story
regex (reusing ``sitemaps.story_urls``), checks robots on every story page,
and yields each page's visible text as it is fetched, so a ``--limit`` run
stops after the first few pages instead of reading a whole site. A domain's
category rows share the same story URL set; each page is produced once with
the first row's category as the hint and the first row's ``count`` as
``query_count`` for the sampling weight.

``per_query`` turns the fetch into a documented probability sample: each
domain keeps a ``random.Random(seed)`` draw of N URLs from its matching
set (the rows share that set, so the sample is drawn once per domain), and
``sampled`` on the items.parquet rows records how many were kept.
"""

from __future__ import annotations

import random
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
    per_query: int | None = None,
    seed: int = common.DEFAULT_SEED,
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
        if per_query is not None and len(urls) > per_query:
            total = len(urls)
            urls = random.Random(
                seed if seed is not None else common.DEFAULT_SEED
            ).sample(urls, per_query)
            log(f"fetch {domain}: sampled {per_query} of {total} story urls")
        # A domain's category rows share the same story URL set; each page
        # is yielded once with the first row's category as the hint, so a
        # --limit run stops after the first few story fetches.
        hint = domain_rows[0].category
        query = domain_rows[0].query
        query_count = domain_rows[0].count
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
            yield common.Produced(
                SourceItem("", url, text.html_to_text(response.text)),
                domain,
                # region is a Jev label for story families; the count
                # row's "US" is the site registry's region, not the
                # story's. Leave it empty for Jev to fill.
                "",
                hint,
                query,
                query_count=query_count,
            )
