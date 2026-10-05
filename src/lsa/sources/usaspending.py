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


def count(query: str, region: str, client: httpx.Client) -> int | None:
    response = http.post_with_backoff(
        client, _URL, json={"filters": {"keywords": [query]}}
    )
    response.raise_for_status()
    results = response.json().get("results")
    if not isinstance(results, dict):
        return None
    groups = [g for g in _GROUPS if isinstance(results.get(g), int)]
    if not groups:
        return None
    return sum(results[g] for g in groups)
