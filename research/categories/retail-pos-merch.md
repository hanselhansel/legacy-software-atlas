# Retail point of sale and merchandising

Slug: `retail-pos-merch`

## Systems

- Toshiba (ex-IBM) 4690 OS with SurePOS ACE / Supermarket Application (store POS, grocery and high-volume)
- JDA / Blue Yonder Merchandise Management System (MMS) on IBM i (AS/400), RPG/CL
- Oracle Retail Merchandising System (ex-Retek RMS), Oracle DB / PL/SQL batch
- Oracle Retail POS (ex-360Commerce) and Oracle Retail Xstore (ex-MICROS Retail / Datavantage)
- NCR Voyix legacy retail POS portfolio (e.g., NCR/Retalix store systems)
- Aptos (ex-Epicor Retail / NSB / CRS) store and merchandising suites
- Microsoft Dynamics RMS (Store Operations / Headquarters), SMB POS, extended support ended 13 Jul 2021
- LS Retail LS Nav on Dynamics NAV (discontinued, replaced by LS Central)
- SAP for Retail (IS-Retail) on ECC, migrating to S/4HANA
- Homegrown IBM i / RPG merchandising and stock systems (e.g., Lidl's legacy inventory system)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Core store POS OS 4690 first released July 1993 (IBM) and is still supported under Toshiba service contracts; Toshiba lists SurePOS ACE as a legacy system. JDA MMS is an IBM i (AS/400) host merchandising system with nearly 400 accounts. Retek (Oracle RMS) predates Oracle's 2005 acquisition. All are on-prem midrange or client-server. ([source](https://en.wikipedia.org/wiki/4690_Operating_System))
- **S2 slow to replace**: met. Lidl spent about 7 years (about 2011 to 2018) and about EUR 500M trying to replace its custom inventory and merchandising system with SAP for Retail (eLWIS), then abandoned it and returned to the old system. A partner of Shopify (vendor-biased) says an Oracle Xstore implementation typically takes 12 to 18 months, with upgrades on a roughly 5-year cycle. NCR Voyix's 10-K says contractual terms can slow the sunset of legacy products. ([source](https://www.retaildetail.eu/news/food/lidls-failed-it-project-cost-half-billion/))
- **S3 workarounds**: met. Boston Retail Partners 2014 Merchandise Planning and Allocation Survey: more than 60% of respondents relied on spreadsheets or homegrown solutions for planning and supply chain needs. The survey was published through a vendor-sponsored (Logility) press release and is dated. A 2026 Incisiv/Anaplan study found 69% of retailers rebalance inventory monthly or less often, which is indirect evidence of batch and manual cycles. ([source](https://www.logility.com/press-release/logility-sponsors-boston-retail-partners-2014-annual-merchandise-planning-and-allocation-survey/))
- **S4 shrinking skills**: met. Fortra 2026 IBM i Marketplace Survey (315 respondents, late 2025): IBM i skills was a top concern for 69%, up from 60%, displacing cybersecurity as the number 1 concern. This applies to IBM i/RPG merchandising hosts such as JDA MMS. The survey has no retail-specific breakdown. 4690/ACE skills are also niche, but no quantified source was found. ([source](https://www.itjungle.com/2026/02/02/skills-displaces-cybersecurity-as-top-concern-for-ibm-i-shops/))

## Segments

Mostly enterprise and upper mid-market. Toshiba positions SurePOS ACE/4690 for high-volume grocery and independent retail. JDA MMS on IBM i serves about 400 retailers, including Robinsons Retail (PH, 1,000+ outlets). Oracle RMS/Xstore and 360Commerce served tier-1 retailers (Sears, Gap, Home Depot). The NCR Voyix 10-K names enterprise and mid-market convenience/fuel, grocery/drug/mass, and department/specialty retail. In SMB, the legacy footprint is Microsoft Dynamics RMS (extended support ended July 2021) and LS Nav on Dynamics NAV (discontinued). In SEA, the SMB long tail is going straight from cash registers or paper to cloud POS (KiotViet, StoreHub). Government: no evidence found of meaningful government use beyond state-run retailers. Not researched.

## Reasons buyers stay

- Checkout downtime costs revenue directly, and offline-capable lanes (e.g., SurePOS ACE offline functionality) are trusted.
- Deep customization of merchandising logic. Lidl's eLWIS failed partly because SAP valued inventory at retail price while Lidl used purchase price, and Lidl reverted to its old system after about EUR 500M.
- Long hardware and service contracts. 4690 is still supported under service contracts, and NCR says contracts can hinder legacy sunset.
- Integration web of payments certification (EMV/PCI), loyalty, fuel and scale peripherals, and ERP batch interfaces that would all need re-testing.
- Peak-season change freezes and multi-thousand-store rollout logistics stretch replacements over years.
- Vendors offer in-place paths (Toshiba ELERA 'without requiring infrastructure replacement', LS Nav to LS Central, Oracle cloud upgrades) that lower switching pressure.

## Notes

Sources and caveats:
- Vendor-disclosed install counts for the legacy cores are mostly old: JDA MMS ~400 accounts (2014), MICROS 330k sites (2014, includes hospitality), Aptos 122k stores (2015). Toshiba and NCR disclose no current counts. The NCR Voyix FY2025 10-K confirms legacy revenue and contractual barriers to sunsetting, but gives no lane or customer numbers.
- S3 evidence is a 2014 BRP survey reported through a vendor (Logility) press release. Treat it as directional.
- S4 evidence is the IBM i community overall, with no retail split. No quantified source was found for 4690/ACE skills scarcity.
- Buyer universe figures are establishment or enterprise counts from statistical registers, not counts of POS/merch buyers. The addressable enterprise buyer set is far smaller (e.g., TH: 0.1% of establishments are large).
- Partly or wholly unverified:
  - SG: SingStat page 404. The figure is from a search snippet.
  - PH: PSA 403. The figure is from a search snippet.
  - AU: ABS page text gave no retail count.
  - VN: GSO unreachable. An Enterprise Singapore guide was used instead.
  - EU: only the NACE G aggregate.
  - IN: 2013-14 census share; the 16.06M count comes from a search snippet, the 35.41% share from the PDF.
- Not verified, so excluded from fields: Microsoft RMS '45,000 companies' (third-party blogs only) and JDA's '360 retailers in 60 countries' (search snippet of JDA collateral).
- The Lidl case is a homegrown merchandising system, not a packaged vendor product. It still shows multi-year replacement risk.
- Retek's first ship date was not confirmed. Only 'Oracle partner since 1986' and the 2005 acquisition were confirmed.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
