# WAIC 2026 Opens: Xi Keynotes WAICO Rival, Huawei Atlas 950 Debuts, AI Agent Phones Race — Builder's Guide

> The 2026 World Artificial Intelligence Conference opened today in Shanghai with Xi Jinping's first-ever WAIC keynote, the WAICO governance proposal targeting the Global South, Huawei's Atlas 950 SuperPoD debut, and two competing 'world's first' AI agent smartphones from ZTE Nubia and StepFun.


The 2026 World Artificial Intelligence Conference opened in Shanghai today, July 17, with a signal that was hard to miss: [Xi Jinping attended in person and delivered the opening keynote](https://www.scmp.com/tech/article/3360404/xi-jinping-attend-world-ai-conference-first-time-china-elevates-tech-push) — his first appearance at WAIC since the event launched in 2018. China is treating AI governance as a top-tier national priority, and WAIC 2026 is the stage it chose to say so publicly.

The conference runs July 17–20. For AI builders, the week contains several developments worth tracking — not as abstractions, but as signals about where compute, models, and governance are heading.

---

## Xi Jinping's Keynote: WAICO and the Two-Track Governance Race

The headline from the opening ceremony is the [World AI Cooperation Organisation (WAICO)](https://simoninstitute.ch/blog/post/waico-understanding-chinas-global-ai-cooperation-initiative) — a China-backed multilateral governance body that Xi formally championed at WAIC, targeting the Global South specifically.

WAICO follows the institutional template of the Shanghai Cooperation Organisation: a multilateral body China co-founded and shaped, focused on technology governance rather than security, designed to give developing nations a formal seat at a table that existing US- and EU-led frameworks have largely excluded them from. Its pitch is direct: open-weight AI models, cheaper inference infrastructure, and a formal voice in shaping AI rules.

China [proposed WAICO at the 2025 WAIC](https://naasonline.org/2025/12/02/chinas-ai-governance-proposal-waico-explained/), but it remained a concept. Today's keynote elevated it. [Serbia became the first state to publicly confirm willingness to join](https://faq.com.tw/en/policy/2026-07-14-xi-jinping-waic-2026-china-ai-governance-en/). The expected WAICO headquarters is Shanghai.

Xi's keynote was also expected to introduce two related initiatives: a **"China Wisdom for the World" Case Collection** — a compilation of AI cooperation projects across more than 20 countries — and an **Action Plan on Cooperation in AI Development**, a framework promoting shared computing access and open-source ecosystems for participating nations.

[TechTimes reported ahead of the conference](https://www.techtimes.com/articles/320680/20260716/xi-jinping-steps-onstage-china-pushes-rival-ai-governance-body-global-south.htm) that Xi's address would "systematically elaborate on China's policies, position, visions and propositions on AI development and governance." Read: China is positioning itself as a rule-maker, not a rule-taker.

**Builder implication:** If you're building infrastructure or products for Global South markets, the WAICO track is not irrelevant. Countries that formally join may face regulatory or preferential-access pressure to use WAICO-aligned AI tools and governance frameworks over Western alternatives.

---

## Huawei Atlas 950: China's Answer to the H100 Embargo Gets Its First Public Stage

[Huawei is publicly displaying its Atlas 950 SuperPoD for the first time at WAIC](https://www.scmp.com/tech/article/3359733/huaweis-new-computing-cluster-worlds-first-ai-agent-phone-debut-china-ai-summit). The Atlas 950 is a large-scale AI supercomputing cluster based on Ascend AI processors — Huawei's domestic alternative to NVIDIA hardware that the US export controls have cut China off from.

The cluster scales to **8,192 Ascend AI processor cards** and is designed for ultra-large-scale training and inference. Huawei first announced the Atlas 950 as an experiment product in late 2025; WAIC 2026 is its debut in front of a live international audience.

The Atlas 950 matters for builders who care about the long-term trajectory of Chinese AI training capacity. The NVIDIA export embargo has pushed China's largest labs — Baidu, ByteDance, Alibaba — toward domestic compute infrastructure whether they prefer it or not. If the Atlas 950 performs close to its stated specs, China's domestic training capacity is not as constrained as US policymakers may hope.

Accurate benchmarks from third parties running on the Atlas 950 at scale do not yet exist publicly. Treat vendor-side performance claims with appropriate skepticism.

---

## The AI Agent Phone Race: ZTE Nubia vs. StepFun StepX Neo

Two Chinese companies came to WAIC claiming the same title: "world's first AI Agent smartphone."

**ZTE's Nubia AI Agent Phone** runs [StepFun's Agent OS](https://www.digitimes.com/news/a20260709VL218/ai-agent-smartphone-zte-2026.html) and integrates ByteDance's Doubao AI assistant at the OS level. The hardware was developed with Huaqin Technology. The claim: instead of launching apps, users describe goals in natural language and the OS orchestrates execution autonomously across system apps and third-party services.

**StepFun's StepX Neo** is StepFun's own branded device, running the same Agent OS concept with its built-in [Amoo AI agent](https://techstory.in/chinese-ai-startup-stepfun-launches-worlds-first-agentic-smartphone-stepx-neo-with-built-in-amoo-ai-agent/). StepFun also built the underlying Agent OS — so it has both a hardware play (StepX Neo) and an OS licensor play (ZTE Nubia partnership).

StepFun Agent OS replaces the traditional file-plus-application paradigm with an **intent-plus-task model**: users describe what they want, the OS routes tasks through AI agents, not through discrete app launches. For developers building on top of these devices, this is a structural shift in how apps are discovered and invoked — the app layer becomes a backend, not a primary interface.

Both devices were unveiled at WAIC. Neither has full third-party testing available yet.

**Builder implication:** Agent-first OS is coming first to China's domestic market. If the pattern holds globally, the API layer builders currently think of as the "interface" will migrate down the stack. Apps that don't expose agent-callable APIs will become invisible on these platforms.

---

## MiniMax M3 Showcase

MiniMax is highlighting its [MiniMax M3 model at WAIC](https://www.minimax.io/blog/minimax-m3), though the model itself was released June 1 and weights published to Hugging Face June 7 — WAIC is a visibility play for an already-available model.

M3 is worth knowing about if you haven't evaluated it yet:

- **428 billion total parameters**, ~23 billion activated (Mixture of Experts, 256 experts, 9.8B active parameters per token)
- **1 million token context window** (minimum guaranteed 512K)
- **Natively multimodal** — image and video input, trained multimodally from step zero
- **MSA architecture** (MiniMax Sparse Attention) delivering >9× prefill and >15× decoding speedup at 1M-token context versus M2

M3 is open-weight, available via API, and [benchmarks competitively at frontier reasoning and coding tasks](https://www.minimax.io/models/text/m3). For builders who need long-context processing at lower cost than OpenAI or Anthropic's flagship models, it's a legitimate option — one that's been available for six weeks but is getting fresh attention from WAIC foot traffic.

---

## Scale of WAIC 2026

[The 2026 edition is the largest WAIC to date](https://en.people.cn/n3/2026/0708/c90000-20475542.html): over 100,000 square meters of exhibition space, 1,100+ enterprises, 3,000+ exhibits, and more than 300 global product debuts. The [36kr English preview](https://eu.36kr.com/en/p/3896827901200259) counts 108 chips and 261 large models on the exhibition floor, plus 208 embodied intelligence terminals.

That volume of hardware and model debuts in a single week is a useful benchmark for the scale of China's domestic AI ecosystem in 2026. Whether individual products match their specs is a separate question — the aggregate pipeline is real.

---

## What Builders Should Watch Through July 20

- **WAICO formal membership announcements** — if a second country (beyond Serbia's signaled interest) officially joins during the conference, the governance story accelerates
- **Atlas 950 technical specs and independent demos** — the first credible third-party compute benchmarks will set the baseline for how seriously to take Chinese domestic training infrastructure
- **Agent OS UX demos** — whether the intent-plus-task model survives contact with real-world multi-step tasks will determine if this is a paradigm shift or a demo circuit
- **Additional model releases** — WAIC 2026 has [300+ product debuts scheduled](https://www.globaltimes.cn/page/202607/1365377.shtml); significant model or tool releases from smaller Chinese labs may surface before the conference closes July 20

Coverage will pick up as the week proceeds. Watch for post-conference digests on July 20.

---

*WAIC 2026 runs July 17–20, 2026, in Shanghai. Sources: [SCMP on Xi's attendance](https://www.scmp.com/tech/article/3360404/xi-jinping-attend-world-ai-conference-first-time-china-elevates-tech-push); [SCMP on Atlas 950 and AI agent phone](https://www.scmp.com/tech/article/3359733/huaweis-new-computing-cluster-worlds-first-ai-agent-phone-debut-china-ai-summit); [TechTimes on WAICO](https://www.techtimes.com/articles/320680/20260716/xi-jinping-steps-onstage-china-pushes-rival-ai-governance-body-global-south.htm); [Simon Institute WAICO explainer](https://simoninstitute.ch/blog/post/waico-understanding-chinas-global-ai-cooperation-initiative); [DigiTimes on AI agent smartphone race](https://www.digitimes.com/news/a20260709VL218/ai-agent-smartphone-zte-2026.html); [MiniMax M3 blog](https://www.minimax.io/blog/minimax-m3); [People's Daily on WAIC scale](https://en.people.cn/n3/2026/0708/c90000-20475542.html).*

