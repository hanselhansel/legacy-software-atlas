"""Shared fixtures for awards tests: mock transports, no real sleeping."""

from __future__ import annotations

import httpx
import pytest

from lsa.sources import http, robots


@pytest.fixture(autouse=True)
def _reset_host_caches():
    robots._reset_cache()
    http._LAST_AT.clear()
    yield
    robots._reset_cache()
    http._LAST_AT.clear()


@pytest.fixture
def mock_client():
    """Factory of httpx.Client over MockTransport; never reaches the network."""

    def _make(handler) -> httpx.Client:
        return httpx.Client(transport=httpx.MockTransport(handler))

    return _make


@pytest.fixture
def no_sleep(monkeypatch):
    """Replace http._sleep with a recorder; clears the host-pacing clock."""
    calls = []
    monkeypatch.setattr(http, "_sleep", calls.append)
    http._last_call.clear()
    yield calls
    http._last_call.clear()
