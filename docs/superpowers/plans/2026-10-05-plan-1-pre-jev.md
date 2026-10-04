# Plan 1: setup and pre-Jev research

> **For agentic workers:** Devin lanes implement code tasks (`devin -p --model swe-2-max`, one
> worktree per lane). Claude runs research tasks through dynamic workflows and reviews every
> diff. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the repo, finish all research that needs no Jev, count the real items each
Jev pass would read, and print a Jev cost estimate for Hansel's credit decision.

**Architecture:** Python package `lsa` (uv). Research lives as markdown plus CSV under
`research/`. Collectors count before they fetch: each source module answers
`count(query) -> int` from an official API or search result total, and only later plans fetch
items. The estimator multiplies counts by measured tokens per item and the Jev price.

**Tech Stack:** Python 3.11+, uv, httpx, duckdb, pyarrow, pytest, ruff, gitleaks.

**Spec:** `docs/superpowers/specs/2026-10-05-legacy-software-atlas-design.md`

Later plans (written after the Jev gate): Plan 2 Jev passes and estimates, Plan 3 deep dives
and playbook, Plan 4 site pages (in `hanselhansel/hansel-site`).

## Global Constraints

- No GitHub Actions. Local verify only: `scripts/verify.sh` (gitleaks, ruff, pytest).
- Tests never call the network. Use `httpx.MockTransport`.
- No secrets in files. The Jev key is read from env `TYPESAFE_API_KEY` only at runtime.
- Official APIs and bulk downloads first; public pages only; respect robots.txt; no logins,
  paywalls or paid data.
- Store URLs, dates, quotes under 30 words, derived labels. No full third-party text in git.
- Regions: US, EU, UK, SG, IN, ID, VN, MY, TH, PH, AU (ISO alpha-2 codes, `EU` for EU-level).
- Copy: no em dashes anywhere in tracked prose.
- Jev price: `input_usd_per_million = 0.042` (`jev-1.13.0`, docs.typesafe.ai/models, 2026-09-28).
- Jev target: under $25 total.

## Review Focus

- A source that returns no total (pagination only): `count` must return `None`, never 0.
- Rate limits and 429s: collectors back off and resume; a count run is idempotent.
- Non-English portals (VN, TH, ID): queries carry local-language synonyms from research.
- One organisation seen in several sources: org names normalise before counting distinct orgs.
- Estimate with a missing tokens-per-item measure: fall back to a stated default and flag it.

---

### Task 1: Scaffold (Devin lane A)

**Files:** `pyproject.toml`, `src/lsa/__init__.py`, `src/lsa/contracts.py`, `src/lsa/paths.py`,
`scripts/verify.sh`, `.gitleaks.toml`, `.githooks/pre-push`, `.gitignore`,
`configs/prices.toml`, `configs/budgets.toml`, `README.md`, `tests/test_contracts.py`

**Produces:**
- `contracts.CountRecord(source: str, family: str, region: str, category: str, system: str, query: str, count: int | None, method: str, counted_at: str)`
- `contracts.EvidenceRow(source, family, url, fetched_at, region, category, system, org, excerpt, lane: Literal["count","depth"])` with `excerpt` at most 30 words (validator raises).
- `paths.ROOT`, `paths.RAW`, `paths.DERIVED`, `paths.RESEARCH`.
- `budgets.toml` with `account_total = 0.00` (Hansel sets it at the gate).

- [ ] Tests: `test_excerpt_over_30_words_raises`, `test_count_none_allowed`, `test_region_must_be_known_code`.
- [ ] Implement, run `scripts/verify.sh`, expect `verify: ok`. Commit.

### Task 2: Desk research (Claude, dynamic workflow)

**Files:** `research/categories.csv`, `research/categories/<slug>.md`, `research/vendors.csv`,
`research/challengers.csv`, `research/sources.csv`

**Produces:**
- `categories.csv`: `slug, name, systems, s1, s2, s3, s4, signs_met, kept, reason, sources`
  (about 40 candidates; kept when `signs_met >= 2`).
- `vendors.csv`: `category, vendor, product, first_shipped, disclosed_customers, regions, source`.
- `challengers.csv`: `category, company, founded, hq, funding_usd, strategy, traction, source`.
- `sources.csv`: `family, source, region, access (api|bulk|search|page), count_method, url, notes`.
- Per category md: synonyms and local-language search terms per region, buyer universe and
  its register, the evidence for each sign.

- [ ] Workflow fans out one researcher per category plus one per region for sources.
- [ ] Claude verifies a sample of citations per category and fixes or drops bad rows.
- [ ] Direction check: if fewer than 15 categories pass, stop and tell Hansel. Commit.

### Task 3: Counting collectors (Devin lanes B, C, D)

**Consumes:** Task 1 contracts; Task 2 `sources.csv` and synonyms.
**Files:** `src/lsa/sources/<family>/<source>.py`, `tests/sources/test_<source>.py`,
`src/lsa/count.py` (CLI `uv run lsa count --family F`)

- Lane B, procurement: USAspending, TED, Contracts Finder, AusTender, GeBIZ, PhilGEPS, plus
  any APAC portal `sources.csv` marks api or bulk.
- Lane C, jobs and HN: public job board totals per query and region; HN filter over the
  local 605,125-comment sample from `jev-opportunity-atlas` (local paths, no network).
- Lane D, pages: vendor and SI customer stories, review sites, events, social via search
  result totals.

Each module: `count(query: str, region: str) -> int | None`. Writes
`data/derived/counts.parquet` (rows of `CountRecord`).

- [ ] Per source, mock-transport tests for: a normal total, a missing total (`None`), a 429
  then success.
- [ ] Run the live counts (Claude, not Devin), at polite rates. Commit code; counts parquet is
  tracked (small, no third-party text).

### Task 4: Jev estimate (Devin lane E)

**Consumes:** `counts.parquet`, `configs/prices.toml`.
**Files:** `src/lsa/estimate.py`, `tests/test_estimate.py`, CLI `uv run lsa estimate`

- `estimate(counts, passes: list[Pass]) -> Estimate` where
  `Pass(name, family, prefilter_keep: float, tokens_per_item: int, items_per_call: int)`.
  Defaults: tokens_per_item from a 50-item text sample per family measured in Task 3; packing 5.
- Prints per pass: items, calls, tokens, USD, and the total against the $25 target.
- [ ] Tests: arithmetic on fixed counts; missing tokens measure falls back and flags. Commit.

### Task 5: Gate report (Claude)

- [ ] Write `docs/reports/2026-10-pre-jev.md`: what research found, kept categories, volumes
  per source, the estimate, and the recommended credit.
- [ ] Merge `chore/bootstrap` and lane branches to `main` after `scripts/verify.sh` passes.
- [ ] Ask Hansel for the Jev credit.
