# Mechanical Orchard

## Summary

Mechanical Orchard (MO) replaces custom COBOL, JCL, CICS and Db2 workloads on IBM mainframes with modern code that the customer owns and can run on a public cloud [1][2][3]. It does not translate source line by line. It records what the running system takes in and puts out, has AI write replacement code in small slices, and cuts a slice over only when its outputs match the old ones byte for byte [4][5]. MO says it was founded in October 2022. It reported more than $10 million of revenue and a profit for 2023, and has about 100 staff [5][6][3][9]. SEC filings suggest it had raised roughly $95 million to $102 million by January 2026; the range depends on whether the seed is already counted in the Series A filing (inferred) [7][8]. It has publicly retired applications, not whole mainframes [10][11]. The lesson: once AI makes code cheap, the scarce product is proof of equivalence, and the old system's own behaviour is the cheapest specification a challenger can get.

## The legacy it attacks

The target is the custom estate on IBM z/OS: COBOL batch jobs run by JCL, CICS transactions, IMS and Db2 databases, VSAM files, and some PL/I, Assembler, Easytrieve and IDMS [1]. IBM said in 2022 that its Z platform served two thirds of the Fortune 100, 45 of the top 50 banks, 8 of the top 10 insurers, 7 of the top 10 global retailers and 8 of the top 10 telcos [12]. In July 2025 GAO found that the 11 federal legacy systems most in need of modernisation were about 23 to 60 years old. As of February 2025, agencies had finished only 3 of the 10 modernisations GAO flagged in 2019 [13].

Five forces keep them in place.

- **Failed exits.** A Fortune 500 retailer that MO began working with in March 2023 had paid a global integrator for three years and $40 million to transpile COBOL to Java. The result ran at a tenth of mainframe speed and never reached production [10]. ISG estimates that testing takes more than 70% of mainframe-to-cloud migration time [14].
- **Cost, contracts and skills.** That retailer's nearly 7 million lines ran on about 6,000 MIPS across five partitions. Infrastructure cost tens of millions of dollars a year, and the system depended on nine engineers, several near retirement [10]. Capacity-based software charges tie that spend to incumbent contracts (inferred). GAO reports a dwindling pool of people who can support the Treasury's COBOL and Assembly systems [13].
- **Hidden behaviour.** MO argues that logic lives in CICS conversations, batch timing, error paths and schedulers, not only in the source [15].
- **Guarded access.** Rob Mee describes the mainframe as a fortress guarded by security, compliance, network and database teams, where a data request can carry an eight-week SLA [16].
- **Career and compliance risk.** MO published a survey by TechTarget's Enterprise Strategy Group of 150 senior IT decision makers (April 2024). In it, 27% worried they could lose their jobs if a technology they backed failed [17]. An analyst notes that regulated owners need evidence of behavioural equivalence before they will run new code [18].

## Origin

Rob Mee founded Pivotal Labs. He became chief executive of its corporate successor, Pivotal Software, in August 2015 and left after VMware completed its $2.7 billion purchase in December 2019 [19][3]. In April 2020, at the request of a former CDC director, he gathered former colleagues to build software for state Covid contact tracing teams. The states could not operate it, so his team ran it. That build-and-run model led to Ratio PBC, then to Mechanical Orchard [20]. MO launched in November 2022 with a $7 million seed. Its investors included Spider Capital, Bloomberg Beta and Cendana Capital [20][3]. The co-founders included COO Matthew Work, previously at Cognizant and Amazon, and Dan Podsedly, VP of R&D [3][21]. Kent Beck, creator of Extreme Programming, was chief scientist by January 2023 and stepped down in November 2024 [22][23].

The insight was a digital transplant: copy the behaviour of a black-box system whose source or experts may be gone, then run the copy for the client [20]. By October 2023 the rule was that the running system is the specification [24].

Why then:

