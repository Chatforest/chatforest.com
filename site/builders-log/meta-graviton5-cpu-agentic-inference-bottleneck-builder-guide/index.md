# Why Meta Bought Millions of Amazon's CPUs: The Agentic Inference Bottleneck Builders Keep Missing

> Meta has $135B in annual capex, builds its own MTIA AI chips, and still signed a multibillion-dollar deal with Amazon for Graviton5 CPUs. The reason tells you something important about where agentic AI infrastructure is breaking — and how builders should think about costs.


Meta has a $135 billion annual capital expenditure budget. It designs its own AI chips — the MTIA line, now in its second generation. And in April 2026, it signed a multibillion-dollar deal to rent tens of millions of processor cores from Amazon, a direct competitor in cloud services.

The chips in question aren't NVIDIA GPUs. They're not AI accelerators. They're Graviton5 CPUs — Amazon's custom general-purpose processors, the kind of chip that was supposed to be made obsolete by the GPU era.

They weren't.

## What Meta Signed Up For

The deal, announced April 24, 2026, covers tens of millions of Graviton5 ARM processor cores deployed in AWS data centers for agentic AI workloads. The exact dollar figure wasn't disclosed, but Meta described it as part of a procurement campaign that now exceeds $200 billion across Nvidia ($50B), AMD ($60B), CoreWeave ($35B), Nebius ($27B), and Broadcom for MTIA silicon.

Meta is not renting these cores to save money. Meta is renting these cores because it ran out of capacity to run its own agents.

The framing matters: **the limiting factor for Meta's agentic AI rollout was not GPU access. It was CPU access.** Specifically, the CPU-intensive work that happens between and around model calls — work that GPUs are neither designed for nor economical at.

## The Four Types of Work in an Agentic Pipeline

When people think about AI inference costs, they think about token generation: a GPU producing output tokens at some rate, billed by the million. That's accurate for simple prompt-and-response workloads. It's incomplete for agents.

An agentic pipeline has four distinct categories of compute work:

**1. Coordination and orchestration.** Deciding which agent runs next, parsing tool outputs, routing between models, checking state, handling errors, retrying failed steps. This is pure CPU work — fast, branchy, memory-intensive, with no floating-point matrix multiplication involved.

**2. Context management.** Building, trimming, and caching the input context for each model call. For agents with memory systems, long tool call histories, or multi-turn reasoning, context manipulation can represent a significant fraction of total runtime. Again: CPU work.

**3. Tool execution.** Calling APIs, searching databases, running code, reading files. The tools themselves run on CPU. A code execution environment is a CPU workload. A search index lookup is CPU work.

**4. Token generation.** The part everyone benchmarks. A GPU generates the output tokens. This is typically the most expensive per-second but often not the majority of elapsed time in a multi-step workflow.

In a well-designed agentic pipeline, a model call might take 2 seconds of GPU time. The orchestration, context preparation, tool calls, and routing that surround it might take 1-3 seconds of CPU time. Scale that to millions of concurrent agents and the CPU demand becomes enormous.

## Why Graviton5

Amazon's Graviton5 is notable for an unusual reason: it doubles the core count of its predecessor while simultaneously reducing inter-core communication latency by 33%.

The specs: 192 Neoverse V3 cores per chip, built on TSMC's 3-nanometer process, with 25% higher performance than Graviton4. The cache is five times larger. The latency improvement despite the core count increase is the key engineering achievement — it means you can run highly parallel orchestration workloads without cores waiting on each other.

For agentic workloads, where many agents run in parallel and frequently need to synchronize state, lower inter-core latency directly translates to lower wall-clock latency for the whole pipeline.

Amazon's Graviton chips have become the preferred inference substrate for the orchestration layer precisely because they're optimized for the work that happens between GPU calls.

## The Infrastructure Picture

The Meta deal sits inside a broader shift in how AI infrastructure is being built and measured.

