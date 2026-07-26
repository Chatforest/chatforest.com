# RAG Best Practices — Python Ecosystem (LangChain, LlamaIndex, Haystack) (as of 22 Jul 2026) — Beginner Edition

> Plain-English guide to building RAG systems in Python — chunking, hybrid retrieval, vector stores, streaming, evaluation, and security. Beginner-friendly re-leveling of the 2026-07-22 technical entry. Accurate as of 22 Jul 2026.


<!-- This file lands at content/ai/beginner/python-rag-best-practices/2026-07-22/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW snapshot-date dir.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# RAG Best Practices — Python Ecosystem (Beginner Edition) (as of 22 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **22 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

---

## What is RAG, and why should you care?

**RAG** stands for **Retrieval-Augmented Generation**. That is a mouthful, so here is what it means in plain terms:

Imagine you ask a very well-read friend a question. Normally, they answer from memory. With RAG, before answering, they first look up the most relevant pages in a specific book you hand them — and then give you an answer based on what they read just now. The "friend" is an AI language model (LLM — Large Language Model). The "book" is your private collection of documents. RAG lets the AI answer questions about documents it was never trained on.

**Why use RAG instead of just asking the AI?**
A general AI has no knowledge of your internal company documents, your product manuals, or anything private. RAG bridges that gap without re-training the AI from scratch.

**Two terms you will see everywhere in this guide:**

- **Embedding** — A list of numbers that captures the meaning of a piece of text. Two pieces of text with similar meanings will have similar number-lists. This is what allows the system to find relevant documents by meaning, not just by keyword matching.
- **Vector store** (also called a vector database) — A specialized database that stores those number-lists and can search them very quickly. Think of it as a library catalog organized by meaning rather than by alphabet.

---

## Before you start — what you need (and what it might cost)

**Technical prerequisites:** Python 3.10 or newer, the `pip` package manager (or `uv`), an API key from an AI provider such as OpenAI or Anthropic with a payment method on file, and a running vector store (Practice 5 explains your options).

⚠️ **Cost warning:** Running automated quality evaluations (see Practice 8) calls an AI API once for every test question. A set of 200 test questions can cost $0.20 to $5.00 per evaluation run, depending on which AI model you use. This adds up quickly if you run evaluations carelessly. Keep your test sets small until you understand your costs.

⚠️ **Privacy warning: read Practices 10 and 11 before you load any documents.** Once personal information is embedded in a vector store, it can be retrieved by anyone with search access. Do not index private or sensitive data until you have access controls in place.

---

## Package versions used in this guide (check these before you start) 🕒

This guide was written on 2026-07-22. Package versions change. Before installing, verify you are getting what you expect by checking the PyPI pages linked below.

