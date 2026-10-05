"""Award collectors (plan 3, lane L): one module per award source.

Each module exposes ``SOURCES`` (the names it writes into ``award_id`` /
``source``), ``REGIONS`` (query regions it covers) and
``collect(rows, client, *, per_query, log)``, a lazy iterator of
``common.AwardRow`` for the query rows in its regions. ``collect.py`` is
the driver the CLI calls: it routes rows to modules, dedupes on
``award_id``, applies the per-query and total caps, and hands the kept
rows to ``common.write_awards`` / ``common.write_items``.
"""

from __future__ import annotations

from types import ModuleType

_MODULES: tuple[ModuleType, ...] | None = None


def collectors() -> tuple[ModuleType, ...]:
    """Award source modules, lazily imported like ``count.api_sources``."""
    global _MODULES
    if _MODULES is None:
        from lsa.awards import austender, gebiz, ted, uk, usaspending

        _MODULES = (usaspending, ted, uk, austender, gebiz)
    return _MODULES
