# Which legacy software is ready for AI-native replacement

Review report for Hansel, version 3. Data as of 5 October 2026.

## 0. How to read this report

Section 1 gives the question and the answer on one page. Section 2 explains how the study was done, including the new measures for pain, lock-in and crowding. Section 3 shows all 35 categories in one table and says what moved since version 2. Section 4 explains each factor, with one worked example per factor and full tables for pain, lock-in and crowding. Section 4A is new. It answers your question directly: is anything sizeable, painful and a good fit for AI, with low lock-in and low crowding? It answers at the level of categories and at the level of workflows. Section 5 adds your build-versus-buy lens. Section 6 explains where COBOL and mainframe now ranks. Section 7 covers regions. Sections 8 to 10 cover the challengers, the eight deep cases and the playbook. Section 11 names where to look next. Section 12 lists each gap in the study, what this round did to shrink it, and what remains. Section 13 sets out five decisions about the site, meaning the public website that will present the atlas. Section 14 maps every section to its source files. Sections 1 to 13 each start with a short summary in plain words, then the detail.

## 1. The question and the answer in one page

**In short.** The study asked which kinds of old business software an AI-native company could realistically replace, and where a founder should look first. This version measures pain, lock-in and crowding mostly from counts of real events, plus a regulator judgment and the workaround grade, instead of proxies. The order changed a lot. Utility billing now leads alone at 75. It is the only category that is sizeable, painful, a good fit for AI, only mildly hard to leave, and lightly crowded by AI-native challengers. Its pass is narrow, and three inputs could each undo it (Section 4A). Six more categories miss by one point. The search finds more inside categories, at the level of single workflows that do not touch the core system. Two cautions apply. Low crowding here means few AI-native challengers, not few challengers. And workflow sizes count whole US occupations, so they rank workflows but do not size markets.

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
- **Ranking into fifths**: the new measures score a category 1 to 5 by where it sits against the other categories. The bottom fifth scores 1 and the top fifth scores 5. Section 2 explains the rule.

**Headline conclusions**

1. **The map is unchanged.** 35 of 46 candidate categories passed a strict legacy test. Their legacy spend adds to about $178B a year on midpoints, or $118B to $271B if you add the low and high estimates. Categories range from $0.4B (port terminals) to $18.6B (telecom billing).
2. **The ranking now spreads out.** Scores run from 30 to 75 on a 0 to 100 scale. Utility billing leads alone at 75. Telecom billing, airline reservations and construction project accounting follow at 70. In version 2 the range was 30 to 50, with five categories tied at the top.
3. **The new measures moved the order more than any new market fact.** The rank correlation between the version 2 and version 3 totals is 0.36. A rank correlation measures, from -1 to 1, how closely two lists agree on order, and 1 means the same order. The average total rose from 41 to 56, and no category fell. Most of the rise comes from crowding. Its average fell from 4.6 to 2.9, because two of its three inputs now count only AI-native companies (the third counts all recent Y Combinator companies) and each input ranks categories into fifths.
4. **One category passes all five search tests, narrowly.** Utility billing has $2.5B of legacy spend, all of it buyable, with pain 4, AI fit 4, lock-in 2 and crowding 1. Three things could each undo the pass: AI fit 4 uses Jev's score, which runs about half a point high; lock-in sits exactly on 2.0; and its regulator answer is a close call (Section 4A). Six miss by one point: telecom billing and construction accounting on crowding, airline reservations on pain, mainframe on lock-in, agriculture on size, and laboratory information systems on AI fit.
5. **Workflows widen the search.** 130 of 210 workflows do not touch the core system. 55 of those have no AI-native funding round mapped to them in 24 months. Each round is mapped to one workflow, and two exits in the rounds list are left out. 17 of the 55 also sit in categories with pain 3 or more and show AI usage at or above the median. Collections and arrears work recurs: five of the 17. Customer contact appears twice, and billing disputes and inquiry lookups once each.
6. **Mainframe rises to 65, but its money is still mostly not for sale.** Lock-in fell from 5 to 3 and crowding from 5 to 2. Both drops partly reflect what the new measures leave out (Section 6). Only $0.6B of its $14.5B is buyable.
7. **The build-versus-buy and challenger findings are unchanged.** $42.5B (24%) of legacy spend sits with buyers who usually build or own the system. Mid-sized firms are the best first buyer in most categories but hold only $20.6B (12%) of the spend, against $100.0B (56%) for large enterprises. 119 of 177 AI-native challenger rows work on top of the old system rather than replace it. None of the eight deep cases has displaced a market-leading core.

**How much to trust this.** Pain, lock-in and crowding now rest mostly on counts: 2,718 app reviews, 438 apps, 1,922 public contract awards, 353 replacement projects, 298 AI-native funding rounds and 1,939 Y Combinator companies. They also use a yes-or-no regulator judgment and the old workaround grade, and the app rating is a proxy for pain. Coverage is uneven. Lock-in for 25 of 35 categories rests on only two inputs, and 15 lock-in scores round up from exactly half a point. Crowding ignores modern challengers that are not AI-native, such as Kraken in utility billing. The workflow labour values count every US worker in an occupation, across all industries, and sum to $6.3T over 210 workflows. Read the ranking as three tiers, not 35 places.

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
3. **Average.** The factor is the average of the available input scores, rounded to the nearest whole number, with exact halves rounded up.

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
| Lock-in | Regulator approval | Yes if a regulator must approve the switch, or must be formally notified and review it. Yes scores 5 and no scores 1 | Research per category, with cited rules | 35 | 14 yes, 21 no |
| Crowding | AI-native with traction | Number of AI-native challengers with named customers or reported revenue | The challenger table (Step 4) | 35 | 92 challengers |
| Crowding | AI-native funding per $1B | Disclosed AI-native funding rounds in the 24 months to 2 October 2026, divided by the category's legacy spend in billions | A list of 298 rounds, 268 with amounts, $11.0B in all. Five rows are exits or stake purchases (see below) | 35 | 298 rounds |
| Crowding | Y Combinator companies | Companies from Y Combinator's 2024 to 2026 batches that sell software doing the category's work, AI-native or not. Y Combinator is a startup accelerator | Y Combinator's public company list (1,939 companies, 3 of them from early 2027 batches), labelled by Jev | 35 | 316 companies |

A median is the middle value when the values are sorted. Size and AI fit did not change. The total is still 35 + 5 x (size + pain + AI fit - lock-in - crowding), which puts every possible result on a 0 to 100 scale. All five factors are weighted equally, and so are the inputs inside each factor.

**Changes from the approved plan.** Three definitions differ from plan 3, and the plan did not record the change:
- **Failed or overrun replacements** is a share of all documented cases. The plan defined it as a count per $1B of legacy spend.
- **Keep-alive share** is a share of award counts. The plan defined it as a share of public IT spend.
- **Regulator approval** counts a switch that must be formally notified and reviewed as well as one that must be approved. The plan defined it as "regulator approval required".

**Exits in the rounds list.** Five of the 298 rows record an exit or a stake purchase rather than a plain funding round: Learned Hand's sale to Clio, BHC Global's majority purchase of POWERCONNECT.AI, a private-equity majority stake in Arkstone, and a strategic minority stake in Valon (listed under two categories). None has a disclosed amount, so funding per $1B is unaffected. They still count in each category's number of rounds and in workflow crowding. Section 4A removes the two that sit on workflows that do not touch the core.

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
- **Crowding**: how many AI-native rounds research mapped to this workflow. Each round is mapped to exactly one workflow. 297 of the 298 rounds are mapped, and one card-processing round maps to no listed workflow. 96 workflows have none. Two of the mapped rows are exits (see above).
- **Pain**: the category's pain score.

The **opportunity index** ranks each workflow against the other 209 on labour value, AI usage and pain, where higher is better, and on crowding, where higher is worse. It adds the first three ranks and subtracts the fourth. A workflow that touches the core gets a penalty large enough to put it at or below every workflow that does not. One core-touching workflow ties at -109 with the lowest workflow that does not touch the core (title search). The index runs from -679 to 462.

**Cost and audit.** The bulk labelling was done by Jev, a non-generative classifier sold by TypeSafe. The study has no affiliation with TypeSafe. Jev labelled job posts, tenders, vendor and integrator stories, Hacker News comments, AI fit, and this round's contract awards, app reviews and Y Combinator companies. It cost $0.67 in total over 5,023 calls, well inside the $8 cap. This round ran four labelling runs (awards, app reviews, and Y Combinator twice, once per wording). They cost $0.26 over 1,704 calls, covering 6,576 distinct items and 8,515 item labels. Separate Claude agents labelled samples blind, without seeing Jev's answers. The award audit used a random sample. The app review and Y Combinator audits each used 30 random items plus 30 that Jev had labelled positive, so their agreement figures overweight positives and are not agreement across the whole population. The bar was 80% agreement. Questions under it were reworded once or dropped. This round's results:
- **Award category**: 92%, used.
- **Award action** (maintain, extend, replace, consult, other): 70% on five choices. Collapsed to keep-alive, replace or other, it reached 83% and was used that way. The collapse was chosen after seeing the audit.
- **App review backend failure**, counted at a probability of 0.7 or more: 87%, used.
- **Y Combinator category**: 67% on the first wording, 85% after one rewording, used. The second score was measured against labels made for the first wording, which already applied the stricter reading.

From earlier rounds, the "reason to stay" question scored 79% and is used only as colour, and the Hacker News pain cut of 0.7 was chosen after seeing its audit. Neither Hacker News comments nor job posts feed the pain score any more. Jev rated tasks about half a point more automatable than the blind labels did.

## 3. The whole map

**In short.** All 35 categories score between 30 and 75. Eight sit in the top tier (65 to 75), 15 in the middle (55 and 60) and 12 at the bottom (30 to 50). The penalties, lock-in and crowding, now do most of the sorting. One step on any factor still moves a total by 5, so small changes in evidence can move a category a whole tier.

Ties are listed by legacy spend. Criticality is defined in Section 1. The v2 column shows each total in version 2, including the two corrections that report made for a funding parse bug (telecom billing 40 and laboratory information systems 30).

