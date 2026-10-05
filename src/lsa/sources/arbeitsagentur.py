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

import httpx

from lsa.sources import http
from lsa.sources.phrase import escaped

SOURCE = "arbeitsagentur"
FAMILY = "jobs"
REGIONS = ("EU",)

_URL = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs"
_API_KEY = "jobboerse-jobsuche"


def count(query: str, region: str, client: httpx.Client) -> int | None:
    params: dict = {"size": 1}
    if (phrase := escaped(query)) is not None:
        params["was"] = phrase
    response = http.get_with_backoff(
        client,
        _URL,
        params=params,
        headers={"X-API-Key": _API_KEY},
    )
    response.raise_for_status()
    total = response.json().get("maxErgebnisse")
    if isinstance(total, int | float):
        return int(total)
    if isinstance(total, str) and total.isdigit():
        return int(total)
    return None
