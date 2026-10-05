"""AusTender OCDS award collection (AU federal contracts, lane L).

``GET /ocds/findByDates/contractPublished/{start}/{end}`` returns OCDS
release packages paged by a ``links.next`` cursor. Each release's
``contracts[]`` are the awards, keyed by their ``CN`` number. The API
takes no keyword filter, so releases are windowed (``_WINDOW_DAYS``,
``_CHUNK_DAYS`` per slice) and matched locally by phrase on contract
title + description + procuring entity.

Verified live 2026-10-05: ~100 releases/day; ``parties`` carry
``procuringEntity``/``supplier`` roles; ``contract.value.amount`` is a
decimal string; UNSPSC classifications sit under ``contracts[].items``;
``tender.procurementMethod`` is ``open`` or ``limited``.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterator

import httpx

from lsa.awards.common import (
    AwardRow,
    QueryRow,
    date_chunks,
    matches_phrase,
    ocds_procedure,
)
from lsa.sources import http, robots

SOURCE = "austender"
SOURCES = (SOURCE,)
REGIONS = ("AU",)

URL = "https://api.tenders.gov.au/ocds/findByDates/contractPublished"
_BY_ID = "https://api.tenders.gov.au/ocds/findById"

_WINDOW_DAYS = 90
_CHUNK_DAYS = 7


def _party(release: dict, role: str) -> str:
    for p in release.get("parties") or []:
        if role in (p.get("roles") or []):
            return str(p.get("name") or "")
    return ""


def _contract_text(release: dict, contract: dict) -> str:
    return " ".join(
        str(part)
        for part in (
            contract.get("title"),
            contract.get("description"),
            _party(release, "procuringEntity"),
        )
        if part
    )


def _contract_row(
    release: dict, contract: dict, row: QueryRow
) -> AwardRow:
    cn = str(contract.get("id") or contract.get("awardID") or "")
    period = contract.get("period") or {}
    value = contract.get("value") or {}
    try:
        amount = float(str(value.get("amount"))) if value.get("amount") is not None else None
    except (TypeError, ValueError):
        amount = None
    cpv = ";".join(
        str((i.get("classification") or {}).get("id"))
        for i in contract.get("items") or []
        if (i.get("classification") or {}).get("id")
    )
    return AwardRow(
        award_id=f"{SOURCE}:{cn}",
        source=SOURCE,
        region=row.region,
        category_hint=row.category,
        query=row.query,
        buyer=_party(release, "procuringEntity"),
        title=str(contract.get("title") or ""),
        text=str(contract.get("description") or ""),
        value=amount,
        currency=str(value.get("currency") or ""),
        start_date=str(period.get("startDate") or "")[:10],
        end_date=str(period.get("endDate") or "")[:10],
        duration_months=None,
        procedure=ocds_procedure(
            (release.get("tender") or {}).get("procurementMethod")
        ),
        cpv_or_psc=cpv,
        url=f"{_BY_ID}/{cn}" if cn else "",
    )


def collect(
    rows: list[QueryRow],
    client: httpx.Client,
    *,
    per_query: int | None,
    log: Callable[[str], None] | None = print,
) -> Iterator[AwardRow]:
    """Contract rows for AU queries; first free matching query wins a CN."""
    log = log or (lambda _m: None)
    rows = [r for r in rows if r.region in REGIONS]
    if not rows:
        return
    if not robots.allowed(URL, client):
        log(f"{SOURCE}: robots.txt disallows {URL}, skipped")
        return
    seen: set[str] = set()
    kept: Counter[str] = Counter()
    try:
        for start, end in date_chunks(_WINDOW_DAYS, _CHUNK_DAYS):
            if per_query is not None and all(
                kept[r.query] >= per_query for r in rows
            ):
                return
            url = f"{URL}/{start}T00:00:00Z/{end}T00:00:00Z"
            while url:
                response = http.get_with_backoff(client, url)
                response.raise_for_status()
                package = response.json()
                for release in package.get("releases") or []:
                    for contract in release.get("contracts") or []:
                        cn = str(contract.get("id") or "")
                        if not cn or cn in seen:
                            continue
                        matched = next(
                            (
                                r
                                for r in rows
                                if (
                                    per_query is None
                                    or kept[r.query] < per_query
                                )
                                and matches_phrase(
                                    _contract_text(release, contract),
                                    r.query,
                                )
                            ),
                            None,
                        )
                        if matched is None:
                            continue
                        seen.add(cn)
                        kept[matched.query] += 1
                        yield _contract_row(release, contract, matched)
                url = (package.get("links") or {}).get("next")
    except Exception as exc:  # noqa: BLE001 - one bad window never stops a run
        log(f"{SOURCE}: {exc}")
