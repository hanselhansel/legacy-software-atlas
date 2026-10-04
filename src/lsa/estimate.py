"""Pre-gate Jev cost estimate from counted items (plan 1, task 4).

Each ``[[pass]]`` in ``configs/passes.toml`` covers one count family. Free rule
and keyword prefilters run first and keep ``prefilter_keep`` of the counted
items; the rest go to Jev packed ``items_per_call`` to a call. Token cost is
``tokens_per_item`` measured on a real sample where available, else the stated
``default_tokens_per_item`` fallback flagged by ``tokens_measured=False``, the
same measured-or-stated-default pattern the HN study used before its
calibration runs (spec section 7).
"""

from __future__ import annotations

import math
import tomllib
from dataclasses import dataclass
from pathlib import Path

from lsa.contracts import CountRecord


@dataclass(frozen=True)
class Pass:
    name: str
    family: str
    prefilter_keep: float
    tokens_per_item: int | None
    items_per_call: int = 5
    overhead_tokens_per_call: int = 120

    def __post_init__(self) -> None:
        if not 0.0 < self.prefilter_keep <= 1.0:
            raise ValueError("prefilter_keep must lie in (0, 1]")
        if self.tokens_per_item is not None and self.tokens_per_item <= 0:
            raise ValueError("tokens_per_item must be a positive int or None")
        if self.items_per_call < 1:
            raise ValueError("items_per_call must be >= 1")
        if self.overhead_tokens_per_call < 0:
            raise ValueError("overhead_tokens_per_call must be >= 0")


@dataclass(frozen=True)
class PassEstimate:
    name: str
    items_counted: int
    items_sent: int
    calls: int
    input_tokens: int
    usd: float
    tokens_measured: bool


@dataclass(frozen=True)
class Estimate:
    passes: tuple[PassEstimate, ...]
    total_usd: float
    target_usd: float
    within_target: bool
    uncounted_sources: tuple[str, ...]


def load_passes(path: Path) -> list[Pass]:
    """Passes from a ``configs/passes.toml`` file (array of ``[[pass]]``)."""
    data = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    return [Pass(**{"tokens_per_item": None, **row}) for row in data.get("pass", [])]


def read_counts(path: Path) -> list[CountRecord]:
    """CountRecord rows from a counts parquet written by the collectors."""
    import pyarrow.parquet as pq

    return [CountRecord(**row) for row in pq.read_table(Path(path)).to_pylist()]


def input_price(prices_path: Path, model: str = "jev-1.13.0") -> float:
    """USD per million input tokens for `model` from a prices.toml file."""
    data = tomllib.loads(Path(prices_path).read_text(encoding="utf-8"))
    for row in data.get("price", []):
        if row.get("model") == model:
            return float(row["input_usd_per_million"])
    raise ValueError(f"no price row for model {model!r} in {prices_path}")


def estimate(
    counts: list[CountRecord],
    passes: list[Pass],
    price_usd_per_million: float,
    target_usd: float = 25.0,
    default_tokens_per_item: int = 400,
) -> Estimate:
    """Per-pass cost estimate plus the total against `target_usd`.

    A count of None means the source returned no total; its items are not
    counted (never as zero) and its source is reported in uncounted_sources.
    """
    uncounted: set[str] = set()
    out = []
    for p in passes:
        items_counted = 0
        for rec in counts:
            if rec.family != p.family:
                continue
            if rec.count is None:
                uncounted.add(rec.source)
            else:
                items_counted += rec.count
        items_sent = math.ceil(items_counted * p.prefilter_keep)
        calls = math.ceil(items_sent / p.items_per_call)
        measured = p.tokens_per_item is not None
        per_item = p.tokens_per_item if measured else default_tokens_per_item
        input_tokens = items_sent * per_item + calls * p.overhead_tokens_per_call
        out.append(
            PassEstimate(
                name=p.name,
                items_counted=items_counted,
                items_sent=items_sent,
                calls=calls,
                input_tokens=input_tokens,
                usd=input_tokens / 1e6 * price_usd_per_million,
                tokens_measured=measured,
            )
        )
    total = sum(pe.usd for pe in out)
    return Estimate(
        passes=tuple(out),
        total_usd=total,
        target_usd=target_usd,
        within_target=total <= target_usd,
        uncounted_sources=tuple(sorted(uncounted)),
    )


def format_table(est: Estimate) -> str:
    """One line per pass, then the total against the target."""
    lines = [
        (
            f"{'pass':<14}{'items':>8}{'sent':>8}{'calls':>7}{'tokens':>10}"
            f"{'usd':>10}  measured"
        )
    ]
    for p in est.passes:
        lines.append(
            f"{p.name:<14}{p.items_counted:>8}{p.items_sent:>8}{p.calls:>7}"
            f"{p.input_tokens:>10}{p.usd:>10.6f}  "
            f"{'yes' if p.tokens_measured else 'no'}"
        )
    status = "within target" if est.within_target else "OVER TARGET"
    lines.append(
        f"total ${est.total_usd:.6f} vs target ${est.target_usd:.2f}: {status}"
    )
    if est.uncounted_sources:
        lines.append(
            "uncounted sources (no total returned): "
            + ", ".join(est.uncounted_sources)
        )
    return "\n".join(lines)
