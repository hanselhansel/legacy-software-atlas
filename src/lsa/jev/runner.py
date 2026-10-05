"""Batch runner: packed items -> answer parts, ledger + budget + resume.

Sync port of jev-opportunity-atlas ``inference.runner`` minus the response
cache (``done.jsonl`` resume covers crashes). Per pack: ``done`` skip ->
``pending`` ledger row -> per-attempt reserve/settle through ``on_attempt`` ->
``calculated``/``unknown`` final row -> answer rows -> done rows. A crash
leaves a ``pending`` row the next run reconciles to ``unknown``; a
``BudgetExceeded`` stops the run cleanly with ``stopped="budget"`` and
everything completed so far stays flushed.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from lsa.jev.budget import BudgetExceeded, BudgetGuard, ledger_path
from lsa.jev.client import JevClient
from lsa.jev.ledger import Ledger, read_rows, unresolved_pending
from lsa.jev.questions import (
    canonical_json,
    pack_body,
    pack_questions,
    pack_state,
    unpack_answers,
)
from lsa.jev.state import (
    answer_rows,
    append_done,
    ensure_manifest,
    load_done,
    write_part,
)

FLUSH_ITEMS = 200
CHARS_PER_TOKEN = 3.2


def _utcnow() -> str:
    return datetime.now(UTC).isoformat()


@dataclass
class RunContext:
    run_id: str
    client: JevClient
    guard: BudgetGuard
    model: str
    price_version: str
    run_dir: Path
    items_per_call: int = 5
    budget: str | None = None

    def __post_init__(self) -> None:
        if self.budget is None:
            self.budget = self.guard.name


def _chunks(items: list[dict], size: int) -> list[list[dict]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def _base_row(ctx, qs, members, logical_call_id: str) -> dict:
    return {
        "ts": _utcnow(),
        "run_id": ctx.run_id,
        "pass": ctx.budget,
        "logical_call_id": logical_call_id,
        "item_ids": [str(m["item_id"]) for m in members],
        "slot_count": len(members),
        "model_requested": ctx.model,
        "price_version": ctx.price_version,
    }


def _final_row(ctx, qs, members, logical_call_id: str, a) -> dict:
    known = a.charge_known
    return {
        **_base_row(ctx, qs, members, logical_call_id),
        "attempt": a.attempt,
        "started_at": a.started_at,
        "ended_at": a.ended_at,
        "request_ms": a.request_ms,
        "http_status": a.http_status,
        "request_id": a.request_id,
        "error_type": a.error_type,
        "validation": a.validation,
        "input_tokens": a.input_tokens,
        "output_tokens": a.output_tokens,
        "model_returned": a.model_returned,
        "cost_class": "calculated" if known else "unknown",
        "cost_usd": (a.input_tokens or 0) * ctx.guard.usd_per_input_token
        if known
        else None,
    }


def _reconcile_pending(ledger: Ledger, lp: Path) -> None:
    """Crash leftovers: unresolved pending rows become unknown final rows."""
    for row in unresolved_pending(read_rows(lp)):
        ledger.append(
            {
                **row,
                "cost_class": "unknown",
                "cost_usd": None,
                "validation": "not_attempted",
                "ended_at": _utcnow(),
            },
            sync=True,
        )


def run(ctx: RunContext, items: list[dict], qs, lp: Path | None = None) -> dict:
    """Label ``items`` in packs of ``ctx.items_per_call``. Returns counters:
    completed/failed/skipped_done/new_requests/stopped/wall_s."""
    t0 = time.monotonic()
    lp = ledger_path(lp)
    ctx.run_dir.mkdir(parents=True, exist_ok=True)
    ensure_manifest(
        ctx.run_dir, qs, ctx.model, ctx.price_version, ctx.guard.cap_usd
    )
    out = {
        "completed": 0,
        "failed": 0,
        "skipped_done": 0,
        "new_requests": 0,
        "stopped": None,
    }
    rows_buf: list[dict] = []
    ids_buf: list[str] = []

    def flush() -> None:
        if not ids_buf:
            return
        seq = write_part(ctx.run_dir, rows_buf)
        append_done(
            ctx.run_dir,
            [
                {"item_id": iid, "question_set": qs.label, "part": seq}
                for iid in ids_buf
            ],
        )
        rows_buf.clear()
        ids_buf.clear()

    with Ledger(lp) as ledger:
        _reconcile_pending(ledger, lp)
        done = load_done(ctx.run_dir, qs.label)
        pending = [i for i in items if str(i["item_id"]) not in done]
        out["skipped_done"] = len(items) - len(pending)
        for seq, members in enumerate(_chunks(pending, ctx.items_per_call)):
            if _process_pack(ctx, qs, ledger, members, seq, out, rows_buf, ids_buf):
                break
            if len(ids_buf) >= FLUSH_ITEMS:
                flush()
        flush()
    out["wall_s"] = time.monotonic() - t0
    return out


def _process_pack(ctx, qs, ledger, members, seq, out, rows_buf, ids_buf) -> bool:
    """One packed call over ``members``. Returns True when the run must stop."""
    questions = pack_questions(qs, len(members))
    state = pack_state(members)
    body = pack_body(members, qs, ctx.model)
    est = math.ceil(len(canonical_json(body).encode("utf-8")) / CHARS_PER_TOKEN)
    lcid = f"{qs.label}:{ctx.run_id}:{seq}"
    handle = None

    def on_attempt(event) -> None:
        nonlocal handle
        if event.phase == "before_send":
            handle = ctx.guard.reserve(est)
            ledger.append(
                {
                    **_base_row(ctx, qs, members, lcid),
                    "attempt": event.attempt_no,
                    "started_at": _utcnow(),
                    "cost_class": "pending",
                },
                sync=True,
            )
            out["new_requests"] += 1
        else:
            a = event.attempt
            ctx.guard.settle(handle, a.input_tokens, a.charge_known)
            ledger.append(_final_row(ctx, qs, members, lcid, a), sync=True)

    try:
        res = ctx.client.evaluate(state, questions, ctx.model, on_attempt=on_attempt)
    except BudgetExceeded:
        out["stopped"] = "budget"
        return True
    if not res.ok:
        out["failed"] += len(members)
        return False
    per_item = unpack_answers(questions, res.answers, members)
    last = res.attempts[-1]
    for m in members:
        iid = str(m["item_id"])
        member = per_item.get(iid)
        if member is None:
            out["failed"] += 1
            continue
        rows_buf.extend(
            answer_rows(
                ctx.run_id,
                iid,
                qs,
                member,
                res.model_returned,
                last.request_id,
                lcid,
            )
        )
        ids_buf.append(iid)
        out["completed"] += 1
    return False


def merge_answers(run_dirs: list[Path]) -> list[dict]:
    """All ANSWERS part rows across run dirs (latest part per item wins)."""
    import pyarrow.parquet as pq

    seen: dict[tuple[str, str, str], dict] = {}
    for d in run_dirs:
        for part in sorted((d / "answers").glob("part-*.parquet")):
            for row in pq.read_table(part).to_pylist():
                key = (row["question_set"], row["item_id"], row["question_id"])
                seen[key] = row
    return list(seen.values())
