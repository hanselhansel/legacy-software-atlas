"""Shared fixtures for source-collector tests."""

from __future__ import annotations

import httpx
import pytest

from lsa.sources import http


@pytest.fixture
def no_sleep(monkeypatch):
    """Replace http._sleep with a recorder; clears the host-pacing clock."""
    calls: list[float] = []
    monkeypatch.setattr(http, "_sleep", calls.append)
    http._last_call.clear()
    yield calls
    http._last_call.clear()


@pytest.fixture
def mock_client():
    """Factory of httpx.Client over MockTransport; never reaches the network."""

    def _make(handler) -> httpx.Client:
        return httpx.Client(transport=httpx.MockTransport(handler))

    return _make
