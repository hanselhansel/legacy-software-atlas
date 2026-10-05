# Licensing, permits and case management

Slug: `gov-licensing-permits`

## Systems

- Accela Civic Platform / Accela Automation, plus Tidemark Advantage (Tidemark founded 1984; Accela put it on 'life support' in 2014) and Permits Plus (from Sierra Computer Systems)
- Infor Public Sector (formerly Hansen) building permits, licensing and code enforcement
- Tyler Technologies EnerGov (Enterprise Permitting & Licensing)
- CentralSquare Naviline (formerly SunGard/H.T.E.) community development modules on IBM iSeries/AS/400 with DB2
- Granicus Amanda (formerly CSDC / Calytera, CSDC founded 1989; not checked against a primary source here)
- Idox Uniform, Acolaid and Tascomi (UK planning, building control, licensing back office)
- NEC Software Solutions (formerly Northgate) M3, iLAP and Assure (UK land and property)
- Civica APP, Agile APAS, DEF MasterGov (smaller UK planning systems)
- Infor Pathway (Australia and New Zealand council property and regulatory)
- In-house mainframes, such as NYC Department of Buildings BIS, which DOB NOW is replacing
- National platforms in Asia: Singapore CORENET 2.0 (being replaced by CORENET X), Indonesia OSS-RBA with SIMBG, Philippines DICT eBPLS/iBPLS

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Branson, MO's ERP RFP says the city has run the Naviline/CentralSquare suite on an AS/400 for twenty years, on a DB2 database on an IBM iSeries AS400 server. Its functional areas include planning, permitting and code enforcement. Supporting evidence: NYC DOB describes BIS as a mainframe that DOB NOW will replace (nyc.gov/site/buildings/industry/building-up.page). Tidemark was founded in 1984 (govcon.com). The UK Catapult report says legacy planning software typically runs a local client with document management on a local server. ([source](https://bransonmo.gov/DocumentCenter/View/16403/ERP-System-RFP-2666-13-?bidId=))
- **S2 slow to replace**: met. California State Auditor Report 2014-116 on BreEZe, the Department of Consumer Affairs licensing and enforcement system. It was proposed in 2009 at $28M. By January 2015 it had cost $96M. Phase 1 (10 entities) finished in October 2013 and phase 2 (8 entities) was planned for March 2016. The remaining 19 of 37 planned entities were uncertain or removed. User acceptance testing alone ran 11 months. Supporting evidence: the URA circular says CORENET X will run alongside CORENET 2.0 during a phased cut-over starting 2H 2023 (ura.gov.sg/Corporate/Guidelines/Circulars/dc23-01). ([source](https://information.auditor.ca.gov/reports/summary/2014-116))
- **S3 workarounds**: met. The Connected Places Catapult 2021 critique of UK legacy planning software reports these workarounds: planners find manual workarounds and copy and paste content between programmes (some of this is taught in training). Planning officers manage caseloads in Excel sheets and manual lists rather than the system's tracking tool. Geo-referenced data has to be copied by hand from GIS into planning software. Separately, Branson, MO's Naviline RFP says reports are built in Cognos and external tools such as Microsoft Excel. ([source](https://cp-catapult.s3.amazonaws.com/uploads/2021/01/Transforming-the-digital-architecture-of-planning.pdf))
- **S4 shrinking skills**: met. This applies to the IBM i (AS/400) part of the installed base, such as CentralSquare Naviline (formerly H.T.E.), which Branson, MO runs on iSeries AS400/DB2. In Fortra's 2026 IBM i Marketplace Survey (315 respondents, fielded late 2025), 69% named IBM i skills a top concern, up from 60%. Skills became the top concern for the first time, displacing cybersecurity. Caveat: most Accela, Tyler EnerGov and Idox installs run on mainstream Windows/.NET/Java stacks, so scarce skills are a weaker sign for the category than for core banking. No source specific to permitting COBOL/RPG skills was found. ([source](https://www.itjungle.com/2026/02/02/skills-displaces-cybersecurity-as-top-concern-for-ibm-i-shops/))

## Segments

Almost all buyers are government.
(1) Small local governments, the SMB equivalent: US towns and counties on integrated midrange suites such as CentralSquare Naviline on AS/400. Branson, MO (about 11,400 residents) has run Naviline for about 20 years.
(2) Mid-market cities and councils on Accela, Tyler EnerGov, Idox Uniform, NEC M3/Assure and Infor Pathway. Kansas City paid about $6M (2014) to replace aging permitting software with EnerGov.
(3) Large enterprise jurisdictions: Hansen counted 15 of the 25 largest US cities and counties as customers before the Infor deal (secondary). NYC DOB runs the BIS mainframe.
(4) State and central licensing agencies: California DCA's BreEZe covers 37 boards and bureaus. Singapore's BCA/URA run CORENET. Indonesia's BKPM runs OSS-RBA. The Philippines' DICT supplies eBPLS to LGUs.
In ASEAN the market is more centralised (national platforms) than in the US, UK and Australia, where each local authority buys its own system.

## Reasons buyers stay

- Decades of permit, parcel and case history plus scanned documents sit in proprietary schemas. The Catapult report describes a UK council that judged retrieving its own data from a vendor too risky because of contract complexity, so it chose to upgrade and extend instead.
- Tight integration with finance, utility billing, GIS and cashiering in integrated suites (Naviline, Pathway, Tyler). Replacing permitting alone breaks fee and parcel links.
- Large replacement programmes have failed publicly: California's BreEZe went from $28M to $96M and covered about half its planned scope. This makes councils and boards risk-averse.
- Statutory clocks, fee schedules and local code rules are configured into workflows over years, and must be rebuilt and re-validated.
- Procurement and budget cycles: UK councils often roll Idox Uniform maintenance forward in 3-year extensions (e.g., Tameside 2024-27, Dartford 2025-28, per Contracts Finder search results) instead of re-platforming.
- National mandates in ASEAN (OSS-RBA, CORENET X, eBPLS) set the agenda, so local agencies wait for central integration rather than buy independently.
- Vendor evergreen maintenance models (e.g., Tyler includes upgrades in maintenance) lower the pressure to switch.

## Notes

Open problems:
- Several primary sources were blocked (403 or connection refused) and could not be opened: Anaheim's Tidemark staff report, Oxford City Council's 2024 cabinet report on a 7-year, £1m+ Uniform replacement, Find a Tender and Contracts Finder notices, PSA PSGC pages, BusinessWire and Benzinga Tyler releases, and the CentralSquare Fusion docs. Facts that rest only on search snippets are flagged in the relevant fields.
- Vendor install counts are sparse and old. Accela's last hard number found is 400+ agencies (2001). Hansen's is 470 (2007). Tyler does not split out EnerGov in what was read; the 2014 release says 60+ wins after the acquisition. Idox claims 90%+ of UK local authorities use at least one product. Infor Pathway claims 70+ ANZ councils.
- Granicus Amanda (CSDC) and CentralSquare TRAKiT / Community Plus belong on the list but were not checked against a primary source.

Caveat on the S4 (scarce skills) finding: it rests on IBM i/RPG skills data and applies to the AS/400 part of the base (Naviline/H.T.E.). Most permitting platforms are Windows client-server or .NET, so the case for this category rests on S1-S3 (aged client-server cores, multi-year replacements, Excel and copy-paste workarounds).

ASEAN looks structurally different. Permitting is being centralised in national platforms: Singapore's CORENET X, which replaces CORENET 2.0 from 2H 2023 and is mandatory for large projects from Oct 2025 (per secondary sources); Indonesia's OSS-RBA; and the Philippines' DICT eBPLS, with 906 LGUs signing MOAs by Oct 2022 (per search result). So the legacy-replacement buyer there is often one central agency, not thousands of local ones. Search results also show Indonesian audit findings that OSS-RBA is not integrated with SIMBG and GISTARU, which forces manual steps; the BPK page was blocked.

No AI-native challengers specific to SEA or India were found in this pass.

Buyer counts:
- EU: the CEMR figure (about 100,000) covers all of Europe.
- India: the ULB count comes from a secondary summary of the Local Government Directory.
- Vietnam: only the 34-province figure was opened.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
