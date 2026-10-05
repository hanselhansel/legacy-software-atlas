"""Kalibrr job counts (ID and PH jobs).

GETs the job board's public ``kjs/job_board/search`` endpoint with ``text``
carrying the query as a double-quoted exact phrase and a ``country`` filter
mapped from the region code, then reads ``count``. The endpoint is
undocumented; the shape was confirmed by live calls in sources.csv. An
empty query omits ``text`` for the sanity guard's match-all probe.

``from_alternative: true`` in the response means there was no exact match and
the count is a fuzzy fallback for different terms. That total does not
describe the requested query, so ``count`` returns ``None`` for it.
"""

from __future__ import annotations

import httpx

from lsa.sources import http
from lsa.sources.phrase import quoted

SOURCE = "kalibrr"
FAMILY = "jobs"
REGIONS = ("ID", "PH")

_COUNTRIES = {"ID": "Indonesia", "PH": "Philippines"}
_URL = "https://www.kalibrr.com/kjs/job_board/search"


def count(query: str, region: str, client: httpx.Client) -> int | None:
    params: dict = {
        "limit": 1,
        "offset": 0,
        "country": _COUNTRIES[region],
    }
    if (phrase := quoted(query)) is not None:
        params["text"] = phrase
    response = http.get_with_backoff(client, _URL, params=params)
    response.raise_for_status()
    data = response.json()
    if data.get("from_alternative"):
        return None
    total = data.get("count")
    return int(total) if isinstance(total, int | float) else None
