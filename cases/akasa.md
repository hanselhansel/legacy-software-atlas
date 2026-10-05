# AKASA

## Summary

AKASA sells AI that runs on top of Epic and other hospital billing systems and does work that revenue cycle staff and coding vendors do today [1][2][3]. Founded in 2018 as Alpha Health, it first automated claim-status checks with machine learning plus remote human experts, then rebuilt itself in 2024 around language models fine-tuned on each hospital's records for coding and documentation [4][5][6][7]. By October 2026 its customers held $180B+ in net patient revenue and about 1 in 10 US inpatient discharges. That month it launched autonomous inpatient coding, which no named customer yet runs in production (inferred) [8]. The lesson: in hospital billing, the money goes to overlays that own a hard, auditable judgment step. Olive AI automated clicks and shut down. Thoughtful AI's stand-alone service was wound down inside its new parent [9][10][11][12].

## The legacy it attacks

AKASA attacks three stacked layers.

The system of record. Epic released Resolute Professional Billing in 1987 [13]. In 2025 Epic held 43.7% of US acute hospitals and 56.9% of beds; Oracle Health held 21.9% of hospitals and MEDITECH 14.7% [14]. Billing shares a database with scheduling and the chart, so replacing billing means replacing the EHR (inferred). NYC Health + Hospitals budgeted $289M over five years just to implement Epic's revenue cycle product, on top of a $764M Epic upgrade [15].

Coding software. 3M's health information unit, now Solventum, claimed a leading US position in computer-assisted coding (CAC) in 2024 and said 75%+ of US hospitals used at least one of its tools [16]. The unit has $1.4B in annual sales. Solventum plans to separate it, through a spinoff or a combination with a peer [17].

Labor. The US employs 200,700 medical records specialists at a median $51,140 (2025 data) [18]. In an HFMA survey run with AKASA, 76% of health systems used outside coding vendors and 55% used documentation (CDI) vendors [19].

Why it stuck: rules, data and skills. At Cleveland Clinic, coding one case means reviewing 100+ documents and choosing among 140,000+ codes, which can take up to an hour [20]. AKASA counts 59 documents and nearly 50,000 words in an average inpatient encounter [21], and coders are expected to finish at least two an hour [22]. The workforce is aging: 55% of Cleveland Clinic's coders were retirement-eligible in 2025 [23]. Existing vendor contracts and Epic-specific workflows add inertia (inferred).

## Origin

Four founders started Alpha Health in 2018 [4][24]. CEO Malinka Walaliyadde had led healthcare investments at Andreessen Horowitz and helped build its healthcare team, after roles at Counsyl and Deloitte [25]. Founding CTO Varun Ganapathi holds a Stanford PhD and had sold startups to Google and Udacity [26]. Ben Beadle-Ryby had led revenue cycle consulting as a partner at the Advisory Board Company and Optum [25]. Andy Atwal completed the team [24].

The insight: the back end of care, not the clinic, blocked progress, and modern software had ignored it [25]. a16z's investment note said hospitals spend $0.25 to collect each $1 of revenue, and that generic RPA copies human steps, errors included [24]. Alpha Health borrowed the driverless-car model: software does the task, remote revenue cycle experts handle exceptions, and the system learns from their fixes [5].

Why then. RPA's limits were visible. Alpha Health's 2020 survey found 58.8% of hospital finance leaders mistook RPA for AI. It also cited Forrester data that more than half of RPA programs ran fewer than 10 bots [27]. COVID strained hospital administrative teams and forced staff cuts, which favored remotely deployed automation [24][28]. The second why-now was large language models. In 2021 AKASA's first transformer approach to coding hit a 512-token limit against charts averaging 1,500 words [29]. By 2025 its models read 50,000-word inpatient records [22]. Walaliyadde states the overlay bet directly: "We're probably not going to reinvent the entire healthcare payment rails of the U.S." [22]

## First wedge

The first job was claim-status follow-up in hospital business offices, alongside other routine back-office tasks [6][30]. The product checked claims on payer portals and returned the results to the EHR. It routed exceptions to work queues for hospital staff or AKASA's experts [30][31]. AKASA rejected the RPA label [27], but this was RPA-shaped work (inferred).

The customer type was the large health system [25]. Montage, the documented case, ran Epic [30]. AKASA gave three reasons for starting with claim status [31]:

