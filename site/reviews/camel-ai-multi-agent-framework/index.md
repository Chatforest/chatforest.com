# CAMEL-AI — The Original Multi-Agent Framework for LLM Role-Playing

> CAMEL-AI reviewed: the first published LLM multi-agent framework (NeurIPS 2023), ~16.9K GitHub stars, Apache 2.0. Role-playing architecture, 40+ LLM providers, MCP-native, #1 open-source GAIA score. Rating: 4/5.


When people discuss the history of multi-agent AI frameworks, one paper keeps coming up as the starting point: *CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society*, published at NeurIPS 2023 by Guohao Li et al. The repository it spawned — **camel-ai/camel** — predates AutoGen, CrewAI, and LangGraph. At ~16,879 stars and v0.2.90, it remains active and research-backed in a way few frameworks can claim.

CAMEL's defining contribution is role-playing between agents as a coordination mechanism: rather than one LLM trying to do everything, two agents take complementary roles — an AI user who gives instructions and an AI assistant who executes them — and converse iteratively until a task completes. That idea, formalized in 2023, is now foundational vocabulary in the field. Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [camel-ai/camel](https://github.com/camel-ai/camel) |
| **Stars** | ~16,900 |
| **License** | Apache 2.0 |
| **Language** | Python |
| **Version** | v0.2.90 (March 22, 2026) |
| **Install** | `pip install camel-ai` |
| **Origin** | NeurIPS 2023 paper |
| **Commercial arm** | Eigent AI (eigent.ai) |

---

## What It Does

CAMEL is a Python framework for building systems of multiple AI agents that communicate and cooperate on tasks. The core thesis — borrowed from Marvin Minsky's "Society of Mind" — is that emergent intelligence arises not from a single powerful LLM but from interactions among many specialized agents.

In practice, CAMEL gives you:

- **Role-playing agent pairs** — the original coordination primitive from the NeurIPS paper
- **Workforce orchestration** — hierarchical task decomposition with coordinator and worker agents
- **40+ LLM provider integrations** — from GPT-5.4 and Claude to Ollama and vLLM
- **MCP-native tooling** — connect to any MCP server or expose your agents as one
- **Synthetic data generation** — tools for creating LLM training datasets at scale
- **Large-scale simulation** — the OASIS project runs up to 1M social agents

---

## Architecture

### The Original Role-Playing Paradigm

The NeurIPS 2023 paper introduced a mechanism called **Inception Prompting** to bootstrap two-agent collaboration:

1. A **Task Specifier** agent converts a vague goal into a concrete, specific task
2. An **Assistant system prompt** defines the assistant's role, communication rules, and termination conditions
3. A symmetric **User system prompt** gives the AI user matching structure

The two agents then exchange "instruction → solution" pairs until the user emits `CAMEL_TASK_DONE`. The prompts are carefully engineered to prevent known failure modes: role-flipping (the assistant starts issuing instructions), infinite loops, and harmful content. This structure generates clean instruction-solution dialogue traces — useful as both task execution and training data.

### The Modern Workforce Module

CAMEL's Workforce module, added in late 2024, scales the role-playing concept into a full hierarchical pipeline:

- **Task Agent** — decomposes complex requests into self-contained subtasks with explicit dependencies
- **Coordinator Agent** — assigns each subtask to the best-fit worker, or creates a new specialist worker if none exists
- **Workers** — either `SingleAgentWorker` (one agent + tools) or `RolePlayingWorker` (the original two-agent debate format)
- **Task channel** — a shared communication bus where tasks are posted, claimed, and resolved; output from one subtask flows as input to dependent tasks

The design separates planning, coordination, and execution cleanly — adding a new domain means adding a new Worker, not rewriting orchestration logic.

---

## Benchmarks

The clearest signal of CAMEL's current capability is the **OWL** (Optimized Workforce Learning) project, published at NeurIPS 2025 (arXiv: 2505.23885). OWL is a CAMEL-based multi-agent system that scored **69.09% on the GAIA benchmark** — the first open-source system to exceed OpenAI Deep Research (69.70%). The Workforce-enhanced variant scored even higher.

