# Procurement and accounts payable

Slug: `procurement-ap`

## Systems

- SAP R/3 / ECC (SAP Business Suite 7) MM purchasing and FI-AP payables, on-prem client-server
- SAP R/2 mainframe (predecessor, 1979)
- Oracle E-Business Suite (Oracle Applications / Financials: Purchasing, iProcurement, Payables), on-prem
- JD Edwards World (RPG on IBM System/3x, AS/400 / IBM i) Accounts Payable and Procurement
- JD Edwards EnterpriseOne and PeopleSoft Financials/Supply Chain (Oracle-owned on-prem)
- Ariba Buyer (on-prem e-procurement, 1996-era), now SAP Ariba
- Basware on-prem invoice scan-and-capture / P2P (1985 origin)
- Tally / Tally.ERP 9 / TallyPrime (India and South Asia SMB desktop accounting)
- MISA SME accounting (Vietnam desktop accounting)
- Accurate (CPSSoft, Indonesia desktop accounting, now Accurate Online)
- MYOB desktop (AccountRight) in Australia
- Excel spreadsheets and paper/PDF invoice keying layered on top of the ERP

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The dominant procurement/AP cores were built before 2005 as mainframe, midrange or client-server software. SAP R/2 (mainframe, 1979) was followed by R/3, launched 6 July 1992 with a three-tier client/server design. MM (purchasing) and FI (payables) were among its most used modules. JD Edwards WorldSoftware was built in RPG on IBM System/3x and AS/400 in the mid-1980s. Oracle sold applications from the late 1980s. Basware dates from 1985 and Tally from 1986. ([source](https://en.wikipedia.org/wiki/SAP_R/3))
- **S2 slow to replace**: met. SAP pushed the end of Business Suite 7 (ECC) maintenance from 2025 to 2027, with optional extended maintenance to 2030, for customers in 'longer conversion phases'. In one public-sector case, Birmingham City Council started replacing its SAP R/3 finance and procurement system with Oracle Fusion in 2018. The go-live was planned for Dec 2020. As of Jan 2026 the system was still incomplete, and forecast cost had grown from GBP 19M to GBP 144.4M through 2027/28. ([source](https://www.theregister.com/2026/01/29/birmingham_oracle_latest/))
- **S3 workarounds**: met. Ardent Partners' State of ePayables 2025 (204 AP professionals) found that 48.6% of invoices still arrive by manual (non-electronic) means and only 35.4% are processed straight-through. The average exception rate was 18.4%. It says each paper invoice 'must be scanned or manually entered'. Birmingham City Council spent more than GBP 5M on manual workaround labour because its ERP bank reconciliation did not work. ([source](https://d15fjz85703yz4.cloudfront.net/1517/5157/1685/Ardent_Partners_-_State_of_ePayables_2025_-_Bottomline_-_FINAL.pdf))
- **S4 shrinking skills**: met. This is met for the IBM i / RPG slice (JD Edwards World and homegrown AS/400 AP). In Fortra's 2026 IBM i Marketplace Survey (315 respondents), 69% named IBM i skills a top concern, up from 45% in 2020. It was the first time in nine years that skills displaced cybersecurity at the top. The 2024 survey found 89% of IBM i developers use RPG. No primary source was found on ABAP or Oracle EBS skill scarcity. Commentary on SAP's deadline extension (IFS CEO quoted in TechTarget) says there 'aren't the skills or resources available to migrate everyone'. ([source](https://www.itjungle.com/2026/02/02/skills-displaces-cybersecurity-as-top-concern-for-ibm-i-shops/))

## Segments

Enterprise and upper mid-market: SAP ECC (MM/FI-AP), Oracle EBS, PeopleSoft and JD Edwards are the core here. SAP's 2020 release ties the 2027/2030 ECC deadline to its large installed base, and only 13,800 had adopted S/4HANA by then. Mid-market: JD Edwards World/EnterpriseOne on IBM i (RPG) is concentrated in US mid-market manufacturers and distributors. JDE ran on 15% of installed AS/400s. Government: Birmingham City Council ran finance and procurement on SAP R/3 until a troubled 2018-2026 Oracle Fusion replacement. SMB: desktop accounting suites handle purchasing and payables, including Tally (2.5M+ businesses, IN), Accurate (110K+ companies, ID), MISA (VN) and MYOB (AU). Across all segments, Ardent's 2025 survey shows about half of invoices still arrive by non-electronic means.

## Reasons buyers stay

- The ERP is the system of record for the general ledger, vendor master and 3-way match. Ripping out purchasing/AP means touching the core ERP, and Birmingham's SAP R/3 replacement shows what that risk costs.
- Vendors keep extending support: SAP maintenance runs to 2027, optional to 2030, then customer-specific. Oracle extended EBS 12.2 Premier Support repeatedly (per search results, through at least 2036/2037). That removes any forcing deadline.
- Heavy customisation (ABAP, RPG, Oracle Forms) encodes approval rules, tax and local e-invoicing compliance.
- Bolt-on AP automation (capture, workflow) can be layered on top without replacing the core.
- SMBs in IN, ID, VN rely on local tax/e-invoice compliance built into Tally, Accurate and MISA, and accountants are trained on them.
- Migration is multi-year, scarce SI capacity goes to S/4HANA conversions, and finance teams fear period-close disruption.

## Notes

Every source URL listed was opened, with these exceptions. Several primary pages returned 403/404: MCA India bulletin, PSA/DTI Philippines, the SBA Advocacy FAQ, Oracle's lifetime support PDF and blog, and encyclopedia.com on JD Edwards. For IN (1.85M active companies), PH (1.2M establishments, 4,640 large) and MY (1,086,386 MSMEs), the counts come from search snippets of those registers and should be checked before publishing. The Malaysia DOSM PDF was opened but only showed state-level MSME charts. The Indonesia figure is from the 2016 Economic Census (most recent full listing read). Vietnam is from the preliminary 2026 Economic Census reported by VnExpress, citing the NSO. No vendor-disclosed install count was found for SAP ECC, Oracle EBS, JD Edwards World or MYOB. SAP's 13,800 figure (2020) counts S/4HANA adopters, not ECC. Oracle EBS 12.2 Premier Support extensions (through at least 2036/2037) come from search results only, since the Oracle pages were blocked. S4 is sourced for the IBM i / RPG slice (JD Edwards World). No primary source was found for ABAP or Oracle Forms skill scarcity. S3 rests on Ardent Partners' 2025 survey (n=204, sponsored PDF). Its numbers: 48.6% non-electronic invoices, 35.4% straight-through, $9.84 average cost per invoice. The Birmingham council's GBP 5M+ manual workaround spend supports it. Tipalti's 2021 figures are dated. A $200M debt raise and about 10,000 customers in 2025 appeared only in search snippets. Thai and Vietnamese search terms are partly given without diacritics (VN) for search-engine robustness. Use the diacritic forms too, e.g. 'kế toán công nợ phải trả', 'nhân viên mua hàng'.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
