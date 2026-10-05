"""Shared fixtures for source-collector tests."""

from __future__ import annotations

import httpx
import pytest

from lsa.sources import http


class _SleepLog(list):
    """Recorded sleeps that also unpacks as ``get_kwargs``.

    Both lanes named their fixture ``no_sleep``: one lane read it as the
    list of seconds ``http._sleep`` was asked to wait, the other passed it
    as ``get_kwargs`` (a ``{"sleep": fn}`` mapping). ``keys`` plus
    ``__getitem__`` give the list a minimal mapping face, so
    ``**no_sleep`` yields ``{"sleep": log.append}`` and every wait lands in
    the same list either way.
    """

    def keys(self):
        return ["sleep"]

    def __getitem__(self, key):
        if key == "sleep":
            return self.append
        return super().__getitem__(key)


@pytest.fixture
def no_sleep(monkeypatch):
    """Replace http._sleep with a recorder; clears the host-pacing clock."""
    calls = _SleepLog()
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
