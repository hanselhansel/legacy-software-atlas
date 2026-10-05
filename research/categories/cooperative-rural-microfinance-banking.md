# Cooperative, rural and microfinance banking (core + ERP for small lenders)

Slug: `cooperative-rural-microfinance-banking`

## Systems

- Jack Henry Symitar Episys (US credit unions)
- Jack Henry SilverLake, CIF 20/20, Core Director (US community banks)
- Fiserv credit union cores: DNA, Portico, XP2, Spectrum, CUSA, Galaxy, Charlotte, CubicsPlus, OnCU, Reliance and others
- Fiserv Premier and Signature on IBM i (AS/400) for community banks
- Atruvia agree21 (German Volksbanken and Raiffeisenbanken)
- InfrasoftTech (now Kiya.ai) OMNIEnterprise CBS (Indian co-operative banks)
- NABARD-led common national ERP for PACS (India)
- USSI IBS Core (Indonesian BPR/BPRS, koperasi, LKM, LPD)
- PT Sinergi Prakarsa Utama ARB+ (Indonesian BPR)
- In-house or local PowerBuilder, Delphi and FoxPro client-server BPR cores (Indonesia)
- Local Philippine rural-bank CBS vendors listed by RBAP: Byte per Byte, CoreServ, 3i Infotech, Kris Finsoft, MB Philippines, Rural Net, TIM, Sagesoft, SSCGI, CyberSysDOTNet, Entheos IT
- Excel, paper ledgers and manual MIS at microfinance institutions

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. These lenders run cores built before 2005 on midrange or client-server platforms. Fiserv's Premier core runs on IBM i (AS/400). Fiserv acquired it in 1995 with ITI, and by 2009 it served about 2,000 customers, using COBOL and DB2 layers. Jack Henry's Episys was already serving over 560 credit unions by the FY2011 10-K. In Indonesia, USSI's BPR core grew out of a 1994 Bandung co-op accounting software shop, and a practitioner reports that many BPRs run PowerBuilder-based cores (https://www.linkedin.com/pulse/powerbuilder-susah-mati-zulmach-). ([source](https://www.itjungle.com/2009/12/08/fhs120809-story01/))
- **S2 slow to replace**: met. Jack Henry's FY2021 10-K says outsourced core customers typically sign contracts of seven or more years, with per-account fees and minimum guaranteed payments. Atruvia needed three years and 60 series migrations to move 341 German cooperative banks and entities (about 21.5M accounts) onto agree21 (https://atruvia.de/pressemitteilungen/17-02-2020-nach-drei-jahren-serienmigration-nutzen-jetzt-alle-volks-und-raiffeisenbanken-ein-gemeinsames-it-verfahren). India's PACS ERP rollout is a five-year programme (2022-23 to 2026-27). Counter-evidence: Fiserv's FY2013 10-K says its account processing contracts generally run three to five years. ([source](https://www.sec.gov/Archives/edgar/data/779152/000077915221000073/jkhy-20210630.htm))
- **S3 workarounds**: met. TechCrunch (2015) reports that the microfinance institutions Oradian targets ran on legacy software such as Temenos, Excel spreadsheets, or pen and paper. In the Philippines, PearlPay's CEO said 94% of rural banks lack access to e-money, and BHF Rural Bank's pilot was described as the first Philippine rural bank on cloud core banking (https://technology.inquirer.net/86869/financial-technology-startup-targets-rural-banking-sector). Vietnamese People's Credit Funds still lack customer information management systems comparable to commercial banks (https://thitruongtaichinhtiente.vn/hieu-qua-cua-quy-tin-dung-nhan-dan-trong-hoat-dong-tai-chinh-vi-mo-23801.html). Caveat: much of this is vendor-sourced. A MIX/CGAP figure (41% of MFIs on manual MIS) appeared only in a search snippet and was not verified. ([source](https://techcrunch.com/2015/05/20/oradian/))
- **S4 shrinking skills**: not met. No source found that is specific to this category's systems (Episys PowerOn, IBM i RPG and COBOL cores, PowerBuilder or FoxPro BPR cores). Sector-wide evidence exists: BizTech (Apr 2025) reports that 71% of IT leaders say mainframe teams are understaffed and that COBOL engineers are retiring (https://biztechmagazine.com/article/2025/04/how-financial-services-companies-can-maintain-mainframes-cobol-experts-retire). The ILO-OJK study names internal staff's lack of technology knowledge as a main barrier for Indonesian BPR/BPRS, but that is a user-skills gap, not scarcity of legacy-language programmers. Left false pending category-specific evidence. ([source](https://www.ilo.org/resource/news/joint-study-ilo-and-ojk-reveals-urgent-need-digital-transformation-rural))

## Segments

These lenders are SMB and lower mid-market by asset size, with a government-led segment in India and the Philippines. US: 4,287 credit unions plus community banks served by Jack Henry and Fiserv. Episys spans credit unions from $3M to $25B in assets. Indonesia: about 1,500 BPR/BPRS that must hold Rp6bn minimum core capital, mostly on local vendors (USSI over 300 BPR, Sinergi ARB+). India: government-run PACS computerisation (67,930 sanctioned) plus 1,457 UCBs, 57.5% of them Tier 1 (smallest). Philippines: a BSP-funded programme (M-2026-042) subsidises rural banks moving to SaaS cloud cores (https://fintechnews.ph/73196/cloud/bsp-rural-banks-cloud-core-banking/). Germany: cooperative banks are already consolidated onto one group utility (Atruvia), which reduces greenfield demand. SG and MY: small credit co-ops (22 in SG; 549 credit and banking co-ops in MY) running mostly ERP- or accounting-grade systems (no vendor evidence found).

## Reasons buyers stay

- Outsourced core contracts typically run 7+ years with minimum guaranteed payments, so exit is expensive (Jack Henry FY2021 10-K)
- Full migrations take years, even inside a captive group: three years for 341 German co-op banks onto agree21
- Technology cost is the top barrier for Indonesian BPR/BPRS, and fewer than 28% partner with tech firms (ILO-OJK 2023)
- Internal staff lack the skills to adopt new technology (ILO-OJK 2023)
- New rules require data centres and DR sites in Indonesia and formal IT governance (POJK 34/2025), which favours incumbent local vendors and on-shore hosting
- Group or government mandates fix the platform: Atruvia for German Volks- und Raiffeisenbanken, the NABARD common ERP for Indian PACS
- Vendors bundle regulatory reporting (POJK compliance) into the core, which raises switching risk

## Notes

The evidence is strongest for the US (Jack Henry and Fiserv filings), Indonesia (ILO-OJK study, POJK 34/2025, USSI profile) and India's PACS programme. It is weakest for TH, VN, SG, MY and AU, where no vendor-disclosed core banking install counts for co-ops were found. Secondary sources were used where primary ones failed. PIB, RBI and Business Standard pages returned 403. The BusinessWorld item on the BSP rural-bank cloud programme returned 403; the fintechnews.ph summary of BSP Memorandum M-2026-042 was used instead. That memo funds up to three years of SaaS subscription after an implementation of up to six months. The Indian PACS figures are now partly verified via indiancooperative.com (secondary), not the Ministry site. The Indonesian BPR count (about 1,345 BPR plus 173 BPRS, mid-2025) came from search snippets of OJK and Bisnis.com, not from the OJK PDF itself. OJK expects consolidation toward about 1,000, which shrinks the buyer pool but forces migrations. ILO-OJK study: 865 BPR and 77 BPRS sampled, tech partnership below 28%, launched 10 Aug 2023. POJK 34/2025 was announced 8 Jan 2026 and takes effect one year after promulgation; it covers IT governance, architecture, third-party risk and on-shore data and DR centres. Germany is a captive market: all Volksbanken and Raiffeisenbanken run Atruvia agree21. S4 is left false because no category-specific skills-scarcity source was found. Fiserv's FY2013 10-K cites 3 to 5 year account-processing contracts, against Jack Henry's 7+ years for outsourced cores. Open-source Apache Fineract/Mifos is a further option for MFIs but was not researched.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
