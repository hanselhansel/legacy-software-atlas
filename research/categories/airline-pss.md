# Airline reservations and passenger service

Slug: `airline-pss`

## Systems

- IBM ACP / TPF / z/TPF mainframe transaction platform (origin of PARS/IPARS reservation applications)
- Sabre host reservation system (American Airlines/IBM, built 1960, live 1964) and its airline-hosted successor SabreSonic Customer Sales & Service
- Amadeus Altéa Suite (Reservation, Inventory, Departure Control), hosted PSS for full-service carriers
- Navitaire Open Skies (1994, HP3000) and New Skies (conversions from 2005), LCC PSS now owned by Amadeus
- Travelport (Worldspan/Galileo/Apollo) z/TPF hosting of airline internal reservation systems (Delta, United, Northwest historically)
- SITA Gabriel (Unisys-based) and SITA Horizon PSS
- Videcom VRS (UK, regional/small carriers)
- Radixx (LCC PSS, Sabre-owned since 2019)
- Airline in-house legacy PSS (e.g. ANA domestic system operating since 1988)
- Cryptic / green-screen agent terminals and Sabre Scribe scripts layered on the host

## Legacy signs (first pass)

- **S1 pre-cloud core**: met. The category's core runs on IBM ACP/TPF, built in the mid-1960s by IBM with North American and European airlines and renamed TPF in 1979. Sabre built its system on IBM mainframes in 1960 and launched it in 1964. Travelport ran Delta, United and Northwest reservation systems on mainframes in Atlanta (FY2008 10-K). ANA's in-house domestic PSS has been running since 1988. Navitaire Open Skies (1994) ran on HP3000. Sabre's FY2025 10-K says its architecture 'evolved from mainframe-based transaction processing', which confirms the mainframe origin. ([source](https://en.wikipedia.org/wiki/Transaction_Processing_Facility))
- **S2 slow to replace**: met. Southwest took three years (July 2014 to May 2017) and more than 1,500 people to move to Amadeus Altéa. Qantas moved to Altéa one module at a time from 2002 to 2008 and signed a 10-year agreement in 2007. ANA announced in Feb 2023 that it would replace a domestic PSS running since 1988, with migration over FY2025-26. LATAM signed a 10-year Sabre PSS contract in 2015, and implementation ran to 2018. Sabre's 10-K says SaaS/hosted contracts typically run 3 to 10 years with minimum volume requirements. ([source](https://investors.southwest.com/news-events/press-releases/detail/604/southwest-airlines-completes-transition-to-amadeus-alta))
- **S3 workarounds**: met. Automation Anywhere (April 2020) built an 'Airline Call Center Bot' for major airlines. It reads ticket data from emails, opens the booking and refund applications, validates the PNR and issues e-vouchers. It cut cancellation handling from 20 minutes manual to under 3 minutes, a UI-level re-keying workaround. Agents and airlines still use cryptic host commands, and Sabre Scribe scripts automate them by reading the host screen. The scripting evidence comes from search snippets and Sabre training material; the DataArt article that explicitly says these scripts 'rely on screen scraping' returned 403 and could not be read. Evidence of spreadsheet use inside airlines was not found. ([source](https://www.automationanywhere.com/company/press-room/automation-anywhere-bot-slashes-flight-cancellation-processing-times-from-20-minutes-to-3-minutes))
- **S4 shrinking skills**: met. IBM's own z/TPF Redpaper (REDP-4611) says 'specialized TPF skills can be scarce'. It also says IBM moved z/TPF development from Assembler to C/C++ and Eclipse tooling to widen the skills pool. Other workloads still need special skills. CIO Dive (2024) reports mainframe skill gaps persisting for two decades as experienced staff retire, and cites plane booking as a mainframe workload. ([source](https://www.redbooks.ibm.com/redpapers/pdfs/redp4611.pdf))

## Segments

Legacy PSS cuts across every airline size, but the buyer is always an air carrier, and buyer counts are small (tens per country, about 350 Category A licences in the EU). Enterprise: network and flag carriers run TPF-descended hosts or Altéa. Examples: Delta and United were historically hosted by Travelport on z/TPF; Sabre's own host; ANA's in-house domestic PSS since 1988. Mid-market: LCCs and hybrids run Navitaire New Skies (70+ airlines), Radixx, Hitit Crane (73 customers) or Videcom. Government: many Asian buyers are state-owned flag carriers (Garuda Indonesia, Vietnam Airlines, Air India until 2022, Malaysia Airlines via Khazanah), so tenders may run through public procurement. SMB: small regionals and charters (EU Category B, Part 135) mostly use light hosted systems such as Videcom.

## Reasons buyers stay

- Cutover risk is existential. A PSS swap touches every booking, ticket and check-in. Southwest needed 3 years and 1,500+ people, and Qantas phased modules over 2002-2008.
- Long hosted contracts with minimum annual volume commitments (Sabre: 3-10 years) and exit costs.
- Interline, codeshare, alliance and GDS connectivity, and IATA EDIFACT/ticketing/BSP integrations, are built around the incumbent host.
- Performance: z/TPF is purpose-built for high-volume seat-inventory transactions, and IBM positions it as unique for airline workloads.
- Incumbents are modernizing in place (Sabre moving off mainframe to cloud; Amadeus Nevio offer/order with Finnair, Lufthansa Group, AF-KLM, BA, Saudia). That lowers the urgency to switch vendor.
- Agents and airport staff are trained on cryptic commands and scripts, so retraining costs are high.
- Revenue management, loyalty, DCS and accounting systems are tightly coupled to PSS data feeds.

## Notes

The legacy core here is the IBM ACP/TPF lineage (1960s), plus 1990s-2000s hosted PSS (Navitaire Open Skies 1994, Altéa 2000-2008). Many large carriers have already moved to hosted Altéa, Navitaire or SabreSonic. So the remaining true legacy buyers are in-house systems (ANA domestic since 1988), TPF-hosted US network carriers, and small carriers on Gabriel- or Videcom-era systems. The vendor market is very concentrated (Amadeus, Sabre, Navitaire, Hitit, IBS, Videcom), and switching is rare and slow. Source gaps: several register pages returned 403 or timed out (FAA operators page, CAAT, BITRE, CASA, MAVCOM, DGCA India list, Travel Weekly, DataArt). Counts for SG, TH, MY and AU come partly from search snippets of official sites, as marked in each field. The '225 airlines' Sabre figure was not confirmed in a filing opened. The Sabre FY2025 10-K gives no PSS customer count, and the FY2018 10-K gives airline contract terms of 3-7 years. The S3 evidence is RPA/UI automation and host scripting, not a documented spreadsheet workaround. The Amadeus Nevio source URL is from search results; the opened Amadeus pages were the Altéa product page, airlines overview and FY2025 results. Some sources are secondary (Wikipedia TPF/Sabre/Navitaire pages, Hospitality Upgrade for the Qantas timeline, Tracxn for FLYR).

Vendors, challengers, buyer universe and fact checks are in the CSV files under `research/`.
