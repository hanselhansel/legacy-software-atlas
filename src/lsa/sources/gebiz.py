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

import httpx

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


def count(query: str, region: str, client: httpx.Client) -> int | None:
    params: dict = {"resource_id": RESOURCE_ID, "limit": 1}
    if phrase := _normalize(query):
        params["q"] = query
    else:
        # Match-all probe: unfiltered dataset total.
        response = http.get_with_backoff(
            client, _URL, params=params, min_interval=2.5
        )
        response.raise_for_status()
        result = response.json().get("result")
        if not isinstance(result, dict):
            return None
        return _total(result)
    hits = 0
    offset = 0
    for _ in range(_MAX_PAGES):
        page = params | {"limit": _PAGE, "offset": offset}
        response = http.get_with_backoff(
            client, _URL, params=page, min_interval=2.5
        )
        response.raise_for_status()
        result = response.json().get("result")
        if not isinstance(result, dict):
            return None
        total = _total(result)
        if total is None:
            return None
        records = result.get("records") or []
        hits += sum(
            1 for r in records if phrase in _normalize(_record_text(r))
        )
        offset += len(records)
        if not records or offset >= total:
            break
    return hits
