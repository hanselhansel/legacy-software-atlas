# Which legacy software is ready for AI-native replacement

Review report for Hansel, version 3, rescored. Data as of 5 October 2026. This edition applies three fixes that the first version 3 draft listed as open: one rule for the regulator input, one decimal instead of rounding halves up, and only category-specific rounds in crowding's funding input.

## 0. How to read this report

Section 1 gives the question and the answer on one page. Section 2 explains how the study was done, including the new measures for pain, lock-in and crowding. Section 3 shows all 35 categories in one table and says what moved since version 2 and since the first version 3 draft. Section 4 explains each factor, with one worked example per factor and full tables for pain, lock-in and crowding. Section 4A is new. It answers your question directly: is anything sizeable, painful and a good fit for AI, with low lock-in and low crowding? It answers at the level of categories and at the level of workflows. Section 5 adds your build-versus-buy lens. Section 6 explains where COBOL and mainframe now ranks. Section 7 covers regions. Sections 8 to 10 cover the challengers, the eight deep cases and the playbook. Section 11 names where to look next. Section 12 lists each gap in the study, what this round did to shrink it, and what remains. Section 13 sets out five decisions about the site, meaning the public website that will present the atlas. Section 14 maps every section to its source files. Sections 1 to 13 each start with a short summary in plain words, then the detail.

## 1. The question and the answer in one page

**In short.** The study asked which kinds of old business software an AI-native company could realistically replace, and where a founder should look first. This version measures pain, lock-in and crowding mostly from counts of real events, plus a regulator judgment and the workaround grade, instead of proxies. The order changed a lot. Utility billing leads at 69.5, half a point ahead of mainframe. It is the only category that is sizeable, painful, a good fit for AI, only mildly hard to leave, and lightly crowded by AI-native challengers. Its pass is narrow, and two inputs could each undo it (Section 4A). Mainframe misses by half a point on lock-in, and agriculture misses only on size. The search finds more inside categories, at the level of single workflows that do not touch the core system. Two cautions apply. Low crowding here means few AI-native challengers, not few challengers. And workflow sizes count whole US occupations, so they rank workflows but do not size markets.

**The question.** Which legacy software categories are ready for an AI-native company to replace, and where should a founder look first?

Terms used throughout:
- **Legacy software**: a system whose core was built before about 2005 and is slow and costly to replace.
- **Category**: one job that software does for a buyer, such as core banking or payroll.
- **Core system**: the system of record, meaning the system that holds the official data, such as the ledger or the policy file.
- **Workflow**: one piece of work inside a category, such as bill disputes in telecom billing. The study lists six per category, 210 in all.
- **AI-native challenger**: a company the study labels as built around AI from the start, selling into a legacy category.
- **Legacy spend**: what buyers worldwide pay each year for systems in a category that are still legacy.
- **Buyable spend**: the part of legacy spend held by buyer segments that normally buy the software rather than build or own it. Section 5 explains the split.
- **ERP**: enterprise resource planning, the software that runs a firm's finance, orders, inventory and production in one system.
- **Critical and important**: a category is **critical** when two things are both true: the business stops or loses its licence if the system fails, and the system is where the firm competes. It is **important** when only the first is true: the business depends on it but does not compete on it. Payroll is the standard example. 22 categories are critical and 13 are important.
- **Ranking into fifths**: the new measures score each input 1 to 5 by where the category sits against the other categories. The bottom fifth scores 1 and the top fifth scores 5. Pain, lock-in and crowding are averages of these input scores, kept to one decimal, so they read like 3.6. Section 2 explains the rule.

**Headline conclusions**

1. **The map is unchanged.** 35 of 46 candidate categories passed a strict legacy test. Their legacy spend adds to about $178B a year on midpoints, or $118B to $271B if you add the low and high estimates. Categories range from $0.4B (port terminals) to $18.6B (telecom billing).
2. **The ranking now spreads out.** Scores run from 31 to 69.5 on a 0 to 100 scale. Utility billing leads at 69.5 and mainframe follows at 69. Manufacturing ERP and construction project accounting come next at 67, then telecom billing and government tax administration at 66.5. In version 2 the range was 30 to 50, with five categories tied at the top.
3. **The new measures moved the order more than any new market fact.** The rank correlation between the version 2 totals and these totals is 0.28. A rank correlation measures, from -1 to 1, how closely two lists agree on order, and 1 means the same order. The average total rose from 41 to 56. Only medical billing fell, from 45 to 42.5. Most of the rise comes from crowding. Its average fell from 4.6 to 2.9, because two of its three inputs now count only AI-native companies (the third counts all recent Y Combinator companies) and each input ranks categories into fifths.
4. **One category passes all five search tests, narrowly.** Utility billing has $2.5B of legacy spend, all of it buyable, with pain 3.6, AI fit 4, lock-in 2.0 and crowding 1.7. Two things could each undo the pass: AI fit 4 uses Jev's score, which runs about half a point high, and lock-in sits exactly on the 2.0 line, where one non-competitive award would tip it (Section 4A). Mainframe misses only on lock-in, by half a point (2.5). Agriculture misses only on size. Construction accounting (crowding 3.3), telecom billing and student information systems (lock-in 3.5 each) miss on one test by more.
5. **Workflows widen the search.** 130 of 210 workflows do not touch the core system. 55 of those have no AI-native funding round mapped to them in 24 months. Each round is mapped to one workflow, and the six exits and stake purchases in the rounds list are left out. 16 of the 55 also sit in categories with pain 3 or more and show AI usage at or above the median. Collections and arrears work recurs: five of the 16. Customer contact appears twice, and billing disputes and inquiry lookups once each.
6. **Mainframe rises to 69, but its money is still mostly not for sale.** Lock-in fell from 5 to 2.5 and crowding from 5 to 2.0. Both drops partly reflect what the new measures leave out (Section 6). Only $0.6B of its $14.5B is buyable.
7. **The build-versus-buy and challenger findings are unchanged.** $42.5B (24%) of legacy spend sits with buyers who usually build or own the system. Mid-sized firms are the best first buyer in most categories but hold only $20.6B (12%) of the spend, against $100.0B (56%) for large enterprises. 119 of 177 AI-native challenger rows work on top of the old system rather than replace it. None of the eight deep cases has displaced a market-leading core.
8. **Three fixes since the first version 3 draft moved some categories a whole tier.** A single regulator rule dropped airline reservations from 70 to 56.5 and lifted government tax administration from 55 to 66.5. Keeping one decimal lifted mainframe from 65 to 69. Counting only category-specific rounds cut telecom billing's crowding from 2.7 to 1.7. Section 3 explains each fix.

**How much to trust this.** Pain, lock-in and crowding now rest mostly on counts: 2,718 app reviews, 438 apps, 1,922 public contract awards, 353 replacement projects, 298 AI-native funding rounds and 1,939 Y Combinator companies. They also use a yes-or-no regulator judgment, now coded with one rule for all 35 categories, and the old workaround grade, and the app rating is a proxy for pain. Coverage is uneven. Lock-in for 25 of 35 categories rests on only two inputs, so one regulator answer moves it by 2 points. Crowding ignores modern challengers that are not AI-native, such as Kraken in utility billing. The workflow labour values count every US worker in an occupation, across all industries, and sum to $6.3T over 210 workflows. Read the ranking as three tiers, not 35 places.

## 2. How we did it, in plain steps

**In short.** Steps 1, 2, 4 and 5 are the same as in version 2. Step 3 changed. Pain, lock-in and crowding are now each the average of several measured inputs, and each input ranks categories into fifths. A new step 6 scores 210 workflows inside the categories. All the paid labelling so far cost $0.67.

**Step 1. Choose categories and apply a strict legacy test.** We started with 46 candidates: 38 seeded and 8 added for Asia Pacific coverage. Each was checked for four signs of legacy, and each sign needed a cited source:
- **Pre-cloud core**: the main systems first shipped before about 2005 as mainframe, midrange or on-premise client-server.
- **Slow to replace**: replacement is a multi-year program, or contracts run 7 years or more.
- **Workarounds**: users report spreadsheets, re-keying or screen-scraping around the system.
- **Shrinking skills**: jobs for the system's skills are hard to fill or skew to older staff.

Each sign was graded strong, weak or not met. A category stayed only if it had at least one strong sign and its strong signs plus half its weak signs reached 2.5. 35 stayed and 11 were dropped: accounting firm practice, anti-money-laundering compliance, civil registration and ID, e-invoicing, freight forwarding and customs, hotel management, law firm practice, pharmacy, real estate property management, regulatory reporting, and transport management. A fact-check opened 256 key citations, and 232 (91%) held.

**Step 2. Size each category by legacy spend.** For each category we took global annual spend on that kind of software, mostly for 2025, from analyst reports and vendor revenue. We multiplied it by the share still on legacy systems, which gives a low and a high figure. The midpoint is the geometric mean of the two: the square root of low times high, which sits closer to the low figure than a plain average does. A second, bottom-up figure (possible buyers times spend per buyer) is used only to split the total by region and by buyer size. It does not set the total.

**Step 3. Score five factors.** Each factor scores 1 to 5. Size and AI fit work as in version 2:
- **Size**: the legacy spend midpoint, in bins. Under $0.1B scores 1, under $1B scores 2, under $5B scores 3, under $20B scores 4, and $20B or more scores 5.
- **AI fit**: Jev, the classifier described below, scored 12 core tasks per category for how much of each AI could do. The scores are weighted by how much time each task takes, averaged and rounded.

Pain, lock-in and crowding are new. Each is built in three moves:
1. **Measure.** Each input gets a raw value per category, plus a count of the observations behind it, called n. An input with fewer observations than its minimum is left out for that category.
2. **Rank into fifths.** For each input, count how many other categories with data have a lower raw value. Divide that count by the number of categories with data, multiply by 5, drop the fraction and add 1. With all 35 categories, a category scores 1 when fewer than 7 others are lower, 2 for 7 to 13, 3 for 14 to 20, 4 for 21 to 27, and 5 for 28 or more. For app rating the order is flipped, so a lower rating counts as more pain. Tied categories share the lower score. Two inputs skip this step and score directly: the workaround sign and regulator approval.
3. **Average.** The factor is the average of the available input scores, kept to one decimal. The first version 3 draft rounded it to a whole number with exact halves rounded up. That is fixed (Section 3).

The inputs:

| Factor | Input | What it is | Source | Categories with enough data | Observations |
|---|---|---|---|---:|---:|
| Pain | Keep-alive share | Share of public IT contract awards for the category that maintain or extend the old system rather than replace it | Public award databases in the EU, US, Singapore, UK and Australia (1,922 awards), labelled by Jev | 13 (minimum 10 awards) | 423 awards labelled maintain, extend or replace |
| Pain | Backend-failure share | Share of app reviews that complain about outages, downtime, failed or delayed transactions, wrong balances or sync errors | Apple App Store reviews of the category's customer-facing apps, labelled by Jev | 18 (minimum 50 reviews) | 2,718 reviews |
| Pain | App rating, inverted | Average star rating of the category's customer-facing apps. A lower rating scores higher | Apple App Store, 482 listings across 19 storefronts in 11 regions | 30 (minimum 3 apps) | 438 apps |
| Pain | Failed or overrun replacements | Share of documented replacement projects that were cancelled, rolled back, or finished late or over budget | A ledger of 353 projects built from company filings, audit reports and press | 35 (minimum 3 cases) | 353 projects |
| Pain | Workaround sign | The workaround grade from the legacy test. Strong scores 5 and weak scores 3 | Step 1 | 35 | 3 strong, 32 weak |
| Lock-in | Contract length | Median length, in months, of public awards for the category | The same award databases | 8 (minimum 10 awards) | 281 awards with a length |
| Lock-in | Non-competitive share | Share of awards made without open competition (negotiated without a competition, or awarded directly) | The same award databases | 9 (minimum 10 awards) | 272 awards with a known procedure |
| Lock-in | Replacement time | Median months a documented replacement took | The replacement ledger | 35 (minimum 3 cases) | 228 projects with a duration |
| Lock-in | Regulator approval | Yes if, in the US, EU or UK, a sector regulator must approve, or be formally told in advance of, replacing or outsourcing the core system. Yes scores 5 and no scores 1 | Research per category, with cited rules, recoded to this one rule | 35 | 17 yes, 18 no |
| Crowding | AI-native with traction | Number of AI-native challengers with named customers or reported revenue | The challenger table (Step 4) | 35 | 92 challengers |
| Crowding | AI-native funding per $1B | Disclosed AI-native funding rounds aimed at the category in the 24 months to 2 October 2026, divided by the category's legacy spend in billions | A list of 298 rows, 268 with amounts, $11.0B in all. 284 are category-specific rounds (260 with amounts, $9.0B). The other 14 are company-wide raises or exits and do not count (see below) | 35 | 284 rounds |
| Crowding | Y Combinator companies | Companies from Y Combinator's 2024 to 2026 batches that sell software doing the category's work, AI-native or not. Y Combinator is a startup accelerator | Y Combinator's public company list (1,939 companies, 3 of them from early 2027 batches), labelled by Jev | 35 | 316 companies |

A median is the middle value when the values are sorted. Size and AI fit did not change, and still score whole numbers. The total is still 35 + 5 x (size + pain + AI fit - lock-in - crowding), which puts every possible result on a 0 to 100 scale. Because pain, lock-in and crowding keep one decimal, totals move in half points. Utility billing, for example, is 35 + 5 x (3 + 3.6 + 4 - 2.0 - 1.7) = 69.5. All five factors are weighted equally, and so are the inputs inside each factor.

**Changes from the approved plan.** Three definitions differ from plan 3, and the plan did not record the change:
- **Failed or overrun replacements** is a share of all documented cases. The plan defined it as a count per $1B of legacy spend.
- **Keep-alive share** is a share of award counts. The plan defined it as a share of public IT spend.
- **Regulator approval** counts a replacement that a regulator must be formally told about in advance as well as one it must approve. The plan defined it as "regulator approval required". Since the rescore, one written rule applies to all 35 categories, limited to the US, EU and UK.

**Company-wide raises and exits in the rounds list.** Each of the 298 rows now carries a scope. 284 are rounds aimed at the category. 8 are company-wide raises by companies that sell across many industries, $2.0B in all: Sierra's two raises and Wonderful's three in telecom billing, Quantexa in tax administration, Ambience in medical billing and Lumi in retail. 6 record an exit or a stake purchase rather than a funding round: Learned Hand's sale to Clio, BHC Global's majority purchase of POWERCONNECT.AI, a private-equity majority stake in Arkstone, New Mountain Capital's control investment in SmarterDx, and a strategic minority stake in Valon (listed under two categories). None of the exits has a disclosed amount. Only the 284 count toward funding per $1B, in money and in number of rounds. Workflow crowding still counts every row. Section 4A leaves out the exits there.

**Step 4. Map who already sells replacements.** We listed 436 challenger rows, one per company and category, covering about 417 companies. Each row records a strategy, whether the company is AI-native, and a status:
- **Traction**: named customers or reported revenue.
- **Early**: launched or piloting, too soon to judge.
- **Acquired**: the challenger itself was bought.
- **Stalled**: still operating but losing ground or inactive.
- **Failed**: shut down or left the category.
- **Pending**: the outcome is unresolved. This applies to one row, GROW.

**Step 5. Write deep cases and a playbook.** We wrote eight deep cases, six on companies with real traction and two on failures. From them and the challenger table we drew a playbook of strategies by stage.

**Step 6. Score workflows.** Research split each category into six workflows and named the occupations that do each one, with the share of their time it takes. Each workflow gets:
- **Labour value**: US employment in those occupations, times their mean annual wage, times the time share. Employment and wages come from the US government's occupational employment and wage survey (OEWS). Tasks come from O*NET, the US Labor Department's database of tasks per occupation. The figure counts every US worker in those occupations, in every industry, not only those in the category.
- **AI usage**: the Anthropic Economic Index task penetration figure, averaged over the workflow's O*NET tasks. The Economic Index is Anthropic's public dataset of which work tasks show up in Claude usage. Task penetration is a 0 to 1 figure per task for how much of Claude usage that task accounts for. Higher means more of the work already shows Claude use. It covers Claude only, not AI use in general. 51 of 210 workflows score 0.
- **Touches core**: a research judgment on whether the work changes the system of record. 80 workflows do and 130 do not. This stands in for lock-in.
- **Crowding**: how many AI-native rounds research mapped to this workflow. Each round is mapped to exactly one workflow. 297 of the 298 rounds are mapped, and one card-processing round maps to no listed workflow. 96 workflows have none. Six of the mapped rows are exits or stake purchases and eight are company-wide raises (see above).
- **Pain**: the category's pain score, to one decimal.

