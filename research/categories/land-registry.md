# Land and property registry

Slug: `land-registry`

## Systems

- US county recorder land-records systems: Tyler Technologies Eagle Recorder / EagleSoftware, Harris Recording Solutions OnCore (legacy, 2003) and Acclaim, Fidlar AVID/Laredo, Kofile, Catalis Official Records, Infocon County systems on IBM AS/400 (IBM i)
- HM Land Registry (England and Wales) core register on a mainframe (140M documents, about 1 PB), plus the eDRS scanned-form channel, now retired
- Queensland Automated Titles System (ATS, from 1994)
- Landgate WA Smart Register (replaced 2015 to 2017 by NLR-T/Advara)
- NSW LRS and Victoria SERV registries (privatised under 35- and 40-year concessions)
- Singapore SLA INLIS (1998) and the Land Titles registry
- India: Bhoomi (Karnataka, NIC, 1999-2001), state RoR systems under DILRMP, NGDRS e-registration
- Indonesia ATR/BPN KKP (Komputerisasi Kegiatan Pertanahan): desktop, then Geo-KKP, then KKP-Web
- Malaysia SPTB (Sistem Pendaftaran Tanah Berkomputer, 1995) and e-Tanah
- Philippines LRA Land Titling Computerization Project (LARES, BOO, awarded 2000)
- Vietnam district- and province-level land databases (VILG/MPLIS) moving to a national land database
- Thailand Department of Lands Land Information System

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Many core registers predate 2005 and run on-prem. Queensland's ATS went live in April 1994. Singapore's INLIS launched in 1998. Malaysia's SPTB was piloted in 1989-90 and implemented from 1995. Bhoomi dates from 1999-2001. HMLR keeps its core register and 140M documents on a mainframe. Infocon, serving Pennsylvania counties since 1976, supports IBM System i (AS/400). Landgate's CEO said the world's roughly 37 Torrens jurisdictions run bespoke systems built around 2000 and all need replacing. ([source](https://www.governmentnews.com.au/digitally-disrupted-land-registry/))
- **S2 slow to replace**: met. NSW sold a 35-year concession for registry operations, starting 1 July 2017. Victoria granted a 40-year concession in 2018 for A$2.86bn. HMLR's Local Land Charges migration has run since about 2015 and is now pushed to end-2028. Malaysia's e-Tanah was announced in 2003 and is still not national, with full Peninsular coverage targeted for 2030. The Philippines LTCP was awarded in 2000 and had not started 5 years later. Vietnam's World Bank VILG project was extended to June 2023 with 125 of 250 districts done. ([source](https://www.premier.vic.gov.au/land-use-victoria-proceeds-deliver-infrastructure-boost-0))
- **S3 workarounds**: met. HMLR's Strategy 2025+ says most of its data is paper, scanned images or PDFs that machines cannot read, that legacy systems copy paper forms, and that spatial and text data sit in unconnected systems. Kofile/AWS describes county staff indexing documents by hand, taking minutes per document, and searching microfiche. Landeed's business is pulling fragmented state land records from 24 Indian states into one searchable layer. Spreadsheets and screen-scraping are not named explicitly in these sources. ([source](https://www.gov.uk/government/publications/hm-land-registry-strategy-2025/hm-land-registry-strategy-2025))
- **S4 shrinking skills**: not met. No source found that ties a COBOL or RPG skills shortage to a land registry specifically. General evidence: COBOL runs in about 45 of 50 US state governments, experts retire daily, and few universities teach it (Route Fifty, 2023). HMLR's mainframe language and Pennsylvania counties' AS/400 (RPG) platforms point to the same risk. A reported Erie County, PA plan to replace an Infocon/AS/400 recorder system (about $40k a year in maintenance) appeared in search results, but the page could not be opened. ([source](https://www.route-fifty.com/emerging-tech/2023/11/government-runs-64-year-old-language-could-ai-help-change/392380/))

## Segments

Almost all government. Buyers are national or state land registries (HMLR, SLA, ATR/BPN, LRA, DOL, Malaysian state PTGs, Australian state registrars, Indian state revenue and registration departments) and, in the US, about 3,000 county recorders and clerks (Census of Governments; Kofile claims 3,000+ counties). Some registries now buy through long privatised concessions: NSW for 35 years, Victoria for 40 years, and BOO in the Philippines. Mid-market and enterprise use is on the demand side (title insurers, banks, conveyancers), which consume registry data through e-recording (Simplifile, 2,019 counties) and e-conveyancing (PEXA). SMB use is minimal apart from small county offices.

## Reasons buyers stay

- The register carries a state guarantee of title (for example, the NSW Torrens Assurance Fund), so integrity outranks speed. HMLR said this explicitly when it delayed LLC to 2028.
- Long concession and BOO contracts (35-40 years in AU, BOO in PH) lock in the operator's platform.
- Data migration is hard: paper, microfiche and scanned titles (25M in PH, 27M titles at HMLR) must be converted while transactions keep flowing.
- Changing the register often needs a statutory amendment (Malaysia amended the National Land Code for SPTB; Queensland's Land Title Act 1994 created ATS).
- Procurement is political and slow, with audit-body challenges (e.g. COA questions on the PH LTCP).
- Systems are bespoke to local law. Landgate found no off-the-shelf product among about 37 Torrens jurisdictions.

## Notes

Several primary sources returned 403 or failed DNS and are not cited: Tyler product page, NSW Audit Office, PIB, Kompas, Manila Bulletin, CNBC, citizenportal (Erie County AS/400), Fidlar and kav-egov. US vendors do not publish install-base counts: Tyler and Harris give none, and Fidlar's "200+ counties" came from search snippets only. The Kofile figure of 3,000+ counties is a vendor claim. It is close to the total number of US counties (3,031), so it probably counts counties that use any Kofile service, not counties running its system of record. The Queensland ATS source is the Titles QLD Land Title Practice Manual PDF; its text was extracted locally. The Vietnam evidence comes from a FIG 2022 presentation PDF, also extracted locally. Gaps: Indonesia (KKP first-ship year and total office count are approximate), Thailand (no vendor identified) and the EU (national systems are too varied; ELRA count used). S4 is unproven for this category. HMLR's mainframe language is not disclosed. The UK LLC programme date of about 2015 is not sourced (one commenter mentions 2008). The confirmed facts are a delay to end-2028 and 110 councils migrated by Mar 2025.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
