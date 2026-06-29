# Zamba2-VL: Hybrid Mamba2-Transformer VLM Cuts Time-to-First-Token by 10x

> Zyphra released Zamba2-VL on June 12, 2026 — a hybrid SSM-Transformer vision-language model at 1.2B, 2.7B, and 7B scales that delivers roughly 10x lower time-to-first-token than Transformer baselines, while matching competitive VLMs on document and chart tasks. Here is the architecture, the benchmarks, and when to use it over InternVL or Qwen-VL.


Zyphra released **Zamba2-VL** on June 12, 2026: a family of hybrid vision-language models at 1.2B, 2.7B, and 7B parameters, all under Apache 2.0. The core claim is architectural: by replacing the standard Transformer backbone with Zyphra's Mamba2–Transformer hybrid, these models deliver roughly **10x lower time-to-first-token** on long prefills while remaining competitive with the best open-weight VLMs of similar size.

If you are building anything where the first token of a vision response needs to arrive fast — document streaming, real-time analysis, edge deployment — this is the first open-weight VLM architecture worth evaluating for that constraint.

## What Zamba2-VL Is

Zamba2-VL is a three-stage trained multimodal model that stacks a Zyphra-designed language backbone with a vision encoder borrowed from Qwen2.5-VL. It exists in three sizes:

| Size | Param count (language) | Total with vision | Notes |
|------|----------------------|-------------------|-------|
| Zamba2-VL-1.2B | 1.2B | ~1.5B | Smallest; on-device target |
| Zamba2-VL-2.7B | 2.7B | ~3.2B | Mid-tier; best counting scores at its class |
| Zamba2-VL-7B | 7B | ~8B | Flagship; competitive against 8B Transformer VLMs |

All three use Apache 2.0 licensing, making them deployment-friendly.

## Architecture

The design has three components:

**Language backbone: Zamba2 hybrid SSM-Transformer.** Instead of pure Transformer layers, Zamba2 interleaves Mamba2 state-space layers with a small number of shared Transformer blocks, each augmented with LoRA projectors. Mamba2 layers operate on a constant-size recurrent state — there is no key-value cache that grows with sequence length. The shared Transformer blocks handle global context where it matters most.

The practical consequence for inference: at 32k-token prefill lengths, the KV cache of a standard Transformer is doing significant memory work. Zamba2 is not. This is where the 10x TTFT advantage comes from — it is not compute savings per se, it is memory access pattern savings.

**Vision encoder: Qwen2.5-VL ViT.** Zyphra chose this encoder over SigLIP-2 and CLIP in an ablation study. The Qwen2.5-VL ViT uses 2D rotary position embeddings applied to image patches and supports dynamic-resolution processing — image inputs are not resized to a fixed shape before encoding. The ablation numbers: Qwen2.5-VL ViT scored 73.14 average across image benchmarks versus SigLIP-2 at 66.18 and CLIP at 61.87.

**Connector: 2-layer MLP adapter.** A two-layer MLP pools 2×2 patch-embedding windows into single vectors, reducing the vision token count by 4x before passing into the LLM backbone. This is a standard spatial compression approach — the result is that a high-resolution image generates far fewer tokens downstream.

## Training Pipeline

Three stages, totaling roughly 50 billion tokens:

- **Stage 1 (Alignment, 230M tokens):** Only the MLP adapter is trained, at low resolution (0.3MP). Data is primarily image-caption pairs from LLaVA-ReCap-558K.
- **Stage 2 (Pretraining, 30B tokens):** Full model training on a heterogeneous multimodal mix up to 2.7MP resolution. Document and OCR data deliberately oversampled to compensate for Mamba2's initial weaker performance on text-dense vision tasks.
- **Stage 3 (SFT, 20B tokens):** Instruction tuning on curated multi-turn conversation and grounding data.

The OCR/document upsampling in Stage 2 is notable — the team diagnosed a gap early and compensated in training rather than in architecture.

## Benchmarks

### 7B model vs. 8B Transformer VLMs

| Benchmark | Zamba2-VL-7B | PerceptionLM-8B | Qwen3-VL-8B | InternVL3.5-8B | Molmo2-8B |
|-----------|:---:|:---:|:---:|:---:|:---:|
| AI2D (test) | 90.6 | 91.8 | 92.3 | 92.5 | **94.1** |
| ChartQA (test) | 85.3 | 86.0 | 85.3 | **86.7** | 86.0 |
| DocVQA (test) | 92.9 | 94.6 | **96.1** | 92.3 | 93.2 |
| TextVQA (val) | 81.0 | 80.4 | 83.2 | 77.7 | **83.9** |
| OCRBench | 81.6 | 84.2 | **87.2** | 83.8 | 61.4 |
| VQA v2.0 (val) | 82.8 | 84.0 | 82.5 | 78.6 | **86.1** |
| MathVista (mini) | 61.2 | 62.2 | 66.1 | **73.9** | 61.4 |
| MMMU (val) | 44.0 | 43.8 | 54.3 | **58.0** | 47.7 |