| # | Category | Legacy spend, USD B: low to high (mid) | Criticality | Total | v2 | Size | Pain | AI fit | Lock-in | Crowding |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Utility billing | 1.5 to 4.2 (2.5) | Important | 75 | 35 | 3 | 4 | 4 | 2 | 1 |
| 2= | Telecom billing | 13.2 to 26.2 (18.6) | Critical | 70 | 40 | 4 | 4 | 4 | 2 | 3 |
| 2= | Airline reservations | 2.2 to 4.0 (3.0) | Critical | 70 | 45 | 3 | 2 | 4 | 1 | 1 |
| 2= | Construction project accounting | 0.8 to 1.8 (1.2) | Important | 70 | 45 | 3 | 4 | 4 | 1 | 3 |
| 5= | Custom COBOL and mainframe | 11.1 to 19.0 (14.5) | Critical | 65 | 40 | 4 | 3 | 4 | 3 | 2 |
| 5= | Government benefits | 7.5 to 21.0 (12.5) | Critical | 65 | 45 | 4 | 4 | 4 | 5 | 1 |
| 5= | Manufacturing ERP | 6.0 to 12.7 (8.7) | Important | 65 | 50 | 4 | 4 | 3 | 1 | 4 |
| 5= | Student information systems | 1.2 to 3.6 (2.1) | Important | 65 | 40 | 3 | 4 | 4 | 4 | 1 |
| 9= | Core banking | 9.6 to 17.5 (13.0) | Critical | 60 | 50 | 4 | 2 | 4 | 3 | 2 |
| 9= | Payroll and HR | 6.0 to 15.0 (9.5) | Important | 60 | 45 | 4 | 3 | 4 | 3 | 3 |
| 9= | Retail point of sale | 3.1 to 8.8 (5.3) | Critical | 60 | 40 | 4 | 4 | 3 | 3 | 3 |
| 9= | Laboratory information systems | 0.9 to 2.0 (1.3) | Critical | 60 | 30 | 3 | 3 | 3 | 2 | 2 |
| 9= | Trade finance | 0.7 to 2.1 (1.2) | Important | 60 | 50 | 3 | 2 | 4 | 3 | 1 |
| 9= | Licensing and permits | 0.7 to 1.8 (1.1) | Important | 60 | 50 | 3 | 4 | 4 | 2 | 4 |
| 9= | Courts and justice case management | 0.7 to 1.6 (1.0) | Critical | 60 | 50 | 3 | 4 | 4 | 4 | 2 |
| 9= | Agriculture and commodity trading | 0.4 to 1.0 (0.6) | Critical | 60 | 45 | 2 | 3 | 4 | 2 | 2 |
| 17= | Card issuing and processing | 8.4 to 17.6 (12.2) | Critical | 55 | 40 | 4 | 2 | 4 | 3 | 3 |
| 17= | Government tax administration | 4.5 to 11.2 (7.1) | Critical | 55 | 40 | 4 | 3 | 3 | 5 | 1 |
| 17= | Wealth and portfolio accounting | 2.0 to 4.8 (3.1) | Important | 55 | 40 | 3 | 4 | 4 | 4 | 3 |
| 17= | Pension and provident fund admin | 1.4 to 3.6 (2.2) | Critical | 55 | 35 | 3 | 3 | 4 | 4 | 2 |
| 17= | Mortgage servicing | 1.4 to 3.1 (2.1) | Critical | 55 | 45 | 3 | 2 | 4 | 3 | 2 |
| 17= | Wholesale distribution ERP | 0.8 to 4.0 (1.8) | Critical | 55 | 40 | 3 | 4 | 3 | 2 | 4 |
| 17= | Port terminal operating systems | 0.3 to 0.7 (0.4) | Critical | 55 | 40 | 2 | 2 | 3 | 1 | 2 |
| 24= | Procurement and payables | 3.5 to 9.0 (5.6) | Important | 50 | 45 | 4 | 2 | 4 | 3 | 4 |
| 24= | Co-op, rural and microfinance banking | 4.0 to 7.8 (5.6) | Important | 50 | 35 | 4 | 2 | 3 | 4 | 2 |
| 24= | Medical billing | 2.6 to 8.8 (4.8) | Important | 50 | 45 | 3 | 4 | 4 | 3 | 5 |
| 24= | Capital markets back office | 1.5 to 4.9 (2.7) | Critical | 50 | 35 | 3 | 2 | 4 | 3 | 3 |
| 28= | Hospital records (EHR) | 9.3 to 17.2 (12.7) | Critical | 45 | 40 | 4 | 3 | 3 | 3 | 5 |
| 28= | Financial close and general ledger | 3.0 to 11.2 (5.8) | Important | 45 | 45 | 4 | 2 | 4 | 3 | 5 |
| 28= | Loan origination and servicing | 3.5 to 7.7 (5.2) | Critical | 45 | 45 | 4 | 3 | 4 | 4 | 5 |
| 28= | Field service and maintenance | 1.8 to 3.5 (2.5) | Important | 45 | 35 | 3 | 4 | 3 | 3 | 5 |
| 28= | Warehouse management | 1.0 to 2.1 (1.4) | Critical | 45 | 35 | 3 | 3 | 2 | 2 | 4 |
| 28= | Land and property registry | 0.5 to 1.2 (0.7) | Critical | 45 | 40 | 2 | 3 | 4 | 5 | 2 |
| 34 | Insurance policy administration | 1.4 to 3.8 (2.3) | Critical | 40 | 35 | 3 | 2 | 4 | 4 | 4 |
| 35 | Insurance claims | 2.0 to 6.5 (3.6) | Critical | 30 | 30 | 3 | 2 | 3 | 5 | 4 |

**Top tier (65 to 75, eight categories).** Each earns 9 to 12 points from the positive factors (size, pain, AI fit) and loses 2 to 6 to the penalties. Airline reservations loses only 2 and utility billing 3. Three of the eight are among the six pools above $12B: telecom billing, mainframe and government benefits. Government benefits and student information systems reach the top tier despite lock-in of 5 and 4, because both score crowding 1.

**Middle tier (55 and 60, 15 categories).** These earn 7 to 11 points and lose 3 to 7. The four categories tied at the top of version 2 alongside manufacturing ERP now sit here at 60: core banking, trade finance, licensing and permits, and courts.

**Bottom tier (30 to 50, 12 categories).** These lose 6 to 9 points to the penalties, and 9 of the 12 lose 7 or more. Five score the maximum crowding of 5: medical billing, hospital records, financial close, loan origination, and field service. Insurance claims is last at 30, with lock-in 5 and crowding 4.

**What separates the tiers.** The penalties do more of the work than in version 2. Points from the positive factors run from 7 to 12, and penalties run from 2 to 9. Their standard deviations (how much they vary) are 1.15 and 1.66 points. Their correlations with the total (how closely they move with it, from -1 to 1) are +0.51 and -0.80.

By factor:

| Factor | Standard deviation | Correlation with total |
|---|---:|---:|
| Size | 0.62 | +0.08 |
| Pain | 0.84 | +0.42 |
| AI fit | 0.53 | +0.33 |
| Lock-in | 1.15 | -0.48 |
| Crowding | 1.31 | -0.59 |

Crowding sorts the list most, then lock-in, then pain. Size sorts it least, because 32 of 35 categories score 3 or 4 on it. Ranking into fifths spreads lock-in and crowding across the whole 1 to 5 scale by design, which is why they now vary most.

**What moved since version 2, and why.**
- **The range widened from 30 to 50 to 30 to 75, and the average rose from 41 to 56.** No category fell. Three stayed level: financial close (45), loan origination (45) and insurance claims (30).
- **Crowding fell most.** Its average went from 4.6 to 2.9. Version 2 counted every challenger row, AI-native or not, including failed and acquired ones, and stopped rising at 9 rows. That gave 24 categories the maximum of 5. Version 3 counts AI-native challengers with traction, recent AI-native funding scaled to market size, and recent Y Combinator companies (AI-native or not), and ranks each into fifths. Five categories now score 5.
- **Pain rose and spread.** Its average went from 2.2 to 3.0. In version 2, 28 categories scored 2. Now 12 score 2, 10 score 3 and 13 score 4.
- **Lock-in fell slightly and spread.** Its average went from 3.3 to 3.0. It now runs from 1 to 5, and no longer reuses the legacy signs.
- **The biggest movers.** Utility billing rose 40 points (35 to 75): pain up 2, lock-in down 2, crowding down 4. Telecom billing and laboratory information systems rose 30. Airline reservations, construction accounting, mainframe and student information systems rose 25. Each gained on at least two of three counts: lower crowding, lower lock-in and higher pain.
- **The former top tier.** Core banking, trade finance, courts, and licensing and permits each rose 10, less than most. They had moderate crowding in version 2 already, so they gained less when crowding was re-measured. Manufacturing ERP rose 15 to 65.

## 4. What drives the ranking

**In short.** Crowding and lock-in sort the list most. Pain now has real evidence behind it and sorts the list more than AI fit or size. Each factor has a weakness worth knowing before you quote a rank. The two that matter most: lock-in leans heavily on a yes-or-no regulator input, and two of crowding's three inputs count only AI-native companies.

### 4.1 Size

**What it measures.** Annual legacy spend, scored on the midpoint.

**Worked example: utility billing.** Its legacy spend runs from $1.5B to $4.2B. The midpoint is the square root of 1.5 times 4.2, which is $2.5B. That sits between $1B and $5B, so size scores 3.

**How it varies.** No category reaches size 5, because telecom billing's $18.6B midpoint sits just under the $20B line. 14 categories score 4, 18 score 3, and 3 score 2 (agriculture, land registry and port terminals).

**What it lifts or sinks.** Size 4 lifts telecom billing, mainframe, government benefits and manufacturing ERP within the top tier. Size 2 holds agriculture and port terminals down despite low penalties.

**Weakness.** The ranges are wide, and 18 of 35 cross a bin line. The fragility runs both ways:
- **Downward.** Courts ($1.04B), permits ($1.13B) and trade finance ($1.17B) sit just above the $1B line. At their low estimates, all three would score size 2 and fall from 60 to 55.
- **Upward.** At their high estimates, telecom billing ($26.2B) and government benefits ($21.0B) reach size 5, and medical billing ($8.8B) reaches size 4. Telecom billing would then score 75 and tie utility billing. Government benefits would score 70 and medical billing 55.

The share still on legacy is a judgment call. It ranges from 15% to 35% in capital markets, and up to 95% in the highest case.

### 4.2 Pain

**What it measures.** How much buyers and their customers suffer from the old system. Pain is the average of up to five inputs, defined in Section 2: keep-alive share of public contracts, backend-failure share of app reviews, inverted app rating, the failed or overrun share of documented replacements, and the workaround sign.