- The vendor changes no claim or payer data, so security risk is low.
- It is the cheapest automation to buy.
- It lets a hospital test a vendor before trusting it with harder work.

Staffing gaps added urgency. One academic center had 43 vacancies on a revenue cycle team of more than 400, and AKASA says a single workflow produced 20 FTEs of work [32].

That wedge did not compound (inferred). The one that did came with the 2024 generative AI products. In June 2024 AKASA launched a coding assistant whose suggestions coders accept or revise [7]. It then built an AI reviewer that re-checks encounters after human coders finish [22], now sold as a review of every inpatient encounter before billing [1]. Walaliyadde says the reviewer followed a test in which a third-party auditor preferred AI-coded encounters to human-coded ones. He calls it an easy wedge because frontline workflow does not change [22]. He estimates inpatient coding drives 50% to 60% or more of a health system's revenue [22].

## First 10 customers

AKASA has not published its first ten. Three early accounts are on the record.

- Sutter Health, its largest customer at the June 2020 Series A, whose leaders endorsed Alpha Health in the release [5].
- Nebraska Methodist Health System [25]. In March 2021, CFO Jeff Francis (listed under Methodist Health System) said automation had taken over claim-status checks [6]. In October 2026, listed under Nebraska Methodist, he said the system had moved with AKASA step by step [8].
- Montage Health, a 256-bed Epic system, chose AKASA through an RFP. Claim status took four months to build. Within three months of go-live AKASA had worked about 3,000 claims across five payers. Montage then added payers and its medical group. AKASA reports 13% fewer A/R days and 300+ staff hours saved a month [30].

How AKASA found them is not documented. Founder networks are the likely channel, through Beadle-Ryby's consulting clients and a16z (inferred). It sold with no per-user licenses, no consultants, remote deployment and a shared-value fee tied to customer savings [5]. It promised to be running within 90 days of receiving data [28]. By August 2021 its customers represented $100B+ in net patient revenue [33]. By 2022 those customers ran 450+ hospitals in all 50 states [25]. Sales cycle length is not disclosed. Montage's RFP-to-live path took at least four months (inferred) [30].

## How big it is now

| Round | Date | Amount | Lead |
|---|---|---|---|
| Seed | before June 2020 | about $5M ($25M total less the $20M A) | a16z [5] |
| Series A | 10 June 2020 | $20M | a16z [5] |
| Series B | 23 March 2021 | $60M | BOND [6] |
| Unnamed round (reported) | 18 June 2024 | $120M | not disclosed [34] |

Company releases add up to $85M [5][6]. TechCrunch reports a $120M round and $205M in total, without naming the series [34]. AKASA's press page has no release for this round, and Tracxn lists $85M across three rounds [35][36]. Treat the 2024 round as unconfirmed.

Headcount: Fortune listed 244 US employees in January 2023 [37]. AKASA's Great Place To Work profile, updated February 2026, lists 97 US-based employees [38]. Tracxn estimates 247 (August 2026) [36].

Scale, all company-reported:

- Customer net patient revenue: $100B+ (August 2021) [33]; still $100B+ across nearly 500 hospitals (June 2023) [32]; $145B+ (2026 overview) [4]; $160B+ (June 2026) [39]; $180B+ (October 2026) [8].
- Discharges: customers account for about 1 in 10 US inpatient discharges [8]. That is their share, not the volume AKASA codes. Against 35.7M US admissions in 2024 [40], it implies about 3.5M stays a year at customer hospitals (inferred).
- Growth: inpatient volume processed rose almost 6x in the year to October 2026 [8]. AKASA says it grew more than 10x after its mid-2024 mid-cycle launch, without naming the metric [39].
- Cleveland Clinic: the coding tool reached all US locations in four months in 2025. The CDI tool followed a pilot [41]. AKASA says it processes 100% of the Clinic's enterprise inpatient volume [1].
- Named customers: Cleveland Clinic, Nebraska Methodist, Duke, Johns Hopkins and Stanford [4][8]. Revenue is not disclosed.

## What made it hard

Payer pushback and regulation. Coding sets payment, so captured codes show up as payer cost. In September 2026 the Blue Cross Blue Shield Association estimated that more complex inpatient coding, which it tied to hospital AI, added $942M to its members' costs from 2023 to 2025 [42]. About 70% came from secondary diagnoses. Its claims-based analysis did not prove AI caused the increase [43]. A July 2026 GAO technology spotlight found few independent studies of these tools' accuracy [44].