- Retirements were draining the people who understood these systems [20].
- Language models could write code that nobody trusted. In June 2023 Roberto Ostinelli, now CTO, had two GPT-4 agents pair through a test-driven exercise for about $6 a run. GPT-3 failed the task [25]. Tests drawn from real behaviour supplied the missing trust (inferred).
- Mee says a late-2024 breakthrough let MO quickly develop and validate AI-generated code, and that work became Imogen [26].
- AWS, Microsoft and Google wanted an on-ramp for mainframe applications and data, and partnered with MO for it [3].

## First wedge

The first job was one batch program. At the Fortune 500 retailer, the teams picked a high-performance batch process in the physical inventory system, the same job that had sunk the previous attempt [10]. Work began in March 2023 with a VPN link from the cloud to the mainframe and an automated delivery pipeline. By the end of April the replica matched full production runs, and it went live on 27 June 2023 [10].

Batch came first because each run has inputs and outputs that can be captured. A month of captured runs gives both a description of the job and a ready-made test suite [16]. The retailer had already failed twice, first with a consultancy-led lift-and-shift and then with the transpile. It was open to an incremental approach with ongoing proof of feasibility [10]. Having already paid for the failure of translation made a behaviour-first pitch easier to buy (inferred).

The other early anchor was Omni Logistics. Emergence says MO moved Omni's core applications to the cloud within about a year of its founding [27]. Retail and logistics face lighter regulation than banking, which likely shortened approvals (inferred). Forward Air announced on 25 January 2024 that it had completed its purchase of Omni [28], two weeks before MO named Omni as a customer [21]. Omni is absent from later MO material (inferred).

## First 10 customers

**Finding them.** Emergence credited Mee with more than 30 years of client work and the trust of thousands of executives and engineers [27]. That network likely supplied the early deals (inferred).

**Selling them.** In 2023 the door opener was a low-investment discovery phase [24]. By early 2024 it was a 6 to 8 week pilot that rewrote one component and ran it in parallel until the outputs matched [3]. By 2025 the unit was a minimum viable modernisation: a cluster of jobs rewritten in staging over 8 to 12 weeks [16]. By August 2026 MO offered a free proof of concept, under NDA and without access to the prospect's data. It shows about 100,000 lines characterisation-tested, in days [29].

**Implementing them.** MO engineers built the pipeline, ran old and new side by side and cut over one workload at a time [10][9]. At the retailer, later jobs reached production at two a week, and CICS screens and data migration started in September 2023 [10]. Mee said a firm of about 100 people lacked the scale to run these programmes alone [16]. Thoughtworks became MO's first partner in April 2025 [5].

**Who they were.** About ten organisations are described publicly, two by name (inferred count):

- Omni Logistics, named in February 2024 [21], and the Fortune 500 retailer from March 2023 [10].
- Logistics firms and multi-billion-dollar retailers by April 2024 [30]. Public sector and consumer goods clients by April 2025 [5].
- By April 2026: a North American bank (COBOL, Assembler and Easytrieve to Java on AWS), a global automaker working in an air-gapped environment, a manufacturer's warranty system, a North American retailer's sales system, and a Latin American insurer's claims system that drives 30% of its mainframe use [31].
- Fortune 100 healthcare and Fortune 20 automotive buyers, quoted anonymously on MO's site [32].
- SulAmérica, named in April 2026, which took more than 130,000 lines of COBOL to verified equivalence in months [33]. MO links that talk to the 30% claims system [31]. The presenter put it this way: "This isn't translated code." [33]

**Sales cycle.** Not published. The retailer work began about four months after launch [20][10], which points to relationship-led first sales (inferred). Mee names inertia, and the cynicism left by failed projects, as his biggest challenge [34]. Bloop, a startup that sold AI legacy-code modernisation, including transformation projects for banks, saw deals take 18 to 24 months before it pivoted away [35].

**Pricing.** In 2024 MO said it modernised and then operated customer applications [30]. Since 2025 it says it develops, licenses and implements software [5]. Customers own the code [2]. The AWS Marketplace listing shows an Imogen unit at $100,000 per month on a one-month contract. It tells buyers to contact MO for scoped pricing or a private offer [36].

