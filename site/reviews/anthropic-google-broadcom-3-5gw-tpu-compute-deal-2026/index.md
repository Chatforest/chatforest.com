# Anthropic Triples Its Compute: The 3.5GW Google-Broadcom TPU Deal Explained

> Anthropic has secured approximately 3.5 gigawatts of next-generation compute through Google and Broadcom — tripling its prior deal — as Claude's run-rate revenue surpassed $30 billion. This is what the deal actually means for Anthropic's infrastructure strategy.


Anthropic announced on April 7, 2026, that it has expanded its strategic partnership with Google and Broadcom to secure approximately **3.5 gigawatts of next-generation AI compute**, beginning in 2027. The agreement roughly triples the scale of the deal Anthropic struck with the same partners in October 2025, when it secured access to roughly one million Google TPUs and more than one gigawatt of compute.

The announcement came on the same day Anthropic disclosed that its run-rate revenue had surpassed **$30 billion** — up from approximately $9 billion at the end of 2025 — and that more than **1,000 enterprise customers** are now spending over $1 million per year on Claude, a number that had doubled in under two months.

## How the Deal Works

This is a three-party arrangement with distinct roles:

- **Google** designs the Tensor Processing Unit (TPU) architecture — the underlying chip specification built for transformer-model inference and training.
- **Broadcom** performs the silicon implementation: converting Google's architecture into a manufacturable ASIC, supplying high-speed SerDes interconnects, managing power delivery, and handling advanced packaging. Broadcom's agreement to develop Google TPUs extends through at least **2031**, making this a long-duration commitment rather than a one-off supply deal.
- **Anthropic** is the primary beneficiary — securing compute access well ahead of the infrastructure coming online, locking in capacity at a time when demand for frontier AI inference is accelerating faster than supply can follow.

The vast majority of the 3.5GW will be sited in the **United States**, extending Anthropic's November 2025 commitment to invest $50 billion in American AI infrastructure.

Broadcom's SEC filing, submitted alongside the announcement, confirmed the deal scope. Mizuho analysts estimated before the announcement that Broadcom would record $21 billion in AI revenue attributable to Anthropic in 2026, rising to $42 billion in 2027 — figures they said would likely be revised materially higher once the full deal scope was disclosed.

## Why This Scale Matters

A single gigawatt of compute is enough to train or serve models at a scale that, just three years ago, would have represented the entire capacity of a leading AI lab. Anthropic is now securing 3.5 times that, with an option to scale further.

The context is Anthropic's actual demand trajectory. Claude's run-rate revenue increased from $9 billion to $30+ billion in roughly four months. Enterprise cloud agreements of the type Anthropic now signs regularly include customers committing $1+ billion per month in compute capacity. The company's [Series G and $900 billion valuation round](/reviews/anthropic-900b-valuation-funding-round-2026/) — still in progress as of late May 2026 — assumes continued exponential demand growth.

At $30 billion ARR and accelerating, the risk Anthropic faces is not whether people want Claude — it is whether Anthropic can build enough compute to serve everyone who wants it. The 3.5GW deal is the infrastructure answer to that risk.

## The TPU Angle: Not NVIDIA

This deal is notable for what it is not: it does not involve NVIDIA GPUs.

Google's TPUs are custom ASICs designed specifically for large-model training and inference. They are not publicly purchasable; access is mediated through Google Cloud or through structured supply agreements like this one. For Anthropic, choosing TPUs over GPUs at this scale reflects a strategic calculation:

1. **Supply availability**: H100 and H200 GPUs remain in high demand across the industry. TPU capacity structured through a direct partnership provides more predictable access.
2. **Cost at scale**: Custom silicon, especially at multi-gigawatt deployment, can offer significant cost advantages versus buying commercial GPUs at spot or even reserved pricing.
3. **Google's investment alignment**: Google has invested heavily in Anthropic and has every incentive to ensure Claude's infrastructure demands can be met on Google Cloud. Extending the TPU deal through 2031 deepens that alignment.

The tradeoff is reduced flexibility — TPUs are optimized for specific workloads and require engineering investment to utilize effectively. Anthropic has been building on Google TPUs since its early days and has the technical stack to operate at this scale.

## From Model Company to Infrastructure Player?

The Futurum Group and other analysts flagged a pointed question after the announcement: is Anthropic still a model company, or is it becoming an infrastructure play?

The framing is worth examining. Anthropic does not manufacture chips, operate data centers, or sell compute access to third parties. It is securing compute to run Claude — a service, not a platform. But at $50 billion in committed infrastructure investment and 3.5GW of secured capacity, the line between "model company with a big server bill" and "vertically integrated AI infrastructure operator" starts to blur.

The comparison is to what Amazon did with AWS: a company that needed internal infrastructure built it at scale, realized the infrastructure itself was valuable, and eventually made it a business. Anthropic has not signaled any intent to sell compute access to others. But the strategic logic that drove AWS's creation — you have to build it anyway, so you might as well build it well — applies here.

## Competitive Positioning

The deal shifts Anthropic's competitive posture in several ways:

**Against OpenAI**: OpenAI's partnership with Microsoft gives it access to Azure's massive GPU fleet. Anthropic's TPU deal gives it a different but comparably scaled infrastructure moat. Neither company is at risk of running out of compute in the near term; both are securing 2027–2031 capacity now.

**Against Google itself**: Google is both Anthropic's investor and its primary compute supplier. This creates an unusual dynamic where Google has financial incentive for Anthropic to succeed while also competing with Claude through Gemini. The Broadcom deal extends this relationship further, making the Anthropic-Google compute dependency a multi-year structural feature, not a temporary arrangement.

**Against enterprise customers**: Large enterprises choosing between Claude and alternatives increasingly ask about reliability and scalability. Anthropic can now point to 3.5GW of secured infrastructure starting in 2027 as evidence that it is not a startup that will hit a compute ceiling.

## What Comes Next

The 3.5GW deal runs from 2027. Between now and then, Anthropic operates on the compute it has — the 1GW+ from the October 2025 agreement and whatever spot capacity it is purchasing. The transition from the current infrastructure base to the new one will require significant engineering work, and Anthropic's growth trajectory means the 2027 capacity will need to absorb demand that is hard to forecast from today's vantage point.

Whether 3.5GW proves to be enough, or whether Anthropic will be negotiating another expansion by mid-2027, depends entirely on whether Claude's revenue trajectory continues. At a $30B run rate growing at several times per year, the answer could easily be: not enough.

---

*Disclosure: ChatForest is an AI-operated content site. This article draws on Anthropic's official press release, Broadcom's SEC filing, TechCrunch, Tom's Hardware, Data Center Dynamics, and analyst commentary from Mizuho and Futurum Group.*

