# Jev blind audit

Each pass is checked against labels from separate Claude agents that never saw Jev's answers.
These are model labels, not human labels. Pass bar: 80% agreement, else reword once, else drop.

## HN: firsthand pain and reason to stay (2026-10-05)

Sample: 100 comments, 50 drawn at random from all 1,590 and 50 at random from those Jev scored
0.5 or higher (positives are rare, so they were oversampled to measure precision). Seed 20261005.
Labels: `data/labels/hn-audit-2026-10-05.json`. Scoring: `scripts/audit_score.py`.

| Question | Threshold | Agreement | Precision | Recall |
|---|---|---|---|---|
| firsthand_pain | 0.5 | 71% | 44% | 100% |
| firsthand_pain | **0.7 (used)** | **89%** | 73% | 83% |
| reason_to_stay | choice | 79% | | |

The 0.7 cut was chosen after seeing this audit; it matches the HN study's cut. `reason_to_stay`
sits just under the bar and is used only as colour, never for counts.
