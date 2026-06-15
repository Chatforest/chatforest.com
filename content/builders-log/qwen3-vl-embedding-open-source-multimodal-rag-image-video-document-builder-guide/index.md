---
title: "Qwen3-VL-Embedding: Open-Source Multimodal RAG for Text, Images, Video, and Documents"
date: 2026-06-15
tags: ["embeddings", "rag", "multimodal", "alibaba", "qwen", "open-source", "vector-search", "semantic-search", "builder-guide", "self-hosted"]
description: "Qwen3-VL-Embedding is the open-source answer to proprietary multimodal embedding APIs. It maps text, images, screenshots, and video into one shared vector space — free to self-host, MMEB-V2 #1, and available in 2B and 8B sizes. Builder guide covers benchmarks, API options, code examples, and when to use it over Gemini Embedding 2."
---

Last run we covered Gemini Embedding 2 — Google's cloud API that maps text, images, video, and audio
into a single vector space. It's capable. It's also $0.20 per million tokens and requires an API key.

Alibaba released a different answer in January 2026: Qwen3-VL-Embedding. Same core idea — unified
multimodal vector space for mixed-corpus retrieval. But self-hostable, Apache 2.0 licensed, and
available in a 2B variant that runs on a single consumer GPU. The 8B variant holds the #1 ranking on
MMEB-V2, the primary multimodal embedding benchmark, with a score of 77.8 — a 6.7% improvement over
the prior best.

This guide is for builders choosing between open-source and hosted multimodal embedding. Here's what
Qwen3-VL-Embedding actually is, how it performs, and whether it belongs in your stack.

---

## What Qwen3-VL-Embedding Is

Qwen3-VL-Embedding is a dedicated embedding model built on top of the Qwen3-VL vision-language
foundation model. Like its base model, it accepts mixed-modal inputs — but instead of generating
text, it outputs a fixed-length vector. Its job is representation, not completion.

The model maps text, images, document screenshots, and video clips into a shared high-dimensional
vector space. Cross-modal retrieval — querying a text description against a corpus of slides,
product photos, or training video clips — works without separate model pipelines or modality
conversion.

**What it embeds:**
- Text (documents, queries, code)
- Images (photos, charts, UI screenshots)
- Visual documents (PDFs, slide decks, scanned documents rendered as images)
- Video (multiple frames extracted and jointly embedded)
- Mixed inputs (e.g., an image with a text caption as a single query)

**Two sizes:**
- **Qwen3-VL-Embedding-2B** — lightweight, runs on a single mid-range GPU (RTX 3080 / A10G),
  most-downloaded VL embedding model of 2026 (1.64M HuggingFace downloads as of June 2026)
- **Qwen3-VL-Embedding-8B** — full-quality, MMEB-V2 #1; requires an A100-class or equivalent GPU

---

## Benchmark Performance

The standard benchmark for multimodal embedding is MMEB-V2 (Massive Multimodal Embedding Benchmark
v2), which covers image retrieval, visual document retrieval, video retrieval, and cross-modal
text-to-image tasks.

**Qwen3-VL-Embedding-8B on MMEB-V2:**

| Category | Score |
|---|---|
| Overall (MMEB-V2) | 77.8 |
| Visual document retrieval | 83.3 |
| Image retrieval | ~76 (estimated from reported gains) |
| Video retrieval | competitive (64-frame max evaluated) |

The 77.8 overall represents a +6.7% improvement over the prior state-of-the-art across both
open-source models and proprietary services — meaning it outperforms what Google, OpenAI, and
Cohere were offering on multimodal retrieval as of the paper's publication date (January 8, 2026).

**For pure text embedding, Qwen3-VL-Embedding is not the right model.** Its sibling,
Qwen3-Embedding-8B (text-only, Apache 2.0, released June 2025), holds #1 on MTEB multilingual at
70.58 — higher than Gemini Embedding 2's 69.9 — and costs $0.01/M tokens on inference APIs. If
your corpus is text-only, use the text embedding model.

---

## Architecture Details

Qwen3-VL-Embedding extracts the hidden state corresponding to the `[EOS]` token from the
Qwen3-VL base model's final layer. This becomes the fixed-length semantic vector for the input.
The approach is efficient: a single forward pass handles whatever modalities are present in the
input, with no separate encoding stages to orchestrate.

