# bloop (cautionary case)

## Summary

bloop, a London startup from Y Combinator's Summer 2021 batch, tried to move COBOL applications at banks and other large enterprises off the mainframe by converting them into readable Java [1][2]. It ran COBOL through a static transpiler, used LLMs to refactor the output, tested every change against the original program's behavior, and sold the work as fixed-price pilots [3][4]. It ran this business for about a year from its March 2024 launch, earned at least one six-figure payment, named no customer publicly, pivoted to the developer tool Vibe Kanban in June 2025 and shut down on 10 April 2026 [5][6]. The lesson: Louis put bank sales cycles at 18 to 24 months. A small team living on 2021 funding, with no experienced enterprise seller, could not wait that long, even though Louis says the technology worked [5][7].

## The legacy it attacks

IBM said in April 2022 that 45 of the world's top 50 banks, 8 of the top 10 insurers, 7 of the top 10 retailers and 8 of the top 10 telcos value its mainframe for their most critical workloads [8]. Anthropic's post cites an estimate that COBOL handles about 95% of US ATM transactions, with hundreds of billions of lines in production [9]. bloop targeted mainframe and midrange estates moving to the cloud [10]. The owners are banks, insurers, retailers, telcos and governments [8][12]. One prospect told the founders it ran a billion lines of COBOL [4].

Why these systems stuck:

- **Regulation.** TSB's April 2018 platform migration affected all its branches and a significant proportion of its 5.2 million customers, and some issues lasted until December 2018. UK regulators fined it £48.65 million in 2022, on top of £32.7 million in redress [11]. It was a platform move rather than a COBOL rewrite. It is still the failure bank risk teams plan against (inferred).
- **Cost and time.** GAO found the 11 most critical US federal legacy systems are about 23 to 60 years old, 8 use outdated languages such as COBOL and assembly, and they cost about $754 million a year to run. As of February 2025 only 3 of the 10 modernizations GAO flagged in 2019 were complete [12].
- **Skills and tests.** GAO says Treasury's COBOL systems depend on a dwindling pool of skilled people [12]. bloop co-founder Louis Knight-Webb said retirements outpace new COBOL engineers, some customers had one engineer left who understood the code, and bloop had yet to see a customer with tests [4].
- **Data.** Gartner argues data volume and interconnection make wholesale migration impossible for most large enterprises [13].
- **Vendors.** Incumbents have sold to these banks for about 40 years [5]. IBM's revenue was rising on unusually high mainframe sales in 2026 [13].
- **Training data.** On bloop's COBOLEval benchmark GPT-4 solved 8.9% of problems, against 67% on the Python original [14].

## Origin

Louis Knight-Webb, a software developer who had co-founded the political-ad transparency project Who Targets Me, started bloop with Gabriel Gordon-Hall, an ML research engineer [4][15][1]. The UK company was incorporated on 27 April 2021 [16]. A Delaware company, Bloop AI, Inc., followed on 9 July 2021 and appears to be the parent (inferred) [17].

The first product, code search on a fine-tuned embedding model, was overtaken when GitHub Copilot launched about a month into YC [4]. Enterprise code search followed from a few months after YC [4]. A GPT-4 version launched on Hacker News in March 2023 as a free desktop app, with a $12 per user per month cloud plan for teams [18]. It made a few sales, but larger deals stalled against GitHub's bundle [4].

The COBOL idea came from those sales calls and from developer events. One contact cited a billion lines of COBOL, and the founders barely knew what COBOL was [4]. The insight was an arbitrage. LLMs write good Java and poor COBOL. So transpile COBOL to Java mechanically, then have LLMs refactor the Java, with the original program's behavior as ground truth [3].

Why then. GPT-4-class models could refactor Java, while COBOLEval showed LLMs wrote poor COBOL [3][14]. bloop cited a Kyndryl 2023 survey saying firms were moving 37% of their application portfolio off the mainframe [2]. IBM made watsonx Code Assistant for Z, a COBOL-to-Java tool, available in October 2023 [19]. Regulation cut the other way: the PRA's operational resilience framework arrived in 2021 [11].

bloop announced its COBOL products on 20 March 2024, and its homepage switched from code search between 27 February and 24 March [2][20][21]. bloop called the product bloop modernise [2]. No bloop source opened for this study uses the name ModerniseAI.

## First wedge

The March 2024 launch had three products [2][21]:

