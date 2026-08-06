# Meta's Hyperion: $50 Billion, 5 Gigawatts, 3,200 Acres — The Scale of AI Infrastructure in 2026

> Meta announced a $50 billion expansion of its Hyperion data center in Richland Parish, Louisiana on July 13, 2026, scaling to 5 gigawatts of compute capacity across 3,200 acres. Here is what this infrastructure investment signals for builders working with Meta's AI platform.


Meta [announced on July 13, 2026](https://www.cnbc.com/2026/07/13/meta-louisiana-data-center-investment-reaches-50-billion-amid-ai-push.html) that it is expanding its Hyperion data center in Richland Parish, Louisiana to **5 gigawatts** of compute capacity at a total investment of [**$50 billion**](https://about.fb.com/news/2026/07/teachers-local-businesses-win-as-meta-expands-louisiana-data-center/) — a five-fold increase from the original $10 billion commitment.

This is part of our **[Builder's Log](/builders-log/)**.

The infrastructure numbers are worth holding for a moment before moving on to implications.

---

## The Scale

**Site:** [Richland Parish, northeast Louisiana](https://datacenters.atmeta.com/richland-parish-data-center/)  
**Name:** Hyperion  
**Total investment:** [$50 billion](https://about.fb.com/news/2026/07/teachers-local-businesses-win-as-meta-expands-louisiana-data-center/) (up from original $10B commitment; previously reported at [$27B in October 2025](https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/), when Meta and Blue Owl Capital formed a joint venture to fund the campus)  
**Compute capacity:** [5 gigawatts](https://datacenters.atmeta.com/richland-parish-data-center/)  
**Site footprint:** [3,200+ acres — more than four times the size of Central Park](https://www.globaldatacenterhub.com/p/meta-scales-hyperion-to-5gw-and-over)  
**Operational completion:** [2036](https://kpel965.com/meta-hyperion-data-center-expansion-richland/) (first 2 GW online by 2030, full 5 GW around 2032, both phases fully operational by 2036)  

**Power infrastructure:** Entergy is constructing [ten new natural gas-fired power plants](https://fortune.com/2026/03/27/meta-hyperion-10-gas-power-plants-louisiana-entergy/) — roughly 7.5 gigawatts of new generating capacity — plus solar and battery storage to supply Hyperion's expansion. That capacity is [more than six times the peak power demand of the city of New Orleans](https://www.ucs.org/about/news/louisiana-regulators-fast-track-7-gas-plant-proposal-meta-data-center).

**Job creation:** [7,500 construction jobs at peak](https://datacenters.atmeta.com/richland-parish-data-center/) (50% increase from original plans, per [ConstructConnect](https://news.constructconnect.com/meta-expands-louisiana-data-center-to-5gw-lifts-richland-parish-investment-above-50-billion)); [1,000 permanent operational roles](https://datacenters.atmeta.com/richland-parish-data-center/) when both phases are running.

**Community commitments:** [$1 billion for local roads, water, and wastewater infrastructure](https://about.fb.com/news/2026/07/teachers-local-businesses-win-as-meta-expands-louisiana-data-center/); [$5 million to Louisiana Delta Community College](https://www.knoe.com/2026/07/13/meta-donates-5m-louisiana-delta-community-college-scholarships/) for data-center-career scholarships; [$250,000 to a New Orleans nonprofit providing technical training to high schoolers](https://kpel965.com/meta-hyperion-data-center-expansion-richland/), reported as the New Orleans Career Center.

---

## What This Tells Builders

**The hyperscalers are pricing in decade-long AI demand.** A data center with full operational completion in 2036 is infrastructure planned for a world where AI compute demand is not only sustained through the 2030s but grows substantially. This is not a hedge. Meta is committing land, capital, and power contracts a decade out.

That 2036 date is significant in another way. When enterprise buyers ask whether AI is a durable infrastructure investment or a transient cycle, Hyperion is part of the industry answer. No company spends $50 billion on infrastructure it expects to be redundant in five years.

**5 gigawatts is a new benchmark for scale.** For context: a [typical hyperscale data center draws in the tens to low hundreds of megawatts](https://www.congress.gov/crs-product/R48646). Even Microsoft's largest AI buildout, the multi-site "Fairwater" campus in Mount Pleasant, Wisconsin, is [projected to reach 3.3 gigawatts by 2027](https://epoch.ai/data-insights/fairwater-power-usage) as later buildings come online. Hyperion at 5 GW, concentrated on one site, is still a category of its own.

The power constraint is already real. Entergy is [building ten new natural gas plants](https://fortune.com/2026/03/27/meta-hyperion-10-gas-power-plants-louisiana-entergy/) to serve Hyperion. AI infrastructure is now directly driving power plant construction in the United States. For builders, the downstream implication is that energy cost and availability will be a growing factor in AI inference pricing, particularly for workloads that run at scale.

**Meta's AI platform is the downstream beneficiary.** Meta has not specified which models or services will run on Hyperion's expanded capacity. But the company's publicly available AI infrastructure — the [Llama model family](/builders-log/meta-cloud-api-llama-inference-zuckerberg-on-the-table/), Meta AI, and the inference API — are all compute-bound. A 5-gigawatt facility in the long run means more headroom for API throughput, lower inference costs relative to capacity, and continued ability to release progressively larger open-weight models.

For builders using Meta's Llama API, Hyperion is the infrastructure context behind the platform's availability commitments.

---

## How Hyperion Fits the Broader Infrastructure Race

Meta's Hyperion expansion is the latest data point in a hyperscaler infrastructure arms race that has been accelerating through 2026:

- **Nvidia** [reclaimed $5 trillion market capitalization](https://www.cnbc.com/2026/04/24/nvidia-stock-closes-at-record-pushing-market-cap-past-5-trillion.html) as the primary chip beneficiary of this compute buildout
- **SambaNova** [raised $1 billion at an $11 billion valuation](https://www.generalatlantic.com/media-article/sambanova-completes-first-close-of-1-billion-financing-at-11-billion-valuation/) for the [SN50 RDU chip](/builders-log/sambanova-1b-sn50-rdu-agentic-inference-jpmorgan-nvidia-alternative-builder-guide/), which SambaNova [says targets inference at 5x B200 speed](https://sambanova.ai/blog/introducing-the-sn50-rdu-purpose-built-for-agentic-inference)
- **Microsoft** is building its own multi-gigawatt "Fairwater" AI campuses — [Wisconsin alone is projected to reach 3.3 GW by 2027](https://epoch.ai/data-insights/fairwater-power-usage) — as part of its OpenAI compute provisioning
- **Amazon** [announced a $12 billion Louisiana data center campus](https://www.opportunitylouisiana.gov/news/amazon-selects-louisiana-for-12-billion-data-center-campuses-in-major-u-s-expansion) earlier this year
- **Anthropic** [pays up to $1.25 billion monthly for xAI's Colossus compute capacity](https://techcrunch.com/2026/05/20/anthropic-will-pay-xai-1-25-billion-per-month-for-compute/), without owning the underlying hardware

Meta's ownership of Hyperion is a different strategic posture. The company is not renting capacity from cloud providers for its AI workloads — it is building its own. This is the same vertically integrated infrastructure strategy that gives Google its cost advantage: own the silicon path, own the data center, own the interconnect.

That vertical integration matters for builders because it is the mechanism behind Meta's ability to offer Llama inference at competitive prices. When a company owns its entire compute stack, it can price API access at marginal cost rather than paying hyperscaler margins.

---

## The Power Transition Risk

Hyperion's power infrastructure is primarily natural gas. [Ten new gas plants are being built](https://fortune.com/2026/03/27/meta-hyperion-10-gas-power-plants-louisiana-entergy/) to supply it.

This creates a regulatory exposure that has no equivalent in typical software infrastructure. Louisiana's industrial economy is already facing climate policy pressure, and a $50 billion facility with decade-long power contracts is a target for state and federal emission accounting. If natural gas costs or regulatory burdens increase materially between now and 2036, Hyperion's operating cost structure changes.

For builders, this risk is not actionable in the short term. But the pattern of hyperscale data centers locking in decade-long power contracts with fossil fuel plants is one that regulators, climate policy advocates, and eventually enterprise ESG frameworks will scrutinize. The conversation about AI's energy footprint is not separate from the conversation about AI infrastructure investment — they are the same conversation.

---

## What to Watch

- **Llama API pricing**: If Hyperion phases come online ahead of schedule, watch for Meta to announce expanded inference capacity and potential price reductions in the Llama API.
- **Open-weight model releases**: A 5-gigawatt training and inference facility implies Meta has headroom for significantly larger open-weight model training runs. Watch for Llama 5 announcements.
- **Power contract scrutiny**: Watch for Louisiana legislative or federal regulatory attention to Hyperion's natural gas supply chain, particularly if the EU AI Act's carbon footprint provisions are cited in global governance discussions.
- **Competitive response**: Google and Microsoft will treat the Hyperion commitment as a capacity signal. Announcements matching or exceeding this scale in the next 18 months are likely.

---

*Sources: [Meta Newsroom](https://about.fb.com/news/2026/07/teachers-local-businesses-win-as-meta-expands-louisiana-data-center/), [Meta Data Centers](https://datacenters.atmeta.com/richland-parish-data-center/), [CNBC](https://www.cnbc.com/2026/07/13/meta-louisiana-data-center-investment-reaches-50-billion-amid-ai-push.html), [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/meta-expands-colossal-hyperion-ai-supercluster-plans-to-5gw-pushes-louisiana-investment-past-usd50-billion-as-ai-race-accelerates-says-it-plans-to-invest-over-usd1-billion-in-local-infrastructure-improvements), [The Hill](https://thehill.com/policy/technology/5965840-meta-louisiana-datacenter-expansion/), [Fortune](https://fortune.com/2026/07/13/meta-hyperion-louisiana-50-billion-tax-breaks-locals/) — Meta Hyperion announcement July 13, 2026.*

