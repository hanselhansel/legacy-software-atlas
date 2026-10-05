"""TED (Tenders Electronic Daily) notice counts (EU procurement).

POSTs a full-text expert query (``FT~"..."``) to the keyless v3 search API and
reads ``totalNoticeCount``. The field comes back null on syntax-check
responses, which maps to ``None``.
"""

from __future__ import annotations

import httpx

from lsa.sources import http

SOURCE = "ted"
FAMILY = "procurement"
REGIONS = ("EU",)

_URL = "https://api.ted.europa.eu/v3/notices/search"


def count(query: str, region: str, client: httpx.Client) -> int | None:
    phrase = query.replace('"', "").strip()
    body = {
        "query": f'FT~"{phrase}"',
        "fields": ["publication-number"],
        "limit": 1,
    }
    response = http.post_with_backoff(client, _URL, json=body)
    response.raise_for_status()
    total = response.json().get("totalNoticeCount")
    return int(total) if isinstance(total, int | float) else None
