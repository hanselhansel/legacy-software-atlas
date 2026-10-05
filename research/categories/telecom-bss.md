# Telecom billing and BSS

Slug: `telecom-bss`

## Systems

- CSG Advanced Convergent Platform (ACP, formerly CCS), mainframe-hosted cable/broadband billing
- Amdocs Ensemble / Amdocs CES (customer care and billing)
- Ericsson Billing (formerly LHS BSCS, BSCS iX)
- Oracle Communications Billing and Revenue Management (formerly Portal Infranet)
- Netcracker (NEC) BSS/OSS suite
- Operator in-house COBOL/CICS/DB2 batch billing on mainframes
- Huawei CBS/BSS (named by Totogi as a legacy incumbent)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. CSG's billing platform began as a First Data subsidiary in 1982. ACP still runs on mainframe capacity: CSG's 2009 10-K/A lists a 'Work Order for Mainframe Computer Service' with Infocrossing. Ericsson's BSCS first shipped in 1990 as an on-prem client/server system (Oracle DB, C/C++). Amdocs started in 1982. A large US telco's billing system ran 5M+ lines of COBOL and 4,000 JCL procedures on CICS/DB2 for 30+ years (updraftworks.com/case-studies-legacy-modernization.html). ([source](https://www.sec.gov/Archives/edgar/data/1005757/000119312509188328/d10ka.htm))
- **S2 slow to replace**: met. CSG's FY2005 10-K says TCI signed a 15-year exclusive contract in 1997 to move all its customers onto CSG billing, and Comcast inherited it. In 2005 about two-thirds of accounts had moved to ACP, after the 2004 upgrade. Charter's CSG agreement runs to March 31, 2028 with an automatic one-year extension (CSG 10-K, via search snippet). Comcast received 10-year stock warrants in 2014 as an incentive to convert accounts onto CSG (CSG Q1 2024 10-Q). ([source](https://www.sec.gov/Archives/edgar/data/0001005757/000119312506053833/d10k.htm))
- **S3 workarounds**: met. Cambridge Management Consulting (Paul Brooker) says invoicing and other key operator processes stay 'fragmented, manual, and dependent on people bridging the gap between systems'. It says staff are often the costliest automation tool an operator owns, re-keying data and reconciling records between disconnected BSS. It lists spreadsheets and manual processes as part of the legacy stack. This is consultant commentary, not survey data. ([source](https://www.cambridgemc.com/the-complexity-tax))
- **S4 shrinking skills**: met. AWS for Industries (Feb 25, 2025) says telco mainframes run BSS/OSS rating, charging and billing. It warns that shrinking mainframe expertise puts operators at risk of losing critical application knowledge. No telecom-specific headcount data was found. General COBOL workforce ageing figures came only from secondary sources. ([source](https://aws.amazon.com/blogs/industries/aws-mainframe-modernization-transforming-telco-from-legacy-constraints-to-digital-innovation/))

## Segments

Enterprise: Tier 1 and Tier 2 carriers and cable operators are the core users. Amdocs' top ten customers make up about 70% of its revenue (AT&T 25.9%, T-Mobile 19.9%). CSG depends on Charter and Comcast for about 39% of its revenue. Ericsson BSCS sits mainly in national mobile operators. Mid-market: regional operators, MVNOs and ISPs, often on Oracle BRM, Netcracker or regional suites. The ID, IN and TH registers show over 1,000 small licensees, mostly ISPs, that rarely run heavy legacy BSS. Government: state-owned operators such as BSNL/MTNL (IN), VNPT, Viettel and MobiFone (VN), and NT (TH) are buyers, but no system-level evidence was gathered for them. SMB: not a user of this legacy category.

## Reasons buyers stay

- Billing is revenue-critical. A failed cutover hits cash and the regulator at once, so operators run parallel systems and byte-for-byte output comparisons (updraftworks case: a 14-month migration of a 30-year COBOL system).
- Long exclusive contracts and conversion incentives tie operators in: TCI/Comcast signed a 15-year exclusive contract with CSG, Comcast received 10-year conversion warrants, and Charter's term runs to 2028.
- Operators already hold fully paid licenses and buy long-term managed services, which lowers the run cost of staying (Amdocs 20-F).
- Decades of tariff, discount and regulatory logic are embedded in the system and poorly documented.
- Industry vendors frame BSS transformations as multi-year programmes with a record of failures (Totogi CEO on 'billions' wasted), which discourages replacement.

## Notes

Several pages could not be read. ACMA timed out twice, so the AU count of about 340 comes only from a search snippet. NTC (PH), Ofcom numbering data, the Komdigi dittel page, the Lexology telecom guides and Fierce Network all returned 403. VNTA refused the connection. IMDA's FBO list is rendered by JavaScript, so no count was taken. The FCC 499 database and BEREC GADB show no totals. In the CSG FY2023 10-K the fetch did not surface the Charter 2028 term. That term comes from a search snippet of CSG filings, so the S2 citation rests on the TCI 15-year contract in the FY2005 10-K. The 'mainframe' evidence for ACP is the Infocrossing mainframe work-order exhibit in CSG's 2009 10-K/A. S4 rests on one AWS blog statement plus general COBOL-workforce commentary; no telecom-specific skills survey was found. S3 rests on consultant commentary (Cambridge MC); no quantitative telecom spreadsheet survey was opened. TM Forum revenue-assurance figures (1.9% leakage) appeared only in snippets. Market consolidation is notable: Amdocs absorbed MATRIXX (Dec 2025), Qvantel absorbed Optiva (Dec 2025) and Ericsson took a minority stake in LotusFlare (Dec 2025). Several 'challengers' are now owned by incumbents. Huawei and ZTE BSS are significant in ID, TH, MY and PH, but no primary source was gathered on them. The Amdocs '~400 customers' figure is from the FY2025 20-F text, quoted via search; the fetched excerpt confirmed the customer concentration figures.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