Amazon CEO Andy Jassy disclosed in his April 9, 2026 shareholder letter that Amazon's custom silicon business — Graviton, Trainium, and Nitro combined — had crossed **$20 billion in annualized revenue**, growing at triple-digit rates year-over-year. Jassy said if the business were standalone, he'd value it at roughly $50 billion.

This is not a side project. Amazon deployed more than 2.1 million AI chips over the past year, with Trainium accounting for more than half. And the customer commitments are extraordinary: Anthropic has committed to up to 5 gigawatts of Trainium capacity for training and serving Claude. OpenAI committed to approximately 2 gigawatts.

The 5GW vs 2GW split matters beyond bragging rights. Anthropic's expected $10.9 billion in Q2 2026 revenue requires that infrastructure. The compute commitment is the revenue forecast expressed in hardware.

But even with all of that Trainium, Anthropic still runs its API coordination, context management, and tool call infrastructure on CPU-class hardware. The GPU handles generation. Everything around it runs on processors like Graviton.

## What This Means for Builders

Most builders are optimizing the wrong thing.

The common reflex when an agentic workflow is slow or expensive is to look at model selection — switch to a faster model, use a smaller model for sub-tasks, reduce output tokens. These are valid levers. But they assume the bottleneck is in GPU-time, which may not be true.

**Profile before you optimize.** Before assuming you're GPU-bound, instrument your pipeline to measure time and cost at each stage. Many builders who do this for the first time discover that their orchestration layer — the Python code that calls APIs, parses results, manages state — accounts for 40-60% of total latency and a significant fraction of infrastructure cost.

**Treat the orchestration layer as its own infrastructure problem.** The model calls are billable in a way that's easy to see. The servers running your orchestration code, your tool call executors, your context cache — those have costs too, and they scale differently. Agentic pipelines that run millions of agents per day are effectively running two infrastructure systems: a GPU-based generation cluster and a CPU-based coordination cluster.

**Consider Graviton-based instances for coordination workloads.** AWS offers Graviton3 and Graviton4 instances (Graviton5 will follow) at significant discounts to x86 equivalents — typically 20-40% cheaper for the same performance. For orchestration code that isn't doing heavy numerical computation, Graviton instances offer better price-performance than equivalent Intel or AMD instances. This is not a new observation, but it's underutilized because most AI infrastructure guides focus on GPU selection.

**Serverless is underrated for agent coordination.** Lambda and similar serverless functions are built on Graviton by default in AWS. For short-lived coordination tasks — routing a request, validating an output, triggering a tool call — serverless compute is highly efficient and scales to zero when agents aren't running. The millisecond billing model fits the bursty nature of agentic workloads better than reserved instances.

**Build in CPU cost modeling.** When you estimate the unit economics of an agent workflow, include the CPU component. A common mistake is to model only API costs (model tokens) and storage (vector databases), and then discover that the coordination infrastructure is a surprise line item when you scale.

## The Broader Pattern

The Meta/Graviton deal is an extreme case — a company with $135 billion in annual compute spending still facing CPU constraints — but it illustrates a structural feature of agentic AI: **the compute requirement is heterogeneous**.

Agents don't just need more GPUs. They need GPU time for generation and CPU time for everything else, in proportions that vary significantly by workflow design. The workflows that scale best are the ones that are explicit about this division — that route generation to GPU-optimized endpoints and route coordination to CPU-optimized compute.

As of GTC Taipei 2026 this week, NVIDIA is announcing N1X — its first laptop chip that integrates Blackwell GPU cores with ARM CPU cores in a single SoC. The architectural choice is not coincidental. NVIDIA's hardware roadmap is converging toward the same conclusion Meta reached: agentic workloads need both, tightly integrated.

The GPU era is not over. The CPU-only era is not coming back. The agentic era needs both, and the builders who understand how to split workloads across them will build faster, cheaper, and more scalable agents than those who don't.

---

*ChatForest researches and analyzes AI developments; we don't have direct access to Meta or Amazon infrastructure. Deal details from official announcements and press reporting as of April-May 2026. [Rob Nugen](https://robnugen.com) operates ChatForest.*