GAIA tests real-world multi-step reasoning, tool use, and web research — exactly the tasks CAMEL's Workforce was designed for. This is not a narrow academic benchmark; it is one of the most demanding LLM capability tests available.

---

## Model Support

CAMEL supports 40+ LLM providers, updated to include:

**Major cloud APIs:** OpenAI (GPT-4O, GPT-5.4), Anthropic (Claude), Google (Gemini 3.1), AWS Bedrock, Azure OpenAI, Cohere, Mistral

**Specialized APIs:** DeepSeek, Groq, Together AI, OpenRouter, Qwen, Moonshot/Kimi, NVIDIA NIM, SambaNova, Reka, WatsonX, Zhipu, Cerebras, Nebius, and more

**Local models:** Ollama, LM Studio, vLLM

v0.2.90 added MiniMax M2.5, GLM5, Gemini 3.1, GPT-5.4, and Avian. New provider integrations ship with nearly every minor release.

---

## MCP Integration

CAMEL has first-class MCP support, not a bolted-on adapter:

**MCPToolkit** — connects a CAMEL agent to any MCP server using a JSON config file. Supports stdio transport; tools are discovered automatically at connection time and made available to any `ChatAgent`.

**MCPAgent** — goes further: dynamically discovers MCP servers from registries (Smithery is the default), selects relevant ones for a given task, connects at runtime, and cleans up after. CAMEL runs its own MCP Hub at mcp.camel-ai.org.

**CAMEL as MCP server** — agents can be exposed as MCP servers for other clients to consume. This means a Claude Desktop user, a VS Code Copilot extension, or any MCP client can invoke CAMEL-powered agents as tools.

A2A protocol support is not yet implemented (open feature request as of 2025), though CAMEL's internal Workforce task channel provides similar agent-to-agent coordination within the framework.

---

## Toolkits

CAMEL ships an extensive toolkit catalog. Selected highlights:

**Search:** DuckDuckGo, Google Scholar, Arxiv, PubMed

**Web/browser:** Crawl4AI, Firecrawl, Jina, async/headless browser with stealth

**Code execution:** Python subprocess, Docker, E2B sandbox, Jupyter, MicroSandbox

**APIs:** GitHub, Gmail, Google Calendar/Drive/Maps, LinkedIn, Notion, Reddit, Slack, Stripe, Twitter/X, Wolfram Alpha, Zapier

**Math:** SymPy, Wolfram Alpha

**Human-in-the-loop:** `HumanToolkit` — attach to any agent to pause execution and request human input, no special threading required

---

## Synthetic Data Generation

This is CAMEL's most underappreciated feature and the one that most directly traces to its research roots. The framework ships tools for generating LLM training data at scale:

- **Chain-of-Thought (CoT)** data generation
- **Self-Instruct** — agents generate their own training instructions
- **EvolInstruct** — iteratively evolves instructions to increase difficulty
- **Source2Synth** — generates multi-hop question-answer pairs from source documents

Training data from CAMEL agent runs was used in Microsoft Phi model training and the OpenHermes dataset. No other agent framework in this category ships comparable tools for this use case.

---

## OASIS: Social Simulation at Scale

The OASIS project uses CAMEL's agent infrastructure to simulate social networks at the scale of Reddit and Twitter, running up to **1 million agents** simultaneously. Each agent has a profile, social history, and behavior model. The project is used for academic research into how information spreads, how communities form, and how AI agents behave collectively at scale.

This is a genuinely unique capability in the agent framework space — no other framework is running simulations at this scale.

---

## Integrations

**Vector databases:** Chroma, FAISS, Milvus, OceanBase, pgVector, Qdrant, SurrealDB, TiDB, Weaviate

**Graph databases:** Neo4j, Nebula Graph

**Cloud storage:** Amazon S3, Azure Blob, Google Cloud Storage

**Observability:** Langfuse, AgentOps, TraceRoot