**Reading these numbers honestly:** Zamba2-VL-7B lands competitively on document-heavy tasks (ChartQA tied with Qwen3-VL, DocVQA within 3 points of Qwen3). It falls noticeably behind on MMMU (44.0 vs. InternVL3.5's 58.0) and MathVista (61.2 vs. InternVL3.5's 73.9). Those 14-point gaps on MMMU are real. The hybrid architecture appears to give up some general reasoning for latency gains.

### Visual counting: standout performance

The most distinctive benchmark result is on visual counting tasks:

| Benchmark | Zamba2-VL-1.2B | Zamba2-VL-2.7B | Zamba2-VL-7B | InternVL3.5-1B (reference) |
|-----------|:---:|:---:|:---:|:---:|
| PixMoCount | 62.5 | 82.5 | 85.3 | 32.8 |
| CountBenchQA | 56.9 | 87.5 | 90.6 | — |

The 1.2B model at PixMoCount (62.5) more than doubles the score of the 1B InternVL at the same size class (32.8). The 2.7B at CountBenchQA (87.5) exceeds what most 7B Transformer VLMs achieve. This is a legitimate differentiator, not a benchmark cherry-pick — visual counting is a practically useful capability for inventory, retail, and structured data extraction tasks.

### All three sizes: document and reasoning

| Benchmark | 1.2B | 2.7B | 7B |
|-----------|:---:|:---:|:---:|
| DocVQA | 87.4 | 90.9 | 92.9 |
| ChartQA | 77.6 | 79.6 | 85.3 |
| OCRBench | 71.4 | 73.6 | 81.6 |
| VQA v2.0 | 78.0 | 79.6 | 82.8 |
| MMMU | 32.4 | 37.7 | 44.0 |
| MathVista | 48.7 | 51.0 | 61.2 |

The scaling is consistent. DocVQA improves 5.5 points from 1.2B to 7B; MMMU improves 11.6 points — reasoning tasks scale more steeply with model size than document reading.

## Installation and Usage

Zamba2-VL is **not compatible with standard HuggingFace transformers**. It requires a custom fork:

```bash
# Required: Zyphra's custom transformers
pip install "transformers @ git+https://github.com/Zyphra/transformers.git@zamba2-vl"
pip install qwen-vl-utils==0.0.2
pip install flash_attn

# Required for performance: Mamba2 kernels (must build from source)
pip install --no-build-isolation "causal-conv1d @ git+https://github.com/Zyphra/z-causal-conv1d.git@zamba2-vl"
pip install --no-build-isolation "mamba-ssm @ git+https://github.com/Zyphra/mamba.git@zamba2-vl"
```

The custom transformers fork and Mamba2 kernels are non-optional for getting the advertised latency profile. Without the Mamba2 kernels installed, the model will fall back to a slower path with significantly higher latency and memory usage.

### Basic inference (single image)

```python
from transformers import Zamba2_VLForConditionalGeneration, Zamba2_VLProcessor
import torch
from PIL import Image
from qwen_vl_utils import process_vision_info
import requests

device = "cuda"

# Load model and processor
processor = Zamba2_VLProcessor.from_pretrained(
    "Zyphra/Zamba2-VL-7B",
    temporal_patch_size=1
)
model = Zamba2_VLForConditionalGeneration.from_pretrained(
    "Zyphra/Zamba2-VL-7B",
    device_map=device,
    torch_dtype=torch.bfloat16,
    attn_implementation="flash_attention_2"
)

# Load an image
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

# Build conversation
num_img_tokens = 3400  # controls resolution: more tokens = higher resolution input
conversation = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": image,
                "max_pixels": num_img_tokens * 28 * 28,
                "min_pixels": 10 * 28 * 28
            },
            {"type": "text", "text": "What do you see in the image?"},
        ],
    },
]

# Tokenize and generate
prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
images, _ = process_vision_info(conversation)
inputs = processor(
    text=prompt,
    images=images,
    add_special_tokens=True,
    return_tensors="pt"
)
inputs = {k: v.to(device) for k, v in inputs.items()}

outputs = model.generate(**inputs, max_new_tokens=256)
response = processor.tokenizer.decode(
    outputs[0][inputs["input_ids"].shape[-1]:],
    skip_special_tokens=True
)
print(response)
```

The `num_img_tokens` parameter directly controls how many tokens the vision encoder generates per image. At 3400, you are feeding high-resolution patches. Reduce to 1024–1600 for faster inference when full resolution is not needed.

### Document processing pipeline

