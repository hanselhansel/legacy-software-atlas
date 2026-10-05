# Real estate property management

Slug: `property-management`

## Systems

- Yardi Voyager (Voyager 5/6 client-server, now 7S/8 hosted SaaS)
- MRI Software (MRI Commercial/Residential Management, Qube in UK; Rockend REST Professional desktop in AU/NZ)
- RealPage OneSite (heritage Rent Roll on-premise systems)
- SAP Real Estate Management (Classic RE in R/3, Flexible Real Estate Management RE-FX in ECC 6.0 / S/4HANA)
- Oracle JD Edwards World / EnterpriseOne Real Estate Management (IBM i / AS400, RPG)
- Aareon GES (German housing-industry ERP run in Aareon data centre until Jan 2021), Wodis Sigma / Wodis Yuneo, RELion
- NEC Housing (formerly Northgate OHMS / SAM-Codeman) and Civica Universal Housing in UK social housing
- Jupix (UK lettings desktop-era software, 20+ years)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. RealPage 10-K: company formed in 1998 to acquire Rent Roll, Inc., which sold on-premise property management systems; first on-demand system (OneSite) only in June 2001. MRI was founded 1971 as Management Reports Incorporated; Rockend 1979 with desktop REST Professional; Yardi's product began on Apple II/DOS in 1984 and Voyager ran as a Windows client-server product before 7S SaaS. JD Edwards World Real Estate runs on IBM i midrange. ([source](https://www.sec.gov/Archives/edgar/data/1286225/000128622521000007/rp-20201231.htm))
- **S2 slow to replace**: met. SAP RE-FX migration guide: SAP ERP 6.0 mainstream maintenance ends 31 Dec 2027 (extended to 2030) and it recommends starting 18-24 months before target go-live, with discovery, prepare, explore/realize, cutover, hypercare phases. Redirect Consulting notes the Yardi Voyager 5 to 6 upgrade 'amounted, effectively, to a whole new implementation'. Brighton & Hove's housing asset management replacement schedule ran from procurement in winter 2021 to deployment in spring 2023 on an interim incumbent contract. No source opened shows 7+ year contracts; evidence is for 18-24 month replacement programmes, so this is a moderate rather than strong signal. ([source](https://re-expect.de/en/sap-re-fx-migration-von-ecc-zu-s-4hana-der-komplette-leitfaden/))
- **S3 workarounds**: met. MRI Software survey (Feb 2018, 219 executives): 42% of commercial and multifamily owners/operators rely at least partly on spreadsheets or paper-based processes; more than 1 in 10 rely on them alone. DigitalStaff describes screen-scraping bots that log into Yardi like a human to extract data when SQL or reports fall short, and cites $20K+ annual extraction fees; AP vendors describe manual line-by-line re-keying of invoices into Voyager. ([source](https://www.mrisoftware.com/news/survey-40-percent-real-estate-companies-spreadsheets-paper-based-processes/))
- **S4 shrinking skills**: met. Applies to the JD Edwards World / IBM i segment of the category, not to Yardi/MRI/RealPage (which run on SQL Server/.NET stacks). ITConvergence: over 50% of organizations report difficulty hiring IBM i and RPG expertise, nearly 1 in 4 expect a critical shortage within three years, 56% of IBM i professionals have 30+ years experience, fewer than 2% of US CS graduates have RPG exposure, and many firms rely on one or two people for their iSeries. ([source](https://www.itconvergence.com/blog/what-happens-when-your-last-iseries-admin-retires/))

## Segments

Enterprise and mid-market dominate legacy use: RealPage (31,700+ clients, 19.7M units, 10-K 2020), MRI (45,000+ clients) and Yardi serve institutional multifamily, commercial and REIT operators; SAP RE-FX and JD Edwards Real Estate sit in large corporates, developers and corporate real-estate departments. Government and quasi-government: UK local authorities and housing associations run NEC Housing (ex-Northgate) and Civica (e.g. Hackney's NEC SAM contract, Royal Greenwich's NEC Housing contract 2025-2030); German housing companies ran Aareon GES until 2021. SMB: in AU, Rockend REST Professional desktop software manages 55% of rentals; MRI survey shows 46% of respondents were firms of 10 or fewer staff and over 1 in 10 firms use only spreadsheets/paper.

## Reasons buyers stay

- Trust accounting and owner/tenant ledgers are regulated (e.g. AU trust accounting, US affordable housing compliance), so cutover risk is high
- Deep integrations: payments, screening, utilities, GL, investor reporting built around the incumbent's data model
- Upgrades within the same vendor already resemble re-implementations (Voyager 5 to 6), so switching vendors looks worse
- Vendors are consolidators (MRI bought Rockend, Qube; Aareon bought Arthur; RealPage bought Buildium), so the 'modern' option is often the same vendor
- Lease abstracts, CAM/recovery rules and custom reports encoded over decades
- SAP RE-FX customers tie the decision to the broader S/4HANA program and its 2027/2030 deadlines

## Notes

Legacy here is mostly first-generation client-server and hosted-but-old platforms (Yardi Voyager, MRI, RealPage heritage, SAP RE, JD Edwards World on IBM i, Aareon GES, UK social housing systems), not mainframe. S4 is met only for the JDE World/IBM i RPG slice; the big US vendors run modern-enough stacks, so skill scarcity is not a category-wide sign. S2 rests on 18-24 month replacement programmes (SAP RE-FX planning, Brighton & Hove, Voyager 5 to 6 re-implementation). No opened source shows 7+ year contracts. Rotherham's 1995 Northgate contract appears only in a search snippet because the council site refused connection. Yardi's own site returned 403, so no vendor-disclosed Yardi customer count; the 20,000 figure is a GetLatka estimate. Buyer-universe counts are weak for ID, VN, TH and PH (no official register count found). US SUSB and AU ABS class counts exist but sit in downloadable data files I did not extract. Consolidation is a recurring pattern: MRI bought Rockend (2019) and Qube, Aareon bought Arthur Online (2021), RealPage absorbed Rent Roll. Several modern challengers end up inside legacy incumbents. AI-native entrants (EliseAI) mostly overlay leasing and resident communication on top of the incumbent PMS rather than replacing the ledger. Few funded APAC challengers: SE Asia plays such as SPEEDHOME are rental marketplaces, not PMS ledger replacements.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
