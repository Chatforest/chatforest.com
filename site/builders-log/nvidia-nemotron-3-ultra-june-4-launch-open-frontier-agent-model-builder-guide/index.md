# Nemotron 3 Ultra Launches June 4: The First Open Frontier Model Built for Agents

> Nvidia's Nemotron 3 Ultra — 550B parameters, 55B active, 300+ tokens/second — goes live on Hugging Face, OpenRouter, and build.nvidia.com on June 4. Here is what builders need to know about deploying it, what the open-weights model means for API economics, and why the DGX Station and RTX Spark hardware roadmap matters.


At GTC Taipei on June 1, Jensen Huang announced a 550-billion-parameter open model that runs at 300 tokens per second, costs 30% less to operate than comparable frontier models, and is specifically designed for multi-step agent workflows. It launches publicly on June 4.

**Nemotron 3 Ultra** is not NVIDIA's first open model — the Nemotron line goes back to 2024. But it is the first to land squarely in the territory that closed-API providers like OpenAI and Anthropic have owned: frontier-scale, production-grade intelligence with native agent reasoning. If you have been waiting for open weights to reach the quality tier where they are viable for production agent pipelines, June 4 is the inflection point worth paying attention to.

This is the what-it-is, how-to-deploy-it, and what-to-do-with-it breakdown.

---

## What Nemotron 3 Ultra Actually Is

**Nemotron 3 Ultra** uses a **mixture-of-experts (MoE) architecture**: 550 billion total parameters, 55 billion active per forward pass. The MoE structure is why NVIDIA can claim frontier-quality output at inference costs closer to a 55B dense model than a 550B dense model — at any given token, only a fraction of the network fires.

Key published numbers from the June 1 keynote:

| Metric | Nemotron 3 Ultra |
|---|---|
| Total parameters | 550B |
| Active parameters per token | ~55B |
| Context window | 1M tokens |
| Intelligence Index | 48 |
| Output throughput | 300+ tokens/second |
| Claimed cost vs. comparable frontier | ~30% lower |
| Claimed speed vs. comparable frontier | ~5x faster |
| Weights license | Open (to be confirmed at launch) |

The **Intelligence Index of 48** puts it above current top-ranked US open-weight models. NVIDIA has not published a full benchmark table yet, but the GTC Taipei keynote cited specific domains: coding, research, and multi-step enterprise workflows.

The **1M token context** is meaningful for agent pipelines — it means you can feed long conversation history, large codebases, or extended document sets without chunking. Most builders running agents today are constrained by context at 200K or 400K; a 1M window changes what you can keep in a single pass.

---

## Why "Built for Agents" Is a Different Claim

Frontier language models have generally been trained for human conversation: a user sends a prompt, the model responds, the user reads. Agent workflows are structurally different: the model receives a task, calls tools, evaluates results, decides next steps, and loops — sometimes for hundreds of turns across many minutes.

NVIDIA designed Nemotron 3 Ultra's training data and fine-tuning process around this loop structure, not around single-turn conversation quality. The specific improvements they cite:

- **91% agent productivity** on their internal benchmark — the model successfully completes assigned multi-step tasks without human re-intervention
- Trained on **ReAct patterns** and **tool-invocation sequences** at scale
- Long-context attention mechanism designed for **accumulated state**: tool outputs, prior reasoning traces, and memory objects accumulated over a long task session

The practical test for builders is how the model handles **error recovery**: when a tool call fails or returns unexpected output, does the model adapt its strategy or get stuck? NVIDIA's published claim is that error recovery is a primary training objective.

---

## Where to Get It on June 4

Nemotron 3 Ultra will be available through four channels simultaneously at launch:

**1. Hugging Face** — open-weights download. Free to use, no rate limits, but you supply your own GPU infrastructure. The model card will include the license terms, which NVIDIA has not published in full yet. Expect a research or community license similar to LLaMA 4 Maverick's terms.

**2. ModelScope** — NVIDIA's China-accessible distribution partner for developers building in that region.

**3. OpenRouter** — Managed inference API, pay-per-token. OpenRouter already hosts Nemotron 3 Super (120B) as a free tier entry point. Ultra will likely land with similar tiered pricing: free for low-volume requests, per-token cost for sustained throughput.

**4. build.nvidia.com (NIM microservices)** — NVIDIA's hosted API catalog. Free for prototyping through the NVIDIA Developer Program, rate-limited, no credit card required. Production use requires NVIDIA AI Enterprise (priced from $4,500/GPU/year or ~$1/GPU/hour via cloud partner).

For most builders evaluating the model, start with **build.nvidia.com free tier** or **OpenRouter**. Both let you run API calls without standing up GPU infrastructure. The HuggingFace weights are the path for teams that want to self-host, fine-tune, or run behind their own firewall.

---

## The Deployment Decision Tree

The choice between deploying Nemotron 3 Ultra and using a closed frontier model (GPT-5.x, Claude Sonnet/Opus, Gemini 3.x) depends on a few questions:

**Does your use case require fine-tuning?**

Closed API models do not expose weights. If your agent needs to internalize proprietary domain knowledge — specific internal vocabulary, specialized reasoning patterns, confidential product data — you cannot fine-tune GPT or Claude. With Nemotron 3 Ultra's open weights, fine-tuning on a controlled dataset is possible. You need GPU infrastructure to do it, but the capability exists.

**What are your data privacy requirements?**

Sending data to a third-party API means your data leaves your infrastructure. For regulated industries (healthcare, finance, legal), this creates compliance overhead. Self-hosted Nemotron on your own infrastructure or NVIDIA DGX Station means data never leaves your control.

