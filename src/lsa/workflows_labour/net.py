"""One-shot file downloads for the lane's source datasets.

``download`` streams a GET to a path, aborting when the transfer runs
past ``deadline_s`` (the lane's two-minute timebox). A partially written
file is discarded so a later retry never reads it as a complete cache.
"""

from __future__ import annotations

import time
from pathlib import Path

import httpx

DEADLINE_S = 120.0
CHUNK = 1 << 16
ATTEMPTS = 2


class DownloadTimeout(Exception):
    """Raised when a download exceeds the deadline."""


def download(
    client: httpx.Client,
    url: str,
    dest: Path,
    *,
    deadline_s: float = DEADLINE_S,
) -> Path:
    """Stream ``url`` to ``dest``; raise after ``deadline_s`` seconds."""
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.name + ".part")
    t0 = time.monotonic()
    last_exc: Exception | None = None
    for _ in range(ATTEMPTS):
        try:
            with (
                client.stream("GET", url) as resp,
                open(tmp, "wb") as f,
            ):
                resp.raise_for_status()
                for chunk in resp.iter_bytes(CHUNK):
                    if time.monotonic() - t0 > deadline_s:
                        raise DownloadTimeout(
                            f"{url}: download exceeded {deadline_s:.0f}s"
                        )
                    f.write(chunk)
            tmp.replace(dest)
            return dest
        except (httpx.HTTPError, DownloadTimeout, OSError) as exc:
            last_exc = exc
            if tmp.exists():
                tmp.unlink()
            if time.monotonic() - t0 > deadline_s:
                break
    raise last_exc or DownloadTimeout(f"{url}: no attempts made")
