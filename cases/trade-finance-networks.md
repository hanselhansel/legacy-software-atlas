## Summary

Contour, we.trade and Marco Polo were bank-backed blockchain networks, started from 2017, that set out to replace paper letters of credit (LCs) and paper-heavy open-account trade finance [1][2][3]. Each tried to put the buyer, the seller and both of their banks on one shared ledger, so documents and payment promises moved as data instead of couriered paper [4][5][6]. All three failed as consortia. we.trade went into liquidation in June 2022 and Marco Polo in February 2023. Contour's bank owners pulled funding in October 2023, when it was running at about 60-70 transactions a month. Meanwhile AI document-checking overlays such as Cleareye and Traydstream signed J.P. Morgan, Lloyds, NatWest, Deutsche Bank and Citi, and built integrations with the Finastra, CGI and Surecomp systems banks already ran [7][8][9][10][11][12][13][14][15][16]. The lesson: a product that pays back inside one bank's operations team gets bought, and one that pays back only when every counterparty switches at once does not (inferred).

## The legacy it attacks

Documentary trade still runs on paper. In ICC's 2018 survey of more than 250 banks in over 90 countries, 52% said paper had not been removed from document checking, and one transaction could carry more than 100 pages [17].

Banks book it on a few long-lived engines. Finastra's Trade Innovation serves more than 200 banks [18]. CGI's hosted Trade360 has run for 25 years, covers 322 bank locations in 93 countries, processes about 15 million transactions a year and bills per transaction [19]. Surecomp's customers span more than 80 countries [20].

Around the engines sit operations teams. They check LCs, bills of lading and invoices against ICC rules (UCP 600 and ISBP), screen for sanctions and trade-based money laundering (TBML), and re-key data into back-end systems [15][21]. J.P. Morgan's trade business receives nearly 4 million documents a year [22]. A vendor factsheet puts a large trade bank's yearly spend on risk, compliance, sanctions and AML tasks at US$25m to US$42m [15].

It stuck for two reasons.

- **Law.** A bill of lading is a transferable document. The holder's rights passed by physically handing over the paper [23]. UNCITRAL adopted its Model Law on Electronic Transferable Records (MLETR) on 13 July 2017 so that control of one electronic record could do the same job [24][23]. 13 jurisdictions have laws based on or influenced by it, some covering only certain documents [25]. English law accepted electronic trade documents from 20 September 2023 [26]. Electronic bills of lading (eBLs) were 1.2% of container bills issued by DCSA members' carriers in 2021 and nearly 5% in the first half of 2024 [27].
- **Switching cost.** HSBC chose CGI Trade360 in April 2019 and launched its first two markets in October 2022 [28][29]. That is about 3.5 years for one of the best-resourced buyers (inferred).

The networks targeted the paper moving between the four parties, not these engines, which they still needed at each end (inferred).

## Origin

Contour began in mid-2017 as Voltron, an LC project on R3's Corda ledger [9][1]. Eight banks founded it, among them HSBC, ING, BNP Paribas and Standard Chartered [1]. In May 2018 HSBC and ING ran a live LC for Cargill on soybeans shipped from Argentina to Malaysia in 24 hours, against the usual five to ten days [4]. It incorporated in Singapore in January 2020 as Contour, with Carl Wegner as CEO [30][31].

we.trade began in January 2017 as the Digital Trade Chain, built by Deutsche Bank, HSBC, KBC, Natixis, Rabobank, Société Générale, UniCredit and IBM [2] on Hyperledger Fabric [7]. In October 2018 it absorbed the Batavia project, adding CaixaBank, Erste Group and UBS for 12 bank shareholders [32].

Marco Polo, launched in 2017, was run by TradeIX, co-founded and led by Rob Barnes, on R3's Corda [3][6][55].

The shared insight: if all four parties saw one record, nobody would reconcile paper, and an LC could close in a day [4]. The timing was the ledger boom (inferred): BCG forecast in August 2016 that blockchain would reach trade finance within three years [21].

The same report named a second path: it cited Citibank's view that intelligent OCR could lift productivity in labour-heavy trade tasks by as much as 50% [21]. Traydstream took it. It was incorporated in London on 21 April 2016 [33], and co-founder Achille D'Antoni said in 2017 that none of the dozen OCR products the team reviewed could handle trade paper in all its formats [34]. CEO Sameer Sehgal argued in 2018 that a ledger leaves the document checking itself undone [35]. Cleareye was founded in 2019 [36]; its co-founders include CEO Mariya George and President Sarath Sasikumar [37].

