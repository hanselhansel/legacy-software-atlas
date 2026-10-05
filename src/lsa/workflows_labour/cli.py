"""``lsa workflows-labour`` (plan 3, lane N): workflow labour pools.

Reads ``research/workflows.csv`` + ``research/workflow_occupations.csv``,
downloads O*NET task statements, BLS OEWS wages (public API v2) and the
Anthropic Economic Index task-usage file into ``data/raw/``, and writes
``data/derived/workflows.parquet``: labour value, employment share sum
and AI usage per workflow, region US. ``--refresh`` re-downloads the
cached sources. Each download is timeboxed at two minutes; a source that
fails is noted in the ``notes`` column and the run continues.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from lsa import paths


def _workflows_labour(args: argparse.Namespace) -> None:
    from lsa.workflows_labour import labour, onet

    if not args.workflows.exists():
        raise SystemExit(f"workflows csv not found: {args.workflows}")
    if not args.occupations.exists():
        raise SystemExit(f"occupations csv not found: {args.occupations}")
    raw_dir = args.raw_dir or paths.RAW
    if args.dry_run:
        workflows = labour.load_workflows(args.workflows)
        occs = labour.load_occupations(args.occupations)
        tasks = sum(
            1
            for r in occs
            for _ in onet.split_tasks(r.get("onet_tasks") or "")
        )
        print(
            f"dry run: {len(workflows)} workflows, {len(occs)} occupation "
            f"rows, {tasks} task texts; nothing written"
        )
        return
    out = args.out or paths.DERIVED / "workflows.parquet"
    rows = labour.run(
        workflows_path=args.workflows,
        occ_path=args.occupations,
        out_path=out,
        raw_dir=raw_dir,
        onet_path=args.onet,
        oews_cache=args.oews_cache,
        aiuse_path=args.aiuse,
        refresh=args.refresh,
        log=print,
    )
    print(f"wrote {len(rows)} workflow rows to {out}")
    ranked = sorted(
        (r for r in rows if r["labour_value_usd"] is not None),
        key=lambda r: -r["labour_value_usd"],
    )
    for r in ranked[:10]:
        print(
            f"{r['labour_value_usd'] / 1e9:>8.1f}B  {r['category']:<28} "
            f"{r['workflow_id']}"
        )


def register(sub) -> None:
    p = sub.add_parser(
        "workflows-labour",
        help="workflow labour pools: OEWS value + AEI usage (lane N)",
    )
    p.add_argument(
        "--workflows",
        type=Path,
        default=paths.RESEARCH / "workflows.csv",
        help="category,workflow_id,workflow,description,touches_core csv",
    )
    p.add_argument(
        "--occupations",
        type=Path,
        default=paths.RESEARCH / "workflow_occupations.csv",
        help="workflow_id,soc_code,title,time_share,onet_tasks csv",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=None,
        help="output parquet (default: data/derived/workflows.parquet)",
    )
    p.add_argument(
        "--raw-dir",
        type=Path,
        default=None,
        help="raw download root (default: data/raw)",
    )
    p.add_argument(
        "--onet",
        type=Path,
        default=None,
        help="local task_statements csv; skips the O*NET download",
    )
    p.add_argument(
        "--oews-cache",
        type=Path,
        default=None,
        help="oews api cache json (default: data/raw/oews/api.json)",
    )
    p.add_argument(
        "--aiuse",
        type=Path,
        default=None,
        help="local usage csv; skips the Hugging Face download",
    )
    p.add_argument(
        "--refresh",
        action="store_true",
        help="re-download cached source files",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="count inputs; no fetch, no writes",
    )
    p.set_defaults(func=_workflows_labour)
