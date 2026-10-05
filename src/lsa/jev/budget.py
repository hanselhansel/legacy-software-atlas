"""Budget guard: reserve estimated cost before each send, settle after.

Ported from jev-opportunity-atlas ``inference.budget`` to the single cumulative
ledger at ``data/derived/jev_ledger.jsonl``. ``committed_usd = spent + unknown +
reserved`` can never pass the per-pass cap, and ``account_committed_usd`` (this
pass plus every other pass in the ledger) can never pass ``account_total``.
Unknown charges (timeouts, 5xx, null usage) settle at the worst case of
``max(worst_case_tokens_unknown, 2 * estimated_tokens)``; unresolved ``pending``
rows rebuild the same way from disk.

``for_pass`` takes one flock on the ledger file itself, so only one paid run
can be in flight at a time and no pair of runs can split a cap.
"""

from __future__ import annotations

import fcntl
import os
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Self

from lsa import paths
from lsa.jev.ledger import read_rows, unresolved_pending

LEDGER_NAME = "jev_ledger.jsonl"
DEFAULT_WORST_CASE_TOKENS = 4000


class BudgetExceeded(RuntimeError):
    pass


class BudgetLocked(RuntimeError):
    pass


def ledger_path(path: Path | None = None) -> Path:
    return Path(path) if path is not None else paths.DERIVED / LEDGER_NAME


def load_budgets(path: Path | None = None) -> dict:
    cfg_path = Path(path) if path is not None else paths.ROOT / "configs" / "budgets.toml"
    return tomllib.loads(cfg_path.read_text(encoding="utf-8"))


def pass_cap(cfg: dict, slug: str) -> float:
    """USD cap for a pass slug; a pass with no entry may not spend."""
    caps = cfg.get("caps") or {}
    return float(caps.get(slug, 0.0))


def worst_case_tokens(cfg: dict) -> int:
    return int(
        cfg.get(
            "worst_case_tokens_per_unknown_attempt", DEFAULT_WORST_CASE_TOKENS
        )
    )


def committed_by_pass(rows: list[dict], usd_per_token: float, worst: int) -> dict:
    """Committed USD per pass slug: calculated spend plus every unknown or
    unresolved-pending attempt at the flat worst case."""
    out: dict[str, float] = {}
    pending_ids = {
        (r.get("run_id"), r.get("logical_call_id"), r.get("attempt"))
        for r in unresolved_pending(rows)
    }
    for r in rows:
        cls = r.get("cost_class")
        key = (r.get("run_id"), r.get("logical_call_id"), r.get("attempt"))
        name = r.get("pass") or "<none>"
        if cls == "calculated" and r.get("cost_usd") is not None:
            out[name] = out.get(name, 0.0) + r["cost_usd"]
        elif cls == "unknown" or (cls == "pending" and key in pending_ids):
            out[name] = out.get(name, 0.0) + worst * usd_per_token
    return out


def headroom(
    cfg: dict,
    slug: str,
    usd_per_token: float,
    ledger: Path | None = None,
) -> dict:
    """Read-only committed/remaining USD for a pass and the whole account."""
    worst = worst_case_tokens(cfg)
    committed = committed_by_pass(read_rows(ledger_path(ledger)), usd_per_token, worst)
    cap = pass_cap(cfg, slug)
    mine = committed.get(slug, 0.0)
    total = cfg.get("account_total")
    account = sum(committed.values())
    return {
        "cap_usd": cap,
        "committed_usd": mine,
        "remaining_usd": cap - mine,
        "account_total_usd": total,
        "account_committed_usd": account,
        "account_remaining_usd": (
            total - account if total is not None else None
        ),
    }


@dataclass
class Reservation:
    """Open reservation returned by ``reserve`` and consumed by ``settle``."""

    est_tokens: int
    cost_usd: float


