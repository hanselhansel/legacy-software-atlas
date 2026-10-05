# Valon

## Summary

Valon replaces the mortgage servicing system of record, a market National Mortgage News describes as a duopoly of ICE's MSP and Sagent [1]. It wrote its own cloud core, licensed its own servicer in all 50 states, and ran about 810,000 loans on it before selling that servicer to Carrington, which adopts ValonOS as its core platform [2][3][4][5]. Newrez agreed in January 2026 to move all its servicing, over 4 million homeowners, onto ValonOS from 2027. But Newrez is leaving an in-house system, not MSP, and no MSP shop has publicly confirmed a move [6][7][8][9]. The lesson: in a regulated core market, running the business on your own software can be the sales pitch. Once the proof has done its job, it can be sold to a customer.

## The legacy it attacks

The target is the servicing core: loan setup, escrow, investor reporting and regulatory work [10]. ICE's MSP, inherited from Black Knight, ran about 36 million active loans in FY2022, out of roughly 66 million US first and second liens and credit lines [10]. In 2019 PennyMac said Black Knight "by its own admission" controlled over 62% of the first-lien loan market [11]. ICE paid $11.9 billion for Black Knight in September 2023 [12]. Its servicing software revenue was $871 million in 2025, up 3%, helped by "MSP new client implementations" and "contractual price increases" [13]. Sagent, now selling its newer Dara platform, is the other large vendor [1]. A few large servicers run their own cores, such as PennyMac's SSE and Newrez's ServicingDirector [11][8].

The stack is old. An October 2026 ICE job post for the MSP team asks for 8+ years of z/OS mainframe development, with COBOL, CICS, JCL and VSAM/DB2 [14]. PennyMac, a litigant, called MSP "outdated, mainframe 'green screen' technology designed decades ago" [11].

Why it stuck:

- **Switching cost.** A move "can take 12 to 18 months, or longer," Black Knight told investors [10].
- **Contracts.** Its software and hosting contracts "typically span five to seven years" [10].
- **Litigation.** Black Knight sued PennyMac in November 2019, after PennyMac said it would not renew MSP and would move to its own system. PennyMac filed an antitrust suit the next day [11]. An arbitrator awarded Black Knight $155.2 million for breach of contract in 2023 but rejected its trade-secret claims [15].
- **Regulation.** Sagent counts "some 8,800 different rules" a servicer may face [16].
- **Data.** PennyMac said Black Knight charged clients extra to use its tools to move their own loan data in and out of MSP [11].
- **Skills.** The same job post calls Claude Code knowledge "a strong plus," which suggests ICE wants AI help to maintain COBOL (inferred) [14].

## Origin

TechCrunch named Andrew Wang, Eric Chiang and Jon Hsu as the founders of the company, first called Peach Street, in New York in June 2019 [2]. Valon's About page now lists Wang, Linda Du and Hsu as co-founders [20]. Wang, an engineer, did principal investing at Soros [17] and worked at Goldman Sachs and Google [18]. As a "mortgage trader," he saw noisy data from "archaic and disparate servicing systems" [19]. Chiang and Hsu brought product and engineering experience from Google and Twilio [2]. Du, now President, COO and co-founder, came from Two Sigma and Goldman Sachs [18][20]. Early backer Brian McGrath says neither she nor Wang "had ever serviced a mortgage" [21].

The insight had two parts. Correct data needed "a complete overhaul of the core system and infrastructure" [19]. And nobody would buy a core from outsiders. Within three to six months, Wang says, they saw that servicers' answer would be: "Not only do I have zero trust in you, but we've also spent hundreds of millions of dollars trying to improve these systems and we've fantastically failed" [22]. So they would build a servicer first and sell software later [23].

Why then:

