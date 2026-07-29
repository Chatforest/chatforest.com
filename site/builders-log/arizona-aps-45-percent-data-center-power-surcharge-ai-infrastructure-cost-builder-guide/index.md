# Arizona's 45% Data Center Power Surcharge Is a Preview of What's Coming Everywhere

> Arizona Public Service is proposing a 45% rate increase specifically for data centers. The ACC decision comes in December 2026, with new rates effective early 2027. Here's what the APS case means for builders evaluating self-hosted infrastructure and what the broader 27-state pattern tells you about the future of AI compute costs.


On May 19, 2026, Arizona regulators [opened evidentiary hearings](https://azcapitoltimes.com/news/2026/05/19/aps-rate-case-kicks-off-with-hours-of-protest-over-14-rate-increase/) on a rate case that would impose a 45% electricity rate increase on data centers operating in the state. The utility is Arizona Public Service (APS), [Arizona's largest and longest-serving energy provider](https://www.aps.com/en/About/Our-Company/About-us), serving about 1.4 million customers. The target is what APS itself calls ["extra-large energy users"](https://www.aps.com/en/Utility/Regulatory-and-Legal/Rate-case) — the category that encompasses every significant AI compute facility in the Phoenix metro area and surrounding regions.

The ACC (Arizona Corporation Commission) is [expected to issue a final decision in December 2026, with new rates taking effect in early 2027 if approved](https://azcapitoltimes.com/news/2026/06/01/what-happens-now-the-aps-rate-case-isnt-over/).

This is not a local Arizona story. It is a preview of a regulatory shift that is now moving through [27 states simultaneously](https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers) — and builders evaluating where and how to run AI inference workloads need to factor it in before committing to infrastructure.

---

## What APS Is Actually Proposing

APS [filed its rate case with the ACC on June 13, 2025](https://www.aps.com/en/Utility/Regulatory-and-Legal/Rate-case). The headline numbers, [as broken out by customer class](https://www.abc15.com/news/local-news/investigations/arizona-public-service-seeks-permission-to-raise-electric-rates-every-year):

- **~14% average rate increase** for customers overall
- **~16% increase** for residential customers (roughly $20/month per household)
- **45%+ increase** for extra-large energy users, including data centers

The current rates are pegged to APS's 2021–2022 cost basis — a period before the AI compute buildout accelerated. Since then, [APS says it has invested more than $2 billion per year in infrastructure maintenance and upgrades](https://www.aps.com/en/Utility/Regulatory-and-Legal/Rate-case), and the utility cites equipment cost increases in the 60–90% range, with transformers as the most-cited example. The 45% figure is APS's attempt to close that gap on the customers driving the most incremental load.

Anne Carlton, APS's regulatory compliance manager, [told KTAR News](https://ktar.com/arizona-business/data-centers-aps-rate-hike/5812611/): "One of the big proposals we have in this rate case is actually a 45% increase for their (data centers') rates to make sure that they will continue to pay their fair share, even if they grow at the rate that we expect them to, which is very, very large." On equipment costs, she said separately: "We've seen our equipment increases from 60 to 90% for things like transformers, which we have hundreds of thousands of."

The regulatory calendar:

| Event | Date |
|---|---|
| Rate case filed | June 13, 2025 |
| ACC evidentiary hearings begin | May 19, 2026 |
| ACC evidentiary hearings conclude | [Extended past their original late-June target, wrapping in early July 2026](https://www.kjzz.org/business/2026-07-09/extended-corporation-commission-hearings-on-aps-rate-increase-wrap) |
| Judge's recommended order | Expected ahead of the December ACC vote (exact date not yet published) |
| ACC open meeting / final vote | [December 2026](https://azcapitoltimes.com/news/2026/06/01/what-happens-now-the-aps-rate-case-isnt-over/) |
| New rates take effect | [Early 2027](https://azcapitoltimes.com/news/2026/06/01/what-happens-now-the-aps-rate-case-isnt-over/) |

**Opposition**: Arizona Attorney General Kris Mayes [was granted formal intervenor status](https://ktar.com/arizona-news/intervention-aps-rate-hike-request/5750534/) against the proposal — [the first time in state history an Arizona AG has intervened in a rate case](https://www.utilitydive.com/news/arizona-attorney-general-mayes-opposes-aps-proposed-14-rate-hike/760205/) — [calling it "blatant" corporate greed](https://www.azfamily.com/2026/03/03/arizona-ag-kris-mayes-challenges-aps-rate-hike-proposal-calls-it-greed/). APS faces organized residential customer protest as well — [the hearings have run for hours with residents testifying against the 14% increase for homes](https://azcapitoltimes.com/news/2026/05/19/aps-rate-case-kicks-off-with-hours-of-protest-over-14-rate-increase/). The data center surcharge is largely separate from that fight, but it affects the regulatory optics.

The ACC could approve, reject, or modify the proposal. A compromise rate — somewhere between current levels and the 45% ask — is the most likely outcome. But even a 20–30% increase for large-load customers would materially change Arizona's attractiveness for self-hosted AI compute.

---

## Why Arizona Data Centers Are Under Pressure

Arizona's data center buildout has been aggressive. The Phoenix metro area has become one of the largest US data center markets, partly because land is available, partly because temperatures have historically kept cooling costs lower than expected, and partly because state and local governments actively recruited hyperscalers and colocation providers.

That recruitment worked. By 2030, [Electric Power Research Institute (EPRI) modeling projects Arizona will be one of seven states where data centers consume more than 20% of the state's total electricity](https://www.eenews.net/articles/data-centers-share-of-us-electricity-seen-doubling-by-2030/) (the others are Indiana, Iowa, Nebraska, Nevada, Oregon, and Wyoming). That kind of load concentration changes the math for everyone else on the grid.

The core tension APS is navigating: the infrastructure needed to serve those data centers — substations, transformers, transmission upgrades, new generation capacity — must be paid for by someone. APS's position is that the entity creating the need should bear the cost. Residential customers, understandably, agree.

---

## This Is Happening in 27 States Simultaneously

The Arizona case is the most visible current example, but it is not isolated.

**States with large-load legislation already enacted:** [California, Ohio, Utah](https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers).

**States with legislation actively in progress:** [27 states have some version of large-load cost recovery legislation under consideration, according to the MultiState tracker as of April 2026](https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers).

The common mechanism across these bills: require data center developers to pay for the grid upgrades needed to interconnect their facilities, rather than socializing those costs through rate base. The specific implementation varies — some require upfront cost deposits, some impose ongoing surcharges, some require developers to bring matching generation capacity online.

**The utility capex picture is enormous.** [US investor-owned utilities have collectively announced $1.4 trillion in capital spending through 2030, a 27% jump from the $1.1 trillion plan published the prior year](https://powerlines.org/utilities-are-planning-to-spend-1-4-trillion-on-capital-expenditures-through-2030-as-utility-bills-rise-study-finds/). [PowerLines estimates residential customers are on track to absorb roughly $700 billion of that $1.4 trillion through rate increases](https://powerlines.org/utilities-are-planning-to-spend-1-4-trillion-on-capital-expenditures-through-2030-as-utility-bills-rise-study-finds/) — unless state legislatures succeed in redirecting more of those costs to large-load customers.

**The price impact is already measurable, but one widely-cited number needs a caveat.** [Bloomberg's analysis of wholesale electricity prices at grid nodes near major data-center hubs found increases of as much as 267% between 2020 and 2025](https://www.bloomberg.com/graphics/2025-ai-data-centers-electricity-prices/) — but [that figure measures wholesale generation costs at specific local nodes, not what shows up on a residential bill](https://www.wral.com/news/state/fact-check-data-center-electricity-bills-june-15/), since wholesale supply costs are only 30–50% of a typical bill. What is well-documented at the national retail level: [the EIA projects average US residential electricity prices will rise about 5% in 2026](https://www.eia.gov/pressroom/releases/press588.php), and [Fortune reports a nearly 40% cumulative increase in US electricity prices since 2021](https://fortune.com/2026/05/20/electricity-bills-surging-not-just-data-centers/). [A November 2025 Consumer Reports survey of 2,146 US adults found 78% at least somewhat concerned that new data centers will raise their energy bills](https://advocacy.consumerreports.org/press_release/new-survey-from-consumer-reports-finds-majority-of-households-strained-by-energy-bills-concerned-over-data-centerss-impact-on-bills).

---

## The Ratepayer Protection Pledge: Voluntary, Not Enforceable

On [March 4, 2026, in conjunction with the White House, a group of major data center operators signed what the administration called the "Ratepayer Protection Pledge"](https://www.whitehouse.gov/releases/2026/03/president-trump-secures-historic-commitment-to-keep-electricity-costs-down-amid-data-center-boom/). Original signatories included [Amazon, Google, Meta, Microsoft, OpenAI, Oracle, and xAI](https://www.whitehouse.gov/ratepayer-protection-pledge/). [The pledge commits signatories to procure the generation resources their new demand requires, and to cover the cost of new delivery-infrastructure upgrades (including network upgrades) needed to serve their own data centers](https://www.whitehouse.gov/ratepayer-protection-pledge/).

The pledge is real in the sense that these companies are making a commitment with reputational weight. It is not real in the sense that it has no legal enforcement mechanism. State regulators are not bound by it, and the 27-state legislative wave has not paused because of it. What the pledge does not cover: the rate adjustments APS is seeking for its *existing* large-load customers — the pledge only addresses costs tied to signatories' own new generation and new delivery upgrades, not the embedded-cost-recovery gap utilities like APS are trying to close through general rate cases.

The Biden-era CHIPS infrastructure model (mandatory cost-sharing as a condition of incentives) set a precedent, but the current administration has preferred voluntary frameworks. The gap between voluntary commitments and state-level mandatory cost recovery legislation is where the regulatory friction lives — and it is substantial.

---

## What This Means for Builders

The APS rate case is a cost signal, not just a policy story. Here is how to think through the implications depending on your infrastructure setup.

### If you run your own GPU cluster in Arizona (or are planning to)

Factor a 15–45% increase in power costs into your TCO model for 2027 and beyond. The ACC decision arrives in December 2026. Even a partial approval — say, a 25% surcharge rather than 45% — materially changes payback calculations for owned infrastructure. Arizona colocation pricing will move similarly; colo providers pass power costs through on variable terms.

The breakeven window for owned GPU infrastructure (typically 18–36 months against on-demand cloud pricing) lengthens when the power cost assumption rises. If your model assumed $0.07/kWh and the real number is $0.10/kWh by 2027, rebuild the model before committing to hardware.

### If you're evaluating where to locate self-hosted inference

Run the power cost comparison across candidate regions before signing leases or colo contracts. Current pricing snapshots:

- **Arizona (Phoenix metro)**: Under APS proposal, large-load rates rise 45% — decision December 2026
- **Texas (ERCOT zones)**: Competitive retail market; variable but currently lower than APS asks; [large-load cost-recovery legislation (SB6) was already signed into law in June 2025](https://www.mcguirewoods.com/client-resources/alerts/2025/7/texas-senate-bill-6-significantly-expands-regulatory-oversight-over-large-loads-in-ercot/) and is now moving through PUCT rulemaking, not pending in the legislature
- **Virginia (Northern Virginia)**: Largest US data center cluster; Dominion Energy rate cases ongoing; [Virginia's State Corporation Commission created a new large-load rate class (25 MW+) with minimum-payment requirements in its November 2025 Dominion rate case ruling](https://virginiamercury.com/2025/11/25/scc-approves-chesterfield-gas-plant-and-dominion-rate-hike-creates-new-rate-class-for-data-centers/)
- **Pacific Northwest**: Historically cheap hydro power; [BPA's (Bonneville Power Administration) transmission queue is under pressure — data centers alone are driving roughly 18 GW of new load requests against BPA's current 11-12 GW system load](https://newprojectmedia.com/interview-bonneville-power-administration-executives-discuss-new-projects-being-connected-to-grid-in-next-two-years/) — but the region still has among the lowest large-scale rates in the US and is actively building out to attract AI workloads
- **Wyoming, Montana**: Low population density, coal/gas transitioning to wind; state legislatures less aggressive on large-load cost recovery; early-stage for AI compute

Regions actively building renewable generation have an incentive to attract large-load customers to justify the build. Regions with legacy grid infrastructure under strain are more likely to impose surcharges. That correlation should inform site selection decisions.

### If you rely entirely on managed APIs (Claude, GPT, Gemini, etc.)

You are insulated from the APS rate case directly — for now. The hyperscalers signed the Ratepayer Protection Pledge, and their data center contracts are typically long-term with power purchase agreements (PPAs) locked at current rates. Microsoft, Google, and Amazon have massive renewable energy PPA portfolios specifically to hedge this risk.

What you are not insulated from: **long-term API pricing drift**. The compute cost basis for frontier model inference will increase as power costs rise for the hyperscalers' own training runs and inference capacity. That increase won't show up in API pricing immediately — the hyperscalers can absorb it and are competing hard on price — but the direction of travel is upward.

Watch for "infrastructure surcharges" or region-specific pricing differentials in cloud billing, similar to how AWS and Azure already price inference differently across availability zones. As large-load cost recovery legislation matures, cloud regions in high-surcharge states will become more expensive relative to regions in states with friendlier regulatory environments.

### If you're building cost-sensitive inference at scale

The managed API vs. self-host calculation is actively shifting. Self-hosting made sense when power costs were low and predictable. As large-load cost recovery legislation spreads, the power cost advantage of self-hosting in major US markets is narrowing. The economics now increasingly favor either:

1. **Managed APIs** — for workloads where you don't need the absolute lowest per-token cost and want infrastructure risk insulated
2. **Self-hosting in renewable-build regions** — for workloads large enough to justify on-prem compute, locate in regions where state policy is aligned with large-load growth (Pacific Northwest, Wyoming, some Mountain West states) rather than fighting it

The middle ground — colocation in major metro markets at conventional electricity rates — is getting more expensive. That is not a reason to abandon it, but it should show up in your cost projections.

---

## The Broader Signal

The APS rate case is interesting for the number attached to it (45%) and because Arizona is the most active current site of AI data center construction and regulatory friction. But the actual signal is simpler: **the era of cheap, unsurcharged large-load power in the US is ending**.

The infrastructure cost of the AI compute buildout is real, and it is being socialized in ways that are now generating significant political backlash. State legislatures are responding by shifting those costs back toward large-load customers. Utilities are filing rate cases that reflect their actual cost basis, not 2021 pricing. The Ratepayer Protection Pledge represents the industry's attempt to preempt mandatory cost recovery legislation — but it has not stopped 27 state bills from moving.

For builders, the practical implication is simple: **power cost is no longer a flat-rate commodity for AI infrastructure**. Location, utility, state legislation, and regulatory calendar are now material variables in infrastructure TCO models. Build them in.

---

*Sources: [APS — official rate case page](https://www.aps.com/en/Utility/Regulatory-and-Legal/Rate-case), [APS — About Us](https://www.aps.com/en/About/Our-Company/About-us), [KTAR — APS data center rate increase / Anne Carlton quotes](https://ktar.com/arizona-business/data-centers-aps-rate-hike/5812611/), [ABC15 — rate increase breakdown by customer class](https://www.abc15.com/news/local-news/investigations/arizona-public-service-seeks-permission-to-raise-electric-rates-every-year), [Arizona Capitol Times — hearings kick off, May 19 2026](https://azcapitoltimes.com/news/2026/05/19/aps-rate-case-kicks-off-with-hours-of-protest-over-14-rate-increase/), [Arizona Capitol Times — what happens now, June 2026](https://azcapitoltimes.com/news/2026/06/01/what-happens-now-the-aps-rate-case-isnt-over/), [KJZZ — hearings wrap, July 2026](https://www.kjzz.org/business/2026-07-09/extended-corporation-commission-hearings-on-aps-rate-increase-wrap), [KTAR — Mayes granted intervention](https://ktar.com/arizona-news/intervention-aps-rate-hike-request/5750534/), [Utility Dive — Mayes opposes 14% hike](https://www.utilitydive.com/news/arizona-attorney-general-mayes-opposes-aps-proposed-14-rate-hike/760205/), [Arizona Family — Mayes "greed" quote](https://www.azfamily.com/2026/03/03/arizona-ag-kris-mayes-challenges-aps-rate-hike-proposal-calls-it-greed/), [E&E News — EPRI data center load-growth report](https://www.eenews.net/articles/data-centers-share-of-us-electricity-seen-doubling-by-2030/), [MultiState — State Data Center Laws Tracker](https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers), [PowerLines — $1.4T utility capex report](https://powerlines.org/utilities-are-planning-to-spend-1-4-trillion-on-capital-expenditures-through-2030-as-utility-bills-rise-study-finds/), [Bloomberg — wholesale electricity prices near data centers](https://www.bloomberg.com/graphics/2025-ai-data-centers-electricity-prices/), [WRAL — fact-check on the 267% claim](https://www.wral.com/news/state/fact-check-data-center-electricity-bills-june-15/), [EIA — 2026 electricity price outlook](https://www.eia.gov/pressroom/releases/press588.php), [Fortune — 40% cumulative price increase since 2021](https://fortune.com/2026/05/20/electricity-bills-surging-not-just-data-centers/), [Consumer Reports — November 2025 survey](https://advocacy.consumerreports.org/press_release/new-survey-from-consumer-reports-finds-majority-of-households-strained-by-energy-bills-concerned-over-data-centerss-impact-on-bills), [White House — Ratepayer Protection Pledge announcement](https://www.whitehouse.gov/releases/2026/03/president-trump-secures-historic-commitment-to-keep-electricity-costs-down-amid-data-center-boom/), [White House — Ratepayer Protection Pledge signatories and terms](https://www.whitehouse.gov/ratepayer-protection-pledge/), [McGuireWoods — Texas SB6 large-load rules](https://www.mcguirewoods.com/client-resources/alerts/2025/7/texas-senate-bill-6-significantly-expands-regulatory-oversight-over-large-loads-in-ercot/), [Virginia Mercury — Dominion rate case, new data-center rate class](https://virginiamercury.com/2025/11/25/scc-approves-chesterfield-gas-plant-and-dominion-rate-hike-creates-new-rate-class-for-data-centers/), [New Project Media — BPA capacity and data center load](https://newprojectmedia.com/interview-bonneville-power-administration-executives-discuss-new-projects-being-connected-to-grid-in-next-two-years/)*