**Worked example: utility billing.** It is one of seven categories with all five inputs.
- **Keep-alive share.** 50 public awards were labelled, and 45 of them were labelled maintain, extend or replace. 24 of those 45 (53%) maintain or extend the old system. 8 of the 13 categories with enough awards have a lower share. 8 divided by 13, times 5, is 3.1. Drop the fraction and add 1: score 4.
- **Backend-failure share.** 49 of 250 app reviews (20%) complain about a backend failure. 12 of 18 categories are lower: score 4.
- **App rating.** Its 24 customer-facing apps average 3.41 stars. 19 of 30 categories have better ratings, so less pain: score 4.
- **Failed or overrun replacements.** 6 of 12 documented replacements (50%) were cancelled or finished late or over budget. 16 of 35 categories are lower: score 3.
- **Workaround sign.** Weak: score 3.
- **Average.** (4 + 4 + 4 + 3 + 3) / 5 = 3.6, which rounds to 4.

**What the pain evidence looks like.** The inputs count real events. Some of the cases behind them:
- **Courts.** California's statewide court case management system was cancelled in 2012 after 108 months and $407M. 13 of 18 labelled public awards for courts keep the old system alive.
- **Government benefits.** The US Social Security Administration's disability case processing system was cancelled after 91 months and $356M. Services Australia's entitlements calculation engine was cancelled after 48 months and $127M. 8 of 11 documented replacements failed or overran.
- **Payroll.** California's State Controller cancelled its 21st Century Project after 94 months and $373M. Queensland Health's payroll replacement finished late or over at $166M.
- **Retail point of sale.** Lidl cancelled its replacement after 84 months and $590M.
- **Utility billing.** Duke Energy's Customer Connect took 58 months and $900M and finished late or over. The regulator research records an Ohio case where the state commission proposed a $1.45M fine and ordered an audit after more than 106,000 billing errors.
- **Manufacturing ERP.** 8 of 10 documented replacements finished late or over, including Clorox at $580M over 48 months.
- **Telecom billing.** 75 of 200 app reviews (38%) describe a backend failure, the highest share among categories with 100 or more reviews. Telstra's replacement took 118 months and $690M.
- **Loan origination and hospital records.** 23 of 50 lending app reviews (46%) and 31 of 100 hospital app reviews (31%) describe backend failures.

Across the ledger, 158 of 353 documented replacements (45%) were cancelled or finished late or over budget. 116 finished late or over, 42 were cancelled or rolled back, 90 finished on time and 105 are still running.

**All 35 categories.** Each cell shows the raw value, the number of observations in brackets, and the 1 to 5 score in bold. "Too few" means the input had data below its minimum and was left out. Categories are in the order of Section 3.

| Category | Pain (mean) | Keep-alive awards | Backend-failure reviews | App rating | Failed or overrun replacements | Workaround sign |
|---|---|---|---|---|---|---|
| Utility billing | 4 (3.60) | 53% (45): **4** | 20% (250): **4** | 3.41 (24): **4** | 50% (12): **3** | weak: **3** |
| Telecom billing | 4 (3.50) | too few (3) | 38% (200): **5** | 4.09 (33): **2** | 58% (12): **4** | weak: **3** |
| Airline reservations | 2 (2.00) | too few (6) | 12% (380): **2** | 4.28 (27): **2** | 8% (12): **1** | weak: **3** |
| Construction project accounting | 4 (3.67) | no data | no data | 2.05 (7): **5** | 50% (8): **3** | weak: **3** |
| Custom COBOL and mainframe | 3 (3.33) | too few (6) | no data | 3.85 (3): **3** | 56% (9): **4** | weak: **3** |
| Government benefits | 4 (3.75) | too few (3) | 18% (100): **3** | 3.37 (20): **4** | 73% (11): **5** | weak: **3** |
| Manufacturing ERP | 4 (4.33) | 71% (17): **5** | no data | no data | 80% (10): **5** | weak: **3** |
| Student information systems | 4 (3.60) | 27% (44): **2** | 20% (54): **4** | 2.46 (9): **5** | 55% (11): **4** | weak: **3** |
| Core banking | 2 (2.20) | 20% (15): **1** | 8% (150): **1** | 4.29 (33): **2** | 60% (10): **4** | weak: **3** |
| Payroll and HR | 3 (3.40) | 30% (10): **2** | 19% (150): **4** | 3.05 (5): **4** | 64% (11): **4** | weak: **3** |
| Retail point of sale | 4 (4.00) | too few (1) | no data | no data | 75% (8): **5** | weak: **3** |
| Laboratory information systems | 3 (2.80) | 45% (20): **3** | 20% (100): **4** | 3.63 (22): **3** | 20% (10): **1** | weak: **3** |
| Trade finance | 2 (1.67) | no data | no data | 4.33 (6): **1** | 14% (7): **1** | weak: **3** |
| Licensing and permits | 4 (4.40) | 55% (11): **4** | 18% (50): **3** | 2.93 (6): **5** | 78% (9): **5** | strong: **5** |
| Courts and justice case management | 4 (3.75) | 72% (18): **5** | too few (17) | 3.05 (15): **4** | 50% (10): **3** | weak: **3** |
| Agriculture and commodity trading | 3 (3.00) | no data | no data | 3.66 (6): **3** | 18% (11): **1** | strong: **5** |
| Card issuing and processing | 2 (2.00) | too few (3) | 14% (250): **2** | 4.33 (25): **1** | 33% (12): **2** | weak: **3** |
| Government tax administration | 3 (3.33) | too few (7) | no data | 3.05 (13): **4** | 45% (11): **3** | weak: **3** |
| Wealth and portfolio accounting | 4 (4.00) | too few (3) | too few (3) | 2.35 (3): **5** | 60% (10): **4** | weak: **3** |
| Pension and provident fund admin | 3 (3.25) | too few (2) | 18% (300): **2** | 3.50 (23): **3** | 67% (9): **5** | weak: **3** |
| Mortgage servicing | 2 (1.67) | no data | no data | 4.83 (3): **1** | 20% (10): **1** | weak: **3** |
| Wholesale distribution ERP | 4 (4.33) | too few (1) | no data | 1.66 (8): **5** | 70% (10): **5** | weak: **3** |
| Port terminal operating systems | 2 (2.33) | too few (2) | too few (12) | 3.62 (14): **3** | 17% (12): **1** | weak: **3** |
| Procurement and payables | 2 (2.33) | 25% (12): **1** | no data | no data | 50% (10): **3** | weak: **3** |
| Co-op, rural and microfinance banking | 2 (2.25) | no data | 18% (100): **3** | 3.93 (8): **2** | 8% (12): **1** | weak: **3** |
| Medical billing | 4 (3.67) | too few (1) | too few (36) | 3.41 (10): **4** | 22% (9): **2** | strong: **5** |
| Capital markets back office | 2 (1.75) | too few (2) | 8% (50): **1** | 4.57 (7): **1** | 42% (12): **2** | weak: **3** |
| Hospital records (EHR) | 3 (2.80) | 0% (63): **1** | 31% (100): **5** | 3.84 (27): **3** | 42% (12): **2** | weak: **3** |
| Financial close and general ledger | 2 (2.33) | 42% (12): **2** | no data | no data | 30% (10): **2** | weak: **3** |
| Loan origination and servicing | 3 (2.75) | too few (2) | 46% (50): **5** | 4.87 (3): **1** | 30% (10): **2** | weak: **3** |
| Field service and maintenance | 4 (3.50) | 62% (34): **4** | too few (6) | 4.25 (4): **2** | 67% (9): **5** | weak: **3** |
| Warehouse management | 3 (3.33) | 47% (74): **3** | no data | no data | 62% (8): **4** | weak: **3** |
| Land and property registry | 3 (2.75) | too few (6) | 0% (51): **1** | 2.80 (10): **5** | 30% (10): **2** | weak: **3** |
| Insurance policy administration | 2 (2.25) | no data | 12% (50): **2** | 4.39 (31): **1** | 50% (8): **3** | weak: **3** |
| Insurance claims | 2 (2.00) | no data | 10% (259): **1** | 4.10 (33): **2** | 38% (8): **2** | weak: **3** |

**How it varies.** 12 categories score 2, 10 score 3 and 13 score 4. None scores 1 or 5. Licensing and permits has the highest average (4.40), and trade finance and mortgage servicing the lowest (1.67).

**What it lifts or sinks.** Pain 4 lifts student information systems into the top tier: with pain 3 it would score 60. Utility billing, telecom billing and construction accounting also score pain 4, but with pain 3 they would still be in the top tier at 70, 65 and 65. Pain 2 holds airline reservations, core banking, trade finance and mortgage servicing back.

**Weakness.**
- **Coverage is uneven.** Keep-alive share reaches its minimum in 13 categories and backend-failure share in 18. 15 categories rest on three inputs or fewer. Retail point of sale rests on two: its replacement record and the workaround sign.
- **The app inputs measure end customers.** They come from customer-facing apps, such as a bank's or a carrier's app. A legacy back end causes only part of what those customers complain about.
- **The awards lean European and public.** 1,457 of 1,922 awards come from the EU's public tender database. A high keep-alive share can also mean the old system works well enough. Hospital records shows 0 of 63 because its public awards are replacements.
- **The replacement ledger favours famous projects.** Failures get written up more than quiet successes. Ongoing projects count in the base, which lowers the rate for categories in the middle of replacing. Some projects appear in two categories, such as Commonwealth Bank and Centrelink under both their own category and mainframe, and Pennsylvania's unemployment system under government benefits ($170M) and mainframe ($153M), with different costs.
- **The workaround sign barely varies.** 32 of 35 categories grade weak, so it pulls averages toward 3.
- **Sensitivity.** Without the workaround sign, manufacturing ERP and mainframe rise to 70. Without pain at all, airline reservations would lead alone.

### 4.3 AI fit

**What it measures.** Jev scored 12 core tasks per category for how much of each AI could do. The scores are weighted by how much time each task takes, averaged and rounded.

**Worked example: utility billing.** Its 12 tasks average 3.61 after weighting by time share, which rounds to 4. Government tax administration averages 3.46, which rounds to 3.

**How it varies.** 24 categories score 4, 10 score 3, and only warehouse management scores 2. The averages run from 2.499 (warehouse, just under 2.5, so it rounds down) to 4.13 (construction accounting).

**What it sinks.** The ten categories at 3 lose a point against the rest. They include hospital records, both ERP categories, retail, tax administration and laboratory information systems. AI fit 3 is what keeps laboratory information systems from passing the search in Section 4A.

