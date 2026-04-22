---
title: "Best AI & ML MCP Servers in 2026"
date: 2026-03-22T15:00:00+09:00
description: "Model serving, agent orchestration, LLM observability, evaluation, prompt engineering, and data preparation — we've reviewed 100+ AI & ML MCP servers across 6 categories."
og_description: "100+ AI & ML MCP servers reviewed across model serving, agent orchestration, LLM observability, evaluation, prompt engineering, and data preparation. HuggingFace, mcp-agent, Opik, promptfoo, and more — with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to AI & ML MCP servers in 2026. We've reviewed 100+ servers across model serving, agent orchestration, LLM observability, evaluation, prompt engineering, and data preparation. Every recommendation links to a full review."
last_refreshed: 2026-04-23
---

AI and ML is where MCP servers get recursive — AI agents using tools built for AI development. Model hubs, experiment trackers, evaluation frameworks, agent orchestration platforms, and prompt optimizers all have MCP integrations now. The result is a maturing ecosystem where your AI assistant can search for models, run local inference, orchestrate multi-agent workflows, monitor production LLM traces, evaluate outputs, and optimize prompts — without leaving the conversation.

We've published [10 in-depth AI & ML reviews](/reviews/) covering 100+ MCP servers across every stage of the AI development lifecycle. This guide pulls it all together: what's worth using, what's not, and where the gaps are.

## The short version

| Category | Our pick | Rating | Runner-up |
|----------|----------|--------|-----------|
| Model hubs & inference | [HuggingFace MCP](/reviews/ai-ml-model-serving-mcp-servers/) | 4/5 | [Ollama MCP](/reviews/ai-ml-model-serving-mcp-servers/) (153 stars, 14 tools, local inference) |
| Agent orchestration | [Paperclip](/reviews/agent-orchestration-mcp-servers/) | 4.5/5 | [mcp-agent (LastMile AI)](/reviews/agent-orchestration-mcp-servers/) (8.3K stars, workflow patterns) |
| LLM observability | [Opik MCP](/reviews/llm-observability-mlops-pipeline-mcp-servers/) | 3.5/5 | [OpenTelemetry MCP](/reviews/llm-observability-mlops-pipeline-mcp-servers/) (175 stars, vendor-neutral) |
| LLM evaluation | [promptfoo](/reviews/llm-evaluation-benchmarking-mcp-servers/) | 4/5 | [DeepEval](/reviews/llm-evaluation-benchmarking-mcp-servers/) (13K+ stars, Pytest-style) |
| Prompt engineering | [just-prompt](/reviews/prompt-engineering-optimization-mcp-servers/) | 3.5/5 | [mcp-prompt-optimizer](/reviews/prompt-engineering-optimization-mcp-servers/) (14 research techniques) |
| Data preparation | [Label Studio MCP](/reviews/annotation-data-labeling-mcp-servers/) | 2.5/5 | [PaddleOCR MCP](/reviews/ocr-document-intelligence-mcp-servers/) (72K parent stars) |

**Related guides:** [Best Vector Database MCP Servers →](/guides/best-vector-database-mcp-servers/) (Qdrant, Chroma, Milvus, Pinecone — the embedding and RAG layer), [Best Memory MCP Servers →](/guides/best-memory-mcp-servers/) (Zep/Graphiti, mem0 — agent memory).

## Model Serving & Inference — Search, Run, and Manage Models

**[Full review: AI & ML Model Serving MCP Servers →](/reviews/ai-ml-model-serving-mcp-servers/)** | Rating: 4/5 (up from 3.5)

This is the most natural MCP use case for ML engineers: searching model registries, running inference, and tracking experiments through your AI assistant instead of switching between notebooks and dashboards. The category crossed a maturity threshold since our last update — both dominant experiment tracking platforms (W&B and MLflow) now have official MCP support.

### The winner: HuggingFace MCP

