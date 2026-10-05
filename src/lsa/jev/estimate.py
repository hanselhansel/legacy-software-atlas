"""Run-level cost estimate, printed before every paid dispatch.

Distinct from ``lsa.estimate`` (the pre-Jev gate): this estimates one actual
run of one pass over the pending item set, on the same token basis as the gate
(``tokens_per_item`` plus per-call overhead), then compares against the pass
cap and ``account_total`` headroom in ``configs/budgets.toml``.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

from lsa.jev.budget import headroom, ledger_path


@dataclass(frozen=True)
class RunEstimate:
    pass_name: str
    slug: str
    items_pending: int
    items_done: int
    items_selected: int
    calls: int
    est_input_tokens: int
    est_usd: float
    cap_usd: float
    committed_usd: float
    remaining_usd: float
    account_total_usd: float | None
    account_committed_usd: float
    account_remaining_usd: float | None
    affordable: bool


def estimate_run(
    pass_cfg,
    slug: str,
    items_pending: int,
    items_done: int,
    budgets: dict,
    usd_per_token: float,
    limit: int | None = None,
    ledger: Path | None = None,
) -> RunEstimate:
    """Estimated cost to label up to ``limit`` pending items of one pass."""
    selected = items_pending if limit is None else min(limit, items_pending)
    calls = math.ceil(selected / pass_cfg.items_per_call) if selected else 0
    tokens = (
        selected * (pass_cfg.tokens_per_item or 0)
        + calls * pass_cfg.overhead_tokens_per_call
    )
    usd = tokens * usd_per_token
    head = headroom(budgets, slug, usd_per_token, ledger_path(ledger))
    within_pass = usd <= head["remaining_usd"]
    within_account = (
        head["account_remaining_usd"] is None
        or usd <= head["account_remaining_usd"]
    )
    return RunEstimate(
        pass_name=pass_cfg.name,
        slug=slug,
        items_pending=items_pending,
        items_done=items_done,
        items_selected=selected,
        calls=calls,
        est_input_tokens=tokens,
        est_usd=usd,
        cap_usd=head["cap_usd"],
        committed_usd=head["committed_usd"],
        remaining_usd=head["remaining_usd"],
        account_total_usd=head["account_total_usd"],
        account_committed_usd=head["account_committed_usd"],
        account_remaining_usd=head["account_remaining_usd"],
        affordable=within_pass and within_account,
    )


def format_run_estimate(est: RunEstimate) -> str:
    """Human-readable pre-run estimate block."""
    account_total = (
        f"${est.account_total_usd:.2f}"
        if est.account_total_usd is not None
        else "uncapped"
    )
    account_remaining = (
        f"${est.account_remaining_usd:.6f}"
        if est.account_remaining_usd is not None
        else "uncapped"
    )
    verdict = "affordable" if est.affordable else "OVER BUDGET: refusing to run"
    return "\n".join(
        [
            f"pass:     {est.pass_name}",
            (
                f"pending:  {est.items_pending} items "
                f"({est.items_done} done, {est.items_selected} selected)"
            ),
            f"calls:    {est.calls} packed calls",
            f"tokens:   {est.est_input_tokens} input (est)",
            f"cost:     ${est.est_usd:.6f} (est)",
            (
                f"pass cap: ${est.cap_usd:.6f} "
                f"(committed ${est.committed_usd:.6f}, "
                f"remaining ${est.remaining_usd:.6f})"
            ),
            (
                f"account:  {account_total} total "
                f"(committed ${est.account_committed_usd:.6f}, "
                f"remaining {account_remaining})"
            ),
            f"verdict:  {verdict}",
        ]
    )
