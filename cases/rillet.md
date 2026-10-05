# Rillet

## Summary

Rillet is a new general ledger and finance ERP that takes venture-backed companies off QuickBooks, NetSuite, Sage Intacct and some older enterprise ledgers [1]. It pulls transactions straight from tools such as Stripe, Salesforce and Brex [2]. It keeps the accounting math deterministic [3] and uses AI for intake and review, with a human approving every entry [4]. Its own CPAs run migrations that it says take 4 to 6 weeks [2][5]. By August 2026 it claimed 600+ customers in 60 countries and a $1B valuation, yet only about 30% came from NetSuite or Sage Intacct, roughly 180 companies against NetSuite's 43,000 (inferred) [6][7][1][8]. The lesson: a system of record cannot be sold as a feature wedge, so Rillet aimed at a moment, the month a company outgrows QuickBooks, and bought trust with accountants on its own payroll (inferred).

## The legacy it attacks

Venture-backed companies climb a ladder of ledgers. Most start on QuickBooks and move to NetSuite or Sage Intacct. Rillet's 2024 launch release framed the choice as 25-year-old software built for small businesses (QuickBooks) or for large corporations (NetSuite) [9].

NetSuite was founded in 1998 [10]. Oracle agreed to buy it in July 2016 for about $9.3B, when it ran 30,000+ companies and subsidiaries [10]. In 2026 NetSuite claimed 43,000+ customers, including 61% of technology companies that went public since 2011 [8]. Intacct was founded in 1999 and Sage bought it for $850M in 2017 [11]. Older mid-market firms still run Microsoft Dynamics GP. Its product support and updates end on 31 December 2029, and security patches end on 30 April 2031 [12].

Controllers and small accounting teams run these systems, often helped by outside admins and implementation partners (inferred). Sequoia says graduating companies land on systems that take 10+ specialists and 15 to 20 days of manual close work each month [13]. Rillet says NetSuite needs a full-time admin or consultant and up to 18 months to implement [5]. Both are interested parties.

Why they stick:

- **Audit.** The ledger is the audited system of record. Sequoia's Julien Bek called removing it "a kind of open-heart surgery" [2].
- **Migration pain.** OnlineMedEd's move from QuickBooks to NetSuite took over six months plus three months of cleanup [14].
- **Skills.** New hires and outsourced firms know QuickBooks, NetSuite and Intacct, not Rillet [15].
- **Bundles and contracts.** NetSuite sells add-on modules and discounts multiyear deals [8]. Lunai Bioworks paid NetSuite about $85K to $100K a year and was quoted $150K+ for a multi-currency module, per a Rillet case study [16].
- **Data gravity.** Years of history and audit trail live in the old ledger (inferred). Kopp argues the live data already sits in upstream systems that "pump down" what he calls "dumb journal entries" into the ledger [17].

## Origin

Nicolas Kopp (CEO) and Stelios Modes (CTO) founded Rillet in 2021 [18]. The legal entity is Gnau Inc., a Delaware corporation with a New York address [19]. Kopp was US CEO of the neobank N26 [2]. Modes built N26's payment infrastructure [20]. Sequoia says both hit the limits of legacy ledgers while scaling N26 [13].

The idea came from the monthly close. Kopp says he sometimes waited four to six weeks for consolidations across entities [4]. He concluded it "was really not a human problem… it was really a software problem" [21].

Why then:

- **Data moved.** Revenue, spend and payroll data now sit in API-first tools such as Stripe, Salesforce, Ramp, Brex and Rippling, which Rillet reads directly [2].
- **Incumbents aged and changed hands.** NetSuite and Intacct became units of Oracle and Sage [10][11]. Rillet calls such owners "slow-moving conglomerates" [20].
- **Labor shrank.** US bachelor's and master's accounting graduates fell 6.6% combined in the 2023-24 academic year, per AICPA data [22]. At launch Rillet pitched relief for "an already shrinking accounting workforce" [23].
- **LLMs arrived mid-build.** Rillet was founded in 2021 [18] and added AI later. Its site offered an AI co-pilot waitlist in June 2023 [24]. Its July 2024 launch still said "automation-first ERP" [25]. "AI-native" became the label with the 2025 rounds [26] (inferred from wording).

