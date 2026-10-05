"""Shared httpx client and polite fetch helper (plan 1, task 3).

``make_client`` builds the one client every collector uses, stamped with the
study's research User-Agent and a 30 s timeout. ``get_with_backoff`` enforces
two courtesies on top of ``client.get``:

- at least ``MIN_INTERVAL_S`` seconds between requests to the same host, so a
  count run never hammers a site, and
- retries on 429 and 5xx (and transport errors) up to ``MAX_TRIES``, honouring
  the server's ``Retry-After`` hint when it sends one.

The per-host clock lives at module level so politeness holds across every
client a run creates. ``sleep`` and ``now`` are injectable so tests never wait.
"""

from __future__ import annotations

import time
from collections.abc import Callable
from email.utils import parsedate_to_datetime

import httpx

USER_AGENT = (
    "legacy-software-atlas research "
    "(github.com/hanselhansel/legacy-software-atlas)"
)
TIMEOUT_S = 30.0
MIN_INTERVAL_S = 2.0
MAX_TRIES = 5
BASE_BACKOFF_S = 2.0

_LAST_AT: dict[str, float] = {}


def make_client(**kwargs) -> httpx.Client:
    """httpx.Client with the research User-Agent and a 30 s timeout."""
    headers = {"User-Agent": USER_AGENT}
    headers.update(kwargs.pop("headers", {}) or {})
    return httpx.Client(
        headers=headers,
        timeout=TIMEOUT_S,
        follow_redirects=True,
        **kwargs,
    )


def _retry_after_seconds(response: httpx.Response, now: float) -> float | None:
    """``Retry-After`` as seconds, or None when absent or unparsable."""
    header = response.headers.get("retry-after")
    if not header:
        return None
    header = header.strip()
    if header.isdigit():
        return float(header)
    try:
        at = parsedate_to_datetime(header).timestamp()
    except (TypeError, ValueError):
        return None
    return max(0.0, at - now)


def get_with_backoff(
    client: httpx.Client,
    url: str,
    *,
    max_tries: int = MAX_TRIES,
    sleep: Callable[[float], None] = time.sleep,
    now: Callable[[], float] = time.monotonic,
) -> httpx.Response:
    """GET ``url`` with per-host spacing and 429/5xx retries.

    Waits so consecutive calls to one host are at least ``MIN_INTERVAL_S``
    apart. Retries on 429, 5xx and ``httpx.TransportError``; on 429 it waits
    at least the server's ``Retry-After`` hint. Returns the final response
    when retries run out on status errors (callers check ``status_code``);
    re-raises the last transport error when every try failed to connect.
    """
    host = httpx.URL(url).host or ""
    last_error: httpx.TransportError | None = None
    for attempt in range(max_tries):
        gap = MIN_INTERVAL_S - (now() - _LAST_AT.get(host, 0.0))
        if gap > 0:
            sleep(gap)
        try:
            response = client.get(url)
        except httpx.TransportError as exc:
            last_error = exc
            if attempt == max_tries - 1:
                raise
            sleep(BASE_BACKOFF_S * (attempt + 1))
            continue
        finally:
            _LAST_AT[host] = now()
        if response.status_code == 429 or response.status_code >= 500:
            if attempt == max_tries - 1:
                return response
            hint = _retry_after_seconds(response, now()) or 0.0
            sleep(max(hint, BASE_BACKOFF_S * (attempt + 1)))
            continue
        return response
    # Unreachable: the loop always returns or raises. Satisfies the type
    # checker.
    raise last_error or httpx.TransportError("get_with_backoff exhausted")
