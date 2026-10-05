# AML, KYC and financial-crime compliance (transaction monitoring, screening, case management)

Slug: `aml-kyc-financial-crime`

## Systems

- NICE Actimize SAM (Suspicious Activity Monitoring), ActOne case management, WL-X/CDD (on-prem, now also X-Sight/Xceed cloud)
- Oracle Financial Services FCCM / Behavior Detection (ex-Mantas Behavior Detection Platform), Oracle FLEXCUBE-integrated AML
- SAS Anti-Money Laundering / SAS Visual Investigator
- SymphonyAI NetReveal (ex-Norkom, ex-BAE Systems Detica NetReveal)
- FICO TONBELLER Siron AML / Siron KYC / Siron Embargo
- LexisNexis Risk Solutions Firco Continuity / Firco Trust / Firco Compliance Link (ex-FircoSoft, OFAC Agent)
- Nasdaq Verafin (cloud, community banks and credit unions; mid-2000s origin)
- Rules-based scenario engines feeding manual alert triage, plus RPA bots and spreadsheets for investigation and SAR/STR narrative assembly

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The dominant engines were all first shipped as on-prem client-server software before 2005. Mantas came from SRA's mid-1990s NASD surveillance work and launched in June 2001 with Merrill Lynch and Wells Fargo as customers. FircoSoft (founded 1990) deployed its first sanctions filter, OFAC Agent, in 1994. Actimize began selling AML software in 2000. SAS AML started in 2001-02. None of these were mainframe products. They are on-prem rule and scenario engines, and NICE's FY2024 20-F still reports rising demand for on-premises Financial Crime and Compliance products. ([source](https://www.washingtontechnology.com/2001/06/sra-ventures-launches-first-commercial-it-company/350405/))
- **S2 slow to replace**: met. TD Bank's US resolution documents (filed with the SEC) describe a failure to substantively update its transaction monitoring system between 2014 and 2022, about 8 years, despite warnings. Domestic ACH and most check activity went unmonitored, and about $18.3T of activity was not monitored from 2018 to April 2024. The resolution adds a 3-year independent monitorship. This shows that monitoring stacks stay unchanged for many years. I found no primary source on vendor contract terms of 7+ years or on the duration of a named replacement programme. ([source](https://www.sec.gov/Archives/edgar/data/947263/000119312524282664/d40074d40app.htm))
- **S3 workarounds**: met. The HKMA/Deloitte 2021 AML/CFT Regtech Survey of 170 institutions found that 120 had run AML process-optimisation work in the previous two years. Of those, 82 used technology, including RPA at 49 institutions, low-code workflow tools at 29 and process mining at 20. RPA here is screen-level automation layered over legacy AML and case systems. NICE's own 2018 SAM9 release (SEC exhibit) pitches RPA to remove manual searches for third-party data and to cut single-alert investigation time by up to 70%. I found no primary source counting spreadsheet use. ([source](https://www.hkma.gov.hk/media/eng/doc/key-functions/banking-stability/aml-cft/seminar_20211005_4.pdf))
- **S4 shrinking skills**: not met. These platforms run on Java, Oracle DB and SAS, not COBOL or RPG, and I found no primary source showing that their platform-specific skills (Actimize, Mantas/OFSAA, SAS AML scenario tuning) are scarce. The closest evidence is the HKMA 2021 survey: 71 of 170 institutions (41.7%) said knowledge and skill limits held back their AML/CFT programmes. That is a general skills gap, not a shrinking legacy-language pool, so S4 is not met. ([source](https://www.hkma.gov.hk/media/eng/doc/key-functions/banking-stability/aml-cft/seminar_20211005_4.pdf))

## Segments

Enterprise and tier-1 banks run the pre-2005 on-prem engines. Mantas launched with Merrill Lynch and Wells Fargo and was used by ABN Amro, Citibank and Credit Suisse. Firco is used by 9 of the top 10 banks. NetReveal served 200 leading financial institutions. Actimize SAM/ActOne went to Bank of Ayudhya in Thailand. Mid-market and regional banks run SAS AML (300+ licensees in 69 countries) and FICO TONBELLER Siron (1,000+ banks and commercial organisations, DACH-heavy). US SMB banks and credit unions mostly moved to cloud Verafin (2,000+ institutions) and similar vendors, so the legacy footprint there is smaller. Government shows up as regulator and data-sharing hub rather than as a buyer: MAS COSMIC (live 1 Apr 2024) links DBS, OCBC, UOB, SCB, Citi and HSBC to share red-flag customer information on legal-person misuse, trade-finance abuse and proliferation financing. Payment firms and insurers are also in scope; fintechs mostly start on cloud tools such as Unit21, Hawk and ComplyAdvantage.

## Reasons buyers stay

- Regulatory model risk: rule scenarios that examiners have already reviewed and validated must be re-tuned, back-tested and parallel-run on any new engine, and regulators (FCA, DOJ/OCC, MAS) punish monitoring gaps hard. TD Bank's 2024 resolution and the FCA's HSBC and Metro Bank fines show the cost of getting it wrong
- Deep integration with core banking, payments (SWIFT/Fedwire/SEPA message filters) and data feeds. Firco has held SWIFT Alliance Screening certification since 2001
- Incumbents are adding AI to their existing products (NICE X-Sight/Xceed cloud, Oracle FCCM Cloud, SymphonyAI Sensa on NetReveal), so banks can modernise without switching vendor
- Vendors also sell AI overlays (ThetaRay with Matrix USA; Silent Eight on top of existing screening) that leave the legacy rules engine in place
- On-prem demand is still growing: NICE's FY2024 20-F reports higher demand for on-premises Financial Crime and Compliance products in 2024
- Data residency rules and the need for explainable models favour proven on-prem deployments in APAC and EU banks

## Notes

Coverage gaps: I found no primary source that measures how much legacy AML software is installed, by region or overall. The vendor counts above are self-reported and from different years. The rest of this note is caveats.

1. Unverified figures. Some customer counts came only from search snippets I could not open: Actimize 400+ clients and 10 of the top 10 US banks; FircoSoft 770+ customers; ComplyAdvantage about 500 customers and about $171M raised; Unit21 $45M Series C (Jun 2023, page returned 403). Treat them as unverified. Oracle FCCM/Mantas has no current disclosed customer count.

2. Blocked or unreadable sources. Several primary pages returned 403 or a bot-check page: the DOJ TD Bank release, the FCA HSBC and Commerzbank releases, the i-flex/Mantas reports on Finextra and Business Standard, and the OJK statistics PDF. For TD Bank I used the SEC Form 40-APP filing instead. BNM, BOT and the OJK portal did not show counts in readable form. Malaysia, Thailand and Indonesia buyer counts are therefore weak.

3. S-sign judgments.
   - S1 is met on on-prem client-server, not mainframe.
   - S2 rests on TD Bank going about 8 years without a substantive monitoring update. I found no primary source for contract length.
   - S3 rests on RPA adoption in the HKMA survey (49 of 120 institutions), not on a direct count of spreadsheet use.
   - S4 is not met: the stack is Java, Oracle and SAS, not COBOL.

4. AI angle. Rules-based monitoring is widely reported to produce about 90-95% false-positive alerts, but I found only vendor blogs for this, not primary sources. The AI case shows up in the incumbents' own pitches: NICE's 2018 SAM9 release (SEC exhibit) cites up to 70% faster investigations with ML and RPA. Challengers split into AI overlays (Quantexa, ThetaRay, Silent Eight, Lucinity) and greenfield replacements (Hawk, Tookitaki, Feedzai, Unit21).

5. COSMIC. The MAS COSMIC page confirms launch on 1 Apr 2024, the six banks (DBS, OCBC, UOB, SCB, Citibank, HSBC) and three risk areas (legal persons, trade finance, proliferation financing).

6. Vendor ownership changes: Norkom to BAE to SymphonyAI; Mantas to Oracle; FircoSoft to RELX/LexisNexis; TONBELLER to FICO; Actimize to NICE. Most of the installed base now sits with large software or data owners.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