Rillet says it spent three years building before launch [27].

## First wedge

Kopp says a narrow product was not an option. Selling a partial ERP, "you get laughed out of a room," so Rillet was "platform-first" [28]. The wedge sat in the messaging and one product: SaaS and AI companies with shared pain, and a module for revenue recognition, invoicing and ARR tracking [28].

The archive matches. In June 2022 the site read "Accounting for SaaS companies" [29]. In January 2023 it promised revenue recognition and SaaS metrics "built right in" for teams patching an outgrown ledger with spreadsheets [30]. By late 2024 its footer linked a "Maxio + QBO" to Rillet switching page, aimed at companies running QuickBooks plus a bolt-on revenue tool [31].

Why this job and this buyer:

- **A forced switching moment.** Kopp says the first ideal customer was "very clear once you start outgrowing QuickBooks," while NetSuite migrations have less defined "insertion points" [17]. Postscript left QuickBooks after an acquisition added Israeli shekel exposure [32].
- **Clean inputs.** SaaS revenue starts as structured CRM and billing records, which suits rules-based automation (inferred).
- **Audit pressure.** Halcyon left QuickBooks and Maxio partly because its revenue recognition was "not audit-ready for an upcoming audit" [33].

## First 10 customers

Rillet has not named its first ten customers. The archive gives a partial view. In January 2023 its site quoted users at Omni, Codat, Lang.ai and Rundoo, plus the accounting firm Graphite Financial [30]. Lang.ai's COO said Rillet was "closing our books for the month and handling invoicing for us" within weeks [30]. Early Rillet was part software, part service (inferred).

**Finding them.** Kopp says "nobody wants to buy an ERP from startup." With zero references, first customers came through "creative ways," "some customer desperation" and a bet on the team [17]. During stealth Rillet ran "multiple micro-launches" with live customers, some giving "very negative feedback" [28]. First Round helped host a New York heads-of-finance dinner in June 2023 [34]. Ramp became a partner in November 2023 [35]. Image Relay's accounting director heard of Rillet in an industry Slack channel [31].

**Selling.** Sales cycle length is not public. Kopp describes sandbox accounts during evaluation and no multi-meeting funnel [17].

**Implementing.** An in-house team of controllers, auditors and CPAs extracts the data, has the customer review the chart of accounts and department structure, and runs an automated reconciliation, in 4 to 8 weeks [3]. Allovue left Sage Intacct in one week and cut software spend from $60,000 to $20,000 a year, per Rillet [36].

**Pricing.** In January 2023 plan tiers were set by seats and integrations, with no public prices, a 30-day free trial, included historical data migration and CPA support [37]. Multi-entity and multi-currency were marked beta [37]. Rillet now says it prices on features and complexity, not seats or revenue [18]. A third-party tracker puts the median contract near $28,300 a year, range $20,100 to $34,800, with no sample size given [38].

Rillet had 70+ customers at its July 2024 launch [25] and 100 by year end, with an NPS of 70 [27].

## How big it is now

| Round | Date | Amount | Lead | Notes |
|---|---|---|---|---|
| Pre-seed and seed | announced 29 Jul 2024 | $13.5M | First Round, Creandum | Susa Ventures; angels incl. former CAO of Facebook and Stripe [2][9] |
| Series A | 28 May 2025 | $25M | Sequoia | angels incl. former NetSuite CFO Ron Gill [26] |
| Series B | 6 Aug 2025 | $70M | a16z, ICONIQ | about $500M valuation per a source; Oak HC/FT, FOG Ventures [39] |
| Series C | Aug 2026 | $100M | ICONIQ | $1B valuation; came together in under 48 hours [7] |

A Form D filed on 1 September 2026 reports $100.1M of equity sold to 22 investors, first sale on 18 August 2026, with Julien Bek, Alex Rampell and Seth Pierrepont as directors [19]. The four rounds sum to $208.5M (inferred).