- **Costs had climbed.** a16z cited the cost of a performing loan rising from $59 to $156 between 2008 and 2013 [17]. MBA put 2024 costs at $176 per performing loan and $1,573 per non-performing loan [24]. Personnel make up 75% of total expense "in many shops," Sagent says [16].
- **The incumbent was under fire.** Wang said the leading vendor controlled "more than half of all U.S. residential loans" [25]. PennyMac's 2019 exit showed a big servicer could leave MSP, at a price [11][15].
- **Cloud and COVID.** The platform was built on Google Cloud [2]. Over 5% of mortgages were in forbearance in early 2021 [17]. The podcast host's notes say Valon "only broke through because of a COVID-era expedited approval program for tech companies" [22].
- **LLMs changed the pitch later.** Valon launched as "mobile-first" [2]. After OpenAI's o3 announcement in December 2024, an "AGI is Coming" all-hands cut the servicer-to-software timeline to "one to two years, not five to ten" [22]. By 2026 ValonOS was sold as "an AI-native operating system" [7]. Valon was born cloud-native and became AI-native later (inferred).

## First wedge

The first job was subservicing conventional agency loans, Fannie Mae first, for owners of mortgage servicing rights (MSRs), on Valon's own platform [23][25][3]. The anchor customer was Rithm, then called NRZ. It invested early and "committed to letting us service loans from Newrez" [23]. NRZ also joined the Series A [2].

Why subservicing: Valon's 2020 primer notes that a master servicer can contract the work out and "can have multiple subservicers" to spread risk [26]. So a new subservicer can win a slice of a book without the owner touching its own core (inferred). The pitch was cost. Major players spent about $1 billion a year on servicing fees, and Valon aimed to cut that by at least 10% [27].

Why conventional loans first: they are the most standardized product (inferred). Fannie Mae approved Valon by February 2021, the first new servicer approved on a new proprietary system [17][25]. Freddie Mac and FHA approvals followed in 2021 [28], and Freddie loan support shipped in 2022 [3]. Ginnie Mae issuer approval came in December 2024 [29]. As of June 2026, full Ginnie Mae servicing in ValonOS was still being built [1].

The borrower experience was the visible proof: over 70% of homeowners registered online in 2021, and satisfaction averaged 93.6% in Q4 2022 [28][3].

## First 10 customers

**Found** through investors. McGrath, then at Jefferies, introduced the founders to Rithm CEO Michael Nierenberg [23][21]. NRZ and Jefferies joined the Series A [2], and Starwood Capital and Freedom Mortgage affiliates joined the Series B [30]. No public record shows which of them, beyond Rithm, sent loans.

Concentration was high. At end-2023 Valon subserviced 4.9% of the UPB underlying Rithm's MSRs, or $25.9 billion [31], when Valon's whole platform held over $55 billion [32]. Rithm was close to half of Valon's book (inferred). By end-2025 Valon subserviced 3.6% of Rithm's MSR interests [6].

**Sold** by founders. Wang says he sold "over 100 million dollars of recurring revenue and contracts for the original operating business with basically just me as the key salesperson" [22]. The Mortgage Scoop wrote that Valon had "no branding, sales or marketing" [9]. Du: "The best marketing is our operating business" [9].

**Implemented** by hand at first. For the first loan, Du and Wang "mapped every loan field, every document, in a spreadsheet" [22]. Valon went from 75 homeowners ($14.5 million) at end-2020 to 24,000 ($5.62 billion) at end-2021, including 15,000 mortgages boarded in 31 days [28].

**Sales cycle.** Subservicing commitments reached $10 billion in about a year [2]. Software deals run longer. Carrington's CEO said his team was "in their shop for well over a year" first [1]. Newrez bought the software about six years after Rithm's first bet [23].

**Pricing.** MSR owners pay subservicers a subservicing fee [6]. For ValonOS, Wang says contracts "run five years or longer" and Valon is "paid on the savings the AI generates" [33]. In the podcast, Du puts the software pipeline at "millions in ACV" [22]. The Mortgage Scoop, in its own words, put the largest contracts at "$100M-plus in ACV" [9]. The two figures are hard to reconcile.

## How big it is now

