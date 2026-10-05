# Law firm practice management

Slug: `legal-practice-management`

## Systems

- Elite Enterprise (Thomson Reuters/Elite; on-prem time and billing, end of maintenance 2022)
- Elite 3E (on-prem and cloud; successor to Enterprise)
- ProLaw (Elite; on-prem integrated front/back office for mid-size firms)
- Aderant Expert (on-prem; cloud version Expert Sierra) and legacy Aderant CMS / acquired RainMaker, Omega, Javelan
- PCLaw and Time Matters (LexisNexis, now PCLaw | Time Matters JV with LEAP; Windows desktop)
- Tabs3 / PracticeMaster (on-prem desktop, cloud option added)
- LexisNexis Axxia (UK; end of life Jan 2020)
- Tikit FirmWare, Envision, Partner for Windows, SOS Connect, Pilgrim LawSoft (UK mid-tier legacy PMS)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Time Matters shipped as MS-DOS software in 1989 and on Windows from 1994. Tabs3 dates from 1979 and still offers on-prem versions. Clark Hill ran Elite Enterprise on-prem from 1994 until it moved to 3E cloud around 2025. LexisNexis described PCLaw as its 'on-premise solution' in 2019. Aderant Expert is on-prem; only 40% of Expert firms had moved to cloud Sierra by 2026. ([source](https://en.wikipedia.org/wiki/Time_Matters))
- **S2 slow to replace**: met. Clark Hill ran Elite Enterprise from 1994 to roughly 2025, about 30 years. Elite Enterprise went into maintenance-only mode in 2016 and support ended 31 Dec 2022, yet migrations were still finishing in 2025. Legal IT Insider (2016) warned that an Enterprise migration is 'a slog' of at least a year. Lights-On says PMS selection plus implementation takes 12 to 24 months, with about 60 UK firms caught by end-of-life dates. Aderant says it took eight years after Sierra's 2018 launch to move 40% of Expert firms to cloud. ([source](https://www.legalsupportnetwork.co.uk/resource/clark-hill-completes-move-from-enterprise-to-3e-in-the-cloud-by-elite/))
- **S3 workarounds**: met. BigHand's 2025 pricing and budgeting report found 49% of firms have no legal pricing or budgeting tool, and nearly half still use manual tools for budgets and financial reporting outside the PMS. This shows spreadsheet workarounds, but no primary survey was found that measures re-keying or screen-scraping against the PMS itself. ([source](https://www.bighand.com/en-us/resources/whitepapers/2025-legal-pricing-and-budgeting-report/))
- **S4 shrinking skills**: not met. No cited evidence of a COBOL/RPG-style skills shortage. These systems run on Windows/SQL Server (and some older Unix/Informix-era Elite builds, not confirmed in sources opened). The only constraint found is Lights-On's note of 'limited supplier resource' for about 60 UK firms facing PMS/DMS end of life. That is consultant capacity, not a scarce language skill. ([source](https://www.lights-on.com/is-your-firm-running-end-of-life-software/))

## Segments

Two tiers. Enterprise and upper mid-market (roughly 50+ lawyers) run Elite Enterprise/3E, ProLaw and Aderant Expert. Elite counts 75% of the Am Law 100. Aderant claims 98% of the Am Law 200, and only 23% of its Am Law 200 Expert users were on cloud Sierra. SMB and solo firms run desktop PCLaw, Time Matters and Tabs3: PCLaw/Time Matters alone had 15,000 paying customers in 2019. In Australia, Smokeball estimates 100,000 small and mid-size firms across Australia and the US use no law-specific software at all. Small firms dominate the counts: 78% of Australian practices are sole practices, and 6,613 of Malaysia's 7,551 firms have 1-5 lawyers. Government legal departments are a minor segment. Filevine sells to government agencies, but no legacy-PMS evidence was found for government.

## Reasons buyers stay

- Replacement is a full reimplementation, not an upgrade. Enterprise-to-3E moves were described as at least a year of 'slog' and costlier than planned.
- Trust/client-account accounting and regulator rules (SRA, state bars) make data migration high-risk.
- Deep customisation and integrations (DMS, e-billing, docketing) built over decades. Aderant markets Sierra as moving these over intact.
- Incumbent vendors offer lift-and-shift cloud hosting of the same product (Expert Sierra, 3E cloud), so firms can modernise without switching vendor.
- Partners resist changing time-entry and billing workflows. Firms on vendor-acquired legacy products often stay with the same vendor family (22 Aderant legacy clients in 2014 'didn't really look at other solutions').

## Notes

Market split: Elite (3E/Enterprise/ProLaw) and Aderant (Expert) dominate large firms worldwide, including in SG/MY/AU. Desktop PCLaw, Time Matters and Tabs3 dominate US/Canada SMB firms. UK mid-tier had its own legacy set (Axxia, Envision, FirmWare, Enterprise), much of it past end of life by 2020-2022. Incumbents are moving their own installed bases to hosted versions (3E cloud, Expert Sierra), which narrows the opening for outsiders at the top end. The opening is wider in SMB, where Clio, Filevine and Smokeball are growing fast.

Gaps:
- No primary firm counts for EU (CCBE counts lawyers only), IN (all-India advocate total not verified; Ministry of Law PDF returned 403), ID, TH or PH. Those registers count lawyers, not firms.
- The US Census figure came from a search snippet because the data.census.gov profile did not render.
- The Singapore firm count (about 1,000 in 2021) came from a snippet because the article returned 403.
- First-ship dates for Elite Enterprise (in use by 1994), Aderant CMS and PCLaw are not confirmed in primary sources. The Canadian Lawyer claim that PCLaw was 'introduced in 2019' is wrong and was ignored.
- S3 rests on BigHand's 49% manual pricing/budgeting finding, not on PMS re-keying data.
- S4 is not met: no scarce-language evidence was found.
- No SEA-local legacy PMS vendors were found with disclosed install bases.

Sources also opened:
- Elite Enterprise end-of-life advice: https://www.legaltechnology.com/2016/03/16/comment-advice-to-elite-enterprise-firms-start-migration-by-slicing-the-salami-rather-than-going-for-big-bang/
- Aderant Sierra migration stats: https://www.aderant.com/expert-to-sierra-migration/
- Aderant 170 Sierra clients: https://legaltechnology.com/2024/03/05/aderant-announces-it-has-170-expert-sierra-clients/
- PCLaw | Time Matters JV with LEAP: https://www.lexisnexis.com/community/pressroom/b/news/posts/leap-and-lexisnexis-close-formation-of-joint-venture-in-practice-management-software
- Aderant legacy-platform clients (2014): https://www.prweb.com/releases/22_law_firms_on_legacy_platforms_upgrade_to_aderant_expert_and_aderant_total_office/prweb12118958.htm
- ProLaw history: https://legaltechnology.com/2023/04/11/guest-post-why-elite-and-prolaw-didnt-work-at-tr/

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