- **Customers:** nearly 200 in May 2025 [2], 300+ in January 2026 [4], 600+ in 60 countries in August 2026 [6]. Kopp's August 2026 mix: 50% from Intuit, 30% from NetSuite and Sage Intacct, 20% from Oracle, SAP, Workday and Microsoft [1]. About 40% sit outside tech [40].
- **Revenue:** not disclosed. Revenue had grown five-fold since launch as of May 2025 [2]. ARR doubled in 12 weeks (August 2025) [39]. In August 2026 Rillet said "new ARR doubled last quarter" and AI agent usage grows 70% a month [27].
- **Headcount:** 15 to 80 during 2025 [27]. Competitor Numeric counted 90 to 120 on LinkedIn in February 2026 [41].
- **Named customers:** Windsurf and Decagon (May 2025) [2]; Postscript and Bitwarden (August 2025) [20]; Neuralink, Mercor, Skild AI, Sotheby's and LangChain (August 2026) [6]. Mercor runs $2B+ of ARR with a three-person finance team, per the company [40].
- **Channel:** Armanino and Wiss (2025) [39], an alliance with EY US (29 April 2026) [42], RSM (September 2026) [43], and per ICONIQ, KPMG and half the top 30 US accounting firms [6]. Expensify's Q1 2026 results list a new agreement with "Rillet ERP" [44].

## What made it hard

**Sales cycle and trust.** Prospects asked "How many other customers do you have?" when the answer was zero [3][17]. NetSuite now sells the same doubt, calling Rillet a young company "still building the track record that many finance leaders and auditors look for" [8].

**Audit and regulation.** Rillet holds SOC 1 Type II and SOC 2 Type II reports [18]. Its EY alliance is pitched on risk and controls [42]. Auditors may be meeting the product for the first time [45]. US auditor-independence rules limit what an audit firm may implement for its own audit clients, which caps the Big Four channel (inferred).

**Breadth.** After the first five to ten sales, the support load of a wide platform meant "you really start drowning" [28]. Gaps remain: no inventory, manufacturing or project accounting [15]. NetSuite says Rillet lacks multibook accounting and broad localization and only recently added basic fixed assets [8]. Kopp concedes Rillet "would not legitimately be able to support Toyota today" [17].

**Migration.** Kopp says winning customers off NetSuite and bigger systems "took a little longer," because the switching moment there is less defined [17]. Rillet quotes 4 to 6 weeks but also reports a G2 reviewer average of about two months [18]. Rillet says leaving Intacct or NetSuite is often faster than leaving QuickBooks or Xero, because that data was already cleaned once [36].

**Talent.** An early go-to-market hire, a former auditor, could not ramp on outbound email and tools, costing three to four months of runway [46]. Kopp says early on "nobody wants to work for your company" [28].

**Incumbent response.** NetSuite published a "NetSuite vs. Rillet" page and lists Rillet beside SAP and Workday in its switcher menu [8]. On 7 October 2025 it announced NetSuite Next, with agentic workflows and Autonomous Close, rolling out in North America within 12 months [47]. Intuit launched Intuit Enterprise Suite in September 2024 [48]. Its annualized revenue passed $145M in Q4 fiscal 2026, up 4x, and about three-quarters of Intuit's mid-market customer additions came from upgrades or desktop migrations within its own base [49].

**Cash.** Rillet built for three years before launch [27]. Its first disclosed capital was a combined $13.5M pre-seed and seed [2]. Kopp calls the long stealth "really not the recommended approach" [28]. Capital stopped binding once growth showed: three rounds in about 15 months (inferred from dates).

## Strategy

Rillet is **greenfield with migration-led delivery**. It is a new ledger meant to be the system of record, not an overlay on NetSuite. It lands where no real ERP exists yet, then uses CPA-run migrations and audit-firm alliances to take accounts from incumbents (inferred from [1][5][42]). It has made no acquisitions we could find. Early on it also did some customers' books, itself or through a partner network [30][50]. That service layer was a bridge, not the model (inferred).

The path runs from the QuickBooks exit, to a wider product (receivables, payables, bank reconciliation, close, revenue recognition, consolidation and the Aura agents) [51], to NetSuite, Intacct and enterprise ledgers [1]. Kopp says Rillet will "never" build HR or CRM [17]. He expects pricing by "jobs to be done," such as an AR clerk, in two to three years [17].

