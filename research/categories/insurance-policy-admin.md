# Insurance policy administration

Slug: `insurance-policy-admin`

## Systems

- DXC (ex-CSC/PMSC/Mynd) Series II / Series III PMS (P&C policy management system, z/OS mainframe, 1970s-1980s)
- DXC CyberLife (life, z/OS mainframe, first released 1995 by Cybertek)
- DXC VANTAGE-ONE (life and annuity, mainframe; MassMutual a named user)
- DXC SMART400 family on IBM AS/400: POLISY/400, LIFE/400, GROUP/400, and the Asia variants LIFE/Asia, POLISY/Asia, GROUP/Asia (RPG/COBOL on IBM i; widely used by insurers in Asia)
- DXC Assure Integral and Assure Ingenium (multiline/life PAS)
- Infosys McCamish VPAS (life and annuity PAS plus BPO, US)
- Sapiens ALIS, IDIT, CoreSuite
- Majesco (now with Cover-All, InsPro) policy admin suites
- Guidewire InsuranceSuite / PolicyCenter (first shipped 2006, Java; modern-era, but now the incumbent many carriers moved to)
- Duck Creek Policy (P&C)
- TCS BaNCS for Insurance (life, P&C, health; strong in India, AU, UK)
- eBaoTech LifeSystem / GeneralSystem (Java core, Asia)
- Home-grown COBOL/mainframe and RPG/AS400 policy systems

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Several dominant policy admin cores were first shipped well before 2005 on mainframe or midrange:
- DXC Series II (PMS) was first developed by Seibels Bruce in the 1970s and runs on z/OS.
- CyberLife was first released in 1995 and runs on z/OS (lookupmainframesoftware).
- PMSC's mainframe Series III was built in the late 1980s and had 63 insurer customers by 1992 (referenceforbusiness).
- Celent says the AS/400-based SMART400 systems (Polisy/400, Life/400, Group/400) are still in use today. ([source](https://www.lookupmainframesoftware.com/soft_detail/dispsoft/2696))
- **S2 slow to replace**: met. Vendor filings show long contracts:
- Guidewire's 10-K (FY2025): initial subscription agreements are generally five years, and some customers sign initial terms of seven years or longer. Customer evaluation cycles are often extensive.
- Majesco's 10-K (2019): fees are typically under multi-year agreements of five to seven years.
- Sapiens' 20-F (2024): the sales cycle is typically one to two years, and delivery takes several months to a few years.

A DXC case study describes a life insurance data migration from 17 source systems (some up to 40 years old) that took 3 years. ([source](https://www.sec.gov/Archives/edgar/data/1528396/000152839625000221/gwre-20250731.htm))
- **S3 workarounds**: met. Pace (an AI operations vendor whose customers include Prudential, Palomar, Convex and WTW) says its agents work across legacy systems and green-screen interfaces, and 'interface directly with legacy admin systems, mainframes, and desktop apps to execute updates'. In other words, it automates manual re-keying into legacy policy systems. At Palomar, it resolves more than 90% of policy servicing tasks. McKinsey's figure that 30-40% of commercial underwriters' time goes to admin tasks such as rekeying data appeared in search results, but the McKinsey page timed out, so it is not cited here. ([source](https://withpace.com/))
- **S4 shrinking skills**: met. Rocket Software surveyed 276 IT directors and VPs (reported in Digital Insurance). 52% said finding staff familiar with legacy systems development was a significant challenge, and only 35% said their workforce had the needed skills. The article adds that COBOL developers and mainframe specialists who maintain policy and claims cores are retiring. A training vendor's page on LifeAsia (AS/400) notes that fewer professionals today know RPG and COBOL. Job posts for LifeAsia/AS400 developers (SMART/400, COBOL) appear in Kuala Lumpur. ([source](https://www.dig-in.com/opinion/insurance-it-leaders-have-an-ai-infrastructure-problem))

## Segments

Legacy policy admin systems sit mainly with enterprise and mid-market carriers:

- **Enterprise:** Duck Creek's 10-K names Progressive, Liberty Mutual, AIG, The Hartford and GEICO as customers. It also says many carriers run home-grown legacy systems that are "costly and inefficient to maintain". DXC says 21 of the top 25 global insurers use its systems. MassMutual runs VANTAGE-ONE on DXC.
- **Mid-market:** Majesco's customers include regional insurers and MGAs. Duck Creek lists regional carriers such as UPC, Coverys and Mutual Benefit Group. In Asia, AS/400 LifeAsia/POLISY/Asia installs are common at mid-size life and general insurers (LifeAsia developer job posts in Kuala Lumpur).
- **Government:** state-owned insurers are in each register:
  - LIC of India in the IRDAI lists.
  - Indonesia's mandatory and social insurers in the OJK list (Asuransi Wajib and Asuransi Sosial).
  - National Reinsurance Corporation of the Philippines in the Insurance Commission list.
- **SMB:** small MGAs and insurtechs tend to start on SaaS cores (Socotra, INSTANDA) rather than the legacy systems.

No opened source gave a quantified split by segment.

## Reasons buyers stay

- Reliability and stability for mission-critical processing. Celent cites this as why SMART400/Polisy/400/Life/400 remain in use.
- The need to keep ongoing business running during change (Celent).
- Replacement cost and risk: sales cycles of 1-2 years and delivery of months to years (Sapiens 20-F). Subscriptions run 5-7+ years (Guidewire 10-K, Majesco 10-K).
- Data conversion complexity: one DXC migration moved 719,000 policy records from 17 source systems, some up to 40 years old, over 3 years.
- Long-tail closed books: life and annuity policies stay in force for decades, so old products must keep being serviced.
- Tightly coupled surrounding applications. A MassMutual executive cited apps tightly coupled to DXC platforms as an enabler for rehosting rather than replacing.
- Regulatory reporting and actuarial logic embedded in legacy code, with outsourced AMS contracts. DXC has run application outsourcing for a VANTAGE-ONE annuity block for about 20 years (search snippet).

## Notes

**Gaps and caveats**

- **Federato:** its $100M Series D (Goldman Sachs, Nov 2025, about $180M total per search snippets) is left out of challengers. Businesswire and Reinsurance News both returned 403.
- **McKinsey:** the figure that 30-40% of underwriter time goes to rekeying could not be opened (timeout), so it is not cited for S3.
- **DXC LIFE/Asia family size** (about 125 clients, 34 countries, 65M policies, 2010) comes only from a search snippet. The PropertyCasualty360 page did not render.
- **India:** the IRDAI counts come from Wikipedia (citing IRDAI, 1 Apr 2025). The policyholder.gov.in page did not resolve.
- **Vietnam:** the 85 count is from The Investor, citing the Insurance Supervisory Authority. The non-life and broker breakdown is from a search snippet.
- **US:** only the life count (736) was verified in the NAIC PDF. The P&C (2,000+ companies) and health (1,155) figures came from search snippets.
- **Thailand:** the count is from OIC's 2021-2025 development plan, not a current register snapshot.

**Mixed signals**

- Guidewire, Duck Creek, Majesco and Sapiens are now themselves incumbents with 5-7+ year contracts. Their products post-date 2005, so they do not meet S1. The true pre-2005 legacy cores are the DXC mainframe and AS/400 families (Series II/III, CyberLife, VANTAGE-ONE, SMART400/LifeAsia/POLISY Asia), Infosys McCamish VPAS, and home-grown COBOL/RPG systems.
- In SE Asia (MY, SG, ID, VN, TH, PH), the AS/400 LifeAsia/POLISY/Asia install base is the most useful target signal. Job ads asking for SMART/400, COBOL and RPG are a practical way to find buyers.

**Primary sources used:** SEC 10-K/20-F filings, NAIC, PRA CSV, MAS FID, APRA, OJK, PIDM, IC Philippines, OIC.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