- **Write**, an offline COBOL coding assistant for VS Code built on a smaller version of mAInframer-1, Code Llama models fine-tuned on millions of synthetic COBOL lines. The 34B model scored 10.27% on COBOLEval, ahead of GPT-4's 8.9% [2][14].
- **Understand**, the old code search extended to mainframe languages [2].
- **Modernise**, COBOL-to-Java conversion [2].

By January 2025 the homepage sold only Modernise [22].

The job that earned money was narrow. bloop isolated a small cluster of a customer's COBOL that touched a database, a file and a network call, converted it to Java and deployed it to the cloud. The pilot had a fixed price and bloop absorbed overruns [4]. Its first commercial project was a 5 million-line codebase [3].

The buyer was a large enterprise, banks foremost, that had already decided to leave COBOL [4][5]. That made a good first wedge. bloop did not have to sell the decision to migrate. The pilot answered cost and timeline questions nobody could answer while one engineer understood the code. The fixed price kept the buyer's risk small [4]. Readable output was the edge over line-by-line converters, whose machine-generated Java engineers reject [4][22]. bloop claimed deduplication alone cut codebases by at least half [4].

## First 10 customers

No public source names a bloop customer. The record supports a handful of engagements, not ten (inferred). bloop said it had paying customers by June 2024 [3]. In January 2025 Louis said no pilot had yet failed to continue into a full project [4]. In February 2026 he described a Canadian customer that had paid six figures [5].

How it found them:

1. Code-search sales calls and developer events in San Francisco [4].
2. The mainframe community. Louis was on the GSE UK 2024 agenda with a talk titled "GitHub Copilot for COBOL developers" [23]. Both founders were listed on the initial team of the Open Mainframe Project's Zorse proposal, built on COBOLEval, with staff from IBM, Rocket Software and Broadcom [24].
3. Open research. The COBOLEval post drew 106 points on Hacker News [25].
4. A financial-services accelerator. bloop joined the 2025 FinTech Innovation Lab New York, a 12-week program run by Accenture and the Partnership Fund for New York City, with a demo day at BNY scheduled for late June [10]. By June 2025 its site said it was based in New York [26].
5. Founder intro calls booked through the website [22].

Selling and delivery. Each pilot opened with an evaluation matrix agreed with the customer, such as Spring Boot as the target framework [4]. Delivery ran survey, proof-of-concept sprint, then full modernisation [22]. Tests came from historic batch inputs and outputs, recorded green-screen sessions automated with RPA, and LLM-written tests [4]. GPT-4o's 4,096-token output cap, about 350 lines, forced method-by-method refactoring [3]. Some customers needed self-hosted models [3].

Sales cycle and price. Louis put sales cycles at 18 to 24 months [5]. The Canadian deal died overnight when bloop's contact there was fired, during what Louis called the first wave of US tariffs on Canada. Those tariffs took effect on 4 March 2025 (date inferred) [5][27]. The site listed no prices [22]. Pilots were fixed-price, and at least one customer paid six figures [4][5].

## How big it is now

| Item | Figure | Date | Source |
|---|---|---|---|
| Pre-seed | Raised before YC, amount not disclosed | 2021 | [4] |
| YC investment | $125K | Sep 2021 | [28] |
| Main round | $7.31M (Tracxn labels it Series A), lead not shown on Tracxn's public page | Dec 2021 | [28] |
| Investors named by bloop | Y Combinator, Khosla Ventures, Sands Capital, LocalGlobe | Mar 2024 | [2] |
| Total raised | $7.43M, no later round listed | read Oct 2026 | [28] |
| UK staff, average incl. directors | 3, 3, 4, 6 | years to Apr 2022, 2023, 2024, 2025 | [29][30][31] |
| Team size on YC page | 10 | undated, read Oct 2026 | [1] |
| UK net liabilities | £0.57M, £1.61M, £2.69M, £3.73M | 30 Apr 2022, 2023, 2024, 2025 | [29][30][31] |
| Revenue | Never disclosed | | |
| Named customers | None | | |
| Vibe Kanban at shutdown | 30,000 monthly active users, 25,000 GitHub stars | Apr 2026 | [7] |
| GitHub stars | Vibe Kanban 28,264; archived bloop search repo 9,492 | 5 Oct 2026 | [32][33] |
| Status | Shut down 10 Apr 2026; UK company still listed active, confirmation statement made 27 Apr 2026 | | [6][16] |

UK net liabilities rose by £1.0 million to £1.1 million a year in the three years to April 2025 [29][30][31]. That tracks an operating loss funded by the Delaware company (inferred). At that pace the 2021 money could not run far past 2026 (inferred). In November 2025 bloop was hiring two senior engineers at £100,000 each [34]. Bloop AI, Inc. opened a UK establishment in November 2024 and described its business as software tools for legacy modernisation [35].

