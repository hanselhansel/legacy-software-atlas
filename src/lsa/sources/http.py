"""Shared HTTP plumbing for keyless API counting collectors (plan 1, task 3).

Every collector goes through ``make_client`` (descriptive user agent, 30 s
timeout) and ``get_with_backoff`` / ``post_with_backoff``. The wrappers pace
calls to at most one per second per host and retry 429/5xx with exponential
backoff (at most ``MAX_TRIES`` attempts, honouring ``Retry-After``). A status
that stays retryable after the last try raises ``HTTPStatusError``; other
statuses (including other 4xx) come back to the caller.
"""

from __future__ import annotations

import time
from email.utils import parsedate_to_datetime

import httpx

USER_AGENT = (
    "legacy-software-atlas research "
    "(github.com/hanselhansel/legacy-software-atlas)"
)
TIMEOUT = 30.0
MAX_TRIES = 5
MIN_HOST_INTERVAL = 1.0
BACKOFF_MAX = 30.0

_last_call: dict[str, float] = {}


def make_client() -> httpx.Client:
    """Client for live API calls: declared UA, 30 s timeout, redirects on."""
    return httpx.Client(
        timeout=TIMEOUT,
        headers={"User-Agent": USER_AGENT},
        follow_redirects=True,
    )


def _sleep(seconds: float) -> None:
    if seconds > 0:
        time.sleep(seconds)


def _retry_after(response: httpx.Response) -> float | None:
    header = response.headers.get("retry-after")
    if header is None:
        return None
    try:
        return max(float(header), 0.0)
    except ValueError:
        pass
    try:
        return max(parsedate_to_datetime(header).timestamp() - time.time(), 0.0)
    except (TypeError, ValueError):
        return None


def _pace(url: str) -> None:
    """Sleep so calls to one host stay at least ``MIN_HOST_INTERVAL`` apart."""
    host = httpx.URL(url).host or ""
    last = _last_call.get(host)
    if last is not None:
        _sleep(MIN_HOST_INTERVAL - (time.monotonic() - last))
    _last_call[host] = time.monotonic()


def _with_backoff(
    client: httpx.Client, method: str, url: str, **kwargs
) -> httpx.Response:
    for attempt in range(MAX_TRIES):
        _pace(url)
        response = client.request(method, url, **kwargs)
        retryable = response.status_code == 429 or response.status_code >= 500
        if not retryable:
            return response
        if attempt == MAX_TRIES - 1:
            response.raise_for_status()
        _sleep(_retry_after(response) or min(2.0**attempt, BACKOFF_MAX))
    raise AssertionError("unreachable")


def get_with_backoff(
    client: httpx.Client, url: str, **kwargs
) -> httpx.Response:
    return _with_backoff(client, "GET", url, **kwargs)


def post_with_backoff(
    client: httpx.Client, url: str, **kwargs
) -> httpx.Response:
    return _with_backoff(client, "POST", url, **kwargs)
