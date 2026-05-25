# GPT-5.5 Instant: OpenAI Quietly Made This Your ChatGPT Default. Here's What Actually Changed.

> On May 5, 2026, OpenAI replaced GPT-5.3 Instant with GPT-5.5 Instant as ChatGPT's default for all users — no announcement, no warning. It scores 88.7% on SWE-Bench, claims a 52.5% hallucination reduction, and costs $5/$30 per million tokens. Here's the honest breakdown, including the fine print OpenAI didn't lead with.


## The Rollout Nobody Announced

On May 5, 2026, hundreds of millions of ChatGPT users got a new default AI model. Most of them didn't know.

OpenAI published two blog posts and quietly flipped the switch. TechCrunch's headline said it plainly: the company had "quietly replaced" ChatGPT's default with no advance notice. GPT-5.5 Instant was now the brain behind every new ChatGPT conversation for Free, Plus, Pro, Business, and Enterprise users.

This is how OpenAI operates now: incremental improvements deployed at scale, iteration speed prioritized over announcement ceremonies. The quiet rollout is itself a signal — this is infrastructure, not a launch event.

So what did everyone actually get?

---

## What GPT-5.5 Instant Is (and Isn't)

**GPT-5.5 Instant** is the default-tier model in OpenAI's current product family. It is not the most powerful model OpenAI offers — that's GPT-5.5 Pro ($30/$180 per million input/output tokens). It's not the deepest reasoner — that's GPT-5.5 Thinking, which activates extended chain-of-thought. It is the fast, broadly capable everyday model that OpenAI ships to everyone by default.

The "Instant" designation has a specific meaning in OpenAI's model family: low latency, high throughput, optimized for the overwhelming majority of tasks that don't need maximum compute. Think of it as a System 1 layer — fast, fluid, good for most things — with automatic escalation to a System 2 layer (Thinking mode) when the task genuinely demands it.

Architecture-wise, OpenAI describes GPT-5.5 Instant as using **quantization and sparse routing** to hit its speed targets. For typical agentic workflow prompts — 500 to 2,000 tokens of context — responses begin arriving roughly 20–30% faster than GPT-5.4. The model can automatically switch to Thinking mode for sufficiently complex tasks (multi-file code analysis, advanced math, system architecture design), or users can select Thinking manually.

The API model identifier is simply **`gpt-5.5`** — no "instant" suffix. The Instant branding is a ChatGPT product label, not an API distinction. It's also accessible via the `chat-latest` alias in both the Responses API and Chat Completions API.

GPT-5.5 Instant became available in the API on **April 24, 2026** — eleven days before the ChatGPT default rollout. GPT-5.3 Instant remains available to paid users via model configuration through approximately August 2026, then retires.

---

## Benchmarks

| Benchmark | GPT-5.5 Instant | Context |
|---|---|---|
| **SWE-Bench Verified** | **88.7%** | Software engineering task completion |
| **SWE-Bench Pro** | 58.6% | End-to-end single-pass complex tasks |
| **MMLU** | 92.4% | Expert-level knowledge (above human expert) |
| **GPQA Diamond** | 93.5–93.6% | Graduate-level science reasoning |
| **AIME 2025** | 81.2 | Mathematical olympiad problems |
| **Terminal-Bench 2.0** | 82.7% | Complex CLI workflows (state-of-the-art at launch) |

The SWE-Bench score of 88.7% is strong — above Claude Code's previously cited 87.6% and, notably, above Grok Build's 70.8%. For developers evaluating coding models, that number is meaningful and comes from a widely-used third-party benchmark, not an OpenAI-run eval.

The AIME score (81.2 vs 65.4 for GPT-5.3 Instant) is a significant jump in mathematical reasoning. Terminal-Bench 2.0's state-of-the-art score suggests genuine improvement on complex multi-step CLI tasks — relevant for agentic use cases.

The caveat is GPQA Diamond. At 93.5–93.6%, GPT-5.5 Instant does not lead the field. Gemini 3.1 Pro Preview scores 94.1–94.3% and GPT-5.4 Pro scores 94.4%. On the most prestigious graduate-level reasoning benchmark, OpenAI's default consumer model is third.

This is worth knowing: GPT-5.5 Instant is an excellent everyday model, not the definitive frontier reasoning model.

---

## The Hallucination Story (Read Carefully)

OpenAI's headline claim: **52.5% fewer hallucinated claims on high-stakes prompts** (medicine, law, finance) compared to GPT-5.3 Instant. They also cite 37.3% fewer inaccurate responses on previously flagged conversation types.

These numbers are real, sourced from OpenAI's internal evaluations, and specifically apply to structured high-stakes queries where the model has been trained toward grounded, verifiable responses.

Here's the fine print. Independent analysis (Wire Blog's review of the methodology) finds a different picture: approximately **23% improvement at the individual claim level** and roughly **3% at the response level**. The gap between 52.5% and 3% isn't fraud — it reflects a measurement scope difference. OpenAI's numbers measure hallucinated claims in a curated high-stakes evaluation set. Independent numbers measure all responses across all query types.

The further complication: on the AA-Omniscience benchmark, GPT-5.5 Instant achieves the highest accuracy score ever recorded (57%) — but also the highest confident-wrong rate of any current top model, more than double Claude Opus 4.7 (36%) and higher than Gemini 3.1 Pro Preview (50%). The model has gotten better at being right and simultaneously more confident when it's wrong.

