"""lsa jev pilot/run: estimate first, --yes gate, zero-account refusal."""

import json
from pathlib import Path

import pytest

from lsa.cli import build_parser
from lsa.jev.cli import _jev
from lsa.jev.client import CANARY_PREFIX, JevClient, RetryPolicy
from lsa.jev.state import load_done, run_dir
from tests.jev.mock_jev import make_transport

CANARY = CANARY_PREFIX + "f" * 64
ROOT = Path(__file__).resolve().parents[2]

PASS = "HN: firsthand pain and reason to stay"
SLUG = "hn-firsthand-pain-and-reason-to-stay"

ITEMS = [
    {"item_id": f"h{i}", "text": f"we still run the thing, comment {i}"}
    for i in range(5)
]


def args_for(tmp_path, *argv):
    parser = build_parser()
    return parser.parse_args(
        [
            *argv,
            "--budgets",
            str(tmp_path / "budgets.toml"),
            "--ledger",
            str(tmp_path / "jev_ledger.jsonl"),
            "--runs",
            str(tmp_path / "jev"),
        ]
    )


def budgets_file(tmp_path, account_total=0.0, cap=0.0) -> Path:
    path = tmp_path / "budgets.toml"
    path.write_text(
        f"account_total = {account_total}\n"
        f"worst_case_tokens_per_unknown_attempt = 4000\n"
        f'[caps]\n"{SLUG}" = {cap}\n',
        encoding="utf-8",
    )
    return path


def client(seen=None, script=None):
    return JevClient(
        api_key=CANARY,
        base="http://mock",
        transport=make_transport(script or [], seen),
        policy=RetryPolicy(max_attempts=3, backoff_initial=0, backoff_max=0),
    )


def test_run_prints_estimate_and_refuses_zero_budget(tmp_path, capsys):
    budgets_file(tmp_path)
    args = args_for(tmp_path, "jev", "run", "--pass", PASS, "--yes")
    with pytest.raises(SystemExit) as exc:
        _jev(args, items=ITEMS, client=client())
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert f"pass:     {PASS}" in out
    assert "pending:  5 items" in out
    assert "verdict:  OVER BUDGET: refusing to run" in out


def test_run_without_yes_prints_estimate_only(tmp_path, capsys):
    budgets_file(tmp_path, account_total=25.0, cap=1.0)
    args = args_for(tmp_path, "jev", "run", "--pass", PASS)
    _jev(args, items=ITEMS, client=client())
    out = capsys.readouterr().out
    assert "verdict:  affordable" in out
    assert "dry run: add --yes to dispatch" in out
    # nothing written: no ledger, no run dir
    assert not (tmp_path / "jev_ledger.jsonl").exists()
    assert not (tmp_path / "jev").exists()


def test_dispatch_spends_once_budget_allows(tmp_path, capsys):
    budgets_file(tmp_path, account_total=25.0, cap=1.0)
    args = args_for(tmp_path, "jev", "run", "--pass", PASS, "--yes")
    seen = []
    c = client(seen)
    _jev(args, items=ITEMS, client=c)
    out = capsys.readouterr().out
    assert "verdict:  affordable" in out
    assert "run done: 5 completed" in out
    assert len(seen) == 1  # 5 items, one packed call (k=5)
    dir_ = run_dir(SLUG, tmp_path / "jev")
    assert load_done(dir_, "hn-firsthand-pain-and-reason-to-stay@v1") == {
        i["item_id"] for i in ITEMS
    }
    ledger = tmp_path / "jev_ledger.jsonl"
    rows = [
        json.loads(line) for line in ledger.read_text().splitlines() if line
    ]
    assert any(r["cost_class"] == "calculated" for r in rows)


def test_pass_name_resolves_by_slug(tmp_path, capsys):
    budgets_file(tmp_path, account_total=25.0, cap=1.0)
    args = args_for(tmp_path, "jev", "run", "--pass", SLUG)
    _jev(args, items=ITEMS, client=client())
    assert f"pass:     {PASS}" in capsys.readouterr().out


def test_unknown_pass_lists_valid_choices(tmp_path):
    budgets_file(tmp_path)
    args = args_for(tmp_path, "jev", "run", "--pass", "nope")
    with pytest.raises(Exception, match="unknown pass"):
        _jev(args, items=ITEMS, client=client())


def test_pilot_caps_items_and_uses_pilot_dir(tmp_path, capsys):
    budgets_file(tmp_path, account_total=25.0, cap=1.0)
    args = args_for(tmp_path, "jev", "pilot", "--pass", PASS, "--n", "2", "--yes")
    seen = []
    _jev(args, items=ITEMS, client=client(seen))
    out = capsys.readouterr().out
    assert "pending:  5 items (0 done, 2 selected)" in out
    assert "run done: 2 completed" in out
    assert len(seen) == 1
    # pilot answers land under <slug>-pilot, never the main pass dir
    pilot_done = load_done(
        run_dir(f"{SLUG}-pilot", tmp_path / "jev"),
        "hn-firsthand-pain-and-reason-to-stay@v1",
    )
    assert pilot_done == {"h0", "h1"}
    assert not (tmp_path / "jev" / SLUG).exists()


def test_pilot_dry_run_is_default(tmp_path, capsys):
    budgets_file(tmp_path, account_total=25.0, cap=1.0)
    args = args_for(tmp_path, "jev", "pilot", "--pass", PASS, "--n", "2")
    seen = []
    _jev(args, items=ITEMS, client=client(seen))
    assert "dry run" in capsys.readouterr().out
    assert seen == []