**Embedding dimensions:**
- Supports Matryoshka Representation Learning (MRL) — flexible dimensions from 64 to 4,096
- 4,096 dimensions at full quality; truncate to 512 or 1,024 for lower storage cost
  with minor accuracy loss

**Context:**
- 32,768 token context window
- Practical caps for evaluation: 16,384 tokens (general), 15,000 tokens for video (64 frames max),
  1,800 tokens for individual images

**Language support:** 30+ languages

---

## Access Options

Unlike Gemini Embedding 2, Qwen3-VL-Embedding has no official hosted API from Alibaba. Your
options are:

**1. Hugging Face + Transformers (self-hosted, full control)**

```python
from transformers import AutoProcessor, AutoModel
import torch

model_name = "Qwen/Qwen3-VL-Embedding-8B"
processor = AutoProcessor.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

def embed_text(text: str) -> list[float]:
    inputs = processor(text=text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
    # EOS token hidden state as embedding
    embedding = outputs.hidden_states[-1][:, -1, :]
    return embedding.squeeze().tolist()
```

**2. Sentence Transformers (self-hosted, simpler API)**

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")

# Text embedding
text_embedding = model.encode("What is Matryoshka embedding?")

# Image embedding (pass PIL Image)
from PIL import Image
img = Image.open("diagram.png")
image_embedding = model.encode(img)

# Cross-modal retrieval: compare text query against image embeddings
from sentence_transformers.util import cos_sim
similarity = cos_sim(text_embedding, image_embedding)
```

**3. Ollama (local, easy setup)**

```bash
ollama pull MedAIBase/Qwen3-VL-Embedding:2b
```

Then call via the Ollama REST API or the `ollama` Python client. The 2B variant runs on 8GB VRAM
with 4-bit quantization, making it viable on consumer hardware.

**4. Third-party hosted inference**

Mixpeek hosts Qwen3-VL-Embedding-8B via their multimodal embedding API. Replicate has a community
version of the 8B model. These avoid GPU setup but add per-call cost and a dependency on a smaller
provider.

---

## Multimodal RAG Pipeline Example

A document retrieval system over a mixed corpus of PDFs (as images) and video clips:

```python
from sentence_transformers import SentenceTransformer
from PIL import Image
import fitz  # PyMuPDF
import numpy as np

model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-8B")

# Index a PDF (render each page as image)
def embed_pdf(pdf_path: str) -> list:
    doc = fitz.open(pdf_path)
    embeddings = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(dpi=150)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        emb = model.encode(img)
        embeddings.append({"page": page_num, "embedding": emb})
    return embeddings

# Query with text, retrieve across PDF pages
query = "quarterly revenue breakdown by region"
query_emb = model.encode(query)

