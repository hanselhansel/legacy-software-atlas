"""USAspending federal contract awards (US procurement, lane L).

Two calls per kept award. ``POST /api/v2/search/spending_by_award/`` with
the quoted keyword (exact match, same contract as the count lane) pages
candidate contract awards — type codes A, B, C, D only, IDVs excluded —
with Award Amount, period-of-performance Start/End Dates and PSC. Then
``GET /api/v2/awards/{generated_internal_id}/`` returns the award detail:
``latest_transaction_contract_data`` carries ``extent_competed`` /
``extent_competed_description`` and ``other_than_full_and_open`` (the
search endpoint accepts an "Extent Competed" field but always returns
null; verified live 2026-10-05), and ``period_of_performance`` gives the
potential end date, the full contract length including options.

The detail call happens inside the lazy iteration, so ``per_query`` caps
both awards and detail calls. A failed detail call degrades the row to
procedure ``unknown``; it never drops the award.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator

import httpx

from lsa.awards.common import AwardRow, QueryRow
from lsa.sources import http, robots
from lsa.sources.phrase import quoted

SOURCE = "usaspending"
SOURCES = (SOURCE,)
REGIONS = ("US",)

_URL_SEARCH = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
_URL_DETAIL = "https://api.usaspending.gov/api/v2/awards/{}/"
_AWARD_URL = "https://www.usaspending.gov/award/"
# FY2025, the last completed federal fiscal year: same window the count
# lane uses, so awards and counts cover the same population.
_TIME_PERIOD = [{"start_date": "2024-10-01", "end_date": "2025-09-30"}]
_CONTRACT_TYPES = ["A", "B", "C", "D"]
_FIELDS = [
    "Award ID",
    "Recipient Name",
    "Start Date",
    "End Date",
    "Award Amount",
    "Awarding Agency",
    "Description",
    "PSC",
]
_PAGE = 100

# latest_transaction_contract_data.extent_competed_description values.
_EXTENT_PROCEDURE = {
    "FULL AND OPEN COMPETITION": "open",
    "FULL AND OPEN COMPETITION AFTER EXCLUSION OF SOURCES": "restricted",
    "COMPETED UNDER SIMPLIFIED ACQUISITION PROCEDURES": "restricted",
    "OTHER THAN FULL AND OPEN COMPETITION": "negotiated_no_competition",
    "FOLLOW ON TO COMPETED ACTION": "negotiated_no_competition",
    "NOT COMPETED": "direct",
    "NOT COMPETED UNDER SIMPLIFIED ACQUISITION PROCEDURES": "direct",
    "NOT AVAILABLE FOR COMPETITION": "direct",
}


def _search(query: str, client: httpx.Client) -> Iterator[dict]:
    """Paged spending_by_award result rows for the quoted keyword."""
    page = 1
    while True:
        response = http.post_with_backoff(
            client,
            _URL_SEARCH,
            json={
                "filters": {
                    "time_period": _TIME_PERIOD,
                    "award_type_codes": _CONTRACT_TYPES,
                    **(
                        {"keywords": [phrase]}
                        if (phrase := quoted(query)) is not None
                        else {}
                    ),
                },
                "fields": _FIELDS,
                "page": page,
                "limit": _PAGE,
                "sort": "Start Date",
                "order": "desc",
            },
        )
        response.raise_for_status()
        payload = response.json()
        yield from payload.get("results") or []
        if not (payload.get("page_metadata") or {}).get("hasNext"):
            return
        page += 1


def _detail(generated_internal_id: str, client: httpx.Client) -> dict:
    """Award detail dict, or {} when the fetch fails."""
    try:
        response = http.get_with_backoff(
            client, _URL_DETAIL.format(generated_internal_id)
        )
        if response.status_code != 200:
            return {}
        return response.json()
    except Exception:  # noqa: BLE001 - detail failure degrades, never drops
        return {}


def _procedure(detail: dict) -> str:
    contract = detail.get("latest_transaction_contract_data") or {}
    desc = contract.get("extent_competed_description")
    if not isinstance(desc, str):
        return "unknown"
    return _EXTENT_PROCEDURE.get(desc.strip().upper(), "unknown")


def _date(value: object) -> str:
    return str(value or "")[:10]


def _award_row(hit: dict, detail: dict, row: QueryRow) -> AwardRow:
    gid = str(hit.get("generated_internal_id") or hit.get("internal_id") or "")
    pop = detail.get("period_of_performance") or {}
    psc = hit.get("PSC")
    if isinstance(psc, dict):
        psc = psc.get("code")
    return AwardRow(
        award_id=f"{SOURCE}:{gid}",
        source=SOURCE,
        region=row.region,
        category_hint=row.category,
        query=row.query,
        buyer=str(
            (detail.get("awarding_agency") or {}).get("name")
            or hit.get("Awarding Agency")
            or ""
        ),
        title=str(detail.get("piid") or hit.get("Award ID") or ""),
        text=str(detail.get("description") or hit.get("Description") or ""),
        value=(
            detail.get("total_obligation")
            if isinstance(detail.get("total_obligation"), int | float)
            else (
                hit.get("Award Amount")
                if isinstance(hit.get("Award Amount"), int | float)
                else None
            )
        ),
        currency="USD",
        start_date=_date(pop.get("start_date") or hit.get("Start Date")),
        # Potential end = full contract length incl. option years; the
        # current end is what's exercised so far.
        end_date=_date(
            pop.get("potential_end_date")
            or pop.get("end_date")
            or hit.get("End Date")
        ),
        duration_months=None,
        procedure=_procedure(detail),
        cpv_or_psc=str(psc or ""),
        url=f"{_AWARD_URL}{gid}" if gid else "",
    )


def collect(
    rows: list[QueryRow],
    client: httpx.Client,
    *,
    per_query: int | None,
    log: Callable[[str], None] | None = print,
) -> Iterator[AwardRow]:
    """Contract award rows for the US queries, lazily paged."""
    log = log or (lambda _m: None)
    rows = [r for r in rows if r.region in REGIONS]
    if not rows:
        return
    if not robots.allowed(_URL_SEARCH, client):
        log(f"{SOURCE}: robots.txt disallows {_URL_SEARCH}, skipped")
        return
    for row in rows:
        kept = 0
        try:
            for hit in _search(row.query, client):
                if per_query is not None and kept >= per_query:
                    break
                gid = str(
                    hit.get("generated_internal_id")
                    or hit.get("internal_id")
                    or ""
                )
                if not gid:
                    continue
                yield _award_row(hit, _detail(gid, client), row)
                kept += 1
        except Exception as exc:  # noqa: BLE001 - one bad query never stops a run
            log(f"{SOURCE} {row.region} {row.query!r}: {exc}")
