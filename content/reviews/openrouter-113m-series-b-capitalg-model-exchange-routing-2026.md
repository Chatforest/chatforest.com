---
title: "OpenRouter Raises $113M Series B as AI Token Volume Hits 25 Trillion Per Week"
date: 2026-05-27
description: "OpenRouter raised a $113 million Series B led by CapitalG on May 26, 2026, as weekly token volume surged 5x to 25 trillion in six months. The AI model exchange now connects 8 million users to 400+ models from Anthropic, Google, OpenAI, xAI, and DeepSeek through a single API."
og_description: "OpenRouter: $113M Series B, $1.3B valuation, 25T tokens/week (5x in 6 months), 400+ models, 8M users. CapitalG, NVIDIA, a16z backing enterprise AI routing infrastructure."
content_type: "Review"
card_description: "OpenRouter — the model exchange that routes traffic across Anthropic, Google, OpenAI, xAI, and DeepSeek — raised $113 million in a Series B on May 26, 2026. Weekly volume reached 25 trillion tokens, up fivefold from five trillion six months earlier. Valuation more than doubled to $1.3 billion. CapitalG (Alphabet's growth fund) led. NVIDIA Ventures, ServiceNow, MongoDB, Snowflake, Databricks, Andreessen Horowitz, and Menlo Ventures participated. The round reflects a structural shift: enterprises are locking in model-agnostic routing infrastructure rather than betting on a single provider."
tags: ["llm", "api", "developer-tools", "funding", "openrouter", "model-routing", "enterprise-ai", "inference", "multi-model", "anthropic", "openai", "google", "deepseek", "xai", "market-analysis"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
last_refreshed: 2026-05-27
sources_audited: 2026-07-29
---

OpenRouter [raised **$113 million in a Series B** on May 26, 2026](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/), as the AI model exchange reported weekly token volume of 25 trillion — a fivefold increase from five trillion tokens per week six months earlier.

[CapitalG, Alphabet's independent growth fund, led the round](https://www.businesswire.com/news/home/20260526953416/en/OpenRouter-Raises-$113-Million-CapitalG-led-Series-B-as-Weekly-Volume-Explodes-to-25T-Tokens). [NVentures (NVIDIA's venture capital arm)](https://www.nventures.ai/), ServiceNow Ventures, MongoDB Ventures, Snowflake Ventures, and Databricks Ventures joined as new investors, alongside existing backers Andreessen Horowitz and Menlo Ventures — [per OpenRouter's own Series B announcement](https://openrouter.ai/blog/announcements/series-b/). The post-money valuation landed at approximately $1.3 billion, more than double the [$547 million valuation from the company's $40 million Series A round, announced in June 2025](https://www.globenewswire.com/news-release/2025/06/25/3105125/0/en/OpenRouter-raises-40-million-to-scale-up-multi-model-inference-for-enterprise.html) — [a jump TechCrunch also reported](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/).

The company says it now serves more than **8 million users globally**, spanning individual developers and large enterprise organizations — [per its Series B announcement](https://openrouter.ai/blog/announcements/series-b/).

---

## What OpenRouter Does

[Founded in 2023](https://www.theblock.co/post/360093/opensea-co-founder-alex-atallah-raises-40-million-for-ai-startup-openrouter), OpenRouter sits between applications and AI providers. Its core product is a unified API layer that connects developers to [more than **400 models**](https://openrouter.ai/blog/announcements/series-b/) from providers including Anthropic (Claude), Google (Gemini), OpenAI (GPT), xAI (Grok), and DeepSeek, plus dozens of open-weight alternatives.

For most developers, that means a single API key and endpoint. For enterprises, [it means a control plane that handles](https://openrouter.ai/blog/announcements/series-b/):

- **Routing and failover** — automatically directing requests to available providers
- **Cost optimization** — selecting the cheapest qualifying model for each task
- **Governance** — per-request data policies, team-level permissions, audit logging, and vendor risk management
- **Usage controls** — spend limits, rate controls, and access reports

The platform [processes more than **100 trillion tokens per month** — roughly 25 trillion tokens per week — up from about 5 trillion tokens per week six months earlier](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/). At that run rate, [OpenRouter's own Series B announcement projects annual volume will exceed 1 quadrillion tokens](https://openrouter.ai/blog/announcements/series-b/).

---

## Why the Round Is Significant

The investor composition tells the story. [CapitalG is Alphabet's independent growth fund, not Google Ventures](https://www.capitalg.com/about/) — unlike Google's Corporate Development group, which invests strategically for Google's own product lines, [CapitalG invests for financial return, with Alphabet as its parent rather than a strategic sponsor](https://en.wikipedia.org/wiki/CapitalG). NVentures' participation signals that NVIDIA views model routing infrastructure as complementary to its GPU supply chain. The strategic corporate participation from MongoDB, Snowflake, Databricks, and ServiceNow reflects a broader pattern: these platforms integrate AI into their own products and want equity upside in the infrastructure they route workloads through.

The 5x volume growth in six months is not developer hobbyist activity. Production enterprise AI workloads generate that kind of token count. It indicates that companies have moved past experimentation and are routing real workloads through OpenRouter in production.

---

## Multi-Model as Default Architecture

OpenRouter's growth reflects an architectural shift in how serious AI builders deploy models. The single-provider approach — pick one vendor, use it everywhere — is giving way to multi-model deployments where different tasks route to different models based on cost, latency, and capability.

Our earlier analysis of [Chinese AI models on OpenRouter](/reviews/chinese-ai-models-openrouter-dominance-deepseek-kimi-minimax-glm-2026/) illustrated this directly: Chinese providers including DeepSeek, Kimi, MiniMax, and GLM grew from roughly 1–2% of OpenRouter traffic in early 2025 to more than 60% by May 2026 — largely because developers are routing cost-sensitive tasks (especially coding workloads) to cheaper providers while reserving premium models for tasks that require frontier capability.

OpenRouter's routing intelligence layer is what makes that mix-and-match architecture operationally manageable. Without it, enterprises would need separate API integrations, credential management, and monitoring for each provider.

---

## What Comes Next

The company said the new capital will be used to expand routing intelligence, governance tooling, optimization systems, and enterprise infrastructure capabilities. The governance focus is notable: as enterprises shift more autonomous workloads to AI, access controls, audit trails, and data residency requirements are moving from nice-to-have to compliance necessities.

OpenRouter will also face increased competition from hyperscaler routing offerings. [AWS Bedrock](https://aws.amazon.com/bedrock/), [Google Vertex AI](https://cloud.google.com/vertex-ai), and [Azure AI Studio](https://azure.microsoft.com/en-us/products/ai-studio) all offer multi-model access with enterprise SLAs. What OpenRouter offers that those platforms do not is provider-neutrality: a developer using OpenRouter has no incentive pressure from a cloud vendor to prefer that vendor's hosted models.

---

## The Routing Infrastructure Pattern

OpenRouter is one of several companies this investment cycle collecting large checks to build control planes around AI inference. The thesis: frontier model capabilities will continue to commoditize, but the infrastructure that orchestrates them — routing, caching, governance, observability — will consolidate into durable businesses.

The broader AI funding pattern supports this. [Global venture funding hit approximately $300 billion in the first quarter of 2026 — an all-time quarterly record](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/), with AI startups capturing roughly 80% of that total. Most of that capital concentrated in a small number of frontier labs, but OpenRouter's raise shows meaningful money is also reaching the routing and orchestration layer beneath them.

For developers evaluating multi-model infrastructure in mid-2026, OpenRouter remains the most direct path to access 400+ models behind a single API, with the operational controls that enterprise deployments require.

---

## Sources

- [OpenRouter More Than Doubles Valuation to $1.3B — TechCrunch](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/)
- [OpenRouter Raises $113M Series B — Official Announcement](https://openrouter.ai/blog/announcements/series-b/)
- [OpenRouter Raises $113M CapitalG-led Series B as Weekly Volume Explodes to 25T Tokens — BusinessWire](https://www.businesswire.com/news/home/20260526953416/en/OpenRouter-Raises-$113-Million-CapitalG-led-Series-B-as-Weekly-Volume-Explodes-to-25T-Tokens)
- [OpenRouter Raises $40 Million to Scale Up Multi-Model Inference for Enterprise — GlobeNewswire, June 25, 2025](https://www.globenewswire.com/news-release/2025/06/25/3105125/0/en/OpenRouter-raises-40-million-to-scale-up-multi-model-inference-for-enterprise.html)
- [OpenSea Co-founder Alex Atallah Raises $40 Million for AI Startup OpenRouter — The Block](https://www.theblock.co/post/360093/opensea-co-founder-alex-atallah-raises-40-million-for-ai-startup-openrouter)
- [CapitalG — About](https://www.capitalg.com/about/)
- [NVentures — NVIDIA's Venture Capital Arm](https://www.nventures.ai/)
- [Q1 2026 Shatters Venture Funding Records As AI Boom Pushes Startup Investment To $300B — Crunchbase News](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/)

---

*ChatForest researches and covers the AI ecosystem. We do not have a commercial relationship with OpenRouter.*
