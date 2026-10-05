"""MyCareersFuture job counts (SG jobs).

GETs the portal's public ``/v2/jobs`` search endpoint with ``search``, a
``limit`` of 1 and ``page=0``, then reads the top-level ``total``. The
endpoint is undocumented; the shape was confirmed by a live call in
sources.csv. ``search`` carries the query as a double-quoted exact phrase;
an empty query omits ``search`` for the sanity guard's match-all probe.
"""

from __future__ import annotations

from collections.abc import Iterator

import httpx

from lsa.contracts import SourceItem
from lsa.sources import http, text
from lsa.sources.phrase import quoted

SOURCE = "mycareersfuture"
FAMILY = "jobs"
REGIONS = ("SG",)

_URL = "https://api.mycareersfuture.gov.sg/v2/jobs"
_DETAIL = "https://www.mycareersfuture.gov.sg/job/"
_PAGE = 100


def _params(query: str, *, limit: int, page: int) -> dict:
    params: dict = {"limit": limit, "page": page}
    if (phrase := quoted(query)) is not None:
        params["search"] = phrase
    return params


def count(query: str, region: str, client: httpx.Client) -> int | None:
    params = _params(query, limit=1, page=0)
    response = http.get_with_backoff(client, _URL, params=params)
    response.raise_for_status()
    total = response.json().get("total")
    return int(total) if isinstance(total, int | float) else None


def _item(job: dict) -> SourceItem:
    uuid = str(job.get("uuid") or "")
    post_id = (job.get("metadata") or {}).get("jobPostId")
    slug = str(post_id).lower() if post_id else uuid
    parts = [
        job.get("title"),
        (job.get("postedCompany") or {}).get("name"),
        text.html_to_text(str(job.get("description") or "")),
    ]
    return SourceItem(
        source_id=uuid,
        url=f"{_DETAIL}{slug}" if slug else "",
        text=" ".join(str(p) for p in parts if p),
    )


def search(query: str, region: str, client: httpx.Client) -> Iterator[SourceItem]:
    """Paged ``results`` rows; ``page`` is 0-based, a short page ends it."""
    page = 0
    while True:
        response = http.get_with_backoff(
            client, _URL, params=_params(query, limit=_PAGE, page=page)
        )
        response.raise_for_status()
        results = response.json().get("results") or []
        for job in results:
            yield _item(job)
        if len(results) < _PAGE:
            return
        page += 1
