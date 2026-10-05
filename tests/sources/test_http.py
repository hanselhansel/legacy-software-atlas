"""Tests for shared HTTP plumbing (plan 1, task 3, lane B).

All transports are httpx.MockTransport; no test touches the network.
"""

from __future__ import annotations

import json

import httpx
import pytest

from lsa.sources import http


def _client(handler) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler))


def _ok(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"ok": True})


@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch):
    """No test sleeps; every call to http._sleep is recorded instead."""
    calls: list[float] = []
    monkeypatch.setattr(http, "_sleep", calls.append)
    http._last_call.clear()
    yield calls
    http._last_call.clear()


def test_make_client_sets_user_agent_and_timeout():
    client = http.make_client()
    assert client.headers["user-agent"] == (
        "legacy-software-atlas research "
        "(github.com/hanselhansel/legacy-software-atlas)"
    )
    assert client.timeout.connect == 30.0


def test_get_with_backoff_returns_200(_no_sleep):
    client = _client(_ok)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_paces_calls_to_same_host(_no_sleep):
    client = _client(_ok)
    http.get_with_backoff(client, "https://a.example/x")
    http.get_with_backoff(client, "https://a.example/y")
    # Second call to a.example waits about a second.
    assert _no_sleep and 0.5 < _no_sleep[0] <= 1.0


def test_no_pace_across_different_hosts(_no_sleep):
    client = _client(_ok)
    http.get_with_backoff(client, "https://a.example/x")
    http.get_with_backoff(client, "https://b.example/x")
    assert _no_sleep == []


def test_429_then_success_retries(_no_sleep):
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.url.path)
        if len(seen) == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"ok": True})

    client = _client(handler)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert response.status_code == 200
    assert len(seen) == 2


def test_retry_after_header_is_honoured(_no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429, headers={"Retry-After": "7"})
        return httpx.Response(200, json={"ok": True})

    client = _client(handler)
    http.get_with_backoff(client, "https://a.example/x")
    assert 7.0 in _no_sleep


def test_persistent_429_raises_after_max_tries(_no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(429)

    client = _client(handler)
    with pytest.raises(httpx.HTTPStatusError):
        http.get_with_backoff(client, "https://a.example/x")
    assert len(calls) == http.MAX_TRIES


def test_5xx_is_retried(_no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(503)

    client = _client(handler)
    with pytest.raises(httpx.HTTPStatusError):
        http.get_with_backoff(client, "https://a.example/x")
    assert len(calls) == http.MAX_TRIES


def test_other_4xx_is_not_retried(_no_sleep):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(404, json={"error": "nope"})

    client = _client(handler)
    response = http.get_with_backoff(client, "https://a.example/x")
    assert response.status_code == 404
    assert len(calls) == 1


def test_post_with_backoff_sends_json(_no_sleep):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = request.read()
        return httpx.Response(200, json={"ok": True})

    client = _client(handler)
    response = http.post_with_backoff(
        client, "https://a.example/x", json={"a": 1}
    )
    assert response.status_code == 200
    assert json.loads(seen["body"]) == {"a": 1}
