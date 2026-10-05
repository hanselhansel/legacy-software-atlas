# Which legacy software is ready for AI-native replacement

Review report for Hansel. Data as of 5 October 2026.

## 0. How to read this report

Section 1 gives the question and the answer on one page. Section 2 explains how the study was done. Section 3 shows all 35 categories in one table. Section 4 explains what drives the ranking, one factor at a time. Section 5 adds your build-versus-buy lens. Section 6 explains why COBOL and mainframe ranks where it does. Section 7 covers regions. Sections 8 to 10 cover the challengers, the eight deep cases and the playbook. Section 11 names where to look next. Section 12 lists what the study cannot tell you yet. Section 13 sets out five decisions about the site, meaning the public website that will present the atlas from the files in `exports/site/`. Section 14 maps every section to its source files. Sections 1 to 13 each start with a short summary in plain words, then the detail.

## 1. The question and the answer in one page

**In short.** The study asked which kinds of old business software an AI-native company could realistically replace, and where a founder should look first. The map is large, but no category stands out, and five categories share the top score. The biggest pools of legacy spending rank lower. They are hard to leave, crowded with challengers, or held by large buyers who usually build or own their systems. AI-native companies mostly work on top of old systems rather than replace them. The best openings have a real market, buyers who purchase rather than build, and few AI-native challengers so far.

**The question.** Which legacy software categories are ready for an AI-native company to replace, and where should a founder look first?

Terms used throughout:
- **Legacy software**: a system whose core was built before about 2005 and is slow and costly to replace.
- **Category**: one job that software does for a buyer, such as core banking or payroll.
- **AI-native challenger**: a company the study labels as built around AI from the start, selling into a legacy category.
- **Legacy spend**: what buyers worldwide pay each year for systems in a category that are still legacy.
- **Critical and important**: a category is **critical** when two things are both true: the business stops or loses its licence if the system fails, and the system is where the firm competes. It is **important** when only the first is true: the business depends on it but does not compete on it. Payroll is the standard example. 22 categories are critical and 13 are important.

**Headline conclusions**

1. **The map is large but uneven.** 35 of 46 candidate categories passed a strict legacy test. Their legacy spend adds to about $178B a year on midpoints, or $118B to $271B if you add the low and high estimates. Categories range from $0.4B (port terminals) to $18.6B (telecom billing).
2. **The ranking is flat.** Scores run only from 30 to 50 on a 0 to 100 scale, and five categories tie at the top with 50: core banking, manufacturing ERP, trade finance, licensing and permits, and courts.
3. **The famous cores rank lower than their size suggests.** Custom COBOL and mainframe is the second-largest pool at $14.5B a year but scores 40. It is the only category with the maximum lock-in score, and it shares the maximum crowding score with 23 others.
4. **About a quarter of the money sits with buyers who usually build or own the system.** That is $42.5B of the $178B (24%), led by large mainframe users ($13.8B) and government benefits agencies ($12.5B). The money still goes to vendors and integrators: IBM and others for the mainframe platform, and Deloitte, Accenture or FAST for benefits systems. But it mostly pays for platforms and custom builds, which a startup cannot simply sell a product into.
5. **The first buyer is mid-market, but most money is enterprise.** On a broad reading, the best first buyer is a mid-sized firm in 27 of 35 categories, or 24 on a strict reading (Section 5). Yet mid-sized firms hold only $20.6B (12%) of legacy spend, against $100.0B (56%) for large enterprises.
6. **AI-native challengers mostly work on top of the old system, and none has replaced a dominant core.** 119 of 177 AI-native challenger rows are overlays, meaning AI that works on top of the old system and writes its results back into it. 73 of 177 are still early. None of the eight deep cases (the company studies in Section 9) has displaced a market-leading core system.
7. **Five categories are worth a closer look.** Core banking, airline reservations, mortgage servicing, trade finance and courts each pass three tests. They score 45 or more. Buyers purchase at least $1B a year of their systems rather than build them. And they have two or fewer AI-native challengers with traction (named customers or reported revenue). Payroll, procurement and construction accounting each miss by one challenger. The playbook drops trade finance, and Section 11 explains why.

**How much to trust this.** The order is fragile. 18 of 35 categories have a spending range that crosses a size boundary. Pain is barely measured. 126 of 146 regional usage estimates (estimates of how many organisations in a region run the old system) rest on a single kind of source, the weakest grade. Two scores in this report correct the published data file because of a funding parse bug (Section 4.5). Read the ranking as three tiers, not 35 places.

## 2. How we did it, in plain steps

**In short.** We picked candidate categories and kept only those with strong evidence of old systems. We sized each by what buyers spend on those old systems, scored each on five factors, mapped who already attacks it, and studied eight companies in depth. A paid classifier labelled the bulk evidence for $0.40 in total.

**Step 1. Choose categories and apply a strict legacy test.** We started with 46 candidates: 38 seeded and 8 added for Asia Pacific coverage. Each was checked for four signs of legacy, and each sign needed a cited source:
- **Pre-cloud core**: the main systems first shipped before about 2005 as mainframe, midrange or on-premise client-server.
- **Slow to replace**: replacement is a multi-year program, or contracts run 7 years or more.
- **Workarounds**: users report spreadsheets, re-keying or screen-scraping around the system.
- **Shrinking skills**: jobs for the system's skills are hard to fill or skew to older staff.

Each sign was graded strong, weak or not met. A category stayed only if it had at least one strong sign and its strong signs plus half its weak signs reached 2.5. 35 stayed and 11 were dropped: accounting firm practice, anti-money-laundering compliance, civil registration and ID, e-invoicing, freight forwarding and customs, hotel management, law firm practice, pharmacy, real estate property management, regulatory reporting, and transport management. A fact-check opened 256 key citations, and 232 (91%) held.

