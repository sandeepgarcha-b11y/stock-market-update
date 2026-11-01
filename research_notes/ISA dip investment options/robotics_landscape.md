# Investable AI Robotics / Physical AI / Automation Landscape (as of 1 Nov 2026)

Research notes compiled 2026-11-01. Every figure is dated where the source gives a date. "STALE" marks data older than ~6 months or from 2025. Calculations marked "[calc]" are my own arithmetic from cited figures, not sourced numbers. Method note: WebFetch was blocked for several hosts in this session (thenextweb.com, caixinglobal.com, sec.gov, home.saxo), so many findings rely on search-result summaries of those pages rather than full-page reads; the most important numbers (ISRG, Teradyne, Symbotic, Hesai, Ouster, IFR, Agility S-4) were consistent across multiple results.

---

## 1. Pure-play and near-pure-play listed robotics companies: real businesses vs story stocks

### Takeaway
The listed "pure plays" split sharply: profitable, cash-generating incumbents (Intuitive Surgical, Fanuc, Yaskawa, Keyence, Symbotic, Unitree) sit alongside tiny-revenue, loss-making story stocks (Serve, Richtech, Doosan Robotics, and the soon-to-list Agility Robotics, valued at $2.5bn on $1.8m of 2025 revenue). The two most important 2026 listing events were Unitree's Shanghai STAR debut (Aug 19, 2026), which went from ~61bn yuan at IPO to a ~$48–66bn peak and then fell ~45% within a week, and Agility's SPAC with Churchill Capital XI (vote Nov 2, 2026; ticker AGLT). ABB's robotics division is being sold to SoftBank (not spun off), so ABB will no longer be a robotics play once the deal closes.

### Cited Findings

