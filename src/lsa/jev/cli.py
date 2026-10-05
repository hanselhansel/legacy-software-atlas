"""``lsa jev`` commands: ``pilot`` and ``run`` over one configured pass.

Both commands print a run estimate first. ``--yes`` arms dispatch; without it
the estimate prints and nothing is sent. Dispatch takes the ledger flock, so
one paid run at a time, and the budget guard refuses any call that would pass
the per-pass cap or ``account_total``. With the committed ``account_total =
0.00`` every dispatch attempt is refused before transport.
"""

from __future__ import annotations

import tomllib
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from lsa import paths
from lsa.estimate import load_passes
from lsa.jev import estimate as jest
from lsa.jev.budget import (
    BudgetGuard,
    BudgetLocked,
    load_budgets,
    pass_cap,
    worst_case_tokens,
)
from lsa.jev.items import load_items
from lsa.jev.questions import question_set, slugify
from lsa.jev.runner import RunContext, run
from lsa.jev.state import load_done, run_dir

DEFAULT_MODEL = "jev-1.13.0"


class PassUnknown(RuntimeError):
    pass


def _resolve_pass(passes, name: str):
    """Pass row matching a full pass name or its slug."""
    for p in passes:
        if p.name == name or slugify(p.name) == name:
            return p
    raise PassUnknown(
        f"unknown pass {name!r} (have: "
        + ", ".join(sorted(slugify(p.name) for p in passes))
        + ")"
    )


def _price(prices_path: Path, model: str) -> tuple[float, str]:
    """(usd per input token, price version) for ``model``."""
    data = tomllib.loads(Path(prices_path).read_text(encoding="utf-8"))
    for row in data.get("price", []):
        if row.get("model") == model:
            return float(row["input_usd_per_million"]) / 1e6, str(
                row.get("version", "")
            )
    raise ValueError(f"no price row for model {model!r} in {prices_path}")


def _new_run_id() -> str:
    return f"{datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')}-{uuid4().hex[:8]}"


def _dir_slug(args, slug: str) -> str:
    """Pilot labels live in a side dir so they never satisfy the main pass."""
    return slug if args.cmd == "run" else f"{slug}-pilot"


def _pending(args, qs, items) -> tuple[list[dict], int]:
    """(pending items, done count) for this question set in the run dir."""
    dir_ = run_dir(_dir_slug(args, qs.slug), args.runs)
    done = load_done(dir_, qs.label)
    pending = [i for i in items if str(i["item_id"]) not in done]
    return pending, len(items) - len(pending)


def _dispatch(args, p, qs, budgets, usd_per_token, price_version, items) -> None:
    slug = qs.slug
    cap = pass_cap(budgets, slug)
    guard = BudgetGuard.for_pass(
        slug,
        cap,
        usd_per_token,
        worst_case_tokens(budgets),
        account_total=budgets.get("account_total"),
        ledger=args.ledger,
    )
    try:
        client = args._client
        if client is None:
            from lsa.jev.client import JevClient
            from lsa.jev.keys import base_url, get_api_key

            client = JevClient(get_api_key(), base_url())
        ctx = RunContext(
            run_id=_new_run_id(),
            client=client,
            guard=guard,
            model=args.model,
            price_version=price_version,
            run_dir=run_dir(_dir_slug(args, slug), args.runs),
            items_per_call=p.items_per_call,
        )
        out = run(ctx, items, qs, lp=args.ledger)
    finally:
        if client is not None:
            client.close()
        guard.close()
    print(
        f"run {out['stopped'] or 'done'}: {out['completed']} completed, "
        f"{out['failed']} failed, {out['skipped_done']} already done, "
        f"{out['new_requests']} requests in {out['wall_s']:.1f}s"
    )
    if out["stopped"] == "budget":
        raise SystemExit(1)


def _jev(args, *, items=None, client=None) -> None:
    p = _resolve_pass(load_passes(args.passes), args.pass_name)
    qs = question_set(p.name, args.questions)
    budgets = load_budgets(args.budgets)
    usd_per_token, price_version = _price(args.prices, args.model)
    if items is None:
        items = load_items(p.family, args.items, args.raw)
    pending, done_n = _pending(args, qs, items)
    limit = getattr(args, "n", None)
    est = jest.estimate_run(
        p,
        qs.slug,
        len(pending),
        done_n,
        budgets,
        usd_per_token,
        limit=limit if args.cmd == "pilot" else None,
        ledger=args.ledger,
    )
    print(jest.format_run_estimate(est))
    if not args.yes:
        print("dry run: add --yes to dispatch")
        return
    if not est.affordable:
        raise SystemExit(1)
    if est.items_selected == 0:
        print("nothing pending; nothing to dispatch")
        return
    args._client = client
    selected = pending[: est.items_selected]
    try:
        _dispatch(args, p, qs, budgets, usd_per_token, price_version, selected)
    except BudgetLocked as exc:
        raise SystemExit(str(exc)) from exc


def register(sub) -> None:
    p_jev = sub.add_parser("jev", help="Jev labeling passes")
    jsub = p_jev.add_subparsers(dest="jev_cmd", required=True)

    def shared(p, need_yes_help):
        p.add_argument("--pass", dest="pass_name", required=True)
        p.add_argument("--model", default=DEFAULT_MODEL)
        p.add_argument("--passes", type=Path, default=paths.ROOT / "configs" / "passes.toml")
        p.add_argument("--questions", type=Path, default=paths.ROOT / "configs" / "questions.toml")
        p.add_argument("--prices", type=Path, default=paths.ROOT / "configs" / "prices.toml")
        p.add_argument("--budgets", type=Path, default=paths.ROOT / "configs" / "budgets.toml")
        p.add_argument("--items", type=Path, default=paths.DERIVED / "items.parquet")
        p.add_argument("--raw", type=Path, default=paths.RAW)
        p.add_argument("--ledger", type=Path, default=None, help="ledger path (default data/derived/jev_ledger.jsonl)")
        p.add_argument("--runs", type=Path, default=None, help="run dir root (default data/derived/jev)")
        p.add_argument("--yes", action="store_true", help=need_yes_help)

    p_pilot = jsub.add_parser(
        "pilot", help="estimate then label N pending items into the pilot dir"
    )
    shared(p_pilot, "dispatch the pilot (default: print estimate only)")
    p_pilot.add_argument("--n", type=int, default=200)
    p_pilot.set_defaults(func=_jev, cmd="pilot")

    p_run = jsub.add_parser(
        "run", help="estimate then label all pending items of a pass"
    )
    shared(p_run, "dispatch the run (default: print estimate only)")
    p_run.set_defaults(func=_jev, cmd="run")