**Step 2. Size each category by legacy spend.** For each category we took global annual spend on that kind of software, mostly for 2025, from analyst reports and vendor revenue. We multiplied it by the share still on legacy systems, which gives a low and a high figure. The midpoint is the geometric mean of the two: the square root of low times high, which sits closer to the low figure than a plain average does. A second, bottom-up figure (possible buyers times spend per buyer) is used only to split the total by region and by buyer size. It does not set the total.

**Step 3. Score five factors.** Each factor scores 1 to 5:
- **Size**: the legacy spend midpoint, in bins. Under $0.1B scores 1, under $1B scores 2, under $5B scores 3, under $20B scores 4, and $20B or more scores 5.
- **Pain**: evidence that users suffer. It draws on workaround evidence, firsthand complaints on Hacker News, and a weighted share of job posts that show the old system in use.
- **AI fit**: how much of the category's daily work AI could do, scored over 12 tasks per category.
- **Lock-in**: how hard it is to leave. It comes from the slow-to-replace sign (which covers multi-year programs and contracts of 7 years or more), skills scarcity and regulation. It counts against the score.
- **Crowding**: how many challenger rows the study lists, including failed and acquired ones, and how much disclosed funding they have. It counts against the score.

The total is 35 + 5 x (size + pain + AI fit - lock-in - crowding). This puts every possible result on a 0 to 100 scale. All five factors are weighted equally.

**Step 4. Map who already sells replacements.** We listed 436 challenger rows, one per company and category, covering about 417 companies. Each row records a strategy, whether the company is AI-native, and a status:
- **Traction**: named customers or reported revenue.
- **Early**: launched or piloting, too soon to judge.
- **Acquired**: the challenger itself was bought.
- **Stalled**: still operating but losing ground or inactive.
- **Failed**: shut down or left the category.
- **Pending**: the outcome is unresolved. This applies to one row, GROW.

**Step 5. Write deep cases and a playbook.** We wrote eight deep cases, six on companies with real traction and two on failures. From them and the challenger table we drew a playbook of strategies by stage.

**Cost and audit.** The bulk labelling was done by Jev, a non-generative classifier sold by TypeSafe. The study has no affiliation with TypeSafe. Jev labelled job posts, tenders, vendor and integrator stories, Hacker News comments and AI fit. It cost $0.40 in total (3,319 calls over 4,839 items), well inside the $8 cap. Separate Claude agents labelled random samples blind, without seeing Jev's answers. Questions under 80% agreement were reworded once or dropped, and two were dropped. There are two exceptions to disclose:
- `reason_to_stay` scored 79% and was kept, but only as colour. It is never used in a count.
- The Hacker News pain filter keeps comments that Jev rates 0.7 or higher as firsthand pain. That cut was chosen after seeing the audit, where it reached 89% agreement. At 0.5, agreement was 71%. The pain score uses this filter.

Jev rated tasks about half a point more automatable than the blind labels did.

## 3. The whole map

**In short.** All 35 categories score between 30 and 50. Five tie at the top, 21 sit in the middle and 9 at the bottom. Top and bottom differ by 4 points on the unscaled sum (50 against 30), and one step on any factor moves a total by 5. Small changes in evidence can move a category a whole tier.

Ties are listed by legacy spend. Criticality is defined in Section 1. Two rows correct the published file `exports/site/scores.json`, which shows telecom billing at 45 and laboratory information systems at 35. Both errors come from a funding parse bug (Section 4.5).

