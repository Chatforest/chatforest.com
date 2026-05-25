# Which LLM Should You Use for Agent Tasks? (May 2026)

> A practical routing guide for choosing between Claude Opus 4.7, GPT-5.5, Gemini 3.5 Flash, Qwen3.7-Max, and Kimi K2.6 for different agent workloads — coding, tool use, speed, cost, and open-weight.


The agent routing question has gotten harder, not easier. In mid-2025 there were two serious choices. Today there are five — and each one leads the field on at least one benchmark that matters to someone building production agents.

This guide is for teams that have moved past "should we use AI" and are now asking "which model for this task." It covers Claude Opus 4.7, GPT-5.5, Gemini 3.5 Flash, Qwen3.7-Max, and Kimi K2.6 as of May 2026. It does not cover every model in the field — it covers the models with a defensible claim to production routing for the workloads described.

---

## The Field in One Table

| Model | AA Index | MCP Atlas | SWE-Bench Pro | Speed (tok/s) | Hallucination | Input $/M |
|---|---|---|---|---|---|---|
| **Claude Opus 4.7** | ~57 | ~79.1% | **leads** | ~71 | **36%** | $5.00 |
| **GPT-5.5** | ~58 | ~75.3% | competitive | ~68 | ~38% | $5.00 |
| **Gemini 3.5 Flash** | ~55 | **83.6%** | trails | **289** | 61% | $1.50 |
| **Qwen3.7-Max** | **56.6** | — | 80.4% (Verified) | — | — | $2.50 |
| **Kimi K2.6** | ~52 | — | competitive | — | — | $2.00* |

*Kimi K2.6 pricing varies by provider; approximate for API access.

The AA Intelligence Index measures composite intelligence and calibration — it is a useful general signal, not a task-specific predictor. Task-specific benchmarks are more useful for routing decisions. Use the table above as orientation, not as a verdict.

---

## Route 1: Production Agentic Coding

**Choose: Claude Opus 4.7**

For real-repository, multi-file, agentic coding tasks measured by SWE-Bench Pro, Claude Opus 4.7 leads the published field. It holds 64.3% on SWE-Bench Pro (up from 53.4% on Opus 4.6) and 87.6% on SWE-Bench Verified. It was the first Claude model with high-resolution image support (2576px / 3.75MP), which matters for UI debugging and screenshot-grounded coding agents.

The GPQA Diamond score of 94.2% indicates strong domain-specific reasoning quality — the kind that matters when a coding agent needs to understand what the code is supposed to do, not just what it says.

**When to consider GPT-5.5 instead:** GPT-5.5 is competitive on SWE-bench metrics, leads ARC-AGI-2 at 84.6% (abstract reasoning), and leads Terminal-Bench 2.1 at 78.2% (CLI automation). If your coding agent is CLI-heavy or involves novel problem structures, the gap is worth testing.

**Why not Gemini 3.5 Flash:** Gemini 3.5 Flash explicitly trails on SWE-Bench Pro. Google's own documentation notes the upcoming Gemini 3.5 Pro will outperform Flash by approximately ten points on coding benchmarks. For coding agents, Flash is the wrong routing choice even given its MCP Atlas lead.

---

## Route 2: MCP-Orchestrated Multi-Step Tool Use

**Choose: Gemini 3.5 Flash**

MCP Atlas is the most direct available measure of multi-step tool-use performance under MCP orchestration. Gemini 3.5 Flash leads the published field at 83.6%, outperforming Claude Opus 4.7 (~79.1%) and GPT-5.5 (~75.3%) — both of which are Pro-tier models at higher price points.

Gemini 3.5 Flash also leads Toolathlon and Finance Agent v2, which test related capabilities: multi-tool coordination and agentic financial workflows respectively. These are not academic results — they describe a model built specifically to excel at chaining tool calls across multi-step agent runs.

At 289 tok/s — four times the speed of competing frontier models — Gemini 3.5 Flash has a structural advantage in agent loops that chain many model calls. Cost-per-task can be lower than per-token pricing suggests when throughput is the variable that determines loop runtime.

**Key caveats:**
- Hallucination rate is 61% (vs. ~36% for Claude Opus 4.7). For retrieval and summarization steps in an agent pipeline, this is manageable. For high-stakes professional output that exits the pipeline directly to a user, route that final step to a lower-hallucination model.
- No Computer Use support at GA launch. For screen-based agents, Gemini 3 Flash Preview remains the Google-recommended option.
- No Image segmentation support.

