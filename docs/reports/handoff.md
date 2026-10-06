# Handoff: Legacy Software Atlas

For an analyst picking this study up cold. Written 2026-10-06. Owner: Hansel.

Read in this order: this file, then `docs/reports/review-report.md` (report v3, the current findings),
then `docs/superpowers/specs/2026-10-05-legacy-software-atlas-design.md` (the original design).

---

## 1. What we are trying to do

A public study for byhansel.com that answers one question for founders:

> **Which legacy software is ready to be replaced by an AI-native company, and where should a founder look first?**

It breaks into the questions the published study must answer:

| # | Question | How the study answers it today |
|---|---|---|
| Q1 | Which legacy systems are still in use? | 35 job categories (core banking, permits, COBOL and mainframe, ...) kept from 46 by a strict legacy test |
| Q2 | How big is each? | Annual global spend still on legacy systems, top-down from analyst and vendor revenue (about $178B in total) |
| Q3 | Who uses them: industries, buyer size, regions? | Buyer counts per register, segment shares, region view, criticality and build-versus-buy by buyer size |
| Q4 | Why do buyers stay, and how locked in are they? | Lock-in score: contract length, non-competitive awards, replacement duration, regulator approval |
| Q5 | How painful are they? | Pain score: keep-alive spend in public contracts, app-review outages, app ratings, failed replacements, workaround evidence |
| Q6 | How much of the work can AI do? | AI-fit score over 420 tasks (12 per category) |
| Q7 | Who is attacking, and how crowded is it? | 436 challengers, 298 AI-native rounds in 24 months, YC 2024+ startups; crowding score |
| Q8 | Where is the opening (big, painful, AI-fit, low lock-in, low crowding)? | Five-test search at category level and an opportunity index over 210 workflows |
| Q9 | How do AI-native companies actually replace legacy, and what fails? | 8 deep cases and a playbook (strategies by stages) |

Audience: people thinking about founding an AI-native company. Public persona rule for all copy: lead
with what readers learn, never Hansel's past credentials. No em dashes in any copy.

## 2. Where everything is

| What | Where |
|---|---|
| Study repo (public) | `hanselhansel/legacy-software-atlas`, local `~/conductor/repos/legacy-software-atlas` |
| Working branch | `chore/bootstrap` (125 commits). **Not merged to `main` yet.** No PR open. |
| Website repo | `hanselhansel/hansel-site`, local `~/hansel-site` (Astro). Untouched by this study so far. |
| Sibling HN study | `~/conductor/repos/jev-opportunity-atlas`, site page `/hn-opportunities` |
| Current findings | `docs/reports/review-report.md` (report v3, about 22,600 words; section 1 is the one-page answer) |
| Design and plans | `docs/superpowers/specs/`, `docs/superpowers/plans/` (plans 1, 2, 3) |
| Method reports | `docs/reports/2026-10-05-pre-jev.md` (volumes and Jev estimate), `docs/reports/jev-audit.md` (every blind audit) |
| Deep cases | `cases/*.md` (8 cases, about 4,000 words each, fact-checked) |
| Playbook | `playbook/playbook.md` (quotes v2 scores, needs a refresh) |
| Research tables | `research/*.csv` (see section 5) |
| Derived data | `data/derived/` (counts, items, awards, apps, workflows, Jev answers and ledger). Raw text is in `data/raw/` and git-ignored. |
| Site exports | `exports/site/categories.json`, `scores.json`, `regions.json`, `workflows.json` |
| Scoring rules | `configs/rubric.toml`; Jev questions `configs/questions.toml`; passes `configs/passes.toml`; caps `configs/budgets.toml` |
| Code | `src/lsa/` (Python 3.11, uv). Main commands below. |

Setup and checks:

```bash
cd ~/conductor/repos/legacy-software-atlas
uv sync
git config core.hooksPath .githooks
scripts/verify.sh                 # gitleaks, ruff, pytest (535 tests); must print "verify: ok"
uv run lsa export                 # rebuilds exports/site/*.json from research/ and data/derived/
```

Other commands: `lsa count`, `lsa fetch`, `lsa awards`, `lsa apps`, `lsa yc`, `lsa workflows-labour`,
`lsa estimate`, `lsa jev pilot|run --pass "<name>" [--yes]`.
The Jev key lives in macOS Keychain (`typesafe-jev-api-key`). Load it only at run time:
`TYPESAFE_API_KEY="$(security find-generic-password -s typesafe-jev-api-key -w)" uv run lsa jev run ...`.
Never write it to a file.

## 3. Decisions already made (do not reopen without Hansel)

