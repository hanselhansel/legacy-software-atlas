"""UK award collection: Find a Tender and Contracts Finder OCDS (lane L).

Both are OCDS release-package search APIs paged by ``cursor`` through
``links.next``. Neither accepts a free-text filter, so each endpoint
walks award-stage releases through a date window in small chunks and
local phrase matching on tender title + description + buyer decides
which queries a release answers.

Endpoint parameter names differ, verified live 2026-10-05:
Find a Tender takes ``updatedFrom``/``updatedTo`` (publishedFrom 400s);
Contracts Finder takes ``publishedFrom``/``publishedTo``. Both take
``stages``, ``limit`` (<=100), ``cursor``.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterator

import httpx

from lsa.awards.common import (
    AwardRow,
    QueryRow,
    date_chunks,
    matches_phrase,
    ocds_procedure,
)
from lsa.sources import http, robots

FTS_URL = "https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages"
CF_URL = "https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search"

SOURCES = ("find-tender", "contracts-finder")
REGIONS = ("UK",)

_LIMIT = 100
_WINDOW_DAYS = 90
_CHUNK_DAYS = 7

# (source, endpoint, from param, to param, notice URL base)
_ENDPOINTS = (
    (
        "find-tender",
        FTS_URL,
        "updatedFrom",
        "updatedTo",
        "https://www.find-tender.service.gov.uk/Notice/",
    ),
    (
        "contracts-finder",
        CF_URL,
        "publishedFrom",
        "publishedTo",
        "https://www.contractsfinder.service.gov.uk/Notice/",
    ),
)


def _party(release: dict, role: str) -> str:
    for p in release.get("parties") or []:
        if role in (p.get("roles") or []):
            return str(p.get("name") or "")
    return ""


def _money(*candidates: dict | None) -> tuple[float | None, str]:
    """First non-null (amount, currency) across value dicts."""
    for cand in candidates:
        if isinstance(cand, dict) and cand.get("amount") is not None:
            return float(cand["amount"]), str(cand.get("currency") or "")
    return None, ""


def _period(period: dict | None) -> tuple[str, str]:
    period = period or {}
    return (
        str(period.get("startDate") or "")[:10],
        str(period.get("endDate") or "")[:10],
    )


def _doc_url(release: dict) -> str:
    containers = (
        list(release.get("contracts") or [])
        + list(release.get("awards") or [])
        + [release.get("tender") or {}]
    )
    for container in containers:
        for doc in container.get("documents") or []:
            if doc.get("url"):
                return str(doc["url"])
    return ""


def _cpv(release: dict) -> str:
    tender = release.get("tender") or {}
    cls = (tender.get("classification") or {}).get("id")
    if cls:
        return str(cls)
    ids = [
        str((i.get("classification") or {}).get("id"))
        for i in tender.get("items") or []
        if (i.get("classification") or {}).get("id")
    ]
    return ";".join(ids)


def _release_text(release: dict) -> str:
    tender = release.get("tender") or {}
    return " ".join(
        str(part)
        for part in (
            tender.get("title"),
            tender.get("description"),
            (release.get("buyer") or {}).get("name"),
        )
        if part
    )


def _release_row(
    release: dict, row: QueryRow, source: str, notice_base: str
) -> AwardRow:
    tender = release.get("tender") or {}
    awards = release.get("awards") or []
    contracts = release.get("contracts") or []
    ocid = str(release.get("ocid") or release.get("id") or "")
    value, currency = _money(
        *[a.get("value") for a in awards],
        *[c.get("value") for c in contracts],
        tender.get("value"),
    )
    start, end = "", ""
    for period in (
        *[c.get("period") for c in contracts],
        *[a.get("contractPeriod") for a in awards],
        tender.get("contractPeriod"),
    ):
        start, end = _period(period)
        if start:
            break
    url = _doc_url(release)
    if not url and len(ocid) >= 36:
        url = f"{notice_base}{ocid[:36]}"
    return AwardRow(
        award_id=f"{source}:{ocid}",
        source=source,
        region=row.region,
        category_hint=row.category,
        query=row.query,
        buyer=str((release.get("buyer") or {}).get("name") or "")
        or _party(release, "buyer"),
        title=str(tender.get("title") or ""),
        text=str(tender.get("description") or ""),
        value=value,
        currency=currency,
        start_date=start,
        end_date=end,
        duration_months=None,
        procedure=ocds_procedure(tender.get("procurementMethod")),
        cpv_or_psc=_cpv(release),
        url=url,
    )


def _collect_endpoint(
    rows: list[QueryRow],
    client: httpx.Client,
    *,
    source: str,
    endpoint: str,
    from_param: str,
    to_param: str,
    notice_base: str,
    per_query: int | None,
    log: Callable[[str], None],
) -> Iterator[AwardRow]:
    """Award-stage releases in date chunks; first free matching query wins."""
    seen: set[str] = set()
    kept: Counter[str] = Counter()
    for start, end in date_chunks(_WINDOW_DAYS, _CHUNK_DAYS):
        if per_query is not None and all(
            kept[r.query] >= per_query for r in rows
        ):
            return
        url, params = endpoint, {
            from_param: start,
            to_param: end,
            "stages": "award",
            "limit": _LIMIT,
        }
        while url:
            response = http.get_with_backoff(client, url, params=params)
            response.raise_for_status()
            package = response.json()
            for release in package.get("releases") or []:
                ocid = str(release.get("ocid") or release.get("id") or "")
                if not ocid or ocid in seen:
                    continue
                text = _release_text(release)
                matched = next(
                    (
                        r
                        for r in rows
                        if (per_query is None or kept[r.query] < per_query)
                        and matches_phrase(text, r.query)
                    ),
                    None,
                )
                if matched is None:
                    continue
                seen.add(ocid)
                kept[matched.query] += 1
                yield _release_row(release, matched, source, notice_base)
            url = (package.get("links") or {}).get("next")
            params = None  # next URL carries its own params


def collect(
    rows: list[QueryRow],
    client: httpx.Client,
    *,
    per_query: int | None,
    log: Callable[[str], None] | None = print,
) -> Iterator[AwardRow]:
    """Award rows for UK queries from Find a Tender then Contracts Finder."""
    log = log or (lambda _m: None)
    rows = [r for r in rows if r.region in REGIONS]
    if not rows:
        return
    for source, endpoint, from_param, to_param, notice_base in _ENDPOINTS:
        if not robots.allowed(endpoint, client):
            log(f"{source}: robots.txt disallows {endpoint}, skipped")
            continue
        try:
            yield from _collect_endpoint(
                rows,
                client,
                source=source,
                endpoint=endpoint,
                from_param=from_param,
                to_param=to_param,
                notice_base=notice_base,
                per_query=per_query,
                log=log,
            )
        except Exception as exc:  # noqa: BLE001 - one endpoint must not stop a run
            log(f"{source}: {exc}")