## First wedge

Contour's wedge was the LC between member banks for large corporates. Cargill came first [4]; later users included Rio Tinto, Tata Group and SAIC [38]. The LC is rule-bound and bank-run, and member banks often sat at both ends (inferred). Tests cut LC processing by up to 90%, from about 10 days to under 24 hours [39].

we.trade aimed at European SMEs trading on open account. Its ledger tracked delivery and could trigger payment under a bank payment undertaking [5]. The first live run, in July 2018, was seven transactions over five days between ten companies through HSBC, KBC, Nordea and Rabobank [40].

Marco Polo offered receivables discounting and an irrevocable commitment from the buyer's bank to pay on the due date, resting on automatic matching of trade data [41][6]. TradeIX said corporate clients saw the commitment replacing some of their LC business [41].

The overlays chose a narrower job inside one bank: checking presented documents against the LC and ICC rules, then running sanctions and TBML checks [15][16]. Traydstream lined up pilots with three banks for the second half of 2017 [34]. Cleareye's anchor was J.P. Morgan's trade group, starting in Asia-Pacific in September 2022 [42]. No counterparty had to change anything (inferred).

## First 10 customers

The networks sold first to their owners. Contour ended with nine bank investors and 22 bank members [9]. we.trade had licence deals with 14 banks by April 2019 [43] and 16 banks in 15 countries by 2022 [7]. Only two shareholder banks, CaixaBank and Nordea, fully deployed it, along with several smaller banks [44]. Marco Polo claimed more than 30 banks [8].

Corporates came through demonstration deals, such as Commerzbank's May 2021 Marco Polo payment commitments for Kuraray Europe and Şişecam, and for KSB and Voith [6].

Rollout was slow. Wegner recalled that one founder bank took more than two years to start using Contour, and the network struggled to get enough small local banks to pay for a node [45]. Contour charged banks and corporates membership dues plus per-transaction fees [39]; we.trade licensed its platform to banks [40].

Overlays closed single-bank deals within about a year. Stanbic Bank Uganda went live on Traydstream in December 2020 after a few months of trial processing [46]. Deutsche Bank piloted Traydstream from July 2021 and agreed to integrate it in August 2022 [47]. J.P. Morgan signed with Cleareye in September 2022 and in April 2023 agreed to map its output into the back office [42][22]. Lloyds began implementing Cleareye in September 2024 [48]. Neither vendor publishes prices (no price list found).

## How big it is now

**Contour.** Its June 2021 Series A+ drew nine banks plus R3, Bain and CryptoBLK, amounts undisclosed [30][41]. In 2023 it processed 60-70 transactions a month [10]. HSBC alone handles more than 250,000 LCs a year [49], so the whole network ran at about 0.3% of one owner's LC flow (inferred, different years). Xalts bought Contour in a deal announced in February 2024, for a price in the high single-digit millions, in cash and stock [38]. Xalts shrank it by almost 90% and sold all of it, debt included, to XDC Ventures in October 2025, when most of its 30-plus network agreements were inactive and DBS and Bangkok Bank were among the active users [50]. Contour never disclosed revenue or headcount (none found).

**we.trade.** It raised close to €12m before 2021 [51], including (inferred) a 2020 round of about €5m in which IBM took 7% [44], then €5.5m in January 2021 [51]. It cut staff by about half in 2020 [7] and lost about €8m that year [52]; an analyst put 2020 revenue near US$4m, citing no source [53]. It claimed many hundreds of live transactions by April 2020 [54].

**Marco Polo.** TradeIX raised a US$16m Series A in June 2018, led by ING Ventures with BNP Paribas, Kistefos and Tech Mahindra [3]. Accenture added an undisclosed sum in December 2019 [55]. At insolvency it had 91 staff and €5.2m of debts, €2.6m of it owed to Ireland's Revenue; liabilities exceeded assets by €2.5m [56][57]. Its successor, Kanexa, sells invoice matching to corporates through Bank of America's CashPro and charges per matched invoice [58][59].

