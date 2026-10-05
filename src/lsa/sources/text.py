"""Visible-text extraction from HTML fragments (stdlib only).

Search APIs return descriptions with markup (``<p>maintain the
<b>core</b> ledger</p>``); Jev needs plain text. ``html_to_text`` drops
tags and script/style bodies and collapses whitespace. It is a fragment
stripper, not a browser: malformed input degrades to a best-effort text.
"""

from __future__ import annotations

import re
from html.parser import HTMLParser

_SKIP = frozenset({"script", "style", "head", "title", "noscript"})
_BREAK = frozenset(
    {"p", "br", "div", "li", "tr", "td", "section", "article", "h1", "h2", "h3"}
)
_WS = re.compile(r"\s+")


class _Visible(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in _SKIP:
            self._skip += 1
        elif tag in _BREAK:
            self.parts.append(" ")

    def handle_endtag(self, tag: str) -> None:
        if tag in _SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self.parts.append(data)


def html_to_text(html: str) -> str:
    """The fragment's visible text, whitespace-collapsed to one line."""
    parser = _Visible()
    parser.feed(html)
    return _WS.sub(" ", " ".join(parser.parts)).strip()