How far it has got: 30% of 600 customers is about 180 NetSuite or Intacct switches, a number equal to about 0.4% of NetSuite's base alone (inferred) [1][8]. In 2025 its CEO called the product "a subset of an ERP" [17].

| | Rillet | Puzzle | Lensing (ex-Everest) |
|---|---|---|---|
| Founded | 2021 [18] | end of 2019 [52] | 2020 [53] |
| Capital | $200M+ [27] | $50M by Nov 2023 [54] | $140M at Nov 2024 launch [55] |
| First buyer | Scaling SaaS and AI finance teams [28] | Startups and their accounting firms [54] | SaaS firms of 251 to 5,000 staff [56] |
| Scope | Ledger core; no HR or CRM [17] | Ledger and close [60] | Ledger plus billing, cloud cost, HR, PSA [58] |
| Price | ~$28K/yr median [38] | $30 to $360/month software plans [59] | Not public [56] |
| Status | 600+ customers, $1B (Aug 2026) [6] | Sale of firm business to Accrual announced Sep 2026 [60] | Renamed Aug 2026; few named customers [61][56] |

Puzzle chased the same idea, a ledger rebuilt for API-first startups, at a far lower price [52][59]. It reached 7,000+ startups, small businesses and accounting firms [60]. In September 2026 Accrual, launched in February 2026 with $75M led by General Catalyst, agreed to buy Puzzle's accounting-firm business and ledger technology, with closing expected in the following weeks [60][62]. Founder Sasha Orloff joins Accrual, and Puzzle continues for startups under a new CEO [60]. General Catalyst had also led Puzzle's seed and Series A [52].

Lensing bet the other way. Co-CEO Franz Faerber spent over 25 years at SAP, much of it on the HANA database [55][63]. It raised $140M before launch [55] and built HR and cloud-cost modules [58]. One research profile describes its bet as "end-to-end scope from day one beats the GL-first land-and-expand playbook" [53]. By August 2026 it claimed customers with combined revenue over $1B in 20+ countries [61], but "named customers are scarce" [56].

## What others can copy

1. **Wedge on a moment, not a feature.** Test: can you name the event that forces a re-platform? For Rillet it is outgrowing QuickBooks, the source of 50% of customers [1], set off at Postscript by an acquisition [32].
2. **Own the migration with domain staff.** Test: does your team take full ownership of the data move and go live inside two months? Rillet staffs migrations with CPAs and ex-auditors [18][3].
3. **Keep the core deterministic.** Test: can an auditor reproduce every posting without a model? Kopp wants "an LLM nowhere near" core calculations [3] and says AI never books an entry without human review [4].
4. **Borrow trust from auditors' peers.** Test: count firms that implement or audit on your platform. Rillet has Armanino, Wiss, EY and RSM [39][42][43].
5. **Ship live before you announce.** Test: production customers on press day. Rillet had 70+ [25].
6. **Price to fund white-glove service.** Test: does first-year revenue cover migration labor? Rillet's ~$28K median can (inferred) [38]. Puzzle lists software plans at $30 to $360 a month and migration at $149, which cannot fund CPA-led migrations (inferred) [59].

## Open questions

- **Revenue.** ARR is undisclosed. Rillet's blog said "new ARR doubled" [27], while Kopp told TechCrunch the annualized revenue rate doubled [1] and ICONIQ wrote of "ARR doubling" [6]. Which measure doubled is unclear. At a $28K median, 600 customers imply roughly $17M a year (inferred, rough; larger deals would raise it).
- **Enterprise proof.** Rillet cites three public customers [5]. Its named public case, Lunai Bioworks, had a market value near $6M on 2 October 2026 [64] and reported a material weakness in its May 2026 10-Q [65].
- **Durability.** No verified renewal data is public [66]. Accounting Podcast hosts noted Rillet's lean-team claims are unverified, and one argued companies will not switch ERPs for a better ledger alone [67].
- **Unit economics.** NetSuite argues AI-native prices may reflect "investor subsidies" and future compute costs [8].
- **Incumbent catch-up.** NetSuite Next and Intuit Enterprise Suite target the same seam [47][49].
- **Scope.** Can Rillet add multibook, localization and fixed assets for the 20% of customers who came from Oracle, SAP, Workday and Microsoft without drowning again [1][8][28]?

