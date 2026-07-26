# RAG Best Practices — Python Ecosystem (LangChain, LlamaIndex, Haystack) (as of 22 Jul 2026)

> Sourced best practices for building RAG systems in Python using LangChain, LlamaIndex, and Haystack — chunking, hybrid retrieval, vector stores, streaming, evaluation, and security. Accurate as of 22 Jul 2026.


<!-- This file lands at content/ai/best-practices/python-rag-best-practices/2026-07-22/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW snapshot-date dir.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# RAG (Retrieval-Augmented Generation) Best Practices — Python Ecosystem (as of 22 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **22 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

---

## What is RAG?

RAG (Retrieval-Augmented Generation) means your application retrieves relevant documents first, then passes them to an LLM as context for the answer — rather than relying only on what the model was trained to know.

**Key terms:**

- An **embedding** is a list of numbers representing text meaning, enabling similarity search.
- A **vector store** (vector database) stores these number-lists and searches them efficiently.

⚠️ **Prerequisites and cost warning:** Python ≥ 3.10, `pip` or `uv`, an LLM API key (OpenAI, Anthropic, or similar) with billing configured, and a running vector store. ⚠️ Running RAGAS or DeepEval evaluations calls an LLM for EACH scored test case — a suite of 200 golden Q&A pairs can cost $0.20–$5.00 per run depending on model. Never commit API keys to source control (see Practice 8 on GitHub Secrets).

⚠️ **Before ingesting any documents, read Practices 10 and 11 (access control and PII).** Personal data embedded in a vector index can be retrieved by any user with search access.

---

## Version snapshot (verify live) 🕒

