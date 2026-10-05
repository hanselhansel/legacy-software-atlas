"""BLS OEWS national employment and wages (plan 3, lane N).

The OEWS flat files (www.bls.gov special-requests zips and
download.bls.gov) answer 403 to scripted clients, so the public API v2
(no key) is the path: for 6-digit occupation code ``occ`` the series
are ``OEUN0000000000000<occ>01`` (national employment) and
``OEUN0000000000000<occ>04`` (annual mean wage), queried with
``latest`` so the newest May release answers (May 2025 at build time).

SOC codes with no OEWS series fall back to the broad group, then the
minor group, then the major group (``13-1021`` -> ``13-1020`` ->
``13-1000`` -> ``13-0000``); the code actually used is recorded per
occupation. Responses cache to ``data/raw/oews/api.json`` so re-runs
stay under the unregistered daily request cap.
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger(__name__)

API = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
EMPLOYMENT = "01"
ANNUAL_MEAN_WAGE = "04"
DATATYPES = (("employment", EMPLOYMENT), ("annual_mean_wage", ANNUAL_MEAN_WAGE))
LEVELS = ("exact", "broad", "minor", "major")
BATCH = 25
DEADLINE_S = 120.0


def soc6(code: str) -> str:
    """Six-digit occupation code: drop O*NET suffix and the dash."""
    return (code or "").strip()[:7].replace("-", "")


def candidates(code: str) -> list[str]:
    """OEWS fallback chain: exact, broad, minor, major group codes."""
    c = soc6(code)
    if len(c) != 6 or not c.isdigit():
        return []
    out = [c]
    for i in (5, 3, 2):
        cand = c[:i] + "0" * (6 - i)
        if cand not in out:
            out.append(cand)
    return out


def level_name(requested: str, used: str) -> str:
    """Name the fallback level a used code sits at vs the requested."""
    chain = candidates(requested)
    return LEVELS[chain.index(used)] if used in chain else "other"


def series_id(occ6: str, datatype: str) -> str:
    """OEWS national series: OE U N <area7> <industry6> <occ6> <dt2>."""
    return f"OEUN0000000000000{occ6}{datatype}"


def _latest_value(series: dict) -> float | None:
    data = series.get("data") or []
    if not data:
        return None
    try:
        return float(str(data[0].get("value", "")).replace(",", ""))
    except ValueError:
        return None


def fetch_values(
    series: list[str],
    client,
    cache_path: Path,
    *,
    refresh: bool = False,
    deadline_s: float = DEADLINE_S,
) -> dict[str, float | None]:
    """``{series_id: value|None}``, cache first, API for the rest."""
    from lsa.sources import http

    cache_path = Path(cache_path)
    have: dict[str, float | None] = {}
    if cache_path.exists() and not refresh:
        have = json.loads(cache_path.read_text(encoding="utf-8"))
    missing = [s for s in series if s not in have]
    t0 = time.monotonic()
    for i in range(0, len(missing), BATCH):
        if time.monotonic() - t0 > deadline_s:
            log.warning(
                "oews api deadline; %d series unqueried",
                len(missing) - i,
            )
            break
        chunk = missing[i : i + BATCH]
        try:
            resp = http.post_with_backoff(
                client, API, json={"seriesid": chunk, "latest": True}
            )
            body = resp.json()
        except Exception as exc:  # noqa: BLE001 - note and continue
            log.warning("oews api batch failed: %s", exc)
            body = {}
        got = {
            s["seriesID"]: _latest_value(s)
            for s in body.get("Results", {}).get("series", [])
            if "seriesID" in s
        }
        for s in chunk:
            have[s] = got.get(s)
    if missing:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(
            json.dumps(have, indent=1, sort_keys=True), encoding="utf-8"
        )
    return {s: have.get(s) for s in series}


@dataclass
class OewsRow:
    soc6_requested: str
    employment: float | None = None
    annual_mean_wage: float | None = None
    emp_soc: str | None = None
    wage_soc: str | None = None
    year: str | None = None


def wages_for(
    codes,
    client,
    cache_path: Path,
    *,
    refresh: bool = False,
    deadline_s: float = DEADLINE_S,
) -> dict[str, OewsRow]:
    """Resolve each SOC code to the nearest OEWS series with data.

    Queries are batched one fallback level at a time (all exact codes
    first) so occupations that resolve early never cost a request.
    """
    requested = {b for c in codes if (b := soc6(c))}
    chains = {b: candidates(b) for b in requested}
    rows = {b: OewsRow(b) for b in requested}
    pending = list(requested)
    for depth, level in enumerate(LEVELS):
        if not pending:
            break
        need = set()
        for b in pending:
            chain = chains[b]
            if depth < len(chain):
                for _, dt in DATATYPES:
                    need.add(series_id(chain[depth], dt))
        vals = fetch_values(
            sorted(need),
            client,
            cache_path,
            refresh=refresh,
            deadline_s=deadline_s,
        )
        still = []
        for b in pending:
            row = rows[b]
            cand = chains[b][depth] if depth < len(chains[b]) else None
            if cand is not None:
                for field, dt in DATATYPES:
                    v = vals.get(series_id(cand, dt))
                    if getattr(row, field) is None and v is not None:
                        setattr(row, field, v)
                        setattr(
                            row, "emp_soc" if field == "employment" else "wage_soc", cand
                        )
            if row.employment is None or row.annual_mean_wage is None:
                still.append(b)
        pending = still
    return rows
