"""USAspending award counts (US procurement).

POSTs ``filters.keywords`` to the keyless ``spending_by_award_count`` endpoint
and sums the procurement instrument groups (contracts + IDVs). Assistance
awards (grants, loans, direct payments, other) are not procurement items, so
they are not part of this count.
"""

from __future__ import annotations

import httpx

from lsa.sources import http

SOURCE = "usaspending"
FAMILY = "procurement"
REGIONS = ("US",)

_URL = "https://api.usaspending.gov/api/v2/search/spending_by_award_count/"
_GROUPS = ("contracts", "idvs")
# FY2025, the last completed federal fiscal year; matches the live-tested
# request recorded in research/sources.csv.
_TIME_PERIOD = [{"start_date": "2024-10-01", "end_date": "2025-09-30"}]


def count(query: str, region: str, client: httpx.Client) -> int | None:
    body = {
        "filters": {"keywords": [query], "time_period": _TIME_PERIOD}
    }
    response = http.post_with_backoff(client, _URL, json=body)
    response.raise_for_status()
    results = response.json().get("results")
    if not isinstance(results, dict):
        return None
    groups = [g for g in _GROUPS if isinstance(results.get(g), int)]
    if not groups:
        return None
    return sum(results[g] for g in groups)
