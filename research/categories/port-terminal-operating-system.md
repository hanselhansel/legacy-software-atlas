# Port and container terminal operating systems (TOS)

Slug: `port-terminal-operating-system`

## Systems

- Navis SPARCS / SPARCS Express (Kaleris), on-prem predecessor of N4
- Navis N4 (Kaleris), first site live 2006
- PSA CITOS (in-house, 1988)
- Hutchison Ports nGen (in-house, 2003)
- Tideworks Mainsail / Mainsail Vanguard (SSA Marine subsidiary)
- Total Soft Bank CATOS (Korea)
- RBS TOPS / TOPX (Australia)
- Pelindo legacy TOS / PTOS-M being consolidated onto ILCS TOS Nusantara (Indonesia)
- Operator in-house legacy TOS (for example Patrick Terminals' 30-year in-house system replaced by N4 in 2020; seen only in search snippets)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Academic history: the first commercial TOS were CITOS (1988) and Navis (1989). Georgia Ports Authority ran Navis SPARCS/Express at Garden City Terminal from fall 2000 until April 2022. Hutchison's nGen went live in 2003. RBS TOPX shipped in 1996. All of these are pre-2005 cores. Gap: the sources read show they are pre-cloud and on-prem, but they do not document a mainframe or midrange architecture. ([source](https://arxiv.org/pdf/1904.13251))
- **S2 slow to replace**: met. GPA's FAQ says SPARCS/Express ran at Garden City Terminal from 2000 to 2022. That is about 21 years of tenure before the N4 cutover, which itself needed a full operational shutdown window. A vendor buyer's guide (INTECH, theintechgroup.com/blog/tos-buyers-guide-terminal-operating-system/) says TOS implementations at mid-to-large terminals take 12 to 24 months, and that migrating 10+ years of history takes 4 to 8 months of data engineering. DP World Australia's N4 standardisation across Sydney, Fremantle, Melbourne and Brisbane ran over 'the last few years' (2013 to 2014) to consolidate 19 systems. Lifecycles run well past 7 years. Single-site projects run 1 to 2 years, and multi-site programmes run multiple years. ([source](https://gaports.com/n4/n4-faqs/))
- **S3 workarounds**: met. Portwise Consultancy reports that smaller terminals still run berth planning on spreadsheets or whiteboards and see the clearest gains when they move off them. Heilig et al. (arXiv 1904.13251) note that terminals typically run several software sub-systems, which makes software and data integration difficult. They cite the Port Strategy piece 'Ditch the spreadsheet' (Rushmere 2017). Evidence is moderate: no source quantifies how widespread re-keying or screen-scraping is at large terminals. ([source](https://www.portwiseconsultancy.com/blog/which-software-helps-with-efficient-berth-planning/))
- **S4 shrinking skills**: met. Weak evidence. KiTalent, a recruiter's market-intelligence article from May 2026, says senior TOS specialists take 8 to 11 months to recruit in Rijeka. It also says one terminal held a Navis N4 integration manager vacancy open for nine months in 2024. The scarcity is in vendor-specific TOS configuration and integration skills (Navis N4/SPARCS administration), not in a dead language like COBOL or RPG. The source is recruiter content marketing and covers Europe only. No APAC-specific or language-level scarcity evidence was found. ([source](https://kitalent.com/articles/rijeka-port-talent-gap))

## Segments

Mostly enterprise and government. Buyers are state port authorities and state-owned operators, for example Georgia Ports Authority (US), JNPA/JNPCT (IN), Pelindo (ID) and the Port Authority of Thailand. Global terminal operators also buy, including PSA, Hutchison, DP World, SSA/Tideworks and ICTSI. Large operators often run in-house cores (PSA CITOS, Hutchison nGen) or Navis N4/SPARCS. Mid-market terminals of roughly 100k TEU and up, plus mixed-cargo terminals, are served by Tideworks, CATOS, RBS TOPS and cloud TOS such as Octopi, which Navis bought in 2019 explicitly to reach small terminals. SMB and very small or river terminals often run berth and yard planning on spreadsheets or whiteboards (Portwise). SMB is not a meaningful buyer of the full TOS.

## Reasons buyers stay

- A TOS is mission-critical real-time control. Failed cutovers hurt operations badly: Felixstowe's June 2018 switch from Navis to Hutchison nGen caused lost boxes and truck queues of up to 16 hours (seen in search snippets; the Seatrade article returned 403).
- Cutovers need a full operational shutdown window (GPA stopped operations overnight for N4) and 12 to 24 months of implementation.
- Deep integration with automated equipment, gates, RFID, EDI and port community systems (PD Ports' Navis role lists SPARCS, MCP, Fast gate, WhereNet RFID, Camco Autogate, VBS). Every interface has to be re-done.
- Data migration of 10+ years of container, vessel and customer history takes 4 to 8 months.
- Big operators treat their in-house TOS as a competitive asset (PSA CITOS, Hutchison nGen) and build the next generation in-house rather than buy.
- There is a small, concentrated vendor field, and specialist TOS staff are hard to hire. Both raise switching risk.

## Notes

Sources that would not open and were not used as evidence: the Seatrade Felixstowe articles (403), CIO.com on CITOS (403), Port Technology's Kaleris listing and Octopi article (403), tsb.co.kr (403), BTS (403), PPA Philippines (TLS error), the USACE WCSC page (403), Patrick Terminals' N4 migration articles (403 or failed), and the Mombasa CATOS paper (DNS failure). Patrick replacing a '30-year-old legacy TOS', Felixstowe's 2018 nGen disruption, Kaleris '650+ organisations', Portchain's total of over $10M, and Awake.AI's details all come from search snippets only and are unverified.

There are inconsistencies. TSB's founding year is 1998 per ITEA and 1988 per a snippet. Navis install counts range from 389 N4 terminals (GPA FAQ, 2022) to 'more than 500 ports' (Kaleris, 2024). Navis was acquired by Accel-KKR in 2021 (Tracxn) and folded into Kaleris in 2022.

On S1, the pre-2005 cores are well documented. The mainframe or client-server architecture is not.

S4 is weak. The only scarcity source is a recruiter's content piece about Europe, and it describes vendor-specific TOS skills, not COBOL or RPG.

PSA Tuas: PSA's page confirms the city terminals move by 2027 and that Tuas is billed as the world's largest fully automated terminal. It does not name CITOS or the new TOS.

APAC footprint seen in opened sources:
- Navis N4: PTP (since 2019; N4 4.0 upgrade) and Northport (MY, contract 2024), TIPS Laem Chabang (TH), SPCT (VN, 2009), JNPCT (IN, 2017), DP World Australia.
- RBS TOPX: Cat Lai (VN, since 2008).
- RBS TOPS: Indonesia, via its regional partner.
- Pelindo's TOS Nusantara (ID).

An Indonesian buyer count above 636 public ports would include terminals that do not need a container TOS. Of the 636, 102 are commercial ports.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
