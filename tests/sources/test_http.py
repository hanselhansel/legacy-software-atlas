"""Backoff and politeness behaviour of the shared client (plan 1, task 3).

All transports are httpx.MockTransport; no test touches the network.
"""

from __future__ import annotations

import json

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


def _ok(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"ok": True})


def test_make_client_sets_user_agent_and_timeout():
    client = http.make_client()
    assert client.headers["user-agent"] == (
        "legacy-software-atlas research "
        "(github.com/hanselhansel/legacy-software-atlas)"
    )
    assert client.timeout.connect == 30.0


def test_get_with_backoff_returns_200(mock_client):
    client = mock_client(_ok)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_paces_calls_to_same_host(mock_client, no_sleep):
    client = mock_client(_ok)
    http.get_with_backoff(client, "https://a.example/x")
    http.get_with_backoff(client, "https://a.example/y")
    # Second call to a.example waits about a second.
    assert no_sleep and 0.5 < no_sleep[0] <= 1.0


def test_no_pace_across_different_hosts(mock_client, no_sleep):
    client = mock_client(_ok)
    http.get_with_backoff(client, "https://a.example/x")
    http.get_with_backoff(client, "https://b.example/x")
    assert no_sleep == []


def test_429_then_success_retries(mock_client, no_sleep):
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.url.path)
        if len(seen) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"ok": True})

    client = mock_client(handler)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert response.status_code == 200
    assert len(seen) == 2


def test_retry_after_header_is_honoured(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429, headers={"Retry-After": "7"})
        return httpx.Response(200, json={"ok": True})

    client = mock_client(handler)
    http.get_with_backoff(client, "https://a.example/x")
    assert 7.0 in no_sleep


def test_persistent_429_raises_after_max_tries(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(429)

    client = mock_client(handler)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert len(calls) == http.MAX_TRIES
    with pytest.raises(httpx.HTTPStatusError):
        response.raise_for_status()


def test_5xx_is_retried(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(503)

    client = mock_client(handler)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert len(calls) == http.MAX_TRIES
    assert response.status_code == 503


def test_5xx_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(503)
        return httpx.Response(200, json={"ok": True})

    client = mock_client(handler)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert response.status_code == 200
    assert len(calls) == 2


def test_transport_error_then_success(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            raise httpx.ConnectError("boom", request=request)
        return httpx.Response(200, json={"ok": True})

    client = mock_client(handler)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert response.status_code == 200
    assert len(calls) == 2


def test_transport_error_raises_after_max_tries(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        raise httpx.ConnectError("boom", request=request)

    client = mock_client(handler)
    with pytest.raises(httpx.ConnectError):
        http.get_with_backoff(client, "https://a.example/x")
    assert len(calls) == http.MAX_TRIES


def test_retry_after_is_capped(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429, headers={"Retry-After": "9999"})
        return httpx.Response(200, json={"ok": True})

    client = mock_client(handler)
    http.get_with_backoff(client, "https://a.example/x")
    assert http.RETRY_AFTER_MAX in no_sleep
    assert max(no_sleep) <= http.RETRY_AFTER_MAX


def test_min_interval_paces_call_slower(mock_client, no_sleep):
    client = mock_client(_ok)
    http.get_with_backoff(
        client, "https://a.example/x", min_interval=2.5
    )
    http.get_with_backoff(
        client, "https://a.example/y", min_interval=2.5
    )
    assert no_sleep and no_sleep[0] > 2.0


def test_other_4xx_is_not_retried(mock_client, no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(404, json={"error": "nope"})

    client = mock_client(handler)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert response.status_code == 404
    assert len(calls) == 1


def test_post_with_backoff_sends_json(mock_client, no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = request.read()
        return httpx.Response(200, json={"ok": True})

    client = mock_client(handler)
    response = http.post_with_backoff(
        client, "https://a.example/x", json={"a": 1}
    )
    assert response.status_code == 200
    assert json.loads(seen["body"]) == {"a": 1}
