"""Backoff and politeness behaviour of the shared client."""

import httpx
import pytest

from lsa.sources import http


def _client(handler):
    return http.make_client(transport=httpx.MockTransport(handler))


def test_user_agent_and_timeout():
    client = http.make_client()
    assert client.headers["user-agent"] == http.USER_AGENT
    assert client.timeout.read == http.TIMEOUT_S == 30.0


def test_retries_429_then_success():
    calls = []

    def handler(request):
        calls.append(request.url.path)
        if len(calls) == 1:
            return httpx.Response(429)
        return httpx.Response(200, text="ok")

    slept = []
    response = http.get_with_backoff(
        _client(handler),
        "https://api.test/path",
        sleep=slept.append,
    )
    assert response.status_code == 200
    assert calls == ["/path", "/path"]
    assert slept, "a 429 must wait before retrying"


def test_honours_retry_after():
    calls = []

    def handler(request):
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429, headers={"Retry-After": "7"})
        return httpx.Response(200)

    slept = []
    http.get_with_backoff(
        _client(handler), "https://api.test/x", sleep=slept.append
    )
    assert max(slept) >= 7.0


def test_retries_5xx_then_success():
    responses = iter([httpx.Response(503), httpx.Response(200, text="ok")])

    def handler(request):
        return next(responses)

    response = http.get_with_backoff(
        _client(handler), "https://api.test/y", sleep=lambda _s: None
    )
    assert response.status_code == 200


def test_gives_up_after_max_tries():
    def handler(request):
        return httpx.Response(500)

    response = http.get_with_backoff(
        _client(handler),
        "https://api.test/z",
        max_tries=3,
        sleep=lambda _s: None,
    )
    assert response.status_code == 500


def test_per_host_spacing():
    """Second call to the same host waits out the min interval."""
    now = [1000.0]
    slept = []

    def handler(request):
        return httpx.Response(200)

    client = _client(handler)
    http.get_with_backoff(
        client, "https://a.test/1", sleep=slept.append, now=lambda: now[0]
    )
    now[0] += 0.5
    http.get_with_backoff(
        client, "https://a.test/2", sleep=slept.append, now=lambda: now[0]
    )
    assert slept[-1] == pytest.approx(http.MIN_INTERVAL_S - 0.5)


def test_transport_error_retries_then_raises():
    calls = []

    def handler(request):
        calls.append(1)
        raise httpx.ConnectError("down")

    with pytest.raises(httpx.ConnectError):
        http.get_with_backoff(
            _client(handler),
            "https://down.test/",
            max_tries=2,
            sleep=lambda _s: None,
        )
    assert len(calls) == 2