| # | Category | Legacy spend, USD B: low to high (mid) | Criticality | Total | Size | Pain | AI fit | Lock-in | Crowding |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1= | Core banking | 9.6 to 17.5 (13.0) | Critical | 50 | 4 | 2 | 4 | 3 | 4 |
| 1= | Manufacturing ERP | 6.0 to 12.7 (8.7) | Important | 50 | 4 | 3 | 3 | 2 | 5 |
| 1= | Trade finance | 0.7 to 2.1 (1.2) | Important | 50 | 3 | 2 | 4 | 3 | 3 |
| 1= | Licensing and permits | 0.7 to 1.8 (1.1) | Important | 50 | 3 | 3 | 4 | 3 | 4 |
| 1= | Courts and justice case management | 0.7 to 1.7 (1.0) | Critical | 50 | 3 | 2 | 4 | 3 | 3 |
| 6= | Government benefits | 7.5 to 21.0 (12.5) | Critical | 45 | 4 | 3 | 4 | 4 | 5 |
| 6= | Payroll and HR | 6.0 to 15.0 (9.5) | Important | 45 | 4 | 2 | 4 | 3 | 5 |
| 6= | Financial close and general ledger | 3.0 to 11.2 (5.8) | Important | 45 | 4 | 2 | 4 | 3 | 5 |
| 6= | Procurement and payables | 3.5 to 9.0 (5.6) | Important | 45 | 4 | 2 | 4 | 3 | 5 |
| 6= | Loan origination and servicing | 3.5 to 7.7 (5.2) | Critical | 45 | 4 | 2 | 4 | 3 | 5 |
| 6= | Medical billing | 2.6 to 8.8 (4.8) | Important | 45 | 3 | 3 | 4 | 3 | 5 |
| 6= | Airline reservations | 2.3 to 4.1 (3.0) | Critical | 45 | 3 | 2 | 4 | 3 | 4 |
| 6= | Mortgage servicing | 1.4 to 3.2 (2.1) | Critical | 45 | 3 | 2 | 4 | 3 | 4 |
| 6= | Construction project accounting | 0.8 to 1.8 (1.2) | Important | 45 | 3 | 2 | 4 | 3 | 4 |
| 6= | Agriculture and commodity trading | 0.4 to 1.0 (0.6) | Critical | 45 | 2 | 3 | 4 | 3 | 4 |
| 16= | Telecom billing | 13.2 to 26.3 (18.6) | Critical | 40 | 4 | 2 | 4 | 4 | 5 |
| 16= | Custom COBOL and mainframe | 11.1 to 19.0 (14.5) | Critical | 40 | 4 | 3 | 4 | 5 | 5 |
| 16= | Hospital records (EHR) | 9.4 to 17.3 (12.7) | Critical | 40 | 4 | 3 | 3 | 4 | 5 |
| 16= | Card issuing and processing | 8.4 to 17.6 (12.2) | Critical | 40 | 4 | 2 | 4 | 4 | 5 |
| 16= | Government tax administration | 4.5 to 11.2 (7.1) | Critical | 40 | 4 | 2 | 3 | 3 | 5 |
| 16= | Retail point of sale | 3.2 to 8.8 (5.3) | Critical | 40 | 4 | 2 | 3 | 3 | 5 |
| 16= | Wealth and portfolio accounting | 2.0 to 4.8 (3.1) | Important | 40 | 3 | 2 | 4 | 3 | 5 |
| 16= | Student information systems | 1.3 to 3.6 (2.1) | Important | 40 | 3 | 2 | 4 | 4 | 4 |
| 16= | Wholesale distribution ERP | 0.8 to 4.0 (1.8) | Critical | 40 | 3 | 2 | 3 | 2 | 5 |
| 16= | Land and property registry | 0.5 to 1.2 (0.7) | Critical | 40 | 2 | 2 | 4 | 3 | 4 |
| 16= | Port terminal operating systems | 0.3 to 0.7 (0.4) | Critical | 40 | 2 | 2 | 3 | 3 | 3 |
| 27= | Co-op, rural and microfinance banking | 4.0 to 7.8 (5.6) | Important | 35 | 4 | 2 | 3 | 4 | 5 |
| 27= | Capital markets back office | 1.5 to 4.9 (2.7) | Critical | 35 | 3 | 2 | 4 | 4 | 5 |
| 27= | Utility billing | 1.5 to 4.2 (2.5) | Important | 35 | 3 | 2 | 4 | 4 | 5 |
| 27= | Field service and maintenance | 1.8 to 3.5 (2.5) | Important | 35 | 3 | 2 | 3 | 3 | 5 |
| 27= | Insurance policy administration | 1.4 to 3.8 (2.3) | Critical | 35 | 3 | 2 | 4 | 4 | 5 |
| 27= | Pension and provident fund admin | 1.4 to 3.6 (2.2) | Critical | 35 | 3 | 2 | 4 | 4 | 5 |
| 27= | Warehouse management | 1.0 to 2.1 (1.4) | Critical | 35 | 3 | 2 | 2 | 2 | 5 |
| 34= | Insurance claims | 2.0 to 6.5 (3.6) | Critical | 30 | 3 | 2 | 3 | 4 | 5 |
| 34= | Laboratory information systems | 0.9 to 2.0 (1.3) | Critical | 30 | 3 | 2 | 3 | 4 | 5 |

**Top tier (50, five categories).** Each earns 9 or 10 points from the positive factors (size, pain, AI fit) and loses only 6 or 7 to the penalties (lock-in, crowding). Courts, trade finance and port terminals have the lowest crowding on the map, and port terminals is held down by its small market. Manufacturing ERP has the lowest lock-in and some measured pain. Core banking pairs a large market with moderate penalties. Three of the five are small markets just above the $1B line.

**Middle tier (45 and 40, 21 categories).** These have the same shape with one more penalty point, or a smaller market. This tier holds five of the six pools above $12B: telecom billing, mainframe, hospital records, government benefits and card processing. Each of the five has lock-in of 4 or 5 and crowding of 5, which cancels out most of what its size adds.

**Bottom tier (35 and 30, nine categories).** Every one has crowding 5, plus either lock-in 4 or AI fit of 3 or lower. Insurance and pensions cluster here: policy administration, claims and pension administration. Laboratory information systems joins claims at 30.

**What separates the tiers.** Both sides do, about equally. Points from the positive factors run from 7 to 11, and penalties run from 6 to 10. That is the same 4-point spread. Their standard deviations (how much they vary) are 0.94 and 1.02 points. Their correlations with the total (how closely they move with it, from -1 to 1) are +0.51 and -0.61.

By factor, the spreads are:

| Factor | Standard deviation | Correlation with total |
|---|---:|---:|
| Size | 0.62 | +0.17 |
| Pain | 0.40 | +0.34 |
| AI fit | 0.53 | +0.44 |
| Lock-in | 0.67 | -0.46 |
| Crowding | 0.64 | -0.50 |

Crowding, lock-in and AI fit sort the list about equally. Size sorts it least, because 32 of 35 categories score 3 or 4 on it. The winners pair moderate penalties with strong AI fit. The biggest markets do not win on size alone. These figures include the two corrections in Section 4.5.

## 4. What drives the ranking

**In short.** No single factor decides the order. Crowding, lock-in and AI fit each sort the list about equally. Size sorts it least, because most categories score 3 or 4 on it. Pain is almost flat. Each factor has a weakness worth knowing before you quote a rank.

### 4.1 Size

**What it measures.** Annual legacy spend, scored on the midpoint.

**How it varies.** No category reaches size 5, because telecom billing's $18.6B midpoint sits just under the $20B line. 14 categories score 4, 18 score 3, and 3 score 2 (agriculture, land registry and port terminals).

**What it lifts or sinks.** Size 4 lifts core banking and manufacturing ERP into the top tier. Size 2 holds agriculture and land registry down despite good AI fit.