| Date | Round | Amount | Investors | Valuation |
|---|---|---|---|---|
| By Feb 2021 | Seed | $3.2M [2] | AlleyCorp, Soros, Kairos, Zigg Capital [2] | Not disclosed |
| Feb 2, 2021 | Series A | $50M [2] | Led by a16z; Jefferies, NRZ, 166 2nd [2] | Not disclosed |
| Nov 3, 2021 | Series B | $43.9M [30] | Starwood Capital and Freedom Mortgage affiliates, Human Capital, Marcelo Claure; a16z, NRZ, 166 2nd returned [30] | About $590M [30] |
| Oct 2024 | Series C | $100M [19] | Led by WestCap, with a16z [19][34] | $1.1B [34] |
| Feb 2, 2026 | Strategic | Undisclosed [35] | Rithm Capital, "significant long-term minority equity ownership" [7] | Not disclosed |

Total raised was $230 million in October 2024 [34], $277 million in December 2025 [9] and over $290 million in August 2026 [5]. The listed rounds sum to $197.1 million, so about $33 million by 2024 is not itemized (inferred). Du mentions a raise "around mid-2022" [22]. Forbes lists a valuation of $1.75 billion dated July 2024 [18]. HousingWire reported $1.1 billion for the Series C announced that October [34]. The two figures may describe the same round.

Scale, as reported:

- **2023:** over 350,000 homeowners, over $55 billion serviced, 274 staff [32].
- **2024:** 371,000 loans, $41 million revenue [18].
- **2025:** 593,000 loans, $86 million revenue, 469 employees [18].
- **Feb 2026:** a "top 10 mortgage servicer" with "over $110B of mortgages serviced" on its platform, and "3 of the 10 biggest servicers signed up to deploy ValonOS" [36].
- **May 2026:** about 800,000 loans and $197 billion UPB, mostly subserviced [37].
- **Aug 2026:** about 810,000 loans, with the servicing staff moving to Carrington [4]. A secondary report in late August, citing Business Insider, puts Valon at about 320 employees [38].

Efficiency claims, unaudited: operating margins above 60% [39] and "70% plus" [22]; over 3,000 loans per employee against an industry average of 750 [23]; servicing cost "3x" below industry [40]. The host's notes for the October 2025 podcast claimed "over $100 million in revenue and more than one million loans under management" [22]. Forbes' 2025 figures do not match [18].

Named customers, dated: Rithm and Newrez, subservicing since about 2020 (inferred), and a ValonOS deal in January 2026 [23][6]. Figure, live by February 2026, reports 40% better delinquency outcomes in its own A/B test [41]. Bayview Asset Management, listed in 2026 [18]. Carrington, May and August 2026 [37][4]. ServiceMac, reported by The Mortgage Scoop in December 2025 to be leaving MSP for Valon. Neither company commented [9].

## What made it hard

**Licensing catch-22s.** Credit bureaus wanted 50 to 100 loans before Valon could report, and "nobody will give you 100 loans to service if you can't report to the credit agencies," Du says [22]. So Valon "gave loans to a bunch of friends" in states with small-loan exemptions [22]. Fannie Mae and Freddie Mac usually want "24 months of profitable operating history," the host notes [22]. New York licensed Valon only in 2022 [3]. Three compliance staff ran 13 state exams in 2021 [28].

**Data migration.** Every client needs "their entire world, data, documents, and logic, translated into our unified schema" [42]. Valon's largest 2023 month boarded over 80,000 mortgages, 19.5 million data values and 7.6 million document images [32]. Decagon says peak call volume ran 2 to 3 times higher than ever before [43].

**Cash.** "We raised around mid-2022, and then by end of 2022 it was basically VC winter," Du says. She says the founders concluded "We will die as a business if we keep going down this path" [22]. Valon "figured out how to monetize float" [22] and cross-sold loans and insurance, plus a tax-dispute pilot [3][32].