## How big it is now

| Round | Announced | Amount | Lead | SEC filing |
|---|---|---|---|---|
| Seed | Nov 2022 | $7M [3] | Not stated; backers include Spider Capital, Bloomberg Beta, Cendana Capital [20] | None found |
| Series A | 7 Feb 2024 | $24M [21] | Emergence Capital [21] | $26.25M sold to 16 investors, first sale 21 Nov 2023 [7] |
| Series B | 6 Aug 2024 | $50M [37] | GV [37] | $40.0M sold at filing, first sale 27 Jun 2024 [38]; $53.0M from 4 investors by Feb 2025 [39]; $69.17M from 12 investors by 13 Jan 2026 [8] |

- The Series A also drew Industry Ventures, Spider Capital, Bloomberg Beta, Cendana Capital and Webb Investment Network [21], and valued MO at $95 million [6]. Fin Capital and MongoDB were named as investors from April 2025 [5], and Munich Re Ventures by January 2026 [34]. They most likely joined through the Series B extension (inferred).
- MO claimed over $84 million raised in April 2025 [5]. Filings plus the seed add up to about $102 million. If the Series A filing already includes converted seed money, the total is closer to $95 million (inferred). The January 2026 filing lists Emergence's Jake Saper and GV's Crystal Huang as outside directors [8][27][37].
- Headcount: 50+ in February 2024 [21], 80+ in August 2024 [37], about 100 in April 2025 [14], 100+ in January 2026 [34], about 100 in September 2026 [9].
- Revenue: more than $10 million, with a profit, in 2023 [6][27]. Later revenue is undisclosed, and the filings decline to state a range [8].
- Throughput: upwards of 10,000 lines of COBOL per engineer per week by April 2026. MO also reports a record of 11,578 fully verified lines in 28 hours at a major North American retailer [31].
- Channels: Thoughtworks (April 2025) [5], DoD Tradewinds (July 2025) [40], Google Cloud Marketplace (November 2025) [41], AWS Marketplace (December 2025) [42], the GSA Schedule via Carahsoft (April 2026) [43] and Leidos (July 2026) [44].

## What made it hard

- **Proving equivalence.** MO tested an LLM-only rewrite of an AWS sample job. The rewrite compiled and ran, but it read a keyed VSAM file as a flat stream, mishandled EBCDIC packed decimals, dropped an assembler branch and changed the abend code [4]. None of these sit in the business rules. MO's fix is a harness that feeds COBOL and Java the same input and compares the bytes [4].
- **Getting the data.** Capturing production data is 25% of MO's own effort model [45]. One customer's capture ran to about 600 GB, and MO's worked example uses six months of data [46].
- **Performance and model limits.** The retailer's earlier transpile ran at a tenth of mainframe speed [10]. Mee says models fail on large programs, so each program must first be cut into self-contained units [16].
- **Incumbent and platform response.** On 23 February 2026 Anthropic published a blog post on COBOL modernisation with Claude Code [47]. IBM shares fell 13% that day, their worst day since October 2000 [48]. IBM Software's chief commercial officer, Rob Thomas, replied that modernisation is not a COBOL language problem [49]. IBM is also building AI accelerators into the mainframe itself [14]. AWS gives its mainframe modernisation agent away free [50]. Google's Dual Run is designed to run old and new systems in parallel on production workloads and compare the results [51]. Verification, MO's core, is becoming a hyperscaler feature (inferred).
- **Team.** The pipeline still stalls on unaddressable code paths or unlicensed utilities, and then needs engineers who can read legacy code [9]. Matthew Work, an officer and director on the February 2025 filing, is absent from the January 2026 filing [39][8], which suggests he has left (inferred).
- **Cash.** MO was profitable in 2023 [27] but took $50 million from GV in a raise Mee called unsolicited [2]. The Series B stayed open for about 18 months and grew to $69.17 million [38][8]. No new priced round has been announced (inferred).

## Strategy

