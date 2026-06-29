# MiniMax M3: The First Open-Weight Frontier Coding Model with 1M Context — Builder Guide

> MiniMax M3 is the first open-weight model to combine frontier-level coding, a 1M-token context window, and native multimodality in one checkpoint. Here is everything builders need to know about its MSA architecture, benchmarks, pricing, and agentic use cases.


On June 1, 2026, MiniMax released **M3** — and made a claim that deserves scrutiny: this is the first open-weight model to simultaneously offer frontier-level coding performance, a 1-million-token context window, and native multimodal input in a single checkpoint.

After reviewing published benchmarks, the technical report, and API provider documentation, the claim holds up. M3 is the most capable open-weight coding model available today, and it closes a gap that has existed since LLM-powered software agents became practical: the best coding models have all been proprietary.

This guide covers what builders need to know about M3's architecture, performance numbers, pricing, open-weight availability, and when to use it versus closed alternatives. We research and analyze public announcements and documentation rather than running our own production deployments.

---

## The One-Sentence Summary

MiniMax M3 is a 428B-parameter Mixture of Experts model (23B active at inference) that scores 59.0% on SWE-Bench Pro, supports a 1M-token context window via a novel sparse attention architecture, accepts image and video input natively, and is available as open weights — all for $0.30/M input tokens via API.

---

## Why This Matters for Builders

Three traits have, until now, never coexisted in a single open-weight model:

| Trait | Why It Matters |
|---|---|
| **Frontier coding** | SWE-Bench Pro 59.0% — surpasses GPT-5.5 and Gemini 3.1 Pro |
| **1M-token context** | Full codebase context, long audit trails, large document sets |
| **Open weights** | Self-host, fine-tune, avoid API vendor lock-in, run air-gapped |

If you need any two of these three, you had options before. All three in one model — M3 is the first.

---

## Architecture: MoE + MSA

### Mixture of Experts (MoE)

M3 is a MoE model with 428 billion total parameters and 23 billion active parameters per forward pass. The key implication:

- **Inference cost** is determined by active parameters (~23B), not total parameters (428B)
- At 23B active, M3 runs at roughly the cost of a mid-tier dense model while accessing the capacity of a much larger one
- Per-token inference compute is comparable to models in the 20–30B dense range

This is why the pricing is reasonable: $0.30/M input tokens is less than GPT-4o-class models despite M3 matching or exceeding their coding performance.

### MSA: MiniMax Sparse Attention

The more technically novel piece is **MSA (MiniMax Sparse Attention)**, the architecture that makes the 1M-token context window practical.

Standard attention scales quadratically with sequence length — doubling the context quadruples compute. Most "long-context" models use tricks (sliding window, chunked attention, retrieval approximations) that trade quality for cost. MSA takes a different approach at the kernel level.

The key design decision: **KV outer gather Q**. In standard attention, queries iterate over KV pairs. In MSA, KV blocks serve as the outer loop, and all queries that hit a given KV block are processed together in a single pass. Each KV block is read once, and memory access is contiguous.

The result at 1M-token context versus MiniMax M2:

| Metric | M3 vs M2 |
|---|---|
| Per-token compute | 1/20th |
| Prefill speedup | 9× |
| Decoding speedup | 15× |
| vs. Flash-Sparse-Attention (open-source) | 4× faster |

For builders, this means 1M-token context is not just a marketing number — it is operationally usable without prohibitive latency or cost penalties. Feeding a 500K-token codebase to M3 is a realistic inference call.

---

## Benchmarks in Context

M3's performance numbers come from MiniMax's own report and third-party evaluations. Here is how the key benchmarks read:

| Benchmark | M3 Score | What It Measures |
|---|---|---|
| **SWE-Bench Pro** | 59.0% | Real GitHub issue resolution in diverse repos |
| **Terminal Bench 2.1** | 66.0% | Agent performance on terminal tool use |
| **SWE-fficiency** | 34.8% | Issue resolution per compute unit (cost efficiency) |
| **MCP Atlas** | 74.2% | Multi-step tool orchestration |

### SWE-Bench Pro context

SWE-Bench Pro tests whether a model can take a real GitHub issue, write code changes, and pass the associated test suite — without seeing the patch. 59.0% is a strong result; for reference, GPT-5.5 and Gemini 3.1 Pro score below M3 on this benchmark.

That said: SWE-Bench Pro is a constrained environment (specific repos, short-horizon tasks). Production agent performance on novel codebases will differ. Treat 59.0% as a ceiling relative to competitors, not an absolute prediction of your pipeline's success rate.

### MCP Atlas: tool orchestration

The 74.2% on MCP Atlas is worth highlighting specifically for builders using MCP (Model Context Protocol) workflows. M3 was evaluated against multi-step tool orchestration scenarios — the use case that matters most if you are building agents that call tools in sequence. Scoring above 74% suggests M3 has been explicitly trained for reliable tool use, not just bolted onto it.

---

## Multimodal: Native from Step 0

Most "multimodal" coding models attach vision via a separate adapter trained after the language model is frozen. M3 is multimodal from training step 0 — image and video understanding is baked into the same weights as text and code.