**Incumbent response.** ICE shipped a new MSP interface in February 2026 and says escrow automation cuts manual touchpoints by up to 87% [44]. It put AI voice and chat agents into beta in March 2026 [45]. In September 2026 Wells Fargo renewed MSP and agreed to bring its full home loan servicing portfolio onto it [46].

**Product scope.** In June 2026 ValonOS was not yet "fully built out to handle the Ginnie Mae servicing product," so Carrington's own loans stay on Sagent for about 12 months [1].

**Borrowers.** The BBB shows 139 complaints closed in three years against Valon Mortgage [47]. This study found no public regulatory enforcement action.

**Talent.** Valon prefers early-career hires, and 70% of its leaders were homegrown [48]. AI then broke the apprenticeship: new hires leaned on it "before they've learned enough to know when it is wrong" [48]. In August 2026 Valon turned off AI for new non-engineering hires until a manager attests they can spot its errors [48].

**Channel conflict.** As a servicer, Valon competed with the servicers it wanted as software buyers (inferred). Wang now says "we want neutrality," and that the only holders above 10% are himself and venture investors [1].

## Strategy

Valon ran a regulated service on its own greenfield core, added AI agents to that service, then turned into a migration-led core replacement. It is not an overlay [19][23][49]. Four steps:

1. **Operate.** Run the servicer and feed every ops failure back into the product: "ops would hit a wall," then "engineering would build and ops would run the process again" [23].
2. **Productize.** ValonOS packages a system of record, workflows and task management [40]. LLM agents propose actions that deterministic code and validators must accept, and an operator reviews the payment agent's moves [49]. Decagon agents deflect over 50% of inbound voice calls [43]. Token spend rose from $300K to $3M, period unstated [50].
3. **Sell the core.** Figure went live [41]. Rithm agreed in January 2026 to migrate "all of Newrez's mortgage servicing operations" over about two years [6].
4. **Divest the proof.** Carrington bought Valon Mortgage with a private equity partner it declined to name, and adopts ValonOS as its core [37][4]. Du: "go all-in as a technology company" [37].

How far it has got:

- **Live:** the roughly 810,000 former Valon loans, now serviced by Carrington on ValonOS [4][1], plus Figure's loans [41].
- **Contracted, not migrated:** Carrington's legacy book of about 998,000 loans and $211 billion UPB, due to move after about 12 months on Sagent, so around 2027 (inferred) [37][1]. Newrez's 4 million-plus homeowners, starting in 2027, in a process Rithm expects to take about two years [7][6].
- **MSP displaced:** none confirmed. Newrez is not an MSP defection. It is "the largest servicer not on MSP or Sagent" [8]. Carrington runs Sagent [1]. Only ServiceMac, a subservicer with over 1 million loans [51], is reported to be leaving MSP, and neither company has confirmed it [9].
- **Scale if it lands:** about 6 million loans on ValonOS, against 36 million on MSP in 2022 (inferred) [5][7][10].

## What others can copy

1. **Run the operation before you sell the core.** Valon's own P&L became the demo: 3,000-plus loans per employee against 750 [23], watched by a buyer from inside for over a year [1]. Test: can you show your unit cost against an outside benchmark, such as MBA's $176 per performing loan [24]?
2. **Enter through a slice, not a switch.** Subservicing let an MSR owner send part of a book without changing its core (inferred) [26]. Rithm sent about 4.9% [31]. Test: can a buyer give you a bounded share of volume under processes it already runs?
3. **Raise from the people who own the volume.** NRZ, Jefferies, Starwood and Freedom Mortgage affiliates invested early [2][30]. Rithm became the anchor client, then the first whole-shop buyer [23][6]. Test: what share of early volume comes from investors, and how fast does it fall?
4. **Remove channel conflict before you go horizontal.** Valon sold its servicer to a buyer that adopts the core [4] and now pitches neutrality [1]. Test: does pipeline grow after the divestiture?
5. **Price on measured savings, over long terms.** Contracts of five years or more, paid on savings [33]. Test: can savings be measured per loan each month, and do they rise as models improve?
6. **Hit the weak flank first.** The first whole-shop conversions came off an in-house core and off Sagent, not MSP [8][1]. Test: segment the market by core system and win in-house and end-of-life cores first (inferred).

