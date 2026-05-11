# Haystack — Production-Grade LLM Pipelines from deepset

> Haystack reviewed: the production-first Python framework for RAG, agents, and LLM pipelines. Type-safe graph-based pipelines, 20 document stores, MCP client support, and enterprise observability. 25K stars, Apache 2.0, ~729K monthly PyPI downloads. Rating: 4/5.


Most LLM frameworks let you chain things together. Haystack makes you *declare* the contract between them — at connect time, with type checking, before anything runs.

Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [deepset-ai/haystack](https://github.com/deepset-ai/haystack) |
| **Stars** | ~25,100 |
| **Forks** | ~2,763 |
| **License** | Apache 2.0 |
| **Language** | Python |
| **Version** | v2.28.0 (April 20, 2026) |
| **Install** | `pip install haystack-ai` |
| **Authors** | deepset GmbH (Berlin; Milos Rusic, Malte Pietsch, Timo Möller) |
| **Downloads** | ~729K monthly PyPI downloads |
| **Founded** | 2019 (v2.0 rewrite: early 2024) |

---

## The Core Idea: Pipelines as Typed Graphs

Haystack is built around one central abstraction: the **Pipeline**. Not a chain, not a sequence — a directed multigraph of **Components** connected by explicitly typed input/output edges.

Every component declares what it takes in and what it produces. Every connection is validated at the time you call `pipeline.connect()`, not when you run it. If you try to pipe a `List[Document]` into a slot expecting a `str`, Haystack tells you immediately. This distinction matters in production: pipeline misconfiguration errors surface at development time, not at 3 AM when a user triggers an unexpected path.

```python
from haystack import Pipeline
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.components.builders import PromptBuilder
from haystack.components.generators import OpenAIChatGenerator

pipeline = Pipeline()
pipeline.add_component("retriever", InMemoryBM25Retriever(document_store=store))
pipeline.add_component("prompt_builder", PromptBuilder(template=template))
pipeline.add_component("llm", OpenAIChatGenerator(model="gpt-4o-mini"))

pipeline.connect("retriever.documents", "prompt_builder.documents")
pipeline.connect("prompt_builder.prompt", "llm.messages")

result = pipeline.run({"retriever": {"query": "What causes Aurora Borealis?"}})
```

Pipelines serialize to YAML — every component, every connection, every configuration parameter — which makes them version-controllable, shareable, and editable outside Python. They support branching, parallel paths (via `AsyncPipeline`), and loops, which Haystack uses to implement agentic correction cycles.

---

## Components: The Building Blocks

A component is a Python class decorated with `@component` that implements a typed `run()` method. 117 official and community integrations are available on [haystack.deepset.ai/integrations](https://haystack.deepset.ai/integrations).

The ecosystem covers every phase of an LLM application:

**Document processing:** converters (PDF, DOCX, PPTX, XLSX, HTML, Markdown), `DocumentSplitter` (fixed chunking), `EmbeddingBasedDocumentSplitter` (semantic chunking, v2.22.0), `MarkdownHeaderSplitter` (v2.24.0), `DocumentCleaner`, `DocumentDeduplicator`

**Retrieval:** BM25 retrievers, embedding-based retrievers, hybrid retrieval, multi-query expansion via `QueryExpander` + `MultiQueryTextRetriever` / `MultiQueryEmbeddingRetriever` (v2.21.0), `SentenceWindowRetriever`, `LLMRanker` for semantic reranking (v2.26.0)

**Generation:** chat and text generators for every major LLM provider (see LLM Support section), streaming via callbacks

**Tooling:** `Tool`, `ComponentTool`, `@tool` decorator, `PipelineTool`, `MCPTool`, `MCPToolset`, `Toolset`, `SearchableToolset`

Custom components written once can be published and reused across pipelines.

---

## RAG: The Original Strength

RAG is where Haystack began and where it remains strongest. The standard pattern splits into two independent pipelines:

**Indexing pipeline:** document converters → document splitter → text embedder → document writer

**Query pipeline:** retriever → prompt builder → LLM generator

This separation is deliberate. Indexing runs once (or on update); querying runs per user request. Keeping them separate makes each independently testable and scalable.

Haystack's **Document Store** abstraction provides a consistent interface over 20 backends:

| Backend | Type |
|---|---|
| Elasticsearch | Keyword + dense |
| OpenSearch | Keyword + dense |
| Azure AI Search | Managed |
| FAISS | In-memory vector |
| Qdrant | Vector |
| Milvus | Vector |
| Weaviate | Vector |
| Pinecone | Managed vector |
| Chroma | Lightweight vector |
| MongoDB | Document + vector |
| pgvector | PostgreSQL extension |
| AstraDB | Cassandra-based |
| Azure CosmosDB | Managed |
| SingleStore | HTAP |
| Supabase | Postgres SaaS |
| LanceDB | Embedded vector |
| Neo4j | Graph + vector |
| Couchbase | Multi-model |
| ArcadeDB | Multi-model |
| Valkey | Redis-compatible |

Every document store exposes its own Retriever components, so the interface is identical regardless of backend. Swapping from FAISS to Qdrant is a one-line change.

Advanced retrieval options include **hybrid search** (BM25 + embeddings combined), **multi-query retrieval** (v2.21.0 expands a query semantically before retrieving), and **LLM-based reranking** (v2.26.0's `LLMRanker` applies semantic relevance scoring after retrieval). Sentence-window expansion (`SentenceWindowRetriever`) provides context enrichment without reconfiguring the index.

---

## Agent Capabilities

Haystack's agent story is newer than its RAG story but has been advancing quickly. The universal `Agent` component implements a tool-using loop: the LLM decides which tool to call, the tool executes, the result feeds back to the LLM, repeat until the LLM produces a text response without a tool call or a maximum step count is hit.

**v2.28.0 (April 2026)** introduced **State injection for tools** — the biggest agent enhancement to date. Tools and components can declare a `State` parameter to receive and modify live agent state at invocation time without extra wiring. This enables tools that read conversation history, update shared memory, or coordinate across multi-agent hierarchies without the pipeline author having to manually route state.

Other agent features worth noting:

**Human-in-the-loop (v2.23.0):** Agents can pause before executing a tool and ask for human confirmation. Three modes: `always` (confirm every call), `once` (confirm on first invocation per tool), `never`. This is a genuine production feature — not a demo capability.

**Dynamic tool discovery via `SearchableToolset` (v2.25.0):** A BM25-based keyword search over large tool catalogs. When an agent has dozens or hundreds of tools available, the LLM context window can't hold all their descriptions. `SearchableToolset` lets the agent dynamically search for relevant tools at invocation time — only the matching tools are included in the context.

**Multi-agent composition:** Agents wrap other agents as `ComponentTool` or `PipelineTool`. There is no dedicated orchestration layer (unlike LangGraph's `StateGraph` or CrewAI's `Crew`), but full pipelines — including other agents — can be composed as tools within a parent agent.

**Dynamic system prompts (v2.26.0):** Jinja2-templated system prompts evaluate at runtime, allowing per-user customization without rebuilding the pipeline.

Tool creation has five paths:
1. `Tool` class — manual definition
2. `@tool` decorator — wraps Python functions  
3. `ComponentTool` — any Haystack component becomes a tool
4. `PipelineTool` — any Haystack pipeline becomes a tool
5. `MCPTool` / `MCPToolset` — tools loaded from MCP servers

---

## MCP Support

**MCP Client (consuming MCP servers):**

The `mcp-haystack` integration package provides MCP client capabilities:

```bash
pip install mcp-haystack
```

- **Version:** 1.3.0 (March 24, 2026); stable since v1.0.0 (November 2025)
- **Transports:** Streamable HTTP (`StreamableHttpServerInfo`), SSE (`SSEServerInfo`), StdIO (`StdioServerInfo`)
- **`MCPTool`:** connects to a single MCP server and exposes one tool; returns `TextContent`, `ImageContent`, or `EmbeddedResource`
- **`MCPToolset`:** connects to an MCP server and dynamically discovers and loads all its tools

The `MCPToolset` integration means any MCP server — hundreds of them — can be dropped into a Haystack agent without custom wrapper code. The tool catalog from an MCP server becomes part of the agent's available tools immediately.

**MCP Server (exposing Haystack as MCP):**

**Hayhooks** (`pip install hayhooks`) deploys Haystack pipelines as REST APIs and as MCP servers. Any deployed pipeline is automatically listed as an MCP Tool via SSE transport. Claude Desktop, Cursor, Windsurf, and other MCP clients can connect directly to a Hayhooks instance and invoke Haystack pipelines as tools.

---

## LLM Support

Haystack is LLM-agnostic by design. Swap providers without touching pipeline logic:

**Cloud providers:** OpenAI (including Responses API via `OpenAIResponsesChatGenerator`, v2.20.0), Azure OpenAI, Google Gemini + Vertex AI, Anthropic, Cohere, Mistral, Meta Llama, Amazon Bedrock, HuggingFace Inference API, NVIDIA, WatsonX, OpenRouter, Together AI, Fireworks, AIMLAPI

**Self-hosted/local:** `HuggingFaceLocalChatGenerator` (multimodal image-text-to-text as of v2.27.0), `LlamaCppChatGenerator`, `OllamaChatGenerator`, `vLLMChatGenerator`

**OpenAI-compatible passthrough:** DeepInfra, Anyscale, and any provider with an OpenAI-compatible API endpoint

All generators implement the same interface; a pipeline built with OpenAI can switch to Ollama by replacing one component.

---

## Observability

Haystack treats observability as a first-class concern, not an afterthought:

**Tracing backends:**
- **OpenTelemetry** — auto-detected when the SDK is installed; zero-config activation
- **Datadog** — via `ddtrace` library
- **Langfuse** — `LangfuseConnector` component inserted into any pipeline
- **MLflow** — native integration with token usage and cost tracking
- **Weights & Biases Weave** — `WeaveConnector` component
- **Custom** — implementable via `Tracer` interface
- **Local debugging** — `LoggingTracer` for inspection without external backend; Jaeger for local trace visualization

**What gets traced:** component execution order, per-component latencies, token usage and costs (MLflow), exceptions and errors, input/output content (opt-in, disabled by default for privacy).

The privacy default is notable. Haystack explicitly disables content tracing to prevent sensitive user data from leaving the system. Teams working with regulated data (healthcare, finance, legal) can use all observability features without risk of inadvertent data exposure.

---

## Production Context

Haystack is backed by deepset GmbH (Berlin, founded 2018), which raised $14M Series A (Google Ventures, 2022) and $30M Series B (Balderton Capital, 2023), and was named a Gartner Cool Vendor in AI Engineering in 2024. The framework has been in production longer than most of its competitors — Haystack 1.x dates to 2019 — and the Haystack 2.0 rewrite (early 2024) rebuilt on lessons from those years of enterprise deployment.

Enterprise users include **Airbus** (combined table + text QA for pilots and maintenance), **Lufthansa Industry Solutions** (AI knowledge assistant), **The Economist**, **Oxford University Press**, **European Commission**, **Netflix**, **Apple**, **LEGO**, and **Intel**. Notable 2025 partnerships: Meta (Llama Stack), MongoDB, NVIDIA, AWS, and PwC.

The framework has ~300 GitHub contributors, 4,000+ Discord members, and deepset has published one fine-tuned model with 52M+ HuggingFace downloads.

PyPI monthly downloads of ~729K are significantly below LangChain (~25M) and below LlamaIndex (~6.8M). Haystack occupies a narrower, more enterprise-focused niche — teams that want correctness and observability guarantees over rapid prototyping velocity.

---

## Limitations

**Steep learning curve.** The graph-based pipeline model requires understanding of typed component contracts, input/output connections, and the indexing vs. query pipeline distinction before you can do anything useful. Teams expecting LangChain-style quick iteration will find Haystack slower to start with.

**Complex setup.** The framework is not designed for non-technical users or quick prototypes. The upfront investment in proper component contracts pays off at scale, but it is a real investment.

**Haystack 1.x → 2.x migration pain.** The v2.0 rewrite was a near-complete break. Different package names (`farm-haystack` vs `haystack-ai`), different terminology (nodes → components), different document store architecture. Teams on 1.x faced significant migration work; this history produces some negative community sentiment.

**Breaking changes within 2.x.** v2.28.0 changed `Agent.run()` signatures, HTTP exception types (httpx replacing requests), and LLM component initialization — all in a minor version bump. Active development brings capability improvements at the cost of API stability in some areas.

**Smaller ecosystem than LangChain.** 117 integrations vs LangChain's larger catalog, and fewer community tutorials, Stack Overflow answers, and blog posts. Teams hitting edge cases have fewer community resources to draw on.

**No dedicated multi-agent orchestration.** Unlike LangGraph (StateGraph), CrewAI (Crew/Flow), or AG2 (GroupChat), Haystack has no first-class multi-agent coordination layer. Multi-agent systems are built via component composition — powerful but lower-level.

**Agent capabilities are maturing.** Human-in-the-loop, state injection, and SearchableToolset were all added in 2025-2026. The core agent architecture is solid, but the surrounding ecosystem of agent-specific tooling is less mature than the RAG ecosystem.

---

## Who Should Use Haystack

**Best fit:**
- Teams building production RAG systems who need correctness guarantees, not just demos
- Organizations with compliance or privacy requirements (explicit content tracing opt-in)
- Enterprise teams who want pipeline serialization for DevOps / version control workflows
- Projects that need to combine multiple document stores or swap backends without refactoring

**Look elsewhere if:**
- You need rapid prototyping with minimal upfront investment (LangChain)
- You need sophisticated multi-agent orchestration patterns (LangGraph, CrewAI, AG2)
- Your team is Python-non-technical (Haystack is code-first throughout)
- You're building on top of systematic prompt optimization (DSPy)

---

## Rating: 4 / 5

Haystack occupies a distinct position in the agent framework landscape: the production-correctness framework. Where LangChain prioritizes flexibility and rapid iteration, Haystack prioritizes type safety, pipeline verifiability, and observability-by-default. For enterprise teams building systems that need to be maintained over months and years — not just demonstrated — these properties matter.

The 20-backend document store abstraction is the strongest RAG infrastructure story of any reviewed framework. The observability setup (OTEL + Langfuse + MLflow + W&B, with privacy-safe defaults) is enterprise-grade. The bi-weekly release cadence of 2025-2026 has steadily upgraded the agent capabilities from an afterthought to a genuine feature set.

What holds it back from 4.5: the smaller ecosystem relative to LangChain and LlamaIndex, the steeper initial investment required, the lack of dedicated multi-agent orchestration, and the ~729K monthly PyPI volume that suggests a narrower practitioner base to draw community support from. These are real tradeoffs, not temporary gaps.

**For teams that prize correctness and maintainability in production LLM systems: Haystack is the strongest option in its class.**

---

*Reviewed 2026-05-06. Version v2.28.0. Ratings are the author's assessment based on publicly available information — we research and analyze; we do not test hands-on. See our [review methodology](/about/).*