The **opportunity index** ranks each workflow against the other 209 on labour value, AI usage and pain, where higher is better, and on crowding, where higher is worse. It adds the first three ranks and subtracts the fourth. A workflow that touches the core gets a penalty large enough to put it at or below every workflow that does not. One core-touching workflow ties at -109 with the lowest workflow that does not touch the core (title search). The index runs from -644 to 498. Pain now ranks on one decimal, so the index differs from the first version 3 draft.

**Cost and audit.** The bulk labelling was done by Jev, a non-generative classifier sold by TypeSafe. The study has no affiliation with TypeSafe. Jev labelled job posts, tenders, vendor and integrator stories, Hacker News comments, AI fit, and this round's contract awards, app reviews and Y Combinator companies. It cost $0.67 in total over 5,023 calls, well inside the $8 cap. This round ran four labelling runs (awards, app reviews, and Y Combinator twice, once per wording). They cost $0.26 over 1,704 calls, covering 6,576 distinct items and 8,515 item labels. Separate Claude agents labelled samples blind, without seeing Jev's answers. The award audit used a random sample. The app review and Y Combinator audits each used 30 random items plus 30 that Jev had labelled positive, so their agreement figures overweight positives and are not agreement across the whole population. The bar was 80% agreement. Questions under it were reworded once or dropped. This round's results:
- **Award category**: 92%, used.
- **Award action** (maintain, extend, replace, consult, other): 70% on five choices. Collapsed to keep-alive, replace or other, it reached 83% and was used that way. The collapse was chosen after seeing the audit.
- **App review backend failure**, counted at a probability of 0.7 or more: 87%, used.
- **Y Combinator category**: 67% on the first wording, 85% after one rewording, used. The second score was measured against labels made for the first wording, which already applied the stricter reading.

From earlier rounds, the "reason to stay" question scored 79% and is used only as colour, and the Hacker News pain cut of 0.7 was chosen after seeing its audit. Neither Hacker News comments nor job posts feed the pain score any more. Jev rated tasks about half a point more automatable than the blind labels did.

## 3. The whole map

**In short.** All 35 categories score between 31 and 69.5. Nine sit in the top tier (62.5 to 69.5), 16 in the middle (54 to 61) and 10 at the bottom (31 to 52). The tier lines sit where they did in the first version 3 draft, halfway between its 5-point steps. The penalties, lock-in and crowding, still do most of the sorting. A whole step on any input can still move a total by several points, and one regulator answer moves it by up to 10, so small changes in evidence can move a category a whole tier. Three fixes made since the first version 3 draft did exactly that for a few categories.

Ties are listed by legacy spend. Criticality is defined in Section 1. The v3 column shows each total in the first version 3 draft, before the three fixes. The v2 column shows each total in version 2, including the two corrections that report made for a funding parse bug (telecom billing 40 and laboratory information systems 30).

| # | Category | Legacy spend, USD B: low to high (mid) | Criticality | Total | v3 | v2 | Size | Pain | AI fit | Lock-in | Crowding |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Utility billing | 1.5 to 4.2 (2.5) | Important | 69.5 | 75 | 35 | 3 | 3.6 | 4 | 2.0 | 1.7 |
| 2 | Custom COBOL and mainframe | 11.1 to 19.0 (14.5) | Critical | 69 | 65 | 40 | 4 | 3.3 | 4 | 2.5 | 2.0 |
| 3= | Manufacturing ERP | 6.0 to 12.7 (8.7) | Important | 67 | 65 | 50 | 4 | 4.3 | 3 | 1.2 | 3.7 |
| 3= | Construction project accounting | 0.8 to 1.8 (1.2) | Important | 67 | 70 | 45 | 3 | 3.7 | 4 | 1.0 | 3.3 |
| 5= | Telecom billing | 13.2 to 26.2 (18.6) | Critical | 66.5 | 70 | 40 | 4 | 3.5 | 4 | 3.5 | 1.7 |
| 5= | Government tax administration | 4.5 to 11.2 (7.1) | Critical | 66.5 | 55 | 40 | 4 | 3.3 | 3 | 3.0 | 1.0 |
| 7= | Student information systems | 1.2 to 3.6 (2.1) | Important | 64 | 65 | 40 | 3 | 3.6 | 4 | 3.5 | 1.3 |
| 7= | Agriculture and commodity trading | 0.4 to 1.0 (0.6) | Critical | 64 | 60 | 45 | 2 | 3.0 | 4 | 1.5 | 1.7 |
| 9 | Government benefits | 7.5 to 21.0 (12.5) | Critical | 62.5 | 65 | 45 | 4 | 3.8 | 4 | 5.0 | 1.3 |
| 10 | Core banking | 9.6 to 17.5 (13.0) | Critical | 61 | 60 | 50 | 4 | 2.2 | 4 | 3.0 | 2.0 |
| 11= | Payroll and HR | 6.0 to 15.0 (9.5) | Important | 60.5 | 60 | 45 | 4 | 3.4 | 4 | 3.0 | 3.3 |
| 11= | Licensing and permits | 0.7 to 1.8 (1.1) | Important | 60.5 | 60 | 50 | 3 | 4.4 | 4 | 2.0 | 4.3 |
| 11= | Courts and justice case management | 0.7 to 1.6 (1.0) | Critical | 60.5 | 60 | 50 | 3 | 3.8 | 4 | 3.7 | 2.0 |
| 14= | Laboratory information systems | 0.9 to 2.0 (1.3) | Critical | 58 | 60 | 30 | 3 | 2.8 | 3 | 2.2 | 2.0 |
| 14= | Port terminal operating systems | 0.3 to 0.7 (0.4) | Critical | 58 | 55 | 40 | 2 | 2.3 | 3 | 1.0 | 1.7 |
| 16= | Wealth and portfolio accounting | 2.0 to 4.8 (3.1) | Important | 57.5 | 55 | 40 | 3 | 4.0 | 4 | 3.5 | 3.0 |
| 16= | Pension and provident fund admin | 1.4 to 3.6 (2.2) | Critical | 57.5 | 55 | 35 | 3 | 3.2 | 4 | 4.0 | 1.7 |
| 18 | Trade finance | 0.7 to 2.1 (1.2) | Important | 57 | 60 | 50 | 3 | 1.7 | 4 | 3.0 | 1.3 |
| 19= | Card issuing and processing | 8.4 to 17.6 (12.2) | Critical | 56.5 | 55 | 40 | 4 | 2.0 | 4 | 3.0 | 2.7 |
| 19= | Airline reservations | 2.2 to 4.0 (3.0) | Critical | 56.5 | 70 | 45 | 3 | 2.0 | 4 | 3.0 | 1.7 |
| 21= | Co-op, rural and microfinance banking | 4.0 to 7.8 (5.6) | Important | 55 | 50 | 35 | 4 | 2.2 | 3 | 3.5 | 1.7 |
| 21= | Wholesale distribution ERP | 0.8 to 4.0 (1.8) | Critical | 55 | 55 | 40 | 3 | 4.3 | 3 | 2.0 | 4.3 |
| 21= | Land and property registry | 0.5 to 1.2 (0.7) | Critical | 55 | 45 | 40 | 2 | 2.8 | 4 | 2.5 | 2.3 |
| 24= | Procurement and payables | 3.5 to 9.0 (5.6) | Important | 54 | 50 | 45 | 4 | 2.3 | 4 | 2.5 | 4.0 |
| 24= | Retail point of sale | 3.1 to 8.8 (5.3) | Critical | 54 | 60 | 40 | 4 | 4.0 | 3 | 4.5 | 2.7 |
| 26 | Mortgage servicing | 1.4 to 3.1 (2.1) | Critical | 52 | 55 | 45 | 3 | 1.7 | 4 | 3.0 | 2.3 |
| 27= | Capital markets back office | 1.5 to 4.9 (2.7) | Critical | 50.5 | 50 | 35 | 3 | 1.8 | 4 | 3.0 | 2.7 |
| 27= | Warehouse management | 1.0 to 2.1 (1.4) | Critical | 50.5 | 45 | 35 | 3 | 3.3 | 2 | 1.5 | 3.7 |
| 29 | Financial close and general ledger | 3.0 to 11.2 (5.8) | Important | 46.5 | 45 | 45 | 4 | 2.3 | 4 | 3.0 | 5.0 |
| 30 | Loan origination and servicing | 3.5 to 7.7 (5.2) | Critical | 45.5 | 45 | 45 | 4 | 2.8 | 4 | 4.0 | 4.7 |
| 31 | Field service and maintenance | 1.8 to 3.5 (2.5) | Important | 45 | 45 | 35 | 3 | 3.5 | 3 | 2.5 | 5.0 |
| 32 | Hospital records (EHR) | 9.3 to 17.2 (12.7) | Critical | 43 | 45 | 40 | 4 | 2.8 | 3 | 3.5 | 4.7 |
| 33 | Medical billing | 2.6 to 8.8 (4.8) | Important | 42.5 | 50 | 45 | 3 | 3.7 | 4 | 4.5 | 4.7 |
| 34 | Insurance policy administration | 1.4 to 3.8 (2.3) | Critical | 42 | 40 | 35 | 3 | 2.2 | 4 | 3.5 | 4.3 |
| 35 | Insurance claims | 2.0 to 6.5 (3.6) | Critical | 31 | 30 | 30 | 3 | 2.0 | 3 | 4.5 | 4.3 |

**Top tier (62.5 to 69.5, nine categories).** Each earns 9.0 to 11.8 points from the positive factors (size, pain, AI fit) and loses 3.2 to 6.3 to the penalties. Agriculture loses only 3.2 and utility billing 3.7. Three of the nine are among the six pools above $12B: mainframe, telecom billing and government benefits. Government benefits reaches the top tier despite lock-in 5.0, and student information systems despite lock-in 3.5, because both score crowding 1.3. Government tax administration joined the tier after the regulator recode.

**Middle tier (54 to 61, 16 categories).** These earn 7.3 to 11.4 points and lose 2.7 to 7.2. Core banking (61), and payroll, licensing and permits, and courts (60.5 each) lead it. Airline reservations dropped here to 56.5 after the regulator recode.

**Bottom tier (31 to 52, 10 categories).** These lose 5.2 to 9.2 points to the penalties, and 7 of the 10 lose 7 or more. Five score crowding of 4.7 or more: financial close and field service (5.0), and loan origination, hospital records and medical billing (4.7). Insurance claims is last at 31, with lock-in 4.5 and crowding 4.3.

**What separates the tiers.** The penalties do more of the work than in version 2. Points from the positive factors run from 7.3 to 11.8, and penalties run from 2.7 to 9.2. Their standard deviations (how much they vary) are 1.12 and 1.60 points. Their correlations with the total (how closely they move with it, from -1 to 1) are +0.45 and -0.78.

By factor:

| Factor | Standard deviation | Correlation with total |
|---|---:|---:|
| Size | 0.62 | +0.07 |
| Pain | 0.80 | +0.41 |
| AI fit | 0.53 | +0.24 |
| Lock-in | 1.00 | -0.41 |
| Crowding | 1.25 | -0.67 |

Crowding sorts the list most, then lock-in and pain about equally. Size sorts it least, because 32 of 35 categories score 3 or 4 on it. Ranking into fifths spreads lock-in and crowding across the whole 1 to 5 scale by design, which is why they vary most.

**What moved since version 2, and why.**
- **The range widened from 30 to 50 to 31 to 69.5, and the average rose from 41 to 56.** Only medical billing fell, from 45 to 42.5, after its regulator answer became yes. No category stayed level.
- **Crowding fell most.** Its average went from 4.6 to 2.9. Version 2 counted every challenger row, AI-native or not, including failed and acquired ones, and stopped rising at 9 rows. That gave 24 categories the maximum of 5. Version 3 counts AI-native challengers with traction, recent category-specific AI-native funding scaled to market size, and recent Y Combinator companies (AI-native or not), and ranks each into fifths. Two categories now score 5.0.
- **Pain rose and spread.** Its average went from 2.2 to 3.0. In version 2, 28 categories scored 2. Now pain runs from 1.7 to 4.4: 12 categories sit below 2.5, 10 from 2.5 to 3.4 and 13 at 3.5 or more.
- **Lock-in fell slightly and spread.** Its average went from 3.3 to 2.9. It now runs from 1.0 to 5.0, and no longer reuses the legacy signs.
- **The biggest movers.** Utility billing rose 34.5 points (35 to 69.5): pain up 1.6, lock-in down 2, crowding down 3.3. Mainframe rose 29, laboratory information systems 28, telecom billing and government tax administration 26.5, and student information systems 24. Each gained on at least two of three counts: lower crowding, lower lock-in and higher pain.
- **The former top tier.** Core banking rose 11, courts and licensing and permits 10.5, and trade finance 7, less than most. They had moderate crowding in version 2 already, so they gained less when crowding was re-measured. Manufacturing ERP rose 17 to 67.

**What moved since the first version 3 draft, and why.** Three fixes listed as open in that draft are now done. The rank correlation between the draft's totals and these is 0.86, so the order mostly held, but a few categories moved a tier.
- **One rule for the regulator input (done).** Every category is now coded against one written rule: yes only when, in the US, EU or UK, a sector regulator must approve, or be formally told in advance of, replacing or outsourcing the core system. Cost reviews after the fact, data-protection notices and audit do not count. Seven answers changed. Airline reservations, hospital records, medical billing, retail point of sale and telecom billing became yes. Government tax administration and land registry became no. Airline reservations fell from 70 to 56.5, medical billing from 50 to 42.5 and retail from 60 to 54. Government tax rose from 55 to 66.5 and land registry from 45 to 55. Telecom billing lost 10 points here and won half of them back on crowding.
- **One decimal instead of rounding halves up (done).** Pain, lock-in and crowding now keep one decimal, so the 15 lock-in averages that sat exactly on a half count as halves instead of rounding up. Mainframe rose from 65 to 69 (lock-in 2.5 instead of 3, pain 3.3 instead of 3), warehouse management from 45 to 50.5 and co-op banking from 50 to 55. Utility billing lost 3.5 points from this change alone, because its pain of 3.6 no longer rounds to 4 and its crowding, 1.3 before the funding fix, no longer rounds down to 1.
- **Only category-specific rounds in funding per $1B (done).** Company-wide raises by horizontal companies, $2.0B over eight rounds, and the six exits and stake purchases no longer count. Telecom billing's funding fell from $87.2M to $2.1M per $1B of legacy spend, and its crowding from 2.7 to 1.7, because Sierra's and Wonderful's raises were about 97% of its money. Medical billing (Ambience) and government tax (Quantexa) also dropped. Since each input ranks categories into fifths, a few others moved up a fifth on funding without new money: utility billing from 2 to 3, which cost it 2 points. Cognition's and Anthropic's raises were never in the list, so mainframe and telecom billing are now treated alike.

## 4. What drives the ranking

**In short.** Crowding sorts the list most, then lock-in and pain about equally. Pain now has real evidence behind it and sorts the list more than AI fit or size. Each factor has a weakness worth knowing before you quote a rank. The two that matter most: lock-in leans heavily on a yes-or-no regulator input, and two of crowding's three inputs count only AI-native companies.

### 4.1 Size

**What it measures.** Annual legacy spend, scored on the midpoint.

**Worked example: utility billing.** Its legacy spend runs from $1.5B to $4.2B. The midpoint is the square root of 1.5 times 4.2, which is $2.5B. That sits between $1B and $5B, so size scores 3.

**How it varies.** No category reaches size 5, because telecom billing's $18.6B midpoint sits just under the $20B line. 14 categories score 4, 18 score 3, and 3 score 2 (agriculture, land registry and port terminals).

**What it lifts or sinks.** Size 4 lifts mainframe, manufacturing ERP, telecom billing, government tax administration and government benefits within the top tier. Size 2 holds port terminals in the middle tier despite low penalties, and is the only test agriculture fails in Section 4A.

**Weakness.** The ranges are wide, and 18 of 35 cross a bin line. The fragility runs both ways:
- **Downward.** Courts ($1.04B), permits ($1.13B) and trade finance ($1.17B) sit just above the $1B line. At their low estimates, all three would score size 2 and lose 5 points: courts and permits from 60.5 to 55.5, trade finance from 57 to 52.
- **Upward.** At their high estimates, telecom billing ($26.2B) and government benefits ($21.0B) reach size 5, and medical billing ($8.8B) reaches size 4. Telecom billing would then score 71.5 and lead alone. Government benefits would score 67.5 and medical billing 47.5.

The share still on legacy is a judgment call. It ranges from 15% to 35% in capital markets, and up to 95% in the highest case.

### 4.2 Pain

**What it measures.** How much buyers and their customers suffer from the old system. Pain is the average of up to five inputs, defined in Section 2: keep-alive share of public contracts, backend-failure share of app reviews, inverted app rating, the failed or overrun share of documented replacements, and the workaround sign.

