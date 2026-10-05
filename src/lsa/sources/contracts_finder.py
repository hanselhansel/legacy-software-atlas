"""Contracts Finder notice counts (UK procurement).

POSTs a keyword ``searchCriteria`` to the v2 ``search_notices`` endpoint and
reads ``hitCount``. Anonymous search works; the documented OAuth2 client
credentials are only needed for publishing.

The ``keyword`` field honors a double-quoted phrase as an exact match
(verified live 2026-10-05: ``"window cleaning"`` returned 846 vs 17338
unquoted). The schema's ``queryString`` field is documented as the
alternative supporting quotes, but the live endpoint ignores it entirely, so
it stays unset. An empty query sends empty criteria, the match-all probe.
"""

from __future__ import annotations

from collections.abc import Iterator

import httpx

from lsa.contracts import SourceItem
from lsa.sources import http
from lsa.sources.phrase import quoted

SOURCE = "contracts-finder"
FAMILY = "procurement"
REGIONS = ("UK",)

_URL = (
    "https://www.contractsfinder.service.gov.uk"
    "/api/rest/2/search_notices/json"
)
_PAGE = 50
_DETAIL = "https://www.contractsfinder.service.gov.uk/notice/"


def _criteria(query: str) -> dict:
    criteria: dict = {}
    if (phrase := quoted(query)) is not None:
        criteria["keyword"] = phrase
    return criteria


def count(query: str, region: str, client: httpx.Client) -> int | None:
    body = {"searchCriteria": _criteria(query), "size": 1}
    response = http.post_with_backoff(client, _URL, json=body)
    response.raise_for_status()
    total = response.json().get("hitCount")
    return int(total) if isinstance(total, int | float) else None


def _item(notice: dict) -> SourceItem:
    nid = str(notice.get("id") or "")
    parts = [
        notice.get("title"),
        notice.get("organisationName"),
        notice.get("publishedDate"),
        notice.get("description"),
    ]
    text = " ".join(str(p) for p in parts if p is not None)
    return SourceItem(
        source_id=nid, url=f"{_DETAIL}{nid}" if nid else "", text=text
    )


def search(query: str, region: str, client: httpx.Client) -> Iterator[SourceItem]:
    """Paged ``noticeList`` rows; ``page`` is 1-based, a short page ends it."""
    page = 1
    while True:
        body = {
            "searchCriteria": _criteria(query),
            "page": page,
            "size": _PAGE,
        }
        response = http.post_with_backoff(client, _URL, json=body)
        response.raise_for_status()
        notices = response.json().get("noticeList") or []
        for notice in notices:
            yield _item(notice)
        if len(notices) < _PAGE:
            return
        page += 1
