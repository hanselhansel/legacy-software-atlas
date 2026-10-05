# Regulatory and prudential reporting (bank/insurer/fund returns to regulators)

Slug: `regulatory-prudential-reporting`

## Systems

- Regulator collection platforms (legacy): APRA Direct to APRA (D2A, Java/Oracle desktop client, built by 2002, decommissioned March 2026), Bank of England OSCA (switched off Dec 2022), RBI legacy XBRL portal (discontinued from Dec 2023), MAS MASNET (decommissioning announced 2026), BOT Data Management System (fixed reports, being replaced by RDT), BNM STATsmart Excel-template submission
- Regulator collection platforms (replacements): APRA Connect, BoE BEEDS, RBI CIMS, BI-ANTASENA (BI/OJK/LPS integrated reporting, live July 2021), OJK APOLO, MAS Data Collection Gateway, BOT Regulatory Data Transformation (RDT)
- Bank-side regulatory reporting engines: Regnology (Abacus / Reporting Hub, now also owning OneSumX, AgileREPORTER and Moody's RegReporting), Nasdaq AxiomSL ControllerView, Oracle OFSAA Regulatory Reporting (i-flex Reveleus lineage)
- US community-bank call report preparation desktop tools: Jack Henry Regulatory Filing (formerly Sheshunoff), FIS Compliance Solutions (formerly The Intercept Group, callreporter), DBI Financial Systems
- Spreadsheet / end-user-computing last-mile and XBRL/XML file preparation
- Regional specialists: Fintellix (India/APAC), Nawadata (Indonesia APOLO/ANTASENA), RegCentric Reg360 (Australia)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. APRA's D2A collection system was completed by 2002 as an installed desktop client (CFR Annual Report 2002). iTnews describes it as a Java-based Oracle application that took XML/XBRL or manual entry. On the vendor side, AxiomSL was founded in 1991 and Regnology's Abacus sold its first licences in 1994, both well before 2005. ([source](https://www.cfr.gov.au/news/annual-reports/2002/pdf/2002.pdf))
- **S2 slow to replace**: met. APRA put D2A's replacement out to tender in 2018 and planned to finish implementation in late 2019. APRA Connect then went live 18 months late, in September 2021. In February 2026 APRA still had D2A scheduled for replacement by end-2027, about 9 years after the tender, and APRA calls it a 'multi-year program'. A security pentest finding forced D2A's early decommission in March 2026. In the UK, the BoE/FCA Transforming Data Collection and the PRA Future Banking Data reforms are also multi-year programmes. ([source](https://www.itnews.com.au/news/apra-pulls-data-submission-system-after-security-pentest-624620))
- **S3 workarounds**: met. BearingPoint's 2025 study of 50 institutions in 9 European countries found 90% of banks still use spreadsheets and other manual tools in their reporting processes, and three in four rely on supervisor feedback to catch errors. A March 2022 Bank of Thailand study of 9 commercial banks found staff time is the largest reporting cost and that balance-sheet returns involve 'numerous manual works'. APRA's 2018 consultation found entities wanted 'less manual entry'. ([source](https://www.bearingpoint.com/en/about-us/news-and-media/press-releases/banks-remain-dependent-on-supervisory-feedback-to-identify-and-correct-reporting-errors/))
- **S4 shrinking skills**: not met. No category-specific source found. The legacy stack here is Java/Oracle clients, SQL/ETL, XBRL and spreadsheets, not COBOL or RPG. General banking talent-shortage articles exist, but none of the sources opened shows that regulatory-reporting system skills specifically are scarce. ([source](https://www.itnews.com.au/news/apra-to-rip-and-replace-core-financial-data-platform-499546))

## Segments

All four segments use these systems, at different tiers. Government: the regulators run the collection platforms themselves (APRA D2A to APRA Connect, BoE OSCA to BEEDS, RBI XBRL to CIMS, BI-ANTASENA and OJK APOLO, MAS DCG, BOT RDT, BNM STATsmart). Enterprise: Tier 1 and 2 banks and insurers buy engines like AxiomSL, Regnology/OneSumX/AgileREPORTER and Moody's (AGILE alone serves 150+ banks), and FR Y-9C filers above $3bn. Mid-market and SMB: US community banks, which are about 90% of the 4,238 FDIC-insured institutions, use desktop call-report preparation tools from Jack Henry (Sheshunoff), FIS (Intercept) and DBI, per the Fed vendor list. Small Australian credit unions, super funds and insurers relied on D2A data entry or XML files. Indonesian regional development banks buy local APOLO reporting tools. Even large banks show spreadsheet dependence: 90% of banks in BearingPoint's European study.

## Reasons buyers stay

- The regulator sets the format, and returns change constantly. Incumbent vendors ship taxonomy and template updates for dozens of jurisdictions (AxiomSL lists 100+ US Fed/FFIEC forms alone), which a new entrant has to match before it can win a deal.
- Errors carry penalties and supervisory attention. In Indonesia, POJK 22/2025 sets fines for inaccurate reports. Banks are reluctant to change the system that produces signed-off returns.
- Regulators move slowly. APRA ran D2A for about 24 years, and its replacement slipped 18 months and then needed a multi-year migration. Firms time their own changes to the regulator's platform cutovers.
- Vendor consolidation: Regnology bought VERMEG AGILE (2024), Wolters Kluwer FRR (2025, about EUR 450m) and Moody's RegReporting (2026). Customers face a forced roadmap, not an open market.
- Reporting is a large but bounded cost, around 0.31% of opex for Thai banks per the BOT 2022 study, so the business case for replacement is often weak outside regulatory deadlines.
- The logic sits in data lineage and reconciliations upstream of the reporting tool, so swapping the last-mile tool alone does not cut the manual work.

## Notes

The premise is confirmed and updated. APRA did replace D2A with APRA Connect: go-live September 2021, 18 months late (xbrl.org). The migration was planned to finish by end-2027. Then a pentest on 19 March 2026 found vulnerabilities, APRA took D2A offline on 20 March and announced its decommission on 27 March 2026. APRA told entities to uninstall the client and offered email submission as a stopgap. Life insurance collections move to APRA Connect for the 31 Dec 2026 period, and most super forms from 30 Sept 2026. D2A dates to 2002 (CFR Annual Report 2002).

The same regulator re-platforming is happening elsewhere: BoE OSCA to BEEDS (OSCA off 1 Dec 2022), RBI XBRL to CIMS (from Dec 2023), BI-ANTASENA (July 2021), OJK APOLO (POJK 22/2025), MAS MASNET to DCG/CorpPass (2026), BOT DMS to RDT (from 2020). Each cutover is a trigger event for bank-side tooling.

The vendor market consolidated sharply in 2024-26: Regnology absorbed AGILE, OneSumX and Moody's RegReporting, and Nasdaq owns AxiomSL. That likely pushes customers through forced migrations, which is an opening for challengers.

Gaps:
- S4 is not met; no source shows scarce skills for this stack.
- No vendor-disclosed customer counts were found for OneSumX, AxiomSL, Jack Henry, FIS or DBI on pages opened. The secondary claims (AxiomSL 250+ institutions, Regnology 7,000 institutions in 2022) were not confirmed on a page opened.
- Thailand and Vietnam bank counts are not confirmed from regulator pages.
- The EU count covers only ECB significant institutions.
- Insurer and pension-fund registers (EIOPA, NAIC, APRA super, IRDAI, OJK IKNB) were not counted.
- Suade's Series A amount was not confirmed on a page opened.
- No AI-native challenger with material funding was found that is focused on prudential returns specifically. The funded AI compliance startups found (Norm AI, Apiax, Eisen) target rules and compliance ops, not return production.

Key cost benchmarks: UK banks spend GBP 2-4.5bn a year on reporting (BoE Future of Finance, via PRA search result, not opened). Thai banks spend about THB 1bn a year (0.31% of opex), from the BOT 2022 study, which was opened.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
