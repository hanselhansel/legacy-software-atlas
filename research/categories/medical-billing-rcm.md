# Medical billing and revenue cycle

Slug: `medical-billing-rcm`

## Systems

- Epic Resolute (Hospital Billing / Professional Billing), built on the Chronicles database and written in M (MUMPS)
- Oracle Health (Cerner) Patient Accounting, Soarian Financials and Invision (ex-Siemens/SMS), being folded into RevElate
- MEDITECH MAGIC (1982) and Client/Server (1994) financials, migrating to Expanse
- TruBridge (ex-CPSI, Healthland) community-hospital EHR and RCM
- Altera Digital Health Paragon and Sunrise (ex-Allscripts/Eclipsys)
- SAP IS-H patient management and billing (DACH and EU hospitals; mainstream support ends 2027, extended support to 2030)
- InterSystems TrakCare (Asia/Oceania, UK, Middle East)
- HBCIS patient administration system (Queensland Health, early 1980s) and DXC iPM/webPAS (Australia)
- VA VistA (US government, being replaced by Oracle Health)
- Indonesia SIMRS (hospital information systems) plus BPJS V-Claim/E-Klaim INA-CBG, often not bridged to each other
- Singapore National Billing System (NBS) alongside the Epic-based NGEMR

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The dominant cores all predate 2005 and were built as on-prem or midrange systems. Epic Resolute shipped in 1987 on the Chronicles/M (MUMPS) database. MEDITECH adopted MAGIC in 1982, where code runs on a central server and clients act as dumb terminals, and added Client/Server in 1994. Expanse only arrived in 2018. Queensland's HBCIS dates from the early 1980s, and UC Davis replaced Invision and Signature billing systems that had run for two decades. ([source](https://en.wikipedia.org/wiki/Meditech))
- **S2 slow to replace**: met. NYC Health + Hospitals budgeted $289M over five years (2017-2020) to implement Epic revenue cycle across 11 hospitals. iTnews reports that replacing Queensland Health's HBCIS is 'likely to take around seven years' and cost over $200M. On SAP IS-H, DSAG says the tender alone takes about two years before implementation starts. VA's Cerner EHR contract from 2018 ran 10 years and $10B (Fierce Healthcare, search result only, could not open). LA County and SF also sought 10-year Epic EHR and revenue cycle contracts (pages blocked). ([source](https://www.nychealthandhospitals.org/wp-content/uploads/2017/05/Public-hospitals-to-spend-289-million-on-Epics-revnue-cycle-software-implementation-Politico.pdf))
- **S3 workarounds**: met. The 2024 CAQH Index sorts provider transactions into fully electronic, partially electronic (web portals and IVR, meaning re-keying into payer portals) and manual (phone, fax, email, mail). It puts the remaining savings opportunity at $20B and notes that the Change Healthcare breach forced 'reliance on costly manual workarounds'. A UC Davis internal audit found staff creating 'dummy' appointments as a workaround so billing could run after the Epic Resolute conversion. In Indonesia, unbridged SIMRS and BPJS E-Klaim force casemix teams to re-enter data manually (sistemkesehatan.id, a secondary source). ([source](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf))
- **S4 shrinking skills**: met. Health IT Outcomes notes that Epic is written in MUMPS, a language from the late 1960s, and calls MUMPS programmers 'a dying breed', which makes it hard to find developers. MEDITECH (MIIS/MAGIC), VA VistA and InterSystems-based TrakCare share the M/MUMPS lineage. The SAP IS-H end of support adds pressure on scarce IS-H/ABAP integration skills in DACH, but no primary source quantifying that shortage was found. ([source](https://www.healthitoutcomes.com/doc/is-epic-future-proof-0001))

## Segments

Enterprise: large US health systems and academic medical centers run Epic Resolute or Oracle Health Patient Accounting/Soarian. Epic holds 56.9% of US acute beds (KLAS 2025). Mid-market: community hospitals run MEDITECH MAGIC/Client Server (14.7% of US hospitals), Altera Paragon and TruBridge. About 98% of TruBridge's acute clients have under 100 beds (10-K). Government: VA VistA being replaced by Oracle Health. NYC Health + Hospitals is on Epic revenue cycle. Queensland Health runs the 1980s HBCIS in all public hospitals. Singapore's public clusters use the NGEMR (Epic) plus the National Billing System across 60+ institutions. SAP IS-H runs in public and private hospitals across DACH. SMB physician practices mostly use cloud PM/billing (athenahealth, eClinicalWorks, NextGen) and outsourced billers. They depend heavily on payer portals, phone and fax (CAQH partially electronic and manual categories), not on mainframe cores. In ASEAN, private hospital groups and public hospitals run local HIS (Indonesian SIMRS, Thai HIS, PH iHOMIS) that must bridge to national payer claim systems (BPJS E-Klaim, PhilHealth eClaims, Thai NHSO e-Claim).

## Reasons buyers stay

- Billing is tied into the EHR. Epic Resolute and MEDITECH financials share one database with scheduling and clinical data, so replacing billing usually means replacing the EHR.
- Cash-flow risk at go-live. After the UC Davis Epic conversion, staff resorted to 'dummy' appointments to keep certain billing running.
- Very high cost and long timelines: $289M over five years for NYC H+H revenue cycle, about 7 years and $200M+ for Queensland's PAS replacement.
- Payer and regulatory rules are encoded over decades (US payer edits, German DRG billing in IS-H, BPJS INA-CBG, PhilHealth case rates). Rebuilding them is risky.
- Vendors keep extending support. SAP IS-H has extended maintenance to 2030 and a transition option to 2033. Queensland bought extended HBCIS support to 2023.
- Procurement friction. DSAG estimates two years just to tender an IS-H successor, and public buyers must run formal tenders.
- Incumbent consolidation keeps customers in place. Oracle is folding Soarian and Invision into RevElate, IKS Health bought TruBridge, and MEDITECH reports 84% legacy retention.

## Notes

Coverage is strongest for the US, with AU, SG, EU (DACH) and ID as secondary. No primary-source ASEAN AI-native RCM challengers with disclosed funding were found. A search for Indonesian cloud SIMRS vendors (simrs.id, HealthCore) found products but no funding, and an AU search found no billing-specific raise. Sources that could not be opened (403 or empty) and are therefore not cited: LA County Epic board memo, SF 10-year Epic contract article, Fierce Healthcare VA contract article, AIHW pages, King's Fund, Building Queensland (SSL error), Oracle Health revenue cycle roadmap PDF. The VA 10-year/$10B Oracle Cerner contract and the AIHW private-hospital count come only from search snippets. There is no Eurostat EU hospital-count series, so the EU buyer universe is given in beds. Epic does not disclose a customer count, so KLAS market share (via HealthSystemCIO) stands in for it. Thailand's counts are 2021 (MOPH via the HiT review), and Indonesia's 2023 count is BPS data reported by Kompas, not the live Kemenkes SIRS register. The S4 source (Health IT Outcomes) is a trade opinion piece, not labor-market data. The S3 Indonesian re-keying claim is from a vendor blog. The core S3 evidence is the CAQH Index plus the UC Davis audit (pdf: https://auditreports.ucop.edu/?action=public_ar_display&id=ec1a0b2003913b76). For UK NHS trusts, billing is limited to private patients and overseas visitor charging, so the RCM buyer pool there is narrower than the trust count suggests.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