Data, not migration. AKASA migrates no core system [2], but it tunes a model for each customer on that customer's records [1][22]. Walaliyadde says off-the-shelf and clinical models such as Med-PaLM fell short and that AKASA invested in its own GPU compute. He also says its pre-LLM coding model was never commercialized at scale [22].

Sales friction. Buyers name integration, cost and data security as the top barriers. At large systems cost leads, at 52.5% [19].

Incumbent response. Epic's Penny suggests codes to hospital and professional coders and proposes CDI queries [45]. Epic says Penny will code on its own over time and that 85%+ of its customers use Epic AI [46]. By August 2026 Penny coded radiology and emergency medicine autonomously, with surgery and pathology planned [47]. Oracle Health added coding suggestions in August 2026, for ambulatory professional fees only [48]. Analyst Brendan Keeler reports that apps in Epic's Toolbox partner tier are subject to Epic's non-compete provisions [49].

Talent and cash. The reported 2024 round came 39 months after the Series B (inferred), through a funding drought. US digital health funding was $29B for all of 2021 and $2.5B in the third quarter of 2023 [10]. Great Place To Work counts of US headcount fell from 244 in January 2023 to 97 in February 2026 [37][38], though Tracxn still estimates 247 [36]. A real decline would fit an exit from labor-heavy service work (inferred). Co-founder Varun Ganapathi is now listed as an advisor and Sanjay Siddhanti as CTO [50].

Workforce politics. In October 2024 Walaliyadde said AKASA did not believe in replacing coders with technology [51]. Two years later it launched coding designed to run with no human intervention [8].

## Strategy

AKASA is an overlay that has run three versions of the play (inferred).

1. AI-run service, 2018 to 2023. Bots plus remote experts did back-office tasks inside the customer's EHR [5][6]. In 2022 the founders discussed expanding into supply chain, HR and IT [25].
2. Mid-cycle software, 2024 to 2025. Authorization Advisor came in March 2024 [52], a coding product in June 2024 [7] and a CDI product in 2025 [41]. The suite reviews every inpatient encounter before billing and overlays Epic- and Oracle-based workflows without changing them. Sales start with a retrospective review of past encounters [1][2]. AKASA charges no upfront fee and invoices only after measured financial improvement [1].
3. Autonomy, October 2026. Inpatient stays are coded in under 90 seconds after discharge, against 30 to 60 minutes for a coder [8]. Blinded third-party tests covered encounters representing 65% to 85% of inpatient volume. They checked MS-DRG, principal diagnosis, quality capture and present-on-admission accuracy, and AKASA says it matched or beat human coders [8]. Outpatient facility encounters are next [8].

How far toward the core: AKASA leaves Epic's billing system alone (inferred). It goes after coder hours, rules-based CAC and outsourced coding (inferred). Capstone Partners says spending on autonomous coding and billing rose from $200M in 2024 to $450M in 2025, displacing offshore outsourcing [3]. The prebill product runs at enterprise scale [1]. The autonomous product is days old, and Cleveland Clinic only intends to explore it [8].

Why the money goes to overlays. The core is sunk. Epic covers 56.9% of US acute beds [14], and NYC Health + Hospitals committed over $1B to Epic and its revenue cycle rollout (inferred sum) [15]. AKASA is paid from measured revenue lift, not a capital budget [1]. Capital follows:

- SmarterDx, a prebill clinical AI overlay, grew from about $50M to about $150M in revenue after New Mountain Capital bought it [53]. It is merging with Datavant, backed by $2.7B of KKR and Neuberger Berman preferred equity [54].
- Commure raised $70M at a $7B valuation in May 2026 [55].

The counter-bet is Candid Health. It rebuilt the billing core, raised $120M in July 2026, and says AI added on top of legacy systems has yet to deliver [56].

The two warnings.

Olive AI taught bots to use hospital software as a person would, from EHRs to portals to claims [9]. It raised over $900M and reached a $4B valuation and 900+ hospitals [57]. Axios found it delivered a fraction of the savings it promised [58]. 4sight Health CEO David Johnson writes in HFMA that Epic made Olive stop using Epic's name in marketing, and that its AI often turned out to be screen scraping [59]. Olive cut about 450 jobs in July 2022 and 200 in February 2023, then shut down at the end of October 2023 [10][57].