**Worked example: utility billing.** It is one of seven categories with all five inputs.
- **Keep-alive share.** 50 public awards were labelled, and 45 of them were labelled maintain, extend or replace. 24 of those 45 (53%) maintain or extend the old system. 8 of the 13 categories with enough awards have a lower share. 8 divided by 13, times 5, is 3.1. Drop the fraction and add 1: score 4.
- **Backend-failure share.** 49 of 250 app reviews (20%) complain about a backend failure. 12 of 18 categories are lower: score 4.
- **App rating.** Its 24 customer-facing apps average 3.41 stars. 19 of 30 categories have better ratings, so less pain: score 4.
- **Failed or overrun replacements.** 6 of 12 documented replacements (50%) were cancelled or finished late or over budget. 16 of 35 categories are lower: score 3.
- **Workaround sign.** Weak: score 3.
- **Average.** (4 + 4 + 4 + 3 + 3) / 5 = 3.6. Pain is 3.6. Before the rescore it rounded to 4.

**What the pain evidence looks like.** The inputs count real events. Some of the cases behind them:
- **Courts.** California's statewide court case management system was cancelled in 2012 after 108 months and $407M. 13 of 18 labelled public awards for courts keep the old system alive.
- **Government benefits.** The US Social Security Administration's disability case processing system was cancelled after 91 months and $356M. Services Australia's entitlements calculation engine was cancelled after 48 months and $127M. 8 of 11 documented replacements failed or overran.
- **Payroll.** California's State Controller cancelled its 21st Century Project after 94 months and $373M. Queensland Health's payroll replacement finished late or over at $166M.
- **Retail point of sale.** Lidl cancelled its replacement after 84 months and $590M.
- **Utility billing.** Duke Energy's Customer Connect took 58 months and $900M and finished late or over. In Ohio, the state commission proposed a $1.45M fine and ordered an audit after more than 106,000 billing errors.
- **Manufacturing ERP.** 8 of 10 documented replacements finished late or over, including Clorox at $580M over 48 months.
- **Telecom billing.** 75 of 200 app reviews (38%) describe a backend failure, the highest share among categories with 100 or more reviews. Telstra's replacement took 118 months and $690M.
- **Loan origination and hospital records.** 23 of 50 lending app reviews (46%) and 31 of 100 hospital app reviews (31%) describe backend failures.

Across the ledger, 158 of 353 documented replacements (45%) were cancelled or finished late or over budget. 116 finished late or over, 42 were cancelled or rolled back, 90 finished on time and 105 are still running.

**All 35 categories.** Each cell shows the raw value, the number of observations in brackets, and the 1 to 5 score in bold. "Too few" means the input had data below its minimum and was left out. Categories are in the order of Section 3.

| Category | Pain (mean) | Keep-alive awards | Backend-failure reviews | App rating | Failed or overrun replacements | Workaround sign |
|---|---|---|---|---|---|---|
| Utility billing | 3.6 (3.60) | 53% (45): **4** | 20% (250): **4** | 3.41 (24): **4** | 50% (12): **3** | weak: **3** |
| Custom COBOL and mainframe | 3.3 (3.33) | too few (6) | no data | 3.85 (3): **3** | 56% (9): **4** | weak: **3** |
| Manufacturing ERP | 4.3 (4.33) | 71% (17): **5** | no data | no data | 80% (10): **5** | weak: **3** |
| Construction project accounting | 3.7 (3.67) | no data | no data | 2.05 (7): **5** | 50% (8): **3** | weak: **3** |
| Telecom billing | 3.5 (3.50) | too few (3) | 38% (200): **5** | 4.09 (33): **2** | 58% (12): **4** | weak: **3** |
| Government tax administration | 3.3 (3.33) | too few (7) | no data | 3.05 (13): **4** | 45% (11): **3** | weak: **3** |
| Student information systems | 3.6 (3.60) | 27% (44): **2** | 20% (54): **4** | 2.46 (9): **5** | 55% (11): **4** | weak: **3** |
| Agriculture and commodity trading | 3.0 (3.00) | no data | no data | 3.66 (6): **3** | 18% (11): **1** | strong: **5** |
| Government benefits | 3.8 (3.75) | too few (3) | 18% (100): **3** | 3.37 (20): **4** | 73% (11): **5** | weak: **3** |
| Core banking | 2.2 (2.20) | 20% (15): **1** | 8% (150): **1** | 4.29 (33): **2** | 60% (10): **4** | weak: **3** |
| Payroll and HR | 3.4 (3.40) | 30% (10): **2** | 19% (150): **4** | 3.05 (5): **4** | 64% (11): **4** | weak: **3** |
| Licensing and permits | 4.4 (4.40) | 55% (11): **4** | 18% (50): **3** | 2.93 (6): **5** | 78% (9): **5** | strong: **5** |
| Courts and justice case management | 3.8 (3.75) | 72% (18): **5** | too few (17) | 3.05 (15): **4** | 50% (10): **3** | weak: **3** |
| Laboratory information systems | 2.8 (2.80) | 45% (20): **3** | 20% (100): **4** | 3.63 (22): **3** | 20% (10): **1** | weak: **3** |
| Port terminal operating systems | 2.3 (2.33) | too few (2) | too few (12) | 3.62 (14): **3** | 17% (12): **1** | weak: **3** |
| Wealth and portfolio accounting | 4.0 (4.00) | too few (3) | too few (3) | 2.35 (3): **5** | 60% (10): **4** | weak: **3** |
| Pension and provident fund admin | 3.2 (3.25) | too few (2) | 18% (300): **2** | 3.50 (23): **3** | 67% (9): **5** | weak: **3** |
| Trade finance | 1.7 (1.67) | no data | no data | 4.33 (6): **1** | 14% (7): **1** | weak: **3** |
| Card issuing and processing | 2.0 (2.00) | too few (3) | 14% (250): **2** | 4.33 (25): **1** | 33% (12): **2** | weak: **3** |
| Airline reservations | 2.0 (2.00) | too few (6) | 12% (380): **2** | 4.28 (27): **2** | 8% (12): **1** | weak: **3** |
| Co-op, rural and microfinance banking | 2.2 (2.25) | no data | 18% (100): **3** | 3.93 (8): **2** | 8% (12): **1** | weak: **3** |
| Wholesale distribution ERP | 4.3 (4.33) | too few (1) | no data | 1.66 (8): **5** | 70% (10): **5** | weak: **3** |
| Land and property registry | 2.8 (2.75) | too few (6) | 0% (51): **1** | 2.80 (10): **5** | 30% (10): **2** | weak: **3** |
| Procurement and payables | 2.3 (2.33) | 25% (12): **1** | no data | no data | 50% (10): **3** | weak: **3** |
| Retail point of sale | 4.0 (4.00) | too few (1) | no data | no data | 75% (8): **5** | weak: **3** |
| Mortgage servicing | 1.7 (1.67) | no data | no data | 4.83 (3): **1** | 20% (10): **1** | weak: **3** |
| Capital markets back office | 1.8 (1.75) | too few (2) | 8% (50): **1** | 4.57 (7): **1** | 42% (12): **2** | weak: **3** |
| Warehouse management | 3.3 (3.33) | 47% (74): **3** | no data | no data | 63% (8): **4** | weak: **3** |
| Financial close and general ledger | 2.3 (2.33) | 42% (12): **2** | no data | no data | 30% (10): **2** | weak: **3** |
| Loan origination and servicing | 2.8 (2.75) | too few (2) | 46% (50): **5** | 4.87 (3): **1** | 30% (10): **2** | weak: **3** |
| Field service and maintenance | 3.5 (3.50) | 63% (34): **4** | too few (6) | 4.25 (4): **2** | 67% (9): **5** | weak: **3** |
| Hospital records (EHR) | 2.8 (2.80) | 0% (63): **1** | 31% (100): **5** | 3.84 (27): **3** | 42% (12): **2** | weak: **3** |
| Medical billing | 3.7 (3.67) | too few (1) | too few (36) | 3.41 (10): **4** | 22% (9): **2** | strong: **5** |
| Insurance policy administration | 2.2 (2.25) | no data | 12% (50): **2** | 4.39 (31): **1** | 50% (8): **3** | weak: **3** |
| Insurance claims | 2.0 (2.00) | no data | 10% (259): **1** | 4.10 (33): **2** | 38% (8): **2** | weak: **3** |

**How it varies.** Pain runs from 1.7 to 4.4. 12 categories sit below 2.5, 10 from 2.5 to 3.4 and 13 at 3.5 or more. Licensing and permits is highest (4.4), and trade finance and mortgage servicing lowest (1.7).

**What it lifts or sinks.** Pain of 3.6 keeps student information systems in the top tier: at 3.0 it would score 61. Utility billing (3.6), construction accounting (3.7) and telecom billing (3.5) would stay in the top tier at 3.0. Pain of 2.0 or less holds six categories back: trade finance and mortgage servicing (1.7), capital markets (1.8), and airline reservations, card processing and insurance claims (2.0). Laboratory information systems sits just under the search line at 2.8.

**Weakness.**
- **Coverage is uneven.** Keep-alive share reaches its minimum in 13 categories and backend-failure share in 18. 15 categories rest on three inputs or fewer. Retail point of sale rests on two: its replacement record and the workaround sign.
- **The app inputs measure end customers.** They come from customer-facing apps, such as a bank's or a carrier's app. A legacy back end causes only part of what those customers complain about.
- **The awards lean European and public.** 1,457 of 1,922 awards come from the EU's public tender database. A high keep-alive share can also mean the old system works well enough. Hospital records shows 0 of 63 because its public awards are replacements.
- **The replacement ledger favours famous projects.** Failures get written up more than quiet successes. Ongoing projects count in the base, which lowers the rate for categories in the middle of replacing. Some projects appear in two categories, such as Commonwealth Bank and Centrelink under both their own category and mainframe, and Pennsylvania's unemployment system under government benefits ($170M) and mainframe ($153M), with different costs.
- **The workaround sign barely varies.** 32 of 35 categories grade weak, so it pulls averages toward 3.
- **Sensitivity.** Without the workaround sign, manufacturing ERP rises to 70.5 and ties utility billing (70.5) for the lead, with mainframe at 70. Without pain at all, mainframe would lead alone.

### 4.3 AI fit

**What it measures.** Jev scored 12 core tasks per category for how much of each AI could do. The scores are weighted by how much time each task takes, averaged and rounded.

**Worked example: utility billing.** Its 12 tasks average 3.61 after weighting by time share, which rounds to 4. Government tax administration averages 3.46, which rounds to 3.

**How it varies.** 24 categories score 4, 10 score 3, and only warehouse management scores 2. The averages run from 2.499 (warehouse, just under 2.5, so it rounds down) to 4.13 (construction accounting).

**What it sinks.** The ten categories at 3 lose a point against the rest. They include hospital records, both ERP categories, retail, tax administration and laboratory information systems. AI fit 3 is one of the tests government tax administration fails in Section 4A, and one of three narrow misses for laboratory information systems.

**Weakness.** Jev rated tasks about half a point more automatable than blind labellers (3.46 against 2.97). Across 60 sampled tasks, the two agreed on order with a rank correlation of 0.83. That is a check on tasks, not on the category order. Rounding also creates cliffs: tax administration averages 3.46 and scores 3, while card processing averages 3.52 and scores 4. AI fit is now the only part still rounded to a whole number. The rescore kept one decimal for pain, lock-in and crowding only. At one decimal, tax administration would score 3.5 and gain 2.5 points. The audit says AI fit should rank categories against each other, never act as an absolute claim. The search in Section 4A uses "AI fit 4 or more" as an absolute bar. On the blind labellers' scale, about 0.49 lower, only construction accounting (4.13) and payroll (4.07) would still score 4.

**A second view.** The workflow data adds an independent measure: how much the category's work already shows up in AI usage, from the Anthropic Economic Index. Averaged per category, it agrees with AI fit only loosely. The rank correlation is 0.46. AI fit is a rating of what AI could do. The Economic Index records what people already use Claude for.

### 4.4 Lock-in

**What it measures.** How hard it is for a buyer to leave the old system. It counts against the score.

**How it is derived, step by step.**
1. **Contract length.** Take every public award that Jev placed in the category and that states a start and end date. Find the median length in months. A category needs at least 10 such awards.
2. **Non-competitive share.** Take every award in the category with a known procedure. Find the share awarded without open competition. A category needs at least 10 such awards.
3. **Replacement time.** Take every documented replacement in the ledger with a start and end date. Find the median length in months. A category needs at least 3.
4. **Rank each of these three into fifths** among the categories that have enough data. Longer contracts, more non-competitive awards and longer replacements score higher.
5. **Regulator approval.** Score 5 if, in the US, EU or UK, a sector regulator must approve, or be formally told in advance of, replacing or outsourcing the core system, and 1 if not.
6. **Average** the available scores and keep one decimal.

**Worked example: student information systems.** It is one of seven categories with all four inputs.
- **Contract length.** The median of 23 awards is 60 months. 6 of the 8 categories with enough awards have shorter contracts. 6 divided by 8, times 5, is 3.75. Drop the fraction and add 1: score 4.
- **Non-competitive share.** 3 of 17 awards (18%) were made without competition. 8 of 9 categories are lower: score 5.
- **Replacement time.** The median of 7 documented replacements is 60 months. 21 of 35 categories are shorter: score 4. Los Angeles Unified's student system replacement was cancelled after 72 months and $112M.
- **Regulator approval.** No regulator approves or must be told in advance of the switch: score 1.
- **Average.** (4 + 5 + 4 + 1) / 4 = 3.5. Lock-in is 3.5. Before the rescore it rounded up to 4.

**All 35 categories.** Each cell shows the raw value, the number of observations in brackets, and the 1 to 5 score in bold. "Too few" means the input had data below its minimum and was left out. "No data" means none was found. "mo" means months.

| Category | Lock-in (mean) | Contract length (median) | Non-competitive awards | Replacement time (median) | Regulator approval |
|---|---|---|---|---|---|
| Utility billing | 2.0 (2.00) | 48 mo (18): **3** | 0% (12): **1** | 40 mo (9): **3** | no: **1** |
| Custom COBOL and mainframe | 2.5 (2.50) | too few (4) | too few (4) | 69 mo (6): **4** | no: **1** |
| Manufacturing ERP | 1.2 (1.25) | 12 mo (15): **1** | 0% (14): **1** | 38 mo (5): **2** | no: **1** |
| Construction project accounting | 1.0 (1.00) | no data | no data | 6 mo (5): **1** | no: **1** |
| Telecom billing | 3.5 (3.50) | no data | no data | 36 mo (11): **2** | yes: **5** |
| Government tax administration | 3.0 (3.00) | too few (6) | too few (8) | 72 mo (6): **5** | no: **1** |
| Student information systems | 3.5 (3.50) | 60 mo (23): **4** | 18% (17): **5** | 60 mo (7): **4** | no: **1** |
| Agriculture and commodity trading | 1.5 (1.50) | no data | no data | 39.5 mo (4): **2** | no: **1** |
| Government benefits | 5.0 (5.00) | too few (1) | too few (4) | 84 mo (9): **5** | yes: **5** |
| Core banking | 3.0 (3.00) | too few (5) | 0% (14): **1** | 57 mo (7): **3** | yes: **5** |
| Payroll and HR | 3.0 (3.00) | too few (5) | too few (8) | 81.5 mo (10): **5** | no: **1** |
| Licensing and permits | 2.0 (2.00) | too few (5) | too few (8) | 49 mo (7): **3** | no: **1** |
| Courts and justice case management | 3.7 (3.67) | 72 mo (15): **5** | too few (8) | 102 mo (5): **5** | no: **1** |
| Laboratory information systems | 2.2 (2.25) | 36.1 mo (19): **2** | 10% (20): **4** | 36 mo (5): **2** | no: **1** |
| Port terminal operating systems | 1.0 (1.00) | too few (2) | no data | 34 mo (4): **1** | no: **1** |
| Wealth and portfolio accounting | 3.5 (3.50) | too few (9) | too few (8) | 36 mo (9): **2** | yes: **5** |
| Pension and provident fund admin | 4.0 (4.00) | too few (4) | 10% (10): **4** | 57.5 mo (8): **3** | yes: **5** |
| Trade finance | 3.0 (3.00) | no data | no data | 27 mo (4): **1** | yes: **5** |
| Card issuing and processing | 3.0 (3.00) | too few (3) | too few (6) | 16 mo (9): **1** | yes: **5** |
| Airline reservations | 3.0 (3.00) | too few (4) | too few (4) | 14.5 mo (12): **1** | yes: **5** |
| Co-op, rural and microfinance banking | 3.5 (3.50) | no data | no data | 39 mo (8): **2** | yes: **5** |
| Wholesale distribution ERP | 2.0 (2.00) | no data | no data | 41 mo (5): **3** | no: **1** |
| Land and property registry | 2.5 (2.50) | too few (5) | too few (5) | 60 mo (5): **4** | no: **1** |
| Procurement and payables | 2.5 (2.50) | too few (5) | too few (9) | 60 mo (7): **4** | no: **1** |
| Retail point of sale | 4.5 (4.50) | no data | no data | 63 mo (6): **4** | yes: **5** |
| Mortgage servicing | 3.0 (3.00) | no data | too few (1) | 24 mo (3): **1** | yes: **5** |
| Capital markets back office | 3.0 (3.00) | too few (1) | too few (1) | 30.5 mo (10): **1** | yes: **5** |
| Warehouse management | 1.5 (1.50) | 12 mo (65): **1** | 0% (30): **1** | 48 mo (3): **3** | no: **1** |
| Financial close and general ledger | 3.0 (3.00) | too few (6) | too few (5) | 73 mo (4): **5** | no: **1** |
| Loan origination and servicing | 4.0 (4.00) | too few (2) | too few (2) | 40 mo (5): **3** | yes: **5** |
| Field service and maintenance | 2.5 (2.50) | 12 mo (43): **1** | 5% (56): **3** | 94 mo (7): **5** | no: **1** |
| Hospital records (EHR) | 3.5 (3.50) | 48 mo (14): **3** | 0% (17): **1** | 104 mo (5): **5** | yes: **5** |
| Medical billing | 4.5 (4.50) | too few (2) | no data | 60 mo (6): **4** | yes: **5** |
| Insurance policy administration | 3.5 (3.50) | no data | too few (1) | 35.5 mo (8): **2** | yes: **5** |
| Insurance claims | 4.5 (4.50) | no data | no data | 60 mo (4): **4** | yes: **5** |

