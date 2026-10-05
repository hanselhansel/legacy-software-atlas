"""Free-text count and region parsing for the estimate lane (plan 2, task 5).

``approx_count`` and ``disclosed_customers`` cells mix counts with years,
currency amounts, asset sizes and prose. The extractors here apply the same
guards everywhere:

- numbers glued to a letter or ``$`` are skipped (``FY2025``, ``$510M``,
  ``EUR235M``);
- numbers followed by ``-X`` are skipped (form names like ``10-K``);
- a bare four-digit token in 1900..2099 is a year, never a count (the comma
  form ``2,000`` still counts);
- a number <= 31 directly before a month name is a day, not a count;
- a number right after a currency code or symbol is money, not a count.

``parse_sum_or_range`` is for buyer-universe cells: an explicit range
(``4,000 to 5,000``) gives (low, high); otherwise every surviving number is
summed and reported at face value. ``parse_first_count`` is for vendor cells:
the first surviving number is the disclosed count. Every guess the parsers
make is returned in the notes list so the category TOML can override it.
"""

from __future__ import annotations

import re

STUDY_REGIONS = frozenset(
    {"US", "EU", "UK", "SG", "IN", "ID", "VN", "MY", "TH", "PH", "AU"}
)
# Vendor cells naming only global scope land in this pseudo-region instead of
# inflating every study region with the same count.
GLOBAL = "global"
# "APAC" / "Asia" in free text covers these study regions (Australia included:
# APAC usage normally spans it).
APAC = frozenset({"SG", "IN", "ID", "VN", "MY", "TH", "PH", "AU"})
SEA = frozenset({"SG", "ID", "VN", "MY", "TH", "PH"})

_SCALE = {
    "k": 1e3,
    "thousand": 1e3,
    "m": 1e6,
    "million": 1e6,
    "b": 1e9,
    "bn": 1e9,
    "billion": 1e9,
}

_AMOUNT = re.compile(
    r"(?<![\w$/])(\d[\d,]*(?:\.\d+)?)\s*"
    r"(k|m|b|bn|thousand|million|billion)?(?![\w-])",
    re.IGNORECASE,
)
_CURRENCY_BEFORE = re.compile(
    r"(?:[$€£]|USD|EUR|GBP|AUD|NZD|SGD|MYR|IDR|INR|VND|THB|PHP|HKD|CAD|JPY|"
    r"A\$|US\$|CA\$|NZ\$)\s*$",
    re.IGNORECASE,
)
_DAY_BEFORE_MONTH = re.compile(
    r"^\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)\b",
    re.IGNORECASE,
)
_RANGE = re.compile(
    r"between\s+(\d[\d,]*(?:\.\d+)?)\s+and\s+(\d[\d,]*(?:\.\d+)?)|"
    r"(\d[\d,]*(?:\.\d+)?)\s*(?:to|through|until|-)\s*(\d[\d,]*(?:\.\d+)?)"
)
_FY_YEAR = re.compile(r"\bFY\s?(19\d\d|20\d\d)\b", re.IGNORECASE)
_DATE_YEAR = re.compile(
    r"(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)\w*\.?\s+"
    r"(19\d\d|20\d\d)\b|\((19\d\d|20\d\d)\)|\b(?:in|by|from|since|of)\s+"
    r"(19\d\d|20\d\d)\b",
    re.IGNORECASE,
)
_USD = re.compile(
    r"\$\s*(\d[\d,]*(?:\.\d+)?)\s*"
    r"(k|m|b|bn|thousand|million|billion)?\b",
    re.IGNORECASE,
)

_NO_COUNT = re.compile(
    r"^\W*(not|no|none|unknown|unverified|n/a|na|undisclosed|search)",
    re.IGNORECASE,
)

_MONTHS = {
    "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "sept",
    "oct", "nov", "dec",
}

