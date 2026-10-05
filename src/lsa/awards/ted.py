"""TED v3 award collection (EU procurement, lane L).

``POST /v3/notices/search`` with the same quoted ``FT=...`` expert query
the count lane uses. Every matched notice — tender or contract-award —
yields a row; the value prefers the awarded tender value over the lot's
estimated value, and the duration prefers explicit contract dates over
the lot's stated duration (converted to months from its unit).

TED field values come back as scalars, ``lang -> value(s)`` dicts, or
lists; ``_pick`` normalizes all three. Field names verified live
2026-10-05 (``organisation-name-buyer`` / ``description-lot`` work,
``buyer-name`` / ``description`` do not).
"""

from __future__ import annotations

from collections.abc import Callable, Iterator

import httpx

from lsa.awards.common import AwardRow, QueryRow
from lsa.sources import http, robots
from lsa.sources.phrase import quoted

SOURCE = "ted"
SOURCES = (SOURCE,)
REGIONS = ("EU",)

_URL = "https://api.ted.europa.eu/v3/notices/search"
_DETAIL = "https://ted.europa.eu/en/notice/-/detail/"
_PAGE = 100  # API caps limit at 250; 100 keeps payloads readable
_FIELDS = [
    "publication-number",
    "notice-title",
    "notice-type",
    "organisation-name-buyer",
    "description-lot",
    "publication-date",
    "procedure-type",
    "classification-cpv",
    "estimated-value-lot",
    "estimated-value-cur-lot",
    "tender-value",
    "tender-value-cur",
    "result-value-lot",
    "result-value-cur-lot",
    "duration-period-value-lot",
    "duration-period-unit-lot",
    "contract-duration-start-date-lot",
    "contract-duration-end-date-lot",
]

# eForms procedure-type codelist -> study procedure.
_TED_PROCEDURE = {
    "open": "open",
    "restricted": "restricted",
    "comp-proc-neg": "restricted",
    "comp-dial": "restricted",
    "innovation-partn": "restricted",
    "neg-with-call": "restricted",
    "comp-tend": "restricted",
    "exp-int-rail": "restricted",
    "neg-wout-call": "negotiated_no_competition",
    "dir-award": "direct",
    "oth-sing": "other",
    "oth-mult": "other",
    "oth": "other",
}
_UNIT_MONTHS = {"month": 1.0, "year": 12.0, "week": 1 / 4.345, "day": 1 / 30.4375}


def _pick(value: object) -> str:
    """One string out of a TED field: eng of a lang dict, first of a list."""
    if isinstance(value, dict):
        eng = value.get("eng")
        chosen = eng if eng is not None else next(iter(value.values()), None)
        return _pick(chosen)
    if isinstance(value, list):
        return _pick(value[0]) if value else ""
    return str(value) if value is not None else ""


def _number(value: object) -> float | None:
    text = _pick(value).replace(",", "").strip()
    try:
        return float(text)
    except ValueError:
        return None


def _value(notice: dict) -> tuple[float | None, str]:
    """(value, currency): awarded tender > lot result > lot estimate."""
    for amount_key, cur_key in (
        ("tender-value", "tender-value-cur"),
        ("result-value-lot", "result-value-cur-lot"),
        ("estimated-value-lot", "estimated-value-cur-lot"),
    ):
        amount = _number(notice.get(amount_key))
        if amount is not None:
            return amount, _pick(notice.get(cur_key)).upper()
    return None, ""


def _duration_months(notice: dict) -> float | None:
    value = _number(notice.get("duration-period-value-lot"))
    unit = _pick(notice.get("duration-period-unit-lot")).lower()
    if value is None or unit not in _UNIT_MONTHS:
        return None
    return round(value * _UNIT_MONTHS[unit], 1)


def _procedure(notice: dict) -> str:
    code = _pick(notice.get("procedure-type")).lower()
    return _TED_PROCEDURE.get(code, "unknown")


def _date(value: object) -> str:
    return _pick(value)[:10]


def _notice_row(notice: dict, row: QueryRow) -> AwardRow:
    number = _pick(notice.get("publication-number"))
    value, currency = _value(notice)
    return AwardRow(
        award_id=f"{SOURCE}:{number}",
        source=SOURCE,
        region=row.region,
        category_hint=row.category,
        query=row.query,
        buyer=_pick(notice.get("organisation-name-buyer")),
        title=_pick(notice.get("notice-title")),
        text=_pick(notice.get("description-lot")),
        value=value,
        currency=currency,
        start_date=_date(notice.get("contract-duration-start-date-lot")),
        end_date=_date(notice.get("contract-duration-end-date-lot")),
        duration_months=_duration_months(notice),
        procedure=_procedure(notice),
        cpv_or_psc=";".join(
            str(c) for c in (notice.get("classification-cpv") or [])
        ),
        url=f"{_DETAIL}{number}" if number else "",
    )


def collect(
    rows: list[QueryRow],
    client: httpx.Client,
    *,
    per_query: int | None,
    log: Callable[[str], None] | None = print,
) -> Iterator[AwardRow]:
    """Notice rows for the EU queries; a short page marks the last page."""
    log = log or (lambda _m: None)
    rows = [r for r in rows if r.region in REGIONS]
    if not rows:
        return
    if not robots.allowed(_URL, client):
        log(f"{SOURCE}: robots.txt disallows {_URL}, skipped")
        return
    for row in rows:
        kept = 0
        page = 1
        try:
            while True:
                body = {
                    "query": (
                        f"FT={phrase}"
                        if (phrase := quoted(row.query)) is not None
                        else "publication-date >= 20000101"
                    ),
                    "fields": _FIELDS,
                    "limit": _PAGE,
                    "page": page,
                }
                response = http.post_with_backoff(client, _URL, json=body)
                response.raise_for_status()
                notices = response.json().get("notices") or []
                for notice in notices:
                    if per_query is not None and kept >= per_query:
                        break
                    if not _pick(notice.get("publication-number")):
                        continue
                    yield _notice_row(notice, row)
                    kept += 1
                if len(notices) < _PAGE or (
                    per_query is not None and kept >= per_query
                ):
                    break
                page += 1
        except Exception as exc:  # noqa: BLE001 - one bad query never stops a run
            log(f"{SOURCE} {row.region} {row.query!r}: {exc}")