| Package | Version as of 2026-07-22 | Where to verify |
|---|---|---|
| `langchain-core` | **1.5.0** (released 2026-07-21) | [pypi.org/project/langchain-core](https://pypi.org/project/langchain-core/) |
| `langchain` | **1.3.14** (released 2026-07-16) | [pypi.org/project/langchain](https://pypi.org/project/langchain/) |
| `langchain-community` | **SUNSET** — repo archived 2026-06-19; do not use (see Practice 1) | [github.com/langchain-ai/langchain-community](https://github.com/langchain-ai/langchain-community) |
| `llama-index-core` | **0.14.23** (released 2026-06-24) | [pypi.org/project/llama-index-core](https://pypi.org/project/llama-index-core/) |
| `haystack-ai` | **3.0.0** (released 2026-07-20) | [pypi.org/project/haystack-ai](https://pypi.org/project/haystack-ai/) |

---

## How to read the labels

- ✅ **independently-corroborated** — 2+ independent publishers confirmed this
- 📄 **vendor-documented** — from official vendor documentation (authoritative but a single source)
- ⚠️ **WARNING** — a default that can cost money, break your system, or remove a safety net
- 🕒 **verify live** — this information changes fast (versions, prices, quotas); check it before you rely on it

---

## Practice 1: Stop importing from `langchain-community` — switch to standalone packages

### What is `langchain-community` and why does it matter?

`langchain-community` was a single Python package that bundled hundreds of connectors to third-party tools (databases, vector stores, APIs, and more) all in one place. It was convenient, but it became too large to maintain. The maintainers archived (froze) the repository on 2026-06-19 — it is now read-only. No bug fixes. No security patches. Ever again.

If your code still imports from it, you are building on a foundation that will eventually crack.

### How to check if you are affected

Run this command in your terminal:

```
pip show langchain-community
```

If you see a version number printed, you are affected and need to migrate. If you see "WARNING: Package(s) not found", you are fine.

### What to do instead

Each connector now lives in its own dedicated package. Replace your old import with the new one. For example:

| Old import (do not use) | New package to install | New import |
|---|---|---|
| `from langchain_community.vectorstores import Chroma` | `pip install langchain-chroma` | `from langchain_chroma import Chroma` |
| `from langchain_community.vectorstores import Qdrant` | `pip install langchain-qdrant` | `from langchain_qdrant import Qdrant` |
| `from langchain_community.chat_models import ChatOpenAI` | `pip install langchain-openai` | `from langchain_openai import ChatOpenAI` |

For a full list of current package names, visit the [LangChain integrations page](https://docs.langchain.com/oss/python/integrations/providers/overview).

**Why this matters for beginners:** Code that still imports from `langchain-community` will break when you update Python or other dependencies. You will get confusing error messages that are hard to debug. Migrating now prevents a painful surprise later.

**One thing to watch:** The new standalone packages are maintained by different people (the connector vendor or community volunteers). Quality varies. Before adopting a new package, glance at its GitHub repository to see if it has been active recently.

**Sources:** [github.com/langchain-ai/langchain-community](https://github.com/langchain-ai/langchain-community) (archived 2026-06-19) · [LangChain forum: migration guidance](https://forum.langchain.com/t/recommended-migration-path-for-tools-and-integrations-following-the-langchain-community-sunset/3934) (2026) · [github.com/langchain-ai/langchain-community/issues/674](https://github.com/langchain-ai/langchain-community/issues/674) (2026-06-19)

**Confidence:** ✅ independently-corroborated (LangChain official repo + LangChain community forum, two different publisher surfaces) 🕒 verify live

---

## Practice 2: Split your documents into chunks of 400–512 tokens with 10–20% overlap

### What is "chunking" and why do you have to do it?

An AI language model can only read a limited amount of text at once. You cannot feed it an entire 500-page manual and ask a question. You have to cut the manual into smaller pieces — called **chunks** — and then find and send only the most relevant pieces.

**Token** is the unit of text that AI models count. Roughly 100 tokens is about 75 words or half a page of plain text.

**Overlap** means that each chunk shares some text with the chunk before it. This prevents important sentences from being cut in half across two chunks, losing their meaning.

### The recommended starting point

Use `RecursiveCharacterTextSplitter` with a chunk size of 512 tokens and an overlap of 51 tokens (which is about 10%). This splitter is smart about where it cuts: it prefers to cut at paragraph breaks first, then line breaks, then sentence boundaries, then word boundaries — so it avoids cutting in the middle of a sentence.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
# NOTE: do NOT use `from langchain.text_splitter` — that import path is deprecated

splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=51)
```

**Why this matters for beginners:**
- Chunks that are too small lose their surrounding context — the AI cannot understand what the chunk is about.
- Chunks that are too large flood the AI with irrelevant text and waste money (you pay per token).
- The 512-token / 51-token-overlap setting is a broadly recommended starting point, not a proven perfect answer. Once you have evaluation metrics running (see Practice 8), you can tune it for your specific documents.

**Things to keep in mind:**
- For simple factoid questions ("What is the boiling point of water?"), smaller chunks around 256 tokens often work better.
- For complex analytical questions, larger chunks around 1,024 tokens give the AI more context.
- If your documents are scanned PDFs with poor quality (blurry, rotated, handwritten), no chunking strategy will help — you need to fix the document parser first (see Practice 9).
- One study from NVIDIA found that for PDF documents, keeping chunks aligned to page boundaries worked best. The 400–512 token recommendation comes from practitioner experience, not a single definitive study — treat it as a starting point.

**Sources:** [firecrawl.dev/blog/best-chunking-strategies-rag](https://www.firecrawl.dev/blog/best-chunking-strategies-rag) (2026) · [redis.io/blog/rag-at-scale](https://redis.io/blog/rag-at-scale/) (pub. 2026-01-21, updated 2026-05-21)

**Confidence:** ✅ independently-corroborated

---

## Practice 3: Use hybrid retrieval (keyword search + vector search) — not vector search alone

> ⚠️ **HAYSTACK 3.0.0 BREAKING CHANGES (released 2026-07-20 — 2 days before this snapshot)**
>
> The Haystack code examples in this practice were written for Haystack 2.x. Haystack 3.0.0 introduced major breaking changes:
> - `AsyncPipeline` removed; a unified `Pipeline` class now has both sync and async `run()` methods
> - `OpenAIGenerator`, `AzureOpenAIGenerator`, `HuggingFaceAPIGenerator`, `HuggingFaceLocalGenerator` removed entirely — Chat Generators replace them
> - `SentenceTransformersSimilarityRanker` moved to `haystack-core-integrations` (separate package)
> - `PromptBuilder` and `ChatPromptBuilder` now treat Jinja2 template variables as required by default
> - Pipeline deserialization blocks unsafe imports by default
>
> **Before running the Haystack code below, verify it against the 3.0.0 release notes at [haystack.deepset.ai/release-notes/3.0.0](https://haystack.deepset.ai/release-notes/3.0.0).** This practice is marked ⚠️ PENDING full 3.0.0 migration verification.

### Two ways to search — and why you need both

**Vector search** (also called dense retrieval) finds documents by meaning. Ask "what is the capital of France?" and it finds documents about Paris even if they never say "capital."

**Keyword search** (also called BM25 or sparse retrieval) finds documents by exact word matches. Ask for "ISO 9001:2015 clause 4.3" and it finds documents containing exactly that code.

**The problem:** Each method fails at what the other does well. A product code like "SKU-78234" or a legal citation like "Section 230" will get buried or missed by pure vector search — but keyword search will find it instantly.

**Hybrid retrieval** runs both searches and combines the results. A technique called Reciprocal Rank Fusion (RRF) merges the two ranked lists into one. This is the production-ready approach.

### What you need first

```
pip install rank_bm25
```

BM25 is not built into LangChain — this separate package provides it.

### How to set it up in LangChain

```python
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever  # NOTE: langchain-community is sunset as of 2026-06-19
# Alternative: use the standalone rank_bm25 package directly — see Practice 1 for migration guidance

retriever = EnsembleRetriever(retrievers=[bm25_retriever, vector_retriever], weights=[0.4, 0.6])
```

The weights `[0.4, 0.6]` mean: 40% influence from keyword results, 60% from vector results. You can tune these.

### LlamaIndex and Haystack options

- **LlamaIndex:** Use `HybridRetriever` or combine a `BM25Retriever` with a `VectorIndexRetriever` and pass both to `RetrieverQueryEngine`.
- **Haystack:** Wire `InMemoryBM25Retriever` and `InMemoryEmbeddingRetriever` in parallel, merge with `DocumentJoiner`, then rerank with `SentenceTransformersSimilarityRanker`. (Check the 3.0.0 release notes before using — see the warning above.)

**Why this matters for beginners:** If your documents contain product codes, legal citations, standard numbers, or any precise identifiers, pure vector search will miss them. Hybrid retrieval can recover 1–9% more relevant results than vector-only, depending on your content and queries (the improvement is much larger on keyword-heavy content).

**Things to keep in mind:**
- BM25 requires keeping a separate keyword index in memory or in a search engine like Elasticsearch. For small collections (under 50,000 documents), the overhead is minimal.
- The 1–9% improvement is an average across query types — on keyword-heavy content the improvement is much larger.

🕒 **Cohere Rerank update:** If you use Cohere's reranking service, note that Cohere Rerank 3.5 was deprecated July 1, 2026. API requests to `cohere-rerank-3.5` will automatically forward to the fast model from August 1, 2026. Current model IDs are `rerank-v4.0-pro` and `rerank-v4.0-fast` (32,000 token context). Verify at [docs.cohere.com/docs/models](https://docs.cohere.com/docs/models).

**Sources:** [comet.com/site/blog/using-advanced-retrievers-in-langchain](https://www.comet.com/site/blog/using-advanced-retrievers-in-langchain/) (2025) · [haystack.deepset.ai/cookbook/hybrid_rag_pipeline_with_breakpoints](https://haystack.deepset.ai/cookbook/hybrid_rag_pipeline_with_breakpoints) (2026) · [redis.io/blog/rag-at-scale](https://redis.io/blog/rag-at-scale/) (updated 2026-05-21) · markaicode.com/architecture/rag-architecture-with-langchain (confirmed live 2026-07-22, unlinked — 403 bot-protection)

**Confidence:** ✅ independently-corroborated

---

## Practice 4: In LlamaIndex, use `SentenceWindowNodeParser` to embed small and retrieve big

### The problem: embedding a paragraph buries the key sentence

When you embed a whole paragraph as a single unit, the embedding captures the average meaning of all the sentences. The precise sentence that answers the question gets diluted. Vector search then struggles to pinpoint it.

### The solution: embed each sentence, but retrieve its neighbors too

`SentenceWindowNodeParser` (a feature of LlamaIndex — a Python framework for building RAG systems) does something clever:

1. It splits your document into individual sentences.
2. It embeds each sentence separately — giving you precise, fine-grained matches.
3. It stores the surrounding sentences (a "window") as hidden metadata attached to each sentence.
4. When a sentence is retrieved as a match, `MetadataReplacementPostProcessor` expands it back to include the surrounding window before sending it to the AI.

Result: you get the precision of sentence-level matching with the context of paragraph-level retrieval.

```python
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.core.postprocessor import MetadataReplacementPostProcessor

node_parser = SentenceWindowNodeParser.from_defaults(window_size=3)
index = VectorStoreIndex(nodes, ...)
query_engine = index.as_query_engine(
    node_postprocessors=[MetadataReplacementPostProcessor(target_metadata_key="window")]
)
```

`window_size=3` means include 3 sentences before and after the matched sentence.

**Why this matters for beginners:** This is a simple technique that noticeably improves answer quality on longer documents. The AI gets exactly the right passage rather than a vague paragraph that loosely relates to the question.

**Things to keep in mind:**
- On very short documents or dense tables, a window of 3 surrounding sentences can pull in unrelated content. Reduce `window_size` if that happens.
- Because every sentence becomes its own index entry, the index will be larger than a paragraph-based one.
- This pattern has not been compared head-to-head against page-level chunking in a peer-reviewed study.

**Sources:** medium.com/@Modexa "7 LlamaIndex retrieval tweaks" (confirmed live 2026-07-22, unlinked — 403 bot-protection) · [developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index](https://developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index/) (2026-06-24 release)

**Confidence:** 📄 vendor-documented (LlamaIndex official docs) + one independent practitioner source — labelled ✅ independently-corroborated on the pattern, thin on the specific performance claim

---

## Practice 5: Choose your vector store by size — Chroma for learning, Qdrant or pgvector for production

### What is a vector store and why do you need to choose one?

A vector store is the database where your document embeddings (the lists of numbers from Practice 2) are saved and searched. Your choice affects how much setup work is required, how fast searches run, and how many documents you can store.

### The simple guide

If you are just learning or building a small prototype, use **Chroma**. It runs locally with three lines of code. No server to set up.

If you already have PostgreSQL running (a popular open-source database), add **pgvector** to it. Free, no new database to learn.

If you are building something that real users will depend on and you need to store millions of documents, use **Qdrant**.

| Your situation | Recommended store | LangChain package | LlamaIndex package |
|---|---|---|---|
| Learning / prototype (under 500,000 vectors) | Chroma | `langchain-chroma` | `llama-index-vector-stores-chroma` |
| Production, running on your own server, over 5 million vectors | Qdrant | `langchain-qdrant` | `llama-index-vector-stores-qdrant` |
| Already running PostgreSQL | pgvector | `langchain-postgres` | `llama-index-vector-stores-postgres` |
| Need both keyword and image search | Weaviate | `langchain-weaviate` | `llama-index-vector-stores-weaviate` |

**If you are a complete beginner and just want something that works with no server setup:** Use Supabase or Neon. Both offer a free tier of PostgreSQL with pgvector already installed. You get a connection string and you are done — no server to manage.

**Why this matters for beginners:** Starting with the wrong database means painful migration later. Chroma is great for learning, but its cloud offering was still in beta as of mid-2026. Qdrant's Rust-based core handles very large data sets by adding more machines rather than requiring a bigger single machine. pgvector is convenient if your team already knows PostgreSQL, but performance drops significantly beyond about 10 million vectors unless you set up special index types (`ivfflat` or `hnsw`).

**Things to keep in mind:**
- ⚠️ Chroma went through a major internal rewrite in 2025. Tutorials from before 2025 may show API calls that no longer work. Always pin exact package versions in your `requirements.txt` file so updates do not break your code.
- pgvector requires PostgreSQL version 15 or newer with the `vector` extension installed. If you use a managed host (Supabase, Neon, or AWS RDS), this is handled automatically.

**Sources:** [baeseokjae.github.io/posts/vector-database-comparison-2026](https://baeseokjae.github.io/posts/vector-database-comparison-2026/) (2026) · [jangwook.net/en/blog/en/vector-db-comparison-2026-qdrant-chroma-pgvector](https://jangwook.net/en/blog/en/vector-db-comparison-2026-qdrant-chroma-pgvector/) (2026) · [developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index](https://developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index/) (2026)

**Confidence:** ✅ independently-corroborated 🕒 verify live (cloud-tier availability and extension support change)

---

## Practice 6: Stream AI responses to the browser so users do not stare at a blank screen

### What is streaming?

Normally, an AI generates its complete answer and then sends it all at once. This means users wait 3–10 seconds staring at nothing before any text appears.

**Streaming** sends each word (actually each token) to the browser as soon as it is generated, just like watching someone type. Users perceive this as much faster, even when the total time is the same.

**SSE** (Server-Sent Events) is the standard web technique for this. Think of it as a live radio broadcast — the server sends a continuous stream of data, and the browser listens. It requires no special library beyond what FastAPI (a Python web framework) already provides.

**LCEL** (LangChain Expression Language) is LangChain's way of chaining together retrieval and AI generation steps. LCEL has built-in support for streaming.

### How to set it up

```python
# minimal sketch — not copy-paste production code
from fastapi.responses import StreamingResponse
import json

async def rag_stream(query: str):
    async for event in rag_chain.astream_events({"question": query}, version="v2"):
        if event["event"] == "on_chat_model_stream":
            yield f"data: {json.dumps(event['data']['chunk'].content)}\n\n"
    # Missing for production: error handling if rag_chain raises mid-stream, input validation on `query`

@app.get("/stream")
async def stream_endpoint(query: str):
    return StreamingResponse(rag_stream(query), media_type="text/event-stream")
```

**Why this matters for beginners:** A blank screen for 5 seconds feels broken. Streaming text appearing word by word feels alive. For any user-facing RAG application, streaming is the difference between a prototype and something people actually want to use.

**Things to keep in mind:**
- ⚠️ Use `version="v2"` in `astream_events()`. Version `v1` is deprecated — do not hardcode `version="v1"` in new code.
- Streaming bypasses response-level caching (see Practice 7). If you combine streaming with caching, cache at the retrieval step, not the generation step.
- The code above is a minimal sketch. A production version needs error handling for when the AI chain fails mid-stream, and input validation to reject malicious or malformed queries.

**Sources:** [reference.langchain.com/python/langchain-core/runnables/base/Runnable/astream_events](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/astream_events) (official LangChain API ref, 2026) · medium.com/@eric_vaillancourt "Mastering LangChain RAG Streaming" (confirmed live 2026-07-22, unlinked — 403 bot-protection) · [blog.futuresmart.ai: Async RAG System with FastAPI, Qdrant & LangChain](https://blog.futuresmart.ai/rag-system-with-async-fastapi-qdrant-langchain-and-openai) (2025)

**Confidence:** ✅ independently-corroborated

---

## Practice 7: Use Redis semantic caching to avoid paying the AI twice for the same question

### What is a cache and what makes it "semantic"?

A **cache** stores the result of an expensive operation so you can reuse it without doing the work again. A normal cache stores exact matches: the same question, character for character, returns the stored answer.

A **semantic cache** is smarter. It checks whether the new question has a *similar enough meaning* to a question already answered. "What is the return policy?" and "How do I return an item?" are different strings but mean the same thing. A semantic cache catches both.

**Redis** is a popular in-memory database. Here it stores the cached answers. `RedisSemanticCache` (from the `langchain-redis` package) handles the similarity matching automatically.

### What you need first

⚠️ **Redis prerequisite:** You need a running Redis instance before this code will work. If you run Redis on your own machine (Ubuntu), install it with:

```
sudo apt install redis-server && sudo systemctl start redis
```

For cloud deployment (a server on the internet), Redis Cloud offers a free tier at [redis.io/try-free](https://redis.io/try-free). Without a running Redis, the code below will fail with a connection error.

### How to set it up

```python
from langchain_redis import RedisSemanticCache
from langchain.globals import set_llm_cache

set_llm_cache(RedisSemanticCache(
    redis_url="redis://localhost:6379",
    embeddings=your_embedding_model,
    score_threshold=0.92,
))
```

The `score_threshold` of `0.92` means: if the new question is 92% similar to a stored one, return the cached answer. Set it higher (0.95) if you need precise matches; lower (0.85–0.90) if you want to save more money and can tolerate slightly less precise cache hits.

**Why this matters for beginners:** Every call to an AI API costs money. If 100 users ask similar questions throughout the day, without a cache you pay the AI 100 times. With a semantic cache, you pay once and serve the rest from storage at sub-100 millisecond response times instead of multi-second AI calls. One published analysis found semantic caching reduced AI API calls by up to 68.8% in the tested workload.

**Things to keep in mind:**
- ⚠️ The 68.8% figure comes from a single paper cited in a Redis vendor blog post. It was measured on a specific workload with high question repetition. Your savings depend entirely on how often your users ask similar questions. On a diverse query workload, savings will be lower.
- ⚠️ **Session bleed is a real risk.** If you cache answers without separating them by user or tenant, one user's answer (which might reference their private data) can be returned to a completely different user. Always scope your cache keys by tenant. This is not optional.

**Sources:** [redis.io/blog/rag-at-scale](https://redis.io/blog/rag-at-scale/) (updated 2026-05-21) · [weblineindia.com/blog/build-rag-with-langchain-redis-vector-search](https://www.weblineindia.com/blog/build-rag-with-langchain-redis-vector-search/) (2025) · markaicode.com/architecture/rag-architecture-with-langchain (confirmed live 2026-07-22, unlinked — 403 bot-protection)

**Confidence:** ✅ independently-corroborated (the general pattern) | ⚠️ The specific 68.8% cost reduction figure is `thin` — single vendor-cited paper, verify for your workload

---

## Practice 8: Test your RAG pipeline automatically — catch quality problems before your users do

### Why testing an AI pipeline is different from testing normal code

Normal code either runs or crashes. A RAG pipeline can run perfectly — no errors, no exceptions — and still give wrong, misleading, or made-up answers. The only way to catch this is to measure the quality of the answers with specific metrics.

**CI** (Continuous Integration) means running automated checks every time you change your code. Tools like GitHub Actions do this automatically when you push code to GitHub. Adding RAG quality checks to CI means you find out immediately if a code change made your answers worse — before any user sees it.

### The four metrics that matter most

- **Faithfulness** — Does the answer contradict what the retrieved documents say? An AI that makes things up fails this.
- **Answer Relevancy** — Does the answer actually address the question asked?
- **Context Precision** — Are the retrieved documents relevant to the question?
- **Context Recall** — Did the retrieval step find all the documents that matter?

Use at least two of these four in your automated tests.

### Two tools for running these checks

**RAGAS** integrates with LangChain and LangSmith (LangChain's tracing tool). Use `RagasEvaluatorChain` to score your pipeline.

**DeepEval** integrates with `pytest` (Python's standard testing tool). Write a test file and run it like this:

```
deepeval test run tests/test_rag.py
```

Inside the test file, use `assert_test` to fail the test if quality drops below your threshold:

```python
assert_test(test_case, metrics=[FaithfulnessMetric(threshold=0.7)])
```

### Keeping your API key secret in GitHub Actions

When you set up automated testing in GitHub Actions, you need to give it your AI API key. **Never paste the actual key directly into the YAML file.** Anyone who can see your repository will see your key, and the AI provider will revoke it immediately.

Use GitHub Secrets instead:

1. Go to your GitHub repository.
2. Click Settings > Secrets and variables > Actions > New repository secret.
3. Name: `OPENAI_API_KEY` — Value: your actual key.
4. In your YAML file, reference it as `${{ secrets.OPENAI_API_KEY }}`.

```yaml
# GitHub Actions snippet
- name: Run RAG evals
  env:
    # ⚠️ NEVER paste your actual API key here.
    # Use GitHub Secrets: Settings > Secrets and variables > Actions > New repository secret
    # Name: OPENAI_API_KEY  Value: your-actual-key
    # Then reference it as ${{ secrets.OPENAI_API_KEY }} as shown below.
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  run: poetry run deepeval test run tests/test_rag.py
```

**Never put an actual API key value in this file** — if you push the YAML with a real key in plaintext, GitHub will detect it and notify the API provider, and your key will be revoked.

**Why this matters for beginners:** RAG quality degrades silently. A new batch of documents, a version bump to your embedding model, or a small prompt edit can make your answers wrong — with no Python error to warn you. Automated evals catch this before users notice, the same way unit tests catch code bugs.

**Things to keep in mind:**
- ⚠️ Both RAGAS and DeepEval call an AI to score each test case. This costs money on every CI run. Keep your test set to 50–200 question-answer pairs to control costs. Most teams run DeepEval in CI on every code change and run RAGAS on a scheduled schedule, sampling 1–5% of live user queries.

🕒 **RAGAS version note (verify before using):** This guide references RAGAS. The current version is 0.4.3 (January 2026), which has significant API differences from the older 0.1.x series. The `RagasEvaluatorChain` class is from the 0.1.x era — verify whether it is still available in 0.4.x before using it. ⚠️ PENDING (#ragas-0.4-api-verification)

🕒 **DeepEval 4.x breaking changes (verify your environment):** DeepEval 4.1.2 (July 2026) removed the `API_KEY` environment variable alias — you must now use `CONFIDENT_API_KEY` for Confident AI uploads. The `additional_metadata` parameter was renamed to `metadata`. Per-result `.log` output was deprecated; use `results_folder` instead. The `assert_test` pattern itself still works.

**Sources:** [docs.ragas.io/en/stable/](https://docs.ragas.io/en/stable/) (RAGAS official docs) · [confident-ai.com/blog/how-to-evaluate-rag-applications-in-ci-cd-pipelines-with-deepeval](https://www.confident-ai.com/blog/how-to-evaluate-rag-applications-in-ci-cd-pipelines-with-deepeval) (Confident AI, 2025) · [deepeval.com/docs/evaluation-unit-testing-in-ci-cd](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd) (DeepEval official docs, 2026)

**Confidence:** ✅ independently-corroborated (RAGAS docs + DeepEval docs = two independent vendors)

---

## Practice 9: Use the right PDF parser for your document type — the wrong one produces garbage

### Why does the parser choice matter so much?

"PDF" is not a single format. A PDF can be:
- A text-based document (text is stored as text inside the file).
- A scanned image (text is just pixels — no extractable text without OCR).
- A financial report with complex tables.
- A mixed folder of Word files, HTML pages, and emails.

Using the wrong parser for your document type produces scrambled, incomplete, or missing text. Everything downstream — chunking, embedding, retrieval — will be built on bad input.

**OCR** (Optical Character Recognition) is the technology that reads text from images. Scanned PDFs need it. Text-based PDFs do not.

### Match your tool to your need

| What you have | Best tool | How to install |
|---|---|---|
| Text-based PDFs (most office documents) | `PyMuPDF` (imported as `fitz`) | `pip install pymupdf` |
| PDFs with tables (financial reports, data sheets) | `pdfplumber` | `pip install pdfplumber` |
| A mixed folder of PDFs, Word files, HTML, emails | `unstructured` | `pip install unstructured` |
| Scanned PDFs or images of documents | `unstructured` with Tesseract OCR | `pip install unstructured` then `sudo apt install tesseract-ocr` |

**Important about scanned PDFs:** Tesseract is a system program, not a Python package. Running `pip install unstructured` alone will appear to succeed but will silently fail on scanned PDFs. You must separately run `sudo apt install tesseract-ocr` (on Ubuntu/Debian) to install the system dependency.

Both LangChain (using `UnstructuredFileLoader`) and LlamaIndex (using `SimpleDirectoryReader` with file-type routing) can use these parsers automatically behind the scenes.

**Why this matters for beginners:** Garbled text going in means garbled answers coming out. No amount of clever chunking, embedding, or retrieval can fix bad source text. Getting the parser right is the most important step in building a RAG system.

**Things to keep in mind:**
- `unstructured` pulls in large optional dependencies (Tesseract, Poppler, and others). This can make Docker container images very large. Pin the version number — `unstructured` has had breaking API changes between minor releases.
- For image-heavy PDFs where layout matters (slide decks, diagrams), even OCR may not be enough. Consider using a vision AI service like LlamaParse or a cloud document AI API.

**Sources:** medium.com/@hchenna "Technical Comparison — Python Libraries for Document Parsing" (confirmed live 2026-07-22, unlinked — 403 bot-protection) · [firecrawl.dev/blog/best-chunking-strategies-rag](https://www.firecrawl.dev/blog/best-chunking-strategies-rag) (2026) · [haystack.deepset.ai/tutorials/27_first_rag_pipeline](https://haystack.deepset.ai/tutorials/27_first_rag_pipeline) (Haystack official tutorial, 2026)

**Confidence:** ✅ independently-corroborated

---

## Practice 10: Lock down who can see which documents — do not rely on telling the AI to keep secrets

### Why "just tell the AI not to reveal it" does not work

A common beginner mistake is to include a prompt instruction like: "Do not show documents from the Finance team to non-Finance users." This feels like a security measure. It is not.

A technique called **prompt injection** embeds hidden instructions inside a retrieved document. When the AI reads that document, the hidden instructions can override your safety prompt. The AI then reveals things it was told not to reveal — not because the AI is malicious, but because it is following instructions it found in the document.

The only real defense is to prevent the AI from ever seeing the restricted document in the first place.

### How to do it: metadata filters

**Step 1: Tag every document at ingest time.**

When you load documents into your vector store, attach access group labels as metadata:

```python
# at ingest
doc.metadata["access_groups"] = ["finance", "exec-team"]
```

**Step 2: Filter at retrieval time, not at prompt time.**

When a user makes a query, tell the vector store to only search documents that match that user's groups — before any results reach the AI:

```python
# LangChain / Chroma example
# NOTE: {"$in": user_groups} filter syntax is Chroma-specific — see note below
retriever = vectorstore.as_retriever(
    search_kwargs={"filter": {"access_groups": {"$in": user_groups}}}
)
```

This filter runs inside the database. The AI only ever receives documents the user is allowed to see.

**Important: each vector store has different filter syntax.** The `{"$in": user_groups}` format above is specific to Chroma. Other stores use different syntax:
- Qdrant uses payload filter syntax (`models.Filter(must=[models.FieldCondition(...)])`)
- Weaviate uses its own `where` filter
- pgvector uses SQL `WHERE` predicates

Check your specific vector store's documentation for the correct syntax.

**Why this matters for beginners:** If you skip this step, every user of your RAG system effectively has access to every document you ever indexed. In a multi-user application, this is a serious data leak waiting to happen. Filtering at the retrieval layer is the only reliable solution.

**Things to keep in mind:**
- ⚠️ Metadata filters only work if the vector store actually indexes (tracks) that metadata field. Not all stores do this automatically. Verify before relying on it.
- ⚠️ Make sure your code gets the user's group list from a trusted source (your authentication system) — not from something the user controls, like a request header they could modify.
- ⚠️ If a document is tagged with the wrong access group when it is first loaded, the wrong people will see it, silently. Audit your ingestion pipeline regularly.

**Sources:** [snyk.io/articles/what-is-rag-and-how-to-secure-it](https://snyk.io/articles/what-is-rag-and-how-to-secure-it/) (Snyk, 2025) · [dev.to/devopsstart: RAG Security — Prevent Data Leaks with Access Control](https://dev.to/devopsstart/rag-security-prevent-data-leaks-with-access-control-lb9) (2025) · [scalacode.com/blog/how-to-secure-rag-pipeline](https://www.scalacode.com/blog/how-to-secure-rag-pipeline/) (2026)

**Confidence:** ✅ independently-corroborated (three independent publishers: Snyk, dev.to, ScalaCode)

---

## Practice 11: Remove personal information from documents before embedding — not after

### What is PII and why does it matter here?

**PII** stands for Personally Identifiable Information — names, email addresses, phone numbers, national ID numbers, medical information, and similar data. Many document collections contain PII mixed in with legitimate content.

**The problem:** Once PII is embedded in a vector store, similarity search can surface it for any semantically related query — even from a completely different user's session. A question about "contact details" might retrieve a document containing someone's home address, medical record, or social security number.

The time to remove PII is before it ever enters the vector store, not after.

### What you need

```
pip install presidio-analyzer presidio-anonymizer spacy
```

Then download the language model that `presidio-analyzer` requires:

```
python -m spacy download en_core_web_lg
```

**This second command is required.** Presidio uses spaCy (a natural language processing library) to recognize names, places, and other entities. Without the language model download, `presidio-analyzer` will fail when you try to initialize it. `pip install` alone does not download this model.

### The correct order of operations

```python
# conceptual order of operations — ingestion pipeline
raw_text → PII_scrub() → chunk() → embed() → store()
# NOT:
raw_text → chunk() → embed() → store() → retrieve() → PII_filter() → LLM
```

Scrub first, then chunk, then embed. Not the other way around.

**Why this matters for beginners:** If you scrub after retrieval ("I'll just filter it at the end"), you have already stored the PII in your vector database. Any query that semantically resembles the PII context can surface it. You have also already sent the document through a third-party embedding API — meaning that API provider has potentially seen the personal data. Pre-embedding scrubbing prevents both problems.

**Things to keep in mind:**
- Automated PII scrubbers are imperfect. They miss unusual formats (like domain-specific ID codes) and sometimes flag legitimate content as PII (false positives that corrupt the text).
- For medical or legal documents, combine automated scrubbing with a human review step.
- If you replace PII with reversible tokens (so you can restore the original later), store the token-to-original mapping in a separate, access-controlled database — never in the same vector store you are protecting.

**Sources:** [scalacode.com/blog/how-to-secure-rag-pipeline](https://www.scalacode.com/blog/how-to-secure-rag-pipeline/) (2026) · [snyk.io/articles/what-is-rag-and-how-to-secure-it](https://snyk.io/articles/what-is-rag-and-how-to-secure-it/) (Snyk, 2025)

**Confidence:** ✅ independently-corroborated

---

## Practice 12: Keep document loading and user queries in separate processes

### What is the problem with doing both in one place?

When a user asks a question, your application searches the vector store — this needs to be fast (under a second ideally).

When you load new documents, you chunk them, embed them, and write them to the vector store — this is slow and uses a lot of resources.

If both happen in the same running process, a large document load can consume 30% of your process's capacity and slow down query responses for all users simultaneously.

### The fix: separate the two workloads

Run document loading in a background worker (a separate process). Run user queries in your web API. They share the same vector store, but they do not compete for the same CPU and memory.

```
[Document Source] --> [Ingestion Worker] --> [Vector Store] <-- [Query API]
```

Tools for background workers in Python include **Celery** (a popular task queue), **FastAPI BackgroundTask** (built into FastAPI for simple cases), or a dedicated service you write yourself.

**Deletion is not automatic:** If you delete a document from your source, you must explicitly add it to a deletion queue. The ingestion pipeline does not automatically clean up orphaned vectors (old chunks still in the vector store from a now-deleted document).

**Why this matters for beginners:** Without this separation, a large document import will make your application feel slow or broken for every user who happens to be querying at the same time. A production guide for Redis noted that a single large `upsert` operation can block 30% of concurrent reads on the same process.

**Things to keep in mind:**
- There will be a delay between when a document is loaded and when it appears in query results. This is normal and usually acceptable (seconds to minutes).
- If your application requires truly immediate document availability (live news feeds, real-time pricing), you need a more complex approach called change-data-capture (CDC) streaming, which is significantly more complex to build and operate.

**Sources:** [redis.io/blog/rag-at-scale](https://redis.io/blog/rag-at-scale/) (updated 2026-05-21) · markaicode.com/architecture/rag-architecture-with-langchain (confirmed live 2026-07-22, unlinked — 403 bot-protection) · [pristren.com/blog/haystack-rag-pipeline-framework](https://pristren.com/blog/haystack-rag-pipeline-framework/) (2025)

**Confidence:** ✅ independently-corroborated

---

## Held pending fixes (not publish-ready)

- Haystack 3.0.0 released 2026-07-20 (two days before this snapshot). The launch-week page confirms agents are now central; detailed migration notes for `Pipeline`, `PromptBuilder`, and `DocumentStore` from 2.x to 3.0 could not be fully verified from fetched pages in this run. All Haystack practices above cite 2.x patterns that are documented in tutorials still live on [haystack.deepset.ai](https://haystack.deepset.ai) — confirm they remain valid under 3.0 before publishing. ⚠️ #PENDING-haystack-3-migration

---

## CHANGELOG (grading → this entry)

1. **[Beginner KILL]** Added RAG definition, key terms (embedding, vector store), prerequisites section with cost warning ($0.20–$5.00/run for 200-case eval suite), and cross-reference to Practices 10 and 11 before the version snapshot table.
2. **[Beginner FIX]** Practice 1 — Added "First check if you have it installed: `pip show langchain-community`" instruction before the migration guidance.
3. **[Beginner FIX]** Practice 2 — Added explicit `from langchain_text_splitters import RecursiveCharacterTextSplitter` import statement with note that `from langchain.text_splitter` is deprecated.
4. **[Timekeeper KILL + Beginner KILL]** Practice 3 — Added prominent WARNING block at the top of Practice 3 detailing Haystack 3.0.0 breaking changes (released 2026-07-20): `AsyncPipeline` removal, generator removals, `SentenceTransformersSimilarityRanker` moved to integrations, `PromptBuilder` variable handling change, pipeline deserialization change. Marked ⚠️ PENDING full 3.0.0 migration verification.
5. **[Beginner FIX]** Practice 3 — Changed "(Requires `pip install rank_bm25` for the BM25 side)" to a visible prerequisite block before the code.
6. **[Beginner FIX]** Practice 3 — Added explicit `from langchain.retrievers import EnsembleRetriever` and `from langchain_community.retrievers import BM25Retriever` imports with sunset caveat and alternative guidance.
7. **[Timekeeper KILL]** Practice 3 and reranker mentions — Added Cohere Rerank deprecation note: Rerank 3.5 deprecated July 1 2026; auto-forward to fast model from August 1 2026; current model IDs `rerank-v4.0-pro` and `rerank-v4.0-fast`.
8. **[Beginner FIX]** Practice 4 — Added `from llama_index.core import VectorStoreIndex` import statement to the code block.
9. **[Beginner FIX]** Practice 5 — Added parentheticals defining "self-hosted" and "horizontal clustering"; added recommendation to use Supabase or Neon for beginners (free-tier pgvector, no server setup).
10. **[Beginner FIX]** Practice 6 — Added production gap comment inside the streaming function: error handling and input validation notes.
11. **[Skeptic FIX]** Practice 7 — Reframed "68.8% cost reduction" to accurately describe what the paper measures (cache-hit/API-call reduction) versus the Redis vendor blog's restatement.
12. **[Beginner KILL]** Practice 7 — Added Redis prerequisite block before the code with Ubuntu install command and Redis Cloud free-tier link.
13. **[Beginner KILL]** Practice 8 — Added GitHub Secrets warning comments inside the YAML `env:` block explaining how to set up secrets instead of pasting keys; added plain-English warning that plaintext keys in YAML will be detected and revoked.
14. **[Beginner FIX]** Practice 8 — Added CI/CD explanation before the code snippet defining what CI means.
15. **[Timekeeper FIX]** Practice 8 — Updated RAGAS source URL from `docs.ragas.io/en/v0.1.21/howtos/integrations/langchain.html` to `docs.ragas.io/en/stable/`; added RAGAS API note about 0.1.x vs 0.4.x API changes and `RagasEvaluatorChain` availability caveat; marked ⚠️ PENDING (#ragas-0.4-api-verification).
16. **[Timekeeper FLAG]** Practice 8 — Added DeepEval 4.1.2 (July 2026) breaking changes note: `API_KEY` alias removed, `additional_metadata` → `metadata`, `.log` deprecated; `assert_test` pattern still works.
17. **[Beginner FIX]** Practice 9 — Updated "Scanned PDFs / images" Install column to include `sudo apt install tesseract-ocr` with explanation that Tesseract is a system dependency and `pip install unstructured` alone will silently fail on scanned PDFs.
18. **[Beginner FIX]** Practice 10 — Added caveat clarifying that `{"$in": user_groups}` is Chroma's filter syntax; noted Qdrant payload filter syntax, Weaviate `where` filter, and pgvector SQL `WHERE` predicates differ.
19. **[Beginner FIX]** Practice 11 — Added prerequisites block before the conceptual diagram: `pip install presidio-analyzer presidio-anonymizer spacy` and `python -m spacy download en_core_web_lg` with explanation that the spaCy model download is required for initialization.
20. **[Front matter]** Updated `grading_result` from `"pending"` to `"graded — 0 fabrications"`.
21. **[Re-level]** Re-leveled from the 2026-07-22 technical entry to beginner track; facts unchanged. Plain-English analogies and definitions added throughout. All warnings, caveats, 🕒 verify-live notes, and ⚠ PENDING items preserved verbatim. No new facts, statistics, or URLs introduced.
22. **[Link-check gate]** Practice 4 — Unlinked medium.com/@Modexa "7 LlamaIndex retrieval tweaks" (confirmed live 2026-07-22; 403 bot-protection; 1 occurrence).
23. **[Link-check gate]** Practice 6 — Unlinked medium.com/@eric_vaillancourt "Mastering LangChain RAG Streaming" (confirmed live 2026-07-22; 403 bot-protection; 1 occurrence).
24. **[Link-check gate]** Practice 9 — Unlinked medium.com/@hchenna "Technical Comparison — Python Libraries for Document Parsing" (confirmed live 2026-07-22; 403 bot-protection; 1 occurrence).
25. **[Link-check gate]** Practices 3, 7, 12 — Unlinked markaicode.com/architecture/rag-architecture-with-langchain/ (confirmed live 2026-07-22; 403 bot-protection; 3 occurrences).

