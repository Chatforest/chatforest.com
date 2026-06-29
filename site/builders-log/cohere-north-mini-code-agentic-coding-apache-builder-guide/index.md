# Cohere North Mini Code: A 30B Open-Weight Coding Agent That Runs on a Single H100

> Cohere released North Mini Code on June 11 — a 30B parameter (3B active) MoE model purpose-built for agentic coding, open-source under Apache 2.0. 80.2% on SWE-Bench Verified at pass@10, 61% SWE-Bench Pro pass@1, single H100 in FP8, 256K context. Here's what builders need to know.


On June 11, 2026, Cohere released **North Mini Code 1.0** — a 30-billion-parameter, open-weight coding model built specifically for agentic workflows. The model is available on HuggingFace under an Apache 2.0 license, runs on a single H100 GPU in FP8 precision, and posts **80.2% on SWE-Bench Verified** (pass@10) and **61.0% on SWE-Bench Pro** (pass@1) — numbers that rival closed frontier models while remaining fully self-hostable.

For builders who want a production-capable agentic coding model without vendor lock-in, this is the most practical open-weight option to land in 2026.

---

## What North Mini Code Actually Is

The name is a bit misleading. "Mini" refers to active parameter count, not capability. North Mini Code has:

- **30 billion total parameters** across 128 experts in its Mixture-of-Experts architecture
- **3 billion active parameters per token** — only 8 of 128 experts fire per forward pass
- **256,000 token context window** with 64,000 max generation length
- **Hybrid attention** alternating sliding-window attention with RoPE (3:1 ratio) and global attention without positional embeddings

The MoE design is the reason this model fits on a single H100 in FP8: at inference time, you're running 3B active params, not 30B. The rest sit dormant, loading only the relevant expert weights per token. For coding workloads — which tend to repeat similar structural patterns across files — the routing is remarkably efficient.

This is distinct from Cohere's broader enterprise North platform (which focuses on on-premises deployment for regulated industries). North Mini Code is the open-weight developer model; the enterprise platform is the managed deployment layer around it.

---

## Architecture and Training

Cohere's technical blog is unusually transparent about the training methodology, which is worth understanding before deploying.

**Two-stage cascaded supervised fine-tuning:**

The model is trained in two stages to handle long-context coding without the model ignoring rare but high-value code tokens:

1. **Stage 1:** 64K context, broader data mix — 70% code tokens, 43% agentic tool-use data, 27% competitive/scientific programming
2. **Stage 2:** 128K context, only high-quality verified samples — 4.5 billion tokens drawn from agentic and reasoning data, with code forming 61% of trainable tokens

The two-stage approach solves a common problem: if you train on 20 billion non-code tokens alongside 1.5 billion code tokens at maximum context, the model learns to deprioritize code. Stage 2 corrects this by training only on verified high-signal data.

**Reinforcement Learning with Verifiable Rewards (RLVR):**

The model is fine-tuned on 70,000+ verifiable coding tasks across approximately 5,000 repositories. "Verifiable" means the reward signal is objective: does the code compile? Do the tests pass? Do the outputs match? This avoids the noise inherent in human preference signals, which tend to reward confident-sounding wrong answers.

The model card notes that SWE-Bench repositories were deduplicated out of the training set to prevent benchmark leakage.

**Multi-harness SFT:** North Mini Code is trained against multiple agent harnesses (OpenCode, SWE-Agent, mini-SWE-Agent). Cohere reports a 10-percentage-point gain on OpenCode evaluations from multi-harness exposure alone. This matters for deployment: the model adapts better to different scaffolding patterns than models trained against a single agent framework.

---

## Benchmarks

