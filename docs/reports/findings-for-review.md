# Legacy software ready for replacement: findings for review

Data: `/Users/hansel/conductor/repos/legacy-software-atlas`, branch `chore/bootstrap` at a629123 (not merged to main). Source paths below are relative to it. Total = 35 + 5 x (size + pain + AI fit - lock-in - crowding), each part 1 to 5. Size counts possible buyers, meaning organisations or sites, summed across 11 regions on a scale that tops out at 100,000.

## The answer in five lines

1. The highest-scoring categories are ordinary back-office software with many buyers. Permits, construction accounting and manufacturing ERP score 55 or more under every size view tested. They are not openings: AI-native challengers with traction already sell in all three (4, 3 and 5), and each has crowding 4 or 5.
2. The famous cores (mainframes, insurance, pensions, telecom billing) sit at the bottom. All 13 categories with lock-in 4 or 5 score 45 or less.
3. AI-native challengers mostly sit on top of the old system. 119 of 177 AI-native rows are overlays (113 of about 166 companies).
4. None of the eight deep dives has replaced a dominant core. The closest ran the work themselves first.
5. Read the ranking as tiers. Pain is barely measured, 126 of 146 usage estimates are grade C, and two of the top five (agriculture and medical billing) lean on Indian registers.

## Ten findings

