"""EURES job counts (EU jobs).

POSTs a keyword search to the portal's public jv-search endpoint and reads
``numberRecords``. The body mirrors the portal's own front end: one keyword
with ``specificSearchCode`` EVERYWHERE and every filter list empty.

The endpoint is undocumented by the Commission; the body shape follows the
reverse-engineered OpenAPI spec (rorar/EURES-API-Documentation) and the live
call recorded in sources.csv.
"""

from __future__ import annotations

import httpx

from lsa.sources import http

SOURCE = "eures"
FAMILY = "jobs"
REGIONS = ("EU",)

_URL = "https://europa.eu/eures/api/jv-searchengine/public/jv-search/search"


def _body(query: str) -> dict:
    return {
        "resultsPerPage": 1,
        "page": 1,
        "sortSearch": "BEST_MATCH",
        "keywords": [
            {"keyword": query, "specificSearchCode": "EVERYWHERE"}
        ],
        "publicationPeriod": None,
        "occupationUris": [],
        "skillUris": [],
        "requiredExperienceCodes": [],
        "positionScheduleCodes": [],
        "sectorCodes": [],
        "educationAndQualificationLevelCodes": [],
        "positionOfferingCodes": [],
        "locationCodes": [],
        "euresFlagCodes": [],
        "otherBenefitsCodes": [],
        "requiredLanguages": [],
        "minNumberPost": None,
        "sessionId": None,
        "userPreferredLanguage": None,
        "requestLanguage": "en",
    }


def count(query: str, region: str, client: httpx.Client) -> int | None:
    response = http.post_with_backoff(client, _URL, json=_body(query))
    response.raise_for_status()
    total = response.json().get("numberRecords")
    return int(total) if isinstance(total, int | float) else None
