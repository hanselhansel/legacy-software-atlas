"""Shared fixtures: reset per-host caches between tests."""

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
def no_sleep():
    """get_kwargs that make get_with_backoff never wait."""

    return {"sleep": lambda _seconds: None}
