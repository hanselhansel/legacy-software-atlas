"""Build the site export JSON files (plan 2, task 6).

``lsa export`` loads the kept categories, desk research, sign regrades,
labelled items and the score inputs once, then writes:

- ``exports/site/categories.json``: one object per kept category with name,
  systems, signs (grade, why, source), estimates per region and segment,
  the five score parts with their evidence links, the market block
  (possible buyers and value) and the build-vs-buy lens, reasons to stay,
  and the challenger list.
- ``exports/site/scores.json``: the same score blocks plus totals, sorted
  by total descending so the site can rank categories.
- ``exports/site/regions.json``: every study region x kept category with
  possible buyers, market value, the usage estimate when one exists and an
  evidence level, plus a per-region summary.

Missing per-category TOML files under ``configs/categories/`` are generated
with the documented defaults first; existing files are read, never
rewritten.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from lsa import (
    catconfig,
    criticality,
    estimates,
    labels,
    market,
    measures,
    paths,
    score_inputs,
    scores,
    topdown,
)

DESK = "desk-research-2026-10-05.json"
REGRADE = "regrade-2026-10-05.json"


def load_categories(path: Path | None = None) -> list[dict]:
    """``research/categories.csv`` rows marked ``kept``."""
    p = Path(path or paths.RESEARCH / "categories.csv")
    with open(p, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("kept") == "True"]


def load_desk(path: Path | None = None) -> dict[str, dict]:
    """``{slug: desk research category object}``."""
    p = Path(path or paths.RESEARCH / "raw" / DESK)
    data = json.loads(Path(p).read_text(encoding="utf-8"))
    return {c["slug"]: c for c in data["categories"]}


def load_regrade(path: Path | None = None) -> dict[str, dict]:
    """``{slug: {s1..s4: {grade, why, source}}}``."""
    p = Path(path or paths.RESEARCH / "raw" / REGRADE)
    rows = json.loads(Path(p).read_text(encoding="utf-8"))
    return {r["slug"]: r for r in rows}


def load_challengers(path: Path | None = None) -> dict[str, list[dict]]:
    """``{slug: [challenger rows]}`` from research/challengers.csv."""
    p = Path(path or paths.RESEARCH / "challengers.csv")
    if not Path(p).exists():
        return {}
    out: dict[str, list[dict]] = {}
    with open(p, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out.setdefault(row["category"], []).append(row)
    return out


def _sign_block(regrade_row: dict | None, cat_row: dict) -> dict:
    """s1..s4 with grade, why and source; grades fall back to the csv."""
    signs = {}
    for key in ("s1", "s2", "s3", "s4"):
        entry = (regrade_row or {}).get(key) or {}
        signs[key] = {
            "grade": entry.get("grade", cat_row.get(key, "not_met")),
            "why": entry.get("why", ""),
            "source": entry.get("source", ""),
        }
    return signs


def _slice_json(s: estimates.SliceEstimate) -> dict:
    return {
        "companies_low": s.companies_low,
        "companies_high": s.companies_high,
        "grade": s.grade,
        "families": list(s.families),
        "notes": list(s.notes),
        "sources": list(s.sources),
    }


def _score_json(score: scores.CategoryScore) -> dict:
    return {
        "slug": score.slug,
        "total": score.total,
        "total_raw": score.total_raw,
        "flags": list(score.flags),
        "parts": {
            name: {
                "score": part.score,
                "detail": part.detail,
                "evidence": list(part.evidence),
            }
            for name, part in score.parts.items()
        },
    }


def build_category(
    cat_row: dict,
    desk: dict | None,
    regrade_row: dict | None,
    estimate: estimates.CategoryEstimate,
    score: scores.CategoryScore,
    challengers: list[dict],
    mv: market.MarketValue | None = None,
) -> dict:
    """The site object for one kept category."""
    slug = cat_row["slug"]
    desk = desk or {}
    chal = [
        {
            "company": c.get("company", ""),
            "founded": c.get("founded", ""),
            "hq": c.get("hq", ""),
            "funding_usd": c.get("funding_usd", ""),
            "strategy": c.get("strategy", ""),
            "traction": c.get("traction", ""),
            "source": c.get("source", ""),
        }
        for c in challengers
    ]
    return {
        "slug": slug,
        "name": cat_row.get("name") or desk.get("name", slug),
        "systems": desk.get("systems", []),
        "reason": cat_row.get("reason", ""),
        "differentiator": cat_row.get("differentiator", ""),
        "signs": _sign_block(regrade_row, cat_row),
        "reasons_to_stay": desk.get("reasons_to_stay", []),
        "regions": sorted(estimate.regions),
        "segments": sorted(estimate.segments),
        "estimates": {
            "regions": {
                k: _slice_json(v) for k, v in estimate.regions.items()
            },
            "segments": {
                k: _slice_json(v) for k, v in estimate.segments.items()
            },
            "notes": list(estimate.notes),
        },
        "scores": _score_json(score),
        "market": market.market_json(mv) if mv is not None else None,
        "build_vs_buy": market.lens_json(mv) if mv is not None else None,
        "challengers": chal,
    }


def _score_inputs(
    estimate: estimates.CategoryEstimate,
    tasks: list[dict],
    ai_answers: dict[str, dict],
    ai_pass_present: bool,
    sub_scores: dict[str, list[measures.SubScore]],
    mv: market.MarketValue | None = None,
) -> score_inputs.ScoreInputs:
    """Assemble everything ``score_category`` consumes for one slug."""
    universe_mid = mv.buyers_mid if mv and mv.buyers_mid else None
    return score_inputs.ScoreInputs(
        estimate=estimate,
        tasks=tasks,
        ai_answers=ai_answers,
        ai_pass_present=ai_pass_present,
        universe_mid=universe_mid,
        market=mv,
        measures=sub_scores,
    )


def _measure_data(
    cats: list[dict],
    regrade: dict[str, dict],
    research: Path,
    derived: Path,
    jev_root: Path,
    items_path: Path,
    challengers: dict[str, list[dict]],
) -> measures.MeasureData:
    """Load every lane O measure source once (absent files -> None)."""
    s3 = {
        c["slug"]: _sign_block(regrade.get(c["slug"]), c)["s3"]["grade"]
        for c in cats
    }
    return measures.MeasureData(
        s3=s3,
        awards=measures.load_parquet(derived / "awards.parquet"),
        award_answers=measures.load_pass_answers(jev_root, measures.AWARDS_SET),
        review_categories=measures.item_categories(items_path, "app_reviews"),
        review_answers=measures.load_pass_answers(
            jev_root, measures.REVIEWS_SET
        ),
        apps=measures.load_parquet(derived / "apps.parquet"),
        cases=measures.load_csv(research / "replacement_cases.csv"),
        regulator=measures.regulator_map(
            measures.load_csv(research / "regulator_approval.csv")
        ),
        challengers=challengers,
        rounds=measures.load_csv(research / "ai_native_rounds_24m.csv"),
        legacy_mid=measures.legacy_midpoints(
            measures.load_csv(research / "market_size.csv")
        ),
        yc_answers=measures.load_pass_answers(jev_root, measures.YC_SET),
    )


def run_export(
    out_dir: Path,
    *,
    research_dir: Path | None = None,
    configs_dir: Path | None = None,
    rubric_path: Path | None = None,
    items_path: Path | None = None,
    jev_root: Path | None = None,
    derived_dir: Path | None = None,
    only: frozenset[str] | None = None,
) -> dict:
    """Generate missing configs, score every kept category, write the JSON."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    research = Path(research_dir or paths.RESEARCH)
    derived = Path(derived_dir or paths.DERIVED)
    jev = Path(jev_root or derived / "jev")
    items_p = Path(items_path) if items_path else derived / "items.parquet"

    cats = load_categories(research / "categories.csv")
    if only is not None:
        cats = [c for c in cats if c["slug"] in only]
    desk = load_desk(research / "raw" / DESK)
    regrade = load_regrade(research / "raw" / REGRADE)
    challengers = load_challengers(research / "challengers.csv")
    items = labels.load_labels(items_path=items_path, jev_root=jev_root)
    buyer_universe = estimates.load_csv(research / "buyer_universe.csv")
    vendors = estimates.load_csv(research / "vendors.csv")
    crit_map = criticality.load_criticality(research / "criticality.csv")
    topdown_rows = topdown.load(research / "market_size.csv")
    tasks = score_inputs.load_tasks(research / "tasks.csv")
    ai_answers = score_inputs.load_task_answers(jev_root)
    ai_present = (jev / score_inputs.AI_FIT_PASS).exists()
    rubric = scores.load_rubric(rubric_path)
    sub_map = measures.collect(
        [c["slug"] for c in cats],
        _measure_data(cats, regrade, research, derived, jev, items_p, challengers),
        rubric.measures,
    )

    written_configs = []
    cat_objs, score_objs = [], []
    region_data: list[
        tuple[str, estimates.CategoryEstimate, market.MarketValue]
    ] = []
    for cat in cats:
        slug = cat["slug"]
        cfg_path = catconfig.ensure_config(
            slug, cat.get("name", slug), configs_dir
        )
        written_configs.append(cfg_path)
        cfg = catconfig.load_config(slug, cfg_path)
        est = estimates.estimate_category(
            slug,
            items=items,
            buyer_universe=buyer_universe,
            vendors=vendors,
            config=cfg,
        )
        mv = topdown.calibrate(
            market.market_value(slug, buyer_universe, crit_map.get(slug), cfg),
            topdown_rows.get(slug),
        )
        inp = _score_inputs(
            est,
            tasks,
            ai_answers,
            ai_present,
            sub_map.get(slug, {}),
            mv,
        )
        sc = scores.score_category(slug, inp, rubric)
        cat_objs.append(
            build_category(
                cat,
                desk.get(slug),
                regrade.get(slug),
                est,
                sc,
                challengers.get(slug, []),
                mv,
            )
        )
        score_objs.append(_score_json(sc))
        region_data.append((slug, est, mv))

    score_objs.sort(key=lambda s: s["total"], reverse=True)
    site = out_dir / "site"
    site.mkdir(exist_ok=True)
    cat_path = site / "categories.json"
    sco_path = site / "scores.json"
    reg_path = site / "regions.json"
    cat_path.write_text(
        json.dumps(cat_objs, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    sco_path.write_text(
        json.dumps(score_objs, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    reg_path.write_text(
        json.dumps(
            market.regions_view(region_data), indent=2, ensure_ascii=False
        )
        + "\n",
        encoding="utf-8",
    )
    return {
        "categories": cat_path,
        "scores": sco_path,
        "regions": reg_path,
        "configs": written_configs,
    }


def print_summary(result: dict) -> None:
    for name in ("categories", "scores", "regions"):
        print(f"wrote {result[name]}")
    print(f"{len(result['configs'])} category configs checked")
