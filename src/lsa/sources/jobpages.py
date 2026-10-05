"""Keyword result totals from public job-search pages (plan 1, task 3).

Each site builds one search URL per query, checks robots.txt first, then
parses the visible result total from the returned HTML with a site-specific
regex (or JSON embedded in the page, which is still part of the public page,
not an API call).

``count()`` returns an int only when the page loads and a total is visible;
robots denial, HTTP failures and unparseable pages all return None. Callers
record the None with a ``method`` string that says which case it was.

Sites robots or terms bar us from fetching are never attempted; ``SKIPPED``
documents why.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

import httpx

from lsa.sources import http, robots

log = logging.getLogger(__name__)

# Never fetched. Reasons are checked against robots.txt and site terms at
# build time; the runtime check would also return None.
SKIPPED: dict[str, str] = {
    "naukri.com": "robots.txt disallows job-search pages for crawlers",
    "glints.com": "robots.txt disallows the keyword search path",
}

_INT = re.compile(r"\d+")


def _num(text: str) -> int | None:
    digits = _INT.findall(text)
    return int("".join(digits)) if digits else None


def _slug(query: str) -> str:
    slug = re.sub(r"[^\w]+", "-", query.lower(), flags=re.UNICODE)
    return slug.strip("-")


def _q(query: str) -> str:
    return httpx.QueryParams({"q": query})["q"]


@dataclass(frozen=True)
class Site:
    key: str
    host: str
    region: str
    url_template: str  # {q} = url-encoded query, {slug} = slugged query
    total_patterns: tuple[str, ...]

    def url(self, query: str) -> str:
        return self.url_template.format(q=_q(query), slug=_slug(query))

    def parse_total(self, html_text: str) -> int | None:
        for pattern in self.total_patterns:
            match = re.search(pattern, html_text, re.IGNORECASE | re.DOTALL)
            if match:
                return _num(match.group(1))
        return None


SEEK_FAMILY_PATTERNS = (
    r'"displayTotalCount"\s*:\s*"([\d,\.]+)"',
    r'"totalCount"\s*:\s*"?([\d,\.]+)',
    r">\s*([\d,\.]+)\s+[\w ]*jobs?\b",
)

INDEED_PATTERNS = (
    r'class="[^"]*jobsearch-ResultsInfo[^"]*"[^>]*>.*?([\d,\.]+)\s*jobs',
    r'"jobsearch-ResultsInfo".*?([\d,\.]+)\s*jobs',
    r"([\d,\.]+)\s*jobs\b",
)

SITES: tuple[Site, ...] = (
    Site(
        key="seek-au",
        host="www.seek.com.au",
        region="AU",
        url_template="https://www.seek.com.au/jobs?keywords={q}",
        total_patterns=SEEK_FAMILY_PATTERNS,
    ),
    Site(
        key="jobstreet-my",
        host="my.jobstreet.com",
        region="MY",
        url_template="https://my.jobstreet.com/jobs?keywords={q}",
        total_patterns=SEEK_FAMILY_PATTERNS,
    ),
    Site(
        key="jobstreet-ph",
        host="ph.jobstreet.com",
        region="PH",
        url_template="https://ph.jobstreet.com/jobs?keywords={q}",
        total_patterns=SEEK_FAMILY_PATTERNS,
    ),
    Site(
        key="jobstreet-id",
        host="id.jobstreet.com",
        region="ID",
        url_template="https://id.jobstreet.com/jobs?keywords={q}",
        total_patterns=SEEK_FAMILY_PATTERNS,
    ),
    Site(
        key="jobsdb-th",
        host="th.jobsdb.com",
        region="TH",
        url_template="https://th.jobsdb.com/jobs?keywords={q}",
        total_patterns=SEEK_FAMILY_PATTERNS,
    ),
    Site(
        key="jobthai",
        host="www.jobthai.com",
        region="TH",
        url_template="https://www.jobthai.com/th/jobs?keyword={q}",
        total_patterns=(r"พบ\s*([\d,\.]+)\s*ตำแหน่งงาน",),
    ),
    Site(
        key="topcv",
        host="www.topcv.vn",
        region="VN",
        url_template="https://www.topcv.vn/tim-viec-lam-{slug}",
        total_patterns=(r"([\d,\.]+)\s*việc làm",),
    ),
    Site(
        key="itviec",
        host="itviec.com",
        region="VN",
        url_template="https://itviec.com/it-jobs/{slug}",
        total_patterns=(r"headline-total-jobs[^>]*>\s*([\d,\.]+)",),
    ),
    Site(
        key="careerviet",
        host="www.careerviet.vn",
        region="VN",
        url_template="https://www.careerviet.vn/viec-lam/{slug}-k-vi.html",
        total_patterns=(r"Tuyển dụng\s*([\d,\.]+)\s*việc làm",),
    ),
    Site(
        key="careersgov-sg",
        host="jobs.careers.gov.sg",
        region="SG",
        url_template="https://jobs.careers.gov.sg/?q={q}",
        total_patterns=(
            r'"total[\w]*"?\s*:\s*"?([\d,\.]+)',
            r"([\d,\.]+)\s*jobs?\s*(?:found|available)",
        ),
    ),
    Site(
        key="indeed-my",
        host="malaysia.indeed.com",
        region="MY",
        url_template="https://malaysia.indeed.com/jobs?q={q}",
        total_patterns=INDEED_PATTERNS,
    ),
    Site(
        key="indeed-au",
        host="au.indeed.com",
        region="AU",
        url_template="https://au.indeed.com/jobs?q={q}",
        total_patterns=INDEED_PATTERNS,
    ),
)

SITES_BY_REGION: dict[str, tuple[Site, ...]] = {
    region: tuple(s for s in SITES if s.region == region)
    for region in {s.region for s in SITES}
}


def count_site(
    site: Site,
    query: str,
    client: httpx.Client,
    *,
    get_kwargs: dict | None = None,
) -> tuple[int | None, str]:
    """One site's visible total for ``query``.

    Returns ``(count, method)`` where method explains the outcome:
    ``search-result-total``, ``robots-disallowed``, ``http <status>`` or
    ``no-total-in-page``. Never raises for expected fetch failures.
    """
    kwargs = get_kwargs or {}
    url = site.url(query)
    if not robots.allowed(url, client, get_kwargs=kwargs):
        log.info("robots disallows %s (%s)", site.key, url)
        return None, "robots-disallowed"
    try:
        response = http.get_with_backoff(client, url, **kwargs)
    except httpx.TransportError as exc:
        log.warning("transport error %s %s: %s", site.key, url, exc)
        return None, "transport-error"
    if response.status_code != 200:
        log.warning("%s %s -> HTTP %s", site.key, url, response.status_code)
        return None, f"http-{response.status_code}"
    total = site.parse_total(response.text)
    if total is None:
        log.info("no total parsed on %s %s", site.key, url)
        return None, "no-total-in-page"
    return total, "search-result-total"


def count(
    query: str,
    region: str,
    client: httpx.Client,
    *,
    get_kwargs: dict | None = None,
) -> int | None:
    """Largest visible total across the region's sites, or None.

    Sites in one region index overlapping pools; the max is the least-wrong
    regional figure. None means no site returned a total.
    """
    totals = [
        value
        for site in SITES_BY_REGION.get(region, ())
        if (
            value := count_site(site, query, client, get_kwargs=get_kwargs)[0]
        )
        is not None
    ]
    return max(totals) if totals else None


def records_for_query(
    query: str,
    region: str,
    category: str,
    client: httpx.Client,
    counted_at: str,
    *,
    get_kwargs: dict | None = None,
) -> list:
    """One CountRecord per site in ``region`` (imports lazily to stay cheap)."""
    from lsa.contracts import CountRecord

    records = []
    for site in SITES_BY_REGION.get(region, ()):
        value, method = count_site(site, query, client, get_kwargs=get_kwargs)
        records.append(
            CountRecord(
                source=site.key,
                family="jobs-pages",
                region=region,
                category=category,
                system="",
                query=query,
                count=value,
                method=method,
                counted_at=counted_at,
            )
        )
    return records