**What this means in practice:** If you're using GPT-5.5 Instant for medicine, law, or finance where it has been specifically trained toward caution and verification, you will see meaningful improvements over GPT-5.3. For general-purpose queries, the improvement is real but modest. And for any query where you need the model to accurately signal its uncertainty, exercise extra care — GPT-5.5 Instant's confident tone does not reliably track its actual accuracy.

---

## Pricing

| Tier | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| **Standard API** | **$5.00** | **$30.00** |
| Batch / Flex | $2.50 | $15.00 |
| Priority | $12.50 | $75.00 |
| Cached input | $0.50 | — |

**Long-context surcharge**: Prompts exceeding 272,000 tokens incur a 2x input / 1.5x output premium.

For context: GPT-5.5 Pro runs $30/$180 per million input/output tokens. GPT-5.5 Instant at $5/$30 is meaningfully cheaper for most workloads while delivering most of the capability.

The long-context surcharge at 272K is a notable pricing cliff. If your workload involves frequent 300K–500K token prompts, the effective cost is substantially higher than the headline $5 figure. For workloads staying under 272K, the pricing is competitive.

**Context window**: 1,050,000 tokens (just over 1 million). Maximum output: 128,000 tokens.

---

## What's Better, What's Worse

**Genuine improvements over GPT-5.3 Instant:**

- SWE-Bench: meaningful coding capability gain (88.7% vs GPT-5.3's estimated 82–84%)
- AIME 2025 math: 81.2 vs 65.4 — significant jump
- Terminal-Bench 2.0: state-of-the-art CLI task performance
- Speed: 20–30% faster response initiation on typical prompts
- Hallucination reduction in high-stakes domains: real, if narrower than advertised
- Enhanced personalization (memory from past chats, files, Gmail) rolling out to Plus/Pro

**Observed regressions:**

- **Creative writing quality**: Multiple reviewers note GPT-5.5 Instant produces "noticeably more formulaic output" for open-ended creative tasks compared to GPT-5.3 Instant. The conciseness optimization that reduces verbosity in technical contexts flattens creative range.
- **GPQA leadership**: The model is third on the field's most prestigious reasoning benchmark, behind Gemini 3.1 Pro Preview and GPT-5.4 Pro.
- **Confident-wrong rate**: Highest of any current top model on AA-Omniscience.

---

## The Family Context

GPT-5.5 Instant exists in a model family that has gotten genuinely complex:

| Model | Pricing | Position |
|---|---|---|
| GPT-5.5 Pro | $30 / $180 per M | Maximum capability |
| GPT-5.5 Thinking | Variable | Extended reasoning |
| **GPT-5.5 Instant** | **$5 / $30 per M** | **Default (this model)** |

GPT-4o was deprecated in February 2026. GPT-5.3 Instant is now in end-of-life mode. GPT-5.5 Instant is the new baseline, and it's a substantial baseline — not a legacy model held over by inertia, but a genuinely capable system that leads SWE-Bench and Terminal-Bench.

For most developers evaluating OpenAI's API, GPT-5.5 Instant is the right starting point: it's the default, it's well-priced for its capability tier, and it has strong benchmark coverage. The question is whether the task requires something more — longer context without the surcharge, maximum reasoning depth (Pro/Thinking), or specific domain optimizations. For most applications, the answer will be no.

---

## What Builders Should Know

**For agentic workflows and software engineering**: GPT-5.5 Instant's 88.7% SWE-Bench and 82.7% Terminal-Bench results make it a competitive choice. The speed improvement over GPT-5.4 is meaningful for agentic loops where latency compounds.

**For long-context workloads**: The 1M token window is available, but the 272K pricing cliff is real. If you're regularly sending 500K–1M token prompts, run the actual cost math before assuming $5/M input pricing.

**For high-stakes information queries**: The hallucination reduction is genuine in the specific domains OpenAI studied. Don't assume it eliminates confident incorrect responses — it doesn't.

**For creative applications**: Consider whether the formulaic regression matters for your use case. If you need the previous Instant model's creative behavior, GPT-5.3 Instant remains available until approximately August 2026.

**For researchers and competitive analysis**: The AA-Omniscience confident-wrong finding is the most interesting data point in this launch. It raises a real question about how to interpret the overall accuracy improvement — and suggests that for applications where calibrated uncertainty matters, you should run your own evaluations rather than relying on headline hallucination numbers.

---

## The Honest Assessment

GPT-5.5 Instant is a genuinely good model at a fair price point. The coding benchmarks are the strongest argument for it: 88.7% SWE-Bench is the current standard bearer for production-grade software engineering tasks. The speed improvement is real. The pricing is competitive for the capability tier.

The honest caveats are also real. The hallucination improvement is narrower than advertised. The creative regression is documented and may matter to you. The confident-wrong rate is the highest of any current top model. And on GPQA Diamond — the benchmark that best captures frontier reasoning — it's third.

OpenAI didn't make a big deal of this launch because it didn't need to. GPT-5.5 Instant is a solid, incremental improvement deployed at scale. It will serve most users well for most tasks. That's exactly what a default model should do.

Just don't mistake "default" for "best" — and read the hallucination fine print before deploying it anywhere the stakes are high.

**Rating: 4/5** — Strong everyday model with best-in-class coding benchmarks; hallucination claims are inflated, creative regressions are real, and it doesn't lead GPQA.

---

*ChatForest researches AI tools and platforms. All benchmark figures and pricing information are sourced from OpenAI's official documentation, press coverage, and independent evaluation organizations. This review was published May 23, 2026.*

