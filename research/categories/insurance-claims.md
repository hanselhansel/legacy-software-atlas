# Insurance claims management

Slug: `insurance-claims`

## Systems

- In-house mainframe / midrange claims systems (COBOL, IBM z/OS, IBM i / AS400 RPG) at carriers, many 20+ years old
- Guidewire ClaimCenter (on-prem Java versions, first sold 2003; now moving to Guidewire Cloud)
- DXC Assure Claims, formerly CSC / DXC RISKMASTER (corporate risk, self-insured, TPA claims)
- FINEOS Claims / AdminSuite (life, accident, health, group and absence claims; company founded 1993)
- Duck Creek Claims
- Sapiens claims products (IDIT, ClaimsPro / ClaimsMaster)
- Majesco P&C Core Suite Claims
- Insurity claims (Sure Suite)
- Fadata INSIS (EMEA composite core incl. claims)
- Lloyd's / London market bureau claims infrastructure (ECF, with re-keying into managing-agent systems)

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. Guidewire's 2011 S-1 says P&C carriers typically rely on legacy core systems that have run for 20 years or more and use outdated programming languages. That dates them to before about 1991. Guidewire's own replacement product, ClaimCenter, was first sold in 2003 as on-prem Java software. The vendors in this field also predate cloud: DXC RISKMASTER dates from the early 1980s and FINEOS was founded in 1993. ([source](https://www.sec.gov/Archives/edgar/data/1528396/000119312511240194/ds1.htm))
- **S2 slow to replace**: met. Guidewire's FY2025 10-K says initial subscription agreements usually run five years with annual renewals after that, and some customers sign terms of seven years or longer. It also calls sales cycles lengthy and unpredictable. The 2011 S-1 says implementation and testing take 6 to 24 months or longer. Sapiens' FY2024 20-F says delivery runs from several months to a few years, and sales cycles typically take one to two years. ([source](https://www.sec.gov/Archives/edgar/data/1528396/000152839625000221/gwre-20250731.htm))
- **S3 workarounds**: met. Lloyd's Blueprint Two describes the London market's data handling. Missing direct data provision forces 'laborious data extraction, validation and manual processing', which leads to rework, errors and re-keying. On delegated-authority claims and premium data, a single data capture platform 'will remove significant manual processing currently required'. Separately, an April 2026 industry report summarised by ClaimsPages found that 72% of organisations rely on Excel or homegrown tools for critical workflows, and that more than 50% of policy and claims processes still need human intervention. That report's author is not named, so it is weaker evidence. ([source](https://assets.lloyds.com/media/472b74ba-fe3b-47d6-aa7b-d37c2ba2e179/lloyds-blueprint-two.pdf))
- **S4 shrinking skills**: met. Guidewire's S-1 says the specialised IT staff qualified to maintain legacy core systems are retiring and hard to replace, which leaves aging systems poorly supported. A Rocket Software survey of 276 IT directors and VPs, reported by Digital Insurance in March 2026, found that 52% struggle to find staff who know legacy systems development. Only 35% said their IT workforce has the skills to support those systems. The survey is cross-industry, and the article frames the COBOL and mainframe retirement risk around insurers' policy and claims cores. ([source](https://www.dig-in.com/opinion/insurance-it-leaders-have-an-ai-infrastructure-problem))

## Segments

Mainly enterprise and mid-market insurers, with government buyers and self-insured corporates as well. Guidewire (about 500 customers, 270+ on ClaimCenter), Duck Creek (150+, including four of the top five North American carriers) and Insurity (22 of the top 25 P&C carriers) sell mostly to large and mid-size P&C carriers. FINEOS sells to large group life, accident and health carriers. DXC Assure Claims / RISKMASTER covers corporate risk managers, self-insured organisations, TPAs and risk pools. Government also buys. For example, Tasmania's Motor Accidents Insurance Board is replacing its legacy Motor Accidents Claims System (MACS) with FINEOS (https://www.lifeinsuranceinternational.com/news/maib-fineos-replace-legacy-claims-system/). SMB insurers and MGAs tend to run vendor-hosted packages or homegrown and spreadsheet processes rather than mainframes. Lloyd's Blueprint Two documents manual and spreadsheet-heavy delegated-authority claims handling among coverholders and managing agents.

## Reasons buyers stay

- Long contracts: Guidewire initial terms run five years with annual renewals, and some run seven years or longer, which locks in the incumbent.
- Implementation risk and time: 6 to 24+ months per Guidewire's S-1 and 'several months to a few years' per Sapiens. Claims history must be migrated (for example, Heritage converted about 240k claims).
- Claims systems link to policy admin, payments, reserving, reinsurance, fraud tools and regulator reporting, so a swap touches many integrations.
- Regulatory and audit continuity: claims reserves, litigation files and regulator-mandated data (for example, Lloyd's ECF and bureau messaging) must stay intact.
- Sunk configuration: decades of customer-specific business rules live in the incumbent system.
- Vendors offer an upgrade path instead of replacement (Guidewire Cloud, DXC AWS hosting), so carriers modernise in place.
- High retention signals inertia (DXC cites 98.5%+ customer retention).

## Notes

The legacy layer in claims has two tiers. (1) In-house mainframe and AS400 cores, which Guidewire's S-1 described as 20+ years old. (2) First-generation packaged on-prem systems: RISKMASTER (early 1980s), FINEOS (1993), ClaimCenter (2003). These are now being pushed to vendor cloud. ClaimCenter does not itself meet S1 because it shipped in 2003; it is listed as the dominant installed base and the main modernisation target.

Gaps and caveats:
- The NAIC US count (6,228 domestic insurers, 2024) comes from the national overview pages inside the NAIC New York Key Facts PDF. The standalone national PDF returned 404.
- Thailand's count is secondary (citing OIC). The OIC primary register was not retrievable.
- India's life insurer list page returned 404. Only the general (28) and health (8) IRDAI lists were opened.
- Malaysia counts come from a WebFetch summary of the BNM directory page.
- The UK count of about 408 is unique FRNs I counted myself in the PRA CSV.
- The S3 spreadsheet statistic (72%) comes from an unnamed industry report via ClaimsPages. The Lloyd's Blueprint Two re-keying and manual-processing statements are primary but cover London market placement and delegated-authority claims data, not carrier claims systems generally.
- No primary source found for COBOL skill scarcity specific to claims. The S4 evidence is Guidewire's S-1 (insurer legacy core staff retiring) plus a cross-industry Rocket Software survey.
- Sapiens and FINEOS did not disclose total customer counts in the filings read. Search snippets claiming Sapiens 600+ customers and FINEOS 50 to 60+ customers were not verified, so they were left out.
- Five Sigma revenue is a third-party (Latka) estimate.
- Challengers in SEA are mostly full-stack or embedded insurtechs (Igloo, Roojai, Sunday) rather than claims-system vendors. No AI-native claims-core vendor headquartered in ID, VN, MY, TH or PH was found.

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