## Open questions

- Will a confirmed MSP shop finish a move? ServiceMac is unconfirmed [9], and Wells Fargo just consolidated onto MSP [46].
- Can ValonOS run Ginnie Mae servicing at Carrington's scale by 2027 [1]?
- Can Newrez move 4 million-plus homeowners in about two years without borrower harm? Rithm flags data conversion and running "multiple servicing systems concurrently" as risks [6].
- How much of the 60% to 70% margin came from software, and how much from float and cross-sell [22][39]? (inferred question)
- What does Valon earn as software only? Forbes' $86 million for 2025 predates the sale [18].
- Is neutrality real when Rithm is both an investor and the largest announced software customer (inferred) [7][6]?
- Will lock-in now protect Valon? Rithm says leaving ValonOS later "may be limited by contractual restrictions, switching costs" [6].

## Sources

1. National Mortgage News (Spencer Lee), "How Valon and Carrington plan to crack a servicing tech duopoly," June 3, 2026. https://www.nationalmortgagenews.com/news/how-valon-and-carrington-plan-to-crack-a-servicing-tech-duopoly
2. TechCrunch (Mary Ann Azevedo), "Valon closes on $50M a16z-led Series A to grow mobile-first mortgage servicing platform," Feb 2, 2021. https://techcrunch.com/2021/02/02/valon-closes-on-50m-a16z-led-series-a-to-grow-mobile-first-mortgage-servicing-platform/
3. Valon blog, "Valon's 2022 in Review," Jan 26, 2023. https://www.valon.ai/blog/valons-2022-in-review
4. HousingWire (Sarah Wolak), "Carrington completes acquisition of Valon Mortgage," Aug 4, 2026. https://www.housingwire.com/articles/carrington-acquires-valon-mortgage/
5. Carrington and Valon press release (Business Wire, via Yahoo Finance), "Carrington Completes Acquisition of Valon Mortgage and Will Adopt ValonOS as Its Core Servicing Platform," Aug 4, 2026. https://finance.yahoo.com/real-estate/articles/carrington-completes-acquisition-valon-mortgage-100000792.html
6. Rithm Capital, Form 10-K for FY2025, SEC EDGAR, filed Feb 2026. https://www.sec.gov/Archives/edgar/data/1556593/000155659326000012/nrz-20251231.htm
7. Newrez press release, "AI-Native Platform to Advance Newrez Servicing Capabilities," Feb 2, 2026. https://www.newrez.com/press-news/ai-native-platform-to-advance-newrez-servicing-capabilities/
8. The Mortgage Scoop (James Kleimann), "NewRez Ditches Its Legacy Servicing System for Valon," Feb 2, 2026. https://www.themortgagescoop.com/p/valon-lands-a-whale
9. The Mortgage Scoop (James Kleimann), newsletter item on ServiceMac and Valon, Dec 19, 2025. https://www.themortgagescoop.com/p/hard-times-for-easy-money-dscrs-a-stealthy-mortgage-tech-unicorn-lands-a-new-client
10. Black Knight, Inc., Form 10-K for FY2022, SEC EDGAR, filed Feb 2023. https://www.sec.gov/Archives/edgar/data/1627014/000155837023002252/bki-20221231x10k.htm
11. PennyMac, "Servicing Systems Environment: Frequently Asked Questions," Nov 14, 2019. https://s201.q4cdn.com/340896660/files/doc_presentations/2019/11/2019-Servicing-Systems-Environment-FAQ.pdf
12. HousingWire (Connie Kim), "ICE completes $11.9B acquisition of Black Knight," Sept 5, 2023. https://www.housingwire.com/articles/ice-completes-11-7b-acquisition-of-black-knight/
13. Intercontinental Exchange, Form 10-K for FY2025, SEC EDGAR, filed Feb 5, 2026. https://www.sec.gov/Archives/edgar/data/1571949/000157194926000004/ice-20251231.htm
14. ICE job post, "Senior Mainframe Developer" (MSP Mortgage Technology team), via freehire.me, Oct 2, 2026. https://freehire.me/jobs/senior-mainframe-developer-intercontinental-exchange-holdings-inc-mbjskvl3
15. HousingWire (Flavia Furlan Nunes), "Black Knight awarded $155M in trade secrets theft lawsuit against Pennymac," Nov 28, 2023. https://www.housingwire.com/articles/black-knight-awarded-155m-in-trade-secrets-theft-lawsuit-against-pennymac/
16. Sagent blog (Ken Posner), "If Servicing Is The Strategic High Ground, Then Why Is Servicing Technology Still Broken?," Oct 1, 2026. https://sagent.com/2026/10/01/if-servicing-is-the-strategic-high-ground-then-why-is-servicing-technology-still-broken/
17. Andreessen Horowitz (Angela Strange), "Investing in Valon: Mortgage servicing that actually offers good service," Feb 2, 2021. https://a16z.com/announcement/investing-in-valon-mortgage-servicing-that-actually-offers-good-service/
18. Forbes, Valon company profile (Fintech 50, 2026 listing), read Oct 2026. https://www.forbes.com/companies/valon/
19. Valon blog (Andrew Wang), "Valon Announces Series C Capital Raise," Oct 22, 2024. https://www.valon.ai/blog/valon-announces-series-c
20. Valon, About page, read Oct 2026. https://www.valon.ai/about
21. Valon blog (Brian McGrath), "Why I joined Valon," Apr 9, 2026. https://www.valon.ai/blog/Brian-McGrath-joins-valon
22. Fintech Leaders podcast (Substack), episode with Andrew Wang and Linda Du, Oct 28, 2025. https://fintechleaders.substack.com/p/valons-ceo-sold-100m-without-a-sales
23. Valon blog (Andrew Wang and Linda Du), "Six Years in the Making," Feb 2, 2026. https://www.valon.ai/blog/six-years-in-the-making
24. Mortgage Bankers Association, MBA Newslink, "Chart of the Week: Cost of Servicing Performing and Non-Performing Loans," July 28, 2025. https://newslink.mba.org/mba-newslinks/2025/july/mba-newslink-friday-oct-20-2022/chart-of-the-week-cost-of-servicing-performing-and-non-performing-loans/
25. HousingWire (Alex Roha), "Digital servicer Valon snaps up $50M in Series A round," Feb 2, 2021. https://www.housingwire.com/articles/digital-servicer-valon-snaps-up-50m-in-series-a-round/
26. Valon blog, "Guide to the Mortgage Galaxy," Feb 1, 2020. https://www.valon.ai/blog/guide-to-the-mortgage-galaxy
27. Valon blog, "A Perfectly Boring Podcast with Valon Co-Founder and CEO, Andrew Wang," Oct 26, 2021. https://www.valon.ai/blog/a-perfectly-boring-podcast
28. Valon blog, "Valon's 2021 in Review," Jan 10, 2022. https://www.valon.ai/blog/valons-2021-in-review
29. National Mortgage News (Spencer Lee), "Ginnie Mae issuer approval granted to subservicer Valon," Dec 3, 2024. https://www.nationalmortgagenews.com/news/ginnie-mae-issuer-approval-granted-to-subservicer-valon
30. Bloomberg, via WealthManagement.com, "Starwood Backs Mortgage Startup Valon at $590 Million Valuation," Nov 3, 2021. https://www.wealthmanagement.com/investing-strategies/starwood-backs-mortgage-startup-valon-at-590-million-valuation
31. Rithm Capital, Form 10-K for FY2023, SEC EDGAR, filed Feb 2024. https://www.sec.gov/Archives/edgar/data/1556593/000155659324000007/nrz-20231231.htm
32. Valon blog, "Valon's 2023 in Review," Dec 5, 2023. https://www.valon.ai/blog/valons-2023-in-review
33. Valon blog (Andrew Wang), "Long AI, Short the Model," May 6, 2026. https://www.valon.ai/blog/long-ai-short-the-model
34. HousingWire (Kennedy Edgerton), "Mortgage servicing startup Valon raises $100M in Series C funding round," Oct 24, 2024. https://www.housingwire.com/articles/mortgage-servicing-startup-valon-100m-series-c-funding/
35. National Mortgage News (Spencer Lee), "Rithm takes minority stake in servicing platform Valon," Feb 2, 2026. https://www.nationalmortgagenews.com/news/rithm-takes-minority-stake-in-servicing-platform-valon
36. Next Play newsletter (Ben Lang), "Meet the startup transforming the mortgage industry," Feb 27, 2026. https://nextplayso.substack.com/p/meet-the-startup-transforming-the
37. HousingWire (Sarah Wolak), "Carrington to acquire Valon Mortgage, add 800K loans to servicing," May 7, 2026. https://www.housingwire.com/articles/carrington-buys-valon-mortgage/
38. Hoodline (Juliana Vance), "New York Fintech Valon Bars New Hires From Using AI Until They Prove Themselves," Aug 29, 2026. https://hoodline.com/2026/08/new-york-fintech-valon-bars-new-hires-from-using-ai-until-they-prove-themselves/
39. HousingWire, "2025 Vanguard: Andrew Wang" award profile, 2025 (no day shown). https://www.housingwire.com/winner-profile/2025-vanguard-andrew-wang/
40. Valon, homepage, read Oct 2026. https://www.valon.ai
41. Valon blog (Michael Tannenbaum of Figure and Andrew Wang), "AI x Blockchain in Mortgage Fuels Outcomes, not Buzzwords," Feb 4, 2026. https://www.valon.ai/blog/ai-blockchain-mortgage-partnership
42. Valon job post, "System Conversion Project Manager," via Built In Seattle, listing removed Jan 13, 2026. https://www.builtinseattle.com/job/system-conversion-project-manager/8053473
43. Decagon, "Valon Customer Success Story," undated, read Oct 2026. https://decagon.ai/case-studies/valon
44. ICE press release, "ICE Introduces New MSP User Experience, Launches Next Phase of Enhanced Servicing Automation," Feb 10, 2026. https://ir.theice.com/press/news-details/2026/ICE-Introduces-New-MSP-User-Experience-Launches-Next-Phase-of-Enhanced-Servicing-Automation/default.aspx
45. HousingWire (Sarah Wolak), "ICE launches AI voice and chat agents for mortgage servicing," Mar 17, 2026. https://www.housingwire.com/articles/ice-ai-mortgage-servicing-agents/
46. ICE press release (via Yahoo Finance), "Intercontinental Exchange Expands Agreement with Wells Fargo to Support Full Home Loan Servicing Portfolio on MSP," Sept 29, 2026. https://finance.yahoo.com/real-estate/articles/intercontinental-exchange-expands-agreement-wells-130000383.html
47. Better Business Bureau, Valon Mortgage Inc complaints page, read Oct 2026. https://www.bbb.org/us/az/phoenix/profile/mortgage-lenders/valon-mortgage-inc-1126-1000089348/complaints
48. Valon blog (Andrew Wang and Jake Mintz), "We turned off AI access for new hires," Aug 18, 2026. https://www.valon.ai/blog/we-turned-off-ai-access-for-new-hires
49. Valon blog (Maxim Gurevich), "Your LLM Isn't the Agent," June 26, 2026. https://www.valon.ai/blog/your-llm-isnt-the-agent
50. Valon blog (Andrew Wang and Hugh Han), "The Substrate Underneath the Harness," May 14, 2026. https://www.valon.ai/blog/the-substrate-underneath-the-harness
51. The MortgagePoint, "ServiceMac Exceeds One Million Loans & Over $300B in Subservicing Portfolio," Feb 6, 2026. https://themortgagepoint.com/2026/02/06/servicemac-exceeds-one-million-loans-over-300b-in-subservicing-portfolio/

