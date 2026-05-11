# LlamaIndex — The RAG-First Agent Framework with 78 Vector Store Integrations

> LlamaIndex reviewed: the dominant RAG framework for LLM applications. 49.1K stars, MIT, Python, v0.14.21. Deep data integration (78 vector stores, 104 LLMs), event-driven Workflows, MCP client and server support. Rating: 4.5/5.


Most agent frameworks treat data retrieval as a feature. LlamaIndex treats it as the whole point.

Since Jerry Liu launched it in 2022, LlamaIndex has built the most comprehensive data integration layer in the agent ecosystem: six index types, 78 vector store backends, 104 LLM providers, and a commercial document parsing product that handles 50+ file types including handwriting and complex tables. The framework's thesis — that connecting private and domain data to LLMs is the core challenge of building useful AI applications — has proven correct enough that it now has 49,100 GitHub stars and 6.8 million monthly PyPI downloads.

This is a review of what that looks like in practice: where LlamaIndex excels, what it doesn't do, and who should use it.

Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [run-llama/llama_index](https://github.com/run-llama/llama_index) |
| **Stars** | ~49,100 |
| **Forks** | ~7,400 |
| **License** | MIT |
| **Language** | Python (≥3.10) |
| **Version** | v0.14.21 (April 21, 2026) |
| **Install** | `pip install llama-index` |
| **Authors** | Jerry Liu (creator), Logan Markewich; maintained by LlamaIndex, Inc. |
| **Downloads** | ~6.8M monthly PyPI downloads |
| **Commercial product** | LlamaParse — enterprise document parsing/OCR |

---

## The Core Idea: Context Augmentation

LlamaIndex is built around a specific problem: LLMs are trained on public data, but most valuable enterprise knowledge lives in private documents, databases, and APIs that no LLM has seen. The solution is context augmentation — retrieving the right private data and injecting it into the LLM's context at inference time.

This is what RAG (Retrieval-Augmented Generation) means in practice, and LlamaIndex systematizes it into a five-stage pipeline:

1. **Load** — ingest data from any source (PDFs, databases, APIs, websites)
2. **Index** — structure that data for efficient retrieval
3. **Store** — persist the indexed data somewhere queryable
4. **Query** — retrieve the right data and synthesize a response
5. **Evaluate** — measure retrieval quality and response accuracy

Every other major framework treats some subset of these stages as one feature among many. LlamaIndex has built dedicated primitives, integrations, and best practices for each stage.

---

## Core Abstractions

### Documents and Nodes

Everything starts with a `Document` — a raw data representation with text content and metadata. A PDF becomes a Document; a database row becomes a Document; a GitHub issue becomes a Document. LlamaIndex ships with dozens of data connectors for common sources.

Documents are then processed into `Node` objects — chunked, cleaned, and enriched pieces of the original content. Nodes are the atomic retrieval unit: the chunk that gets scored against a query, embedded into a vector, and retrieved when relevant. How you chunk matters: LlamaIndex provides a range of text splitters, token splitters, and semantic chunking strategies.

### Indices

The six index types are where LlamaIndex's data layer becomes concrete:

| Index | Use case |
|-------|----------|
| `VectorStoreIndex` | Vector similarity search — the default for most RAG applications |
| `SummaryIndex` | Iterative summarization across all nodes — good for full-document synthesis |
| `DocumentSummaryIndex` | Per-document summaries for intelligent routing |
| `KnowledgeGraphIndex` | Triplet-based knowledge graph construction and traversal |
| `PropertyGraphIndex` | Rich property graph with structured metadata — enables graph-RAG |
| `KeywordTableIndex` | Sparse keyword-based retrieval for exact match |

Most applications start with `VectorStoreIndex` and never need the others. But the others exist for real use cases: `PropertyGraphIndex` for knowledge graph reasoning, `DocumentSummaryIndex` for routing queries across large document collections, `KeywordTableIndex` when exact term matching matters.

### Query Engines and Chat Engines

A `QueryEngine` wraps an index and answers natural language questions in a single call. A `ChatEngine` wraps a query engine and adds conversational memory — questions are contextual, referring to previous exchanges. These are LlamaIndex's user-facing interfaces for the RAG pipeline.

Advanced retrieval techniques are layered on top:

- **Sub-question query engine** — decomposes complex multi-part questions into sub-questions, routes each to the appropriate index, and synthesizes the combined results
- **HyDE** (Hypothetical Document Embeddings) — generates a hypothetical answer to use as the retrieval query, improving semantic match quality
- **RouterQueryEngine** — selects the right index or query engine based on the question's nature
- **Query fusion** — runs multiple retrievers and combines results
- **Re-ranking** — node postprocessors that score and filter retrieved chunks before response synthesis

### StorageContext

LlamaIndex decouples the storage layer from the indexing logic. `StorageContext` provides a unified configuration point for four pluggable backends:

- **Document store** — raw document storage
- **Index store** — index metadata and structure
- **Vector store** — the embeddings and their associated metadata
- **Chat store** — conversation history

This separation means you can build a production system where the vector store is Pinecone, the document store is S3, and the chat store is Redis — all configured through a single object.

---

## RAG Depth: 78 Vector Store Integrations

The headline number is 78 vector store integrations. This is the broadest support of any agent framework:

**Major providers**: Pinecone, Weaviate, Qdrant, Chroma, FAISS, LanceDB, Milvus, MongoDB, Elasticsearch, OpenSearch, Redis, Cassandra, Neo4j, Supabase, DuckDB, pgvecto-rs, Azure AI Search, Vertex AI Vector Search

**Regional providers**: Alibaba Cloud, Baidu VectorDB, Tencent Cloud VectorDB, Oracle Vector, IBM Db2, Volcano Engine — breadth that LangChain and CrewAI don't match

**Database-native**: PostgreSQL (via pgvector and pgvecto-rs), SQLite, DuckDB — for teams that want to keep vectors in their existing database

The practical consequence: LlamaIndex can meet your team where your data already is. If your company runs on MongoDB, there's a native integration. If you're on Cassandra, there's a native integration. If you want the simplest possible start with zero infrastructure, `VectorStoreIndex` uses an in-memory store by default.

---

## Agent Capabilities

LlamaIndex has evolved significantly in the agent space. The current architecture centers on three agent types:

**FunctionAgent** — the primary agent for tool-calling workflows. Takes a list of tools, an LLM, and an optional memory object. Generates tool calls in the LLM's native function-calling format (OpenAI-style, Anthropic-style, etc.).

**ReActAgent** — uses the classic ReAct (Reason → Act → Observe) prompting strategy. Works with any LLM, not just those with native function-calling support.

**CodeActAgent** — an alternate prompting approach focused on generating code to express actions.

```python
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.tools import FunctionTool

def get_weather(city: str) -> str:
    """Returns current weather for a city."""
    return f"Sunny, 22°C in {city}"

agent = FunctionAgent(
    tools=[FunctionTool.from_defaults(fn=get_weather)],
    llm=llm,
    system_prompt="You are a helpful assistant."
)
```

### Workflows: Event-Driven Pipelines

The `Workflow` system is LlamaIndex's most powerful abstraction for complex, multi-step pipelines. Workflows are defined as classes with `@step`-decorated methods connected by typed Events:

```python
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step

class MyWorkflow(Workflow):
    @step
    async def process_query(self, ev: StartEvent) -> StopEvent:
        # retrieve, generate, return
        result = await self.run_agent(ev.query)
        return StopEvent(result=result)
```

Typed events act as a form of compile-time routing — a step that emits a `RetrievedEvent` can only be received by steps that accept `RetrievedEvent`. This makes the control flow explicit and debuggable. It's more structured than LangChain's LCEL, and closer to LangGraph's graph model — but without requiring explicit graph construction.

Workflows support:
- **Concurrent step execution** — steps can run in parallel when they emit compatible events
- **State serialization** via `ctx.to_dict()` / `Context.from_dict()` for checkpointing
- **Human-in-the-loop** — workflows can pause and wait for external input between steps
- **DBOS integration** for durable execution — survives process restarts

### Multi-Agent Patterns

LlamaIndex supports three multi-agent patterns at increasing complexity:

**1. AgentWorkflow** (recommended starting point) — built-in linear handoff. The active agent passes control to the next agent via a tool call. Simple to configure, limited to sequential hand-offs:

```python
from llama_index.core.agent.workflow import AgentWorkflow

workflow = AgentWorkflow(
    agents=[researcher, writer, reviewer],
    root_agent="researcher"
)
result = await workflow.run("Write a report on AI agent frameworks")
```

**2. Orchestrator Agent** — a central coordinator with specialist agents as callable tools. The orchestrator decides when to invoke each specialist; control returns to the orchestrator after each call. More flexible than AgentWorkflow, analogous to CrewAI's hierarchical process.

**3. Custom Planner** — define the coordination logic yourself via structured prompts (XML/JSON plans), parsed and executed imperatively. Maximum flexibility, maximum implementation cost.

None of these approaches is as mature as LangGraph's explicit graph model for truly complex stateful orchestration. But for most multi-agent use cases, the AgentWorkflow and Orchestrator patterns are sufficient.

---

## Memory System

LlamaIndex's memory system has undergone significant evolution. The current model unifies short-term and long-term memory through a `Memory` class:

**Short-term**: A FIFO message queue (`ChatMemoryBuffer`) with a configurable token limit. Messages are dropped oldest-first when the limit is reached.

**Long-term memory blocks** — three types that compose:
- `StaticMemoryBlock` — fixed context injected into every prompt (user preferences, system facts)
- `FactExtractionMemoryBlock` — LLM extracts facts from conversation history and stores them as durable knowledge
- `VectorMemoryBlock` — past messages embedded into a vector store, retrieved semantically when relevant to the current query

This tiered approach is more sophisticated than smolagents (in-process only) and CrewAI's LanceDB memory, though less fully integrated than Agno's built-in four-level memory stack.

State persistence for Workflows uses `ctx.to_dict()` with JSON serializers. For production durability, LlamaIndex recommends DBOS integration, which provides crash-recovery guarantees — a differentiator that most frameworks lack.

---

## MCP Support

MCP support is provided via `llama-index-tools-mcp` (v0.4.8, requires `mcp>=1.24.0`).

**Install**: `pip install llama-index-tools-mcp`

### As MCP Client

`BasicMCPClient` connects to any MCP server over three transports:
- **Streamable HTTP** — default for HTTP/HTTPS endpoints
- **SSE** — detected via `/sse` URL patterns or `?transport=sse` query parameter
- **stdio** — spawns a local subprocess via `StdioServerParameters`

`McpToolSpec` wraps a `BasicMCPClient` and converts MCP tools into LlamaIndex `FunctionTool` objects that any agent can use:

```python
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

client = BasicMCPClient("https://my-mcp-server.example.com/mcp")
tool_spec = McpToolSpec(client=client, allowed_tools=["search", "fetch"])
tools = tool_spec.to_tool_list()

agent = FunctionAgent(tools=tools, llm=llm)
```

Additional features:
- `include_resources=True` — exposes MCP resources as tools (not just tool calls)
- `get_tools_from_mcp_url()` — convenience helper for direct tool extraction
- **OAuth 2.0 authentication** with customizable token storage

### As MCP Server

`workflow_as_mcp()` converts any LlamaIndex Workflow into an MCP-compatible server application:

```python
from llama_index.tools.mcp import workflow_as_mcp

mcp_app = workflow_as_mcp(MyWorkflow)
# launch with: mcp dev script.py
```

This is the cleanest "expose LlamaIndex as MCP" mechanism of any framework reviewed — it operates at the Workflow level, meaning any multi-step pipeline with human-in-the-loop, state management, and tool orchestration can become an MCP endpoint. Smolagents and LangGraph do not have an equivalent.

---

## LLM Support: 104 Integrations

LlamaIndex supports 104 LLM integrations. The major categories:

| Provider | Notes |
|----------|-------|
| OpenAI | GPT-4o, GPT-4o-mini, o3, o4-mini |
| Anthropic | Claude 3.5/4.x family |
| Azure OpenAI | Azure-hosted OpenAI deployments |
| Google | Vertex AI, Gemini API (Google GenAI) |
| AWS | Bedrock (native) + Bedrock Converse |
| Mistral AI | Native integration |
| Groq | Ultra-fast inference |
| Ollama | Local inference |
| HuggingFace | Hub API + local Transformers |
| LiteLLM | 100+ additional providers via proxy |
| DeepSeek, Fireworks, Together, Replicate, SageMaker | Additional cloud providers |
| Databricks, IBM, NVIDIA TensorRT/Triton | Enterprise and hardware-accelerated |

LiteLLM as a provider effectively unlocks the entire ecosystem — any model LiteLLM supports becomes available to LlamaIndex without an additional integration.

---

## Observability

LlamaIndex has first-class observability support, with a shift from the legacy `CallbackManager` to a modern instrumentation module:

**LlamaTrace / Arize Phoenix** — the flagship observability partnership. Hosted platform with LLM Traces, LLM Evals, and dataset management. One-liner setup:

```python
import llama_index.core
llama_index.core.set_global_handler("arize_phoenix")
```

**OpenTelemetry** — full trace instrumentation of all LlamaIndex events. Integrates with any OTEL-compatible backend (Jaeger, Zipkin, Datadog, etc.).

**MLflow Tracing** — one-click instrumentation via `mlflow.llama_index.autolog()`.

**W&B Weave** — automatic patching and call tracking.

**Langfuse** — OpenInference instrumentation (modern path) + deprecated callback handler.

**SigNoz** — OTEL-based traces, logs, and metrics.

This is the deepest observability integration of any agent framework reviewed. LangGraph has LangSmith; LlamaIndex has a broader menu of options including open-source backends.

---

## LlamaHub and the Ecosystem

LlamaHub (llamahub.ai) is LlamaIndex's community marketplace for data loaders, agent tools, Llama Packs (pre-built pipelines), and Llama Datasets. The structure mirrors HuggingFace Hub but for data integration artifacts rather than models.

The practical value: if you want to ingest data from Notion, Google Drive, GitHub, Confluence, Slack, or dozens of other sources, there's likely a community-maintained data loader that handles the authentication, pagination, and metadata extraction. You don't start from scratch.

LlamaParse extends this commercially: a dedicated document parsing product with VLM-powered understanding of 50+ file types, handling of complex tables, charts, handwriting, and multi-column layouts — the hard cases that naive PDF-to-text conversion fails on. HIPAA, GDPR, SOC2 compliant. 10,000 free monthly pages; enterprise pricing above that. It integrates directly with the OSS framework as a `DocumentReader`.

---

## Limitations

**Agent orchestration is secondary.** LlamaIndex's three multi-agent patterns work, but they're less mature than LangGraph's explicit graph model or CrewAI's role-based crew system. For teams building complex stateful multi-agent systems, LangGraph is the stronger choice; for teams building data-intensive single-agent or simple multi-agent pipelines, LlamaIndex is.

**Fragmented documentation from API churn.** The framework has undergone multiple significant revisions: `ChatMemoryBuffer` deprecated in favor of `Memory`, `CallbackManager` deprecated for the instrumentation module, various agent APIs replaced. This means many tutorials and Stack Overflow answers reference the old way. The official docs are generally current, but third-party resources often aren't.

**Heavy dependencies.** The core package pulls in SQLAlchemy, tiktoken, nltk, networkx, and pillow even for simple use cases. Not unusual for a framework of this scope, but worth knowing if you're building a minimal deployment.

**No built-in MCP server beyond Workflow wrapping.** `workflow_as_mcp()` is a clean mechanism, but it requires your entrypoint to be a LlamaIndex Workflow. If you want to expose arbitrary functions or a query engine as MCP, you need to wrap it in a Workflow first.

**Version churn continues.** v0.14.21 with 21 patch releases in 2026 alone reflects active development — which is good — but also means integration packages sometimes lag behind core changes.

**Temporal data challenges.** No built-in mechanism for handling stale facts — a real limitation for applications where retrieved knowledge needs recency awareness.

---

## What It's Good For

LlamaIndex earns its 49,100 stars in a clear niche: **teams building LLM applications that depend on connecting to private or domain-specific data**.

If your application needs to answer questions over internal documents, query a database, process PDFs, or combine multiple data sources intelligently, LlamaIndex has the most complete solution: mature loading, indexing, retrieval, and evaluation infrastructure that other frameworks ask you to build yourself.

If you're specifically building a data-intensive pipeline — say, an enterprise knowledge base search, a contract review tool, a technical documentation Q&A system — LlamaIndex's five-stage RAG pipeline and 78 vector store integrations make it the most capable starting point.

For pure agent orchestration without significant data retrieval needs, LangGraph or CrewAI may be simpler. For multi-agent systems at production scale with complex state, LangGraph is the stronger choice. But most production AI applications involve data — and for those, LlamaIndex's depth is hard to match.

---

## Rating: 4.5/5

LlamaIndex is the most complete data integration framework in the agent ecosystem. The five-stage RAG pipeline, 78 vector store integrations, 104 LLM providers, and LlamaHub ecosystem represent years of investment in the unglamorous but critical work of connecting LLMs to real data. The event-driven Workflow system is well-designed, the `workflow_as_mcp()` server mechanism is uniquely capable, and the observability integrations are the deepest of any framework reviewed.

The half-point deduction reflects real gaps: agent orchestration is secondary to data retrieval (LangGraph is better for complex multi-agent state), documentation fragmentation from API churn creates friction, and the framework's breadth means there's more to learn before productivity kicks in compared to more opinionated frameworks like CrewAI.

| Capability | Notes |
|-----------|-------|
| **MCP Client** | ✓ stdio, SSE, Streamable HTTP (llama-index-tools-mcp) |
| **MCP Server** | ✓ workflow_as_mcp() — any Workflow becomes MCP endpoint |
| **Multi-agent** | AgentWorkflow (handoff), Orchestrator, Custom Planner |
| **Memory/persistence** | Tiered (short-term FIFO + long-term blocks); Workflow checkpointing; DBOS for durability |
| **Human-in-the-loop** | ✓ Workflow step pausing |
| **RAG depth** | 6 index types, 78 vector stores — best in class |
| **LLM support** | 104 integrations |
| **Observability** | Arize Phoenix, OpenTelemetry, MLflow, W&B Weave, Langfuse |
| **Language** | Python only |
| **License** | MIT |
| **API stability** | Stable core; active integration churn |

