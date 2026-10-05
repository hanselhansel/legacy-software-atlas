# Freight forwarding and customs brokerage

Slug: `freight-forwarding-customs`

## Systems

- CargoWise / CargoWise One (WiseTech Global; ediEnterprise heritage, company founded 1994)
- Descartes broker and forwarder enterprise systems and customs filing (Descartes founded 1981)
- Kewill Forward / Kewill customs (founded 1972) -> BluJay Solutions (2016) -> e2open (2021) -> WiseTech Global (Aug 2025)
- Riege Scope (Riege founded 1985; predecessor ProCarS ran on networked PCs then multi-user UNIX servers)
- Magaya Supply Chain / freight management (about 25 years old, started around 2000-2001)
- ECUS5-VNACCS (Thai Son, Vietnam) desktop customs declaration software
- In-house legacy forwarding systems at large forwarders (e.g. DHL Global Forwarding 'Logis', target of the failed NFE replacement)
- Government filing cores that broker software must connect to: US CBP ACS (COBOL mainframe) / ACE, UK CHIEF (1994, retired 2022-2024) -> CDS, SG TradeNet, IN ICEGATE, ID CEISA, VN VNACCS, MY MyCIEDS/uCustoms, TH e-Customs, PH E2M

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The customs filing core in the US is a mainframe. CBP's Automated Commercial System (mid-1980s) runs on 3.9 million lines of COBOL on CBP's last remaining mainframe and cost about $25M a year to maintain. Retirement was targeted for Q1 FY24. On the forwarder side, Kewill dates to 1972 and Riege to 1985 (ProCarS on multi-user UNIX servers). DHL Global Forwarding's legacy 'Logis' system was reported as up to 30 years old. GoFreight's CEO says many forwarders 'still use antiquated ERP systems that were developed over 20 years ago' (https://www.prnewswire.com/news-releases/gofreight-raises-23m-to-automate-freight-forwarding-workflows-and-expand-its-team-301684587.html). ([source](https://tmf.cio.gov/cbp-case-study/))
- **S2 slow to replace**: met. DHL Global Forwarding's New Forwarding Environment was a €750m program to replace its legacy forwarding systems. Pilots began in 2013. It was halted in August 2015 and abandoned in October 2015 with a €345m write-off (€308m of assets plus €37m for rollback). Government cores are just as slow to replace. HMRC began replacing CHIEF (1994) in 2013-14 with an original target of January 2019 (NAO, https://www.nao.org.uk/reports/the-customs-declaration-service/), and CHIEF was finally closed in 2022 for imports and 2024 for exports. CBP started work on ACE in 1994 and was still retiring the ACS mainframe in FY24. ([source](https://theloadstar.com/dp-dhl-finally-abandons-ill-fated-nfe-it-project-and-is-forced-to-write-off-e345m/))
- **S3 workarounds**: met. In HMRC's Ipsos MORI survey of UK customs intermediaries (Feb 2021), only 61% of those completing declarations in-house had automated software to reduce processing time. Of those, 72% used it for all declarations and 9% for less than half. That leaves about 39% keying declarations without automation. BCG (2018) found forwarders 'still rely on email, personal handoffs, and even faxes' for shipping documents, and only 5 of the top 20 forwarders sent automated confirmation emails. Challengers such as Expedock sell AI that turns paper invoices and statements into data for existing forwarding systems, which is a sign that re-keying is common. ([source](https://assets.publishing.service.gov.uk/media/604b5f978fa8f505bdfcfc7c/HMRC_Research_Report_610_Customs_Intermediaries_Wave_2.pdf))
- **S4 shrinking skills**: not met. No sourced evidence ties scarce skills to the forwarder and broker systems themselves. Those cores (CargoWise, Descartes, Riege, Magaya) are proprietary vendor platforms, not COBOL or RPG estates. Where talent is short, it is short in vendor-specific expertise, and only anecdotal sources say so. The only COBOL link is on the government side. CBP's ACS ran 3.9M lines of COBOL (https://tmf.cio.gov/cbp-case-study/), and GAO-19-471 says COBOL has 'a dwindling number of people available with the skills needed to support it', but that statement is generic and not about forwarding software. Not met for this category. ([source](https://www.gao.gov/assets/gao-19-471.pdf))

## Segments

All four segments use these systems, with different products. Enterprise: the largest global forwarders use CargoWise global rollouts (24 of the top 25 are WiseTech customers, and 14 are on CargoWise global rollouts per FY25 results) or in-house systems (e.g. DHL's Logis and the abandoned NFE). Mid-market and SMB: about 16,170 US licensed brokers, about 8,400 UK intermediaries and over 1,000 Vietnamese customs agents run packaged software such as Magaya, Descartes, Riege Scope, ECUS or CargoWise. HMRC research shows many smaller UK intermediaries file without automation. Government: customs administrations run the filing cores (CBP ACS/ACE, HMRC CHIEF/CDS, SG TradeNet, VN VNACCS), and those cores are themselves legacy modernization programs.

## Reasons buyers stay

- Every country's customs filing interface is certified separately (ACE ABI, CDS, TradeNet, VNACCS, ICEGATE). Incumbent vendors maintain these certifications and each regulatory change, which is costly for a newcomer to copy.
- Failed replacements are costly. DHL wrote off €345m after its €750m NFE program to replace legacy forwarding systems collapsed.
- Network effects. CargoWise covers 24 of the top 25 forwarders, and Descartes' GLN connects 26,000+ customers, so partners and agents share the same messaging rails.
- Consolidation spreads incumbents without new contracts. WiseTech says DSV's integration of DB Schenker extends CargoWise use, and WiseTech now owns e2open/BluJay (ex-Kewill).
- The accounting, operations and customs modules are tightly coupled, and migration needs historical shipment data kept for audit. Vendors note read-only access to the old system is often kept for 6-12 months.
- Regulatory liability. Licensed brokers are personally accountable for filings, so they avoid switching unproven filing engines.

## Notes

The vendor field is consolidating. WiseTech (CargoWise) closed its acquisition of e2open, which already owned BluJay and before it Kewill, on 4 Aug 2025. Two of the three largest legacy forwarding and customs lineages now sit in one company, next to Descartes. The strongest primary evidence of legacy status is on the government side: CBP ACS is a COBOL mainframe, and HMRC took 2013-2024 to replace CHIEF. On the forwarder side, the strongest evidence is DHL's €345m NFE write-off. S4 is not met because the forwarder cores are proprietary vendor platforms, not dying-language estates. Buyer counts: official counts were found for the US (CBP 16,170 brokers; FMC 9,600+ OTIs), UK (HMRC research, about 8,400 intermediaries) and VN (1,108 agents). EU, IN and ID rely on association proxies. SG, MY, TH, PH and AU registers exist but no total was found on pages that opened (the ABF page returned 403). Riege's customer count (700+) and Magaya's founding year (2001) came only from search snippets, not opened pages. The DHL 'Logis' age claim (30 years) comes from an Air Cargo News search snippet. The Loadstar page opened confirms the €750m program, the €345m write-off and the 2015 abandonment. Several large forwarders (Expeditors, Kuehne+Nagel) run in-house systems not covered here.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
