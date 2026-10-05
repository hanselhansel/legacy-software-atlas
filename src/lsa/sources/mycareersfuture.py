"""MyCareersFuture job counts (SG jobs).

GETs the portal's public ``/v2/jobs`` search endpoint with ``search``, a
``limit`` of 1 and ``page=0``, then reads the top-level ``total``. The
endpoint is undocumented; the shape was confirmed by a live call in
sources.csv. ``search`` carries the query as a double-quoted exact phrase;
an empty query omits ``search`` for the sanity guard's match-all probe.
"""

from __future__ import annotations

import httpx

from lsa.sources import http
from lsa.sources.phrase import quoted

SOURCE = "mycareersfuture"
FAMILY = "jobs"
REGIONS = ("SG",)

_URL = "https://api.mycareersfuture.gov.sg/v2/jobs"


def count(query: str, region: str, client: httpx.Client) -> int | None:
    params: dict = {"limit": 1, "page": 0}
    if (phrase := quoted(query)) is not None:
        params["search"] = phrase
    response = http.get_with_backoff(client, _URL, params=params)
    response.raise_for_status()
    total = response.json().get("total")
    return int(total) if isinstance(total, int | float) else None
