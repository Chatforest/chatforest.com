---
title: "SpaceX Filed for the Largest IPO in History. The AI Section Is the Most Interesting Part."
date: 2026-05-25
description: "SpaceX's S-1 reveals a company pouring $12.7B into AI compute, renting its Colossus supercomputer to Anthropic for $1.25B/month, and planning orbital data centers by 2028. Here's what the filing actually says."
tags: ["spacex", "ai-industry", "infrastructure", "compute", "ipo", "elon-musk", "anthropic", "xai"]
rating: 4
sources_audited: 2026-07-29
---

## The Headline

SpaceX (legally, Space Exploration Technologies Corp.) [filed its S-1 with the SEC on May 20, 2026](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001181412&type=S-1) — [File No. 333-296070, CIK 0001181412](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm) — targeting a **June 12 Nasdaq debut under ticker SPCX** with a **[$75 billion raise](https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html)** (555,555,555 Class A shares at an [expected $135.00 per share](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm), per Amendment No. 2 to the S-1) — implying a **[roughly $1.77 trillion valuation, per CNBC's reporting on the pricing](https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html)** (the S-1 itself does not state a headline valuation figure; this is the market-cap math on the priced shares). It would be the largest IPO in history by a wide margin. (Saudi Aramco's 2019 listing held the prior record, raising **[$25.6 billion, or $29.4 billion including the exercised over-allotment option](https://edition.cnn.com/2019/12/05/investing/saudi-aramco-ipo-price)** — not $35.4 billion as sometimes reported.)

The headline numbers are staggering. But buried inside the filing is a detailed window into SpaceX's AI infrastructure bet — one that rewrites how you should think about the Colossus supercomputer, the Anthropic deal, and the future of orbital computing.

---

## Three Companies in One S-1

SpaceX's S-1 breaks the business into three segments. Only one of them is profitable.

### Connectivity (Starlink)

- **[$11.4 billion revenue](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm)** in 2025, growing roughly 50% year-over-year (49.8%, per the S-1)
- **$4.4 billion operating income** — the only segment making money
- **10.3 million subscribers** across 164 countries
- One quiet risk buried in the filing: [average revenue per user (ARPU) is declining](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm). It was $99/month in 2023; it's $66/month in Q1 2026. Subscriber growth is outpacing pricing power.

Starlink is the engine that makes everything else possible. Its operating profit funds the rest.

### Space (Launch)

- **[$4.1 billion revenue](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm)**, a deliberate **$657 million operating loss**
- **$3.8 billion in capex** — almost all of it Starship R&D
- SpaceX currently handles more than **[80% of global mass to orbit](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm)**; in 2025 alone it completed 170 Falcon/Starship missions, of which 159 used a flight-proven (reused) booster — a **93.5% reuse rate for the year**, per the S-1's operating data

SpaceX is losing money in Launch by design. It's building Starship to bring the cost-per-kg to orbit low enough to make orbital manufacturing viable. The losses are a bet on a future business, not an operational failure.

### AI (xAI / Grok / Colossus)

- **[$3.2 billion revenue](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm)** in 2025
- **$6.4 billion operating loss** — a -199% margin
- **$12.7 billion in capex** for AI infrastructure — **$7.7 billion in Q1 2026 alone**

The AI segment is losing more than twice what it earns. SpaceX spent $7.7 billion on AI infrastructure in a single quarter. For scale: [Amazon's total 2025 capital expenditures were $131.8 billion](https://www.cnbc.com/2026/02/05/amazon-amzn-q4-earnings-report-2025.html) for the full year — roughly 10x SpaceX's full-year 2025 AI capex ($12.7 billion) — which underscores how early-stage SpaceX's AI buildout still is relative to the hyperscalers it is trying to compete with for compute share.

The bet: Colossus becomes the most important AI compute cluster in the world. Whether that logic holds is the central question the S-1 raises.

---

## The Colossus Infrastructure

The filing discloses what the Colossus cluster actually is, in numbers that hadn't been public before — and they're more granular, and in places smaller, than the "220,000 GPUs" figure that circulated in press coverage of the Anthropic deal (see below). Here's what the [S-1 itself says](https://www.sec.gov/Archives/edgar/data/1181412/000162828026039276/spaceexplorationtechnologi.htm):

**COLOSSUS** (Memphis, Tennessee) — SpaceX's first cluster, online in 122 days:
- **~100,000 Nvidia H100 GPUs**
- **~130 megawatts** of compute power

The S-1 does not mention H200 GPUs anywhere in the filing; that detail, which circulated in 2024–2025 press coverage of the original Colossus buildout, is not part of the company's own disclosed figures for this cluster.

**COLOSSUS II** (Memphis, Tennessee **and** Southaven, Mississippi — not Booneville, as some secondary coverage has stated):
- First cluster: **~110,000 Nvidia GB200 GPUs**, ~210 MW, online in 91 days
- Second cluster: **110,000 Nvidia GB300 GPUs**, 220 MW, online 64 days later
- That's roughly **220,000 GPUs and 430 MW already online at Colossus II alone** — more than double Colossus I's scale, not "comparable" to it, as is sometimes claimed
- A further planned expansion phase would add **at least 220,000 more GB300 GPUs and 400+ additional MW**

Combined, the S-1 states COLOSSUS and COLOSSUS II currently provide **approximately 325,000 Nvidia GPUs** and **approximately 1.0 gigawatt** of compute power. SpaceX's own language is that xAI became **["the first company to deploy a coherent gigawatt-scale AI training cluster"](https://www.sec.gov/Archives/edgar/data/1181412/000162828026039276/spaceexplorationtechnologi.htm)** — a narrower claim than "the first coherent gigawatt-scale cluster" (i.e., a claim about being first to *deploy* one, not a claim that no comparable cluster exists elsewhere). Whether even that narrower claim holds is debatable — Meta and Google both operate training infrastructure at broadly similar scale — but SpaceX's construction timelines (91–122 days per cluster, per its own figures above) are unusually fast.

---

## The Anthropic Deal: $45 Billion to a Competitor

The S-1's most surprising disclosure is the Anthropic compute contract.

> "SpaceX entered into Cloud Services Agreements with Anthropic for access to compute capacity across COLOSSUS and COLOSSUS II, with the customer agreeing to pay **[$1.25 billion per month through May 2029](https://www.sec.gov/Archives/edgar/data/1181412/000162828026039276/spaceexplorationtechnologi.htm)**, with capacity ramping in May and June 2026 at a reduced fee." (paraphrasing the S-1's own description of the Cloud Services Agreement; [secondary coverage of the same filing language here](https://www.thevccorner.com/p/spacex-spcx-ipo-s1-teardown-valuation-2026))

That's approximately **$45 billion over three years** ($1.25B × 36 months, May 2026–May 2029) — one of the largest compute contracts ever disclosed publicly. Per the S-1, Anthropic gets:
- Access to compute capacity **across both COLOSSUS and COLOSSUS II** — not just Colossus I alone — which the filing says [together provide approximately 325,000 Nvidia GPUs](https://www.sec.gov/Archives/edgar/data/1181412/000162828026039276/spaceexplorationtechnologi.htm)
- [More than 300 megawatts of compute capacity](https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html), per Anthropic's and SpaceX's own public statements at the time the deal was announced (the S-1 itself does not break out a specific megawatt figure for Anthropic's allocation)
- A ramp-up period (May–June 2026) at a reduced fee before full billing begins

**The strategic strangeness is real.** Elon Musk runs xAI, which makes Grok — a direct competitor to Anthropic's Claude. Musk had [previously called Anthropic "evil" and said it "hates Western Civilization,"](https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html) then reversed course the week the deal was announced, [writing on X](https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html): *"Everyone I met was highly competent and cared a great deal about doing the right thing. No one set off my evil detector."*

One critical clause: after an initial three-month period, **either party can cancel with 90 days' notice.** The $45 billion contract is, after that initial period, effectively a rolling 90-day commitment. That term is disclosed directly in the S-1's description of the Cloud Services Agreement, though it does not appear to have disrupted Anthropic's planning.

From SpaceX's perspective: Colossus was built for xAI training. When xAI isn't fully utilizing capacity, renting it to Anthropic generates high-margin revenue. One caveat worth flagging: the Cloud Services Agreement was signed in May 2026 — after fiscal year 2025 closed — so the AI segment's **$3.2B in 2025 revenue** cannot itself reflect Anthropic rental income. Per the S-1, that 2025 AI revenue instead came from **X platform advertising and Grok-related subscriptions, data licensing, and API access**; the Anthropic contract is a 2026-and-forward revenue stream, not a driver of the 2025 figures cited above.

---

## The Orbital Computing Plan

The most speculative part of the AI section is the orbital computing roadmap.

[SpaceX's S-1 discloses](https://www.sec.gov/Archives/edgar/data/1181412/000162828026039276/spaceexplorationtechnologi.htm) it expects to **begin deploying orbital AI compute satellites "as early as 2028."** The rationale:

- Terrestrial power constraints are binding. Data centers require land, water cooling, and grid connections — all increasingly constrained.
- The S-1 states space-based solar can generate **"more than five times the energy per unit area" of terrestrial solar**, citing continuous illumination, no atmospheric interference, and optimal orientation.
- Low Earth Orbit provides edge-compute capability that reduces latency for satellite-linked applications globally.

The economics are unproven and the deployment timeline is aggressive, but this is not a throwaway footnote. SpaceX has plausible infrastructure to execute it: Falcon 9 and Starship launch capacity, satellite bus manufacturing from Starlink, and power-generation expertise from its Starshield military contracts.

If orbital computing works at scale, SpaceX's moat expands dramatically — it would control both the compute and the only practical delivery mechanism for orbital compute hardware. No other company is positioned to attempt this.

---

## Governance: The Musk Lock

SpaceX's S-1 structures control definitively in Musk's favor.

- **[Class A shares](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm)** (public): 1 vote per share
- **Class B shares** (Musk): 10 votes per share
- **[Musk's voting power: approximately 82.4%](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm)** of the combined voting power immediately after the offering at the $135.00 IPO price (82.3% if the underwriters' over-allotment option is exercised in full) — a separate figure elsewhere in the same filing, counting shares underlying Musk's outstanding stock options, puts his "combined voting power" at 84.4%. Either way, not 85.1% as some secondary sources have stated.
- SpaceX will be a "controlled company" under Nasdaq's listing rules and intends to rely on exemptions from the independent-board and independent-committee requirements that apply to other public companies

This is not unusual for tech IPOs — Google and Meta used similar structures at IPO — but SpaceX's concentration is at the high end. Musk can block any transaction, governance change, or strategic shift without minority shareholder consent. Investors buying SPCX are buying exposure to Musk's judgment, not acquiring governance rights.

---

## The Claimed TAM (and Why You Should Be Skeptical)

[SpaceX's S-1 claims](https://www.sec.gov/Archives/edgar/data/1181412/000162828026039276/spaceexplorationtechnologi.htm) a **$28.5 trillion total addressable market**. The breakdown:

| Segment | TAM |
|---|---|
| AI / Enterprise | $26.5T (93%) |
| Connectivity | $1.6T |
| Space | $370B |

The AI TAM figure incorporates enterprise software, cloud computing, data center revenue, and agentic AI services. It is a maximalist interpretation. The S-1 itself acknowledges in risk factors that several addressable markets it counts toward that total — including transportation, energy production, and manufacturing on the Moon and Mars, and asteroid mining — **["do not exist today."](https://www.sec.gov/Archives/edgar/data/1181412/000162828026039276/spaceexplorationtechnologi.htm)**

This is typical IPO disclosure math. The $26.5T AI TAM doesn't represent SpaceX's realistic capture — it represents the theoretical universe. Actual 2025 revenue from AI was $3.2 billion, against a $6.4 billion operating loss.

---

## What This Means for AI Infrastructure

**The cost of building at scale is now public.** SpaceX spent $12.7 billion on AI capex in 2025, against $3.2 billion in AI revenue. That's a 4:1 spending-to-revenue ratio. This is infrastructure economics: you build before you earn. But seeing these numbers in a public filing normalizes the scale.

**Colossus is real, and it's rented.** The Anthropic deal demonstrates that SpaceX's compute infrastructure is production-ready and generating external revenue. The Anthropic deal at $1.25B/month is not theoretical — it's a disclosed customer contract in an SEC filing.

**Orbital computing is the long bet.** No other AI infrastructure company is positioned to execute orbital compute deployment. If power and land constraints remain binding for terrestrial data centers through 2028-2030, SpaceX's space-based alternative goes from speculative to strategic.

**Musk is simultaneously a hyperscaler, a competitor, and a customer's landlord.** SpaceX/xAI competes directly with OpenAI (Grok vs. ChatGPT) and Anthropic (Grok vs. Claude). Anthropic is paying SpaceX $1.25B/month. Musk's relationship with OpenAI is separately contentious: the Anthropic deal was announced [the same week Musk was testifying in his ongoing lawsuit against OpenAI and CEO Sam Altman](https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html) in federal court in Oakland. The AI competitive map just got more structurally complicated.

---

## Rating: 4/5

The SpaceX S-1 is one of the most information-dense IPO filings in years for AI infrastructure watchers. Starlink is a real, profitable business. Colossus is real infrastructure. The Anthropic deal is real revenue. The orbital computing plan is a credible long-term bet by the one company capable of executing it.

The risks are also real: the AI segment is losing $6.4 billion annually, ARPU compression is pressuring Starlink, and Musk's roughly 82-84% voting control means investors are buying belief in one person's execution, not governance. The implied ~$1.77T valuation requires Colossus to succeed, Starship to bring down orbital launch costs, and orbital computing to materialize — in roughly that order.

**IPO date: June 12, 2026. Ticker: SPCX.**

---

## Sources

**Primary source — the S-1 filing itself, via SEC EDGAR (CIK 0001181412, File No. 333-296070):**
- [SpaceX (Space Exploration Technologies Corp.) — original Form S-1, filed May 20, 2026](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm)
- [SpaceX — Form S-1/A Amendment No. 1](https://www.sec.gov/Archives/edgar/data/1181412/000162828026039276/spaceexplorationtechnologi.htm)
- [SpaceX — Form S-1/A Amendment No. 2 (priced at $135.00/share)](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm)
- [Full EDGAR filing history for SpaceX's S-1](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001181412&type=S-1)

**Secondary reporting:**
- [SpaceX S-1 Deep Dive: Decoding the $1.75T IPO — Vested Finance](https://vestedfinance.com/blog/us-stocks/inside-spacexs-s-1-decoding-the-three-engine-bet-going-public-as-spcx/)
- [SpaceX SPCX S-1 Teardown: Valuation, Starlink, xAI, Anthropic Deal — The VC Corner](https://www.thevccorner.com/p/spacex-spcx-ipo-s1-teardown-valuation-2026)
- [SpaceX Targets $135 IPO Price at $1.77 Trillion Valuation — CNBC](https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html)
- [SpaceX IPO: 8 Things to Know Before It Goes Public — Forbes](https://www.forbes.com/sites/investor-hub/article/spacex-ipo-things-to-know/)
- [Anthropic, SpaceX announce compute deal that includes space development — CNBC](https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html)
- [Saudi Aramco Raises $25.6 Billion in World's Biggest IPO — CNN](https://edition.cnn.com/2019/12/05/investing/saudi-aramco-ipo-price)
- [Amazon Q4 2025 earnings report — CNBC](https://www.cnbc.com/2026/02/05/amazon-amzn-q4-earnings-report-2025.html)

---

*ChatForest reviews AI tools and industry developments. We research publicly available sources and do not provide financial advice. This article is based on publicly available S-1 filings and reporting.*
