# Plan 3: better measures for pain, lock-in, crowding, and a workflow-level search

Approved by Hansel on 2026-10-05 ("go") after the measure research in the thread. The 150-label human
check is optional and not scheduled.

## Global constraints
- Free sources only; respect robots.txt and terms; no logins. G2, Gartner, Capterra and Reddit are out (blocked).
- Jev budget: `account_total` stays 8.00; new passes get caps that fit the remaining ~$7.60.
- No text redistribution in git: ids, URLs, numbers, labels, excerpts under 30 words.
- Effort high for research agents. Devin lanes in their own worktrees.

## Lanes
| Lane | Owner | Output |
|---|---|---|
| L procurement | Devin | `data/derived/awards.parquet`: award id, source, region, buyer, title and description window, value, start, end, duration months, procedure (open, restricted, negotiated without competition, direct), CPV/PSC, category hint. Collectors: USAspending, TED v3, UK Find a Tender and Contracts Finder (OCDS), AusTender OCDS, GeBIZ. |
| M app stores | Devin | `data/derived/apps.parquet` (rating, count, per app per storefront) and review windows for Jev, from the iTunes Search/Lookup API and the customer-reviews RSS feed. App list from research. |
| N workflows | Devin | `data/derived/workflows.parquet`: workflow x occupation x task, US employment and wage (BLS OEWS), task share (O*NET), labour value, AI usage on the tasks (public AI usage dataset on Hugging Face), crowding per workflow from YC. Mapping from research. |
| O scores | Devin | New pain, lock-in and crowding parts per the rubric below; workflow scores; exports. |
| Research | Claude workflows | app list per category and region; replacement-case ledger (duration, cost, outcome); SEA and India annual-report mentions of core systems; workflow-to-occupation mapping; challenger round dates (24 months) and hq; YC survival cohort. |
| Jev | Claude | awards: maintain / extend / replace / consult / other plus category; reviews: outage or backend complaint vs other; YC descriptions: category and workflow. |

## New rubric (each 1 to 5)
- **Pain** = mean of available sub-scores, each binned across categories by quintile: keep-alive share of public
  IT spend on the category's systems (maintain + extend over maintain + extend + replace), outage share of app
  reviews, mean app rating (inverted), failed-or-overrun replacement count per $1B legacy spend, workaround sign.
- **Lock-in** = mean of quintile sub-scores: median contract duration, non-competitive award share, median
  replacement duration from the case ledger, regulator approval required (0/1 from research).
- **Crowding** = mean of quintile sub-scores: AI-native challengers with traction, AI-native funding in the last
  24 months per $1B legacy spend, YC companies 2024 to 2026 in the category.
- Size and AI fit unchanged. Sub-scores with no data are skipped and the count of inputs is shown.

## Order
1. Research workflows and Devin lanes L, M, N in parallel.
2. Jev passes, blind audit on 60 items per new question (80% bar, one rewording).
3. Lane O scoring; rerun export.
4. Report v3 for Hansel, then the five site decisions.
