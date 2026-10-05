"""O*NET task statements (plan 3, lane N).

The O*NET database Task Statements table (U.S. Department of Labor,
CC BY 4.0, onetcenter.org) lists every task per O*NET-SOC code.
``task_file`` downloads the current db CSV into git-ignored
``data/raw/onet/``; ``load_tasks`` parses it; ``match_tasks`` maps each
`` | ``-separated task text in ``research/workflow_occupations.csv`` to
an O*NET Task ID:

1. exact task-text match (any SOC),
2. normalised-text match within the same SOC (punctuation stripped,
   lowercased),
3. best token-overlap within the same SOC, kept above a floor.

Every input task records a quality: ``exact``, ``normalized``,
``overlap`` (with the score) or ``unmatched``.
"""

from __future__ import annotations

import csv
import logging
import re
from dataclasses import dataclass
from pathlib import Path

from lsa.workflows_labour import net

log = logging.getLogger(__name__)

DB_PAGE = "https://www.onetcenter.org/database.html"
FILE_TEMPLATE = (
    "https://www.onetcenter.org/dl_files/database/"
    "{ver}_csv/task_statements.csv"
)
FALLBACK_VERSIONS = ("db_31_0", "db_30_0", "db_29_0", "db_28_0")
_VERSION_RE = re.compile(r"(db_\d+_\d+)_csv/task_statements")

_SPLIT = re.compile(r"\s*\|\s*")
_NONALNUM = re.compile(r"[^a-z0-9 ]+")
_WS = re.compile(r"\s+")

MIN_OVERLAP = 0.34


def soc_base(code: str) -> str:
    """The 7-char SOC of an O*NET or plain code (``13-2099.04`` -> ``13-2099``)."""
    return (code or "").strip()[:7]


def norm(text: str) -> str:
    """Lowercase, punctuation stripped, whitespace collapsed."""
    return _WS.sub(
        " ", _NONALNUM.sub(" ", (text or "").lower())
    ).strip()


def split_tasks(cell: str) -> list[str]:
    """The `` | ``-separated task texts of one onet_tasks cell."""
    return [p.strip() for p in _SPLIT.split(cell or "") if p.strip()]


@dataclass
class OnetTask:
    soc: str
    onet_soc: str
    task_id: str
    task: str
    norm: str
    tokens: frozenset[str]


@dataclass
class TaskMatch:
    workflow_id: str
    soc_code: str
    task_text: str
    task_id: str | None
    quality: str
    score: float | None


def load_tasks(path: Path) -> list[OnetTask]:
    """Parse the Task Statements csv (comma or tab delimited)."""
    tasks = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        header = f.readline()
        f.seek(0)
        dialect = "excel-tab" if "\t" in header else "excel"
        for r in csv.DictReader(f, dialect=dialect):
            task = (r.get("Task") or "").strip()
            tid = (r.get("Task ID") or "").strip()
            code = (r.get("O*NET-SOC Code") or "").strip()
            if not (task and tid and code):
                continue
            n = norm(task)
            tasks.append(
                OnetTask(
                    soc=soc_base(code),
                    onet_soc=code,
                    task_id=tid,
                    task=task,
                    norm=n,
                    tokens=frozenset(n.split()),
                )
            )
    return tasks


def _match_one(
    workflow_id: str,
    soc_code: str,
    text: str,
    cands: list[OnetTask],
    exact_idx: dict[str, list[OnetTask]],
) -> TaskMatch:
    hits = exact_idx.get(text)
    if hits:
        pick = next(
            (t for t in hits if t.soc == soc_base(soc_code)), hits[0]
        )
        return TaskMatch(workflow_id, soc_code, text, pick.task_id, "exact", 1.0)
    n = norm(text)
    for t in cands:
        if t.norm == n:
            return TaskMatch(
                workflow_id, soc_code, text, t.task_id, "normalized", 1.0
            )
    best: OnetTask | None = None
    score = 0.0
    toks = frozenset(n.split())
    if toks:
        for t in cands:
            inter = len(toks & t.tokens)
            if not inter:
                continue
            s = inter / len(toks | t.tokens)
            if s > score:
                best, score = t, s
    if best is not None and score >= MIN_OVERLAP:
        return TaskMatch(
            workflow_id, soc_code, text, best.task_id, "overlap", score
        )
    return TaskMatch(
        workflow_id, soc_code, text, None, "unmatched", score or None
    )


def match_tasks(
    occ_rows: list[dict], tasks: list[OnetTask]
) -> list[TaskMatch]:
    """Match every task text of every occupation row."""
    by_soc: dict[str, list[OnetTask]] = {}
    exact_idx: dict[str, list[OnetTask]] = {}
    for t in tasks:
        by_soc.setdefault(t.soc, []).append(t)
        exact_idx.setdefault(t.task, []).append(t)
    out = []
    for row in occ_rows:
        wid = (row.get("workflow_id") or "").strip()
        code = (row.get("soc_code") or "").strip()
        cands = by_soc.get(soc_base(code), [])
        for text in split_tasks(row.get("onet_tasks") or ""):
            out.append(_match_one(wid, code, text, cands, exact_idx))
    return out


def _candidate_urls(client) -> list[str]:
    """Current db csv URL from the database page, then known versions."""
    urls = []
    try:
        from lsa.sources import http

        resp = http.get_with_backoff(client, DB_PAGE)
        if resp.status_code == 200:
            m = _VERSION_RE.search(resp.text)
            if m:
                urls.append(FILE_TEMPLATE.format(ver=m.group(1)))
    except Exception as exc:  # noqa: BLE001 - page probe is best-effort
        log.info("onet database page: %s", exc)
    urls += [FILE_TEMPLATE.format(ver=v) for v in FALLBACK_VERSIONS]
    return list(dict.fromkeys(urls))


def task_file(
    raw_dir: Path,
    *,
    refresh: bool = False,
    client=None,
    deadline_s: float = net.DEADLINE_S,
    log=print,
) -> Path | None:
    """The cached Task Statements csv, downloading when needed."""
    dest = Path(raw_dir) / "task_statements.csv"
    if dest.exists() and not refresh:
        return dest
    own = client is None
    if own:
        from lsa.sources import http

        client = http.make_client()
    try:
        for url in _candidate_urls(client):
            try:
                return net.download(
                    client, url, dest, deadline_s=deadline_s
                )
            except Exception as exc:  # noqa: BLE001 - try next version
                log(f"onet download {url}: {exc}")
        return None
    finally:
        if own:
            client.close()