## What made it hard

**Sales cycle against runway.** Louis said 18 to 24 month cycles were going to kill bloop relative to its runway and the milestones it needed to raise again [5]. In June 2024 bloop advertised plenty of runway [3]. A year later it did not (inferred).

**Cash and talent.** bloop lived on its 2021 funding, which Louis credits for surviving every pivot [28][5]. It built a transpiler for messy, poorly documented COBOL dialects [4] with four to six UK staff on average [30][31]. Mechanical Orchard, a migration rival, raised $50 million in August 2024 and had more than 80 staff [36]. At shutdown no people or money were left to keep servers running [37].

**Buyer chaos.** The Canadian cancellation had nothing to do with product or competitors. Internal upheaval at the buyer ended it [5].

**Founder-market fit.** The founders had no mainframe of their own. Louis said it was not a problem they had faced. He also said he did not enjoy selling to banks, whose buyers respond to risk more than technology, and that the bank's harder problem is what to do with developers a migration makes redundant [5].

**Regulation and data.** Some customers barred sending code to outside model providers [3]. Batch tests needed customers' historic inputs and outputs [4]. bloop's published material covers code and tests. It says nothing about moving VSAM or Db2 data (inferred).

**Incumbents with downstream revenue.** AWS made its mainframe tool generally available on 15 May 2025, converting COBOL, JCL and Db2 to Java and Postgres [38], and prices the agent at zero [39]. Louis argued that AWS recovers this on cloud bills for decades, and Accenture through transformation programs [5]. IBM's tool converts COBOL to Java and is pitched to keep workloads on IBM Z [19].

**Moat erosion.** In January 2025 Louis said the need to build a real transpiler insulated bloop from general coding agents [4]. By February 2026 he said off-the-shelf tools could convert COBOL to Java [5]. On 23 February 2026 Anthropic published COBOL guidance claiming modernization in quarters instead of years [9], and IBM shares fell 13% that day [40].

**Category risk.** Gartner predicts more than 70% of mainframe exit projects started in 2026 will miss their intended benefits, and 75% of mainframe-exit vendors will pivot or cease to exist by 2030 [13]. bloop had already done both when The Register reported the forecast [6][13].

## Strategy

bloop was migration-led, delivered as an AI-run service. Louis called the COBOL year a move into services [5], and the site described a research lab converting code for customers [22]. Two overlay products, a COBOL coding assistant and code understanding, were dropped within ten months [2][22].

The planned path to the core: translation as the wedge into risk-averse enterprises, then maintenance, Java upgrades and new features on the converted code [4]. bloop offered Java on z/OS as a target [2] but found no customer who wanted it [4].

How far it got: pilots, at least one six-figure engagement and a 5 million-line first project [5][3]. No source shows a converted system in production or a core ledger replaced (inferred). bloop left the category about 15 months after launch; the Vibe Kanban repository was created on 14 June 2025 [32]. COBOLEval survives, now hosted by the Zorse project [41].

## What others can copy

1. **Size runway to the buyer's clock.** bloop faced 18 to 24 month cycles on limited runway [5]. Test: at the first paid bank pilot, months of cash exceed 1.5 times the median pilot-to-contract time.
2. **Contract phase two inside phase one.** The fixed-price pilot got bloop in [4] but did not survive the firing of its buyer-side contact [5]. Test: every pilot carries pre-agreed phase-two pricing and three named executive sponsors.
3. **Hire the enterprise seller before the first bank pilot.** Asked at the April 2026 shutdown talk what he would change, Louis said: "I'd hire somebody who's really good at selling to enterprise" [7]. He was looking back on the whole company, after explaining that Vibe Kanban never sold to enterprises. Test: a founding-team member has closed a seven-figure regulated IT deal.
4. **Earn after cutover, or partner with someone who does.** AWS prices its mainframe agent at zero [39] because, in Louis's reading, the cloud bill pays later [5]. Test: over half of contract value lands after go-live.
5. **Do not build the moat on a model weakness.** bloop's moat assumed LLMs could not handle COBOL [4]. AWS made its tool generally available four months later, and a frontier lab published COBOL guidance thirteen months later [38][9]. Test: rerun your benchmark against frontier agents each quarter. If the gap halves, move the moat to verification, data or distribution.
6. **Sell the equivalence evidence.** Tests built from production inputs and recorded sessions give a bank's risk team something it can check [4], and regulators punish failed cutovers [11]. Test: a per-module evidence pack the risk team signs without the vendor present.