class BudgetGuard:
    def __init__(
        self,
        cap_usd: float,
        usd_per_input_token: float,
        worst_case_tokens_unknown: int,
        name: str | None = None,
        account_total: float | None = None,
        other_committed_usd: float = 0.0,
    ):
        self.cap_usd = cap_usd
        self.usd_per_input_token = usd_per_input_token
        self.worst_case_tokens_unknown = worst_case_tokens_unknown
        self.name = name
        self.account_total = account_total
        self.other_committed_usd = other_committed_usd
        self.spent_usd = 0.0
        self.unknown_usd = 0.0
        self.unknown_attempts = 0
        self.reserved_usd = 0.0
        self._lock_fd: int | None = None

    @property
    def committed_usd(self) -> float:
        return self.spent_usd + self.unknown_usd + self.reserved_usd

    @property
    def account_committed_usd(self) -> float:
        return self.other_committed_usd + self.committed_usd

    def reserve(self, est_tokens: int) -> Reservation:
        cost = est_tokens * self.usd_per_input_token
        if self.committed_usd + cost > self.cap_usd or (
            self.account_total is not None
            and self.account_committed_usd + cost > self.account_total
        ):
            total = (
                f"{self.account_total:.6f}"
                if self.account_total is not None
                else "none"
            )
            raise BudgetExceeded(
                f"pass cap for {self.name or '<unnamed>'!r}: "
                f"cap {self.cap_usd:.6f}, committed {self.committed_usd:.6f}, "
                f"account total {total}, "
                f"account committed {self.account_committed_usd:.6f}, "
                f"request {cost:.6f} would pass a cap"
            )
        self.reserved_usd += cost
        return Reservation(est_tokens=est_tokens, cost_usd=cost)

    def settle(
        self, handle: Reservation, actual_tokens: int | None, known: bool
    ) -> None:
        self.reserved_usd -= handle.cost_usd
        if known:
            self.spent_usd += (actual_tokens or 0) * self.usd_per_input_token
        else:
            self.unknown_attempts += 1
            self.unknown_usd += (
                max(self.worst_case_tokens_unknown, 2 * handle.est_tokens)
                * self.usd_per_input_token
            )

    @classmethod
    def for_pass(
        cls,
        slug: str,
        cap_usd: float,
        usd_per_input_token: float,
        worst_case_tokens_unknown: int,
        account_total: float | None = None,
        ledger: Path | None = None,
    ) -> BudgetGuard:
        """Guard for one pass, holding an exclusive flock on the ledger file
        and seeded with the ledger's committed spend for this pass and all
        others."""
        lp = ledger_path(ledger)
        if account_total is None:
            cfg = load_budgets()
            if "account_total" not in cfg:
                raise RuntimeError("account_total missing in configs/budgets.toml")
            account_total = cfg["account_total"]
        lp.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(lp, os.O_CREAT | os.O_RDWR, 0o644)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(fd)
            raise BudgetLocked(
                f"jev ledger {lp} is held by another run"
            ) from None
        rows = read_rows(lp)
        committed = committed_by_pass(
            rows, usd_per_input_token, worst_case_tokens_unknown
        )
        others = sum(v for k, v in committed.items() if k != slug)
        guard = cls(
            cap_usd,
            usd_per_input_token,
            worst_case_tokens_unknown,
            name=slug,
            account_total=account_total,
            other_committed_usd=others,
        )
        # Split this pass's committed total back into spent/unknown buckets:
        # each unknown or unresolved-pending row counts at the flat worst case,
        # matching committed_by_pass.
        pending = {
            (r.get("run_id"), r.get("logical_call_id"), r.get("attempt"))
            for r in unresolved_pending(rows)
        }
        for r in rows:
            if r.get("pass") != slug:
                continue
            cls_ = r.get("cost_class")
            key = (r.get("run_id"), r.get("logical_call_id"), r.get("attempt"))
            if cls_ == "calculated" and r.get("cost_usd") is not None:
                guard.spent_usd += r["cost_usd"]
            elif cls_ == "unknown" or (cls_ == "pending" and key in pending):
                guard.unknown_attempts += 1
                guard.unknown_usd += (
                    worst_case_tokens_unknown * usd_per_input_token
                )
        guard._lock_fd = fd
        return guard

    def close(self) -> None:
        fd, self._lock_fd = self._lock_fd, None
        if fd is not None:
            try:
                fcntl.flock(fd, fcntl.LOCK_UN)
            finally:
                os.close(fd)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc) -> bool:
        self.close()
        return False
