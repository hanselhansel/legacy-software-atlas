"""TED (Tenders Electronic Daily) notice counts (EU procurement).

POSTs a full-text expert query (``FT="..."``) to the keyless v3 search API
and reads ``totalNoticeCount``. The ``=`` term operator does exact matching;
the ``~`` operator stems search terms on multilingual fields like FT, which
is what inflated counts such as ``FT~"Baan"`` to fuzzy matches of the Dutch
word "baan" (help page, "Term operators"). The field comes back null on
syntax-check responses, which maps to ``None``.

An empty query becomes ``publication-date >= 20000101``, a documented
comparison against the archive start, so the sanity guard gets a match-all
total.
"""

from __future__ import annotations

import httpx

from lsa.sources import http
from lsa.sources.phrase import quoted

SOURCE = "ted"
FAMILY = "procurement"
REGIONS = ("EU",)

_URL = "https://api.ted.europa.eu/v3/notices/search"
# Dates must match the field's 20YYMMDD pattern; 2000 covers the archive.
_MATCH_ALL = "publication-date >= 20000101"


def count(query: str, region: str, client: httpx.Client) -> int | None:
    phrase = quoted(query)
    body = {
        "query": f"FT={phrase}" if phrase is not None else _MATCH_ALL,
        "fields": ["publication-number"],
        "limit": 1,
    }
    response = http.post_with_backoff(client, _URL, json=body)
    response.raise_for_status()
    total = response.json().get("totalNoticeCount")
    return int(total) if isinstance(total, int | float) else None
