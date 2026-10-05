# Hospital records (EHR)

Slug: `ehr-hospital`

## Systems

- Epic (Chronicles database on M/MUMPS, Hyperspace client)
- Oracle Health / Cerner Millennium
- MEDITECH MAGIC, Client/Server and 6.x (legacy) and Expanse (current)
- VA VistA / CPRS (MUMPS)
- SAP IS-H patient management, often paired with Dedalus/Cerner i.s.h.med (DACH and EU)
- Altera (ex-Allscripts/Eclipsys) Sunrise Clinical Manager
- Queensland Health HBCIS patient administration system (AU)
- Malaysia MOH Total Hospital Information System (THIS), Cerner-based at Selayang
- HOSxP (Thailand), SIMRS/SIMGOS (Indonesia), iHOMIS (Philippines), and local vendor HIS in Vietnam (named from search results, not verified)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The dominant cores date from before 2005 and run on on-prem or midrange setups:
- Epic was founded in 1979, and its Chronicles database is written in M/MUMPS.
- MEDITECH shipped MAGIC (1979-82, central server with dumb terminals), then Client/Server (1994) and 6.x (2006). It moved to a web platform only with Expanse in 2018.
- VA testimony says VistA has run for more than 40 years.
- Queensland's HBCIS dates from about 1990. SingHealth has run Sunrise since 1998, and Malaysia's THIS since 1999.
- SAP IS-H has more than 30 years in DACH hospitals. ([source](https://ehr.meditech.com/about/meditechs-50th-anniversary))
- **S2 slow to replace**: met. VA EHR replacement:
- The original 2018 Cerner contract was about $10B over 10 years.
- The 2022 IDA estimate was $49.8B: 13 years of implementation plus 15 years of sustainment.
- Deployments paused for 20 months (April 2023 to December 2024).
- GAO says not all VA centers will be on the new system by the May 2028 contract end.

Other examples:
- Queensland's HBCIS replacement was put at about 7 years and more than A$200M.
- SingHealth extended its Sunrise contract to 2029, 31 years after go-live.
- SAP gave IS-H users until 2027 (mainstream) and 2030 (extended), with a transition option to 2033. ([source](https://www.gao.gov/products/gao-25-106874))
- **S3 workarounds**: met. Workarounds are documented in research and in real hospitals:
- A 2022 scoping review of 62 studies (2010-2021) found paper persistence, duplicate entry, copy-paste, and spreadsheets or external systems run alongside the EHR.
- Malaysia, Selayang Hospital: after its Cerner EMR crashed in 2021, staff used a radiologist-built backup system and later a COVID quarantine system. Lab results, prescriptions, referrals and registrations went manual (CodeBlue, 2023).
- Vietnam: many hospitals run paper and electronic records in parallel (Tuoi Tre, 2024).
- Indonesia: Kemenkes notes manual matching between SITB and SATUSEHAT. ([source](https://pmc.ncbi.nlm.nih.gov/articles/PMC8965666/))
- **S4 shrinking skills**: met. VA's executive director of software product management told the House (March 2023) that about 70% of VA's MUMPS programmers are retirement-eligible. He said MUMPS is not taught in computer science classes and VA has limited options to hire replacements. The same applies to the M/MUMPS base under Epic Chronicles and MEDITECH MAGIC, but we found no primary source quantifying skill scarcity for those vendors. Vietnam's public hospitals also report trouble attracting IT staff because of salary caps (Tuoi Tre). ([source](https://www.nextgov.com/modernization/2023/03/official-vas-legacy-ehr-must-be-maintained-not-long-term-solution/383753/))

## Segments

Government buyers:
- US VA (VistA to Oracle).
- UK NHS trusts (206 under Frontline Digitisation).
- Singapore public clusters through Synapxe (Sunrise to Epic NGEMR).
- Malaysia MOH (THIS, which covers only 24% of MOH hospitals).
- Queensland Health (HBCIS).
- Indonesian district hospitals (21% of hospitals) on SIMRS/SIMGOS.
- Vietnam and Philippines public hospitals.

Enterprise and mid-market buyers:
- US multi-hospital systems (Epic, Oracle, MEDITECH). KLAS says most 2025 decisions came from systems with 2-10 hospitals.
- HCA, with 189 hospitals, is still migrating from older MEDITECH to Expanse.
- German university and private chains (Sana, LMU, MHH) on SAP IS-H.

SMB buyers:
- US community and critical-access hospitals on MEDITECH MAGIC/C-S or TruBridge.
- Thai community hospitals on HOSxP.
- Small private hospitals in ID, VN and PH on local vendor HIS. ID: private/other owners hold 28% of hospitals.

## Reasons buyers stay

- High switching cost. MEDITECH's 10-K example: a typical 150-bed hospital pays a $3M product fee plus a $1M implementation fee, then about $30K a month.
- Patient-safety and go-live risk. VA paused rollout for 20 months, and 75% of surveyed users said the new system did not make them as efficient as possible (GAO-25-106874).
- Program cost overruns. VA's EHR estimate went from about $10B to $37-50B life-cycle.
- Data migration from decades of clinical records. VistA holds 15M+ lines of MUMPS code, and VA says modernizing would mean rewriting it almost from scratch.
- Epic's network effects (Care Everywhere, MyChart) and the KLAS-ranked suite lock in large systems. Epic's share keeps rising.
- Regulatory and certification requirements (ONC, NHS DSPT, Kemenkes PMK 24/2022 RME and SATUSEHAT integration) favour incumbent certified vendors.
- Public-sector budget and procurement constraints. Malaysia MOH cites budget limits, Queensland's procurement was delayed by a conflict-of-interest probe, and Vietnam's small bidders under-deliver.
- Retraining large clinical workforces and the downtime risk of a cutover.

## Notes

US acute EHR market (KLAS 2026): Epic 43.7% of hospitals, Oracle Health 21.9%, MEDITECH 14.7%. The legacy story is less one vendor's mainframe and more three things:
- MUMPS/M-based cores: Epic Chronicles, VistA, MEDITECH MAGIC.
- 1990s client-server installs: Cerner Millennium, Sunrise, MEDITECH C/S and 6.x, SAP IS-H.
- Government in-house or ageing systems: VistA, HBCIS, Malaysia THIS.

Forced replacement events to watch:
- SAP IS-H end of mainstream support in 2027 and extended support in 2030 (DACH).
- NHS Frontline Digitisation 2026 deadline.
- VA EHRM, with the Oracle contract running to May 2028.
- Indonesia PMK 24/2022 RME mandate and SATUSEHAT integration.
- Vietnam's MoH push for 100% hospital EMR (search results say by Oct 2025, other reports say 2030).
- Singapore's NGEMR (Epic) rollout to public clusters and private hospitals.

Gaps and caveats:
- EU hospital count: the Eurostat hlth_rs_hosp dataset could not be retrieved; only bed counts are cited.
- Several primary pages returned 403 (AIHW private list, MOH Malaysia Health Facts PDF, PIB India, DOH PH FOI). For those regions the counts come from secondary pages or search summaries, as flagged in each row.
- Epic and Oracle Health do not publish hospital counts. Market share comes from KLAS via trade press.
- S4 rests on VA testimony about MUMPS. We found no primary evidence of skill scarcity for Epic or MEDITECH specifically.

SEA legacy HIS vendors were named from search snippets only and not verified with opened sources: HOSxP (Thailand, cited as 800+ hospitals), iHOMIS (Philippines), and Vietnam local vendors (FPT, VNPT, Viettel).

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
