# Field service and maintenance (EAM/CMMS)

Slug: `field-service-maintenance`

## Systems

- IBM Maximo (7.6.x on-prem, now Maximo Application Suite)
- SAP Plant Maintenance (PM) in SAP R/3 / ECC 6.0 (now SAP EAM on S/4HANA)
- Infor EAM / Datastream 7i / MP2 (now HxGN EAM, rebranded Octave Attune EAM in 2026)
- IFS Applications EAM (now IFS Cloud; IFS Ultimo)
- Oracle E-Business Suite Enterprise Asset Management (eAM) / JD Edwards Capital Asset Management
- Spreadsheets and paper work orders (the de facto system at many SMB sites)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The dominant EAM cores predate 2005 and were on-prem: Maximo first released 1985 as a stand-alone IBM PC product, later on AIX/HP-UX/Solaris/Windows servers. Datastream (Infor/HxGN EAM) was founded 1986. IFS shipped its first maintenance system in 1985 for UNIX at Swedish nuclear plants. ([source](https://en.wikipedia.org/wiki/Maximo_(software)))
- **S2 slow to replace**: met. Partly met. SAP ECC 6.0 mainstream support ends 31 Dec 2027, extended maintenance runs to 2030, and ERP Research says to plan 12-24 months for an S/4HANA migration (the PM module moves with the rest of the ERP). IBM ended standard support for Maximo 7.6.1 on 30 Sep 2025, with extended support to Sep 2026 and sustained support to 2030. MaxIron reports that automation scripts, integrations, UI reconfiguration and OpenShift ops overrun their plans. No source found for EAM contract terms of 7+ years. 'Multi-year' rests on the SAP 12-24 month range plus vendor support windows running to 2030. ([source](https://www.erpresearch.com/en-us/blog/sap-ecc-6.0-end-of-support))
- **S3 workarounds**: met. UpKeep's statistics page (2018 data): 53% of facilities use a CMMS, 55% use spreadsheets and schedules, 44% still use paper. It also cites 'up to 80%' of CMMS implementations failing. Prometheus Group documents Maximo planners exporting work orders to Excel for scheduling, shift rotations and crew assignments, with no write-back to Maximo, so the data goes stale. MXLoader and MaxQuickLoad exist to bulk-load Excel into Maximo. ([source](https://upkeep.com/learning/maintenance-metrics/maintenance-statistics))
- **S4 shrinking skills**: not met. Not established. EAM runs on Java/ABAP/Oracle, not COBOL/RPG, and no source found that quantifies scarce Maximo or SAP PM skills. IT Jobs Watch shows only 38 permanent jobs in England citing Maximo in the 6 months to Oct 2026 (65 two years earlier), with a £70,000 median salary, up from £55,000 two years earlier. That is thin, volatile demand at a rising price, which hints at a small specialist pool but does not prove scarcity. MAS 9's move to Red Hat OpenShift adds a new skill requirement (MaxIron), but again without a scarcity measure. ([source](https://www.itjobswatch.co.uk/jobs/england/maximo.do))

## Segments

Enterprise and government run the legacy EAM cores: Maximo, SAP PM and HxGN/Infor EAM serve utilities, oil and gas, transport, public agencies and large manufacturers. Enlyft's Maximo profile shows 42% of tracked users above 1,000 employees and 35% medium-sized (https://enlyft.com/tech/products/ibm-maximo). Mid-market plants use Infor/Datastream MP2-era products, IFS, or ECC PM inside their ERP. SMBs mostly have no EAM: UpKeep cites 55% using spreadsheets and 44% using paper. That SMB gap is where MaintainX, UpKeep and Limble grew. Asian registers (DOSM: 94.5% of Malaysian manufacturing establishments are MSMEs) suggest most of the SEA buyer count is SMBs on spreadsheets, not legacy EAM.

## Reasons buyers stay

- Deep integration with ERP finance, procurement and inventory (SAP PM sits inside ECC), so replacing EAM means touching the ERP
- Regulated asset histories (nuclear, utilities, aviation, rail) with audit trails and compliance workflows built over decades
- Heavy customization (automation scripts, integration framework) that MaxIron says routinely overruns migration plans
- Vendor support windows stretch to 2030 (SAP ECC extended maintenance, Maximo sustained support), which delays urgency
- Large asset hierarchies and parts catalogues that are costly to cleanse and migrate
- Licence economics: Maximo perpetual-to-MAS trade-up and AppPoints credit existing spend if customers stay with IBM

## Notes

Key forcing events: IBM Maximo 7.6.1 standard support ended 30 Sep 2025, extended support ends Sep 2026, and MAS dual-support rights for EAM 7.6.1 end 30 Apr 2027 (https://maxiron.com/insights/mas-dual-support-eam-7-6-1-ends-april-2027/). SAP ECC mainstream support ends 31 Dec 2027. Both push a large installed base into migrations in 2026-2027.

Ownership changes: Infor EAM became HxGN EAM when Hexagon bought it (Oct 2021), and is now Octave Attune EAM after the Hexagon software spin-off (May 2026). Only secondary sources were opened for this; the arcweb page returned 403.

Gaps: no vendor-disclosed customer count for Maximo or SAP PM; Datastream's 6,700 (2006 SEC filing) is the only primary count. Buyer-universe counts for US, ID, VN, TH, PH and AU were not verified because official sites were blocked (403/timeouts) or the data sits in cubes. The ID and PH rows carry a placeholder source and their counts should be treated as missing. Manufacturing establishment counts overstate the EAM buyer universe; a 50+ or 250+ employee filter plus utilities, transport and public agencies is a better proxy. S4 is marked not met because EAM skills are Java/ABAP, not COBOL/RPG, and no scarcity data was found. S2 is only partly met: SAP migrations run 12-24 months and support windows run to 2030, but no source for 7+ year contracts was found. Challenger plays: SMB-first greenfield (MaintainX, UpKeep, Limble), sensor-plus-CMMS overlay on SAP/Oracle (Tractian), and industrial incumbents buying cloud CMMS (Rockwell/Fiix).

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