**The overlays.** Cleareye raised an undisclosed seed round led by Season Two Ventures in November 2021 and an undisclosed strategic round from J.P. Morgan in June 2023, and had 114 staff in May 2025 [36][22]. It had more than 10 clients by the end of 2024 [60]. By September 2026 its named clients were J.P. Morgan, Bank of America, Lloyds, Mizuho, Axis Bank, Riyad Bank, NatWest and RAKBANK [61].

Traydstream raised US$3.5m in August 2018 [62], US$8m led by Spearhead Capital in May 2021 [63], US$21m led by Pivot Investment Partners and e& capital in September 2023 [64] and US$11m from the same pair in August 2025 [65]. Tracxn records a further undisclosed round in August 2026, US$66.2m raised in total and 133 staff [66]. Traydstream, now also backed by Mashreq's NeoVentures, claims US$350bn of trade, over 7 million transactions and 68 countries [67]. Deutsche Bank and SMBC use it [11], and Citi offers it to clients [13].

For scale, CGI says Trade360 processed more than 15 million transactions in 2025 [61], against about 800 a year on Contour in 2023 (inferred).

## What made it hard

- **Four corners or nothing.** A network LC worked only if buyer, seller and both banks used the same network [45]. R3's head of trade later called paper the most interoperable instrument available [68].
- **The law lagged.** The UK act took effect on 20 September 2023, after we.trade and Marco Polo had failed and about five weeks before Contour's closure memo [26][9]. With eBLs at 1.2% in 2021 [27], a digital LC usually still rested on paper transport documents (inferred).
- **The back office came last.** Contour announced integration with Finastra's Fusion Trade Innovation in October 2022 and with Surecomp in March 2023 [69][70]. Wegner later said one more year of funding would have connected more bank back offices [71].
- **Governance blocked the cash.** None of Contour's bank owners would lead a round for two more years of runway, and venture funds balked at the ownership structure [9]. Wegner pitched 170 VC firms and family offices without success [45]. we.trade's owners could not agree on new money, and an expected €2-3m from Euler Hermes never came [7].
- **Users did not ask for it.** Corporates saw Contour as making life easier for banks [45]. we.trade's founding COO, Roberto Mancone, left in 2019 saying the industry built what providers valued, not users [72]. Barnes, by then Kanexa's CEO, said of Marco Polo: "no bank wanted to use it and there was no buy-in" [58].
- **The market turned.** Bank of America pulled out of a proposed US$12m deal with Marco Polo in late January 2023, after a run of blockchain collapses that included Maersk and IBM's TradeLens [8].
- **The incumbents moved.** HSBC, an owner of both Contour and we.trade, put its global trade platform on CGI Trade360 [9][7][28]. By October 2022, 88% of its trade transactions started digitally [29]. Finastra, CGI and Surecomp opened their platforms to fintech add-ons [73][61][16].

## Strategy

The networks were greenfield. They built a new rail and new instruments (a digital LC, a bank payment undertaking, a payment commitment) and asked every counterparty to move [39][5][6]. The planned path ran from one instrument to all of trade: Contour said in June 2021 it would move into open account [41]. Booking engines were never in scope (inferred). By 2022-2023 Contour was integrating with them as an add-on [69][70], an overlay posture reached late and without overlay economics (inferred).

How far they got: no bank replaced a booking engine with any of them (inferred). The successors moved toward single paying buyers (inferred). Xalts pitched Contour as a Plaid-style API layer for trade [71]. XDC plans stablecoin settlement pilots [50]. Komgo, the only network of that cohort still standing in 2023, announced a planned integration with Finastra's engine in September 2026 [10][74].

The winners are overlays by design. ClearTrade is pre-integrated with Finastra Trade Innovation and connects to existing back offices by API [15]. Traydstream agreed to integrate with Surecomp's RIVO in January 2023 and announced a planned native CGI Trade360 integration in October 2025 [16][14]. Cleareye partnered with RIVO in April 2024 [75]. They replace the examiner's keying and checking, not the engine, and none has shown a path into the core (inferred). The largest buyers may skip them: HSBC built its own checker, Smart Checking, live in Hong Kong, the UAE and the UK [11].

## What others can copy