## Open questions

- Did any bloop conversion reach production, and did the 5 million-line project finish? Neither is public [3].
- How many pilots converted? The January 2025 claim of no failed conversions predates the Canadian cancellation (inferred) [4][5].
- Would a systems-integrator or hyperscaler partner, reachable through the Accenture-run lab, have shortened the cycle? Untested [10].
- Can a standalone AI migration vendor earn margins when AWS gives its agent away? Unproven [39].
- Does a deterministic transpiler still matter now that general agents read COBOL? Unresolved [9][13].
- Where did the converter go? Public repositories hold the archived search engine and COBOLEval, not the transpiler (inferred) [33][41].

## Sources

1. Y Combinator, company page for Vibe Kanban (formerly bloop), Summer 2021 batch, accessed 5 Oct 2026. https://www.ycombinator.com/companies/bloop
2. bloop blog (Louis Knight-Webb), Modernising Legacy Code with AI, 20 Mar 2024 (Wayback capture 31 Mar 2024). https://web.archive.org/web/20240331182231/https://bloop.ai/blog/modernising-legacy-code
3. bloop blog (Louis Knight-Webb), Building an AI Agent (To Modernise COBOL), 16 Jun 2024 (Wayback capture 19 Jun 2024). https://web.archive.org/web/20240619004357/https://bloop.ai/blog/building-an-ai-agent
4. Scaling DevTools (Jack Bridger), episode 117, Louis Knight-Webb from Bloop.ai, the YC startup turning COBOL into Java, page with full transcript, 2 Jan 2025. https://scalingdevtools.com/podcast/episodes/louis-bloop
5. Scaling DevTools (Jack Bridger), episode 175, Louis from Vibe Kanban: 20,000 GitHub stars and walking away from 6-figure deals, page with full transcript, 15 Feb 2026. https://scalingdevtools.com/podcast/episodes/louis-from-vibe-kanban-20-000-github-stars-and-walking-away-from-6-figure-deals
6. Vibe Kanban blog (Louis Knight-Webb), Goodbye bloop, 10 Apr 2026. https://www.vibekanban.com/blog/shutdown
7. AI Engineer (YouTube), Software Engineering Is Becoming Plan and Review, talk by Louis Knight-Webb at AI Engineer Europe, auto-captions read, published 2 May 2026. https://www.youtube.com/watch?v=W76woOYHlvY
8. IBM Newsroom, Announcing IBM z16: Real-time AI for Transaction Processing at Scale and Industry's First Quantum-Safe System, 5 Apr 2022. https://newsroom.ibm.com/2022-04-05-Announcing-IBM-z16-Real-time-AI-for-Transaction-Processing-at-Scale-and-Industrys-First-Quantum-Safe-System
9. Anthropic (claude.com blog), COBOL Modernization with AI: Breaking the Cost Barrier, 23 Feb 2026. https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization
10. FinTech Innovation Lab, FinTech Innovation Lab New York Announces 2025 Class, 27 Mar 2025. https://www.fintechinnovationlab.com/news/new-york/fintech-innovation-lab-new-york-announces-2025-class/
11. Bank of England, TSB fined £48.65m for operational resilience failings, 20 Dec 2022. https://www.bankofengland.co.uk/news/2022/december/tsb-fined-for-operational-resilience-failings
12. US Government Accountability Office, GAO-25-107795, Agencies Need to Plan for Modernizing Critical Decades-Old Legacy Systems, 17 Jul 2025. https://files.gao.gov/reports/GAO-25-107795/index.html
13. The Register (Simon Sharwood), AI-powered mainframe exits are a bubble set to pop (Gartner analysis), 15 Apr 2026. https://www.theregister.com/2026/04/15/gartner_mainframe_exit_analysis/
14. bloop blog (Gabriel Gordon-Hall), Evaluating LLMs on COBOL, 30 Mar 2024 (Wayback capture 31 Mar 2024). https://web.archive.org/web/20240331182159/https://bloop.ai/blog/evaluating-llms-on-cobol
15. AI Engineer, speaker profile of Louis Knight-Webb, accessed 5 Oct 2026. https://ai.engineer/speakers/louis-knight-webb
16. Companies House, BLOOP AI LIMITED (13362018) company overview, accessed 5 Oct 2026. https://find-and-update.company-information.service.gov.uk/company/13362018
17. Companies House, OSIN01 registration of the UK establishment of Bloop AI, Inc., with Delaware certificate of incorporation filed 9 Jul 2021; registered 27 Jan 2025. https://find-and-update.company-information.service.gov.uk/company/FC042143/filing-history/MzQ1MTg5NjAwNGFkaXF6a2N4/document?format=pdf&download=0
18. Hacker News, Launch HN: Bloop (YC S21), Code Search with GPT-4, 20 Mar 2023. https://news.ycombinator.com/item?id=35236275
19. IBM Newsroom, IBM Launches watsonx Code Assistant, Delivers Generative AI-powered Code Generation Capabilities Built for Enterprise Application Modernization, 26 Oct 2023. https://newsroom.ibm.com/2023-10-26-IBM-Launches-watsonx-Code-Assistant,-Delivers-Generative-AI-powered-Code-Generation-Capabilities-Built-for-Enterprise-Application-Modernization
20. bloop.ai homepage, code-search era, Wayback capture 27 Feb 2024. https://web.archive.org/web/20240227141528/https://bloop.ai/
21. bloop.ai homepage, legacy modernisation launch with Modernise, Write and Understand, Wayback capture 24 Mar 2024. https://web.archive.org/web/20240324024506/https://bloop.ai/
22. bloop.ai homepage, Modernise only, Wayback capture 10 Jan 2025. https://web.archive.org/web/20250110045103/https://bloop.ai/
23. GSE UK, 2024 conference agenda, GitHub Copilot for COBOL developers (Louis Knight-Webb, bloop AI Limited), 2024. https://conferences.gs-uk.org/2024/agenda/presentation/3604
24. GitHub, Open Mainframe Project TAC issue 642, Zorse project proposal, 17 Apr 2024 (read via GitHub API). https://api.github.com/repos/openmainframeproject/tac/issues/642
25. Hacker News, How well can LLMs write COBOL? (discussion of the bloop post), 30 Mar 2024 (read via HN Algolia API). https://hn.algolia.com/api/v1/items/39873793
26. bloop.ai homepage, New York location, Wayback capture 2 Jun 2025. https://web.archive.org/web/20250602145318/https://bloop.ai/
27. Holland & Knight, U.S. Implements Threatened Tariffs on Canada, Mexico and China, 4 Mar 2025. https://www.hklaw.com/en/insights/publications/2025/03/us-implements-threatened-tariffs-on-canada-mexico-and-china
28. Tracxn, Bloop: Funding Rounds and List of Investors, accessed 5 Oct 2026. https://tracxn.com/d/companies/bloop/__hqMc93zC_T45GG3d4slM5LtzNE1YugULEXT2rSKm4pI/funding-and-investors
29. Companies House, Bloop AI Limited micro-entity accounts to 30 Apr 2022, approved 26 Jan 2023. https://find-and-update.company-information.service.gov.uk/company/13362018/filing-history/MzM2NzM1Mjk0N2FkaXF6a2N4/document?format=xhtml&download=1
30. Companies House, Bloop AI Limited micro-entity accounts to 30 Apr 2024, with 2023 comparatives, approved 11 Feb 2025. https://find-and-update.company-information.service.gov.uk/company/13362018/filing-history/MzQ1NDg4NzUzOGFkaXF6a2N4/document?format=xhtml&download=1
31. Companies House, Bloop AI Limited micro-entity accounts to 30 Apr 2025, with 2024 comparatives, approved 29 Jan 2026. https://find-and-update.company-information.service.gov.uk/company/13362018/filing-history/MzUwMjI5OTk2NmFkaXF6a2N4/document?format=xhtml&download=1
32. GitHub REST API, BloopAI/vibe-kanban repository metadata, accessed 5 Oct 2026. https://api.github.com/repos/BloopAI/vibe-kanban
33. GitHub REST API, BloopAI/bloop repository metadata (archived), accessed 5 Oct 2026. https://api.github.com/repos/BloopAI/bloop
34. bloop.ai homepage, makers of Vibe Kanban, with open positions, Wayback capture 16 Nov 2025. https://web.archive.org/web/20251116155511/https://bloop.ai/
35. Companies House, BLOOP AI, INC. (FC042143) overseas company overview, accessed 5 Oct 2026. https://find-and-update.company-information.service.gov.uk/company/FC042143
36. Mechanical Orchard, Mechanical Orchard secures $50 million to safely transition large organizations off risky legacy software, 6 Aug 2024. https://www.mechanical-orchard.com/insights/mechanical-orchard-secures-50-million-to-safely-transition-large-organizations-off-risky-legacy-software
37. X (Louis Knight-Webb, @tokengobbler), post announcing the bloop shutdown, 10 Apr 2026 (text read via the api.fxtwitter.com mirror). https://x.com/tokengobbler/status/2042647208135123078
38. AWS Migration and Modernization Blog, post announcing general availability of AWS Transform, 15 May 2025. https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-generally-available/
39. AWS, AWS Transform pricing page, accessed 5 Oct 2026. https://aws.amazon.com/transform/pricing/
40. DevOps.com (Tom Smith), A blog post about COBOL just cost IBM $30 billion. Here's what actually happened, 25 Feb 2026. https://devops.com/a-blog-post-about-cobol-just-cost-ibm-30-billion-heres-what-actually-happened/
41. GitHub REST API, zorse-project/COBOLEval, the redirect target of BloopAI/cobolEval, accessed 5 Oct 2026. https://api.github.com/repositories/774969181

