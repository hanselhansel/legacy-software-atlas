"""Runner: packed calls over a real transport mock, ledger, resume, budget."""

import json

import pyarrow.parquet as pq
import pytest

from lsa.jev.budget import BudgetGuard
from lsa.jev.client import CANARY_PREFIX, JevClient, RetryPolicy
from lsa.jev.ledger import LEDGER_FIELDS, Ledger, read_rows, unresolved_pending
from lsa.jev.questions import QuestionSet, canonical_json, pack_body
from lsa.jev.runner import RunContext, run
from lsa.jev.state import load_done
from tests.jev.mock_jev import make_transport

CANARY = CANARY_PREFIX + "f" * 64
PRICE = 0.042e-6
WORST = 4000

QS = QuestionSet(
    "t: p",
    "t-p",
    1,
    "t-p@v1",
    {
        "prob": {"type": "probability", "instructions": "is `item` bad?"},
        "kind": {
            "type": "choice",
            "instructions": "kind of `item`?",
            "criteria": {"a": "A", "b": "B"},
        },
    },
    "x" * 64,
)


def items(n: int, prefix: str = "it") -> list[dict]:
    return [
        {"item_id": f"{prefix}{i}", "text": f"text {i} mentions COBOL"}
        for i in range(n)
    ]


def make_ctx(tmp_path, script, cap_usd=10.0, items_per_call=2, seen=None):
    client = JevClient(
        api_key=CANARY,
        base="http://mock",
        transport=make_transport(script, seen),
        policy=RetryPolicy(max_attempts=3, backoff_initial=0, backoff_max=0),
    )
    guard = BudgetGuard(
        cap_usd=cap_usd,
        usd_per_input_token=PRICE,
        worst_case_tokens_unknown=WORST,
        name="t-p",
        account_total=None,
    )
    ctx = RunContext(
        run_id="r-test",
        client=client,
        guard=guard,
        model="jev-1.13.0",
        price_version="typesafe-2026-09-28",
        run_dir=tmp_path / "jev" / "t-p",
        items_per_call=items_per_call,
    )
    return ctx, client


def read_answers(dir_):
    rows = []
    for part in sorted((dir_ / "answers").glob("part-*.parquet")):
        rows.extend(pq.read_table(part).to_pylist())
    return rows


def test_full_run_writes_answers_done_and_ledger(tmp_path):
    ledger = tmp_path / "jev_ledger.jsonl"
    ctx, client = make_ctx(tmp_path, [])
    out = run(ctx, items(4), QS, lp=ledger)
    client.close()
    assert out["stopped"] is None
    assert (out["completed"], out["failed"], out["new_requests"]) == (4, 0, 2)

    answers = read_answers(ctx.run_dir)
    assert len(answers) == 8  # 4 items x 2 questions
    assert {r["item_id"] for r in answers} == {"it0", "it1", "it2", "it3"}
    assert {r["qtype"] for r in answers} == {"probability", "choice"}
    prob = next(r for r in answers if r["question_id"] == "prob")
    assert prob["probability"] == 0.8 and prob["question_set"] == "t-p@v1"

    done = load_done(ctx.run_dir, QS.label)
    assert done == {"it0", "it1", "it2", "it3"}

    rows = read_rows(ledger)
    assert unresolved_pending(rows) == []
    final = [r for r in rows if r["cost_class"] == "calculated"]
    assert len(final) == 2
    assert all(r["pass"] == "t-p" for r in final)
    assert all(r["item_ids"] for r in final)
    assert ctx.guard.spent_usd == pytest.approx(2 * 300 * PRICE)


def test_packed_request_shape(tmp_path):
    seen = []
    ctx, client = make_ctx(tmp_path, [], items_per_call=2, seen=seen)
    run(ctx, items(2), QS, lp=tmp_path / "l.jsonl")
    client.close()
    body = json.loads(seen[0].content)
    assert body["state"] == {"i1": "text 0 mentions COBOL", "i2": "text 1 mentions COBOL"}
    assert set(body["questions"]) == {
        "i1_prob", "i1_kind", "i2_prob", "i2_kind",
    }
    assert body["questions"]["i1_prob"]["type"] == "noul"
    assert body["questions"]["i2_prob"]["type"] == "noul"


