"""Per-workflow labour pools and AI usage (plan 3, lane N).

One row of ``data/derived/workflows.parquet`` per workflow in
``research/workflows.csv``:

- ``labour_value_usd`` = sum over the workflow's occupations of
  OEWS national employment x mean annual wage x ``time_share``;
- ``employment_share_sum`` = sum of employment x ``time_share``;
- ``ai_usage`` = mean Anthropic Economic Index usage share over the
  workflow's O*NET-mapped tasks (deduplicated by Task ID, null when
  nothing maps);
- ``n_tasks`` / ``n_tasks_matched`` = distinct task texts research
  listed / matched to an O*NET Task ID;
- ``notes`` = fallbacks and gaps (SOC -> broader OEWS group, unmatched
  tasks, unavailable sources). Region is ``US`` (OEWS national).
"""

from __future__ import annotations

import csv
import logging
from collections import defaultdict
from pathlib import Path

from lsa.workflows_labour import aiuse, oews, onet

log = logging.getLogger(__name__)

REGION = "US"

SCHEMA_FIELDS = (
    ("workflow_id", "string"),
    ("category", "string"),
    ("region", "string"),
    ("labour_value_usd", "float64"),
    ("employment_share_sum", "float64"),
    ("ai_usage", "float64"),
    ("n_tasks", "int64"),
    ("n_tasks_matched", "int64"),
    ("notes", "string"),
)


def load_workflows(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_occupations(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _fmt_soc(soc6: str | None) -> str:
    return (
        f"{soc6[:2]}-{soc6[2:]}"
        if soc6 and len(soc6) == 6
        else str(soc6)
    )


def _share(value: str | None) -> float | None:
    try:
        return float(value) if value not in (None, "") else None
    except ValueError:
        return None


def workflow_rows(
    workflows: list[dict],
    occs: list[dict],
    matches: list[onet.TaskMatch],
    wages: dict[str, oews.OewsRow],
    usage_by_id: dict[str, float | None],
    *,
    global_notes: list[str] | None = None,
) -> list[dict]:
    """Assemble the parquet rows (unsorted input order)."""
    occ_by_wf: dict[str, list[dict]] = defaultdict(list)
    for r in occs:
        occ_by_wf[(r.get("workflow_id") or "").strip()].append(r)
    match_by_wf: dict[str, list[onet.TaskMatch]] = defaultdict(list)
    for m in matches:
        match_by_wf[m.workflow_id].append(m)

    rows = []
    for w in workflows:
        wid = (w.get("workflow_id") or "").strip()
        notes: list[str] = list(global_notes or [])

        labour = 0.0
        emp_sum = 0.0
        any_wage = False
        for r in occ_by_wf.get(wid, []):
            code = (r.get("soc_code") or "").strip()
            req = oews.soc6(code)
            share = _share(r.get("time_share"))
            if share is None:
                notes.append(f"{code} bad time_share")
                continue
            wr = wages.get(req)
            if (
                wr is None
                or wr.employment is None
                or wr.annual_mean_wage is None
            ):
                notes.append(f"{code} no oews")
                continue
            any_wage = True
            labour += wr.employment * wr.annual_mean_wage * share
            emp_sum += wr.employment * share
            used = {s for s in (wr.emp_soc, wr.wage_soc) if s}
            if used - {req}:
                worst = max(
                    used - {req},
                    key=lambda u: oews.candidates(req).index(u)
                    if u in oews.candidates(req)
                    else 9,
                )
                notes.append(
                    f"{code} via {oews.level_name(req, worst)} "
                    f"{_fmt_soc(worst)}"
                )

        # A task text counts once per workflow; it is matched when any
        # of its occupation listings resolved to a Task ID.
        matched: dict[str, bool] = {}
        task_ids = []
        for m in match_by_wf.get(wid, []):
            key = onet.norm(m.task_text)
            matched[key] = matched.get(key, False) or m.task_id is not None
            if m.task_id is not None:
                task_ids.append(m.task_id)
        unmatched = sum(1 for ok in matched.values() if not ok)
        shares = [
            usage_by_id[tid]
            for tid in dict.fromkeys(task_ids)
            if usage_by_id.get(tid) is not None
        ]
        if unmatched:
            notes.append(f"{unmatched}/{len(matched)} tasks unmatched")
        rows.append(
            {
                "workflow_id": wid,
                "category": (w.get("category") or "").strip(),
                "region": REGION,
                "labour_value_usd": labour if any_wage else None,
                "employment_share_sum": emp_sum if any_wage else None,
                "ai_usage": (
                    sum(shares) / len(shares) if shares else None
                ),
                "n_tasks": len(matched),
                "n_tasks_matched": len(matched) - unmatched,
                "notes": "; ".join(notes),
            }
        )
    return rows


def write_parquet(rows: list[dict], path: Path) -> Path:
    import pyarrow as pa
    import pyarrow.parquet as pq

    schema = pa.schema(
        [(name, getattr(pa, t)()) for name, t in SCHEMA_FIELDS]
    )
    table = pa.Table.from_pylist(
        [{k: r.get(k) for k, _ in SCHEMA_FIELDS} for r in rows],
        schema=schema,
    )
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(table, path)
    return path


def run(
    *,
    workflows_path: Path,
    occ_path: Path,
    out_path: Path,
    raw_dir: Path,
    onet_path: Path | None = None,
    oews_cache: Path | None = None,
    aiuse_path: Path | None = None,
    refresh: bool = False,
    client=None,
    log=print,
) -> list[dict]:
    """Load inputs, fetch the three sources, write workflows.parquet."""
    workflows = load_workflows(Path(workflows_path))
    occs = load_occupations(Path(occ_path))
    raw_dir = Path(raw_dir)
    own = client is None
    if own:
        from lsa.sources import http

        client = http.make_client()
    global_notes: list[str] = []
    try:
        tpath = (
            Path(onet_path)
            if onet_path is not None
            else onet.task_file(
                raw_dir / "onet", refresh=refresh, client=client, log=log
            )
        )
        tasks = onet.load_tasks(tpath) if tpath else []
        if not tasks:
            global_notes.append("onet task file unavailable")
        matches = onet.match_tasks(occs, tasks)

        wages = oews.wages_for(
            {r.get("soc_code") for r in occs},
            client,
            oews_cache or raw_dir / "oews" / "api.json",
            refresh=refresh,
        )
        if not any(w.employment for w in wages.values()):
            global_notes.append("oews unavailable")

        upath = (
            Path(aiuse_path)
            if aiuse_path is not None
            else aiuse.usage_file(
                raw_dir / "aiuse", refresh=refresh, client=client, log=log
            )
        )
        shares = aiuse.usage_shares(upath) if upath else {}
        if not shares:
            global_notes.append("ai usage file unavailable")
        usage_by_id = {t.task_id: shares.get(t.norm) for t in tasks}

        rows = workflow_rows(
            workflows,
            occs,
            matches,
            wages,
            usage_by_id,
            global_notes=global_notes,
        )
        write_parquet(rows, out_path)
        return rows
    finally:
        if own:
            client.close()
