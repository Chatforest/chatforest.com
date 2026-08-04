---
title: "Anthropic Signs $19B Kentucky Data Center Lease: 401 MW of Dedicated Compute by 2028"
date: 2026-07-07
description: "Anthropic signed a 20-year, $19 billion lease for TeraWulf's Justified Data campus — a 401 MW AI infrastructure site built on a former aluminum smelter in Hawesville, Kentucky. Initial capacity arrives in H2 2027. Here's what it adds to Anthropic's compute picture and what builders should expect."
content_type: "Builder's Log"
categories: ["Anthropic", "Infrastructure", "AI Industry"]
tags: ["anthropic", "claude", "compute", "infrastructure", "data-center", "rate-limits", "capacity", "terawulf", "kentucky"]
sources_audited: 2026-08-04
---

On July 6, 2026, Anthropic signed a 20-year lease with TeraWulf Inc. for the Justified Data campus in Hawesville, Kentucky — a purpose-built AI infrastructure site expected to generate approximately $19 billion in contracted revenue for TeraWulf over the initial lease term. ([TeraWulf press release](https://investors.terawulf.com/news-events/press-releases/detail/142/terawulf-announces-anthropic-lease-at-justified-data-campus-and-sale-of-majority-interest-in-abernathy-joint-venture-to-fluidstack) · [CNBC](https://www.cnbc.com/2026/07/06/anthropic-terawulf-data-center-ai.html))

The campus will deliver approximately 401 megawatts of critical IT load in phases ([TeraWulf SEC 8-K, July 6, 2026](https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-26-080583/tm2619468d1_8k.htm)). Initial capacity comes online in the second half of 2027. Full buildout is expected by early 2028.

For builders on Claude, this is the fourth major infrastructure commitment Anthropic has announced in 2026, and the one with the longest time horizon before it affects your API experience.

---

## What TeraWulf Is and Why the Site Matters

TeraWulf is an AI infrastructure developer that acquires industrial power sites and converts them for high-density compute. The Justified Data campus sits on the former Century Aluminum smelter in Hawesville, Hancock County, Kentucky — a site TeraWulf, through affiliate Justified DataPower LLC, acquired from Century for $200 million in cash in a deal that closed February 2, 2026, with Century retaining a 6.8% non-dilutive minority equity stake in the development entity, Raylan Data Holdings LLC ([TeraWulf press release](https://investors.terawulf.com/news-events/press-releases/detail/129/terawulf-expands-digital-and-power-infrastructure-portfolio) · [Century Aluminum 8-K](https://www.stocktitan.net/sec-filings/CENX/8-k-century-aluminum-co-reports-material-event-bfc05500fd48.html)).

The aluminum angle matters. Smelting is one of the most energy-intensive industrial processes that exists. The Hawesville smelter ran at a scale that required dedicated high-voltage transmission lines, an on-site substation, and a direct connection to the regional transmission network. All of that infrastructure stays in place when you repurpose the site for data centers.

The result: approximately 480 MW of immediately available grid-connected power and more than 250 buildable acres ([TeraWulf press release](https://investors.terawulf.com/news-events/press-releases/detail/129/terawulf-expands-digital-and-power-infrastructure-portfolio)). Those are not planned numbers — the grid connection already exists. For comparison, large-scale (100+ MW) greenfield power projects in the U.S. face a median of four-plus years from interconnection request to commercial operation, per Lawrence Berkeley National Laboratory's annual interconnection-queue research ([LBNL, "Queued Up: 2025 Edition"](https://emp.lbl.gov/publications/queued-2025-edition-characteristics)). The Hawesville site's existing grid connection sidesteps that queue entirely.

---

## The Lease Structure

The deal is a 20-year lease, with Anthropic holding two successive five-year renewal options — giving Anthropic the option to extend to 30 years at the same campus if it chooses. Rent payments begin upon delivery of each phase, so Anthropic starts paying for capacity as it comes online rather than up front ([TeraWulf SEC 8-K, July 6, 2026](https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-26-080583/tm2619468d1_8k.htm)).

The $19 billion figure is the expected total contracted revenue over the 20-year initial term. Payments are backed by investment-grade credit ([TeraWulf SEC 8-K](https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-26-080583/tm2619468d1_8k.htm)), which is why this lease structure is comparable to infrastructure bonds rather than typical technology contracts. The credit quality also tells you something about how counterparties view Anthropic's long-term viability.

TeraWulf simultaneously announced a separate transaction: it is selling its 50.1% stake in the Abernathy Joint Venture — a different data center it co-owned with Fluidstack — to an investor group led by Fluidstack for approximately $530 million, paid in three installments through April 2027 ([TeraWulf SEC 8-K](https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-26-080583/tm2619468d1_8k.htm)). TeraWulf is monetizing that co-investment (roughly $450 million of invested capital) at a premium and redeploying the capital toward wholly-owned, single-tenant AI campuses like Justified Data. That is a strategic statement: the Anthropic lease is the business model TeraWulf is building toward.

---

## How This Fits Anthropic's Compute Portfolio

Before this announcement, Anthropic's compute picture for 2026 consisted of:

**SpaceX Colossus 1 (Memphis, Tennessee):** 220,000+ NVIDIA GPUs, 300+ MW ([Anthropic](https://www.anthropic.com/news/higher-limits-spacex)), reportedly $1.25 billion per month through at least May 2029 per SpaceX's IPO-related S-1 disclosures ([Winbuzzer](https://winbuzzer.com/2026/05/21/anthropic-could-pay-xai-125b-for-colossus-compute-xcxwbn/)). Mixed-generation NVIDIA silicon — H100, H200, and GB200 ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/musks-colossus-1-ai-supercomputers-inefficient-mixed-architecture-design-couldnt-be-used-to-train-grok-so-anthropics-using-it-for-inference-instead-musk-readies-unified-blackwell-only-colossus-2-for-frontier-training-and-potential-ipo)). Already online; Anthropic tied this capacity directly to doubled Claude Code rate limits, removed peak-hour restrictions, and higher Opus API limits in Q2 2026 ([Anthropic](https://www.anthropic.com/news/higher-limits-spacex)).

**Amazon Trainium (Indiana):** Dedicated 1,200-acre campus with approximately $11 billion in facility investment ([CNBC](https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html)), built for Trainium-based AI training. Amazon holds a $5 billion equity stake in Anthropic; chip access is part of that arrangement ([Anthropic](https://www.anthropic.com/news/anthropic-amazon-compute)).

**Google TPUs (New York, Texas, Louisiana, Indiana):** A $35 billion Apollo/Blackstone private credit deal closed June 5, 2026 to finance chip purchases ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-05/apollo-wraps-up-35-billion-debt-to-buy-ai-chips-for-anthropic)), building on Anthropic's October 2025 agreement for access to up to 1 million TPUs ([Anthropic](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services) · [Google Cloud](https://www.googlecloudpresscorner.com/2025-10-23-Anthropic-to-Expand-Use-of-Google-Cloud-TPUs-and-Services)) across four states. Broadcom disclosed 3.5 gigawatts of committed Google TPU capacity starting in 2027 ([Tom's Hardware](https://www.tomshardware.com/tech-industry/broadcom-expands-anthropic-deal-to-3-5gw-of-google-tpu-capacity-from-2027)).

**TeraWulf Justified Data (Hawesville, Kentucky):** 401 MW by early 2028. The newest and most distant timeline entry.

The picture is one of systematic diversification across chip architectures (NVIDIA GPUs, Google TPUs, Amazon Trainium), infrastructure ownership models (leased hardware, contracted facility access, purpose-built lease), and geographic locations. Anthropic now has compute in Memphis, Indiana, New York, Texas, Louisiana, and Kentucky.

---

## The Timeline for Builders

Colossus 1 is already running and has already produced visible results for Claude API users. The Google TPU deal is financing hardware that is partly online and partly ramping. The Amazon Trainium campus is in active deployment.

The TeraWulf campus is different: it is not online yet, and will not be until H2 2027 at the earliest. If you are building applications today that depend on Claude's rate limits, pricing, or availability, this announcement does not change anything in the next 12 months.

What it does change is the 2027-2028 planning horizon. When 401 MW comes online, Anthropic will have added capacity equivalent to roughly one and a third Colossus 1 facilities — all of it dedicated, purpose-built, and fully owned under long-term terms. The GPU and TPU mix running on that capacity is not publicly specified, but 401 MW at modern AI compute densities represents training and inference capacity at a scale that will be significant for the API.

The practical read for builders:

- **Near-term (2026):** No direct impact. Colossus 1, Google TPUs, and Amazon Trainium are the capacity drivers. Watch for what happens to Claude Code's temporary 50%-higher weekly limits, originally set to expire July 13, 2026 and already extended once, to July 19 ([Help Net Security](https://www.helpnetsecurity.com/2026/07/13/claude-code-weekly-limits-promotion-extended/)).
- **2027:** Initial Hawesville capacity comes online in the second half. Expect announcements tracking compute delivery, potentially followed by API improvements similar to the pattern after Colossus 1 came online.
- **2028:** Full 401 MW buildout complete, adding to the SpaceX, Amazon, and Google commitments already cited above.

---

## The Power Story

The deeper story in this deal is power, not compute. Every major AI data center built from scratch in 2026 faces the same constraint: grid interconnection takes years. The Hawesville smelter sidesteps this because the power infrastructure was built to run continuous industrial loads 24 hours a day.

Aluminum smelting requires extraordinarily stable, high-current power. The equipment onsite — transformers, switchgear, high-voltage lines — is sized for industrial production, not a typical commercial building. AI data centers, which need continuous high-draw power with high reliability, are almost ideal inheritors of that infrastructure.

This makes the acquisition pattern worth watching. Industrial site repurposing — steel mills, paper mills, smelters — is emerging as a category of AI infrastructure acquisition precisely because the power is already there. TeraWulf has made it a core strategy. If this model proves out, expect more announcements that follow the same pattern.

For builders who care about the carbon footprint of inference, Kentucky's grid runs heavily on coal and natural gas — coal alone is the state's primary electricity source, with coal and gas together accounting for roughly 92% of generation, per the U.S. Energy Information Administration's Kentucky electricity profile ([EIA](https://www.eia.gov/electricity/state/kentucky/)). TeraWulf has not announced renewable energy commitments for the Hawesville campus specifically, though the broader conversation around AI-as-renewable-energy-buyer (which has been part of other data center announcements in 2026) may apply here as the buildout progresses.

---

## What This Signals

A 20-year lease with investment-grade credit backing is not a hedge. It is a statement that Anthropic expects sustained, large-scale compute demand from Claude users for at least two decades.

That kind of commitment changes the risk profile for builders who are deciding whether to architect long-term on Claude. Cloud providers can reprice, deprioritize, or shut down capacity. A purpose-built campus with a 20-year lease and five-year renewal options cannot be unwound quickly. The commitment is bilateral: Anthropic is locked in, which means Anthropic cannot easily walk away from the compute infrastructure — or the product line it is supporting.

The practical builder implication is simple: Anthropic's infrastructure strategy is now visibly long-horizon in a way that quarterly cloud contracts are not. The $19 billion commitment to Kentucky comes on top of the $35 billion Google TPU deal, the $1.25 billion per month Colossus 1 contract, and the Amazon Trainium campus. The company is building compute infrastructure at a scale and with a permanence that matches the ambitions in the product.

Rate limits, pricing, and availability are the day-to-day metrics builders track. Those will continue to shift as each infrastructure phase goes live. The longer-horizon read is that Anthropic is attempting to build the physical infrastructure layer that makes the Claude API genuinely reliable at enterprise scale — not just powerful, but stable and available for the next 20 years.
