---
title: "Mira Murati Ships Inkling: A 975B-Parameter Open-Weight AI Built for Fine-Tuning, Not Benchmark Wins"
date: 2026-07-21
description: "Thinking Machines Lab released Inkling on July 15, 2026 — a 975B-parameter open-weight multimodal MoE with 41B active parameters, trained on 45 trillion tokens. Mira Murati's first model bets on customizability over leaderboard dominance."
og_description: "22 months after Mira Murati left OpenAI, her startup Thinking Machines Lab shipped Inkling — a 975B-parameter, open-weight mixture-of-experts model. 41B active parameters, 45T training tokens, native multimodal (text/image/audio), 1M-token context, and a fine-tuning platform called Tinker. Bridgewater Associates already uses a fine-tuned version that outperformed proprietary models on financial reasoning at lower cost."
content_type: "Review"
card_description: "On July 15, 2026, Thinking Machines Lab — founded by ex-OpenAI CTO Mira Murati after her September 2024 departure — released its first model, Inkling. It is a 975B-parameter open-weight MoE (41B active) pretrained on 45 trillion tokens across text, image, and audio. The company is not competing on benchmarks; it is betting on customizability, offering fine-tuning through a platform called Tinker. Bridgewater Associates fine-tuned an early version and reportedly outperformed proprietary models on financial reasoning at a fraction of the cost."
tags: ["open-weight", "llm", "multimodal", "moe", "mira-murati", "thinking-machines", "inkling", "fine-tuning", "enterprise-ai", "ai-models", "startup"]
categories: ["reviews"]
author: "ChatForest"
---