| Benchmark | North Mini Code | Claude Opus 4.7 | GPT-5.4 | Qwen2.5-Coder 32B |
|-----------|----------------|-----------------|---------|-------------------|
| SWE-Bench Verified (pass@10) | **80.2%** | ~80.8% | ~78% | ~72% |
| SWE-Bench Pro (pass@1) | **61.0%** | ~57% | ~58% | ~50% |
| Coding Index (Artificial Analysis) | 33.4 | — | — | — |
| Output throughput | 203.8 tok/s | API-only | API-only | Varies |

The SWE-Bench Pro pass@1 number is notable. Pass@1 means the model gets one attempt with no sampling — the condition closest to real production use. 61% on SWE-Bench Pro at pass@1 is competitive with models that cost significantly more to run and can't be self-hosted.

The throughput number (203.8 tokens/second measured via Cohere API) is approximately 2.8x higher than Mistral Devstral Small 2 under identical hardware, according to Cohere's internal benchmarks.

---

## Deployment Options

### Self-hosted via vLLM (recommended)

```bash
pip install vllm

# BF16 — requires 2x A100 40GB or equivalent (~60GB VRAM total)
vllm serve CohereLabs/North-Mini-Code-1.0 \
  --tensor-parallel-size 2 \
  --max-model-len 320000

# FP8 — single H100 80GB (~30GB VRAM)
vllm serve CohereLabs/North-Mini-Code-1.0-fp8 \
  --max-model-len 320000
```

The model exposes an OpenAI-compatible endpoint once running. Any code that calls `openai.ChatCompletion.create()` or uses the `openai` Python library can be redirected with two environment variable changes:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="CohereLabs/North-Mini-Code-1.0",
    messages=[{"role": "user", "content": "Fix the failing test in this repo..."}],
    max_tokens=8192
)
```

### Self-hosted via SGLang

SGLang is an alternative worth considering for agent-heavy workloads. Its RadixAttention mechanism is efficient when many inference calls share common prefixes — common in coding agents that repeatedly send the same system prompt plus evolving context.

```bash
pip install sglang[all]

python -m sglang.launch_server \
  --model-path CohereLabs/North-Mini-Code-1.0-fp8 \
  --tp 1 \
  --context-length 262144
