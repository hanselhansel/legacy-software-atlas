# How AI-native companies take on legacy software

Most AI-native challengers work around legacy cores rather than replace them.

This playbook draws on eight case studies, 436 challenger rows and 35 scored categories. Rows are company-category pairs. About 19 rows repeat a company, so the 436 rows cover roughly 417 companies. Eight rows use other strategies and sit outside the five below. Much of the evidence for migration, acquire and greenfield comes from rows that are not AI-native (259 of 436).

Labels were recoded for this version so that each company carries one label, and so that "acquire" means the challenger did the buying:
- Pismo, Finxact, Plex, Fiix and Clearwater move from acquire to greenfield. They were bought. They did not buy a legacy book.
- Thought Machine and Zeta are greenfield in every row.
- Sagent is acquire in every row.
- Valon is AI-native in every row.
- GROW moves from acquired to pending.

Every count below uses the recoded set.

## Data limits

- **Pain is barely measured.** Pain scores come from HN comments and from the share of job posts that name the legacy system. In 30 of 35 categories the pain signal is "weak" and the job-post share is under the 0.3 threshold.
- **India and EU job data are thin.** Any claim about those markets rests on few data points.
- **EU size entries are tiny and grade C.** Examples: courts EU 16-48, benefits EU 2-6.
- **Procurement activity is not measured.** Keyword searches for tenders mostly returned off-topic results.
- **Some size scores count the wrong unit.** In at least nine categories, one grade-C size row counts something other than buying organisations:
  - courts (AU 300,000)
  - land registry (AU 2,600,000)
  - mortgage servicing (US 36,000,040, which is MSP's loan count, not a count of servicers)
  - gov benefits (global 6,600,152)
  - telecom-bss (US 90.4M)
  - ehr-hospital (global 650M)
  - pension (IN 340M)
  - utility-billing (VN 27M)
  - loan-origination (US 48.8M)

  The total score is 35 + 5 × raw, so one bad row can add 10 to 15 points.
- **Survivorship.** Only 19 of 436 rows (4.4%) are stalled or failed, so the table under-samples dead companies. Known failures named in the cases are missing from it.¹
- **Exit quality is not coded.** "Acquired" mixes strategic exits, distressed sales and acqui-hires (see Failure patterns).

¹ Olive AI was an overlay. It raised over $900M and shut down in October 2023 (see AKASA). we.trade went into liquidation in June 2022 and Marco Polo in February 2023 (see Trade-finance networks). Adding all three would raise stalled or failed to 22 of 439 rows. Overlay would go to 7 of 215 (3.3%), and greenfield networks to 10 of 146 (6.8%).

## The short version

- **Overlay is the most common AI-native strategy.** 119 of 177 AI-native rows sit on top of the old system. Only 3 lead with migration, and 1 with acquisition. Being common does not mean it works better. AI-native traction is about the same across strategies: 51% for overlay, 52% for greenfield, 60% for AI-run service.
- **AI-native rows are young.** 73 of 177 AI-native rows are early, against 23 of 259 other rows. Many are too young to have failed or been bought, so outcome comparisons are weak.
- **In the eight cases, replacing a dominant core is slow.**
  - Valon took about six years to sell its first whole-shop core. The buyer was Newrez, part of Rithm, which is Valon's anchor investor and a customer. Newrez was leaving an in-house core, not MSP (see Valon).
  - Rillet's roughly 180 NetSuite or Intacct switches equal about 0.4% of NetSuite's base. That figure is inferred, and it overstates share because it divides switches from both ledgers by NetSuite's base alone (see Rillet).
  - Table rows outside the cases did replace cores: Kraken, Thought Machine and Candid Health (see Replace the core).
- **Proof came from running the work, and it cost people.**
  - Valon ran about 810,000 loans on its own core before selling its servicer (see Valon).
  - GovWell bought speed with staff. 21 of its 71 staff work in deployment and support and are filed under service cost. 35 of 71 work in sales and marketing. It reports no gross margin (see GovWell).
- **The category ranking needs a re-grade.** The four public-sector picks scored high on size rows in the wrong units. Corrected, courts scores 55 (or 50), land registry 45, mortgage servicing 40 and government benefits 35. Courts shows low disclosed funding and small budgets, not a proven opening.

## Five strategies

AI-native rows skew early. Of 177, 92 have traction, 73 are early, 10 were acquired and 2 failed. Only 23 of 259 other rows are early, so compare traction with care. In the table, acquired means the challenger itself was bought. Rates are shares of each strategy's rows.

| Strategy | Rows | Traction | Stalled or failed | Acquired | AI-native |
|---|---:|---:|---:|---:|---:|
| Overlay | 214 | 133 | 6 (2.8%) | 18 (8.4%) | 119 |
| Greenfield | 144 | 97 | 8 (5.6%) | 13 (9.0%) | 31 |
| Migration-led | 33 | 24 | 3 (9.1%) | 4 (12.1%) | 3 |
| AI-run service | 27 | 14 | 2 (7.4%) | 2 (7.4%) | 20 |
| Acquire | 10 | 9 | 0 | 0 | 1 |

Migration-led also holds 1 pending row (GROW).

Traction split by AI-native:

| Strategy | AI-native with traction | Other rows with traction |
|---|---:|---:|
| Overlay | 61 of 119 (51%) | 72 of 95 (76%) |
| Greenfield | 16 of 31 (52%) | 81 of 113 (72%) |
| Migration-led | 2 of 3 | 22 of 30 (73%) |
| AI-run service | 12 of 20 (60%) | 2 of 7 |
| Acquire | 0 of 1 | 9 of 9 |

Within each column the rates are close. The gap between columns is mostly age.

### Overlay

- **What it is.** AI works on top of the system of record and writes back to it. The incumbent stays.
- **When it fits.** Overlays show up at every lock-in level: 29 of 43 rows at lock-in 2, 116 of 231 at 3, 65 of 150 at 4 and 4 of 12 at 5. Buyers range from builders on QuickBooks (Adaptive) to hospital systems on Epic (AKASA) and courts. Courts (7 of 7 rows) and distribution ERP (13 of 16) are overlay-heavy.
- **Evidence.** 133 of 214 rows have traction, and 119 are AI-native. 49 of those 119 are early. AKASA touches no core and bills only after measured gains (see AKASA). Document checkers won J.P. Morgan, Lloyds and Citi as the networks died (see Trade-finance networks).
- **How it breaks.** The platform ships the feature or buys the overlay. Trimble bought Flashtract, one of 18 acquired overlay rows (see Adaptive). 10 of those 18 are not AI-native. Overlays are not the most-acquired strategy: 8.4% of overlay rows were bought, against 12.1% for migration and 9.0% for greenfield. Olive AI raised over $900M automating clicks and shut down in 2023 (see AKASA). It is missing from the table.

### Greenfield

- **What it is.** A new system of record for buyers the incumbent prices out or ignores.
- **When it fits.** SMB and small government, where a founder or a council makes the call. It holds 78 of 231 rows at lock-in 3, 55 of 150 at lock-in 4, and none at 5. In payroll and HR, 13 of 18 rows are greenfield.
- **Evidence.** 97 of 144 rows have traction, but only 31 are AI-native. GovWell started with towns under 50,000 people (see GovWell). Rillet wins the month a company outgrows QuickBooks (see Rillet).
- **How it breaks.**
  - Networks need every counterparty to switch at once. Contour ran 60 to 70 transactions a month when its owners pulled funding (see Trade-finance networks).
  - Breadth also hurts. Rillet's support load swamped it after five to ten sales (see Rillet).
  - Greenfield's stalled or failed rate is 5.6%. That is below migration (9.1%) and AI-run service (7.4%), and above overlay (2.8%). All 8 greenfield failures are not AI-native. The 31 AI-native greenfield rows have none, though 15 of them are early.

### AI-run service

- **What it is.** Sell the outcome. The challenger does the work with AI and licensed staff, then often sells the stack.
- **When it fits.** Licensed work, priced per unit, that buyers already outsource. In an HFMA survey AKASA co-ran, 76% of health systems used outside coding vendors (see AKASA). All 4 such rows in insurance claims are AI-native. The strategy appears at every lock-in level, with buyers from carriers to consumers.
- **Evidence.**
  - 20 of 27 rows are AI-native, the highest share of any strategy.
  - Valon ran a licensed servicer and pitched its own unit cost (see Valon). It claims 3,000+ loans per employee against an industry average of 750. That claim is unaudited. Valon's own figures give about 1,260 in 2025 (593,000 loans / 469 staff) and about 2,500 in August 2026 (810,000 / about 320).
  - Adaptive kept builders' books before it built its product (see Adaptive).
  - The 7 non-AI rows are weaker. 2 have traction, and both are Commure, counted twice. 2 stalled or failed: Benefits Data Trust and Smarter Technologies.
- **How it breaks.** Licenses, cash and channel conflict.
  - Credit bureaus wanted 50 to 100 loans before Valon could report to them (see Valon).
  - Valon competed with its software buyers (inferred), then sold the servicer.
  - The model needs capital. Valon had raised over $290M by August 2026. Benefits Data Trust, a call-center service, closed in 2024 with 250 to 273 staff.

### Migration-led

- **What it is.** Win by moving data and logic off the old core, with proof that nothing changed.
- **When it fits.** High lock-in, and an enterprise buyer already committed to leaving. It is 1 of 43 rows at lock-in 2 and 4 of 12 at lock-in 5. Lock-in 5 is a single category, mainframe COBOL, so "4 of 12" describes that category only. Utility billing puts 6 of its 12 rows here.
- **Evidence.**
  - 24 of 33 rows have traction. Only 1 is early, so the rate reflects age. Among rows that are not AI-native, migration's traction rate (73%) matches overlay (76%) and greenfield (72%).
  - Only 3 rows are AI-native.
  - Mechanical Orchard records what the old system takes in and puts out (see Mechanical Orchard). A slice cuts over only when outputs match byte for byte.
  - Kraken ran Octopus Energy's billing, then licensed it to 40 utilities in 27 countries.
- **How it breaks.** Sales cycles outrun cash, and platforms give the tool away.
  - A bloop co-founder put bank sales cycles at 18 to 24 months (see bloop).
  - AWS prices its mainframe agent at zero (see bloop).
  - GROW's 2025 takeover of HESTA's administration brought a long member-services outage.

### Acquire

- **What it is.** Buy a legacy vendor or its book, then move the customers to a modern core.
- **When it fits.** Fragmented service markets, or a legacy vendor with a captive base. Its 10 rows span 8 categories and every lock-in level from 2 to 5.
- **Evidence.**
  - 10 rows: 9 with traction, 1 early, and none stalled, failed or acquired.
  - Only 1 is AI-native: Procode AI, which buys surgical billing agencies.
  - Sagent took over Fiserv's legacy servicing cores and is moving that base onto Dara.
  - IKS Health bought TruBridge, a rural hospital EHR and billing vendor, for about $557M.
  - No deep-dive case used this strategy.
- **How it breaks.** The buyer can end up running the legacy it meant to retire (inferred). Rocket Software paid $2.275B for the Micro Focus COBOL business and modernizes it in place.
- **Recoded rows.** Pismo (Visa), Finxact (Fiserv), Plex and Fiix (Rockwell) and Clearwater were acquisition targets, not acquirers. They now count as greenfield.

## Four stages

Each cell shows what the cases did and where they stalled.

| Strategy | First wedge | First 10 customers | Expand | Replace the core |
|---|---|---|---|---|
| Overlay | One auditable step, no new screens: AKASA's prebill review, Adaptive's AP. Stalled: AKASA's claim-status start. | Founder-sold, priced on gains or below the cost of a hire. AKASA won Montage by RFP. Adaptive had about 10 paying. | More steps and channels, such as 40+ accounting firms at Adaptive. Risk (open question in the case): Adaptive links to Foundation and Vista by CSV only. | Declined. Adaptive sits on the ERP. AKASA leaves Epic billing alone. |
| Greenfield | A forced switch: outgrowing QuickBooks (Rillet), small-town permits (GovWell), digital letters of credit (networks). | Founder sales plus heavy service. GovWell signed five governments before writing code. Stalled: one Contour bank took two years to start. | Modules, departments, audit-firm partners. Stalled: Rillet's breadth, GovWell's RFP ceiling, Contour's tiny volume. | Partial: about 180 NetSuite or Intacct switches, one Accela town. The networks never aimed at booking engines (inferred). |
| AI-run service | A licensed slice. Valon subserviced agency loans for Rithm. AKASA ran claim status with remote experts. | Investors who own volume. Rithm, Valon's anchor investor, was close to half of Valon's book (inferred). | Volume and unit-cost proof: 593,000 loans and $86M revenue in 2025. Stalled: license catch-22s, 2022 cash. | Sell the stack. Newrez, part of Rithm and so a related party, moves 4M+ homeowners off an in-house core onto ValonOS from 2027. No MSP shop yet. |
| Migration-led | The job that sank the last project: one batch program at Mechanical Orchard. Fixed-price COBOL pilots at bloop. | Paid pilots, likely through founder networks (inferred). About ten described at Mechanical Orchard. Stalled: no named customer at bloop. | Job clusters, then screens and applications, sold through integrators. Stalled: bloop's 18 to 24 month cycles. | Applications retired, no whole mainframe switched off. bloop pivoted to a developer tool in June 2025, and that company shut down in April 2026. |
| Acquire | Buy a book. Procode AI bought a surgical billing agency. | Inherited with the book. | Move the base to a new core, as Sagent does with Dara. | No case evidence yet. |

**First wedge.** The wedges that grew share three traits. The buyer already pays for the job. One buyer gets the full return. Someone can audit the output. AKASA's claim-status start was cheap and safe but did not compound (inferred). Its prebill review did, because coders' screens stayed the same (see AKASA). A Contour letter of credit needed four parties on the network (see Trade-finance networks).

**First 10 customers.** Founders did the selling. Early buyers came through networks or out of need. Valon's CEO says he sold over $100M of contracts almost alone (see Valon). Rillet's CEO says nobody wants to buy an ERP from a startup (see Rillet). Its first buyers came through partners, dinners and some desperation.

**Expand.** Growth came from adding modules, departments and channels inside one buyer type. GovWell sold Casa Grande seven modules for $135,638 a year (see GovWell). Rillet added EY and RSM as partners (see Rillet). AKASA once planned moves into supply chain, HR and IT (see AKASA). Its growth came after it narrowed to inpatient coding and documentation.

**Replace the core.** None of the eight cases has done this against a dominant incumbent.
- Valon came closest. Its first whole-shop wins came off an in-house core and off Sagent, not off MSP. The first buyer, Newrez, is part of Rithm, Valon's anchor investor and a customer (see Valon).
- Mechanical Orchard has retired applications, not whole mainframes (see Mechanical Orchard).
- The overlays chose not to try (see Adaptive, AKASA).

Table rows outside the cases show it can be done. None of these three is AI-native:
- Kraken (migration) bills for 40 utilities, with $500M+ in contracted revenue and 70M to 90M accounts.
- Thought Machine passed $100M revenue in FY2025 and has signed 68 banks, 18 of them tier 1.
- Candid Health, a greenfield RCM core, has raised $219M. Its ARR grew 190% and its net dollar retention is about 180%. The AKASA case names it as the counter-bet.

## Choosing a strategy

Start with the score parts, then the buyer. Each part scores 1 to 5. Lock-in and crowding subtract from the total.

Pain is barely measured. It scores 2 or 3 in all 35 categories, and the signal is weak in 30 of them (see Data limits). AI fit is 4 in 24 categories. The AI-native share of rows barely changes with AI fit: 61 of 145 rows at AI fit 3 or less, 116 of 291 at 4.

Size, lock-in and crowding do the sorting. But size has unit errors, and lock-in levels mostly track single categories.

| If the category shows | Lean toward | Evidence |
|---|---|---|
| Lock-in 2 | Greenfield or overlay | 1 of 43 rows is migration-led. All 43 sit in three categories (manufacturing ERP, distribution ERP, warehouse management), each at crowding 5. |
| Lock-in 3 | Greenfield at a switching moment, with hands-on migration | Rillet, GovWell |
| Lock-in 4 or 5 | Overlay first, migration with proof of equivalence, or greenfield for a buyer the incumbent ignores | 23 of 162 rows are migration-led, while greenfield holds 55 of 150 rows at lock-in 4. Lock-in 5 is one category (mainframe COBOL, 12 rows). |
| Size 5 | A slice of one buyer's volume | At end-2023 Rithm sent Valon 4.9% of the UPB underlying its MSRs, yet Rithm was close to half of Valon's book (inferred). Rithm is also Valon's anchor investor, so concentration and related-party risk are high. Several size-5 scores are unit errors (see Data limits). |
| Size 2 or 3 | One buyer who gets the full return | Traydstream needed one bank. Contour needed four parties. |
| Pain 3 (low confidence) | The workaround buyers already pay for | 76% of health systems used outside coding vendors, in an HFMA survey AKASA co-ran |
| AI fit 4 | An agent or service that owns one judgment step | AKASA's coding review, Valon's payment agent |
| AI fit 3 or less | Workflow and service first, agents later | MaintainX (field service, AI fit 3, not AI-native) reached 13,000+ customers on workflow software |
| Crowding 5 | The step platforms and funded rivals skip | AKASA's autonomous inpatient coding, which no named customer yet runs in production (inferred) |
| Crowding 3 | Open ground, but check budgets and coverage | 3 categories, 23 rows: courts, trade finance, port TOS. Funded overlays already serve trade finance. Port TOS has no AI-native traction and one AI-native failure (eYARD). Learned Hand's Riverside contract was $10k. Low crowding may mean low study coverage. |

Crowding counts every challenger and its funding, AI-native or not. Check the AI-native count yourself. Government benefits scores 5 on crowding with only 3 AI-native challengers.

- **SMB.** Enter below the incumbent's price floor, at a moment that forces a switch.
  - Adaptive charged $300 a month on top of QuickBooks (see Adaptive).
  - Keep adoption one-sided. Flashtract needed both contractors and subcontractors to join (inferred), and Trimble bought it.
  - Watch ticket size. At Adaptive's $599 entry price, 750 customers would bring in about $5.4M a year. That is a reference point, not an estimate, because most of Adaptive's 750+ customers pay custom prices. The customer count is also unstable: Adaptive claimed more than 1,000 in February 2026 and 750+ in September 2026.
- **Enterprise.** Sell a slice the buyer can try inside processes it already runs.
  - AKASA proves value on last year's encounters, then prices on the gain (see AKASA).
  - Budget for long cycles. Carrington spent well over a year inside Valon before buying (see Valon).
  - Borrow distribution from integrators and core vendors (see Mechanical Orchard, Trade-finance networks).
- **Government.** Enter where procurement is a council vote.
  - GovWell's median sales cycle is three months (see GovWell).
  - Above the small-town band, Winston-Salem's RFP asks for references from places near 400,000 people.
  - Five mostly government categories are courts, permits, benefits, tax and land registry. In them, 36 of 55 rows are overlays and none are migration-led. Utility billing (6 of 12 rows migration-led) and student information (3 migration rows) also sell largely to public bodies, and they are left out of that count.

## Failure patterns

Four patterns recur in the cautionary cases. The table cannot rank them. It under-samples dead companies, and its acquired rows mix good and bad outcomes.

The 39 acquired rows break down as follows. The split is our reading of the row text, a judgment call.
- **About 26 strategic or private-equity exits.** CCC paid $730M for EvolutionIQ, Rockwell paid $2.22B for Plex and Autodesk paid about $3.6B for MaintainX. Altruist's sale has not closed.
- **4 distressed sales:**
  - MATRIXX, sold after it failed to refinance
  - powercloud, sold for €30M after a restructuring
  - Paige, sold for under 40% of the capital it raised
  - omni:us, sold after headcount fell from 59 to 45
- **6 small-team absorptions or acqui-hires:** CivCheck, Flashtract, Civira AI, Thoughtful AI, and Brace twice.
- **3 unclear:** Vendr, Trade Ledger, and Puzzle's partial sale.

Pismo and Brace each appear twice, so the 39 rows are 37 companies. GROW is recoded as pending.

**Absorbed by incumbents.** By our reading, at least 8 of the 39 acquired rows went to an incumbent in the same category. Fiserv bought Finxact, Trimble bought Flashtract, Navis bought Octopi, Amdocs bought MATRIXX, Hansen bought powercloud, Clariti bought CivCheck, Accela bought Civira AI and CCC bought EvolutionIQ. Amdocs paid about 2.2 to 2.9 times sales for MATRIXX after it failed to refinance. Hansen paid €30M for powercloud. GROW pulled HESTA away from Link, which is now part of MUFG. MUFG's pension arm then signed a binding scheme to buy GROW in August 2026, while GROW's auditors carried going-concern doubts. The inputs do not confirm the deal closed. Some exits paid well: CCC paid $730M for EvolutionIQ. Test (judgment, not a finding): no single legacy platform carries over half your revenue. The Adaptive case calls 50% an inferred threshold.

**Sales cycle longer than runway.** This pattern rests on one company.
- bloop raised $7.43M in total and averaged 3 to 6 UK staff (see bloop).
- Its co-founder put bank sales cycles at 18 to 24 months.
- In January 2025 he said no pilot had yet failed to convert.
- A Canadian customer paid six figures, then the deal died when bloop's contact was fired.
- bloop pivoted to the developer tool Vibe Kanban in June 2025. That company shut down in April 2026.
- The table has only 3 AI-native migration rows, so there is little to compare it with.

Valon, by contrast, had servicing revenue ($86M in 2025) while its software deals took years (see Valon). Test (judgment, not a finding): cash covers 1.5 times the median time from pilot to contract (see bloop).

**Consortium governance.**
- Contour, we.trade and Marco Polo were owned by the banks meant to use them.
- No Contour bank owner would lead a round, and 170 investors passed (see Trade-finance networks).
- At we.trade, owners could not agree on new money, and only 2 of its shareholder banks fully deployed it. It went into liquidation in June 2022. Marco Polo followed in February 2023.
- The same trap shows when a parent is also the main customer. Kaluza stalled amid a shareholder deadlock. MassMutual shut its spin-off Haven Technologies, saying the standalone economics did not work.

Test (judgment, not a finding): one investor can fund 24 months without a vote (see Trade-finance networks).

**Point tools becoming features.** Overlays make up 8 of the 10 acquired AI-native rows. That is close to their 67% share of all AI-native rows (119 of 177), so the count says little on its own. The stronger evidence is that platforms now ship the same steps:
- Epic codes radiology and emergency medicine on its own (see AKASA).
- ICE put AI voice and chat agents into beta for MSP users (see Valon).
- Intuit and Foundation added AI to construction accounting (see Adaptive).
- NetSuite announced an autonomous close (see Rillet).
- AWS gives its mainframe agent away (see bloop).
- HSBC built its own document checker (see Trade-finance networks).

Test (judgment, not a finding): if the platform lists your feature, plan for bundling (see AKASA).

## Where to look next (provisional)

The original shortlist covered categories scoring 50 or more with two or fewer AI-native challengers showing traction. Four of its five picks scored high on size rows in the wrong units. Re-graded in buyer units, only courts and agriculture still reach 50. Every category needs a buyer-unit re-grade before any ranking. Treat the five notes below as candidates to check, not a ranking.

The filter also has a coverage problem. "Two or fewer AI-native challengers" is a count from the study, whose India and EU coverage is thin. A gap here is a gap in the study's coverage, not necessarily in the market. Trade finance stays dropped, since funded overlays already do its document checking (see Trade-finance networks).

1. **Courts and justice case management (55, or 50 if the SG row also goes; was 60).**
   - Scores: size 4 (or 3), pain 2, AI fit 4, lock-in 3, crowding 3.
   - All 7 challengers are overlays. Disclosed funding is about $8M, but 4 of the 7 rows have no parsed funding figure (jAI, Gotiva, eCourtDate, CaseLines).
   - Of 5 AI-native rows, 2 have traction and 2 were acquired, by Clio and Jusbrasil. Both exits were small: Learned Hand had raised about $5M, and jAI had no outside funding.
   - Known contracts run from $10k to about $314k. Read this as low disclosed funding and small budgets.
   - Crowding is computed from the study's own 7 rows, so low crowding may just mean low coverage.
   - No row rebuilds the case management core.
   - Fit: GovWell's play for county and municipal courts, with drafting or transcription as the wedge.
   - Risk: budgets may be too small to fund a core.
2. **Land registry (45; was 55).**
   - Scores: size 3, pain 2, AI fit 4, lock-in 3, crowding 4.
   - 5 of 9 challengers are AI-native, all overlays or services. Among those, only Landeed and Orbital have traction. Medici, Balcony and PEXA (not AI-native) also have traction.
   - Landeed is India-based, where the study's data is thin.
   - Counties are buying new cores now. Medici Land Governance, coded as a non-AI greenfield, won three county recording RFPs in 2026. DuPage's contract is $899,900 over about three and a half years. Those RFPs were titled "AI-Native" recording system, so Medici's label needs review. If it is recoded, AI-native traction here rises to three.
   - Fit: an AI-native recording system sold county by county, GovWell style.
   - Risk: Advara, a registry spin-off, found no outside customer.
3. **Mortgage servicing (40; was 55).**
   - Scores: size 2, pain 2, AI fit 4, lock-in 3, crowding 4. The old US size row counted MSP's loans, not servicers.
   - 3 of 7 challengers are AI-native. Valon is the only AI-native challenger replacing the core. Sagent (Dara), Thought Machine (Together) and PennyMac's in-house SSE are core rows in the same category.
   - MSP ran about 36 million loans in 2022 (see Valon). No MSP shop has confirmed a move off it.
   - Kastle overlays MSP and says it is live at 10 of the top 25 servicers.
   - Fit: overlay MSP now, or target servicers on in-house and end-of-life cores (see Valon). Ginnie Mae servicing is a gap: ValonOS could not fully run it in June 2026.
   - Risk: ICE is adding AI to MSP, and Wells Fargo just renewed it.
4. **Government benefits (35; was 50).**
   - Scores: size 2, pain 3, AI fit 4, lock-in 4, crowding 5.
   - Crowding comes from non-AI money such as Hyperscience and Unite Us. Only 3 of 14 challengers are AI-native: Fortuna Health, Turnout and Careforce.
   - At one plan, Kern, the Medi-Cal renewal rate rose from 38% to 96% with Careforce's agents. That figure comes from a blog by CHCF, which invested $500K in Careforce. Careforce is coded early.
   - Fit: overlays and AI-run services at the edges, such as renewals and claims filing.
   - Risk: lock-in 4 keeps the core out of reach. Benefits Data Trust, a service, closed in 2024.
5. **Agriculture and commodity trading (50, unchanged).**
   - Scores: size 3, pain 3, AI fit 4, lock-in 3, crowding 4.
   - 3 of 11 challengers are AI-native, and only CommodityAI shows traction. That traction is estimated, not reported: GetLatka put its ARR at about $330K in September 2025, with a team of 6.
   - Traders still run shipments through email, PDFs and WhatsApp.
   - Fit: an overlay that writes trades back into the existing system, as CommodityAI does.
   - Risk: data plays have failed here. Gro Intelligence raised over $117M and closed in 2024.

Pick one category from this list. Confirm the gap exists outside the study. Find the step its platform has not shipped. Run that step for one buyer before you sell software, and budget for it. Valon raised over $290M while it ran a servicer, and Benefits Data Trust, a service, closed.

## Limits

- **Eight cases.** Stage claims and "how it breaks" claims rest on eight case studies. Table rows show the claims can fail elsewhere.
- **Row-level counts.** Counts are rows, not companies. About 19 rows repeat a company.
- **Our recoding.** Recoding the labels (acquire targets, per-company consistency, Valon, GROW) moved several counts. Other coding errors likely remain.
- **Judgment calls.** Exit types, the "same-category incumbent" count and every "Test" line are judgment.
- **Unaudited figures.** Company claims (loans per employee, ARR, customer counts) are unaudited unless stated.
- **No causation.** Strategy and outcome are associated in the table, not shown to be cause and effect. Age and category explain much of the variation.
- **Scores.** Category scores await a buyer-unit size re-grade, and pain scores rest on weak signals.