**Weakness.** The ranges are wide, and 18 of 35 cross a bin line. The fragility runs both ways:
- **Downward.** Courts ($1.04B), permits ($1.13B) and trade finance ($1.17B) sit just above the $1B line. At their low estimates, all three would score size 2 and drop out of the top tier.
- **Upward.** At their high estimates, telecom billing ($26.3B) and government benefits ($21.0B) reach size 5, and medical billing ($8.8B) reaches size 4. Government benefits and medical billing would then score 50. Telecom billing would score 45 with its corrected crowding.

The share still on legacy is a judgment call. It ranges from 15% to 35% in capital markets, and up to 95% in the highest case.

### 4.2 Pain

**What it measures.** Pain starts at 1 and can rise to 5:
- +2 for strong workaround evidence (+1 for weak).
- +1 for at least 5 firsthand-pain comments on Hacker News.
- +1 when at least 30% of the category's labelled job posts show the old system in use. This share is weighted: each post counts in proportion to how many results its search returned, divided by the number of posts sampled from that search.

**How it varies.** 28 categories score 2 and 7 score 3. Three reach 3 through strong workaround evidence (agriculture, permits, medical billing). Two get there through job posts (manufacturing ERP, government benefits) and two through Hacker News (hospital records, mainframe).

**What it lifts.** Pain 3 is what puts manufacturing ERP and permits in the top tier.

**Weakness.** Hacker News held only 68 firsthand-pain comments across all 35 categories, and 44 of them are about mainframes. If pain were held at 2 everywhere, the top tier would shrink to core banking, courts and trade finance.

The job-post weighting also matters. An unweighted share, where every post counts once, gives different results:
- Core banking is 0.27 weighted and 0.42 unweighted. Unweighted, it would get pain 3 and score 55, alone at the top.
- Government benefits is 0.46 weighted and 0.18 unweighted. Unweighted, it would drop to 40.
- Student information systems is 0.38 unweighted. Unweighted, it would rise to 45.

### 4.3 AI fit

**What it measures.** Jev scored 12 core tasks per category for how much of each AI could do. The scores are weighted by how much time each task takes, averaged and rounded.

**How it varies.** 24 categories score 4, 10 score 3, and only warehouse management scores 2. The averages run from 2.50 (warehouse) to 4.13 (construction accounting).

**What it sinks.** The ten categories at 3 lose a point against the rest. They include hospital records, both ERP categories, retail and tax administration. Warehouse management loses two.

**Weakness.** Jev rated tasks about half a point more automatable than blind labellers (3.46 against 2.97). Across 60 sampled tasks, the two agreed on order with a rank correlation of 0.83. A rank correlation measures, from -1 to 1, how closely two lists agree on order, and 1 means the same order. That is a check on tasks. It does not show that the category order holds, so treat AI fit as a rough guide to how categories compare, not as a claim about what AI can do. Rounding also creates cliffs and hides spread. Tax administration averages 3.46 and scores 3, while card processing averages 3.52 and scores 4. Averages of 3.52 and 4.13 both score 4.

### 4.4 Lock-in

**What it measures.** Lock-in starts at 1 and can rise to 5:
- +2 for strong evidence of slow replacement (+1 for weak).
- +1 for strong evidence of shrinking skills.
- +1 when regulation or certification is a reason buyers stay.

**How it varies.** 3 categories score 2 (manufacturing ERP, distribution ERP, warehouse management), 19 score 3, 12 score 4, and only mainframe scores 5.

**What it sinks.** Lock-in 4 sinks insurance, pensions, card processing, telecom billing, hospital records and government benefits.

**Weakness.** Lock-in reuses two of the four legacy signs. The more strongly a category proves it is legacy, the more lock-in penalises it. Contract length enters only through the slow-to-replace sign (contracts of 7 years or more). Lock-in does not measure switching rates.

### 4.5 Crowding

**What it measures.** Crowding counts challenger rows:
- Under 2 scores 1, under 5 scores 2, under 9 scores 3, and 9 or more scores 4.
- +1 when disclosed challenger funding exceeds $500M.

**How it varies.** Every category has at least 7 challenger rows, so none scores below 3. 3 categories score 3 (courts, trade finance, port terminals), 8 score 4 and 24 score 5. These counts include the two corrections below.

**What it lifts or sinks.** Low crowding is the main reason courts and trade finance reach the top. Crowding 5 holds down most of the middle and bottom tiers.

**Weakness.** Crowding counts every row, AI-native or not. That includes incumbents' own products, such as AWS's and IBM's mainframe tools. It also includes challengers that failed (bloop, Contour) or were bought (Learned Hand, jAI), so it overstates how many challengers still sell there. The count stops rising at 9, so 9 and 21 rows score the same. Funding totals mix venture rounds with purchase prices and company-wide raises. Low crowding can also mean the study found fewer companies there.

The funding figures also contain a parse bug. `src/lsa/scores.py` passes each `funding_usd` cell through `parse_counts.parse_usd`. That function takes only the first figure written with "$" and skips numbers written without it. Two scores change as a result, and one figure is wrong without changing its score:
- **Telecom billing.** The parser counted $121.2M: the first "$" round of gaiia ($13.2M), Wonderful ($34M), Gigs ($20M), MATRIXX ($50M) and LotusFlare ($4M). It missed Totogi's "100,000,000" entirely. The rows' own totals are Totogi $100M, gaiia $66M, Wonderful $280M, Gigs $93M, MATRIXX $150M and LotusFlare $10M. That is about $699M even before Sierra's reported $1B+ of cash, which is over the $500M line. Crowding is 5, not 4, and the total is 40, not 45.
- **Laboratory information systems.** The parser counted $1.8M. It skipped amounts written without "$", such as PathAI "~255M", Paige "220M+" and Proscia "130M". With the rest, they come to about $638M. Crowding is 5, not 4, and the total is 30, not 35.
- **Agriculture.** The funding figure is inflated by currency errors. Grao Direto's R$145.3M (Brazilian reais) and AgriDigital's A$25M (Australian dollars) are read as US dollars. The total stays under $500M either way, so the score does not change.