**How it varies.** Lock-in runs from 1.0 to 5.0. 3 categories sit below 1.5, 6 from 1.5 to 2.4, 13 from 2.5 to 3.4, 9 from 3.5 to 4.4 and 4 at 4.5 or more. 15 averages sit exactly on a half, and now count as halves.

**What the table shows.**
- **The regulator input carries the most weight.** All 17 categories where a regulator must approve or be told in advance score 3.0 or more: 6 score 3.0, 5 score 3.5, 2 score 4.0, 3 score 4.5 and government benefits 5.0. The 18 without run from 1.0 to 3.7. All four categories at 4.5 or more have a regulator: government benefits, insurance claims, medical billing and retail point of sale.
- **Most categories rest on two inputs.** Contract length and non-competitive share reach their minimum in only 8 and 9 categories. For the other 25, lock-in is the average of replacement time and the regulator answer.
- **The lowest lock-in.** Construction accounting (median replacement 6 months over 5 cases) and port terminals (34 months over 4) score 1.0, and manufacturing ERP (12-month contracts, no non-competitive awards in 14, 38-month replacements) 1.2. Airline reservations has the shortest replacements after construction (14.5 months over 12 cases), but now scores 3.0 because of its regulator answer.
- **The longest replacements.** Hospital records (104 months), courts (102), field service (94), government benefits (84) and payroll (81.5).

**What it sinks.** Lock-in of 4.5 or more sinks government benefits, insurance claims, medical billing and retail point of sale. Lock-in of 3.5 to 4.0 holds back telecom billing, student information systems, courts and pension administration, and is the only search test each of them fails.

**Weakness.**
- **The regulator input is a yes or no that scores 1 or 5.** With only two inputs, it moves lock-in by up to 2 points and a total by up to 10.
- **Uneven regulator coding (fixed).** The first version 3 draft applied the rule unevenly, for example core banking yes but utility billing no on similar facts. Every category is now coded against one written rule: yes only when, in the US, EU or UK, a sector regulator must approve, or be formally told in advance of, replacing or outsourcing the core system. Seven answers changed (Section 3). Core banking stays yes (advance notice of material outsourcing to UK and EU supervisors). Utility billing stays no, because state commissions review the cost in rate cases after the fact rather than approve the switch. Mainframe stays no, because bank and insurer owners are coded in their own categories.
- **Borderline calls remain.** The research marks five answers as borderline: airline reservations (border-data certification, not the whole system), medical billing (the regulator is also the payer), retail (fiscal and card-payment devices, not merchandising), tax administration (an IRS data-protection notice, which the rule excludes) and mainframe (yes if any bank owner counted). Each would move its total by 10 points if flipped. A yes for tax administration would drop it from 66.5 to 56.5.
- **Rounding (fixed).** The first draft rounded 15 lock-in averages that sat exactly on a half up to the next whole number. Lock-in now keeps one decimal. Mainframe's 2.5 no longer becomes 3, so it misses the search by half a point instead of a whole one. Two averages sit on a quarter (1.25 and 2.25) and show as 1.2 and 2.2.
- **Some results look odd.** Card processing has a median replacement of 16 months but scores 3.0 because of the regulator answer, and airline reservations (14.5 months) now does too. Telecom billing's replacement time scores only 2 although Telstra's replacement took 118 months, because its median over 11 cases is 36.
- **The airline ledger may reflect what gets published.** 11 of 12 airline replacements finished on time. As an inference, vendor-announced migrations may be over-represented.
- **Lock-in still does not measure switching rates,** meaning how many buyers actually change system each year.
- **Sensitivity.** Without the regulator input, telecom billing would lead alone at 74, and trade finance, card processing, mortgage servicing, capital markets and airline reservations would each rise 10 points. Utility billing would fall to 68 and fail the search, because its lock-in would be 2.3.

### 4.5 Crowding

**What it measures.** How many AI-native challengers already attack the category. It counts against the score.

**Worked example: telecom billing.**
- **AI-native with traction.** Three: Totogi, Sierra and Wonderful. 18 of 35 categories have fewer. 18 divided by 35, times 5, is 2.6. Drop the fraction and add 1: score 3.
- **AI-native funding per $1B.** Six rounds in 24 months, but five of them are company-wide raises by Sierra and Wonderful, who sell customer-service agents across many industries. They no longer count. The one category-specific round, gaiia's $40M, divided by $18.6B of legacy spend, is $2.1M per $1B. Only 3 of 35 categories are lower: score 1. Before the rescore, all six counted, about $1,624M or $87.2M per $1B, and the input scored 4.
- **Y Combinator companies.** One since 2024. Only the 6 categories with none are lower: score 1.
- **Average.** (3 + 1 + 1) / 3 = 1.67, kept as 1.7. Before the rescore it was (3 + 4 + 1) / 3 = 2.67, rounded to 3.

**All 35 categories.** Each cell shows the raw value and the 1 to 5 score in bold. The funding cell also shows the number of category-specific rounds and their total.

| Category | Crowding (mean) | AI-native with traction | AI-native funding per $1B of legacy spend, 24 months | YC companies, 2024 to 2026 |
|---|---|---|---|---|
| Utility billing | 1.7 (1.67) | 0: **1** | $30.3M (3 rounds, $76M in all): **3** | 0: **1** |
| Custom COBOL and mainframe | 2.0 (2.00) | 4: **4** | $1.6M (4 rounds, $23M in all): **1** | 1: **1** |
| Manufacturing ERP | 3.7 (3.67) | 5: **5** | $16.3M (13 rounds, $142M in all): **2** | 17: **4** |
| Construction project accounting | 3.3 (3.33) | 3: **3** | $44.8M (4 rounds, $54M in all): **3** | 9: **4** |
| Telecom billing | 1.7 (1.67) | 3: **3** | $2.1M (1 round, $40M in all): **1** | 1: **1** |
| Government tax administration | 1.0 (1.00) | 0: **1** | $0.5M (1 round, $4M in all): **1** | 0: **1** |
| Student information systems | 1.3 (1.33) | 0: **1** | $0.5M (2 rounds, $1M in all): **1** | 2: **2** |
| Agriculture and commodity trading | 1.7 (1.67) | 1: **1** | $41.4M (3 rounds, $25M in all): **3** | 1: **1** |
| Government benefits | 1.3 (1.33) | 2: **2** | $8.0M (6 rounds, $100M in all): **1** | 1: **1** |
| Core banking | 2.0 (2.00) | 0: **1** | $32.5M (10 rounds, $422M in all): **3** | 3: **2** |
| Payroll and HR | 3.3 (3.33) | 3: **3** | $16.6M (9 rounds, $157M in all): **2** | 24: **5** |
| Licensing and permits | 4.3 (4.33) | 4: **4** | $118.8M (9 rounds, $134M in all): **5** | 14: **4** |
| Courts and justice case management | 2.0 (2.00) | 2: **2** | $6.0M (3 rounds, $6M in all): **1** | 6: **3** |
| Laboratory information systems | 2.0 (2.00) | 1: **1** | $14.8M (3 rounds, $20M in all): **2** | 7: **3** |
| Port terminal operating systems | 1.7 (1.67) | 0: **1** | $47.6M (1 round, $21M in all): **3** | 0: **1** |
| Wealth and portfolio accounting | 3.0 (3.00) | 1: **1** | $166.0M (13 rounds, $509M in all): **5** | 7: **3** |
| Pension and provident fund admin | 1.7 (1.67) | 2: **2** | $17.9M (5 rounds, $39M in all): **2** | 0: **1** |
| Trade finance | 1.3 (1.33) | 1: **1** | $8.5M (2 rounds, $10M in all): **1** | 3: **2** |
| Card issuing and processing | 2.7 (2.67) | 2: **2** | $35.9M (13 rounds, $437M in all): **3** | 6: **3** |
| Airline reservations | 1.7 (1.67) | 1: **1** | $13.9M (2 rounds, $42M in all): **2** | 2: **2** |
| Co-op, rural and microfinance banking | 1.7 (1.67) | 2: **2** | $21.4M (5 rounds, $120M in all): **2** | 0: **1** |
| Wholesale distribution ERP | 4.3 (4.33) | 6: **5** | $117.6M (16 rounds, $214M in all): **4** | 15: **4** |
| Land and property registry | 2.3 (2.33) | 2: **2** | $107.9M (6 rounds, $78M in all): **4** | 1: **1** |
| Procurement and payables | 4.0 (4.00) | 3: **3** | $78.1M (12 rounds, $438M in all): **4** | 21: **5** |
| Retail point of sale | 2.7 (2.67) | 3: **3** | $16.7M (7 rounds, $88M in all): **2** | 6: **3** |
| Mortgage servicing | 2.3 (2.33) | 2: **2** | $108.6M (4 rounds, $224M in all): **4** | 0: **1** |
| Capital markets back office | 2.7 (2.67) | 0: **1** | $43.6M (7 rounds, $118M in all): **3** | 18: **4** |
| Warehouse management | 3.7 (3.67) | 3: **3** | $182.3M (10 rounds, $261M in all): **5** | 8: **3** |
| Financial close and general ledger | 5.0 (5.00) | 5: **5** | $126.9M (18 rounds, $736M in all): **5** | 20: **5** |
| Loan origination and servicing | 4.7 (4.67) | 8: **5** | $105.9M (16 rounds, $550M in all): **4** | 19: **5** |
| Field service and maintenance | 5.0 (5.00) | 5: **5** | $209.1M (15 rounds, $517M in all): **5** | 34: **5** |
| Hospital records (EHR) | 4.7 (4.67) | 5: **5** | $156.1M (16 rounds, $1,983M in all): **5** | 11: **4** |
| Medical billing | 4.7 (4.67) | 5: **5** | $83.2M (18 rounds, $398M in all): **4** | 31: **5** |
| Insurance policy administration | 4.3 (4.33) | 4: **4** | $272.4M (12 rounds, $619M in all): **5** | 9: **4** |
| Insurance claims | 4.3 (4.33) | 4: **4** | $106.3M (15 rounds, $383M in all): **4** | 19: **5** |

**How it varies.** Crowding runs from 1.0 to 5.0. 4 categories sit below 1.5, 13 from 1.5 to 2.4, 6 from 2.5 to 3.4, 7 from 3.5 to 4.4 and 5 at 4.5 or more.

**Crowding that is not "everything is crowded".** Ranking into fifths spreads the scores by design, so the absolute numbers matter too:
- **Six categories have no AI-native challenger with traction:** utility billing, student information systems, core banking, government tax administration, port terminals and capital markets back office.
- **Recent AI-native money is very uneven.** Category-specific rounds run from about $1M in student information systems and $4M in tax administration to $1,983M in hospital records.
- **13 categories have two or fewer Y Combinator companies since 2024,** and six have none.
- **Nine categories score 4 or 5 on every input:** medical billing, hospital records, financial close, loan origination, field service, insurance policy administration, insurance claims, wholesale distribution ERP, and licensing and permits. Two of them (financial close and field service) score 5 on all three.

**What it lifts or sinks.** Low crowding lifts government tax administration (1.0), government benefits and student information systems (1.3 each) into the top tier, and keeps utility billing (1.7) at the top. Crowding of 4.7 or more holds down five of the ten bottom-tier categories.

**Weakness.**
- **Two of its three inputs count only AI-native companies.** The third counts all recent Y Combinator companies, AI-native or not. Modern challengers that are not AI-native and not from recent Y Combinator batches do not count. In utility billing, Kraken raised a $1B round at an $8.65B valuation in December 2025, and six challengers that are not AI-native have traction, Kraken among them. Utility billing still scores crowding 1.7.
- **Company-wide raises (fixed).** The first draft counted Sierra's $350M and $950M rounds fully against telecom billing, about 80% of its $1,624M, while Cognition's and Anthropic's raises did not count against mainframe. Now each round carries a scope, and only rounds aimed at the category count toward funding per $1B. Eight company-wide raises ($2.0B) and six exits or stake purchases are left out. Telecom billing's crowding fell from 2.7 to 1.7. Sierra and Wonderful still count as AI-native challengers with traction in telecom billing, because the challenger table records traction for them there.
- **Incumbents' own AI does not count.** AWS gives its mainframe agent away, IBM ships its own code assistant, and Epic ships steps that challengers once sold. In utility billing, Kraken launched autonomous agents built with Sierra in June 2026. None of this shows in crowding.
- **The scores are relative.** An input score of 1 means among the least crowded fifth, not empty, and a crowding of 1.0 means that on all three inputs.
- **Gaps in the inputs.** 30 of the 298 rows have no disclosed amount, 24 of them among the 284 category-specific rounds. The scope tags are research judgments. Two are marked borderline: Ambience in medical billing (it sells only to healthcare) and Lumi in retail. Quantexa, tagged company-wide in tax administration, is not AI-native by the atlas definition at all. The Y Combinator category label passed its audit only after one rewording.
- **The version 2 parse bug no longer affects scores.** The rounds list stores amounts as numbers, so the funding parser that misread telecom billing and laboratory information systems in version 2 is no longer used for scoring. It still affects the funding text in the challenger table.
- **Sensitivity.** Without the Y Combinator input, construction accounting would lead at 68.5, with utility billing and manufacturing ERP at 68. Utility billing's crowding would be 2.0, still inside the search line.

## 4A. The search: big, painful, AI-fit, low lock-in, low crowding

**In short.** You asked whether anything is sizeable, painful and a good fit for AI, with low lock-in and low crowding. At the category level, one category passes all five tests, narrowly: utility billing. Mainframe misses by half a point on lock-in, and agriculture misses only on size. Three more miss on one test by 1.5 points or less. At the workflow level, 16 workflows pass a stricter cut, because the edges of a category escape its core lock-in and most of its crowding. The workflow list is better read as leads to check than as markets, because its size measure counts whole US occupations.

### The tests

A category passes when it meets all five. Pain, lock-in and crowding now carry one decimal, so the lines are exact: 2.9 fails a "3 or more" test and 2.1 fails a "2 or less" test.
- **Size 3 or more**: at least $1B of legacy spend.
- **Pain 3.0 or more.**
- **AI fit 4 or more.** This uses Jev's score as an absolute bar, which the audit warns against (Section 4.3). On the blind labellers' scale, utility billing's 3.61 would become about 3.12 and score 3, and it would fail. Under a relative test, the top half of the 35 on AI fit, it still passes: it ranks 17th of 35, the last place inside the top half. Telecom billing (20th) would then miss on AI fit as well as lock-in.
- **Lock-in 2.0 or less.**
- **Crowding 2.0 or less.**

### At the category level

| Category | Total | Size | Pain | AI fit | Lock-in | Crowding | Misses on | Buyable spend, USD B |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| Utility billing | 69.5 | 3 | 3.6 | 4 | 2.0 | 1.7 | Passes | 2.5 |
| Custom COBOL and mainframe | 69 | 4 | 3.3 | 4 | 2.5 | 2.0 | Lock-in by 0.5 | 0.6 |
| Agriculture and commodity trading | 64 | 2 | 3.0 | 4 | 1.5 | 1.7 | Size by 1 | 0.05 |
| Construction project accounting | 67 | 3 | 3.7 | 4 | 1.0 | 3.3 | Crowding by 1.3 | 1.2 |
| Telecom billing | 66.5 | 4 | 3.5 | 4 | 3.5 | 1.7 | Lock-in by 1.5 | 18.6 |
| Student information systems | 64 | 3 | 3.6 | 4 | 3.5 | 1.3 | Lock-in by 1.5 | 2.1 |