def test_zero_cap_refuses_before_transport(tmp_path):
    """account_total 0.00 semantics: reserve fails before any send."""
    seen = []
    ctx, client = make_ctx(tmp_path, [], cap_usd=0.0, seen=seen)
    out = run(ctx, items(4), QS, lp=tmp_path / "l.jsonl")
    client.close()
    assert out["stopped"] == "budget"
    assert seen == [], "a refused call must never reach the transport"
    assert read_rows(tmp_path / "l.jsonl") == []
    assert not (ctx.run_dir / "done.jsonl").exists()


def test_budget_stop_flushes_completed_packs(tmp_path):
    """A cap that fits exactly one packed call: pack 1 lands, pack 2 refused."""
    est = __import__("math").ceil(
        len(
            canonical_json(pack_body(items(2)[:2], QS, "jev-1.13.0")).encode()
        )
        / 3.2
    )
    cap = (300 + est - 1) * PRICE  # settles 300; second reserve of est fails
    seen = []
    ctx, client = make_ctx(tmp_path, [], cap_usd=cap, seen=seen)
    out = run(ctx, items(4), QS, lp=tmp_path / "l.jsonl")
    client.close()
    assert out["stopped"] == "budget"
    assert out["completed"] == 2 and out["failed"] == 0
    assert len(seen) == 1
    assert load_done(ctx.run_dir, QS.label) == {"it0", "it1"}
    assert len(read_answers(ctx.run_dir)) == 4


def test_resume_skips_done_items(tmp_path):
    ledger = tmp_path / "l.jsonl"
    ctx, client = make_ctx(tmp_path, [])
    run(ctx, items(4), QS, lp=ledger)
    client.close()

    seen = []
    ctx2, client2 = make_ctx(tmp_path, [], seen=seen)
    ctx2.run_id = "r-test-2"
    out = run(ctx2, items(4), QS, lp=ledger)
    client2.close()
    assert out["skipped_done"] == 4 and out["new_requests"] == 0
    assert seen == []
    # still exactly one part: no duplicate answers appended
    assert len(read_answers(ctx.run_dir)) == 8


def test_done_row_with_missing_part_is_redone(tmp_path):
    ledger = tmp_path / "l.jsonl"
    ctx, client = make_ctx(tmp_path, [])
    run(ctx, items(2), QS, lp=ledger)
    client.close()
    part = ctx.run_dir / "answers" / "part-1.parquet"
    part.unlink()

    seen = []
    ctx2, client2 = make_ctx(tmp_path, [], seen=seen)
    ctx2.run_id = "r-test-2"
    out = run(ctx2, items(2), QS, lp=ledger)
    client2.close()
    assert out["skipped_done"] == 0 and out["completed"] == 2
    assert len(seen) == 1


def test_crash_pending_reconciles_to_unknown(tmp_path):
    ledger = tmp_path / "l.jsonl"
    with Ledger(ledger) as led:
        row = {k: None for k in LEDGER_FIELDS}
        row.update(
            ts="2026-10-05T00:00:00Z",
            run_id="r-dead",
            **{"pass": "t-p"},
            logical_call_id="LC1",
            attempt=1,
            started_at="2026-10-05T00:00:00Z",
            cost_class="pending",
        )
        led.append(row, sync=True)

    ctx, client = make_ctx(tmp_path, [])
    out = run(ctx, items(2), QS, lp=ledger)
    client.close()
    assert out["completed"] == 2
    rows = read_rows(ledger)
    assert unresolved_pending(rows) == []
    unknown = [r for r in rows if r["cost_class"] == "unknown"]
    assert len(unknown) == 1 and unknown[0]["run_id"] == "r-dead"


def test_failed_call_counts_failed_not_done(tmp_path):
    ledger = tmp_path / "l.jsonl"
    ctx, client = make_ctx(tmp_path, ["422"] * 6)
    out = run(ctx, items(4), QS, lp=ledger)
    client.close()
    assert out["failed"] == 4 and out["completed"] == 0
    assert load_done(ctx.run_dir, QS.label) == set()
    rows = read_rows(ledger)
    assert unresolved_pending(rows) == []
    finals = [r for r in rows if r["cost_class"] != "pending"]
    assert all(r["cost_class"] == "calculated" for r in finals)


def test_manifest_refuses_a_different_model(tmp_path):
    ctx, client = make_ctx(tmp_path, [])
    run(ctx, items(2), QS, lp=tmp_path / "l.jsonl")
    client.close()
    ctx2, client2 = make_ctx(tmp_path, [])
    ctx2.model = "jev-2.0.0"
    with pytest.raises(Exception, match="model"):
        run(ctx2, items(2), QS, lp=tmp_path / "l.jsonl")
    client2.close()
