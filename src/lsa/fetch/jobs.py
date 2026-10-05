"""jobs fetcher: pages the four job API counters."""

from __future__ import annotations

from lsa.fetch import api

FAMILY = "jobs"

plan_rows = api.plan_rows


def fetch(rows, client, **kwargs):
    yield from api.fetch(FAMILY, rows, client, **kwargs)