1. **Count who must change before value appears.** A Contour LC needed four parties on the network; Traydstream at Stanbic needed one bank [45][46]. Test: does one buyer get the full return if no counterparty changes anything?
2. **Distribute through the incumbent core.** Both overlays have live or announced integrations with Trade Innovation, Trade360 or RIVO [15][14][16]. Test: is a live integration with the buyer's booking engine in place before the pilot starts?
3. **Price against a budget line.** Risk and compliance tasks cost a large trade bank US$25m to US$42m a year, per a vendor factsheet [15]. RAKBANK bought Cleareye to meet UAE central bank TBML rules [37]. Test: does the pilot cut minutes per presentation, or close a named compliance gap, within six months?
4. **Check the law per corridor.** eBLs were nearly 5% of container bills in the first half of 2024, and 13 jurisdictions have MLETR-based laws [27][25]. Test: are the target documents legally valid in electronic form in most of the buyer's corridors today?
5. **Have one owner who can write the next cheque.** No Contour bank owner would lead its round, and 170 investors passed [9][45]. Test: can one investor fund 24 months of runway without a consortium vote?
6. **Plan for insourcing at the top.** HSBC built its own checker while peers bought from vendors [11]. Test: what share of revenue comes from banks big enough to build?

## Open questions

- **Can an overlay become the core?** None has replaced a booking engine (inferred). Conpend, a peer with more than 35 financial institution clients, sold a majority stake to Cape Investment Partners in July 2025 [76].
- **Will incumbents absorb the layer?** Finastra already offers AI document checks through partners [73]. It could build or buy its own (inferred).
- **Are the metrics independent?** Cleareye's 98% classification and 91% extraction rates come from an awards profile [60]. A 2024 Finastra factsheet gave lower figures: extraction above 80% and classification at 85% [15]. This study found no independent benchmark.
- **Does digitisation shrink the market?** Cleareye, Lloyds, Finastra and Enigio extracted structured electronic transport data with no OCR [61]. If eBLs scale, paper checking shrinks (inferred).
- **Do overlays make money?** Neither firm publishes revenue. Traydstream filed group accounts to March 2025 in July 2026 [77], not analysed here.
- **Can a network work now?** XDC bets that stablecoin settlement changes Contour's economics [50][78]. Only volume will tell.

## Sources