**Are you optimizing for speed or cost?**

NVIDIA claims 300+ tokens/second through NIM. At that throughput, Nemotron 3 Ultra is viable for latency-sensitive agent workflows that would be too slow with models like Claude Opus or GPT-5.5. The 30% cost reduction claim needs production validation, but if it holds at scale, the economics shift meaningfully for high-volume pipelines.

**Does agent-specific training matter for your task?**

For simple tool-calling agents — retrieve, summarize, respond — general-purpose frontier models work fine and have well-established developer tooling. For long-horizon autonomous tasks (debug a codebase, run a multi-step research workflow, manage a persistent process over hours), Nemotron 3 Ultra's agent-specific training may provide reliability improvements that justify migrating.

---

## What NemoClaw Adds (And Where That Article Lives)

Nemotron 3 Ultra does not stand alone. NVIDIA launched it alongside **NemoClaw**, an open-source orchestration framework for building agent pipelines on top of Nemotron models. NemoClaw handles task decomposition, multi-agent delegation, tool invocation with error recovery, and policy enforcement through **OpenShell** — a sandboxed runtime that prevents agents from accessing unauthorized system resources.

We covered NemoClaw and OpenShell in detail in a separate guide: [Jensen Huang Called OpenClaw the New Linux. NemoClaw Is How You Deploy It Safely.](/builders-log/nvidia-nemoclaw-gtc-taipei-openclaw-enterprise-security-builder-guide/) If you are building on Nemotron 3 Ultra for enterprise or security-sensitive workflows, read that first.

The short version: NemoClaw + Nemotron 3 Ultra is NVIDIA's answer to "how do you run production agents without relying on a closed-model API provider."

---

## The Hardware Roadmap That Makes Local Deployment Viable

Right now, self-hosting a 550B parameter MoE model requires meaningful GPU infrastructure — this is not a laptop experiment. But NVIDIA's hardware announcements at GTC Taipei/Computex change the mid-term trajectory for local inference:

**DGX Station for Windows** — NVIDIA's new deskside workstation runs the GB300 Grace Blackwell Ultra superchip with 775GB of coherent unified memory. That is enough headroom to run Nemotron 3 Ultra at production-grade throughput, locally, without cloud dependency. Partners including HP, Dell, Asus, Supermicro, and MSI are bringing DGX Station systems to market in Q4 2026; HP has confirmed August availability for their unit.

**RTX Spark** (formerly codenamed N1X) — the consumer/developer play: a laptop superchip with an Arm-based Grace CPU and Blackwell GPU sharing 128GB of unified LPDDR5X memory. RTX Spark won't run a full 550B model, but NVIDIA has Nemotron 3 Nano and Nemotron 3 Super (120B) in the same family for local inference on smaller hardware. RTX Spark systems from Dell, HP, Lenovo, Asus, and MSI arrive in fall 2026.

The pattern being established: **cloud API for experimentation → NIM managed API for production → DGX Station for on-premises sovereignty**. Nemotron 3 Ultra is designed to run across all three without model substitution.

---

## What to Do This Week

**If you are evaluating whether to switch model providers:**

1. On June 4, sign up for NVIDIA Developer Program and hit Nemotron 3 Ultra on build.nvidia.com
2. Run your actual agent benchmarks — the tasks your pipeline does, not synthetic leaderboard tasks
3. Compare results and latency against your current model on the same tasks
4. Check the license terms on the Hugging Face model card before assuming open commercial use

**If you are building a new agent pipeline and haven't committed to a provider:**

Hold your decision until you have tested Nemotron 3 Ultra on your specific task type. If your workflow involves long-horizon task completion, the agent-optimized training may be measurable. If it's primarily summarization or Q&A, the advantage over existing providers is likely marginal.

**If fine-tuning on proprietary data is part of your roadmap:**

Nemotron 3 Ultra's open weights make it the first frontier-scale model where this is technically possible. The infrastructure cost is real — fine-tuning a 550B MoE model requires multi-GPU setups — but for teams where model ownership matters more than convenience, June 4 is the first realistic option at this quality tier.

---

## The Competitive Context

Nemotron 3 Ultra enters a landscape where **Meta LLaMA 4 Maverick** (400B/17B active MoE) and **Mistral Large 3** hold the top open-model positions. NVIDIA's Intelligence Index 48 claim puts Ultra above both on their internal ranking, though independent third-party evals will matter more than NVIDIA's own numbers.

The structural difference from Meta's LLaMA line is the training objective: LLaMA 4 Maverick optimizes for broad capability; Nemotron 3 Ultra is specifically trained for agent reasoning and tool use. Whether that specialization produces measurable production gains depends heavily on your use case.

Compared to closed frontier models: GPT-5.5 Instant and Claude Sonnet 4.6 remain strong choices for teams that want managed infrastructure, broad tool ecosystems, and established developer tooling. Nemotron 3 Ultra is competitive on raw capability; the open-weights value comes from fine-tuning control and data privacy, not from raw benchmark scores.

---

## Key Dates

- **June 4** — Nemotron 3 Ultra available on Hugging Face, ModelScope, OpenRouter, build.nvidia.com
- **August 2026** (approx.) — HP DGX Station for Windows ships; on-premises Ultra deployment becomes accessible at deskside scale
- **Fall 2026** — RTX Spark laptops ship; Nemotron 3 Nano/Super run locally on 128GB unified memory
- **Q4 2026** — Broader DGX Station availability from Asus, Dell, Supermicro, MSI, Gigabyte

We will update this article when June 4 pricing for OpenRouter and NIM is confirmed.