Thoughtful AI raised $20M in July 2024 for agents doing claims, eligibility and payment posting [60]. In May 2025 New Mountain Capital folded it into Smarter Technologies, the same group as SmarterDx [61]. In April 2026 it gave customers about 90 days' notice that its stand-alone service would end. Acuity News attributes that to portfolio strategy rather than product failure [11]. A competitor says the practice-management vendor CentralReach had shut down unsanctioned bots, Thoughtful's among them [12].

The pattern (inferred): both sold clicks across many tasks, and neither owned a step whose output a customer could audit in dollars. AKASA ran a milder version of that play until 2023, then narrowed.

## What others can copy

1. Enter after the work is done. Sell a review of finished work before selling its replacement. Test: the first product changes no frontline screen. At Cleveland Clinic, coders accepted about half of AKASA's flags in the first 60 days [21].
2. Prove value on last year's data, then price on lift. Test: a retrospective review yields a dollar figure before full rollout, and fees start only after measured gain [2][1].
3. Pick the judgment step the platform has not shipped. Epic automates radiology and emergency medicine coding, and Oracle suggests only ambulatory professional fee codes [47][48]. Neither had announced autonomous inpatient coding by October 2026 (inferred). Test: read the platform's published AI feature list. If your feature is on it, plan for it to be bundled [45].
4. Earn autonomy in stages. Suggestions came first, then 100% review, then autonomy on the 65% to 85% of volume where blinded tests matched coders [8]. Test: publish the share of volume that runs with no human and the accuracy metric behind it.
5. Build for the auditor on the other side. A payer group now links $942M in added costs to hospital AI coding [42]. Test: every code links to a cited passage and a log of whether software or a person made the call [43].
6. Stay narrow. AKASA's 2022 plans reached into supply chain, HR and IT [25]. Its growth came after it focused on the inpatient mid-cycle [39]. Test: the share of revenue from one workflow.

## Open questions

- Does autonomy hold up outside vendor-run tests? GAO says independent accuracy studies are scarce [44]. No named customer is live on autonomous inpatient coding yet (inferred) [8].
- Will payers push back on price? AKASA's fees rise with captured revenue, the same capture the Blue Cross Blue Shield Association calls cost inflation (inferred) [1][42].
- Will Epic absorb it? Penny already suggests hospital codes and CDI queries and promises more autonomy [45][46]. Walaliyadde argues Epic's breadth makes a deep single-task product unlikely from it [22].
- What does the business look like? Revenue, margins and churn are undisclosed, the 2024 round is unconfirmed, and headcount sources disagree [34][36][38].
- Does per-hospital fine-tuning scale? Each customer needs its own trained model [1], which may keep margins closer to services than software (inferred).
- What happened to the 2021 to 2023 automation customers? Customer revenue sat near $100B from August 2021 to June 2023 [33][32]. How many of those accounts remain is not public.

## Sources

