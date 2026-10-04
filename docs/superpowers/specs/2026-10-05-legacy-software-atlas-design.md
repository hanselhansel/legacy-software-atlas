# Legacy Software Atlas: design

Date: 2026-10-05. Owner: Hansel. Status: approved in conversation on 2026-10-04 (thread
"Legacy software study"), with the go to implement end to end.

## 1. Goal

Find which legacy software is ready to be replaced by AI-native companies, and show it so a
founder can decide where to look deeper. The study answers seven questions per category:

1. Which legacy systems are still in use?
2. How many people use them?
3. How many companies use them, and in which industries?
4. Why do buyers stay (regulation, switching cost, contracts, skills, data)?
5. Which segments use them (SMB, mid-market, enterprise, government, other)?
6. Where are the users (US, EU and UK, Asia Pacific, specific countries)?
7. Which AI-native challengers are attacking, and how?

It ends with a replacement playbook drawn from real cases.

Audience: people thinking about building an AI-native company to replace legacy software.
Success: a reader can name 3 categories worth a closer look, say why with sourced numbers,
and pick a replacement strategy that fits each.

## 2. Unit of analysis: job categories

The map is 25 to 40 job categories (for example core banking, insurance policy admin,
hospital records, government benefits, freight and customs, manufacturing ERP). Each
category lists its legacy products and technologies (for example COBOL on mainframe,
IBM i / AS/400, Oracle E-Business Suite) and is scored the same way.

## 3. What counts as legacy

A category is on the map when its dominant installed systems show at least 2 of 4 signs.
Each sign needs a cited source.

| Sign | Evidence that counts |
|---|---|
| S1 Pre-cloud core | Core architecture first shipped before about 2005 as mainframe, midrange or on-prem client-server, per vendor history or analyst notes |
| S2 Slow to replace | Typical replacement is a multi-year program, or contracts typically run 7 years or more, per case studies, tenders or vendor filings |
| S3 Workarounds | Users report spreadsheets, re-keying or screen-scraping around the system, per reviews, forums, job posts or HN |
| S4 Shrinking skills | Job posts for the system's skills (COBOL, RPG, Natural, PowerBuilder) are hard to fill or skew to older staff, per job boards and surveys |

Categories tested and rejected stay in the data with the reason, so the cut is auditable.

## 4. Regions

US, EU and UK, and Asia Pacific: Singapore, India, Indonesia, Vietnam, Malaysia, Thailand,
Philippines, Australia. Other countries appear only where a source covers them for free.

## 5. Evidence

Two lanes stay separate, as in the HN study.

- **Counting lane.** Sources with a known universe, used for ranges: buyer registers,
  tenders, job posts, vendor-disclosed customer counts.
- **Depth lane.** Sources used for reasons, quotes and cases, never for proportions:
  social posts, reviews, webinars, interviews, HN.

### 5.1 Sources

| Family | Examples | Used for |
|---|---|---|
| Buyer universes | FDIC and NCUA registers, ECB and EBA lists, MAS, RBI, OJK, SBV, BNM, BOT, BSP, APRA lists, hospital and insurer registers, government directories | How many possible buyers per category, segment, region |
| Vendor disclosures | Annual reports and 10-Ks, investor decks, customer counts, customer stories, press releases (SAP, Oracle, IBM, Temenos, Infosys Finacle, Fiserv, FIS, Jack Henry, Guidewire, Duck Creek, Epic, Oracle Health, Infor, Sage and others) | Named users, counts, regions |
| Systems integrators | Accenture, TCS, Infosys, Wipro, Cognizant, Deloitte, Capgemini, NTT Data case studies | Named users, project length, cost |
| Government purchasing | USAspending, SAM.gov, TED (EU), Contracts Finder (UK), GeBIZ (SG), GeM and CPPP (IN), LPSE and INAPROC (ID), muasamcong (VN), MyProcurement / ePerolehan (MY), e-GP (TH), PhilGEPS (PH), AusTender (AU) | Named public buyers, contract length and value |
| Job posts | Public job boards and ATS pages: LinkedIn public listings, Indeed, MyCareersFuture (SG), Naukri (IN), JobStreet (ID, MY, PH), Seek (AU), TopCV / VietnamWorks (VN), JobsDB (TH) | Which companies run which system, by industry, size, region; skills scarcity (S4) |
| Events and webinars | User groups (ASUG, OAUG, Quest), vendor conferences, webinar speaker and sponsor lists | Named users, active usage |
| Reviews | G2, Gartner Peer Insights, Capterra, TrustRadius public pages | Pain (S3), segment |
| Social | Reddit, public LinkedIn and X posts, found through search | Pain, reasons to stay |
| HN | The 605,125-comment sample from the HN study, re-read for legacy-tool mentions | Pain, builder attempts |
| Challengers | Funding announcements, company sites, customer stories, founder interviews and podcasts, filings where public | Challenger map and deep dives |

