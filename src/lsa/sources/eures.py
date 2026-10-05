"""EURES job counts (EU jobs).

POSTs a keyword search to the portal's public jv-search endpoint and reads
``numberRecords``. The body mirrors the portal's own front end: one keyword
with ``specificSearchCode`` EVERYWHERE and every filter list empty. The
keyword goes out wrapped in double quotes as the exact-phrase form.

The endpoint is undocumented by the Commission; the body shape follows the
reverse-engineered OpenAPI spec (rorar/EURES-API-Documentation) and the live
call recorded in sources.csv. Per that spec an empty ``keywords`` array is
the documented unfiltered search, so an empty query sends ``[]`` for the
sanity guard's match-all probe.
"""

from __future__ import annotations

from collections.abc import Iterator

import httpx

from lsa.contracts import SourceItem
from lsa.sources import http, text
from lsa.sources.phrase import quoted

SOURCE = "eures"
FAMILY = "jobs"
REGIONS = ("EU",)

_URL = "https://europa.eu/eures/api/jv-searchengine/public/jv-search/search"
_DETAIL = "https://europa.eu/eures/portal/jv-se/jv-details/"
_PAGE = 50


def _body(query: str, *, per_page: int = 1, page: int = 1) -> dict:
    phrase = quoted(query)
    return {
        "resultsPerPage": per_page,
        "page": page,
        "sortSearch": "BEST_MATCH",
        "keywords": (
            [{"keyword": phrase, "specificSearchCode": "EVERYWHERE"}]
            if phrase is not None
            else []
        ),
        "publicationPeriod": None,
        "occupationUris": [],
        "skillUris": [],
        "requiredExperienceCodes": [],
        "positionScheduleCodes": [],
        "sectorCodes": [],
        "educationAndQualificationLevelCodes": [],
        "positionOfferingCodes": [],
        "locationCodes": [],
        "euresFlagCodes": [],
        "otherBenefitsCodes": [],
        "requiredLanguages": [],
        "minNumberPost": None,
        "sessionId": None,
        "userPreferredLanguage": None,
        "requestLanguage": "en",
    }


def count(query: str, region: str, client: httpx.Client) -> int | None:
    response = http.post_with_backoff(client, _URL, json=_body(query))
    response.raise_for_status()
    total = response.json().get("numberRecords")
    return int(total) if isinstance(total, int | float) else None


def _item(jv: dict) -> SourceItem:
    jid = str(jv.get("id") or "")
    parts = [
        jv.get("title"),
        (jv.get("employer") or {}).get("name"),
        text.html_to_text(str(jv.get("description") or "")),
    ]
    return SourceItem(
        source_id=jid,
        url=f"{_DETAIL}{jid}" if jid else "",
        text=" ".join(str(p) for p in parts if p),
    )


def search(query: str, region: str, client: httpx.Client) -> Iterator[SourceItem]:
    """Paged ``jvs`` rows; ``page`` is 1-based, a short page ends it."""
    page = 1
    while True:
        response = http.post_with_backoff(
            client, _URL, json=_body(query, per_page=_PAGE, page=page)
        )
        response.raise_for_status()
        jvs = response.json().get("jvs") or []
        for jv in jvs:
            yield _item(jv)
        if len(jvs) < _PAGE:
            return
        page += 1
