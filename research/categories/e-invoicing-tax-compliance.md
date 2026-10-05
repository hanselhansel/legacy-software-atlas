# E-invoicing and indirect-tax compliance (clearance e-invoice, VAT/GST reporting)

Slug: `e-invoicing-tax-compliance`

## Systems

- On-prem ERP tax/e-document layers bolted onto SAP ECC 6.0 (SAP eDocument / Document and Reporting Compliance on ECC); ECC mainstream maintenance ends 31 Dec 2027
- Vertex L Series (mainframe), Q Series and on-prem O Series tax engines
- Sovos (ex-Taxware, founded 1979) indirect tax and e-invoicing
- Thomson Reuters ONESOURCE Indirect Tax (ex-Sabrix, acquired 2009) plus Pagero e-invoicing network (acquired 2024)
- Avalara e-invoicing and live reporting
- EDICOM EDI / e-invoicing VAN
- Government-issued free tools: Indonesia DJP e-Faktur Client Desktop; Malaysia LHDN MyInvois Portal (Excel batch upload); India NIC IRP offline Excel tools (Bulk Generation Tool, GePP)
- Local accounting suites with e-invoice modules, e.g. MISA meInvoice (Vietnam)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The incumbent tax engines date from 1978-1979 and began on mainframes. KPMG says Vertex products moved "from mainframes to PCs and now to the cloud" and calls L Series and Q Series the older architecture. Surety Systems describes L Series as a mainframe deployment being phased out. Vertex was founded in 1978 (10-K). In many enterprises the e-invoice layer still runs on SAP ECC: SAP DRC supports ECC, and ECC mainstream maintenance ends 31 Dec 2027. ([source](https://kpmg.com/us/en/capabilities-services/alliances/kpmg-vertex/upgrade-to-vertex-o-series.html))
- **S2 slow to replace**: met. BDO says a large organisation realistically needs 12 to 18 months at a minimum to scope, procure, configure, test and deploy for the 2026-27 mandates, and that ERP timelines run longer than compliance timelines. Vertex gross revenue retention was 94-95% from 2022 to 2025 (10-K), which shows low churn. Caveat: we found no source showing 7+ year contracts. The multi-year claim rests on the 12-18 month minimum plus ERP coupling. ([source](https://www.bdo.com/insights/tax/the-e-invoicing-readiness-challenge-systems-processes-and-the-hidden-complexity))
- **S3 workarounds**: met. Tax authorities build spreadsheet workarounds into their own platforms. LHDN's MyInvois FAQ (updated 9 Mar 2026) describes Batch Upload as a pre-defined Microsoft Excel spreadsheet: up to 100 documents per file, 25 MB maximum, errors fixed by re-uploading a corrected Excel file. India's GSTN e-invoice leaflet says most IRPs offer reporting via offline tool and online web tool, as well as API. India's IRP offline Bulk Generation Tool is Excel-based. In India, e-invoices cover only about 62-73% of the invoice count reported in GSTR-1 (GST 8-year report). ([source](https://www.hasil.gov.my/media/ccwb1hnj/myinvois-portal-faqs.pdf))
- **S4 shrinking skills**: not met. We found no source showing COBOL/RPG-style scarcity for this category. The closest evidence is general: Deloitte's 2025 Tax Transformation Trends survey (1,000 leaders) found 45% struggle to access specialist AI skills, 42% data analytics skills and 36% specialist tax technical talent. That is a tax-technology talent gap, not a dying-language gap, so the sign is not met. ([source](https://www.deloitte.com/global/en/about/press-room/top-concerns-in-2025-new-deloitte-tax-transformation-trends-report.html))

## Segments

Every segment uses these systems, through different products. Enterprise: Vertex's 4,867 direct customers average about $138k ARR each and include most of the Fortune 500; Sovos and Thomson Reuters ONESOURCE/Pagero serve multinationals running SAP ECC or S/4. Mid-market: Avalara has 43,000+ customers and EDICOM 18,000+. SMB: governments push small firms onto free state tools, such as Malaysia's MyInvois Portal with Excel batch upload (phase 4 is up to RM5m turnover), India's IRP offline Excel tools, and Indonesia's e-Faktur Desktop for all 735k PKP. Local suites also serve SMBs, e.g. MISA, which has 400k+ businesses and households in Vietnam. Government: SAP DRC and Peppol B2G handle public-sector invoicing, and MISA reports 44,500+ public units. Mandates roll out top-down by turnover in MY, IN, SG and PH, so enterprises are compliant first and SMBs are the newest buyers.

## Reasons buyers stay

- Tight coupling to ERP: e-invoice generation sits inside the order-to-cash flow, and BDO notes ERP timelines are longer than compliance timelines
- Regulatory risk: a rejected or uncleared invoice is not a valid tax invoice (e.g. India B2B invoices need a valid IRN), so switching vendors is a risk to revenue
- Vendors bundle tax content updates and country certifications (Peppol access points, India IRPs, Indonesia PJAP, LHDN-recognised providers), and replacements must re-certify
- Low churn shows stickiness: Vertex gross revenue retention is 94-95% (2022-2025)
- Free government channels (MyInvois Portal, India IRP offline tools, e-Faktur Desktop) give SMBs a zero-cost workaround and weaken the case to buy
- SAP ECC end of maintenance (2027, extended to 2030) folds e-invoicing into the larger S/4 program, which delays standalone replacement
- Audit trail, legal archiving and multi-year retention of signed XML tie customers to the incumbent's archive

## Notes

Mandate facts checked against primary sources:
- Malaysia: phases on 1 Aug 2024 (>RM100m), 1 Jan 2025 (RM25-100m), 1 Jul 2025 (RM5-25m) and 1 Jan 2026 (up to RM5m); under RM3m exempt (hasil.gov.my). The Star (Dec 2025) reports the government raising the exemption threshold to RM1m and 111,600 taxpayers live.
- Singapore: GST InvoiceNow applies from 1 Nov 2025 to new voluntary registrants that are newly incorporated, and from 1 Apr 2026 to all new voluntary registrants. Remaining GST-registered businesses follow from 1 Apr 2028 to 1 Apr 2031 by turnover band (IRAS e-Tax Guide PDF, text extracted).
- India: e-invoice threshold is Rs 5 crore aggregate turnover; six IRPs; offline tools (GSTN leaflet).
- Indonesia: Coretax replaced e-Faktur in Jan 2025, then e-Faktur Desktop was reopened to all PKP from 12 Feb 2025 (pajak.go.id).
- Vietnam: Decree 123 mandate from 1 Jul 2022, XML plus digital signature (Fonoa blog, secondary).
- Philippines: RR 8-2022 / RR 11-2025 deadline 31 Dec 2026 (Grant Thornton PH).

Not verified with an opened source:
- UK April 2029 B2B e-invoicing mandate (search results only; Forbes returned 403).
- Thailand's total active juristic-person count.
- Vietnam's active-enterprise total.
- Pagero's founding year.
- SAP DRC's first-ship date.

Other source notes:
- Surety Systems wrongly says O Series is cloud-only, so S1 cites KPMG instead.
- The Vertex 10-K FY2025 shows 4,867 direct customers. A search snippet's 5,425 'direct and indirect' figure was not verified.
- Sovos acquired Flowie (vendor site).
- Vertex acquired ecosio and partnered with Brinta.
- Sovos, Vertex and Thomson Reuters are buying e-invoicing networks, so incumbents are consolidating rather than being displaced.
- In APAC, the main incumbents are often free government portals and Excel tools, not vendor software. The opening for challengers is ERP-to-authority API overlays (PJAP, IRP GSP/ASP, MyInvois intermediaries, Peppol access points).
- S4 is not met: the skills gap is in tax-technology and AI talent, not legacy languages.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
