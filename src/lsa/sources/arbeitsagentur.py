"""Bundesagentur fuer Arbeit Jobsuche counts (Germany, EU jobs).

GETs ``/pc/v6/jobs`` with a ``was`` full-text parameter and ``size=1``, then
reads ``maxErgebnisse``. Authentication is the publicly documented static
clientId ``jobboerse-jobsuche`` sent as ``X-API-Key`` (bund.dev OpenAPI spec of
the agency's own API). The spec types ``maxErgebnisse`` as string, so both int
and string are coerced.

``was`` parses Lucene-style syntax: an unescaped ``/`` splits the phrase into
OR terms even inside quotes, so specials are backslash-escaped and the phrase
is wrapped in double quotes (verified live 2026-10-05: ``"SAP FI\\/CO
Berater"`` returned 9 vs 208 unquoted, ``"z\\/TPF"`` 0 vs 191534 unescaped).
An empty query omits ``was`` for the sanity guard's match-all probe.
"""

from __future__ import annotations

from collections.abc import Iterator

import httpx

from lsa.contracts import SourceItem
from lsa.sources import http
from lsa.sources.phrase import escaped

SOURCE = "arbeitsagentur"
FAMILY = "jobs"
REGIONS = ("EU",)

_URL = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs"
_API_KEY = "jobboerse-jobsuche"
_DETAIL = "https://www.arbeitsagentur.de/jobsuche/jobdetail/"
_PAGE = 100


def _page(query: str, client: httpx.Client, page: int, size: int) -> dict:
    params: dict = {"size": size, "page": page}
    if (phrase := escaped(query)) is not None:
        params["was"] = phrase
    response = http.get_with_backoff(
        client,
        _URL,
        params=params,
        headers={"X-API-Key": _API_KEY},
    )
    response.raise_for_status()
    return response.json()


def count(query: str, region: str, client: httpx.Client) -> int | None:
    total = _page(query, client, page=1, size=1).get("maxErgebnisse")
    if isinstance(total, int | float):
        return int(total)
    if isinstance(total, str) and total.isdigit():
        return int(total)
    return None


def _item(job: dict) -> SourceItem:
    jid = str(job.get("hashId") or job.get("refnr") or "")
    parts = [
        job.get("titel"),
        job.get("arbeitgeber"),
        (job.get("arbeitsort") or {}).get("ort"),
        job.get("aktuelleVeroeffentlichungsdatum"),
        job.get("beruf"),
    ]
    return SourceItem(
        source_id=jid,
        url=f"{_DETAIL}{jid}" if jid else "",
        text=" ".join(str(p) for p in parts if p),
    )


def search(query: str, region: str, client: httpx.Client) -> Iterator[SourceItem]:
    """Paged ``stellenangebote`` rows; a short page marks the last page."""
    page = 1
    while True:
        jobs = _page(query, client, page, _PAGE).get("stellenangebote") or []
        for job in jobs:
            yield _item(job)
        if len(jobs) < _PAGE:
            return
        page += 1
