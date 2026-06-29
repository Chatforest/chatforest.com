# DiffusionGemma 26B: Google's Text-Diffusion Model Hits 1100 Tokens/Sec — What Builders Actually Need to Know

> Google DeepMind released DiffusionGemma 26B-A4B on June 10 — a text-diffusion model that generates tokens in parallel batches rather than one at a time, hitting 1100+ tok/s on H100. Apache 2.0, 3.8B active params, 18GB VRAM in NVFP4. The catch: it scores meaningfully lower than Gemma 4 on reasoning and coding. Here's the honest breakdown.


On June 10, 2026, Google DeepMind released **DiffusionGemma 26B-A4B-it** — a model that replaces the standard one-token-at-a-time autoregressive inference loop with a text diffusion approach that generates 15–20 tokens per forward pass. The result: **1100+ tokens per second on an H100 in FP8**, which is roughly 4x faster than a comparably-sized autoregressive model on the same hardware.

It's open-weight, Apache 2.0, fits in 18GB of VRAM when quantized to NVFP4, and has day-zero support in vLLM, Transformers, MLX, and Unsloth.

The trade-off is real: DiffusionGemma scores substantially lower than Gemma 4 on reasoning, math, and coding. Google is explicitly calling this release experimental and recommending Gemma 4 for quality-critical production workloads. For builders, the question is whether the speed profile makes sense for your specific use case — and in several cases, it might.

---

## What Text Diffusion Actually Means (and Why It's Fast)

Standard autoregressive language models generate one token at a time. Each token depends on the previous tokens, so the process is inherently sequential. You can batch multiple requests, but you can't parallelize the generation of a single response.

Text diffusion works differently. The model starts with a "canvas" of 256 masked tokens and iteratively denoises them — predicting the most likely tokens, committing the high-confidence ones, and re-running the diffusion pass on the remainder. Each denoising step can update 15–20 tokens simultaneously. With up to 48 maximum denoising steps and adaptive stopping when predictions stabilize, a typical 512-token response might require 20–30 denoising passes instead of 512 autoregressive steps.

The architecture uses an encoder-decoder design: an autoregressive encoder processes and caches the prompt context, then a bidirectional-attention decoder runs the diffusion passes over the generation canvas. The bidirectional attention in the decoder is what allows parallel token prediction — unlike autoregressive models, the decoder can "see" the entire canvas position at once, not just positions to the left.

This is the same principle that made diffusion models dominant in image generation (where every pixel can be denoised in parallel). DiffusionGemma applies it to discrete text tokens.

---

## Model Specs

| Property | Value |
|----------|-------|
| Total parameters | 25.2B |
| Active parameters | 3.8B |
| Expert configuration | 8 active / 128 total + 1 shared |
| Layers | 30 |
| Context window | 256K tokens |
| Canvas size | 256 tokens per pass |
| Vocabulary | 262K tokens |
| Vision encoder | ~550M parameters |
| Supported inputs | Text, image, video (≤60s @ 1fps) |
| Supported languages | Pre-trained on 140+, strong on 35+ |
| Training data cutoff | January 2025 |
| License | Apache 2.0 |

The MoE design keeps the active compute low. At 3.8B active parameters per forward pass (despite 25.2B total weights), the inference cost per token batch is closer to a 4B dense model than a 26B dense model. This is why the VRAM requirement is manageable: you need room to store the 25.2B weights plus activation memory, but the compute per step is light.

---

## Benchmark Results

Be honest with yourself about these numbers before deploying.

### Reasoning and Knowledge

| Benchmark | DiffusionGemma | Gemma 4 |
|-----------|----------------|---------|
| MMLU Pro | 77.6% | 82.6% |
| AIME 2026 (no tools) | 69.1% | 88.3% |
| GPQA Diamond | 73.2% | 82.3% |
| BigBench Extra Hard | 47.6% | 64.8% |

The AIME gap is the most telling: **69.1% vs 88.3%**. On competition math, the quality cost of diffusion-based generation is significant. Gemma 4 is clearly better for tasks requiring multi-step reasoning.

### Multimodal

| Benchmark | DiffusionGemma | Gemma 4 |
|-----------|----------------|---------|
| MMMU Pro | 54.3% | 73.8% |
| MATH-Vision | 70.5% | 82.4% |
| OmniDocBench 1.5 | **0.319** | 0.149 |

The OmniDocBench number is the interesting exception: **DiffusionGemma outperforms Gemma 4 on document parsing**. OCR, layout-aware extraction, and dense document understanding are tasks where the bidirectional attention in the diffusion decoder provides a structural advantage. If document processing is your primary workload, this score is worth taking seriously.