**Weakness.** Jev rated tasks about half a point more automatable than blind labellers (3.46 against 2.97). Across 60 sampled tasks, the two agreed on order with a rank correlation of 0.83. That is a check on tasks, not on the category order. Rounding also creates cliffs: tax administration averages 3.46 and scores 3, while card processing averages 3.52 and scores 4. The audit says AI fit should rank categories against each other, never act as an absolute claim. The search in Section 4A uses "AI fit 4 or more" as an absolute bar. On the blind labellers' scale, about 0.49 lower, only construction accounting (4.13) and payroll (4.07) would still score 4.

**A second view.** The workflow data adds an independent measure: how much the category's work already shows up in AI usage, from the Anthropic Economic Index. Averaged per category, it agrees with AI fit only loosely. The rank correlation is 0.46. AI fit is a rating of what AI could do. The Economic Index records what people already use Claude for.

### 4.4 Lock-in

**What it measures.** How hard it is for a buyer to leave the old system. It counts against the score.

**How it is derived, step by step.**
1. **Contract length.** Take every public award that Jev placed in the category and that states a start and end date. Find the median length in months. A category needs at least 10 such awards.
2. **Non-competitive share.** Take every award in the category with a known procedure. Find the share awarded without open competition. A category needs at least 10 such awards.
3. **Replacement time.** Take every documented replacement in the ledger with a start and end date. Find the median length in months. A category needs at least 3.
4. **Rank each of these three into fifths** among the categories that have enough data. Longer contracts, more non-competitive awards and longer replacements score higher.
5. **Regulator approval.** Score 5 if a regulator must approve the switch or must be formally notified and review it, and 1 if not.
6. **Average** the available scores and round, with exact halves rounded up.

**Worked example: student information systems.** It is one of seven categories with all four inputs.
- **Contract length.** The median of 23 awards is 60 months. 6 of the 8 categories with enough awards have shorter contracts. 6 divided by 8, times 5, is 3.75. Drop the fraction and add 1: score 4.
- **Non-competitive share.** 3 of 17 awards (18%) were made without competition. 8 of 9 categories are lower: score 5.
- **Replacement time.** The median of 7 documented replacements is 60 months. 21 of 35 categories are shorter: score 4. Los Angeles Unified's student system replacement was cancelled after 72 months and $112M.
- **Regulator approval.** No regulator approves or must be notified of the switch: score 1.
- **Average.** (4 + 5 + 4 + 1) / 4 = 3.5, which rounds up to 4.

**All 35 categories.** Each cell shows the raw value, the number of observations in brackets, and the 1 to 5 score in bold. "Too few" means the input had data below its minimum and was left out. "No data" means none was found. "mo" means months.

| Category | Lock-in (mean) | Contract length (median) | Non-competitive awards | Replacement time (median) | Regulator approval |
|---|---|---|---|---|---|
| Utility billing | 2 (2.00) | 48 mo (18): **3** | 0% (12): **1** | 40 mo (9): **3** | no: **1** |
| Telecom billing | 2 (1.50) | no data | no data | 36 mo (11): **2** | no: **1** |
| Airline reservations | 1 (1.00) | too few (4) | too few (4) | 14.5 mo (12): **1** | no: **1** |
| Construction project accounting | 1 (1.00) | no data | no data | 6 mo (5): **1** | no: **1** |
| Custom COBOL and mainframe | 3 (2.50) | too few (4) | too few (4) | 69 mo (6): **4** | no: **1** |
| Government benefits | 5 (5.00) | too few (1) | too few (4) | 84 mo (9): **5** | yes: **5** |
| Manufacturing ERP | 1 (1.25) | 12 mo (15): **1** | 0% (14): **1** | 38 mo (5): **2** | no: **1** |
| Student information systems | 4 (3.50) | 60 mo (23): **4** | 18% (17): **5** | 60 mo (7): **4** | no: **1** |
| Core banking | 3 (3.00) | too few (5) | 0% (14): **1** | 57 mo (7): **3** | yes: **5** |
| Payroll and HR | 3 (3.00) | too few (5) | too few (8) | 81.5 mo (10): **5** | no: **1** |
| Retail point of sale | 3 (2.50) | no data | no data | 63 mo (6): **4** | no: **1** |
| Laboratory information systems | 2 (2.25) | 36.1 mo (19): **2** | 10% (20): **4** | 36 mo (5): **2** | no: **1** |
| Trade finance | 3 (3.00) | no data | no data | 27 mo (4): **1** | yes: **5** |
| Licensing and permits | 2 (2.00) | too few (5) | too few (8) | 49 mo (7): **3** | no: **1** |
| Courts and justice case management | 4 (3.67) | 72 mo (15): **5** | too few (8) | 102 mo (5): **5** | no: **1** |
| Agriculture and commodity trading | 2 (1.50) | no data | no data | 39.5 mo (4): **2** | no: **1** |
| Card issuing and processing | 3 (3.00) | too few (3) | too few (6) | 16 mo (9): **1** | yes: **5** |
| Government tax administration | 5 (5.00) | too few (6) | too few (8) | 72 mo (6): **5** | yes: **5** |
| Wealth and portfolio accounting | 4 (3.50) | too few (9) | too few (8) | 36 mo (9): **2** | yes: **5** |
| Pension and provident fund admin | 4 (4.00) | too few (4) | 10% (10): **4** | 57.5 mo (8): **3** | yes: **5** |
| Mortgage servicing | 3 (3.00) | no data | too few (1) | 24 mo (3): **1** | yes: **5** |
| Wholesale distribution ERP | 2 (2.00) | no data | no data | 41 mo (5): **3** | no: **1** |
| Port terminal operating systems | 1 (1.00) | too few (2) | no data | 34 mo (4): **1** | no: **1** |
| Procurement and payables | 3 (2.50) | too few (5) | too few (9) | 60 mo (7): **4** | no: **1** |
| Co-op, rural and microfinance banking | 4 (3.50) | no data | no data | 39 mo (8): **2** | yes: **5** |
| Medical billing | 3 (2.50) | too few (2) | no data | 60 mo (6): **4** | no: **1** |
| Capital markets back office | 3 (3.00) | too few (1) | too few (1) | 30.5 mo (10): **1** | yes: **5** |
| Hospital records (EHR) | 3 (2.50) | 48 mo (14): **3** | 0% (17): **1** | 104 mo (5): **5** | no: **1** |
| Financial close and general ledger | 3 (3.00) | too few (6) | too few (5) | 73 mo (4): **5** | no: **1** |
| Loan origination and servicing | 4 (4.00) | too few (2) | too few (2) | 40 mo (5): **3** | yes: **5** |
| Field service and maintenance | 3 (2.50) | 12 mo (43): **1** | 5% (56): **3** | 94 mo (7): **5** | no: **1** |
| Warehouse management | 2 (1.50) | 12 mo (65): **1** | 0% (30): **1** | 48 mo (3): **3** | no: **1** |
| Land and property registry | 5 (4.50) | too few (5) | too few (5) | 60 mo (5): **4** | yes: **5** |
| Insurance policy administration | 4 (3.50) | no data | too few (1) | 35.5 mo (8): **2** | yes: **5** |
| Insurance claims | 5 (4.50) | no data | no data | 60 mo (4): **4** | yes: **5** |

**How it varies.** 4 categories score 1, 7 score 2, 13 score 3, 7 score 4 and 4 score 5.

**What the table shows.**
- **The regulator input carries the most weight.** All 14 categories where a regulator must approve or review the switch score 3 or more: 5 score 3, 5 score 4 and 4 score 5. The 21 without score from 1 to 4. All four 5s have a regulator: government benefits, tax administration, land registry and insurance claims.
- **Most categories rest on two inputs.** Contract length and non-competitive share reach their minimum in only 8 and 9 categories. For the other 25, lock-in is the average of replacement time and the regulator answer.
- **The lowest lock-in.** Airline reservations (median replacement 14.5 months over 12 cases), construction accounting (6 months over 5), manufacturing ERP (12-month contracts, no non-competitive awards in 14, 38-month replacements) and port terminals (34 months over 4) score 1.
- **The longest replacements.** Hospital records (104 months), courts (102), field service (94), government benefits (84) and payroll (81.5).

**What it sinks.** Lock-in 5 sinks government benefits, tax administration, land registry and insurance claims. Lock-in 4 holds back student information systems and courts, and keeps both from passing the search.

**Weakness.**
- **The regulator input is a yes or no that scores 1 or 5.** With only two inputs, it moves lock-in by up to 2 points. The rule is also applied unevenly. Core banking is marked yes because a switch triggers mandatory notice to supervisors. Mainframe is marked no, though its research note says banks and insurers must notify supervisors before such moves. Utility billing is marked no, though its note says Ohio's commission had to grant rule waivers before installation, and that regulated utilities usually disclose the project to their regulator before go-live. A yes would fail utility billing on the search. The approved plan defined this input as "regulator approval required". This report widened it to approval or formal notification and review, which makes these borderline calls harder.
- **Rounding.** 15 of 35 lock-in averages sit at exactly half a point and round up. Mainframe (2.5) is one. Rounded down, it would pass the search.
- **Some results look odd.** Card processing has a median replacement of 16 months but scores 3 because of the regulator answer. Telecom billing scores 2 although Telstra's replacement took 118 months, because its median over 11 cases is 36.
- **The airline ledger may reflect what gets published.** 11 of 12 airline replacements finished on time. As an inference, vendor-announced migrations may be over-represented.
- **Lock-in still does not measure switching rates,** meaning how many buyers actually change system each year.
- **Sensitivity.** Without the regulator input, trade finance rises from 60 to 70.

### 4.5 Crowding

**What it measures.** How many AI-native challengers already attack the category. It counts against the score.

**Worked example: telecom billing.**
- **AI-native with traction.** Three: Totogi, Sierra and Wonderful. 18 of 35 categories have fewer. 18 divided by 35, times 5, is 2.6. Drop the fraction and add 1: score 3.
- **AI-native funding per $1B.** Six rounds in 24 months total about $1,624M. Divided by $18.6B of legacy spend, that is $87.2M per $1B. 21 of 35 categories are lower: score 4.
- **Y Combinator companies.** One since 2024. Only the 6 categories with none are lower: score 1.
- **Average.** (3 + 4 + 1) / 3 = 2.67, which rounds to 3.

**All 35 categories.** Each cell shows the raw value and the 1 to 5 score in bold. The funding cell also shows the number of rounds and their total.