## 5. The build-versus-buy lens

**In short.** Your idea was to ask, for each category and buyer size, whether buyers normally buy this software or build it themselves. Building in-house is uncommon. It shows up mostly where the system is critical and the buyer is very large: big banks, big mainframe users and governments. $42.5B (24%) of legacy spend sits with buyers who usually build or own the system. That spend still goes to vendors and integrators, but mostly for platforms and custom builds, not products a startup can sell. The lens also shows that the best first buyer is usually mid-market, while most of the money sits with large enterprises.

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
- **Some middle-tier categories are mostly buyable at scale.** Telecom billing ($18.6B), hospital records ($12.7B), card processing ($12.2B) and payroll ($9.5B) all count as fully buyable. In hospital records, every commercial segment buys. In the other three, enterprise is Mixed (some large buyers build), and it holds 83% of telecom spend, 85% of card spend and 58% of payroll spend. Part of that money may not be open to a vendor.
- **The first buyer and the money live in different places.** On a broad reading, mid-market is the best first buyer in 27 of 35 categories, and local or state government in 6 more. That reading puts three borderline profiles in mid-market: mainframe ("lower end of enterprise and upper end of mid-market"), hospital records (rural hospitals under 100 beds, closer to small business) and co-op banking (rural banks). It also counts utility billing (city and co-op utilities) as government. Read strictly, mid-market leads in 24. Across all 35 categories, mid-market holds $20.6B of legacy spend. Enterprise holds $100.0B, government $42.1B and small businesses $15.3B. A founder enters at mid-market and has to move up to large buyers to reach most of the money.

## 6. Why COBOL and mainframe ranks where it does

**In short.** Mainframe is the archetype of legacy and the second-largest pool, but it ties for 16th. It does well on size, pain and AI fit, then loses more than it gains. It is the hardest category to leave, and it ties for the most crowded. The large enterprises that hold the spend own their application code and run their own migrations.

**The numbers.** The positive factors add 11 points (size 4, pain 3, AI fit 4), the joint highest on the map with government benefits. The penalties take away 10 points (lock-in 5, crowding 5), the highest on the map. The net is 1, which scores 40.

**Why lock-in is at the maximum.** It is the only category with strong evidence of slow replacement, strong evidence of shrinking skills, and regulation as a reason to stay.

**Why crowding is at the maximum.** It has 12 challenger rows with $5.8B of disclosed funding. Most of that funding is Cognition's company-wide raises and Rocket Software's $2.275B purchase of the Micro Focus COBOL business. Seven of the 12 are AI-native: Mechanical Orchard, Hypercubic, Cognition (Devin), Zengines, Kodesage, Anthropic (Claude Code) and bloop, which failed. AWS gives its mainframe migration agent away. IBM ships its own code assistant. Rocket modernises the COBOL estate it bought. The day Anthropic published its COBOL post in February 2026, IBM's share price fell 13%.

**Why buyable spend is small.** Large enterprises wrote their COBOL and still own it. They buy the platform and some outsourcing, then run the migration themselves or through integrators. That puts $13.8B of the $14.5B with buyers who own the system, though most of it is paid to platform vendors. Only the mid-market slice ($0.6B) is Mixed. Small businesses do not run mainframes. The government segment is set to $0, which Section 5 flags as a data gap.

**What the deep cases add.** Mechanical Orchard has retired applications, not whole mainframes. bloop sold AI conversion of COBOL to Java. It expected bank sales cycles of 18 to 24 months and left the category within about 15 months.

**What would have to be true for mainframe to be the best opening.**
1. **Leaving gets faster.** Proof of equivalence means evidence that the new code gives exactly the same outputs as the old code. If it cut migrations to a matter of quarters, the slow-replacement grade would weaken and lock-in would drop to 4. That alone lifts the total to 45.
2. **Crowding falls to 4.** Crowding is a count plus a funding test, so it falls only if disclosed funding drops under $500M or the count falls below 9 rows. Funding would drop under $500M if, for example, Cognition's company-wide raises and the Rocket purchase were not counted. With lock-in 4 and crowding 4, the total would be 50, level with the top tier. As an inference, not a study finding: the step most likely to stay open to a newcomer is verification, which means producing proof of equivalence.
3. **Enterprises start buying the outcome.** Large owners might hand migration to vendors on fixed-price or outcome terms. Much of the $13.8B would then become buyable, and mainframe would be one of the largest buyable pools on the map. Buyable spend is not part of the score, so this changes the build-versus-buy view, not the rank.

Until then, the realistic entry is the one the research names. That means smaller enterprises and upper mid-market firms running 400 to 2,000 MIPS (a measure of mainframe capacity) and spending $1M to $5M a year with mainframe vendors.

## 7. Regions

**In short.** The study split each category's spend across 11 regions. Treat the split as a rough guide only. It follows counts of possible buyers, not observed spending, and some of its results cannot be right. Usage evidence is broad in the US, the EU, Australia and Singapore, and thin everywhere else.

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

## 8. Who is attacking and how

**In short.** Most AI-native challengers work on top of the old system. They automate steps and write the results back into the incumbent's system rather than replace it. Many are too early to have succeeded or failed, so the table cannot yet say which strategy works best.

**Strategies.**
- **Overlay**: AI works on top of the system of record and writes back to it. The system of record is the system that holds the official data, such as the ledger or the policy file.
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

**The overlay finding.** 119 of 177 AI-native rows (67%) are overlays. Only 3 lead with migration and 1 with acquisition. Most attempts to replace a core come from companies that are not AI-native. Examples are modern banking cores such as Thought Machine, Mambu and 10x, and Kraken in utility billing.