MO is migration-led, and it began close to an AI-run service. The 2022 plan was to build replacements and operate them for clients [20]. In February 2024 Blocks and Files compared it to a professional services firm [3]. Imogen, launched in April 2025, turned a workflow MO had run by hand into a licensed platform [5][4]. HFS calls MO a software company with forward-deployed engineers [9]. A Hypercubic co-founder counters that its model is closer to professional services [52].

The route from wedge to core runs from one batch job to clusters of jobs, then CICS screens and transactions, then whole applications, and finally the mainframe [16][10][24]. Imogen keeps old and new running together and gives access to VSAM, Db2 and IMS data during phased cutover [1][4]. The rule is to move first and improve later [4].

Automation has climbed. In August 2024 MO said developers debugged and reviewed the finished product [2]. In July 2026 it released an autonomous build-and-verify pipeline with no human code review, in which separate agents check output against captured behaviour [44][53]. MO also ingests Google Mainframe Assessment Tool output and AWS Transform business rules [54], and Google presents it as a partner building Gemini-powered modernisation factories [55]. HFS says the long-term aim is to maintain these systems with agents after the rewrite [9].

How far it has got:

- **Retailer.** One of its largest global inventory and supply chain systems, which handles vendor replenishment, was retired by September 2024. Across the engagement, MO reports batch cycle time improved 265%, throughput up 347% and code cut by 50% to 65% so far [10]. MO expected two of the largest remaining applications to be finished by January 2026 [10]. No public update confirms that (inferred).
- **Manufacturer.** The four remaining warranty batch jobs moved to Python on AWS Batch, and three Db2 schemas to Postgres, in four months [11].
- **SulAmérica.** More than 130,000 lines reached verified equivalence and were described as ready for production. Whether the code is live is not stated [33].
- No named customer has publicly switched off a whole mainframe (inferred).

## What others can copy

1. **Make the incumbent's runtime your specification.** Capture real inputs and outputs and make byte-level equivalence the acceptance test [4][46]. Test: post-cutover reconciliation defects per workload, target zero.
2. **Start with the job that killed the last project.** The retailer's first workload reached production in under four months [10]. Test: days from contract to first production cutover, target under 120.
3. **Sell proof before price.** A free proof of concept on about 100,000 lines in days shows results before the budget fight [29]. Test: share of proofs of concept that convert to paid work within two quarters.
4. **Sell the layer the platforms skip.** AWS gives its mainframe modernisation agent away [50]. MO takes the business rules AWS extracts, plus Google's assessment output, and adds verification [54]. Test: share of pipeline co-sold with a hyperscaler.
5. **Run the method by hand before you productise it.** Imogen automates a workflow MO previously ran by hand [4]. Test: lines replicated per engineer-week each quarter. MO reports upwards of 10,000 [31].
6. **Borrow distribution while small.** A firm of about 100 people sells through Thoughtworks, Leidos, the GSA Schedule and two cloud marketplaces [9][5][44][43][41][42]. Test: partner-sourced share of new programmes.

## Open questions

- **Whole exits.** Has any customer switched off a mainframe, and did the retailer finish two of its largest remaining applications by January 2026 [10]?
- **Coverage.** Captured flows can miss seasonal peaks and rare exception paths [18]. HFS reports symbolic-execution test suites that cover about 99% of code [9], but no independent audit is public (inferred).
- **Economics.** Revenue has been undisclosed since 2023 [8], and headcount has held near 100 [14][9]. Whether margins look like software or services is unknown (inferred).
- **Commoditisation.** AWS's free agent and Google's Dual Run already cover parts of the verification job [50][51].
- **Regulators.** This study found no public regulator view on AI-written code that no human reviews [44].
- **Fidelity versus improvement.** MO's security chief calls the goal bug-for-bug compatibility [56]. The improve step after the move is not yet documented at scale (inferred).
- **Patent.** The launch release cites a patented method [5]. This study did not find the patent.
- **Federal.** MO holds Tradewinds, GSA and Leidos channels [40][43][44] but names no federal customer (inferred).

