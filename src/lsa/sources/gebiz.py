"""GeBIZ awarded-tender counts via data.gov.sg (SG procurement).

GETs ``datastore_search`` on the MOF GeBIZ dataset (awarded tenders FY2021+).
The endpoint has no server-side phrase syntax: ``q`` matches loosely and its
validator rejects quotes and tsquery operators with HTTP 409 (verified live
2026-10-05), while ``full_text`` is ignored. So ``q`` is only the candidate
filter and ``count`` pages the matched records and keeps the ones whose
field text contains the exact phrase, as research/sources.csv prescribes
("filter tender_description client-side ... for exact-phrase counts").

An empty query skips ``q`` and returns the unfiltered ``result.total``, the
sanity guard's match-all probe.
"""

from __future__ import annotations

from collections.abc import Iterator

import httpx

from lsa.contracts import SourceItem
from lsa.sources import http

SOURCE = "gebiz"
FAMILY = "procurement"
REGIONS = ("SG",)

_URL = "https://data.gov.sg/api/action/datastore_search"
RESOURCE_ID = "d_acde1106003906a75c3fa052592f2fcb"
# datastore_search caps limit at 32000; a few pages cover the ~18k-row set.
_PAGE = 32000
_MAX_PAGES = 8


def _normalize(text: object) -> str:
    """Whitespace-collapsed, case-folded text for phrase containment."""
    return " ".join(str(text).split()).casefold()


def _record_text(record: dict) -> str:
    """Searchable text of a row: every non-internal field joined."""
    return " ".join(
        str(v)
        for k, v in record.items()
        if k != "rank" and not k.startswith("_")
    )


def _total(result: dict) -> int | None:
    total = result.get("total")
    return int(total) if isinstance(total, int | float) else None


def _matched(
    query: str, client: httpx.Client
) -> Iterator[tuple[list, int, str]]:
    """Each candidate page's records plus the dataset total; the candidate
    filter is ``q`` and phrase containment happens record-side, exactly as
    ``count`` does."""
    phrase = _normalize(query)
    params = {"resource_id": RESOURCE_ID, "q": query}
    offset = 0
    for _ in range(_MAX_PAGES):
        page = params | {"limit": _PAGE, "offset": offset}
        response = http.get_with_backoff(
            client, _URL, params=page, min_interval=2.5
        )
        response.raise_for_status()
        result = response.json().get("result")
        if not isinstance(result, dict):
            return
        total = _total(result)
        if total is None:
            return
        records = result.get("records") or []
        yield records, total, phrase
        offset += len(records)
        if not records or offset >= total:
            return


def count(query: str, region: str, client: httpx.Client) -> int | None:
    if not _normalize(query):
        # Match-all probe: unfiltered dataset total.
        params = {"resource_id": RESOURCE_ID, "limit": 1}
        response = http.get_with_backoff(
            client, _URL, params=params, min_interval=2.5
        )
        response.raise_for_status()
        result = response.json().get("result")
        if not isinstance(result, dict):
            return None
        return _total(result)
    hits = 0
    valid = False
    for records, _total_, phrase in _matched(query, client):
        valid = True
        hits += sum(
            1 for r in records if phrase in _normalize(_record_text(r))
        )
    return hits if valid else None


def search(query: str, region: str, client: httpx.Client) -> Iterator[SourceItem]:
    """The exact-phrase matched records as items. The datastore has no
    per-record page, so ``url`` anchors the row inside the dataset URL."""
    if not _normalize(query):
        return
    for records, _total_, phrase in _matched(query, client):
        for record in records:
            if phrase not in _normalize(_record_text(record)):
                continue
            sid = str(record.get("tender_no") or record.get("_id") or "")
            yield SourceItem(
                source_id=sid,
                url=f"{_URL}?resource_id={RESOURCE_ID}#row={sid}" if sid else "",
                text=_record_text(record),
            )
