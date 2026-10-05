# Manufacturing ERP

Slug: `erp-manufacturing`

## Systems

- SAP ERP / ECC 6.0 (R/3 lineage, ABAP, on-prem client-server)
- Infor XA (ex-MAPICS, IBM i, RPG)
- Infor LX (ex-BPCS, IBM i, RPG/AS-SET)
- Infor LN (ex-Baan)
- JD Edwards World (IBM i, RPG) and JD Edwards EnterpriseOne
- QAD Enterprise Applications (ex-MFG/PRO, Progress 4GL)
- Epicor ERP / Vantage / Vista lineage (now Kinetic)
- Plex (cloud manufacturing ERP/MES, now Rockwell)
- IBM i (AS/400) midrange platform running RPG manufacturing ERP

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Every core manufacturing ERP above first shipped well before 2005 as midrange or on-prem client-server software. MAPICS (now Infor XA) shipped in 1977 on IBM System/34-38 and AS/400 in RPG. BPCS (now Infor LX) dates from the early 1980s on IBM i. JD Edwards World ran on System/38 and then AS/400. SAP R/3 launched in July 1992 and ECC 6.0 in 2006 on the R/3 base. QAD's suite is written in Progress 4GL. ([source](https://en.wikipedia.org/wiki/Infor_XA))
- **S2 slow to replace**: met. DSAG survey (198 senior leaders, Dec 2025 to Jan 2026): only 37% of ECC users expect to be on S/4HANA by the 2027 deadline. Nearly half plan to finish by end-2030, and 4% target 2033 or later. The DSAG chairman blames landscape complexity, skills shortages and budgets. SAP has stretched ECC support three times: mainstream to 2027, extended to 2030 at a 2-point premium, then a private-edition transition option to 2033. Panorama's 2024 ERP Report gives a 15.5-month median for a single implementation. The multi-year signal comes from the ECC migration programmes, not from individual projects. ([source](https://www.theregister.com/2026/02/27/dsag_ecc_sap/))
- **S3 workarounds**: met. Qlector research (June to Sept 2025): 50% of companies still use Excel or paper planning to supplement their ERP. Excel is used for shift-level micro-scheduling. Caveats: Qlector is a vendor, and the sample was a small set of large Slovenian manufacturers. No regulator or large-sample primary source was found. ([source](https://www.qlector.com/resources/insights/how-leading-manufacturers-plan-production-50-still-depend-on-excel-and-paper))
- **S4 shrinking skills**: met. 2026 Fortra IBM i Marketplace Survey, as reported by LiminalArc: 69% of shops name IBM i skills their top concern, ahead of security for the first time in nine years. 91% still run RPG in production. 72% of IBM i developers are over 50 and about 36% are over 60. 21% of shops rely on just 3 to 5 developers. This is the platform under MAPICS/XA, BPCS/LX and JDE World. The Fortra primary page returned 403, so the secondary report is cited. ([source](https://www.liminalarc.co/2026/08/the-rpg-skills-cliff/))

## Segments

Enterprise: SAP ECC is the enterprise legacy core. The ASUG survey (173 members) found about two-fifths of Americas SAP users not yet live or moving to S/4HANA. DSAG found about half of German-speaking ECC users will run past 2027 (theregister.com 2025-11-05 and 2026-02-27). Mid-market: Infor LN (1,500+ discrete manufacturers per infor.com), QAD (about 6,000 sites per its 2009 10-K, Fortune 1000 and mid-market), Epicor (20,000+ manufacturers, discrete mid-market per erpresearch.com), and IBM i RPG systems (Infor XA/LX, JDE World). These sit mostly with mid-market and lower-enterprise discrete manufacturers. SMB: smaller manufacturers mostly run spreadsheets or entry-level accounting systems rather than legacy ERP, which is why Katana, Fulcrum and Odoo target them. Government: not a meaningful buyer segment for manufacturing ERP; state-owned manufacturers in VN, ID and IN are the exception, and no source was found quantifying them.

## Reasons buyers stay

- Business process change is the top barrier to leaving ECC (49% of ASUG respondents). Customizations come second (44%) and organizational inertia third (37%).
- Vendors keep extending support: SAP ECC mainstream runs to 2027, extended to 2030 at +2 points, and a private-edition transition option to 2033. JD Edwards EnterpriseOne premier support runs to 2033.
- Migration capacity is short. DSAG cites skills shortages, parallel transformation projects and budget limits as reasons to delay.
- Deep shop-floor integration (MES, PLCs, EDI with OEM customers, quality and traceability records) makes cutover risky for plants that cannot stop production.
- Sunk cost and stability: decades-old RPG/Progress systems work, and replacement implementations still have a median of 15.5 months (Panorama 2024).

## Notes

Gaps and caveats:
(1) Indonesia and Vietnam buyer counts are not verified from official registers. The BPS and NSO pages returned 403 or timed out. The VN figure comes from a private database.
(2) The India ASI and Philippines ASPBI counts are relayed through a secondary summary or a search snippet, because the official PDFs were unreachable.
(3) S4 rests on the Fortra 2026 IBM i survey as reported by LiminalArc, since Fortra's own page returned 403. It applies to IBM i/RPG systems (Infor XA/LX, JDE World), not to SAP ABAP.
(4) S3 evidence is weak: a vendor (Qlector) survey of a small sample of Slovenian manufacturers. A stronger large-sample source is still needed.
(5) S2 relies on the length of SAP ECC migration programmes and support extensions (2027, 2030, 2033). Panorama 2024 gives a 15.5-month median for single ERP implementations, so 'multi-year' holds for large ECC estates more than for SMB projects.
(6) No vendor-disclosed current SAP ECC customer count was found in an opened source. The figure of about 35,000 ECC customers (Gartner) appears only in search snippets.
(7) Epicor's own about page returned 403. Its customer count (23,000+, or 20,000+ manufacturers) comes from third-party summaries.
(8) Most AI-native ERP startups (DualEntry, Rillet, Campfire) are finance-first, not manufacturing. Doss positions itself as an overlay on existing ERPs, not a full manufacturing ERP replacement.
(9) No SEA-headquartered manufacturing-ERP challenger with disclosed funding was found.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
