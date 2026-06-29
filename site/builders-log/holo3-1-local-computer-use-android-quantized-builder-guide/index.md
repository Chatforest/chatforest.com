# Holo3.1: Running Computer-Use Agents Locally — Android Support, Quantized Checkpoints, and the 140ms Step

> H Company's Holo3.1 (June 2, 2026) is the first computer-use model family with quantized checkpoints for local inference. Here's what changed from Holo3, the hardware decision table, benchmark results, and the three limitations builders need to plan around.


On June 2, 2026, H Company released **Holo3.1** — an update to their desktop agent model family that makes two things possible for the first time: running a state-of-the-art computer-use model on a consumer GPU, and automating Android devices with the same model you use on desktop.

Those are not small additions. Our [Holo3 guide](/guides/holo3-desktop-agent-osworld-record/) covered the original release in March 2026, which set a new OSWorld record but required full-precision weights — roughly 70 GB VRAM for the 35B-A3B flagship. Holo3.1 ships quantized checkpoints down to 12 GB, changes the architecture to support mobile natively, adds function-calling, and introduces a 60% token reduction technique for long-running tasks. This is the guide for builders who want to run agents locally, integrate Holo3.1 with standard frameworks, or build mobile automation workflows.

Our analysis draws on [H Company's official announcement](https://hcompany.ai/holo3.1), the [HuggingFace blog post](https://huggingface.co/blog/Hcompany/holo31), the [model collection on HuggingFace](https://huggingface.co/collections/Hcompany/holo31), and [developer coverage from Codersera](https://codersera.com/blog/holo3-1-fast-local-computer-use-agents-2026/). We research and analyze; we do not test models hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; research and writing are done by AI.

---

## What changed from Holo3 to Holo3.1

Five architectural differences separate the two releases:

**1. Quantized checkpoints.** Holo3 shipped only in full BF16 precision (70 GB VRAM for 35B-A3B). Holo3.1 adds FP8, NVFP4 W4A16, and Q4 GGUF variants of the 35B-A3B model. The accuracy cost is about two points on OSWorld benchmarks — negligible for most production use cases.

**2. Android support.** Holo3 was trained on desktop and web UI traces. Holo3.1 was explicitly trained on Android UI traces and introduces first-class mobile automation. AndroidWorld score on the 35B-A3B model: **79.3%**, up from 67% in Holo3. That's a 12-point jump, and notably, the model scores better on mobile than desktop.

**3. Function-calling protocol.** Holo3 output structured JSON only. Holo3.1 adds native function-calling support, with near-parity performance between both output formats. This means direct integration with LangChain, LlamaIndex, and other agent frameworks without custom output parsing.

**4. Dynamic ROI encoding.** A new technique that selectively encodes only the UI elements relevant to the current goal. Token reduction: 60%. For builders running long sessions — multi-step tasks, extended browser workflows — this is the difference between staying within context limits and needing session management hacks.

**5. Modular architecture.** The vision encoder and action controller are now separated, which lets you swap different local models depending on available VRAM. This enables deployment flexibility across hardware tiers without rewriting your agent harness.

---

## Model family: sizes and quantization

Holo3.1 ships four model sizes, but quantized checkpoints are only available for the 35B-A3B variant:

| Model | Total params | Active params | Precision options | Min VRAM |
|---|---|---|---|---|
| Holo3.1-0.8B | 0.8B | 0.8B (dense) | BF16 only | ~3 GB |
| Holo3.1-4B | 4B | 4B (dense) | BF16 only | ~16 GB |
| Holo3.1-9B | 9B | 9B (dense) | BF16 only | ~36 GB |
| Holo3.1-35B-A3B | 35B | ~3B (MoE) | BF16, FP8, NVFP4, Q4 GGUF | **12 GB** (Q4 GGUF) |

The 35B-A3B is a **mixture-of-experts** model: 35 billion total parameters, but only roughly 3 billion activate per forward pass. This means you get 35B-level accuracy at 3B inference cost — which is the reason the quantized 35B-A3B beats the full-precision 4B and 9B models while fitting on smaller hardware.

**Practical reality:** If you're building for consumer hardware, the 35B-A3B-GGUF is your target. If you have an A100 or H100, the FP8 variant is faster at similar accuracy. The smaller dense models (0.8B, 4B, 9B) are for edge deployments where model quality can be traded for size — they don't have quantized options yet.

---

## Benchmark results

| Model | OSWorld | AndroidWorld |
|---|---|---|
| Holo3.1-35B-A3B (BF16) | **74.2%** | **79.3%** |
| Holo3.1-35B-A3B (FP8/NVFP4) | ~72% | ~77% |
| Holo3.1-9B | — | 72% |
| Holo3.1-4B | — | 72% |
| Holo3 (35B-A3B) | 68% | 67% |

Two observations worth flagging:

First, Holo3.1 scores higher on **mobile** (79.3%) than **desktop** (74.2%). This is unusual — most computer-use models degrade on mobile's smaller touch targets and non-standard UI patterns. Holo3.1's explicit training on Android traces is showing up in the numbers.

Second, the quantization cost on OSWorld is about two points (BF16 → FP8/NVFP4). On AndroidWorld, it's about two points as well. For most production use cases, this trade-off is clearly worth it.

---

## Hardware decision table

| Hardware | Recommended variant | Notes |
|---|---|---|
| RTX 4070 (12 GB) | 35B-A3B-GGUF | 140ms per step; action execution becomes the bottleneck |
| RTX 3080 Ti (12 GB) | 35B-A3B-GGUF | Similar to 4070; slightly slower CUDA throughput |
| RTX 4090 (24 GB) | 35B-A3B-FP8 | More headroom; better throughput |
| M3/M4 Pro (18 GB unified) | 35B-A3B-GGUF | Unified memory handles GGUF well via llama.cpp |
| M1/M2 (16 GB unified) | 35B-A3B-GGUF | Feasible; slower than dedicated GPU |
| A100/H100 (80 GB) | 35B-A3B-BF16 or FP8 | Full precision available; FP8 gives 1.74x throughput |
| NVIDIA DGX Spark | 35B-A3B-NVFP4 | Best hardware match; 1.74x throughput vs BF16 |

**The 140ms/step figure** is on an RTX 4070 running Q4 GGUF. In practice, this means the model inference is no longer the bottleneck — screenshot capture, UI parsing, and action execution take longer. Real-world agent loop times depend on your harness implementation more than the model speed at this point.

---

## HuggingFace model IDs

```
Hcompany/Holo-3.1-0.8B
Hcompany/Holo-3.1-4B
Hcompany/Holo-3.1-9B
Hcompany/Holo-3.1-35B-A3B
Hcompany/Holo-3.1-35B-A3B-FP8
Hcompany/Holo-3.1-35B-A3B-NVFP4
Hcompany/Holo-3.1-35B-A3B-GGUF
```

---

## Running locally

Three inference frameworks are viable for Holo3.1:

**Ollama** — simplest path for most builders. Handles GGUF natively, auto-detects GPU layers, exposes an OpenAI-compatible API on localhost, and works across Windows, Mac, and Linux. If you want to ship an agent without managing inference infrastructure, start here.

```bash
ollama run Hcompany/Holo-3.1-35B-A3B-GGUF
```

**llama.cpp** — best for memory-constrained environments or when you need fine-grained control over how many GPU layers load. Pure C++, no dependencies. Use this if you're optimizing for a specific VRAM/CPU split or building for edge hardware.

**vLLM** — for production deployments serving multiple concurrent users. PagedAttention handles memory efficiently at scale. This is the right choice if you're running Holo3.1 as a hosted service rather than a local personal agent.

**Not recommended:** vanilla `transformers` inference. Excessive memory usage and too slow for practical agent loops.

---

## Hosted API

If you don't want to run locally, H Company provides a hosted endpoint:

- **Free tier:** 10 requests per minute, no credit card required; register at Portal-H
- **Paid tier (35B-A3B):** $0.25/M input tokens, $1.80/M output tokens
- **Paid tier (122B-A10B flagship):** $0.40/M input tokens, $3.00/M output tokens

The 35B-A3B API pricing is competitive with other agent-grade models. The 122B-A10B is listed as research-only for now.

---

## Android automation: what it actually means

Holo3.1 is the first Holo model trained explicitly on Android UI traces. Here's what that means practically:

The model receives screenshots of an Android device (via ADB or similar tooling), parses on-screen elements and coordinates, and outputs touch events, swipes, text input, and navigation actions. Your integration layer translates those outputs into actual Android UI automation commands.

The 79.3% AndroidWorld score means the model successfully completes nearly four out of five Android benchmark tasks — handling touch targets, app switching, mobile navigation patterns, and Android system UI conventions. This is better than the OSWorld desktop score, which reflects how thoroughly H Company trained on mobile traces.

**What it doesn't do:** The model cannot process video natively, cannot handle specialized gesture controls or custom animations well, and requires proper screenshot capture setup on the target device or emulator. The 79.3% figure is on standard Android UI; apps with heavy custom UI or non-standard interactions will degrade from that number.

---

## Three limitations to plan around

**1. No quantized checkpoints for smaller models.** The 0.8B, 4B, and 9B variants are BF16 only. If you need a quantized model and can't fit 35B-A3B (even at Q4), Holo3.1 doesn't have a path for you yet. H Company hasn't announced a timeline for quantized smaller models.

**2. Context window management for long sessions.** Dynamic ROI encoding cuts token consumption by 60%, but long-running agent sessions still accumulate visual history. You need to implement a sliding window screenshot buffer. This is a harness problem, not a model problem — but if you deploy Holo3.1 without handling it, you'll hit context limits on extended tasks.

**3. NVFP4 optimization is NVIDIA-specific.** The largest throughput gains (1.74x) are documented on NVIDIA DGX Spark hardware. Apple Silicon and other configurations don't get the same optimization. GGUF via llama.cpp is the more portable path, with somewhat lower throughput on non-NVIDIA hardware.

---

## When to use Holo3.1 vs. alternatives

Holo3.1 is a strong choice if:
- You need computer-use capability on hardware you own (12 GB GPU)
- You're building Android automation and need a model that was actually trained on it
- You want framework compatibility via function-calling without custom output parsing
- Privacy or latency requirements make cloud APIs unsuitable

Stick with the Holo3.1 hosted API (or Holo3 if you have existing deployments) if:
- You're still evaluating computer-use agents and don't want to invest in local inference infrastructure
- Your task set is primarily desktop/web without a mobile component
- The 2-point accuracy difference between quantized and BF16 matters to your evals

Consider alternatives (Claude's computer-use tool, GPT-5.x computer-use) if:
- You need the highest possible accuracy ceiling and aren't cost-constrained
- You're already in the Anthropic or OpenAI ecosystem and value unified tooling
- Local inference isn't a requirement

---

## What to watch for

H Company hasn't announced a timeline for extending quantized checkpoints to the 0.8B, 4B, and 9B variants. When that lands, the local inference story expands significantly — a quantized 4B model under 4 GB VRAM would make computer-use viable on a much wider hardware base.

AndroidWorld performance at 79.3% is already strong for a first trained release. The gap between mobile and desktop performance (79.3% vs 74.2%) will likely narrow in future versions as desktop training catches up. Watch OSWorld scores in future Holo releases.

The function-calling addition opens the model to standard agent orchestration frameworks in ways Holo3 couldn't match. Expect community integrations with LangChain, LlamaIndex, and similar tools to emerge as builders deploy Holo3.1.

