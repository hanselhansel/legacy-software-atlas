"""Fetchers (plan 2, task 1): turn counted query rows into items.

One module per count family. A module exposes ``plan_rows(rows)`` (the
counted rows worth paging) and ``fetch(rows, args, client, log)`` (a
generator of ``common.Produced``). The shared plumbing in ``common`` reads
counts.parquet, dedupes items, cuts the text window each pass needs
(``configs/passes.toml``), writes ``data/raw/<family>/<id>.json`` and
upserts ``data/derived/items.parquet``.
"""

from __future__ import annotations

from types import ModuleType

_FETCHERS: dict[str, ModuleType] = {}


def fetchers() -> dict[str, ModuleType]:
    """family -> fetch module, lazily imported like ``count.api_sources``."""
    if not _FETCHERS:
        from lsa.fetch import (
            hn,
            integrator,
            jobs,
            jobs_pages,
            procurement,
            vendor,
        )

        _FETCHERS.update(
            {
                "procurement": procurement,
                "jobs": jobs,
                "jobs-pages": jobs_pages,
                "vendor": vendor,
                "integrator": integrator,
                "hn": hn,
            }
        )
    return _FETCHERS
