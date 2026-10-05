"""Append-only spend ledger: pending reconciliation and summaries."""

import json

import pytest

from lsa.jev.ledger import (
    LEDGER_FIELDS,
    Ledger,
    read_rows,
    summarize,
    unresolved_pending,
)


def row(**over):
    base = {k: None for k in LEDGER_FIELDS}
    base.update(
        ts="2026-10-05T00:00:00+00:00",
        run_id="r1",
        **{"pass": "tenders-which-category"},
        logical_call_id="L1",
        attempt=1,
        cost_class="calculated",
        cost_usd=0.25,
        input_tokens=300,
    )
    base.update(over)
    return base


def test_append_and_read_roundtrip(tmp_path):
    path = tmp_path / "jev_ledger.jsonl"
    with Ledger(path) as led:
        led.append(row())
        led.append(row(run_id="r2", logical_call_id="L2"))
    rows = read_rows(path)
    assert len(rows) == 2
    assert set(rows[0]) == set(LEDGER_FIELDS)
    assert rows[1]["run_id"] == "r2"


def test_unknown_fields_rejected(tmp_path):
    with Ledger(tmp_path / "l.jsonl") as led:
        with pytest.raises(KeyError, match="unknown ledger fields"):
            led.append({**row(), "api_key": "no"})


def test_unresolved_pending_counts_as_unknown(tmp_path):
    path = tmp_path / "jev_ledger.jsonl"
    with Ledger(path) as led:
        led.append(row(cost_class="pending", cost_usd=None, ended_at=None))
        led.append(
            row(
                logical_call_id="L2",
                cost_class="pending",
                cost_usd=None,
                ended_at=None,
            )
        )
        # L2 gets its final row; L1's pending row stays unresolved.
        led.append(row(logical_call_id="L2", cost_class="unknown", cost_usd=None))
    rows = read_rows(path)
    assert [r["logical_call_id"] for r in unresolved_pending(rows)] == ["L1"]
    s = summarize(path)
    assert s["attempts"] == 2
    assert s["unknown_attempts"] == 2


def test_summarize_groups_by_pass(tmp_path):
    path = tmp_path / "jev_ledger.jsonl"
    with Ledger(path) as led:
        led.append(row(**{"pass": "a"}, cost_usd=0.10))
        led.append(row(**{"pass": "b"}, cost_usd=0.20, logical_call_id="L2"))
        led.append(row(**{"pass": "b"}, logical_call_id="L3", cost_usd=0.05))
    s = summarize(path, by="pass")
    assert s["passes"]["a"]["calculated_usd"] == pytest.approx(0.10)
    assert s["passes"]["b"]["calculated_usd"] == pytest.approx(0.25)
    assert s["passes"]["b"]["logical_calls"] == 2
    assert s["calculated_usd"] == pytest.approx(0.35)


def test_missing_ledger_reads_empty(tmp_path):
    assert read_rows(tmp_path / "nope.jsonl") == []
    s = summarize(tmp_path / "nope.jsonl")
    assert s["attempts"] == 0 and s["calculated_usd"] == 0.0


def test_rows_are_valid_json_lines(tmp_path):
    path = tmp_path / "jev_ledger.jsonl"
    with Ledger(path) as led:
        led.append(row())
    for line in path.read_text().splitlines():
        json.loads(line)