1. AKASA, Prebill Optimization Suite product page, undated (accessed 5 Oct 2026). https://akasa.com/solutions/optimization/
2. AKASA blog, 20 Apr 2026. https://akasa.com/blog/revenue-cycle-ai-partner-health-systems
3. HIT Consultant (Capstone Partners data), 29 Sep 2026. https://hitconsultant.net/2026/09/29/capstone-partners-report-ai-enabled-healthcare-it-ma/
4. AKASA, company overview PDF, 2026. https://storage.pardot.com/1017252/1782152398Vu8v58zW/AKASA_Overview.pdf
5. AKASA (as Alpha Health), Series A press release, 10 Jun 2020. https://akasa.com/press/alpha-health-announces-series-a-funding-and-introduces-unified-automation
6. AKASA, Series B press release, 23 Mar 2021. https://akasa.com/press/akasa-raises-60-million-in-series-b-round
7. AKASA, press release, 18 Jun 2024. https://akasa.com/press/unveils-akasa-medical-coding
8. AKASA, press release, 2 Oct 2026. https://akasa.com/press/autonomous-mid-cycle
9. IEEE Spectrum, 26 Sep 2018. https://spectrum.ieee.org/this-healthcare-ai-loves-crappy-software
10. Healthcare Dive, 1 Nov 2023. https://www.healthcaredive.com/news/olive-ai-shuts-down/698455/
11. Acuity News, 24 Apr 2026. https://acuity.news/technology/thoughtful-ai-shutdown-smarter-technologies-aba-transition-2026/
12. Acuity News, 11 May 2026. https://acuity.news/technology/thoughtful-ai-wind-down-aba-automation-replacement-guide/
13. FundingUniverse, Epic Systems company history, undated. https://www.fundinguniverse.com/company-histories/epic-systems-corporation-history/
14. healthsystemCIO (KLAS data), 14 May 2026. https://healthsystemcio.com/2026/05/14/acute-care-ehr-market-share-2026/
15. Politico, reprinted by NYC Health + Hospitals, May 2017. https://www.nychealthandhospitals.org/wp-content/uploads/2017/05/Public-hospitals-to-spend-289-million-on-Epics-revnue-cycle-software-implementation-Politico.pdf
16. Solventum, SEC Form 8-K Exhibit 99.1, 13 Mar 2024. https://www.sec.gov/Archives/edgar/data/1964738/000162828024010988/exhibit991-8xk.htm
17. HIT Consultant, 6 Aug 2026. https://hitconsultant.net/2026/08/06/solventum-announces-intent-to-separate-health-information-systems-business/
18. US Bureau of Labor Statistics, Occupational Outlook Handbook, 2025 data (accessed 5 Oct 2026). https://www.bls.gov/ooh/healthcare/medical-records-and-health-information-technicians.htm
19. AKASA, press release on HFMA survey, 17 Dec 2025. https://akasa.com/press/hfma-genai-revenue-cycle-survey
20. Cleveland Clinic Newsroom, 29 Apr 2025. https://newsroom.clevelandclinic.org/2025/04/29/cleveland-clinic-and-akasa-announce-strategic-collaboration-to-launch-ai-tools-for-the-revenue-cycle
21. AKASA blog (Becker's webinar recap), 19 Aug 2025. https://akasa.com/blog/cleveland-clinic-genai-leap-midcycle
22. AKASA blog (a16z Raising Health podcast transcript), 16 Jun 2025. https://akasa.com/blog/from-chaos-to-clarity-in-data-with-malinka-walaliyadde
23. AKASA blog (HFMA 2025 session recap), 30 Jun 2025. https://akasa.com/blog/lessons-from-cleveland-clinic/
24. Andreessen Horowitz, 10 Jun 2020. https://a16z.com/announcement/investing-in-akasa-pka-alpha-health/
25. AKASA blog (Becker's Healthcare Podcast transcript), 11 Aug 2022. https://akasa.com/blog/beckers-podcast-may22
26. AKASA blog (The Gradient Podcast), 29 Nov 2022. https://akasa.com/blog/the-gradient-podcast-an-interview-on-ai-and-healthcare-with-akasa-cto-and-co-founder-varun-ganapathi
27. Alpha Health, press release, 2020 (survey fielded May to Jun 2020). https://akasa.com/press/confusion-between-artificial-intelligence-ai-and-robotic-process-automation-rpa-high-among-healthcare-leaders
28. HFMA, 23 Mar 2021. https://www.hfma.org/technology/revenue-cycle-technology/alpha-health-using-machine-learning-to-create-fully-autonomous-revenue-cycle-operations/
29. AKASA blog, 21 Oct 2021. https://akasa.com/blog/using-machine-learning-to-enable-autonomous-medical-coding
30. AKASA, Montage Health case study, undated (accessed 5 Oct 2026). https://akasa.com/case-studies/montage-claim-status-case-study/
31. AKASA blog, 17 Dec 2023. https://akasa.com/blog/why-start-with-claim-status-automation
32. AKASA blog (AWS Health Innovation Podcast transcript), 27 Jun 2023. https://akasa.com/blog/aws-health-innovation-podcast
33. AKASA, press release, 24 Aug 2021. https://akasa.com/press/accelerated-growth-and-expanding-customer-base
34. TechCrunch, 20 Dec 2024. https://techcrunch.com/2024/12/20/heres-the-full-list-of-49-us-ai-startups-that-have-raised-100m-or-more-in-2024/
35. AKASA, press release index (accessed 5 Oct 2026). https://akasa.com/press/
36. Tracxn, company profile, data as of 31 Aug 2026. https://tracxn.com/d/companies/akasa/__qi5hY-G0qopywHUJR-A5GrvRjRNeAjTtfX6FQ6lbFLw
37. Fortune, company profile, data as of 11 Jan 2023. https://fortune.com/company/akasa
38. Great Place To Work, company profile, updated Feb 2026. https://www.greatplacetowork.com/certified-company/7025069
39. AKASA, press release, 4 Jun 2026. https://akasa.com/press/nirav-kamdar-md-joins-akasa-vp-clinical-strategy
40. American Hospital Association, Fast Facts on U.S. Hospitals, 2026 edition (2024 survey data). https://www.aha.org/statistics/fast-facts-us-hospitals
41. AKASA, press release, 13 Oct 2025. https://akasa.com/press/cleveland-clinic-akasa-deepen-ai-partnership
42. TechCrunch, 26 Sep 2026. https://techcrunch.com/2026/09/26/insurers-claim-ai-is-already-increasing-healthcare-costs/
43. healthsystemCIO, 29 Sep 2026. https://healthsystemcio.com/2026/09/29/hospital-ai-coding-audit-trail
44. US Government Accountability Office, GAO-26-109116, 16 Jul 2026. https://www.gao.gov/products/gao-26-109116
45. Epic, Penny product page (accessed 5 Oct 2026). https://www.epic.com/software/penny/
46. Epic, 10 Mar 2026. https://www.epic.com/epic/post/real-results-right-now-how-epic-ai-is-reducing-costs-improving-care-and-helping-patients/
47. Healthcare IT Today, 19 Aug 2026. https://www.healthcareittoday.com/2026/08/19/epic-ugm-2026-judy-faulkner-keynote-and-cool-stuff-ahead/
48. healthsystemCIO, 20 Aug 2026. https://healthsystemcio.com/2026/08/20/oracle-health-coding-ai-agent/
49. Health API Guy (Brendan Keeler), 15 Jan 2025. https://healthapiguy.substack.com/p/an-epic-saga-the-startup-odyssey
50. AKASA, leadership page (accessed 5 Oct 2026). https://akasa.com/leadership
51. AKASA, press release, 16 Oct 2024. https://akasa.com/press/genai-impact-medical-coding-operations
52. AKASA, press release, 14 Mar 2024. https://akasa.com/press/akasa-launches-authorization-advisor
53. HealthcareDealHub (citing Axios), 6 Aug 2026. https://healthcaredealhub.com/news/datavant-acquires-smarterdx-6hax
54. Octus, 9 Sep 2026. https://octus.com/resources/articles/kkr-and-neuberger-berman-provide-2-7b-to-support-merger/
55. HIT Consultant, 19 May 2026. https://hitconsultant.net/2026/05/19/commure-secures-70m-to-drive-85-autonomous-revenue-cycle-execution/
56. Sixth Street, 22 Jul 2026. https://sixthstreet.com/investment_announce/candid-health-raises-120m-led-by-sixth-street-growth-to-fuel-autonomous-revenue-cycle-management-in-healthcare/
57. HIT Consultant, 31 Oct 2023. https://hitconsultant.net/2023/10/31/olive-shutters-business-after-sale-to-waystar-and-humata-health/
58. Axios, 5 Apr 2022 (Wayback Machine snapshot). https://web.archive.org/web/20240520160349/https://www.axios.com/2022/04/05/health-startup-olive-costs-savings
59. HFMA (David W. Johnson), 21 Mar 2025. https://www.hfma.org/finance-and-business-strategy/a-case-study-in-todays-revenue-cycle-dystopia/
60. FinSMEs, 18 Jul 2024. https://www.finsmes.com/2024/07/thoughtful-ai-raises-20m-in-funding.html
61. Healthcare Dive, 21 May 2025. https://www.healthcaredive.com/news/new-mountain-capital-creates-ai-revenue-cycle-management-company-smarter-technologies/748748/

## Fact-check notes

- Summary: Thoughtful AI is no longer called a failure. Its stand-alone service ended inside Smarter Technologies, the parent it shares with SmarterDx, and [11] puts that down to portfolio strategy.
- Legacy, KLAS: "at the end of 2025" changed to "in 2025". The data covers all of January to December 2025 [14].
- Legacy, Solventum: "sells $1.4B a year" now reads as annual sales. Added that the separation could be a spinoff or a combination with a peer [17].
- Legacy, HFMA survey: "AKASA commissioned" changed to "run with AKASA". HFMA and AKASA ran it together [19].
- Legacy: "about 50,000 words" changed to "nearly 50,000 words", as in [21].
- Origin: [25] says Walaliyadde "led healthcare investments" and helped "build" a16z's healthcare team. The draft said he was a partner who helped "start" it.
- Origin: Ganapathi is now described as founding CTO. He is listed as an advisor today [50].
- Origin, COVID: changed to "strained teams and forced staff cuts", which matches [24] and [28].
- First wedge: cut "later extended to authorization status". Neither [6] nor [30] mentions it.
- First wedge: the product returned results "to the EHR". [30] does not name Epic as the place results were written.
- First wedge: "read-only" changed to "changes no claim or payer data". [31] says claims still move between work queues.
- First wedge, 2024 reviewer: [7] (June 2024) is a coding assistant that coders accept or revise. [22] gives no date for the reviewer, and its prebill framing comes from [1]. The sentence now separates the two products.
- First wedge: the academic center's revenue cycle team is "more than 400" people, not 400 [32].
- Customers, Sutter: changed to "its largest customer whose leaders endorsed" Alpha Health. [5] does not name its digital and revenue cycle leaders.
- Customers, Montage: cut "and authorization work". The case study covers only claim status, payers and the medical group [30].
- Funding table: the seed of about $5M is now derived from the $25M total in [5], not marked as inferred.
- Funding table: "Series C" renamed "unnamed round". TechCrunch [34] does not name the series.
- Scale, Cleveland Clinic: [1] says AKASA "processes" 100% of the Clinic's enterprise inpatient volume. The draft said it "reviews 100% before billing".
- Hard, BCBSA: the period is 2023 to 2025, not 2024 and 2025 [43]. BCBSA's claims-based analysis did not prove AI caused the increase.
- Hard, GAO: GAO-26-109116 is a "Science & Tech Spotlight", not a review.
- Hard, Walaliyadde [22]: "coded poorly" changed to "fell short". "Never shipped at scale" changed to "never commercialized at scale", closer to his words.
- Hard, Epic [47]: "emergency" changed to "emergency medicine", and "in development" to "planned". This wording follows the source more closely.
- Hard, Keeler: changed to say Toolbox apps are subject to Epic's non-compete provisions, as [49] puts it.
- Hard, funding: the draft compared a full-year figure ($29B, 2021) with one quarter ($2.5B, Q3 2023) as if they were the same measure. Both periods are now named.
- Hard, headcount: the 244 to 97 drop is now attributed to Great Place To Work counts. Added that Tracxn still estimates 247.
- Hard, workforce: [51] says "replacing coders with technology". [8] says the product is "designed to" run with no human intervention.
- Strategy: [8] says AI matched or beat human coders. That result is now stated.
- Strategy: "replaces coder hours, rules-based CAC and offshore coding [2][3]" is now marked as inferred. [2] says neither, and [3] describes the market, not AKASA.
- Strategy, SmarterDx: the growth to about $150M is now counted from New Mountain's purchase, not "in a year" [53]. "Merging into Datavant" changed to "merging with Datavant" [54].
- Strategy, Commure: added the $70M amount [55].
- Strategy, Candid: the quote is now "AI added on top of legacy systems has yet to deliver". The draft's "has not delivered" overstated [56].
- Strategy, Olive: "much of its AI" changed to "often", as in [59]. The shutdown date is the end of October 2023, citing [57] alongside [10].
- Strategy, Thoughtful: [12] does not say its bots drove practice-management screens. It reports a competitor saying CentralReach shut down unsanctioned bots, Thoughtful's among them. Also noted that Thoughtful and SmarterDx share a parent.
- Copy #2: "before contract" changed to "before full rollout". [2] says value shows before formal rollout.
- Copy #3: "emergency" changed to "emergency medicine". "Ambulatory fee codes" changed to "ambulatory professional fee codes".
- Copy #5: "Payers now attribute $942M" changed to "a payer group links $942M". BCBSA did not prove causation.
- Open questions: "Series C" changed to "2024 round" to match the table.
- Style: the draft had no em dashes or banned hype words. Clauses joined with semicolons and long sentences were split into shorter ones and short lists.
- Not verified: the Axios original [58]. Web Archive was blocked, so I relied on search snippets of the Axios piece, which agree with the claim.