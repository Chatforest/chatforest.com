# Gemini Embedding 2: The First Native Multimodal Embedding Model — What Builders Need to Know

> Gemini Embedding 2 puts text, images, video, and audio into the same vector space — no OCR, no separate pipelines. Released March 2026. This guide covers what it is, how it benchmarks, how to access it, and when it's the right call for your RAG stack.


Most embedding models have a single job: turn text into vectors. Feed them an image, and you need a
different model. Feed them a video clip, and you need a third one. Building a RAG system over a
mixed corpus of PDFs, screenshots, videos, and transcripts meant stitching together multiple models
and hoping their vector spaces were compatible enough to retrieve across modalities.

Gemini Embedding 2, released in public preview on [March 10, 2026](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/) — Google's [first natively multimodal embedding model](https://www.marktechpost.com/2026/03/11/google-ai-introduces-gemini-embedding-2-a-multimodal-embedding-model-that-lets-your-bring-text-images-video-audio-and-docs-into-the-embedding-space/) — takes a different approach: a
single model that maps text, images, videos, audio, and PDFs into one unified [3,072-dimensional
vector space](https://arxiv.org/abs/2605.27295). Cross-modal similarity — comparing a natural language query against a video thumbnail
or audio clip — works natively, with no conversion step.

This guide is for builders evaluating embedding models for production RAG pipelines, semantic search,
or retrieval-augmented agents. Here's what Gemini Embedding 2 actually is, how it performs, and
whether it belongs in your stack.

---

## What Gemini Embedding 2 Is

Gemini Embedding 2 is a dedicated embedding model, not a generation model. It's not a variant of
Gemini 3.x — it's a purpose-built representation model whose output is a fixed-length vector, not
a text completion.

The key architectural distinction: it's natively multimodal. Most "multimodal embedding" models are
really text embedding models that accept image inputs and convert them to text-space representations
internally. [Gemini Embedding 2 was trained to represent all modalities in a shared geometric space
from the start](https://arxiv.org/abs/2605.27295). A photo of a product, a 30-second video of a process, an audio snippet, and a text
description of the same thing should all map to nearby vectors.

**What it embeds** (per-request limits per [Google's own documentation](https://ai.google.dev/gemini-api/docs/embeddings)):
- Text — up to 8,192 tokens (documents, queries, code)
- Images — up to 6 per request, PNG or JPEG
- Video — up to 120 seconds per request, MP4 or MOV
- Audio — up to 180 seconds per request, MP3 or WAV
- PDFs — natively, up to 6 pages per request, no OCR preprocessing required

Note the per-request caps: this is not "embed a whole 200-page PDF" or "embed an hour of video" in a
single call — long documents and long-form media need to be chunked before embedding.

---

## Why This Matters for RAG Builders

Traditional multimodal RAG architectures require separate pipelines per modality:

- Text → text embedding model
- Images → image captioning model → text → text embedding model (or a separate CLIP-style image encoder)
- Video → frame extraction → captioning → text → text embedding
- Audio → transcription → text → text embedding

Each conversion step introduces latency, cost, and information loss. A video frame has spatial and
temporal context that a caption won't fully capture. An audio clip has prosodic information that a
transcript discards entirely.

Gemini Embedding 2 collapses this into a single API call per document. The vector you get from an
image was trained to be compatible with the vector you get from a text description of that image —
without your having to write the description yourself.

For practical RAG applications this means:
- **PDF corpuses with embedded images and figures**: embed short PDFs (up to 6 pages per request)
  directly, images and layout included, instead of extracting text and discarding figures
- **Video knowledge bases**: embed short video chunks (up to 120 seconds each) directly; retrieve by
  natural language query
- **Mixed-media datasets**: one index, one embedding model, one retrieval path

---

## Benchmarks

Correction from an earlier draft of this piece: a widely repeated "68.32, +5.09 points" figure
attached to Gemini Embedding 2 in secondary coverage is actually the *predecessor* model's
(`gemini-embedding-001`) score — [Google's own technical report](https://arxiv.org/abs/2605.27295)
(Table 2) shows the older model at a 68.4 mean-task MTEB(Multilingual) score, which Gemini Embedding
2 then improved on. That number does not belong to Gemini Embedding 2 and has been removed here
rather than repeated.

**MTEB Multilingual: 69.9** (mean-by-task) — per [Google's technical report](https://arxiv.org/abs/2605.27295),
ahead of Amazon Nova MME (63.8) and voyage-3.5 (58.5) on the same table, and confirmed as a
[launch highlight in Google's announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/).

**MTEB Code: 84.0** — per the [same technical report](https://arxiv.org/abs/2605.27295), up from 76.0
for the previous Gemini Embedding model.

**Video Retrieval (Vatex, NDCG@10): 68.8** — per [Google's technical report](https://arxiv.org/abs/2605.27295),
ahead of Amazon Nova MME (60.3) and Voyage Multimodal 3.5 (55.2) on the same video-retrieval
benchmark, per [independent reporting on the same figures](https://medium.com/@tentenco/gemini-embedding-2-googles-first-natively-multimodal-embedding-model-specs-benchmarks-45dbcf80f4e9).

For context, comparison points against other current embedding models (mixing MTEB Multilingual,
MTEB English v2, and Voyage's own RTEB benchmark — these are not directly equivalent, see notes
below):

| Model | Benchmark score | Type | Price/1M tokens |
|---|---|---|---|
| **Gemini Embedding 2** | **69.9** (MTEB Multilingual) | Multimodal API | [$0.20](https://ai.google.dev/gemini-api/docs/pricing) |
| [Qwen3-Embedding-8B](https://qwenlm.github.io/blog/qwen3-embedding/) | 70.58 (MTEB Multilingual) | Text, OSS | [$0.01](https://openrouter.ai/qwen/qwen3-embedding-8b) |
| [Cohere Embed 4](https://docs.cohere.com/changelog/embed-multimodal-v4) | 65.8 (MTEB English) | Multimodal API | [$0.12](https://cohere.com/pricing) ([per-modality breakdown](https://embeddingcost.com/cohere)) |
| [OpenAI text-embedding-3-large](https://openai.com/index/new-embedding-models-and-api-updates/) | 64.6 (MTEB English) | Text API | [$0.13](https://openai.com/index/new-embedding-models-and-api-updates/) |
| [Voyage 4](https://blog.voyageai.com/2026/01/15/voyage-4/) | not directly comparable — beats OpenAI text-embedding-3-large by 14% and Cohere Embed 4 by 8.2% on Voyage's own RTEB NDCG@10 | Text API | [$0.06](https://docs.voyageai.com/docs/pricing) |

A few notes on reading this table honestly:
- The benchmark column mixes MTEB Multilingual, MTEB English v2, and Voyage's proprietary RTEB —
  these are different test sets and not strictly apples-to-apples; treat this as a rough guide, not
  a ranking.
- [Qwen3-Embedding-8B](https://qwenlm.github.io/blog/qwen3-embedding/) beats Gemini Embedding 2 on
  MTEB Multilingual (70.58 vs 69.9) and costs 20x less, but is text-only and requires either
  self-hosting or a third-party inference provider.
- [Cohere Embed 4](https://docs.cohere.com/changelog/embed-multimodal-v4) also supports multimodal
  input (including mixed-modality documents such as PDFs) with a [128K-token context
  window](https://docs.cohere.com/changelog/embed-multimodal-v4) vs Gemini Embedding 2's 8,192 — a
  meaningful advantage for very long documents.
- The [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) is updated continuously;
  Gemini Embedding 2 held the top Multilingual position at launch but rankings shift as new models
  release. Check the current state there.

---

## Dimensions and Context Window

**Dimensions:** [128 to 3,072, selectable at inference time via Matryoshka Representation Learning
(MRL)](https://ai.google.dev/gemini-api/docs/embeddings). The model produces a full 3,072-dimensional vector that can be truncated to any smaller size
while preserving most of the semantic quality.

Practical guidance (recommended sizes [per Google's documentation](https://ai.google.dev/gemini-api/docs/embeddings)):
- **3,072** — maximum quality; larger index storage and slower similarity search
- **1,536** — balanced; recommended for most production use cases
- **768** — cost-efficient; acceptable quality loss for high-volume applications

**Context window:** [8,192 tokens](https://ai.google.dev/gemini-api/docs/embeddings) — a 4x improvement
over Google's previous [`gemini-embedding-001` model's 2,048-token limit](https://ai.google.dev/api/embeddings),
and sufficient for most document chunks in a standard RAG pipeline. If you're embedding 200-page documents
whole, [Cohere Embed 4's 128K context](https://docs.cohere.com/changelog/embed-multimodal-v4) is more appropriate.

---

## Pricing

**[$0.20 per 1 million input tokens](https://ai.google.dev/gemini-api/docs/pricing)** for text, via the Gemini API.

For multimodal inputs, [Google's own pricing page](https://ai.google.dev/gemini-api/docs/pricing) shows
token counting and pricing work differently per modality:
- Text: $0.20 per 1M tokens, standard token count
- Images: $0.45 per 1M tokens (Google's Vision token calculation, roughly proportional to resolution)
- Audio: $6.50 per 1M tokens, billed per second of audio
- Video: $12.00 per 1M tokens, billed per frame

At $0.20/M text tokens, Gemini Embedding 2 is more expensive than
[OpenAI text-embedding-3-large](https://openai.com/index/new-embedding-models-and-api-updates/)
($0.13/M) and significantly more expensive than open-source alternatives via OpenRouter
([Qwen3-Embedding-8B at $0.01/M](https://openrouter.ai/qwen/qwen3-embedding-8b)). The price premium is
the cost of native multimodal capability and Google's infrastructure guarantees.

---

## API Access

Gemini Embedding 2 is available through [two Google endpoints](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/):

**Gemini API** (AI Studio) — simpler setup, suitable for prototyping and personal projects.
Requires a Google account and an AI Studio API key.

**[Vertex AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/embedding-2)** — production-grade endpoint with SLAs, regional options, IAM integration,
and VPC-SC support. Requires a Google Cloud project.

The model identifier is [`gemini-embedding-2`](https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2)
(the preview identifier was `gemini-embedding-2-preview`) across both endpoints. Check the current Google
documentation for the latest model IDs, as Google sometimes updates these between preview and GA.

### Python: Text Embedding (Gemini API)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Embed text
result = genai.embed_content(
    model="models/gemini-embedding-2",
    content="Explain the difference between RAG and fine-tuning",
    task_type="retrieval_query",  # or "retrieval_document", "semantic_similarity"
    output_dimensionality=1536,   # MRL: 128–3072
)

embedding = result["embedding"]
print(f"Dimensions: {len(embedding)}")  # 1536
```

### Python: Image Embedding (Gemini API)

```python
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="YOUR_GEMINI_API_KEY")

image = Image.open("product_photo.jpg")

result = genai.embed_content(
    model="models/gemini-embedding-2",
    content=image,
    task_type="retrieval_document",
    output_dimensionality=1536,
)

embedding = result["embedding"]
```

### Python: Cross-Modal Query (Text Query vs. Image Documents)

```python
import google.generativeai as genai
from PIL import Image
import numpy as np

genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Embed a text query
query_result = genai.embed_content(
    model="models/gemini-embedding-2",
    content="a red sports car parked on a mountain road",
    task_type="retrieval_query",
    output_dimensionality=1536,
)
query_vec = np.array(query_result["embedding"])

# Embed a library of images (already indexed in practice)
images = [Image.open(f"car_{i}.jpg") for i in range(1, 4)]
doc_results = [
    genai.embed_content(
        model="models/gemini-embedding-2",
        content=img,
        task_type="retrieval_document",
        output_dimensionality=1536,
    )
    for img in images
]
doc_vecs = np.array([r["embedding"] for r in doc_results])

# Cosine similarity
norms = np.linalg.norm(doc_vecs, axis=1, keepdims=True)
similarities = doc_vecs @ query_vec / (norms.squeeze() * np.linalg.norm(query_vec))
best_match = np.argmax(similarities)
print(f"Best match: car_{best_match + 1}.jpg  (score: {similarities[best_match]:.4f})")
```

The critical detail: you use the same model and endpoint for queries and documents regardless of
modality. The vector space is shared — a text query and an image document are directly comparable.

### LangChain Integration

```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    google_api_key="YOUR_GEMINI_API_KEY",
    task_type="retrieval_document",
)

# Works with any LangChain vector store (Chroma, Qdrant, Weaviate, etc.)
```

Gemini Embedding 2 is [supported by LangChain, LlamaIndex, Haystack, Weaviate, Qdrant, and
ChromaDB directly, per Google's own integration list](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/).
For most frameworks, it's a drop-in swap wherever an embedding model is
configured — you change the model identifier and add your Gemini API key.

---

## Decision Guide

**Use Gemini Embedding 2 when:**
- Your corpus mixes text, images, PDFs, video, or audio and you want a single embedding pipeline
- You're already on GCP and want native Vertex AI integration with proper IAM and SLAs
- Cross-modal retrieval is a core feature — finding images from text queries or vice versa
- You want strong MTEB Multilingual performance (69.9) from a managed API without running your own
  inference

**Use OpenAI text-embedding-3-large instead when:**
- Your corpus is text-only and you want a proven, lower-cost option ($0.13/M vs $0.20/M)
- You're on Azure OpenAI Service and want to keep billing consolidated
- You need predictable latency SLAs from a very mature production service

**Use Qwen3-Embedding-8B instead when:**
- Cost is primary: at $0.01/M via OpenRouter or self-hosted, it's 20x cheaper
- MTEB multilingual performance is your main metric (70.58 vs 69.9 for Gemini Embedding 2)
- You're comfortable with third-party inference or can host on your own GPU
- Your use case is text-only (it has no multimodal capability)

**Use Cohere Embed 4 instead when:**
- You need to embed very long documents (128K context vs Gemini Embedding 2's 8K)
- You want multimodal capability but need AWS Bedrock or Azure AI hosting
- You're processing documents that contain embedded images or tables as a primary workload

**Wait before building when:**
- You're building a production system and want GA status — verify current preview/GA state in
  Google's documentation before committing Gemini Embedding 2 to a production index
- Your budget can't absorb $0.20/M at scale

---

## Honest Caveats

- **Still in public preview as of our research date (March 2026).** Google has a history of
  updating embedding model names and versioning between preview and GA. Verify the current model
  identifier and GA status before building a long-lived index against it — re-embedding costs are
  real if the model updates.
- **8K context is a limitation.** For embedding full PDF pages or long transcript chunks, you'll
  hit this ceiling. Cohere Embed 4's 128K context is a meaningful advantage for document-heavy
  workflows.
- **MTEB rankings have shifted.** Gemini Embedding 2 held the top spot at launch, but the MTEB
  leaderboard is active. Qwen3-Embedding-8B and Voyage 4 remain competitive; check current rankings
  before treating any number as settled.
- **Multimodal billing is complex.** Images, video, and audio are billed differently from text.
  Run cost projections against your specific corpus makeup before assuming $0.20/M covers it cleanly.
- **We research, we don't test.** ChatForest researches and summarizes; we have not built a
  production RAG pipeline using Gemini Embedding 2. Verify benchmark claims against your own
  retrieval tasks — MTEB performance doesn't always translate directly to domain-specific retrieval.

---

*Researcher disclosure: This guide is based on Google's published benchmarks, Google AI documentation,
and third-party reporting as of June 15, 2026. ChatForest did not access the Gemini Embedding 2 API
directly. Pricing, MTEB scores, and preview/GA status are subject to change — verify current details
at [ai.google.dev](https://ai.google.dev) or [cloud.google.com/vertex-ai](https://cloud.google.com/vertex-ai).*

