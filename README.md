# Legacy Software Atlas

Which legacy software is ready to be replaced by AI-native companies? This study maps
25 to 40 job categories (core banking, insurance policy admin, hospital records and
more), answers seven questions per category from cited sources, scores each on size,
pain, AI fit, lock-in and crowding, and ends with a replacement playbook drawn from
real cases. It is built for people thinking about founding an AI-native company to
replace legacy software.

**Status:** work in progress. No findings yet.

**Disclosure:** no affiliation with TypeSafe.

## Setup

```bash
brew install gitleaks          # required by the local verify gate
uv sync
git config core.hooksPath .githooks
scripts/verify.sh              # gitleaks, ruff, pytest; prints "verify: ok"
```

The Jev key is read from the `TYPESAFE_API_KEY` environment variable at runtime only.
It is never stored in the repo.

## Data and rights

The repo stores URLs, dates, short quotes under 30 words, and derived labels. It does
not redistribute full third-party text or personal data. Code is MIT licensed;
derived labels and aggregates are CC BY 4.0.

## Scoring and exports

`lsa export` writes `exports/site/`:

- `categories.json` and `scores.json`: per category, the five parts
  (size, pain, ai_fit, lockin, crowding) plus the weighted total rescaled
  to 0..100. Pain, lock-in and crowding are means of sub-scores, each a raw
  measure ranked across the categories into quintiles 1..5 (ties share the
  lower quintile; a sub-score below its minimum count in
  `configs/rubric.toml`, or with no source data, is skipped and shown with
  `score: null`). Pain draws on award keep-alive share, app-review backend
  failures, inverted app ratings, the failed-replacement rate and the S3
  grade; lock-in on award duration, non-competitive award share,
  replacement duration and regulator approval; crowding on AI-native
  challengers at traction, 24-month AI-native funding per $1B of legacy
  spend, and YC 2024+ companies.
- `regions.json`: region x category buyer, value and usage estimates.
- `workflows.json`: every row of `research/workflows.csv` sorted by an
  opportunity index, best first. Per workflow the index is
  `rank(labour_value) + rank(ai_usage or the category's ai_fit)
  + rank(the category's pain) - rank(crowding)`, where crowding is the
  count of `ai_native_rounds_24m.csv` rounds mapped to the workflow, ranks
  ascend by value across the workflow set, and a workflow with
  `touches_core` is penalized by the full rank spread so core-touching
  work lands below edge work (it is the lock-in proxy).

## Design

- Design: `docs/superpowers/specs/2026-10-05-legacy-software-atlas-design.md`
- Plans: `docs/superpowers/plans/`