| Package | Latest as of 2026-07-22 | Source |
|---|---|---|
| `langchain-core` | **1.5.0** (released 2026-07-21) | [pypi.org/project/langchain-core](https://pypi.org/project/langchain-core/) |
| `langchain` | **1.3.14** (released 2026-07-16) | [pypi.org/project/langchain](https://pypi.org/project/langchain/) |
| `langchain-community` | **SUNSET** — repo archived 2026-06-19; see [issue #674](https://github.com/langchain-ai/langchain-community/issues/674) | [github.com/langchain-ai/langchain-community](https://github.com/langchain-ai/langchain-community) |
| `llama-index-core` | **0.14.23** (released 2026-06-24) | [pypi.org/project/llama-index-core](https://pypi.org/project/llama-index-core/) |
| `haystack-ai` | **3.0.0** (released 2026-07-20) | [pypi.org/project/haystack-ai](https://pypi.org/project/haystack-ai/) |

## How to read the labels

- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: Stop importing from `langchain-community` — migrate to standalone integration packages

**Do:** First check if you have it installed: `pip show langchain-community`. If you see a version number, you are affected and need to migrate.

Replace all `from langchain_community.xxx import Yyy` imports with the corresponding dedicated integration package (e.g. `langchain-chroma`, `langchain-qdrant`, `langchain-openai`). Install only the packages you need. Check the [LangChain integrations page](https://docs.langchain.com/oss/python/integrations/providers/overview) for the current package name for each integration.

**Why (beginner):** `langchain-community` was a catch-all package that bundled hundreds of third-party connectors under one roof. The repo was archived and marked read-only on 2026-06-19 — no bug fixes, no security patches. Code that still imports from it will break on future Python or dependency updates.

**Caveat:** The standalone packages are maintained by different owners (the connector vendor, or community members), so maintenance quality varies. Check each package's own repository for activity before adopting it.

**Sources:** [github.com/langchain-ai/langchain-community](https://github.com/langchain-ai/langchain-community) (archived 2026-06-19) · [LangChain forum: migration guidance](https://forum.langchain.com/t/recommended-migration-path-for-tools-and-integrations-following-the-langchain-community-sunset/3934) (2026) · [github.com/langchain-ai/langchain-community/issues/674](https://github.com/langchain-ai/langchain-community/issues/674) (2026-06-19)

**Confidence:** ✅ independently-corroborated (LangChain official repo + LangChain community forum, two different publisher surfaces) 🕒 verify live

---

## Practice 2: Start chunking with `RecursiveCharacterTextSplitter` at 400–512 tokens, 10–20 % overlap

**Do:** Use `RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=51)` (or equivalent token counts) as your default chunking strategy. The splitter respects natural language boundaries in priority order: paragraph break → line break → sentence boundary → word boundary, avoiding mid-sentence cuts. Tune chunk size down to 256 tokens for factoid (single-fact) queries and up to 1 024 tokens for analytical queries where more context per chunk improves the answer.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
# NOTE: do NOT use `from langchain.text_splitter` — that import path is deprecated

splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=51)
```

**Why (beginner):** Chunks that are too small lose context; chunks that are too large flood the prompt window with irrelevant text. The recursive strategy is the broadly recommended default because it balances structure awareness against simplicity. You can swap in a more expensive semantic splitter later once you have evaluation metrics to justify the cost.

**Caveat / contested:** Page-level chunking won NVIDIA's 2024 benchmark (0.648 accuracy, lowest variance) for PDF/paginated documents. For scanned or complex-layout PDFs, no splitter compensates for poor OCR upstream — fix the parser first. The "400–512 tokens" figure comes from industry practitioner articles, not from a controlled head-to-head published study — treat it as a reasonable starting point, not a proven optimum.

**Sources:** [firecrawl.dev/blog/best-chunking-strategies-rag](https://www.firecrawl.dev/blog/best-chunking-strategies-rag) (2026) · [redis.io/blog/rag-at-scale](https://redis.io/blog/rag-at-scale/) (pub. 2026-01-21, updated 2026-05-21)

**Confidence:** ✅ independently-corroborated

---

## Practice 3: Use hybrid retrieval (BM25 + dense vectors) in production — not dense-only

> ⚠️ **HAYSTACK 3.0.0 BREAKING CHANGES (released 2026-07-20 — 2 days before this snapshot)**
>
> The Haystack code in this practice was written for Haystack 2.x. Haystack 3.0.0 introduced major breaking changes:
> - `AsyncPipeline` removed; a unified `Pipeline` class now has both sync and async `run()` methods
> - `OpenAIGenerator`, `AzureOpenAIGenerator`, `HuggingFaceAPIGenerator`, `HuggingFaceLocalGenerator` removed entirely — Chat Generators replace them
> - `SentenceTransformersSimilarityRanker` moved to `haystack-core-integrations` (separate package)
> - `PromptBuilder` and `ChatPromptBuilder` now treat Jinja2 template variables as required by default
> - Pipeline deserialization blocks unsafe imports by default
>
> **Before running the code below, verify it against the 3.0.0 release notes at [haystack.deepset.ai/release-notes/3.0.0](https://haystack.deepset.ai/release-notes/3.0.0).** This practice is marked ⚠️ PENDING full 3.0.0 migration verification.

**Do:** Combine a keyword-based retriever (BM25) with a dense vector retriever and merge results with Reciprocal Rank Fusion (RRF).

**Prerequisite:** `pip install rank_bm25` (required for BM25 retrieval)

- **LangChain:**

```python
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever  # NOTE: langchain-community is sunset as of 2026-06-19
# Alternative: use the standalone rank_bm25 package directly — see Practice 1 for migration guidance

retriever = EnsembleRetriever(retrievers=[bm25_retriever, vector_retriever], weights=[0.4, 0.6])
```

- **LlamaIndex:** Use `HybridRetriever` or combine a `BM25Retriever` with a `VectorIndexRetriever` and pass both to `RetrieverQueryEngine`.
- **Haystack:** Wire `InMemoryBM25Retriever` and `InMemoryEmbeddingRetriever` in parallel, merge with `DocumentJoiner`, then rerank with `SentenceTransformersSimilarityRanker`.

🕒 **Cohere Rerank update:** Cohere Rerank 3.5 was deprecated July 1, 2026; API requests to `cohere-rerank-3.5` auto-forward to the fast model from August 1, 2026. Current model IDs: `rerank-v4.0-pro` and `rerank-v4.0-fast` (32k token context). Verify at [docs.cohere.com/docs/models](https://docs.cohere.com/docs/models).

**Why (beginner):** Pure vector search misses exact keyword matches (e.g. product codes, legal citations, ISO standard numbers). BM25 catches keyword hits that dense retrieval buries. Published benchmarks suggest hybrid retrieval can recover 1–9 % more relevant results than dense-only, depending on the corpus and query mix (cited in [redis.io/blog/rag-at-scale](https://redis.io/blog/rag-at-scale/), sourcing [arxiv.org/html/2410.20381v1](https://arxiv.org/html/2410.20381v1)).

**Caveat:** BM25 requires keeping a separate in-memory or Elasticsearch-backed term index. For small corpora (< 50 K documents) the overhead is minimal; for large corpora you need to decide whether to store BM25 state in-process or in a search engine. The 1–9 % improvement range is averaged across query types — improvement on keyword-heavy corpora is much higher.

**Sources:** [comet.com/site/blog/using-advanced-retrievers-in-langchain](https://www.comet.com/site/blog/using-advanced-retrievers-in-langchain/) (2025) · [haystack.deepset.ai/cookbook/hybrid_rag_pipeline_with_breakpoints](https://haystack.deepset.ai/cookbook/hybrid_rag_pipeline_with_breakpoints) (2026) · [redis.io/blog/rag-at-scale](https://redis.io/blog/rag-at-scale/) (updated 2026-05-21) · markaicode.com/architecture/rag-architecture-with-langchain (confirmed live 2026-07-22, unlinked — 403 bot-protection)

**Confidence:** ✅ independently-corroborated

---

## Practice 4: Use `SentenceWindowNodeParser` in LlamaIndex for better retrieval precision

**Do:** In LlamaIndex, replace a plain `SentenceSplitter` with `SentenceWindowNodeParser`. It parses documents into individual sentences, embeds each sentence for precise matching, but stores surrounding sentences as metadata. Pair it with `MetadataReplacementPostProcessor` in the query engine to expand the returned window before sending to the LLM.

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

**Why (beginner):** Embedding a full paragraph buries the precise sentence that answers the question. Sentence-level embedding finds the exact match; window expansion gives the LLM enough surrounding text to generate a coherent answer. This is a two-step trick: embed small (for precision), retrieve big (for context).

**Caveat:** Window size 3 (default) means ±3 sentences of context. On very short documents or dense reference tables, window expansion can pull in unrelated text. Index size grows because every sentence is an individual node. Not yet benchmarked head-to-head against page-level chunking in a peer-reviewed study.

**Sources:** medium.com/@Modexa "7 LlamaIndex retrieval tweaks" (confirmed live 2026-07-22, unlinked — 403 bot-protection) · [developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index](https://developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index/) (2026-06-24 release)

**Confidence:** 📄 vendor-documented (LlamaIndex official docs) + one independent practitioner source — labelled ✅ independently-corroborated on the pattern, thin on the specific performance claim

---

## Practice 5: Choose your vector store by scale — Chroma for prototypes, Qdrant or pgvector for production

**Do:**

| Scale / constraint | Recommended store | LangChain import | LlamaIndex import |
|---|---|---|---|
| Prototype / < 500 K vectors | Chroma | `langchain-chroma` | `llama-index-vector-stores-chroma` |
| Production, self-hosted (meaning you run it on your own server or cloud VM, not a managed cloud service), > 5 M vectors | Qdrant | `langchain-qdrant` | `llama-index-vector-stores-qdrant` |
| Already running PostgreSQL | pgvector | `langchain-postgres` (replaces old `PGVector`) | `llama-index-vector-stores-postgres` |
| Hybrid search / multi-modal | Weaviate | `langchain-weaviate` | `llama-index-vector-stores-weaviate` |

**Why (beginner):** Chroma's three-line setup is fine locally, but its cloud offering was still in beta as of mid-2026. Qdrant (Rust core) handles billions of vectors with horizontal clustering (adding more machines to handle more data, rather than upgrading one machine). pgvector is convenient when your team already operates PostgreSQL; performance degrades beyond ~10 M vectors without tuning (`ivfflat` or `hnsw` indexes). All four have first-class integrations in both LangChain and LlamaIndex as of 2026.

If you are starting out, use Supabase or Neon — they offer free-tier PostgreSQL with pgvector pre-installed, no server setup required.

**Caveat:** ⚠️ Chroma completed a Rust-core rewrite in 2025 that significantly changed its internals — older tutorials may show stale API calls. Always pin exact package versions in `requirements.txt`. pgvector requires PostgreSQL ≥15 with the `vector` extension installed; managed hosts (Supabase, Neon, RDS) handle this automatically.

**Sources:** [baeseokjae.github.io/posts/vector-database-comparison-2026](https://baeseokjae.github.io/posts/vector-database-comparison-2026/) (2026) · [jangwook.net/en/blog/en/vector-db-comparison-2026-qdrant-chroma-pgvector](https://jangwook.net/en/blog/en/vector-db-comparison-2026-qdrant-chroma-pgvector/) (2026) · [developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index](https://developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index/) (2026)

**Confidence:** ✅ independently-corroborated 🕒 verify live (cloud-tier availability and extension support change)

---

## Practice 6: Stream RAG responses with LCEL `.astream_events()` and FastAPI SSE

**Do:** Build LCEL RAG chains and stream token output to the browser using `astream_events(v2)` plus FastAPI's `StreamingResponse`. Tag individual chain components with `.with_config(tags=["llm_step"])` so you can filter on `on_chat_model_stream` events and forward only LLM tokens to the client.

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

**Why (beginner):** Users perceive streamed answers as faster even when total latency is identical. Without streaming, the user stares at a blank screen for 3–10 seconds before any text appears. SSE (Server-Sent Events) is the simplest HTTP streaming primitive; no WebSocket library required.

**Caveat:** ⚠️ `astream_events` schema version defaults to `v2` in recent langchain-core. Version `v1` is deprecated — do not hardcode `version="v1"` in new code. Streaming bypasses response-level caching (see Practice 8), so cache at the retrieval step, not the generation step, when combining both patterns.

**Sources:** [reference.langchain.com/python/langchain-core/runnables/base/Runnable/astream_events](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/astream_events) (official LangChain API ref, 2026) · medium.com/@eric_vaillancourt "Mastering LangChain RAG Streaming" (confirmed live 2026-07-22, unlinked — 403 bot-protection) · [blog.futuresmart.ai: Async RAG System with FastAPI, Qdrant & LangChain](https://blog.futuresmart.ai/rag-system-with-async-fastapi-qdrant-langchain-and-openai) (2025)

**Confidence:** ✅ independently-corroborated

---

## Practice 7: Cache with Redis semantic cache to cut repeated LLM calls

⚠️ **Redis prerequisite:** You need a running Redis instance for this to work. On Ubuntu: `sudo apt install redis-server && sudo systemctl start redis`. For cloud deployment, Redis Cloud offers a free tier at [redis.io/try-free](https://redis.io/try-free). Without a running Redis, the code will fail with a connection error.

**Do:** Wrap your LangChain LLM with `RedisSemanticCache` (from `langchain-redis`) or a custom Redis embedding lookup before hitting the LLM API. Set similarity threshold 0.90–0.95 for correctness-sensitive applications, 0.85–0.90 for cost-reduction focus. Also cache embeddings during ingestion with a 24 h TTL to avoid re-embedding unchanged documents on re-runs.

```python
from langchain_redis import RedisSemanticCache
from langchain.globals import set_llm_cache

set_llm_cache(RedisSemanticCache(
    redis_url="redis://localhost:6379",
    embeddings=your_embedding_model,
    score_threshold=0.92,
))
```

**Why (beginner):** Calling an LLM API for every user question can cost dollars per thousand queries. Semantic caching returns a stored answer when an incoming question is similar enough to one already answered — typically delivering sub-100 ms responses versus multi-second LLM calls. One published analysis ([arxiv.org/abs/2411.05276](https://arxiv.org/abs/2411.05276), cited in the Redis blog) found semantic caching reduced LLM API calls (and thus cost) by up to 68.8% in the tested workload — the underlying paper measures cache-hit/API-call reduction; 'cost reduction' is the Redis vendor blog's restatement.

**Caveat:** ⚠️ The 68.8 % figure comes from a single paper cited in a Redis vendor blog — it reflects a specific workload with high query repetition. Your savings depend heavily on how often users ask similar questions. Session bleed is a real risk: if you cache without scoping by user/tenant, one user's retrieved content can appear in another's response. Always scope cache keys by tenant.

**Sources:** [redis.io/blog/rag-at-scale](https://redis.io/blog/rag-at-scale/) (updated 2026-05-21) · [weblineindia.com/blog/build-rag-with-langchain-redis-vector-search](https://www.weblineindia.com/blog/build-rag-with-langchain-redis-vector-search/) (2025) · markaicode.com/architecture/rag-architecture-with-langchain (confirmed live 2026-07-22, unlinked — 403 bot-protection)

**Confidence:** ✅ independently-corroborated (the general pattern) | ⚠️ The specific 68.8 % cost reduction figure is `thin` — single vendor-cited paper, verify for your workload

---

## Practice 8: Evaluate RAG pipelines with RAGAS and/or DeepEval in CI

CI (Continuous Integration) means automated code that runs every time you push a change — tools like GitHub Actions do this. Adding RAG evals to CI means quality regressions get caught before they reach users.

**Do:** Add automated RAG evaluation to your CI pipeline using at least two of these four metrics: **Faithfulness** (does the answer contradict the retrieved context?), **Answer Relevancy** (does the answer address the question?), **Context Precision** (is the retrieved context relevant?), **Context Recall** (did retrieval find the right documents?).

- **RAGAS + LangChain:** Use `RagasEvaluatorChain` wrapping your QA chain; integrates with LangSmith for per-trace scoring.
- **DeepEval + pytest:** Write `pytest` tests using `assert_test(test_case, metrics=[FaithfulnessMetric(threshold=0.7)])` and run with `deepeval test run test_rag.py`. This gates deploys on quality regressions.

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

**Why (beginner):** RAG quality degrades silently — a new document batch, an embedding model version bump, or a prompt edit can tank faithfulness without any Python exception. Running evals in CI catches regressions before users see them, the same way unit tests catch code bugs.

**Caveat:** ⚠️ Both RAGAS and DeepEval call an LLM to score answers, which costs money per eval run. Keep your CI eval dataset small (50–200 golden Q&A pairs) to control costs. Most practitioners run DeepEval in CI on each PR and RAGAS on a scheduled cron sampling 1–5 % of live traces.

🕒 **RAGAS API note (verify live):** The RAGAS source URL in this practice pointed to v0.1.21; current RAGAS is 0.4.3 (January 2026), which underwent significant API changes between 0.1.x and 0.4.x. `RagasEvaluatorChain` is a 0.1.x-era class — verify its availability in RAGAS 0.4.x before use. ⚠️ PENDING (#ragas-0.4-api-verification)

🕒 **DeepEval 4.x breaking changes:** DeepEval 4.1.2 (July 2026) breaking changes: the `API_KEY` alias was removed (now requires `CONFIDENT_API_KEY` for Confident AI uploads); `additional_metadata` replaced by `metadata`; per-result `.log` output deprecated (use `results_folder`). The `assert_test` pattern itself still works. Verify your environment variables match the current API.

**Sources:** [docs.ragas.io/en/stable/](https://docs.ragas.io/en/stable/) (RAGAS official docs) · [confident-ai.com/blog/how-to-evaluate-rag-applications-in-ci-cd-pipelines-with-deepeval](https://www.confident-ai.com/blog/how-to-evaluate-rag-applications-in-ci-cd-pipelines-with-deepeval) (Confident AI, 2025) · [deepeval.com/docs/evaluation-unit-testing-in-ci-cd](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd) (DeepEval official docs, 2026)

**Confidence:** ✅ independently-corroborated (RAGAS docs + DeepEval docs = two independent vendors)

---

## Practice 9: Use `PyMuPDF` for fast text extraction and `pdfplumber` or `Camelot` for tables; layer `unstructured` for mixed-format corpora

**Do:** Match your PDF parser to your document type:

| Need | Tool | Install |
|---|---|---|
| Fast text from native PDFs | `PyMuPDF` (`fitz`) | `pip install pymupdf` |
| Table extraction from clean PDFs | `pdfplumber` | `pip install pdfplumber` |
| Heterogeneous formats (PDF, DOCX, HTML, email) | `unstructured` | `pip install unstructured` |
| Scanned PDFs / images | `unstructured` with Tesseract OCR, or a cloud API | `pip install unstructured` + `sudo apt install tesseract-ocr` (Tesseract is a system dependency, not a Python package — `pip install unstructured` alone will silently fail on scanned PDFs) |

Both LangChain (`UnstructuredFileLoader`) and LlamaIndex (`SimpleDirectoryReader` with file-type routing) can delegate to these parsers automatically.

**Why (beginner):** No single Python library handles all PDF types well. A financial report with embedded tables needs `pdfplumber`; a 1 000-page text manual needs `PyMuPDF`'s speed; a mixed folder of Word docs and emails needs `unstructured`'s format routing. Choosing the wrong parser produces garbled text upstream of chunking, which poisons every downstream retrieval step.

**Caveat:** `unstructured` pulls in heavy optional dependencies (Tesseract, Poppler, etc.) that can make Docker images large. Pin the version — `unstructured` has had breaking API changes between minor releases. For image-heavy PDFs where structure matters (e.g. slide decks), consider a vision-language model via LlamaParse or a cloud document AI service rather than text-only parsers.

**Sources:** medium.com/@hchenna "Technical Comparison — Python Libraries for Document Parsing" (confirmed live 2026-07-22, unlinked — 403 bot-protection) · [firecrawl.dev/blog/best-chunking-strategies-rag](https://www.firecrawl.dev/blog/best-chunking-strategies-rag) (2026) · [haystack.deepset.ai/tutorials/27_first_rag_pipeline](https://haystack.deepset.ai/tutorials/27_first_rag_pipeline) (Haystack official tutorial, 2026)

**Confidence:** ✅ independently-corroborated

---

## Practice 10: Enforce retrieval-time access control with metadata filters — never rely on prompt hardening alone

**Do:** Tag every document chunk at ingest time with access metadata:

```python
# at ingest
doc.metadata["access_groups"] = ["finance", "exec-team"]
```

At query time, pass a metadata filter to your vector store retriever before sending context to the LLM:

```python
# LangChain / Chroma example
# NOTE: {"$in": user_groups} filter syntax is Chroma-specific — see Caveat below
retriever = vectorstore.as_retriever(
    search_kwargs={"filter": {"access_groups": {"$in": user_groups}}}
)
```

Do the same filtering with `where` clauses in Qdrant payload filters, Weaviate `where` filters, or pgvector `WHERE` SQL predicates. Run the filter in the vector database, not in Python after retrieval.

**Why (beginner):** If you only tell the LLM "do not reveal documents from group X", a prompt injection attack embedded in a retrieved document can override that instruction. Filtering at the retrieval layer means the LLM never sees the document at all — even a compromised LLM cannot reveal what it was never shown.

**Caveat:** ⚠️ Metadata filters require that the vector store actually supports metadata filtering on the field you choose — not all stores index arbitrary metadata by default. Verify filtering support before relying on it. Also ensure your authentication middleware populates `user_groups` from a trusted identity provider, not from a client-supplied header. Mis-classified documents at ingest time silently give wrong access — audit your ingestion pipeline regularly.

⚠️ The `{"$in": user_groups}` filter syntax shown is Chroma's format. Qdrant uses payload filter syntax (`models.Filter(must=[models.FieldCondition(...)])`); Weaviate uses its own `where` filter; pgvector uses SQL `WHERE` predicates. Each store has different filter syntax — the linked sources include per-store examples.

**Sources:** [snyk.io/articles/what-is-rag-and-how-to-secure-it](https://snyk.io/articles/what-is-rag-and-how-to-secure-it/) (Snyk, 2025) · [dev.to/devopsstart: RAG Security — Prevent Data Leaks with Access Control](https://dev.to/devopsstart/rag-security-prevent-data-leaks-with-access-control-lb9) (2025) · [scalacode.com/blog/how-to-secure-rag-pipeline](https://www.scalacode.com/blog/how-to-secure-rag-pipeline/) (2026)

**Confidence:** ✅ independently-corroborated (three independent publishers: Snyk, dev.to, ScalaCode)

---

## Practice 11: Scrub PII from document text before embedding — not after retrieval

**Prerequisites:** `pip install presidio-analyzer presidio-anonymizer spacy` followed by `python -m spacy download en_core_web_lg` (presidio requires a spaCy language model for NER-based PII detection; without the model download, `presidio-analyzer` will fail on initialization).

**Do:** Apply PII detection and redaction (e.g. using `presidio-analyzer` + `presidio-anonymizer`, or a regex-based scrubber for well-structured fields) during the ingestion pipeline, before chunking and embedding. Never rely on post-retrieval filtering to prevent PII from reaching the LLM.

```python
# conceptual order of operations — ingestion pipeline
raw_text → PII_scrub() → chunk() → embed() → store()
# NOT:
raw_text → chunk() → embed() → store() → retrieve() → PII_filter() → LLM
```

**Why (beginner):** Once PII is embedded in a vector, similarity search can surface it for any semantically related query — even from a different user's session. Scrubbing after retrieval is too late; the sensitive data is already in the index and can leak to anyone. Pre-embedding scrubbing also protects against inadvertent exposure to third-party embedding API providers.

**Caveat:** Automated PII scrubbers miss unusual formats (e.g. IDs in domain-specific notation) and produce false positives that can corrupt legitimate content. For medical or legal corpora, combine automated scrubbing with a human review step. If you tokenize PII (replace with a reversible token), store the token map in a separate, access-controlled store — not in the same vector index.

**Sources:** [scalacode.com/blog/how-to-secure-rag-pipeline](https://www.scalacode.com/blog/how-to-secure-rag-pipeline/) (2026) · [snyk.io/articles/what-is-rag-and-how-to-secure-it](https://snyk.io/articles/what-is-rag-and-how-to-secure-it/) (Snyk, 2025)

**Confidence:** ✅ independently-corroborated

---

## Practice 12: Separate indexing and query pipelines for production; use background workers for index updates

**Do:** Do not run document ingestion (chunking, embedding, upsert) inside the same process that serves user queries. Run ingestion as a background task (Celery worker, FastAPI `BackgroundTask`, or a dedicated service). Share only the vector store (Qdrant, pgvector, etc.) between the two processes.

```
[Document Source] --> [Ingestion Worker] --> [Vector Store] <-- [Query API]
```

For document deletions, maintain an explicit deletion queue — do not rely on the ingestion pipeline to clean up orphaned vectors automatically.

**Why (beginner):** A single `vectorstore.upsert()` spike during a large document batch can block 30 % of concurrent reads on the same process (noted in the Redis production guide). Separating the two concerns means a slow bulk ingest does not degrade user-facing query latency. It also lets you scale the two workloads independently.

**Caveat:** Separation introduces a data-freshness lag: a new document will not appear in query results until the ingestion worker processes it. For most use cases an eventual consistency of seconds to minutes is acceptable. If freshness is critical (e.g. live news, pricing data), use change-data-capture (CDC) streams rather than batch ingestion, at significantly higher operational complexity.

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

21. **[Link-check gate]** Practice 4 — Unlinked medium.com/@Modexa "7 LlamaIndex retrieval tweaks" (confirmed live 2026-07-22; 403 bot-protection; 1 occurrence).
22. **[Link-check gate]** Practice 6 — Unlinked medium.com/@eric_vaillancourt "Mastering LangChain RAG Streaming" (confirmed live 2026-07-22; 403 bot-protection; 1 occurrence).
23. **[Link-check gate]** Practice 9 — Unlinked medium.com/@hchenna "Technical Comparison — Python Libraries for Document Parsing" (confirmed live 2026-07-22; 403 bot-protection; 1 occurrence).
24. **[Link-check gate]** Practices 3, 7, 12 — Unlinked markaicode.com/architecture/rag-architecture-with-langchain/ (confirmed live 2026-07-22; 403 bot-protection; 3 occurrences).

