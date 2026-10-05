# Courts and justice case management

Slug: `courts-justice`

## Systems

- Mainframe court systems built in-house, e.g. Hawaii HAJIS and DC Crim (IBM z9/Multiprise, Adabas, Natural 2, COBOL/CICS, 3270 terminals) and JUSTIS (IBM AS/400)
- Victoria (AU) Courtlink, a mainframe case management system installed about 30 years before 2018
- Washington State Judicial Information System (JIS, formerly DISCIS), built in-house since 1988
- US federal CM/ECF (Case Management/Electronic Case Files), nearly 30 years old
- UK HMCTS Libra (magistrates' courts) and Xhibit (Crown Court), now being replaced by Common Platform
- Germany: JUDICA, EUREKA, EUREKA-Fach, forumSTAR, web.sta, MESTA and GO§A, all being replaced by GeFa
- Tyler Technologies Odyssey (now Enterprise Justice), general release 2003
- Journal Technologies eCourt / eSeries
- Justice Systems FullCourt / FullCourt Enterprise
- equivant (Constellation Software) CourtView and JustWare/JWorks
- Court Contexte (COTS base of Hawaii JIMS)
- NSW JusticeLink (KAZ Group/Telstra)
- Singapore CrimsonLogic EFS (2000), replaced by eLitigation (2013)
- India eCourts Case Information System (CIS) by NIC
- Malaysia e-Kehakiman CMS/eFS
- Philippines eCourt
- Indonesia SIPP (Sistem Informasi Penelusuran Perkara) and e-Court of the Mahkamah Agung
- Thailand Court of Justice CIOS

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Hawaii Judiciary RFP J23057, Attachment 7: the criminal and civil case systems were first written in the 1960s and 1970s. HAJIS runs on an IBM z9 mainframe, built with Adabas, Natural 2 and COBOL/CICS, and users reach it only through 3270 terminals or 3270 emulation. DC Crim runs on an IBM Multiprise 3000 with Adabas/Natural. Juvenile JUSTIS has run on AS/400 since 1991. Other examples: Victoria's Courtlink is a mainframe system installed about 30 years before 2018 (Computerworld). Washington JIS has been in-house since 1988. Federal CM/ECF is nearly three decades old (uscourts.gov, 2026). ([source](https://hiepro.ehawaii.gov/resources/108209/ATTACHMENT%207-Attachment%207%20Judiciary%20Technical%20Background%20and%20Current%20Systems.pdf))
- **S2 slow to replace**: met. Maryland's statewide MDEC replacement of local case management systems with Tyler Odyssey began in fall 2014 and finished on 6 May 2024, about 10 years. Other cases: Germany's GeFa started in 2017 to replace JUDICA, EUREKA, forumSTAR and others, with rollout targeted for 2030 (BMJV). HMCTS reform began in 2016 and was extended to March 2025 (NAO, Inside HMCTS). Hawaii's JIMS started in 2003 and still had modules pending in 2012. Victoria picked Journal Technologies in 2019 (A$89.2m, rollout planned mid-2021), and criminal go-live was 2026. California CCMS cost estimates grew from $260m (2004) to $1.9bn (2010) before it was terminated. That last figure is from the CA State Auditor via search only, not opened. ([source](https://www.courts.state.md.us/media/news/2024/pr20240506))
- **S3 workarounds**: met. Hawaii Judiciary RFP J23057: DC Crim and HAJIS do not share data, and 'all case data passed from one system to the other must be manually re-entered'. Case processing relies on paper, fax, phone and messengers, with spreadsheets and simple databases alongside. Victoria: the courts run 'a range of manual and automated processes that sit on top of nine case management systems' (Computerworld 2018). UK: OSR found Common Platform staff entered final results in free-text fields instead of result codes, fixed in August 2024 (https://osr.statisticsauthority.gov.uk/publication/review-of-the-quality-of-criminal-court-statistics-for-england-and-wales). ([source](https://hiepro.ehawaii.gov/resources/108209/ATTACHMENT%207-Attachment%207%20Judiciary%20Technical%20Background%20and%20Current%20Systems.pdf))
- **S4 shrinking skills**: not met. Court-specific evidence that the skills are scarce could not be verified from an opened source. Indirect evidence only. The Georgetown Judicial Innovation Fellowship roadmap (2023) says court legacy systems 'written in outdated languages, like COBOL' make modern functionality 'cost- and resource-prohibitive'. Hawaii shows live Adabas/Natural/COBOL-CICS dependence. Computerworld (2012) reports a general COBOL shortage: 46% of 357 IT staff saw a shortage, and Saginaw County MI had 4m lines of COBOL. Not opened: a Courthouse News story quoting a California court clerk ('Our programmer retired this past December') on losing its only COBOL programmer (blocked by Cloudflare), and a Berrien County MI vendor review citing difficulty finding COBOL/Natural programmers for its court mainframe (HTTP 403). Leaving met=false until one of these primary sources can be opened. ([source](https://www.law.georgetown.edu/tech-institute/wp-content/uploads/sites/42/2023/02/Judicial-Innovation-Fellowship-Roadmap-1.pdf))

## Segments

Government only. The buyers are state and national judiciaries plus county and municipal clerks, not private firms. Enterprise-scale (statewide or national): Maryland MDEC (24 jurisdictions on Tyler Odyssey), Tyler's 22 statewide Enterprise Justice implementations, HMCTS (England and Wales), Germany's 16 Länder (GeFa), India eCourts (2,852+ complexes), Indonesia Mahkamah Agung (950 courts), Vietnam TANDTC (390 courts). Mid-market and SMB equivalents are the fragmented US county and municipal courts. Michigan's 242 trial courts run 16 different case management systems (Michigan legislative report via search), Berrien County MI ran court apps in COBOL/Natural on a county mainframe, and Cook County IL Clerk was still moving its last legacy apps off the mainframe in 2022. Vendors like Justice Systems FullCourt ('hundreds of courts') and equivant (350+ agencies) serve this tier. Adjacent buyers: prosecutors, public defenders and probation, served by Journal Technologies eProsecutor/eDefender.

## Reasons buyers stay

- Replacements fail or run long and over budget. California CCMS ($260m to $1.9bn, then terminated), UK Libra (£146m bid rose to £318m, core application missed its 2001 deadline), HMCTS Common Platform rollout paused over performance problems
- Statewide migrations take a decade or more (Maryland MDEC 2014-2024, Germany GeFa 2017-2030), so courts keep the old system running in parallel for years
- Courts depend on many interfaces with police, prosecutors, criminal history repositories, NCIC and DMV (Hawaii lists AG, HCJDC, NCIC, DOT and police interfaces), so every interface must be rebuilt
- Statutory record-keeping and data integrity. Common Platform free-text results corrupted official criminal statistics (OSR), which raises perceived risk
- Funding is fragmented: Michigan's 242 trial courts have 165 local funding sources. Budgets are annual appropriations, not capital programmes
- Judicial independence and consensus. A single judge can stop a modernization project (Georgetown JIF roadmap)
- Few vendors and lock-in to incumbents (Tyler, Journal Technologies, equivant) with long statewide contracts

## Notes

Every source URL was opened, except where a field says otherwise.

S4 is set to false on purpose. Two court-specific COBOL-scarcity sources showed up in search but could not be opened: Courthouse News (Cloudflare) and the Berrien County MI CMS vendor review (403). The Hawaii RFP J15137 for Natural/ADABAS/COBOL consulting (403) and Michigan's 2023 CMS assessment and 2026 JIS legislative report (403) also could not be opened. Opening any one of these would likely flip S4 to true.

Other figures seen only in search snippets, not opened:
- CA State Auditor: CCMS cost rose from $260m to $1.9bn.
- Cook County IL: $36.4m Tyler contract in 2017 to replace the mainframe. The Clerk's own 2022 IT plan (opened as PDF text) confirms 'Move the final Legacy applications off the Mainframe' and the Odyssey phases from 2018 to 2022.

Market structure: in the US, Tyler, Journal Technologies and equivant (Constellation) are the incumbents, and Tyler's 10-K names Thomson Reuters and Constellation as competitors. Outside the US, most systems are government-built: NIC CIS in India, Mahkamah Agung SIPP in Indonesia, HMCTS in the UK, German Länder systems moving to GeFa, CrimsonLogic in Singapore. So the buyer is usually one central judiciary or ministry, and AI-native challengers mostly sell overlays (transcription, judge copilots, reminders) instead of full replacements.

Philippines: eCourt (2013) was found in a 3ie RCT to have no impact on disposition and to slow clearance at first. Its replacement, eCourt 2.0, is in pilot (SC page failed TLS and was not read).

Malaysia and Thailand: no vendor-disclosed counts found. The UK Common Platform, Libra and Xhibit status comes from the Inside HMCTS blog (Feb 2024): Libra and Xhibit are to be retired, and DCS is retained.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
