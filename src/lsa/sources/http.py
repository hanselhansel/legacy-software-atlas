"""Shared httpx client and polite fetch helpers (plan 1, task 3).

``make_client`` builds the one client every collector uses, stamped with the
study's research User-Agent and a 30 s timeout. ``get_with_backoff`` and
``post_with_backoff`` wrap ``client.request`` with two courtesies:

- at least ``MIN_INTERVAL_S`` seconds between requests to the same host, so a
  count run never hammers a site, and
- retries on 429 and 5xx (and transport errors) up to ``MAX_TRIES``, honouring
  the server's ``Retry-After`` hint when it sends one (capped at
  ``RETRY_AFTER_MAX`` seconds).

A retryable status that persists through the last try is returned to the
caller, who decides whether to ``raise_for_status`` (API collectors do) or
record the status (page collectors and the robots gate do). A transport
error on the last try re-raises. The per-host clock lives at module level so
politeness holds across every client a run creates; ``sleep`` and ``now``
are injectable so tests never wait.
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
MIN_INTERVAL_S = 1.0
MAX_TRIES = 5
BACKOFF_MAX = 30.0
RETRY_AFTER_MAX = 120.0

# Per-host clock for the last request start. ``_LAST_AT`` is an alias of the
# same dict: tests/conftest.py clears the clock under that name while
# tests/sources/conftest.py uses ``_last_call``.
_last_call: dict[str, float] = {}
_LAST_AT = _last_call


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


def _sleep(seconds: float) -> None:
    if seconds > 0:
        time.sleep(seconds)


def _retry_after(response: httpx.Response, now: float) -> float | None:
    """``Retry-After`` as seconds, or None when absent or unparsable."""
    header = response.headers.get("retry-after")
    if header is None:
        return None
    header = header.strip()
    try:
        return max(float(header), 0.0)
    except ValueError:
        pass
    try:
        return max(parsedate_to_datetime(header).timestamp() - now, 0.0)
    except (TypeError, ValueError):
        return None


def _wait(response: httpx.Response, attempt: int, now: float) -> float:
    """Seconds to wait before a retry: Retry-After or exponential, capped."""
    wait = _retry_after(response, now)
    if wait is None:
        wait = min(2.0**attempt, BACKOFF_MAX)
    return min(wait, RETRY_AFTER_MAX)


def _with_backoff(
    client: httpx.Client,
    method: str,
    url: str,
    min_interval: float,
    max_tries: int,
    sleep: Callable[[float], None],
    now: Callable[[], float],
    **kwargs,
) -> httpx.Response:
    host = httpx.URL(url).host or ""
    for attempt in range(max_tries):
        last = _last_call.get(host)
        if last is not None:
            sleep(min_interval - (now() - last))
        _last_call[host] = now()
        try:
            response = client.request(method, url, **kwargs)
        except httpx.TransportError:
            if attempt == max_tries - 1:
                raise
            sleep(min(2.0**attempt, BACKOFF_MAX))
            continue
        retryable = response.status_code == 429 or response.status_code >= 500
        if not retryable or attempt == max_tries - 1:
            return response
        sleep(_wait(response, attempt, now()))
    raise AssertionError("unreachable")


def get_with_backoff(
    client: httpx.Client,
    url: str,
    *,
    min_interval: float = MIN_INTERVAL_S,
    max_tries: int = MAX_TRIES,
    sleep: Callable[[float], None] | None = None,
    now: Callable[[], float] | None = None,
    **kwargs,
) -> httpx.Response:
    """GET ``url`` with per-host spacing and 429/5xx/transport retries."""
    return _with_backoff(
        client,
        "GET",
        url,
        min_interval,
        max_tries,
        sleep or _sleep,
        now or time.monotonic,
        **kwargs,
    )


def post_with_backoff(
    client: httpx.Client,
    url: str,
    *,
    min_interval: float = MIN_INTERVAL_S,
    max_tries: int = MAX_TRIES,
    sleep: Callable[[float], None] | None = None,
    now: Callable[[], float] | None = None,
    **kwargs,
) -> httpx.Response:
    """POST ``url`` with per-host spacing and 429/5xx/transport retries."""
    return _with_backoff(
        client,
        "POST",
        url,
        min_interval,
        max_tries,
        sleep or _sleep,
        now or time.monotonic,
        **kwargs,
    )
