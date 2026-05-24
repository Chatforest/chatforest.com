---
title: "SpaceX Filed for the Largest IPO in History. The AI Section Is the Most Interesting Part."
date: 2026-05-25
description: "SpaceX's S-1 reveals a company pouring $12.7B into AI compute, renting its Colossus supercomputer to Anthropic for $1.25B/month, and planning orbital data centers by 2028. Here's what the filing actually says."
tags: ["spacex", "ai-industry", "infrastructure", "compute", "ipo", "elon-musk", "anthropic", "xai"]
rating: 4
---

## The Headline

SpaceX filed its S-1 with the SEC on May 20, 2026, targeting a **June 12 Nasdaq debut under ticker SPCX** at a **$1.75 trillion valuation** with a **$75 billion raise** — the largest IPO in history by a wide margin. (Saudi Aramco's 2019 listing held the record at $35.4 billion raised.)

The headline numbers are staggering. But buried inside the filing is a detailed window into SpaceX's AI infrastructure bet — one that rewrites how you should think about the Colossus supercomputer, the Anthropic deal, and the future of orbital computing.

---

## Three Companies in One S-1

SpaceX's S-1 breaks the business into three segments. Only one of them is profitable.

### Connectivity (Starlink)

- **$11.4 billion revenue** in 2025, growing 50% year-over-year
- **$4.4 billion operating income** — the only segment making money
- **10.3 million subscribers** across 164 countries
- One quiet risk buried in the filing: average revenue per user (ARPU) is declining. It was $99/month in 2023; it's $66/month in Q1 2026. Subscriber growth is outpacing pricing power.

Starlink is the engine that makes everything else possible. Its operating profit funds the rest.

### Space (Launch)

- **$4.1 billion revenue**, a deliberate **$657 million operating loss**
- **$3.8 billion in capex** — almost all of it Starship R&D
- SpaceX currently handles more than **80% of global mass to orbit** and reuses boosters on **85%+ of flights**

SpaceX is losing money in Launch by design. It's building Starship to bring the cost-per-kg to orbit low enough to make orbital manufacturing viable. The losses are a bet on a future business, not an operational failure.

### AI (xAI / Grok / Colossus)

- **$3.2 billion revenue** in 2025
- **$6.4 billion operating loss** — a -199% margin
- **$12.7 billion in capex** for AI infrastructure — **$7.7 billion in Q1 2026 alone**

The AI segment is losing more than twice what it earns. SpaceX spent $7.7 billion on AI infrastructure in a single quarter. By comparison, this is aggressive even against hyperscaler benchmarks: Microsoft and Amazon each spent roughly $80 billion on AI infrastructure in all of 2025, about 6x SpaceX's pace, but SpaceX has roughly 1/100th the revenue.

The bet: Colossus becomes the most important AI compute cluster in the world. Whether that logic holds is the central question the S-1 raises.

---

## The Colossus Infrastructure

The filing discloses what the Colossus cluster actually is, in numbers that hadn't been public before.

**Colossus I** (Memphis, Tennessee):
- **220,000+ Nvidia GPUs** — H100, H200, and GB200 accelerators
- **300 megawatts** of compute capacity

**Colossus II** (near Booneville, Mississippi):
- Online in early 2026
- Comparable scale to Colossus I

Together, SpaceX claims they form **"the first coherent gigawatt-scale AI training cluster"** — a single unified fabric capable of training models too large to fit inside any other facility. Whether that claim is technically accurate is debated; Meta's and Google's clusters operate at similar scales. But SpaceX has been more aggressive in deploying at that scale in a shorter time.

---

## The Anthropic Deal: $45 Billion to a Competitor

The S-1's most surprising disclosure is the Anthropic compute contract.

> "SpaceX entered into Cloud Services Agreements with Anthropic for access to compute capacity across COLOSSUS and COLOSSUS II, with the customer agreeing to pay **$1.25 billion per month through May 2029**, with capacity ramping in May and June 2026 at a reduced fee."

That's approximately **$45 billion over three years** — one of the largest compute contracts ever disclosed publicly. Anthropic gets:
- Access to the full capacity of Colossus I (220,000+ GPUs)
- 300 megawatts of power and cooling infrastructure
- A ramp-up period (May–June 2026) at a discounted rate before full billing begins

**The strategic strangeness is real.** Elon Musk runs xAI, which makes Grok — a direct competitor to Anthropic's Claude. Musk approved the Anthropic deal personally, reportedly saying: *"No one set off my evil detector."* That quote is not in the S-1 but has been confirmed by multiple sources.

One critical clause: **either party can cancel with 90 days' notice.** The $45 billion contract is technically a 90-day commitment. That risk is disclosed in the S-1's risk factors, though it does not appear to have disrupted Anthropic's planning.

From SpaceX's perspective: Colossus was built for xAI training. When xAI isn't fully utilizing capacity, renting it to Anthropic generates high-margin revenue. The S-1 is frank about this: the AI segment's $3.2B in 2025 revenue came substantially from compute rentals and cloud services, not from Grok subscriptions.

---

## The Orbital Computing Plan

The most speculative part of the AI section is the orbital computing roadmap.

SpaceX's S-1 discloses a plan to **deploy AI compute satellites beginning 2028**. The rationale:

- Terrestrial power constraints are binding. Data centers require land, water cooling, and grid connections — all increasingly constrained.
- Space-based solar arrays generate **5 times more power per unit area** than terrestrial installations (no weather, no night cycles, no atmosphere).
- Low Earth Orbit provides edge-compute capability that reduces latency for satellite-linked applications globally.

The economics are unproven and the deployment timeline is aggressive, but this is not a throwaway footnote. SpaceX has plausible infrastructure to execute it: Falcon 9 and Starship launch capacity, satellite bus manufacturing from Starlink, and power-generation expertise from its Starshield military contracts.

If orbital computing works at scale, SpaceX's moat expands dramatically — it would control both the compute and the only practical delivery mechanism for orbital compute hardware. No other company is positioned to attempt this.

---

## Governance: The Musk Lock

SpaceX's S-1 structures control definitively in Musk's favor.

- **Class A shares** (public): 1 vote per share
- **Class B shares** (Musk): 10 votes per share
- **Musk's combined voting power: 85.1%**
- SpaceX opts out of Nasdaq's independent board of directors requirement

This is not unusual for tech IPOs — Google and Meta used similar structures at IPO — but SpaceX's concentration is at the high end. Musk can block any transaction, governance change, or strategic shift without minority shareholder consent. Investors buying SPCX are buying exposure to Musk's judgment, not acquiring governance rights.

---

## The Claimed TAM (and Why You Should Be Skeptical)

SpaceX's S-1 claims a **$28.5 trillion total addressable market**. The breakdown:

| Segment | TAM |
|---|---|
| AI / Enterprise | $26.5T (93%) |
| Connectivity | $1.6T |
| Space | $370B |

The AI TAM figure incorporates enterprise software, cloud computing, data center revenue, and agentic AI services. It is a maximalist interpretation. The S-1 itself acknowledges in risk factors that several addressable markets, including orbital manufacturing and asteroid mining, **"do not yet exist."**

This is typical IPO disclosure math. The $26.5T AI TAM doesn't represent SpaceX's realistic capture — it represents the theoretical universe. Actual 2025 revenue from AI was $3.2 billion, against a $6.4 billion operating loss.

---

## What This Means for AI Infrastructure

**The cost of building at scale is now public.** SpaceX spent $12.7 billion on AI capex in 2025, against $3.2 billion in AI revenue. That's a 4:1 spending-to-revenue ratio. This is infrastructure economics: you build before you earn. But seeing these numbers in a public filing normalizes the scale.

**Colossus is real, and it's rented.** The Anthropic deal demonstrates that SpaceX's compute infrastructure is production-ready and generating external revenue. The Anthropic deal at $1.25B/month is not theoretical — it's a disclosed customer contract in an SEC filing.

**Orbital computing is the long bet.** No other AI infrastructure company is positioned to execute orbital compute deployment. If power and land constraints remain binding for terrestrial data centers through 2028-2030, SpaceX's space-based alternative goes from speculative to strategic.

**Musk is simultaneously a hyperscaler, a competitor, and a customer's landlord.** SpaceX/xAI competes directly with OpenAI (Grok vs. ChatGPT) and Anthropic (Grok vs. Claude). Anthropic is paying SpaceX $1.25B/month. OpenAI and SpaceX have their own tense relationship given Musk's previous investment and current legal history. The AI competitive map just got more structurally complicated.

---

## Rating: 4/5

The SpaceX S-1 is one of the most information-dense IPO filings in years for AI infrastructure watchers. Starlink is a real, profitable business. Colossus is real infrastructure. The Anthropic deal is real revenue. The orbital computing plan is a credible long-term bet by the one company capable of executing it.

The risks are also real: the AI segment is losing $6.4 billion annually, ARPU compression is pressuring Starlink, and Musk's 85.1% voting control means investors are buying belief in one person's execution, not governance. The $1.75T valuation requires Colossus to succeed, Starship to bring down orbital launch costs, and orbital computing to materialize — in roughly that order.

**IPO date: June 12, 2026. Ticker: SPCX.**

---

*ChatForest reviews AI tools and industry developments. We research publicly available sources and do not provide financial advice. This article is based on publicly available S-1 filings and reporting.*
