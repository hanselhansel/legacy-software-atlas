# Capital markets trading, clearing and brokerage back-office

Slug: `capital-markets-trading-clearing`

## Systems

- Broadridge Brokerage Processing Services (BPS), the US broker-dealer back office. Its lineage goes back to the ADP brokerage services group (1962), and Broadridge still runs it on mainframe infrastructure that Kyndryl operates
- 63 moons (formerly Financial Technologies) ODIN broker front-office/trading terminal (India, 1998)
- 63 moons exchange trading, clearing and settlement stack (DOME framework 2002; MCX platform since 2003)
- ASX CHESS clearing, settlement and subregister system (Australia, live since 1994)
- NSE NOW broker trading front end (India, discontinued 2020)
- MPC (Micro Piranti Computer) S21 / S21+ BOFIS broker back office (Indonesia)
- FSS FLEX core securities system (Vietnam)
- TCS BaNCS for market infrastructure and brokerage. It is the replacement platform at MCX rather than a legacy incumbent

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Every core system I verified predates 2005. Broadridge brokerage processing started in 1962 under ADP. Broadridge's FY2026 10-K says Kyndryl supports its 'mainframe, midrange, network and data center operations', with that agreement extended to 31 Dec 2031 and a new mainframe equipment lease starting March 2027. ASX CHESS went live in 1994. 63 moons' ODIN shipped in 1998 and its DOME exchange framework in 2002. DOME ran MCX trading and clearing from 2003 until the move to TCS in Oct 2023. ([source](https://www.sec.gov/Archives/edgar/data/0001383312/000162828026052243/br-20260630.htm))
- **S2 slow to replace**: met. MCX picked TCS in Feb 2021 to replace 63 moons by 30 Sep 2022. Go-live slipped to Dec 2022, then Jun 2023, then Oct 2023, and SEBI asked MCX on 28 Sep 2023 to hold off. MCX had to buy extensions from 63 moons. Fees went from Rs 15 cr a quarter to Rs 60 cr, then Rs 81 cr, then Rs 125 cr. Rs 222 cr was paid over the three quarters Oct 2022 to Jun 2023, more than MCX's FY2021-22 profit of Rs 118 cr, and SEBI fined MCX Rs 25 lakh in May 2025 for not disclosing it (Moneylife report on the SEBI order). In Australia, ASX started replacing CHESS in 2016. It paused in Nov 2022 and wrote off A$245-255m. Release 1 of the new design is due 20 Apr 2026, with the full program running to about 2029. Broadridge carries $819m of deferred client conversion costs amortised over multi-year service terms, and its mainframe outsourcing runs to 2031. ([source](https://www.moneylife.in/article/sebi-slaps-rs25-lakh-penalty-on-mcx-for-delay-in-disclosures-linked-to-63-moons-contract/77238.html))
- **S3 workarounds**: met. In an April 2026 report, The TRADE cites Acuiti's head of research: most sell-side firms surveyed still rely on spreadsheets, emails and chat messaging. The headline survey numbers (sample size, percentages) sit behind a paywall and I could not verify them. The evidence is industry-wide and not tied to a named legacy product. ([source](https://www.thetradenews.com/tradeplus/sell-side-stuck-at-a-crossroad-between-manual-processes-and-dominating-automation/))
- **S4 shrinking skills**: met. The RBA's 2023 assessment says ASX has significant key-person risk on current CHESS because of the skills needed to service the ageing system, including people with experience in its programming language. Many vendors of CHESS's supporting technology had not announced upgrade plans beyond 2025. Clear Street's founders also describe market infrastructure as still running on archaic COBOL mainframes, but that is a challenger's claim, not independent evidence. No India or SEA skills-scarcity source was found. ([source](https://rba.gov.au/payments-and-infrastructure/financial-market-infrastructure/clearing-and-settlement-facilities/assessments/2022-2023/special-topic-the-current-chess.html))

## Segments

Legacy cores sit in two places. The first is market infrastructure: exchanges, clearing corporations and depositories. Examples are MCX on 63 moons until Oct 2023 and ASX CHESS, both national single-buyer, government-supervised replacements. The second is mid-market and enterprise broker-dealers and clearing firms. In the US, Broadridge BPS serves the 15 largest wealth providers and 20 of the 25 primary dealers. In India, small and mid-size brokers depended on ODIN (vendor-claimed 70-80% retail broking share) or on NSE NOW, which at least a third of about 800 NSE members used alone before it was shut in 2020. In Indonesia, MPC S21 BOFIS claims more than half of IDX members. In Vietnam, FSS FLEX runs at nearly 40 securities companies. Pure SMB use is limited to small brokers that license packaged terminals or back offices. Regulators (SEBI, RBA/ASIC, OJK via IDX's BOFIS rules) act as the government-side buyer or forcing function.

## Reasons buyers stay

- Regulators gate cutover. SEBI asked MCX on 28 Sep 2023 to hold its planned 3 Oct go-live, and the RBA/ASIC oversee CHESS milestones, so switching takes regulatory sign-off and mock trading.
- Replacement failure is costly and public. ASX wrote off A$245-255m in 2022 after Accenture found the new software 63% complete. Boards that saw this choose the incumbent extension.
- The incumbent gains pricing power during migration. MCX's 63 moons support fees rose from Rs 15 cr to Rs 125 cr a quarter while the TCS platform slipped, and staying still looked safer than a rushed cutover.
- Conversion costs are sunk and multi-year. Broadridge carries $819m of deferred client conversion costs amortised over service terms, and clients would face the same cost again to leave.
- Network integration: a broker back office links to the exchange, the depository (KSEI C-BEST in Indonesia, VSDC in Vietnam, CDSL/NSDL in India), bank RDN accounts and the clearing house. Every link has to be re-certified.
- The current system works. ASX's 2022 release said current CHESS remains secure and stable and is performing well.

## Notes

This study verifies the seed's Rs 222 cr figure, but via Moneylife's report on SEBI's 23 May 2025 order, not Business Standard (Business Standard returned 403). The order covers Oct 2022 to Jun 2023, three quarters, not nine months. Quarterly fees went from Rs 15 cr (previous year) to Rs 60 cr, then Rs 81 cr, then Rs 125 cr, and MCX had held a 99-year licence. A further six-month extension (Jul-Dec 2023) was priced at Rs 125 cr a quarter, Rs 250 cr in total (multibagg summary). Business Today confirms the planned 3 Oct 2023 TCS CDP go-live. Other reports say SEBI asked MCX on 28 Sep 2023 to hold off, so the actual cutover date should be checked against an MCX exchange circular.

ASX CHESS is the strongest primary-source case for S1, S2 and S4: the RBA assessment, plus ASX's 17 Nov 2022 release on the A$245-255m write-off, which I read as a PDF. Broadridge's FY2026 10-K confirms mainframe dependence through 2031. S3 evidence is industry-wide (Acuiti, via The TRADE), not tied to a specific product.

Gaps:
- No verified buyer counts for UK, EU, SG and MY. FCA and Bursa pages blocked automated access, and the ESMA and MAS pages give no inline count.
- The VN count includes banks.
- First-ship dates for MPC S21 and FSS FLEX were not found.
- FIS, ION/Fidessa, Nasdaq market tech, SS&C and Thai/Malaysian/Philippine broker back-office vendors were not researched.
- No AI-native challenger with India or SEA traction was found. The Asia-relevant replacements found are TCS (large vendor) and FSS's own next-gen core (SHS go-live, June 2026, seen only in search snippets).

The PSE and ASX counts are my own automated parses and should be checked by hand.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
