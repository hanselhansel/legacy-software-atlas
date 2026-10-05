# Student information systems

Slug: `student-information`

## Systems

- Ellucian Banner (SCT Banner; Oracle DB, Oracle Forms/PL-SQL, on-prem since the 1980s, now moving to Banner SaaS)
- Ellucian Colleague (Datatel; UniData/Envision/UniBasic multivalue stack)
- Ellucian PowerCampus (SunGard)
- Oracle PeopleSoft Campus Solutions (Student Administration, first deployed 1998-99)
- Jenzabar CX/EX/PX/QX (acquired CARS, Poise/Campus America, Quodata products) and SONIS
- Tribal SITS:Vision (UK/Commonwealth HE, since 1991)
- Tribal Callista (Australian university consortium SMS)
- Tribal ebs (UK further education)
- ESS SIMS (formerly Capita SIMS; English schools, since 1984; Windows client-server on SQL Server)
- PowerSchool SIS (K-12; US/Canada)
- TechnologyOne StudentOne / Student Management (AU, from 1992)
- Home-grown or locally built SIAKAD academic systems reporting to PDDikti Feeder (Indonesia)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The dominant cores date from 1979-1998. Colleague signed its first client in 1979. SITS:Vision has existed since 1991. SIMS was in schools from 1984 and is still a client-server app on SQL Server with legacy Windows API components. PeopleSoft Student Administration first deployed in 1998-99. Tribal's FY2024 report says fewer than a third of SITS customers run on Tribal Cloud, so most still run it on-prem. Exeter, for example, ran SITS on-prem for 24 years before moving in 2024. ([source](https://www.tribalgroup.com/hubfs/Tribal%20Group%20plc%20AR24_Low%20Res_V1.pdf))
- **S2 slow to replace**: met. Lehigh's move from on-prem Banner to Banner SaaS kicked off in fall 2024 and is planned as a five-year program. A Higher Ed Intel analysis says ERP modernization usually takes 3-7 years, and large deals run 7-15+ years: WashU's Workday program spans at least 7 years and costs $265M, and MHEC signed a 15-year Oracle agreement for 2025-2040. Tribal told Callista customers in 2015 that support would last only seven years. Ten universities then extended it again in 2021 with a 5-year A$55M agreement. ([source](https://its.lehigh.edu/banner-saas-transition-driving-innovation-future-ready-lehigh))
- **S3 workarounds**: met. EdTech Magazine (Mar 2026) describes shadow data in US higher ed: faculty download class rosters to manage grades offline, and administrative staff export student information to spreadsheets for reporting, outside the SIS. In Indonesia, institutions must report to the PDDikti Feeder. SEVIMA sells SIAKAD as Feeder-integrated so that reporting 'won't overwhelm' campuses, which implies manual reporting without it. That is weaker, vendor-sourced evidence. ([source](https://edtechmagazine.com/higher/article/2026/03/shadow-data-higher-education-governing-unsanctioned-data-it-becomes-ferpa-problem-perfcon))
- **S4 shrinking skills**: met. This is moderate evidence, not COBOL-grade. Tribal's FY2024 annual report says SMS customers carry technical debt and unmodernised integrations, worsened by 'challenges in finding and retaining resources to mitigate these risks.' Colleague runs on niche multivalue skills (UniData, Envision, UniBasic), and postings ask for 4-6+ years of Colleague-specific experience (search results only, not opened). Banner needs Oracle PL/SQL and Forms, which are not scarce. EDUCAUSE 2024 data shows a general higher-ed IT hiring squeeze: only 56% of leaders say they can hire into existing roles. ([source](https://www.tribalgroup.com/hubfs/Tribal%20Group%20plc%20AR24_Low%20Res_V1.pdf))

## Segments

Enterprise and government buyers dominate, plus mid-market private colleges. Higher ed: large public and research universities run Banner, PeopleSoft Campus Solutions or SITS:Vision. Smaller privates and community colleges run Colleague, Jenzabar or PowerCampus; Jenzabar holds 20% of institutions with 1,000-2,499 students. K-12 is a public-sector (government) segment: PowerSchool covers 90+ of the 100 largest US districts and 38 state/province-wide contracts, and English state schools are moving off SIMS. In SE Asia, Indonesia's 4,400+ institutions are mostly small private campuses (SMB-scale buyers) running local SIAKAD systems that report to the government PDDikti Feeder.

## Reasons buyers stay

- Replacement is a 3-7 year, high-risk program (Lehigh plans five years for Banner SaaS alone), and it has to fit around the fixed academic calendar.
- Decades of local customization, regulatory reporting (IPEDS, HESA/OfS returns, DfE census, PDDikti Feeder) and financial-aid logic are embedded in the old core.
- Failed implementations are costly. Tribal settled its dispute with NTU Singapore in 2024 after the SITS contract was terminated, and the settlement plus legal costs came to £3.0m.
- Vendors keep extending legacy support. Oracle committed PeopleSoft support to at least 2037, and the Callista universities extended support again in 2021 even though Tribal had said in 2015 that support would last only seven years.
- Incumbents offer a lift-and-shift path to vendor-hosted cloud (Banner SaaS, Tribal Cloud) that keeps the same data model and avoids a re-platform.
- Integrations with LMS, CRM, finance and HR all depend on the SIS schema.

## Notes

1. Market events. The UK schools market shows the clearest legacy-to-cloud flip. SIMS fell from about 83-85% share a decade ago to 31.7% of English state schools in Oct 2025, while Arbor rose to 44% and Bromcom to about 16%. The CMA looked at SIMS switching barriers in 2024. In HE, Tribal (SITS, Callista, ebs) agreed in Sep 2026 to sell its businesses to Main Capital Partners-backed Thames Bidco. The offer was £189.3M, raised to £231.2M, with a shareholder meeting expected 2 Oct 2026. A US education-software provider was reported to be weighing a rival bid. This is from search results only, and the primary RNS was not opened. Ellucian is pushing Banner and Colleague customers to Banner SaaS and 'Ellucian Student'. This is incumbent-led migration, not displacement.

2. Data gaps.
- No opened source gave Banner's exact first-ship year or a PeopleSoft Campus Solutions customer count.
- AISHE's PIB release, PDDikti, CHED's statistics page and TEQSA's register could not be opened (403, cert error, timeout), so secondary sources or a snippet are flagged in buyer_universe.
- The Singapore count excludes the 6 autonomous universities.
- The Malaysia count is private HEIs only.
- US K-12 districts (PowerSchool's market) are not counted.

3. Strength of the legacy signs.
- S4 is the weakest. Only Colleague's multivalue Envision/UniBasic stack is truly niche. Banner's Oracle PL/SQL skills are common. The evidence is Tribal's own report that SMS customers struggle to find and retain staff.
- S3 evidence is general higher-ed shadow-data practice, not specific to one system.
- In SE Asia (ID, VN, TH, PH), the legacy base is mostly home-grown or local-vendor academic systems built for government reporting (PDDikti Feeder in Indonesia), not the US/UK incumbents. Tribal does serve Malaysia from a Kuala Lumpur delivery centre.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
