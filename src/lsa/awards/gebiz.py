"""GeBIZ awarded-tender collection via data.gov.sg (SG procurement, lane L).

Reuses the count lane's ``sources.gebiz._matched`` paging verbatim: the
``q`` param is only a loose candidate filter and the exact-phrase match
happens record-side on the joined field text (the endpoint 409s on
quoted phrases; verified live 2026-10-05).

Each record is an awarded tender: ``agency`` is the buyer,
``awarded_amt`` the SGD award value, ``award_date`` the ``d/m/yyyy``
award date (no contract period exists in the dataset), and
``tender_no`` embeds the procurement type at offset 3..6 after the
agency code (``ACR000ETT21000001`` -> ``ETT`` open e-tender). "Awarded
to No Suppliers" rows are not awards and are skipped.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterator
from datetime import date

import httpx

from lsa.awards.common import AwardRow, QueryRow
from lsa.sources import gebiz as _src
from lsa.sources import robots

SOURCE = "gebiz"
SOURCES = (SOURCE,)
REGIONS = ("SG",)

_URL = _src._URL
_ROW_URL = f"{_URL}?resource_id={_src.RESOURCE_ID}"

_TYPE_CODE = re.compile(r"^[A-Z]+000([A-Z]{3})\d")
# GeBIZ tender_no type codes -> study procedure. ETT e-tenders are open;
# requests for quotation go to invited suppliers; small-value purchases
# are direct buys.
_TYPE_PROCEDURE = {
    "ETT": "open",
    "EPT": "open",
    "RIT": "restricted",
    "ERQ": "restricted",
    "ESQ": "restricted",
    "ITQ": "restricted",
    "SVP": "direct",
}


def _award_date(value: str) -> str:
    """GeBIZ ``d/m/yyyy`` award dates to ISO."""
    try:
        day, month, year = (int(part) for part in value.split("/"))
        return date(year, month, day).isoformat()
    except (ValueError, TypeError):
        return ""


def _procedure(tender_no: str) -> str:
    match = _TYPE_CODE.match(tender_no or "")
    if not match:
        return "unknown"
    return _TYPE_PROCEDURE.get(match.group(1), "unknown")


def _awarded(status: str) -> bool:
    text = (status or "").casefold()
    return "award" in text and "no supplier" not in text


def _record_row(record: dict, row: QueryRow) -> AwardRow | None:
    """The award row for a matched record, None when not an award."""
    status = str(record.get("tender_detail_status") or "")
    if not _awarded(status):
        return None
    tender_no = str(record.get("tender_no") or record.get("_id") or "")
    supplier = str(record.get("supplier_name") or "")
    try:
        amount = float(str(record.get("awarded_amt") or "").replace(",", ""))
    except ValueError:
        amount = None
    native = f"{tender_no}-{supplier}".rstrip("-")
    return AwardRow(
        award_id=f"{SOURCE}:{native}",
        source=SOURCE,
        region=row.region,
        category_hint=row.category,
        query=row.query,
        buyer=str(record.get("agency") or ""),
        title=tender_no,
        text=str(record.get("tender_description") or ""),
        value=amount,
        currency="SGD",
        start_date=_award_date(str(record.get("award_date") or "")),
        end_date="",
        duration_months=None,
        procedure=_procedure(tender_no),
        cpv_or_psc="",
        url=f"{_ROW_URL}#row={native}" if native else "",
    )


def collect(
    rows: list[QueryRow],
    client: httpx.Client,
    *,
    per_query: int | None,
    log: Callable[[str], None] | None = print,
) -> Iterator[AwardRow]:
    """Awarded records for SG queries; ``q`` narrows, phrase decides."""
    log = log or (lambda _m: None)
    rows = [r for r in rows if r.region in REGIONS]
    if not rows:
        return
    if not robots.allowed(_URL, client):
        log(f"{SOURCE}: robots.txt disallows {_URL}, skipped")
        return
    for row in rows:
        kept = 0
        seen: set[str] = set()
        try:
            for records, _total, phrase in _src._matched(row.query, client):
                for record in records:
                    if per_query is not None and kept >= per_query:
                        return
                    if phrase not in _src._normalize(
                        _src._record_text(record)
                    ):
                        continue
                    award_row = _record_row(record, row)
                    if award_row is None or award_row.award_id in seen:
                        continue
                    seen.add(award_row.award_id)
                    yield award_row
                    kept += 1
        except Exception as exc:  # noqa: BLE001 - one bad query never stops a run
            log(f"{SOURCE} {row.region} {row.query!r}: {exc}")