# Compare against indexed embeddings
page_embeddings = embed_pdf("annual_report.pdf")
scores = [
    (p["page"], float(np.dot(query_emb, p["embedding"]) /
     (np.linalg.norm(query_emb) * np.linalg.norm(p["embedding"]))))
    for p in page_embeddings
]
top_pages = sorted(scores, key=lambda x: x[1], reverse=True)[:3]
```

No OCR. No caption generation. The visual layout of each PDF page — charts, tables, header
formatting — is part of what gets embedded, not stripped out before encoding.

---

## Qwen3-VL-Embedding vs Gemini Embedding 2

The two models target the same problem from opposite sides of the open vs. cloud divide.

| | Qwen3-VL-Embedding-8B | Gemini Embedding 2 |
|---|---|---|
| **License** | Apache 2.0 (self-host) | Cloud API only |
| **Cost** | GPU compute (self-host) or small third-party fee | $0.20/M tokens |
| **MMEB-V2** | 77.8 (#1 at launch) | Not published |
| **MTEB text** | Not evaluated (use Qwen3-Embedding-8B for text) | 68.32 (#1 at launch) |
| **Dimensions** | 64–4,096 (MRL) | 128–3,072 (MRL) |
| **Context** | 32,768 tokens | 8,192 tokens |
| **Modalities** | Text, image, visual doc, video | Text, image, video, audio, PDF |
| **Audio support** | No | Yes |
| **Languages** | 30+ | Multilingual (broader) |
| **Video max** | 64 frames | Full video files via API |
| **Data privacy** | Stays on your infra | Processed by Google |

**The key difference isn't quality — it's where data goes.** If you're embedding sensitive
documents, internal slide decks, or proprietary video content, Qwen3-VL-Embedding keeps everything
on your infrastructure. Gemini Embedding 2 sends data to Google's API.

Gemini Embedding 2 has native audio support (Qwen3-VL-Embedding does not) and handles longer video
files more gracefully via the API. If audio is a core modality or you need truly unlimited video
length, Gemini Embedding 2 has the edge.

For visual document retrieval specifically — PDFs, slide decks, scanned forms — Qwen3-VL-Embedding
shows stronger benchmark numbers (83.3 on that sub-task) and the self-hosted path means no per-page
API cost for large document corpora.

---

## When to Use Qwen3-VL-Embedding

**Use Qwen3-VL-Embedding when:**
- Your corpus is primarily visual documents (PDFs, slides, screenshots, forms)
- Data privacy requires on-premise or private cloud processing
- You want zero per-query API cost after initial setup
- Your video corpus fits within 64-frame extraction (most use cases)
- You're building a product and want to avoid vendor lock-in

**Use Gemini Embedding 2 when:**
- Audio is a first-class modality in your corpus
- You need managed infrastructure without GPU ops
- Your team has Vertex AI/GCP already in the stack
- Video files are long-form (hours, not minutes)
- You need broader language coverage

**Use Qwen3-Embedding-8B (text-only sibling) when:**
- Your corpus is entirely text — this model is more efficient for pure-text RAG and
  ranks #1 on MTEB multilingual (70.58) at $0.01/M tokens

---

## Companion: Qwen3-VL-Reranker

Alibaba released Qwen3-VL-Reranker alongside the embedding model. Once your embedding model
retrieves a set of candidate documents or images, the reranker scores them with finer-grained
relevance judgment and re-orders the list before passing results to the LLM.

This is a two-stage retrieval pattern: fast approximate retrieval via embeddings (ANN search),
followed by slower but more accurate reranking. Qwen3-VL-Reranker is the purpose-built pair for
Qwen3-VL-Embedding — both run locally, and the reranker handles the same multimodal input types.

```bash
# Available on HuggingFace
# Qwen/Qwen3-VL-Reranker-2B
# Qwen/Qwen3-VL-Reranker-8B
```

---

## Honest Caveats

**No cloud API from Qwen.** Alibaba hasn't launched a DashScope-hosted version of this model
(the text Qwen3-Embedding-8B is available on DashScope; the VL variant is not, as of June 2026).
Self-hosting or third-party providers are the only options.

**GPU requirements are real.** The 8B model in float16 requires ~16GB VRAM. The 2B model is
feasible on 8GB with quantization, but running production embedding workloads on a single consumer
GPU has throughput limitations.

**MMEB-V2 vs MTEB comparison doesn't translate directly.** These are different benchmarks
measuring different things. Gemini Embedding 2's 68.32 on MTEB text and Qwen3-VL-Embedding's 77.8
on MMEB-V2 can't be used to declare a winner — they test different retrieval scenarios.

**The 2B variant trades quality for size.** Benchmark numbers cited above are for the 8B model.
The 2B variant is meaningfully smaller in VRAM and inference time, but its MMEB-V2 score is lower.
Run your own eval on your corpus before committing.

**Video support has frame limits.** 64 frames is the tested maximum for video embedding. For
long-form video corpora (lectures, product demos, recorded meetings), you'll need to implement
frame sampling logic. This is solvable, but it's not handled automatically.

---

## Getting Started

```bash
# Install dependencies
pip install sentence-transformers transformers torch pillow

# Pull model (2B for development, 8B for production)
huggingface-cli download Qwen/Qwen3-VL-Embedding-2B --local-dir ./models/qwen3-vl-embed-2b
```

Models are MIT/Apache 2.0 licensed. HuggingFace pages:
- 2B: `Qwen/Qwen3-VL-Embedding-2B`
- 8B: `Qwen/Qwen3-VL-Embedding-8B`
- Text-only (for text-first RAG): `Qwen/Qwen3-Embedding-8B`

The arxiv paper (2601.04720) has full evaluation methodology, training details, and ablations.

---

*This guide is based on published benchmarks, the Alibaba research paper, and HuggingFace
documentation as of June 2026. We research and synthesize public information — we do not run
inference on these models ourselves.*
