"""USAspending award counts (US procurement).

POSTs ``filters.keywords`` to the keyless ``spending_by_award_count`` endpoint
and sums the procurement instrument groups (contracts + IDVs). Assistance
awards (grants, loans, direct payments, other) are not procurement items, so
they are not part of this count.

Each keyword is wrapped in double quotes: per the API contract, quoted terms
perform exact matches rather than the default fuzzier full-text match
(award_ids doc; verified live 2026-10-05). An empty query omits ``keywords``
entirely, which returns the unfiltered FY total used as the sanity guard's
match-all probe.
"""

from __future__ import annotations

from collections.abc import Iterator

import httpx

from lsa.contracts import SourceItem
from lsa.sources import http
from lsa.sources.phrase import quoted

SOURCE = "usaspending"
FAMILY = "procurement"
REGIONS = ("US",)

_URL = "https://api.usaspending.gov/api/v2/search/spending_by_award_count/"
_GROUPS = ("contracts", "idvs")
# FY2025, the last completed federal fiscal year; matches the live-tested
# request recorded in research/sources.csv.
_TIME_PERIOD = [{"start_date": "2024-10-01", "end_date": "2025-09-30"}]

# Item search uses the sibling ``spending_by_award`` endpoint: same filters,
# paged ``results`` rows keyed by display names plus ``internal_id`` /
# ``generated_internal_id``, and ``page_metadata.hasNext`` for paging.
_URL_SEARCH = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
_FIELDS = [
    "Award ID",
    "Recipient Name",
    "Start Date",
    "End Date",
    "Award Amount",
    "Awarding Agency",
    "Description",
]
# Contracts plus the IDV family, matching the count's ``contracts`` +
# ``idvs`` groups.
_PROCUREMENT_TYPES = (
    "A", "B", "C", "D",
    "IDV_A", "IDV_B", "IDV_B_A", "IDV_B_B", "IDV_B_C",
    "IDV_C", "IDV_D", "IDV_E",
)
_PAGE = 100
_AWARD_URL = "https://www.usaspending.gov/award/"


def _filters(query: str) -> dict:
    filters: dict = {"time_period": _TIME_PERIOD}
    if (phrase := quoted(query)) is not None:
        filters["keywords"] = [phrase]
    return filters


def count(query: str, region: str, client: httpx.Client) -> int | None:
    filters = _filters(query)
    response = http.post_with_backoff(client, _URL, json={"filters": filters})
    response.raise_for_status()
    results = response.json().get("results")
    if not isinstance(results, dict):
        return None
    groups = [g for g in _GROUPS if isinstance(results.get(g), int)]
    if not groups:
        return None
    return sum(results[g] for g in groups)


def _award_item(row: dict) -> SourceItem:
    gid = str(row.get("generated_internal_id") or "")
    parts = [
        row.get("Award ID"),
        row.get("Recipient Name"),
        row.get("Awarding Agency"),
        row.get("Award Amount"),
        row.get("Start Date"),
        row.get("Description"),
    ]
    text = " ".join(str(p) for p in parts if p is not None)
    return SourceItem(
        source_id=gid or str(row.get("internal_id") or ""),
        url=f"{_AWARD_URL}{gid}" if gid else "",
        text=text,
    )


def search(query: str, region: str, client: httpx.Client) -> Iterator[SourceItem]:
    """Paged award rows for the query; item text is the award row itself."""
    filters = _filters(query)
    filters["award_type_codes"] = list(_PROCUREMENT_TYPES)
    page = 1
    while True:
        response = http.post_with_backoff(
            client,
            _URL_SEARCH,
            json={
                "filters": filters,
                "fields": _FIELDS,
                "page": page,
                "limit": _PAGE,
                "sort": "Start Date",
                "order": "desc",
            },
        )
        response.raise_for_status()
        payload = response.json()
        for row in payload.get("results") or []:
            yield _award_item(row)
        if not (payload.get("page_metadata") or {}).get("hasNext"):
            return
        page += 1
