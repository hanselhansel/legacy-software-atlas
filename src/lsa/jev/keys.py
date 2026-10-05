"""API key and endpoint. The Jev key comes from env ``TYPESAFE_API_KEY`` only;
it is never logged, stored, or read from Keychain (plan 2 constraints)."""

import os

PRODUCTION_BASE = "https://api.typesafe.ai"


class MissingKey(RuntimeError):
    pass


def get_api_key() -> str:
    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        raise MissingKey("no Jev key: set TYPESAFE_API_KEY")
    return key


def base_url() -> str:
    return os.environ.get("TYPESAFE_BASE_URL", PRODUCTION_BASE).rstrip("/")
