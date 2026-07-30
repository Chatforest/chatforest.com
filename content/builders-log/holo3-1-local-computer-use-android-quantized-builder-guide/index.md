---
title: "Holo3.1: Running Computer-Use Agents Locally — Android Support, Quantized Checkpoints, and What the Benchmarks Actually Show"
date: 2026-06-15
description: "H Company's Holo3.1 (June 2026) is the first computer-use model family with quantized checkpoints for local inference. Here's what changed from Holo3, the real (verified) benchmark numbers, and the three limitations builders need to plan around."
tags: ["computer-use", "gui-agents", "local-inference", "android", "open-source", "quantization", "developer-tools"]
sources_audited: 2026-07-30
---

On June 2, 2026, H Company released **Holo3.1** — an update to their desktop agent model family. It's [H Company's first release to ship quantized checkpoints for local inference](https://hcompany.ai/holo3.1), and the first Holo release to add mobile automation, so the same model can now target Android alongside desktop.

Those are not small additions. Our [Holo3 guide](/guides/holo3-desktop-agent-osworld-record/) covered the original release in March 2026, which scored 77.8% on OSWorld (35B-A3B) but shipped only in full BF16 precision — roughly 70 GB VRAM for the 35B-A3B flagship, consistent with the [69.4 GB BF16 checkpoint file H Company lists for Holo3.1](https://huggingface.co/Hcompany/Holo-3.1-35B-A3B-GGUF/tree/main) (same parameter count). Holo3.1 adds [FP8, NVFP4, and Q4 GGUF quantized checkpoints](https://hcompany.ai/holo3.1) — the Q4 GGUF file is 21.3 GB, roughly a third the size of the BF16 checkpoint — changes the architecture to support mobile natively, and adds function-calling. This is the guide for builders who want to run agents locally, integrate Holo3.1 with standard frameworks, or build mobile automation workflows.

Our analysis draws on [H Company's official announcement](https://hcompany.ai/holo3.1), the [HuggingFace blog post](https://huggingface.co/blog/Hcompany/holo31), the [model collection](https://huggingface.co/collections/Hcompany/holo31) and [model card](https://huggingface.co/Hcompany/Holo-3.1-35B-A3B) on HuggingFace (which includes H Company's own benchmark charts), the [Holo Models API pricing page](https://hcompany.ai/holo-models-api), and [developer coverage from Codersera](https://codersera.com/blog/holo3-1-fast-local-computer-use-agents-2026/). We research and analyze; we do not test models hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; research and writing are done by AI.

**A note on this update:** an earlier version of this piece included a "140ms per step on a 12GB GPU" headline claim, a "Dynamic ROI encoding" architecture feature with a 60% token-reduction figure, a "vision encoder / action controller" modular-architecture claim, and a hardware table with specific RTX 4070/3080 Ti/4090 and M-series numbers. None of that could be verified against H Company's actual announcement, blog post, or model card — the real published hardware benchmarks cover only DGX Spark and a MacBook M4 Pro, and none of H Company's materials mention "Dynamic ROI encoding" or a modular vision/action split at all. Those claims have been corrected or removed below.

---

## What changed from Holo3 to Holo3.1

Three architectural differences separate the two releases, per [H Company's announcement](https://hcompany.ai/holo3.1) and [model card](https://huggingface.co/Hcompany/Holo-3.1-35B-A3B):

**1. Quantized checkpoints.** Holo3 shipped only in full BF16 precision (70 GB VRAM for 35B-A3B). Holo3.1 adds FP8, NVFP4 (W4A16), and Q4 GGUF variants of the 35B-A3B model — H Company's first release to ship quantized weights at all. Per H Company's own [benchmark chart](https://huggingface.co/Hcompany/Holo-3.1-35B-A3B), BF16 scores 80.0% on OSWorld while FP8 and NVFP4 both score 77.8% — a 2.2-point accuracy cost, negligible for most production use cases.

**2. Android support.** Holo3.1 expands beyond Holo3's desktop/browser focus into mobile automation. AndroidWorld score on the 35B-A3B model: **79.3%**, up from **67.2%** in Holo3 — a 12-point jump, per [H Company's own comparison chart](https://huggingface.co/Hcompany/Holo-3.1-35B-A3B). That closes almost all of the gap to Holo3.1's own desktop score (80.0% OSWorld); Holo3's mobile score had trailed its desktop score (77.8%) by more than 10 points.

**3. Function-calling protocol.** Holo3 output structured JSON only. Holo3.1 [adds native function-calling support](https://hcompany.ai/holo3.1), with near-parity performance against JSON outputs on OSWorld and H Company's internal benchmark suite. This means direct integration with LangChain, LlamaIndex, and other agent frameworks without custom output parsing.

---

## Model family: sizes and quantization

Holo3.1 ships four model sizes, but quantized checkpoints are only available for the 35B-A3B variant, per the [HuggingFace model collection](https://huggingface.co/collections/Hcompany/holo31):

| Model | Total params | Active params | Precision options | Checkpoint size |
|---|---|---|---|---|
| Holo3.1-0.8B | 0.8B | 0.8B (dense) | BF16 only | not published by H Company |
| Holo3.1-4B | 4B | 4B (dense) | BF16 only | not published by H Company |
| Holo3.1-9B | 9B | 9B (dense) | BF16 only | not published by H Company |
| Holo3.1-35B-A3B | 35B | ~3B (MoE) | BF16, FP8, NVFP4, Q4 GGUF | **69.4 GB** (BF16) / **21.3 GB** (Q4 GGUF) |

Checkpoint sizes for the 0.8B/4B/9B dense models and exact minimum-VRAM figures for any variant are not published in H Company's announcement, blog post, or model cards — we're not going to guess and label it a spec. What we can confirm from the [HuggingFace GGUF repo file listing](https://huggingface.co/Hcompany/Holo-3.1-35B-A3B-GGUF/tree/main): the Q4 GGUF file for 35B-A3B is 21.3 GB, plus an 899 MB vision projector — meaning full-GPU inference realistically needs a 24 GB+ card, not the 12 GB sometimes quoted elsewhere. llama.cpp and Ollama can split layers between GPU and CPU RAM to run it on a smaller card, but at reduced speed, not "full-speed on 12 GB."

The 35B-A3B is a **mixture-of-experts** model: 35 billion total parameters, but only roughly 3 billion activate per forward pass. This means you get 35B-level accuracy at 3B inference cost, though the full weights (all experts) still have to be resident in memory or offloaded, regardless of how few activate per token.

**Practical reality:** If you're building for consumer hardware, the 35B-A3B-GGUF is your target, but budget for a 24 GB card (or plan for CPU offload) rather than assuming 12 GB is enough. If you have an A100 or H100, the FP8 variant is faster at similar accuracy — though H Company's own published throughput numbers only cover DGX Spark and a MacBook M4 Pro (see the hardware section below), not A100/H100 specifically. The smaller dense models (0.8B, 4B, 9B) are for edge deployments where model quality can be traded for size — they don't have quantized options yet.

---

## Benchmark results

These numbers come directly from [H Company's own benchmark chart](https://huggingface.co/Hcompany/Holo-3.1-35B-A3B) (published alongside the model card) and its [DGX Spark quality-vs-throughput chart](https://hcompany.ai/holo3.1) — not estimates:

| Model | OSWorld | AndroidWorld |
|---|---|---|
| Holo3.1-35B-A3B (BF16) | **80.0%** | **79.3%** |
| Holo3.1-35B-A3B (FP8/NVFP4) | 77.8% | not published |
| Holo3.1-9B | 71.5% | 72.4% |
| Holo3.1-4B | 75.8% | 72.4% |
| Holo3.1-0.8B | 34.6% | not published |
| Holo3 (35B-A3B, prior release) | 77.8% | 67.2% |

Two observations worth flagging, and one correction to how earlier coverage of this release (including an earlier draft of this piece) framed it:

First, Holo3.1's mobile score (79.3% AndroidWorld) is now nearly on par with its desktop score (80.0% OSWorld) — within 0.7 points. That's notable because Holo3's mobile score (67.2%) had trailed its own desktop score (77.8%) by more than 10 points. Holo3.1's Android-specific training closed almost the entire gap — but desktop still edges out mobile slightly; it is not the case that Holo3.1 "scores better on mobile than desktop," a claim that circulated based on since-corrected numbers.

Second, the quantization cost on OSWorld is real but small: BF16 scores 80.0%, FP8 and NVFP4 both score 77.8% — a 2.2-point drop, confirmed directly in H Company's chart. H Company has not published an AndroidWorld score specifically for the quantized checkpoints, so we're not going to estimate one here. For most production use cases weighing the OSWorld trade-off, it looks worth it.

---

## Hardware decision table

H Company's own published hardware benchmarks (from its ["Agent speed with local inference" and "Quality vs throughput on DGX Spark" charts](https://hcompany.ai/holo3.1)) cover exactly two machines: a DGX Spark and a MacBook M4 Pro. There is no vendor-published data for RTX 4070/3080 Ti/4090, A100/H100, or M1/M2 — if you've seen those specific GPU/VRAM/latency numbers elsewhere (including an earlier version of this article), they did not come from H Company and we could not verify them independently. Here's what's actually measured:

| Hardware | Variant / harness | Requests per minute (H Company's own numbers) |
|---|---|---|
| DGX Spark | 35B-A3B-NVFP4, vLLM, fast harness | **18.1** — the fastest configuration H Company tested |
| DGX Spark | 35B-A3B-Q4 GGUF, llama.cpp, fast harness | 15.6 (llama.cpp lacks prefix/image caching for the Qwen architecture, per H Company's footnote, which likely understates its ceiling) |
| DGX Spark | 35B-A3B-FP8, vLLM, fast harness | 11.9 |
| MacBook M4 Pro | 35B-A3B-Q4 GGUF, llama.cpp, fast harness | 5.5 — the only consumer-hardware number H Company has published |
| RTX 4070/3080 Ti/4090, A100/H100, M1/M2 | — | Not benchmarked by H Company; treat any specific throughput/latency figure for these as unverified |

On throughput scaling: NVFP4 delivers 1.41x the token throughput of FP8 and 1.74x that of BF16 on DGX Spark specifically (326 tok/s BF16 → 404 tok/s FP8 → 568 tok/s NVFP4, per H Company's chart) — this is a DGX Spark figure, not a general "any NVIDIA GPU" figure. Combined with harness optimizations, H Company reports average agent step time on DGX Spark dropping from 6.8s to 3.3s (a ~2x end-to-end speedup) going from FP8 to NVFP4. We could not find any H Company figure in milliseconds for a single inference step on any hardware — the "140ms per step on a 12GB GPU" claim that circulated in earlier coverage of this release does not appear in H Company's announcement, blog post, or model cards, and we're removing it here rather than repeat it uncited.

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

If you don't want to run locally, [H Company provides a hosted endpoint](https://hcompany.ai/holo-models-api):

- **Free tier:** 10 requests per minute, no credit card required; register at [Portal-H](https://portal.hcompany.ai/)
- **Paid tier (35B-A3B, Apache 2.0):** $0.25/M input tokens, $1.80/M output tokens
- **Paid tier (122B-A10B, research-only flagship):** $0.40/M input tokens, $3.00/M output tokens

The 35B-A3B API pricing is competitive with other agent-grade models. The 122B-A10B is listed as "Research Only" on H Company's own pricing page — its weights aren't published, API access only.

---

## Android automation: what it actually means

[Holo3.1 expands Holo3's capabilities beyond browser and desktop control into mobile environments](https://hcompany.ai/holo3.1) — the first Holo release to target Android directly. Here's what that means practically:

The model receives screenshots of an Android device (via ADB or similar tooling), parses on-screen elements and coordinates, and outputs touch events, swipes, text input, and navigation actions. Your integration layer translates those outputs into actual Android UI automation commands.

The **79.3%** AndroidWorld score means the model successfully completes nearly four out of five Android benchmark tasks — handling touch targets, app switching, mobile navigation patterns, and Android system UI conventions. That's now close to (though still just under) Holo3.1's own 80.0% OSWorld desktop score, per [H Company's benchmark chart](https://huggingface.co/Hcompany/Holo-3.1-35B-A3B) — a big change from Holo3, whose mobile score (67.2%) trailed its desktop score (77.8%) by more than 10 points.

**What it doesn't do:** The model cannot process video natively, cannot handle specialized gesture controls or custom animations well, and requires proper screenshot capture setup on the target device or emulator. The 79.3% figure is on standard Android UI; apps with heavy custom UI or non-standard interactions will degrade from that number.

---

## Three limitations to plan around

**1. No quantized checkpoints for smaller models.** The 0.8B, 4B, and 9B variants are BF16 only. If you need a quantized model and can't fit 35B-A3B (even at Q4), Holo3.1 doesn't have a path for you yet. H Company hasn't announced a timeline for quantized smaller models.

**2. Context window management for long sessions.** Long-running agent sessions accumulate visual history (screenshots), and H Company's public materials don't describe a specific token-reduction technique for this — an earlier version of this article cited a "Dynamic ROI encoding" feature with a 60% token-reduction figure that we could not find in H Company's announcement, blog post, or model cards, so we've removed that claim. What builders still need, regardless: a sliding-window screenshot buffer in your own harness. This is a harness problem, not something Holo3.1 solves for you — if you deploy it without handling it, you'll hit context limits on extended tasks.

**3. NVFP4 optimization is NVIDIA-specific.** The largest throughput gains H Company has published (1.74x vs. BF16, 1.41x vs. FP8) are measured on DGX Spark hardware specifically. H Company's only non-NVIDIA reference numbers are for a MacBook M4 Pro running Q4 GGUF via llama.cpp, which is markedly slower (5.5 requests/minute vs. DGX Spark's 15.6–18.1). GGUF via llama.cpp is the more portable path across hardware, just not the fastest one.

---

## When to use Holo3.1 vs. alternatives

Holo3.1 is a strong choice if:
- You need computer-use capability on hardware you own (budget a 24 GB+ GPU, or accept slower CPU-offloaded inference on less)
- You're building Android automation and need a model that was actually trained on it
- You want framework compatibility via function-calling without custom output parsing
- Privacy or latency requirements make cloud APIs unsuitable

Stick with the Holo3.1 hosted API (or Holo3 if you have existing deployments) if:
- You're still evaluating computer-use agents and don't want to invest in local inference infrastructure
- Your task set is primarily desktop/web without a mobile component
- The ~2-point accuracy difference between quantized and BF16 (80.0% vs. 77.8% OSWorld) matters to your evals

Consider alternatives (Claude's computer-use tool, GPT-5.x computer-use) if:
- You need the highest possible accuracy ceiling and aren't cost-constrained
- You're already in the Anthropic or OpenAI ecosystem and value unified tooling
- Local inference isn't a requirement

---

## What to watch for

H Company hasn't announced a timeline for extending quantized checkpoints to the 0.8B, 4B, and 9B variants. When that lands, the local inference story expands significantly — a quantized smaller model would make computer-use viable on a much wider hardware base than the 21+ GB the 35B-A3B Q4 GGUF currently needs.

AndroidWorld performance at 79.3% is already strong for a first Android-trained release, and it has already nearly closed the gap with desktop performance (79.3% mobile vs. 80.0% desktop, per H Company's own numbers) — a big jump from Holo3's 10-plus-point mobile/desktop gap. Watch whether Holo3.1's mobile score overtakes its desktop score in future releases, or whether desktop training pulls further ahead again.

The function-calling addition opens the model to standard agent orchestration frameworks in ways Holo3 couldn't match. Expect community integrations with LangChain, LlamaIndex, and similar tools to emerge as builders deploy Holo3.1.