| Category | Crowding (mean) | AI-native with traction | AI-native funding per $1B of legacy spend, 24 months | YC companies, 2024 to 2026 |
|---|---|---|---|---|
| Utility billing | 1 (1.33) | 0: **1** | $30.3M (4 rounds, $76M in all): **2** | 0: **1** |
| Telecom billing | 3 (2.67) | 3: **3** | $87.2M (6 rounds, $1,624M in all): **4** | 1: **1** |
| Airline reservations | 1 (1.33) | 1: **1** | $13.9M (2 rounds, $42M in all): **1** | 2: **2** |
| Construction project accounting | 3 (3.33) | 3: **3** | $44.8M (4 rounds, $54M in all): **3** | 9: **4** |
| Custom COBOL and mainframe | 2 (2.00) | 4: **4** | $1.6M (4 rounds, $23M in all): **1** | 1: **1** |
| Government benefits | 1 (1.33) | 2: **2** | $8.0M (6 rounds, $100M in all): **1** | 1: **1** |
| Manufacturing ERP | 4 (3.67) | 5: **5** | $16.3M (13 rounds, $142M in all): **2** | 17: **4** |
| Student information systems | 1 (1.33) | 0: **1** | $0.5M (2 rounds, $1M in all): **1** | 2: **2** |
| Core banking | 2 (2.00) | 0: **1** | $32.5M (10 rounds, $422M in all): **3** | 3: **2** |
| Payroll and HR | 3 (3.33) | 3: **3** | $16.6M (9 rounds, $157M in all): **2** | 24: **5** |
| Retail point of sale | 3 (2.67) | 3: **3** | $17.4M (8 rounds, $92M in all): **2** | 6: **3** |
| Laboratory information systems | 2 (1.67) | 1: **1** | $14.8M (4 rounds, $20M in all): **1** | 7: **3** |
| Trade finance | 1 (1.33) | 1: **1** | $8.5M (2 rounds, $10M in all): **1** | 3: **2** |
| Licensing and permits | 4 (4.00) | 4: **4** | $118.8M (9 rounds, $134M in all): **4** | 14: **4** |
| Courts and justice case management | 2 (2.00) | 2: **2** | $6.0M (4 rounds, $6M in all): **1** | 6: **3** |
| Agriculture and commodity trading | 2 (1.67) | 1: **1** | $41.4M (3 rounds, $25M in all): **3** | 1: **1** |
| Card issuing and processing | 3 (2.67) | 2: **2** | $35.9M (13 rounds, $437M in all): **3** | 6: **3** |
| Government tax administration | 1 (1.33) | 0: **1** | $25.2M (2 rounds, $179M in all): **2** | 0: **1** |
| Wealth and portfolio accounting | 3 (3.00) | 1: **1** | $166.0M (13 rounds, $509M in all): **5** | 7: **3** |
| Pension and provident fund admin | 2 (1.67) | 2: **2** | $17.9M (5 rounds, $39M in all): **2** | 0: **1** |
| Mortgage servicing | 2 (2.33) | 2: **2** | $108.6M (5 rounds, $224M in all): **4** | 0: **1** |
| Wholesale distribution ERP | 4 (4.33) | 6: **5** | $117.6M (16 rounds, $214M in all): **4** | 15: **4** |
| Port terminal operating systems | 2 (1.67) | 0: **1** | $47.6M (1 round, $21M in all): **3** | 0: **1** |
| Procurement and payables | 4 (3.67) | 3: **3** | $78.1M (12 rounds, $438M in all): **3** | 21: **5** |
| Co-op, rural and microfinance banking | 2 (1.67) | 2: **2** | $21.4M (5 rounds, $120M in all): **2** | 0: **1** |
| Medical billing | 5 (5.00) | 5: **5** | $134.0M (19 rounds, $641M in all): **5** | 31: **5** |
| Capital markets back office | 3 (2.67) | 0: **1** | $43.6M (7 rounds, $118M in all): **3** | 18: **4** |
| Hospital records (EHR) | 5 (4.67) | 5: **5** | $156.1M (17 rounds, $1,983M in all): **5** | 11: **4** |
| Financial close and general ledger | 5 (5.00) | 5: **5** | $126.9M (18 rounds, $736M in all): **5** | 20: **5** |
| Loan origination and servicing | 5 (4.67) | 8: **5** | $105.9M (17 rounds, $550M in all): **4** | 19: **5** |
| Field service and maintenance | 5 (5.00) | 5: **5** | $209.1M (15 rounds, $517M in all): **5** | 34: **5** |
| Warehouse management | 4 (3.67) | 3: **3** | $182.3M (10 rounds, $261M in all): **5** | 8: **3** |
| Land and property registry | 2 (2.33) | 2: **2** | $107.9M (6 rounds, $78M in all): **4** | 1: **1** |
| Insurance policy administration | 4 (4.33) | 4: **4** | $272.4M (12 rounds, $619M in all): **5** | 9: **4** |
| Insurance claims | 4 (4.33) | 4: **4** | $106.3M (15 rounds, $383M in all): **4** | 19: **5** |

**How it varies.** 6 categories score 1, 10 score 2, 7 score 3, 7 score 4 and 5 score 5.

**Crowding that is not "everything is crowded".** Ranking into fifths spreads the scores by design, so the absolute numbers matter too:
- **Six categories have no AI-native challenger with traction:** utility billing, student information systems, core banking, government tax administration, port terminals and capital markets back office.
- **Recent AI-native money is very uneven.** It runs from about $1M in student information systems to $1,983M in hospital records.
- **13 categories have two or fewer Y Combinator companies since 2024,** and six have none.
- **Nine categories score 4 or 5 on every input:** medical billing, hospital records, financial close, loan origination, field service, insurance policy administration, insurance claims, wholesale distribution ERP, and licensing and permits. Three of them (medical billing, financial close and field service) score 5 on all three.

**What it lifts or sinks.** Crowding 1 is what puts utility billing alone at the top and lifts government benefits and student information systems into the top tier. Crowding 5 holds down five of the twelve bottom-tier categories.

**Weakness.**
- **Two of its three inputs count only AI-native companies.** The third counts all recent Y Combinator companies, AI-native or not. Modern challengers that are not AI-native and not from recent Y Combinator batches do not count. In utility billing, Kraken raised a $1B round at an $8.65B valuation in December 2025, and six challengers that are not AI-native have traction, Kraken among them. Utility billing still scores crowding 1.
- **Company-wide raises are counted unevenly.** Sierra's $350M and $950M rounds count fully against telecom billing and make up about 80% of its $1,624M. Cognition's and Anthropic's raises do not count against mainframe.
- **Incumbents' own AI does not count.** AWS gives its mainframe agent away, IBM ships its own code assistant, and Epic ships steps that challengers once sold. In utility billing, Kraken launched autonomous agents built with Sierra in June 2026. None of this shows in crowding.
- **The scores are relative.** Crowding 1 means among the least crowded fifth, not empty.
- **Gaps in the inputs.** 30 of the 298 rounds have no disclosed amount. Five rows are exits or stake purchases, and they count in the round numbers in the table above: one each in utility billing, courts and laboratory information systems, and one each in loan origination and mortgage servicing. The Y Combinator category label passed its audit only after one rewording.
- **The version 2 parse bug no longer affects scores.** The rounds list stores amounts as numbers, so the funding parser that misread telecom billing and laboratory information systems in version 2 is no longer used for scoring. It still affects the funding text in the challenger table.
- **Sensitivity.** Without the Y Combinator input, utility billing falls to 70 and ties with airline reservations and construction accounting.

## 4A. The search: big, painful, AI-fit, low lock-in, low crowding

**In short.** You asked whether anything is sizeable, painful and a good fit for AI, with low lock-in and low crowding. At the category level, one category passes all five tests, narrowly: utility billing. Six more miss by one point. At the workflow level, 17 workflows pass a stricter cut, because the edges of a category escape its core lock-in and most of its crowding. The workflow list is better read as leads to check than as markets, because its size measure counts whole US occupations.

### The tests

A category passes when it meets all five:
- **Size 3 or more**: at least $1B of legacy spend.
- **Pain 3 or more.**
- **AI fit 4 or more.** This uses Jev's score as an absolute bar, which the audit warns against (Section 4.3). On the blind labellers' scale, utility billing's 3.61 would become about 3.12 and score 3, and it would fail. Under a relative test, the top half of the 35 on AI fit, it still passes: it ranks 17th of 35, the last place inside the top half. Telecom billing (20th) would then miss on AI fit as well as crowding.
- **Lock-in 2 or less.**
- **Crowding 2 or less.**

### At the category level

| Category | Total | Size | Pain | AI fit | Lock-in | Crowding | Misses on | Buyable spend, USD B |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| Utility billing | 75 | 3 | 4 | 4 | 2 | 1 | Passes | 2.5 |
| Telecom billing | 70 | 4 | 4 | 4 | 2 | 3 | Crowding by 1 | 18.6 |
| Airline reservations | 70 | 3 | 2 | 4 | 1 | 1 | Pain by 1 | 3.0 |
| Construction project accounting | 70 | 3 | 4 | 4 | 1 | 3 | Crowding by 1 | 1.2 |
| Custom COBOL and mainframe | 65 | 4 | 3 | 4 | 3 | 2 | Lock-in by 1 | 0.6 |
| Agriculture and commodity trading | 60 | 2 | 3 | 4 | 2 | 2 | Size by 1 | 0.05 |
| Laboratory information systems | 60 | 3 | 3 | 3 | 2 | 2 | AI fit by 1 | 1.3 |

Eight more miss by two points. Student information systems, courts and pension administration miss on lock-in (4). Licensing and permits misses on crowding (4). Core banking, trade finance and mortgage servicing miss on pain (2) and lock-in (3). Payroll misses on lock-in (3) and crowding (3).

**How firm is utility billing's pass?** Narrow. Pain is solid, but three other tests sit on an edge, and crowding needs a large caveat.
- It passes in each sensitivity check in Section 4: without the regulator input, without the workaround sign and without the Y Combinator input.
- Its pain rests on all five inputs, each scoring 3 or 4.
- **AI fit is close to the line.** It passes on Jev's score but would fail on the blind labellers' scale (see the tests above).
- **Lock-in sits exactly on 2.00, the edge of the test.** Contracts run a median 48 months and replacements a median 40 months. The non-competitive input is 0 of 12 awards, and all 12 come from the EU tender database. One non-competitive award among them would make that input score 3, lift lock-in to 2.5, round it up to 3 and fail the test. All 50 utility billing awards come from the EU database, and none from the US, where the best first buyer sits. The buyer research also warns of sole-source renewals with the current vendor.
- **The regulator answer is a close call.** It is marked no, and a yes would lift lock-in to 3 and fail the test. The research found that no regulator approves a switch as such. But state commissions review the spending in rate cases (the hearings where a regulator sets the prices a utility may charge and decides which costs it may recover). Ohio's commission had to grant rule waivers before one installation, and regulated utilities usually disclose the project to their regulator before go-live. That is close to the "formally notified and review it" wording that makes core banking a yes.
- **Crowding needs a large caveat.** It scores 1 because no AI-native challenger has traction and the recent AI-native rounds total about $76M. But Kraken raised $1B at an $8.65B valuation in December 2025, and Gentrack, SEW and others have traction. Kraken also launched autonomous agents built with Sierra in June 2026, so the leading modern vendor is shipping its own AI. The opening is for an AI-native entrant against modern and legacy vendors alike, not an empty market.

