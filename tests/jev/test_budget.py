"""Budget guard: per-pass cap, account cap, cumulative ledger, lock."""

import json
import subprocess
import sys

import pytest

from lsa.jev.budget import (
    BudgetExceeded,
    BudgetGuard,
    BudgetLocked,
    committed_by_pass,
    headroom,
    load_budgets,
    pass_cap,
)
from lsa.jev.ledger import LEDGER_FIELDS, Ledger

PRICE = 0.042e-6
WORST = 4000


def ledger_row(**over):
    base = {k: None for k in LEDGER_FIELDS}
    base.update(
        ts="2026-10-05T00:00:00+00:00",
        run_id="r1",
        **{"pass": "other-pass"},
        logical_call_id="L1",
        attempt=1,
        cost_class="calculated",
        cost_usd=0.25,
        input_tokens=300,
    )
    base.update(over)
    return base


def test_reserve_settle_and_stop():
    g = BudgetGuard(
        cap_usd=0.001, usd_per_input_token=PRICE, worst_case_tokens_unknown=WORST
    )
    r = g.reserve(est_tokens=10_000)  # 0.00042
    g.settle(r, actual_tokens=9_000, known=True)
    assert g.spent_usd == pytest.approx(9_000 * PRICE)
    assert g.reserved_usd == 0
    with pytest.raises(BudgetExceeded):
        g.reserve(est_tokens=20_000)  # would pass the cap


def test_unknown_charges_count_at_worst_case():
    g = BudgetGuard(
        cap_usd=1.0, usd_per_input_token=PRICE, worst_case_tokens_unknown=WORST
    )
    r = g.reserve(est_tokens=500)
    g.settle(r, actual_tokens=None, known=False)
    assert g.unknown_attempts == 1
    assert g.committed_usd == pytest.approx(WORST * PRICE)


def test_retry_worst_case_uses_twice_estimate():
    g = BudgetGuard(
        cap_usd=1.0, usd_per_input_token=PRICE, worst_case_tokens_unknown=WORST
    )
    r = g.reserve(est_tokens=10_000)
    g.settle(r, actual_tokens=None, known=False)
    assert g.unknown_usd == pytest.approx(20_000 * PRICE)


def test_account_total_zero_refuses_first_call(tmp_path):
    """The gate state: account_total = 0.00 refuses any spend."""
    g = BudgetGuard.for_pass(
        "tenders-which-category",
        cap_usd=0.0,
        usd_per_input_token=PRICE,
        worst_case_tokens_unknown=WORST,
        account_total=0.0,
        ledger=tmp_path / "jev_ledger.jsonl",
    )
    try:
        with pytest.raises(BudgetExceeded, match="would pass a cap"):
            g.reserve(est_tokens=1)
    finally:
        g.close()


def test_account_cap_counts_other_passes(tmp_path):
    ledger = tmp_path / "jev_ledger.jsonl"
    with Ledger(ledger) as led:
        led.append(ledger_row(**{"pass": "other-pass"}, cost_usd=0.0009))
    g = BudgetGuard.for_pass(
        "my-pass",
        cap_usd=6.5,
        usd_per_input_token=PRICE,
        worst_case_tokens_unknown=WORST,
        account_total=0.001,
        ledger=ledger,
    )
    try:
        assert g.other_committed_usd == pytest.approx(0.0009)
        assert g.account_committed_usd == pytest.approx(0.0009)
        g.reserve(est_tokens=1000)  # 0.000042 fits under 0.001
        with pytest.raises(BudgetExceeded):
            g.reserve(est_tokens=2000)  # would pass the account cap
    finally:
        g.close()


def test_own_pass_spend_is_cumulative_across_runs(tmp_path):
    ledger = tmp_path / "jev_ledger.jsonl"
    with Ledger(ledger) as led:
        led.append(
            ledger_row(run_id="r1", **{"pass": "my-pass"}, cost_usd=0.25)
        )
        led.append(
            ledger_row(
                run_id="r2", logical_call_id="L9", **{"pass": "my-pass"},
                cost_usd=0.10,
            )
        )
        led.append(ledger_row(**{"pass": "other-pass"}, cost_usd=9.99))
    g = BudgetGuard.for_pass(
        "my-pass",
        cap_usd=1.0,
        usd_per_input_token=PRICE,
        worst_case_tokens_unknown=WORST,
        account_total=25.0,
        ledger=ledger,
    )
    try:
        assert g.spent_usd == pytest.approx(0.35)
        assert g.other_committed_usd == pytest.approx(9.99)
    finally:
        g.close()


