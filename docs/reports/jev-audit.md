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

## The other six passes (2026-10-05)

Sample: 60 items per pass at random from all labelled items, seed 20261005. Bar: 80%.
Round 1 used question set v1. Questions under the bar were reworded once (v2: category only
when the item is mainly about software for that job; size and region only when stated) and
re-labelled blind with the v2 wording.

| Pass | Question | v1 | v2 | Used |
|---|---|---|---|---|
| Tenders | system status | 93% | | yes |
| Tenders | category | 47% | 87% | yes (v2) |
| Job APIs | industry | 83% | 82% | yes (v2) |
| Job APIs | segment | 65% | 97% | yes (v2) |
| Job APIs | legacy in use | 97% | 95% | yes (v2) |
| Job pages | industry | 40% | 42% | **dropped**: listing snippets are too short |
| Job pages | segment | 75% | 95% | yes (v2) |
| Job pages | legacy in use | 98% | 98% | yes (v2) |
| Vendor stories | category | 58% | 55% | **dropped**: use the vendor's mapped category instead |
| Vendor stories | segment | 80% | 90% | yes (v2) |
| Vendor stories | region | 88% | 93% | yes (v2) |
| Vendor stories | in use or replaced | 98% | 98% | yes (v2) |
| SI stories | category | 73% | 97% | yes (v2) |
| SI stories | segment, region, status | 75 to 98% | 98% | yes (v2) |

Finding from the audit itself: blind labellers put about 80% of keyword-matched tenders in no
legacy category at all. Raw tender keyword counts overstate legacy demand several times over;
only Jev-confirmed tenders (v2 category) are used in estimates.
