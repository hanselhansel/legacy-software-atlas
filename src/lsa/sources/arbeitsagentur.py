"""Bundesagentur fuer Arbeit Jobsuche counts (Germany, EU jobs).

GETs ``/pc/v6/jobs`` with a ``was`` full-text parameter and ``size=1``, then
reads ``maxErgebnisse``. Authentication is the publicly documented static
clientId ``jobboerse-jobsuche`` sent as ``X-API-Key`` (bund.dev OpenAPI spec of
the agency's own API). The spec types ``maxErgebnisse`` as string, so both int
and string are coerced.
"""

from __future__ import annotations

import httpx

from lsa.sources import http

SOURCE = "arbeitsagentur"
FAMILY = "jobs"
REGIONS = ("EU",)

_URL = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs"
_API_KEY = "jobboerse-jobsuche"


def count(query: str, region: str, client: httpx.Client) -> int | None:
    response = http.get_with_backoff(
        client,
        _URL,
        params={"was": query, "size": 1},
        headers={"X-API-Key": _API_KEY},
    )
    response.raise_for_status()
    total = response.json().get("maxErgebnisse")
    if isinstance(total, int | float):
        return int(total)
    if isinstance(total, str) and total.isdigit():
        return int(total)
    return None