**Outcomes are too young to judge.** 73 of 177 AI-native rows are early, against 23 of 259 other rows. Three strategies have 20 or more AI-native rows: overlay, greenfield and AI-run service. Their AI-native traction rates are close, at 51% to 60%. The other two have too few rows to compare: migration is 2 of 3 and acquire is 0 of 1. The gap with other rows may be mostly age. That is an inference taken from the playbook. The study records status, not company age. Only 19 of 436 rows are stalled or failed, and known failures such as Olive AI, we.trade and Marco Polo are missing. The table under-counts failure.

## 9. What the deep cases teach

**In short.** The eight cases are grouped here by strategy. The overlays grew by owning one step whose value a buyer can check in dollars. The greenfield companies won at a moment when buyers had to switch, and they did a lot of hands-on service. One AI-run service became the closest thing to a core replacement. The migration cases show that proof of equivalence is the product. None has displaced a dominant core.

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
- **bloop (mainframe, cautionary).** bloop sold AI conversion of COBOL to Java on $7.43M raised. Its founder Louis expected bank sales cycles of 18 to 24 months, longer than its cash would last. That was his expected cycle, not deals that closed (`cases/bloop.md` fact-check). It pivoted in June 2025, and the successor company shut in April 2026. AWS later priced its own mainframe agent at zero. **Lesson:** make sure your cash lasts as long as the buyer's sales cycle, and do not build your advantage on a weakness of today's AI models.

## 10. The playbook in brief

**In short.** The playbook crosses the five strategies with four stages of growth. It shows what worked at each stage and where it broke. A guide then matches a category's scores and buyer to a strategy. The main message: start with one step a buyer can check, sold to one buyer. Treat replacing the core as a later, separate bet.

**Stages.** First wedge (the first product a buyer pays for), first 10 customers, expand, replace the core.

| Strategy | First wedge | First 10 customers | Expand | Replace the core |
|---|---|---|---|---|
| Overlay | One step a buyer can audit, with no new screens (AKASA's pre-bill review, Adaptive's payables) | Founder-sold, priced on gains or below the cost of a hire | More steps and channels, such as 40+ accounting firms at Adaptive | Declined so far |
| Greenfield | A moment when the buyer must switch: outgrowing QuickBooks, small-town permits | Founder sales plus heavy service | Modules, departments, audit-firm partners | Partial: about 180 NetSuite or Intacct switches (QuickBooks moves excluded), one town taken from Accela |
| AI-run service | A licensed slice of one buyer's volume (Valon's subservicing, meaning servicing loans for their owner for a fee) | Investors who own volume | Volume and unit-cost proof: 593,000 loans and $86M revenue in 2025 | Sell the software; first sale to a related party, no MSP shop (servicer running MSP) yet |
| Migration-led | The job that sank the last project | Early customers, with about ten organisations described publicly at Mechanical Orchard | Groups of jobs, then whole applications, sold through integrators | Applications retired, no whole mainframe |
| Acquire | Buy a book of customers | Inherited with the book | Move the base to a new core | No case evidence yet |

**Decision guide.** The playbook's guide was written before the current size method. Its lock-in, AI fit and crowding rows are kept as written. Three rows were changed:
- "Size 2 or 3" is shown as "A small market", because the size bins now cover different dollar amounts.
- "Size 5" is dropped. No category now scores size 5, and the playbook itself says several of its size-5 examples were unit errors.
- "Pain 3" is dropped, because pain is too weak a signal (Section 4.2) to steer a choice of strategy.

| If the category shows | Lean toward |
|---|---|
| Lock-in 2 | Greenfield or overlay |
| Lock-in 3 | Greenfield at a moment when buyers must switch, with hands-on migration (Rillet, GovWell) |
| Lock-in 4 or 5 | Overlay first, migration with proof of equivalence, or greenfield for a buyer the incumbent ignores |
| A small market | One buyer who gets the full return (Traydstream needed one bank; Contour needed four parties) |
| AI fit 4 | An agent or service that owns one judgment step |
| AI fit 3 or less | Workflow software and service first, agents later |
| Crowding 5 | The step platforms and funded rivals skip |
| Crowding 3 | Open ground, but check budgets and study coverage |

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

**In short.** A simple filter keeps categories that pass three tests. They score 45 or more. Buyers purchase at least $1B a year of their systems rather than build them. And they have two or fewer AI-native challengers with traction. Five pass. Three more (payroll, procurement and construction accounting) miss by one challenger each. Each pick has a named first buyer and one main risk. These are candidates to check, not a ranking.

| Category | Total | Criticality | Buyable spend, USD B | AI-native rows (with traction) |
|---|---:|---|---:|---:|
| Core banking | 50 | Critical | 4.6 | 2 (0) |
| Trade finance | 50 | Important | 1.2 | 2 (1) |
| Courts and justice | 50 | Critical | 1.0 | 5 (2) |
| Airline reservations | 45 | Critical | 3.0 | 1 (1) |
| Mortgage servicing | 45 | Critical | 2.1 | 3 (2) |

**Near misses.** Payroll ($9.5B buyable), procurement ($5.6B) and construction accounting ($1.2B) also score 45 and clear $1B buyable. Each has exactly 3 AI-native challengers with traction. Telecom billing, the largest buyable pool on the map ($18.6B), no longer qualifies. Its score is 40 once its challengers' funding is counted correctly (Section 4.5).

1. **Core banking.**
   - **Why:** top tier, critical, and $4.6B buyable among mid-market and small banks. Neither AI-native challenger has traction: Maximum is pre-revenue and Saris AI is early.
   - **First buyer:** banks and credit unions with $1B to $10B in assets. They spend $0.4M to $4M a year on their core, and about a sixth of their six-year contracts come up for renewal each year.
   - **Main risk:** few banks switch. One consultant estimated about 4% per renewal in 2015. Modern cores that are not AI-native already win here, and Thought Machine has signed 68 banks.