## Fact-check notes

- Summary: "bank deals took 18 to 24 months to close" changed to Louis's description of 18 to 24 month sales cycles. In [5] he was describing the cycles he expected, not deals that actually closed.
- Summary: "with technology that worked" changed to "even though Louis says the technology worked". No source shows a conversion in production.
- Summary: "deterministic transpiler" changed to "static transpiler", the term [3] uses.
- IBM [8]: "run IBM Z" changed to "value IBM's mainframe for their most critical workloads", matching IBM's wording.
- Anthropic [9]: "Anthropic estimates" changed to "Anthropic's post cites an estimate". The post presents the 95% figure as an outside estimate.
- TSB [11]: [11] says a "significant proportion" of the 5.2 million customers was hit by the initial issues and some issues lasted until December 2018. Reworded to say that, not that a large share was disrupted until December.
- GAO [12]: "8 use COBOL or assembly" changed to "8 use outdated languages such as COBOL and assembly". Ages are "about" 23 to 60, and the 3 of 10 count is dated "as of February 2025".
- Skills bullet: "none had automated tests" changed to "bloop had yet to see a customer with tests". In [4] Louis said "we haven't seen one yet".
- IBM revenue [13]: reworded to The Register's claim that IBM's revenue was rising on unusually high mainframe sales.
- Origin: "had to look up what COBOL was" softened to "barely knew what COBOL was". In [4] Louis said they had "kinda heard of it".
- Origin: The Hacker News launch [18] was a GPT-4 code search, free on desktop with a $12 cloud plan for teams. It was not the start of enterprise code search, which [4] places a few months after YC.
- Origin: "COBOLEval showed LLM-only translation failed" changed to "LLMs wrote poor COBOL". COBOLEval measures COBOL code generation, not translation.
- Origin: Cut "validated the category" (hype). IBM's tool is now described as made available in October 2023 [19]. DevOps.com [40] says it was announced in August 2023.
- Origin: Kyndryl figure reworded to "37% of their application portfolio", as [2] puts it.
- First wedge: Write packaged "a smaller version" of mAInframer-1 [2], not the 34B model. The 8.9% GPT-4 score matches the table in [14], although that post's prose says 10.27%. The figure is kept as is.
- First 10 customers: The GSE UK talk [23] is titled "GitHub Copilot for COBOL developers". The draft paraphrased it as "AI coding assistants".
- First 10 customers: RPA was used to automate recorded green-screen flows [4]. "Replayed" changed to "automated".
- Sales cycle: The link to the 4 March 2025 tariffs is now marked as inferred. Louis only said "the first wave" of tariffs on Canada [5].
- Table: "lead not disclosed" changed to "lead not shown on Tracxn's public page". Tracxn hides the lead investor field from public view, so it is not confirmed as undisclosed.
- Founder-market fit: "had never run a mainframe" changed to "had no mainframe of their own", with Louis's statement that it was not a problem they had faced [5].
- Incumbents: IBM's tool is "pitched to keep workloads on IBM Z" [19]. The draft said it "keeps the work on Z".
- Copy item 3: The "hire an enterprise seller" quote [7] came in a whole-company retrospective, right after he explained that Vibe Kanban never sold to enterprises. It was not specific to the COBOL business, and that context is now stated.
- Copy item 5: "AWS shipped its tool" changed to "made its tool generally available" [38]. AWS previewed it at re:Invent in December 2024.
- No em dashes were found in the draft. Hype wording was removed in the IBM sentence ("validated the category").