| Topic | Decision |
|---|---|
| Unit of analysis | 25 to 40 job categories; 35 kept |
| Legacy test | Each of 4 signs graded strong / weak / not met by a skeptical re-grade; keep when at least 1 strong and strong + half weak >= 2.5 |
| Data | Free public sources only; respect robots.txt and terms; no logins, no paid data |
| Regions | US, EU, UK, SG, IN, ID, VN, MY, TH, PH, AU |
| Numbers | Ranges with A/B/C grades, every number linked to its source |
| Score | Open 5-part score, total = 35 + 5 x (size + pain + AI fit - lock-in - crowding); readers can re-weight |
| Size | Top-down legacy spend (global spend x legacy share); bottom-up buyers x spend only splits by region and segment |
| Build-vs-buy | Hansel's lens: separate filter by criticality and buyer size, **not** part of the total |
| Pain, lock-in, crowding | Plan 3 measures (section 6); each sub-measure ranked into fifths across categories; part = mean, one decimal |
| Regulator rule | Yes when, in the US, EU or UK, a sector regulator must approve or be told in advance before the core system is replaced or outsourced |
| Funding | Only category-specific AI-native rounds count; company-wide raises (Sierra, Anthropic, Cognition...) and exits are excluded |
| Deep cases | 6 to 8 very deep cases incl. 1 or 2 failures: GovWell, Adaptive, Valon, Mechanical Orchard, Rillet, AKASA, bloop, trade-finance networks |
| Playbook | Strategies (overlay, greenfield, AI-run service, migration-led, acquire) by stages (wedge, first 10, expand, replace core) |
| Site | Observatory building click opens `/observatory` with study cards; building label "Startup Opportunities"; study at `/legacy-software`, cases at `/legacy-software/<slug>`; visual first, using the existing viz catalogue in hansel-site |
| Review gates | Hansel reviews insights and storyline **before any site work** |

Rejected or declined: paid data (BuiltWith, HG), named product-first or technology-first maps, G2,
Gartner, Capterra and Reddit (blocked), Sonnet subagents, forced fresh sessions per phase.

## 4. How the work runs (usage rules from Hansel)

- **Devin builds code.** `devin -p --model swe-2-max --permission-mode dangerous --prompt-file .devin-brief.md`,
  one bounded task per lane in its own git worktree (`git worktree add ../lsa-laneX -b feat/x chore/bootstrap`).
  The orchestrating analyst writes the brief, reviews the diff, runs `scripts/verify.sh`, merges.
- **For the site, Devin builds; the analyst only reviews diffs and runs checks.**
- **Research runs as dynamic workflows** (fan-out agents with schemas, plus a skeptic or fact-check pass).
- **Effort is capped at high, never max.**
- **Jev (TypeSafe classifier) does bulk labelling.** Every pass gets a pilot, a per-pass cap, and a blind audit
  (separate agents label about 60 items without seeing Jev's answers; bar 80% agreement; reword once, else drop).
- **On Hansel's Mac:** long jobs run in background with `caffeinate -i`; do not end a turn with work pending.
- **Git:** never commit to `main`; commit and push after each green step; never `--no-verify`.

Lessons that cost time (avoid repeating):
- Write to `data/derived/items.parquet` from one process at a time; a parallel or overlapping write once dropped 1,300 rows.
- Item ids can repeat across families (a TED notice is both a tender and an award). Dedupe on (family, item_id).
- Check every API count for "returned the whole database" (multi-word queries without phrase syntax did this).
- Check units: several registers and vendor lines counted loans, titles or people, not buyers.
- Arithmetic means of spend ranges that span orders of magnitude explode; use geometric means and a top-down cap.

## 5. What has been done

**Research** (all in `research/`, raw agent output in `research/raw/`):

| File | Rows | Content |
|---|---|---|
| categories.csv | 46 | Legacy test grades, kept flag, reason |
| vendors.csv | 378 | Legacy products, first shipped, disclosed customers (tagged by unit) |
| challengers.csv | 436 | Challengers with AI-native flag, status, strategy, funding, wedge, customers |
| buyer_universe.csv | 525 | Possible buyers per register and region, unit, segment shares |
| criticality.csv | 140 | Criticality and, per buyer size, build-in-house and spend per buyer |
| market_size.csv | 35 | Top-down global spend and legacy share |
| tasks.csv | 420 | 12 core tasks per category with time share |
| replacement_cases.csv | 353 | Documented replacements: duration, cost, outcome |
| regulator_approval.csv | 35 | Recoded with one rule (17 yes, 18 no) |
| ai_native_rounds_24m.csv | 298 | Rounds Oct 2024 to Oct 2026, scope tag |
| workflows.csv, workflow_occupations.csv | 210, 542 | Workflows mapped to SOC occupations and O*NET tasks |
| apps.csv | 482 | Customer-facing apps on legacy cores, App Store ids |
| regional_usage.csv | 369 | Core systems named in Asian and UK annual reports (not yet used in scores) |
| sources.csv | 123 | Free sources per region and how to count them |

**Collected data** (`data/derived/`): 4,839 first-round items (tenders, jobs, job pages, vendor and SI stories,
1,590 HN comments), 1,919 public awards, 2,718 app reviews from 482 apps, 1,939 YC companies (2024+),
210 workflow labour pools (BLS OEWS x O*NET x Anthropic Economic Index).

**Jev:** 11 passes, all blind-audited (see `docs/reports/jev-audit.md`). Spend **$0.67** of the $8.00 cap
(Hansel loaded $10). Two questions were dropped for failing the audit (job-page industry, vendor-story category).

**Analysis:** scores, market value, build-vs-buy lens, region view, workflow index (all in `exports/site/`);
8 deep cases; playbook; report v3 refreshed after the regulator, rounding and funding fixes.

**Current headline (report v3):** utility billing leads (69.5) and is the only category passing all five
tests; mainframe (69) misses only on lock-in. At workflow level, 55 workflows do not touch the core and
have no recent AI-native round; collections and arrears recur.

## 6. How each score is built (short; full detail goes to the report appendix)

- **Size** (1 to 5): legacy spend midpoint in bands <$0.1B, <$1B, <$5B, <$20B, else 5.
- **Pain:** mean of fifths over keep-alive share of public awards (min 10), backend-failure share of app
  reviews (p >= 0.7, min 50), inverted app rating (min 3 apps), failed-or-overran share of replacements (min 3),
  workaround sign grade.
- **AI fit:** time-weighted mean Jev score over the category's 12 tasks (Jev rates about 0.5 points high, so
  it is used only to rank).
