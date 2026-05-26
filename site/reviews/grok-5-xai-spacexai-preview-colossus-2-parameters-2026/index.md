# Grok 5 Is Coming. Here's What xAI's Gigawatt Gamble Is Building Toward.

> Grok 5 has missed two release windows and is still training on the world's first gigawatt-scale AI supercluster. With Q2 2026 as the official target, here's everything confirmed, rumored, and worth watching — and what the wait means for the frontier AI race.


Grok 5 was supposed to arrive in Q1 2026. Then Q2. As of late May, it is still training.

That is not, on its face, unusual. Frontier AI labs routinely miss internal timelines. What makes the Grok 5 situation notable is the infrastructure behind the delay: xAI is training Grok 5 on Colossus 2, the world's first gigawatt-scale AI training supercluster, a facility in Memphis, Tennessee that crossed the 1 gigawatt threshold in January 2026 and is targeting 1.5 gigawatts of continuous power draw by mid-year.

To put that in context: a gigawatt is roughly the output of a commercial nuclear reactor. Most data centers run on tens or hundreds of megawatts. The Colossus 2 facility is operating at a scale that has never been attempted before. Whatever Grok 5 turns out to be, its origin story starts with the largest, most power-intensive AI training infrastructure ever built.

Here is what we know — and what remains speculation.

---

## The Timeline That Has Not Held

xAI first signaled a Q1 2026 Grok 5 release. That window closed without a launch. On February 25, 2026, Grok's official X account updated the projection to Q2 2026. As of May 25, Q2 ends in 36 days.

Prediction market bettors — who tend to be calibrated on AI release timing — are giving roughly 33% odds that Grok 5 ships publicly before June 30. That is not bullish. For reference, xAI's own roadmap pointed to Q2, and the market is pricing meaningful probability it slips again.

The most likely explanation is that Colossus 2 is a new class of infrastructure, and training at that scale involves problems that smaller clusters have not encountered. A gigawatt of power means roughly 550,000 of Nvidia's GB200 or GB300 GPUs running simultaneously. Coordinating training across that many chips — managing memory bandwidth, minimizing idle time, handling hardware failures without losing training progress — is an unsolved engineering problem at that scale. xAI is solving it in real time.

---

## What the Specs Point Toward

The confirmed and reliably reported specifications describe a model that is meaningfully larger than anything currently deployed at public APIs:

**Scale:** Two variants are reportedly in training — a main 6-trillion-parameter model and a heavier 10-trillion-parameter variant. For context, current frontier models don't disclose their parameter counts, but the general understanding is that the leading public models are in the range of 1-2 trillion parameters. If Grok 5's numbers are accurate, it would be training at roughly 3-5x the scale of current competition.

**Architecture:** Mixture-of-Experts (MoE) — the same architecture used by Gemini 3.5 Flash, GPT-5.x, and most large-scale frontier models. MoE activates only a subset of parameters for any given forward pass, making trillion-parameter models computationally tractable despite their nominal size.

**Context window:** Rumored 1.5 million tokens. Current frontier leaders are clustered around 1 million (Claude Opus 4.7, Gemini 3.5 Flash). A 50% increase matters specifically for long-document, multi-file, and multi-session agent use cases.

**Multimodality:** Unlike earlier Grok versions where vision was added post-architecture, Grok 5 is reportedly multimodal from the ground up — text, images, audio, and real-time video with temporal reasoning (the ability to answer "what happened at this specific moment in the video"). Native multimodal training from day one typically produces better cross-modal understanding than retrofitted vision layers.

**X data advantage:** Grok has exclusive access to the full X firehose — real-time social data that no other model has at training or inference time. Whether this translates to meaningful benchmark advantages is unclear, but it is a structural input difference that compounds over time.

---

## What Would "Good" Look Like?

When Grok 5 launches — and current benchmarks will immediately be applied — here is the competitive context:

**Coding:** Claude Opus 4.7 currently sits at 87.6% on SWE-Bench Verified. GPT-5.5 Instant is at 88.7%. Gemini 3.5 Flash reaches 81.0% SWE-Bench at 4x the speed of competing models. For Grok 5 to be competitive, it needs to be at or above the 87–89% tier.

**Reasoning:** GPQA Diamond is the standard gauge. Claude Opus 4.7 and GPT-5.5 are in the low-to-mid 90s. Grok 5 needs to clear 90%+ to be taken seriously by the research community.

**Agentic tasks:** Terminal-Bench 2.1 (Gemini 3.5 Flash: 76.2%), MCP Atlas (Gemini 3.5 Flash: 83.6%). These are increasingly the benchmarks that matter for developers building autonomous agent systems. A Grok 5 score above 85% on MCP Atlas would be notable.

**Speed:** Grok 4.1 Fast currently sits at $0.20/$0.50 per million tokens — the cheapest frontier-class option on the market. Grok 5 will likely tier: a fast, cheaper variant (comparable to Grok 4.1 Fast) and a more capable, more expensive variant (comparable to Grok 4.x Heavy). If xAI can maintain competitive fast-tier pricing while jumping to Grok 5 capability, it changes the cost calculus for high-volume deployments.

---

## The SpaceXAI Context

xAI no longer exists as an independent entity. Following the February 2026 SpaceX acquisition and the May 6 formal dissolution of the xAI brand, Grok and X are now operated as the SpaceXAI division under SpaceX's corporate structure. Michael Nicolls, former Starlink VP, is now the division's president.

This matters for Grok 5 in two ways. First, the IPO clock is running: SpaceX filed its S-1 in May 2026, targeting a June 12 Nasdaq debut. Grok 5 launching before or during the IPO roadshow (June 4) would be a material positive for investor sentiment — it would demonstrate that the AI unit can ship. Second, Anthropic pays SpaceX $1.25 billion per month for compute access to the Colossus cluster. That contract means SpaceXAI has a revenue-generating reason to keep Colossus running at scale even during model training.

---

## What xAI Has Not Said

Grok 5 has no officially confirmed benchmark numbers. No API pricing. No confirmed architecture. No confirmed context window. The 6T parameter claim comes from multiple independent leaks, not xAI statements. The timeline has shifted twice without public explanation.

This information vacuum is notable for a company with Musk's profile — he typically broadcasts development progress publicly on X. The relative quiet around Grok 5 specifics suggests either a deliberate hold for dramatic launch-day impact, or that the model is not yet in a state where specific numbers would land favorably.

---

## What to Watch

**June 30:** Q2 2026 ends. If Grok 5 does not ship by then, the prediction market thesis (33% odds it ships by June 30) will have resolved against, and xAI will need to explain another miss.

**SpaceX IPO (June 12):** Grok 5 before or at the Nasdaq debut would be the optimal narrative moment. An IPO without a model launch is not a disaster, but it is a missed signal.

**Benchmark day:** When Grok 5 ships, the first 48 hours of external evaluations will define the narrative for months. The community response to Grok 4.3 (functional but not competitive at the top) will calibrate expectations cautiously.

---

*This article will be updated when Grok 5 officially launches. ChatForest researches AI models through public sources, reporting, and benchmark results — we do not have API access to pre-release models.*

