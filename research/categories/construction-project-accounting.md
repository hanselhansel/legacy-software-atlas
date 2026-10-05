# Construction project accounting

Slug: `construction-project-accounting`

## Systems

- Sage 300 Construction and Real Estate (formerly Timberline Office), Windows client-server on Pervasive/Actian Zen database
- Trimble Viewpoint Vista (US/global construction ERP, SaaS and client-server)
- Trimble Viewpoint Spectrum (formerly Dexter + Chaney)
- Trimble Viewpoint Jobpac Connect (ANZ, formerly Jobpac)
- Foundation Software (FOUNDATION construction accounting)
- CMiC (Computer Methods International Corp) single-database construction ERP
- Computer Guidance Corp eCMS (runs exclusively on IBM i / OS/400)
- Jonas Construction Software and other Constellation/Jonas construction brands
- Access Coins / COINS (UK and Ireland, Progress OpenEdge ABL based)
- Generic tier-one ERPs used by large contractors (Oracle E-Business Suite 11i/R12, SAP), plus UK tier-two Eque2, RedSky, Causeway

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Core products predate 2005 and remain on-prem client-server. Timberline/Sage 300 CRE dates from 1971 (ERP Advisors). Sage's own KB says the product runs on the Pervasive/Actian database engine, warns that VPN links can lock files and damage data, and recommends RDP for cloud hosting. CGC eCMS runs only on IBM i (OS/400) midrange (IT Jungle). CMiC dates from 1974 and Viewpoint from 1976. Trimble's 2018 8-K still described Viewpoint as selling client-server solutions. ([source](https://us-kb.sage.com/portal/app/portlets/results/viewsolution.jsp?solutionid=224924150049477))
- **S2 slow to replace**: met. Construction News (2019) reports the top 10 UK contractors spent GBP 451m on software over a decade. Kier's Oracle ERP was budgeted at GBP 30m, ended near GBP 90m with delays and GBP 7.3m of writedowns. Balfour Beatty took a GBP 21m writedown. Interserve abandoned a group-wide rollout with a GBP 17m writedown. This shows multi-year, failure-prone replacement at large contractors. No source found for 7+ year contract terms. Mid-market Vista projects are quoted at 6 to 12 months (search snippet, not verified), so the evidence applies mainly to enterprise. ([source](https://www.constructionnews.co.uk/tech/progress-at-what-cost-24-10-2019/))
- **S3 workarounds**: met. Vendor-sourced evidence only. Field Materials markets an AI layer for Viewpoint Vista that removes manual re-keying of POs, packing slips and AP invoices into Vista, and says it replaces spreadsheet workarounds. Siteline's funding post calls subcontractor billing manual, error-prone and paper-ridden, and says these workflows were run in spreadsheets. No independent survey (e.g. CFMA) could be opened. The CFMA event page returned 403. ([source](https://www.fieldmaterials.com/integrations/viewpoint-vista))
- **S4 shrinking skills**: met. This holds only for some products. A COINS ERP Developer post (Square One Resources, Aug 2026) requires Progress OpenEdge ABL plus hands-on COINS experience, and says the client wants an expert from day one, not someone willing to learn the system. That signals a thin talent pool. CGC eCMS runs only on IBM i, an RPG-era platform. The large US mid-market products (Sage 300 CRE on Actian/Pervasive, Vista on Windows/SQL) do not depend on scarce languages. For them the scarce skill is product-specific admin and report-writing knowledge, which no source quantifies. ([source](https://freehire.me/jobs/coins-erp-developer-square-one-resources-nxrazmwz))

## Segments

Mid-market and enterprise contractors are the core users. Small firms use them too, government much less. AppsRunTheWorld's tracked Sage 300 CRE users are 49.5% 0-100 employees and 48% 101-1,000. Tracked Vista users are 58.6% mid-market (101-1,000), 33.2% small and 8.2% large or enterprise. Trimble said Viewpoint served 46% of the ENR 400. CMiC claims about a quarter of the ENR 400. CGC eCMS targets contractors with $250M+ revenue. Foundation targets small to mid labour-intensive contractors. In the UK, tier-one contractors (Kier, Balfour Beatty) run Oracle or SAP, and the tier-two/homebuilder segment runs COINS (43 of top 75 homebuilders), Eque2, RedSky and Causeway. Government owners use these products little; public works agencies more often use generic public-sector ERPs. No source was found on public-sector use. The buyer base is extremely fragmented: 94% of EU construction firms are micro, and 98% of AU firms have fewer than 20 staff. So the addressable legacy base is the small slice of medium and large firms (e.g. 1,176 large plus 27,254 medium firms in Indonesia).

## Reasons buyers stay

- Job costing, payroll and union/certified payroll are embedded in decades of data. Construction payroll (prevailing wage, union fringes, multi-state) is hard to replicate.
- Failed enterprise ERP replacements are well publicised: Kier's Oracle project grew from GBP 30m to about GBP 90m, and Interserve abandoned its rollout with a GBP 17m writedown.
- The Trimble Viewpoint, Sage and Access Coins ecosystems sell bolt-on modules and hosted versions, so customers can move to cloud hosting without re-platforming.
- Point solutions (Field Materials, Siteline, Briq) sit on top of Vista and Sage 300 CRE, which lowers pressure to replace the core.
- Some vendors (e.g. CMiC) still support on-premise deployment, and construction tolerates on-prem more than most industries.
- WIP schedules, surety and bonding reports, and auditors' CFMA-style reporting are built around existing report formats.
- Thin margins (Vietnam contractors under 10% gross) and cyclical cash flow limit IT budgets.

## Notes

Several key pages could not be opened: sage.com (403), GeekWire, ENR, Forbes/CMiC, BusinessWire/COINS, PSA and CEIC (403). Where a figure came only from a search snippet, the field says so. Vendor customer counts are mostly vendor claims. Foundation's 43,000 counts users, not companies. Access Coins' 130,000 counts professionals. Viewpoint's 8,000 customers is from Trimble's April 2018 8-K. AppsRunTheWorld counts (713 Sage 300 CRE, 756 Vista) are third-party samples, not installed bases.

Southeast Asia and India gap: no dominant pre-2005 construction-specific legacy product was found for ID, VN, MY, TH, PH or IN. In those markets contractors appear to run SAP or Oracle (large SOEs and listed contractors), generic local accounting packages, or spreadsheets. Researching local vendors there is a priority next step.

Buyer-universe counts are firm counts, not qualified buyers. Medium and large firms are the realistic market for project-accounting ERP (e.g. Indonesia 1,176 large plus 27,254 medium firms; EU large firms employ 1.83M).

Weak points: Vietnam's count is a 2013 figure, Thailand's is unverified (paywalled), and India uses a single NIC code proxy. S3 rests on vendor marketing (Field Materials, Siteline) rather than an independent survey. S4 holds for COINS (Progress ABL) and CGC eCMS (IBM i) but not for the larger Windows/SQL-based US mid-market products.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