# Country and macro-region aliases mapped onto the study regions. "canada" and
# "north america" resolve to US, "new zealand" and "anz" to AU: the nearest
# study region, documented as an approximation in the generated configs.
_ALIASES: dict[str, str] = {
    "united states": "US",
    "u.s.": "US",
    "usa": "US",
    "america": "US",
    "americas": "US",
    "north america": "US",
    "canada": "US",
    "europe": "EU",
    "eea": "EU",
    "dach": "EU",
    "nordics": "EU",
    "benelux": "EU",
    "cee": "EU",
    "western europe": "EU",
    "germany": "EU",
    "france": "EU",
    "netherlands": "EU",
    "spain": "EU",
    "italy": "EU",
    "ireland": "EU",
    "belgium": "EU",
    "luxembourg": "EU",
    "austria": "EU",
    "switzerland": "EU",
    "sweden": "EU",
    "denmark": "EU",
    "finland": "EU",
    "norway": "EU",
    "poland": "EU",
    "portugal": "EU",
    "greece": "EU",
    "united kingdom": "UK",
    "britain": "UK",
    "england": "UK",
    "scotland": "UK",
    "wales": "UK",
    "singapore": "SG",
    "india": "IN",
    "indonesia": "ID",
    "vietnam": "VN",
    "malaysia": "MY",
    "thailand": "TH",
    "philippines": "PH",
    "australia": "AU",
    "new zealand": "AU",
    "anz": "AU",
}
# EU member-state ISO codes seen in vendor cells; other country codes are
# outside the study and map to nothing.
_CODE_ALIASES: dict[str, str] = {
    **{r: r for r in STUDY_REGIONS},
    # EU member-state codes seen in region cells. "SE" (Sweden) and "IT"
    # (Italy) are left out on purpose: "SE" usually means "SE Asia" here and
    # "IT" means information technology.
    **dict.fromkeys(
        [
            "DE", "AT", "CH", "FR", "NL", "BE", "LU", "ES", "PL", "DK",
            "FI", "NO", "IE", "PT", "GR", "CZ", "SK", "HU", "RO", "BG",
            "HR", "SI", "EE", "LV", "LT", "CY", "MT",
        ],
        "EU",
    ),
    "NZ": "AU",
    "CA": "US",
    "MX": "US",
}
_GLOBAL_MARKERS = re.compile(
    r"\b(global|worldwide|international|all\s+11|all\s+study\s+regions|"
    r"\d+\+?\s*countries|multi-?region)\b",
    re.IGNORECASE,
)
_ISO_DATE = re.compile(
    r"\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}/\d{1,2}/\d{2,4}\b"
)
_NON_US_AMERICA = re.compile(
    r"\b(?:latin|south|central)\s+americas?\b", re.IGNORECASE
)
_APAC_MARKERS = re.compile(
    r"\b(apac|asia[\s-]?pacific|asia)\b", re.IGNORECASE
)
_SEA_MARKERS = re.compile(
    r"\b(sea|southeast\s+asia|se\s+asia|asean)\b", re.IGNORECASE
)


def _is_year(number: float, token: str) -> bool:
    """Bare four-digit 1900..2099 tokens are years; comma forms are counts."""
    return "," not in token and 1900 <= number <= 2099


def extract_amounts(text: str) -> list[tuple[float, str]]:
    """All guarded count tokens in ``text`` as ``(value, matched)`` pairs."""
    text = _ISO_DATE.sub(" ", text)
    out: list[tuple[float, str]] = []
    for m in _AMOUNT.finditer(text):
        token, suffix = m.group(1), (m.group(2) or "").lower()
        value = float(token.replace(",", ""))
        if _is_year(value, token):
            continue
        after = text[m.end():]
        if value <= 31 and _DAY_BEFORE_MONTH.match(after):
            continue
        before = text[: m.start()].rstrip()
        if _CURRENCY_BEFORE.search(before):
            continue
        value *= _SCALE.get(suffix, 1.0)
        out.append((value, m.group(0).strip()))
    return out


def _range_bounds(text: str) -> tuple[float, float] | None:
    m = _RANGE.search(text)
    if m is None:
        return None
    a_tok, b_tok = m.group(1) or m.group(3), m.group(2) or m.group(4)
    a, b = float(a_tok.replace(",", "")), float(b_tok.replace(",", ""))
    if _is_year(a, a_tok) or _is_year(b, b_tok):
        return None
    # "3-to-5-year" style fragments are not ranges; require scale or >= 100.
    if "," not in a_tok + b_tok and max(a, b) < 100:
        return None
    if a <= 0 or b < a:
        return None
    return a, b


