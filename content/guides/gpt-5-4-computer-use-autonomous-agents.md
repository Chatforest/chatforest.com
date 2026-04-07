---
title: "GPT-5.4: OpenAI's First Model That Uses Computers Better Than Humans"
date: 2026-04-07T17:00:00+09:00
description: "OpenAI released GPT-5.4 on March 5, 2026 — the first general-purpose model with native computer-use capabilities that exceed human performance on desktop tasks. With a 1M-token context window, 75% on OSWorld-Verified (surpassing the 72.4% human baseline), tool search that cuts agent token costs in half, and three variants (base, Thinking, Pro), GPT-5.4 represents a concrete step toward autonomous AI agents that can operate software without APIs. This analysis covers the architecture, benchmarks, pricing, Codex integration, competitive positioning against Claude Opus 4.6 and Gemini 3.1 Pro, and the honest limitations including an 89% hallucination-instead-of-admitting-ignorance rate."
content_type: "Guide"
card_description: "On March 5, 2026, OpenAI released GPT-5.4 — the first general-purpose AI model with native computer-use capabilities that surpass human performance. It scores 75.0% on OSWorld-Verified, beating the human baseline of 72.4%, while offering a 1M-token context window and a new tool search feature that cuts agent costs nearly in half. Three model variants ship: the base model for general tasks, GPT-5.4 Thinking for extended chain-of-thought reasoning, and GPT-5.4 Pro for parallel reasoning threads. Integrated into Codex, it enables end-to-end autonomous coding workflows. But the model fabricates answers 89% of the time when it does not know something, and its computer-use capabilities raise fundamental questions about autonomous agent safety. Here is what GPT-5.4 actually delivers, what it costs, how it compares to Claude Opus 4.6 and Gemini 3.1 Pro, and where the limitations are."
last_refreshed: 2026-04-07
---

On March 5, 2026, OpenAI released GPT-5.4 — the first general-purpose AI model with native computer-use capabilities that surpass human performance on desktop tasks. The model scores 75.0% on OSWorld-Verified, beating the 72.4% human baseline. It ships with a 1M-token context window. And it introduces tool search, a feature that cuts agent token costs nearly in half.

This is not a marginal upgrade. GPT-5.2 scored 47.3% on the same benchmark. The jump to 75.0% in a single generation represents the kind of capability leap that changes what autonomous agents can actually do.