Valon blog posts were read through the public content feed behind valon.ai/blog. Each URL above resolves to the same post.

## Fact-check notes

- Litigation: Black Knight sued on Nov 5, 2019, while PennyMac was still on MSP but had said it would not renew. Changed "after PennyMac left MSP" and added PennyMac's antitrust suit the next day [11].
- PennyMac data claim: reworded. Black Knight charged clients to use its products to exchange loan data with MSP. It did not charge for "moving data in and out" in general [11].
- 62% claim: [11] says "first lien loan market", not "first-lien loans".
- Job post [14]: the stack is "8+ years z/OS mainframe" development with COBOL, CICS, JCL and VSAM/DB2 listed separately. Claude Code is called "a strong plus".
- Sagent 75% [16]: added the source's qualifier "in many shops". The draft stated it as an industry-wide figure.
- Founders: Valon's About page [20] lists Wang, Du and Hsu as co-founders, not Chiang. The draft's founder line is now attributed to TechCrunch [2].
- Zero-trust quote: Wang is describing how servicers would react. Servicers did not literally say it to the founders [22].
- Forbearance: [17] gives the over-5% figure as of Feb 2021. Changed "late 2020" to "early 2021".
- "Only broke through" quote: it comes from the podcast host's narrative, not Du. Reattributed [22].
- Subservicing primer [26]: it refers to a master servicer, not an MSR owner. Fixed the wording.
- $1 billion figure [27]: the source says "major players", not "large owners". Fixed.
- Ginnie Mae build-out: dated to June 2026, per [1].
- Rithm share [31][6]: 4.9% is of the UPB underlying Rithm's MSRs, and 3.6% is of its MSR interests. Fixed the wording.
- "No branding, sales or marketing": that is The Mortgage Scoop's own wording [9], not a direct claim by Valon. Attributed accordingly.
- "$100M-plus in ACV": this is the Mortgage Scoop writer's commentary, not a Du quote [9]. Reattributed. "Conflict" softened to "hard to reconcile".
- Valuation: Forbes dates its $1.75 billion valuation to July 2024 [18], before the October 2024 Series C announcement. The draft implied it came later.
- Next Play quote [36]: corrected to "top 10 mortgage servicer" and "over $110B of mortgages serviced".
- Hoodline headcount: noted that it cites Business Insider [38].
- Podcast revenue and loan claim: attributed to the host's notes, not to the company [22].
- "24 months" line: attributed to the host's notes, not Du [22]. Du's credit-bureau quote now reads in full, "...report to the credit agencies".
- Cash section: no source says Valon "cut to profitability". Replaced with Du's actual quote [22]. Cross-sell is no longer cited to [22], which does not mention it. "Tax appeals" became "a tax-dispute pilot" [32].
- Decagon [43]: says call volume was "2–3x higher than ever before" at peak, not "2 to 3 times normal peaks" in an 80,000-loan month. Fixed. Deflection is for inbound voice calls.
- Neutrality [1]: Wang said the only holders above 10% are himself and venture investors. Paraphrase tightened.
- Carrington book [37]: "998,000 loans", not "over 998,000". The 2027 move date is not in [37]. It is inferred from Taffet's "next 12 months" on Sagent [1], so it is now marked inferred.
- Newrez timeline: the 2029 end date was not supported. Replaced with Rithm's "approximately two-year" process starting 2027 [7][6].
- ServiceMac [9]: the report was a Scoop exclusive and neither company commented. "Unconfirmed" now says this outright.
- Scale estimate: added [5] and [7] as the basis for about 6 million loans (Carrington's combined roughly 2 million plus Newrez's 4 million).
- Enforcement: narrowed to "no public regulatory enforcement action". A web search found borrower lawsuits but no regulator orders.
- Style: no em dashes or hype words found in the draft. Long sentences were split for clarity.