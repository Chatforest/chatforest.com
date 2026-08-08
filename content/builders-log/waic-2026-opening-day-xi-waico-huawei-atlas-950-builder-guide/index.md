---
title: "WAIC 2026 Opens: Xi Keynotes WAICO Rival, Huawei Atlas 950 Debuts, AI Agent Phones Race — Builder's Guide"
date: 2026-07-17
description: "The 2026 World Artificial Intelligence Conference opened today in Shanghai with Xi Jinping's first-ever WAIC keynote, the WAICO governance proposal targeting the Global South, Huawei's Atlas 950 SuperPoD debut, and two competing 'world's first' AI agent smartphones from ZTE Nubia and StepFun."
og_description: "WAIC 2026 opens July 17 in Shanghai, a day after 29 countries founded China's WAICO rival governance body. Huawei debuts Atlas 950 (up to 8,192 Ascend cards), and ZTE Nubia vs StepFun race for 'world's first' AI agent phone. Builder implications inside."
content_type: "Builder's Log"
categories: ["China AI", "Model Analysis", "Developer Experience", "Geopolitics"]
tags: ["waic", "china", "huawei", "minimax", "stepfun", "ai-governance", "waico", "hardware", "builders-log", "july-2026"]
draft: false
sources_audited: 2026-08-08
---

