"""Kalibrr job counts (ID and PH jobs).

GETs the job board's public ``kjs/job_board/search`` endpoint with ``text``
carrying the query as a double-quoted exact phrase and a ``country`` filter
mapped from the region code, then reads ``count``. The endpoint is
undocumented; the shape was confirmed by live calls in sources.csv. An
empty query omits ``text`` for the sanity guard's match-all probe.

``from_alternative: true`` in the response means there was no exact match and
the count is a fuzzy fallback for different terms. That total does not
describe the requested query, so ``count`` returns ``None`` for it.
"""

from __future__ import annotations

from collections.abc import Iterator

import httpx

from lsa.contracts import SourceItem
from lsa.sources import http, text
from lsa.sources.phrase import quoted

SOURCE = "kalibrr"
FAMILY = "jobs"
REGIONS = ("ID", "PH")

_COUNTRIES = {"ID": "Indonesia", "PH": "Philippines"}
_URL = "https://www.kalibrr.com/kjs/job_board/search"
_PAGE = 50


def _params(query: str, region: str, *, limit: int, offset: int) -> dict:
    params: dict = {
        "limit": limit,
        "offset": offset,
        "country": _COUNTRIES[region],
    }
    if (phrase := quoted(query)) is not None:
        params["text"] = phrase
    return params


def _page(query: str, region: str, client: httpx.Client, offset: int) -> dict:
    response = http.get_with_backoff(
        client, _URL, params=_params(query, region, limit=_PAGE, offset=offset)
    )
    response.raise_for_status()
    return response.json()


def count(query: str, region: str, client: httpx.Client) -> int | None:
    params = _params(query, region, limit=1, offset=0)
    response = http.get_with_backoff(client, _URL, params=params)
    response.raise_for_status()
    data = response.json()
    if data.get("from_alternative"):
        return None
    total = data.get("count")
    return int(total) if isinstance(total, int | float) else None


def _item(job: dict) -> SourceItem:
    jid = str(job.get("id") or "")
    company = job.get("company") or {}
    code = company.get("code")
    url = (
        f"https://www.kalibrr.com/c/{code}/jobs/{jid}"
        if code
        else f"https://www.kalibrr.com/job-board/{jid}"
    )
    parts = [
        job.get("name"),
        company.get("name"),
        text.html_to_text(str(job.get("description") or "")),
    ]
    return SourceItem(
        source_id=jid,
        url=url if jid else "",
        text=" ".join(str(p) for p in parts if p),
    )


def search(query: str, region: str, client: httpx.Client) -> Iterator[SourceItem]:
    """Paged ``jobs`` rows. ``from_alternative`` means the page answers a
    fuzzy fallback query, not ours, so the whole stream stops."""
    offset = 0
    while True:
        data = _page(query, region, client, offset)
        if data.get("from_alternative"):
            return
        jobs = data.get("jobs") or []
        for job in jobs:
            yield _item(job)
        if len(jobs) < _PAGE:
            return
        offset += _PAGE