### Inference Speed

| Hardware | Tokens per second (FP8 / NVFP4) |
|----------|----------------------------------|
| H100 | 1100+ |
| RTX 5090 | 700+ |

These numbers are for batch inference. Single-request latency depends on the diffusion pass count, which varies with output length and content complexity.

---

## Hardware Requirements

| Configuration | VRAM | Notes |
|---------------|------|-------|
| NVFP4 quantized | ~18GB | RTX 5090 viable (700+ tok/s) |
| BF16 full precision | ~50GB+ | Multi-GPU setup required |
| FP8 | ~28GB | Single H100 preferred |

The NVFP4 path is the practical consumer-GPU option. An RTX 5090 with 32GB VRAM can run the quantized model. RTX 4090 (24GB) is marginal — you may be able to run quantized inference, but with limited headroom for context.

NVIDIA has published an NVFP4-quantized model (`nvidia/diffusiongemma-26B-A4B-it-NVFP4`) specifically for this hardware path.

---

## Deployment

### vLLM (recommended for production)

```bash
pip install vllm

vllm serve "google/diffusiongemma-26B-A4B-it"
```

Once running, the server exposes an OpenAI-compatible endpoint. Any client that uses the `openai` Python library can redirect with two env variable changes:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="google/diffusiongemma-26B-A4B-it",
    messages=[{"role": "user", "content": "Summarize this document..."}],
    max_tokens=1024
)
```

### Transformers (for experimentation)

```python
from transformers import DiffusionGemmaForBlockDiffusion, AutoProcessor

MODEL_ID = "google/diffusiongemma-26B-A4B-it"

processor = AutoProcessor.from_pretrained(MODEL_ID)
model = DiffusionGemmaForBlockDiffusion.from_pretrained(
    MODEL_ID,
    dtype="auto",
    device_map="auto",
)

messages = [{"role": "user", "content": "Why is the sky blue?"}]
inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device)