Four more miss on one test by more. Courts (lock-in 3.7), pension administration (lock-in 4.0) and government benefits (lock-in 5.0) miss on lock-in. Licensing and permits misses on crowding (4.3). Several miss on two or three tests, some by little. Government tax administration misses on AI fit (3) and lock-in (3.0). Core banking and airline reservations miss on pain (2.2 and 2.0) and lock-in (3.0 each). Laboratory information systems misses on three, two of them by 0.2: pain 2.8, AI fit 3 and lock-in 2.2.

**How firm is utility billing's pass?** Narrow. Pain is solid, but two tests sit on an edge, and crowding needs a large caveat.
- It passes without the workaround sign (pain would be 3.8) and without the Y Combinator input (crowding would be 2.0, exactly on the line). Without the regulator input it would fail: lock-in would rise to 2.3, because its "no" answer is one of the inputs holding lock-in down.
- Its pain rests on all five inputs, each scoring 3 or 4.
- **AI fit is close to the line.** It passes on Jev's score but would fail on the blind labellers' scale (see the tests above).
- **Lock-in sits exactly on 2.0, the edge of the test.** Contracts run a median 48 months and replacements a median 40 months. The non-competitive input is 0 of 12 awards, and all 12 come from the EU tender database. One non-competitive award among them would make that input score 3 and lift lock-in to 2.5, which fails the test. All 50 utility billing awards come from the EU database, and none from the US, where the best first buyer sits. The buyer research also warns of sole-source renewals with the current vendor.
- **The regulator answer is now settled by the single rule, but it was a close call.** It is coded no. No US, EU or UK regulator approves a switch or must be told of it in advance. State commissions review the spending in rate cases (the hearings where a regulator sets the prices a utility may charge and decides which costs it may recover), but after the fact, and the rule waivers Ohio's commission granted before one installation were specific to that case. A yes would lift lock-in to 3.0 and fail the test.
- **Crowding needs a large caveat.** It scores 1.7 because no AI-native challenger has traction, no recent Y Combinator company works in it, and its three recent category-specific AI-native rounds total about $76M. Its funding input rose from 2 to 3 in the rescore without new money, because other categories' counted money fell. Kraken raised $1B at an $8.65B valuation in December 2025, and Gentrack, SEW and others have traction. Kraken also launched autonomous agents built with Sierra in June 2026, so the leading modern vendor is shipping its own AI. The opening is for an AI-native entrant against modern and legacy vendors alike, not an empty market.

**What the near misses say.**
- **Mainframe** misses only because its lock-in is 2.5: a 69-month median replacement scores 4 and the regulator answer scores 1. Before the rescore, 2.5 rounded up to 3. Its buyable spend is only $0.6B (Section 6).
- **Agriculture** passes every test except size: it is under $1B, and only $0.05B of it is buyable.
- **Construction accounting** misses on crowding: Adaptive, Field Materials and Pillar have traction, and 9 Y Combinator companies arrived since 2024.
- **Telecom billing** is the largest buyable pool on the map at $18.6B. The rescore swapped its miss. Crowding now passes at 1.7, because the company-wide raises by Sierra and Wonderful no longer count. Lock-in now fails at 3.5, because larger UK providers need their billing system approved by an Ofcom-recognised body, which makes its regulator answer yes.
- **Student information systems** misses on lock-in: contracts run a median 60 months, 18% of awards were made without competition, and replacements take a median 60 months.
- **Airline reservations,** a near miss before the rescore, now misses on two tests. US border authorities must certify the system that sends passenger data, which makes its regulator answer yes, and its pain stays weak at 2.0.

### At the workflow level

The top 15 workflows by opportunity index among those that do not touch the core. Labour value is the pay of all US workers in the workflow's occupations times their time share. AI usage runs from 0 to 1. Category pain is the category's pain score. The rounds column counts rounds mapped to the workflow, and each round is mapped to one workflow only. The published index counts every row in the rounds list, including the six exits and stake purchases. Utility billing's customer-contact round is one of them (POWERCONNECT.AI's majority sale to BHC Global), so it is marked "1 (exit)". Without it, that workflow's index would rise.

