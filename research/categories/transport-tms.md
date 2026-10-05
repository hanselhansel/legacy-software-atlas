# Transport management

Slug: `transport-tms`

## Systems

- Trimble (TMW Systems) TL2000 dispatch on IBM AS/400 / IBM i (5250 green screen)
- Trimble Innovative IES (Innovative Computing Corp.) on IBM i
- Trimble TMW.Suite and TruckMate (Windows client/server)
- McLeod Software LoadMaster and PowerBroker (on-prem carrier and broker TMS)
- Oracle Transportation Management (ex G-Log GC3)
- SAP LE-TRA in R/3 / ECC and SAP TM 9.x on NetWeaver
- Blue Yonder TMS (JDA, from i2 Technologies and Manugistics)
- Manhattan Associates TMS (ex Logistics.com OptiManage)
- Spreadsheets, email and phone for shippers and small carriers with no TMS

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. TMW's TL2000 truckload system ran on IBM AS/400 servers. Version 6.1 for the AS/400 shipped in December 2000. In 2001 TMW's CEO called the AS/400 the platform of choice for a sizeable and growing number of truckload carriers. In 2013 IT Jungle described TL2000 as one of two core IBM i dispatch applications that had relied on 5250 green screens. SAP's LE-TRA shipped in R/3 3.0 in 1993. Oracle OTM descends from G-Log GC3, which predates 2005. ([source](https://www.truckinginfo.com/news/tmw-rounds-out-as400-offerings))
- **S2 slow to replace**: met. Werner Enterprises launched its cloud EDGE TMS (built on Mastery's MasterMind) in 2021. Mastery called it Werner's first cloud-based transportation system. By Q2 2025, four years in, about two-thirds of one-way truckload volume and just over half of dedicated volume had moved, and the migration was still running. Separately, SAP TM 9.6 reaches end of maintenance in 2027, which forces on-prem SAP TM users to migrate to S/4HANA. No source on contract length (7+ years) was found. ([source](https://www.truckingdive.com/news/werner-enterprises-technology-fuel-logistics-growth-q2-2025/758031/))
- **S3 workarounds**: met. Inbound Logistics (2025) says many companies still run transportation on spreadsheets, outdated systems or home-grown tools. A CT Logistics executive quoted there estimates about 7 in 10 shippers use a TMS, so roughly 3 in 10 do not. Re-keying is also documented: Pallet's May 2025 Series B announcement cites a mid-sized carrier that moved 25 employees off repetitive order entry after automating it. Supporting source for the re-keying example: https://www.pymnts.com/news/artificial-intelligence/2025/ai-startups-logistics-pallet-raises-27-million-dollars-scale-automation/ ([source](https://www.inboundlogistics.com/articles/tms-time-to-ditch-the-spreadsheets/))
- **S4 shrinking skills**: met. Major carrier TMS products (TL2000, Innovative IES) still run on IBM i. In Fortra's 2026 IBM i Marketplace Survey, IBM i skills were a top concern for 69% of respondents, up from 45% in 2020. It is now the number one concern for the first time since 2017, with Baby Boomer retirements expected to speed up. Inference for the study: the survey covers IBM i shops in general, not TMS users specifically. No skills data was found for the SAP or Oracle TMS lines. ([source](https://www.itjungle.com/2026/02/02/skills-displaces-cybersecurity-as-top-concern-for-ibm-i-shops/))

## Segments

There are two buyer groups. (1) Mid-market and enterprise for-hire carriers and brokers in North America run carrier TMS products such as McLeod LoadMaster (1,200+ customers), Trimble TMW.Suite / TruckMate, and the IBM i-based TL2000 and Innovative IES (300+ IES users in 2009). Werner, a $2.7B carrier, ran on-prem systems until its 2021 cloud move. (2) Enterprise shippers and large 3PLs run ERP-attached or best-of-breed shipper TMS: SAP LE-TRA / SAP TM, Oracle OTM, Blue Yonder and Manhattan. About a quarter of Oracle GC3 users also ran SAP in 2006. SMB shippers and small carriers mostly have no TMS. About 3 in 10 US shippers run on spreadsheets or parcel portals. In India, SE Asia and the EU, small fleets dominate: 75% of Indian operators own fewer than five trucks, and the EU-27 has 587k road freight firms. These are spreadsheet and WhatsApp workflows more than legacy-TMS replacement. No evidence was found of government agencies as TMS buyers in this category beyond defence logistics, which was not researched.

## Reasons buyers stay

- Carrier TMS products bundle dispatch with settlements, driver pay, fuel tax and accounting (McLeod LoadMaster lists settlements and fuel-tax tools). Ripping one out touches payroll and the general ledger, not just operations.
- IBM i reliability and low run cost. Trimble markets Innovative IES on IBM i for its reliability and data-processing capacity, and offers a web front end instead of a rewrite.
- Vendors keep modernizing the screens in place: the TL2000 Web Edition (2013, Profound Logic) and cloud-hosted TMW.Suite and TruckMate (2019). That lowers the pressure to switch.
- Migration takes years and is risky. Werner's EDGE migration began in 2021 and was still only about two-thirds complete for one-way truckload in 2025.
- For shipper TMS, tight coupling to SAP or Oracle ERP order-to-cash. SAP's path is to move to S/4HANA TM, so many customers re-platform within SAP rather than leave the vendor.
- Years of embedded customization: rating rules, EDI maps and partner integrations to fuel cards and mobile communications.

## Notes

The legacy core here is split. North American carrier TMS shows the clearest legacy signs: TL2000 and Innovative IES on IBM AS/400 / IBM i, still sold by Trimble, which has hundreds of IBM i customers, alongside McLeod's 1,200+ on-prem customers. Shipper-side TMS (SAP LE-TRA from 1993, Oracle OTM from G-Log) is older ERP-attached software, not mainframe software. S4 rests on IBM i skills data that covers all IBM i shops, not TMS users specifically. S2 is shown by one public case (Werner, 2021-2025+ and still in progress). No contract-length data was found. Gaps: several primary pages returned 403, including the FMCSA Pocket Guide, ai.fmcsa registration statistics, the BPS national publication, the Rose Rocket and Pallet BusinessWire releases, and ttnews / sdcexec for G-Log. US carrier counts come from a search-result summary of the MCMIS census, not a rendered page. No official buyer counts were found for SG, MY, PH or ID nationally. The TH figure is from 2007, and the IN figure is from industry research, not a register. For the EU, 586,850 road freight enterprises (2022) was read directly from the DG MOVE pocketbook table. In emerging Asian markets the incumbent is mostly spreadsheets, phone and WhatsApp rather than a legacy TMS, so challengers there (Kargo, Locus) are greenfield. A San Francisco firm also named Kargo raised a $42M Series B in December 2025. It is a different company from Indonesia's Kargo Technologies, so do not conflate the two. Vendor first-ship years for LoadMaster, TL2000, GC3 and Blue Yonder TMS were not found in primary sources.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
