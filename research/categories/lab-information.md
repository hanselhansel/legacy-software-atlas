# Laboratory information systems

Slug: `lab-information`

## Systems

- Sunquest Laboratory (Clinisys, formerly Roper; InterSystems Cache/MUMPS database, AIX/OpenVMS/Linux/Windows)
- SCC Soft Computer SoftLab / SoftPathDx / SoftBank (Oracle on IBM AIX / Red Hat)
- Oracle Health (Cerner) Millennium PathNet, now 'Cerner Laboratory' (Oracle DB on HP-UX/AIX/VMS)
- Epic Beaker (Chronicles/InterSystems-based, bundled with Epic EHR)
- Clinisys WinPath / WinPath Enterprise (UK NHS)
- Telepath (CSC/iSOFT/DXC, now managed by Dedalus in the NHS)
- iLab APEX (UK NHS)
- Orchard Harvest LIS (now Clinisys)
- Auslab (PJA Solutions / Citadel Health, Queensland Health)
- TECHNIDATA TDNexLabs
- Evident (CPSI) Thrive EHR-LIS
- Meditech LIS

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. In the CAP TODAY 2020 LIS guide, vendors self-reported their first installations: Sunquest Laboratory 1979 (InterSystems Cache database; AIX/OpenVMS), Cerner Laboratory/PathNet 1982 (Oracle on HP-UX/AIX/VMS), SCC SoftLab 1985 (IBM AIX), Evident 1986, Orchard Harvest 1993, TECHNIDATA 1973. All are on-premises client-server or midrange systems built long before 2005. In Australia, Auslab was about 22 years old in 2018. In the UK, Kent's Telepath was installed around 1995. ([source](https://www.captodayonline.com/2020/ProductGuides/11-20_CAPTODAY_LIS.pdf))
- **S2 slow to replace**: met. The UK CMA (Roper/CliniSys, 2016) found that NHS LIMS contracts typically run 5 to 10 years, often with extension options. Northumbria's WinPath Enterprise contract runs 10 years, with a hardware refresh halfway through (healthtechdigital.com). Queensland Health signed a $68.5m, 10-year Sunquest contract in 2018 to replace the 22-year-old Auslab. It spent $37.5m, then cancelled the project and extended Auslab support to 2029 (itnews.com.au/news/queensland-health-bins-64m-pathology-system-overhaul-547249). ARN reported that the replacement had been forecast to take 7 years. One more figure comes only from a search snippet of a Medway FOI page that I could not open (403): Kent and Medway's WinPath programme runs 13 years (GBP 23m) and replaces a Telepath installed around 1995. ([source](https://www.itnews.com.au/news/queensland-health-bins-64m-pathology-system-overhaul-547249))
- **S3 workarounds**: met. A JAMIA study (2019) covered 60 clinics at two academic medical centres. Glucometer results already flowed into the LIS through middleware, but staff re-keyed them into the EHR because the devices do not record the ordering provider. The manual transcription error rate was 3.7%, and 14.2% of the errors differed from the true value by more than 20%. The study covered 6,930 paired results from 2015 to 2017. ([source](https://academic.oup.com/jamia/article/26/3/269/5287977))
- **S4 shrinking skills**: not met. This sign is only partly evidenced. The CAP TODAY 2020 guide confirms that Sunquest Laboratory runs on InterSystems Cache, a MUMPS implementation, and that SCC and Cerner run on AIX/VMS/HP-UX. The H Speakers article lists Sunquest, Meditech and VistA as MUMPS users. But no source I opened states that MUMPS/Cache or AIX/VMS skills are scarce for LIS work. A search snippet attributed a 'hard to find MUMPS programmers' statement to GAO. The GAO pages I opened (GAO-19-471, GAO-25-107795) mention only COBOL/assembly skills as dwindling, not MUMPS. Left unmet until a primary source is found. ([source](https://www.captodayonline.com/2020/ProductGuides/11-20_CAPTODAY_LIS.pdf))

## Segments

Mostly enterprise and government. In the CAP TODAY 2020 survey, SCC SoftLab sites skew to US hospitals (724 of 1,199). Cerner reports 80% high-volume sites. Evident's 460 sites are almost all US hospitals. Public systems run the big legacy installs: NHS trusts and networks (Telepath, WinPath, APEX), Queensland Health (Auslab), and the national health systems in the Middle East. Mid-market and SMB (independent labs, physician-office and clinic labs) use Orchard Harvest (1,095 clinic sites) and smaller vendors, and that is where cloud challengers (LigoLab, CrelioHealth, Flabs) mostly sell. In India and SEA, private diagnostic chains and standalone NABL labs are the SMB/mid-market buyers. Government (puskesmas, labkesda, MOH hospitals) is the larger buyer base by count.

## Reasons buyers stay

- Regulated validation: every LIS change must be revalidated under CLIA/CAP/ISO 15189, so switching costs are high
- Deep instrument and middleware interfaces (analyzers, blood bank, microbiology) built up over decades
- Tight coupling to the EHR: Epic Beaker and Cerner PathNet come bundled with the hospital EHR contract
- Failed replacements: Queensland Health spent $37.5m on a Sunquest replacement, cancelled it, and kept Auslab to 2029
- Long contracts: NHS LIMS contracts run 5-10 years with extensions, and network-wide programmes run up to 13 years
- Decades of historical results must be migrated (Auslab held 17 years and 4 billion+ result sets per search snippet)
- Blood bank modules are FDA-regulated medical devices (e.g. Sunquest device recalls), which raises the replacement bar

## Notes

Data quality notes. (1) Most vendor install counts come from the CAP TODAY Nov 2020 LIS product guide, a vendor-reported survey and the best public cross-vendor source; Sunquest and Epic did not report site totals. (2) S4 is set false on purpose. Sunquest runs on InterSystems Cache (a MUMPS implementation) and SCC/Cerner run on AIX/VMS/HP-UX, but no opened source states that these skills are scarce. A search snippet attributed a MUMPS-scarcity statement to GAO, and the GAO pages I opened did not contain it. (3) Kent and Medway's 13-year GBP 23m LIMS programme replacing a c.1995 Telepath comes from search snippets of a WhatDoTheyKnow FOI and a Kent HOSC paper, both 403 on fetch, so it is not used as the primary S2 source. (4) Buyer-universe counts for SG, TH, PH and AU were not found: pages timed out, returned 403, or publish no totals. The Flabs source URL is the company blog domain, and its funding and traction come from search snippets. (5) Market-structure signal: Epic took 77 net hospitals in 2025 while Oracle Health lost 56 (KLAS via search snippets, not opened). EHR consolidation is pulling hospital LIS work toward Epic Beaker, which squeezes standalone legacy LIS (Sunquest, SCC) in the US hospital segment. In SEA and India, the opportunity sits more with fragmented private lab chains.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
