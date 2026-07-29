# Artificial Analysis Launches AA-AgentPerf: The First Hardware Benchmark Built for Agentic AI Workloads

> Artificial Analysis released AA-AgentPerf, a hardware benchmark that replays real multi-turn coding agent trajectories with up to 200 turns and 100K+ token sequences. It sits alongside the original AA-SLT benchmark on their hardware page and measures concurrent agent capacity — not just throughput — across NVIDIA and AMD systems.


Artificial Analysis [released **AA-AgentPerf**](https://artificialanalysis.ai/articles/aa-agentperf), which it calls ["the first agentic inference benchmark"](https://artificialanalysis.ai/articles/aa-agentperf), designed specifically for agentic AI workloads, alongside the original AA-SLT (System Load Test) benchmark on their [hardware evaluation page](https://artificialanalysis.ai/benchmarks/hardware). NVIDIA independently corroborated the "first" framing, [describing AA-AgentPerf as "the industry's first multi-vendor open benchmark"](https://developer.nvidia.com/blog/nvidia-achieves-leading-agentic-coding-performance-on-first-agentic-ai-benchmark/) for agentic workload performance after its GB300 NVL72 and H200 systems were evaluated on it. The timing matters: as AI workloads shift from single-turn completions to multi-turn agent sessions, the hardware rankings that guided infrastructure decisions in 2024 and 2025 no longer necessarily hold.

This is a research-based summary. We have not executed any of the tools or infrastructure described here.

---

## Why a new benchmark

Most GPU benchmarks measure throughput and latency on short or medium prompts answered in a single pass. That reflects how people used AI in 2023. It does not reflect how agents work.

A coding agent running in Claude Code or Cline or OpenCode does not send one 500-token prompt. It sends 200 messages, accumulates a 100,000-token context, calls tools, re-reads modified files, and then sends another turn. Each turn lands on the inference stack with a long KV cache already populated from prior turns. The prefill/decode ratio, the cache hit rate, and the sustained throughput over long sessions are completely different from what single-turn benchmarks exercise.

AA-AgentPerf addresses this gap by replaying actual multi-turn coding agent trajectories — not synthetic workloads — against real hardware, with the production optimizations that inference providers actually use.

---

## What AA-AgentPerf measures

The benchmark evaluates:

- **Concurrent agent capacity** at a target output speed and time-to-first-token
- **Metrics normalized [per accelerator, per system, and per megawatt](https://artificialanalysis.ai/methodology/agentperf)** (per-$/hr and total-cost-of-ownership views are [described as planned future additions](https://artificialanalysis.ai/articles/aa-agentperf), not current metrics)
- **Real trajectory lengths**: [up to 200 turns, with input lengths ranging from ~5K to ~131K tokens per request (mean ~27K) and contexts reaching beyond 100K tokens](https://artificialanalysis.ai/articles/aa-agentperf)
- **Production optimizations allowed**: [KV cache reuse, disaggregated prefill/decode, and speculative decoding](https://artificialanalysis.ai/articles/aa-agentperf)

That last point is significant. Benchmarks that prohibit production optimizations measure how hardware performs in artificial conditions, not how it performs in deployment. AA-AgentPerf is explicitly designed to reflect what buyers actually see when they run agents.

The metric itself also differs from standard benchmarks. AA-SLT, Artificial Analysis's original benchmark, [reports peak system output throughput in tokens per second](https://artificialanalysis.ai/benchmarks/hardware) — useful for single-turn workloads. AA-AgentPerf reports how many agents you can serve concurrently at an acceptable latency target, which is the operational question builders actually face: *how many parallel agent sessions can this hardware handle without degrading?*

---

## Hardware in scope

[AA-AgentPerf's first wave of results compares](https://artificialanalysis.ai/articles/aa-agentperf):

- **NVIDIA**: GB300-NVL72, B300, H200
- **AMD**: MI355X

[Rolling submissions are open now](https://artificialanalysis.ai/articles/aa-agentperf), meaning providers can submit benchmark configurations on an ongoing basis and results publish as they come in. The [first wave of results covers **DeepSeek V4 Pro**](https://artificialanalysis.ai/articles/aa-agentperf) across those systems; **gpt-oss-120b** is listed as coming soon.

---

## How this differs from AA-SLT

| | AA-AgentPerf | AA-SLT |
|---|---|---|
| Workload type | Multi-turn agent trajectories (100K+ tokens) | Short/medium prompts, single-turn |
| Primary metric | Concurrent agent capacity at target SLO | System throughput + per-query speed |
| Production optimizations | Allowed | Controlled |
| Use case | Choosing hardware for agent deployments | Choosing hardware for general LLM inference |

Both benchmarks live on the same hardware page so infrastructure buyers can evaluate a system on both workload types simultaneously.

---

## What this means for builders

**If you buy or rent GPU infrastructure for agent workloads, you need this benchmark.** Hardware that leads single-turn benchmarks can underperform on sustained multi-turn sessions because the workload profile is fundamentally different:

- Long KV caches put different pressure on memory bandwidth and HBM capacity
- Multi-turn sessions with 200 turns stress sustained throughput, not peak throughput
- Disaggregated prefill/decode (separating the long prompt ingestion step from the shorter generation step) changes which hardware configuration wins

The practical implication: a cloud GPU configuration optimized for RAG or chatbot latency may not be the right configuration for running hundreds of simultaneous coding agents. AA-AgentPerf gives you a data point you did not have before.

**For inference providers**, the benchmark creates a new competitive dimension. A provider might lead AA-SLT rankings for cheap general inference but fall behind on AA-AgentPerf if their hardware configuration does not support the long-context, high-KV-cache profile of agentic work. Expect providers to start citing AA-AgentPerf scores in their pricing and capacity pages as the agentic workload share grows.

**For multi-agent system designers**, the concurrent agent capacity metric maps directly to one of the core architecture decisions: how many parallel subagents can you economically run before you exhaust capacity? That is a different question from "how fast is a single agent?" and it needs a different benchmark to answer it.

---

## Where to find the data

The AA-AgentPerf results are published at the [Artificial Analysis hardware benchmarking page](https://artificialanalysis.ai/benchmarks/hardware) alongside AA-SLT.

The benchmark's full methodology — including SLO tiers, power-measurement approach, and trajectory construction — is published on Artificial Analysis's [AA-AgentPerf methodology page](https://artificialanalysis.ai/methodology/agentperf).

---

## Bottom line

Agentic AI workloads have a different hardware performance profile than single-turn inference. Artificial Analysis now provides a benchmark that measures the profile that actually matters for agent deployments. If you are making GPU infrastructure decisions for agent pipelines in 2026, AA-AgentPerf should be in your evaluation alongside AA-SLT — not instead of it.