2. **Trade finance.**
   - **Why:** top tier, the lowest crowding on the map (shared with courts and port terminals), and $1.2B buyable.
   - **First buyer:** mid-sized trade banks under $25B in assets, paying $150K to $800K a year.
   - **Main risk:** the obvious first product is taken. Cleareye and Traydstream already check trade documents for J.P. Morgan, Lloyds, Deutsche Bank and Citi, and HSBC built its own checker. The market sits just above the $1B size line.
   - **Disagreement with the playbook:** `playbook/playbook.md` drops trade finance, because funded overlays already do its document checking. This report keeps it only because it passes the mechanical filter. Treat the playbook's reason as the main risk above, and weigh trade finance below the other four.
3. **Courts and justice case management.**
   - **Why:** top tier, critical, and the lowest crowding on the map (shared with trade finance and port terminals).
   - **First buyer:** US county and city courts serving 50K to 1M people, in states where each court picks its own system. Contracts run $50K to $850K a year.
   - **Main risk:** budgets are small, and the $1.04B market sits right on the size line. Two AI-native challengers were bought: Learned Hand (by Clio) and jAI. Neither deal disclosed its terms. Both had raised little (about $5M, and nothing disclosed for jAI), which hints at modest exits. But Learned Hand became the core of Clio's new judiciary business, so the upside is uncertain rather than shown to be limited. Low crowding may only reflect the study's coverage.
4. **Airline reservations.**
   - **Why:** critical and $3.0B fully buyable. The only AI-native challenger, Fetcherr, sets fares rather than running reservations.
   - **First buyer:** airlines carrying 0.5M to 10M passengers a year. They sign deals of about 5 years and can switch over in months.
   - **Main risk:** only $0.17B of the buyable spend is mid-market. The rest sits with large carriers whose migrations take years (Southwest used 1,500+ people). Hitit's customer count fell from 73 to 67, and Amadeus is building its own replacement.
5. **Mortgage servicing.**
   - **Why:** critical and $2.1B fully buyable. Valon has moved two servicing books onto a new core. Neither came off MSP (the market-leading servicing system, sold by ICE). Newrez is a related party leaving an in-house system. Carrington bought Valon's own servicer.
   - **First buyer:** US servicers with 25K to 500K loans that are about to choose a platform anyway, spending $0.5M to $10M a year.
   - **Main risk:** no MSP shop (a servicer running MSP) has confirmed a move. ICE is adding AI to MSP, and Wells Fargo renewed it. Valon and Kastle are already in the market.

## 12. What this study cannot tell you yet

**In short.** The study ranks categories against each other on public evidence. It cannot yet say how many firms use each system, how much they suffer, or which strategy wins. Several numbers rest on one source or on a model's judgment.

- **Size is an estimate with wide bounds.** 18 of 35 spending ranges cross a size line. The legacy share is a judgment call. The $178B total is the sum of the midpoints. Adding the low estimates gives $118B, and adding the highs gives $271B. Categories can also overlap, which may double count: custom mainframe code runs inside banks, insurers and agencies.
- **The region and buyer-size splits follow buyer counts, not spending.** That produces results such as 91% of medical billing spend landing with government, $11.9B of hospital records spend landing in India, and $0 for mainframe's government segment.
- **Usage counts are rough.** Of 146 regional usage estimates, 126 are grade C, 20 are grade B and none is grade A.
- **Pain is barely measured.** It is 2 or 3 everywhere. Hacker News gave 68 firsthand-pain comments, 44 of them about mainframes. The job-post rule changes three scores if the share is unweighted.
- **AI fit is a model's view.** It runs about half a point high against blind labels. The audit checked task order, not category order, so use it as a rough comparison, not an absolute measure.
- **Crowding mixes things.** It counts challengers that are not AI-native, incumbents' own tools, and failed or acquired challengers. It stops rising at 9 challengers. Some funding totals include purchase prices. A parse bug misread funding in telecom billing, laboratory information systems and agriculture (Section 4.5).
- **Demand from public tenders is unproven.** Blind labellers put about 80% of tenders found by keyword search in no legacy category.
- **Coverage gaps.** India and EU job data are thin, and Naukri, Glints and Reddit were not reachable. A gap in the study is not necessarily a gap in the market.
- **Failures are under-counted.** Only 19 of 436 challenger rows are stalled or failed, and known failures are missing.
- **Eight cases.** Company figures are unaudited unless stated. Some steps are inferred and labelled as inferred.
- **The audit used model labels.** The blind check used Claude agents, not people. One pain cut was chosen after seeing the audit.
- **Weights are a choice.** All five factors count equally. Readers can re-weight on the site.

## 13. Decisions for Hansel about the site

**In short.** Five choices shape what a reader takes away. Each comes with options and a recommendation.

1. **Which ranking view leads?**
   - (a) The published total, with size based on all legacy spend.
   - (b) A total with size based on buyable spend only. Seven categories move: government benefits 45 to 30, mainframe 40 to 30, core banking 50 to 45, agriculture 45 to 40, and port terminals, capital markets and co-op banking down 5 each.
   - (c) The published total shown as three tiers, with buyable spend beside each category and sortable.
   - **Recommend (c).** It keeps the method stable and shows your lens without adding a second score.
2. **Shortlist or filter?**
   - (a) Name the five categories from Section 11.
   - (b) A filter on score, buyable spend and AI-native challengers with traction. It would default to the Section 11 rule and show each result's main risk.
   - (c) No shortlist.
   - **Recommend (b).** The rule is mechanical, and two of its picks sit on the $1B size line: trade finance ($1.17B) and courts ($1.04B). The playbook also drops trade finance. Readers should see the rule and its doubts, not a verdict.
