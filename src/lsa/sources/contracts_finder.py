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

import httpx

from lsa.sources import http
from lsa.sources.phrase import quoted

SOURCE = "contracts-finder"
FAMILY = "procurement"
REGIONS = ("UK",)

_URL = (
    "https://www.contractsfinder.service.gov.uk"
    "/api/rest/2/search_notices/json"
)


def count(query: str, region: str, client: httpx.Client) -> int | None:
    criteria: dict = {}
    if (phrase := quoted(query)) is not None:
        criteria["keyword"] = phrase
    body = {"searchCriteria": criteria, "size": 1}
    response = http.post_with_backoff(client, _URL, json=body)
    response.raise_for_status()
    total = response.json().get("hitCount")
    return int(total) if isinstance(total, int | float) else None
