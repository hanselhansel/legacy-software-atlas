"""HN snapshot counting collector (plan 1, task 3, lane C).

Counts comments in the HN study's local parquet snapshot whose normalized text
mentions a category's search terms, and measures a token-per-comment proxy for
the Jev estimator. The snapshot is read-only and duckdb does all scanning; the
file is never loaded into pandas, and comment text and authors never leave the
query engine.
"""

from __future__ import annotations

import os
import re
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path

from lsa.contracts import CountRecord

DEFAULT_SNAPSHOT = (
    "~/conductor/repos/jev-opportunity-atlas/data/snapshots/"
    "hn-2025-09-28_2026-09-28-v1/comments.parquet"
)
ENV_SNAPSHOT = "LSA_HN_SNAPSHOT"

SOURCE = "hn-snapshot"
FAMILY = "hn"
REGION = "US"
METHOD = "local snapshot regex"
WORDS_TO_TOKENS = 1.33

_ELIGIBLE = "eligible AND in_window"


def snapshot_path() -> Path:
    """Snapshot parquet path from ``LSA_HN_SNAPSHOT``, else the HN study's."""
    return Path(os.environ.get(ENV_SNAPSHOT, DEFAULT_SNAPSHOT)).expanduser()


def _pattern(terms: Iterable[str]) -> str:
    """Case-insensitive regex matching any term on ASCII word boundaries.

    ``(^|[^\\w])...([^\\w]|$)`` is used instead of ``\\b`` so terms that start
    or end on a non-word character (``as/400``, ``.net``) still match at text
    edges while substrings inside longer words (``sap`` in ``sapling``) do not.
    """
    alts = "|".join(re.escape(t) for t in dict.fromkeys(terms) if t.strip())
    if not alts:
        raise ValueError("no search terms to match")
    return rf"(?i)(^|[^a-z0-9_])({alts})([^a-z0-9_]|$)"


def _comments_sql(snapshot: Path) -> str:
    """``read_parquet('<path>')`` with the path escaped as a SQL literal."""
    escaped = str(Path(snapshot)).replace("'", "''")
    return f"read_parquet('{escaped}')"


def _record(category: str, query: str, count: int, counted_at: str) -> CountRecord:
    return CountRecord(
        source=SOURCE,
        family=FAMILY,
        region=REGION,
        category=category,
        system="",
        query=query,
        count=count,
        method=METHOD,
        counted_at=counted_at,
    )


def count_terms(
    snapshot: Path, terms: list[tuple[str, str]]
) -> list[CountRecord]:
    """One CountRecord per category plus a trailing ``_any`` record.

    ``terms`` is a list of ``(category, term)`` pairs; region is ignored
    because HN uses every term regardless of region. Each record's ``query``
    is the category's terms joined by ``" | "`` and ``count`` is the number of
    distinct eligible, in-window comments matching any of them.
    """
    by_category: dict[str, list[str]] = {}
    for category, term in terms:
        cat_terms = by_category.setdefault(category, [])
        if term not in cat_terms:
            cat_terms.append(term)
    if not by_category:
        raise ValueError("no search terms to count")

    import duckdb

    counted_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    comments = _comments_sql(snapshot)
    con = duckdb.connect()
    try:

        def n_matching(pattern: str) -> int:
            row = con.execute(
                f"SELECT COUNT(DISTINCT id) FROM {comments} "
                f"WHERE {_ELIGIBLE} AND regexp_matches(text_norm, ?)",
                [pattern],
            ).fetchone()
            return int(row[0])

        records = [
            _record(
                category,
                " | ".join(cat_terms),
                n_matching(_pattern(cat_terms)),
                counted_at,
            )
            for category, cat_terms in by_category.items()
        ]
        all_terms = [t for ts in by_category.values() for t in ts]
        records.append(
            _record(
                "_any",
                " | ".join(dict.fromkeys(all_terms)),
                n_matching(_pattern(all_terms)),
                counted_at,
            )
        )
    finally:
        con.close()
    return records


def sample_token_lengths(
    snapshot: Path,
    terms: list[tuple[str, str]],
    n: int = 50,
    seed: int = 0,
) -> float:
    """Mean ``word_count * 1.33`` over a seeded sample of matching comments.

    The seeded order comes from ``md5(id || ':' || seed)`` so the sample is
    reproducible. Returns 0.0 when nothing matches.
    """
    import duckdb

    all_terms = [t for _, t in terms]
    comments = _comments_sql(snapshot)
    con = duckdb.connect()
    try:
        row = con.execute(
            "SELECT AVG(word_count * ?) FROM ("
            f"  SELECT word_count FROM {comments} "
            f"  WHERE {_ELIGIBLE} AND regexp_matches(text_norm, ?) "
            "  ORDER BY md5(id::VARCHAR || ':' || ?) LIMIT ?"
            ")",
            [WORDS_TO_TOKENS, _pattern(all_terms), str(seed), n],
        ).fetchone()
    finally:
        con.close()
    return float(row[0] or 0.0)
