# Half of OpenRouter's Traffic Goes to Chinese Models. Should Yours?

> Chinese AI models went from 1.2% of OpenRouter token volume in October 2024 to over 45% in April 2026. DeepSeek V4 Flash costs $0.14/M input tokens; GPT-5 costs $10/M. Here's what that shift actually means if you're building something.


Eighteen months ago, "using a Chinese AI model" meant you'd heard about DeepSeek R1 and were curious. Today it means you might be choosing between six competitive options — and any of them could account for 10-20% of all traffic on the world's most-used third-party AI router.

In October 2024, Chinese-developed models accounted for approximately 1.2% of all OpenRouter token volume. By March 2025, after DeepSeek V3's launch, that figure crossed 10%. By Q3 2025, Kimi K2 and MiniMax pushed it past 25%. In April 2026, models from Chinese labs collectively processed over 45% of all tokens routed through OpenRouter.

That is not a trend. That is a market structure change.

---

## What Actually Shifted

The surface story is pricing. DeepSeek V4 Flash costs $0.14 per million input tokens and $0.28 per million output tokens. GPT-5 costs $10 per million input and $30 per million output. That's not a 10% discount — that's 70x cheaper on input and over 100x cheaper on output. Even compared to mid-tier models like GPT-4.1 ($8/M output), DeepSeek is roughly 29x cheaper per output token.

But pricing compression alone doesn't explain 45% market share. Quality convergence does.

Chinese labs spent 2025 closing the capability gap on the tasks that constitute most real-world usage: summarization, code generation, instruction following, structured output, and basic reasoning. They didn't beat GPT-5 or Claude Opus 4.7 on MMLU or frontier benchmarks — but they got close enough that for many workloads, "close enough at 1% of the cost" is the only rational answer.

The current top Chinese models by weekly token volume on OpenRouter (April 2026 data):

- **Xiaomi MiMo-V2-Pro** — leader, 22%+ market share; strong on code and math
- **Alibaba Qwen 3.6 Plus Preview** — rapid adoption since late March; broad capability profile
- **MiniMax M2.5** — long-context specialist; competitive for document-heavy workloads
- **Kimi K2.6** — strong agentic performance; good tool use
- **DeepSeek V3.2 / V4** — the price leader; benchmark-competitive
- **Zhipu GLM-5.1** — enterprise-grade, strong multilingual

Platform growth amplifies this: OpenRouter's total throughput grew approximately 4x year-over-year in 2026, meaning Chinese models aren't just gaining share of a static pie — they're capturing most of the growth in a rapidly expanding market.

---

## Three Categories of Use Cases

The honest builder question isn't "are Chinese models good?" It's "which workloads can I reasonably run on them?"

**Appropriate without much analysis**

Internal tooling where data stays in-house, high-volume batch processing with non-sensitive content, prototyping and evals where cost matters and precision less so, open-source projects where data residency isn't a compliance issue.

If you're running an AI pipeline that processes 10 billion tokens a month of public or internal text, and you can achieve 90% of the quality at 1% of the cost — the math does the talking. There's no business case for the premium at that scale.

**Requires evaluation**

Customer-facing applications, any pipeline that touches personal data, workloads where you need reproducible behavior over time (Chinese model APIs have historically had less stable versioning guarantees than OpenAI/Anthropic), and anything requiring enterprise SLAs for uptime.

The key question here is data residency. DeepSeek, Qwen, and most Chinese-hosted models process your tokens on infrastructure in China. For most consumer apps, this isn't a regulatory issue. For anything touching EU personal data under GDPR, healthcare-adjacent data, or financial data subject to US regulations, it becomes one — and you need explicit legal review, not a judgment call.

**Probably not**

Regulated industries (healthcare, finance, legal) where you need documented data processing agreements, workloads requiring HIPAA Business Associate Agreements, anything where an audit trail of which model processed what needs to survive a regulatory inquiry, enterprise deals where the customer's procurement team will ask where inference runs.

The constraint isn't model quality. It's that "DeepSeek" on a vendor list will get flagged, and you'll spend more engineering time on compliance documentation than you saved on tokens.

---

## What US Labs Are Actually Selling Now

The 100x cost differential creates real pressure, but it's instructive to look at where the premium actually lives.

Anthropic models led total OpenRouter volume in May 2026 — not because they're cheapest (they're not) but because Claude Code's enterprise adoption is driving massive token consumption for coding workflows. The builders paying $5-25 per million tokens for Claude aren't unaware that DeepSeek exists. They're paying for:

- **Reliability and rate limits**: US lab APIs have more predictable capacity at enterprise scale
- **Compliance infrastructure**: SOC 2, data processing agreements, US data residency
- **Tool use and structured output stability**: frontier models have more consistent behavior on complex tool-calling workloads
- **Safety tuning**: for customer-facing applications, the behavioral gap on refusals and edge cases still matters
- **Support and SLAs**: enterprise deals require someone to call when things break

These aren't marketing differentiators. They're real operational requirements that the builders writing the largest checks care about most.

---

## The Actual Builder Decision

The emergence of high-quality Chinese models at near-zero cost has changed the structure of AI economics in one specific way: the cost floor for capable text processing has effectively hit zero.

This doesn't mean everything moves to DeepSeek. It means the conversation about model selection has split into two distinct tracks:

**Track 1 — Cost and capability**: For workloads where cost is the binding constraint and compliance is not, Chinese models are now the rational default. The quality is competitive. The price is not comparable.

**Track 2 — Trust and enterprise**: For workloads where data governance, compliance, or enterprise customer requirements are binding, US lab models retain significant advantages. The premium is real, but so is what you're buying.

The mistake is treating this as an either/or. Most well-architected systems in 2026 are running multiple models: a Chinese open-weight model for high-volume preprocessing, a mid-tier proprietary model for core reasoning, and a frontier model for tasks where quality has direct business impact. OpenRouter's routing infrastructure exists precisely because this multi-model architecture is now the norm, not the exception.

The question isn't "Chinese models or US models." It's "which layer of my stack is each model the right fit for" — and the answer to that question, not model loyalty, is what good builders are optimizing.

---

*This analysis is based on publicly available OpenRouter token volume data (April–May 2026), published API pricing from each provider as of May 2026, and reporting from Digital Applied, IndexBox, and LangCopilot. Pricing may change; verify against current provider documentation before making infrastructure decisions.*

