# Government tax administration

Slug: `gov-tax`

## Systems

- IRS Individual Master File (IMF) and Business Master File (BMF): IBM-built 1960s mainframe, COBOL and Assembly (US)
- IRS CADE 2 (replacement program for IMF, in build since 2010)
- FAST Enterprises GenTax (COTS integrated tax system, 60+ agencies, US states and abroad)
- SAP ECC 6.0 based tax platforms, e.g. HMRC Enterprise Tax Management Platform (ETMP), 45+ tax regimes (UK)
- ATO National Taxpayer System (NTS, 1975) and ATO Integrated System (AIS, 1994), partly replaced by Accenture-built Integrated Core Processing (ICP) (AU)
- DJP SIDJP (Indonesia core tax system in use since 2002), replaced by Coretax (LG CNS-Qualysoft)
- India Income Tax e-filing and Centralised Processing Centre (CPC 1.0, then CPC 2.0 by Infosys)
- Vietnam GDT TMS centralized tax management application (rolled out 2014-2015, replaced 16 distributed apps)
- Singapore IRAS IRIN (Inland Revenue Interactive Network) integrated system
- In-house mainframe systems at state revenue departments and local property/council tax billing systems

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. IRS Individual Master File relies on core legacy systems installed in the 1960s, written in COBOL and Assembly (CRS). GAO-25-107795 lists two Treasury tax processing systems aged 59 and 51 years on COBOL and Assembly. ATO's National Taxpayer System went live in 1975 and AIS in 1994 (ANAO/IGT). Indonesia's DJP ran its SIDJP core from 2002 until Coretax. ([source](https://files.gao.gov/reports/GAO-25-107795/index.html))
- **S2 slow to replace**: met. IRS Business Systems Modernization has run since the late 1990s; CADE 1 was abandoned in 2009 and CADE 2 began in 2010 with full deployment targeted for FY2028, while key IMF replacement projects were suspended as of May 2024 (CRS). ATO Change Program ran Dec 2003 to June 2010 at A$756.7m and left BAS and Superannuation Guarantee parts undelivered (IGT 2010). HMRC's SAP contract runs to 2035 (The Register). Indonesia's Coretax ran from 2018 regulation to a Dec 2024 build and 2026 handover. ([source](https://www.everycrsreport.com/reports/IF12525.html))
- **S3 workarounds**: met. The IRS still has employees keystroke every digit of paper returns, often hundreds to about 1,000 digits per return. Transcription errors hit about 22 percent of paper returns, and the backlog reached nearly 15 million paper returns in March 2022 (National Taxpayer Advocate). After ICP, the ATO kept legacy core systems that needed data extraction, conversion and synchronisation between multiple systems (ANAO, search summary). ([source](https://www.taxpayeradvocate.irs.gov/news/nta-blog/nta-blog-getting-rid-of-the-kryptonite-the-irs-should-quickly-implement-scanning-technology-to-process-paper-tax-returns/2022/03/))
- **S4 shrinking skills**: met. GAO says both Treasury tax systems run on COBOL and Assembly, languages that have a dwindling number of people available with the skills to support them. It adds that agencies have had difficulty finding employees with such knowledge and may pay a premium for contractors. The two systems cost about $754m a year combined to operate. ([source](https://files.gao.gov/reports/GAO-25-107795/index.html))

## Segments

Government only. Buyers are (1) national tax administrations: IRS, HMRC, ATO, IRAS, DJP, India's CBDT/CBIC, Vietnam's tax department, LHDN/RMCD, Thai Revenue Department, BIR, and the 27 EU national administrations; (2) state and provincial revenue departments: 50 US states plus DC, 8 Australian state revenue offices, 31 Indian state/UT tax departments; (3) local governments collecting property and council tax: 296 English billing authorities, 149 Malaysian PBTs, 500+ Indonesian regions, 1,600+ Philippine LGUs, and US counties and municipalities. The legacy evidence is strongest at the national level (IRS 1960s COBOL/Assembly, ATO 1975 NTS, HMRC systems over 30 years old with 124 legacy systems still in place in March 2024, DJP SIDJP from 2002). FTA says more than 80% of member agencies have started moving off legacy systems. No SMB or enterprise segment exists.

## Reasons buyers stay

- Failed or troubled replacements make agencies cautious: IRS CADE 1 was abandoned in 2009 after cost overruns, the ATO's 2010 ICP rollout caused processing problems and left BAS and SG on legacy, and Indonesia's Coretax drew taxpayer complaints at its 2025 launch.
- Revenue continuity: the systems collect a large share of government revenue (HMRC ETMP handles about GBP 800bn a year), so cutover risk is political.
- Tax law changes every year, and decades of encoded rules in COBOL/Assembly are hard to extract and re-validate.
- Funding is lumpy and political: IRS IRA modernization money may run out by FY2026 and IMF replacement projects were suspended in 2024.
- Procurement and sovereignty constraints: long tenders, single-source awards (SAP's GBP 275m HMRC award), and sovereign-cloud and security accreditation needs.
- Incumbent integrator and COTS lock-in: Aspire-era contracts, GenTax configuration, and maintenance contracts after go-live (LG CNS kept maintenance after the Coretax handover).

## Notes

The category is strongly legacy at the national level. All four signs are met with primary sources: GAO-25-107795 (COBOL/Assembly, scarce skills, systems 51 and 59 years old, $754m a year), CRS IF12525 (IMF from the 1960s, CADE 2 from 2010 to FY2028), the National Taxpayer Advocate (manual keystroking with about 22% transcription errors), and IGT 2010 (ATO Change Program 2003-2010, A$756.7m). HMRC: the NAO via The Register reports 124 of 545 services still on legacy systems in March 2024, some over 30 years old, and SOTF whole-life cost up from GBP 312m to 437m. India CPC 2.0: an 8.5-year duration appears in search snippets but was not confirmed in a page opened; the page opened says Rs4,241.97 crore with an 18-month build. Gaps: no public evidence was opened on the age or language of core systems at IRAS (SG), LHDN/RMCD (MY, though FAST lists Malaysia as a client and RMCD is reportedly a GenTax user), the Thai Revenue Department, or the BIR (PH). Search returned nothing specific for these. OECD Tax Administration 2024 (58 jurisdictions) and IOTA pages returned 403, so the share of COTS versus in-house systems is unsourced. Few true AI-native challengers sell core tax administration. Activity is mostly COTS (FAST, SAP), integrator rebuilds (LG CNS, Infosys, Accenture), AI pilots in taxpayer service and audit selection (California CDTFA genAI sandbox, South Carolina DOR AI audit selection; vendors not verified), and horizontal AI mainframe-migration firms. Consumer and business tax AI startups (April, Numeral, TaxGPT) serve taxpayers, not administrations, and were excluded.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
