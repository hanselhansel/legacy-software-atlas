# Plan 2: Jev passes, estimates and scores

> **For agentic workers:** Devin lanes implement code tasks (`devin -p --model swe-2-max`, one
> worktree per lane). Claude runs the paid Jev runs, the blind audit and the review.

**Goal:** Fetch the counted items, label them with Jev under the `$8.00` cap, turn labels into
graded usage ranges per category, region and segment, and compute the 5-part score.

**Spec:** `docs/superpowers/specs/2026-10-05-legacy-software-atlas-design.md` sections 6 to 8.
**Gate input:** `docs/reports/2026-10-05-pre-jev.md`.

## Global Constraints

- `configs/budgets.toml` `account_total = 8.00` once Hansel confirms the credit. Every paid stage
  prints an estimate and refuses to run past its cap.
- Jev key from env `TYPESAFE_API_KEY` only. Tests use a fake client; no network in tests.
- Item text lives in `data/raw/` (git-ignored). Git holds item ids, URLs, labels, excerpts of 30 words at most.
- Only the passes in `configs/passes.toml` run. New questions need a new pass entry and an estimate.

## Review Focus

- One item matched by several queries: dedupe by URL or notice id before Jev sees it.
- Pages that changed or vanished since counting: fetch failures are logged, never retried in a loop.
- Jev answers outside the allowed choices: rejected and counted as unknown.
- Region inferred from the source, not from Jev, except for vendor and SI stories.
- Estimates with a single source family: grade C, labelled rough.

### Task 1: Fetchers (Devin lane G)
`src/lsa/fetch/<family>.py`: page through each counted query, write `data/raw/<family>/<id>.json`
(text window per `passes.toml`), and `data/derived/items.parquet` (`item_id, family, source, region,
category_hint, url, fetched_at, text_sha256`). Dedupe on URL or source id.

### Task 2: Jev client and runner (Devin lane H)
Port the HN study's Jev client pattern (`../jev-opportunity-atlas/src/atlas/inference/`, read-only):
packed calls, budget ledger, resume from `done.jsonl`, price and calibration from `configs/`.
`lsa jev pilot --pass NAME --n 200` and `lsa jev run --pass NAME --yes`.

### Task 3: Pilot and blind audit (Claude)
200 items per pass. A separate Claude agent labels a random 100 per pass without seeing Jev's answers.
Publish agreement per pass in `docs/reports/jev-audit.md`. A pass under 80% agreement is reworded once,
then dropped if still under.

### Task 4: Main runs (Claude)
Run each pass that passed the audit. Record real spend versus estimate.

### Task 5: Estimates (Devin lane I)
`src/lsa/estimates.py`: per category, region and segment, a `(low, high, grade, sources)` range for
companies using, by triangulating buyer universes (`research/buyer_universe.csv`), labelled job posts
and tenders, and vendor-disclosed counts (`research/vendors.csv`). Assumptions in
`configs/categories/<slug>.toml`. Grades per spec section 6.

### Task 6: Scores (Devin lane I)
`src/lsa/scores.py`: the five parts with written rubrics in `configs/rubric.toml`; equal default weights;
exports `exports/site/scores.json` with every part and its evidence links.
