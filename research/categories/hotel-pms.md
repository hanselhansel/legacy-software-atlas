# Hotel property management

Slug: `hotel-pms`

## Systems

- Oracle Hospitality OPERA 5.x (on-premise / self-hosted; successor to MICROS-Fidelio)
- MICROS-Fidelio (DOS-era predecessor of OPERA)
- Hilton OnQ (proprietary chain PMS, being retired for HotelKey PEP)
- protel PMS (on-premise and cloud, Germany)
- Agilysys LMS and Visual One (on-premise or hosted)
- Maestro PMS (Northwind; Windows/on-premise or hosted)
- IDS Next FortuneNext (on-premise hotel ERP, India/Asia)
- VHP Visual Hotel Program (PT Supranusa Sindata, server-based, Indonesia)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. OPERA, the dominant chain PMS, was announced by MICROS-Fidelio in the late 1990s as an on-premise system on an Oracle database, succeeding the MS-DOS era Fidelio PMS. It reached maturity in 2002-2003. Hilton's proprietary OnQ was deployed to 2,100+ hotels by Q4 2003. Maestro dates to CHS Front Office (1984) and CHS2000 (1994), and protel was founded in 1994. All are pre-2005 on-premise or client-server cores. ([source](https://mastelhospitality.com/news/evolution-opera-pms-oracle-hospitality/))
- **S2 slow to replace**: met. In April 2023 Hilton said it would replace its legacy PMS at more than 7,000 hotels over the following three years, after a rollout that began in early 2022. Hyatt is moving 1,000+ properties from on-premise OPERA V5 to OPERA Cloud and has not published an end date. Oracle said in 2023 that most of its 40,000+ properties were still on old or on-premises systems. It expected Cloud adoption to take about three years. Consultants say group migrations take years, with 6-12 weeks of preparation per property. One counter-example: Motel One moved 100+ hotels in four months. No source was found on contract lengths of 7+ years. ([source](https://stories.hilton.com/releases/hotel-key-partnership))
- **S3 workarounds**: met. One source says manual accounting entry from the PMS is the norm at 20-80 room properties. After the night audit, staff export a report to a spreadsheet and re-key the totals into QuickBooks or Xero. OPERA 5 migration guides add that custom reports must be rebuilt and that point-to-point OXI/SFTP interfaces have accumulated over years. A Caribbean survey found 35% of top processes were mostly manual. The evidence is industry and vendor commentary, not a regulator or a large survey in the target regions. ([source](https://hoteltechinsight.com/2026/04/19/hotel-pms-accounting-software-integration-guide-2026/))
- **S4 shrinking skills**: not met. No source found that the skills for these systems are scarce. They run on Oracle DB, Windows and .NET-era stacks, not COBOL or RPG. There is a general shortage of tech talent in hospitality, from pay competition and the industry's image, but the EHL source says nothing about legacy-system skills specifically. Oracle ended OPERA 5.5 Premier Support in Oct 2021, and OPERA 5.6 Premier Support runs to Dec 2027 with no Extended Support tier. That is vendor-driven obsolescence, not proof of a shrinking skills pool. ([source](https://insights.ehl.edu/recruiting-tech-talent-hospitality))

## Segments

Enterprise: global chains are the core of the legacy installed base. Hilton ran its proprietary OnQ at 2,100+ hotels from 2003 and is replacing it at 7,000+ hotels. Hyatt (1,000+ properties) and Marriott run OPERA V5, and Oracle said in 2023 that most of its 40,000+ OPERA properties were on old or on-premise versions. Mid-market: independent groups, resorts and casino hotels run on-premise protel (14,000+ hotels), Agilysys LMS/Visual One (100 to 7,000+ room properties), Maestro, IDS Next FortuneNext (India) and VHP (Indonesia). SMB: properties of 20-80 rooms often run a basic PMS plus spreadsheet re-keying into accounting, and challengers like Cloudbeds and Hotelogix target this group. Government: no source found showing government agencies as material PMS buyers. Some state-owned hotel operators exist (e.g. ITDC in India), but none was verified.

## Reasons buyers stay

- Deep interface webs: each OPERA 5 OXI/SOAP connection (POS, door locks, PBX, revenue management, CRS) must be re-certified on OHIP, and 'the slowest third party sets the pace' (chatlyn migration guide)
- Custom reports must be rebuilt, since OPERA Cloud standard reports differ from V5 output
- Cutover risk: check-in, payments and housekeeping updates can pause during migration, so it must be scheduled at low occupancy
- Brand standards: chains mandate the PMS, so franchisees cannot switch on their own
- Data quality: duplicate guest profiles and years of inconsistent use migrate as-is unless cleaned first
- Training cost and staff turnover: Hilton cited cutting PMS training from 40 hours to 4 as a benefit, which shows how expensive retraining is
- Vendor still supports on-premise: OPERA 5.6 Premier Support was extended to Dec 2027, which removes urgency

## Notes

The legacy story here is about on-premise and client-server systems, not COBOL. The core products shipped pre-2005: OPERA (late 1990s on Oracle DB), Hilton OnQ (2003), protel (1994) and Maestro (CHS2000, 1994). Replacement runs over years: Hilton's is a three-year program for 7,000+ hotels, Oracle's own Cloud migration is multi-year, and OPERA 5.6 Premier Support ends Dec 2027. S4 is not met because no source shows scarce skills for these systems. S3 rests on industry commentary rather than primary surveys.

Buyer-universe counts mix definitions: licensed hotels (SG, MY, TH), star-rated or classified hotels (ID, IN), statistical establishment counts (US, EU, UK) and all accommodation (VN). They are not directly comparable. No verified current national count was found for the Philippines or Australia.

Sources that failed to load: OPERA's 1998 launch press release (hotel-online 404, hospitalitynet 403), the Oracle Marriott press release (403), Cloudbeds' latest property count (PhocusWire 403) and Hotelogix funding (Business Standard 403). Those claims carry the caveats noted in each field. One philippines.travel link redirected to an unrelated third-party domain and was not followed. ABS 2015-16 data is a useful adoption signal: 84.1% of Australian hotels, motels and serviced apartments (15+ rooms) used a PMS. Census CBP for US needed an API key, so BLS QCEW was used instead.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
