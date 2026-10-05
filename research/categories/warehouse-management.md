# Warehouse management

Slug: `warehouse-management`

## Systems

- Manhattan Associates WMi / PkMS (IBM i / AS/400, RPG)
- Manhattan Warehouse Management for Open Systems (WMOS, tagged 'Legacy' by Gartner Peer Insights) and Manhattan SCALE (.NET, still sold on-prem)
- SAP ERP Warehouse Management (LE-WM), retiring end-2027
- Blue Yonder (JDA / RedPrairie / McHugh Freeman) Dispatcher WMS
- HighJump Advantage / Körber WMS (now Infios)
- Infor WMS / SCE (from EXE Technologies via SSA Global)
- Hardis Reflex WMS (began on AS/400)
- Oracle E-Business Suite WMS
- Government-built systems, e.g. US DLA Distribution Standard System (DSS)
- Green-screen 5250/VT telnet RF terminal emulation in front of host WMS

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Manhattan's PkMS/WMi is written in RPG on IBM i (AS/400). It dates from 1990, and more than 500 companies still ran it in 2009, including Costco, Nordstrom and Staples. Manhattan kept a large RPG team on payroll. Other cores also predate the cloud: Blue Yonder Dispatcher (mid-1980s), HighJump (1983), Hardis Reflex (1992 on AS/400) and SAP LE-WM (R/3 era). ([source](https://www.itjungle.com/2009/12/15/fhs121509-story02/))
- **S2 slow to replace**: met. The US Defense Logistics Agency is replacing its legacy Distribution Standard System with an SAP-based WMS across 34 warehouses. In 2023 Nextgov reported full modernization was due by the end of FY2025. DVIDS shows site go-lives still running from Navy sites (2024) to Europe (July 2025) to Warner Robins, Oklahoma City and Hill (Feb–Jul 2026). Gartner (via SCDigest) calls WMS among the least upgraded applications, because modifications absorb over 50% of post-implementation TCO. Manhattan's own Active subscriptions typically run five years or more, which is below the 7-year contract threshold. The multi-year proof is the replacement duration. ([source](https://www.nextgov.com/modernization/2023/01/defense-logistics-agency-shift-warehouse-management-commercial-software/381544/))
- **S3 workarounds**: met. Ivanti Velocity converts green-screen telnet WMS screens to Android devices 'without needing to write code or cause disruption to existing WMS or ERP systems'. Ivanti reports more than 16,000 customers and over 5 million devices. Samsung Insights notes much of warehousing still runs on telnet, keyboard-driven green-screen processes. This screen-reformatting (screen-scraping) layer is the standard workaround in front of legacy host WMS. Spreadsheet use is weaker: Wikipedia notes smaller facilities use spreadsheets or pen and paper as their WMS. No fetchable primary survey quantified spreadsheet use alongside a legacy WMS. ([source](https://www.ivanti.com/company/press-releases/2021/ivanti-velocity-a-market-leading-mobile-enterprise-application-software-provides-capabilities-for-further-expansion-to-supercharge-supply-chain-warehouse-operations))
- **S4 shrinking skills**: met. In Fortra's 2026 IBM i Marketplace Survey (315 respondents), 69% of IBM i shops named IBM i skills a top concern, up from 60% in 2025 and 45% in 2020. It is the first time skills have outranked cybersecurity in nine years. This applies directly to RPG-based WMS such as Manhattan WMi/PkMS and AS/400-era Reflex. SAP LE-WM skills are also a dead end because support ends 31 Dec 2027. ([source](https://www.itjungle.com/2026/02/02/skills-displaces-cybersecurity-as-top-concern-for-ibm-i-shops/))

## Segments

Legacy tier-1 WMS (Manhattan WMi/PkMS, SAP LE-WM, Blue Yonder Dispatcher, Infor, Reflex) sits mainly in enterprise and upper mid-market. Named WMi users include Costco, Nordstrom, Staples, Foot Locker and Williams-Sonoma (IT Jungle 2009). Blue Yonder Dispatcher users include Home Depot, Cardinal Health and Costco, plus 3PLs, retailers, manufacturers and SMEs (Socius24). Mid-market and SMB lean on HighJump/Körber (4,000+ customers at acquisition), on ERP-embedded WM, or on spreadsheets and pen and paper (Wikipedia notes smaller facilities use spreadsheets or paper as their WMS). Government is also exposed: the US Defense Logistics Agency runs its 34-warehouse network on the government-built legacy Distribution Standard System and is mid-migration to SAP (Nextgov, DVIDS). In SEA and India the 3PL universe is fragmented and dominated by SMEs: 94% of Thai warehouse operators are MSMEs (Krungsri). Cloud-native vendors (Unicommerce, Anchanto) are winning e-commerce SMBs and mid-market there rather than displacing an AS/400 core.

## Reasons buyers stay

- Deep customization. Gartner (via SCDigest) notes that heavy modifications made WMS among the least upgraded applications, with over 50% of post-implementation TCO spent supporting them.
- Execution risk. A WMS outage stops shipping. DLA's SAP rollout runs site by site, with brown-outs and go-live windows each spanning months.
- Green-screen RF flows are fast and stable, and terminal-emulation modernization (Ivanti Velocity, StayLinked) lets firms reskin them on Android without touching the host WMS.
- Vendors keep legacy lines alive. Manhattan still offers SCALE on-prem via perpetual licenses and historically kept RPG staff for WMi.
- Tight integration with MHE/automation, ERP and carrier systems built over decades, which must all be re-tested on cutover.
- Peak-season constraints limit cutover windows to a few months a year, stretching multi-site programs over years.

## Notes

1) Hard deadline: SAP LE-WM. S/4HANA compatibility use ended end-2025 and SAP ERP WM support ends 31 Dec 2027 (igz, an SAP partner: https://www.igz.com/en/blog/conversion-of-sap-wm-to-sap-ewm/). MWPVL estimates over 5,000 SAP WM warehouse installations. This is the largest forced-migration pool in the category.

2) Gaps. The 'WMS lifespan 15+ years' figure attributed to Gartner's Dwight Klappich appeared only in search snippets (supplychain247/mmh returned 403), so it is not cited as evidence. The Federal News Network articles on DLA's 'COBOL warehouse system' and its rollout start at Corpus Christi in 2018 also returned 403. Those details are unverified here. S2 rests on Nextgov plus the DVIDS go-live dates instead.

3) Weak signs. S2 is met through replacement duration (DLA) and Gartner's 'least upgraded' point. The 7+ year contract test is not met: Manhattan's own cloud contracts run 5+ years. S3 is met through terminal-emulation screen reformatting. A quantified spreadsheet-workaround survey for legacy-WMS users was not found in a fetchable source.

4) Buyer universe. The national registers count warehousing establishments (3PL and storage operators) only. Real WMS buyers also include manufacturer, wholesaler and retailer DCs, so treat these figures as a floor. VN and PH lack an opened primary register figure. ID's Bappebti count covers commodity receipt-system warehouses only. The AU figure is division-level.

5) Customer counts. Vendor-disclosed figures are dated: Manhattan WMi 500+ (2009) and HighJump 4,000+ (2017). The Blue Yonder figure of 2,000+ live sites comes from a partner, not a vendor filing. Manhattan's FY2025 10-K discloses no customer count.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
