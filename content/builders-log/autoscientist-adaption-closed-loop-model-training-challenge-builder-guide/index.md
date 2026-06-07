---
title: "AutoScientist: Adaption's Closed-Loop Model Training Tool and the $50K Challenge — Builder Guide"
date: 2026-06-08
description: "Adaption's AutoScientist launched a $50K challenge today (June 8–July 6) for builders who specialize open-source models on real-world domains. Here's how the closed-loop co-optimization works, how to get started on Together AI, and what the prize structure means for your roadmap."
og_description: "Adaption AutoScientist: closed-loop data + training co-optimization built on Together AI. $50K challenge launches June 8. Specialize an 8B model to outperform GPT-4 on your domain. Builder guide inside."
content_type: "Builder's Log"
categories: ["Developer Tools", "AI Training", "Open Source"]
tags: ["autoscientist", "adaption", "sara-hooker", "fine-tuning", "together-ai", "closed-loop-training", "model-specialization", "synthetic-data", "builder-challenge", "open-source", "builder-guide"]
---

Adaption opened the AutoScientist Challenge today, June 8, 2026. The prize pool is $50,000. The challenge runs in two parts through July 6. The tool behind it — AutoScientist — is worth understanding regardless of whether you compete.

---

## What AutoScientist Is

AutoScientist is an automated fine-tuning system from [Adaption](https://adaption.ai/), a San Francisco startup co-founded by Sara Hooker and Sudip Roy. Hooker was VP of Research at Cohere and before that ran a research lab at Google Brain. Roy was Director of Inference at Cohere. Their thesis is that the next leverage point in AI is not bigger models but smarter training.

The problem AutoScientist addresses is concrete: specializing a model for a specific domain requires co-optimizing two things simultaneously — the training data and the training recipe. Human ML engineers run these as separate iterative loops, which is slow and expensive. AutoScientist closes that loop.

**The core mechanism:**

AutoScientist runs an automated closed loop in which both data selection and training hyperparameters are continuously adjusted together. It continues until performance on your defined objective stabilizes. The practical result: a specialized model trained on co-optimized synthetic data, tuned to your task, without a team of ML engineers running experiments across weeks.

Adaption's own benchmarks show AutoScientist raises win rates from 48% to 64% against configurations designed by experienced AI researchers. The bottleneck being replaced is not just time — it is the implicit knowledge of how data composition interacts with training dynamics, which AutoScientist treats as a learnable variable.

---

## Infrastructure: Together AI Underneath

AutoScientist does not require you to provision GPU infrastructure. It runs on top of [Together AI's](https://www.together.ai/) fine-tuning service.

Supported models at launch include large-scale open weights:

| Model | Parameter Scale | Notes |
|---|---|---|
| Kimi K2.5 | ~100B+ MoE | Strong on reasoning and code |
| GLM 5.1 | ~100B+ | General-purpose, multilingual |
| Qwen 3.5-397B | 397B MoE | Large-scale multilingual MoE |

Together AI's partnership announcement with Adaption specifically calls out support for "large models exceeding 100B parameters" — meaning AutoScientist is not just for small specialized models. You can start with a lean 8B or go up to a 397B MoE depending on your budget and task requirements.

**Pricing:** AutoScientist is in a 30-day free trial period. Compute costs pass through from Together AI.

---

## The AutoScientist Challenge

The challenge runs in two back-to-back parts, each two weeks:

### Part 1 — June 8–22
Domains:
- Finance
- Healthcare
- Math and Code
- Legal
- Marketing

### Part 2 — June 23–July 6
Domains:
- Science
- Agriculture
- Data Visualization
- Language
- All Other Domains

**Prize pool:** $50,000 total.

**What they're asking for:** Specialized models that outperform standard baselines on the domain task, with both weights and datasets released publicly. The public release requirement is structural — Adaption's model is to advance the open-source AI ecosystem, not to extract proprietary artifacts.

---

## The Builder Case for Closed-Loop Training

The standard fine-tuning workflow has three components you tune separately: which data to include, how to weight or filter that data, and what training hyperparameters to use. Engineers run experiments across all three, wait for results, adjust, and repeat. The cycle is measured in days to weeks.

AutoScientist treats the data distribution and the training configuration as jointly optimized variables. Synthetic data generation patches the scarcity problem — if you don't have domain data, the system reasons from first principles to generate it. The result is a tighter feedback loop that converges on a usable model faster.

The claim that a developer can take an 8B model and turn it into a specialized engine that outperforms GPT-4 on a specific task, in an afternoon, is not a marketing abstraction — it is a restatement of what closed-loop co-optimization enables when the task is narrow enough. A general-purpose model carries the cost of generality. A model trained specifically for, say, extracting medical claims from clinical notes does not need to write poetry. Narrow scope means the training budget goes entirely to the target distribution.

---

## Who Should Try This

**Strong fit:**
- Builders with a well-defined, narrow task and measurable output quality (F1, accuracy, BLEU, task-specific metric)
- Teams currently spending engineer-weeks on fine-tuning iterations
- Builders in the challenge domains (finance, healthcare, legal, math/code) who want both a potential prize and a production-quality specialized model
- Open-source contributors who want to release domain-specialized weights

**Weaker fit:**
- Tasks where the quality criterion is hard to define (e.g., "sounds professional")
- Projects that need deployment infrastructure, not just training — AutoScientist gets you a model; serving is separate
- Builders whose task changes frequently — specialized models need retraining when the target distribution shifts

---

## Sara Hooker's Framing

Hooker has been consistent since Cohere: compute efficiency and data quality matter more than scale, for most real-world applications. AutoScientist is the practical implementation of that position. The $50M the company has raised reflects investor agreement that there is a durable market for this view even as frontier labs push model scale upward.

Her research background is specifically relevant here. At Google Brain, she worked on model compression, efficient inference, and evaluation methodology. AutoScientist's closed-loop approach is directly descended from that work — the insight that you can automate the human judgment loop in training is a natural extension of automating the human judgment loop in compression.

---

## Getting Started

AutoScientist is in a 30-day free period. To enter the challenge:

1. Visit [adaption.ai](https://adaption.ai/) and create an account
2. Connect a Together AI account (or create one — Together offers credits for new users)
3. Pick a domain from Part 1 (Finance, Healthcare, Math/Code, Legal, Marketing)
4. Define your task and your evaluation metric
5. Let AutoScientist run the co-optimization loop
6. Evaluate the output model against your baseline
7. Submit before June 22 for Part 1 consideration

The public release requirement (weights + dataset) is not optional for the prize, but it is the right call for most builders anyway. Open-weight releases generate documentation, bug reports, and downstream use cases that improve the model. If your specialized task is genuinely proprietary, the prize structure is not a fit — but the tool still is.

---

## What to Watch

The AutoScientist Challenge's public-release requirement will produce a growing catalog of specialized domain models over the next four weeks. Regardless of whether you compete, tracking the submissions will show you what closed-loop co-optimization produces on real-world tasks — and what the performance ceiling looks like for each domain.

If the pattern holds from earlier specialized fine-tuning work (including Hooker's own research), the cleaner and narrower the task definition, the more pronounced the quality advantage over a general-purpose baseline. The challenge results will be a practical data set on where that pattern breaks down.