| # | Workflow | Category (total) | Index | Labour value, USD B | AI usage | AI-native rounds, 24 months | Category pain |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | Taxpayer contact centre and account inquiries | Government tax administration (66.5) | 498 | 85.1 | 0.57 | 0 | 3.3 |
| 2 | Billing, cash application, credit holds and collections | Wholesale distribution ERP (55) | 495 | 34.9 | 0.35 | 0 | 4.3 |
| 3 | Customer and case inquiry lookups across mainframe screens | Custom COBOL and mainframe (69) | 473 | 55.2 | 0.49 | 0 | 3.3 |
| 4 | Performance measurement and client reporting | Wealth and portfolio accounting (57.5) | 467 | 18.1 | 0.58 | 0 | 4.0 |
| 5 | Progress billing, retainage (payment held back until the work is accepted), lien waivers (a contractor's release of its claim on the property once paid) and collections | Construction project accounting (67) | 459 | 20.8 | 0.60 | 0 | 3.7 |
| 6 | Bill disputes, credits and adjustments | Telecom billing (66.5) | 447 | 25.4 | 0.60 | 0 | 3.5 |
| 7 | Customer contact: high-bill inquiries, complaints and account questions | Utility billing (69.5) | 443 | 66.6 | 0.66 | 1 (exit) | 3.6 |
| 8 | Call center, case status inquiries and referrals | Government benefits (62.5) | 429 | 86.8 | 0.36 | 1 | 3.8 |
| 9 | Accounts payable three-way match (checking each invoice against its purchase order and goods receipt) | Wholesale distribution ERP (55) | 422 | 27.8 | 0.17 | 0 | 4.3 |
| 10 | Applicant questions and status inquiries | Licensing and permits (60.5) | 416 | 44.1 | 0.28 | 1 | 4.4 |
| 11 | Credit and collections: arrears, payment arrangements and disconnection | Utility billing (69.5) | 409 | 18.7 | 0.41 | 0 | 3.6 |
| 12 | Employer arrears, inspections and recovery | Pension and provident fund admin (57.5) | 403 | 41.8 | 0.28 | 0 | 3.2 |
| 13 | Admissions application and transcript intake | Student information systems (64) | 397 | 23.2 | 0.30 | 0 | 3.6 |
| 14 | Order capture, activation, number porting (moving a customer's number between carriers) and order fallout (orders that fail between systems) | Telecom billing (66.5) | 386 | 63.9 | 0.11 | 0 | 3.5 |
| 15 | Paper return, payment and correspondence intake and data capture | Government tax administration (66.5) | 384 | 38.7 | 0.22 | 0 | 3.3 |

**What the list shows.**
- **11 categories appear.** Government tax administration, wholesale distribution ERP, telecom billing and utility billing place two workflows each. Borrower servicing in loan origination and reservation-center booking in airline reservations dropped out of the top 15 after the rescore, and licensing applicant questions and tax paper intake came in.
- **12 of the 15 have no AI-native funding round mapped to them in 24 months.** Government benefits' call centre and licensing applicant questions have one each. Utility billing's customer contact shows one, but it is an exit. "No round mapped" is narrower than "no round in the area": telecom billing's five company-wide raises (Sierra and Wonderful) all sit on its customer-care workflow, so its bill disputes show zero.
- **Five of the 15 are contact and inquiry work:** answering customers or applicants, looking up accounts and logging the outcome. Billing, collections, arrears and disputes account for five more.
- **Six sit in categories with lock-in of 3.5 or more.** They do not change the core record, so the index treats them as low lock-in. They are the benefits call centre (lock-in 5.0), employer arrears in pension administration (4.0), and admissions intake, client reporting and telecom billing's two workflows (3.5 each).

**A stricter cut.** Keep only workflows that do not touch the core, have no AI-native funding round mapped to them in 24 months (exits and stake purchases left out), sit in a category with pain 3.0 or more, and show AI usage at or above the median of all 210 (0.18). 55 workflows that do not touch the core have no round mapped, and 16 of them pass. Counting the exits as rounds would give 53 and 14. Company-wide raises stay in this count, because each is mapped to the one workflow where the company sells. Leaving them out too would add one workflow, telecom customer care, where Sierra and Wonderful sell. The 16 include eleven of the top 15 above, plus overnight batch scheduling and 3270 screen transaction entry in mainframe, collections and suspend or restore in telecom billing, master schedule building in student information systems, and judicial research and order drafting in courts. 3270 screens are the green-screen terminals used to work on IBM mainframes. Laboratory information systems' send-out testing and lab billing passed before the rescore and drop out now, because the category's pain is 2.8 rather than a rounded 3. Collections and arrears work recurs: five of the 16. Customer contact appears twice (taxpayer contact and utility customer contact), and billing disputes and inquiry lookups once each. The mainframe screen work is marked as not touching the core. That is a generous research judgment, since entering transactions on those screens writes to the core.

**Caveat on size.** The labour values are not market sizes. Taxpayer contact centre work shows $85.1B because about 1.8M full-time equivalents count toward it. A full-time equivalent is the number of full-time workers that the shares of working time add up to. Nearly all of the 1.8M is 70% of the working time of every US customer service representative, in every industry, not only in tax agencies. Tax examiners add a small share. Summed over 210 workflows, labour value comes to $6.3T, because the same occupations count many times. Use the figure to compare workflows, not to size a business.

### Why the workflow level finds more

1. **It separates the edge from the core.** Category lock-in describes the hardest part of the category: replacing the system of record. 130 of 210 workflows do not touch the core, and 47 of those sit in categories with lock-in above 3.
2. **Crowding is concentrated.** The 21 most crowded workflows, a tenth of the total, hold 40% of the 297 mapped rounds. 96 of 210 workflows have none, or 98 once the six exits and stake purchases are left out. In categories with crowding 3.0 or more, 10 workflows that do not touch the core have no AI-native round.
3. **The size measure is looser.** The median workflow carries $21.0B of labour value, against a median of $3.0B of legacy spend per category. Almost every workflow looks large, so size rarely rules one out.
4. **AI usage is observed, not rated.** It agrees with category AI fit only loosely (rank correlation 0.46), so it surfaces different work.
5. **The index has no pass mark.** It ranks, so some workflow always comes first. The category tests can fail every category. The workflow index cannot.

Point 1 is mostly a consequence of the design. Lock-in is measured only per category, and the index puts every workflow that touches the core at or below all the rest, so the edges are bound to look more open than the core. Point 2 is the real finding: AI-native money is concentrated on a few workflows, and many edges have none. Points 3 and 5 are reasons to check each lead before acting on it.

## 5. The build-versus-buy lens

**In short.** Your idea was to ask, for each category and buyer size, whether buyers normally buy this software or build it themselves. Building in-house is uncommon. It shows up mostly where the system is critical and the buyer is very large: big banks, big mainframe users and governments. $42.5B (24%) of legacy spend sits with buyers who usually build or own the system. That spend still goes to vendors and integrators, but mostly for platforms and custom builds, not products a startup can sell. The lens matters more in this version, because three of the nine top-tier categories hold little buyable spend: government benefits ($0), agriculture ($0.05B) and mainframe ($0.6B). The lens also shows that the best first buyer is usually mid-market, while most of the money sits with large enterprises. None of these figures changed since version 2.

**Critical and important.** These terms are defined in Section 1. 22 categories are critical and 13 are important.

**Buyer segments.** Each category's research sets its own lines for enterprise, mid-market, small business and government, so the lines differ by category. Two examples:
- **Core banking.** Enterprise means banks above about $50B in assets, mid-market means $1B to $50B, and small business means under $1B.
- **Payroll.** Enterprise means firms with about 5,000 or more staff, mid-market means 50 to 1,000, and small business means 1 to 50.

**What the lens shows.** Buyable spend is legacy spend in segments marked Buys or Mixed, where building in-house is not the norm.
- **Critical categories:** $124.3B of legacy spend, of which $84.4B (68%) is buyable.
- **Important categories:** $53.7B, of which $51.0B (95%) is buyable.
- **Build segments.** 12 buyer segments are marked as building in-house being the norm. Three of them have no spend (land registry enterprise, mainframe government, agriculture government), so the tables show them as "-". Of the 9 with spend, 7 are in critical categories.

In the tables below, "Buys" means building in-house is rare, "Mixed" means some buyers build, "Builds" means building or owning the system is common, and "-" means the segment has no spend in this category. Spend is in USD B a year. Some "Buys" and "Mixed" cells carry very small spend. For example, airline reservations small business is $2.5M a year.

**Critical categories**

| Category | Enterprise | Mid-market | SMB | Government | Spend | Buyable | Best first buyer |
|---|---|---|---|---|---:|---:|---|
| Telecom billing | Mixed | Buys | Mixed | Mixed | 18.6 | 18.6 | Tier 2 and 3 operators, altnets, larger virtual operators |
| Hospital records (EHR) | Buys | Buys | Buys | Mixed | 12.7 | 12.7 | US rural and community hospitals under 100 beds |
| Card issuing and processing | Mixed | Buys | Buys | Buys | 12.2 | 12.2 | Issuers with 100K to 1.5M accounts |
| Government tax administration | - | - | - | Mixed | 7.1 | 7.1 | Small and mid-sized US counties |
| Retail point of sale | Mixed | Buys | Buys | - | 5.3 | 5.3 | Retailers with 10 to 200 stores |
| Loan origination and servicing | Mixed | Buys | Buys | Mixed | 5.2 | 5.2 | Mid-market lenders, $1B to $20B banks |
| Core banking | Builds | Buys | Buys | Mixed | 13.0 | 4.6 | Banks and credit unions with $1B to $10B in assets |
| Airline reservations | Buys | Buys | Buys | - | 3.0 | 3.0 | Airlines carrying 0.5M to 10M passengers a year |
| Insurance policy administration | Mixed | Buys | Buys | Mixed | 2.3 | 2.3 | Carriers and agencies with $100M to $1B premium |
| Pension and provident fund admin | Mixed | Buys | Buys | Mixed | 2.2 | 2.2 | Administrators and schemes of 1K to 50K members |
| Mortgage servicing | Mixed | Buys | Buys | - | 2.1 | 2.1 | US servicers with 25K to 500K loans |
| Wholesale distribution ERP | Mixed | Buys | Buys | - | 1.8 | 1.8 | Distributors with $20M to $500M revenue |
| Insurance claims | Builds | Mixed | Buys | - | 3.6 | 1.7 | Carriers and administrators with $50M to $1B premium |
| Warehouse management | Mixed | Buys | Buys | Mixed | 1.4 | 1.4 | Logistics firms and distributors with 1 to 5 sites |
| Laboratory information systems | Mixed | Buys | Buys | Mixed | 1.3 | 1.3 | US independent and specialty labs |
| Courts and justice case management | - | - | - | Mixed | 1.0 | 1.0 | US county and city courts, 50K to 1M residents |
| Land and property registry | - | - | - | Mixed | 0.7 | 0.7 | US county recorders, 50K to 1M residents |
| Custom COBOL and mainframe | Builds | Mixed | - | - | 14.5 | 0.6 | Firms running 400 to 2,000 MIPS of mainframe |
| Capital markets back office | Builds | Mixed | Buys | - | 2.7 | 0.5 | Mid-market brokers, mid-size Asian securities firms |
| Port terminal operating systems | Builds | Buys | - | Mixed | 0.4 | 0.1 | Independent terminals of 100K to 1M containers a year |
| Agriculture and commodity trading | Builds | Buys | Buys | - | 0.6 | 0.05 | Grain co-ops and farm retailers with 10 to 100 sites |
| Government benefits | - | - | - | Builds | 12.5 | 0.0 | Small and mid-sized US state agencies, one module at a time |

Telecom terms. Tier 2 and 3 operators are regional and smaller national carriers. Altnets are alternative network builders, mostly in fibre. Virtual operators (MVNOs) sell mobile service over another operator's network.

**Important categories**

| Category | Enterprise | Mid-market | SMB | Government | Spend | Buyable | Best first buyer |
|---|---|---|---|---|---:|---:|---|
| Payroll and HR | Mixed | Buys | Buys | - | 9.5 | 9.5 | US employers with 100 to 1,000 staff |
| Manufacturing ERP | Buys | Buys | Buys | - | 8.7 | 8.7 | Manufacturers with $20M to $500M revenue |
| Financial close and general ledger | Buys | Buys | Buys | - | 5.8 | 5.8 | Multi-entity firms with $20M to $1B revenue |
| Procurement and payables | Buys | Buys | Buys | - | 5.6 | 5.6 | Firms with 200 to 2,000 staff |
| Medical billing | Buys | Buys | Buys | Mixed | 4.8 | 4.8 | Physician groups with 20 to 300 providers |
| Co-op, rural and microfinance banking | Builds | Buys | Buys | - | 5.6 | 3.1 | Philippine rural banks in the central bank's SaaS scheme |
| Wealth and portfolio accounting | Mixed | Buys | Buys | - | 3.1 | 3.1 | Advisers and family offices with $1B to $20B assets |
| Utility billing | Mixed | Buys | Buys | Mixed | 2.5 | 2.5 | US city and co-op utilities with 10K to 100K meters |
| Field service and maintenance | Buys | Buys | Builds | - | 2.5 | 2.3 | Asset-heavy operators with 50 to 1,000 staff |
| Student information systems | Mixed | Buys | Mixed | Mixed | 2.1 | 2.1 | Colleges with 2,000 to 15,000 students |
| Construction project accounting | Mixed | Buys | Buys | - | 1.2 | 1.2 | Contractors with $10M to $250M revenue |
| Trade finance | Mixed | Buys | Buys | Buys | 1.2 | 1.2 | Mid-sized trade banks under $25B in assets |
| Licensing and permits | - | - | - | Mixed | 1.1 | 1.1 | US towns of 10K to 150K residents |

**What this changes about where to look.**
- **Some big pools are mostly held by buyers who build or own the system.**
  - **Mainframe.** About 96% of its $14.5B ($13.8B) sits with large enterprises, marked Builds, which leaves $0.6B buyable. Most of that $13.8B is platform spend paid to IBM and other vendors. What the enterprise owns is the application code. The best first buyer includes "the lower end of enterprise", whose spend sits inside the $13.8B counted as not buyable. The government segment is $0 because the buyer count found no government buyers. Yet the segment evidence prices agency mainframes at $0.3M to $150M a year, and the buyer profile names state agencies as the next step after the first buyer. That is a gap in the data.
  - **Government benefits ($12.5B).** All of it sits in the government segment, marked Builds. States mostly hire integrators (Deloitte, Accenture, Optum, FAST) to build or configure a system and then own it under federal funding rules. The data counts that as $0 buyable, but it is vendor spend. Vermont is paying FAST $28.1M to replace its unemployment insurance system. The best first buyer, state agencies buying one module at a time, sits in this same segment. Read the $0 as "no packaged core to sell", not "no vendor spend".
  - **Core banking.** It keeps $4.6B of its $13.0B buyable, because banks above about $50B in assets often run their own core.
- **Some large categories are mostly buyable at scale.** Telecom billing ($18.6B), hospital records ($12.7B), card processing ($12.2B) and payroll ($9.5B) all count as fully buyable. In hospital records, every commercial segment buys. In the other three, enterprise is Mixed (some large buyers build), and it holds 83% of telecom spend, 85% of card spend and 58% of payroll spend. Part of that money may not be open to a vendor.
- **The first buyer and the money live in different places.** On a broad reading, mid-market is the best first buyer in 27 of 35 categories, and local or state government in 6 more. That reading puts three borderline profiles in mid-market: mainframe ("lower end of enterprise and upper end of mid-market"), hospital records (rural hospitals under 100 beds, closer to small business) and co-op banking (rural banks). It also counts utility billing (city and co-op utilities) as government. Read strictly, mid-market leads in 24. Across all 35 categories, mid-market holds $20.6B of legacy spend. Enterprise holds $100.0B, government $42.1B and small businesses $15.3B. A founder enters at mid-market and has to move up to large buyers to reach most of the money.
- **Utility billing's money sits mostly with government and enterprise buyers.** Of its $2.5B, government holds $1.28B and enterprise $0.85B. Mid-market holds $0.34B. The best first buyer, city and co-op utilities, sits in the government segment.

## 6. Why COBOL and mainframe ranks where it does

**In short.** Mainframe now ranks 2nd at 69, up from 40 in version 2 and 65 in the first version 3 draft. The market did not change. The measures did. Lock-in fell from 5 to 2.5 and crowding from 5 to 2.0, and both drops partly reflect what the new measures leave out. It misses the search on lock-in by half a point. Before the rescore, 2.5 rounded up to 3 and the miss was a whole point. Its money is still held by large enterprises that own their code: only $0.6B of $14.5B is buyable.

**The numbers.** The positive factors add 11.3 points (size 4, pain 3.3, AI fit 4). The penalties take away 4.5 (lock-in 2.5, crowding 2.0). The net is 6.8, which scores 69. In version 2 the penalties took away 10.

**Pain: 3.3.**
- **Keep-alive share:** too few awards (6), left out.
- **Backend-failure share:** no app reviews, left out. Mainframe is a cross-industry category with few customer-facing apps of its own.
- **App rating:** 3 apps average 3.85 stars: score 3.
- **Failed or overrun replacements:** 5 of 9 (56%). 22 of 35 categories are lower: score 4. California's motor vehicles department cancelled its modernisation after 84 months and $134M. Pennsylvania cancelled its unemployment system after 84 months and $153M.
- **Workaround sign:** weak: score 3.
- **Average:** (3 + 4 + 3) / 3 = 3.33, kept as 3.3.

Version 2 gave mainframe pain 3 through Hacker News, where 44 of 68 firsthand-pain comments were about mainframes. Hacker News no longer feeds pain.

**Lock-in: 2.5.**
- **Contract length and non-competitive share:** too few awards (4 each), left out.
- **Replacement time:** median 69 months over 6 cases. 27 of 35 categories are shorter: score 4.
- **Regulator approval:** no: score 1. Under the single rule, no regulator approves or must be told in advance of a mainframe replacement as such. Banks and insurers must notify supervisors before material outsourcing, but those owners are coded in their own categories. The research marks this as borderline: it would flip to yes if any bank owner counted, which would lift lock-in to 4.5 and drop the total to 59.
- **Average:** (4 + 1) / 2 = 2.5, kept as 2.5. Before the rescore it rounded up to 3.

Version 2 gave mainframe the only lock-in of 5, from strong slow-replacement and skills signs plus regulation. Version 3 no longer reuses the legacy signs.

**Crowding: 2.0.**
- **AI-native with traction:** four. Mechanical Orchard, Cognition (Devin), Zengines and Anthropic (Claude Code): score 4.
- **AI-native funding per $1B:** four rounds in 24 months: Zengines ($9M), Kodesage ($2.4M and $6.6M) and Hypercubic ($5.3M). That is $23M, or $1.6M per $1B, the third lowest on the map after student information systems and tax administration: score 1. All four are category-specific, so the rescore did not change this input.
- **Y Combinator companies:** one: score 1.
- **Average:** (4 + 1 + 1) / 3 = 2.0.

**What the new crowding misses here.** Version 2 counted 12 challenger rows with $5.8B of disclosed funding, mostly Cognition's company-wide raises and Rocket Software's $2.275B purchase of the Micro Focus COBOL business. Version 3 counts neither, and since the rescore it leaves company-wide raises out everywhere, so telecom billing is treated the same way. It also does not count AWS, which gives its mainframe migration agent away, or IBM, which ships its own code assistant. The day Anthropic published its COBOL post in February 2026, IBM's share price fell 13%. Crowding 2.0 understates how contested this category is.

**Why buyable spend is small.** Large enterprises wrote their COBOL and still own it. They buy the platform and some outsourcing, then run the migration themselves or through integrators. That puts $13.8B of the $14.5B with buyers who own the system, though most of it is paid to platform vendors. Only the mid-market slice ($0.6B) is Mixed. Small businesses do not run mainframes. The government segment is set to $0, which Section 5 flags as a data gap.

**What the workflows add.** Customer and case inquiry lookups across mainframe screens rank 3rd among workflows that do not touch the core. They carry $55.2B of labour value, AI usage of 0.49 and no AI-native round mapped to them. Overnight batch scheduling and 3270 screen transaction entry also pass the stricter cut in Section 4A, though the second writes to the core.

**What the deep cases add.** Mechanical Orchard has retired applications, not whole mainframes. bloop sold AI conversion of COBOL to Java. It expected bank sales cycles of 18 to 24 months and left the category within about 15 months.

**What would have to be true for mainframe to be the best opening.**
1. **Lock-in drops to 2.0.** That happens if faster documented replacements pull the median replacement time down one fifth. Rounding no longer decides it. Mainframe would then pass all five search tests. As an inference, not a study finding: proof of equivalence, meaning evidence that new code gives exactly the same outputs as the old, is what would make replacements faster.
2. **Crowding stays low once fully counted.** If crowding counted company-wide raises, platform vendors' agents and acquisitions, it would rise again. The opening is real only if newcomers can win a step those players skip. As an inference: verification, producing proof of equivalence, is the step most likely to stay open.
3. **Enterprises start buying the outcome.** Large owners might hand migration to vendors on fixed-price or outcome terms. Much of the $13.8B would then become buyable, and mainframe would be one of the largest buyable pools on the map. Buyable spend is not part of the score, so this changes the build-versus-buy view, not the rank.

Until then, the realistic entry is the one the research names. That means smaller enterprises and upper mid-market firms running 400 to 2,000 MIPS (a measure of mainframe capacity) and spending $1M to $5M a year with mainframe vendors.

## 7. Regions

**In short.** The study split each category's spend across 11 regions. Treat the split as a rough guide only. It follows counts of possible buyers, not observed spending, and some of its results cannot be right. The published split has not changed since version 2. This round collected 369 named-organisation usage records for six Asian countries and the UK, which would widen coverage a lot once they are folded in.

Terms:
- **Usage evidence**: a source shows companies in that region running the legacy system.
- **Grade B**: two independent kinds of source agree. **Grade C**: one kind of source, or a modelled number. No estimate reached grade A.
- **Possible buyers**: organisations or sites summed across categories. The same firm can count several times, and site counts push the totals up.

| Region | Categories with usage evidence | Grades (B / C) | Categories with a buyer count | Possible buyers | Legacy spend, USD B | Share | Largest item, USD B |
|---|---:|---|---:|---:|---:|---:|---|
| European Union | 23 | 0 / 23 | 30 | 47.5M | 41.3 | 23% | Government benefits (11.0) |
| United States | 29 | 3 / 26 | 32 | 8.7M | 40.3 | 23% | Government tax administration (7.0) |
| India | 6 | 2 / 4 | 35 | 23.5M | 28.8 | 16% | Hospital records (11.9) |
| United Kingdom | 7 | 1 / 6 | 34 | 4.6M | 18.7 | 11% | Custom COBOL and mainframe (6.5) |
| Indonesia | 4 | 1 / 3 | 34 | 58.7M | 13.8 | 8% | Telecom billing (4.0) |
| Australia | 17 | 1 / 16 | 32 | 3.0M | 10.1 | 6% | Telecom billing (4.5) |
| Thailand | 6 | 1 / 5 | 33 | 3.6M | 6.0 | 3% | Telecom billing (3.2) |
| Singapore | 16 | 6 / 10 | 34 | 0.5M | 6.0 | 3% | Card issuing and processing (1.6) |
| Vietnam | 3 | 1 / 2 | 34 | 3.1M | 3.7 | 2% | Telecom billing (0.7) |
| Philippines | 2 | 2 / 0 | 33 | 1.5M | 3.5 | 2% | Telecom billing (0.9) |
| Malaysia | 3 | 1 / 2 | 33 | 3.0M | 2.8 | 2% | Payroll and HR (0.6) |
| Global, not assigned to a region | 30 | 1 / 29 | 2 | 718 | 2.9 | 2% | Airline reservations (1.8) |
| **Total** | | **20 / 126** | | | **178.0** | **100%** | |

Shares are rounded, so the rows sum to 101%.

**Observations.**
1. **The US and EU have the broadest evidence.** Together they hold $81.6B (46%) of the allocated spend. The US has usage evidence in 29 of 35 categories and the EU in 23, though all 23 EU estimates are grade C. Singapore is small ($6.0B) but has the best-graded evidence: 6 of its 16 estimates are grade B.
2. **India's share is mostly a side effect of how the split works.** India shows $28.8B but has usage evidence in only 6 categories. $16.3B of it is hospital records and medical billing, because India's health facility register counts hundreds of thousands of sites. As a result, the split puts $11.9B of hospital records spend in India and $0.4B in the US, which cannot be right.
3. **Telecom billing and small-business counts drive Southeast Asia's spend.** The six Southeast Asian countries hold $35.8B. Telecom billing is the largest item in four of them. Indonesia's 58.7M possible buyers come mostly from small-business counts. Outside Singapore, usage evidence covers only 2 to 6 categories per country.

**New this round, not yet in the split.** Research collected 369 records of named organisations running, replacing or planning to replace a legacy system, mostly from annual reports. 255 say in use, 64 replacing, 32 replaced and 18 planned. Once folded in, the number of categories with usage evidence would rise as follows:

| Region | Categories before | New records | Categories in new records | Categories after |
|---|---:|---:|---:|---:|
| India | 6 | 60 | 16 | 20 |
| Malaysia | 3 | 48 | 17 | 19 |
| Philippines | 2 | 54 | 16 | 18 |
| Indonesia | 4 | 45 | 14 | 17 |
| United Kingdom | 7 | 52 | 11 | 17 |
| Thailand | 6 | 52 | 15 | 16 |
| Vietnam | 3 | 58 | 10 | 13 |

The new pain inputs also reach beyond the US and EU. The 482 app listings span 19 App Store storefronts in all 11 regions, from 75 in the US to 34 in Singapore. The EU's 46 listings are split across Germany, France, the Netherlands, Italy, Spain and four other storefronts. The replacement ledger is weighted to the US (116 cases), the UK (58), Australia (54) and the EU (45), with 79 more across Asia and 1 in Canada.

## 8. Who is attacking and how

**In short.** Most AI-native challengers work on top of the old system. They automate steps and write the results back into the incumbent's system rather than replace it. Many are too early to have succeeded or failed, so the table cannot yet say which strategy works best. This round added a list of recent AI-native funding rounds and the recent Y Combinator batches, which now feed crowding.

**Strategies.**
- **Overlay**: AI works on top of the system of record and writes back to it.
- **Greenfield**: a new system of record for buyers the incumbent ignores or prices out.
- **AI-run service**: the challenger does the work itself with AI and licensed staff, and sells the outcome.
- **Migration-led**: the challenger wins by moving data and logic off the old core, with proof that nothing changed.
- **Acquire**: buy a legacy vendor or its customer book, then move it to a modern core.

| Strategy | Rows | AI-native rows | AI-native with traction | Other rows with traction | Stalled or failed |
|---|---:|---:|---:|---:|---:|
| Overlay | 214 | 119 | 61 (51%) | 72 of 95 (76%) | 6 |
| Greenfield | 144 | 31 | 16 (52%) | 81 of 113 (72%) | 8 |
| Migration-led | 33 | 3 | 2 | 22 of 30 (73%) | 3 |
| AI-run service | 27 | 20 | 12 (60%) | 2 of 7 | 2 |
| Acquire | 10 | 1 | 0 | 9 of 9 | 0 |

Eight more rows use other strategies.

**The overlay finding.** 119 of 177 AI-native rows (67%) are overlays. Only 3 lead with migration and 1 with acquisition. Most attempts to replace a core come from companies that are not AI-native. Examples are modern banking cores such as Thought Machine, Mambu and 10x, and Kraken in utility billing. This is also why the new crowding measure, which counts only AI-native challengers, can call a category open while a modern core vendor is winning in it.

**Outcomes are too young to judge.** 73 of 177 AI-native rows are early, against 23 of 259 other rows. Three strategies have 20 or more AI-native rows: overlay, greenfield and AI-run service. Their AI-native traction rates are close, at 51% to 60%. The other two have too few rows to compare: migration is 2 of 3 and acquire is 0 of 1. The gap with other rows may be mostly age. That is an inference taken from the playbook. The study records status, not company age. Only 19 of 436 rows are stalled or failed, and known failures such as Olive AI, we.trade and Marco Polo are missing. The table under-counts failure.

**New this round.**
- **Recent money.** Research listed 298 AI-native rounds announced between 1 October 2024 and 2 October 2026. 268 disclose an amount, totalling $11.0B. Hospital records ($1,983M) and telecom billing ($1,624M) drew the most. Each round is mapped to one workflow, and 297 of the 298 map to a listed workflow. 284 rows are rounds aimed at the category, 8 are company-wide raises ($2.0B, $1.6B of it Sierra and Wonderful in telecom billing) and 6 are exits or stake purchases (Section 2). Only the 284 feed crowding. Counting only those, hospital records ($1,983M) still drew the most, and telecom billing drew $40M.
- **Recent Y Combinator companies.** Of 1,939 companies in the 2024 to 2026 batches (3 of them from early 2027 batches), Jev placed 316 in a category. By October 2026, 50 of the 1,939 were inactive and 35 acquired. The study has not yet used this as a survival measure.

## 9. What the deep cases teach

**In short.** The eight cases are grouped here by strategy. The overlays grew by owning one step whose value a buyer can check in dollars. The greenfield companies won at a moment when buyers had to switch, and they did a lot of hands-on service. One AI-run service became the closest thing to a core replacement. The migration cases show that proof of equivalence is the product. None has displaced a dominant core. The cases did not change in this round.

**Overlay**

- **Adaptive (construction accounting).** Adaptive automates bills, lien waivers and field updates on top of the contractor's existing ledger. It grew from about 10 paying customers in January 2023 to 750+ companies by September 2026, with $57M raised. It had claimed over 1,000 in February 2026, so the count is unstable. In March 2024 its list price was $300 a month on top of QuickBooks. That is a list price, not a proven launch price. It has replaced hours of work, not ledgers. **Lesson:** enter below the vertical ERP's price floor. Make the product work without the customer's other parties signing up. Treat replacing the ledger as a separate bet.
- **AKASA (hospital billing).** AKASA reviews and codes inpatient stays on top of Epic and similar systems. Its customers hold $180B+ of net patient revenue and account for about 1 in 10 US inpatient discharges. As the case notes, that is the customers' share, not the volume AKASA itself codes. AKASA charges based on the revenue gain it can measure. Olive AI raised over $900M automating clicks across many tasks and shut down in 2023. **Lesson:** own one hard step whose output a customer can audit in dollars, and pick a step the platform has not shipped.

**Greenfield**

- **GovWell (permits).** GovWell sells a new cloud permitting system to small US towns. Founded in April 2023, it reached 200+ agencies in 40+ states, with $34.5M raised. Its published examples show go-lives of 3 to 11 weeks, and it has a three-month median sales cycle. 21 of its 71 staff work in deployment and support. It won on speed and service before AI led its marketing. **Lesson:** enter where a council vote decides the purchase. Its customers are mostly small. La Porte County (111,700 people) is one of the larger ones. Whether the model works for large cities is unproven, and that is an inference from its customer list.
- **Rillet (general ledger).** Rillet sells a new ledger to venture-backed companies. It reached 600+ customers and a $1B valuation by August 2026. About 30% came from NetSuite or Sage Intacct. That is roughly 180 companies, about 0.4% of NetSuite's base. Rillet says its own accountants run migrations in 4 to 6 weeks. The case also cites 4 to 8 weeks, and G2 reviews average about two months. **Lesson:** sell a system of record at the moment a company has to switch, here when it outgrows QuickBooks. Price high enough to fund hands-on migration.
- **Contour, we.trade and Marco Polo (trade finance, cautionary).** These were bank-owned networks that tried to replace paper letters of credit. we.trade went into liquidation in June 2022 and Marco Polo in February 2023. Contour's owners pulled funding in October 2023, when it handled 60 to 70 transactions a month. Meanwhile, document checkers that each bank could buy alone won J.P. Morgan, Lloyds and Citi. **Lesson:** a product that pays back inside one buyer gets bought. One that needs every counterparty to switch does not.

**AI-run service that became a core vendor**

- **Valon (mortgage servicing).** Valon built its own core and ran a licensed servicer on it, up to about 810,000 loans. Revenue was $41M in 2024 and $86M in 2025, and Valon has raised over $290M. In January 2026, Newrez agreed to move 4M+ homeowners onto the core from 2027. In August 2026, Valon sold its servicer to Carrington, which adopts the core. The first sale of a whole servicing operation took about six years. It went to a related party and moved off an in-house system, not off MSP. MSP is the market-leading servicing system, sold by ICE (Intercontinental Exchange). **Lesson:** in a regulated core market, running the business on your own software can be the pitch. It is slow and needs capital.

**Migration-led**

- **Mechanical Orchard (mainframe).** Mechanical Orchard records what the old system takes in and puts out. AI writes replacement code in slices, and each slice cuts over only when its outputs match the old ones byte for byte. It reported over $10M of revenue and a profit for 2023, with about 100 staff. It has retired applications, not whole mainframes. **Lesson:** once AI makes code cheap, proof of equivalence is the scarce product.
- **bloop (mainframe, cautionary).** bloop sold AI conversion of COBOL to Java on $7.43M raised. Its founder Louis expected bank sales cycles of 18 to 24 months, longer than its cash would last. That was his expected cycle, not deals that closed, as the case's fact-check notes. It pivoted in June 2025, and the successor company shut in April 2026. AWS later priced its own mainframe agent at zero. **Lesson:** make sure your cash lasts as long as the buyer's sales cycle, and do not build your advantage on a weakness of today's AI models.

## 10. The playbook in brief

**In short.** The playbook crosses the five strategies with four stages of growth. It shows what worked at each stage and where it broke. A guide then matches a category's scores and buyer to a strategy. The main message: start with one step a buyer can check, sold to one buyer. Treat replacing the core as a later, separate bet. The workflow search in Section 4A is consistent with this. It finds AI-native money concentrated on a few workflows, though its preference for the edges over the core partly follows from how the index is built.

**Stages.** First wedge (the first product a buyer pays for), first 10 customers, expand, replace the core.

| Strategy | First wedge | First 10 customers | Expand | Replace the core |
|---|---|---|---|---|
| Overlay | One step a buyer can audit, with no new screens (AKASA's pre-bill review, Adaptive's payables) | Founder-sold, priced on gains or below the cost of a hire | More steps and channels, such as 40+ accounting firms at Adaptive | Declined so far |
| Greenfield | A moment when the buyer must switch: outgrowing QuickBooks, small-town permits | Founder sales plus heavy service | Modules, departments, audit-firm partners | Partial: about 180 NetSuite or Intacct switches (QuickBooks moves excluded), one town taken from Accela |
| AI-run service | A licensed slice of one buyer's volume (Valon's subservicing, meaning servicing loans for their owner for a fee) | Investors who own volume | Volume and unit-cost proof: 593,000 loans and $86M revenue in 2025 | Sell the software; first sale to a related party, no MSP shop (servicer running MSP) yet |
| Migration-led | The job that sank the last project | Early customers, with about ten organisations described publicly at Mechanical Orchard | Groups of jobs, then whole applications, sold through integrators | Applications retired, no whole mainframe |
| Acquire | Buy a book of customers | Inherited with the book | Move the base to a new core | No case evidence yet |

**Decision guide.** The playbook's guide was written before the current measures, and the playbook itself has not been updated. Lock-in and crowding now run from 1 to 5 by ranking into fifths, with one decimal, so some rows are adjusted to the new scale:
- "Lock-in 2" is shown as "Lock-in 2.0 or less", because lock-in 1 now exists. "Lock-in 3" covers everything above 2.0 and under 3.5, and "Lock-in 4 or 5" is shown as "Lock-in 3.5 or more".
- "Crowding 5" is shown as "Crowding 3.5 or more", and "Crowding 3" as "Crowding 2.0 or less", because crowding now leans on AI-native counts and spreads across the scale.
- "Size 2 or 3" is shown as "A small market", "Size 5" is dropped because no category scores it, and "Pain 3" is dropped, as in version 2.
- Three pieces of advice are this report's additions, not the playbook's, and are marked "(report's addition)" in the table: a workflow that does not touch the core, checking the workflow list, and checking modern challengers that are not AI-native.

| If the category shows | Lean toward |
|---|---|
| Lock-in 2.0 or less | Greenfield or overlay |
| Lock-in above 2.0 and under 3.5 | Greenfield at a moment when buyers must switch, with hands-on migration (Rillet, GovWell) |
| Lock-in 3.5 or more | Overlay first, migration with proof of equivalence, greenfield for a buyer the incumbent ignores, or a workflow that does not touch the core (report's addition) |
| A small market | One buyer who gets the full return (Traydstream needed one bank; Contour needed four parties) |
| AI fit 4 | An agent or service that owns one judgment step |
| AI fit 3 or less | Workflow software and service first, agents later |
| Crowding 3.5 or more | The step platforms and funded rivals skip; check the workflow list for edges with no AI-native rounds (report's addition) |
| Crowding 2.0 or less | Open ground among AI-native challengers, but check budgets and study coverage, and modern challengers that are not AI-native (report's addition) |

By buyer:
- **Small businesses:** enter below the incumbent's price floor, at a moment when they must switch.
- **Enterprises:** sell a slice the buyer can try inside its current process, and budget for long cycles.
- **Government:** enter where a council vote decides the purchase.

**Failure patterns.** The playbook names four:
- Incumbents absorb the challenger. At least 8 of the 39 acquired rows went to an incumbent in the same category.
- Sales cycles outrun the cash (bloop).
- Bank consortia cannot agree to fund their own networks (Contour, we.trade, Marco Polo).
- Point tools become platform features. Epic and AWS now ship steps that challengers once sold. ICE's agents are in beta. NetSuite has announced autonomous close, with rollout within 12 months.

## 11. Where to look next

**In short.** The version 2 filter is kept with a higher score bar. It keeps categories that score 60 or more, have at least $1B of buyable spend, and have two or fewer AI-native challengers with traction. Five pass. Utility billing also passes all five search tests. Government tax administration is new to the list after the regulator recode. Airline reservations, laboratory information systems and trade finance left it, because the rescore put them below 60. Eight more score 60 or more but fail the filter: five on challengers alone, two on buyable spend alone, and mainframe on both. At the workflow level, the best leads are the edges of the categories that come closest: customer contact and collections in utility billing, inquiry lookups in mainframe, taxpayer contact in tax administration, disputes and order capture in telecom billing, and progress billing in construction accounting. These are candidates to check, not a ranking.

| Category | Total | Criticality | Buyable spend, USD B | AI-native rows (with traction) | Passes the five search tests? |
|---|---:|---|---:|---:|---|
| Utility billing | 69.5 | Important | 2.5 | 3 (0) | Yes |
| Government tax administration | 66.5 | Critical | 7.1 | 2 (0) | No, AI fit 3 and lock-in 3.0 |
| Student information systems | 64 | Important | 2.1 | 4 (0) | No, lock-in 3.5 |
| Core banking | 61 | Critical | 4.6 | 2 (0) | No, pain 2.2 and lock-in 3.0 |
| Courts and justice | 60.5 | Critical | 1.0 | 5 (2) | No, lock-in 3.7 |

**Near misses.** Five fail on challengers alone. Manufacturing ERP (67, $8.7B buyable) has 5 AI-native challengers with traction. Construction accounting (67, $1.2B), telecom billing (66.5, $18.6B) and payroll (60.5, $9.5B) each have 3. Licensing and permits (60.5, $1.1B) has 4. Two fail on buyable spend alone: agriculture (64, $0.05B, 1 challenger with traction) and government benefits (62.5, $0). Mainframe (69) fails on both: $0.6B buyable and 4 AI-native challengers with traction. Three categories on the first version 3 list now score below 60: airline reservations (56.5), after its regulator answer became yes, and laboratory information systems (58) and trade finance (57), because keeping one decimal removed rounding in their favour. Their pain (2.8 and 1.7) no longer rounds up, laboratory information systems' lock-in of 2.25 no longer rounds down to 2, and trade finance's crowding of 1.3 no longer rounds down to 1. Laboratory information systems' funding input also moved up a fifth, which keeps its crowding at 2.0. Mortgage servicing, on the version 2 list, now scores 52.

1. **Utility billing.**
   - **Why:** the only category to pass all five search tests, though narrowly (Section 4A). Pain 3.6, resting on all five inputs, including 6 of 12 documented replacements failed or overrun and 20% of 250 app reviews flagging backend failures. No AI-native challenger has traction.
   - **First buyer:** US municipal and co-op utilities with 10,000 to 100,000 meters, bought mostly through government procurement. Each pays about $60K to $600K a year. The research says to plan for migrations of 6 to 18 months.
   - **Main risk:** modern challengers that are not AI-native. Kraken raised a $1B round at an $8.65B valuation in December 2025, and six challengers that are not AI-native have traction. The buyer profile also warns of sole-source renewals with the current vendor. The award data shows no non-competitive awards in 12, but all 12 come from the EU tender database, and none of the 50 utility billing awards is from the US, where the best first buyer sits. One non-competitive award would fail lock-in. Kraken also launched autonomous agents built with Sierra in June 2026.
2. **Government tax administration.**
   - **Why:** crowding 1.0, the lowest on the map, and $7.1B buyable. Neither AI-native challenger has traction: Staple AI and CAMAai are early. Its one category-specific AI-native round is a $3.9M credit facility. Pain is 3.3: apps average 3.05 stars over 13 apps, and 5 of 11 documented replacements failed or overran. Since the regulator recode its lock-in is 3.0, from a 72-month median replacement and no regulator gate.
   - **First buyer:** small and mid-sized US counties and municipal tax collectors on ageing systems. There are about 3,100 US counties, they buy rather than build, and deals run about $50K to $3M a year.
   - **Main risk:** AI fit 3, with a task average of 3.46, so it fails the search on AI fit as well as lock-in. Its regulator answer is borderline. An IRS data-protection notice is due 45 days before federal tax data moves to a contractor or cloud, and the rule excludes it. Counted as yes, the total would drop to 56.5. Modern challengers that are not AI-native already hold the ground: Tyler dominates US county property tax, FAST's GenTax holds 35 state agencies, often on sole-source renewals, and Quantexa and Palantir have traction.
3. **Student information systems.**
   - **Why:** pain 3.6 and crowding 1.3. Its apps average 2.46 stars over 9 apps, and 6 of 11 documented replacements failed or overran. No AI-native challenger has traction, and its recent AI-native rounds total about $1M.
   - **First buyer:** US community and private colleges with about 2,000 to 15,000 students, and UK further-education colleges, facing a vendor-forced move to cloud software. They spend $150K to $1M a year, and many sit near or below Workday Student's $300K minimum.
   - **Main risk:** lock-in 3.5. Contracts run a median 60 months over 23 awards, 18% of awards were made without competition, and replacements take a median 60 months.
4. **Core banking.**
   - **Why:** $4.6B buyable among mid-market and small banks. Neither AI-native challenger has traction: Maximum is pre-revenue and Saris AI is early. Of its 10 recent AI-native rounds ($422M), only Maximum's $30M targets the core ledger. The rest fund lending, onboarding and service workflows.
   - **First buyer:** banks and credit unions with $1B to $10B in assets. They spend $0.4M to $4M a year on their core, and about a sixth of their six-year contracts come up for renewal each year.
   - **Main risk:** weak measured pain (2.2) and few switches. 8% of 150 bank app reviews flag backend failures and apps average 4.29 stars. One consultant estimated in 2015 that about 4% of banks switch per renewal. Modern cores that are not AI-native already win here, and Thought Machine has signed 68 banks.
5. **Courts and justice case management.**
   - **Why:** pain 3.8 and crowding 2.0. 13 of 18 public awards keep the old system alive, and California's statewide system was cancelled after 108 months and $407M.
   - **First buyer:** US county and city courts serving 50K to 1M people, in states where each court picks its own system. Contracts run $50K to $850K a year.
   - **Main risk:** lock-in 3.7. Contracts run a median 72 months and replacements a median 102 months. The $1.04B market sits right on the size line. Two AI-native challengers were bought: Learned Hand (by Clio) and jAI. Learned Hand became the core of Clio's new judiciary business, so the upside is uncertain rather than shown to be limited.

**At the workflow level.** The strongest leads are where the category and workflow views agree:
- **Utility billing:** customer contact on high bills and complaints (7th, AI usage 0.66, one mapped round, which is an exit), and credit and collections (11th, AI usage 0.41, none).
- **Mainframe:** customer and case inquiry lookups across mainframe screens (3rd, AI usage 0.49, none).
- **Government tax administration:** taxpayer contact centre and account inquiries (1st, AI usage 0.57, none), and paper return intake (15th, AI usage 0.22, none).
- **Telecom billing:** bill disputes, credits and adjustments (6th, AI usage 0.60, none), and order capture and number porting (14th, AI usage 0.11, none).
- **Construction accounting:** progress billing, retainage, lien waivers and collections (5th, AI usage 0.60, none).

## 12. What this study cannot tell you yet

**In short.** This round attacked the weakest parts of version 2: pain, lock-in, crowding and the thin evidence outside the US and EU. Pain and crowding now rest mostly on counts, and lock-in no longer reuses the legacy test. The new measures bring their own limits. Lock-in leans on a yes-or-no regulator input, two of crowding's three inputs count only AI-native companies, and workflow sizes count whole occupations. Three limits the first version 3 draft listed are now fixed: uneven regulator coding, rounding halves up, and company-wide raises counted in one category but not another. Size, the regional split, AI fit and the cases did not change.

Each gap below shows what version 2 said, what this round did, and what remains. Version 2's gap list had 12 items. Gaps 2 and 4 come instead from weaknesses named in the body of version 2 (its Sections 4.4 and 4.5), so items 1 to 14 cover the 12 listed gaps plus those two.

1. **Pain was barely measured.** Version 2 scored pain 2 or 3 everywhere, from 68 Hacker News comments and a job-post rule that changed three scores when unweighted.
   - **Done:** pain now averages five inputs built from 2,718 app reviews, 438 apps, 423 public awards labelled maintain, extend or replace, 353 documented replacements and the workaround grade. Scores now run 1.7 to 4.4, kept to one decimal.
   - **Remains:** keep-alive reaches its minimum in 13 categories and backend failure in 18. 15 categories rest on three inputs or fewer. App inputs measure end customers. Awards are mostly European. The replacement ledger favours famous projects and lists some projects twice. No source asks buyers directly.
2. **Lock-in reused the legacy signs and did not measure switching.**
   - **Done:** lock-in now uses contract length, non-competitive share, replacement time and regulator approval, none of which comes from the legacy test.
   - **Done in the rescore:** the regulator input now follows one written rule for all 35 categories: yes only when, in the US, EU or UK, a sector regulator must approve, or be formally told in advance of, replacing or outsourcing the core system. Seven answers changed, which moved airline reservations from 70 to 56.5 and government tax from 55 to 66.5. Lock-in also keeps one decimal now, so the 15 averages that sat on a half no longer round up. That alone lifted mainframe from 65 to 69.
   - **Remains:** 25 of 35 categories rest on two inputs, so one regulator answer moves a total by 10. Five answers are marked borderline (airline reservations, medical billing, retail, tax administration and mainframe). The definition is still wider than the plan's "approval required". Switching rates are still not measured.
3. **Crowding mixed things.** Version 2 counted challengers that were not AI-native, incumbents' tools and failed or acquired challengers, stopped rising at 9 rows, and included purchase prices.
   - **Done:** crowding now counts AI-native challengers with traction, AI-native rounds in 24 months scaled to market size, and recent Y Combinator companies. It has no cap, and it no longer uses the funding parser.
   - **Done in the rescore:** each round now carries a scope, and only the 284 category-specific rounds count toward funding per $1B. Eight company-wide raises ($2.0B) and six exits or stake purchases are left out, so Sierra no longer counts in telecom billing just as Cognition and Anthropic never counted in mainframe. Telecom billing's crowding fell from 2.7 to 1.7.
   - **Remains:** it ignores modern challengers that are not AI-native, such as Kraken. Incumbents' own AI is not counted. The scope tags are research judgments, two of them borderline. 24 of the 284 category-specific rounds lack amounts. Workflow crowding still counts every row. The scores are relative.
4. **The funding parse bug.** Version 2 found that the parser read only the first amount written with "$".
   - **Done:** scoring no longer depends on it.
   - **Remains:** the parser itself is unfixed, so the funding text in the challenger table still reads wrongly in places, including the currency errors in agriculture.
5. **Demand from public tenders was unproven.** Blind labellers put about 80% of keyword-matched tenders in no legacy category.
   - **Done:** 1,922 public contract awards with values, dates and procedures replaced keyword tenders. Jev's category label agreed with blind labels 92% of the time.
   - **Remains:** 1,457 of the 1,922 come from the EU. Contract length and non-competitive share reach their minimum in only 8 and 9 categories. The action label passed only when collapsed to three choices, a choice made after the audit.
6. **AI fit was a model's view.**
   - **Done:** the workflow data adds observed AI usage from the Anthropic Economic Index. Its rank correlation with AI fit by category is 0.46.
   - **Remains:** the category score is still Jev's rating, about half a point high against blind labels, checked on task order but not category order.
7. **Usage counts were rough.** 126 of 146 regional usage estimates were grade C.
   - **Done:** 369 named-organisation usage records for India, Indonesia, Malaysia, the Philippines, Thailand, Vietnam and the UK. Categories with usage evidence would rise to 13 to 20 per country.
   - **Remains:** the records are not yet folded into the regional estimates or their grades. The published file still shows 126 of 146 at grade C.
8. **The region and buyer-size splits follow buyer counts, not spending.**
   - **Done:** nothing this round.
   - **Remains:** 90% of medical billing spend still lands with government, $11.9B of hospital records spend in India, and $0 in mainframe's government segment.
9. **Size is an estimate with wide bounds.**
   - **Done:** nothing this round.
   - **Remains:** 18 of 35 spending ranges cross a size line. The legacy share is a judgment call. Categories can overlap: custom mainframe code runs inside banks, insurers and agencies.
10. **Coverage gaps in job data.** India and EU job data were thin, and Naukri, Glints and Reddit were not reachable.
    - **Done:** job posts and Hacker News no longer feed the score. App stores cover all 11 regions, and annual reports cover six Asian countries and the UK.
    - **Remains:** Naukri, Glints, Reddit, G2, Gartner and Capterra stay out of reach. A gap in the study is not necessarily a gap in the market.
11. **Failures were under-counted.** Only 19 of 436 challenger rows are stalled or failed.
    - **Done:** the replacement ledger records buyer-side failures: 42 cancelled and 116 late or over among 353 projects. The Y Combinator list records 50 inactive and 35 acquired companies since 2024.
    - **Remains:** the challenger table is unchanged, and known failures such as Olive AI, we.trade and Marco Polo are still missing from it. Y Combinator survival is collected but not scored.
12. **The audit used model labels.**
    - **Done:** the three new labelling questions were audited blind on 60 items each. The award sample was random. The app review and Y Combinator samples were 30 random items plus 30 that Jev had labelled positive.
    - **Remains:** the app review and Y Combinator agreement figures overweight positives, so they do not measure agreement across the whole population. The labels are still from Claude agents, not people. The optional check of 150 human labels is not scheduled. Two choices were made after seeing an audit: the Hacker News pain cut and the collapsed award action.
13. **Eight cases.**
    - **Done:** nothing this round.
    - **Remains:** company figures are unaudited unless stated. Some steps are inferred and labelled as inferred.
14. **Weights are a choice.**
    - **Done:** nothing this round.
    - **Remains:** all five factors count equally, and so do the inputs inside each factor. Ranking into fifths, keeping one decimal for pain, lock-in and crowding, and rounding AI fit to a whole number are choices too. Readers can re-weight factors on the site.

New gaps this round:

15. **Workflow labour value counts whole occupations.** It sums to $6.3T over 210 workflows because the same occupations count many times. The top-ranked workflow, taxpayer contact, carries $85.1B, nearly all of it 70% of the working time of every US customer service representative (about 1.8M full-time equivalents). It is not the largest. Several carry more, from order picking ($152.1B) down to government benefits' call centre ($86.8B).
16. **Workflow pain is borrowed from the category, and "touches core" is a research judgment.** Some mainframe screen work is marked as not touching the core.
17. **AI usage is zero for 51 of 210 workflows.** All 51 matched O*NET tasks (2 to 14 each), and the Economic Index records 0 for those tasks. Zero means no Claude usage was recorded for them. The index covers Claude only, not AI use in general, so a zero does not show that no one uses AI for the work.

## 13. Decisions for Hansel about the site

**In short.** The same five choices shape what a reader takes away. The recommendations shift with the new measures. Lead with tiers and show buyable spend. Offer the five-test search as a filter, with its caveats. Show pain with its inputs. Keep Valon for the timeline. Launch after a short fix list.

1. **Which ranking view leads?**
   - (a) The published total, with size based on all legacy spend.
   - (b) A total with size based on buyable spend only. Seven categories move: government benefits 62.5 to 47.5, mainframe 69 to 59, core banking 61 to 56, agriculture 64 to 59, port terminals 58 to 53, co-op banking 55 to 50 and capital markets 50.5 to 45.5.
   - (c) The published total shown as three tiers, with buyable spend beside each category and sortable.
   - **Recommend (c),** with each factor's inputs and n one click away. Three of the nine top-tier categories hold little buyable spend, so readers need buyable spend in view. A second score would add confusion.
2. **Shortlist or filter?**
   - (a) Name the five categories from Section 11.
   - (b) A filter that defaults to the five search tests in Section 4A, can switch to the Section 11 rule, and shows each result's main risk.
   - (c) No shortlist.
   - **Recommend (b).** Only utility billing passes the five tests, narrowly, and its low crowding ignores Kraken. Courts, in Section 11, sits right on the $1B size line, and government tax administration rests on a borderline regulator answer. Readers should see the rule and its doubts, not a verdict. Add the workflow list as a second tab, labelled as leads.
3. **How to show pain?**
   - (a) As it is.
   - (b) As it is, with each input, its n, and a flag on the 15 categories that rest on three inputs or fewer.
   - (c) Drop it from the default total. Mainframe would then lead alone.
   - **Recommend (b).** Pain now has real evidence behind it, and the named failed replacements are the most persuasive content on the site. Version 2 recommended flagging pain as weak. That now holds only for the thinly covered categories.
4. **Which case gets the timeline?**
   - (a) Valon: dated steps from its 2021 Series A to the 2026 Newrez and Carrington deals.
   - (b) Mechanical Orchard: it fits the mainframe chapter.
   - (c) GovWell: from 12 agencies in July 2024 to 200+ in October 2026.
   - **Recommend (a).** It came closest to replacing a core. Its caveats carry the honest lesson: six years, a related-party first buyer, and no MSP shop yet.
5. **When to launch?**
   - (a) Now, as a versioned release.
   - (b) After a short fix list:
     - Decide whether crowding should count modern challengers that are not AI-native.
     - Done in the rescore: one rule for company-wide raises (only category-specific rounds count), one decimal instead of rounding halves up, and one written regulator rule applied to all 35 categories.
     - Decide the five borderline regulator answers, and whether the rule means approval only, as the plan said, or also formal advance notice, as this report uses.
     - Decide whether AI fit should also keep one decimal. Tax administration would gain 2.5 points.
     - Label workflow labour value on the page as the pay of whole occupations, not category spend.
     - Fold the 369 new usage records into the regional estimates, and label the regional split as a rough guide.
     - Update the playbook where it still quotes old scores, size unit errors, the Size 5 row and the old shortlist.
     - Update the size description in the rubric and the evidence strings that still describe size as buyers times segment spend.
     - Fill mainframe's government segment or explain its $0. Note on the page that government benefits' $0 buyable still means vendor spend.
     - Fix the funding parser for the challenger table display.
     - Update the repo's README status, which still says no findings yet, and merge the working branch.
   - (c) After a check of 150 human labels and new job data for India and the EU.
   - **Recommend (b).** The three fixes already done moved top-tier scores by up to 13.5 points. The open crowding rule and the borderline regulator answers could move them as much again, so they belong in the release. Option (c) is blocked by access to sources more than money: all the labelling so far cost $0.67.

## 14. Where the numbers come from

All paths are relative to `/Users/hansel/conductor/repos/legacy-software-atlas`, branch `chore/bootstrap` at commit 4d05769 (not yet merged to `main`). Sums, shares, spreads, correlations, alternative views, the Section 4A search, the Section 11 filter, the version 2 comparison and the split of each change across the three fixes were computed for this report from the files listed. The three fixes are commits 3dad361 (one decimal; category-specific rounds only) and 4d05769 (regulator recode, round scopes, rescored exports). The v3 column comes from `exports/site/scores.json` at commit 6b8495c, the first version 3 draft. Version 2 totals come from `exports/site/scores.json` at commit 2a1c9c9, with telecom billing and laboratory information systems corrected to 40 and 30 as version 2 reported.

| Section | Files |
|---|---|
| 1. Answer | All files below |
| 2. Method | `research/categories.csv` (legacy test, 46 candidates); `research/market_size.csv` (top-down spend, legacy share); `configs/rubric.toml` (factor rules, input minimums, direct scores); `src/lsa/measures.py` and `src/lsa/measures_raw.py` (fifths rule, input definitions); `src/lsa/scores.py` (averaging to one decimal, total); `src/lsa/workflows.py` and `src/lsa/workflows_labour/labour.py` (workflow index, labour value, AI usage); `docs/superpowers/plans/2026-10-05-plan-3-better-measures.md` (measure definitions); `data/derived/awards.parquet` (1,922 awards by source); `data/derived/apps.parquet` (482 listings); `data/derived/items.parquet` (2,718 reviews, 1,939 Y Combinator items); `data/derived/yc.parquet`; `research/apps.csv`; `research/replacement_cases.csv` (353 cases); `research/regulator_approval.csv` (17 yes, 18 no; `rule` column states the single rule); `research/ai_native_rounds_24m.csv` (298 rows; `scope` column: 284 category_specific, 8 company_wide, 6 exit_or_stake); `research/challengers.csv`; `research/workflows.csv` and `research/workflow_occupations.csv` (210 workflows, occupations, time shares); `configs/questions.toml` (Jev question wording); `docs/reports/jev-audit.md` (all audits, including plan 3); `data/derived/jev_ledger.jsonl` (sum of `cost_usd` = $0.67 over 5,023 calls; plan 3 passes $0.26 over 1,704 calls and 6,576 items); `configs/budgets.toml` ($8 cap); `README.md` (TypeSafe disclosure, data sources) |
| 3. Map | `exports/site/scores.json` (totals, parts, sub-scores); `exports/site/categories.json` (`market` low, mid, high; `build_vs_buy.criticality`); `exports/site/scores.json` at 2a1c9c9 (version 2 totals) |
| 4. Factors | `exports/site/scores.json` (`detail.sub_scores`: raw, n, score per input; `detail.mean`; AI fit means); `research/replacement_cases.csv` (named cases, outcomes, durations, costs); `research/regulator_approval.csv` (notes); `research/challengers.csv` (AI-native names, status, Kraken); `research/ai_native_rounds_24m.csv` (rounds, amounts); `exports/site/workflows.json` (AI usage by category); `docs/reports/jev-audit.md` |
| 4A. Search | `exports/site/scores.json`; `exports/site/categories.json` (buyable value, segments); `exports/site/workflows.json` (210 workflows: labour value, AI usage, touches core, pain, crowding, opportunity index); `data/derived/workflows.parquet` (employment share); `research/workflow_occupations.csv`; `research/challengers.csv` |
| 5. Build vs buy | `exports/site/categories.json` (`build_vs_buy`: criticality, segments, segment evidence, buyable value, best first buyer); `research/criticality.csv` |
| 6. Mainframe | `exports/site/scores.json` and `exports/site/categories.json` (mainframe entry); `research/replacement_cases.csv`; `research/regulator_approval.csv`; `research/ai_native_rounds_24m.csv`; `research/challengers.csv`; `exports/site/workflows.json`; `cases/mechanical-orchard.md`; `cases/bloop.md` |
| 7. Regions | `exports/site/regions.json` (usage, grades, buyers, value per region; unchanged since 2a1c9c9); `research/regional_usage.csv` (369 new records); `research/apps.csv`; `research/replacement_cases.csv` (regions); `docs/reports/2026-10-05-pre-jev.md` (unreachable sources) |
| 8. Challengers | `research/challengers.csv` (436 rows); `research/ai_native_rounds_24m.csv`; `data/derived/yc.parquet` (status); `exports/site/scores.json` (Y Combinator counts); `playbook/playbook.md` (strategy table, age inference) |
| 9. Cases | `cases/adaptive.md`, `cases/akasa.md`, `cases/govwell.md`, `cases/rillet.md`, `cases/trade-finance-networks.md`, `cases/valon.md`, `cases/mechanical-orchard.md`, `cases/bloop.md` (fact-check on the sales cycle) |
| 10. Playbook | `playbook/playbook.md` (stages table, choosing a strategy, failure patterns) |
| 11. Openings | `exports/site/scores.json`; `exports/site/categories.json` (buyable value, segments, best first buyer); `research/challengers.csv` (AI-native counts and status); `research/ai_native_rounds_24m.csv`; `research/replacement_cases.csv`; `exports/site/workflows.json`; `cases/valon.md`; `cases/trade-finance-networks.md`; `playbook/playbook.md` (trade finance dropped) |
| 12. Limits | `docs/reports/jev-audit.md`; `exports/site/regions.json`; `research/regional_usage.csv`; `exports/site/scores.json`; `exports/site/workflows.json`; `data/derived/awards.parquet`; `data/derived/yc.parquet`; `src/lsa/parse_counts.py`; `playbook/playbook.md` |
| 13. Decisions | Computed from `exports/site/scores.json` and `exports/site/categories.json`; `playbook/playbook.md`; `configs/rubric.toml`; `src/lsa/scores.py`; `src/lsa/parse_counts.py`; `README.md` |
