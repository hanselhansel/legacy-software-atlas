"""Anthropic Economic Index task usage (plan 3, lane N).

``usage_file`` finds the EconomicIndex dataset on Hugging Face via the
datasets search API (preferring ``Anthropic/EconomicIndex``), lists its
files and downloads the task-level usage file into git-ignored
``data/raw/aiuse/``. At build time that is
``labor_market_impacts/task_penetration.csv``: one row per O*NET task
text with the share of Claude traffic on it. ``usage_shares`` maps
normalised task text to the share; O*NET tasks with no row map to null.
"""

from __future__ import annotations

import csv
import logging
import re
from pathlib import Path
from urllib.parse import quote

from lsa.workflows_labour import net, onet

log = logging.getLogger(__name__)

SEARCH_API = "https://huggingface.co/api/datasets?search=EconomicIndex"
REPO_API = "https://huggingface.co/api/datasets/{repo}"
RESOLVE = "https://huggingface.co/datasets/{repo}/resolve/main/{name}"
PREFERRED_REPO = "Anthropic/EconomicIndex"

# Basenames that hold task text but not a usage share.
_SKIP_BASENAME = (
    "statement",
    "mapping",
    "thinking",
    "emerging",
    "ratings",
    "tasks_to",
    "automation",
)
_SHARE_COLS = ("penetration", "pct", "share", "usage", "proportion", "value")


def find_repo(client) -> str | None:
    """Dataset id of the EconomicIndex repo, preferring Anthropic's."""
    from lsa.sources import http

    data = http.get_with_backoff(client, SEARCH_API).json()
    ids = [d.get("id") for d in data if isinstance(d, dict)]
    if PREFERRED_REPO in ids:
        return PREFERRED_REPO
    return next(
        (i for i in ids if i and "economicindex" in i.lower()), None
    )


def list_files(repo: str, client) -> list[str]:
    """Sibling file names inside the dataset repo."""
    from lsa.sources import http

    data = http.get_with_backoff(client, REPO_API.format(repo=repo)).json()
    return [
        s["rfilename"]
        for s in data.get("siblings", [])
        if "rfilename" in s
    ]


def choose_file(names: list[str]) -> str | None:
    """Pick the task-level usage csv among dataset siblings.

    Preference order on the basename: penetration, usage, share, pct;
    then the shallowest, shortest name for determinism.
    """
    cands = []
    for n in names:
        base = n.rsplit("/", 1)[-1].lower()
        if not base.endswith(".csv") or "task" not in base:
            continue
        if any(s in base for s in _SKIP_BASENAME):
            continue
        cands.append(n)

    def rank(name: str):
        base = name.rsplit("/", 1)[-1].lower()
        ver = max(
            (int(d) for d in re.findall(r"_v(\d+)", base)), default=0
        )
        for i, k in enumerate(("penetration", "usage", "share", "pct")):
            if k in base:
                return (i, -ver, name.count("/"), len(name), name)
        return (9, -ver, name.count("/"), len(name), name)

    return min(cands, key=rank) if cands else None


def _task_col(fields: list[str]) -> str | None:
    for f in fields:
        if f.strip().lower() == "task":
            return f
    for f in fields:
        low = f.strip().lower()
        if "task" in low and not any(
            k in low for k in ("id", "code", "type", "penetration", "pct")
        ):
            return f
    return None


def _share_col(fields: list[str]) -> str | None:
    for want in _SHARE_COLS:
        for f in fields:
            if f.strip().lower() == want or f.strip().lower().endswith(
                "_" + want
            ):
                return f
    return None


def usage_shares(path: Path) -> dict[str, float]:
    """``{normalised task text: usage share}`` from the usage csv."""
    shares: dict[str, float] = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        tcol, scol = _task_col(fields), _share_col(fields)
        if tcol is None or scol is None:
            raise ValueError(
                f"{path}: need task + share columns, got {fields}"
            )
        for r in reader:
            try:
                share = float((r.get(scol) or "").strip())
            except ValueError:
                continue
            n = onet.norm(r.get(tcol) or "")
            if n:
                shares[n] = max(share, shares.get(n, share))
    return shares


def usage_file(
    raw_dir: Path,
    *,
    refresh: bool = False,
    client=None,
    deadline_s: float = net.DEADLINE_S,
    log=print,
) -> Path | None:
    """Cached usage csv, discovered and downloaded when needed."""
    raw_dir = Path(raw_dir)
    cached = sorted(raw_dir.glob("*.csv"))
    if cached and not refresh:
        pick = choose_file([c.name for c in cached]) or cached[0].name
        return raw_dir / pick
    own = client is None
    if own:
        from lsa.sources import http

        client = http.make_client()
    try:
        repo = find_repo(client)
        if repo is None:
            log("aiuse: no EconomicIndex dataset found")
            return None
        name = choose_file(list_files(repo, client))
        if name is None:
            log(f"aiuse: no task-level csv in {repo}")
            return None
        dest = raw_dir / name.rsplit("/", 1)[-1]
        url = RESOLVE.format(repo=repo, name=quote(name, safe="/"))
        return net.download(client, url, dest, deadline_s=deadline_s)
    except Exception as exc:  # noqa: BLE001 - caller notes and continues
        log(f"aiuse download: {exc}")
        return None
    finally:
        if own:
            client.close()
