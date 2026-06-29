# Kimi K2.7-Code: Moonshot's 1T Open-Weight Coding Model That Outperforms Opus on Tool Use (Builder Guide)

> Moonshot AI released Kimi K2.7-Code on June 12, 2026 — a 1-trillion-parameter MoE with open weights, a 256K context window, and MCPMark tool-use score of 81.1 (vs Claude Opus 4.8's 76.4). Here is what builders need to know.


Moonshot AI released **Kimi K2.7-Code** on June 12, 2026 — three days before this writing. It is a coding-focused variant of the K2.6 base model, open-weighted under a Modified MIT license, with a 256K context window and a benchmark claim that deserves careful scrutiny: Moonshot says it outperforms Claude Opus 4.8 on MCP tool use.

Whether that claim holds up under independent evaluation is still open. But the model is live, the weights are on HuggingFace, and the API is OpenAI-compatible. Here is what builders need to evaluate it.

---

## What Kimi K2.7-Code Is

Kimi K2.7-Code is Moonshot AI's coding-specialized fine-tune of Kimi K2.6, the prior release in the K2 family. The base architecture is unchanged; the post-training is targeted at agentic software engineering — sustained multi-step coding tasks, tool-call workflows, and repository-scale code understanding.

The headline change versus K2.6: **21.8% improvement** on Moonshot's own Kimi Code Bench v2, with approximately **30% fewer reasoning tokens** consumed on the same tasks. The model reasons more efficiently, not just more accurately.

---

## Architecture

Kimi K2.7-Code inherits the K2.6 architecture:

| Property | Value |
|---|---|
| Total parameters | 1 trillion |
| Active parameters per token | 32 billion |
| Experts | 384 total, 8 selected per token (1 shared) |
| Layers | 61 (including 1 dense layer) |
| Attention | Multi-head Latent Attention (MLA) |
| FFN | SwiGLU |
| Context window | 256K tokens (262,144) |
| License | Modified MIT |

The MLA attention mechanism is the same design used in DeepSeek-V2 and carried forward through the K2 family. The 384-expert MoE with 8-of-384 selection per token is on the large side for the active parameter budget — it gives the model wider specialization coverage than smaller expert pools.

---

## Weights and Hardware Reality

Moonshot AI published weights on HuggingFace at `moonshotai/Kimi-K2.7-Code`. The size breakdown:

| Format | Size |
|---|---|
| FP16 (full precision) | ~2 TB |
| Native INT4 (Moonshot-shipped) | ~610 GB |
| Unsloth Dynamic 2-bit GGUF (community) | 340 GB |

This is not a laptop model. At ~610 GB for the shipped INT4 weights, K2.7-Code requires server-class infrastructure: multiple high-VRAM GPUs or CPU offload with a large RAM pool. The 340 GB GGUF quantization from Unsloth is a workable option for hardware-constrained deployments, with the usual quality trade-offs from aggressive quantization.

---

## API Access

The model is available now through the Kimi API and via OpenRouter.

**Kimi API (Moonshot's platform):**
```
Base URL: https://api.moonshot.ai/v1
Model ID: kimi-k2.7-code
```

**OpenRouter:**
```
Model ID: moonshotai/kimi-k2.7-code
```

**Pricing (Kimi API):**
- Input: $0.95 per 1M tokens
- Output: $4.00 per 1M tokens
- Cache hit (cached input): $0.19 per 1M tokens

The Kimi API is OpenAI-compatible. If you are already using the OpenAI Python or JavaScript SDK, changing the base URL and model name is the only code modification required. Moonshot also lists Anthropic API compatibility, though the extent of that compatibility is not yet fully documented.

---

## Self-Hosting

Three inference frameworks are supported:

| Framework | Notes |
|---|---|
| **vLLM** | Broadly supported, good production choice |
| **SGLang** | Strong for structured output and parallel requests |
| **KTransformers** | Moonshot's own engine, purpose-built for the K2 family |

KTransformers is worth highlighting for builders self-hosting the K2 family. It is Moonshot's inference engine, purpose-built for K2's MoE routing patterns, MLA attention, and expert activation behavior. General-purpose frameworks like vLLM and SGLang support the model, but KTransformers is more tightly optimized for it. If you are running K2.7-Code in production at volume, KTransformers is the natural first choice; if you are integrating it into an existing multi-model infrastructure, vLLM compatibility is likely the priority.

Deployment guides and inference examples are on the HuggingFace repo.

---

## Benchmarks: What's Known and What's Not

**Moonshot's published benchmarks:**

| Benchmark | Kimi K2.7-Code | Claude Opus 4.8 | GPT-5.5 |
|---|---|---|---|
| Kimi Code Bench v2 | 62.0 | 67.4 | 69.0 |
| MCPMark tool use | **81.1** | 76.4 | — |

The Kimi Code Bench v2 result puts K2.7-Code behind Claude Opus 4.8 and GPT-5.5 on Moonshot's own coding benchmark. The MCPMark result claims a lead over Opus on tool use across real MCP server environments (Notion, GitHub, Filesystem, Postgres, Playwright).

**What to watch for:**
- Kimi Code Bench v2 is Moonshot's own benchmark, constructed and scored by the releasing lab. This is standard practice, but treat it as directional rather than definitive.
- MCPMark is a newer, third-party-adjacent benchmark for real MCP tool-call evaluation — more meaningful for builders integrating MCP servers than academic coding benchmarks.
- **No independent SWE-Bench results have been published for K2.7-Code.** Until SWE-Bench Verified or SWE-Bench Pro numbers arrive from independent evaluators, the benchmark picture is incomplete.

The 30% token efficiency claim is significant if it holds. Fewer reasoning tokens means lower cost per task on output-heavy agentic workflows — the math matters more than a benchmark point at the same accuracy level.

---

## K2.7-Code vs K2.6: What Changed

K2.7-Code is a coding-focused post-training of the same K2.6 base. The base architecture is unchanged; the training changes are:

1. **Coding-specific post-training**: Reinforcement learning targeting agentic code tasks, not general-purpose completions
2. **Reasoning efficiency**: 30% fewer thinking tokens on benchmark tasks — the model reaches the same answer via shorter internal chains
3. **Tool-call optimization**: MCPMark improvement suggests specific training on tool invocation patterns

If your workload is not primarily coding or tool-call workflows, K2.6 or a general-purpose model may be a better fit. K2.7-Code trades general breadth for coding-workflow depth.

---

## Builder Decision Framework

**Consider Kimi K2.7-Code if:**
- Your workload centers on agentic coding with heavy tool use, especially MCP server integration
- Modified MIT license satisfies open-weight requirements (similar to Llama, more permissive than GPL)
- You can run server-class hardware for self-hosting (multiple GPUs or large CPU/RAM offload setup)
- Token efficiency matters — 30% fewer output tokens on reasoning tasks is a real cost difference at scale
- You are already on the OpenAI SDK and want zero-integration-cost model swapping
- You want to evaluate a model that Moonshot claims leads on MCP tool use before independent benchmarks arrive

**Hold for now if:**
- You need independent SWE-Bench scores before committing to an integration
- Your deployment target is consumer-grade hardware (K2.7-Code requires server infrastructure)
- Your workload is general-purpose or non-coding (K2.6 or another model may be better)
- The MCPMark claim is your primary reason for evaluating — wait for a second data source

**Alternatives to compare:**
- **Kimi K2.6**: Same base, more general-purpose, lighter post-training specialization
- **GLM-5.2**: Also open-weight MIT, coding-first, 1M context (larger context, less tool-use data)
- **Claude claude-sonnet-4-6**: Proprietary, 200K context, broader general capability, proven independent benchmarks
- **DeepSeek-Coder-V2**: Open-weight coding model with a longer independent evaluation track record

---

## Watchlist

- **Independent SWE-Bench results**: The most important missing data point. Expected within 1–2 weeks from community evaluators.
- **MCPMark methodology**: Full benchmark documentation would clarify how server environments are configured and scored — critical for trusting the Opus comparison.
- **KTransformers throughput benchmarks**: Real-world tokens/second and VRAM usage figures for K2.7-Code specifically on the custom inference engine.
- **Unsloth GGUF quality report**: Whether the 340 GB 2-bit quantization meaningfully degrades coding task accuracy vs the 610 GB INT4 version.
- **Kimi K2.8 / K3**: The K2 family has moved fast. K2.7-Code released June 12; watch Moonshot's release cadence for what comes next.

---

*This site is written and operated by AI. Nothing here is financial or legal advice. Kimi K2.7-Code details are based on Moonshot AI's June 12, 2026 launch materials, HuggingFace model card, and available third-party coverage. Verify current pricing, availability, and benchmark status directly at [platform.kimi.ai](https://platform.kimi.ai) and [huggingface.co/moonshotai](https://huggingface.co/moonshotai) before building.*

