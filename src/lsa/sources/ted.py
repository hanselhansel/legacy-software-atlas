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

from collections.abc import Iterator

import httpx

from lsa.contracts import SourceItem
from lsa.sources import http
from lsa.sources.phrase import quoted

SOURCE = "ted"
FAMILY = "procurement"
REGIONS = ("EU",)

_URL = "https://api.ted.europa.eu/v3/notices/search"
# Dates must match the field's 20YYMMDD pattern; 2000 covers the archive.
_MATCH_ALL = "publication-date >= 20000101"

# Item search pages the same endpoint; ``fields`` widen from just the
# publication number to the fields Jev reads. ``page`` is 1-based and the
# API caps ``limit`` at 250.
_PAGE = 50
_ITEM_FIELDS = ["publication-number", "notice-title", "buyer-name", "description"]
_DETAIL = "https://ted.europa.eu/en/notice/-/detail/"


def _body(query: str, *, fields: list[str], limit: int, page: int) -> dict:
    phrase = quoted(query)
    return {
        "query": f"FT={phrase}" if phrase is not None else _MATCH_ALL,
        "fields": fields,
        "limit": limit,
        "page": page,
    }


def count(query: str, region: str, client: httpx.Client) -> int | None:
    body = _body(query, fields=["publication-number"], limit=1, page=1)
    response = http.post_with_backoff(client, _URL, json=body)
    response.raise_for_status()
    total = response.json().get("totalNoticeCount")
    return int(total) if isinstance(total, int | float) else None


def _texts(value: object) -> str:
    """A TED field is a lang -> [values] dict (or a plain list/str)."""
    if isinstance(value, dict):
        parts = [str(v) for vals in value.values() for v in _as_list(vals)]
        return " ".join(parts)
    if isinstance(value, list):
        return " ".join(str(v) for v in value)
    return str(value) if value else ""


def _as_list(value: object) -> list:
    return value if isinstance(value, list) else [value]


def _item(notice: dict) -> SourceItem:
    number = str(notice.get("publication-number") or "")
    text = " ".join(
        t
        for t in (
            _texts(notice.get("notice-title")),
            _texts(notice.get("buyer-name")),
            _texts(notice.get("description")),
        )
        if t
    )
    return SourceItem(
        source_id=number, url=f"{_DETAIL}{number}" if number else "", text=text
    )


def search(query: str, region: str, client: httpx.Client) -> Iterator[SourceItem]:
    """Paged notices for the query; a short page marks the last page."""
    page = 1
    while True:
        body = _body(query, fields=_ITEM_FIELDS, limit=_PAGE, page=page)
        response = http.post_with_backoff(client, _URL, json=body)
        response.raise_for_status()
        notices = response.json().get("notices") or []
        for notice in notices:
            yield _item(notice)
        if len(notices) < _PAGE:
            return
        page += 1