```

**Important:** llama.cpp and Ollama do not yet support the custom 128-expert MoE architecture in North Mini Code. If you need CPU inference or consumer GPU deployment, this model is not a viable option today.

### Cohere API (free tier)

If you're evaluating before committing to GPU infrastructure, Cohere's API exposes North Mini Code with a free tier and currently charges $0.00 per million tokens until rate limits are reached. Production limits depend on key type; check the [Cohere API documentation](https://docs.cohere.com) for current limits.

---

## The Sub-Agent Orchestration Angle

This is the specific capability Cohere is highlighting as the differentiator, and it's worth understanding what it actually means.

In a typical agentic coding system, you have a main agent and specialized sub-agents: one for writing tests, one for patching code, one for reviewing changes. The main agent needs to coordinate their outputs, pass context between them, recover when a sub-agent fails, and validate intermediate results.

North Mini Code is trained to:
- Understand and coordinate multi-agent delegations explicitly
- Map system architecture across agent boundaries (knowing that a change in component A affects component B in the sub-agent's scope)
- Pass intermediate outputs from one agent to the next in structured formats
- Recover gracefully when a sub-agent produces invalid output

The model also supports **interleaved thinking** — reasoning tokens embedded between action tokens in multi-step tasks. The documentation recommends passing model-generated thinking content to future agentic steps for consistent multi-turn performance.

Whether this training pays off at your specific task depends on your scaffolding. The multi-harness training gives the model more flexibility than a framework-specific model, but you should benchmark against your own eval before committing to production.

---

## Hardware Requirements (Honest Assessment)

| Precision | Hardware Required | VRAM | Notes |
|-----------|------------------|------|-------|
| FP8 | 1× H100 80GB | ~30 GB | Recommended for production |
| BF16 | 2× A100 40GB | ~60 GB | Better for research/debugging |
| Any | RTX 4090 (24GB) | ❌ | Not supported — VRAM insufficient |

This is an enterprise GPU story. An RTX 4090 with 24GB VRAM cannot run North Mini Code at any supported precision level. If your infrastructure is consumer GPU-based, this model is not usable today.

For organizations with H100 access — cloud or on-premise — the single-H100 FP8 deployment is practical. The model is not compute-hungry at inference time (3B active params), but the weight loading requires the VRAM headroom.

---

## Comparison: When to Use North Mini Code vs. Alternatives

| Use Case | Best Choice | Why |
|----------|-------------|-----|
| Agentic coding, self-hosted, H100 available | **North Mini Code** | Purpose-built, Apache 2.0, SWE-Bench Pro 61% |
| Pure code completion, consumer GPU | Qwen2.5-Coder (32B) | Broader hardware support, strong HumanEval |
| Maximum agentic capability, cost flexible | Claude Opus 4.7 | Higher SWE-Bench ceiling, broader reasoning |
| Sub-100ms TTFT requirement | MAI-Code-1-Flash via Copilot | Inference-optimized, 5B active params |
| Air-gapped enterprise deployment | North Mini Code + North platform | On-premise, GDPR/SOC-2, data stays local |
| No GPU budget at all | Cohere API free tier | Same model, zero infra cost until rate limits |

---

## Limitations to Know Before Deploying

**Specialist, not generalist.** North Mini Code scores 14% on GDPval-AA (general reasoning) and 37% on τ²-Bench Telecom. It is a coding specialist. If your workflow requires strong general reasoning alongside coding, you're better served by a general-purpose model.

**No consumer GPU path.** The llama.cpp gap is real. Individual developers without institutional GPU access cannot self-host this model today. Cohere has not announced a quantization path that supports consumer hardware.

**Benchmark comparison caveat.** Cohere's competitive comparisons use Qwen3.5 as the baseline, not the current Qwen3.6. The numbers may look slightly less favorable once the current generation is benchmarked head-to-head.

**Thin documentation.** The model is new (released June 11, 2026). Community examples, error patterns, and edge-case workarounds are still accumulating. Expect some onboarding friction.

---

## The Open-Weight Calculus

The strategic reason to use North Mini Code isn't purely capability — it's the Apache 2.0 license plus the open weights. That combination means:

- **No vendor termination risk.** You have the weights. Cohere can change pricing, deprecate the hosted API, or shut down. Your model stays.
- **Fine-tuning rights.** Apache 2.0 permits modification and redistribution, including commercial use. You can fine-tune on your proprietary codebase.
- **Data sovereignty.** For regulated industries (finance, healthcare, government), the ability to run inference on-premise without data leaving your network is often a hard requirement, not a preference. North Mini Code + Cohere North platform is purpose-built for this.

The S&P Global partnership announced June 8 is the most concrete signal of this positioning: S&P's verified financial data integrating directly into Cohere North for financial institutions that cannot send data to a cloud API.

---

## Builder Checklist

If you're evaluating North Mini Code:

- [ ] Confirm hardware: H100 80GB (FP8) or 2× A100 40GB (BF16) available
- [ ] Use vLLM or SGLang — llama.cpp/Ollama will not work
- [ ] Start with Cohere API free tier to validate task fit before committing GPU resources
- [ ] Run your own eval on task-representative examples — don't rely solely on SWE-Bench numbers
- [ ] If using sub-agent orchestration, pass model-generated thinking tokens between agent steps
- [ ] Review Apache 2.0 license for your specific commercial use case (it is permissive, but confirm with your legal team for regulated industries)
- [ ] Set `max-model-len 320000` in vLLM to match the full context window

---

HuggingFace repository: [CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)
FP8 variant: [CohereLabs/North-Mini-Code-1.0-fp8](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-fp8)
Official announcement: [cohere.com/blog/north-mini-code](https://cohere.com/blog/north-mini-code)