## Sources

1. Mechanical Orchard, Imogen platform page, undated, accessed 5 Oct 2026. https://www.mechanical-orchard.com/platform
2. TechCrunch (Kyle Wiggers), Series B report, 7 Aug 2024. https://techcrunch.com/2024/08/07/mechanical-orchard-led-by-ex-pivotal-ceo-scores-50-million-round-led-by-alphabets-gv/
3. Blocks and Files (Chris Mellor), company briefing report, 28 Feb 2024. https://www.blocksandfiles.com/ai-ml/2024/02/28/mechanical-orchard-updates-mainframe-migration-with-ai/1606190
4. Mechanical Orchard (Sam Sanders, Field CTO), white paper on verification, 8 Jun 2026. https://www.mechanical-orchard.com/research/mainframe-modernization-is-a-verification-problem
5. Mechanical Orchard, Imogen launch and Thoughtworks partnership release, 3 Apr 2025. https://www.mechanical-orchard.com/insights/mechanical-orchard-ignites-major-shift-in-enterprise-it-transformation-with-imogen
6. SiliconANGLE (Mike Wheatley), Series A report, 7 Feb 2024. https://siliconangle.com/2024/02/07/mechanical-orchard-raises-22m-funding-help-companies-ditch-mainframes-cloud/
7. US SEC EDGAR, Mechanical Orchard Form D (equity offering), filed 9 Feb 2024. https://www.sec.gov/Archives/edgar/data/1953406/000195340624000001/primary_doc.xml
8. US SEC EDGAR, Mechanical Orchard Form D/A, filed 16 Jan 2026 (signed 13 Jan 2026). https://www.sec.gov/Archives/edgar/data/1953406/000195340626000001/primary_doc.xml
9. HFS Research (Hansa Iyengar, David Cushman), Hot Tech profile, 30 Sep 2026. https://www.hfsresearch.com/research/hfs-services-as-software-hot-tech-mechanical-orchard/
10. Mechanical Orchard, Fortune 500 retailer case study, undated, accessed 5 Oct 2026. https://www.mechanical-orchard.com/restoring-confidence-in-modernizing-mainframes
11. Mechanical Orchard, manufacturer warranty system case study, 30 Jul 2026. https://www.mechanical-orchard.com/case-studies/modernizing-a-manufacturing-companys-warranty-system-for-the-cloud
12. IBM Newsroom, z16 launch release, 5 Apr 2022. https://newsroom.ibm.com/2022-04-05-Announcing-IBM-z16-Real-time-AI-for-Transaction-Processing-at-Scale-and-Industrys-First-Quantum-Safe-System
13. US Government Accountability Office, GAO-25-107795 on critical legacy systems, 17 Jul 2025. https://files.gao.gov/reports/GAO-25-107795/index.html
14. Network World (Michael Cooney), Imogen launch report, 3 Apr 2025. https://www.networkworld.com/article/3953659/mechanical-orchard-taps-gen-ai-for-mainframe-to-cloud-modernization.html
15. Mechanical Orchard, monthly newsletter, 25 Feb 2026. https://www.mechanical-orchard.com/insights/half-baked
16. Thoughtworks Technology Podcast with Rob Mee and Rachel Laycock (transcript), 15 May 2025. https://www.thoughtworks.com/insights/podcasts/technology-podcasts/accelerating-mainframe-modernization-generative-ai
17. Mechanical Orchard, survey report by TechTarget Enterprise Strategy Group, fieldwork Apr 2024, accessed 5 Oct 2026. https://www.mechanical-orchard.com/tech-leaders-state-of-mind-report
18. HyperFRAME Research (Stephanie Walter), analyst note, 13 Jul 2026. https://hyperframeresearch.com/2026/07/13/mechanical-orchards-imogen-update-tests-whether-ai-mainframe-modernization-can-move-from-translation-to-proof/
19. Wikipedia, Pivotal Software article, accessed 5 Oct 2026. https://en.wikipedia.org/wiki/Pivotal_Software
20. Mechanical Orchard (Rob Mee), founding post, published at launch in Nov 2022 (page shows 3 Apr 2022). https://www.mechanical-orchard.com/insights/the-seeds-of-mechanical-orchard
21. Mechanical Orchard, Series A release, 7 Feb 2024. https://www.mechanical-orchard.com/insights/mechanical-orchard-raises-24m-in-series-a-round-to-solve-the-legacy-it-modernization-challenge
22. Mechanical Orchard (Kent Beck), company history post, 10 Jan 2023. https://www.mechanical-orchard.com/insights/mechanical-orchard-a-new-company-with-a-long-history
23. Kent Beck, Software Design: Tidy First? newsletter, 15 Nov 2024. https://newsletter.kentbeck.com/p/flying-solo
24. Mechanical Orchard (Kent Beck), method post, 2 Oct 2023. https://www.mechanical-orchard.com/insights/how-to-eat-an-elephant
25. Mechanical Orchard (Roberto Ostinelli), AI pairing experiment, 21 Jun 2023. https://www.mechanical-orchard.com/insights/can-two-ais-play-the-tdd-pairing-game
26. Mechanical Orchard (Rob Mee), Imogen launch post, 3 Apr 2025. https://www.mechanical-orchard.com/insights/the-kitty-hawk-moment-that-changed-legacy-modernization
27. Emergence Capital (Jake Saper, Yaz El-Baba), investment post, 7 Feb 2024. https://www.emcap.com/thoughts/mechanical-orchards-quiet-ai-revolution-moving-the-global-economy-from
28. FreightWaves, Forward Air and Omni Logistics deal close, 25 Jan 2024. https://www.freightwaves.com/news/forward-air-omni-merger-finally-closes
29. Mechanical Orchard, free proof-of-concept offer, 24 Aug 2026. https://www.mechanical-orchard.com/case-studies/poc
30. Mechanical Orchard, Edward Hieatt appointment release, 23 Apr 2024. https://www.mechanical-orchard.com/insights/mechanical-orchard-appoints-edward-hieatt-to-lead-customer-experience
31. Mechanical Orchard (Edward Hieatt), first year of Imogen, 27 Apr 2026. https://www.mechanical-orchard.com/insights/reflections-on-the-first-year-of-imogen
32. Mechanical Orchard, home page customer quotes, accessed 5 Oct 2026. https://www.mechanical-orchard.com/
33. Mechanical Orchard, SulAmérica talk at Google Cloud Next 2026, 24 Apr 2026. https://www.mechanical-orchard.com/media/customer-presentation-at-google-cloud-next-2026-sulamerica
34. Pulse 2.0, interview with Rob Mee, 6 Jan 2026. https://pulse2.com/mechanical-orchard-profile-rob-mee-interview/
35. Scaling DevTools podcast (Jack Bridger), bloop and Vibe Kanban episode notes, 15 Feb 2026. https://scalingdevtools.com/podcast/episodes/louis-from-vibe-kanban-20-000-github-stars-and-walking-away-from-6-figure-deals
36. AWS Marketplace, Imogen by Mechanical Orchard listing, accessed 5 Oct 2026. https://aws.amazon.com/marketplace/pp/prodview-tcry42kis5gxq
37. Mechanical Orchard, Series B release, 6 Aug 2024. https://www.mechanical-orchard.com/insights/mechanical-orchard-secures-50-million-to-safely-transition-large-organizations-off-risky-legacy-software
38. US SEC EDGAR, Mechanical Orchard Form D (equity offering), filed 7 Aug 2024. https://www.sec.gov/Archives/edgar/data/1953406/000195340624000002/primary_doc.xml
39. US SEC EDGAR, Mechanical Orchard Form D/A, filed 5 Feb 2025. https://www.sec.gov/Archives/edgar/data/1953406/000195340625000001/primary_doc.xml
40. Mechanical Orchard, Tradewinds awardable release, 9 Jul 2025. https://www.mechanical-orchard.com/insights/mechanical-orchard-delegated-awardable-for-dod-contracts-on-tradewinds-solutions-marketplace
41. Mechanical Orchard, Google Cloud Marketplace release, 24 Nov 2025. https://www.mechanical-orchard.com/insights/mechanical-orchards-mainframe-modernization-platform-now-available-on-google-cloud-marketplace
42. Mechanical Orchard, AWS Marketplace release, 8 Dec 2025. https://www.mechanical-orchard.com/insights/mechanical-orchards-mainframe-modernization-platform-now-available-in-aws-marketplace
43. Carahsoft, GSA Schedule release, 9 Apr 2026. https://www.carahsoft.com/news/mechanical-orchard-federal-it-modernization-platform-now-available-to-the-public-sector-through-carahsofts-gsa-contract-2026
44. Mechanical Orchard, Summer 2026 release and Leidos partnership, 9 Jul 2026. https://www.mechanical-orchard.com/insights/mechanical-orchard-releases-imogen-platform-improvements
45. Mechanical Orchard, COBOL migration calculator post, 26 Apr 2026. https://www.mechanical-orchard.com/insights/we-rebuilt-that-cobol-migration-calculator
46. Mechanical Orchard, white paper on behaviour-based verification, 22 Sep 2026. https://www.mechanical-orchard.com/research/modernizing-mainframes-a-behavior-based-approach-to-verification
47. Anthropic, Claude blog post on COBOL modernisation, 23 Feb 2026. https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization
48. DevOps.com (Tom Smith), IBM share fall report, 25 Feb 2026. https://devops.com/a-blog-post-about-cobol-just-cost-ibm-30-billion-heres-what-actually-happened/
49. IT-Online, opinion by Rob Thomas of IBM Software, 4 Mar 2026. https://it-online.co.za/2026/03/04/lost-in-translation-what-the-ai-code-debate-keeps-getting-wrong/
50. Amazon Web Services, AWS Transform pricing page, accessed 5 Oct 2026. https://aws.amazon.com/transform/pricing/
51. heise online (Moritz Förster), Google Cloud mainframe tools report, 5 Aug 2026. https://www.heise.de/en/news/Google-Cloud-Mainframe-modernization-with-four-building-blocks-11399665.html
52. Hacker News, comment by a Hypercubic co-founder on its launch thread, 10 Nov 2025. https://news.ycombinator.com/item?id=45880663
53. Mechanical Orchard (Roberto Ostinelli), software dark factory post, 7 Jul 2026. https://www.mechanical-orchard.com/insights/the-software-dark-factory-modernizing-legacy-systems-with-no-humans-in-the-loop
54. Mechanical Orchard (Nick Keune), AWS Transform integration post, 8 Jul 2026. https://www.mechanical-orchard.com/insights/imogen-now-integrated-with-aws-transform
55. Google Cloud Next 2026, session BRK1-071 listing, 22 Apr 2026. https://www.googlecloudevents.com/next-vegas/session/3913023/real-world-mainframe-modernization-redefined-with-gemini
56. Mechanical Orchard (Sam Pierson, CISO), ISO/IEC 27001 announcement, 18 Sep 2026. https://www.mechanical-orchard.com/insights/mechanical-orchard-iso-iec-certification

