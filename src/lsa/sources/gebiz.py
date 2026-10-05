"""GeBIZ awarded-tender counts via data.gov.sg (SG procurement).

GETs ``datastore_search`` on the MOF GeBIZ dataset (awarded tenders FY2021+)
with a full-text ``q`` and reads ``result.total``. ``q`` matches loosely
(either word), so this count is an upper bound on exact-phrase hits.
"""

from __future__ import annotations

import httpx

from lsa.sources import http

SOURCE = "gebiz"
FAMILY = "procurement"
REGIONS = ("SG",)

_URL = "https://data.gov.sg/api/action/datastore_search"
RESOURCE_ID = "d_acde1106003906a75c3fa052592f2fcb"


def count(query: str, region: str, client: httpx.Client) -> int | None:
    # datastore_search allows 4 calls per 10 s without a developer key, so
    # calls are paced at 2.5 s rather than the 1 s default.
    response = http.get_with_backoff(
        client,
        _URL,
        params={"resource_id": RESOURCE_ID, "q": query, "limit": 1},
        min_interval=2.5,
    )
    response.raise_for_status()
    result = response.json().get("result")
    if not isinstance(result, dict):
        return None
    total = result.get("total")
    return int(total) if isinstance(total, int | float) else None
