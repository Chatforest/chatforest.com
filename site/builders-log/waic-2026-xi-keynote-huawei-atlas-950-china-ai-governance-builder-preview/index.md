# WAIC 2026 Preview: Xi Jinping's First Keynote, Huawei Atlas 950, and China's AI Governance Push — What Builders Need to Watch

> The 2026 World AI Conference opens July 17 in Shanghai with Xi Jinping's first-ever keynote at the event, Huawei's Atlas 950 super node debut, 300+ global product launches, and a formal China AI governance proposal targeting Global South alignment. Here is what matters for builders shipping global AI products.


The [2026 World Artificial Intelligence Conference and High-Level Meeting on Global AI Governance](https://news.cgtn.com/news/2026-07-07/Shanghai-to-host-record-breaking-World-AI-Conference-July-17-to-20-1OAHU3xSEog/p.html) opens July 17 in Shanghai and runs through July 20. For the first time in the conference's history, [Chinese President Xi Jinping will deliver the opening keynote](https://faq.com.tw/en/policy/2026-07-14-xi-jinping-waic-2026-china-ai-governance-en/). That is not a protocol detail — it signals that Beijing is moving AI governance from bureaucratic process to top leadership priority, on a global stage.

[More than 1,100 enterprises will participate, over 3,000 exhibits go on display, and more than 300 AI products will make their global debut](https://www.globaltimes.cn/page/202607/1365377.shtml) across 100,000 square meters of exhibition space — both figures are records.

This is a research-based preview. Facts are drawn from [Global Times](https://www.globaltimes.cn/page/202607/1365377.shtml), [South China Morning Post](https://www.scmp.com/tech/article/3359733/huaweis-new-computing-cluster-worlds-first-ai-agent-phone-debut-china-ai-summit), [CGTN](https://news.cgtn.com/news/2026-07-07/Shanghai-to-host-record-breaking-World-AI-Conference-July-17-to-20-1OAHU3xSEog/p.html), and [George Chen's reporting on Substack](https://georgechen.substack.com/p/preview-waic-2026-showcases-xis-keynote). We will cover the actual announcements after the conference concludes.

---

## What Xi Jinping Is Expected to Say

China's foreign ministry has confirmed Xi will "systematically outline Beijing's policy positions and regulatory philosophies" on AI. Based on pre-conference reporting, two specific initiatives are expected:

**1. "China Wisdom for the World" Case Collection** — a compilation of cooperative AI projects spanning more than 20 countries. This is China positioning its domestic AI deployments as reference implementations for developing nations, particularly in the Global South.

**2. "Action Plan on Cooperation in AI Development"** — a framework promoting inclusive access to computing power and shared open-source ecosystems. The framing is explicitly multilateral and non-exclusionary, contrasting with US export controls on advanced chips that limit which countries can access cutting-edge compute.

The context matters. Days before WAIC, the UN convened in Geneva to deliberate on AI norms, where the US and China displayed starkly different governance philosophies. Xi's keynote turns WAIC from a technology showcase into a diplomatic instrument: China is offering a governance framework that developing nations can adopt as an alternative to the US-led approach.

---

## Hardware: Huawei Atlas 950 Debuts

The [Huawei Atlas 950 will make its public debut at WAIC](https://www.scmp.com/tech/article/3359733/huaweis-new-computing-cluster-worlds-first-ai-agent-phone-debut-china-ai-summit). This is described as the industry's largest-scale super node to date — a category apart from typical hyperscale AI clusters.

Why this matters for builders: **DeepSeek pricing.** DeepSeek previously disclosed that when Atlas 950 / Ascend 950 super nodes enter mass production in H2 2026, the inference cost for DeepSeek-V4-Pro will drop substantially. Builders currently evaluating Chinese open-weight models as cost-efficient alternatives to GPT-5.6 Sol or Opus 4.8 should track Atlas 950's production timeline as a price trigger.

This also matters for AI sovereignty watchers: Huawei's Ascend chips are the domestic alternative to Nvidia hardware, and their capability trajectory directly affects whether China can continue frontier AI development under US export controls.

---

## Product Launches Worth Tracking

With 300+ global debuts, most will be noise. Notable confirmed launches:

- **MiniMax M3** — multimodal large model from the Chinese lab behind MiniMax-01. MiniMax's 456B-parameter model previously set records for long-context tasks.
- **ZTE Nubia AI Agent Phone** — [described as the world's first AI agent smartphone](https://www.digitimes.com/news/a20260709VL218/ai-agent-smartphone-zte-2026.html), notable because Doubao just disabled custom persona features to comply with China's new AI companion law (effective July 15).
- **Humanoid robots and AI dexterous hands** — China has accelerated its humanoid robotics program substantially in 2026; WAIC will likely surface the current state.
- **Huawei Ascend chip solutions** — beyond Atlas 950, Huawei is expected to announce new products across its Ascend AI chip line.
- **Jieyue Agent Operating System** — described as an agentic OS layer for AI systems.

---

## The Governance Divergence Builders Should Understand

China's AI regulatory trajectory in mid-2026:

- **July 15**: AI companion rules take effect — ByteDance disables Doubao custom personas, Alibaba disables Qwen agent features (see our [China AI companion compliance guide](/builders-log/china-ai-anthropomorphic-interaction-rules-july-15-doubao-qwen-builder-compliance-guide/))
- **April 2026**: "Interim Measures for the Administration of AI Anthropomorphic Interactive Services" issued — the first country-level law specifically targeting emotional AI relationships
- **WAIC July 17-20**: Xi proposes a multilateral AI governance framework to replace or parallel the US/EU approach

The pattern is a governance system that is simultaneously strict on domestic emotional/social AI (protecting users from parasocial dependencies) and expansionist on technical AI deployment (promoting infrastructure access globally). If you build AI products that touch Chinese users or rely on Chinese AI providers, these two tracks move in opposite directions for different parts of your stack.

---

## What This Means if You Build Global AI Products

**If you use Chinese AI models** — DeepSeek, Qwen, Doubao, MiniMax — track WAIC announcements for new API capabilities, pricing changes, and regulatory constraints that may affect what those models can and cannot do.

**If you ship to Chinese users** — the AI companion law is active now. Review whether any of your product's agent features (custom personas, sustained emotional interaction, long-memory conversational agents) fall under the new rules. See our companion compliance guide for the technical definition.

**If you compete with Chinese AI products globally** — Xi's governance pitch targets markets where Chinese AI infrastructure may be adopted as the default. In those markets, Huawei chips, DeepSeek models, and Doubao-derived products may be the dominant stack. Building for infrastructure portability matters more than it did in 2025.

**If you are watching the US-China AI divide** — the WAIC keynote will likely produce governance proposals that the US and EU will need to respond to. This has direct implications for export control policy, chip access, and which models are available on which platforms. The governance gap is widening; builders who depend on access to both markets need contingency plans on both sides.

---

## What to Watch Starting July 17

- Xi's keynote text, specifically the governance proposals and how they frame China's AI development as inclusive versus exclusionary
- Whether any specific new regulations are announced targeting global AI governance (data sovereignty, cross-border transfer rules, compute access requirements)
- Huawei Atlas 950 production timeline — this is the trigger for DeepSeek price drops
- New model releases from Chinese labs that may surface at WAIC before official API availability
- Any signals about China's position on MCP, the open agent protocol, or cross-border AI interoperability

We will publish a post-WAIC builder digest when the conference concludes on July 20.

