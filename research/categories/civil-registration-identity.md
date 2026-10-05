# Civil registration, vital statistics and national ID systems

Slug: `civil-registration-identity`

## Systems

- US state electronic vital records systems (EVRS/EBRS/EDRS): Genesis Systems COTS suite, Netsmart Vital Records System (VRS, e.g. Wisconsin SVRIS), LexisNexis VitalChek DAVE (renamed VitalIQ in 2024)
- State and municipal mainframe vital-records stacks accessed by TN3270 terminal emulation (Missouri PROD mainframe, being replaced by MoEVR 2.0 from 2026 to 2027) and city mainframe indexes (San Antonio Vital Records)
- Texas TER (legacy Texas Electronic Registrar), replaced by TxEVER on 1 Jan 2019
- Philippines Civil Registry System (CRS-ITP, then CRS-ITP2) run by Unisys under PPP, using Unisys InfoImage imaging
- Philippines PhilCRIS: the Windows successor to the DOS-based CRIS that local civil registry offices use for encoding
- UK GRO England and Wales: the Registration Online (RON) system (local registrars logging since 2009) plus about 270 million microfilmed historic records
- Netherlands GBA, the municipal personal records database in use since 1994. Operatie BRP, its replacement, was cancelled in 2017
- Germany Einwohnermeldewesen (resident registration) software: HSH MESO / VOIS|MESO and AKDB OK.EWO
- Australia state BDM registers: Victoria Lifedata (over 30 years old, patched 1998) and NSW LifeLink (replaced the LifeData system after a project from 2002-03 to 2014)
- Thailand DOPA/BORA central computerized civil registration and population database (1982)
- Indonesia SIAK (Sistem Informasi Administrasi Kependudukan), migrated from distributed district servers (SIAK Terdistribusi) to SIAK Terpusat from 2022
- Vietnam Ministry of Justice shared electronic civil-status software (phần mềm đăng ký, quản lý hộ tịch điện tử dùng chung) and the MPS national population database
- Malaysia JPN registration systems and the MyKad chip platform (IRIS M-COS chip OS, since 2001)
- India Civil Registration System (CRS) software of the Office of the Registrar General of India (ORGI)
- National ID and civil-registry platforms from Thales (Civil Identity Suite) and IDEMIA (e.g. Colombia RNEC platform since about 1997)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. San Antonio's 2020 city audit says Vital Records downloads each day's queue from the state TxEVER system and loads partial data into the city 'Mainframe', which serves as the record index. Mainframe passwords are limited to 4-8 characters with no mixed case. Other pre-2005 cores: Thailand's computerized central civil-registration database dates from 1982 (World Bank case study). The Dutch GBA has run since 1994. Victoria BDM's Lifedata was over 30 years old in 2013. Philippine LCROs use PhilCRIS, the Windows successor to a DOS-based CRIS. Missouri users still reach vital records data through 'Mainframe/TN 3270 Plus' until MoEVR 2.0 arrives. That last point comes from a search snippet only, because the Missouri page returned 403. ([source](https://sanantonio.gov/Portals/0/Files/CityAuditor/Reports/FY2021/AU20-007.pdf))
- **S2 slow to replace**: met. PSA's own presentation: CRS-ITP was a 12-year contract between NSO and Unisys Australia from 23 Dec 1999, extended to 4 Sep 2015. CRS-ITP2 with Unisys runs 12 years, from 30 Sep 2016 to 2028. Unisys has run the Philippine civil registry for close to 30 years over two PPP contracts. Other slow replacements: NSW LifeLink started in 2002-03 and went live in 2014, after the first contractor (UXC) was terminated. The Dutch Operatie BRP ran from 2010 until it was cancelled in July 2017, 33 months late. Wisconsin's WAVE replacement of Netsmart SVRIS was planned as 16 months and slipped from July 2025 to December 2026. ([source](https://getinthepicture.org/system/files/sites/default/files/Philippines-Digital%20Transformation_PSA.pdf))
- **S3 workarounds**: met. San Antonio Vital Records staff download the TxEVER queue every day and upload partial data into the city Mainframe index. Full records go into a separate image viewer, and paper copies of birth records are printed into bound notebooks. This is double entry across systems. UK: in its 2016 inspection, ICIBI found GRO staff pulling records from 270 million microfilmed records by hand and printing them onto paper certificates. Senior managers called the operation 'extremely old-fashioned'. Philippines: LCROs encode paper civil registry documents into PhilCRIS. PSA offices do manual data entry when no PhilCRIS/CRIS file comes with the documents (UNSIAP/NSO training material). ([source](https://sanantonio.gov/Portals/0/Files/CityAuditor/Reports/FY2021/AU20-007.pdf))
- **S4 shrinking skills**: not met. No source found that says skills for civil-registration systems specifically (COBOL, mainframe, DOS CRIS) are scarce. Mainframe use is documented (San Antonio city mainframe, and Missouri TN3270 access per a search snippet). Searches for COBOL job posts tied to vital records found only general Medicaid/MMIS COBOL roles. Those are not evidence for this category. ([source](https://sanantonio.gov/Portals/0/Files/CityAuditor/Reports/FY2021/AU20-007.pdf))

## Segments

Government only. Buyers are national registrars (PSA, JPN, ICA, DOPA, Ditjen Dukcapil, ORGI, UK GRO), state registrars (57 US vital records jurisdictions, 8 Australian BDM registries, Indian Chief Registrars) and municipal or local offices (US city and county vital records such as San Antonio, German Meldebehörden, Philippine LCROs, Vietnamese communes, Indonesian Dinas Dukcapil). Hospitals, funeral directors, medical certifiers and celebrants are mandated users, not buyers. Wisconsin's system has 3,700 business users, and WAVE onboards about 11,000. No SMB, mid-market or enterprise buyer segment exists. PPP concessions such as PSA/Unisys turn the vendor into the operator.

## Reasons buyers stay

- Statute ties legal validity to paper. In England and Wales only a paper certificate or register entry counts as the legal record, so GRO must keep a microfilm-to-paper print operation running (ICIBI 2016)
- Replacement projects have a history of failure: NSW LifeLink took more than 10 years and one contractor was terminated, and the Dutch Operatie BRP was cancelled in 2017 after 33 months of delay with €33M more needed
- Decades of historic records need conversion. Wisconsin's SVRIS Part 2 conversion slipped to April 2026, and its WAVE replacement slipped from July 2025 to December 2026 because data migration was bigger than expected
- Under PPP revenue-share models the incumbent pays the capex and shares citizen fees (PSA/Unisys), so the agency carries little budget pressure to switch
- Vendor-held cryptographic keys and proprietary chip OS create lock-in. MyKad M-COS keys are held only by JPN and IRIS
- Many mandated external users must be retrained and re-credentialed on any new system (hospitals, funeral directors, local registrars, e.g. about 11,000 users in Wisconsin)
- Identity-fraud and security sensitivity makes agencies avoid risk (NSW Audit Office findings on BDM data integrity)

## Notes

No AI-native challenger was found that is replacing civil-registration or vital-records cores. The modern options are open-source DPI (MOSIP, OpenCRVS), biometric/DPI firms (TECH5) and cloud COTS from incumbents (VitalIQ). The incumbent PPP operator model (Unisys in PH) is the clearest APAC pattern: CRS-ITP ran 1999-2015 and CRS-ITP2 runs 2016-2028. Within ITP2, Unisys absorbed more than 1,100 former PSA contractors (https://www.unisys.com/news-release/ph-unisys-philippines-expands-local-team-and-starts-civil-registry/). Several sources were unreachable: health.mo.gov (403), ppp.gov.ph (Cloudflare) and some Indonesian district sites (connection refused). Missouri's 'Mainframe/TN 3270' detail and Indonesia's 514 kabupaten/kota figure come from search snippets only. Wisconsin evidence: DHS Report to the Legislature on Data Processing Projects 2025 (P-00988, https://www.dhs.wisconsin.gov/publications/p00988.pdf), where SVRIS is licensed from Netsmart, Citrix-dependent (US$150k a year) and called 'antiquated'. NL evidence: https://www.gemeente.nu/bedrijfsvoering/burgerzaken/einde-aan-operatie-basisregistratie-personen/ . NSW LifeLink: https://delimiter.com.au/2013/11/26/decade-later-third-time-lucky-nsw-lifelink-project-finishes/ . Victoria Lifedata: https://www.itnews.com.au/news/vic-govt-to-give-new-life-to-births-death-marriages-registry-364375 . Thailand 1982 database: World Bank case study (URL in TH buyer row). Vietnam's MOJ civil-status software was reported unstable and slow in Oct 2024 (https://dantri.com.vn/thoi-su/phan-mem-dang-ky-quan-ly-ho-tich-thuong-xuyen-bi-loi-20241005105643960.htm). S4 is unmet for lack of a category-specific source, not because evidence points against it. Overlap: national ID card issuance (Thales, IDEMIA, IRIS/Datasonic) borders passports and immigration, which may belong to other categories.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
