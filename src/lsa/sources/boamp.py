"""BOAMP tender counts via the DILA opendatasoft portal (France, procurement).

GETs the ``boamp`` dataset ``records`` endpoint with an ODSQL ``search()``
where clause and ``limit=0``, then reads ``total_count``. Region code is EU
per the brief (France is reported under EU-level sources).

The portal's robots.txt disallows /api/ for generic crawlers while the licence
(etalab-2.0) permits reuse; we call it as a declared, low-rate research client,
which is what the API channel exists for.
"""

from __future__ import annotations

import httpx

from lsa.sources import http

SOURCE = "boamp"
FAMILY = "procurement"
REGIONS = ("EU",)

_URL = (
    "https://boamp-datadila.opendatasoft.com"
    "/api/explore/v2.1/catalog/datasets/boamp/records"
)


def _odsql_string(query: str) -> str:
    return query.replace("\\", "\\\\").replace('"', '\\"')


def count(query: str, region: str, client: httpx.Client) -> int | None:
    response = http.get_with_backoff(
        client,
        _URL,
        params={"where": f'search("{_odsql_string(query)}")', "limit": 0},
    )
    response.raise_for_status()
    total = response.json().get("total_count")
    return int(total) if isinstance(total, int | float) else None