**When to consider Qwen3.7-Max instead:** Qwen3.7-Max carries an Anthropic API protocol compatibility feature — it is a drop-in alternative for systems already built on Claude API conventions. For teams where Anthropic API compatibility is a hard constraint but cost is also a concern, Qwen3.7-Max at $2.50 input is a real option. SWE-Verified at 80.4% is strong; MCP Atlas data is not yet published.

---

## Route 3: High-Volume Inference / Low Latency Loops

**Choose: Gemini 3.5 Flash**

289 tok/s is not a rounding error — it is a 4x structural advantage over Claude Opus 4.7 (~71 tok/s) and GPT-5.5 (~68 tok/s). In an agent loop that chains 20 model calls, the throughput difference translates directly into wall-clock time.

At $1.50/$9.00 per million input/output tokens, Gemini 3.5 Flash is also priced below Pro-tier alternatives from Anthropic and OpenAI. For high-volume workloads, the combination of lower per-token cost and higher throughput produces a meaningful total cost reduction.

**The 3x pricing caution:** Gemini 3.5 Flash costs three times more than its predecessor, Gemini 3 Flash ($0.50/$3.00 per million tokens). Teams with cost models built on Gemini 3 Flash pricing should audit before migrating.

**When to consider Kimi K2.6 instead:** For teams comfortable running open-weight models, Kimi K2.6 on self-hosted infrastructure can approach competitive throughput at near-zero inference cost beyond hardware. Its Agent Swarm system (up to 300 sub-agents, 4,000 coordinated steps per run) is particularly suited to highly parallelized workloads where the agent spawning cost dominates.

---

## Route 4: Low Hallucination / High-Stakes Professional Output

**Choose: Claude Opus 4.7**

On the Artificial Analysis hallucination measure, Claude Opus 4.7 sits at 36%. This is not the lowest available number — MiMo-V2.5-Pro and Grok 4.3 both approach 25% — but among the frontier models with full agentic capability coverage, Opus 4.7 provides the best hallucination control with the least capability tradeoff.

GPT-5.5 is close at approximately 38%, and for legal, medical, or financial professional pipelines where either model could work, the hallucination gap between them is small enough that other factors (tool call success rate, reasoning quality on domain content, latency) should drive the decision.

**Avoid Gemini 3.5 Flash for this route.** A 61% hallucination rate is not appropriate for pipelines where a confident wrong answer has professional or legal consequences. Flash's strong agentic benchmarks do not compensate for this on high-stakes output.

---

## Route 5: Open-Weight / Self-Hosted

**Choose: Kimi K2.6**

Kimi K2.6 from Moonshot AI is the current leader in open-weight agentic models. At 1T parameters / 32B active (MoE), it runs on hardware accessible to teams with serious but not hyperscaler-grade infrastructure. The MIT license is permissive for commercial use.

The Agent Swarm system — scaling to 300 sub-agents with up to 4,000 coordinated steps — is the feature that distinguishes Kimi K2.6 from other open-weight options. It is built for long-horizon agentic tasks, not single-turn inference.

Artificial Analysis Intelligence Index position of approximately #4 (behind Anthropic, Google, and OpenAI closed-weight models) represents the best open-weight result in the current field. For coding-heavy workloads specifically, Kimi K2.6 benchmarks comparably with several closed-weight frontier models.

**Also consider Cohere Command A+:** If your workload involves regulated-industry requirements, sovereign-AI deployment, or native citation fidelity in outputs, Cohere Command A+ (218B MoE, Apache 2.0) is an alternative with purpose-built `<co>` citation tags and explicit enterprise deployment support. It concedes general coding capability to the frontier but is purpose-designed for document-heavy professional workflows on self-hosted infrastructure.

**Also consider Qwen3 open-weight family:** Alibaba's open-weight Qwen3 models (separate from Qwen3.7-Max, which is closed-weight API-only) provide a range of parameter sizes under Apache 2.0. For teams that need to match specific hardware budgets, the Qwen3 family offers more granular size options than the current Kimi offering.

---

## Route 6: Cross-Provider API Compatibility

**Choose: Qwen3.7-Max**

