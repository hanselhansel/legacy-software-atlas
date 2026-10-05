"""Tests for the UK OCDS award collector (plan 3, lane L)."""

from __future__ import annotations

import httpx

from lsa.awards import uk
from lsa.awards.common import QueryRow

_FTS = uk.FTS_URL
_CF = uk.CF_URL


def _release(**over):
    release = {
        "ocid": "ocds-b5fd17-aaaa-0001",
        "id": "bbbc7f12-af73-414b-9ae2-793ef227aa11-914730",
        "tag": ["award"],
        "buyer": {"name": "Department for Work and Pensions"},
        "tender": {
            "id": "CF-0036100DQH00000FUqLV2A1",
            "title": "Core banking platform support",
            "description": "Maintenance and extension of the core banking estate.",
            "procurementMethod": "selective",
            "procurementMethodDetails": "Call-off from a framework agreement",
            "value": {"amount": 2565054, "currency": "GBP"},
            "contractPeriod": {
                "startDate": "2026-08-20T00:00:00+01:00",
                "endDate": "2028-08-19T23:59:59+01:00",
            },
            "classification": {"scheme": "CPV", "id": "72000000"},
        },
        "awards": [
            {
                "id": "a1",
                "value": {"amount": 2565054, "currency": "GBP"},
                "contractPeriod": {
                    "startDate": "2026-08-20T00:00:00+01:00",
                    "endDate": "2028-08-19T23:59:59+01:00",
                },
                "documents": [
                    {
                        "url": "https://www.contractsfinder.service.gov.uk/Notice/bbbc7f12-af73-414b-9ae2-793ef227aa11"
                    }
                ],
            }
        ],
    }
    release.update(over)
    return release


def _handler(pages_by_host):
    """pages_by_host: host -> list of pages, each a list of releases.
    The `cursor` param picks the page index (`c0`, `c1`, ...)."""
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        seen.append(str(request.url))
        pages = pages_by_host.get(request.url.host, [[]])
        cursor = request.url.params.get("cursor") or "c0"
        idx = min(int(cursor[1:]), len(pages) - 1)
        links = {}
        if idx + 1 < len(pages):
            links["next"] = str(
                request.url.copy_merge_params({"cursor": f"c{idx + 1}"})
            )
        return httpx.Response(
            200, json={"releases": pages[idx], "links": links}
        )

    return handler, seen


def test_collect_maps_uk_ocds_release(mock_client, no_sleep):
    handler, seen = _handler({httpx.URL(_CF).host: [[_release()]]})
    rows = list(
        uk.collect(
            [QueryRow("core-banking", "UK", "core banking")],
            mock_client(handler),
            per_query=10,
            log=None,
        )
    )
    row = next(r for r in rows if r.source == "contracts-finder")
    assert row.award_id == "contracts-finder:ocds-b5fd17-aaaa-0001"
    assert row.buyer == "Department for Work and Pensions"
    assert row.title == "Core banking platform support"
    assert "core banking estate" in row.text
    assert row.value == 2565054
    assert row.currency == "GBP"
    assert row.start_date == "2026-08-20"
    assert row.end_date == "2028-08-19"
    assert row.procedure == "restricted"
    assert row.cpv_or_psc == "72000000"
    assert row.url == (
        "https://www.contractsfinder.service.gov.uk/Notice/"
        "bbbc7f12-af73-414b-9ae2-793ef227aa11"
    )


def test_collect_fetches_both_endpoints(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        calls.append(request.url.host)
        return httpx.Response(200, json={"releases": []})

    client = mock_client(handler)
    list(
        uk.collect(
            [QueryRow("core-banking", "UK", "core banking")],
            client,
            per_query=None,
            log=None,
        )
    )
    assert httpx.URL(_CF).host in calls
    assert httpx.URL(_FTS).host in calls


def test_collect_filters_locally_by_keyword(mock_client, no_sleep):
    match = _release()
    other = _release(
        **{
            "ocid": "ocds-b5fd17-bbbb-0002",
            "tender": {"title": "School dinners", "description": "Catering."},
        }
    )
    handler, _ = _handler({httpx.URL(_CF).host: [[match, other]], httpx.URL(_FTS).host: [[other]]})
    rows = list(
        uk.collect(
            [QueryRow("core-banking", "UK", "core banking")],
            mock_client(handler),
            per_query=None,
            log=None,
        )
    )
    sources = {r.source for r in rows}
    assert sources == {"contracts-finder"}
    assert rows[0].award_id == "contracts-finder:ocds-b5fd17-aaaa-0001"


def test_collect_follows_cursor_pages(mock_client, no_sleep):
    handler, _ = _handler({httpx.URL(_CF).host: [[_release()], [_release()]], httpx.URL(_FTS).host: [[]]})
    rows = list(
        uk.collect(
            [QueryRow("core-banking", "UK", "core banking")],
            mock_client(handler),
            per_query=None,
            log=None,
        )
    )
    # Same release on two pages dedupes to one row (same award_id).
    assert len(rows) == 1


def test_collect_per_query_caps_matches(mock_client, no_sleep):
    releases = [_release(**{"ocid": f"ocds-{i}"}) for i in range(5)]
    handler, _ = _handler({httpx.URL(_CF).host: [releases], httpx.URL(_FTS).host: [[]]})
    rows = list(
        uk.collect(
            [QueryRow("core-banking", "UK", "core banking")],
            mock_client(handler),
            per_query=2,
            log=None,
        )
    )
    assert len(rows) == 2


def test_collect_window_params(mock_client, no_sleep):
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(404)
        seen.append(request.url)
        return httpx.Response(200, json={"releases": []})

    client = mock_client(handler)
    list(
        uk.collect(
            [QueryRow("core-banking", "UK", "x")],
            client,
            per_query=None,
            log=None,
        )
    )
    cf = [u for u in seen if u.host == httpx.URL(_CF).host][0]
    assert cf.params.get("stages") == "award"
    assert cf.params.get("publishedFrom")
    fts = [u for u in seen if u.host == httpx.URL(_FTS).host][0]
    assert fts.params.get("updatedFrom")
