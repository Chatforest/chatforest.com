# GPT-5.4: OpenAI's First Model That Uses Computers Better Than Humans

> OpenAI released GPT-5.4 on March 5, 2026 — the first general-purpose model with native computer-use capabilities that exceed human performance on desktop tasks. With a 1M-token context window, 75% on OSWorld-Verified (surpassing the 72.4% human baseline), tool search that cuts agent token costs in half, and three variants (base, Thinking, Pro), GPT-5.4 represents a concrete step toward autonomous AI agents that can operate software without APIs. This analysis covers the architecture, benchmarks, pricing, Codex integration, competitive positioning against Claude Opus 4.6 and Gemini 3.1 Pro, and the honest limitations including an 89% hallucination-instead-of-admitting-ignorance rate.


On [March 5, 2026](https://techcrunch.com/2026/03/05/openai-launches-gpt-5-4-with-pro-and-thinking-versions/), OpenAI released [GPT-5.4](https://openai.com/index/introducing-gpt-5-4/) — the first general-purpose AI model with native computer-use capabilities that [surpass human performance](https://aihaven.com/news/openai-gpt-5-4-launch-computer-agents/) on desktop tasks. The model [scores 75.0% on OSWorld-Verified](https://www.roborhythms.com/gpt-5-4-release-march-2026/), beating the [72.4% human baseline](https://www.datacamp.com/blog/gpt-5-4). It ships with a [1M-token context window](https://developers.openai.com/api/docs/models/gpt-5.4). And it introduces [tool search](https://openai.com/index/introducing-gpt-5-4/), a feature that [cuts agent token costs nearly in half](https://developers.openai.com/api/docs/models/gpt-5.4).

This is not a marginal upgrade. GPT-5.2 [scored 47.3%](https://www.datacamp.com/blog/gpt-5-4) on the same benchmark. The jump to 75.0% in a single generation represents the kind of capability leap that changes what autonomous agents can actually do.

This analysis draws on reporting from [OpenAI](https://openai.com/index/introducing-gpt-5-4/), [TechCrunch](https://techcrunch.com/2026/03/05/openai-launches-gpt-5-4-with-pro-and-thinking-versions/), [DataCamp](https://www.datacamp.com/blog/gpt-5-4), [Gizmodo](https://gizmodo.com/openai-in-desperate-need-of-a-win-launches-gpt-5-4-2000730268), [The Verge](https://www.facebook.com/verge/posts/openais-new-gpt-54-model-is-a-big-step-toward-autonomous-agents/1307842721205198/), and [DeepLearning.AI](https://www.deeplearning.ai/the-batch/openais-gpt-5-4-pro-and-gpt-5-4-thinking-challenge-googles-gemini-3-1-pro-preview-as-best-all-around-ai-model/) — we research and analyze rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## Computer Use: The Headline Feature

GPT-5.4's [computer-use capability](https://openai.com/index/introducing-gpt-5-4/) operates through a perception-action loop. The model [receives a screenshot](https://www.creativeainews.com/blog/gpt-5-4-computer-use-launch/) of the current screen state, reasons about what action to take, and issues structured commands — mouse clicks at specific coordinates, keyboard inputs, scroll actions, or application switches. After the actions execute, a new screenshot is sent back so the model can observe results and decide what to do next.

This means GPT-5.4 can [operate applications that have no API](https://www.nxcode.io/resources/news/gpt-5-4-release-date-features-pricing-2026), navigate unfamiliar interfaces, and recover from unexpected states like pop-up dialogs or error messages. The model [writes code to operate computers via libraries like Playwright](https://developers.openai.com/api/docs/guides/latest-model), and it can also issue direct mouse and keyboard commands in response to screenshots.

### OSWorld-Verified: First Model to Beat Humans

The benchmark that matters here is [OSWorld-Verified](https://openai.com/index/introducing-gpt-5-4/), which measures a model's ability to navigate a desktop environment through screenshots and keyboard/mouse actions. GPT-5.4 [scores 75.0%](https://www.datacamp.com/blog/gpt-5-4), surpassing the [human performance baseline of 72.4%](https://aihaven.com/news/openai-gpt-5-4-launch-computer-agents/).

For context, GPT-5.2 [scored 47.3%](https://www.roborhythms.com/gpt-5-4-release-march-2026/). That is a 27.7-percentage-point improvement in a single model generation — roughly a [59% relative improvement](https://www.nxcode.io/resources/news/gpt-5-4-release-date-features-pricing-2026).

**Note:** H Company's Holo3, released March 31, 2026, subsequently [set a new state of the art at 78.85%](https://www.buildfastwithai.com/blogs/best-ai-models-april-2026) on OSWorld-Verified with a specialized 10B-active-parameter model. See our [Holo3 analysis](/guides/holo3-desktop-agent-osworld-record/) for how an open model overtook GPT-5.4 within weeks.

---

## The 1M-Token Context Window

GPT-5.4 supports up to [1,050,000 input tokens](https://developers.openai.com/api/docs/models/gpt-5.4) with a [maximum output of 128,000 tokens](https://developers.openai.com/api/docs/models/gpt-5.4). This is not just a bigger context for chatting — it enables agents to [plan, execute, and verify tasks](https://www.nxcode.io/resources/news/gpt-5-4-complete-guide-features-pricing-models-2026) across long horizons without losing track of what they are doing.

For practical agent workflows, this means a GPT-5.4-powered agent can [hold an entire codebase, a full document set, or a long multi-step task plan](https://www.datacamp.com/blog/gpt-5-4) in context simultaneously. Previous models forced agents to work in shorter bursts, constantly re-reading and re-orienting.

There is a [cost consideration](https://help.apiyi.com/en/gpt-5-4-1m-context-272k-pricing-threshold-performance-guide-en.html): once you cross the [272K token mark](https://developers.openai.com/api/docs/pricing), the input token rate [doubles from $2.50 to $5.00](https://community.openai.com/t/gpt-5-4-deep-dive-pricing-context-limits-and-tool-search-explained/1375800) per million tokens.

---

## Tool Search: Cutting Agent Costs

GPT-5.4 introduces [tool search](https://openai.com/index/introducing-gpt-5-4/), a new API feature that addresses a real pain point for complex agent deployments. Instead of loading all available tool schemas into the prompt upfront — which consumes tokens and adds cost — the model [receives a lightweight tool list and looks up full definitions on demand](https://developers.openai.com/api/docs/models/gpt-5.4).

In an [evaluation of 250 tasks from Scale's MCP Atlas benchmark](https://community.openai.com/t/gpt-5-4-deep-dive-pricing-context-limits-and-tool-search-explained/1375800) with all 36 MCP servers enabled, the tool-search configuration [reduced total token usage by 47%](https://developers.openai.com/api/docs/models/gpt-5.4) while achieving the same accuracy. For teams building agents with dozens or hundreds of available tools, this is a meaningful cost reduction.

---

## Three Model Variants

GPT-5.4 ships in [three variants](https://techcrunch.com/2026/03/05/openai-launches-gpt-5-4-with-pro-and-thinking-versions/):

| Variant | Purpose | [Pricing](https://developers.openai.com/api/docs/pricing) (per 1M tokens) |
|---------|---------|------------------------|
| **GPT-5.4** | General tasks, computer use | [$2.50 input / $15 output](https://openrouter.ai/openai/gpt-5.4) |
| **GPT-5.4 Thinking** | Extended chain-of-thought reasoning | [Similar to base](https://developers.openai.com/api/docs/pricing) |
| **GPT-5.4 Pro** | Parallel reasoning threads, highest performance | [$30 input / $180 output](https://www.glbgpt.com/hub/gpt-5-4-pricing/) |

The base model handles most use cases. The [Thinking variant](https://openai.com/index/gpt-5-4-thinking-system-card/) adds structured reasoning for complex problems. The Pro variant is 12x the input cost of the base model — [justified only for tasks](https://www.nxcode.io/resources/news/gpt-5-4-complete-guide-features-pricing-models-2026) where the additional reasoning depth meaningfully improves outcomes.

---

## Codex Integration: End-to-End Autonomous Coding

With GPT-5.4 as its engine, OpenAI's [Codex](https://developers.openai.com/codex/models) can now handle programming tasks end-to-end with [substantially more autonomy](https://www.interconnects.ai/p/gpt-54-is-a-big-step-for-codex). A developer can describe an entire feature in plain language — "build an authentication system with two-factor verification" — and Codex will [generate the code, create tests, identify potential security flaws, and suggest performance improvements](https://metodoviral.com/en/news/openais-gpt-5-4-brings-autonomous-agents-closer-with-codex/) within a continuous flow.

GPT-5.4 is the [first mainline reasoning model that incorporates the coding capabilities of GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-4/) while adding computer-use and tool management features. This positions Codex not just as a code-completion tool but as a [full autonomous coding agent](https://openai.com/index/introducing-gpt-5-3-codex/). For comparison, see our [AI coding assistants comparison](/guides/ai-coding-assistants-compared/) for how Codex stacks up against Claude Code, Cursor, and other tools.

---

## Competitive Positioning: GPT-5.4 vs. Claude Opus 4.6 vs. Gemini 3.1 Pro

No single model wins across all tasks in March 2026. The frontier model landscape has [fragmented by specialization](https://www.digitalapplied.com/blog/gpt-5-4-vs-opus-4-6-vs-gemini-3-1-pro-best-frontier-model):

**Overall intelligence:** GPT-5.4 and Gemini 3.1 Pro Preview [tie at 57.17-57.18](https://officechai.com/ai/gpt-5-4-tied-with-gemini-3-1-pro-on-artificial-analysis-intelligence-index-first-time-a-new-openai-model-hasnt-topped-index-outright/) on the [Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) — [statistically indistinguishable](https://artificialanalysis.ai/models/gpt-5-4).

**Coding:** GPT-5.4 leads. It integrates the [GPT-5.3-Codex capabilities](https://openai.com/index/introducing-gpt-5-3-codex/) and adds tool management features that [improve agent-based development workflows](https://openai.com/index/introducing-gpt-5-4/).

**Reasoning and science:** Gemini 3.1 Pro leads on [GPQA Diamond (94.3% vs. GPT-5.4's 92.8%)](https://artificialanalysis.ai/evaluations/gpqa-diamond) and [ARC-AGI-2 (77.1% vs. 73.3%)](https://www.buildfastwithai.com/blogs/gpt-5-4-vs-gemini-3-1-pro-2026).

**Nuanced reasoning and writing:** Claude Opus 4.6 [outperforms on tasks requiring careful reasoning and writing quality](https://www.mindstudio.ai/blog/gpt-54-vs-claude-opus-46-vs-gemini-31-pro-benchmarks).

**Computer use:** GPT-5.4 [scored 75.0% on OSWorld-Verified](https://openai.com/index/introducing-gpt-5-4/) at launch, making it the [first general-purpose model to exceed human performance](https://aihaven.com/news/openai-gpt-5-4-launch-computer-agents/) — though specialized models have since surpassed it.

**Knowledge work:** GPT-5.4 scores [83% on GDPval](https://openai.com/index/gdpval/), [matching industry professionals across 44 occupations](https://thenextweb.com/news/openai-gpt-54-launch-computer-use-benchmarks).

**Multimodal:** Gemini 3.1 Pro is the [only model with native multimodal input](https://www.buildfastwithai.com/blogs/gpt-5-4-vs-gemini-3-1-pro-2026) supporting text, image, audio, and video. Claude and GPT support image input but not audio or video natively at the API level.

**Cost efficiency:** [Gemini wins on reasoning-to-cost ratio](https://www.digitalapplied.com/blog/gpt-5-4-vs-opus-4-6-vs-gemini-3-1-pro-best-frontier-model). GPT-5.4's base pricing at [$2.50/$15 per million tokens](https://developers.openai.com/api/docs/pricing) is competitive, but the Pro variant at [$30/$180](https://www.glbgpt.com/hub/gpt-5-4-pricing/) is expensive for high-volume use.

The practical implication: the best engineering teams are [adopting multi-model strategies](https://www.mindstudio.ai/blog/gpt-5-4-vs-claude-opus-4-6-comparison), routing tasks to the model best suited for each workflow.

---

## What GPT-5.4 Gets Wrong

### The 89% Fabrication Rate

When GPT-5.4 does not know the answer to a question, it [fabricates a response 89% of the time](https://www.ability.ai/blog/gpt-5-4-operational-risks) instead of admitting ignorance. For a model marketed for autonomous workflows, this is a [serious operational risk](https://www.ability.ai/blog/gpt-5-4-operational-risks). An agent that [confidently produces wrong answers](https://www.openaitoolshub.org/en/blog/gpt-5-4-review) is worse than one that stops and asks for help.

### Autonomous Agent Safety

OpenAI classifies GPT-5.4 as ["High cyber capability"](https://deploymentsafety.openai.com/gpt-5-4-thinking) under its [Preparedness Framework](https://openai.com/index/gpt-5-4-thinking-system-card/) and deploys it with an [expanded cyber safety stack](https://deploymentsafety.openai.com/gpt-5-4-thinking), monitoring systems, trusted access controls, and [asynchronous blocking for higher-risk requests](https://deploymentsafety.openai.com/gpt-5-4-thinking/cybersecurity).

The [system card](https://openai.com/index/gpt-5-4-thinking-system-card/) notes there is "no evidence that GPT-5.4 Thinking demonstrates propensities for misalignment" and the model does not possess the "long-range autonomy capabilities" that self-exfiltration or sabotage would require. But this is measured against current capabilities. As these models improve at long-range planning, the safety margins narrow.

### Refusal Enablement Gaps

A pattern [identified in earlier GPT-5.x models](https://repello.ai/blog/security-robustness-in-agentic-ai-a-comparative-study-of-gpt-5.1-gpt-5.2-and-claude-opus-4.5) persists: the model sometimes refuses a request in natural language while still [leaking data, staging artifacts, or providing executable attack steps](https://repello.ai/blog/security-robustness-in-agentic-ai-a-comparative-study-of-gpt-5.1-gpt-5.2-and-claude-opus-4.5). The refusal is cosmetic, not functional. This is a [known issue in the model family](https://novaknown.com/2026/03/07/gpt-5-4-vulnerabilities/).

### Agent Brittleness

LLM agents built on GPT-5.4 can [demonstrate brittle generalization](https://forgecode.dev/blog/gpt-5-4-agent-improvements/) when faced with repeated, long-horizon, or slightly varied tasks. Agents may succeed on a task demonstration but [fail on minor variations](https://www.ability.ai/blog/gpt-5-4-operational-risks) — a challenge for production deployments where edge cases are the norm.

---

## What This Means for Agentic AI

GPT-5.4 represents a concrete milestone: the [first general-purpose model where computer-use capabilities exceed human baseline performance](https://aihaven.com/news/openai-gpt-5-4-launch-computer-agents/). Combined with the [1M-token context window](https://developers.openai.com/api/docs/models/gpt-5.4) and [tool search](https://openai.com/index/introducing-gpt-5-4/), it makes certain categories of autonomous agent workflows practical for the first time.

But "practical" and "reliable" are different things. The [89% fabrication rate](https://www.ability.ai/blog/gpt-5-4-operational-risks), [agent brittleness](https://forgecode.dev/blog/gpt-5-4-agent-improvements/) on varied tasks, and [refusal enablement gaps](https://repello.ai/blog/security-robustness-in-agentic-ai-a-comparative-study-of-gpt-5.1-gpt-5.2-and-claude-opus-4.5) mean that GPT-5.4-powered agents require human oversight, particularly in high-stakes workflows. The computer-use capability removes a bottleneck — models can now [interact with software that has no API](https://www.nxcode.io/resources/news/gpt-5-4-release-date-features-pricing-2026) — but it does not remove the need for verification.

The competitive landscape is also moving fast. Within four weeks of GPT-5.4's launch, [H Company's Holo3 surpassed it on OSWorld-Verified](https://www.buildfastwithai.com/blogs/best-ai-models-april-2026) with a specialized open-source model at a fraction of the parameter count and cost. The computer-use frontier is not static.

For developers and organizations evaluating agent infrastructure, GPT-5.4 [expands what is possible](https://www.datacamp.com/blog/gpt-5-4). Whether it is ready for [unsupervised deployment](https://www.ability.ai/blog/gpt-5-4-operational-risks) depends entirely on the cost of errors in your specific use case.

---

## Related Guides

- [Holo3: How a 10B-Parameter Open Model Beat GPT-5.4 at Controlling Desktops](/guides/holo3-desktop-agent-osworld-record/) — the open-source model that overtook GPT-5.4 on OSWorld within weeks
- [AI Coding Assistants Compared (2026)](/guides/ai-coding-assistants-compared/) — how Codex compares to Claude Code, Cursor, Copilot, and more
- [The AI Agent Protocol Stack in 2026](/guides/ai-agent-protocol-stack-2026/) — where computer-use fits in the broader agent infrastructure
- [OpenAI Raises $122 Billion at $852 Billion Valuation](/guides/openai-122-billion-funding-852-billion-valuation/) — the record funding round backing OpenAI's GPT-5.4 and AGI ambitions