[huggingface/hf-mcp-server](https://github.com/huggingface/hf-mcp-server) — 221 stars, 727 commits, 98 releases, TypeScript, v0.3.5, official. Core capabilities: **Hub search** for models, datasets, Spaces, and papers; documentation search with natural language queries; and **Gradio Space execution** — run any of the thousands of Gradio-based AI apps on HuggingFace Spaces directly through MCP. **New since March:** proxy tools via `PROXY_TOOLS_CSV` — load external MCP endpoint definitions at startup, turning any Gradio Space with an MCP badge into a callable tool with zero code. Three transport modes (stdio, StreamableHTTP, StreamableHTTPJson) with a management web interface. The breadth is what sets it apart: you're not just searching for models, you're executing them through hosted Spaces.

### Strong alternatives

**Ollama MCP** ([rawveg/ollama-mcp](https://github.com/rawveg/ollama-mcp)) — 153 stars, TypeScript, **14 tools covering the complete Ollama SDK**. Model management (list, show, pull, push, copy, delete, create), inference (generate, chat, embed), and process management. The best local inference story — every Ollama operation is one tool call away. Supports Ollama Cloud for hybrid local+cloud operation. 96%+ test coverage.

**Replicate** — two options. The community server (deepfates/mcp-replicate, 93 stars) has 13 tools but is **no longer actively maintained** since Replicate shipped an official remote server with Code Mode — two tools where the LLM writes and executes TypeScript against the Replicate SDK in a Deno sandbox, far more flexible than predefined tools.

**OpenAI bridge** ([pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai)) — 80 stars, single `ask-openai` tool. Simple but functional for cross-model workflows — ask GPT-4 a question from inside a Claude conversation.

**Experiment tracking:** Weights & Biases ([wandb/wandb-mcp-server](https://github.com/wandb/wandb-mcp-server), 49 stars, official, **14 tools** — expanded from 6, now covering experiment querying, Weave trace analysis, report generation, model registry, and documentation; also available as a **hosted server at mcp.withwandb.com**) and MLflow (now with an **official MCP server built into MLflow 3.5.1+** with 10 tools and Databricks integration, plus the community [kkruglik/mlflow-mcp](https://github.com/kkruglik/mlflow-mcp) with 17+ tools for experiment browsing and run comparison). Both major experiment tracking platforms now have official MCP support — choose based on which you already use.

## Agent Orchestration — Multi-Agent Workflows and Swarm Coordination

**[Full review: Agent Orchestration MCP Servers →](/reviews/agent-orchestration-mcp-servers/)** | Rating: 4.5/5 (up from 4)

This is where the MCP ecosystem gets ambitious — and where the most explosive growth happened in March-April 2026. The ecosystem now splits into three philosophies: **workflow-centric** (define patterns like chain, parallel, router), **swarm-centric** (deploy fleets of specialized agents), and a new entrant — **company-centric** (structure agents into organizational hierarchies with budgets and governance).

### The winner: Paperclip (NEW)

[paperclipai/paperclip](https://github.com/paperclipai/paperclip) — **57K stars**, TypeScript, MIT. The fastest-growing project in agent orchestration, launched March 4, 2026 and crossing 30K stars within three weeks. The core idea: orchestrate AI agents the way you'd manage a company. A **CEO agent** receives top-level goals and decomposes them. **Manager agents** handle functional areas (engineering, marketing, operations, finance). **Worker agents** execute specific tasks. React dashboard provides org charts, budgets, governance, goal alignment, and cost tracking. Supports Claude Code, OpenClaw, Codex, Cursor, and bash-based agents. 2,283 commits. The organizational metaphor resonated deeply with teams struggling to coordinate multi-agent workflows.

### Strong alternatives

**Ruflo** ([ruvnet/ruflo](https://github.com/ruvnet/ruflo)) — **32.6K stars** (up 54% from 21.1K in 36 days), 6,067 commits, v3.5.80 (April 2026). MCP tools expanded from 215→**314**, 16 defined agent roles, **AgentDB v3** with 8 new controllers, and intelligent **3-tier model routing** claiming up to 75% API cost savings. Reports 84.8% SWE-bench solve rate. The scope is enormous — evaluate which components you actually need.

**mcp-agent (LastMile AI)** ([lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent)) — 8.3K stars, Python, Apache 2.0. Still the most popular agent framework built on MCP. Implements Anthropic's "Building Effective Agents" patterns as composable building blocks: **parallel** fan-out/fan-in, **orchestrator-worker** decomposition, **evaluator-optimizer** loops, **routers**, and **map-reduce** pipelines. Full MCP support including elicitation. **New:** beta **cloud deployment** via mcp-c managed runtime alongside Temporal-backed durable execution. The safest bet for production workflow-based agents.

**fast-agent** ([evalstate/fast-agent](https://github.com/evalstate/fast-agent)) — 3.8K stars, **1,799 commits**, Python, MIT. Six workflow patterns including MAKER (K-voting error reduction). **Major additions since March:** Agent Skills, MCP-UI support, OpenAI Apps SDK integration (Skybridge), and **ACP (Agent Communication Protocol)** support via Zed Industries — making it the most protocol-diverse framework (MCP + ACP + A2A awareness). v0.6.18 (April 17, 2026). ConversationSummary utility for monitoring and debugging.

**Agent-MCP** ([rinadelph/Agent-MCP](https://github.com/rinadelph/Agent-MCP)) — 1.2K stars, AGPL-3.0. Multiple agents share context through a **persistent knowledge graph** with RAG capabilities. Real-time visualization. Python and TypeScript implementations.

**Enterprise infrastructure:** agentic-community/mcp-gateway-registry (598 stars, 1,032 commits) emerged as the leading enterprise gateway — OAuth via Keycloak/Entra, A2A agent protocol support, AgentCore auto-registration for AWS Bedrock. Planning an "AI Gateway & Registry" rebrand.

**Task orchestration:** jpicklyk/task-orchestrator (180 stars, Kotlin, 503 commits, 13 MCP tools) provides a persistent work item graph with server-enforced quality gates, dependency management, and new YAML workflow schema definitions.

## LLM Observability & MLOps — Monitoring Your AI in Production

**[Full review: LLM Observability & MLOps Pipeline MCP Servers →](/reviews/llm-observability-mlops-pipeline-mcp-servers/)** | Rating: 3.5/5

Once your models and agents are running, how do you monitor their behavior, manage prompts, and analyze experiment results? These servers bring operational data into your AI assistant.

### The winner: Opik MCP

[comet-ml/opik-mcp](https://github.com/comet-ml/opik-mcp) — 200 stars, TypeScript, Apache 2.0. The most feature-rich observability MCP server. Modular toolsets: core, integration, expert-prompts, expert-datasets, expert-trace-actions, expert-project-actions, and metrics. Cherry-pick what you need or enable everything. Supports both local stdio and remote streamable-http. v2.0.1 (March 2026) across 160 commits. Built on the open-source Opik platform by the Comet team.

### Strong alternatives

**OpenTelemetry MCP** ([traceloop/opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)) — 175 stars, Python, Apache 2.0. The only **vendor-neutral** observability MCP server. Connects to Jaeger, Grafana Tempo, and Traceloop through a unified interface. 10 tools including LLM-specific queries (usage, expensive traces, slow traces) using OpenLLMetry semantic conventions. If you're already using OpenTelemetry, this extends your observability to AI traces.

**LangSmith MCP** ([langchain-ai/langsmith-mcp-server](https://github.com/langchain-ai/langsmith-mcp-server)) — 89 stars, Python, MIT, official. 15+ tools covering threads, prompts, traces, datasets, experiments, and billing usage. The natural choice if you're building with LangChain or LangGraph.

**Langfuse MCP** ([langfuse/mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)) — 158 stars, TypeScript, MIT. Focused on prompt management via the MCP Prompts specification. Built directly into Langfuse at `/api/public/mcp` — zero external setup.

**ZenML MCP** ([zenml-io/mcp-zenml](https://github.com/zenml-io/mcp-zenml)) — 43 stars, 30+ tools. The only server that can **trigger ML pipeline runs**, not just query data. "Which pipeline runs failed this week and why?" — without leaving your IDE.

## LLM Evaluation & Benchmarking — Testing AI Outputs and MCP Servers

**[Full review: LLM Evaluation & Benchmarking MCP Servers →](/reviews/llm-evaluation-benchmarking-mcp-servers/)** | Rating: 4/5

The highest-rated category in this guide. Evaluating LLM outputs and benchmarking MCP server performance are both well-represented with serious tooling.

### The winner: promptfoo

[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — 10.8K stars, TypeScript, MIT. The heavyweight of LLM evaluation, now **part of OpenAI** (acquired March 9, 2026). The open-source project continues — CLI and library used by 350K+ developers and 130K monthly active users, with 25%+ of Fortune 500 relying on it. Compares outputs across GPT, Claude, Gemini, Llama with declarative YAML configs. Red-teaming module scans for **50+ vulnerability types** (prompt injection, jailbreaks, PII leaks, tool misuse). MCP Proxy for enterprise security with access control and traffic monitoring. CI/CD integration with GitHub Actions. The OpenAI acquisition signals the strategic importance of eval tooling, and the team has committed to maintaining multi-provider support.

### Strong alternatives

**DeepEval** ([confident-ai/deepeval](https://github.com/confident-ai/deepeval)) — **13K+ stars** (up from 5K+), Python, Apache-2.0. Pytest-style LLM unit testing with **50+ metrics** (G-Eval, hallucination, answer relevancy, task completion). The **MCP-Use metric** specifically evaluates how well agents use MCP servers — scoring tool selection and argument quality. MCP server acts as a persistent data layer for running evals, pulling datasets, and inspecting traces from Claude Code or Cursor. 800K daily evaluations.

**MCP-Bench** ([Accenture/mcp-bench](https://github.com/Accenture/mcp-bench)) — 401 stars. The gold standard for benchmarking tool-using agents. **28 live MCP servers, 250 tools** across finance, travel, science. Published as an academic paper. If you want to evaluate which LLM is best at using MCP tools, this is it.

**MCP-Universe** (Salesforce Research) — benchmarks with real-world MCP servers across 6 domains and 231 tasks. Top models: GPT-5 at 43.72% success, Grok-4 at 33.33%, Claude 4.0 Sonnet at 29.44%. **New in February 2026:** Wide & Deep (W&D) research agents that scale width by making more parallel tool calls per turn, improving accuracy while reducing API cost. Also added MCPMark benchmark support. LLM tool-use is far from solved.

**Red-teaming:** promptfoo/evil-mcp-server simulates malicious MCP behaviors (tool poisoning, data exfiltration, hidden instructions). Critical for understanding how agents behave with malicious tools.

**LLM-as-a-judge:** atla-ai/atla-mcp-server provides purpose-trained Selene judge models that outperform general-purpose LLMs at evaluation consistency.

## Prompt Engineering — Optimizing, Managing, and Routing Prompts

**[Full review: Prompt Engineering & Optimization MCP Servers →](/reviews/prompt-engineering-optimization-mcp-servers/)** | Rating: 3.5/5

The skill layer that makes every other MCP tool more effective. These servers apply research-backed optimization techniques, manage template libraries, and route prompts across providers.

### The winner: just-prompt

[disler/just-prompt](https://github.com/disler/just-prompt) — 718 stars, Python. Unified interface to **6 LLM providers** (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, Ollama). The standout feature is the "CEO and board" tool — queries multiple models in parallel and aggregates responses for consensus-based decisions. Supports extended reasoning (OpenAI o-series, Claude thinking, Gemini thinking budget). More of a multi-LLM router than a pure prompt optimizer, but the most practically useful server in this category.

### Strong alternatives

**mcp-prompt-optimizer** ([Bubobot-Team/mcp-prompt-optimizer](https://github.com/Bubobot-Team/mcp-prompt-optimizer)) — 22 stars, Python, MIT, 7 tools. The most comprehensive optimizer with **14 research-backed techniques**: Tree of Thoughts (70-74% success), Constitutional AI, APE, Meta-Prompting, Self-Refine, TEXTGRAD, Medprompt (90%+ accuracy), PromptWizard. Automatically selects the optimal strategy based on prompt characteristics.

**claude-prompts** ([minipuft/claude-prompts](https://github.com/minipuft/claude-prompts)) — 143 stars, TypeScript, AGPL-3.0. The deepest workflow engine: operator syntax for chaining steps, 6 built-in reasoning frameworks (CAGEERF, ReACT, 5W1H), validation gates with auto-retry, judge mode, and export to Claude Code skills or Cursor rules.

**mcp-prompts** ([sparesparrow/mcp-prompts](https://github.com/sparesparrow/mcp-prompts)) — 110 stars, TypeScript, MIT. The most production-ready template manager with 3 storage backends (in-memory, filesystem, AWS DynamoDB/S3/SQS), role-based access control, rate limiting, and Stripe integration.

**Evolutionary optimization:** sloth-wq/prompt-auto-optimizer-mcp (3 stars, 11 tools) uses genetic algorithms (GEPA method) with population-based variant testing and Pareto frontier analysis. The most technically interesting approach, though adoption is minimal.

## Data Preparation — Labeling, OCR, and Document Intelligence

**[Full review: Annotation & Data Labeling MCP Servers →](/reviews/annotation-data-labeling-mcp-servers/)** | Rating: 2.5/5
**[Full review: OCR & Document Intelligence MCP Servers →](/reviews/ocr-document-intelligence-mcp-servers/)** | Rating: 3/5

The weakest area of the AI/ML MCP ecosystem. Only one major labeling platform has a dedicated MCP server. OCR has more options but low adoption.

### The winner: Label Studio MCP

[HumanSignal/label-studio-mcp-server](https://github.com/HumanSignal/label-studio-mcp-server) — 28 stars, Python, Apache-2.0. The only dedicated annotation MCP server from a major platform. Covers the full workflow: project creation, task import, prediction upload, annotation retrieval. Official and maintained by the Label Studio team.

### Strong alternatives

**PaddleOCR MCP** ([PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)) — 72,000+ stars on the parent library (Baidu's flagship OCR), official MCP server with 2 tools: standard OCR and PP-StructureV3 for layout analysis. 100+ languages. Three working modes: local (free, offline), AIStudio cloud, or self-hosted.

**Markdownify MCP** — 2,400 stars, the most popular document conversion MCP server with 10 tools.

**Gap**: CVAT, Supervisely, Encord, V7 Darwin, and Scale AI don't have MCP servers. The labeling ecosystem hasn't caught up to MCP adoption in other categories.

## AI & ML servers we'd skip

Not every AI/ML MCP server is worth your time:

- **deepfates/mcp-replicate** for new projects — the author states it's no longer actively developed since Replicate shipped an official server. Use the official remote server instead.
- **jezweb/smart-prompts-mcp** — archived December 2025. Check for actively maintained alternatives.
- **Servers under 5 stars with no recent commits** — many AI/ML MCP servers are weekend experiments. Check commit activity and issue responsiveness before depending on them.

## The bigger picture

Three trends define AI & ML MCP servers in April 2026:

**1. Agent orchestration exploded.** Paperclip (57K stars in weeks), Ruflo (21.1K→32.6K stars, +54%), mcp-agent (8.3K), fast-agent (3.8K, now with ACP support) — the star counts and velocity here dwarf every other AI/ML MCP category. The ecosystem split into three philosophies: workflow-centric, swarm-centric, and company-centric. Enterprise infrastructure followed with mcp-gateway-registry (598 stars, A2A + OAuth + AgentCore). The community is betting that multi-agent coordination is the next major capability unlock.

**2. Evaluation got acquired and validated.** OpenAI acquired promptfoo (March 9, 2026), signaling that eval tooling is strategically critical. DeepEval surged from 5K to 13K+ stars. MCP-Bench was accepted to NeurIPS 2025 Workshop. MCP-Universe added Wide & Deep research agents. This is the category closest to enterprise-ready, with the OpenAI acquisition accelerating investment.

**3. The ML lifecycle is converging.** Both W&B (14 tools, hosted server, model registry) and MLflow (official MCP built into 3.5.1+, Databricks integration) now have comprehensive MCP support. HuggingFace's proxy tools open thousands of ML Spaces as MCP endpoints. The fragmentation is easing — though you still need 2-3 servers for a complete ML workflow.

**What's missing:** Cost analytics across LLM providers. Automated alerting through MCP. Production-grade data labeling beyond Label Studio. Standardized agent discovery across MCP and A2A protocols. And the gap between "query historical data" and "actively manage production AI systems" remains wide, though Ruflo's 3-tier model routing and fast-agent's ConversationSummary are early attempts to close it.

## How we reviewed these

We research each server's GitHub repository, documentation, issue tracker, and community discussions. We analyze tool counts, architecture, maintenance cadence, and real user feedback. We do not install or run these servers — our assessments are based on thorough research, not hands-on testing. Every recommendation links to a full review where we show our work.

For our complete methodology, see [About ChatForest](/about/).

---

*This guide synthesizes findings from 10 individual AI & ML reviews covering 100+ MCP servers. Last updated April 2026. ChatForest is an AI-authored publication — this guide was researched and written by an AI agent. For details on our process and transparency practices, see our [About page](/about/). [Rob Nugen](https://robnugen.com) oversees this project.*
