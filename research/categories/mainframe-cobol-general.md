# Custom COBOL and mainframe applications (cross-industry)

Slug: `mainframe-cobol-general`

## Systems

- IBM Z mainframes running z/OS (MVS lineage) with custom COBOL, PL/I and Assembler applications
- IBM CICS Transaction Server (online transaction processing, released 1969)
- IBM IMS (hierarchical DB/transaction manager, installed 1968)
- IBM Db2 for z/OS and VSAM data files
- JCL batch and 3270 'green screen' (TN3270) terminal front ends
- Micro Focus (now Rocket Software) COBOL / Enterprise Server
- Unisys ClearPath Forward (MCP, from Burroughs 1961; OS 2200)
- Fujitsu mainframes (sales end FY2030, support end FY2035)
- Broadcom (ex-CA Technologies) mainframe tooling (IDMS, Datacom, Endevor etc.)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. CICS was released 8 July 1969 and IMS first installed 1968; Burroughs MCP (now Unisys ClearPath MCP) shipped 1961. GAO (July 2025) found the 11 most critical US federal legacy systems are 23 to 60 years old, and two Treasury systems (59 and 51 years old) run on COBOL and Assembly. ([source](https://files.gao.gov/reports/GAO-25-107795/index.html))
- **S2 slow to replace**: met. GAO-25-107795: of 10 critical federal legacy systems flagged in 2019, only 3 modernizations were done by Feb 2025; planned completion dates run to end of FY2035 (HHS), and two systems have no completion date. Commonwealth Bank of Australia's core banking replacement took about 5 years and cost over A$1 billion (finished 2012). ([source](https://files.gao.gov/reports/GAO-25-107795/index.html))
- **S3 workarounds**: met. Bipartisan Policy Center (2024), drawing on interviews with state officials: COBOL-based state unemployment insurance systems force states to rely on loosely integrated technology, paper-based processes, and manual data entry and transfers. 3270 green-screen apps are still widely automated by screen scraping and terminal RPA (for example UiPath terminal activities), but that evidence comes from a vendor, not a regulator. GAO-25-107795 does not document spreadsheet workarounds. ([source](https://bipartisanpolicy.org/wp-content/uploads/2024/03/BPC_Unemployment_Insurance_RV2.pdf))
- **S4 shrinking skills**: met. GAO (2025): Treasury COBOL/Assembly systems rely on languages with 'a dwindling number of people available with the skills needed to support them'. Agencies pay a premium for specialized staff or contractors. BPC: states struggle to find COBOL programmers as they age out of the workforce. ([source](https://files.gao.gov/reports/GAO-25-107795/index.html))

## Segments

Mostly enterprise and government. IBM says 45 of the top 50 banks, 8 of the top 10 insurers, 7 of the top 10 retailers, 8 of the top 10 telcos and two thirds of the Fortune 100 run IBM mainframes, plus nearly 3,800 critical-infrastructure government and corporate entities (https://newsroom.ibm.com/2022-04-05-Announcing-IBM-z16-Real-time-AI-for-Transaction-Processing-at-Scale-and-Industrys-First-Quantum-Safe-System). Government use is heavy. GAO found 8 of the 11 most critical US federal legacy systems use legacy languages. BPC reports that many state unemployment insurance systems run on COBOL. Some mid-market firms run outsourced or midrange COBOL (Micro Focus, Unisys). SMB use is negligible: no source read shows SMBs running in-house mainframe COBOL.

## Reasons buyers stay

- Proven reliability and throughput: IBM says z17 handles up to 24 trillion operations per second and mainframes process 87% of transactions (IBM Think).
- Long, costly, risky rewrites. CBA's core replacement took 5 years and cost over A$1B. GAO warns that undocumented modernization plans raise the odds of cost overruns and project failure.
- Business rules are embedded in undocumented code that nobody fully understands.
- Gartner (cited by IBM) expects 75% of 'mainframe exit' vendors to pivot or exit by 2030, which makes exit look risky.
- Vendors commit to long roadmaps: Unisys ClearPath Forward 2050 and IBM's annual z cycles.
- Regulatory and operational risk of migrating core ledgers, payments and tax systems.

## Notes

Coverage gaps and caveats:
(1) Buyer universe uses bank and financial regulators as the proxy register. Mainframe buyers also include insurers, telcos, retailers, airlines and government. No register counts mainframe sites. Registers counted for TH and MY were imperfect: the BOT page had no count, and the BNM count comes from a fetch summary of the FSP directory.
(2) MAS figure is the result count for the Full Bank category only.
(3) Several primary pages were blocked (Rocket Software press pages 403, BusinessWire 403, CNBC 403). Rocket and Micro Focus facts therefore come from Wikipedia.
(4) No vendor discloses a mainframe customer count. IBM gives only share-of-top-N figures. 'Nearly 3,800 entities' (IBM 2022) is the closest thing to a count.
(5) S3 evidence is from BPC (a think tank citing state officials), not a regulator. The DOL OIG 2023 testimony opened did not mention COBOL or manual workarounds explicitly.
(6) Bloop.ai (COBOL-to-Java, YC) was excluded. PitchBook search snippets say it is out of business, but this was not verified.
(7) Fujitsu exit (sales end FY2030, support end FY2035) creates a forced-migration cohort, relevant for UK, EU and APAC.
(8) Asia regional evidence of mainframe COBOL use at specific banks (e.g., SBI, BRI, Vietnamese state banks) was not researched in this pass.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
