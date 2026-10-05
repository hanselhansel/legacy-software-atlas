# Trade finance

Slug: `trade-finance`

## Systems

- China Systems Eximbills (Wang VS, then AS/400, PC LAN, DEC VAX, Java EE from 2002)
- Surecomp IMEX (mainframe and UNIX back office), plus DOKA-NG, allNETT, IBSnet
- Finastra Trade Innovation (formerly Misys Trade Innovation / TI Plus) with Trade Portal
- CGI Trade360 (hosted trade processing, about 25 years in operation)
- Oracle Banking Trade Finance / FLEXCUBE trade modules (named here, no customer count found)
- In-house mainframe LC/collections modules inside core banking (no source found to count them)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Eximbills was first built around 1983 on Wang VS. It then moved to AS/400, PC LAN and DEC VAX, and only added Java EE in 2002. Surecomp's IMEX is still listed as available on mainframe and UNIX platforms (Capterra and banking-gateway vendor profile). Finastra's Trade Innovation was live at Bank of the West by 2000. All of the dominant engines first shipped before 2005 as on-prem or midrange systems. ([source](https://wikibin.org/articles/china-systems.html))
- **S2 slow to replace**: met. HSBC chose CGI Trade360 for its new global trade platform on 30 April 2019 (https://www.cgi.com/uk/en-gb/news/hsbc-chooses-cgi-as-partner-for-delivery-of-transformational-global-trade-technology-platform). The first two markets (UK and Hong Kong) launched on 7 October 2022, about 3.5 years later, and other markets were still being added after that. Systems stay in place a long time. Bank of the West ran Trade Innovation from 2000 until an upgrade to TI Plus in 2008. A search snippet (page returned 403) says Persia International Bank ran Surecomp IBSnet for more than 15 years before moving to Eximbills. In January 2026, BNI was still migrating nine international locations onto Trade Innovation. ([source](https://www.cgi.com/en/hsbc-launches-digital-platform-that-revolutionises-trade-finance))
- **S3 workarounds**: met. BCG says trade processes remain mostly paper based. It says current OCR only lets staff copy and paste document content into back-end fields, which is re-keying with no step change in efficiency. It says legacy architectures need large effort to adapt even to minor policy changes. ICC's 2018 Global Survey found 52% of banks had not removed paper from document verification at all (https://iccwbo.org/news-publications/news/new-icc-survey-shows-pace-trade-finance-digitalisation/). Societe Generale cites 12-15 days to process a paper L/C and manual checks against about 400 ICC rules. I found no source quantifying spreadsheet use specifically. ([source](https://www.bcg.com/publications/2016/digital-revolution-trade-finance))
- **S4 shrinking skills**: not met. Not met: I found no citable source showing a shortage of the platform skills (COBOL, mainframe) these systems run on. IMEX does run on mainframe and UNIX. A search snippet showed a Surecomp COBOL Developer opening for IMEX, but the posting was closed when opened, so I do not cite it. There is evidence of a domain-skill shortage: ITFA (May 2025) says 26% of trade finance professionals are near retirement, under 15% of banks succeed in hiring early-career staff, and qualified practitioners could fall 43% by 2030. ITFA gives no underlying source for these figures. GTR quotes recruiters saying banks keep seeing the same candidates every year. This is scarcity of trade-operations expertise, not of COBOL or RPG skills. ([source](https://itfa.org/the-silent-crisis-understanding-the-expertise-gap-in-global-trade-finance-operations-may-2025/))

## Segments

Buyers are almost all banks, with heavy concentration at enterprise level. The Fed shows about 90% of US banks report zero commercial LCs, and the top five hold over 75-87% of volume. Mid-market regional banks also run these systems. Disclosed examples are Bank of the West, First Hawaiian, Associated Bank, Bank BTPN Indonesia and Banco Pichincha. Government buyers are state-owned banks and export-credit or specialised institutions. Examples are BNI Indonesia (Trade Innovation, 160+ branches, 2,645 trade customers), SBI India and VTB. I found no evidence of SMB banks running a dedicated trade engine. Corporates are a second, smaller segment: Surecomp sells corporate front-ends (allNETT, RIVO), and Komgo serves 200+ corporates and banks.

## Reasons buyers stay

- In-flight instruments: LCs, standbys and guarantees can run for years, so live books have to be migrated in the middle of their life. The BNI migration was still moving nine international locations in 2026.
- SWIFT MT/ISO 20022 certification and UCP 600/URDG rule handling are built into the incumbents (IMEX is fully SWIFT certified).
- Deep integration with core banking, accounting, AML/sanctions screening, treasury and limits. The vendor factsheet lists all of these integrations.
- Volume is concentrated in a few large banks, so smaller banks see little ROI in replacing a working system.
- Incumbents keep releasing new versions (IMEX 8, TI Plus, the Trade360 SaaS model), which lets banks upgrade in place instead of replacing.
- Replacement can take years. HSBC took about 3.5 years from selecting CGI to the first two markets going live.

## Notes

Category conclusion: trade finance meets the legacy profile on S1 (pre-2005 midrange and mainframe engines), S2 (multi-year replacements, decade-plus tenure) and S3 (paper and copy-paste re-keying). S4 is documented only as a shortage of trade-operations expertise (ITFA, unsourced statistics). I found no citable proof of a shortage of COBOL or mainframe skills for these platforms, so S4 is set to false.

Buyer universe is far smaller than bank counts suggest. In the US, about 90% of banks report no commercial LCs, so trade-active buyers are a few hundred banks globally per country cluster, mostly tier-1 and tier-2 banks and state banks.

Vendor counts are vendor-disclosed and not reconciled. Finastra cites 200+ banks. Surecomp cites 300+ clients in one source and 175+ banks in an older one. China Systems: 500 sites in 1998 per an archived Wikipedia article; the 150+ banks figure is from snippets only. CGI cites 322 bank locations.

Gaps:
- I could not open the Finastra factsheet or press pages (403), the Oracle trade pages (403), RBI lists (CAPTCHA/error), the SBV site or the BOT counts. Secondary sources are used for IN, VN and TH and are labelled.
- Oracle Banking Trade Finance, TCS BaNCS and Intellect are relevant vendors in IN and SEA, but I found no disclosed trade-specific counts.
- Contour (bank-backed LC network) shut down in 2023. I did not verify this in this session.

The challenger pattern is mostly AI document-checking overlays (Traydstream, Conpend, TradeSun) sold through or alongside incumbents (Traydstream partners with Surecomp). No greenfield challenger has shown it can replace a back-office booking engine.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
