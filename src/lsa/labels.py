"""Join items.parquet rows to audit-usable Jev answers (plan 2, task 5).

Only the questions ``docs/reports/jev-audit.md`` marks "yes" are loaded, at
the question-set version the audit names: v2 for the reworded sets, v1 for
the tender status set and HN. Dropped labels never reach this module:

- ``job-pages ... industry`` (40% v1, 42% v2): snippets too short;
- ``vendor-stories ... category`` (58% v1, 55% v2): the vendor site row's
  category on the item (``category_hint``) is used instead;
- HN ``reason_to_stay`` (79%): under the bar, loaded for colour only and
  never counted.

Each item resolves to one label view: category, region, segment, status,
pain probability and the sampling weight ``query_count / sampled`` (1.0 for
unsampled families such as HN). Tender and SI categories come from the Jev
category answer; job categories come from the query that fetched the item
(``category_hint``); vendor story categories come from ``category_hint``
(the vendor site row). Regions come from item metadata except for the
vendor and SI story families, which use the Jev region answer (v2).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from lsa import paths

HN_PAIN_YES = 0.7  # firsthand_pain >= 0.7 counts as yes (audit threshold)

# question_set -> usable question_ids, per docs/reports/jev-audit.md.
USABLE: dict[str, frozenset[str]] = {
    "tenders-legacy-system-in-use-being-replaced-or-neither@v1": frozenset(
        {"system_status"}
    ),
    "tenders-which-category@v2": frozenset({"category"}),
    "job-apis-industry-segment-legacy-in-use@v2": frozenset(
        {"industry", "segment", "legacy_in_use"}
    ),
    "job-pages-industry-segment-legacy-in-use@v2": frozenset(
        {"segment", "legacy_in_use"}
    ),
    "vendor-stories-category-in-use-or-replaced-segment-region@v2": frozenset(
        {"segment", "region", "system_status"}
    ),
    "si-stories-category-in-use-or-replaced-segment-region@v2": frozenset(
        {"category", "system_status", "segment", "region"}
    ),
    "hn-firsthand-pain-and-reason-to-stay@v1": frozenset(
        {"firsthand_pain", "reason_to_stay"}
    ),
}

_FALLBACK = frozenset({"unclear", "other", "not_stated", "neither", ""})
SEGMENTS = frozenset({"smb", "mid_market", "enterprise", "government"})


@dataclass(frozen=True)
class LabelledItem:
    item_id: str
    family: str
    url: str
    weight: float
    region: str | None
    category: str | None
    segment: str | None
    industry: str | None
    status: str | None  # in_use / being_replaced / neither
    pain: float | None  # HN firsthand_pain probability
    reason: str | None  # HN reason_to_stay choice (colour only)
    sets: frozenset[str] = frozenset()  # question_sets that answered it


def load_answers(jev_root: Path) -> dict[str, dict[str, dict]]:
    """``{item_id: {question_id: answer row}}`` over usable sets only."""
    import pyarrow.parquet as pq

    out: dict[str, dict[str, dict]] = {}
    jev_root = Path(jev_root)
    if not jev_root.exists():
        return out
    for answers_dir in sorted(jev_root.glob("*/answers")):
        for part in sorted(answers_dir.glob("part-*.parquet")):
            for row in pq.read_table(part).to_pylist():
                allowed = USABLE.get(row["question_set"])
                if allowed is None or row["question_id"] not in allowed:
                    continue
                # sorted parts replay in order, so the latest write wins
                out.setdefault(row["item_id"], {})[row["question_id"]] = row
    return out


def _clean(choice) -> str | None:
    if choice is None or choice in _FALLBACK:
        return None
    return str(choice)


def _choice(ans: dict, qid: str) -> str | None:
    row = ans.get(qid)
    return None if row is None else row.get("choice")


def weight_of(item: dict) -> float:
    """``query_count / sampled`` scaling weight; 1.0 for unsampled items."""
    qc, sampled = item.get("query_count"), item.get("sampled")
    if qc is None or not sampled:
        return 1.0
    return qc / sampled


def label(item: dict, ans: dict) -> LabelledItem:
    """Resolve one items.parquet row plus its usable answers to a label."""
    fam = item["family"]
    region = item.get("region") or None
    category = item.get("category_hint") or None
    segment = industry = status = reason = None
    pain = None
    if fam == "procurement":
        category = _clean(_choice(ans, "category"))
        status = _choice(ans, "system_status")
    elif fam in ("jobs", "jobs-pages"):
        segment = _clean(_choice(ans, "segment"))
        industry = (
            _clean(_choice(ans, "industry")) if fam == "jobs" else None
        )
        status = _choice(ans, "legacy_in_use")
    elif fam in ("vendor", "integrator"):
        region = _clean(_choice(ans, "region")) or region
        segment = _clean(_choice(ans, "segment"))
        status = _choice(ans, "system_status")
        if fam == "integrator":
            category = _clean(_choice(ans, "category"))
    elif fam == "hn":
        row = ans.get("firsthand_pain")
        pain = None if row is None else row.get("probability")
        reason = _choice(ans, "reason_to_stay")
    if status in ("unclear", "other"):
        status = None
    return LabelledItem(
        item_id=str(item["item_id"]),
        family=fam,
        url=str(item.get("url") or ""),
        weight=weight_of(item),
        region=region,
        category=category,
        segment=segment,
        industry=industry,
        status=status,
        pain=pain,
        reason=reason,
        sets=frozenset(
            row["question_set"] for row in ans.values() if "question_set" in row
        ),
    )


def load_labels(
    items_path: Path | None = None, jev_root: Path | None = None
) -> list[LabelledItem]:
    """All items labelled with their usable answers."""
    import pyarrow.parquet as pq

    ip = Path(items_path) if items_path else paths.DERIVED / "items.parquet"
    root = Path(jev_root) if jev_root else paths.DERIVED / "jev"
    answers = load_answers(root)
    return [
        label(row, answers.get(str(row["item_id"]), {}))
        for row in pq.read_table(ip).to_pylist()
    ]


def confirmed(
    labels: list[LabelledItem],
    slug: str,
    *,
    job_in_use_choices: frozenset[str] = frozenset({"in_use"}),
    tender_require_status: frozenset[str] = frozenset(),
    tender_question_set: str = "tenders-which-category@v2",
    job_question_sets: frozenset[str] = frozenset(
        {
            "job-apis-industry-segment-legacy-in-use@v2",
            "job-pages-industry-segment-legacy-in-use@v2",
        }
    ),
) -> list[LabelledItem]:
    """Items that confirm one organisation using the category's software.

    Tenders confirm on a ``tender_question_set`` category match
    (``tender_require_status`` can additionally demand a status answer).
    Job posts confirm on ``legacy_in_use`` in ``job_in_use_choices`` from a
    set in ``job_question_sets`` (default: ``in_use`` only;
    ``being_replaced`` is reported separately by callers).
    """
    out = []
    for it in labels:
        if it.category != slug:
            continue
        if it.family == "procurement":
            if tender_question_set not in it.sets:
                continue
            if tender_require_status and it.status not in (
                tender_require_status
            ):
                continue
            out.append(it)
        elif it.family in ("jobs", "jobs-pages"):
            if not it.sets & job_question_sets:
                continue
            if it.status in job_in_use_choices:
                out.append(it)
    return out


def labelled_job_posts(
    labels: list[LabelledItem], slug: str
) -> list[LabelledItem]:
    """Job-post items for ``slug`` that have any v2 ``legacy_in_use`` answer."""
    return [
        it
        for it in labels
        if it.family in ("jobs", "jobs-pages")
        and it.category == slug
        and it.status is not None
    ]