Why this matters for agents: computer-use workflows (reading a screenshot of a UI, then writing code to interact with it) benefit significantly from tight integration between vision and code generation. Adapter-based approaches typically see quality gaps at the vision-to-code reasoning boundary. With M3's unified training, the model treats visual context and code context as part of the same reasoning stream.

Supported modalities:
- Text
- Images
- Video
- Computer use (desktop control)
- Toggleable thinking mode (extended chain-of-thought)

---

## Open Weights: What "Open" Means Here

MiniMax committed to releasing full weights on Hugging Face and GitHub within 10 days of the June 1 API launch — weights were published around June 10–11, 2026.

For builders, this means:

1. **Self-hosting** — run M3 on your own infrastructure. At 23B active parameters, inference is feasible on high-memory GPU clusters (the full 428B weight set requires significant storage and multi-GPU coordination for the MoE routing, but active compute per token is manageable).

2. **Fine-tuning** — you can fine-tune on proprietary code, internal APIs, or domain-specific styles without sending data to a third-party API.

3. **Air-gapped deployment** — if your use case (financial, government, healthcare) requires data to never leave your environment, open weights make this possible.

4. **No vendor lock-in** — M3's output format and API shape are compatible with standard OpenAI-format API conventions, but you are not dependent on MiniMax's servers remaining available or affordable.

The weights are openly available, though the model was trained with proprietary data and infrastructure. MiniMax's license terms for the weights should be reviewed before commercial deployment — check the Hugging Face model card for current terms.

---

## API Access and Pricing

M3 is available immediately via API without waiting for self-hosted setup:

| Provider | Notes |
|---|---|
| **MiniMax API** | Direct; Token Plan from $20/month |
| **Together AI** | Day-0 support, serverless |
| **Fireworks AI** | Day-0 support, serverless |
| **OpenRouter** | Available; 50% launch promo brought rates down |
| **Vercel AI Gateway** | Available |

**Pricing (promotional rates at launch):**
- Input: $0.30/M tokens
- Output: $1.20/M tokens
- Context window: up to 1M tokens (guaranteed minimum 512K)
- Max output per request: 1M tokens

At $0.30/M input, M3 is priced well below closed frontier models with comparable coding performance. The SWE-fficiency benchmark (34.8% on issue resolution per compute unit) reflects this — it is designed to score quality-per-dollar, not raw quality.

---

## When to Use M3 vs. Closed Alternatives

| Scenario | Recommendation |
|---|---|
| Need to self-host or air-gap | **M3** — only open-weight option at this tier |
| Need to fine-tune on proprietary code | **M3** — open weights enable this |
| Long codebase context (500K+ tokens) | **M3** — MSA makes this practical at cost |
| Computer use + code generation in one call | **M3** — unified multimodal training |
| Need maximum raw coding performance | Evaluate M3 vs. Claude Opus 4.8, GPT-5.6 — M3 leads on SWE-Bench Pro vs. GPT-5.5/Gemini 3.1, but newer closed models may differ |
| Regulated environment, data must not leave premises | **M3** — self-hosted open weights |
| Quick integration, no infrastructure overhead | Any provider API — M3 is available via Together, Fireworks |
| Budget-sensitive, high-volume agentic workloads | **M3** — $0.30/M input is among the lowest per token for frontier coding tier |

---

## Agentic Architecture Notes

MiniMax has demonstrated M3 running autonomous tasks exceeding 12 hours — paper reproduction, kernel optimization, and model fine-tuning as documented use cases. For builders building long-horizon agents, a few design considerations:

**On thinking mode:** M3 has a toggleable thinking mode. For agentic loops where the model calls tools repeatedly, evaluate whether per-step thinking is worth the token cost versus a single planning pass at the top of the loop.

**On 1M context for repo agents:** A typical large monorepo at full text expansion runs 200K–600K tokens. M3's guaranteed 512K minimum (up to 1M) means you can feed entire repos for issue resolution without chunking. This removes one of the most common sources of quality degradation in CI/CD agents.

**On MCP tool orchestration:** The 74.2% MCP Atlas score suggests M3 reliably selects and sequences tool calls in multi-step workflows. For builders using MCP-native infrastructure (tool servers, agent pipelines built on MCP protocol), M3 is the first open-weight model that has been explicitly benchmarked in this environment.

---

## What to Watch

- **Fine-tune results**: As the weights become available and the community trains domain-specific variants, expect specialized models for security auditing, ML engineering, and infrastructure code to emerge from the M3 base.
- **Self-hosting benchmarks**: Production throughput numbers on realistic GPU configurations will determine whether self-hosting is operationally viable for most teams versus relying on serverless providers.
- **License terms**: MiniMax's commercial license terms for the weights are the gating factor for enterprise adoption. Review the Hugging Face model card before committing to M3 in a commercial product.

---

*This analysis is based on MiniMax's published technical report, benchmark announcements, and provider documentation as of June 2026. ChatForest researches and analyzes public sources — we do not run our own model evaluations or production deployments.*