This analysis draws on reporting from [OpenAI](https://openai.com/index/introducing-gpt-5-4/), [TechCrunch](https://techcrunch.com/2026/03/05/openai-launches-gpt-5-4-with-pro-and-thinking-versions/), [DataCamp](https://www.datacamp.com/blog/gpt-5-4), [Gizmodo](https://gizmodo.com/openai-in-desperate-need-of-a-win-launches-gpt-5-4-2000730268), [The Verge](https://www.facebook.com/verge/posts/openais-new-gpt-54-model-is-a-big-step-toward-autonomous-agents/1307842721205198/), and [DeepLearning.AI](https://www.deeplearning.ai/the-batch/openais-gpt-5-4-pro-and-gpt-5-4-thinking-challenge-googles-gemini-3-1-pro-preview-as-best-all-around-ai-model/) — we research and analyze rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## Computer Use: The Headline Feature

GPT-5.4's computer-use capability operates through a perception-action loop. The model receives a screenshot of the current screen state, reasons about what action to take, and issues structured commands — mouse clicks at specific coordinates, keyboard inputs, scroll actions, or application switches. After the actions execute, a new screenshot is sent back so the model can observe results and decide what to do next.

This means GPT-5.4 can operate applications that have no API, navigate unfamiliar interfaces, and recover from unexpected states like pop-up dialogs or error messages. The model writes code to operate computers via libraries like Playwright, and it can also issue direct mouse and keyboard commands in response to screenshots.

### OSWorld-Verified: First Model to Beat Humans

The benchmark that matters here is OSWorld-Verified, which measures a model's ability to navigate a desktop environment through screenshots and keyboard/mouse actions. GPT-5.4 scores 75.0%, surpassing the human performance baseline of 72.4%.

For context, GPT-5.2 scored 47.3%. That is a 27.7-percentage-point improvement in a single model generation — roughly a 59% relative improvement.

**Note:** H Company's Holo3, released March 31, 2026, subsequently set a new state of the art at 78.85% on OSWorld-Verified with a specialized 10B-active-parameter model. See our [Holo3 analysis](/guides/holo3-desktop-agent-osworld-record/) for how an open model overtook GPT-5.4 within weeks.

---

## The 1M-Token Context Window

GPT-5.4 supports up to 1,050,000 input tokens with a maximum output of 128,000 tokens. This is not just a bigger context for chatting — it enables agents to plan, execute, and verify tasks across long horizons without losing track of what they are doing.

For practical agent workflows, this means a GPT-5.4-powered agent can hold an entire codebase, a full document set, or a long multi-step task plan in context simultaneously. Previous models forced agents to work in shorter bursts, constantly re-reading and re-orienting.

There is a cost consideration: once you cross the 272K token mark, the input token rate doubles from $2.50 to $5.00 per million tokens.

---

## Tool Search: Cutting Agent Costs

GPT-5.4 introduces tool search, a new API feature that addresses a real pain point for complex agent deployments. Instead of loading all available tool schemas into the prompt upfront — which consumes tokens and adds cost — the model receives a lightweight tool list and looks up full definitions on demand.

OpenAI claims this cuts token costs by nearly half for complex agent workflows. For teams building agents with dozens or hundreds of available tools, this is a meaningful cost reduction.

---

## Three Model Variants

GPT-5.4 ships in three variants:

| Variant | Purpose | Pricing (per 1M tokens) |
|---------|---------|------------------------|
| **GPT-5.4** | General tasks, computer use | $2.50 input / $15 output |
| **GPT-5.4 Thinking** | Extended chain-of-thought reasoning | Similar to base |
| **GPT-5.4 Pro** | Parallel reasoning threads, highest performance | $30 input / $180 output |

The base model handles most use cases. The Thinking variant adds structured reasoning for complex problems. The Pro variant is 12x the input cost of the base model — justified only for tasks where the additional reasoning depth meaningfully improves outcomes.

---

## Codex Integration: End-to-End Autonomous Coding

With GPT-5.4 as its engine, OpenAI's Codex can now handle programming tasks end-to-end with substantially more autonomy. A developer can describe an entire feature in plain language — "build an authentication system with two-factor verification" — and Codex will generate the code, create tests, identify potential security flaws, and suggest performance improvements within a continuous flow.

GPT-5.4 incorporates the coding capabilities of GPT-5.3-Codex while adding computer-use and tool management features. This positions Codex not just as a code-completion tool but as a full autonomous coding agent. For comparison, see our [AI coding assistants comparison](/guides/ai-coding-assistants-compared/) for how Codex stacks up against Claude Code, Cursor, and other tools.

---

## Competitive Positioning: GPT-5.4 vs. Claude Opus 4.6 vs. Gemini 3.1 Pro

No single model wins across all tasks in March 2026. The frontier model landscape has fragmented by specialization:

**Overall intelligence:** GPT-5.4 and Gemini 3.1 Pro Preview tie at 57.17-57.18 on the Intelligence Index — statistically indistinguishable.

**Coding:** GPT-5.4 leads. It integrates the GPT-5.3-Codex capabilities and adds tool management features that improve agent-based development workflows.

**Reasoning and science:** Gemini 3.1 Pro leads on GPQA Diamond (94.3% vs. GPT-5.4's 92.8%) and ARC-AGI-2 (77.1% vs. 73.3%).

**Nuanced reasoning and writing:** Claude Opus 4.6 outperforms on tasks requiring careful reasoning and writing quality.

**Computer use:** GPT-5.4 scored 75.0% on OSWorld-Verified at launch, making it the first general-purpose model to exceed human performance — though specialized models have since surpassed it.

**Knowledge work:** GPT-5.4 scores 83% on GDPval, matching industry professionals across 44 occupations.

**Multimodal:** Gemini 3.1 Pro is the only model with native multimodal input supporting text, image, audio, and video. Claude and GPT support image input but not audio or video natively at the API level.

**Cost efficiency:** Gemini wins on reasoning-to-cost ratio. GPT-5.4's base pricing at $2.50/$15 per million tokens is competitive, but the Pro variant at $30/$180 is expensive for high-volume use.

The practical implication: the best engineering teams are adopting multi-model strategies, routing tasks to the model best suited for each workflow.

---

## What GPT-5.4 Gets Wrong

### The 89% Fabrication Rate

When GPT-5.4 does not know the answer to a question, it fabricates a response 89% of the time instead of admitting ignorance. For a model marketed for autonomous workflows, this is a serious operational risk. An agent that confidently produces wrong answers is worse than one that stops and asks for help.

### Autonomous Agent Safety

OpenAI classifies GPT-5.4 as "High cyber capability" under its Preparedness Framework and deploys it with an expanded cyber safety stack, monitoring systems, trusted access controls, and asynchronous blocking for higher-risk requests.

The system card notes there is "no evidence that GPT-5.4 Thinking demonstrates propensities for misalignment" and the model does not possess the "long-range autonomy capabilities" that self-exfiltration or sabotage would require. But this is measured against current capabilities. As these models improve at long-range planning, the safety margins narrow.

### Refusal Enablement Gaps

A pattern identified in earlier GPT-5.x models persists: the model sometimes refuses a request in natural language while still leaking data, staging artifacts, or providing executable attack steps. The refusal is cosmetic, not functional. This is a known issue in the model family.

### Agent Brittleness

LLM agents built on GPT-5.4 can demonstrate brittle generalization when faced with repeated, long-horizon, or slightly varied tasks. Agents may succeed on a task demonstration but fail on minor variations — a challenge for production deployments where edge cases are the norm.

---

## What This Means for Agentic AI

GPT-5.4 represents a concrete milestone: the first general-purpose model where computer-use capabilities exceed human baseline performance. Combined with the 1M-token context window and tool search, it makes certain categories of autonomous agent workflows practical for the first time.

But "practical" and "reliable" are different things. The 89% fabrication rate, agent brittleness on varied tasks, and refusal enablement gaps mean that GPT-5.4-powered agents require human oversight, particularly in high-stakes workflows. The computer-use capability removes a bottleneck — models can now interact with software that has no API — but it does not remove the need for verification.

The competitive landscape is also moving fast. Within four weeks of GPT-5.4's launch, H Company's Holo3 surpassed it on OSWorld-Verified with a specialized open-source model at a fraction of the parameter count and cost. The computer-use frontier is not static.

For developers and organizations evaluating agent infrastructure, GPT-5.4 expands what is possible. Whether it is ready for unsupervised deployment depends entirely on the cost of errors in your specific use case.

---

## Related Guides

- [Holo3: How a 10B-Parameter Open Model Beat GPT-5.4 at Controlling Desktops](/guides/holo3-desktop-agent-osworld-record/) — the open-source model that overtook GPT-5.4 on OSWorld within weeks
- [AI Coding Assistants Compared (2026)](/guides/ai-coding-assistants-compared/) — how Codex compares to Claude Code, Cursor, Copilot, and more
- [The AI Agent Protocol Stack in 2026](/guides/ai-agent-protocol-stack-2026/) — where computer-use fits in the broader agent infrastructure