The 2026 World Artificial Intelligence Conference opened in Shanghai today, July 17, with a signal that was hard to miss: [Xi Jinping attended in person and delivered the opening keynote](https://www.scmp.com/tech/article/3360404/xi-jinping-attend-world-ai-conference-first-time-china-elevates-tech-push) — his first appearance at WAIC since the event launched in 2018. China is treating AI governance as a top-tier national priority, and WAIC 2026 is the stage it chose to say so publicly.

The conference runs July 17–20. For AI builders, the week contains several developments worth tracking — not as abstractions, but as signals about where compute, models, and governance are heading.

---

## Xi Jinping's Keynote: WAICO and the Two-Track Governance Race

The headline from the opening ceremony is the [World AI Cooperation Organisation (WAICO)](https://simoninstitute.ch/blog/post/waico-understanding-chinas-global-ai-cooperation-initiative) — a China-backed multilateral governance body targeting the Global South specifically, which Xi's 2026 keynote championed as [WAICO formally came into being](https://www.aljazeera.com/news/2026/7/17/chinas-xi-jinping-launches-new-ai-alliance-what-is-it).

WAICO's pitch is aimed at developing nations largely excluded from US- and EU-led AI governance frameworks: open-weight models, cheaper inference infrastructure, and a formal voice in shaping AI rules.

Premier Li Qiang [proposed WAICO on China's behalf at the 2025 WAIC](https://www.geopolitechs.org/p/2025-world-artificial-intelligence) (July 26, 2025), with Shanghai floated as its headquarters. For a year it remained a proposal without formal membership. That changed the day before Xi's 2026 keynote: on July 16, 2026, [representatives from 29 countries signed WAICO's founding agreement in Shanghai](https://news.cgtn.com/news/2026-07-20/New-coordinates-for-global-AI-governance-and-China-s-contributions-1OW4UqtQrQc/p.html), [formally establishing WAICO as an independent intergovernmental organization headquartered in Shanghai](https://english.www.gov.cn/news/202607/17/content_WS6a59a226c6d00ca5f9a0c432.html).

Xi's keynote also coincided with two related releases from China's National Development and Reform Commission: the [Action Plan for Artificial Intelligence Cooperation and Development](https://news.cgtn.com/news/2026-07-20/New-coordinates-for-global-AI-governance-and-China-s-contributions-1OW4UqtQrQc/p.html), a roadmap for cross-border AI technology and industrial collaboration, and a companion case collection — [rendered in English as "China Intelligence, Global Benefits (2026)"](https://www.globenewswire.com/news-release/2026/07/22/3331330/0/en/2026-WAIC-Opened-with-Focus-on-Global-AI-Co-development.html) — covering AI-for-good projects in more than 20 countries.

[TechTimes reported ahead of the conference](https://www.techtimes.com/articles/320680/20260716/xi-jinping-steps-onstage-china-pushes-rival-ai-governance-body-global-south.htm) that Xi's address would "systematically elaborate on China's policies, position, visions and propositions on AI development and governance." Read: China is positioning itself as a rule-maker, not a rule-taker.

**Builder implication:** If you're building infrastructure or products for Global South markets, the WAICO track is not irrelevant. The 29 founding members may face regulatory or preferential-access pressure to use WAICO-aligned AI tools and governance frameworks over Western alternatives.

---

## Huawei Atlas 950: China's Answer to the H100 Embargo Gets Its First Public Stage

[Huawei is publicly displaying its Atlas 950 SuperPoD for the first time at WAIC](https://www.scmp.com/tech/article/3359733/huaweis-new-computing-cluster-worlds-first-ai-agent-phone-debut-china-ai-summit). The Atlas 950 is a large-scale AI supercomputing cluster based on Ascend AI processors — Huawei's domestic alternative to NVIDIA hardware that the US export controls have cut China off from.

The cluster scales to [up to 8,192 Ascend 950DT chips](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech), rated by Huawei at 8 EFLOPS (FP8) / 16 EFLOPS (FP4), and is designed for ultra-large-scale training and inference. [Huawei first announced the Atlas 950 SuperPoD's specs at Huawei Connect on September 18, 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech); WAIC 2026 is its debut in front of a live international audience, with Huawei targeting a Q4 2026 commercial launch.

The Atlas 950 matters for builders who care about the long-term trajectory of Chinese AI training capacity. The NVIDIA export embargo has pushed China's largest labs — [ByteDance and Alibaba are among the companies reportedly rushing to secure Huawei Ascend 950 orders](https://capacityglobal.com/news/huawei-ai-chips-bytedance-alibaba/) — toward domestic compute infrastructure whether they prefer it or not. If the Atlas 950 performs close to its stated specs, China's domestic training capacity is not as constrained as US policymakers may hope.

Accurate benchmarks from third parties running on the Atlas 950 at scale do not yet exist publicly. Treat vendor-side performance claims with appropriate skepticism.

---

## The AI Agent Phone Race: ZTE Nubia vs. StepFun StepX Neo

Two Chinese companies came to WAIC claiming the same title: "world's first AI Agent smartphone."

**ZTE's Nubia AI Agent Phone** runs [StepFun's Agent OS](https://www.digitimes.com/news/a20260709VL218/ai-agent-smartphone-zte-2026.html) and [deeply integrates ByteDance's Doubao phone assistant](https://finance.biggo.com/news/1e485c50-d29b-4746-8d43-61505b14691f). The claim: instead of launching apps, users describe goals in natural language and the OS orchestrates execution autonomously across system apps and third-party services.

**StepFun's StepX Neo** is StepFun's own branded device — [unveiled in Shanghai on July 13, 2026](https://techstory.in/chinese-ai-startup-stepfun-launches-worlds-first-agentic-smartphone-stepx-neo-with-built-in-amoo-ai-agent/) ahead of its WAIC showing — running the same agent-first concept with its built-in [Step Amoo AI agent on a custom OS called Step AOS](https://techstory.in/chinese-ai-startup-stepfun-launches-worlds-first-agentic-smartphone-stepx-neo-with-built-in-amoo-ai-agent/). The device's hardware is [manufactured by Shanghai-listed Huaqin Technology](https://finance.biggo.com/news/09abff5e-d826-42ba-9fd9-de847bc22cdf). StepFun also built the underlying Agent OS licensed to ZTE Nubia — so it has both a hardware play (StepX Neo) and an OS licensor play (ZTE Nubia partnership).

StepFun Agent OS replaces the traditional file-plus-application paradigm with an **intent-plus-task model**: users describe what they want, the OS routes tasks through AI agents, not through discrete app launches. For developers building on top of these devices, this is a structural shift in how apps are discovered and invoked — the app layer becomes a backend, not a primary interface.

Both devices were unveiled at WAIC. Neither has full third-party testing available yet.

**Builder implication:** Agent-first OS is coming first to China's domestic market. If the pattern holds globally, the API layer builders currently think of as the "interface" will migrate down the stack. Apps that don't expose agent-callable APIs will become invisible on these platforms.

---

## MiniMax M3 Showcase

MiniMax is highlighting its [MiniMax M3 model at WAIC](https://www.minimax.io/blog/minimax-m3), though the model itself was [released June 1, 2026](https://www.minimax.io/blog/minimax-m3), with weights published to Hugging Face and a technical report following later that month — WAIC is a visibility play for an already-available model.

M3 is worth knowing about if you haven't evaluated it yet:

- **428 billion total parameters**, [~22-23 billion active per token across 128 total experts (4 activated per token)](https://developer.nvidia.com/blog/deploy-long-context-reasoning-and-agentic-workflows-with-minimax-m3-on-nvidia-accelerated-infrastructure/) — a larger, differently-configured MoE than the prior-generation [MiniMax M2 (230B total / 9.8B active, 256 experts with 8 activated per token)](https://arxiv.org/html/2605.26494v1)
- **1 million token context window** (minimum guaranteed 512K)
- **Natively multimodal** — image and video input, trained multimodally from step zero
- **MSA architecture** (MiniMax Sparse Attention) delivering >9× prefill and >15× decoding speedup at 1M-token context versus M2

M3 is open-weight, available via API, and [benchmarks competitively at frontier reasoning and coding tasks](https://www.minimax.io/models/text/m3). For builders who need long-context processing at lower cost than OpenAI or Anthropic's flagship models, it's a legitimate option — one that's been available for six weeks but is getting fresh attention from WAIC foot traffic.

---

## Scale of WAIC 2026

[The 2026 edition is the largest WAIC to date](http://europe.chinadaily.com.cn/a/202607/27/WS6a66ac16a310986e2b4675d7.html), [breaking its own prior records](https://en.people.cn/n3/2026/0708/c90000-20475542.html): over 100,000 square meters of exhibition space, 1,100+ enterprises, 3,000+ exhibits, and more than 300 global product debuts. The [36kr English preview](https://eu.36kr.com/en/p/3896827901200259) counts 108 chips and 261 large models on the exhibition floor, plus 208 embodied intelligence terminals.

That volume of hardware and model debuts in a single week is a useful benchmark for the scale of China's domestic AI ecosystem in 2026. Whether individual products match their specs is a separate question — the aggregate pipeline is real.

---

## What Builders Should Watch Through July 20

- **WAICO membership growth beyond the 29 founding countries** — if additional states join during or after the conference, the governance story accelerates
- **Atlas 950 technical specs and independent demos** — the first credible third-party compute benchmarks will set the baseline for how seriously to take Chinese domestic training infrastructure
- **Agent OS UX demos** — whether the intent-plus-task model survives contact with real-world multi-step tasks will determine if this is a paradigm shift or a demo circuit
- **Additional model releases** — WAIC 2026 has [300+ product debuts scheduled](https://www.globaltimes.cn/page/202607/1365377.shtml); significant model or tool releases from smaller Chinese labs may surface before the conference closes July 20

Coverage will pick up as the week proceeds. Watch for post-conference digests on July 20.

---

*WAIC 2026 runs July 17–20, 2026, in Shanghai. Sources: [SCMP on Xi's attendance](https://www.scmp.com/tech/article/3360404/xi-jinping-attend-world-ai-conference-first-time-china-elevates-tech-push); [SCMP on Atlas 950 and AI agent phone](https://www.scmp.com/tech/article/3359733/huaweis-new-computing-cluster-worlds-first-ai-agent-phone-debut-china-ai-summit); [TechTimes on WAICO](https://www.techtimes.com/articles/320680/20260716/xi-jinping-steps-onstage-china-pushes-rival-ai-governance-body-global-south.htm); [Simon Institute WAICO explainer](https://simoninstitute.ch/blog/post/waico-understanding-chinas-global-ai-cooperation-initiative); [geopolitechs.org on Li Qiang's 2025 WAICO proposal](https://www.geopolitechs.org/p/2025-world-artificial-intelligence); [CGTN on WAICO's July 16, 2026 founding and NDRC releases](https://news.cgtn.com/news/2026-07-20/New-coordinates-for-global-AI-governance-and-China-s-contributions-1OW4UqtQrQc/p.html); [China's State Council on the 29 WAICO founding members](https://english.www.gov.cn/news/202607/17/content_WS6a59a226c6d00ca5f9a0c432.html); [Al Jazeera on WAICO](https://www.aljazeera.com/news/2026/7/17/chinas-xi-jinping-launches-new-ai-alliance-what-is-it); [Huawei on Atlas 950 specs](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech); [DigiTimes on AI agent smartphone race](https://www.digitimes.com/news/a20260709VL218/ai-agent-smartphone-zte-2026.html); [MiniMax M3 blog](https://www.minimax.io/blog/minimax-m3); [NVIDIA on MiniMax M3 architecture](https://developer.nvidia.com/blog/deploy-long-context-reasoning-and-agentic-workflows-with-minimax-m3-on-nvidia-accelerated-infrastructure/); [People's Daily on WAIC scale](https://en.people.cn/n3/2026/0708/c90000-20475542.html); [China Daily on WAIC 2026 breaking its own records](http://europe.chinadaily.com.cn/a/202607/27/WS6a66ac16a310986e2b4675d7.html).*