1. Global Trade Review (GTR), 23 Oct 2018. Voltron open testing and founding banks. https://www.gtreview.com/news/digital-trade/blockchain-project-voltron-launches-open-testing-phase/
2. KBC Group newsroom, 2017 (release undated). Digital Trade Chain becomes we.trade, Santander joins. https://newsroom.kbc.com/digital-trade-chain-consortium-launches-wetrade-announces-joint-venture-and-welcomes-santander
3. Global Trade Review (GTR), 27 Jun 2018. TradeIX Series A and Marco Polo members. https://www.gtreview.com/news/digital-trade/tradeix-to-aggressively-grow-blockchain-ecosystem-after-ing-investment/
4. Global Banking & Finance Review, 15 May 2018. HSBC and ING live LC for Cargill on Corda. https://www.globalbankingandfinance.com/hsbc-and-ing-execute-ground-breaking-live-trade-finance-transaction-on-r3s-corda-blockchain-platform/
5. Ledger Insights, 21 Jan 2020. we.trade products and automated payments. https://www.ledgerinsights.com/wetrade-blockchain-trade-finance-automated-payments/
6. Commerzbank, May 2021. Live Marco Polo payment commitment transactions. https://www.commerzbank.de/group/newsroom/press-releases/transactions-marco-polo.html
7. Global Trade Review (GTR), 6 Jun 2022. we.trade closure, funding history, shareholders. https://www.gtreview.com/news/top-stories/we-trade-calls-it-quits-after-running-out-of-cash/
8. Global Trade Review (GTR), 23 Feb 2023. Marco Polo liquidation, missed launches, Bank of America deal. https://www.gtreview.com/news/top-stories/marco-polo-brings-in-liquidators-as-funds-run-dry/
9. Global Trade Review (GTR), 27 Oct 2023. Contour shutdown memo, owners, failed funding round. https://www.gtreview.com/news/top-stories/exclusive-contour-to-shut-down-as-bank-shareholders-pull-funding/
10. Ledger Insights, 1 Nov 2023. Contour closure, monthly transaction count, other networks. https://www.ledgerinsights.com/contour-blockchain-trade-finance-network-shutter/
11. Global Trade Review (GTR), 29 Sep 2026. HSBC builds its own AI document checking; vendor map. https://www.gtreview.com/news/digital-trade/hsbc-goes-proprietary-on-ai-trade-doc-checking/
12. NatWest Group, 27 May 2026. NatWest partners with Cleareye.ai. https://www.natwestgroup.com/news-and-insights/news-room/press-releases/enterprise/2026/may/natwest-partners-with-cleareye-ai-to-transform-trade-operations-.html
13. Citi, 4 Dec 2023. Citi collaboration with Traydstream. https://www.citigroup.com/global/news/press-release/2023/citi-collaborates-with-traydstream-to-streamline-document-services-for-faster-and-more-effective-client-solutions
14. Traydstream, 3 Oct 2025. Native integration with CGI Trade360. https://traydstream.com/traydstream-and-cgi-are-collaborating-together-to-deliver-seamless-trade-finance-automation/
15. Finastra with Cleareye.ai, May 2024 (file date). ClearTrade factsheet. https://www.finastra.com/sites/default/files/file/2024-05/resource-cleartrade-cleareyeai-factsheet.pdf
16. Surecomp, 12 Jan 2023. Traydstream document checking for RIVO. https://surecomp.com/news/surecomp-enables-further-trade-finance-efficiencies-with-traydstream-partnership/
17. International Chamber of Commerce (ICC), 23 May 2018. ICC trade finance digitalisation survey. https://iccwbo.org/news-publications/news/new-icc-survey-shows-pace-trade-finance-digitalisation/
18. Global Finance, 4 Feb 2025. Finastra Trade Innovation bank count and partners. https://gfmag.com/award/winner-insights/finastra-anastasia-mcalpine-revamping-trade-finance/
19. CGI, Apr 2025 (file date). CGI Trade360 overview brochure. https://www.cgi.com/sites/default/files/2025-04/cgi-trade360-short-overview-brochure-2025.pdf
20. Surecomp, 14 Jul 2026. Surecomp RIVO adoption and country footprint. https://surecomp.com/news/surecomp-reinforces-digital-trade-finance-leaderships-as-global-ecosystem-continues-to-grow/
21. Boston Consulting Group, 30 Aug 2016. Digital revolution in trade finance. https://www.bcg.com/publications/2016/digital-revolution-trade-finance
22. Cleareye.ai, 20 Jun 2023. J.P. Morgan strategic investment. https://cleareye.ai/jpmorgan-invests-in-financial-technology-provider-cleareye-ai/
23. ICC Academy, 4 Sep 2024. MLETR overview. https://academy.iccwbo.org/digital-trade/article/mletr-an-overview-of-uncitrals-model-law-on-electronic-transferable-records/
24. UNCITRAL, accessed 5 Oct 2026. MLETR text page and adoption date. https://uncitral.un.org/en/texts/ecommerce/modellaw/electronic_transferable_records
25. UNCITRAL, accessed 5 Oct 2026. MLETR enactment status by jurisdiction. https://uncitral.un.org/en/texts/ecommerce/modellaw/electronic_transferable_records/status
26. Steamship Mutual, 21 Sep 2023. UK Electronic Trade Documents Act in force. https://www.steamshipmutual.com/publications/articles/uk-electronic-trade-documents-act-2023-enters-force
27. Global Trade Review (GTR), 17 Sep 2024. DCSA electronic bill of lading adoption. https://www.gtreview.com/news/digital-trade/ebl-adoption-doubles-to-5-but-barriers-to-digitisation-remain-dcsa-finds/
28. CGI, 30 Apr 2019. HSBC selects CGI Trade360 for its global trade platform. https://www.cgi.com/uk/en-gb/news/hsbc-chooses-cgi-as-partner-for-delivery-of-transformational-global-trade-technology-platform
29. CGI, 7 Oct 2022. HSBC Trade Solutions launch in UK and Hong Kong. https://www.cgi.com/en/hsbc-launches-digital-platform-that-revolutionises-trade-finance
30. Ledger Insights, 17 Jun 2021. Contour Series A+ and Singapore incorporation. https://www.ledgerinsights.com/citi-hsbc-ing-blockchain-trade-finance-network-contour-series-a/
31. CTMfile, 29 Jan 2020. Voltron becomes Contour. https://ctmfile.com/story/voltron-transforms-into-contour
32. Global Trade Review (GTR), 3 Oct 2018. we.trade absorbs Batavia. https://www.gtreview.com/news/digital-trade/we-trade-and-batavia-merge-blockchain-platforms-for-trade-finance/
33. Companies House, accessed 5 Oct 2026. Traydstream Limited registration record. https://find-and-update.company-information.service.gov.uk/search/companies?q=traydstream
34. Global Trade Review (GTR), 3 Aug 2017. Traydstream early partnerships and bank pilots. https://www.gtreview.com/news/digital-trade/new-fintech-partnerships-to-push-automation-in-trade-finance/
35. Traydstream (reprint of a Trade Finance Global interview), 12 Jun 2018. CEO interview on blockchain and document processing. https://traydstream.com/blockchain-who-does-the-processing-interview-with-traydstream-ceo/
36. Tracxn, accessed 5 Oct 2026. Cleareye company profile. https://tracxn.com/d/companies/cleareye/__--5lWnExl_G_aXXYMH71cpd_Q0GY36GSeAFXcClnXw0
37. Cleareye.ai, 29 Aug 2025. RAKBANK deployment for UAE TBML rules. https://cleareye.ai/rakbank/
38. TechCrunch, 19 Feb 2024. Xalts acquires Contour. https://techcrunch.com/2024/02/19/xalts-contour/
39. Global Trade Review (GTR), 5 Oct 2020. Contour goes live; pricing model. https://www.gtreview.com/news/top-stories/exclusive-contour-goes-live-making-blockchain-based-trade-finance-a-reality/
40. Global Trade Review (GTR), 3 Jul 2018. First four banks live on we.trade. https://www.gtreview.com/news/digital-trade/first-four-banks-go-live-on-we-trade-blockchain-platform/
41. Global Trade Review (GTR), 21 Jun 2021. Contour plans open account; Marco Polo modules. https://www.gtreview.com/news/top-stories/contour-to-take-on-marco-polo-with-move-into-open-account-trade-finance/
42. Cleareye.ai, 21 Sep 2022. Strategic alliance with J.P. Morgan. https://cleareye.ai/cleareye-ai-announces-strategic-alliance-with-j-p-morgan/
43. Global Trade Review (GTR), 29 Apr 2019. we.trade COO departs; licence count. https://www.gtreview.com/news/digital-trade/exclusive-interview-roberto-mancone-leaves-we-trade-blockchain-company-new-general-manager-appointed/
44. Tech Monitor, 6 Jun 2022. we.trade shutdown, deployment, IBM stake. https://www.techmonitor.ai/emerging-technology/ibm-backed-blockchain-platform-we-trade-shutting-down/
45. Digital Finance (DigFin), 13 Nov 2024. Post-Contour analysis with former CEO. https://www.digfingroup.com/contour-trade-finance/
46. Traydstream, 9 Dec 2020. Stanbic Bank Uganda goes live. https://traydstream.com/news/standard-bank-goes-live-on-traydstream-platform
47. Traydstream, 4 Aug 2022. Deutsche Bank partnership after July 2021 pilot. https://traydstream.com/deutsche-bank-partners-with-traydstream/
48. PYMNTS, 3 Sep 2024. Lloyds and Cleareye.ai partnership. https://www.pymnts.com/artificial-intelligence-2/2024/lloyds-and-cleareye-launch-ai-centric-trade-finance-partnership/
49. HSBC, accessed 5 Oct 2026 (page copyright 2026). HSBC letters of credit product page. https://www.business.hsbc.com/en-gb/products/letters-of-credit
50. Global Trade Review (GTR), 29 Oct 2025. XDC Ventures buys Contour from Xalts. https://www.gtreview.com/news/digital-trade/xdc-ventures-to-re-energise-contour-after-xalts-sale/
51. The Irish Times, 29 Jan 2021. we.trade raises EUR 5.5m. https://www.irishtimes.com/business/technology/dublin-based-blockchain-banking-joint-venture-raises-5-5m-1.4471195
52. The Block (citing Independent.ie), 5 Jun 2022. we.trade liquidation and 2020 loss. https://www.theblock.co/linked/150204/banks-prepare-to-liquidate-irish-blockchain-venture-independent-ie-says
53. Futurum Research, 9 Jun 2022. Analyst note on the we.trade failure. https://futurumgroup.com/insights/hsbc-ibm-and-socgen-backed-blockchain-company-we-trade-is-now-we-broke/
54. Global Trade Review (GTR), 28 Apr 2020. State of trade finance blockchain consortia. https://www.gtreview.com/magazine/volume-18-issue-2/trade-finance-blockchain-consortia-now/
55. Silicon Republic, 17 Dec 2019. Accenture invests in TradeIX. https://www.siliconrepublic.com/business/accenture-tradeix-investment
56. Trade Finance Global, 23 Feb 2023. Marco Polo insolvency, debts, staff. https://www.tradefinanceglobal.com/posts/marco-polo-network-runs-insolvent/
57. Ledger Insights, 24 Feb 2023. Marco Polo insolvency and tax debt. https://www.ledgerinsights.com/marco-polo-blockchain-trade-finance-insolvency/
58. Global Trade Review (GTR), 25 Sep 2023. Kanexa emerges from Marco Polo. https://www.gtreview.com/news/top-stories/kanexa-rises-from-marco-polos-ashes-with-pivot-to-open-account-automation/
59. Global Trade Review (GTR), 25 Sep 2023. Bank of America uses Kanexa in CashPro. https://www.gtreview.com/news/digital-trade/bank-of-america-taps-kanexa-tech-to-tackle-open-account-trade-inefficiencies/
60. Global Trade Review (GTR), 5 Nov 2025. Leaders in Trade awards for 2024 results. https://www.gtreview.com/magazine/the-supply-chain-issue-2025/gtr-leaders-trade-2025-nominees-winners/
61. Global Trade Review (GTR), 23 Sep 2026. Leaders in Trade 2026 winner profiles. https://www.gtreview.com/magazine/gtr-issue-3-2026/gtr-leaders-in-trade-2026-the-winners-profiles/
62. Traydstream, 20 Aug 2018. US$3.5m funding round. https://traydstream.com/news/traydstream-successfully-closes-oversubscribed-funding-round-of-3-5-million
63. Nordic9, 25 May 2021. Traydstream US$8m round led by Spearhead Capital. https://nordic9.com/news/traydstream-to-get-8-million-in-a-round-led-by-spearhead-capital/
64. Global Trade Review (GTR), 27 Sep 2023. Traydstream US$21m Series B. https://www.gtreview.com/news/fintech/traydstream-raises-us21mn-in-latest-funding-round/
65. Global Trade Review (GTR), 27 Aug 2025. Traydstream US$11m round. https://www.gtreview.com/news/digital-trade/traydstream-raises-us11mn-in-latest-funding-round/
66. Tracxn, accessed 5 Oct 2026. Traydstream company profile. https://tracxn.com/d/companies/traydstream/__OEGFgfPoTwpYQzS6i2z4SgK9jB30dFprBwJpv5g7bDA
67. Traydstream, accessed 5 Oct 2026 (page undated). NeoVentures investment and platform metrics. https://traydstream.com/partners/neoventures
68. Trade Finance Global, 8 Dec 2023. Lessons from the Contour collapse, by R3 head of trade. https://www.tradefinanceglobal.com/posts/top-5-trade-lessons-from-the-contour-collapse/
69. Ledger Insights, 10 Oct 2022. Finastra to integrate Trade Innovation with Contour. https://www.ledgerinsights.com/finastra-to-integrate-its-trade-finance-platform-with-contours-blockchain/
70. Treasury Management International, 16 Mar 2023. Surecomp and Contour partnership. https://treasury-management.com/news/surecomp-and-contour-enter-strategic-partnership-to-accelerate-interoperability-between-digital-trade-finance-solutions
71. Global Trade Review (GTR), 20 Feb 2024. Xalts acquisition; former CEO on back-office integration. https://www.gtreview.com/news/top-stories/contour-is-back-xalts-announces-silicon-valley-inspired-acquisition/
72. PYMNTS, 30 Apr 2019. we.trade co-founder voices doubts. https://www.pymnts.com/news/b2b-payments/2019/wetrade-cofounder-quits-blockchain-doubt/
73. Finastra, accessed 5 Oct 2026. Trade Innovation Nexus product page. https://www.finastra.com/lending/solutions/trade-innovation-nexus
74. FinTech Global, 16 Sep 2026. Finastra and Komgo integration. https://fintech.global/2026/09/16/finastra-and-komgo-partner-to-streamline-digital-trade-finance/
75. Surecomp, 16 Apr 2024. Cleareye.ai integrates with RIVO. https://surecomp.com/news/surecomp-and-cleareye-ai-partner-to-enhance-ai-powered-trade-finance-automation/
76. Silicon Canals, 10 Jul 2025. Cape Investment Partners takes majority of Conpend. https://siliconcanals.com/conpend-secures-growth-funding/
77. Companies House, accessed 5 Oct 2026. Traydstream Limited filing history. https://find-and-update.company-information.service.gov.uk/company/10138819/filing-history
78. Contour Network, accessed 5 Oct 2026. Company website. https://www.contour.network/