## Sources

1. TechCrunch, "How AI accounting startup Rillet raised $100M and became a unicorn in 48 hours". 21 Aug 2026. https://techcrunch.com/2026/08/21/how-ai-accounting-startup-rillet-raised-100m-and-became-a-unicorn-in-48-hours/
2. TechCrunch, "Rillet raises $25M from Sequoia to automate general ledger systems using AI". 28 May 2025. https://techcrunch.com/2025/05/28/rillet-raises-25m-from-sequoia-to-automate-general-ledger-systems-using-ai/
3. The FP&A Guy, Future Finance podcast with Nicolas Kopp. Recorded Jun 2025, published 13 Aug. https://www.thefpandaguy.com/future-finance/ai-erp-for-fpanda-teams-to-replace-netsuite-and-automate-close-in-4-weeks-with-nicolas-kopp
4. ERP Advisors Group, "Leaders in ERP: Nicolas Kopp". 30 Jan 2026. https://www.erpadvisorsgroup.com/blog/leaders-in-erp-nicolas-kopp-ceo-rillet
5. Rillet, "Rillet vs. NetSuite" comparison page. Accessed 5 Oct 2026. https://www.rillet.com/compare/netsuite
6. ICONIQ, "ICONIQ leading Rillet's $100M Series C". 18 Aug 2026. https://www.iconiq.com/growth/insights/iconiq-leading-rillets-100m-series-c
7. TechCrunch, "Rillet raises $100M Series C at $1B valuation, 2 years after emerging from stealth". 19 Aug 2026. https://techcrunch.com/2026/08/19/rillet-raises-100m-series-c-at-1b-valuation-2-years-after-emerging-from-stealth/
8. Oracle NetSuite, "NetSuite vs. Rillet: Choose the Best ERP" (Internet Archive capture). 14 Apr 2026. http://web.archive.org/web/20260414130354/https://www.netsuite.com/portal/solutions/netsuite-rillet.shtml
9. PR Newswire (Rillet press release), "Rillet raises $13.5M...". 29 Jul 2024. https://www.prnewswire.com/news-releases/rillet-raises-13-5m-to-build-the-modern-accounting-platform-that-makes-zero-day-close-a-reality-302208527.html
10. NetSuite Inc., Form 8-K Exhibit 99.1 on the Oracle agreement (SEC). 28 Jul 2016. https://www.sec.gov/Archives/edgar/data/0001117106/000110465916135792/a16-15705_1ex99d1.htm
11. Accounting Today, "Sage buys Intacct for $850M". 25 Jul 2017. https://www.accountingtoday.com/news/sage-buys-intacct-for-850m
12. Microsoft Dynamics 365 blog, "Announcing end of support for Dynamics GP". 25 Sep 2024. https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2024/09/25/announcing-end-of-support-for-dynamics-gp/
13. Sequoia Capital, "Partnering with Rillet: The Financial ERP for the AI Age". 28 May 2025. https://sequoiacap.com/article/partnering-with-rillet-the-financial-erp-for-the-ai-age/
14. Rillet case study, OnlineMedEd. Undated, accessed 5 Oct 2026. https://www.rillet.com/case-studies/netsuite-to-rillet-how-onlinemeded-simplified-reporting-and-modernized-their-ledger
15. ERP Scorecard, Rillet ERP review page. Last reviewed 6 Jul 2026. https://erpscorecard.com/erp-systems/rillet
16. Rillet case study, Lunai Bioworks. Undated, accessed 5 Oct 2026. https://www.rillet.com/case-studies/lunai-bioworks-a-global-public-company-achieved-continuous-close-with-rillet
17. Metronome, Unpack Pricing ep. 12 with Nicolas Kopp (transcript). 2025, exact date not shown. https://metronome.com/podcast/unpack-pricing/why-ai-demands-a-new-approach-to-financial-systems-of-record
18. Rillet, "What is Rillet?". Updated 5 Aug 2026. https://info.rillet.com/what-is-rillet
19. SEC EDGAR, Form D, Gnau Inc. (CIK 0002096698). Filed 1 Sep 2026. https://www.sec.gov/Archives/edgar/data/2096698/000209669826000003/primary_doc.xml
20. GlobeNewswire (Rillet press release), "Rillet raises $70M...". 6 Aug 2025. https://www.globenewswire.com/news-release/2025/08/06/3128328/0/en/rillet-raises-70m-to-replace-20th-century-accounting-software-with-ai-native-erp-built-by-accountants.html
21. AlleyWatch, founder interview with Nicolas Kopp. Aug 2024. https://www.alleywatch.com/2024/08/rillet-automation-accounting-high-growth-companies-erp-nicolas-kopp/
22. CFO Dive, "US accounting degree graduates drop 6.6%". 27 Oct 2025. https://www.cfodive.com/news/us-accounting-degree-graduates-drop-talent-shortage/803914/
23. Financial IT, "Rillet Secures $13.5M in Funding...". 30 Jul 2024. https://financialit.net/news/fundraising-news/rillet-secures-135m-funding-led-first-round-capital-and-creandum
24. Rillet AI page, Internet Archive snapshot. 10 Jun 2023. http://web.archive.org/web/20230610134002/https://rillet.com/features/ai/
25. FinSMES, "Rillet Raises $13.5M in Funding". 29 Jul 2024. https://www.finsmes.com/2024/07/rillet-raises-13-5m-in-funding.html
26. Cooley, "Rillet Secures $25 Million Series A". 28 May 2025. https://www.cooley.com/news/coverage/2025/2025-05-28-rillet-secures-$25-million-series-a
27. Rillet blog (Nicolas Kopp), Series C announcement. Aug 2026. https://www.rillet.com/blog/100m-series-c
28. a16z speedrun newsletter, "Nicolas Kopp: Take the wedge every single time". 16 Sep 2026. https://speedrun.substack.com/p/nicolas-kopp-take-the-wedge-every
29. Rillet homepage, Internet Archive snapshot. 28 Jun 2022. http://web.archive.org/web/20220628113042/https://rillet.com/
30. Rillet homepage, Internet Archive snapshot. 31 Jan 2023. http://web.archive.org/web/20230131080147/https://rillet.com/
31. Rillet blog, "Rev Rec + QBO to Rillet Success Story" (archived). 29 May 2024. http://web.archive.org/web/20241107030006/https://www.rillet.com/blog/rev-rec-and-qbo-to-rillet-success-story
32. Rillet case study, Postscript. Undated, accessed 5 Oct 2026. https://www.rillet.com/case-studies/how-postscript-went-multi-entity-multi-currency-and-cut-their-close-to-3-days
33. Rillet case study, Halcyon. Undated, accessed 5 Oct 2026. https://www.rillet.com/case-studies/how-halcyon-went-multi-entity-and-brought-its-entire-accounting-function-in-house
34. Rillet blog, "Rillet's inaugural New York Heads of Finance dinner" (archived). 19 Jun 2023. http://web.archive.org/web/20241107030734/https://www.rillet.com/blog/heads-of-finance-dinner
35. Rillet blog, "Announcing the Ramp x Rillet partnership" (archived). 27 Nov 2023. http://web.archive.org/web/20241107023224/https://www.rillet.com/blog/announcing-the-ramp-x-rillet-partnership-for-more-cost-effective-accounting
36. Rillet blog, "Allovue's Transition from Sage Intacct to Rillet" (archived). 6 Mar 2024. http://web.archive.org/web/20241107043958/https://www.rillet.com/blog/allovues-transition-from-sage-intacct-to-rillet
37. Rillet plans page, Internet Archive snapshot. 31 Jan 2023. http://web.archive.org/web/20230131125624/https://rillet.com/plans/
38. ERP Research, "Rillet Pricing 2026". Mid-2026. https://www.erpresearch.com/pricing/rillet
39. Reuters via Investing.com, "AI accounting startup Rillet raises $70 million...". 6 Aug 2025. https://www.investing.com/news/economy-news/ai-accounting-startup-rillet-raises-70-million-in-andreessen-horowitz-iconiqled-round-4172975
40. Fortune, "Accounting AI startup Rillet reaches unicorn status". 18 Aug 2026. https://fortune.com/2026/08/18/rillet-unicorn-1-billion-valuation-series-c-nicolas-kopp-accounting-ai/
41. Numeric (a competitor), "Rillet vs Campfire". 27 Feb 2026. https://www.numeric.io/blog/rillet-vs-campfire
42. EY newsroom, "EY announces alliance with Rillet...". 29 Apr 2026. https://www.ey.com/en_gl/newsroom/2026/04/ey-announces-alliance-with-rillet-to-provide-ai-native-finance-transformation-with-risk-and-controls-built-in
43. RSM US newsroom, "RSM and Rillet Bring Agentic Finance to the Middle Market". 21 Sep 2026. https://rsmus.com/newsroom/2026/rsm-rillet-agentic-finance-middle-market.html
44. Expensify, Q1 2026 results, Form 8-K Exhibit 99.1 (SEC). 7 May 2026. https://www.sec.gov/Archives/edgar/data/1476840/000147684026000031/exhibit991-8xkq126earnings.htm
45. ERP Research, "AI-Native ERP Systems". 22 Jul 2026. https://www.erpresearch.com/en-us/ai-native-erp
46. Rippling, "He hired exactly right, and still lost 3 months of runway". Undated, c. mid-2025 (inferred). https://www.rippling.com/resources/he-hired-exactly-right-and-still-lost-3-months-of-runway
47. SiliconANGLE, "Oracle NetSuite overhauls user experience, introduces AI-driven updates". 7 Oct 2025. https://siliconangle.com/2025/10/07/oracle-netsuite-overhauls-user-experience-introduces-ai-driven-updates/
48. CPA Practice Advisor, "Intuit Launches AI-Enabled Intuit Enterprise Suite". 17 Sep 2024. https://www.cpapracticeadvisor.com/2024/09/17/intuit-launches-ai-enabled-intuit-enterprise-suite/110627/
49. Intuit, Q4 fiscal 2026 conference call remarks. 25 Aug 2026. https://investors.intuit.com/_assets/_1600dcf5d024a28739f5190ddda8d1c7/intuit/db/946/10378/webcast_transcript/Q4+FY26+Earnings+Script.pdf
50. Rillet solutions page, Internet Archive snapshot. 31 Jan 2023. http://web.archive.org/web/20230131123057/https://rillet.com/solutions/
51. Rillet homepage. Accessed 5 Oct 2026. https://www.rillet.com/
52. TechCrunch, "Puzzle is building a modern accounting package for today's API-enabled startups". 16 Feb 2023. https://techcrunch.com/2023/02/16/puzzle-is-building-a-modern-accounting-package-for-todays-api-enabled-startups/
53. Altis, Everest Systems company research. Updated 2026. https://www.altis.vc/research/company/everest
54. Puzzle blog, "Puzzle raises an additional $30M...". 14 Nov 2023. https://puzzle.io/blog/puzzle-raises-an-additional-30m-to-fuel-a-new-era-of-ai-powered-accounting
55. Lensing (then Everest Systems), press release on emerging from stealth. 20 Nov 2024. https://lensing.ai/everest-systems-emerges-from-stealth-with-140-million-funding
56. ERP Research, "Everest Systems: Pricing, Modules & Honest Review". Last reviewed 29 Jul 2026. https://www.erpresearch.com/en-us/everest-systems
57. FF News, "Accrual to Acquire Puzzle...". Sep 2026. https://ffnews.com/news/accrual-to-acquire-puzzle-expanding-its-ai-platform-into-client-accounting-servi-e5c48cc1
58. Lensing homepage. Accessed 5 Oct 2026. https://lensing.ai/
59. Puzzle pricing page. Accessed 5 Oct 2026. https://puzzle.io/pricing
60. CPA Practice Advisor, "Accrual Takes the Leap Into CAS By Acquiring Puzzle's Technology". 2 Sep 2026. https://www.cpapracticeadvisor.com/2026/09/02/accrual-takes-the-leap-into-cas-by-acquiring-puzzle/189565/
61. Lensing, "Everest reveals new name, Lensing...". 4 Aug 2026. https://lensing.ai/news/everest-reveals-new-name-lensing/
62. CPA Practice Advisor, "Startup Accrual Officially Launches with $75M in Funding". 5 Feb 2026. https://www.cpapracticeadvisor.com/2026/02/05/startup-accrual-officially-launches-with-75m-in-funding-to-bring-ai-native-automation-to-accounting/177600/
63. Lensing blog, "The Co-Founders' Vision Behind Lensing". 4 Jun 2025. https://lensing.ai/blog/the-co-founders-vision-behind-lensing-erp-built-for-saas-businesses/
64. WallStreetZen, Lunai Bioworks (LNAI) quote page. Data as of 2 Oct 2026. https://www.wallstreetzen.com/stocks/us/nasdaq/lnai
65. Lunai Bioworks, Form 10-Q (SEC). Filed 15 May 2026. https://www.sec.gov/Archives/edgar/data/1527728/000173112226000749/e7638_10-q.htm
66. ERP Scorecard, "Rillet Review 2026". 13 Jul 2026, updated 13 Sep 2026. https://erpscorecard.com/articles/rillet-review-2026
67. Earmark CPE / The Accounting Podcast, "AI Is Rewriting the Economics of Accounting Software". 15 Sep 2026. https://earmarkcpe.com/ai-is-rewriting-the-economics-of-accounting-software/