## Fact-check notes

- Summary: the funding total was given as "about $102 million". It is now a range of roughly $95 million to $102 million, because the $26.25M Series A Form D may include converted seed money ($7M + $26.25M + $69.17M = $102.4M).
- Summary: re-cited the headcount and "applications, not whole mainframes" claims to [9][10][11]. Sources [7][8] do not support them.
- GAO: changed "11 most critical systems were 23 to 60 years old" to "about 23 to 60". Added that the 3-of-10 count is as of February 2025, which is what the report says.
- Retailer cost: [10] says "tens of millions" is infrastructure spend. Wording now says so.
- Mee "fortress": "a data request can wait eight weeks" became "can carry an eight-week SLA", matching his words in [16].
- ESG survey: [17] does not say MO commissioned it. Now reads "MO published a survey by TechTarget's ESG", with respondents described as senior IT decision makers who "worried they could lose" jobs.
- HyperFRAME [18]: rephrased "regulated owners need evidence of equivalence" as the analyst's view, which is what the note supports.
- Pivotal: "chief executive of its corporate successor" now names Pivotal Software and says Mee left after VMware completed the deal. [19] confirms the 18 Aug 2015 start, and [3] gives the $2.7B price and the December 2019 close.
- Co-founders: "Co-founders were" became "co-founders included". Blocks and Files names Mee, Work and Podsedly, but other early staff may also count.
- Mee breakthrough: "fast and verifiable" became "quickly develop and validate", matching [26].
- Batch rationale: [3] has no statement that batch came first because of discrete inputs and outputs. The claim is rewritten and re-cited to Mee's podcast remark [16].
- Retailer receptiveness: [10] confirms the earlier lift-and-shift. Its wording is "ongoing proof of feasibility", not "proof of progress". Text corrected.
- Omni: "in MO's first year" became "within about a year of its founding", per [27]. FreightWaves reports the deal completion was announced on 25 January 2024. It does not give a separate close date.
- Discovery phase: "low-cost" became "low-investment", per [24].
- Proof of concept: added "without access to your data" and "characterisation-tested". The offer is about 100,000 lines characterisation-tested, not a run on the prospect's own code, per [29].
- Thoughtworks: "first delivery partner" became "first partner". [5] calls it the "inaugural partnership".
- April 2026 customer list: the bank engagement in [31] does not name a "payments system", so that detail is removed. The automaker is "global", not described as an "air-gapped workload".
- Bloop: [35] says "transformation projects to banks", not banks as the sole market. Wording adjusted.
- AWS Marketplace pricing: "request a quote" became "contact MO for scoped pricing or a private offer", per [36].
- Series B row: added the first sale date of 27 Jun 2024 from [38]. The Series B "stayed open for 18 months" became "about 18 months" (June 2024 to January 2026).
- Board: "Saper and Huang sat on the board" was incomplete. The January 2026 filing also lists Mee and Hieatt as directors, so the text now says "outside directors". Re-cited Saper's Emergence affiliation to [27].
- Throughput: [31] is dated 27 April 2026 and says "upwards of 10,000 lines... replicating", so "by March 2026" became "by April 2026". The record was at "a major North American retailer", not a "Fortune 100 retailer".
- Anthropic [47]: "COBOL modernisation guide" became "blog post", per the source.
- Rob Thomas: "IBM software executive" became his title, chief commercial officer of IBM Software, per [49].
- Google Dual Run: "runs... and compares" became "is designed to run... and compare". [51] describes what Google "intends" to do.
- Automation: "In August 2024 developers reviewed all AI output" overstated [2]. It now says developers "debugged and reviewed the finished product".
- Imogen data access: "reads VSAM, Db2 and IMS data through standard interfaces" became "gives access to... during phased cutover". Neither [1] nor [4] mentions standard interfaces.
- Google [55]: "partner in Gemini-powered modernisation" became "partner building Gemini-powered modernisation factories", per the session listing.
- Retailer outcome: [10] describes the retired system as a "global inventory and supply chain system" that handles vendor replenishment. The 265%, 347% and 50% to 65% figures are engagement-wide, not specific to that system. "The two largest remaining applications" became "two of the largest remaining applications", which MO "expected" to finish. The same fix is applied in Open questions.
- Manufacturer: "the last four" became "the four remaining", matching [11].
- SulAmérica: "production status is not stated" was wrong. [33] calls the code "ready for production". Text now says whether it is live is not stated.
- Copy item 5: "workflow MO ran manually for years" became "previously ran by hand". [4] gives no duration. "Verified lines" became "lines replicated", matching [31].
- Style: no em dashes or banned hype words remained. "Pivotal" is kept only as the company name.