output = model.generate(**inputs, max_new_tokens=512)
text = processor.decode(output[0], skip_special_tokens=False)
```

Note: `DiffusionGemmaForBlockDiffusion` is a new class specific to this model. Standard `AutoModelForCausalLM` will not work — this model's generation loop is different from autoregressive models.

### Image input

```python
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://example.com/document.jpg"},
            {"type": "text", "text": "Extract all text from this document."}
        ]
    },
]
inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=2048)
```

**Image placement matters**: Google's documentation is explicit — place images before text in your prompts for best performance.

**Token budgets for image resolution**: 70, 140, 280, 560, 1120 tokens. Lower budgets (70–280) for classification and captioning; higher budgets (560–1120) for OCR and document parsing where detail matters.

### NVFP4 via NVIDIA build (for RTX 5090)

```bash
# Pull from NVIDIA's hosted endpoint (no local download required)
docker model run hf.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4
```

Or pull and run locally using the HuggingFace weights directly.

---

## Diffusion Sampling Settings

The model has configurable denoising parameters. Google's recommended defaults:

| Parameter | Value |
|-----------|-------|
| Maximum denoising steps | 48 |
| Temperature start | 0.8 |
| Temperature end | 0.4 |
| Temperature schedule | Linear decay |
| Entropy bound | 0.1 |
| Entropy threshold | 0.005 |

Adaptive stopping kicks in when per-canvas entropy drops below 0.005 and predictions stabilize. For short factual responses, this typically terminates well before 48 steps. For longer, more complex outputs, expect the full step count.

You can trade quality for speed by reducing `max_denoising_steps` — fewer passes means faster generation but more noise in the output. Experiment on your specific workload to find the right balance.

---

## Thinking Mode

DiffusionGemma includes a thinking mode that produces internal reasoning before a final answer:

```python
# Enable thinking with system prompt
messages = [
    {"role": "system", "content": "<|think|>Work through the problem step by step before answering."},
    {"role": "user", "content": "What's the most efficient way to process 10,000 PDFs?"}
]
```

Thinking output is wrapped in `<|channel>thought\n[reasoning]<channel|>[final answer]` markers. The reasoning token stream is separate from the output and can be surfaced to users or discarded.

Important: thinking mode adds denoising passes for the reasoning canvas before the answer canvas. It will slow down overall generation relative to non-thinking mode. For high-throughput use cases, profile carefully before enabling thinking by default.

---

## When to Use DiffusionGemma (and When Not To)

### Strong use cases

**Document extraction and OCR.** The OmniDocBench 1.5 result (0.319 vs Gemma 4's 0.149) is the clearest signal that DiffusionGemma has a genuine advantage in document-parsing workflows. If you're processing PDFs, invoices, forms, or dense structured documents, the combination of speed and this specific quality advantage makes it worth evaluating seriously.

**High-throughput batch inference.** Summarizing thousands of short texts, generating product descriptions at scale, or any batch workflow where throughput matters more than frontier reasoning quality. At 1100 tokens/second on a single H100, you're covering substantially more ground per GPU-hour.

**Interactive applications requiring real-time streaming.** The parallel generation means first-token latency is different from autoregressive models — but steady-state throughput is high. For chat-adjacent interfaces where users are watching tokens appear, the speed profile can feel noticeably snappier.

**Multimodal pipelines with image/video input.** The vision encoder handles object detection, captioning, chart reading, and video frame analysis. At 256K context, you can process a long document with many embedded images in a single inference call.

### Cases where Gemma 4 is better

**Multi-step reasoning.** The AIME 69.1% vs 88.3% gap is not noise. If your workflow involves complex mathematical reasoning, extended logic chains, or any task that requires consistent multi-step coherence, use Gemma 4.

**Coding.** Google's own model card notes weaker coding evaluation performance relative to Gemma 4. For anything beyond simple code generation or syntax correction, the quality difference is likely to show in production.

**Research or analysis tasks.** BigBench Extra Hard (47.6% vs 64.8%) suggests that tasks requiring extended, structured reasoning will produce meaningfully lower quality outputs.

---

## Comparison to Alternatives

| Use Case | Best Choice | Why |
|----------|-------------|-----|
| Fastest open-weight text generation | **DiffusionGemma** | 4x faster, Apache 2.0 |
| Highest quality open-weight general reasoning | Gemma 4 (27B) | +5–19 points across benchmarks |
| Best open-weight agentic coding | North Mini Code (Cohere) | Purpose-built, SWE-Bench 61% pass@1 |
| Document OCR and extraction | **DiffusionGemma** | OmniDocBench best-in-class |
| Consumer GPU (24GB VRAM) | Gemma 4 27B FP8 | DiffusionGemma NVFP4 marginal on 4090 |
| Consumer GPU (32GB VRAM) | **DiffusionGemma NVFP4** | RTX 5090 viable, 700+ tok/s |
| No GPU budget | Gemini 3.5 Flash API | Speed + quality at hosted API rates |

---

## Limitations to Know Before Deploying

**Training cutoff is January 2025.** The model's world knowledge stops there. For tasks requiring up-to-date information, you need retrieval augmentation.

**Canvas size constrains coherence.** Each 256-token canvas is denoised semi-independently. Very long structured outputs — particularly those requiring strict formatting or referencing content from many pages back — can show incoherence at canvas boundaries. This is an architectural constraint, not something you can tune away.

**Diffusion != autoregressive for all tasks.** The generation mechanics change what "temperature" and "sampling" mean. Some prompting techniques that work reliably for autoregressive models (few-shot examples, specific chain-of-thought formats) behave differently under text diffusion. Plan for a re-evaluation pass if you're porting an existing prompt library.

**Experimental positioning.** Google's own release notes describe DiffusionGemma as experimental and do not recommend it for production workloads where quality is the primary constraint. That's a meaningful signal from the team that built it.

---

## Builder Checklist

- [ ] Confirm your use case: speed-critical (batch/throughput) OR document extraction → evaluate DiffusionGemma; reasoning/coding → use Gemma 4
- [ ] Hardware path: NVFP4 for RTX 5090 (700+ tok/s), FP8 for H100 (1100+ tok/s), BF16 for multi-GPU research
- [ ] Use `DiffusionGemmaForBlockDiffusion` class in Transformers — standard `AutoModelForCausalLM` will not work
- [ ] Place images before text in multimodal prompts
- [ ] Set image token budget based on detail level: 70–280 for captioning/classification, 560–1120 for OCR/documents
- [ ] Benchmark your specific workload — don't rely only on MMLU numbers for your decision
- [ ] Profile thinking mode overhead before enabling by default in high-throughput pipelines
- [ ] Plan for canvas boundary effects in very long structured outputs
- [ ] Implement retrieval augmentation if your task requires post-January-2025 world knowledge
- [ ] Review Apache 2.0 license terms for your commercial deployment (permissive; confirm with legal for regulated industries)

---

Model weights: [google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)
NVFP4 variant: [nvidia/diffusiongemma-26B-A4B-it-NVFP4](https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4)
Official announcement: [blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)
NVIDIA build endpoint: [build.nvidia.com/google/diffusiongemma-26b-a4b-it](https://build.nvidia.com/google/diffusiongemma-26b-a4b-it/modelcard)

