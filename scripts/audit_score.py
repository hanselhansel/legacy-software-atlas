"""Score a Jev pass against blind agent labels.

Usage: uv run python scripts/audit_score.py <pass-slug> <labels.json> [question-set version]
labels.json is a list of {"item_id", "answers": {question_id: bool | option}}.
Probability answers count as yes at >= 0.5. Prints agreement per question and,
for probability questions, precision and recall of Jev's yes against the labels.
"""

import json
import sys

import duckdb


def main(slug: str, labels_path: str, version: str | None = None) -> None:
    labels = {x["item_id"]: x["answers"] for x in json.load(open(labels_path))}
    rows = duckdb.sql(
        f"select item_id, question_id, qtype, probability, choice "
        f"from 'data/derived/jev/{slug}/answers/*.parquet' "
        + (f"where question_set = '{slug}@v{version}'" if version else "")
    ).fetchall()
    by_q: dict[str, list[tuple]] = {}
    for item, q, qtype, prob, choice in rows:
        if item in labels and q in labels[item]:
            jev = (prob >= 0.5) if qtype == "probability" else choice
            by_q.setdefault(q, []).append((jev, labels[item][q], qtype))
    for q, pairs in sorted(by_q.items()):
        agree = sum(a == b for a, b, _ in pairs) / len(pairs)
        line = f"{q}: n={len(pairs)} agreement={agree:.0%}"
        if pairs[0][2] == "probability":
            tp = sum(a and b for a, b, _ in pairs)
            fp = sum(a and not b for a, b, _ in pairs)
            fn = sum(b and not a for a, b, _ in pairs)
            prec = tp / (tp + fp) if tp + fp else float("nan")
            rec = tp / (tp + fn) if tp + fn else float("nan")
            line += f" precision={prec:.0%} recall={rec:.0%}"
        print(line)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
