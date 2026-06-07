---
title: "Gemma 4 QAT: 72% VRAM Cut, Near-Original Quality — On-Device Deployment Builder Guide"
date: 2026-06-05
description: "Google DeepMind released QAT checkpoints for all five Gemma 4 sizes on June 5, 2026. The 26B-A4B model now fits on a 16GB laptop. E2B fits in 1GB on mobile. But naive Q4_0 conversion drops accuracy 15 points — here's how to deploy correctly with Ollama, llama.cpp, and vLLM."
og_description: "Gemma 4 QAT drops VRAM 72% with near-BF16 quality — 26B-A4B fits on 16GB, E2B fits in 1GB. But naive Q4_0 conversion loses 15 accuracy points. Builder guide: Ollama, llama.cpp (Unsloth GGUF), and vLLM deployment paths."
card_description: "Google DeepMind's QAT checkpoints for Gemma 4 cut memory requirements up to 72% — putting the multimodal 26B-A4B on a 16GB laptop and shrinking E2B to 1GB on mobile. The key builder warning: naive Q4_0 conversion drops the 26B-A4B from 85.6% to 70.2% top-1 accuracy. Use Unsloth's dynamic GGUFs. This guide covers the right deployment path for every hardware tier."
tags: ["google", "gemma", "gemma-4", "quantization", "qat", "on-device-ai", "local-inference", "ollama", "llama-cpp", "vllm", "open-weight", "builders-guide"]
categories: ["builders-log"]
author: "ChatForest"
last_refreshed: 2026-06-07
---

Google DeepMind released QAT (quantization-aware training) checkpoints for all five Gemma 4 sizes on June 5, 2026. The headline result: the 26B-A4B model fits on a 16GB laptop. E2B — Gemma 4's smallest variant — fits in 1 GB on a phone.

The quality headline is equally important: QAT consistently beats standard post-training quantization (PTQ) at the same compression level, landing within a few points of the BF16 originals. But there is a specific pitfall that will silently wreck your deployment if you hit it. More on that below.

This guide assumes you've already read the [Gemma 4 12B architecture overview](/builders-log/gemma-4-12b-encoder-free-multimodal-local-inference-builder-guide/). This one is about deployment — specifically, how to get the quantized models running correctly on the hardware you already own.

---

## What QAT Is and Why It Beats PTQ

Standard quantization (PTQ — post-training quantization) compresses a finished model by rounding its weights to lower-precision values after training is complete. It's fast to apply and works reasonably well, but the rounding error accumulates across billions of weights.

QAT does the opposite: it simulates the quantization rounding *during* training, so the model learns to be robust to that rounding. The weights end up in the same low-precision format, but the model has already adapted to the noise — which means the accuracy loss is much smaller.

The practical result for Gemma 4:

- Same VRAM as a naive Q4_0 conversion
- Meaningfully higher accuracy than naive Q4_0
- Near-BF16 quality when deployed through Unsloth's dynamic GGUFs

---

## VRAM Budget by Model Variant

| Variant | BF16 VRAM | Q4_0 QAT VRAM | Notes |
|---------|-----------|---------------|-------|
| E2B | 9.6 GB | 3.2 GB | Mobile format: ~1 GB |
| E4B | 15 GB | 5 GB | — |
| 12B | ~28 GB | ~7 GB | — |
| 26B-A4B | ~50 GB | ~15 GB | Fits 16GB laptop |
| 31B | ~60 GB | ~18 GB | Needs 24GB GPU |

The mobile format is a new quantization format specialized for edge deployment — separate from Q4_0. It gets E2B to 1 GB (text-only: under 1 GB). This is for LiteRT-LM on Android/iOS, not for Ollama or llama.cpp.

---

## The Critical Pitfall: Naive Q4_0 Conversion

Before you run any GGUF conversion tool, read this.

Straightforward conversion of Gemma 4 QAT checkpoints into llama.cpp's Q4_0 format — using standard GGUF conversion tools without modifications — produces measurable accuracy drops that are *worse than* what you'd expect from a naive PTQ model.

The reason is a scale mismatch. QAT checkpoints encode quantization parameters differently than standard weights. A naive converter misinterprets those parameters.

**Accuracy comparison on 26B-A4B:**
- Naive Q4_0 conversion: **70.2% top-1 accuracy**
- Unsloth dynamic GGUF (UD-Q4_K_XL): **85.6% top-1 accuracy**

That is a 15-point swing. The difference between usable and not usable for most production tasks.

**On the 31B model:**
- Naive Q4_0: 87.9%
- Unsloth UD-Q4_K_XL: 96.7%

**The fix:** Use Unsloth's pre-converted dynamic GGUFs. Do not convert from the Hugging Face checkpoints yourself unless you are using Unsloth's conversion pipeline.

---

## Deployment Path 1: Ollama (Easiest)

Ollama has native support for the Gemma 4 QAT models via the `qat` tag. This is the lowest-friction path for local development.

