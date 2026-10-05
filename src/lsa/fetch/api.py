"""Driver for the API families (procurement, jobs).

Each counted row already names its source module; ``fetch`` maps
``row.source`` back to the module through ``count.api_sources`` and streams
``mod.search(row.query, row.region, client)``. Guard-rejected, dropped and
match-all rows never arrive here: ``plan_rows`` applies the shared
``common.fetchable`` rule. A source that raises is logged and skipped, the
same skip-never-crashes discipline ``count.run_api_counts`` uses.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from types import ModuleType

import httpx

from lsa import count as cnt
from lsa.contracts import CountRecord
from lsa.fetch import common


def plan_rows(rows: list[CountRecord]) -> list[CountRecord]:
    return common.plan_rows(rows)


def fetch(
    family: str,
    rows: list[CountRecord],
    client: httpx.Client,
    *,
    log: Callable[[str], None] | None = print,
    **_unused,
) -> Iterator[common.Produced]:
    """Yield Produced items by paging each row's own source module."""
    log = log or (lambda _m: None)
    modules: dict[str, ModuleType] = {
        mod.SOURCE: mod for mod in cnt.api_sources(family)
    }
    for row in rows:
        mod = modules.get(row.source)
        if mod is None or not hasattr(mod, "search"):
            log(f"fetch {family}: no searcher for source {row.source}")
            continue
        try:
            for item in mod.search(row.query, row.region, client):
                yield common.Produced(
                    item, row.source, row.region, row.category, row.query
                )
        except Exception as exc:  # noqa: BLE001 - one bad row never stops a run
            log(f"fetch {row.source} {row.region} {row.query!r}: {exc}")
