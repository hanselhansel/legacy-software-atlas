# Pharmacy management

Slug: `pharmacy-systems`

## Systems

- QS/1 Pharmacy System / NRx (RedSail Technologies, ex-Smith Technologies), US independents and LTC
- Rx30 (Transaction Data Systems / Outcomes), US independents, character-based Linux/Unix heritage
- PioneerRx, BestRx, PrimeRx, Axys (RedSail Technologies portfolio), US
- McKesson EnterpriseRx / Pharmaserv, US chains and independents
- VA VistA Outpatient Pharmacy (PSO), MUMPS-based, US federal
- EMIS (now Enlivio Health) ProScript Connect, UK community PMR
- Cegedim Pharmacy Manager (ex-Nexphase) and Boots Columbus (built with Cegedim), UK
- Positive Solutions Analyst PMR, UK
- JAC and Ascribe, UK NHS hospital pharmacy stock control
- Pharmagest/Equasens LGPI (now 'id.'), France
- CGM Lauer-Fischer (WINAPO), Germany
- Fred IT Fred Dispense (on-prem; cloud successor Fred NXT), Z Software, Minfos, Australia
- Marg ERP (desktop pharma retail/distribution billing), India
- MyPhIS / Clinic Pharmacy System (Pharmaniaga for MOH), Malaysia public sector
- Local GPP pharmacy software (KiotViet and ~50 vendors connected to the national drug database), Vietnam

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. QS/1 shipped its first pharmacy system in 1977 and Rx30 in 1980. Rx30 reviewers in 2016-2018 describe a Linux-based, command-driven system with sub-numbered menus. GAO-17-179 says VA's Outpatient Pharmacy core was developed in the 1980s and uses character-based input screens. These are on-prem, pre-2005 cores still in production. ([source](https://www.gao.gov/assets/gao-17-179.pdf))
- **S2 slow to replace**: met. Malaysia MOH awarded Pharmaniaga a 10-year PhIS contract in March 2011 and renewed it to June 2030, about 19 years, with rollout running 2014-2026. VA reported $187.6M spent on Pharmacy Re-engineering in FY2002-2016 (GAO-17-179). BioScrip's 10-K says it spent two years building a consolidated dispensing system and then migrated through 2008-2009. ([source](https://phisportal.moh.gov.my/project-profile/pharmacy-information-system-phis-dan-clinic-pharmacy-system-cps))
- **S3 workarounds**: met. A 2024 Journal of Patient Safety qualitative study found most community pharmacies hand-transfer e-prescription data. Staff work split-screen and type each order into dispensing software. GAO-17-179 says VA pharmacies must manually input paper or faxed prescriptions from non-VA providers. Rx30 reviewers report tracking on paper during POS outages. ([source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11335435/))
- **S4 shrinking skills**: not met. No primary source found documenting scarce skills. Community PMS (PioneerRx, Rx30, ProScript, LGPI, Fred) run on Windows/Linux stacks, not COBOL/RPG. The exception is VA VistA pharmacy, built on MUMPS. In 2010, VA's CIO cited over 15M lines of MUMPS code but said nothing about programmer scarcity. Scarcity claims exist only in blogs and forums, so the sign is unproven. ([source](https://www.nextgov.com/people/2010/08/mumps-to-be-retained-for-va-vista-system-for-now/223213/))

## Segments

SMB: independent community pharmacies are the core buyers of legacy PMS. The US has 18,960 independents on QS/1, Rx30, PioneerRx, BestRx and PrimeRx. ProScript Connect targets UK independents. Australian independents run Fred Dispense, Z and Minfos; Indian chemists use desktop Marg ERP. Mid-market: regional chains, such as Rowlands' 529 UK branches, which moved off a legacy platform onto ProScript Connect in 2017. Enterprise: large chains run proprietary or co-built systems (CVS RxConnect, Boots Columbus with Cegedim). Long-term-care and specialty pharmacies use QS/1 and BioScrip-style consolidated systems. Government: VA VistA Outpatient Pharmacy (US), MOH Malaysia MyPhIS across 1,342 facilities, and NHS hospital trusts on JAC/Ascribe, such as Northern Ireland's regional JAC system.

## Reasons buyers stay

- Claims adjudication, PBM/payer and NHS EPS/eRx accreditation are certified per PMS. Titan was the first new UK PMR accredited in 15 years (2019), which shows how high the switching barrier is.
- Each switch means migrating patient medication records, refill histories and controlled-drug registers, with regulatory risk if records are lost.
- Pharmacy staff are trained on keystroke-heavy workflows. Reviewers note learning curves, and retraining interrupts dispensing.
- Integrations with wholesalers, robots and dispensing automation, IVR, POS and national drug databases (e.g. Vietnam CSDL Duoc) are built per PMS.
- Consolidation (RedSail now ~16,000 US pharmacies) and bundled services such as payments, data and adherence programs lock customers into vendor ecosystems.
- Public-sector contracts run long. Malaysia's PhIS contract runs 2011 to 2030 and VA modernised in place for 14+ years.
- Thin independent-pharmacy margins (DIR fees, reimbursement pressure) leave little budget or time for a migration project.

## Notes

1. Legacy pharmacy systems are mostly 1977-1995 on-prem client-server or character-based products (QS/1, Rx30, VA VistA), not mainframe COBOL. S4 (scarce skills) is therefore unproven. The main lock-in comes from certification, migrating records and controlled-drug registers, and vendor consolidation: RedSail went from ~12,000 to ~16,000 US pharmacies with the PrimeRx deal (Feb 2026) after DOJ scrutiny.
2. Several vendor pages returned 403 or 502, so their counts are marked unverified: fred.com.au, Pharmagest, McKesson EnterpriseRx fact sheet, EMIS '5,700 pharmacies' claim, Titan '1,000 pharmacies' article. No vendor-disclosed count was found for McKesson EnterpriseRx/Pharmaserv, Cegedim Pharmacy Manager, Z Software or Minfos (search snippets only: Z 1,600+, Minfos 900+).
3. Buyer counts are mixed in vintage. Vietnam is 2019, Australia FY2023 behind Statista's paywall, Thailand from a news article citing FDA data, Philippines unconfirmed. The Singapore data.gov.sg dataset (243 rows) may be older than HSA's current licence count.
4. Strongest primary sources: GAO-17-179 for VA (1980s core, character screens, manual input of outside prescriptions, $187.6M re-engineering FY2002-2016) and the MOH Malaysia PhIS portal (2011 contract renewed to 2030).
5. Most AI-native challengers are overlays (Asepha, Faks, Foundation Health's PAIGE) that sit on top of the incumbent PMS rather than replacing it. Full cloud replacements: Titan (UK), Vmedis (ID), KiotViet (VN), and the incumbents' own cloud products (Fred NXT, RedSail Axys).

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
