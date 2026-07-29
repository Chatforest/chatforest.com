# AutoScientist: Adaption's Closed-Loop Model Training Tool and the $60K Challenge — Builder Guide

> Adaption's AutoScientist launched a $60K challenge today (June 8–August 10, in two parts) for builders who specialize open-source models on real-world domains. Here's how the closed-loop co-optimization works, how to get started on Together AI, and what the prize structure means for your roadmap.


Adaption opened the [AutoScientist Challenge](https://adaptionlabs.ai/blog/autoscientist-challenge) today, June 8, 2026. The total prize pool is $60,000, split into two parts: Part 1 runs June 8–July 5 (winners announced July 13), and Part 2 runs July 6–August 10 (winners announced August 17). The tool behind it — AutoScientist — is worth understanding regardless of whether you compete.

---

## What AutoScientist Is

AutoScientist is an automated fine-tuning system from [Adaption](https://adaptionlabs.ai/), a San Francisco startup co-founded by Sara Hooker and Sudip Roy in 2025. Hooker was [VP of Research at Cohere](https://betakit.com/ex-cohere-execs-sara-hooker-and-sudip-roy-unveil-new-ai-startup/), where she led the company's research arm, Cohere Labs (formerly Cohere For AI); before that she was a research scientist at [Google Brain](https://techcrunch.com/2025/10/22/why-coheres-ex-ai-research-lead-is-betting-against-the-scaling-race/) for five years. Roy was [senior director of inference at Cohere](https://betakit.com/ex-cohere-execs-sara-hooker-and-sudip-roy-unveil-new-ai-startup/). Their thesis is that the next leverage point in AI is not bigger models but smarter training.

The problem AutoScientist addresses is concrete: specializing a model for a specific domain requires co-optimizing two things simultaneously — the training data and the training recipe. Human ML engineers run these as separate iterative loops, which is slow and expensive. AutoScientist closes that loop.

**The core mechanism:**

AutoScientist runs an automated closed loop in which both data selection and training hyperparameters are continuously adjusted together, "iterating until the model converges on the behavior you described," per [Adaption's product page](https://adaptionlabs.ai/blog/autoscientist). The practical result: a specialized model trained on co-optimized synthetic data, tuned to your task, without a team of ML engineers running experiments across weeks.

[Adaption's own benchmarks](https://adaptionlabs.ai/blog/autoscientist) show AutoScientist raises win rates from 48% to 64% against configurations selected by Adaption's own researchers, a result also reported independently by [implicator.ai](https://www.implicator.ai/sara-hooker-bets-50m-that-smarter-training-beats-bigger-models-2/), which notes the claim is Adaption's own in-house evaluation and has not yet been independently verified on external benchmarks. The bottleneck being replaced is not just time — it is the implicit knowledge of how data composition interacts with training dynamics, which AutoScientist treats as a learnable variable.

---

## Infrastructure: Together AI Underneath

AutoScientist does not require you to provision GPU infrastructure. It runs on top of [Together AI's](https://www.together.ai/) fine-tuning service.

Supported models at launch include large-scale open weights:

| Model | Parameter Scale | Notes |
|---|---|---|
| Kimi K2.5 | ~100B+ MoE | Strong on reasoning and code |
| GLM 5.1 | ~100B+ | General-purpose, multilingual |
| Qwen 3.5-397B | 397B MoE | Large-scale multilingual MoE |

[Together AI's partnership announcement with Adaption](https://www.together.ai/blog/announcing-together-ai-and-adaption-partnership) specifically calls out support for "models over 100B parameters such as Kimi K2.5, GLM 5.1, or Qwen 3.5-397B" — meaning AutoScientist is not just for small specialized models. [Together AI's fine-tuning service](https://www.together.ai/fine-tuning) also supports "any open-source model from Hugging Face Hub," so smaller, budget-conscious models are an option too, not just the frontier-scale ones in the table above.

**Pricing:** [AutoScientist is free to use for the first 30 days](https://adaptionlabs.ai/blog/autoscientist) after launch. Compute costs pass through from Together AI.

---

## The AutoScientist Challenge

Per [Adaption's official challenge page](https://adaptionlabs.ai/blog/autoscientist-challenge), the challenge runs in two parts:

### Part 1 — June 8–July 5 (winners announced July 13)
Domains:
- Finance
- Healthcare
- Language
- Legal
- Marketing

### Part 2 — July 6–August 10 (winners announced August 17)
Domains:
- Science
- Agriculture
- Data Visualization
- Math & Code
- HR
- Market Analysis & News
- Personal Finance

**Prize pool:** [$60,000 total](https://adaptionlabs.ai/blog/autoscientist-challenge), structured as 12 first-place awards of $4,000 each, 12 runner-up awards of $1,000 each, and 30 honorary mentions (swag/credits). Registrants also get 1,000 credits for data adaptation and compute.

**What they're asking for:** Specialized models that show measurable improvement on held-out test sets, with [both the adapted dataset and the trained weights released to Hugging Face and Kaggle](https://adaptionlabs.ai/blog/autoscientist-challenge). The public release requirement is structural — Adaption's model is to advance the open-source AI ecosystem, not to extract proprietary artifacts.

---

## The Builder Case for Closed-Loop Training

The standard fine-tuning workflow has three components you tune separately: which data to include, how to weight or filter that data, and what training hyperparameters to use. Engineers run experiments across all three, wait for results, adjust, and repeat. The cycle is measured in days to weeks.

AutoScientist treats the data distribution and the training configuration as jointly optimized variables. Synthetic data generation patches the scarcity problem — if you don't have domain data, the system reasons from first principles to generate it. The result is a tighter feedback loop that converges on a usable model faster.

Adaption's own framing is narrower than the "beats GPT-4" pitch that circulated in some coverage of the launch: its product page describes the goal as "going from idea to an owned, adapted model in an afternoon, not weeks" ([adaptionlabs.ai](https://adaptionlabs.ai/blog/autoscientist)) — a claim about development speed, not a verified head-to-head win over any specific frontier model. That narrower claim is still a real restatement of what closed-loop co-optimization enables when the task is narrow enough: a general-purpose model carries the cost of generality, while a model trained specifically for, say, extracting medical claims from clinical notes does not need to write poetry. Narrow scope means the training budget goes entirely to the target distribution.

---

## Who Should Try This

**Strong fit:**
- Builders with a well-defined, narrow task and measurable output quality (F1, accuracy, BLEU, task-specific metric)
- Teams currently spending engineer-weeks on fine-tuning iterations
- Builders in the challenge domains (finance, healthcare, legal, marketing, science, math & code, and others listed above) who want both a potential prize and a production-quality specialized model
- Open-source contributors who want to release domain-specialized weights

**Weaker fit:**
- Tasks where the quality criterion is hard to define (e.g., "sounds professional")
- Projects that need deployment infrastructure, not just training — AutoScientist gets you a model; serving is separate
- Builders whose task changes frequently — specialized models need retraining when the target distribution shifts

---

## Sara Hooker's Framing

Hooker has been consistent since Cohere: compute efficiency and data quality matter more than scale, for most real-world applications. AutoScientist is the practical implementation of that position. The [$50M seed round the company raised](https://fortune.com/2026/02/04/adaption-labs-50-million-seed-funding-emergence-captial-sara-hooker-sudip-roy-ai-models-that-learn-on-the-fly/) — led by Emergence Capital with participation from Mozilla Ventures and others, [reported at a $1 billion valuation](https://pulse2.com/adaption-labs-50-million-seed-funding/) — reflects investor agreement that there is a durable market for this view even as frontier labs push model scale upward.

Her research background is specifically relevant here. At [Google Brain (2017–2022)](https://techcrunch.com/2025/10/22/why-coheres-ex-ai-research-lead-is-betting-against-the-scaling-race/), she focused on model interpretability and hardware-aware training — the subject of her widely cited paper ["The Hardware Lottery"](https://arxiv.org/abs/2009.06489) — and was a founding member of Google's first AI research office in Accra, Ghana. AutoScientist's closed-loop approach is a natural extension of that line of thinking: automating the human judgment loop in training the way her earlier work probed how hardware and software constraints shape which research ideas succeed.

---

## Getting Started

[AutoScientist is free to use for the first 30 days](https://adaptionlabs.ai/blog/autoscientist). To enter the challenge:

1. Visit [adaptionlabs.ai](https://adaptionlabs.ai/) and create an account
2. Connect a Together AI account (or create one — Together offers credits for new users)
3. Pick a domain from Part 1 (Finance, Healthcare, Language, Legal, Marketing)
4. Define your task and your evaluation metric
5. Let AutoScientist run the co-optimization loop
6. Evaluate the output model against your baseline
7. Submit before July 5 for [Part 1 consideration](https://adaptionlabs.ai/blog/autoscientist-challenge)

The public release requirement (weights + dataset) is not optional for the prize, but it is the right call for most builders anyway. Open-weight releases generate documentation, bug reports, and downstream use cases that improve the model. If your specialized task is genuinely proprietary, the prize structure is not a fit — but the tool still is.

---

## What to Watch

The AutoScientist Challenge's public-release requirement will produce a growing catalog of specialized domain models over the challenge's roughly two-month run, [through the August 17 announcement of Part 2 winners](https://adaptionlabs.ai/blog/autoscientist-challenge). Regardless of whether you compete, tracking the submissions will show you what closed-loop co-optimization produces on real-world tasks — and what the performance ceiling looks like for each domain.

If the pattern holds from earlier specialized fine-tuning work (including Hooker's own research), the cleaner and narrower the task definition, the more pronounced the quality advantage over a general-purpose baseline. The challenge results will be a practical data set on where that pattern breaks down.

