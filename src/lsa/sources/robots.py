"""robots.txt checks, fetched once per host and cached (plan 1, task 3).

Every page collector calls ``allowed`` before fetching a page. The rules map
is kept per origin so a count run fetches ``/robots.txt`` at most once per
host. The check uses our real User-Agent, so named bot groups only apply
when they name us; ``User-agent: *`` is the usual match.

Fetch outcomes follow RFC 930: a missing or 4xx robots file means no rules
(allow all); 5xx, 429 or an unreachable host means assume disallow, the
conservative reading.
"""

from __future__ import annotations

import urllib.robotparser
from dataclasses import dataclass

import httpx

from lsa.sources import http

_robots_txt = urllib.robotparser.RobotFileParser
_CACHE: dict[str, _Rules] = {}


@dataclass
class _Rules:
    """Parsed robots rules, or a fixed verdict when no file was usable."""

    parser: urllib.robotparser.RobotFileParser | None
    allow_all: bool = False
    deny_all: bool = False

    def can_fetch(self, url: str) -> bool:
        if self.allow_all:
            return True
        if self.deny_all or self.parser is None:
            return False
        return self.parser.can_fetch(http.USER_AGENT, url)

    def sitemaps(self) -> list[str]:
        if self.parser is None:
            return []
        return self.parser.site_maps() or []


def _origin(url: str) -> str:
    parsed = httpx.URL(url)
    return f"{parsed.scheme}://{parsed.host}:{parsed.port or (443 if parsed.scheme == 'https' else 80)}"


def _rules(origin: str, client: httpx.Client, **kwargs) -> _Rules:
    robots_url = f"{origin}/robots.txt"
    try:
        response = http.get_with_backoff(client, robots_url, **kwargs)
    except httpx.TransportError:
        return _Rules(parser=None, deny_all=True)
    status = response.status_code
    if status == 429 or status >= 500:
        return _Rules(parser=None, deny_all=True)
    if status >= 400:
        return _Rules(parser=None, allow_all=True)
    parser = _robots_txt(robots_url)
    parser.parse(response.text.splitlines())
    return _Rules(parser=parser)


def rules_for(
    url: str,
    client: httpx.Client,
    *,
    get_kwargs: dict | None = None,
) -> _Rules:
    """Parsed robots rules for ``url``'s origin, fetched once per origin."""
    kwargs = get_kwargs or {}
    origin = _origin(url)
    rules = _CACHE.get(origin)
    if rules is None:
        rules = _rules(origin, client, **kwargs)
        _CACHE[origin] = rules
    return rules


def allowed(
    url: str,
    client: httpx.Client,
    *,
    get_kwargs: dict | None = None,
) -> bool:
    """True when robots.txt lets our User-Agent fetch ``url``.

    The first call for a host fetches ``/robots.txt``; later calls on the
    same host reuse the parsed rules without another request.
    """
    return rules_for(url, client, get_kwargs=get_kwargs).can_fetch(url)


def declared_sitemaps(origin: str) -> list[str]:
    """Sitemap URLs a host's robots.txt declared (empty before ``allowed``)."""
    rules = _CACHE.get(origin)
    return rules.sitemaps() if rules else []


def _reset_cache() -> None:
    """Drop cached rules. Tests use this to isolate per-host behaviour."""
    _CACHE.clear()