For document-heavy workloads (the model's strongest use case), structured extraction with explicit output formatting improves reliability:

```python
def extract_document_fields(image_path: str, fields: list[str]) -> dict:
    """Extract structured fields from a document image."""
    image = Image.open(image_path)
    field_list = "\n".join(f"- {f}" for f in fields)

    conversation = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": image,
                    "max_pixels": 5000 * 28 * 28,  # higher res for documents
                    "min_pixels": 100 * 28 * 28
                },
                {
                    "type": "text",
                    "text": (
                        f"Extract the following fields from this document. "
                        f"Return JSON only.\n\nFields:\n{field_list}"
                    )
                },
            ],
        },
    ]

    prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
    images, _ = process_vision_info(conversation)
    inputs = processor(text=prompt, images=images, add_special_tokens=True, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    outputs = model.generate(**inputs, max_new_tokens=512)
    raw = processor.tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:],
        skip_special_tokens=True
    )

    import json
    # Strip markdown fences if present
    raw = raw.strip().removeprefix("```json").removesuffix("```").strip()
    return json.loads(raw)

# Example
result = extract_document_fields(
    "invoice.png",
    ["invoice_number", "date", "total_amount", "vendor_name", "line_items"]
)
```

For invoice and receipt processing, set `max_pixels` higher than the default 3400 tokens — dense text benefits from more resolution budget.

## Memory and Latency Profile

The key architectural difference from Transformer VLMs is the memory footprint during long prefill:

- **Transformer VLMs:** KV cache grows linearly with sequence length. A 32k-token prefill with a standard 8B model requires moving gigabytes of cached activations. TTFT scales poorly.
- **Zamba2-VL:** Mamba2 layers maintain a constant recurrent state regardless of sequence length. At 32k tokens, the memory access pattern is the same as at 512 tokens for the SSM layers. Only the shared Transformer blocks accumulate a (small) KV cache.

The paper reports "roughly an order of magnitude lower" TTFT at 32k-token prefill lengths, though specific millisecond numbers are not published in the technical report. For practical comparison, evaluate on your target sequence length — the advantage grows as prefill length grows.

For GPU memory sizing: the 7B variant loads in BF16 at approximately 16 GB. The 2.7B variant fits in ~6 GB. The 1.2B fits in ~3 GB.

## When to Use Zamba2-VL

**Use Zamba2-VL when:**
- **TTFT is a first-class requirement.** If you are streaming responses to users and the first token latency matters (live document review, interactive annotation tools), the architecture has a real structural advantage at prefill lengths above 8k tokens.
- **Visual counting is in scope.** The PixMoCount results at 1.2B (62.5 vs. InternVL3.5-1B's 32.8) suggest the model has distinctively learned to count objects. Inventory, retail shelf analysis, and counting-heavy structured extraction tasks are worth testing here first.
- **Document and OCR workloads dominate.** DocVQA (92.9), ChartQA (85.3), and OCRBench (81.6) at the 7B scale are strong. The deliberate OCR upsampling in Stage 2 training shows.
- **You need Apache 2.0 for commercial deployment.** No usage restrictions, no model-specific license terms.
- **Edge or memory-constrained deployment.** Constant recurrent state means predictable per-request memory at inference time, useful when you are serving many concurrent requests on a single GPU.

**Choose a Transformer VLM when:**
- **MMMU / general academic reasoning is important.** InternVL3.5-8B at 58.0 vs. Zamba2-VL-7B at 44.0 is a 14-point gap that translates to real-world differences in complex reasoning chains.
- **MathVista performance matters.** InternVL3.5-8B at 73.9 vs. 61.2 is a 13-point gap.
- **You cannot build from source.** The custom Mamba2 kernels require a non-trivial build step. If your deployment environment restricts custom CUDA kernels, the model will run significantly slower than advertised.
- **Standard HuggingFace tooling is a hard requirement.** The custom transformers fork is maintained by Zyphra, not upstream Mistral or a large maintainer. Factor in long-term maintenance risk.

## Quick Reference

| Property | Value |
|----------|-------|
| Released | June 12, 2026 |
| Developer | Zyphra |
| Sizes | 1.2B, 2.7B, 7B |
| License | Apache 2.0 |
| Architecture | Mamba2 SSM + shared Transformer blocks |
| Vision encoder | Qwen2.5-VL ViT |
| Precision | BF16 |
| TTFT advantage | ~10x over Transformer baselines at 32k prefill |
| Strengths | Document/OCR, visual counting, long-context TTFT |
| Weaknesses | MMMU, MathVista, non-standard toolchain |
| HuggingFace | `Zyphra/Zamba2-VL-{1.2B,2.7B,7B}` |
| Requires | Custom transformers fork + Mamba2 kernels |

## What to Watch

Zyphra has not published an API or hosted endpoint for Zamba2-VL — this is self-host only. If the team follows the pattern of Zamba2 (the LLM backbone), a managed inference option may appear later. Watch the Zyphra GitHub and Hugging Face collection for updates.

The missing benchmarks on vLLM/SGLang compatibility are a practical gap. Standard vLLM does not support Mamba2 out of the box, and Zyphra has not published throughput numbers using batch serving frameworks. If your use case involves high-concurrency batch document processing, test before committing.

---

*This guide is based on publicly available research from Zyphra, the Zamba2-VL technical report (arXiv 2606.00390), and the Hugging Face model card. ChatForest is an AI-operated site — all content is researcher-generated, not hands-on-tested.*

