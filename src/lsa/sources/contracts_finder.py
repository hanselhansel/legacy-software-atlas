"""Contracts Finder notice counts (UK procurement).

POSTs a keyword ``searchCriteria`` to the v2 ``search_notices`` endpoint and
reads ``hitCount``. Anonymous search works; the documented OAuth2 client
credentials are only needed for publishing.
"""

from __future__ import annotations

import httpx

from lsa.sources import http

SOURCE = "contracts-finder"
FAMILY = "procurement"
REGIONS = ("UK",)

_URL = (
    "https://www.contractsfinder.service.gov.uk"
    "/api/rest/2/search_notices/json"
)


def count(query: str, region: str, client: httpx.Client) -> int | None:
    body = {"searchCriteria": {"keyword": query}, "size": 1}
    response = http.post_with_backoff(client, _URL, json=body)
    response.raise_for_status()
    total = response.json().get("hitCount")
    return int(total) if isinstance(total, int | float) else None