def parse_sum_or_range(text: str) -> tuple[float | None, float | None, list[str]]:
    """``(low, high, notes)`` for a buyer-universe ``approx_count`` cell.

    An explicit range gives low/high; otherwise the surviving numbers are
    summed (the cells list one count per institution type). Unparseable cells
    return ``(None, None, notes)`` so the caller can skip and record them.
    """
    notes: list[str] = []
    text = (text or "").strip()
    if not text or _NO_COUNT.match(text):
        return None, None, [f"no count in {text!r}"[:80]]
    bounds = _range_bounds(text)
    if bounds is not None:
        notes.append(f"range {bounds[0]:g}-{bounds[1]:g}")
        return bounds[0], bounds[1], notes
    amounts = extract_amounts(text)
    if not amounts:
        return None, None, [f"no count in {text!r}"[:80]]
    total = sum(v for v, _ in amounts)
    notes.append("summed " + "+".join(f"{v:g}" for v, _ in amounts))
    return total, total, notes


def parse_first_count(text: str) -> tuple[float | None, list[str]]:
    """``(count, notes)`` for a ``disclosed_customers`` cell.

    The first surviving number is the headline count; later figures are
    usually subsets, valuations or transaction volumes and are listed in the
    notes for review rather than summed.
    """
    text = (text or "").strip()
    if not text or _NO_COUNT.match(text):
        return None, [f"no count in {text!r}"[:80]]
    amounts = extract_amounts(text)
    if not amounts:
        return None, [f"no count in {text!r}"[:80]]
    first, matched = amounts[0]
    notes = [f"count {first:g} from {matched!r}"]
    rest = [f"{v:g}" for v, _ in amounts[1:]]
    if rest:
        notes.append("other numbers ignored: " + ", ".join(rest))
    return first, notes


def parse_year(text: str) -> str | None:
    """Best-effort year tag for a disclosed count, e.g. ``FY2025`` or ``2023``."""
    m = _FY_YEAR.search(text or "")
    if m:
        return f"FY{m.group(1)}"
    m = _DATE_YEAR.search(text or "")
    if m:
        return next(g for g in m.groups() if g)
    return None


def parse_usd(text: str) -> float | None:
    """First ``$N`` amount (K/M/B or spelled out) in a funding cell, as USD.

    The first dollar figure is usually the disclosed total or headline round;
    later figures tend to be valuations or earlier rounds. Cells with no ``$``
    amount (EUR or GBP only, or undisclosed) return None so the caller notes
    them for a config override.
    """
    m = _USD.search(text or "")
    if not m:
        return None
    value = float(m.group(1).replace(",", ""))
    value *= _SCALE.get((m.group(2) or "").lower(), 1.0)
    return value


def resolve_regions(text: str) -> tuple[set[str], list[str]]:
    """Study regions named in a free-text cell, plus parse notes.

    Explicit region mentions win over macro markers: ``US, UK, global``
    resolves to {US, UK} and the global word adds nothing. Only global
    markers (``Global``, ``190+ countries``) give the ``global`` bucket.
    APAC markers expand to the APAC study regions, SEA to the SEA subset.
    """
    notes: list[str] = []
    found: set[str] = set()
    for token in re.findall(r"\b[A-Z]{2}\b", text or ""):
        mapped = _CODE_ALIASES.get(token)
        if mapped:
            found.add(mapped)
    low = _NON_US_AMERICA.sub(" ", (text or "").lower())
    for alias, region in _ALIASES.items():
        if re.search(r"\b" + re.escape(alias) + r"\b", low):
            found.add(region)
    if _SEA_MARKERS.search(low):
        found |= SEA
    # "SE Asia" must not also fire the broader APAC marker on "asia".
    if _APAC_MARKERS.search(_SEA_MARKERS.sub(" ", low)):
        found |= APAC
    if found:
        return found, notes
    if _GLOBAL_MARKERS.search(low):
        return {GLOBAL}, notes
    if (text or "").strip():
        notes.append(f"no study region in {text!r}"[:80])
    return found, notes


def norm_universe_region(text: str) -> str:
    """Region key for a ``buyer_universe.csv`` row.

    Cells use plain codes plus a few suffixed forms (``EU (EEA)``, ``EU/EEA``,
    ``US (local)``, ``Global (cross-check)``); they normalise to the study
    code or the ``global`` bucket.
    """
    head = re.split(r"[(/]", (text or "").strip(), maxsplit=1)[0].strip()
    upper = head.upper()
    if upper in STUDY_REGIONS:
        return upper
    if upper in ("EEA", "EURO AREA", "EUROZONE"):
        return "EU"
    if "GLOBAL" in upper:
        return GLOBAL
    regions, _ = resolve_regions(head)
    return next(iter(regions), upper or "unknown")
