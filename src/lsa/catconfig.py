"""Per-category assumption files ``configs/categories/<slug>.toml``.

``lsa export`` writes one file per kept category on first run, then reads
it: every number the estimate and score methods assume lives in the file so
a reader can rerun the arithmetic (spec section 6). Editing a value and
re-running the export applies it; the file is never overwritten.

Only the TOML keys below are read; anything else in the file is ignored so
free-form review notes are safe.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path

from lsa import paths

CONFIGS_DIR = paths.ROOT / "configs" / "categories"


@dataclass(frozen=True)
class CategoryConfig:
    slug: str
    # high = min(buyer_universe, low x multiplier)
    multiplier: float = 3.0
    # buyer-universe family estimate = universe midpoint x penetration
    penetration: float = 1.0
    # confirmed-signal estimate = weighted confirmed / detection_rate
    detection_rate: float = 1.0
    # two family estimates agree when they differ by at most this factor
    agree_within: float = 2.0
    tender_question_set: str = "tenders-which-category@v2"
    tender_require_status: tuple[str, ...] = ()
    job_question_sets: tuple[str, ...] = (
        "job-apis-industry-segment-legacy-in-use@v2",
        "job-pages-industry-segment-legacy-in-use@v2",
    )
    job_in_use_choices: tuple[str, ...] = ("in_use",)
    universe_skip: tuple[str, ...] = ()
    universe_overrides: dict[str, tuple[float, float]] = field(
        default_factory=dict
    )
    vendor_exclude: tuple[str, ...] = ()
    vendor_overrides: dict[str, float] = field(default_factory=dict)
    # "global": rows naming >1 study region land in the global bucket;
    # "each": the whole count is added to every named region.
    multi_region_policy: str = "global"
    challenger_exclude: tuple[str, ...] = ()
    funding_overrides: dict[str, float] = field(default_factory=dict)
    regulation_patterns: tuple[str, ...] = ("regulat", "certif")


def default_toml(slug: str, name: str) -> str:
    """The generated config text for one category."""
    return f'''# Assumptions for "{name}" ({slug}), plan 2 tasks 5 and 6.
# `lsa export` wrote this file once and reads it on every run: edit values and
# rerun the export to apply. Every assumed number lives here, not in code.
slug = "{slug}"

[estimate]
multiplier = 3.0        # high = min(buyer universe high, low x multiplier)
penetration = 1.0       # buyer-universe family estimate = universe midpoint x this
detection_rate = 1.0    # confirmed-signal estimate = weighted confirmed / this
agree_within = 2.0      # two family estimates agree within this factor

[confirmed]
# One confirmed item counts as one organisation; org names are not extracted.
tender_question_set = "tenders-which-category@v2"
tender_require_status = []   # e.g. ["in_use", "being_replaced"] to also need a status
job_question_sets = ["job-apis-industry-segment-legacy-in-use@v2", "job-pages-industry-segment-legacy-in-use@v2"]
job_in_use_choices = ["in_use"]   # legacy_in_use answers counted as "legacy in use"

[buyer_universe]
skip = []   # register-name substrings whose rows are dropped before parsing
# [buyer_universe.override.US]   # hand-set a region's universe when parsing is wrong
# low = 0
# high = 0

[vendors]
# Every row for the category counts as a legacy product unless excluded here.
exclude_products = []      # product-name substrings whose rows are dropped
count_overrides = {{}}       # "Vendor | Product" -> exact customer count
multi_region_policy = "global"   # "each" counts a multi-region row in every named region

[challengers]
exclude_companies = []
funding_overrides = {{}}     # "Company" -> disclosed USD total (replaces parsed funding)

[lockin]
regulation_patterns = ["regulat", "certif"]   # reason-to-stay substring match
'''


def config_path(slug: str, configs_dir: Path | None = None) -> Path:
    return (configs_dir or CONFIGS_DIR) / f"{slug}.toml"


def ensure_config(
    slug: str, name: str, configs_dir: Path | None = None
) -> Path:
    """Write the default file when absent; returns the path either way."""
    path = config_path(slug, configs_dir)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(default_toml(slug, name), encoding="utf-8")
    return path


def _str_tuple(values) -> tuple[str, ...]:
    return tuple(str(v) for v in values or ())


def load_config(slug: str, path: Path | None = None) -> CategoryConfig:
    """Config for ``slug``; the file may be absent (defaults then apply)."""
    path = path or config_path(slug)
    if not path.exists():
        return CategoryConfig(slug=slug)
    data = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    est = data.get("estimate", {})
    conf = data.get("confirmed", {})
    bu = data.get("buyer_universe", {})
    vend = data.get("vendors", {})
    chal = data.get("challengers", {})
    lock = data.get("lockin", {})
    overrides = {
        str(region).upper(): (float(v["low"]), float(v["high"]))
        for region, v in (bu.get("override") or {}).items()
        if isinstance(v, dict) and "low" in v and "high" in v
    }
    policy = str(vend.get("multi_region_policy", "global"))
    if policy not in ("global", "each"):
        policy = "global"
    return CategoryConfig(
        slug=slug,
        multiplier=float(est.get("multiplier", 3.0)),
        penetration=float(est.get("penetration", 1.0)),
        detection_rate=float(est.get("detection_rate", 1.0)),
        agree_within=float(est.get("agree_within", 2.0)),
        tender_question_set=str(
            conf.get("tender_question_set", "tenders-which-category@v2")
        ),
        tender_require_status=_str_tuple(conf.get("tender_require_status")),
        job_question_sets=_str_tuple(conf.get("job_question_sets"))
        or CategoryConfig.job_question_sets,
        job_in_use_choices=_str_tuple(conf.get("job_in_use_choices"))
        or ("in_use",),
        universe_skip=_str_tuple(bu.get("skip")),
        universe_overrides=overrides,
        vendor_exclude=_str_tuple(vend.get("exclude_products")),
        vendor_overrides={
            str(k): float(v)
            for k, v in (vend.get("count_overrides") or {}).items()
        },
        multi_region_policy=policy,
        challenger_exclude=_str_tuple(chal.get("exclude_companies")),
        funding_overrides={
            str(k): float(v)
            for k, v in (chal.get("funding_overrides") or {}).items()
        },
        regulation_patterns=_str_tuple(lock.get("regulation_patterns"))
        or ("regulat", "certif"),
    )
