"""procurement fetcher: pages the four procurement API counters."""

from __future__ import annotations

from lsa.fetch import api

FAMILY = "procurement"

plan_rows = api.plan_rows


def fetch(rows, client, **kwargs):
    yield from api.fetch(FAMILY, rows, client, **kwargs)
