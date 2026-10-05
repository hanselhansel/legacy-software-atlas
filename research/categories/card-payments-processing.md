# Card issuing and payments processing

Slug: `card-payments-processing`

## Systems

- Fiserv (ex-First Data/PaySys) VisionPLUS and FirstVision: IBM mainframe, COBOL/CICS/VSAM credit card management system
- Fiserv Optis: North American credit card processing platform (ex-First Data)
- TSYS TS2 / TS1 (Global Payments Issuer Solutions, being sold to FIS): mainframe cardholder processing system
- ACI Worldwide BASE24: HP/Tandem NonStop switch and authorization system for ATM/POS/card
- FIS BASE2000 (Kordoba): mainframe card processing
- HPS PowerCARD: card issuing/acquiring suite (on-prem licensed)
- OpenWay Way4: licensed card issuing/acquiring platform, dominant in Vietnam

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Mphasis identifies TS2 (TSYS, 1994), VisionPLUS (Paysys, 1995) and BASE2000 (FIS Kordoba) as mainframe products built on COBOL, JCL and Assembler, with VSAM/DB2/IMS data stores and CICS. VisionPLUS descends from CardPac (1982). ACI history dates BASE24 to Tandem NonStop systems in the early 1980s. ([source](https://www.mphasis.com/home/thought-leadership/blog/mainframe-based-credit-card-products.html))
- **S2 slow to replace**: met. In 2012 Bank of America moved its consumer card portfolio from aging in-house technology to TSYS. It signed a minimum six-year term plus a 24-month conversion, so about 8 years end to end, with an option to license TS2 in-house afterwards. Chase took a perpetual TS2 license with a six-year payment term (TSYS 2004 8-K, https://www.sec.gov/Archives/edgar/data/0000721683/000072168304000062/chaserelease.htm). In Vietnam, BIDV's move from Cadencie to Way4 took 18 months against a 'usual 30' months, per OpenWay's CEO (https://fpt-is.com/en/bidv-and-the-fpt-openway-joint-venture-complete-core-card-system-migration-to-the-world-class-way4-platform/). Global Payments' 10-K describes issuer revenue as coming from long-term contracts with annual minimums and early-termination penalties. ([source](https://www.americanbanker.com/payments/news/bank-of-america-returns-its-consumer-card-portfolio-to-tsys))
- **S3 workarounds**: met. Rivero, a dispute-software vendor, says most issuing banks piece together Mastercard dispute fund reconciliation from fragments of documentation, tribal knowledge and manual spreadsheets. Teams chase discrepancies across Mastercom reports, clearing files and GL entries. Its dispute guide says many issuers 'still rely on spreadsheets, emails, and legacy tools'. Caveat: this is vendor marketing, not an independent survey. No regulator or independent study was found. ([source](https://rivero.tech/blog/issuer-banks-reconcile-mastercard-dispute-fund-movements-guide))
- **S4 shrinking skills**: met. In BMC's 2025 Mainframe Survey, 45% of financial-services respondents named staffing and skills a top challenge. BMC describes the generational handoff of mainframe expertise as 'already underway'. Live VisionPLUS job posts (Citi, Synechron, Experis UK) ask for COBOL/CICS/VSAM/JCL plus several years of VisionPLUS CMS experience, so the skill is niche and product-specific. Caveat: the BMC figure covers all financial-services mainframes, not card processing alone. ([source](https://www.bmc.com/blogs/mainframe-survey-financial-services-key-takeaways/))

## Segments

Enterprise: the largest issuers run these systems directly or under license. JPMorgan Chase took a perpetual TS2 license. Bank of America moved off its in-house system onto TS2 in 2012-2014. Truist signed a long-term TS2 deal. Citi job posts recruit VisionPLUS CMS COBOL developers. Mid-market and SMB: community banks and credit unions mostly reach the same mainframe platforms through outsourced processors (Fiserv Optis, TSYS, FIS) rather than owning them. Fiserv's 10-K says it serves financial institutions, group service providers, retailers and consumer finance companies. Government: Fiserv's 10-K lists government payment processing and prepaid processing next to credit card processing. In Asia, licensed on-prem platforms (VisionPLUS, Way4, PowerCARD, BASE24) sit at large and mid-sized banks, e.g. 14 Vietnamese institutions on Way4 and BIDV's migration off Cadencie. I found no source quantifying the SMB vs enterprise split.

## Reasons buyers stay

- Long contracts with annual minimums and early-termination penalties (Global Payments 10-K). The Bank of America TS2 deal had a 6-year minimum term.
- Conversions are risky multi-year projects: 24 months for Bank of America, and a 'usual 30 months' for a core card migration per OpenWay.
- Mainframe platforms are proven at very large scale (600M+ cards on VisionPLUS versions) with high availability for authorization.
- Scheme certifications, regulatory reporting and fraud and collections integrations are built up over decades around the core.
- Incumbents are modernizing in place. Fiserv is re-engineering Optis (Celent), which lowers the urgency to switch.
- Licensed in-house options (TS2 perpetual license) let large banks keep control without a platform change.

## Notes

Coverage gaps and caveats. (1) Vendor-disclosed customer counts are thin. Fiserv's FY2024 10-K and Global Payments' FY2024 10-K give no issuer client or account counts. The 600M VisionPLUS card figure is from Wikipedia, not the vendor. (2) S3 rests on a dispute-software vendor's marketing pages, not an independent survey. (3) S4 uses BMC's financial-services-wide mainframe survey (45% cite staffing/skills), not a card-specific study. (4) The TH and MY buyer counts come from Wikipedia because the BOT and BNM pages I opened gave no counts. The VN figure covers only the 33 domestic joint-stock banks, not state-owned, foreign or JV banks. (5) Several challenger founding dates and Pismo's $1B price appear in search snippets but were not in the pages I opened, so I left them unstated. (6) Global Payments agreed to sell Issuer Solutions (TSYS) to FIS (announced 2025). I did not open a source confirming close status. (7) I did not identify an AI-native challenger specifically rewriting card processor cores. AI activity found is in surrounding functions such as disputes (e.g. Rivero), not verified for funding. (8) Other dominant Asian systems such as CardPro, Euronet Cadencie (BIDV's former system per FPT IS) and Euronet Ren were not profiled in depth.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