### 5.2 Rules

- Official APIs and bulk downloads first. Scrape only public pages, respecting robots.txt
  and site terms, at polite rates. No logins, no paywalls, no paid data.
- The repo stores URLs, dates, short quotes under 30 words, and derived labels. It does not
  redistribute full third-party text or personal data. Personal names appear only for public
  figures quoted from public sources (founders, executives speaking at events).
- Every number on the site links to the rows that produced it.

## 6. Estimates

Each category gets, per region and segment where evidence allows:

- **Companies using**: a range (low, high), built by triangulating at least two source
  families, for example share of a buyer universe seen in job posts and tenders, scaled by a
  documented detection rate, cross-checked against vendor-disclosed counts.
- **People using**: a range from companies times typical seat counts from vendor or SI
  sources. Shown only where seat evidence exists.
- **Grade**: A when 3 or more independent families agree within 2x, B for 2 families,
  C for one family or a modelled number. Grade C numbers are labelled as rough.

Assumptions sit in one config file per category, so any reader can rerun the arithmetic.

## 7. Jev

Jev (TypeSafe, non-generative classifier) does the bulk labelling. Questions are choice,
score or probability. Planned uses:

1. Job posts and pages: which category and legacy system, which industry, which segment.
   Region usually comes from metadata and needs no call.
2. Tenders and SI or vendor stories: is a legacy system named as in use, being replaced, or
   neither.
3. Reviews, social posts and HN comments: firsthand pain with a legacy system, and the
   reason for staying (choice list from section 1, question 4).
4. AI fit: share of a category's core tasks that are reading, sorting, form-filling or
   reconciling, scored over task descriptions.

Cost control, carried over from the HN study:

- Rule filters and keyword prefilters run first, free. Jev sees only candidates.
- Packed calls (several items per call), shortest text window that answers the question.
- `configs/budgets.toml` holds per-stage caps and an `account_total` that only Hansel sets.
  Target: **under $25 total**, the same as the HN study.
- A pilot measures real cost per item before any main run.
- Blind audit: a separate Claude agent labels a random sample without seeing Jev's answers.
  Agreement is published. Disclosed as model labels, not human labels.

**Gate:** before the first paid call, the pre-Jev phase measures real item counts per
source and prints a cost estimate. Hansel decides the credit amount from that number.

## 8. Ranking

Each category scores 1 to 5 on five parts, with a written rubric per part:

| Part | Direction | Main evidence |
|---|---|---|
| Size | + | Companies using times spend per company |
| Pain | + | S3 evidence, reviews, social, HN |
| AI fit | + | Jev task scoring |
| Lock-in | penalty | Regulation, switching cost, contract length |
| Crowding | penalty | Count and funding of AI-native challengers |

Default weights are equal. The page shows every part beside the total, and readers can
re-weight in the browser. The written findings use the default weights only.

## 9. Challenger map and deep dives

- **Challenger map**: every AI-native company found per category, with founding year, funding,
  strategy (section 10) and evidence of traction.
