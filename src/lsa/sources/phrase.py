"""Exact-phrase query shapers for the keyless API counters.

Counters send each count query as an exact phrase. ``quoted`` wraps the
query in double quotes for APIs whose search syntax treats ``"..."`` as a
phrase (USAspending, TED, Contracts Finder, MyCareersFuture, Kalibrr,
EURES). ``escaped`` additionally backslash-escapes the Lucene-style
specials an API parses even inside quotes (Bundesagentur Jobsuche splits
``/`` into OR terms inside quotes, so ``z/TPF`` must go out as
``"z\\/TPF"``). Both return ``None`` for empty input so the caller can map
an empty query to the source's match-all request for the sanity guard.
"""

from __future__ import annotations

_LUCENE_SPECIALS = frozenset('\\+-=&|><!(){}[]^"~*?:/')


def _clean(query: str) -> str:
    """The query with embedded double quotes removed, whitespace collapsed."""
    return " ".join(query.replace('"', " ").split())


def quoted(query: str) -> str | None:
    """The query wrapped in double quotes as an exact phrase, else None."""
    text = _clean(query)
    return f'"{text}"' if text else None


def escaped(query: str) -> str | None:
    """Quoted phrase with Lucene specials backslash-escaped, else None."""
    text = _clean(query)
    if not text:
        return None
    body = "".join(f"\\{c}" if c in _LUCENE_SPECIALS else c for c in text)
    return f'"{body}"'