1. **Old cores are nearly universal. Strong evidence of workarounds is rare.** 34 of 35 kept categories have strong evidence of a core built before about 2005. Only 3 have strong workaround evidence: agriculture, permits and medical billing. The scoring adds 2 pain points for strong workaround evidence, and that is the only reason those three have pain 3. Their top-five rank follows from the rule and is not an independent finding. Kept categories were also chosen for having at least one strong sign. Source: `research/categories.csv`. Confidence: solid.
2. **Three leaders hold under every size view.** Permits (60), construction accounting (55) and manufacturing ERP (55) stay at 55 or more without India's registers and when size counts only regions with usage evidence. Source: `exports/site/scores.json`, recomputed from `research/buyer_universe.csv`. Confidence: fair.
3. **The famous cores rank last.** All 13 categories with lock-in 4 or 5 score 45 or less, and 11 score 40 or less. Source: `exports/site/scores.json`. Confidence: solid.
4. **Size does most of the sorting.** All 14 size-5 categories score 45 or more. Only 3 of the other 21 reach 50. Pain is 2 in 28 categories, AI fit 4 in 24, crowding 5 in 22. Source: `exports/site/scores.json`. Confidence: solid.
5. **Two of the top five lean on Indian registers.** India's e-NAM list is 88% of agriculture's 156,496 possible buyers, and the list's own note says the enterprise buyer set is much smaller. India's health facility register is 261,270 of medical billing's 299,652 possible buyers (87%), and it counts facilities, not organisations. Without India, agriculture scores 55 and medical billing 50. Under view (b), medical billing scores 45. Hospital EHR is 97% India (465,000 of 479,537, counting clinics, labs and pharmacies) and falls from 45 to 40 without India. Source: `research/buyer_universe.csv`. Confidence: solid.
6. **The size fix moved 20 of 35 categories.** Courts fell from first (60) into a tie at 45. Agriculture and medical billing rose 10 each. Tax administration rose 5 once a double count is removed (10 as published, see "Buyers" below). That makes the tie at 45 nine categories, not ten. No other part changed. Source: `exports/site/scores.json` at 8a0651b and a629123. Confidence: solid.
7. **Overlay is the default AI-native play.** 119 of 177 AI-native rows overlay the incumbent. 3 lead with migration and 1 with acquisition. The rows cover about 166 companies, 113 of them overlays (68%), so the ratio holds. Source: `research/challengers.csv`. Confidence: fair (it measures the study's coverage).
8. **AI-native outcomes are too young to judge.** 73 of 177 AI-native rows are early, against 23 of 259 others. Traction runs 51% to 60% across the three main AI-native strategies. Source: `research/challengers.csv`. Confidence: fair.
9. **No deep dive has replaced a dominant core, and platforms now ship the wedges.** Valon's first whole-shop buyer left an in-house core, not MSP. Rillet's share is an inference. About 180 switches (30% of 600+ customers, from the CEO's own customer mix) come from NetSuite and Intacct, and dividing them by NetSuite's base alone gives about 0.4%. The playbook says this overstates share. Epic now codes some specialties itself, and AWS gives its mainframe agent away. Outside the deep dives, some companies have replaced cores: PennyMac, Kraken and Thought Machine. Source: `cases/valon.md`, `cases/rillet.md`, `cases/akasa.md`, `cases/bloop.md`, `playbook/playbook.md`. Confidence: solid for Valon, Epic and AWS. Thin for Rillet's share.
10. **The playbook's shortlist rule returns four categories, and three of them sit on the cut-off.** The rule: score 50 or more, with two or fewer AI-native challengers with traction. It returns agriculture (60) and core banking, mortgage servicing and trade finance (50 each). Those three are part of a seven-way tie at rank 6. Under view (b), they fall to 45 and agriculture falls to 50, so only agriculture passes. Few AI-native challengers does not mean an empty market. All four have non-AI challengers with traction. Source: `exports/site/scores.json`, `research/challengers.csv`. Confidence: thin.

## The ranking

The table has twelve rows because seven categories tie at 50. "Before" is the export before the size fix.

| # | Category | Total | Before | Size | Pain | AI fit | Lock-in | Crowding |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1= | Agriculture and commodity trading | 60 | 50 | 5 | 3 | 4 | 3 | 4 |
| 1= | Licensing and permits | 60 | 55 | 5 | 3 | 4 | 3 | 4 |
| 3= | Construction project accounting | 55 | 55 | 5 | 2 | 4 | 3 | 4 |
| 3= | Manufacturing ERP | 55 | 50 | 5 | 3 | 3 | 2 | 5 |
| 3= | Medical billing and revenue cycle | 55 | 45 | 5 | 3 | 4 | 3 | 5 |
| 6= | Core banking | 50 | 45 | 4 | 2 | 4 | 3 | 4 |
| 6= | Financial close and GL | 50 | 50 | 5 | 2 | 4 | 3 | 5 |
| 6= | Mortgage servicing | 50 | 55 | 4 | 2 | 4 | 3 | 4 |
| 6= | Payroll and HR | 50 | 50 | 5 | 2 | 4 | 3 | 5 |
| 6= | Procurement and AP | 50 | 50 | 5 | 2 | 4 | 3 | 5 |
| 6= | Trade finance | 50 | 50 | 3 | 2 | 4 | 3 | 3 |
| 6= | Wholesale distribution ERP | 50 | 45 | 5 | 2 | 3 | 2 | 5 |

Pain is the only part that separates the two leaders from construction accounting.

**Three surprises**
- **Agriculture ties for first and medical billing ranks third, both on Indian registers.** Agriculture rose 10 points on possible buyers, and 88% of them come from India's e-NAM register of mostly small traders. Its only AI-native challenger with traction is CommodityAI, at an estimated $330K ARR. Medical billing rose 10 points the same way: 87% of its possible buyers are Indian health facilities.
- **Mainframe COBOL, the archetype of legacy, ties for last at 35.** Lock-in 5 and crowding 5 cancel everything else.
- **Core banking has no AI-native challenger with traction, but it is not an empty market.** 6 of its 8 challengers are non-AI cores, and Visa and Fiserv bought two of them. Thought Machine alone runs 68 banks, 18 of them tier 1.

**Three that fell after the size fix**
- **Courts, 60 to 45.** The old size used a 300,000 figure from one Victorian court system. Counted in buyer units, there are about 118 court systems across 11 regions. Size went from 5 to 2.
- **Land registry, 55 to 45.** The old size used 2.6 million from one Queensland titles system. Possible buyers are 3,308, of which 3,031 are US county governments. Size went from 5 to 3.
- **Government benefits, 50 to 40.** The old size summed vendor figures to 6,600,152. Possible buyers are about 3,470, of which 3,000 are EU social security institutions. Size went from 5 to 3.

Telecom billing, pensions and mainframe COBOL also fell 10 points.

### Where to look next, re-derived

This uses the playbook's rule (50 or more, at most two AI-native challengers with traction) on the new scores. Trade finance passed the rule before too. The playbook dropped it because funded overlays already do the document checking. It is listed here because the rule is mechanical, and that reason is its doubt.

| Category | Total | View (b) | AI-native with traction | Check first |
|---|---:|---:|---:|---|
| Agriculture and commodity trading | 60 | 50 | 1 | The India register (finding 5). Bushel, which is not AI-native, already serves 2,600 grain facilities (the buyer universe lists 7,922 US facilities) and has raised at least $73M. Gro Intelligence raised over $117M and closed in 2024. |
| Core banking | 50 | 45 | 0 | Non-AI cores already win here: Thought Machine (68 banks, 18 of them tier 1, more than $100M revenue), Mambu, 10x and Zeta. Both AI-native rows are early. Maximum is pre-revenue with no named banks. |
| Mortgage servicing | 50 | 45 | 2 | The buyer count leaves out US nonbank servicers, yet every named Valon buyer (Newrez, Carrington, ServiceMac) is a nonbank. Sagent's Dara and Thought Machine already compete. PennyMac replaced MSP with its own system. No MSP shop has confirmed a move to an AI-native core, and Wells Fargo renewed MSP in September 2026. |
| Trade finance | 50 | 45 | 1 | Overlays already check documents for J.P. Morgan, Lloyds and Citi. Non-AI Traydstream serves Deutsche Bank, SMBC and Citi. HSBC built its own. |

Courts, land registry and benefits drop out. The three stable leaders fail the rule because AI-native challengers already sell there: 4 with traction in permits, 3 in construction accounting and 5 in manufacturing ERP. Each also has crowding 4 or 5.

## What the deep dives teach

- **Adaptive.** An overlay on builders' existing ledgers grew from about 10 paying customers to 750+ companies (September 2026). It claimed more than 1,000 in February 2026, so treat the count as unstable. It replaced hours, not ledgers.
- **AKASA.** Hospital billing money goes to overlays that own one auditable step. Olive AI raised over $900M automating clicks and shut down.
- **bloop.** A co-founder said bank cycles of 18 to 24 months outran its runway. bloop pivoted to Vibe Kanban in June 2025, and that successor company shut in April 2026.
- **GovWell.** Greenfield wins where a council vote is the procurement. It has a three-month median sales cycle, 200+ agencies, and 21 of 71 staff in deployment and support.
- **Mechanical Orchard.** When code is cheap, proof of equivalence is the product. It has retired applications but no whole mainframe yet.
- **Rillet.** A new ledger sells at a forced moment: outgrowing QuickBooks. Only about 180 of 600+ customers left NetSuite or Intacct.
- **Trade-finance networks.** Products that pay back only when every party switches die. Three bank consortia failed, and single-bank checkers won.
- **Valon.** Running a licensed servicer on its own core was the pitch. The first whole-shop sale took about six years and went to a related party.

## What the data cannot say yet

- **Pain.** HN gives 68 firsthand-pain matches across 35 categories, 44 of them mainframe. Two categories reach the HN bar of 5 comments, and two reach the 30% job-post bar.
- **Usage.** 126 of 146 regional estimates are grade C, and none is grade A. Global vendor rows have no buyer cap, so five categories show more users than possible buyers.
- **Buyers.** Size sums organisations or sites (`BUYER_UNITS` in `src/lsa/estimates.py`) across all 11 regions, including regions with no usage evidence.
  - 73 of 525 universe rows count sites or establishments. Examples: construction US (953,703 BLS establishments), wholesale distribution US (627,800), India health facilities, and US grain storage sites.
  - Mortgage servicing leaves out US nonbank servicers.
  - Tax administration counts US local governments twice. The US row's high end (91,492) already includes 91,438 local governments, and a separate "US (local)" row adds them again. Removing either row gives size 4 and a total of 40.
  - Smaller overlaps move no score: utility billing US, trade finance US and cooperative banking India.
- **Size scale.** The scale tops out at 100,000 possible buyers. Fourteen categories score 5. They range from financial close at 116,211, which clears the line only by counting UK medium firms, to payroll at 54 million. Size does most of the sorting (finding 4), so the top tiers cannot tell a large market from a very large one.
- **Crowding.** It counts every challenger, AI-native or not, and the count tops out at 9 rows, which 29 categories reach. At least 11 rows count purchase prices or valuations as funding. Removing them all moves only wholesale distribution ERP, from 50 to 55. The 55 tier would then hold four categories and the 50 tie six. The 11 rows:
  - Pismo (card payments) and Pismo (core banking)
  - Finxact, $650M
  - Acumatica, $2B
  - Plex, $2.22B
  - EvolutionIQ, $730M
  - Assured, $1B valuation
  - Rocket Software, $2.275B (Rocket's own purchase of another business)
  - IKS Health, $557M (its purchase of TruBridge)
  - powercloud, $32M sale price
  - Clearwater, $8.4B take-private

  IBS Software's $450M secondary stake may be a twelfth.
- **Demand.** Blind labellers put about 80% of keyword-matched tenders in no legacy category.
- **Regions.** India has usage evidence in 6 categories and the Philippines in 2. Naukri, Glints and Reddit were unreachable.
- **Outcomes.** Only 19 of 436 rows are stalled or failed. Olive AI, we.trade and Marco Polo are missing.
- **Labels.** The blind audit used Claude agents, not people. Jev rates tasks about half a point more automatable (3.46 against 2.97).
- **Cost.** Calculated Jev spend was $0.40 for 4,839 items (3,319 calls, 9.58M input tokens). The figure comes from a price table, not an invoice. Per item, it ran about 5 to 7 times the plan, which estimated $2.11 for an upper bound of 141,000 items. Full coverage would cost about $14: small, but over the $8 cap in `configs/budgets.toml`. Access problems are the bigger limit.

## Proposed storyline for the site

1. **The highest scores are in the back office.** Permits, construction accounting and manufacturing ERP lead under every size view, and AI-native challengers already sell in all three. Exhibit: ranked dot plot of all 35 totals, with a whisker for the size-view range.
2. **The famous cores rank last.** Mainframes, insurance, pensions and telecom billing have few possible buyers, and the lock-in and crowding penalties sink them further. Mainframe, pensions, telecom and policy admin have size 3, and claims has size 4. Mainframe, pensions and telecom each fell 10 points on size alone. Telecom, at 40, sits above the bottom tier. Exhibit: small multiples, one panel per score part.
3. **Challengers sit on top.** Two in three AI-native rows overlay the old system (113 of about 166 companies). Exhibit: treemap of 436 challenger rows by strategy, shaded by AI-native.
4. **None of the eight cases, and no AI-native row, has replaced a dominant core.** Wedges work. Others have replaced cores (PennyMac, Kraken and Thought Machine, in the playbook's "Replace the core" stage), but none of them is AI-native or a case here. Exhibit: strategy x stage matrix.
5. **Run the work, then sell the software.** Valon ran its own servicer and used it as the pitch. The first buyer was a related party: Newrez, part of Rithm, Valon's anchor investor, which supplied about half its book. The Newrez deal was signed in January 2026, when Valon had about 593,000 loans. Carrington watched from inside for over a year, then bought Valon's servicer in August 2026, at about 810,000 loans. This chapter rests on one case. Exhibit: timeline of a case (Valon).
6. **Where to look next.** Four categories pass the rule, and each carries a doubt. Three sit exactly on the 50 cut-off and fall to 45 under view (b). All four have non-AI challengers with traction. Exhibit: scatter of total score against AI-native challengers with traction. Label the x-axis that way, not "crowding". The crowding score counts all challengers plus funding and is already subtracted in the total.
7. **Count buyers, not records.** Counting records instead of organisations or sites put courts first. Counting buyers moved 20 of 35 categories. Exhibit: slope chart.
8. **What this map cannot see.** Evidence thins outside the US, EU, Australia and Singapore. Exhibit: map of regions, shaded by the number of categories with usage evidence.

## Decisions for Hansel

1. **Which size view leads?** (a) All 11 regions, as published. (b) Only regions with usage evidence: 13 categories fall, agriculture drops to 50, and medical billing drops to 45. (c) Publish (a), with (b) as a whisker on each dot. **Recommend (c):** it keeps the method and shows where the order is fragile.
2. **Name a shortlist?** (a) Name the four. (b) Show the rule as a filter, with its output under both views and each pick's doubt. Under view (a) it returns agriculture (60) and core banking, mortgage servicing and trade finance (50 each, on the cut-off). Under view (b) it returns agriculture alone (50). (c) No shortlist. **Recommend (b):** the rule is mechanical, three picks sit on the cut-off, and every pick has a known caveat and non-AI challengers with traction.
3. **What happens to pain?** (a) Keep as is. (b) Keep, flagged as a weak signal. (c) Drop from the default total until re-measured. **Recommend (b):** pain alone lifts the two leaders above construction accounting, and it comes mostly from the workaround rule, so readers should see how weak it is.
4. **Which case carries the timeline?** (a) Valon. (b) GovWell. (c) AKASA. **Recommend (a):** it came closest to replacing a dominant core. Its caveats carry the honest lesson: a related-party first buyer, one case, and no MSP shop yet.
5. **Launch when?** (a) Now, versioned. (b) After fixing the crowding funding values and the tax administration double count. (c) After India and EU job data. **Recommend (b):** both fixes move a published score (wholesale distribution ERP 50 to 55, tax administration 45 to 40). Access gaps will not close soon, and money is not the main block. Full Jev coverage would cost about $14, which needs only a small raise of the $8 cap.