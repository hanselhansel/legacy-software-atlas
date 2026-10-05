# Accounting firm practice and tax prep

Slug: `accounting-practice`

## Systems

- Thomson Reuters UltraTax CS (CS Professional Suite; desktop install, also hosted via Virtual Office CS)
- Intuit Lacerte and ProSeries (desktop professional tax)
- Drake Tax (desktop, Drake Software, est. 1977)
- Wolters Kluwer CCH ProSystem fx Tax / Engagement (on-premise; migrating to CCH Axcess)
- DATEV on-premise suite for German Steuerberater (Kanzlei-Rechnungswesen, Kanzleimanagement; data centre model since 1966)
- IRIS Accountancy Suite, Keytime, PTP (UK desktop; migrating to IRIS Elements)
- CCH Central (UK, Wolters Kluwer)
- Caseware Working Papers (desktop audit file, since 1988)
- MYOB Accountants Enterprise / Accountants Office (AU, on-prem SQL Server)
- Access HandiSoft (AU, on-prem, 30+ years)
- CompuTax CompuOffice and SAG Infotech Genius (India desktop tax suites)
- MISA SME (Vietnam desktop accounting, used by service bureaus)
- Access UBS Accounting (Malaysia/Singapore desktop accounting, used by bookkeeping firms)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Core products predate 2005 and were built as desktop/client-server: UltraTax ran on DOS until a 1995 move to 32-bit Windows; Drake dates to 1977; Lacerte was bought by Intuit in 1998; DATEV began in 1966 as a data-processing cooperative; Caseware Working Papers since 1988; CompuTax 1989; MISA SME 1994-96. MYOB AE still requires on-prem SQL Server and Windows Server. ([source](https://www.cpapracticeadvisor.com/2008/12/01/creative-solutions-ultratax/5231/))
- **S2 slow to replace**: met. Migrations run for many years. Wolters Kluwer only saw group recurring cloud software exceed on-premise revenue in 2024, with Tax & Accounting still migrating CCH ProSystem fx users to CCH Axcess. DATEV says its core Kanzleimanagement application will only start moving users to the cloud from October 2026, 60 years after founding. IRIS migrates Keytime/PTP/Accountancy Suite customers to Elements in phases and offers desktop hosting (IRIS Anywhere) as an interim. No evidence found of 7+ year contract terms; these are annual licences, so the slowness is in migration, not contract length. ([source](https://www.datev.de/content/dam/markenassets/unternehmenskommunikation/presse/im-fokus/jahrespressekonferenz/jpk-2026/Pressemappe_JPK2026_gesamt_ohne%20Sperrfrist.pdf))
- **S3 workarounds**: met. Re-keying of source documents into tax software is the core workaround, and a market has grown up around it. Thomson Reuters paid $500M for SurePrep, whose 1040 automation removes manual data entry and was used by 23,000+ tax professionals. Filed (TechCrunch, May 2025) reads documents and enters data into existing systems, and says professionals spend about half their time on automatable low-value tasks. UltraTax ships a bar-code scan and data-entry utility, and is often hosted (Virtual Office CS) rather than replaced. ([source](https://www.thomsonreuters.com/en/press-releases/2023/january/thomson-reuters-completes-acquisition-of-sureprep-llc))
- **S4 shrinking skills**: not met. No evidence that the software's technical skills are scarce. These are vendor-maintained Windows/.NET/SQL Server products, not COBOL/RPG systems that firms run themselves. A related but different shortage does exist: the CPA Journal reports US first-time CPA exam candidates fell from 48,004 (2016) to 32,188 (2021) and about 75% of AICPA members are at retirement age. That is a shortage of operators, not of system skills, so S4 is not met as defined. ([source](https://www.cpajournal.com/2025/08/15/the-accounting-profession-is-in-crisis-3/))

## Segments

Mostly SMB, with a long tail of sole practitioners and some mid-market and enterprise firms. Evidence: 72% of India's 100,138 CA firms are sole practices (ICAI data); Drake serves 70,000+ mostly small preparers; UltraTax CS Express targets firms under 250 returns. The top of the market also runs these systems: IRIS counts 93 of the top 100 UK firms, Caseware Working Papers is used by Big Four and other large networks, and DATEV covers most of Germany's roughly 89,500 tax advisers. Governments are not buyers of practice software; they act as e-filing counterparties (IRS, HMRC, ATO, DJP Coretax) and their form and API changes drive yearly updates. In SEA (VN, MY, TH, ID, PH), firms mostly use desktop SMB ledgers such as MISA, Access UBS, Accurate and Zahir, plus Excel and government e-filing portals, rather than a dedicated practice suite.

## Reasons buyers stay

- Yearly form updates, diagnostics and e-file certification are built in; a new entrant has to match thousands of federal and state forms before a firm can switch
- Prior-year data rollover and multi-year client history live in the incumbent's proprietary file format
- Busy-season risk: firms will not migrate mid-season, so a switch can only happen once a year
- Integrated suites (CS Professional Suite, CCH Axcess/ProSystem, DATEV, IRIS) bundle tax, accounts production, practice management and document management
- Staff are trained on input-sheet workflows (e.g., Lacerte's input-sheet interface)
- Vendors offer hosting (Virtual Office CS, IRIS Anywhere, Access HandiSoft Online, MYOB hosting partners), which cuts the pressure to replace
- Confidentiality, data residency and sovereignty concerns (DATEV runs its own data centres for this reason)
- AI overlay tools (SurePrep, Filed, Juno) write into the existing tax engine rather than replacing it, which extends incumbents' life

## Notes

The legacy problem here is desktop client-server software that the vendors still ship and update every year. It is not mainframe software. Incumbents (Thomson Reuters, Intuit, Wolters Kluwer, DATEV, IRIS, MYOB/Access) are moving customers to cloud over many years. Wolters Kluwer's group cloud software first passed on-premise revenue in 2024, and DATEV's core practice-management app only starts its cloud migration in Oct 2026. Most AI challengers are overlays that write into UltraTax, CCH and Lacerte, not replacements. Thomson Reuters bought SurePrep for $500M, which suggests incumbents will buy that layer. S4 (scarce system skills) is not met. The operator shortage (CPA pipeline) is real but is a different thing. Data gaps: no vendor-disclosed customer counts for UltraTax, Lacerte, ProSystem fx or MYOB AE; first-ship years for ProSystem fx, IRIS and MYOB AE not found. The Vietnam tax-agent count is from 2019. The Malaysia figure covers only AOB-registered PIE auditors. Thailand has no firm-level count. The Australia TPB figure could not be opened (site timed out) and comes from a search excerpt. The ACRA SG figures were read from the PDF layout: 1,288 RPAs and 794 PAEs in the top row, 3,844 qualified individuals and 3,321 CSPs in the bottom row. In SEA the category barely exists as dedicated practice software. Firms there use desktop SMB ledgers (MISA, UBS), Excel and government e-filing portals, so challengers there look like Osome (an AI service) more than practice-suite replacements.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