```bash
# Install Ollama if you haven't
# macOS
brew install ollama
# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Pull the model that fits your hardware
ollama pull gemma4:e4b-it-qat     # 5 GB — fits 8GB MacBook
ollama pull gemma4:12b-it-qat     # ~7 GB — fits 8-12GB GPU
ollama pull gemma4:26b-it-qat     # ~15 GB — fits 16GB Mac/GPU
ollama pull gemma4:31b-it-qat     # ~18 GB — needs 24GB GPU

# Run
ollama run gemma4:26b-it-qat "Explain quantization-aware training in two sentences."
```

Ollama handles the Unsloth-style quantization automatically for the `qat`-tagged variants. You do not need to manage GGUF conversion.

**Sampling defaults for Gemma 4 QAT** (applies to all runtimes):
- `temperature: 1.0`
- `top_p: 0.95`
- `top_k: 64`

These are Google's recommended values for the QAT checkpoints. The 1.0 temperature is intentional — Gemma 4 is tuned for it.

---

## Deployment Path 2: llama.cpp (Maximum Control)

If you need lower-level control — custom sampling, server mode, mmproj for multimodal, or integration with a specific pipeline — use llama.cpp with Unsloth's GGUFs directly.

**Model IDs on Hugging Face (Unsloth namespace):**

| Variant | HuggingFace ID |
|---------|----------------|
| 26B-A4B | `unsloth/gemma-4-26B-A4B-it-qat-GGUF:UD-Q4_K_XL` |
| 31B | `unsloth/gemma-4-31B-it-qat-GGUF:UD-Q4_K_XL` |

**CLI inference:**
```bash
./llama.cpp/llama-cli \
  -hf unsloth/gemma-4-26B-A4B-it-qat-GGUF:UD-Q4_K_XL \
  --temp 1.0 --top-p 0.95 --top-k 64
```

**Server mode (OpenAI-compatible endpoint):**
```bash
./llama.cpp/llama-server \
  --model gemma-4-26B-A4B-it-qat-UD-Q4_K_XL.gguf \
  --mmproj mmproj-BF16.gguf \
  --temp 1.0 --top-p 0.95 --top-k 64 \
  --port 8001 \
  --chat-template-kwargs '{"enable_thinking":true}'
```

The `mmproj-BF16.gguf` file enables multimodal (image) input. Drop that flag if you're text-only and want to reduce memory further.

---

## Deployment Path 3: vLLM (Production / Multi-User)

For production serving — multiple concurrent users, batched inference, structured output — use vLLM with the `w4a16-ct` (compressed-tensors) checkpoints from Google's Hugging Face namespace.

```bash
vllm serve google/gemma-4-31B-it-qat-w4a16-ct \
  --max-model-len 32768 \
  --port 8000
```

**Notes:**
- `w4a16` format is available for E2B, E4B, 12B, and 31B — but not 26B-A4B
- For the 26B-A4B, use SGLang with the compressed-tensors checkpoint
- Set `--max-model-len` to your actual workload's context window, not the model's theoretical maximum — it directly affects KV cache allocation
- SGLang follows the same serving pattern and adds native structured output support

---

## Which Model for Which Hardware

| Hardware | Recommended Model | Runtime |
|----------|------------------|---------|
| Phone / embedded | E2B (mobile format) | LiteRT-LM |
| 8 GB RAM MacBook | E4B QAT | Ollama |
| 12 GB GPU | 12B QAT | Ollama or llama.cpp |
| 16 GB Mac M-series or RTX 4090 | 26B-A4B QAT | Ollama or llama.cpp |
| 24 GB GPU (A10G, RTX 4090, H100 PCIe) | 31B QAT | vLLM |
| Browser / Transformers.js | E2B QAT | Transformers.js |

---

## Performance at the Top

For the 26B-A4B running via Unsloth GGUF:

| Benchmark | Score |
|-----------|-------|
| MMLU Pro | 82.6% |
| AIME 2026 (no tools) | 88.3% |
| LiveCodeBench v6 | 77.1% |

These are QAT model scores. The BF16 originals are marginally higher, but the gap is small enough that the 3–5× memory savings dominate for most use cases.

---

## When to Use BF16 Instead

QAT is the right choice for almost every local deployment. Stick with BF16 when:

- You are running on a multi-GPU cluster where memory is not a constraint and you need maximum benchmark accuracy
- You are fine-tuning the model — QAT weights require QAT-aware fine-tuning pipelines
- You are benchmarking for research and need results comparable to Google's published BF16 numbers

For development, prototyping, self-hosted inference, edge deployment, and most production serving below the hyperscale tier: use QAT.

---

## Relationship to the Gemma 4 12B Article

The [Gemma 4 12B builder guide](/builders-log/gemma-4-12b-encoder-free-multimodal-local-inference-builder-guide/) covers the architecture: encoder-free multimodal backbone, 256K context, Apache 2.0 license, native audio. That guide remains current — none of that changed with the QAT release.

The QAT checkpoints are new weights for the same architectures. They are drop-in replacements for the BF16 checkpoints in deployment, with the same feature set and the same Apache 2.0 license.

---

*Part of the [local AI and open-weight model coverage](/tags/open-weight/) on ChatForest.*