## Fact-check notes

- Summary: migration claim now cites only [2][5]. [3] gives 4 to 8 weeks and [4] gives no timeframe. [3] and [4] now back the deterministic-math and human-review points.
- Legacy: Dynamics GP's 31 Dec 2029 date covers product support and updates only. Security patches run to 30 Apr 2031, per [12].
- Legacy: Lunai's NetSuite cost changed to "$85K to $100K." The case study says $100K, but the CFO's quote in it says "85 grand."
- Origin: Kopp's four-to-six-week wait now says "sometimes," matching "in some cases" in [4].
- Origin: the 6.6% drop counts bachelor's and master's graduates combined. Bachelor's degrees alone fell 3.3% [22].
- First 10 customers: the implementation step changed from "clean up" to "review" the chart of accounts, matching [3].
- How big: the Series C note now says the round "came together" in under 48 hours. [7] reports the commitment window, not a legal close. The Form D first sale is 18 Aug.
- How big: EY alliance changed to "EY US." The EY release names Ernst & Young LLP (EY US).
- How big: Expensify "filing" changed to "results," since the item is the earnings release exhibit.
- What made it hard: the "zero customers" point now also cites [17]. The word zero comes from the Metronome transcript, not [3].
- What made it hard: "took a little longer" in [17] is about winning customers off legacy systems, not migration time. The sentence was rewritten.
- What made it hard: Intuit's "own base" now says "upgrades or desktop migrations," the wording in [49].
- Strategy: the 0.4% figure now states that it compares NetSuite plus Intacct switches with NetSuite's base alone.
- Strategy table: Puzzle's $30 to $360 is software-only list pricing, so it is now labeled "software plans." Service plans cost more [59].
- Strategy table and text: the Accrual deal for Puzzle was announced on 2 Sep 2026 and was "expected to close in the coming weeks" [60]. "Sold" changed to "sale announced."
- Strategy table: Puzzle scope now cites [60], which names the ledger and month-end close products. The [57] citation was not verified.
- Strategy: Faerber's SAP tenure changed from "26 years" to "over 25 years," per his own wording in [63]. The co-CEO title is sourced to [55].
- Copy list #6: Puzzle pricing now reads "software plans," as above.
- Open questions: the revenue bullet implied only press said ARR doubled. Kopp told TechCrunch the annualized revenue rate doubled [1], and ICONIQ wrote "ARR doubling" [6].
- Open questions: "20% enterprise cohort" changed to the 20% who came from Oracle, SAP, Workday and Microsoft [1]. That group is not all enterprise; Microsoft includes Dynamics GP.
- Sources: [3] date corrected to recorded Jun 2025, published 13 Aug. [28] dated 16 Sep 2026. [43] dated 21 Sep 2026.
- No em dashes or banned hype words were found in the draft. Verified unchanged: customer counts and mix, funding table, Form D details, NetSuite and Intacct history, NetSuite comparison-page claims, archive snapshots, Allovue, Postscript, Halcyon, OnlineMedEd, Rippling (three to four months), Intuit IES figures, Lunai market cap and material weakness, Accrual funding, Lensing claims.