- **Deep dives**: 6 to 8 very deep cases, chosen from top-scoring categories where a
  challenger has real traction (funding and named customers), plus 1 or 2 cases that stalled
  or failed. Each covers: origin and founders' insight, first wedge, first 10 customers, how
  big it is now (funding, headcount, revenue where public), what made it hard (regulation,
  data migration, sales cycle, incumbent response), strategy, and what others can copy.
  Every claim is sourced; anything inferred is labelled as inferred.

## 10. Replacement playbook

Strategies times stages.

- Strategies (expected, confirmed by the cases): overlay on top of the old system; win the
  greenfield (new customers the incumbent ignores); AI-run service that sells the outcome;
  buy the legacy vendor or its book; migration-led (win on moving the data).
- Stages: first wedge, first 10 customers, expand, replace the core.
- Each cell cites the cases that did it and where it broke. Each category on the map lists
  which strategies fit it.

## 11. Site (byhansel.com)

- **Observatory page** at `/observatory`: one card per study, with title, one key number, a
  one-line finding and a small live preview of its lead chart. Clicking the observatory
  building in the garden opens it. The building's label becomes "Startup Opportunities".
- The HN study keeps `/hn-opportunities` and its title becomes
  "Startup Opportunities from Hacker News" where it is listed.
- **Study page** at `/legacy-software`: same frame as the HN study (opener with key facts,
  chapter rail, exhibits). Chapters: thesis, the map, the score table with re-weighting and
  category detail, the challengers, the playbook, method.
- **Deep-dive pages** at `/legacy-software/<slug>`, linked from the map and the playbook.
- Visual first: each chapter opens with one exhibit from the existing visualization
  catalogue and a one-sentence finding. Text stays short. Copy follows `brand/` voice rules:
  no em dashes, leads with what the reader learns.
- Data flows like the HN study: the atlas repo exports finished chart JSON; the site copies it
  in at build time through a script under `scripts/legacy/`.

## 12. Repository

Public repo `hanselhansel/legacy-software-atlas`, local at
`~/conductor/repos/legacy-software-atlas`. Python with uv, same tooling as the HN atlas.

```
configs/        budgets.toml, prices.toml, categories/<slug>.toml (assumptions)
data/raw/       fetched sources (git-ignored when large or third-party)
data/derived/   parquet tables: evidence rows, labels, estimates, scores
research/       categories/<slug>.md, vendors.md, challengers.md, sources.md
cases/          deep dives, one markdown file each
playbook/       strategies and stages
src/lsa/        collectors, jev client, estimation, scoring, exports
exports/site/   chart JSON the site reads
scripts/verify.sh  gitleaks, ruff, pytest (local only, no GitHub Actions)
```

Code is MIT. Derived labels and aggregates are CC BY 4.0. Third-party text is not
redistributed.

## 13. Who does what

- Claude (Opus): plans, writes Devin briefs, does the independent desk research and the deep
  dives, reviews every diff, runs verification, ships.
- Devin CLI (`devin -p --model swe-2-max`): one bounded task per lane in its own worktree,
  for collectors, the Jev pipeline, estimation, exports and site pages.
- Dynamic workflows: fan-out desk research across categories, vendors and challengers.
- Jev: bulk labelling as in section 7.
- Codex: images if any are needed.

## 14. Phases and gates

1. **Setup**: repo, tooling, verify gate, README.
2. **Pre-Jev research**: category long list with the legacy test, vendor map per category,
   source inventory per region, buyer universes, challenger long list. Collectors fetch raw
   items and count them. Output: real volumes and a Jev cost estimate.
3. **Gate: Jev credit.** Hansel sets `account_total`.
4. **Jev passes**: pilot, main runs, blind audit.
5. **Estimates and scores.**
6. **Deep dives and playbook.**
7. **Site**: observatory page, building label, study page, deep-dive pages.
8. **Release**: full local verify in both repos, gstack `/ship` then `/land-and-deploy`
   for the site, live checks.

Work stops for Hansel only at the Jev credit gate, or when a finding would change the
research direction (for example the legacy test cuts the map below 15 categories, or a
region has no usable free sources).

## 15. Out of scope

Paid data, interviews, surveys, non-public sources, live updating, translation of the site.