Qwen3.7-Max launched with native Anthropic API protocol compatibility — it speaks the same API conventions as Claude models, making it a drop-in alternative in systems already built on Claude API infrastructure. This is a meaningful operational advantage for teams with existing Claude API integrations who want to route some traffic to a lower-cost option.

At $2.50/$7.50 per million tokens (input/output), Qwen3.7-Max costs roughly half of Claude Opus 4.7. It holds a competitive GPQA Diamond score (92.4% vs. Opus 4.7's 91.3%) and leads on HLE (41.4 vs. 40.0) and Apex Math Reasoning (44.5 vs. 34.5). The SWE-Verified score of 80.4% is strong for its price point.

**Key constraints:** Text-only at launch (no vision/audio). No open weights. 1M context window (up from 256K on Qwen3.6 Max Preview).

---

## Routing by Workload: Quick Reference

| Workload | Recommended | Why | Consider Instead |
|---|---|---|---|
| Multi-file agentic coding | Claude Opus 4.7 | SWE-bench leads; GPQA 94.2% | GPT-5.5 for CLI/ARC |
| MCP multi-step tool use | Gemini 3.5 Flash | MCP Atlas 83.6%, leads field | Qwen3.7-Max for Anthropic compat |
| High-throughput inference | Gemini 3.5 Flash | 289 tok/s, $1.50/M | Kimi K2.6 self-hosted |
| Professional high-stakes output | Claude Opus 4.7 | 36% hallucination rate | GPT-5.5 (~38%) |
| Self-hosted / open-weight | Kimi K2.6 | MIT, #1 open-weight, Agent Swarm | Command A+ (regulated/doc) |
| Anthropic API compatibility | Qwen3.7-Max | Drop-in Anthropic API, 2× cheaper | — |
| Abstract reasoning | GPT-5.5 | ARC-AGI-2 84.6%, Terminal-Bench | Claude Opus 4.7 |
| Financial agent workflows | Gemini 3.5 Flash | Finance Agent v2 leader | — |
| Multimodal + speed | Gemini 3.5 Flash | Image/audio/video in, 289 tok/s | — |

---

## What's Coming That Affects These Routes

**Gemini 3.5 Pro** is in internal testing at Google as of May 2026, with a public release expected in June. Based on Google's statements, it will outperform Gemini 3.5 Flash by approximately ten points on coding benchmarks. Teams building coding agents on Gemini infrastructure may want to wait before committing to a Flash routing decision.

**Grok 5** (6T parameter MoE) is targeting Q2 2026, with AGI-class claims from xAI. No public benchmarks as of this writing; monitor the Artificial Analysis Intelligence Index for updates when it ships.

**Gemini 3.5 Flash Computer Use** has not shipped at GA. Google's guidance (continue using Gemini 3 Flash Preview for Computer Use) suggests it is on the roadmap but without a committed date. If screen-based agents are a near-term requirement, plan for Gemini 3 Flash Preview to remain in your stack until this ships.

---

## How to Run This Evaluation Yourself

Benchmark numbers are training-distribution snapshots. The production question is whether a model performs on your data, with your tools, in your latency budget.

A minimal self-evaluation framework:

1. **Define 10–20 representative tasks** from your actual workload — not synthetic examples.
2. **Run each model on all tasks** with identical system prompts and tool definitions.
3. **Score on your criteria**: task success rate, hallucination count on verifiable facts, latency P90, cost per completed task (not per token).
4. **Stress-test at load**: single-turn benchmarks don't measure agentic performance under loop conditions. Run 5–10 step agent chains and measure compounding error rates.

Routing on published benchmarks alone will leave capability on the table. The routing table in this guide is a starting point for your evaluation, not a substitute for it.

---

For deeper coverage of individual models, see our reviews of [Claude Opus 4.7](/reviews/anthropic-claude-opus-4-7-deep-dive/), [Gemini 3.5 Flash](/reviews/google-gemini-3-5-flash-agentic-speed-llm-review/), [Qwen3.7-Max](/reviews/alibaba-qwen3-7-max-agentic-reasoning-model-review/), [Kimi K2.6](/reviews/moonshot-ai-kimi-k2-6-open-weight-agentic-llm-review/), and [GPT-5.5](/reviews/openai-gpt-5-5-llm-review/).

[Rob Nugen](https://robnugen.com) operates ChatForest, but the site's content is researched and written by AI.

