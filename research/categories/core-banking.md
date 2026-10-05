# Core banking

Slug: `core-banking`

## Systems

- FIS Systematics (IBM mainframe, COBOL; Systematics Inc. founded 1968, now FIS)
- Jack Henry SilverLake (IBM System/38 then AS/400 / IBM i, RPG; developed 1986-87)
- Jack Henry CIF 20/20 (IBM System/36 then AS/400, RPG/400; lineage to Jack Henry's original 1977 system)
- Jack Henry Core Director (Windows client/server)
- Jack Henry Symitar Episys (credit unions)
- Fiserv Premier, Precision, Signature, Cleartouch, Portico, DNA (Fiserv account processing)
- Temenos Transact / T24 (GLOBUS lineage 1988, T24 launched 2003)
- Finastra Fusion Equation (Kapiti, IBM AS/400) and Fusion Midas (1975-76, IBM System/32, RPG II)
- Silverlake Axis SIBS (IBM AS/400 / Power Systems; Silverlake founded 1989)
- Oracle FLEXCUBE (i-flex, 1997)
- Infosys Finacle (1999)
- TCS BaNCS (FNS origin, acquired by TCS 2005)
- SAP for Banking (replacement core at CBA 2008-2012)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The leading cores date from 1968 to 1999 and run on mainframe or midrange hardware. Systematics was founded in 1968 and became FIS. Jack Henry's SilverLake was developed in 1986-87 for IBM System/38 and AS/400. Its 10-K still lists 520 SilverLake banks, 260 CIF 20/20 banks and 170+ Core Director banks (client/server), and Jack Henry still resells IBM Power Systems. Midas was first live in 1976 on IBM System/32 using RPG II. Silverlake SIBS runs mainly on IBM AS/400. FLEXCUBE shipped in 1997 and Finacle in 1999. CBA's CIO said in 2008 that the legacy systems it was replacing had run the Group for over 45 years. ([source](https://www.sec.gov/Archives/edgar/data/779152/000077915225000055/jkhy-20250630.htm))
- **S2 slow to replace**: met. Commonwealth Bank announced its core banking modernisation (SAP plus Accenture) in April 2008 with a forecast of about A$580M over four years. It declared the work complete in October 2012 after five years and more than A$1B spent (iTnews). TSB committed to its migration to Proteo4UK in December 2015 and did the main migration in April 2018, about 2.5 years. The PRA's Final Notice fined TSB GBP18.9M, and the total FCA plus PRA fine was GBP48.65M. Jack Henry told IT Jungle in 2022 that its cloud-native rewrite would take about 15 years to deliver, and that most customers would keep running current IBM i systems for 10 to 15 years. On contract length, Jack Henry's outsourced core contracts typically run six years (FY2025 10-K). Fiserv historically disclosed 3-to-5-year processing terms. So no opened primary filing confirms 7+ year contracts. The sign is met on multi-year replacement, not on the 7+ year contract test. ([source](https://www.itjungle.com/2022/03/28/inside-jack-henrys-long-term-modernization-roadmap/))
- **S3 workarounds**: met. In the SDNY opinion in In re Citibank August 11, 2020 Wire Transfers (Feb 2021, Judge Furman), Flexcube released any payment as an outbound wire unless the operator suppressed that default. Per Citi's Fund Sighting Manual, suppressing a principal payment meant setting all three fields (FRONT, FUND, PRINCIPAL) to an internal 'wash account'. The opinion describes this as the easiest (or perhaps only) way to do the transaction. The operators set only one field, and about $894M of principal went to lenders by mistake. The work was a manual six-eye (maker-checker-approver) process run partly by Wipro staff in India. This is a documented manual workaround on a legacy loan system. I found no regulator-grade source quantifying spreadsheet or screen-scraping use across banks. ([source](https://www.nysd.uscourts.gov/sites/default/files/2021-02/20cv6539%20Citibank%20Opinion.pdf))
- **S4 shrinking skills**: met. BMC cites Reuters: an estimated 43% of banking systems and 95% of ATM swipes use COBOL, many mainframe and COBOL experts are nearing retirement, and only 75 US schools still taught COBOL in 2017. GAO-25-107795 (July 2025) says agencies, including Treasury, whose systems run COBOL and Assembly, have had difficulty finding staff with these skills and may pay a premium for specialists. Jack Henry is rewriting its RPG-on-IBM-i cores into .NET, C# and Go over about 15 years (IT Jungle 2022). The BMC page is a vendor blog citing Reuters, and the GAO report covers government, not banks. ([source](https://www.bmc.com/blogs/cobol-trends/))

## Segments

Legacy cores show up in every segment.

- SMB and mid-market: US community banks and credit unions are the core of Jack Henry's and Fiserv's installed base. Jack Henry reports 260 CIF 20/20 banks from de novo to $6B, 170+ Core Director banks up to $2B, 520 SilverLake banks from $1B to $55B and about 715 Symitar credit unions (FY2025 10-K). Indonesia's 1,339 BPRs, India's 1,457 urban co-operative banks and the 366 Philippine rural and cooperative banks are similar small-bank pools, but I found no vendor-level evidence for them.
- Enterprise: CBA replaced 45-year-old legacy systems in 2008-2012. Citi ran syndicated loan payments on Flexcube (Revlon case). Barclays has run FIS core since 2012. About 40% of the 20 largest SEA banks run Silverlake SIBS on AS/400, including OCBC, UOB, CIMB and Maybank per broker coverage. TSB migrated 5.2M customers in 2018.
- Government: state-owned banks are major buyers, e.g. India's 12 public sector banks (SBI uses TCS BaNCS modules) and Vietnam's state-owned commercial banks. GAO documents COBOL dependence at US Treasury, but that is government finance, not banking.

## Reasons buyers stay

- The risk of a failed migration is existential and publicly punished: TSB's 2018 migration led to GBP48.65M in FCA and PRA fines and multi-day outages for 5.2M customers.
- Replacement takes years and costs a lot: CBA's program ran five years and cost over A$1B against an original A$580M four-year forecast.
- Vendors themselves expect 10-15 years of coexistence. Jack Henry says most customers will keep running IBM i cores for ten or fifteen years and it will keep supporting them.
- Outsourced core contracts auto-renew at multi-year terms (Jack Henry's typically run six years; Fiserv cites high renewal rates), and termination fees and deconversion costs build switching friction.
- The core is the system of record for deposits, loans and the GL, with decades of business rules held only in code. The Citi Flexcube case shows how much process knowledge sits in manuals and operator habits.
- Regulator expectations on operational resilience and outsourcing (PRA/FCA, MAS TRM, OJK, RBI) add approval and testing overhead to any switch.
- Integration lock-in: payments, digital banking, cards and regulatory reporting are all wired to the existing core's interfaces.

## Notes

Method: every source URL below was opened with WebFetch, and PDFs were text-extracted locally.

Gaps and caveats:
1. S2 is met on multi-year replacement (CBA: five years, more than A$1B; Jack Henry: 15-year rewrite; TSB: about 2.5-year build and a failed cutover). No opened primary source confirms 7+ year contracts. Jack Henry discloses six-year typical outsourcing terms, and Fiserv historically disclosed 3-5 years.
2. S3 rests on one strong primary source, the SDNY Citibank/Revlon opinion on a manual Flexcube workaround. I found no regulator survey quantifying spreadsheet or re-keying use around cores. The search results that claim such figures are vendor blogs and are not cited.
3. S4 relies on a BMC blog citing Reuters (Reuters itself blocked fetch) and on GAO-25-107795, which covers federal agencies, not banks.
4. Vendor customer counts are vendor-disclosed: Jack Henry 10-K FY2025 and the Temenos about page. Fiserv and FIS do not disclose core client counts in the opened filings. Finacle, TCS BaNCS and Finastra vendor pages returned 403 errors, so their counts come from Wikipedia or trade press, or are marked unknown.
5. Buyer universe: the EU less-significant-institution count (about 1,800) was not verified from an opened page; only the 114 significant entities were. UK counts are approximate from the PRA list page. Thailand uses Wikipedia because the BOT page I opened gave no counts.
6. Silverlake SIBS share and known users come from a KGI Securities broker report (2020), not a company filing.
7. Systematics first product release year is unverified; the company was founded in 1968.

Two further challengers seen in search but not opened are not included: Titan ($3M, 2026, banking-native AI) and Tuum.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