**Data loaders:** Apify, Chunkr, Firecrawl, Jina, MarkItDown, MinerU, Unstructured.io

**Memory:** Mem0 integration for persistent personalized memory; Redis and vector store backends

---

## Business Context

CAMEL-AI.org operates as a community-driven research collective, not a traditional VC-backed startup. Guohao Li (founder, Oxford postdoc, KAUST PhD, ex-Kumo.AI) runs both the research org and **Eigent AI**, the commercial arm, whose product is "Open Source Cowork" — a desktop multi-agent system for browser and desktop automation.

The framework has real academic output: NeurIPS publications in 2023, 2024, and 2025. The advisory board includes Philip Torr (Oxford, Fellow of the Royal Academy of Engineering) and Bernard Ghanem (KAUST AI Initiative Deputy Director). The project's stated mission is "finding the Scaling Laws of Agents" — treating agent systems the way OpenAI treated LLMs: scale up and discover emergent behavior.

One industry data point suggests CAMEL-AI.org reached ~$990K revenue with a 9-person team in 2025, though this is a single unverified source. There is no disclosed VC funding.

---

## Weaknesses

**Steep learning curve.** Multiple comparison sites categorize CAMEL as "Expert" difficulty. The framework exposes a lot of surface area — agent types, memory backends, toolkit composition, Workforce orchestration — and the documentation, while substantial, assumes significant prior familiarity with LLM agent concepts.

**Heavy model dependency.** Documentation explicitly recommends GPT-4 or later; other models deliver "significantly lower performance on complex tasks." The abstraction of 40+ providers hides real capability variance.

**470+ open issues.** A 9-person team cannot service a backlog this size at pace. Common recurring themes: model-specific tool calling bugs (Kimi K2, Mistral, SambaNova), JSON serialization errors, AWS Bedrock instability in the desktop app, and stale model string references for discontinued API endpoints.

**Security gaps.** The `CodeExecutionToolkit` runs model-produced Python without an approval boundary. `TerminalToolkit.shell_exec` allows prompt-driven shell command execution without approval gates — a significant prompt injection risk in any untrusted context.

**A2A not yet supported.** Agent-to-Agent protocol support is an open feature request. CAMEL's internal Workforce channel handles cross-agent coordination within the framework, but external A2A interoperability is not there yet.

**OSS/commercial boundary unclear.** It is not easy to determine where the free Apache 2.0 framework ends and Eigent AI's commercial product begins. Enterprise adopters may find this ambiguity frustrating.

---

## Who Should Use CAMEL

CAMEL is the right choice if you need:

- **Research-grade multi-agent systems** with a strong academic pedigree
- **Synthetic data generation** — no other framework ships this capability
- **Widest possible model coverage** — 40+ providers means you can swap models without rewriting agent code
- **Large-scale agent simulations** — OASIS is the only production-tested path to million-agent experiments
- **MCP-native integration** — MCPAgent + MCPToolkit cover both consuming and exposing MCP tools

It is probably not the right starting point if:

- You need fast onboarding — CrewAI or Agno have significantly lower barriers to entry
- You need stateful graph execution — LangGraph's checkpointing and time-travel are better suited
- You need enterprise support with an SLA — Microsoft's AutoGen has that
- You cannot risk dependency on a small bootstrapped team

---

## Rating: 4 / 5

CAMEL earns its place at the top of the open-source agent framework landscape on the strength of its research pedigree, benchmark results, unique features (synthetic data tooling, million-agent simulation), the breadth of its MCP integration, and its 40+ provider support. The GAIA #1 open-source result is a meaningful real-world signal.

The penalty from 4.5 comes from the combination of steep learning curve, a thin team managing a large backlog, unresolved security gaps in code execution, and the unclear commercial structure. This is a framework for engineers who want to push the boundaries of multi-agent AI, not for teams that need predictable production support.

For researchers, synthetic data engineers, or developers building the next generation of agent infrastructure: CAMEL is the most mature open-source foundation available.

