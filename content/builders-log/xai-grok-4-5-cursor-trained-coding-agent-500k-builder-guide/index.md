---
title: "Grok 4.5: SpaceXAI and Cursor's Jointly Trained Coding Agent — 500K Context, $2/MTok, #1 Agentic Tool Use"
date: 2026-07-08
description: "Released July 8, 2026, Grok 4.5 is SpaceXAI's first model co-developed with Cursor and trained on real IDE session data. 500K context, $2/$6 per MTok, configurable reasoning effort, #1 on Artificial Analysis agentic tool use. Trails Fable 5 on DeepSWE but leads on SWE Marathon. Not available in EU. Here is the builder case for it."
tags: ["llm", "grok", "xai", "spacexai", "cursor", "coding-agent", "agentic-ai", "frontier-model", "api", "developer-tools"]
sources_audited: 2026-08-05
---

On July 8, 2026, [SpaceXAI released Grok 4.5](https://x.ai/news/grok-4-5) — its first model co-developed with Cursor, trained on real developer session data from the Cursor IDE. The release was broken by [Axios](https://www.axios.com/2026/07/08/spacexai-grok-new-model) and covered in depth by [MarkTechPost](https://www.marktechpost.com/2026/07/08/spacexai-releases-grok-4-5/) and [DataCamp](https://www.datacamp.com/blog/grok-4-5). This is a research-based guide; we reviewed those sources and independent benchmark data from [BenchLM](https://benchlm.ai/models/grok-4-5) and [Artificial Analysis](https://artificialanalysis.ai/models/grok-4-5). We did not run the model ourselves.

---

## What Grok 4.5 is

Grok 4.5 is [SpaceXAI's targeted model for coding, agentic tool calling, and knowledge work](https://www.marktechpost.com/2026/07/08/spacexai-releases-grok-4-5/). It is not a general-purpose frontier model or a reasoning flagship — it is purpose-built for developer workflows and multi-step agent tasks, specifically the kind that happen inside an IDE over an extended session.

The model runs with a [500,000-token context window](https://datanorth.ai/news/xai-releases-grok-4-5-coding-focused-model), accepts text and image inputs, and supports [configurable reasoning effort (low, medium, or high — high is the default)](https://docs.x.ai/developers/grok-4-5). [Knowledge cutoff is February 1, 2026](https://docs.x.ai/developers/grok-4-5), per xAI's own model documentation.

Grok 4.5 is built on SpaceXAI's V9 foundation — the same [1.5-trillion-parameter base](https://x.com/elonmusk/status/2071184354756477041) Elon Musk described when announcing the model's private beta — with additional training specifically for coding and agent tasks, per [MarkTechPost's coverage](https://www.marktechpost.com/2026/07/08/spacexai-releases-grok-4-5/). SpaceXAI trained it across [tens of thousands of NVIDIA GB300 GPUs](https://www.datacamp.com/blog/grok-4-5) on coding, science, engineering, and mathematics data, with reinforcement learning covering "hundreds of thousands of tasks, including agent runs that lasted for hours."

---

## The Cursor data advantage

The distinguishing fact about Grok 4.5 is where part of its training data came from. Per [SpaceXAI's launch announcement](https://x.ai/news/grok-4-5), the model was trained on real Cursor session data — actual interaction logs from developers working inside live codebases. That data does not exist anywhere outside of Cursor's servers. No standalone model lab has it.

This matters in a specific, narrow way: the model's training distribution includes what engineers actually do in long IDE sessions, not what researchers construct as proxy tasks. On the specific agentic-tool-use dimension of the [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/grok-4-5-brings-spacexai-to-the-the-intelligence-frontier), Grok 4.5 "takes the top position" — the one benchmark category most directly correlated with that training signal. (Note: this is a sub-dimension ranking, not the overall Intelligence Index, where Grok 4.5 placed #4 — see benchmark table below. Artificial Analysis and BenchLM re-run these evaluations continuously, so newer models may have since overtaken this specific ranking.)

Whether Cursor-sourced training data provides durable advantage over larger-scale synthetic approaches is not settled. But the benchmark result exists, and the mechanism is plausible.

---

## Benchmark results

Based on [BenchLM's independent benchmarks](https://benchlm.ai/models/grok-4-5) and [DataCamp's comparative analysis](https://www.datacamp.com/blog/grok-4-5):

| Benchmark | Grok 4.5 | Notes |
|---|---|---|
| **DeepSWE 1.0** | 62.0% | Trails Claude Fable 5 |
| **DeepSWE 1.1** | 53.0% | Trails Claude Fable 5 |
| **Terminal-Bench 2.1** | 83.3% | Within 1 point of the leader |
| **SWE-Bench Pro** | 64.7% | Trails Claude Fable 5 |
| **SWE Marathon** | 29% | Leads Opus 4.8 (26%) |
| **Artificial Analysis Intelligence Index** | 54, #4 overall | #1 on agentic tool use |

[DataCamp's analysis](https://www.datacamp.com/blog/grok-4-5) summarizes the picture accurately: Grok 4.5 leads on SWE Marathon and tops the agentic tool use ranking, but Claude Fable 5 leads on DeepSWE 1.0, DeepSWE 1.1, and SWE-Bench Pro. Grok 4.5 is #1 at the task type most resembling a real multi-step agent run; it trails on isolated repository-editing tasks where Fable 5 is optimized.

On speed, SpaceXAI claims approximately 80 tokens per second, while [Artificial Analysis' independent measurement in mid-July](https://www.datacamp.com/blog/grok-4-5) put it closer to 120 tokens per second. (Artificial Analysis re-benchmarks models on a rolling basis, so its live model page may show a different current figure than this mid-July snapshot.)

---

## Pricing

Standard pricing per [SpaceXAI's official page](https://x.ai/news/grok-4-5) and [DataCamp](https://www.datacamp.com/blog/grok-4-5):

| Item | Rate |
|---|---|
| Input (first 200K context) | $2.00 / MTok |
| Output | $6.00 / MTok |
| Cached input | $0.50 / MTok |
| Web search / X search / code execution | $5.00 / 1K calls |
| File attachment search | $10.00 / 1K calls |

A fast-serving variant is available at approximately $4/$18 per MTok input/output for latency-sensitive paths, [per launch coverage](https://explainx.ai/blog/grok-4-5-public-launch-spacexai-july-2026). [Cursor offered 50% off Grok 4.5 usage at launch](https://explainx.ai/blog/cursor-doubled-usage-limits-again-july-21-2026), a promotion that ran through July 21 before reverting to standard rates.

For comparison: Claude Opus 4.8 lists at [$5/$25 per MTok](https://platform.claude.com/docs/en/about-claude/pricing) (input/output) — Anthropic's standard API rate, [confirmed independently](https://www.vellum.ai/blog/claude-opus-4-8-benchmarks-explained). At $2/$6, Grok 4.5 is roughly 2.5–4× cheaper per token, not the double-digit multiple sometimes floated in early coverage. The comparison is not apples-to-apples — Opus 4.8 has a broader capability profile — but for coding and agentic tasks specifically, the cost gap is still meaningful.

---

## Where it is available

Per [SpaceXAI's announcement](https://x.ai/news/grok-4-5) and [DataCamp](https://www.datacamp.com/blog/grok-4-5):

- **SpaceXAI API console** — model ID: `grok-4.5` — OpenAI-compatible endpoints
- **Grok Build** — default model as of launch
- **Cursor** — all plans, including free
- **Model gateways** — OpenRouter, Vercel AI SDK, Cloudflare, Snowflake, Databricks Mosaic
- **Office add-ins** — SpaceXAI's enterprise integrations

**EU availability:** Not available as of launch day. [SpaceXAI cited EU AI Act compliance](https://www.trendingtopics.eu/spacexai-and-cursor-launch-grok-4-5-not-yet-in-the-eu/) as the reason. Expected later in July 2026 per their updated developer guide.

---

## Builder decision guide

**Use Grok 4.5 when:**
- You are building multi-step agent workflows where tool calling and action chains are the primary cost driver
- Your tasks look like long IDE sessions — multi-file edits, repo exploration, iterative debugging — rather than one-shot code generation
- Token cost is a constraint and you need something closer to Opus-class quality at $2 input (not $5)
- You are already in the Cursor ecosystem and the 50% launch discount reduces risk

**Consider alternatives when:**
- You need maximum accuracy on isolated repository-editing benchmarks (SWE-Bench Pro, DeepSWE 1.0/1.1) — Fable 5 leads there
- Your users are in the EU — Grok 4.5 is not available there yet
- You need longer context than 500K tokens — [Thinking Machines' Inkling](https://thinkingmachines.ai/news/introducing-inkling/) (1M context) or [xAI's own Grok 4.20](https://www.digitalapplied.com/blog/grok-4-20-full-release-2m-context-lowest-hallucination) (2M context) may fit better for very large codebases
- Knowledge cutoff matters: February 1, 2026 means events from the past five months are not in its training

The $2/$6 pricing opens Grok 4.5 to workloads where cost previously ruled out a frontier model. The agentic tool use advantage is real and documented. The benchmark shortfall versus Fable 5 on static coding tasks is also real. Neither story is wrong — they describe the same model at different points in the benchmark surface.