**What the near misses say.**
- **Telecom billing** is the largest buyable pool on the map at $18.6B. It misses on crowding, and about 80% of its recent AI-native money is Sierra's company-wide raises.
- **Construction accounting** misses on crowding: Adaptive, Field Materials and Pillar have traction, and 9 Y Combinator companies arrived since 2024.
- **Airline reservations** has the lowest penalties on the map but weak pain: 12% of 380 reviews flag backend failures, apps average 4.28 stars, and only 1 of 12 replacements failed.
- **Mainframe** misses because its lock-in average of 2.5 rounds up.
- **Agriculture** is under $1B. **Laboratory information systems** has AI fit 3.

### At the workflow level

The top 15 workflows by opportunity index among those that do not touch the core. Labour value is the pay of all US workers in the workflow's occupations times their time share. AI usage runs from 0 to 1. Category pain is the category's pain score. The rounds column counts rounds mapped to the workflow, and each round is mapped to one workflow only. The published index counts the two exits in the rounds list as rounds. Utility billing's customer-contact round is one of them (POWERCONNECT.AI's majority sale to BHC Global), so it is marked "1 (exit)". Without it, that workflow's index would rise.

| # | Workflow | Category (total) | Index | Labour value, USD B | AI usage | AI-native rounds, 24 months | Category pain |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | Taxpayer contact centre and account inquiries | Government tax administration (55) | 462 | 85.1 | 0.57 | 0 | 3 |
| 2 | Bill disputes, credits and adjustments | Telecom billing (70) | 447 | 25.4 | 0.60 | 0 | 4 |
| 3 | Customer and case inquiry lookups across mainframe screens | Custom COBOL and mainframe (65) | 437 | 55.2 | 0.49 | 0 | 3 |
| 4 | Progress billing, retainage (payment held back until the work is accepted), lien waivers (a contractor's release of its claim on the property once paid) and collections | Construction project accounting (70) | 435 | 20.8 | 0.60 | 0 | 4 |
| 5 | Billing, cash application, credit holds and collections | Wholesale distribution ERP (55) | 435 | 34.9 | 0.35 | 0 | 4 |
| 6 | Customer contact: high-bill inquiries, complaints and account questions | Utility billing (75) | 431 | 66.6 | 0.66 | 1 (exit) | 4 |
| 7 | Performance measurement and client reporting | Wealth and portfolio accounting (55) | 419 | 18.1 | 0.58 | 0 | 4 |
| 8 | Credit and collections: arrears, payment arrangements and disconnection | Utility billing (75) | 397 | 18.7 | 0.41 | 0 | 4 |
| 9 | Call center, case status inquiries and referrals | Government benefits (65) | 393 | 86.8 | 0.36 | 1 | 4 |
| 10 | Order capture, activation, number porting (moving a customer's number between carriers) and order fallout (orders that fail between systems) | Telecom billing (70) | 386 | 63.9 | 0.11 | 0 | 4 |
| 11 | Admissions application and transcript intake | Student information systems (65) | 385 | 23.2 | 0.30 | 0 | 4 |
| 12 | Employer arrears, inspections and recovery | Pension and provident fund admin (55) | 373 | 41.8 | 0.28 | 0 | 3 |
| 13 | Borrower servicing calls and inquiries | Loan origination and servicing (45) | 364 | 72.6 | 0.60 | 1 | 3 |
| 14 | Accounts payable three-way match (checking each invoice against its purchase order and goods receipt) | Wholesale distribution ERP (55) | 362 | 27.8 | 0.17 | 0 | 4 |
| 15 | Reservation-center booking and PNR servicing (the PNR, or passenger name record, is the booking file) | Airline reservations (70) | 353 | 50.1 | 0.44 | 0 | 2 |

**What the list shows.**
- **12 categories appear.** Utility billing, telecom billing and wholesale distribution ERP place two workflows each.
- **13 of the 15 have no AI-native funding round mapped to them in 24 months.** Government benefits' call centre and loan borrower servicing have one each. Utility billing's customer contact shows one, but it is an exit. "No round mapped" is narrower than "no round in the area": telecom billing's five company raises (Sierra and Wonderful) all sit on its customer-care workflow, so its bill disputes show zero.
- **Six of the 15 are contact and inquiry work:** answering customers, looking up accounts and logging the outcome. Billing, collections and disputes account for five more.
- **Six sit in categories with lock-in of 4 or 5,** such as tax administration and government benefits. They do not change the core record, so the index treats them as low lock-in. Three are contact work (taxpayer contact, the benefits call centre and borrower servicing). The other three are employer arrears in pension administration, client reporting in wealth accounting and admissions intake in student information systems.

**A stricter cut.** Keep only workflows that do not touch the core, have no AI-native funding round mapped to them in 24 months (exits left out), sit in a category with pain 3 or more, and show AI usage at or above the median of all 210 (0.18). 55 workflows that do not touch the core have no round mapped, and 17 of them pass. Counting the two exits as rounds would give 53 and 15. The 17 include ten of the top 15 above, plus paper return intake in tax administration, send-out testing and lab billing in laboratory information systems, collections and suspend or restore in telecom billing, overnight batch scheduling and 3270 screen transaction entry in mainframe, master schedule building in student information systems, and judicial research and order drafting in courts. 3270 screens are the green-screen terminals used to work on IBM mainframes. Collections and arrears work recurs: five of the 17. Customer contact appears twice (taxpayer contact and utility customer contact), and billing disputes and inquiry lookups once each. The mainframe screen work is marked as not touching the core. That is a generous research judgment, since entering transactions on those screens writes to the core.

**Caveat on size.** The labour values are not market sizes. Taxpayer contact centre work shows $85.1B because about 1.8M full-time equivalents count toward it. A full-time equivalent is the number of full-time workers that the shares of working time add up to. Nearly all of the 1.8M is 70% of the working time of every US customer service representative, in every industry, not only in tax agencies. Tax examiners add a small share. Summed over 210 workflows, labour value comes to $6.3T, because the same occupations count many times. Use the figure to compare workflows, not to size a business.

### Why the workflow level finds more

1. **It separates the edge from the core.** Category lock-in describes the hardest part of the category: replacing the system of record. 130 of 210 workflows do not touch the core, and 39 of those sit in categories with lock-in 4 or 5.
2. **Crowding is concentrated.** The 21 most crowded workflows, a tenth of the total, hold 40% of the 297 mapped rounds. 96 of 210 workflows have none, or 98 once the two exits are left out. In categories with crowding 3 or more, 18 workflows that do not touch the core have no AI-native round.
3. **The size measure is looser.** The median workflow carries $21.0B of labour value, against a median of $3.0B of legacy spend per category. Almost every workflow looks large, so size rarely rules one out.
4. **AI usage is observed, not rated.** It agrees with category AI fit only loosely (rank correlation 0.46), so it surfaces different work.
5. **The index has no pass mark.** It ranks, so some workflow always comes first. The category tests can fail every category. The workflow index cannot.

Point 1 is mostly a consequence of the design. Lock-in is measured only per category, and the index puts every workflow that touches the core at or below all the rest, so the edges are bound to look more open than the core. Point 2 is the real finding: AI-native money is concentrated on a few workflows, and many edges have none. Points 3 and 5 are reasons to check each lead before acting on it.

## 5. The build-versus-buy lens

**In short.** Your idea was to ask, for each category and buyer size, whether buyers normally buy this software or build it themselves. Building in-house is uncommon. It shows up mostly where the system is critical and the buyer is very large: big banks, big mainframe users and governments. $42.5B (24%) of legacy spend sits with buyers who usually build or own the system. That spend still goes to vendors and integrators, but mostly for platforms and custom builds, not products a startup can sell. The lens matters more in this version, because two of the eight top-tier categories hold little buyable spend: government benefits ($0) and mainframe ($0.6B). The lens also shows that the best first buyer is usually mid-market, while most of the money sits with large enterprises. None of these figures changed since version 2.

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

**In short.** Mainframe now ties for 5th at 65, up from 40. The market did not change. The measures did. Lock-in fell from 5 to 3 and crowding from 5 to 2, and both drops partly reflect what the new measures leave out. It misses the search on lock-in by one point, and that point comes from rounding 2.5 up. Its money is still held by large enterprises that own their code: only $0.6B of $14.5B is buyable.

**The numbers.** The positive factors add 11 points (size 4, pain 3, AI fit 4). The penalties take away 5 (lock-in 3, crowding 2). The net is 6, which scores 65. In version 2 the penalties took away 10.

**Pain: 3.**
- **Keep-alive share:** too few awards (6), left out.
- **Backend-failure share:** no app reviews, left out. Mainframe is a cross-industry category with few customer-facing apps of its own.
- **App rating:** 3 apps average 3.85 stars: score 3.
- **Failed or overrun replacements:** 5 of 9 (56%). 22 of 35 categories are lower: score 4. California's motor vehicles department cancelled its modernisation after 84 months and $134M. Pennsylvania cancelled its unemployment system after 84 months and $153M.
- **Workaround sign:** weak: score 3.
- **Average:** (3 + 4 + 3) / 3 = 3.33, which rounds to 3.

Version 2 gave mainframe pain 3 through Hacker News, where 44 of 68 firsthand-pain comments were about mainframes. Hacker News no longer feeds pain.

**Lock-in: 3.**
- **Contract length and non-competitive share:** too few awards (4 each), left out.
- **Replacement time:** median 69 months over 6 cases. 27 of 35 categories are shorter: score 4.
- **Regulator approval:** no: score 1. The research note says no regulator approves a mainframe replacement as such in this cross-industry category, though banks and insurers must notify supervisors before material IT moves.
- **Average:** (4 + 1) / 2 = 2.5, which rounds up to 3.

Version 2 gave mainframe the only lock-in of 5, from strong slow-replacement and skills signs plus regulation. Version 3 no longer reuses the legacy signs.

**Crowding: 2.**
- **AI-native with traction:** four. Mechanical Orchard, Cognition (Devin), Zengines and Anthropic (Claude Code): score 4.
- **AI-native funding per $1B:** four rounds in 24 months: Zengines ($9M), Kodesage ($2.4M and $6.6M) and Hypercubic ($5.3M). That is $23M, or $1.6M per $1B, the second lowest on the map after student information systems: score 1.
- **Y Combinator companies:** one: score 1.
- **Average:** (4 + 1 + 1) / 3 = 2.

**What the new crowding misses here.** Version 2 counted 12 challenger rows with $5.8B of disclosed funding, mostly Cognition's company-wide raises and Rocket Software's $2.275B purchase of the Micro Focus COBOL business. Version 3 counts neither. It also does not count AWS, which gives its mainframe migration agent away, or IBM, which ships its own code assistant. The day Anthropic published its COBOL post in February 2026, IBM's share price fell 13%. Crowding 2 understates how contested this category is.

**Why buyable spend is small.** Large enterprises wrote their COBOL and still own it. They buy the platform and some outsourcing, then run the migration themselves or through integrators. That puts $13.8B of the $14.5B with buyers who own the system, though most of it is paid to platform vendors. Only the mid-market slice ($0.6B) is Mixed. Small businesses do not run mainframes. The government segment is set to $0, which Section 5 flags as a data gap.

**What the workflows add.** Customer and case inquiry lookups across mainframe screens rank 3rd among workflows that do not touch the core. They carry $55.2B of labour value, AI usage of 0.49 and no AI-native round mapped to them. Overnight batch scheduling and 3270 screen transaction entry also pass the stricter cut in Section 4A, though the second writes to the core.

**What the deep cases add.** Mechanical Orchard has retired applications, not whole mainframes. bloop sold AI conversion of COBOL to Java. It expected bank sales cycles of 18 to 24 months and left the category within about 15 months.

**What would have to be true for mainframe to be the best opening.**
1. **Lock-in drops to 2.** That happens if halves round down, or if faster documented replacements pull the median below the next fifth. Mainframe would then pass all five search tests. As an inference, not a study finding: proof of equivalence, meaning evidence that new code gives exactly the same outputs as the old, is what would make replacements faster.
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
- **Recent money.** Research listed 298 AI-native rounds announced between 1 October 2024 and 2 October 2026. 268 disclose an amount, totalling $11.0B. Hospital records ($1,983M) and telecom billing ($1,624M) drew the most. Each round is mapped to one workflow, and 297 of the 298 map to a listed workflow. Five rows are exits or stake purchases rather than plain funding rounds (Section 2).
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

**Decision guide.** The playbook's guide was written before the current measures, and the playbook itself has not been updated. Lock-in and crowding now run from 1 to 5 by ranking into fifths, so some rows are adjusted to the new scale:
- "Lock-in 2" is shown as "Lock-in 1 or 2", because lock-in 1 now exists.
- "Crowding 5" is shown as "Crowding 4 or 5", and "Crowding 3" as "Crowding 1 or 2", because crowding now leans on AI-native counts and spreads across the scale.
- "Size 2 or 3" is shown as "A small market", "Size 5" is dropped because no category scores it, and "Pain 3" is dropped, as in version 2.
- Three pieces of advice are this report's additions, not the playbook's, and are marked "(report's addition)" in the table: a workflow that does not touch the core, checking the workflow list, and checking modern challengers that are not AI-native.

| If the category shows | Lean toward |
|---|---|
| Lock-in 1 or 2 | Greenfield or overlay |
| Lock-in 3 | Greenfield at a moment when buyers must switch, with hands-on migration (Rillet, GovWell) |
| Lock-in 4 or 5 | Overlay first, migration with proof of equivalence, greenfield for a buyer the incumbent ignores, or a workflow that does not touch the core (report's addition) |
| A small market | One buyer who gets the full return (Traydstream needed one bank; Contour needed four parties) |
| AI fit 4 | An agent or service that owns one judgment step |
| AI fit 3 or less | Workflow software and service first, agents later |
| Crowding 4 or 5 | The step platforms and funded rivals skip; check the workflow list for edges with no AI-native rounds (report's addition) |
| Crowding 1 or 2 | Open ground among AI-native challengers, but check budgets and study coverage, and modern challengers that are not AI-native (report's addition) |

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

**In short.** The version 2 filter is kept with a higher score bar. It keeps categories that score 60 or more, have at least $1B of buyable spend, and have two or fewer AI-native challengers with traction. Seven pass. Utility billing also passes all five search tests. Nine more score 60 or more but fail the filter: six on challengers alone, two on buyable spend alone, and mainframe on both. At the workflow level, the best leads are the edges of the categories that come closest: customer contact and collections in utility billing, disputes and order capture in telecom billing, and progress billing in construction accounting. These are candidates to check, not a ranking.

| Category | Total | Criticality | Buyable spend, USD B | AI-native rows (with traction) | Passes the five search tests? |
|---|---:|---|---:|---:|---|
| Utility billing | 75 | Important | 2.5 | 3 (0) | Yes |
| Airline reservations | 70 | Critical | 3.0 | 1 (1) | No, pain 2 |
| Student information systems | 65 | Important | 2.1 | 4 (0) | No, lock-in 4 |
| Core banking | 60 | Critical | 4.6 | 2 (0) | No, pain 2 and lock-in 3 |
| Courts and justice | 60 | Critical | 1.0 | 5 (2) | No, lock-in 4 |
| Laboratory information systems | 60 | Critical | 1.3 | 4 (1) | No, AI fit 3 |
| Trade finance | 60 | Important | 1.2 | 2 (1) | No, pain 2 and lock-in 3 |

**Near misses.** Six fail on challengers alone. Telecom billing (70, $18.6B buyable), construction accounting (70, $1.2B), payroll (60, $9.5B) and retail point of sale (60, $5.3B) each have 3 AI-native challengers with traction. Licensing and permits (60, $1.1B) has 4, and manufacturing ERP (65, $8.7B) has 5. Two fail on buyable spend alone: government benefits (65, $0) and agriculture (60, $0.05B, 1 challenger with traction). Mainframe (65) fails on both: $0.6B buyable and 4 AI-native challengers with traction. Mortgage servicing, on the version 2 list, now scores 55.

1. **Utility billing.**
   - **Why:** the only category to pass all five search tests, though narrowly (Section 4A). Pain 4, resting on all five inputs, including 6 of 12 documented replacements failed or overrun and 20% of 250 app reviews flagging backend failures. No AI-native challenger has traction.
   - **First buyer:** US municipal and co-op utilities with 10,000 to 100,000 meters, bought mostly through government procurement. Each pays about $60K to $600K a year. The research says to plan for migrations of 6 to 18 months.
   - **Main risk:** modern challengers that are not AI-native. Kraken raised a $1B round at an $8.65B valuation in December 2025, and six challengers that are not AI-native have traction. The buyer profile also warns of sole-source renewals with the current vendor. The award data shows no non-competitive awards in 12, but all 12 come from the EU tender database, and none of the 50 utility billing awards is from the US, where the best first buyer sits. One non-competitive award would fail lock-in. Kraken also launched autonomous agents built with Sierra in June 2026.
2. **Airline reservations.**
   - **Why:** the lowest penalties on the map, lock-in 1 and crowding 1, and $3.0B fully buyable. The only AI-native challenger, Fetcherr, sets fares rather than running reservations.
   - **First buyer:** airlines carrying 0.5M to 10M passengers a year. They sign deals of about 5 years and can switch over in months.
   - **Main risk:** pain is weak. 12% of 380 reviews flag backend failures, apps average 4.28 stars, and 1 of 12 documented replacements failed. Only $0.17B of the buyable spend is mid-market. The rest sits with large carriers whose migrations take years (Southwest used 1,500+ people). Hitit's customer count fell from 73 to 67, and Amadeus is building its own replacement.
3. **Student information systems.**
   - **Why:** pain 4 and crowding 1. Its apps average 2.46 stars over 9 apps, and 6 of 11 documented replacements failed or overran. No AI-native challenger has traction, and its recent AI-native rounds total about $1M.
   - **First buyer:** US community and private colleges with about 2,000 to 15,000 students, and UK further-education colleges, facing a vendor-forced move to cloud software. They spend $150K to $1M a year, and many sit near or below Workday Student's $300K minimum.
   - **Main risk:** lock-in 4. Contracts run a median 60 months over 23 awards, 18% of awards were made without competition, and replacements take a median 60 months.
4. **Core banking.**
   - **Why:** $4.6B buyable among mid-market and small banks. Neither AI-native challenger has traction: Maximum is pre-revenue and Saris AI is early. Of its 10 recent AI-native rounds ($422M), only Maximum's $30M targets the core ledger. The rest fund lending, onboarding and service workflows.
   - **First buyer:** banks and credit unions with $1B to $10B in assets. They spend $0.4M to $4M a year on their core, and about a sixth of their six-year contracts come up for renewal each year.
   - **Main risk:** weak measured pain and few switches. 8% of 150 bank app reviews flag backend failures and apps average 4.29 stars. One consultant estimated in 2015 that about 4% of banks switch per renewal. Modern cores that are not AI-native already win here, and Thought Machine has signed 68 banks.
5. **Courts and justice case management.**
   - **Why:** pain 4 and crowding 2. 13 of 18 public awards keep the old system alive, and California's statewide system was cancelled after 108 months and $407M.
   - **First buyer:** US county and city courts serving 50K to 1M people, in states where each court picks its own system. Contracts run $50K to $850K a year.
   - **Main risk:** lock-in 4. Contracts run a median 72 months and replacements a median 102 months. The $1.04B market sits right on the size line. Two AI-native challengers were bought: Learned Hand (by Clio) and jAI. Learned Hand became the core of Clio's new judiciary business, so the upside is uncertain rather than shown to be limited.
6. **Laboratory information systems.**
   - **Why:** lock-in 2 and crowding 2, with $1.3B buyable. 20% of 100 app reviews flag backend failures. Flabs is the only AI-native challenger with traction.
   - **First buyer:** US mid-market independent and specialty labs that are not tied to an Epic Beaker or Oracle Health bundle. They pay $40K to $300K a year and decide in months.
   - **Main risk:** AI fit 3, with a task average of 2.92. Mid-market holds only $0.07B of the spend, against $0.91B for enterprise. Only 2 of 10 documented replacements failed or overran.
7. **Trade finance.**
   - **Why:** crowding 1 and $1.2B buyable. Cleareye.ai is the only AI-native challenger with traction.
   - **First buyer:** mid-sized trade banks under $25B in assets, paying $150K to $800K a year.
   - **Main risk:** the lowest measured pain on the map (average 1.67, shared with mortgage servicing), with 1 of 7 replacements failed. The obvious first product is taken: Cleareye and Traydstream already check trade documents for J.P. Morgan, Lloyds, Deutsche Bank and Citi, and HSBC built its own checker. The market sits just above the $1B size line.
   - **Disagreement with the playbook:** the playbook drops trade finance, because funded overlays already do its document checking. This report keeps it only because it passes the mechanical filter. Weigh it below the others.

**At the workflow level.** The strongest leads are where the category and workflow views agree:
- **Utility billing:** customer contact on high bills and complaints (6th, AI usage 0.66, one mapped round, which is an exit), and credit and collections (8th, AI usage 0.41, none).
- **Telecom billing:** bill disputes, credits and adjustments (2nd, AI usage 0.60, none), and order capture and number porting (10th, AI usage 0.11, none).
- **Construction accounting:** progress billing, retainage, lien waivers and collections (4th, AI usage 0.60, none).
- **Airline reservations:** reservation-center booking and servicing (15th, AI usage 0.44, none).

## 12. What this study cannot tell you yet

**In short.** This round attacked the weakest parts of version 2: pain, lock-in, crowding and the thin evidence outside the US and EU. Pain and crowding now rest mostly on counts, and lock-in no longer reuses the legacy test. The new measures bring their own limits. Lock-in leans on a yes-or-no regulator input, two of crowding's three inputs count only AI-native companies, and workflow sizes count whole occupations. Size, the regional split, AI fit and the cases did not change.

Each gap below shows what version 2 said, what this round did, and what remains. Version 2's gap list had 12 items. Gaps 2 and 4 come instead from weaknesses named in the body of version 2 (its Sections 4.4 and 4.5), so items 1 to 14 cover the 12 listed gaps plus those two.

1. **Pain was barely measured.** Version 2 scored pain 2 or 3 everywhere, from 68 Hacker News comments and a job-post rule that changed three scores when unweighted.
   - **Done:** pain now averages five inputs built from 2,718 app reviews, 438 apps, 423 public awards labelled maintain, extend or replace, 353 documented replacements and the workaround grade. Scores now run 2 to 4, with 12, 10 and 13 categories at each level.
   - **Remains:** keep-alive reaches its minimum in 13 categories and backend failure in 18. 15 categories rest on three inputs or fewer. App inputs measure end customers. Awards are mostly European. The replacement ledger favours famous projects and lists some projects twice. No source asks buyers directly.
2. **Lock-in reused the legacy signs and did not measure switching.**
   - **Done:** lock-in now uses contract length, non-competitive share, replacement time and regulator approval, none of which comes from the legacy test.
   - **Remains:** 25 of 35 categories rest on two inputs. The regulator input is yes or no and applied unevenly (core banking yes; mainframe and utility billing no). Its definition was widened from the plan's "approval required" to approval or formal notification and review. 15 averages round up from a half. Switching rates are still not measured.
3. **Crowding mixed things.** Version 2 counted challengers that were not AI-native, incumbents' tools and failed or acquired challengers, stopped rising at 9 rows, and included purchase prices.
   - **Done:** crowding now counts AI-native challengers with traction, AI-native rounds in 24 months scaled to market size, and recent Y Combinator companies. It has no cap, and it no longer uses the funding parser.
   - **Remains:** it now ignores modern challengers that are not AI-native, such as Kraken. Company-wide raises count in telecom billing (Sierra) but not in mainframe (Cognition, Anthropic). Incumbents' own AI is not counted. 30 of 298 rounds lack amounts, and five rows are exits or stake purchases. The scores are relative.
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
    - **Remains:** all five factors count equally, and so do the inputs inside each factor. Ranking into fifths and rounding halves up are choices too. Readers can re-weight factors on the site.

New gaps this round:

15. **Workflow labour value counts whole occupations.** It sums to $6.3T over 210 workflows because the same occupations count many times. The top-ranked workflow, taxpayer contact, carries $85.1B, nearly all of it 70% of the working time of every US customer service representative (about 1.8M full-time equivalents). It is not the largest. Several carry more, from order picking ($152.1B) down to government benefits' call centre ($86.8B).
16. **Workflow pain is borrowed from the category, and "touches core" is a research judgment.** Some mainframe screen work is marked as not touching the core.
17. **AI usage is zero for 51 of 210 workflows.** All 51 matched O*NET tasks (2 to 14 each), and the Economic Index records 0 for those tasks. Zero means no Claude usage was recorded for them. The index covers Claude only, not AI use in general, so a zero does not show that no one uses AI for the work.

## 13. Decisions for Hansel about the site

**In short.** The same five choices shape what a reader takes away. The recommendations shift with the new measures. Lead with tiers and show buyable spend. Offer the five-test search as a filter, with its caveats. Show pain with its inputs. Keep Valon for the timeline. Launch after a short fix list.

1. **Which ranking view leads?**
   - (a) The published total, with size based on all legacy spend.
   - (b) A total with size based on buyable spend only. Seven categories move: government benefits 65 to 50, mainframe 65 to 55, core banking 60 to 55, agriculture 60 to 55, port terminals 55 to 50, capital markets 50 to 45 and co-op banking 50 to 45.
   - (c) The published total shown as three tiers, with buyable spend beside each category and sortable.
   - **Recommend (c),** with each factor's inputs and n one click away. Two of the eight top-tier categories hold little buyable spend, so readers need buyable spend in view. A second score would add confusion.
2. **Shortlist or filter?**
   - (a) Name the seven categories from Section 11.
   - (b) A filter that defaults to the five search tests in Section 4A, can switch to the Section 11 rule, and shows each result's main risk.
   - (c) No shortlist.
   - **Recommend (b).** Only utility billing passes the five tests, narrowly, and its low crowding ignores Kraken. Three of the seven in Section 11 sit near the $1B size line. Readers should see the rule and its doubts, not a verdict. Add the workflow list as a second tab, labelled as leads.
3. **How to show pain?**
   - (a) As it is.
   - (b) As it is, with each input, its n, and a flag on the 15 categories that rest on three inputs or fewer.
   - (c) Drop it from the default total. Airline reservations would then lead alone.
   - **Recommend (b).** Pain now has real evidence behind it, and the named failed replacements are the most persuasive content on the site. Version 2 recommended flagging pain as weak. That now holds only for the thinly covered categories.
4. **Which case gets the timeline?**
   - (a) Valon: dated steps from its 2021 Series A to the 2026 Newrez and Carrington deals.
   - (b) Mechanical Orchard: it fits the mainframe chapter.
   - (c) GovWell: from 12 agencies in July 2024 to 200+ in October 2026.
   - **Recommend (a).** It came closest to replacing a core. Its caveats carry the honest lesson: six years, a related-party first buyer, and no MSP shop yet.
5. **When to launch?**
   - (a) Now, as a versioned release.
   - (b) After a short fix list:
     - Decide two crowding rules: whether to count modern challengers that are not AI-native, and one rule for company-wide raises (Sierra in telecom billing against Cognition and Anthropic in mainframe).
     - Decide how to round exact halves in lock-in, which affects 15 categories, and apply the regulator rule the same way in core banking, mainframe and utility billing. Decide whether the rule means approval, as the plan said, or also formal notification and review, as this report used.
     - Label workflow labour value on the page as the pay of whole occupations, not category spend.
     - Fold the 369 new usage records into the regional estimates, and label the regional split as a rough guide.
     - Update the playbook where it still quotes old scores, size unit errors, the Size 5 row and the old shortlist.
     - Update the size description in the rubric and the evidence strings that still describe size as buyers times segment spend.
     - Fill mainframe's government segment or explain its $0. Note on the page that government benefits' $0 buyable still means vendor spend.
     - Fix the funding parser for the challenger table display.
     - Update the repo's README status, which still says no findings yet, and merge the working branch.
   - (c) After a check of 150 human labels and new job data for India and the EU.
   - **Recommend (b).** The two crowding rules and the rounding rule each move top-tier scores, so they belong in the release. Option (c) is blocked by access to sources more than money: all the labelling so far cost $0.67.

## 14. Where the numbers come from

All paths are relative to `/Users/hansel/conductor/repos/legacy-software-atlas`, branch `chore/bootstrap` at commit 6b8495c (not yet merged to `main`). Sums, shares, spreads, correlations, alternative views, the Section 4A search, the Section 11 filter and the version 2 comparison were computed for this report from the files listed. Version 2 totals come from `exports/site/scores.json` at commit 2a1c9c9, with telecom billing and laboratory information systems corrected to 40 and 30 as version 2 reported.

| Section | Files |
|---|---|
| 1. Answer | All files below |
| 2. Method | `research/categories.csv` (legacy test, 46 candidates); `research/market_size.csv` (top-down spend, legacy share); `configs/rubric.toml` (factor rules, input minimums, direct scores); `src/lsa/measures.py` and `src/lsa/measures_raw.py` (fifths rule, input definitions); `src/lsa/scores.py` (averaging, half-up rounding, total); `src/lsa/workflows.py` and `src/lsa/workflows_labour/labour.py` (workflow index, labour value, AI usage); `docs/superpowers/plans/2026-10-05-plan-3-better-measures.md` (measure definitions); `data/derived/awards.parquet` (1,922 awards by source); `data/derived/apps.parquet` (482 listings); `data/derived/items.parquet` (2,718 reviews, 1,939 Y Combinator items); `data/derived/yc.parquet`; `research/apps.csv`; `research/replacement_cases.csv` (353 cases); `research/regulator_approval.csv` (14 yes, 21 no); `research/ai_native_rounds_24m.csv` (298 rounds); `research/challengers.csv`; `research/workflows.csv` and `research/workflow_occupations.csv` (210 workflows, occupations, time shares); `configs/questions.toml` (Jev question wording); `docs/reports/jev-audit.md` (all audits, including plan 3); `data/derived/jev_ledger.jsonl` (sum of `cost_usd` = $0.67 over 5,023 calls; plan 3 passes $0.26 over 1,704 calls and 6,576 items); `configs/budgets.toml` ($8 cap); `README.md` (TypeSafe disclosure, data sources) |
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
