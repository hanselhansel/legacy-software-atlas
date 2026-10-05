# Wealth and portfolio accounting

Slug: `wealth-portfolio-accounting`

## Systems

- SS&C Advent Axys (Windows client-server PMS, REPLANG report language)
- SS&C Advent APX and Geneva
- FIS Investment Accounting Manager (formerly InvestOne; COBOL, IBM mainframe/CICS origin)
- SEI TRUST 3000 (bank trust and investment accounting)
- Avaloq Banking Suite / Avaloq Core (private banking and wealth core)
- Temenos Triple'A Plus (ex-Odyssey Financial Technologies) and T24 Private Wealth
- SimCorp Dimension (front-to-back investment management)
- WealthSpectrum by Applied Software (India PMS back office)
- Excel/spreadsheet aggregation in family offices

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. FIS InvestOne was built in-house in COBOL in the 1980s on IBM mainframe and still runs a COBOL engine wrapped in Java. It runs over 60% of mutual funds. Goldman Sachs licensed InvestOne in 1991 and still ran it on mainframe with a custom COBOL layer. Advent built one of the first PC-based portfolio accounting apps in 1983 (Axys lineage). SEI built TRUST 3000 in the 1970s. Avaloq was founded 1985. ([source](https://www.microfocus.com/media/case-study/fis-cs.pdf))
- **S2 slow to replace**: met. Goldman Sachs (AWS re:Invent 2024 FSI312 slides) ran a 12-month tactical mainframe replatform of InvestOne inside a roughly 5-year strategic plan to move to FIS's modern platform. SEI's 10-K says SEI Wealth Platform initial contracts typically run 5 to 7 years, with TRUST 3000 at 3 to 7 years. The Platform rolled out in the UK from 2007, to US banks from 2012 and to advisors from 2015. Julius Baer began its Temenos core replacement in 2015 and targets most of the Swiss replacement by 2028. Kitces says 60 to 80% of PMS implementations miss their original timeline. DBS has run Avaloq for 18 years. ([source](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/events/approved/reinvent-2025/reinvent/2024/slides/fsi/FSI312_Replatforming-for-reinvention-Modernizing-mainframes-at-Goldman-Sachs.pdf))
- **S3 workarounds**: met. RBC/Campden North America Family Office Report 2024: the operational risks family office executives cite most often are over-reliance on spreadsheets and manual data aggregation. Avaloq's 2023 survey of 200 wealth professionals (UK, CH, DE, SG, JP, HK) found 45% call their systems outdated, 54% use too many applications and 14% use 10 to 15 systems (finews.com). Simple's 2024 family office report says many still rely on Excel. ([source](https://www.rbcwealthmanagement.com/assets/wp-content/uploads/documents/campaign/the-north-america-family-office-report-2024.pdf))
- **S4 shrinking skills**: met. Goldman Sachs' InvestOne slides list 'Difficult finding mainframe skill set' as a business challenge. They also cite about $6M a year in mainframe cost, custom COBOL modules that are hard to change, and FIS eventually ending mainframe support. Advent's REPLANG report language remains niche, and consultants such as AdventGuru sell that expertise. Avaloq roles ask for proprietary scripting and certification. That last point comes from job posts, not a skills-shortage study. ([source](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/events/approved/reinvent-2025/reinvent/2024/slides/fsi/FSI312_Replatforming-for-reinvention-Modernizing-mainframes-at-Goldman-Sachs.pdf))

## Segments

Enterprise: mainframe and big-core systems (FIS InvestOne at Goldman Sachs and fund administrators, SEI TRUST 3000 at 94 US banks in 2016, U.S. Bank's TRUST 3000 to SEI Wealth Platform move, Avaloq at DBS and Julius Baer, SimCorp at 190+ asset managers). Mid-market: Advent Axys/APX at RIAs and wealth managers (Kitces counts about 2,000 mid-to-large RIAs as the core target), plus Temenos Triple'A Plus at regional private banks such as BPI and EFG. SMB and family offices: Axys and spreadsheets (RBC 2024 report). Government: limited direct use, though central banks and sovereign funds appear among SimCorp clients.

## Reasons buyers stay

- Book of record and audited performance history live in the old system; conversions risk breaking GIPS-style return series and cost-basis data
- 60-80% of PMS implementations overrun timelines and costs can revert to list price (Kitces)
- Custom reports (REPLANG on Axys/APX) and custom COBOL orchestration layers (Goldman on InvestOne) embed years of firm-specific logic
- Vendors offer modernisation without switching: FIS replatformed InvestOne to Linux/containers and 75% of its clients are hosted; SS&C keeps shipping Axys versions
- Long 5-7 year contracts and multi-entity core-banking integration (Avaloq, Temenos) tie wealth accounting to the bank core
- Regulatory reporting and custodian feeds are already wired and certified

## Notes

The strongest primary evidence is in four sources. (1) FIS/Micro Focus case study: InvestOne was written in COBOL on IBM mainframe in the 1980s and runs over 60% of mutual funds. (2) Goldman Sachs AWS re:Invent 2024 slides: InvestOne licensed in 1991, about $6M a year mainframe cost, 'difficult finding mainframe skill set', 5-year strategic plan. (3) SEI 10-K FY2016: TRUST 3000 at 94 US banks, contracts of 3-7 years and 5-7 years. (4) RBC 2024 family office report on spreadsheet reliance. Gaps: Axys, APX and Geneva first-ship years were not confirmed in a primary source (Kitces dates Advent's PC accounting to 1983). Temenos Triple'A Plus's installed base (reported as about 110 at the 2010 Odyssey deal) could not be opened because Finextra and BankTech blocked fetch, so it is omitted. SimCorp Dimension's launch year was not confirmed. UK and AU firm-level register counts were not extracted: the FCA register returned 403, and for AU only the individual adviser count was found. The Thailand count overlaps across licence types. The Vietnam count comes via VnEconomy citing the SSC. SS&C's 2015 10-K cites 4,200+ Advent customers at acquisition, but I did not open it; the 4,300 figure is from A-Team. The fintechfutures Ridgeline page returned 403, so the WealthManagement.com article was used instead. Challenger founding years left blank were not stated in the sources opened. Treat the Addepar founding year (commonly 2009) as unverified.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
