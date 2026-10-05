"""Customer-story counts from vendor and integrator XML sitemaps.

Discovery order per site: Sitemap: lines declared in robots.txt, then the
conventional ``/sitemap.xml`` and ``/sitemap_index.xml`` candidates. Sitemap
indexes are followed recursively (visited-set, capped at MAX_SITEMAPS).
``story_path_regex`` matches on the URL path and picks out customer-story,
case-study and success-story pages.

Every fetch goes through robots.allowed first; when robots.txt itself cannot
be fetched (5xx, 429, unreachable) the site is skipped entirely per RFC 930.
A site that yields no usable sitemap counts as None, never zero.
"""

from __future__ import annotations

import csv
import gzip
import logging
import re
import xml.etree.ElementTree as ET
from collections import deque
from dataclasses import dataclass

import httpx

from lsa.contracts import CountRecord
from lsa.sources import http, robots

log = logging.getLogger(__name__)

MAX_SITEMAPS = 80

FALLBACK_SITEMAPS = ("/sitemap.xml", "/sitemap_index.xml", "/sitemap-index.xml")

# Sites run as consultancies rather than product vendors.
INTEGRATOR_DOMAINS = frozenset(
    {
        "accenture.com",
        "capgemini.com",
        "cognizant.com",
        "deloitte.com",
        "infosys.com",
        "tcs.com",
        "wipro.com",
    }
)


@dataclass(frozen=True)
class VendorSite:
    vendor: str
    domain: str
    story_path_regex: str
    categories: tuple[str, ...]  # empty means uncategorized

    @property
    def family(self) -> str:
        return "integrator" if self.domain in INTEGRATOR_DOMAINS else "vendor"

    @property
    def origin(self) -> str:
        return f"https://{self.domain}"

    @property
    def pattern(self) -> re.Pattern[str]:
        return re.compile(self.story_path_regex)


def load_sites(path) -> list[VendorSite]:
    """Parse research/vendor_sites.csv."""
    sites = []
    with open(path, newline="") as handle:
        for row in csv.DictReader(handle):
            categories = tuple(
                c.strip() for c in row["categories"].split(";") if c.strip()
            )
            sites.append(
                VendorSite(
                    vendor=row["vendor"].strip(),
                    domain=row["domain"].strip(),
                    story_path_regex=row["story_path_regex"].strip(),
                    categories=categories,
                )
            )
    return sites


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _locs(element: ET.Element, kind: str) -> list[str]:
    out = []
    for node in element:
        if _local(node.tag) != kind:
            continue
        loc = node.find("{*}loc")
        if loc is None:
            loc = node.find("loc")
        if loc is not None and loc.text:
            out.append(loc.text.strip())
    return out


def _maybe_decompress(url: str, body: bytes) -> bytes:
    if body[:2] == b"\x1f\x8b" or url.endswith(".gz"):
        try:
            return gzip.decompress(body)
        except OSError:
            return body
    return body


def _parse_sitemap(body: bytes) -> tuple[str, list[str]] | None:
    """(kind, locs): kind is ``index`` for child sitemaps, ``urlset`` else."""
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return None
    tag = _local(root.tag)
    if tag == "sitemapindex":
        return "index", _locs(root, "sitemap")
    if tag == "urlset":
        return "urlset", _locs(root, "url")
    return None


def _fetch(
    url: str, client: httpx.Client, kwargs: dict
) -> tuple[bytes | None, str | None]:
    """(body, error) for one sitemap URL; error set when unusable."""
    if not robots.allowed(url, client, get_kwargs=kwargs):
        return None, "robots-disallowed"
    try:
        response = http.get_with_backoff(client, url, **kwargs)
    except httpx.TransportError:
        return None, "transport-error"
    if response.status_code != 200:
        return None, f"http-{response.status_code}"
    return _maybe_decompress(url, response.content), None


def page_urls(
    site: VendorSite,
    client: httpx.Client,
    *,
    get_kwargs: dict | None = None,
) -> tuple[list[str] | None, str]:
    """Every page URL in the site's sitemaps, or (None, method) on failure."""
    kwargs = get_kwargs or {}
    rules = robots.rules_for(site.origin + "/", client, get_kwargs=kwargs)
    if rules.deny_all:
        log.warning("%s: robots.txt unusable, skipping site", site.domain)
        return None, "robots-unavailable"

    declared = rules.sitemaps()
    candidates = list(declared) or [
        site.origin + path for path in FALLBACK_SITEMAPS
    ]

    queue: deque[str] = deque(candidates)
    seen: set[str] = set()
    urls: list[str] = []
    parsed_any = False
    last_error: str | None = None
    while queue and len(seen) < MAX_SITEMAPS:
        sitemap_url = queue.popleft()
        if sitemap_url in seen:
            continue
        seen.add(sitemap_url)
        body, error = _fetch(sitemap_url, client, kwargs)
        if error is not None:
            last_error = error
            log.warning("%s %s: %s", site.domain, sitemap_url, error)
            continue
        parsed = _parse_sitemap(body)
        if parsed is None:
            last_error = "unparseable-sitemap"
            log.warning("%s %s: unparseable XML", site.domain, sitemap_url)
            continue
        parsed_any = True
        kind, locs = parsed
        if kind == "index":
            queue.extend(locs)
        else:
            urls.extend(locs)

    if not parsed_any:
        return None, last_error or "no-sitemap"
    return list(dict.fromkeys(urls)), "ok"


def story_urls(
    site: VendorSite,
    client: httpx.Client,
    *,
    get_kwargs: dict | None = None,
) -> tuple[list[str] | None, str]:
    """Page URLs whose path matches the site's story regex."""
    urls, method = page_urls(site, client, get_kwargs=get_kwargs)
    if urls is None:
        return None, method
    pattern = site.pattern
    return [u for u in urls if pattern.search(httpx.URL(u).path)], "ok"


def records_for_site(
    site: VendorSite,
    client: httpx.Client,
    counted_at: str,
    *,
    get_kwargs: dict | None = None,
) -> list[CountRecord]:
    """One CountRecord per (site, category); same count on each row."""
    matching, method = story_urls(site, client, get_kwargs=get_kwargs)
    count = len(matching) if matching is not None else None
    method = "sitemap-url-count" if matching is not None else method
    categories = site.categories or ("",)
    return [
        CountRecord(
            source=site.domain,
            family=site.family,
            region="US",
            category=category,
            system=site.vendor,
            query=site.story_path_regex,
            count=count,
            method=method,
            counted_at=counted_at,
        )
        for category in categories
    ]


def sample_story_urls(
    sites: list[VendorSite],
    client: httpx.Client,
    n: int,
    *,
    get_kwargs: dict | None = None,
) -> list[str]:
    """Up to ``n`` story page URLs across the sites, robots-permitted only."""
    kwargs = get_kwargs or {}
    picked: list[str] = []
    for site in sites:
        if len(picked) >= n:
            break
        matching, _ = story_urls(site, client, get_kwargs=kwargs)
        for url in matching or []:
            if len(picked) >= n:
                break
            if robots.allowed(url, client, get_kwargs=kwargs):
                picked.append(url)
    return picked
