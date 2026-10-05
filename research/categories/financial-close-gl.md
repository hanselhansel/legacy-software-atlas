# Financial close and general ledger

Slug: `financial-close-gl`

## Systems

- SAP R/3 / SAP ERP 6.0 (ECC) FI-CO general ledger
- Oracle E-Business Suite General Ledger (Oracle Financials, 11i / R12 / 12.2)
- Oracle PeopleSoft Financials 9.2 General Ledger
- Oracle JD Edwards World (IBM i / AS/400) and JD Edwards EnterpriseOne General Accounting
- Oracle Hyperion Financial Management (HFM) / Hyperion Enterprise for consolidation and close
- Microsoft Dynamics GP (Great Plains Dynamics)
- Infor SunSystems
- Tally (Tally.ERP 9 / TallyPrime) in India and South Asia
- Spreadsheet-based close (Excel) layered on top of the ERP

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The dominant GL cores all first shipped before 2005 as on-prem or midrange systems. SAP R/3 launched in July 1992. JD Edwards World was built on IBM System/38 and then AS/400, and Oracle still documents it as the 'JD Edwards World IBM i' environment. Great Plains Dynamics 1.0 shipped in February 1993 as 32-bit Windows client-server software. Tally dates from 1986. Hyperion Enterprise was named in 1995. ([source](https://en.wikipedia.org/wiki/SAP_ERP ; https://en.wikipedia.org/wiki/JD_Edwards ; https://docs.oracle.com/cd/E59116_01/nav/technology.htm ; https://en.wikipedia.org/wiki/Microsoft_Dynamics_GP))
- **S2 slow to replace**: met. Oracle's Lifetime Support Policy PDF, downloaded and read, gives Premier Support to Dec 2037 for E-Business Suite 12.2, JD Edwards EnterpriseOne 9.2 and Hyperion Financial Management 11.2. It shows JD Edwards World A9.4 on Sustaining Support indefinitely (Premier ended Apr 2022, Extended Apr 2025). SAP set ECC mainstream maintenance to end-2027 with optional extended maintenance to end-2030. Gartner estimated in 2025 that over 60% of SAP customers were still on ECC6 with no move decided, and that about 40% would still run ECC in key areas in 2030. ASUG's 2024 survey (n=208) found S/4HANA migrations average 1.5 years and range up to 6 years, and 46% said the move took more time and resources than expected. Microsoft Dynamics GP support runs to Dec 2029 with security patches to Apr 2031. These are 30-to-40-year product lives, with replacements that take years. ([source](https://www.oracle.com/us/assets/lifetime-support-applications-069216.pdf ; https://news.sap.com/2020/02/sap-s4hana-maintenance-2040-clarity-choice-sap-business-suite-7/ ; https://www.theregister.com/2025/02/12/gartner_sap_maintenance_2030/ ; https://www.asug.com/insights/the-state-of-sap-s-4hana-adoption-trends-successes-and-challenges))
- **S3 workarounds**: met. BlackLine's FY2025 10-K says traditional close processes are heavily manual and rely on error-prone spreadsheets. In Ledge's 2025 close benchmark (vendor survey, n=100), 94% of teams use Excel in the month-end close, 50% say it slows the close, most automate under 40% of it, and 27% take more than 7 business days. A Gartner survey of 497 controllership staff (published Feb 2024, via CFO Dive) found 59% make several errors a month, citing manual work and rushed data review during the close. Rillet's 2025 funding release calls incumbent ERPs databases whose real finance work happens in spreadsheets (a vendor claim). ([source](https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm ; https://www.ledge.co/content/month-end-close-benchmarks-for-2025 ; https://www.cfodive.com/news/half-accountants-make-errors-each-month-gartner-accounting-audit-auditing-PCAOB/708138/))
- **S4 shrinking skills**: met. This sign holds only for the IBM i / RPG segment (JD Edwards World and homegrown AS/400 GLs). Oracle documents JD Edwards World as an IBM i environment. In Fortra's 2025 IBM i Marketplace Survey (via TechChannel), IBM i skills were the second-largest concern at 60% of respondents, up from third the year before. A vendor white paper from ASNA, an RPG migration vendor (Nov 2024), projects the average RPG programmer at about 70 by 2025 and most RPG talent retired by 2030. That is an assumption-based projection, so weight it lightly. No comparable scarcity evidence was found for SAP ABAP or Oracle EBS PL/SQL skills, so S4 is weaker for the SAP and Oracle EBS core of the category. ([source](https://techchannel.com/cybersecurity/fortra-ibm-i-marketplace-survey/ ; https://docs.oracle.com/cd/E59116_01/nav/technology.htm ; https://www.asna.com/en/white-paper/ibm-i-crisis-decade))

## Segments

Enterprise is the core. SAP ECC, Oracle EBS, PeopleSoft and Hyperion HFM are large-company systems. Wikipedia's SAP ERP article cites implementation costs of $50M to $500M for Fortune 500 firms and $10M to $20M for midsize firms. Hyperion was the consolidation system of record for many SAP customers. Mid-market is the second pool. Great Plains' FY2000 10-K defines its market as midmarket firms with $1M to $500M revenue. JD Edwards World and EnterpriseOne and Infor SunSystems (6,000+ customers) also sit here. SMB use is concentrated in Tally (2.5M+ businesses, mainly India) and in GP and older on-prem packages. Government and public sector also run Oracle EBS, PeopleSoft and SAP GLs, but no source counting government installs was opened, so this is unquantified. The buyer-universe counts above are for large and listed firms, which fits the enterprise and upper mid-market focus.

## Reasons buyers stay

- The GL is the audited system of record. Changing it touches SOX/ICFR controls, audit trails and statutory reporting, and migrations run 4 months to 6 years (ASUG 2024).
- Vendors keep extending support. Oracle Premier Support for EBS 12.2, JDE E1 9.2 and HFM 11.2 runs to at least Dec 2037. SAP ECC extended maintenance runs to 2030, with options to 2033.
- Heavy customization. 44% of ASUG members cite customizations and 49% cite business-process change as barriers (The Register, Nov 2025).
- Gartner says many SAP customers cannot build a compelling business case for S/4HANA.
- Local statutory, tax and e-invoicing localizations (e.g. India GST in Tally, SE Asian tax packs) are already built and certified in the legacy product.
- Close-overlay tools such as BlackLine, FloQast and Numeric let firms fix close pain without replacing the GL, which delays a core swap.
- Third-party support (Rimini Street, Spinnaker) and Sustaining Support let firms run frozen versions indefinitely.

## Notes

Method: WebSearch and WebFetch. Several primary pages (Oracle blogs, gartner.com, SBA PDF, SAP history, Bursa Malaysia) returned 403. Oracle's Lifetime Support Policy PDF (oracle.com/us/assets/lifetime-support-applications-069216.pdf) was downloaded with curl and read locally. Its rows show EBS 12.2 Premier Support to Dec 2037, JDE EnterpriseOne 9.2 to Dec 2037, HFM 11.2 to Dec 2037, and JDE World A9.4 with Premier ending Apr 2022, Extended ending Apr 2025, then Sustaining Support indefinitely.

Gaps:
(1) No vendor-disclosed current customer count for SAP ECC, Oracle EBS, JD Edwards or Dynamics GP. A widely repeated figure of about 35,000 ECC customers comes from third-party blogs and is not used.
(2) The Hyperion '12,000 customers' figure is unverified.
(3) The S3 Ledge survey is a vendor survey (n=100). The Gartner error survey was read through CFO Dive because gartner.com returned 403.
(4) S4 evidence applies to the IBM i / RPG (JD Edwards World) segment, not to SAP or Oracle EBS skills.
(5) Buyer universe uses large-firm counts (US, EU, UK, AU) and exchange listings (SG, IN, ID, VN, MY, TH, PH) as proxies. These are not sector-specific registers. The US figure of 21,041 is from a search snippet of the SBA 2026 FAQ, whose page returned 403.
(6) No SE Asia-native AI GL challenger with verifiable funding was found. All challengers listed are US-based and sell mainly to US tech and mid-market companies.
(7) Fortra's 2026 survey reportedly ranks IBM i skills first (69%), but that page returned 403. The 2025 figure (60%, second place) is cited instead.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
