# Utility billing and customer information

Slug: `utility-billing-cis`

## Systems

- SAP IS-U (Industry Solution Utilities on ECC/R/3); successor is SAP S/4HANA Utilities
- Oracle Utilities Customer Care & Billing (CC&B), from SPL WorldGroup
- Customer/1 (Andersen Consulting-era mainframe COBOL CIS, still in some US utilities)
- Home-grown mainframe CIS (e.g. LADWP's 39-year-old CIS replaced in 2013)
- HTE / SunGard / CentralSquare on IBM AS/400 (iSeries)
- JD Edwards / Denovo UCIS on IBM i (AS/400), DB2, RPG/CL
- Harris (Constellation Software): CIS Infinity (Advanced Utility Systems), NorthStar CIS
- Hansen Technologies: Banner / Hansen CIS
- Gentrack: Velocity, Junifer, g2/g2.0
- Tyler Technologies: Incode utility billing, Munis utility billing, ERP 9
- In-house state-utility CIS in Asia: EVN CMIS (Vietnam), PLN AP2T (Indonesia), TNB e-CIBS (Malaysia)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Several cores predate 2005 and run on mainframe or midrange hardware. Santa Fe, NM bills 35,000+ customers on JD Edwards/Denovo UCIS v7.3 with DB2 on IBM iSeries/AS400 (OS V7.1). Danbury, CT runs utility billing and financials on HTE, an AS400 system. LADWP replaced a 39-year-old CIS in Sept 2013, so that system dates from about 1974. SAP IS-U was introduced in 1998 on R/3. EVN CMIS went live in 2004. ([source](https://santafenm.gov/media/rfps_docs/1706P.pdf))
- **S2 slow to replace**: met. Santa Fe issued an RFP in 2014 to replace UCIS with CIS Infinity. In 2015 it terminated its implementation PM contractor, and a later RFP still describes UCIS on AS400 as the live system. LADWP took 'over three years of planning and development' to replace its CIS. Ogden, UT describes a 5-year transition to integrated city software before its billing cutover. Danbury's RFP asks bidders to define annual escalation for 10 years. SAP gives IS-U users until end-2027, or end-2030 with paid extended maintenance, to finish moving to S/4HANA Utilities. ([source](https://www.greatervalleyglencouncil.org/update-on-ladwps-new-customer-billing-and-information-system/))
- **S3 workarounds**: met. Gulfport, MS (2026 RFP, Tyler ERP 9, in use 21 years) lists these problems: staff must manually prepare and send notifications and collections, autopay/ACH errors need manual intervention, and the system relies on manual or batch file imports and exports. Ogden, UT says replacing its billing system lets it 'automate many manual processes'. Wilmington's legacy CIS needed 'manual patchwork fixes'. None of the primary sources read named spreadsheets explicitly, but manual re-keying and batch-file workarounds are documented. ([source](https://mygulfport.us/wp-content/uploads/2026/03/Utility-Billing-Software-RFP-Requirements-and-Specifications.pdf))
- **S4 shrinking skills**: met. Santa Fe, NM had to go to outside contractors for custom RPG and CL programming, DB2-on-iSeries SQL, and 'UCIS, DB2, RPG, and CL maintenance and support' to keep its AS/400 utility billing system running. More broadly, GAO (GAO-25-107795, July 2025) says agencies 'have had difficulty finding employees' with COBOL-era skills and may pay a premium for specialized staff or contractors. That GAO finding covers federal systems, not utilities specifically. Customer/1 CIS job ads still require mainframe COBOL (Indeed listing found in search, page not openable). ([source](https://santafenm.gov/media/rfps_docs/Utility-Billing_City_of_Santa_Fe_Data_Services_RFPv3.3_.pdf))

## Segments

Every segment uses legacy systems. Government and municipal: US cities and water/sewer commissions run AS/400-era systems. Santa Fe NM runs UCIS on iSeries and Danbury CT runs HTE on AS400. Gulfport MS has used Tyler ERP 9 for 21 years, and Ogden UT ran Incode. Public authorities: LADWP ran a 39-year-old mainframe CIS until 2013. State-owned utilities in Asia: EVN uses CMIS (since 2004), PLN uses AP2T (since 2012), and TNB uses e-CIBS, which an integrator calls legacy. Enterprise and mid-market investor-owned utilities and EU suppliers: SAP IS-U and Oracle CC&B, with a forced IS-U migration deadline of 2027/2030. SMB: the roughly 45,000 small US water utilities under 10,000 connections are Current Software's target and often run small on-prem packages. Mid-market munis and co-ops use Harris (Infinity, NorthStar), Tyler and Hansen Banner.

## Reasons buyers stay

- Billing is regulated and revenue-critical. Failed cutovers cause bill shocks, such as Amarillo's 2026 new system overcharging 55,000+ customers and triggering an $85K audit, and LADWP's post-2013 billing breakdown.
- Replacement takes years and gets budgeted as capital: LADWP took 3+ years, Santa Fe's replacement attempt stalled after its 2014 RFP, and Ogden spent a 5-year ERP transition.
- Data conversion risk: decades of account history, rate structures and custom code (RPG/CL, COBOL, ABAP) must be migrated.
- Deep integration with meter data management, ERP, payments and field service. TNB's CRM, for example, integrates with e-CIBS, ERMS and LGBNet.
- Public procurement cycles and multi-year contracts (Danbury asks for 10-year escalation schedules), plus the need to cite peer references converted from the same legacy product.
- In Asia, core billing is often built in-house by state utilities (EVN CMIS, PLN AP2T) and is a national standard, so there is no vendor sale to replace.

## Notes

Many primary pages could not be opened: oracle.com (403), Seattle auditor NCIS memo (403), Ofgem (redirect loop), AER register (timeout), NEA/DOE Philippines (403/DNS), the Hansen and Gentrack annual-report PDFs (over 10MB). Counts that came only from search snippets are labelled as such inside the relevant fields. The oft-cited 'Oracle CC&B 400+ utilities' figure could not be confirmed from a primary source. S3 evidence is manual re-keying, manual notifications and batch-file workarounds from city RFPs, not explicit spreadsheet use. S4 rests on Santa Fe outsourcing RPG/CL/AS400 skills plus GAO's July 2025 federal finding on COBOL staff scarcity, which is not utility-specific. In Southeast Asia (VN, ID, MY, TH) the dominant billing cores are in-house systems at state monopolies (EVN CMIS 2004, PLN AP2T 2012, TNB e-CIBS). The buyer count there is tiny (1-3 electricity distributors per country), but the water side is fragmented: Indonesia has 393 PDAMs. The strongest forcing event is SAP's IS-U deadline (end-2027 mainstream, end-2030 extended). Kraken's press release is dated 29 Dec 2025. The Ogden UT billing packet (INCODE to Munis migration after a 5-year ERP transition) is at https://www.ogdencity.gov/DocumentCenter/View/20166/04-19-22-Info-Utility-Billing-Info-Item-Packet

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
