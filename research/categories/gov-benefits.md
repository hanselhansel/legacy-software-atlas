# Government benefits and social security

Slug: `gov-benefits`

## Systems

- In-house COBOL mainframe benefit systems (US SSA: over 60 million lines of COBOL as of 2010)
- State unemployment insurance (UI) mainframe systems from the 1970s and 1980s, mostly COBOL (US)
- Centrelink ISIS (Income Security Integrated System) on Rocket/CCA Model 204 (Australia)
- DWP ICL/Fujitsu VME mainframe benefit suite (JSAPS, Pension Strategy Computer System launched 1988), COBOL from the 1980s (UK)
- Deutsche Rentenversicherung rvSystem/rvDialog, COBOL on z/OS mainframes (Germany)
- IBM/Merative Cúram Social Program Management (client-server/Java SPM suite, 1990s origin)
- Deloitte-built state integrated eligibility systems for Medicaid and SNAP (US)
- CPF Board COBOL mainframe applications (Singapore, partly modernised to Java under BEACON from 2018)
- EPFO Field Office Application Software, decentralised regional databases (India, replaced by CITES 2.01 in 2026)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. SSA runs its core retirement and disability workloads on COBOL, with over 60 million lines as of June 2010 (SSA OIG A-14-11-11132). Centrelink ISIS is a mainframe system about 40 years old that hard-codes the payment rules, runs on Model 204 (first deployed 1972) and handles about 62 million transactions a day. DWP's Pension Strategy Computer System launched in 1988 and still runs the live State Pension caseload (NAO 2021). GAO-23-105478 found state UI systems ranging from 7 to about 50 years old. ([source](https://oig-files.ssa.gov/audits/full/A-14-11-11132_0.pdf))
- **S2 slow to replace**: met. UK: in 2010 DWP planned to move 8 million households to Universal Credit by 2017. The NAO (Feb 2024) says completion will be at least six years later than planned, with some migration running to 2028. Australia: WPIT was a seven-year program (2015-2022, about A$1.5B). By June 2020 only 13% of ISIS had been decommissioned. The A$191M entitlements engine replacement was scrapped in 2023. The Model 204 licence ran under a 2003-2014 deal worth A$98.5M, then a three-year A$35.1M extension. DWP's VME re-platforming ran 2016-2021. ([source](https://www.nao.org.uk/wp-content/uploads/2024/02/progress-in-implementing-universal-credit-report.pdf))
- **S3 workarounds**: met. NAO (Sept 2021) on 134,000 underpaid State Pensions: administration 'has limited automation'. Caseworkers pull information from different IT systems and copy it across by hand, and must set timed prompts on the system manually. DWP then had to review about 273,000 cases by hand. ANAO/iTnews: Services Australia has no documentation of the age-pension business rules hard-coded in ISIS, and staff had little training on manual recalculation. ([source](https://www.nao.org.uk/wp-content/uploads/2021/09/Investigation-into-underpayments-of-State-Pension.pdf))
- **S4 shrinking skills**: met. SSA OIG (2012) recommended that SSA's human capital plan 'address the loss of COBOL programmers' and keep COBOL expertise as legacy programmers retire. GAO-25-107795 says COBOL and assembly have 'a dwindling number of people available with the skills', and that agencies may pay a premium for staff or contractors. An ANAO audit (reported by iTnews) flagged that Model 204 skills are running down as experienced Centrelink staff leave. ([source](https://oig-files.ssa.gov/audits/full/A-14-11-11132_0.pdf))

## Segments

Almost entirely government. National social security and pension agencies are the main buyers: SSA, DWP, Deutsche Rentenversicherung, Centrelink, CPF, EPFO, BPJS, VSS, SSO, SSS and EPF. In the US, state agencies are a large second tier: 56 Medicaid programs and 53 UI programs, with 25 states on Deloitte eligibility contracts. Counties and cities also buy (Cúram at Clark County NV, Sonoma County and NYC; UK local authorities for Housing Benefit). A small private-sector edge exists: employers using filing software such as VNPT-BHXH in Vietnam, and health plans and providers on social-care networks such as Unite Us. No SMB or mid-market buyers of the core systems were found.

## Reasons buyers stay

- Payment rules are hard-coded and undocumented. Services Australia has no documentation of the age-pension business rules inside ISIS, so moving them is risky (ANAO via iTnews).
- Replacements have failed or slipped. Australia scrapped a A$191M entitlements engine in 2023 because it ran slower than Model 204. Universal Credit is at least 6 years late.
- Errors in benefit payments are politically costly. Deloitte system rollouts brought backlogs (Kentucky: 50,000 cases, 600+ defects) and wrong notices (KFF Health News).
- The old cores are stable and pay out at huge scale: DWP about USD 202B a year, ISIS about 62M transactions a day. Rehosting COBOL (DWP VME-R, DRV Baden-Württemberg, CPF BEACON) is often preferred to a rewrite.
- Benefit rules change every year by statute, so agencies have to keep paying while they migrate, which forces long parallel running.
- Procurement and funding cycles (federal matching funds, multi-year budgets) favour large incumbent integrators.

## Notes

Evidence is strongest for the US, UK, AU, DE and SG. Primary sources: SSA OIG 2012 (60M+ lines of COBOL); GAO-23-105478 (state UI systems 7 to 50 years old); GAO-25-107795 (dwindling COBOL skills); NAO 2021 and 2024 (State Pension system from 1988 with manual copying between systems; Universal Credit at least 6 years late); ANAO via iTnews (ISIS on Model 204, WPIT decommissioning shortfall). The Bundesrechnungshof report 'Deutsche Rentenversicherung im Wettlauf gegen die Zeit' (Dec 2023, https://www.bundesrechnungshof.de/SharedDocs/Downloads/DE/Berichte/2023/hauptband-2023/10-volltext.pdf?__blob=publicationFile&v=6) flags long-delayed modernisation of the shared pension data centre (DSRV). Only the landing summary was readable. For ASEAN and India, no public source was found that names the legacy core technology at BPJS, VSS, SSO, SSS/GSIS or KWSP/PERKESO. What was found: Thailand's SSO held a public review of its roughly 850M baht IT budget in Jan 2026 (https://thestandard.co/social-security-it-budget-review/), and India's EPFO finished moving 34 crore accounts from 120+ regional databases to CITES 2.01 in July 2026. Treat S1-S4 for SEA as unverified. Most challengers are overlays (access, payments, referrals) or integrators, not core replacements. No AI-native startup with funding was found replacing a national benefits core. Checkr has floated AI eligibility verification but has no government customers ('still conceptual', Yahoo Finance), so it is excluded. Vendor customer counts are scarce. Cúram's '80+ agency customers' (IBM, 2011) appeared only in search snippets and was not confirmed from a page opened. The S1 and S4 source PDF (SSA OIG) was read through a local text extraction. The NAO Universal Credit PDF was fetched with curl and text-extracted.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