**Surgical robotics — Intuitive Surgical (NASDAQ: ISRG) — real, highly profitable business**
- Q3 2026 (quarter to Sep 30, 2026): revenue $3.05bn, +22% YoY from $2.51bn; da Vinci procedures ~906,000 (+14%); Ion procedures ~49,700 (+31%); instruments & accessories $1.80bn (+18%); systems revenue $769m (+30%) — [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001035267/000103526726000071/isrg-20260930.htm)
- Q3 2026: 546 da Vinci systems placed (315 da Vinci 5) vs 427 a year earlier; installed base ~12,094 (+12%) — [Intuitive release via BioSpace](https://www.biospace.com/press-releases/intuitive-announces-third-quarter-2026-earnings)
- Q3 2026 GAAP operating income fell to $593m from $760m due to a $450m pre-tax antitrust class-action settlement charge; non-GAAP operating income $1.27bn (vs $976m); non-GAAP EPS $3.00 (vs $2.40) — [Capital.com](https://capital.com/en-ae/news/intuitive-announces-third-quarter-earnings); [8-K release](https://www.sec.gov/Archives/edgar/data/0001035267/000103526726000067/q326ex-991earningsrelease.htm)
- 2026 non-GAAP gross margin guidance 68.7–69.3%, including ~0.9pt tariff impact — [BioSpace](https://www.biospace.com/press-releases/intuitive-announces-third-quarter-2026-earnings)

**Industrial robots / factory automation — Japan (real, profitable businesses)**
- Fanuc (TSE: 6954): April–June 2026 quarter (reported Jul 31, 2026) orders +36.9% YoY to ¥281.9bn, a single-quarter record; robot division orders +8.1%, FA (factory automation/CNC) division +63.8%; FY guidance raised — revenue ¥909.6bn → ¥948.1bn, net profit ¥184.9bn → ¥198.0bn — [TechNews (Taiwan), Aug 3, 2026](https://finance.technews.tw/2026/08/03/fanuc-raises-full-year-forecast/)
- Fanuc shares plunged on the day of those record results (reported as down as much as 16%), i.e. good news was already priced in — [TechNews, Aug 3, 2026](https://finance.technews.tw/2026/08/03/fanuc-raises-full-year-forecast/)
- Fanuc fiscal Q2 (Apr–Sep 2026) results were scheduled for Oct 23, 2026; a third-party summary reports orders +49.0% YoY with FA orders +130.1%, but the figure is garbled in the source and not verified against Fanuc's release — [2Slides summary](https://2slides.com/ar/gallery/fanuc-h1-fy2026-earnings-presentation) (UNVERIFIED)
- Yaskawa Electric (TSE: 6506): fiscal Q2 (reported ~Oct 9–12, 2026) orders a record, +38% YoY and +13% QoQ, driven by data-centre and semiconductor investment; H1 revenue +9.8% but operating profit −5.5% (ERP disruption, Europe restructuring) — [Quartr summary](https://quartr.com/events/yaskawa-electric-corporation-6506-q2-2027_FkEGQPLu); [TechNews, Oct 12, 2026](https://finance.technews.tw/2026/10/12/yaskawa-orders-hit-record-raises-profit-forecast/)
- Conflict on Yaskawa guidance: TechNews says profit and revenue forecasts were raised; Smartkarma (Oct 9, 2026) says FY operating income guidance was cut to ¥57.5bn from ¥60.0bn (in line with consensus ¥57.91bn) — [TechNews](https://finance.technews.tw/2026/10/12/yaskawa-orders-hit-record-raises-profit-forecast/); contradicted by [Smartkarma](https://www.smartkarma.com/home/?p=505174)
- Yaskawa Q1 FY2026 (Mar–May 2026): semiconductor-related robotics orders +141% YoY, +55% QoQ — [Yaskawa Q&A, Jul 2026](https://www.yaskawa-global.com/wp-content/uploads/2026/07/261Q_QA_EN.pdf)

**ABB (SIX: ABBN) — robotics division being sold, no longer a robotics play post-close**
- Oct 8, 2025: SoftBank Group agreed to buy 100% of ABB's robotics business for $5.375bn (≈¥818.7bn), subject to EU, China and US approvals; closing planned "mid-to-late 2026" — [SoftBank press release](https://group.softbank/en/news/press/20251008) (STALE, 2025)
- The sale replaced ABB's April 2025 plan to spin robotics off as a separately listed company in 2026; ABB expects ~$5.3bn net cash proceeds and a ~$2.4bn pre-tax book gain; robotics reported as discontinued operations from Q4 2025 — [Robotics 24/7](https://www.robotics247.com/article/abb_divests_robotics_division_to_softbank_group_for_5.375b/ABB_Group); [Financier Worldwide](https://www.financierworldwide.com/fw-news/2025/10/9/softbank-agrees-54bn-deal-for-abbs-robotics-division)
- I found no report confirming that the deal has closed as of Nov 1, 2026 (searches surfaced only announcement-era coverage) — see Gaps

**Teradyne (NASDAQ: TER) — owns Universal Robots and MiR; now mostly an AI semiconductor-test play**
- Q3 2026: revenue $1.306bn (+70% YoY, AI test demand); Robotics segment $96m, its highest Q3 ever and first-ever profitable quarter; non-GAAP EPS $2.29 vs $0.85; Q4 2026 guidance $1.25–1.35bn — [CryptoBriefing](https://cryptobriefing.com/teradyne-q3-revenue-ai-demand/); [Panabee](https://www.panabee.com/news/teradyne-earnings-q4-2026)
- [calc] Robotics = ~7% of Teradyne Q3 2026 revenue ($96m / $1,306m).

**Warehouse automation — Symbotic (NASDAQ: SYM) — real revenue, newly profitable, heavy customer concentration**
- Fiscal Q3 2026 (to Jun 27, 2026; reported Aug 5–6, 2026): revenue $721m (+22% YoY); GAAP net income $55m; adjusted EBITDA $95m (more than doubled); backlog $22.5bn (slightly down QoQ), excluding Walmart's 400-unit back-of-store contract; FQ4 guidance $760–780m — [Nasdaq/earnings call highlights](https://www.nasdaq.com/articles/symbotic-q3-earnings-call-highlights); [MarketBeat](https://www.marketbeat.com/instant-alerts/symbotic-q3-earnings-call-highlights-2026-08-06/)
- Walmart = 85% of fiscal 2025 sales; one (weak) source says shares were down ~27% YTD in 2026 — [simplify.jobs](https://simplify.jobs/c/Symbotic) (low-quality source; verify)
- Fiscal Q2 2026 revenue $676.5m (+23%) — [MarketScale](https://www.marketscale.com/industries/industrial-iot/symbotic-reports-second-quarter-fiscal-year-2026-results)

**US small-cap "story stocks" (tiny revenue, losses)**
- Serve Robotics (NASDAQ: SERV): Q1 2026 revenue ~$3.0m, EPS −$0.65 (vs −$0.51 est.), cash & securities $197.4m; Q2 2026 revenue $3.2m (+404% YoY, but only +9% QoQ); 2026 revenue guidance slashed to $9–10m from $26m because of lower-than-expected Uber volume — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/why-serve-robotics-serv-one-130606493.html); [QuiverQuant](https://www.quiverquant.com/news/Serve+Robotics+Q2+Revenue+Reaches+%243.2+Million+as+Fleet+Expands); [Nasdaq](https://www.nasdaq.com/articles/can-serve-robotics-turn-2000-robots-revenue-growth-engine)
- Richtech Robotics (NASDAQ: RR): Q1 2026 revenue $1.15m, 45% below $2.09m estimate; a financial restatement turned the quarter into "a credibility test"; strategy shifting to robots-as-a-service — [Barchart](https://www.barchart.com/story/news/3064289/richtech-robotics-financial-restatement-turns-what-should-be-a-breakout-quarter-into-a-credibility-test); Seeking Alpha author rates it Sell on valuation — [Seeking Alpha](https://seekingalpha.com/article/4817309-richtech-robotics-stock-some-progress-but-valuation-stretched-sell) (opinion)

**Agility Robotics (SPAC with Churchill Capital Corp XI, NASDAQ: CCXI → AGLT)**
- Pre-money equity value $2.5bn; >$620m gross proceeds expected (~$424m trust if no redemptions + ~$200m PIPE led by Foxconn); SEC declared S-4 effective Oct 13, 2026; CCXI shareholder vote Nov 2, 2026; closing expected Nov 2026 (Q4 2026); tickers AGLT / AGLTW — [SEC Form 425](https://www.sec.gov/Archives/edgar/data/0002074973/000121390026111470/ea0309365-425_churchill11.htm); [TechNews, Oct 14, 2026](https://finance.technews.tw/2026/10/14/humanoid-robot-agility-november-listing-sec-filing-effective/); [humanoid.guide](https://humanoid.guide/agility-robotics-spac-deal-would-take-digit-to-nasdaq/)
- From S-4 coverage: 2025 net sales ~$1.78m ($1.55m robot sales); 2025 net loss ~$138m; operating spend $111m (vs $71m in 2024); ~$100m cash burn in 2025; filing warns losses could grow — [The Robot Report](https://www.therobotreport.com/agility-robotics-reports-18m-revenue-ahead-of-humanoid-spac/); [GeekWire](https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/); [Mike Kalil](https://mikekalil.com/blog/agility-robotics-sec-filing/)
- Digit deployed/committed at nine customer facilities (GXO, Schaeffler, Toyota Motor Manufacturing Canada, Amazon, Mercado Libre); >$300m multi-year Digit v5 orders (1,000 robots, 3-yr RaaS), which the filing says "is not a measure of current period revenue" and is milestone-dependent — [GeekWire](https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/); [The Robot Report](https://www.therobotreport.com/agility-robotics-reports-18m-revenue-ahead-of-humanoid-spac/)
- [calc] $2.5bn pre-money / $1.78m 2025 revenue ≈ 1,400x trailing sales.

**China / Hong Kong**
- Unitree (Shanghai STAR Market, listed Aug 19, 2026): IPO priced at 150.80 yuan/share, ~61bn yuan issuance market cap (~$9bn), raising ~6.1bn yuan (~$904m); retail oversubscription >8,000x (STAR record) — [Gasgoo](https://autonews.gasgoo.com/articles/market-industry/unitree-ipo-priced-at-15080-yuan-per-share-corresponding-to-issuance-market-cap-of-nearly-61-billion-yuan-2085662758073761793); [Caixin, Aug 18, 2026](https://www.caixinglobal.com/2026-08-18/unitree-to-debut-at-61-billion-yuan-valuation-in-closely-watched-shanghai-ipo-102475173.html)
- Unitree opened at 1,100 yuan (+629%), briefly implying ~445bn yuan (~$66bn); closed day one up ~460% (~$50bn); ~6 days later it was ~45% below its peak (~$30bn wiped); closed below 600 yuan on Aug 26, 2026 — [Gasgoo](https://autonews.gasgoo.com/articles/market-industry/unitree-surges-629-at-open-one-lot-yields-up-to-470000-yuan-market-cap-exceeds-400-billion-yuan-2090018320131842049); [AI Weekly](https://aiweekly.co/node/10377); [The Next Web](https://thenextweb.com/news/unitree-shares-45-percent-slump-bubble-fears); [Caixin, Aug 28, 2026](https://www.caixinglobal.com/2026-08-28/analysis-unitree-shares-slide-as-investors-reassess-humanoid-robot-valuations-102478761.html)
- Unitree is a real, profitable business: 2025 revenue ~1.70bn yuan (1.699–1.708bn); net profit attributable ~278m yuan; profit ex-non-recurring items ~590–600m yuan (gap due to one-off share-based pay); core gross margin ~60% — [36Kr](https://eu.36kr.com/en/p/3825497010229890); [Gasgoo](https://autonews.gasgoo.com/articles/icv/unitree-wins-ipo-approval-as-robot-makers-face-tougher-profit-challenges-2061816669448765440)
- Unitree H1 2026 (less certain): reported revenue 1.152bn yuan (+48.5%), attributable net profit 274m yuan, deducted net profit 244m yuan (−19.3%) — i.e. growth with falling core profit; Q1 2026 revenue 423m yuan (+68.5%), adjusted profit −52.6% — [36Kr](https://eu.36kr.com/en/p/3945679641902464) (secondary; not checked against SSE filing)
- [calc] At the IPO valuation (61bn yuan): ~36x 2025 sales, ~219x 2025 attributable profit. At ~600 yuan/share (~243bn yuan, Aug 26): ~143x sales, ~870x attributable profit (~410x ex-non-recurring profit). Current (late-Oct) Unitree price not found.
- UBTech (HKEX: 9880): H1 2026 (reported Aug 28, 2026) full-size humanoid revenue RMB590.3m, +1,445% YoY, 46.5% of group revenue; total H1 revenue ~RMB1.27bn (+104%, aggregator figure) — [KR-Asia](https://kr-asia.com/ubtechs-full-size-humanoid-robot-revenue-jumps-1445-in-h1-2026); [Let's Data Science](https://letsdatascience.com/news/ubtech-reports-surge-in-humanoid-robot-revenue-d0622c64)
- UBTech Walker orders >RMB800m (~$112m) cumulative since early 2025 (as of Nov 2025, STALE); 2026 production target conflicting (5,000 vs 10,000 units); April 2026 $37m contract to deploy Walker S2 at Fangchenggang border crossing — [SCMP](https://www.scmp.com/tech/tech-trends/article/3332372/chinas-humanoid-robots-get-factory-jobs-ubtechs-model-scores-us112-million-orders); [Humanoids Daily](https://www.humanoidsdaily.com/companies/ubtech-robotics)
- Pipeline: AgiBot formally started its Hong Kong IPO process Jul 24, 2026 (sponsors CITIC, CICC, Morgan Stanley; earlier valuation target HK$40–50bn ≈ US$5.1–6.4bn); Galbot (raised $362m, Mar 2026) and X Square Robot have filed confidentially in HK; Leju and Deep Robotics reportedly filed in Shenzhen/Shanghai — [Caixin, Jul 24, 2026](https://caixinglobal.com/2026-07-24/agibot-begins-hong-kong-ipo-process-as-chinas-embodied-ai-startups-race-to-list-102467856.html); [TechNode](https://technode.com/2026/07/27/agibot-starts-hong-kong-ipo-process/); [SCMP](https://scmp.com/tech/tech-war/article/3363028/chinas-x-square-robot-submits-confidential-filing-hong-kong-ipo-sources-say); [Caixin, Mar 2026](https://www.caixinglobal.com/2026-03-03/galbot-raises-362-million-in-fresh-funding-eyes-hong-kong-ipo-102418742.html)
- Hong Kong H1 2026 IPO proceeds HK$210bn, +92% YoY (PwC) — [Binance Square citing PwC](https://www.binance.com/ar/square/post/347453077279553) (secondary)

**Korea**
- Doosan Robotics (KRX): has not posted a single quarter of operating profit since its 2023 IPO; Q1 2026 consolidated operating loss KRW12.069bn; humanoid partnership with Nvidia — [Daum / K-Humanoid Wars Pt 3](https://v.daum.net/v/20260303101555582); [edaily](https://en.edaily.co.kr/news/eda202608145748/)
- Rainbow Robotics (KRX): Samsung Electronics raised its stake from 14.7% to 35% (KRW267bn) to become largest shareholder (deal early 2025, STALE); humanoid commercialisation targeted for 2028; shares reportedly rose from ~KRW350k to ~KRW670k (+91%) over three months (date ambiguous) — [Nasdaq](https://www.nasdaq.com/articles/samsung-becomes-largest-shareholder-rainbow-robotics); [Daum / K-Humanoid Wars Pt 2](https://v.daum.net/v/UBBkbyV7CW?f=p)
- Foreign net buying of Korean stocks in 2026 led by Hyundai Motor (KRW324bn), then Doosan Robotics (KRW316bn) and Rainbow Robotics (KRW177bn) — [Seoulz](https://www.seoulz.com/korea-robotics-stocks-2026/) (period unclear)
- Hyundai Motor took 100% of Boston Dynamics (bought SoftBank's ~10% stake, ~$325m, announced Jul 16, 2026); a senior executive told Reuters an IPO is unlikely in 2027 because Atlas is not deployed at scale and the company is unprofitable; Meritz sees 2029–30 listing; Hyundai shares jumped 10% in a day in Jan 2026 on robot-IPO hopes — [Korea Times](https://www.koreatimes.co.kr/business/companies/20260716/hyundai-motor-group-to-take-full-ownership-of-boston-dynamics); [The Star/Reuters, Sep 14, 2026](https://www.thestar.com.my/tech/tech-news/2026/09/14/exclusive-ipo-for-humanoid-robot-maker-boston-dynamics-unlikely-in-2027-executive-says); [Asiae](https://view.asiae.co.kr/en/article/2026011317151875488)

### Inferences
- Rough classification (my judgement from the cited numbers):

| Company (listing) | Robotics purity | Business quality | UK retail access (general platform knowledge, not verified this session) |
|---|---|---|---|
| Intuitive Surgical (NASDAQ) | Very high (surgical robots) | Highly profitable, 22% growth | Easy (all major UK platforms) |
| Fanuc, Yaskawa (Tokyo) | High (robots + CNC/motion) | Profitable, record orders | Possible on platforms with Tokyo access (e.g. ii, IG, Saxo, IBKR); not all platforms; some via US OTC ADRs (FANUY, YASKY) |
| Keyence (Tokyo) | Medium (sensors/vision/automation) | Very profitable | As Fanuc |
| Symbotic (NASDAQ) | High (warehouse automation) | Newly GAAP-profitable; Walmart dependency | Easy |
| Teradyne (NASDAQ) | Low (~7% robotics) | Profitable; AI test driven | Easy |
| Unitree (Shanghai STAR) | Very high (humanoids/quadrupeds) | Profitable but extreme valuation | Effectively not accessible to UK retail (STAR shares via Stock Connect are generally restricted) |
| UBTech (HKEX) | Very high (humanoids) | Fast revenue growth; profitability not confirmed | Possible on platforms with HK access |
| Doosan Robotics, Rainbow Robotics (KRX) | Very high | Loss-making / early | Rarely available on UK retail platforms |
| Serve, Richtech (NASDAQ) | Very high | Story stocks: tiny revenue, losses, guidance cuts / restatement | Easy, but speculative |
| Agility (AGLT, from ~Nov 2026) | Very high (humanoid) | Story stock: $1.8m revenue, ~$100m burn | Will be US-listed, so likely accessible once listed |
| ABB (SIX) | Falling to ~zero after SoftBank sale | n/a | Accessible, but no longer a robotics play |
| Hyundai Motor (KRX; GDRs in London) | Low (Boston Dynamics inside a carmaker) | Profitable | GDRs possibly accessible |

- Unitree's IPO is the clearest evidence of humanoid froth in 2026: a profitable but small (~$240m revenue) company briefly valued at ~$50–66bn, then losing ~$30bn in a week.
- Japanese incumbents' 2026 order strength is being driven more by AI data-centre and semiconductor capex (Fanuc FA +63.8%, Yaskawa semis-related robotics +141%) than by humanoids or general factory robot demand (Fanuc robot orders only +8.1%).
- Agility's valuation relies almost entirely on the SPAC/humanoid narrative; SPAC history (Q6) suggests caution.

### Gaps
- Whether the ABB–SoftBank robotics deal has closed (expected mid-to-late 2026): no confirmation found.
- Fanuc's and Yaskawa's exact Oct 2026 quarterly figures from primary releases (only secondary summaries found; Fanuc Q2 figure garbled).
- UBTech's H1 2026 net profit/loss and current share price; Unitree's current (late-Oct 2026) share price.
- Richtech's Q2 2026 actual results; Serve's Q3 2026 results (not yet found).
- Harmonic Drive / Nabtesco / Hiwin 2026 results (see Q3) — not found.
- Other 2025–26 US robotics IPOs beyond Agility: I found no confirmed others in this research (Boston Dynamics IPO not before 2028 per Hyundai).

---

## 2. Big-tech / platform exposure and private players

### Takeaway
Big-tech exposure gives diluted robotics exposure: robotics is undisclosed or a tiny share of revenue at Nvidia, Alphabet and Amazon, and Tesla's Optimus has only just started early production, with outside deliveries not expected until around end-2027. The most-hyped humanoid/robot-AI developers (Figure AI ~$39bn, Physical Intelligence ~$5.6bn last round with talks at $11–20bn, 1X, Boston Dynamics) are private and not open to retail investors.

### Cited Findings

**Tesla (NASDAQ: TSLA) — Optimus**
- Q3 2026 call (Oct 21, 2026): Tesla has begun early Optimus production on a high-volume line in Fremont (in space freed by Model S/X); Q3 deck calls these the first production-quality bots; Musk said deliveries to outside companies are expected around end-2027 ("I do expect these issues to be solved around the end of next year") — [Nasdaq](https://www.nasdaq.com/articles/tesla-optimus-humanoid-robot-key-takeaways-q3-earnings-call); [Not a Tesla App](https://notateslaapp.com/news/4866/tesla-officially-begins-optimus-robot-production)
- Ramp to 20,000 units/week expected to take at least a year; one source cites ~1m units/yr line capacity; AI5 chip targeted for Optimus around April 2027; no price, named external customer or production volume disclosed — [Tech-Insider](https://tech-insider.org/tesla-optimus-sales-2027-20000-week-target-2026/); [TechRepublic](https://www.techrepublic.com/article/news-tesla-optimus-robot-launch-timeline/) (secondary; I could not check the primary transcript)
- Tesla forward P/E ~157.7 as of Sep 21, 2026 — [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/TSLA); other providers give very different numbers (e.g. 192x forward in June 2026; 413x on Aug 6, 2026) depending on earnings basis — [24/7 Wall St](https://247wallst.com/investing/2026/06/25/tesla-stock-price-prediction-why-the-ev-maker-is-sitting-right-at-fair-value/); [Eulerpool](https://eulerpool.com/stock/Tesla-Stock-US88160R1014/forwardpe)

**Nvidia (NASDAQ: NVDA) — Isaac / GR00T / Jetson Thor**
- Q2 FY2027 (quarter to Jul 26, 2026; reported Aug 26, 2026): revenue $96.2bn, +106% YoY, +18% QoQ — [StockTitan (NVDA release)](https://www.stocktitan.net/news/NVDA/nvidia-announces-financial-results-for-second-quarter-fiscal-98x41cxh35vk.html)
- From FY2027 Nvidia reports two platforms, Data Center and Edge Computing; Edge Computing (which absorbs gaming, pro visualisation, automotive/robotics and OEM) was $7.2bn in Q2 FY27, +27% from ~$5.7bn; robotics revenue is no longer separately disclosed — [Sci-Tech Today](https://www.sci-tech-today.com/news/nvidia-q2-fiscal-2027-earnings/); [Rex Shares](https://www.rexshares.com/nvidia-earnings/)
- Last separate figure: Automotive revenue $604m in Q4 FY2026 (+6% YoY) — [Nvidia 8-K Q4 FY26](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm); automotive & robotics was ~1% of sales in Q1 FY2026 ($567m) — [Nasdaq/Zacks](https://www.nasdaq.com/articles/robotics-demand-rises-will-jetson-thor-unlock-new-market-nvda) (STALE, 2025)
- Jetson Thor (launched Aug 2025): 7.5x prior-generation performance; developer kit $3,499; T5000 module $2,999 at 1,000+ units — [Sherwood](https://www.sherwood.news/markets/nvidia-rallies-after-launching-jetson-thor-robot-brain/) (STALE, 2025)
- [calc] Edge Computing = ~7.5% of Q2 FY27 revenue; robotics is a fraction of that, so Nvidia is overwhelmingly a data-centre AI play with a robotics option.

**Alphabet (NASDAQ: GOOGL) — Intrinsic, DeepMind**
- Feb 25, 2026: Alphabet moved robotics-software unit Intrinsic under Google; it remains a separate entity but collaborates with Google DeepMind and uses Gemini models and Google Cloud — [TechCrunch](https://techcrunch.com/2026/02/25/alphabet-owned-robotics-software-company-intrinsic-joins-google); [Dataconomy](https://dataconomy.com/2026/02/26/alphabets-intrinsic-joins-google-to-accelerate-physical-ai)
- Jul 30, 2026: DeepMind reportedly released Gemini Robotics 2 (vision-language-action model), Gemini Robotics ER 2 and an On-Device 2 variant — [Seeking Alpha](https://seekingalpha.com/news/4574852-googles-deepmind-launches-more-advanced-gemini-robotics) (details from weaker mirror sites; verify); April 2026: Gemini Robotics-ER 1.6 opened to developers via Gemini API — same coverage

**Amazon (NASDAQ: AMZN) — warehouse robotics**
- 2026 shareholder letter: >1m robots in fulfilment centres; DeepFleet AI improved fleet travel time by 10%; Jassy floated selling robotics products to outside customers; Amazon acquired humanoid maker Fauna Robotics and doorstep-delivery robot firm Rivr — [SupplyChain247](https://www.supplychain247.com/article/amazon-ai-robotics-delivery-strategy-2026)

**Hyundai / SoftBank / Samsung (indirect)**
- Hyundai owns 100% of Boston Dynamics since Jul 2026; SoftBank sold its BD stake while buying ABB Robotics; Samsung owns 35% of Rainbow Robotics — see Q1 citations ([Korea Times](https://www.koreatimes.co.kr/business/companies/20260716/hyundai-motor-group-to-take-full-ownership-of-boston-dynamics); [SoftBank](https://group.softbank/en/news/press/20251008); [Nasdaq](https://www.nasdaq.com/articles/samsung-becomes-largest-shareholder-rainbow-robotics))

**Private players (not accessible to UK retail)**
- Figure AI: last priced round Series C >$1bn at $39bn post-money (Sep 2025, STALE); no 2026 primary round found; Forge secondary price $174/share (Aug 13, 2026) and DeFi Llama ~$35.1bn suggest secondary marks below $39bn; >350 Figure 03 units produced by Apr 29, 2026; whether it has external paying customers is disputed (BMW Spartanburg; reportedly UPS); no revenue disclosed — [Seeking Alpha](https://seekingalpha.com/news/4495255-figure-raises-1b-in-series-c-hits-39b-valuation-to-scale-humanoid-robot-deployment); [DeFi Llama](https://defillama.com/pre-ipo/figure-ai); [AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/17/figure-ai-700m-strategic-capital-humanoid-divergence-agility); [Axis Intelligence](https://axis-intelligence.com/figure-ai-statistics/) (aggregators)
- One source claims a Figure "$40bn round in Feb 2026" — [TechStackIPO](https://www.techstackipo.com/robotics-pre-ipo-stack-2026); not corroborated elsewhere (conflict)
- Physical Intelligence: last closed round $600m at $5.6bn (late 2025); Bloomberg (Mar 2026) reported talks to raise ~$1bn at >$11bn; one Oct 2026 item reports talks at ~$20bn (single source, unconfirmed) — [Bloomberg Law](https://news.bloomberglaw.com/artificial-intelligence/ai-robotics-lab-in-talks-to-nab-1-billion-at-11-billion-value); [St-Hakky](https://book.st-hakky.com/en/news/physical-intelligence-funding-talks-20-billion)
- 1X Technologies: confirmed funding ~$125m through Jan 2024 Series B ($820m valuation); a ~$1bn raise at $10bn+ is rumoured, not confirmed — [ValueAddVC](https://valueaddvc.com/blog/robotics-startups-2026-figure-physical-intelligence-1x-who-has-the-real-lead) (aggregator)
- Boston Dynamics value estimates range from >$20bn (JoongAng Daily) to >$70bn (one analyst projection) — [Korea JoongAng Daily](https://www.koreajoongangdaily.com/business/boston-dynamics-market-value-likely-exceeds-20-billion-due-to-atlas-robot/12010735); [Daum](https://v.daum.net/v/20260220102951476)
- Humanoid/physical-AI venture funding reportedly $13.2bn in first nine months of 2026 (~1.5x 2024 and 2025 combined) — [NewMarketPitch](https://newmarketpitch.com/products/humanoid-robotics-funding-valuations-report) (promotional source; treat with caution)

### Inferences
- For a retail investor, "big-tech robotics" is a call option inside mega-caps whose valuations depend on other businesses (data-centre GPUs, cloud/ads, e-commerce, EVs/autonomy). Tesla is the only mega-cap where robotics hopes plausibly drive a big part of the valuation (forward P/E ~158x in Sep 2026), but Optimus revenue is at least ~1 year away on management's own (historically optimistic) timetable.
- The "purest" Western humanoid exposure (Figure, Physical Intelligence, 1X, Boston Dynamics, Apptronik) is private; the first listed US humanoid will probably be Agility (AGLT), which makes it likely to trade on scarcity rather than fundamentals.
- Indirect access routes to private names exist through listed backers (e.g. Hyundai → Boston Dynamics; Foxconn → Agility PIPE; Samsung → Rainbow; SoftBank → ABB Robotics), but each is a tiny fraction of the parent's value.

### Gaps
- Meta's robotics effort, Microsoft and OpenAI robotics bets (e.g. OpenAI's investments in Figure/1X/Physical Intelligence): not researched within the tool budget.
- Nvidia does not break out robotics revenue in FY2027; no hard robotics figure exists.
- Amazon's robotics capex/savings figures for 2026 and Alphabet's robotics revenue: not disclosed or not found.
- Figure/1X/Physical Intelligence cash burn: not disclosed.

---

## 3. Picks-and-shovels suppliers: which have the most robotics-specific exposure?

### Takeaway
Among suppliers, the most robotics-sensitive listed names found are Japanese precision-motion makers (Harmonic Drive Systems, Nabtesco) and lidar makers (Hesai, whose robotics lidar shipments rose 193% in Q2 2026 to ~23% of units; Ouster), along with Keyence for sensors/vision. Edge-AI chips (Nvidia, Qualcomm, AMD, Arm) and broad industrial automation groups (Siemens, Rockwell, Schneider) carry real but diluted robotics exposure. Humanoid-component stocks have already re-rated sharply (Ouster +150% YTD, VPG +269% as of Jul 2026).

### Cited Findings
- Harmonic Drive Systems (TSE: 6324): booked ~¥1.3bn humanoid-related orders in fiscal Q2 (Jul–Sep 2025) and expected ~¥2.5bn for FY to Mar 2026; >15 potential humanoid customers; shares jumped on the outlook (Nov 2025, STALE) — [Investing.com](https://www.investing.com/news/stock-market-news/this-japanese-stock-is-surging-on-positive-outlook-for-humanoid-robot-orders-4367329)
- One estimate: Tesla Optimus uses 14 harmonic-drive joints per unit; risks include auto-customer dependence (incl. Nissan) and cheaper Chinese reducers — [Simply Wall St](https://simplywall.st/stocks/jp/capital-goods/tse-6324/harmonic-drive-systems-shares/news/humanoid-robotics-momentum-might-change-the-case-for-investi); [Finimize](https://finimize.com/content/humanoids-are-coming-and-this-overlooked-stock-could-be-their-nvidia) (opinion)
- Nabtesco (TSE: 6268): plans to double RV-reducer capacity by 2026; sells worm-gear drives/actuators for humanoid shoulders, elbows, hips, legs — [Jared Watkins research](https://www.jaredwatkins.com/research/robotics/actuators/nabtesco/); [Industrial Production](https://www.industrial-production.de/drive-technology/drive-technology-for-humanoid-robots--nabtesco-offers-shaft-gears-and-actuators-for-robot-joints.htm)
- Hesai Group (NASDAQ: HSAI; also HKEX-listed): Q2 2026 revenue RMB860.8m (US$126.9m), +21.9%; total lidar shipments 628,275; robotics lidar 142,371 units, +193.4% YoY (≈23% of shipments vs ~14% a year earlier); gross margin 40.1%; net income RMB70.6m (5th straight GAAP-profitable quarter); new robotic actuation/"Kosmo" segment first revenue, 2026 guidance RMB200–300m; Q3 2026 revenue guidance RMB1.1–1.15bn — [Hesai Q2 2026 release](https://hesai.gcs-web.com/news-releases/news-release-details/hesai-group-reports-second-quarter-2026-unaudited-financial); [Pulse 2.0](https://pulse2.com/hesai-robotics-lidar-shipments-jump-193-as-total-lidar-volume-rises-78/); [MarketBeat](https://www.marketbeat.com/instant-alerts/hesai-group-q2-earnings-call-highlights-2026-08-18/)
- Ouster (NYSE: OUST): Q2 2026 revenue $55m (+56% YoY, +12% QoQ); >17,000 sensors shipped; GAAP net loss $18m; Q3 2026 guidance $54.5–57.5m; growth driven by smart infrastructure and industrial (robotics not broken out) — [Ouster 8-K](https://www.sec.gov/Archives/edgar/data/0001816581/000162828026054297/exhibit991-6302026.htm); [CMC Markets Opto](https://www.cmcmarkets.com/en-au/opto/lidar-sector-roundup-ousters-physical-ai-bet)
- As of Jul 2, 2026: Ouster +150% YTD; Vishay Precision Group (VPG) +269% after booking humanoid orders — [24/7 Wall St](https://www.247wallst.com/investing/2026/07/02/the-first-major-robotics-ipo-is-here-5-robotics-stocks-that-could-run-in-the-second-half-of-2026/)
- Keyence (TSE: 6861): up ~44% since Jan 1 as of Sep 30, 2026 (US OTC line, $519.32); Daiwa upgraded to Outperform, target ¥95,000; on Jun 1, 2026 ValueInvesting.io put price ¥80,110 vs a P/E-based "fair value" ~¥45,209 (model opinion) — [MarketScreener](https://uk.marketscreener.com/quote/stock/KEYENCE-CORPORATION-120789230/valuation/); [ValueInvesting.io](https://www.valueinvesting.io/6861.T/valuation/pe-multiples)
- Fanuc's FA/CNC and Yaskawa's motion/robot orders are being pulled by AI data-centre and semiconductor capex (see Q1) — [TechNews](https://finance.technews.tw/2026/08/03/fanuc-raises-full-year-forecast/); [Quartr](https://quartr.com/events/yaskawa-electric-corporation-6506-q2-2027_FkEGQPLu)
- Nvidia Jetson Thor / Edge Computing segment (see Q2) — [Sci-Tech Today](https://www.sci-tech-today.com/news/nvidia-q2-fiscal-2027-earnings/)
- Morgan Stanley has published "humanoid supply chain leaders" lists, and Goldman initiated Sanhua (HK: 2050) at Buy on humanoid actuator exposure — [humanoid.guide](https://humanoid.guide/?p=11501); [Tiger Brokers](https://www-web.itiger.com/news/1134377125) (details not fetched)

### Inferences
- Robotics-specific exposure ranking (my judgement): Harmonic Drive ≈ Nabtesco (reducers are core robot-joint components) > Hesai (robotics ~23% of lidar units and rising, plus actuator push) > Ouster > Keyence/Cognex (machine vision serves broad factory automation) > Fanuc/Yaskawa CNC/motion > THK/NSK/Timken/Regal Rexnord (bearings/linear motion, mostly general industrial) > Siemens/Rockwell/Schneider (automation software/drives, robotics a small slice) > Nvidia/Qualcomm/AMD/Arm (edge AI is a small share of revenue).
- Supplier stocks with humanoid narratives (Ouster, VPG, Harmonic Drive) can move far more than their humanoid revenue justifies; Harmonic Drive's ~¥2.5bn humanoid orders are small relative to company revenue (Harmonic Drive's total revenue not found in this research).
- Chinese component makers (Sanhua, Leaderdrive and others) are a price-deflation threat to Japanese reducer makers (see Q6).

### Gaps
- No 2026 results or share-price data found for Harmonic Drive, Nabtesco, Hiwin, THK, NSK, Timken, Regal Rexnord, Cognex, Sony (sensors), Siemens, Rockwell, Schneider, Qualcomm, AMD, Arm robotics revenue — not researched within tool budget.
- Hesai's share-price reaction and current valuation not found.

---

## 4. Valuations and 2026 YTD share-price performance; signs of froth (incl. ETFs and UK access)

### Takeaway
Performance in 2026 has split. Humanoid/"physical AI" baskets and suppliers rallied (KOID humanoid ETF +22% YTD by Aug 10; Keyence +44% YTD by Sep 30; Ouster +150% YTD by Jul 2), while quality incumbents lagged (Intuitive Surgical reportedly down roughly 10–35% in 2026, depending on date; Symbotic reportedly −27%; BOTZ −6.6% YTD to Jul 24). Valuation froth is concentrated in humanoid names: Unitree at roughly 140x trailing sales after its post-IPO fall, Agility at ~1,400x trailing sales, Tesla at ~158x forward earnings, and Fanuc at ~40x P/E. UK investors can get the theme most easily through LSE-listed UCITS ETFs (iShares RBOT, L&G ROBO, Global X BOTZ UCITS, KraneShares humanoid UCITS).

### Cited Findings

**Single-stock valuation/performance datapoints (dates vary; providers disagree)**
- Tesla forward P/E 157.7 (Sep 21, 2026) — [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/TSLA)
- Fanuc P/E ~40x, labelled "overvalued" (Simply Wall St, ~Aug 2026); ¥8,036 on May 14, 2026; +39% over 365 days to an undated ¥6,035 close; consensus target ¥7,291 — [Webull/Simply Wall St](https://www.webull.com/news/15327782679225344); [Fintel](https://fintel.io/s/jp/6954); [Stockopedia](https://www.stockopedia.com/share-prices/fanuc-TYO:6954/) (dates inconsistent; verify)
- Keyence +44.25% since Jan 1 (Sep 30, 2026, OTC USD) — [MarketScreener](https://uk.marketscreener.com/quote/stock/KEYENCE-CORPORATION-120789230/valuation/)
- Intuitive Surgical: headlines say "Down 24% in 2026", "falling 29% year to date" and "Down 35% in 2026" at different (undated) points; another snapshot shows −10.7% YTD at $407.17; shares rose two days in a row after Q3 results (Oct 23, 2026) — [TIKR](https://www.tikr.com/blog/isrg-down-20-from-its-peak-is-intuitive-surgical-nasdaq-stock-a-buy-at-current-levels); [TIKR](https://www.tikr.com/blog/is-intuitive-surgical-stock-a-buy-now-after-falling-29-year-to-date); [TIKR](https://www.tikr.com/blog/intuitive-surgical-isrg-stock-valuation-2028-forecast) (conflicting; precise YTD not established)
- Symbotic ~−27% YTD (2026) — [simplify.jobs](https://simplify.jobs/c/Symbotic) (weak source)
- Ouster +150% YTD; VPG +269% (Jul 2, 2026) — [24/7 Wall St](https://www.247wallst.com/investing/2026/07/02/the-first-major-robotics-ipo-is-here-5-robotics-stocks-that-could-run-in-the-second-half-of-2026/)
- Unitree: IPO 61bn yuan → day-one close ~$50bn → ~45% off peak within six days; below 600 yuan by Aug 26 — [The Next Web](https://thenextweb.com/news/unitree-shares-45-percent-slump-bubble-fears); [Caixin](https://www.caixinglobal.com/2026-08-28/analysis-unitree-shares-slide-as-investors-reassess-humanoid-robot-valuations-102478761.html)
- Fund managers quoted by Reuters blamed the STAR pricing system (tiny float, retail frenzy) rather than the robots for Unitree's swing — [The Next Web](https://thenextweb.com/news/unitree-shares-45-percent-slump-bubble-fears) (via search summary)
- Barchart: many robotics companies carry high valuations with little or no earnings; humanoid "valuations" in private markets are preferred-share prices with liquidation preferences, not market-clearing prices — [Barchart](https://www.barchart.com/story/news/3636345/3-humanoid-robot-etfs-to-ride-a-speculative-trend) (opinion)

**ETF performance (2026 YTD snapshots, different dates)**
- KraneShares Global Humanoid & Embodied Intelligence ETF (KOID): +22.11% YTD (Aug 10, 2026); +28.32% YTD (Jun 12, 2026); reportedly $6.3bn fund — [24/7 Wall St, Aug 10, 2026](https://247wallst.com/investing/2026/08/10/the-robot-etf-actually-exists-now-tesla-hyundai-and-the-companies-building-the-joints/); [ETF Central](https://www.etfcentral.com/compare-etfs/BOTZ-vs-KOID) (AUM figure unverified)
- Global X Robotics & AI (BOTZ): −6.6% 2026 YTD total return to Jul 24, 2026 (ChartRow) vs "+13% YTD" in a May 28 article — [ChartRow](https://chartrow.com/quote/botz/returns); [24/7 Wall St, May 28, 2026](https://247wallst.com/investing/2026/05/28/three-humanoid-robotics-etfs-built-for-the-tesla-optimus-and-figure-ai-era-most-investors-have-never-heard-of/) (conflict; latest is negative)
- ROBO Global Robotics & Automation (ROBO, US): +19.31% YTD (Jun 12, 2026) — [ETF Central](https://www.etfcentral.com/compare-etfs/ROBO-vs-KOID)

**UK-accessible fund vehicles (UCITS, LSE-listed)**
- Saxo UK (Aug 19, 2026) says UK retail investors should generally use UCITS funds rather than US-listed ETFs; it lists iShares Automation & Robotics UCITS (RBOT) as a broad core holding, plus Global X Robotics & AI (BOTZ UCITS), WisdomTree AI (WTAI), Amundi MSCI Robotics & AI ESG Screened (GOAI) — [Saxo UK](https://www.home.saxo/en-gb/content/articles/etfs/robot-investing-19082026) (via search summary)
- L&G ROBO Global Robotics & Automation UCITS ETF (LSE: ROBG/ROBO): TER 0.80%; AUM ~€931m (MarketScreener); available on Hargreaves Lansdown — [HL](https://www.hl.co.uk/shares/shares-search-results/l/l-and-g-robo-global-robotics-and-automation-ucits/company-information); [MarketScreener](https://www.marketscreener.com/quote/etf/L-G-ROBO-GLOBAL-ROBOTICS--18387427/news/)
- KraneShares launched a humanoid-robotics UCITS ETF on the LSE (MerQube Global Humanoid & Embodied Intelligence Index; ISIN IE000O6Z73N7 quoted Oct 2026), with a humanoid robot ringing the opening bell — [Humanoid Robotics Technology](https://humanoidroboticstechnology.com/industry-news/koid-etf-debuts-at-lse-with-first-ever-humanoid-robot-bell-ringing-led-by-kraneshares/); [finanzen.at](https://www.finanzen.at/etf/kraneshares-global-humanoid-robotics-and-physical-ai-index-etf-ie000o6z73n7); [Structured Retail Products](https://www.structuredretailproducts.com/insights/81438/kranes-robotics-ai-focused-etf-goes-live-on-lse)
- Deutsche Börse listed new humanoid/robotics ETPs on Feb 18, 2026 — [Deutsche Börse](https://cashmarket.deutsche-boerse.com/cash-en/Stay-Informed/newsroom/press-releases/New-ETF-and-ETP-Listings-on-February-18-2026-on-Deutsche-B-rse-4958202)

### Inferences
- [calc] Valuation snapshots: Unitree ~36x 2025 sales at IPO and ~143x at 600 yuan; Agility ~1,400x 2025 sales at the SPAC price. Both are far above profitable incumbents: Fanuc ~40x P/E is rich for a cyclical, but in a different league from the humanoid names.
- Pattern: the market in 2026 rewarded humanoid narrative exposure (KOID, Ouster, Keyence, Korean robot names) and punished incumbents with near-term issues (ISRG litigation/procedure-growth worries, Symbotic customer concentration, Fanuc "sell the news"). This rotation is typical of a thematic hype phase.
- UK ISA practicality (general platform knowledge, not verified this session): US-listed single stocks (ISRG, TSLA, NVDA, TER, SYM, SERV, RR, OUST, HSAI ADR, and AGLT once listed) are ISA-eligible and available on most major UK platforms. US-domiciled ETFs (BOTZ, ROBO, KOID US) are generally not available to UK retail because of PRIIPs/KID rules, so UCITS versions are the route. Tokyo-listed names are available on some platforms (ii, IG, Saxo, IBKR), not all. HK (UBTech) is available on fewer platforms, KRX names rarely, and Shanghai STAR (Unitree) is effectively inaccessible. Private companies (Figure, PI, 1X, Boston Dynamics) are not accessible.

### Gaps
- No reliable, consistently dated forward P/E / EV/sales table for ISRG, Fanuc, Yaskawa, Keyence, Teradyne, Symbotic, Nvidia as of late Oct 2026; providers conflict and full pages could not be fetched.
- Precise 2026 YTD returns to end-Oct for most single names and for UCITS robotics ETFs (RBOT, ROBG, KraneShares UCITS) not found.
- Yaskawa 2026 share-price performance not found.
- Current (late-Oct) Unitree price/market cap not found.

---

## 5. Market size forecasts and realistic adoption timelines

### Takeaway
The industrial-robot market is large, real and growing modestly: IFR counted a record 603,307 installations in 2025 (+11%), with an installed base of ~5m and a forecast of only ~7% CAGR to 806k units in 2029; China accounts for 59%. Humanoids are still tiny (~15–20k units shipped globally in 2025; 50–75k forecast for 2026), but sell-side forecasts keep being raised: Goldman now sees 6.5m units/yr by 2035 (~$138bn); Morgan Stanley sees $28bn globally by 2030 and multi-trillion by 2050. Real scale for humanoids is a 2030s story; 2026–28 is pilot/early-deployment.

### Cited Findings
- IFR World Robotics 2026 (released Sep 24, 2026): 603,307 industrial robots installed in 2025 (+11%, record); operational stock ~5m (+9%); forecast 655,000 installations in 2026 and 806,000 in 2029 (7% CAGR 2026–29) — [IFR Executive Summary WR 2026](https://ifr.org/img/worldrobotics/Executive_Summary_WR_2026_-_Industrial_Robots.pdf); [Robotics Tomorrow](https://www.roboticstomorrow.com/news/2026/09/24/five-million-robots-now-operate-in-factories-globally/27154/)
- IFR: China 354,000 units (≈59% of global); Americas +14% to 57,044 (record); US ~38,000 (+11%, preliminary); Germany 24,800 (−8%), ~41% of EU total; handling/machine tending 59% of new deployments; cobots ~11% of installations — [IFR China press release](https://ifr.org/downloads/press_docs/EN-2026-SEP-24-IFR_Press_Release_WR-CHINA.pdf); [IFR EU release](https://ifr.org/downloads/press_docs/EN-2026-SEP-14-IFR_Press_Release_WR-EU-27.pdf); [Australian Manufacturing](https://www.australianmanufacturing.com.au/industrial-robot-installations-rise-11-as-global-stock-hits-5-million-report/)
- Goldman Sachs (Sep 2026): 2035 global humanoid shipments raised to ~6.48m units from 1.38m; market value raised from ~$38bn to ~$138bn; near-term assumptions 75,000 units in 2026 and 890,000 in 2030 — [24/7 Wall St, Sep 13, 2026](https://247wallst.com/investing/2026/09/13/robots-everywhere-goldman-sachs-now-sees-6-5-million-humanoid-robots-by-2035/); [humanoid.guide](https://humanoid.guide/goldman-raises-2035-humanoid-robot-forecast-to-6-5-million/) (secondary coverage of GS research)
- Goldman (Jan 2026): 2025 global humanoid shipments ~15,000–20,000 units, majority from Chinese manufacturers — [Tiger Brokers](https://www-web.itiger.com/news/1134377125)
- Morgan Stanley (Jun 2026): China 2026 humanoid shipments raised to 50,000 (second doubling in 2026: 14k → 28k → 50k); China humanoid market $2bn in 2026, $15bn by 2030, 446,000 units/yr by 2030 (external sales only); global market ~$3bn (2025) → $28bn (2030) — [AI Weekly](https://aiweekly.co/alerts/morgan-stanley-doubles-china-humanoid-robot-forecast-to-50000); [The Next Web, Jun 24, 2026](https://thenextweb.com/news/china-humanoid-robot-forecast-morgan-stanley-50000); [ForkLog](https://forklog.com/en/morgan-stanley-raises-forecast-for-chinese-humanoid-robot-shipments/)
- Morgan Stanley 2050 long-run figure reported inconsistently: $4.7trn annual humanoid hardware revenue vs $7.5trn annual market revenue (or ~$5trn) — [humanoid.guide](https://humanoid.guide/?p=3205); [MEXC](https://www.mexc.com/news/1171580) (conflicting secondary reports)
- Unitree's own revenue (~1.7bn yuan in 2025) and UBTech's H1 2026 humanoid revenue (RMB590m) give a sense of the real current market size — see Q1 citations
- Timeline datapoints: Tesla external Optimus deliveries ~end-2027 ([Nasdaq](https://www.nasdaq.com/articles/tesla-optimus-humanoid-robot-key-takeaways-q3-earnings-call)); Rainbow Robotics humanoid commercialisation 2028 ([Daum](https://v.daum.net/v/UBBkbyV7CW?f=p)); Boston Dynamics Atlas not deployed at scale, IPO not before 2028 ([The Star/Reuters](https://www.thestar.com.my/tech/tech-news/2026/09/14/exclusive-ipo-for-humanoid-robot-maker-boston-dynamics-unlikely-in-2027-executive-says)); Caixin calls 2026 "the first year of large-scale humanoid deployment" in China ([Caixin, Jun 15, 2026](https://www.caixinglobal.com/2026-06-15/in-depth-chinas-humanoid-robot-boom-sparks-fears-of-bruising-price-wars-102454393.html))

### Inferences
- [calc] Goldman's 2035 value (~$138bn) over 6.48m units implies an average selling price of roughly $21k per humanoid, which assumes steep cost declines, a deflationary dynamic that favours scale producers (largely Chinese) over margins.
- Banks have raised forecasts repeatedly within months (MS tripled its China 2026 number; GS nearly 5x'd its 2035 units). Rapid upward revisions are typical of hype phases and should be treated as sentiment indicators as much as analysis.
- Even on bullish numbers, the humanoid market in 2026 (~$2–3bn) is a fraction of the industrial-robot and automation markets; for the next 3–5 years, revenue in listed "robotics" companies will come mostly from industrial/surgical/warehouse automation, not humanoids.

### Gaps
- IFR service-robot (professional service robots) 2026 statistics not retrieved.
- IFR's 2025 industrial-robot market value (US$) not retrieved.
- Primary Goldman/MS reports not accessible; figures are from secondary coverage.

---

## 6. Bull and bear arguments for the theme

### Takeaway
Bull case: record industrial robot installations and orders (driven by AI/semiconductor capex), profitable leaders (ISRG, Fanuc, Unitree), fast humanoid revenue growth from small bases (UBTech +1,445%), maturing AI "robot brains" (Nvidia Thor, Gemini Robotics 2) and sell-side forecasts that keep rising. Bear case: classic thematic hype signs (8,000x IPO oversubscription, a 45% post-IPO crash, ~1,400x-sales SPAC), Chinese overcapacity and price wars (150+ humanoid firms; official bubble warning), cash-burning startups, a poor SPAC track record, guidance cuts and restatements at small caps, slipping timelines (Tesla, Boston Dynamics), and tariff/geopolitical risk (though the Oct 28, 2026 Section 232 decision imposed no tariffs for now).

### Cited Findings

**Bull points**
- Record IFR installations (603,307 in 2025), installed base ~5m, forecast growth to 806k by 2029 — [IFR](https://ifr.org/img/worldrobotics/Executive_Summary_WR_2026_-_Industrial_Robots.pdf)
- Record orders at Fanuc (Apr–Jun 2026, +36.9%) and Yaskawa (fiscal Q2, Jun–Aug 2026, reported Oct 2026, +38%) on AI/semis/data-centre demand — [TechNews](https://finance.technews.tw/2026/08/03/fanuc-raises-full-year-forecast/); [Quartr](https://quartr.com/events/yaskawa-electric-corporation-6506-q2-2027_FkEGQPLu)
- Surgical robotics compounding: ISRG Q3 2026 revenue +22%, procedures +14–15% — [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001035267/000103526726000071/isrg-20260930.htm)
- Humanoid revenue becoming real in China: UBTech H1 2026 humanoid revenue RMB590m (+1,445%); Unitree profitable, ~60% gross margin — [KR-Asia](https://kr-asia.com/ubtechs-full-size-humanoid-robot-revenue-jumps-1445-in-h1-2026); [36Kr](https://eu.36kr.com/en/p/3825497010229890)
- Component demand inflecting: Hesai robotics lidar +193%; Teradyne Robotics first profitable quarter — [Hesai](https://hesai.gcs-web.com/news-releases/news-release-details/hesai-group-reports-second-quarter-2026-unaudited-financial); [CryptoBriefing](https://cryptobriefing.com/teradyne-q3-revenue-ai-demand/)
- Forecast upgrades: GS 2035 humanoid units 1.38m → 6.48m; MS China 2026 units 14k → 50k — [24/7 Wall St](https://247wallst.com/investing/2026/09/13/robots-everywhere-goldman-sachs-now-sees-6-5-million-humanoid-robots-by-2035/); [AI Weekly](https://aiweekly.co/alerts/morgan-stanley-doubles-china-humanoid-robot-forecast-to-50000)
- Big-tech commitment: Amazon >1m robots, plus acquisitions of Fauna and Rivr; Google folded Intrinsic into Google/DeepMind; Tesla started Optimus production line — [SupplyChain247](https://www.supplychain247.com/article/amazon-ai-robotics-delivery-strategy-2026); [TechCrunch](https://techcrunch.com/2026/02/25/alphabet-owned-robotics-software-company-intrinsic-joins-google); [Nasdaq](https://www.nasdaq.com/articles/tesla-optimus-humanoid-robot-key-takeaways-q3-earnings-call)
- Tariff risk eased: Oct 28, 2026 Section 232 proclamation found robotics/industrial machinery imports a national-security threat but imposed no tariffs, directing negotiations instead; Commerce to flag any need for further action — [White House fact sheet](https://www.whitehouse.gov/fact-sheets/2026/10/fact-sheet-president-donald-j-trump-adjusts-imports-of-robotics-industrial-machinery-and-their-parts-and-components-into-the-united-states/); [DroneXL, Oct 28, 2026](https://dronexl.co/2026/10/28/trump-section-232-robotics-industrial-machinery-talks-drone-tariffs/)

**Bear points**
- Hype/froth: Unitree retail oversubscription >8,000x, +629% open, then −45% from peak in six days (~$30bn lost) — [Gasgoo](https://autonews.gasgoo.com/articles/market-industry/unitree-surges-629-at-open-one-lot-yields-up-to-470000-yuan-market-cap-exceeds-400-billion-yuan-2090018320131842049); [The Next Web](https://thenextweb.com/news/unitree-shares-45-percent-slump-bubble-fears)
- Official bubble warning: China's NDRC (Nov 27–28, 2025) warned of bubble risk in humanoid robotics; >150 Chinese humanoid companies, more than half startups or cross-sector entrants; technology paths, business models and use cases "yet to fully mature" — [Bloomberg](https://www.bloomberg.com/news/articles/2025-11-27/china-warns-of-bubble-risk-in-booming-humanoid-robotics-industry); [Fortune](https://fortune.com/2025/11/28/china-warns-of-bubble-risks-in-booming-humanoid-robots-arena) (STALE but still the key official warning)
- Price deflation: Caixin (Jun 15, 2026) reports "involution" in semi-humanoid and entertainment robots, with prices falling fast and leaders using price cuts to squeeze out rivals — [Caixin](https://www.caixinglobal.com/2026-06-15/in-depth-chinas-humanoid-robot-boom-sparks-fears-of-bruising-price-wars-102454393.html)
- China dominance: 59% of global industrial robot installations in 2025 — [IFR China release](https://ifr.org/downloads/press_docs/EN-2026-SEP-24-IFR_Press_Release_WR-CHINA.pdf); cheaper Chinese reducers threaten Harmonic Drive/Nabtesco share — [Simply Wall St](https://simplywall.st/stocks/jp/capital-goods/tse-6324/harmonic-drive-systems-shares/news/humanoid-robotics-momentum-might-change-the-case-for-investi) (opinion)
- Cash burn: Agility 2025 revenue $1.78m vs net loss ~$138m and ~$100m cash burn, with filing warning of larger losses; Boston Dynamics unprofitable; Doosan Robotics never had an operating-profit quarter since IPO — [The Robot Report](https://www.therobotreport.com/agility-robotics-reports-18m-revenue-ahead-of-humanoid-spac/); [Mike Kalil](https://mikekalil.com/blog/agility-robotics-sec-filing/); [The Star/Reuters](https://www.thestar.com.my/tech/tech-news/2026/09/14/exclusive-ipo-for-humanoid-robot-maker-boston-dynamics-unlikely-in-2027-executive-says); [Daum](https://v.daum.net/v/20260303101555582)
- Execution misses at small caps: Serve 2026 revenue guidance cut from $26m to $9–10m; Richtech Q1 miss plus financial restatement — [Nasdaq](https://www.nasdaq.com/articles/can-serve-robotics-turn-2000-robots-revenue-growth-engine); [Barchart](https://www.barchart.com/story/news/3064289/richtech-robotics-financial-restatement-turns-what-should-be-a-breakout-quarter-into-a-credibility-test)
- SPAC track record: Q1 2026 de-SPACs median close+7-day return −13.06% (n=10), median redemptions 90.2% (3-yr avg 95.7%); Q2 2026 median −31.59% (average −16.41%) — [Houlihan Capital Q1 2026](https://www.houlihancapital.com/wp-content/uploads/2026/05/Q1-2026-SPAC-Report-v2.pdf); [Houlihan Capital Q2 2026](https://www.houlihancapital.com/wp-content/uploads/2026/08/Q2-2026-SPAC-Report.pdf)
- Academic evidence: de-SPACs average abnormal returns of −14.1% at 12 months, −20.2% at 18 months, −18.0% at 24 months (Kiesel et al., European Financial Management 2023); Goldman (2021) found the median SPAC underperformed the Russell 3000 by 42pp in the six months after closing (STALE) — [Kiesel et al.](https://aisberg.unibg.it/handle/10446/226949); [Fortune](https://fortune.com/2021/09/16/spac-returns-ipos-goldman-sachs/amp)
- Timelines slip: Tesla external Optimus deliveries now ~end-2027 (earlier 2025-era timelines were revised); Boston Dynamics missed its 4-year IPO commitment (June 2025) and an IPO is unlikely in 2027 — [Nasdaq](https://www.nasdaq.com/articles/tesla-optimus-humanoid-robot-key-takeaways-q3-earnings-call); [The Star/Reuters](https://www.thestar.com.my/tech/tech-news/2026/09/14/exclusive-ipo-for-humanoid-robot-maker-boston-dynamics-unlikely-in-2027-executive-says)
- "Sell the news" at incumbents: Fanuc shares plunged on record orders and a guidance raise (Aug 2026) — [TechNews](https://finance.technews.tw/2026/08/03/fanuc-raises-full-year-forecast/)
- Customer concentration: Symbotic 85% Walmart (FY2025) — [simplify.jobs](https://simplify.jobs/c/Symbotic)
- Private valuations are preferred-share marks; Figure secondary marks (~$35bn) are below its $39bn round — [Barchart](https://www.barchart.com/story/news/3636345/3-humanoid-robot-etfs-to-ride-a-speculative-trend); [DeFi Llama](https://defillama.com/pre-ipo/figure-ai)
- Tariff/legal regime still unsettled: Section 232 finding leaves the door open to later action; the Supreme Court struck down IEEPA tariffs in Feb 2026 but Section 232 tariffs have survived legal challenges; ISRG carries a ~0.9pt gross-margin tariff hit in 2026 — [DroneXL](https://dronexl.co/2026/10/28/trump-section-232-robotics-industrial-machinery-talks-drone-tariffs/); [BioSpace](https://www.biospace.com/press-releases/intuitive-announces-third-quarter-2026-earnings)

### Inferences
- The theme shows several classic late-hype markers: record IPO oversubscription, sharp post-IPO reversal, SPAC vehicles bringing pre-revenue companies to market, thematic ETFs gathering assets quickly, and repeated large upward revisions to sell-side TAMs. Comparable past thematic cycles (e.g. 2020–21 SPAC/EV/lidar wave, in which many lidar SPACs fell 80%+) suggest pre-revenue names carry high drawdown risk even if the long-term theme proves right. (The lidar-SPAC comparison is general knowledge, not sourced in this session.)
- The highest-quality, most accessible exposure for a UK ISA investor is arguably a combination of profitable incumbents (ISRG, Fanuc/Yaskawa/Keyence where the platform allows, Symbotic with concentration risk) and a diversified UCITS robotics ETF. Humanoid pure plays are either inaccessible (Unitree, private names) or highly speculative (Agility, Serve, Richtech). This is an inference, not advice.
- China competition is a two-edged factor: it makes the humanoid volume forecasts more credible (cheap hardware), but it compresses margins for Western/Japanese hardware makers and leaves the most investable volume winners on mainland exchanges that UK retail cannot easily reach.

### Gaps
- Humanoid startup cash burn data (Figure, 1X, Apptronik, PI) is not disclosed.
- No 2026 US export-control action specific to robotics found (only Section 232 tariff process); Chinese export controls on rare earths/magnets (relevant to actuators) not researched.
- Historical robotics-ETF drawdown statistics (e.g. BOTZ/ROBO 2021–22 drawdowns) not retrieved.
