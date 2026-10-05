"""Append-only JSONL spend ledger at data/derived/jev_ledger.jsonl.

One row per network attempt (cost_class calculated | unknown | pending). A
``pending`` row written before send is superseded by the final row for the same
(run_id, logical_call_id, attempt); on restart an unresolved pending row counts
as an unknown charge, never silently dropped. Ported from jev-opportunity-atlas
``inference.ledger``, but cumulative: every pass and run shares the one file,
so account-wide spend is a single scan.
"""

from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path
from typing import Self

SYNC_EVERY = 50

LEDGER_FIELDS = (
    "ts",
    "run_id",
    "pass",
    "logical_call_id",
    "item_ids",
    "slot_count",
    "attempt",
    "model_requested",
    "model_returned",
    "request_id",
    "started_at",
    "ended_at",
    "request_ms",
    "http_status",
    "error_type",
    "validation",
    "input_tokens",
    "output_tokens",
    "cost_class",
    "cost_usd",
    "price_version",
)


class Ledger:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._fh = self.path.open("a", encoding="utf-8")
        self._rows = 0
        self._closed = False

    def append(self, row: dict, sync: bool = False) -> None:
        unknown = set(row) - set(LEDGER_FIELDS)
        if unknown:
            raise KeyError(f"unknown ledger fields: {sorted(unknown)}")
        out = {k: row.get(k) for k in LEDGER_FIELDS}
        self._fh.write(json.dumps(out, ensure_ascii=False) + "\n")
        self._rows += 1
        self._fh.flush()
        if sync or self._rows % SYNC_EVERY == 0:
            os.fsync(self._fh.fileno())

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._fh.flush()
        os.fsync(self._fh.fileno())
        self._fh.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc) -> bool:
        self.close()
        return False


def read_rows(path) -> list[dict]:
    p = Path(path)
    if not p.exists():
        return []
    return [
        json.loads(line)
        for line in p.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def unresolved_pending(rows: list[dict]) -> list[dict]:
    """Pending rows with no non-pending row for the same
    (run_id, logical_call_id, attempt): sends that crashed mid-flight."""
    finals = {
        (r.get("run_id"), r.get("logical_call_id"), r.get("attempt"))
        for r in rows
        if r.get("cost_class") != "pending"
    }
    return [
        r
        for r in rows
        if r.get("cost_class") == "pending"
        and (r.get("run_id"), r.get("logical_call_id"), r.get("attempt"))
        not in finals
    ]


def _attempt_stats(rows: list[dict]) -> dict:
    """Totals for a row subset: calculated spend, unknown attempt count."""
    return {
        "attempts": len(rows),
        "logical_calls": len({r.get("logical_call_id") for r in rows}),
        "calculated_usd": sum(
            r["cost_usd"]
            for r in rows
            if r.get("cost_class") == "calculated" and r.get("cost_usd") is not None
        ),
        "unknown_attempts": sum(
            1 for r in rows if r.get("cost_class") in ("unknown", "pending")
        ),
        "input_tokens": sum(
            r["input_tokens"] for r in rows if r.get("input_tokens") is not None
        ),
        "by_status": dict(
            Counter(str(r.get("http_status") or "none") for r in rows)
        ),
    }


def summarize(path, by: str | None = None) -> dict:
    """Spend and attempt totals over the ledger; unresolved pending rows count
    as unknown attempts. ``by="pass"`` adds a per-pass breakdown."""
    rows = read_rows(path)
    pending = unresolved_pending(rows)
    network = [r for r in rows if r.get("cost_class") != "pending"] + pending
    summary = _attempt_stats(network)
    if by == "pass":
        groups: dict = {}
        for r in network:
            groups.setdefault(r.get("pass"), []).append(r)
        summary["passes"] = {name: _attempt_stats(rs) for name, rs in groups.items()}
    elif by is not None:
        raise ValueError(f"unknown summarize grouping: {by!r}")
    return summary