- **Lock-in:** mean of fifths over median award duration, non-competitive award share, median replacement
  duration, regulator approval (yes 5, no 1).
- **Crowding:** mean of fifths over AI-native challengers with traction, category-specific AI-native funding
  in 24 months per $1B of legacy spend, YC 2024+ companies in the category.
- **Workflow opportunity index:** ranks of labour value, AI usage, category pain, minus crowding, minus a
  penalty when the workflow touches the core. Labour value is all US labour in that work, **not** a market size.

## 7. What is not done yet

1. **Hansel's review of report v3 and the five site decisions** (report section 13): which ranking view leads,
   shortlist or filter, how to show pain, which case gets the timeline, launch timing.
2. **Merge `chore/bootstrap` to `main`** of the study repo (after content is settled).
3. **Known data gaps** (report section 12): lock-in rests on two inputs for most categories; India, Indonesia,
   Vietnam, Malaysia, Thailand and Philippines evidence is thin; `regional_usage.csv` not yet in the scores;
   failures under-sampled; audit labels are model labels (an optional 150-label human check by Hansel was
   offered, not scheduled); market sizes have wide ranges.
4. **Stale files:** playbook quotes v2 scores; the study repo README still says "no findings yet".
5. **The site** (plan 4, not written): `/observatory` page, building label, `/legacy-software` study page,
   deep-dive pages, data copy-in script under `hansel-site/scripts/legacy/`, full verify, `/ship`, `/land-and-deploy`.

## 8. Next phase: Hansel's improvements (plan only, not implemented)

These came from Hansel on 2026-10-06. Do them before the site build.

**N1. Restructure the report around the questions.**
Lead with the questions in section 1 (Q1 to Q9) and, for each, the answer and how it was reached.
Move assumptions, method, derivations, worked examples and sensitivity checks into an appendix.
Keep the explanation of how we got here (which Hansel liked) in that appendix.
Acceptance: the main body reads as question, answer, evidence; nothing in it requires the appendix to follow.

**N2. Show the top three providers per category on the map.**
For each of the 35 categories, the three incumbent vendors with the largest installed base or legacy revenue
(name, product, share or customer count, source), plus the leading challenger.
Start from `research/vendors.csv` (378 rows, classified customer counts) and `research/market_size.csv`
(vendor-revenue legs in the method notes); fill gaps with vendor filings.
Acceptance: every category row on the map shows three named providers with a sourced figure or "undisclosed".

**N3. Give each category quotes, anecdotes and the specific pain.**
For each category, say what exactly is painful about using the system, with evidence a reader can feel:
2 to 4 short quotes (under 30 words, linked) from app reviews, HN comments, audit-office and regulator
reports, replacement case write-ups, and public contract text; 1 or 2 anecdotes (a named failed migration,
an outage, a keep-alive contract); and a one-line verdict ("painful because ...", or "not very painful
because ..."). COBOL and mainframe is Hansel's example: name the concrete pains (scarce skills, batch
windows, change cost, testing, outage risk) and the evidence for each.
Sources already collected: `data/raw/app_reviews` with Jev backend-failure labels, `data/raw/hn` with
firsthand-pain labels, `research/replacement_cases.csv`, `data/raw/awards`, the eight cases.
Acceptance: all 35 categories have a pain card with quotes, an anecdote and a verdict tied to the pain score.

Suggested order: N2 (data, small), N3 (research workflow plus a pick-and-check pass; Jev not needed),
then N1 (rewrite), then send to Hansel, then the site decisions and plan 4.

## 9. First steps for the next analyst

1. `scripts/verify.sh` and `uv run lsa export`; confirm `verify: ok` and that `exports/site/scores.json`
   matches report v3 section 3.
2. Read report v3 sections 1, 3, 4A and 12, then `docs/reports/jev-audit.md`.
3. Ask Hansel for his review notes on report v3 and the section 13 decisions if not already given.
4. Start N2, N3, N1 as above. Keep Jev under the $8.00 cap (about $7.33 left).
5. Leave the untracked `nao.html` in the repo root alone; it is not part of this study.