3. **How to show pain?**
   - (a) As it is.
   - (b) As it is, flagged as a weak signal.
   - (c) Drop it from the default total. The top tier would shrink to core banking, courts and trade finance.
   - **Recommend (b),** with a note showing what (c) would do. Pain alone puts manufacturing ERP and permits in the top tier.
4. **Which case gets the timeline?**
   - (a) Valon: dated steps from its 2021 Series A to the 2026 Newrez and Carrington deals.
   - (b) Mechanical Orchard: it fits the mainframe chapter.
   - (c) GovWell: from 12 agencies in July 2024 to 200+ in October 2026.
   - **Recommend (a).** It came closest to replacing a core. Its caveats carry the honest lesson: six years, a related-party first buyer, and no MSP shop yet.
5. **When to launch?**
   - (a) Now, as a versioned release.
   - (b) After a short fix list:
     - Fix the funding parser (`parse_counts.parse_usd`, called from `src/lsa/scores.py`) so it reads amounts written without "$" and converts other currencies. Then re-export. Telecom billing moves to 40 and laboratory information systems to 30.
     - Update the playbook where it still quotes scores or size errors from before the current size method:
       - "The short version": the "ranking needs a re-grade" bullet.
       - "Data limits": the size unit errors.
       - "Choosing a strategy": "size has unit errors" and the Size 5 row.
       - "Where to look next" and "Limits".
     - Update the source files that still describe the old size method (size as buyers times segment spend): `configs/rubric.toml` `[size]`, the `src/lsa/scores.py` docstring, and the `scores.json` evidence strings that read "(12758 buyers x segment spend)".
     - Fill mainframe's government segment or explain its $0. Note on the page that government benefits' $0 buyable still means vendor spend.
     - Label the regional split as a rough guide on the page.
     - Decide whether crowding should count purchase prices, and failed or acquired challengers.
     - Update the repo's README status and merge the working branch.
   - (c) After adding India and EU job data.
   - **Recommend (b).** The fixes are small, and the parse bug and the old playbook scores contradict the map. Option (c) is blocked by access to sources, not money: all the labelling so far cost $0.40.

## 14. Where the numbers come from

All paths are relative to `/Users/hansel/conductor/repos/legacy-software-atlas`, branch `chore/bootstrap` at commit 2a1c9c9 (not yet merged to `main`). Sums, shares, spreads, correlations, alternative views and the Section 11 filter were computed for this report from the files listed. The telecom billing and laboratory information systems scores were recomputed from the row totals in `research/challengers.csv`. `exports/site/scores.json` still shows 45 and 35.

| Section | Files |
|---|---|
| 1. Answer | All files below |
| 2. Method | `research/categories.csv` (legacy test, 46 candidates, kept and dropped); `research/market_size.csv` (top-down spend and legacy share); `configs/rubric.toml` (factor rules, size bins); `research/challengers.csv` (rows, statuses); `docs/reports/2026-10-05-pre-jev.md` (candidate origin, fact-check, item counts); `docs/reports/jev-audit.md` (blind audit, `reason_to_stay` at 79%, the 0.7 pain cut); `data/derived/jev_ledger.jsonl` (sum of `cost_usd` = $0.40 over 3,319 calls and 4,839 items); `configs/budgets.toml` ($8 cap); `docs/superpowers/specs/2026-10-05-legacy-software-atlas-design.md` (sign definitions, Jev description); `README.md` (TypeSafe disclosure) |
| 3. Map | `exports/site/scores.json` (totals, parts); `exports/site/categories.json` (`market` low, mid, high; `build_vs_buy.criticality`); `research/challengers.csv` (corrected funding for two categories) |
| 4. Factors | `exports/site/scores.json` (part details: spend ranges, pain components, weighted and unweighted job-post shares, AI fit means, lock-in grades, challenger counts and funding); `configs/rubric.toml`; `src/lsa/scores.py` and `src/lsa/parse_counts.py` (funding parse); `src/lsa/score_inputs.py` and `src/lsa/labels.py` (job-post weighting); `research/challengers.csv` (funding cells); `docs/reports/jev-audit.md` |
| 5. Build vs buy | `exports/site/categories.json` (`build_vs_buy`: criticality, segments, segment evidence, buyable value, best first buyer); `research/criticality.csv` (criticality tests, segment evidence) |
| 6. Mainframe | `exports/site/scores.json` and `exports/site/categories.json` (mainframe entry); `research/challengers.csv` (12 mainframe rows); `cases/mechanical-orchard.md`; `cases/bloop.md` |
| 7. Regions | `exports/site/regions.json` (usage, grades, buyers, value per region); `docs/reports/2026-10-05-pre-jev.md` (unreachable sources) |
| 8. Challengers | `research/challengers.csv` (436 rows); `playbook/playbook.md` (strategy table, recoding, company count, age inference) |
| 9. Cases | `cases/adaptive.md`, `cases/akasa.md`, `cases/govwell.md`, `cases/rillet.md`, `cases/trade-finance-networks.md`, `cases/valon.md`, `cases/mechanical-orchard.md`, `cases/bloop.md` |
| 10. Playbook | `playbook/playbook.md` (stages table, choosing a strategy, failure patterns) |
| 11. Openings | `exports/site/categories.json` (scores, buyable value, best first buyer); `research/challengers.csv` (AI-native counts and status); `cases/valon.md`; `cases/trade-finance-networks.md`; `playbook/playbook.md` (where to look next, trade finance dropped) |
| 12. Limits | `docs/reports/jev-audit.md`; `exports/site/regions.json`; `exports/site/categories.json`; `exports/site/scores.json`; `src/lsa/parse_counts.py`; `playbook/playbook.md` (data limits, under-counted failures) |
| 13. Decisions | Computed from `exports/site/categories.json`; `playbook/playbook.md`; `configs/rubric.toml`; `src/lsa/scores.py`; `README.md` |