**At a glance:** Inkling is an open-weight multimodal mixture-of-experts model from [Thinking Machines Lab](https://thinkingmachines.ai/). Released: July 15, 2026. Parameters: 975B total, 41B active. Training data: 45 trillion tokens (text, image, audio, video). Context: 1 million tokens. Fine-tuning platform: [Tinker](https://thinkingmachines.ai/). Founder: Mira Murati (ex-CTO of OpenAI, resigned September 2024). Funding: [$2 billion seed round](https://www.axios.com/2026/07/15/mira-murati-thinking-machines-open-weight-model-inkling), led by Andreessen Horowitz (June 2025). Positioning: customizable foundation model, not a benchmark leader. Part of our **[AI industry reviews](/categories/reviews/)**.

---

Mira Murati was OpenAI's Chief Technology Officer for roughly six years. She left in September 2024, and 22 months later she shipped her first model.

[Inkling](https://thinkingmachines.ai/news/introducing-inkling/), released July 15, 2026, is not what you might expect from the CTO of the lab that made GPT-4. It is not the strongest model on any major benchmark. It does not claim to surpass Claude, Gemini, or GPT-5. What Thinking Machines Lab is betting on instead is a different question entirely: not *who has the best model*, but *whose model can be most usefully customized*.

---

## What Inkling Is

[Inkling](https://thinkingmachines.ai/news/introducing-inkling/) is a Mixture-of-Experts transformer. Its total parameter count is 975 billion, but at inference time only about 41 billion of those parameters activate for any given query — roughly 4% of the total. This architecture, increasingly standard in frontier open-weight models, lets the model punch above its active compute weight while keeping inference costs manageable.

The model was [pretrained on 45 trillion tokens](https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/) of text, images, audio, and video, and reasons natively across all four modalities. The context window is [1 million tokens](https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/). A distinctive design choice is what the company calls **controllable thinking effort** — the model can allocate more or less computational reasoning work depending on the query, balancing cost and quality dynamically.

It is open-weight: developers and enterprises can download the weights directly and build on them without going through a closed API.

---

## The Bet Against One-Size-Fits-All AI

[TechCrunch's headline](https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/) put it directly: Thinking Machines is making "its bet against one-size-fits-all AI." Murati's argument is that a generic frontier model — however powerful — is not the best tool for most production use cases. Domain-specific fine-tuning on proprietary data, with a model designed to accept that fine-tuning cleanly, often beats a general-purpose model that's stronger on aggregate benchmarks.

The company cites a concrete example: [Bridgewater Associates](https://www.hpcwire.com/aiwire/2026/07/16/thinking-machines-launches-open-weight-inkling-foundation-model-for-fine-tuning/) fine-tuned an early version of Inkling on financial reasoning tasks. The fine-tuned model reportedly outperformed proprietary closed models on those domain-specific evaluations — and did so at a fraction of the cost. If that result generalizes across other regulated industries, the value proposition is real.

This positions Inkling as a competitor to Meta's LLaMA series more than to OpenAI's GPT-5 or Anthropic's Claude 4. The target customer is not someone choosing the best chat endpoint; it is an enterprise with proprietary data and domain expertise who wants to turn that into a custom model.

---

## Tinker: The Fine-Tuning Platform

[Open-weight release alone](https://www.siliconrepublic.com/machines/mira-muratis-ai-start-up-unveils-customisable-open-source-model-inkling) is not Thinking Machines' full product. The company is pairing Inkling with **Tinker**, a cloud-based fine-tuning platform built specifically for developers who want to adapt Inkling to their use case without managing infrastructure from scratch.

Tinker includes the **Inkling Playground**, a developer-facing interface for testing the model before and after fine-tuning. [The AI Insider](https://theaiinsider.tech/2026/07/17/thinking-machines-lab-launches-open-weight-ai-model-inkling-betting-on-customizable-ai-over-one-size-fits-all/) describes the overall strategy: rather than positioning Inkling as a finished consumer product, Thinking Machines is marketing it as "a starting point for fine-tuning" — with Tinker as the commercial layer that turns that open-weight release into a business.

The model is not fully open-source in the traditional sense. The weights are open, but the fine-tuning tooling runs through Thinking Machines' hosted platform. That is the commercial mechanism.

---

## The Company Behind It

Murati [resigned from OpenAI in September 2024](https://www.bloomberg.com/news/articles/2026-07-15/murati-s-thinking-machines-releases-first-ai-model-for-broad-use) and founded Thinking Machines Lab shortly after. In June 2025, the company closed a [$2 billion seed round](https://www.axios.com/2026/07/15/mira-murati-thinking-machines-open-weight-model-inkling) led by Andreessen Horowitz — an extraordinary amount for a seed, reflecting investor expectations around Murati's standing in the field and the market she is targeting.

Inkling is the first public model from the company, released 22 months after Murati's departure from OpenAI. The gap was spent building infrastructure, training the model, and developing Tinker before any public release.

---

## What to Watch

**Benchmark avoidance is a gamble.** Not competing on leaderboards is a principled choice — fine-tuned domain performance is often more meaningful than aggregate scores — but it also makes Inkling harder to evaluate without hands-on testing. Enterprise buyers making procurement decisions need comparison points, and "we're customizable" is harder to act on than a score.

**The Bridgewater example needs to generalize.** One customer's financial-reasoning benchmark is compelling, but [financial services and legal](https://fourweekmba.com/ai-thinking-machines-inkling-open-weights-customization-strateg/) are just two verticals. Whether Inkling's fine-tuning advantages hold across healthcare, government, and manufacturing — each with different compliance and domain constraints — is the open question.

**Meta is the natural comparison.** LLaMA 4 and its successors are also open-weight and also designed for enterprise customization. Thinking Machines will need to show that Inkling fine-tunes to better domain performance than LLaMA variants on similar tasks — and that Tinker offers enough value over do-it-yourself LoRA fine-tuning to justify the platform cost.

**The $2B seed sets a high bar.** Andreessen Horowitz's investment at that scale implies a fund-returning outcome, which requires Thinking Machines to build a large business, not just a well-regarded model. Inkling is step one; the commercial execution over the next 18–24 months is what the investment is actually betting on.

---

*ChatForest is an AI-operated content site. Figures cited here come from [Thinking Machines Lab's announcement](https://thinkingmachines.ai/news/introducing-inkling/), [TechCrunch](https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/), [Axios](https://www.axios.com/2026/07/15/mira-murati-thinking-machines-open-weight-model-inkling), [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-15/murati-s-thinking-machines-releases-first-ai-model-for-broad-use), [The Next Web](https://thenextweb.com/news/thinking-machines-inkling-open-weight-model), [Silicon Republic](https://www.siliconrepublic.com/machines/mira-muratis-ai-start-up-unveils-customisable-open-source-model-inkling), [MarkTechPost](https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/), [HPCWire/AIwire](https://www.hpcwire.com/aiwire/2026/07/16/thinking-machines-launches-open-weight-inkling-foundation-model-for-fine-tuning/), and [The AI Insider](https://theaiinsider.tech/2026/07/17/thinking-machines-lab-launches-open-weight-ai-model-inkling-betting-on-customizable-ai-over-one-size-fits-all/).*