## Fact-check notes

- Summary: "Contour shut in November 2023" changed to owners pulling funding in October 2023. Xalts bought the network and kept it running, so it never fully shut [9][45][71].
- Summary: "signed ... by plugging into the Finastra, CGI and Surecomp systems" overstated cause and effect. J.P. Morgan's integration was into its own processing system [42], and the Trade360 link was only announced [14]. Now reads "signed ... and built integrations with".
- Surecomp: "works in more than 80 countries" changed to "customers span more than 80 countries", matching the source's wording [20].
- Law: "the law tied title to one paper original" is not in [23]. Replaced with what the source says: rights pass by handing over the paper, and control of an electronic record does the same job.
- MLETR: dropped "Only" and added that some enactments cover only certain documents (China covers bills of lading only, Mauritius bills of exchange only) [25].
- eBL share: the denominator is now limited to DCSA members' container bills [27].
- Marco Polo: "set up" changed to "launched" (September 2017) [8]. Barnes changed from "founded" to "co-founded" [55].
- BCG: the 50% OCR productivity figure was Citibank's speculation, "as much as" and not "about". It is now attributed that way [21].
- D'Antoni: "no existing OCR could read trade paper" overstated his quote. He said none of a dozen products they reviewed fit [34].
- Marco Polo commitment: it is a promise to pay on the due date and relies on data matching. Payment is not due "once trade data matched" [6]. The LC-substitute claim is now attributed to what clients said, per TradeIX's Cotti [41].
- we.trade first run: added "over five days" [40].
- Traydstream pilots: "late 2017" changed to "the second half of 2017" (Q3 and Q4) [34].
- we.trade deployment: "only two shareholders" now adds "along with several smaller banks", as the source says [44].
- Contour small banks: the line about small banks not paying for nodes is the article's narrative, not a quote from Wegner. It is no longer attributed to him [45].
- J.P. Morgan: "by April 2023 mapped its output into the back office" changed to "in April 2023 agreed to map". The source describes an agreement, not finished work [22].
- Contour volume: "early 2023" changed to "2023". The source gives no month [10].
- Xalts deal: changed to "a deal announced in February 2024". DigFin says it closed in January [45].
- we.trade funding: "about €12m" changed to "close to €12m" [51]. "hundreds" changed to "many hundreds" [54].
- R3 quote: the source says paper is the most interoperable "instrument", not "format" [68].
- Contour back office: Finastra's product in 2022 was Fusion Trade Innovation [15][69]. Wegner's claim was specifically about one more year of funding [71].
- Mancone: reworded to match his quote about solutions providers value rather than users [72].
- Barnes quote corrected. The source says "no buy-in, so it was a commercial disaster", not "no commercial buy-in" [58].
- Bank of America: "partnership" changed to "deal". Sources variously call it an investment, an acquisition or a partnership [8][56][57].
- Komgo: "now plugs into Finastra's engine" was wrong. The September 2026 integration is planned, not live [74]. "2019-cohort" replaced with "the only network of that cohort still standing in 2023" [10].
- Traydstream and CGI: the Trade360 integration is now marked as announced and planned [14]. "Cleareye joined RIVO" changed to "partnered with RIVO" [75].
- Copy lesson 2: "Both overlays ship inside" changed to "have live or announced integrations with" [14].
- Cleareye metrics: "awards submission" changed to "awards profile". Added that the 2024 Finastra factsheet gives lower rates (extraction above 80%, classification 85%) [15].
- Style: the draft had no em dashes or banned hype words, so none were removed.