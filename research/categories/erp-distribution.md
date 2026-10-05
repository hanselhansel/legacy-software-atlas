# Wholesale distribution ERP

Slug: `erp-distribution`

## Systems

- Epicor Prophet 21 (P21)
- Epicor Eclipse (Rocket UniVerse multivalue/Pick backend, Eterm character UI)
- Epicor BisTrack (lumber/building materials)
- Infor A+ / Distribution Enterprise i (RPG on IBM i / AS400)
- Infor Distribution SX.e / CloudSuite Distribution (Progress 4GL/OpenEdge)
- Infor Distribution FACTS (no longer sold)
- DDI System Inform (Advantive)
- Microsoft Dynamics GP (Great Plains)
- SAP Business One (ex-TopManage)
- Pronto Xi (Australia, Informix/Unix heritage)
- JD Edwards World (RPG on IBM i)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Eclipse first shipped 1990 on a UniVerse multivalue database with the Eterm terminal UI. Infor A+ is an RPG suite on IBM i (OS/400) from Daly & Wolcott (1988). SX.enterprise was built on Progress database tools. Activant/Triad installed its first system in 1973. All are on-prem, client-server or midrange cores shipped before 2005. ([source](https://en.wikipedia.org/wiki/Eclipse_ERP ; https://www.itjungle.com/2011/05/03/fhs050311-story07/))
- **S2 slow to replace**: met. Wesco, the largest US electrical distributor, is spending $500M on a multi-year transformation to replace a mix of legacy systems. It had invested $270M by Feb 2025 and said it was 'more than halfway' through its build. Epicor's P21 on-prem phase-out spans 2028 to 2029. Advisors say mid-market migrations take 12 to 18 months from decision to go-live, so large programs run for years. No source found for 7+ year contract terms. ([source](https://www.digitalcommerce360.com/2025/02/12/wesco-500-million-digital-transformation-plans/ ; https://www.crestwood.com/blog/prophet-21-phase-out/))
- **S3 workarounds**: met. Conexiom serves 16 of the top 20 industrial distributors. Its business is turning orders that arrive as email, PDF, spreadsheet, image or text into ERP transactions. Across 20M+ orders it analysed, 74% had issues such as wrong part numbers or prices. Distribution Strategy Group (Q1 2026, n=233) found 55% of distributors have ERP, CRM, ecommerce and analytics that are not integrated. Proton.ai says P21 data is spread across records and is not on any single screen, so reps assemble it by hand. ([source](https://www.prnewswire.com/news-releases/conexiom-launches-ai-powered-ideal-order-platform-to-revolutionize-sales-order-automation-302386165.html ; https://distributionstrategy.com/report/state-of-distributor-technology-2026/))
- **S4 shrinking skills**: met. In Fortra's 2026 IBM i Marketplace Survey (315 respondents), 69% named IBM i skills a top concern, up from 60% in 2025 and 45% in 2020. This is the first time in nine years it ranks above cybersecurity. It applies directly to RPG/IBM i distribution ERPs (Infor A+, JD Edwards World). No comparable survey was found for Progress 4GL (SX.e) or UniVerse/Pick (Eclipse) skills. ([source](https://www.itjungle.com/2026/02/02/skills-displaces-cybersecurity-as-top-concern-for-ibm-i-shops/))

## Segments

Mostly mid-market, plus upper SMB. P21, Eclipse, DDI Inform and SX.e target branch-based distributors with roughly $10M to $1B+ revenue. Eclipse users are described as multi-branch firms with hundreds of employees. Enterprise distributors also run legacy stacks: Wesco has 18 ERPs across 30 business units and runs SX.e (per AppsRunTheWorld), and a $500M program is replacing its legacy systems. SMB distributors in SG/MY/PH/AU tend to run Dynamics GP, SAP Business One, Pronto Xi or accounting software. Government is not a meaningful buyer segment. Sources: https://en.wikipedia.org/wiki/Eclipse_ERP ; https://www.digitalcommerce360.com/2025/02/12/wesco-500-million-digital-transformation-plans/

## Reasons buyers stay

- Deep vertical logic: contract and customer-specific pricing, rebates, multi-branch inventory, counter sales and buying-group integrations accumulated over decades (P21, Eclipse built for electrical/HVAC/PVF).
- Heavy customizations and integrations to ecommerce, EDI and WMS make replacement risky. Advisors cite 12 to 18 months for mid-market migrations.
- Vendors keep the old systems running. Epicor says the P21 on-prem phase-out is not end-of-life, and active support runs to June 2029.
- Thin distribution margins and fear of order and fulfilment disruption during cutover.
- Users are productive on character-based and green-screen order entry.
- Vendor-sanctioned cloud paths (Epicor Cloud, Infor CloudSuite, Business Central) let firms re-host without re-platforming.

## Notes

The category is concentrated in Epicor (P21, Eclipse, BisTrack) and Infor (A+, SX.e, FACTS, now CloudSuite Distribution), with long US mid-market tails (DDI, Dynamics GP) and Pronto in AU. Both incumbents are forcing cloud moves. The final on-prem P21 release is 2028.1 (May 2028), active support ends 30 Jun 2029, Dynamics GP support ends 31 Dec 2029, and Infor no longer sells on-prem SX.e/FACTS. This creates a 2026-2029 decision window.

Gaps:
(1) No vendor-disclosed current customer counts for P21 or Eclipse. 5,000+ P21 is a third-party figure.
(2) The P21 first-ship year is not verified in an opened source. Search snippets say Prophet 21 Inc. was founded in 1967.
(3) SEA buyer counts are weak. MY and PH are only wholesale+retail combined. The ID figure is national category G, verified only via a provincial bulletin. The VN figure comes from a press report, and the IN figure is from the 2005 census.
(4) No source for 7+ year contract terms.
(5) Most challengers overlay the legacy ERP (order entry, sales AI) rather than replace it. No funded AI-native distribution ERP replacement focused on SEA was found.

Several sources returned 403 (CIO, Enterprise Times, PSA, BPS publication pages) and were not used as cited sources.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