def test_unresolved_pending_counts_at_worst_case(tmp_path):
    ledger = tmp_path / "jev_ledger.jsonl"
    with Ledger(ledger) as led:
        led.append(
            ledger_row(cost_class="pending", cost_usd=None, ended_at=None)
        )
    g = BudgetGuard.for_pass(
        "other-pass",
        cap_usd=1.0,
        usd_per_input_token=PRICE,
        worst_case_tokens_unknown=WORST,
        account_total=25.0,
        ledger=ledger,
    )
    try:
        assert g.unknown_attempts == 1
        assert g.committed_usd == pytest.approx(WORST * PRICE)
    finally:
        g.close()


def test_second_guard_is_locked_out(tmp_path):
    ledger = tmp_path / "jev_ledger.jsonl"
    g = BudgetGuard.for_pass(
        "p1",
        cap_usd=1.0,
        usd_per_input_token=PRICE,
        worst_case_tokens_unknown=WORST,
        account_total=25.0,
        ledger=ledger,
    )
    try:
        with pytest.raises(BudgetLocked):
            BudgetGuard.for_pass(
                "p2",
                cap_usd=1.0,
                usd_per_input_token=PRICE,
                worst_case_tokens_unknown=WORST,
                account_total=25.0,
                ledger=ledger,
            )
        # another process cannot take the lock either
        script = (
            "import fcntl, sys\n"
            f"fh = open({str(ledger)!r}, 'a')\n"
            "try:\n"
            "    fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)\n"
            "except BlockingIOError:\n"
            "    sys.exit(1)\n"
            "sys.exit(0)\n"
        )
        assert subprocess.run(
            [sys.executable, "-c", script], check=False
        ).returncode == 1
    finally:
        g.close()
    # after close, the lock is free
    assert subprocess.run(
        [sys.executable, "-c", script], check=False
    ).returncode == 0


def test_pass_cap_defaults_to_zero_when_missing():
    assert pass_cap({"account_total": 8.0}, "no-such-pass") == 0.0
    assert pass_cap({"caps": {"p": 0.5}, "account_total": 8.0}, "p") == 0.5


def test_headroom_reports_per_pass_and_account(tmp_path):
    ledger = tmp_path / "jev_ledger.jsonl"
    with Ledger(ledger) as led:
        led.append(ledger_row(**{"pass": "a"}, cost_usd=0.20))
        led.append(
            ledger_row(
                **{"pass": "b"}, logical_call_id="L2", cost_usd=0.10
            )
        )
    cfg = {"account_total": 8.0, "caps": {"a": 1.0, "b": 2.0}}
    head = headroom(cfg, "a", PRICE, ledger)
    assert head["cap_usd"] == 1.0
    assert head["committed_usd"] == pytest.approx(0.20)
    assert head["remaining_usd"] == pytest.approx(0.80)
    assert head["account_committed_usd"] == pytest.approx(0.30)
    assert head["account_remaining_usd"] == pytest.approx(7.70)


def test_committed_by_pass_counts_unknown_and_pending():
    rows = [
        ledger_row(**{"pass": "a"}, cost_usd=0.5),
        ledger_row(
            **{"pass": "a"}, logical_call_id="L2", cost_class="unknown",
            cost_usd=None,
        ),
        ledger_row(
            **{"pass": "b"}, logical_call_id="L3", cost_class="pending",
            cost_usd=None, ended_at=None,
        ),
    ]
    out = committed_by_pass(rows, PRICE, WORST)
    assert out["a"] == pytest.approx(0.5 + WORST * PRICE)
    assert out["b"] == pytest.approx(WORST * PRICE)


def test_repo_budgets_config_refuses_everything():
    """configs/budgets.toml as committed: account_total 0.00, all caps 0.00."""
    from lsa import paths

    cfg = load_budgets()
    assert cfg["account_total"] == 0.0
    assert cfg["worst_case_tokens_per_unknown_attempt"] > 0
    assert set(cfg["caps"]) and all(v == 0.0 for v in cfg["caps"].values())
    assert paths.ROOT  # silence unused import lint
