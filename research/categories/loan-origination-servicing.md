# Loan origination and servicing

Slug: `loan-origination-servicing`

## Systems

- ICE (formerly Black Knight) MSP mortgage servicing system: z/OS mainframe, COBOL batch and CICS
- ICE Encompass (formerly Ellie Mae) mortgage loan origination system
- Finastra Loan IQ (formerly IQ Financial Systems / Misys) commercial and syndicated loan servicing
- FIS Commercial Loan Servicing (formerly ACBS) commercial loan system
- Sagent LoanServ (formerly Fiserv Lending Solutions) mortgage and consumer loan servicing
- Nucleus Software FinnOne / FinnOne Neo retail and SME lending (APAC, India)
- Loan modules in core banking systems from FIS, Fiserv, Jack Henry and CSI (US community banks)
- In-house servicing systems such as Ocwen's REALServicing

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. PennyMac's 2019 complaint, filed as an SEC exhibit, says MSP 'was first developed over 50 years ago' and runs on outdated interfaces connected to a mainframe with batch back-end processing. MSP held 63% of US first-lien loans in 2022 (Black Knight 10-K). Other cores also predate 2005: Loan IQ (bought by Misys in 2004 with 29 clients), FinnOne (late 1990s) and ACBS (1990s). ([source](https://www.sec.gov/Archives/edgar/data/1745916/000110465919060273/a19-22055_1ex99d2.htm))
- **S2 slow to replace**: met. Black Knight FY2022 10-K: contracts for software and hosting solutions 'typically span five to seven years'. Deferred contract costs are amortized over 5 to 10 years, and the risk factors cite 'the time and expense associated with switching'. Replacements take years. PennyMac's in-house replacement of MSP was a multi-year program, 2011 to 2019. Newrez will start moving about 4M loans to ValonOS only in 2027 (National Mortgage News). The FTC 2023 complaint cites lenders' 'high switching costs, lengthy switching timelines' for LOSs. ([source](https://www.sec.gov/Archives/edgar/data/1627014/000155837023002252/bki-20221231x10k.htm))
- **S3 workarounds**: met. In its 2017 suit against Ocwen, the CFPB alleged that the REALServicing platform produced errors through 'system failures and deficient programming'. It said Ocwen's manual workarounds 'often failed to correct inaccuracies and produced still more errors'. A UK lender-sector survey (Kani 2025, cited by kennek) found 56% of 250 payments and lending firms still use manual, spreadsheet-based reconciliation. That survey is secondary and covers reconciliation, not origination. No primary survey that quantifies spreadsheet use in loan origination was found. ([source](https://consumerfinance.gov/about-us/newsroom/cfpb-sues-ocwen-failing-borrowers-throughout-mortgage-servicing-process))
- **S4 shrinking skills**: met. ICE is hiring Senior Mainframe Developers in Jacksonville, FL for MSP. The role needs 8+ years of z/OS COBOL Batch and CICS, JCL, VSAM/DB2 and ISPW on mortgage-servicing applications. The post lists 'Claude Code knowledge/experience' as a plus. On scarcity, BizTech (2025) reports that 71% of IT leaders say mainframe teams are understaffed and that COBOL experts are retiring as universities stop teaching the language. ([source](https://freehire.me/jobs/senior-mainframe-developer-intercontinental-exchange-holdings-inc-mbjskvl3))

## Segments

All four segments use these systems, split by product. Enterprise: MSP serviced 63% of US first-lien mortgages in 2022, and Loan IQ claims about 70% of global syndicated loan volume and 9 of the top 10 agent banks. Mid-market: Encompass is the default LOS for independent mortgage lenders and banks (40%+ share per the FTC), and FinnOne serves mid-size banks and NBFCs across India and Southeast Asia (200+ institutions). SMB: US community banks and credit unions mostly service loans in the modules of their core vendors (FIS, Fiserv, Jack Henry, CSI). CCG Catalyst says these 'support most commercial loans' but lack flexibility for complex credits. Government: ICE says housing agencies use MSP alongside banks, mortgage companies and credit unions (mortgagetech.ice.com/solutions/servicing). Government-sponsored lenders such as Thailand's SFIs and Malaysia's DFIs are also buyers, but no source naming their specific systems was found.

## Reasons buyers stay

- Contracts typically run 5 to 7 years, and conversion costs are amortized over 5 to 10 years (Black Knight FY2022 10-K)
- Switching is 'a significant undertaking' with lengthy timelines. ICE itself estimated the first-year cost of switching LOS for a lender (FTC complaint).
- Investor and regulator reporting (GSEs, Ginnie Mae, CFPB servicing rules) is already built into incumbent systems. A rebuild risks compliance errors, as the CFPB's Ocwen case shows.
- Ecosystem lock-in: ancillary services (PPE, default, data) are integrated with the incumbent LOS or servicing system, and the FTC says assembling them is a barrier to entry
- Network effects in syndicated lending: agent banks and the counterparties they serve are all on Loan IQ
- Data conversion risk for millions of borrower accounts. Ocwen still had 15% of a ResCap transfer unverified 3 years later.
- Big-bank migrations are multi-year programs (PennyMac 2011 to 2019; Newrez to Valon starting in 2027)

## Notes

The strongest primary evidence is in US mortgage servicing. Black Knight's FY2022 10-K gives MSP's 63% first-lien share and 5 to 7 year contracts. PennyMac's SEC-filed complaint describes MSP as a 50-year-old mainframe system, and ICE job posts confirm COBOL/CICS on z/OS. Gaps: (1) Finastra pages returned 403, so the Loan IQ share comes from SourceForge's copy of vendor claims. The 2004 acquisition facts come from search snippets (Finextra returned 403). (2) The ACBS 1991/1993 dates are from search snippets, because LANSA returned 403. (3) No primary survey quantifying spreadsheet use in origination was found. S3 rests on the CFPB's Ocwen allegations. (4) The India count is the RBI FSR stress-test sample, not a full register, and the about 9,000 NBFCs figure is unverified. (5) The EU count covers the euro area SSM only. (6) The Malaysia list is BNM's list hosted on Affin's site, undated (BNM's own pages render with JavaScript). (7) No primary evidence names which legacy systems Southeast Asian banks run beyond FinnOne's claim of 50+ countries. Job-post and tender searches using the terms above are the suggested next step. MSP is a 1960s-era mainframe, but Encompass (2000s, client-server, now cloud) only weakly meets S1. The category's legacy core is servicing more than origination.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
