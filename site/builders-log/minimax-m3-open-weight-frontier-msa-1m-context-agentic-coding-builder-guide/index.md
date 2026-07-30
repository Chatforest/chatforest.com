# MiniMax M3: The First Open-Weight Frontier Coding Model with 1M Context — Builder Guide

> MiniMax M3 is the first open-weight model to combine frontier-level coding, a 1M-token context window, and native multimodality in one checkpoint. Here is everything builders need to know about its MSA architecture, benchmarks, pricing, and agentic use cases.


On June 1, 2026, MiniMax released **M3** — and made a claim that deserves scrutiny: this is the first open-weight model to simultaneously offer frontier-level coding performance, a 1-million-token context window, and native multimodal input in a single checkpoint. The [model card on Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3) is the primary source for architecture and benchmark details.

After reviewing published benchmarks and provider documentation, the narrow claim holds up: no other open-weight release combines all three traits in one checkpoint. That is a different claim than "best open-weight coding model" — on aggregate coding leaderboards, other open-weight models (GLM-5.2, DeepSeek V4 Pro, Kimi K2.6/K3) have ranked above or near M3 depending on the benchmark ([LiveBench](https://livebench.ai/), [Artificial Analysis open-weight models leaderboard](https://artificialanalysis.ai/models/open-source)). What M3 closes is narrower: the specific gap where frontier-tier coding, 1M-token context, and native multimodality had never shipped together in an open-weight release.

This guide covers what builders need to know about M3's architecture, performance numbers, pricing, open-weight availability, and when to use it versus closed alternatives. We research and analyze public announcements and documentation rather than running our own production deployments.

---

## The One-Sentence Summary

MiniMax M3 is a 428B-parameter Mixture of Experts model (23B active at inference) that scores 59.0% on SWE-Bench Pro, supports a 1M-token context window via a novel sparse attention architecture, accepts image and video input natively, and is available as open weights — all for $0.30/M input tokens via API.

---

## Why This Matters for Builders

Three traits have, until now, never coexisted in a single open-weight model:

| Trait | Why It Matters |
|---|---|
| **Frontier coding** | SWE-Bench Pro 59.0%, vs. 58.6% for GPT-5.5 and 54.2% for Gemini 3.1 Pro ([MiniMax M3 launch post](https://www.minimax.io/blog/minimax-m3)) — the GPT-5.5 gap is under 1 point and self-reported by MiniMax at launch, so treat it as a rough parity claim, not a clear win |
| **1M-token context** | Full codebase context, long audit trails, large document sets |
| **Open weights** | Self-host, fine-tune, avoid API vendor lock-in, run air-gapped |

If you need any two of these three, you had options before. All three in one model — M3 is the first.

---

## Architecture: MoE + MSA

### Mixture of Experts (MoE)

M3 is a MoE model with roughly 428 billion total parameters and roughly 23 billion active parameters per forward pass ([MiniMax-M3 model card, Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3)). The key implication:

- **Inference cost** is determined by active parameters (~23B), not total parameters (428B)
- At 23B active, M3 runs at roughly the cost of a mid-tier dense model while accessing the capacity of a much larger one
- Per-token inference compute is comparable to models in the 20–30B dense range

This active-parameter design is part of why the pricing is reasonable at $0.30/M input tokens ([MiniMax's own pricing](https://www.minimax.io/models/text/m3)) for a model posting frontier-tier coding scores — see the pricing section below for how that compares to specific closed-model rates.

### MSA: MiniMax Sparse Attention

The more technically novel piece is **MSA (MiniMax Sparse Attention)**, the architecture that makes the 1M-token context window practical ([MiniMax M3 launch post](https://www.minimax.io/blog/minimax-m3); [MiniMax-M3 model card](https://huggingface.co/MiniMaxAI/MiniMax-M3)).

Standard attention scales quadratically with sequence length — doubling the context quadruples compute. Most "long-context" models use tricks (sliding window, chunked attention, retrieval approximations) that trade quality for cost. MSA takes a different approach at the kernel level.

The key design decision, per MiniMax's own description: **KV outer gather Q**. In standard attention, queries iterate over KV pairs. In MSA, KV blocks serve as the outer loop, and all queries that hit a given KV block are processed together in a single pass. Each KV block is read once, and memory access is contiguous.

The result at 1M-token context versus MiniMax M2, per MiniMax's launch post:

| Metric | M3 vs M2 |
|---|---|
| Per-token compute | 1/20th |
| Prefill speedup | 9× |
| Decoding speedup | 15× |
| vs. Flash-Sparse-Attention (open-source) | 4× faster |

For builders, this means 1M-token context is not just a marketing number — it is operationally usable without prohibitive latency or cost penalties. Feeding a 500K-token codebase to M3 is a realistic inference call.

---

## Benchmarks in Context

M3's performance numbers below are self-reported by MiniMax in its [launch post](https://www.minimax.io/blog/minimax-m3) and [model card](https://huggingface.co/MiniMaxAI/MiniMax-M3); MiniMax had not published independently-audited eval logs for these specific runs at the time of writing. Here is how the key benchmarks read:

| Benchmark | M3 Score | What It Measures |
|---|---|---|
| **[SWE-Bench Pro](https://labs.scale.com/leaderboard/swe_bench_pro_public)** | 59.0% | Real GitHub issue resolution in diverse repos |
| **[Terminal-Bench 2.1](https://www.tbench.ai/leaderboard/terminal-bench/2.1)** | 66.0% | Agent performance on terminal tool use |
| **[SWE-fficiency](https://arxiv.org/abs/2511.06090)** | 34.8% | Optimizing an existing codebase's *runtime performance* on real workloads (matching or beating an expert's speedup while passing tests) — not issue resolution and not a cost-per-token metric |
| **[MCP-Atlas](https://arxiv.org/abs/2602.00933)** | 74.2% | Multi-step tool orchestration across real MCP servers |

### SWE-Bench Pro context

[SWE-Bench Pro](https://labs.scale.com/leaderboard/swe_bench_pro_public) tests whether a model can take a real GitHub issue, write code changes, and pass the associated test suite — without seeing the patch. Per MiniMax's [own launch numbers](https://www.minimax.io/blog/minimax-m3), M3's 59.0% edges out GPT-5.5 (58.6%) and clears Gemini 3.1 Pro (54.2%) — but the GPT-5.5 gap is under a point and both M3 figures come from MiniMax's self-reported eval, not the third-party Scale leaderboard, so treat "surpasses GPT-5.5" as approximate parity rather than a clear lead.

That said: SWE-Bench Pro is a constrained environment (specific repos, short-horizon tasks). Production agent performance on novel codebases will differ. Treat 59.0% as a ceiling relative to competitors, not an absolute prediction of your pipeline's success rate.

### MCP-Atlas: tool orchestration

The 74.2% on [MCP-Atlas](https://arxiv.org/abs/2602.00933) — a Scale AI benchmark of 1,000 tasks spanning 36 real MCP servers and 220 tools — is worth highlighting specifically for builders using MCP (Model Context Protocol) workflows. It scores multi-step, cross-server tool orchestration where the prompt doesn't name the tools to use, closer to how an agent actually has to work. That score is MiniMax's own reported number ([launch post](https://www.minimax.io/blog/minimax-m3)), not an independent leaderboard result.

---

## Multimodal: Native from Step 0

Most "multimodal" coding models attach vision via a separate adapter trained after the language model is frozen. MiniMax says M3 is multimodal from training step 0 — image and video understanding trained into the same weights as text and code, rather than bolted on afterward ([MiniMax-M3 model card](https://huggingface.co/MiniMaxAI/MiniMax-M3)).

Why this matters for agents: computer-use workflows (reading a screenshot of a UI, then writing code to interact with it) benefit significantly from tight integration between vision and code generation. M3 scores 70.0% on [OSWorld-Verified](https://os-world.github.io/), a benchmark of real desktop GUI tasks — behind closed frontier models like Claude Opus 4.8 (83.4%) but a real, independently-trackable computer-use capability rather than a marketing label.

Supported modalities, per MiniMax's model page:
- Text
- Images
- Video (including video understanding)
- Computer use (desktop GUI control)
- Toggleable thinking mode (extended chain-of-thought)

([MiniMax-M3 product page](https://www.minimax.io/models/text/m3))

---

## Open Weights: What "Open" Means Here

MiniMax committed to releasing full weights and a technical report within 10 days of the June 1 API launch ([MiniMax M3 launch post](https://www.minimax.io/blog/minimax-m3)). The [MiniMaxAI/MiniMax-M3 repository's commit history on Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3/commits/main) shows the initial weights commit landing June 12, 2026, roughly in line with that window.

For builders, this means:

1. **Self-hosting** — run M3 on your own infrastructure. At 23B active parameters, inference is feasible on high-memory GPU clusters (the full 428B weight set requires significant storage and multi-GPU coordination for the MoE routing, but active compute per token is manageable).

2. **Fine-tuning** — you can fine-tune on proprietary code, internal APIs, or domain-specific styles without sending data to a third-party API.

3. **Air-gapped deployment** — if your use case (financial, government, healthcare) requires data to never leave your environment, open weights make this possible.

4. **No vendor lock-in** — M3's output format and API shape are compatible with standard OpenAI-format API conventions, but you are not dependent on MiniMax's servers remaining available or affordable.

The weights are released under MiniMax's own "minimax-community" license, not a standard OSI license like Apache 2.0 or MIT ([MiniMax-M3 model card, Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3)). Review the license text on that page before commercial deployment — "open weights" here means downloadable and self-hostable, not necessarily unrestricted commercial use.

---

## API Access and Pricing

M3 is available immediately via API without waiting for self-hosted setup:

| Provider | Notes |
|---|---|
| **[MiniMax API](https://www.minimax.io/models/text/m3)** | Direct; Token Plan from $20/month |
| **[Together AI](https://www.together.ai/models/minimax-m3)** | Serverless inference; Together says its inference team optimized serving for the 1M-context, multimodal architecture |
| **[Fireworks AI](https://fireworks.ai/blog/minimax-m3-launch)** | Day-0 support, serverless and on-demand deployments |
| **[OpenRouter](https://openrouter.ai/minimax/minimax-m3)** | Available via OpenRouter's unified API |
| **[Vercel AI Gateway](https://vercel.com/changelog/minimax-m3-on-ai-gateway)** | Available, no markup pass-through pricing |

**Pricing**, per MiniMax's own [pricing/model page](https://www.minimax.io/models/text/m3):
- Standard tier (requests ≤512K input tokens): $0.30/M input tokens, $1.20/M output tokens
- Long-context tier (requests >512K input tokens): billed at 2x the standard rate
- Context window: up to 1M tokens, with a stated guaranteed minimum of 512K

At $0.30/M input for the standard tier, M3 is priced well below closed frontier models such as Claude Opus 4.8, which lists $5/M input and $25/M output tokens on [Anthropic's pricing page](https://claude.com/pricing). Note the M3 figure is MiniMax's own published rate, not an independently audited "cost per solved task" figure — for that kind of comparison, see the SWE-fficiency caveat above (it measures code performance optimization, not price-per-quality).

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

MiniMax's [launch post](https://www.minimax.io/blog/minimax-m3) documents M3 running autonomous tasks for extended stretches: a paper-reproduction task ran "nearly 12 hours" and produced 18 commits and 23 experimental figures; a CUDA kernel-optimization task ran roughly 24 continuous hours across 147 benchmark submissions and 1,959 tool calls; and a model fine-tuning ("PostTrainBench") task ran a full data-synthesis-to-evaluation loop over 12 hours without human intervention. For builders building long-horizon agents, a few design considerations:

**On thinking mode:** M3 has a toggleable thinking mode. For agentic loops where the model calls tools repeatedly, evaluate whether per-step thinking is worth the token cost versus a single planning pass at the top of the loop.

**On 1M context for repo agents:** A typical large monorepo at full text expansion runs 200K–600K tokens. M3's guaranteed 512K minimum (up to 1M) means you can feed entire repos for issue resolution without chunking. This removes one of the most common sources of quality degradation in CI/CD agents.

**On MCP tool orchestration:** The 74.2% [MCP-Atlas](https://arxiv.org/abs/2602.00933) score is MiniMax's self-reported result and suggests M3 reliably selects and sequences tool calls in multi-step workflows. This is not a claim unique to M3, though — other open-weight models (GLM-5.2 and Kimi K3, among others) are also scored on the [MCP-Atlas leaderboard](https://labs.scale.com/leaderboard/mcp_atlas), some above M3's number. For builders using MCP-native infrastructure, the useful takeaway is that MCP-Atlas is becoming a standard reference point across both open and closed models, so it's worth checking the live leaderboard rather than relying on any single vendor's launch-day number.

---

## What to Watch

- **Fine-tune results**: As the weights become available and the community trains domain-specific variants, expect specialized models for security auditing, ML engineering, and infrastructure code to emerge from the M3 base.
- **Self-hosting benchmarks**: Production throughput numbers on realistic GPU configurations will determine whether self-hosting is operationally viable for most teams versus relying on serverless providers.
- **License terms**: MiniMax's commercial license terms for the weights are the gating factor for enterprise adoption. Review the Hugging Face model card before committing to M3 in a commercial product.

---

*This analysis is based on MiniMax's published technical report, benchmark announcements, and provider documentation as of June 2026. ChatForest researches and analyzes public sources — we do not run our own model evaluations or production deployments.*

