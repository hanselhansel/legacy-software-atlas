# Payroll and HR administration

Slug: `payroll-hr`

## Systems

- SAP ERP HCM / SAP HR & Payroll (R/3, ECC 6.0), with country payroll versions
- Oracle PeopleSoft HCM (HRMS)
- Oracle E-Business Suite HRMS / Payroll (e.g. NHS ESR)
- Infor Lawson S3 HR/Payroll (ex-Lawson Software)
- UKG (Kronos) Workforce Central time and attendance, on-prem
- ADP legacy in-country and global payroll platforms (ADP iHCM, ADP Global Payroll), being moved to ADP Lyric / Workforce Now
- In-house COBOL mainframe government payroll (e.g. California Uniform State Payroll System, Colorado CPPS)
- IBM AS/400 (IBM i) payroll applications at municipalities and mid-market firms
- Spreadsheet-based payroll (Excel) at SMBs

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Every dominant core was built before 2005. SAP R/3 shipped in 1992 as three-tier client/server with HR/payroll as a core module. PeopleSoft HRMS v1 shipped in 1989 as client-server. Lawson began as mainframe software for Burroughs/IBM. Public-sector payroll is still mainframe: California's Legislative Analyst's Office says the state payroll systems were developed more than 30 years ago, and the State Controller describes its mainframe technology as stable but hard to staff. ([source](https://lao.ca.gov/Publications/Report/3590))
- **S2 slow to replace**: met. NHS England and Wales: the Oracle-based ESR, which pays about 1.9 million staff, is being replaced under a 15-year, £1.4bn Infosys contract. Infosys takes over by Aug 2026 and ESR support ends in 2035. California: the CSPS replacement is estimated at $1.2bn over about 6 years, completing Sept 2031, after the earlier 21st Century/MyCalPAYS attempt (started 2006) was cancelled in 2013 (https://lao.ca.gov/Publications/Report/5011). SAP ERP HCM customers get maintenance to 2027/2030 and H4S4 to 2040, which lets on-prem payroll run for years more. ([source](https://www.publictechnology.net/2025/11/13/health-and-social-care/nhs-sheds-light-on-plans-for-1-4bn-hr-system/))
- **S3 workarounds**: met. City of Killeen (TX) FY2013 payroll audit: departments keep time on paper timecards and key it by hand into the AS400 payroll system each pay period. Finance then recalculates each employee's paycheck in a spreadsheet and compares it with the AS400 result. Supporting evidence: Strada's 2024 poll of 271 companies in 42 countries found 51% still rely on spreadsheets to process payroll (vendor survey, https://stradaglobal.com/insights/why-do-companies-rely-on-spreadsheets-in-payroll-processing/). HHS said in April 2026 that replacing its COBOL payroll automated tasks that took up to six hours of manual effort (https://www.nextgov.com/modernization/2026/04/hhs-replaces-cobol-based-payroll-system/412723/). ([source](https://killeentexas.gov/ArchiveCenter/ViewFile/Item/148))
- **S4 shrinking skills**: met. California LAO (2017): the State Controller's Office reported trouble hiring staff with the technical expertise to maintain and operate the mainframe technology behind the payroll system for about 260,000 employees. InfoWorld (2008) on the same COBOL payroll: COBOL programmers are increasingly hard to find (https://www.infoworld.com/article/2291870/california-s-cobol-conundrum.html). Skills scarcity is documented for public-sector mainframe payroll. It is not documented for SAP/PeopleSoft skills in the sources read. ([source](https://lao.ca.gov/Publications/Report/3590))

## Segments

Government and enterprise run the heaviest legacy cores. US state payroll is mainframe/COBOL: California pays about 260k employees on 30-50-year-old systems, and Colorado's CPPS dates from 1986 (no source was opened for Colorado). US federal: HHS replaced a COBOL payroll in 2026. UK health: NHS ESR on Oracle EBS pays 1.9m staff. AU state health: Queensland's SAP payroll replaced LATTICE in 2010. Large enterprises and higher education run SAP ERP HCM, PeopleSoft and Infor Lawson (Workday says it serves 65%+ of the Fortune 500, which marks the migrated tier). Mid-market runs on-prem or hosted payroll (AS/400 apps, Kronos WFC, ADP Workforce Now with 90k+ clients). SMBs mostly use spreadsheets or bureau services: a 2024 vendor poll found 51% using spreadsheets, and ADP RUN serves SMBs. In SEA and India, enterprises often run SAP HCM country versions, while SMBs use spreadsheets or local SaaS (Talenta, Sprout, Base.vn).

## Reasons buyers stay

- Payroll is mission-critical and has zero tolerance for error. Queensland Health's 2010 SAP payroll go-live underpaid or failed to pay about 78,000 staff and cost about AUD 1.2bn, which makes buyers very risk-averse.
- Deep local statutory logic (tax, social security, awards and union agreements, e.g. PPh 21/BPJS in Indonesia, Australian awards) is embedded and tested in the old system.
- Vendors keep extending support (SAP HCM to 2030 and H4S4 to 2040; PeopleSoft rolling to at least 2036), which removes any forcing deadline.
- Replacement is a reimplementation, not an upgrade (e.g. Kronos WFC to UKG Pro WFM), and needs parallel payroll runs and data migration.
- Public-sector procurement cycles and long managed-service contracts (NHS ESR: 15 years) lock incumbents in.
- Integration with GL, time and attendance, pensions and benefits, and banks.

## Notes

Coverage gaps and caveats:
(1) Vendors do not disclose install counts for on-prem SAP ERP HCM, PeopleSoft HCM, Oracle EBS HRMS, Lawson or Kronos WFC. Only ADP (1.1M clients) and Workday (11.5k customers) disclose counts.
(2) Support dates are from secondary pages, because the Oracle and SAP primary pages returned 403. SAP HCM: 2027 mainstream, 2030 extended, H4S4 to 2040 (search summary of SAP Community and Rizing). PeopleSoft: rolling to at least 2036 (https://www.peoplesoftexcellence.com/blog/oracle-extends-peoplesoft-support-up-to-2036).
(3) S3 primary evidence is a 2013 municipal audit (AS400 plus spreadsheet recalculation). The 51% spreadsheet figure comes from a vendor poll, not a regulator.
(4) S4 evidence is from US public-sector mainframe payroll (California LAO 2017, InfoWorld 2008). No sourced evidence was found for scarce SAP HCM or PeopleSoft skills, or for SEA/India legacy payroll skills.
(5) Buyer-universe sources: the India figure is a secondary summary of MCA data (MCA pages unreachable). The Indonesia figure is SE2016 via news coverage (BPS site redirected), and it counts mostly micro and informal units. The PH figure is PSA data tabulated in a BSP deck. The VN figure is NSO data via VietnamPlus. The US census page I opened did not show the headline firm count; the 5.52M figure came from a search snippet citing SUSB.
(6) Colorado CPPS (1986 mainframe/COBOL) and Queensland Health (LATTICE to SAP, AUD 1.2bn) appear in search results, but their primary pages could not be opened or were only read via secondary sources (Wikipedia/iTnews summaries). Treat them as corroborating, not cited.
(7) I could not verify Warp (AI-native US payroll, reported $18M Series A, 2025), because its source pages returned 404/403, so it is left out of the challengers.
(8) ADP and Workday are both incumbents and modernizers. ADP is moving clients off iHCM and legacy platforms to Lyric HCM.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
