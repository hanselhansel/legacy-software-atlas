# Mortgage servicing

Slug: `mortgage-servicing`

## Systems

- ICE (formerly Black Knight) MSP Mortgage Servicing Platform: z/OS mainframe, COBOL batch + CICS, DB2/VSAM, vendor-hosted
- Sagent LoanServ (ex-Fiserv MortgageServ), now marketed as the Dara cloud platform
- FICS Mortgage Servicer (on-prem / hosted, for mid-size banks, credit unions and commercial servicers)
- Phoebus Software platform (UK/Ireland mortgage and savings administration, designed 1989)
- Target Group (Tech Mahindra) loan management / servicing platform (UK)
- Nucleus Software FinnOne / FinnOne Neo lending suite (India, SE Asia)
- Core-banking loan modules (Temenos, Finacle, Silverlake and similar) used for mortgage servicing at Asian banks. Inferred, no source found for this study.

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. PennyMac's 2019 FAQ says MSP 'is founded on an outdated, mainframe green screen technology designed decades ago' and calls it 'the mainframe computer technology of MSP'. PennyMac's complaint (SEC exhibit) says MSP was 'first developed over 50 years ago' and depends on 'a mainframe that relies on back-end and batch processing technology'. An ICE job post from Oct 2026 for the MSP team asks for z/OS COBOL batch and CICS, JCL and DB2/VSAM. Black Knight's history starts with Computing and Statistical Services in 1962. Phoebus was designed in 1989 and FICS founded in 1983, so the non-US cores also predate 2005. ([source](https://s201.q4cdn.com/340896660/files/doc_presentations/2019/11/2019-Servicing-Systems-Environment-FAQ.pdf))
- **S2 slow to replace**: met. Mr. Cooper's 2022 deal with Sagent includes a seven-year commitment to the servicing platform (National Mortgage News, Feb 11 2022). Black Knight's FY2019 10-K says switching servicing software providers 'can take 12 to 18 months, or longer'. PennyMac's complaint says regulators require extensive testing, so system changes can 'take years to accomplish'. PennyMac gave more than 18 months' notice and moved off MSP module by module over many years. Further corroboration: a 2021 Sagent/Servion deal ran 7 years (search title only, not opened). ([source](https://www.nationalmortgagenews.com/news/mr-cooper-gains-20-stake-in-sagent))
- **S3 workarounds**: met. PennyMac says Black Knight encourages servicers to download loan data from MSP and upload it back so they can do the work in their own or vendor tools, and charges separately for that data exchange. PennyMac's SSE began as 'hundreds' of bolt-on modules around MSP. CFPB Supervisory Highlights Issue 11 (June 2016) found transferees delayed in-flight modifications because IT had to 'manually override data fields whenever the servicing platform rejected transferor data'. No public source was found that names spreadsheets specifically. ([source](https://files.consumerfinance.gov/f/documents/Mortgage_Servicing_Supervisory_Highlights_11_Final_web_.pdf))
- **S4 shrinking skills**: met. ICE's Oct 2026 Senior Mainframe Developer post for the MSP team (onsite in Jacksonville) asks for 8+ years of z/OS COBOL batch and CICS, JCL, DB2/VSAM and ISPW. It lists experience with AI coding tools (Claude Code) as a strong plus, which points to a thin talent pool. Across financial services, a Deloitte survey cited by BizTech (Apr 2025) found 71% of firms say mainframe teams are understaffed and 54% underfunded. That source does not single out mortgage servicing. ([source](https://freehire.me/jobs/senior-mainframe-developer-intercontinental-exchange-holdings-inc-mbjskvl3))

## Segments

Mainframe MSP is concentrated in the US enterprise segment: the largest banks, nonbank servicers and subservicers. MSP serviced about 36M loans (FY2022 10-K) and 7 of the top 10 servicers in the J.D. Power 2024 study per ICE. Mid-market and community banks, credit unions and state housing agencies use MSP (Virginia Housing renewal reported), Sagent LoanServ or FICS Mortgage Servicer. FICS reports 29 of its servicing clients in the MBA top 100 commercial/multifamily servicers (search snippet). Government: state housing finance agencies in the US (e.g. Virginia Housing on MSP), and Asian state housing lenders such as Thailand's Government Housing Bank, which BOT lists as an SFI. In the UK the buyers are mid-market building societies, specialist lenders and closed-book owners, using Phoebus and Target, often through outsourced servicing. In India and SE Asia, mortgages are mostly serviced inside bank core or lending suites (FinnOne, core-banking loan modules), at enterprise and mid-market banks and HFCs. No primary source was found to tie a specific legacy servicing product to SE Asian SMB lenders.

## Reasons buyers stay

- Switching takes 12 to 18 months or longer, and the cost is significant (Black Knight FY2019 10-K).
- Regulators expect extensive testing and validation before a servicer changes major systems (PennyMac complaint).
- Servicing transfers carry CFPB exposure: lost loss-mitigation documents and late payment crediting during data moves.
- Investor, GSE and agency reporting (Fannie, Freddie, Ginnie, FHA/VA) is already built and certified on the incumbent.
- Multi-year contracts (for example Mr. Cooper's 7-year commitment to Sagent) and long renewals lock buyers in.
- Network effects: subservicers, MSR buyers and vendors integrate to MSP formats, so leaving it adds friction on every transfer.
- Vendor litigation risk: Black Knight sued PennyMac in 2019 when it left MSP.

## Notes

The US is the clearest legacy market in this category. One mainframe COBOL/CICS system (ICE MSP, ex-Black Knight) services roughly 51-62% of US first-lien loans, depending on year and source. ICE's FY2025 10-K no longer breaks out MSP loan counts, so the latest hard figure is about 36M loans in Black Knight's FY2022 10-K.

The strongest public evidence comes from PennyMac's 2019 litigation material (FAQ and SEC-filed complaint). It is partisan, so treat its characterisations (mainframe, green screen, 50+ years old) as one side's claims. ICE's own 2026 MSP job post does corroborate the z/OS COBOL/CICS stack.

S2 evidence is a 7-year Mr. Cooper/Sagent commitment plus the 10-K's 12-18 month switching estimate. LoanCare's 7-year MSP renewal appeared in search results, but the page could not be opened, so it is not cited.

S3 rests on vendor-sanctioned data download/upload around MSP and a CFPB finding of manual data-field overrides. No primary source naming spreadsheets was found. S4 rests on ICE's job post and a cross-industry Deloitte survey, not mortgage-specific data.

Outside the US, mortgage servicing is mostly a module of core banking or lending suites. UK has Phoebus (1989) and Target. India and SE Asia have Nucleus FinnOne and bank cores. No primary source was found tying a specific pre-2005 servicing product to ID, VN, MY, TH or PH banks, so S1-S4 should not be generalised to those regions without more research.

Buyer-universe gaps: BNM (MY) and BOT (TH) pages did not render counts. The UK PRA page gave only the ~1,300 total. The EU figure covers euro-area SSM entities only. US nonbank servicers (licensed through NMLS) are a major buyer group and are not counted. Pages that returned 403 or refused connection were not used as sources (mortgageorb, inman, businesswire, rismedia, nationalmortgageprofessional).

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
