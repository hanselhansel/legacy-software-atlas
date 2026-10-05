# Pension, provident fund and superannuation administration

Slug: `pension-provident-fund-admin`

## Systems

- FIS Omni (OmniPlus/OmniPlan, ex-SunGard) 401(k)/DC recordkeeping, COBOL on IBM mainframe, plus FIS Relius
- Heywood (ex-Aquila Heywood) Altair, UK pension administration, from the Watson Wyatt PMS6000 lineage
- Capita Hartlink (UK DB/DC admin software plus outsourced TPA)
- Equiniti Compendia (UK public and private sector schemes)
- Civica UPM (UK local government pensions)
- Bravura Sonata / Sonata Alta (AU/NZ/UK super, pensions and wrap; launched 2010 but on-prem or hosted)
- GBST Composer (AU super and wealth admin)
- Link Group / MUFG Pension & Market Services fund admin platforms (AU super)
- Custom in-house mainframe or client-server pension admin systems at US state and local retirement systems (e.g. NY State and Local Retirement System MEBEL on z/OS, Washington DRS 30-year-old system)
- Sagitec Neospin, Vitech V3locity, LRS PensionGold: the modern-generation replacements for US public pension systems
- National provident fund in-house cores: India EPFO (regional databases replaced by CITES 2.01 in July 2026), Malaysia KWSP Core Provident Fund System, Singapore CPF Board, Vietnam VSS business software (TST etc.), Philippines SSS/GSIS, Indonesia BPJS Ketenagakerjaan

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. FIS Omni/Relius, the leading US DC recordkeeping engine (650 clients, 68m participants), was built in COBOL more than 30 years ago and is only now being moved to a cloud platform (July 2026). OmniPlus runs on IBM mainframes, and practitioner CVs list COBOL, JCL, CICS and DB2. In the public sector, NY State's MEBEL pension system ran on z/OS and was more than 25 years old in 2013. Washington DRS was replacing a 30-year-old system in 2023, and Massachusetts SRB a 38-year-old system in 2010. In India, EPFO ran 120+ decentralised regional databases until July 2026. ([source](https://www.wealthmanagement.com/rpa-news/fis-new-cloud-based-record-keeping-system-could-unlock-the-potential-of-401-k-plans))
- **S2 slow to replace**: met. Washington DRS (Sagitec, 2023): 4 years of implementation plus 2 years of support. FIS's Omni/Relius cloud rebuild started about 4 years before its 2026 launch. HESTA (1m+ members) spent over 2 years preparing its move from Link to GROW Inc, finished June 2025, and members were locked out during the cutover. EPFO CITES 2.01 was approved in 2021 and went live nationally in July 2026. APG's Dutch Wtp migration to its new Festina admin system began more than 4 years before the 2026 transitions. Capita seeks 5 to 10 year TPA contracts (2017 council review). ([source](https://www.sagitec.com/pension-software-company/press-releases/washington-state-department-of-retirement-systems-awards-pension-modernization-project-to-sagitec-solutions))
- **S3 workarounds**: met. Sagitec's case study on a large US Teachers' Retirement System says the legacy PAS could not integrate with employer reporting, finance or telephony. That forced significant manual processing: staff searched several systems and keyed the same data in different places, and employers sent data on paper or disk. In India, EPFO members changing jobs had to file separate PF transfer applications and could be served only at their home regional office until CITES 2.01. Aware Super described its pre-2023 platform as paper-based legacy systems. Both are vendor or secondary sources. ([source](https://www.sagitec.com/hubfs/docs/Neospin-TRS-case-study.pdf?hsLang=en-au))
- **S4 shrinking skills**: met. A NY State audit, reported by Computerworld in 2013, warned that the 25+ year old COBOL/z/OS MEBEL system behind the $160bn NY pension fund depended on a small and dwindling number of specialists who could maintain it. The Comptroller replied that it had hired outside COBOL programmers and trained staff in COBOL and CICS. US 401(k) recordkeeping on FIS OmniPlus still needs COBOL, JCL, CICS, DB2 and the proprietary OmniScript. No pension-specific scarcity data was found for Asian provident funds. ([source](https://www.computerworld.com/article/1392782/cobol-based-system-for-160-billion-pension-fund-is-a-political-football.html))

## Segments

Mostly enterprise and government. National provident and social security funds (EPFO, CPF, KWSP, BPJS Ketenagakerjaan, VSS, SSS/GSIS, SSO Thailand) are single government buyers with in-house or SI-built cores. EPFO only consolidated 120+ regional databases in 2026. US state and local retirement systems (37m+ participants) run custom mainframe or 30-38 year old systems and replace them through multi-year RFPs (Washington DRS, Massachusetts SRB, Virginia RS, Illinois TRS). Large enterprise schemes and TPAs/recordkeepers use licensed platforms: in the UK, Altair holds 75%+ of LGPS and 48 of the top 100 schemes per a 2017 review; in the US, FIS Omni/Relius serves 650 recordkeeper clients and 68m participants; in Australia, Bravura and GBST. Mid-market and SMB employers rarely buy admin systems directly. They join master trusts, multi-employer funds or 401(k) recordkeepers, so the buyer universe is the few hundred administrators and funds, not the roughly 800k US plans.

## Reasons buyers stay

- Benefit rules span decades of legislative changes and member history (DB accrual, tranches, transitional protections) that must be migrated exactly. HESTA moved more than a decade of data and still had a members-locked-out cutover period
- Regulatory and fiduciary risk: payment errors to retirees are highly visible, and boards prefer incumbent stability
- Long outsourcing and TPA contracts (Capita seeks 5 to 10 years) bundle software and administration
- Challenger financial fragility: GROW Inc carried going-concern audit doubts and needed client debt and equity support before MUFG agreed to acquire it in 2026
- Big-bang regulatory deadlines (Dutch Wtp by 2028, UK pensions dashboards) push funds to extend incumbents rather than switch mid-reform
- Concentrated incumbent ecosystems (Heywood Altair across LGPS, FIS Omni across US recordkeepers) supply frameworks, interfaces and skilled staff
- Fund mergers (AU consolidation from 1,656 to 771 APRA funds in 5 years) often settle on the acquirer's existing platform instead of a new one

## Notes

Strongest primary evidence comes from regulators: APRA, TPR, EIOPA, DOL, Census, PPA and OJK. Most legacy and workaround evidence is vendor-sourced (Sagitec, GBST) or trade press (WealthManagement.com, Computerworld 2013), so treat it as biased or dated. India: the CITES 2.01 figures (340m accounts, 120+ databases, approved 2021, build from Jan 2023, live July 2026) were confirmed via adda247 and Open Magazine, both secondary; Business Standard and PIB returned 403. No vendor or SI for CITES was disclosed. Gaps: no primary IT-system evidence was found for SG CPF, MY KWSP (kwsp.gov.my returned 403), ID BPJS Ketenagakerjaan, TH SSO or PH SSS (profile PDF 404), and no first-shipped dates or customer counts for national-fund cores. Indonesia's pension fund count sits in an OJK Excel file that was not parsed. The US public pension system count is not on the Census pages read (check the ASPP unit files). The APRA 58 licensees / 81 funds figure came from a search snippet; the opened page confirmed only 771 APRA-regulated funds in total. Bravura Sonata launched in 2010, so it is not pre-2005 itself, though Bravura was built by consolidating older systems. FIS Omni (COBOL, 30+ years old) is the clearest S1 case for the US DC market, and FIS launched a cloud replacement in July 2026. No AI-native challenger with disclosed funding was found specifically for national provident funds in SEA or India. Challengers so far are UK/US DC platforms (Smart, Vestwell), AU admin-tech (GROW, now being acquired by MUFG), and modern-generation PAS vendors (Sagitec, Vitech). The overlap with gov-benefits (social security agencies) is large in VN, PH and TH, where the provident or pension function sits inside the social security agency.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
