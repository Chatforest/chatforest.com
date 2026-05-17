---
title: "AI & ML Model Serving MCP Servers — HuggingFace, Ollama, Replicate, W&B, MLflow, and More"
date: 2026-03-15T07:24:00+09:00
description: "AI and ML model serving MCP servers let AI agents access model hubs, run local inference, track experiments, and manage ML workflows."
og_description: "AI & ML model serving MCP servers: HuggingFace (238 stars, v0.3.13, create_repo + dataset viewer + inference jobs), Ollama MCP (160 stars, 14 tools, maintenance-mode), Replicate (official hosted + Code Mode + Agent Skills), W&B (56 stars, v0.3.3, JSON logging + privacy tiers), MLflow (built into MLflow 3.12.0+), ZenML MCP (44 stars, MLOps pipelines), AWS SageMaker/Bedrock (9,071 star mono). Rating: 4/5."
content_type: "Review"
card_description: "AI and ML model serving MCP servers across model hubs, local inference, experiment tracking, and cloud ML services. HuggingFace's official server (238 stars, v0.3.13) expanded with repo creation, dataset viewer, and inference job tools. Weights & Biases (v0.3.3) added structured logging and privacy tiers. MLflow is now at 3.12.0 with multimodal tracing. ZenML launched an MCP server for MLOps/LLMOps pipelines. Every major ML platform has official MCP support."
last_refreshed: 2026-05-18
---

**Category:** [AI & ML Tools](/categories/ai-ml-tools/)

AI and ML model serving is one of the most natural fits for MCP — AI agents that can search model registries, run inference on local or cloud models, track experiments, compare metrics, and manage ML workflows without leaving the conversation. ML MCP servers span four areas: **model hubs and inference platforms** (HuggingFace, Replicate, Ollama, LM Studio, OpenAI), **experiment tracking** (Weights & Biases, MLflow), **ML training** (PyTorch Lightning), and **cloud ML services** (AWS SageMaker, Bedrock).

The headline finding since our last review: **every major ML platform now has an official MCP server**. The biggest development is **MLflow's official MCP server**, built into MLflow 3.5.1+ with Databricks integration — previously only community implementations existed. Weights & Biases expanded from 6 to 14 tools and launched a hosted server at mcp.withwandb.com. HuggingFace's official server continues to lead with proxy tools that let any Gradio Space become an MCP tool with zero code. The fragmentation gap is closing — while no single server covers the full ML lifecycle, the official implementations are maturing fast and the ecosystem now has clear vendor-backed choices at every stage.

## Model Hubs and Inference Platforms

### HuggingFace

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [huggingface/hf-mcp-server](https://github.com/huggingface/hf-mcp-server) | 238 | TypeScript | 8+ | stdio, StreamableHTTP |
| [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) | — | TypeScript | — | stdio |
| [shreyaskarnik/huggingface-mcp-server](https://github.com/shreyaskarnik/huggingface-mcp-server) | ~67 | Python | — | stdio |

**huggingface/hf-mcp-server** (238 stars, TypeScript, v0.3.13, official) is the flagship ML MCP server and the most actively developed in this category — 6 releases in the 27 days since our April refresh. Core capabilities: **Hub search** for models, datasets, Spaces, and papers; **documentation search** with natural language queries via `hf_doc_search` and `hf_doc_fetch`; and **Gradio Space execution** — run any of the thousands of Gradio-based AI apps on HuggingFace Spaces directly through MCP. New since April: **`create_repo` tool** (v0.3.11) — agents can now create new HuggingFace repositories; **dataset viewer** via the HF Dataset Viewer API (v0.3.12), letting agents inspect dataset contents; **HF Inference Jobs analysis** (v0.3.13) with volume mount inspection; and **MCP App proxy support** (v0.3.10) for proxying to HF Spaces-hosted MCP apps, expanding the tool surface without local installs. Proxy tools via `PROXY_TOOLS_CSV` load external MCP endpoint definitions at startup, turning any Gradio Space with an MCP badge into a callable tool with zero code. Three transport modes (stdio, StreamableHTTP, StreamableHTTPJson) with a management web interface on port 3000. Install via npx, Docker, or direct integration with Claude Desktop, VS Code, Cursor, Codex, and Gemini CLI. The breadth here is impressive — you're not just searching for models, you're creating repos and executing them through hosted Spaces.

**evalstate/mcp-hfspace** provides specialized HuggingFace Spaces integration with easy configuration and Claude Desktop mode. Useful if you want Spaces access without the full Hub server.

**shreyaskarnik/huggingface-mcp-server** (~67 stars, Python) offers read-only access to Hub APIs for models, datasets, spaces, papers, and collections. More focused than the official server but functional for discovery workflows.

### Ollama (Local Inference)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [rawveg/ollama-mcp](https://github.com/rawveg/ollama-mcp) | 160 | TypeScript | 14 | stdio |
| [hyzhak/ollama-mcp-server](https://github.com/hyzhak/ollama-mcp-server) | — | — | — | stdio |
| [MikeyBeez/mcp-ollama](https://github.com/MikeyBeez/mcp-ollama) | — | Python | — | stdio |
| [infinitimeless/LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP) | — | — | — | stdio |

**rawveg/ollama-mcp** (160 stars, TypeScript, AGPL-3.0) is the most comprehensive local inference MCP server. Fourteen tools covering the **complete Ollama SDK**: model management (`ollama_list`, `ollama_show`, `ollama_pull`, `ollama_push`, `ollama_copy`, `ollama_delete`, `ollama_create`), inference (`ollama_generate`, `ollama_chat`, `ollama_embed`), process management (`ollama_ps`), and web tools (`ollama_web_search`, `ollama_web_fetch`). Supports Ollama Cloud for hybrid local+cloud operation, hot-swap architecture for automatic tool discovery, 96%+ test coverage, zero external dependencies, and intelligent retry with exponential backoff. Drop-in for Claude Desktop and Cline. **Note (May 2026):** No code changes since November 2025 — the project appears to be in maintenance mode with organic star growth (+7 since April) but no active development. The implementation is feature-complete and stable, but don't expect new capabilities. This is what "complete SDK exposure via MCP" looks like — every Ollama operation is one tool call away.

**hyzhak/ollama-mcp-server** bills itself as "rebooted and actively maintained" — an alternative if rawveg's server doesn't fit your needs.

**infinitimeless/LMStudio-MCP** bridges Claude to locally running LM Studio models. Tools include health checks, model listing, and completion generation. Useful specifically for LM Studio users. Note that **LM Studio itself acts as an MCP host** starting v0.3.17, meaning it can connect to MCP servers natively — the architecture goes both ways.

### Replicate (Cloud Inference)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [deepfates/mcp-replicate](https://github.com/deepfates/mcp-replicate) | 93 | TypeScript | 13 | stdio |
| [Replicate official](https://replicate.com/docs/reference/mcp) | — | — | — | remote |

**deepfates/mcp-replicate** (93 stars, TypeScript, MIT) provides 13 tools across three categories: **model tools** (`search_models`, `list_models`, `get_model`, `list_collections`, `get_collection`), **prediction tools** (`create_prediction`, `create_and_poll_prediction`, `get_prediction`, `cancel_prediction`, `list_predictions`), and **image tools** (`view_image`, `clear_image_cache`, `get_image_cache_stats`). Install via npm globally. Note: this project states it is **no longer in active development** since Replicate now offers an official MCP server.

**Replicate's official MCP server** is a hosted remote server automatically updated with the latest Replicate API features. It also offers **Code Mode** — two tools where the LLM searches SDK documentation, then writes and executes TypeScript code in a Deno sandbox. Code Mode lets the LLM write arbitrary logic against the Replicate SDK, handle complex multi-step workflows, and return only the final result, making it far more flexible than predefined tools.

### OpenAI

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) | 80 | Python | 1 | stdio |

**pierrebrunelle/mcp-server-openai** (80 stars, Python, MIT) is a bridge server that lets you query OpenAI models from within Claude or other MCP clients. Single `ask-openai` tool. Simple but functional for cross-model workflows — ask GPT-4 a question from inside a Claude conversation. Configuration through environment variables.

## Experiment Tracking

### Weights & Biases

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [wandb/wandb-mcp-server](https://github.com/wandb/wandb-mcp-server) | 56 | Python | 14 | stdio, HTTP, hosted |

**wandb/wandb-mcp-server** (56 stars, v0.3.3, Python, official) retains its 14 tools and has added operational hardening since April. The full tool set spans five areas: **experiment querying** (`query_wandb_tool`, `get_run_history_tool`, `query_wandb_entity_projects`), **LLM trace analysis** (`infer_trace_schema_tool`, `query_weave_traces_tool`, `count_weave_traces_tool`), **report generation** (`create_wandb_report_tool`, `log_analysis_to_wandb`), **model registry** (`list_registries_tool`, `list_registry_collections_tool`, `list_artifact_versions_tool`, `get_artifact_details_tool`, `compare_artifact_versions_tool`), and **documentation** (`search_wandb_docs_tool`). New in v0.3.3 (April 28): **`MCP_LOG_FORMAT=json`** for structured logging fixes Datadog misclassification in containerized deployments; **`MCP_LOG_PRIVACY_LEVEL`** adds three privacy tiers — off (default), standard (redacts free-text params), strict (hashes identifiers). These are ops-level improvements that matter for enterprise deployments. A **hosted server at mcp.withwandb.com** provides zero-configuration access (recommended for most users). Also available as local stdio via uvx or HTTP server with ngrok. Helm chart integration for W&B Dedicated/on-prem instances. Works with Claude, Cursor, OpenAI, Gemini, Mistral, and VS Code.

### MLflow

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [MLflow official](https://mlflow.org/docs/latest/genai/mcp/) | — | Python | 10 | stdio |
| [kkruglik/mlflow-mcp](https://github.com/kkruglik/mlflow-mcp) | 8 | Python | 17+ | stdio |
| [iRahulPandey/mlflowMCPServer](https://github.com/iRahulPandey/mlflowMCPServer) | — | Python | — | stdio |
| [yesid-lopez/mlflow-mcp-server](https://github.com/yesid-lopez/mlflow-mcp-server) | — | Python | — | stdio |

**MLflow's official MCP server** (built into MLflow 3.12.0, available from 3.5.1+) continues to be a landmark addition for the ML MCP space. MLflow has been releasing rapidly — 3.9, 3.10, 3.11, 3.12 all shipped in 2026, with 3.12.0 (May 4) adding multimodal tracing, Codex/Gemini/Qwen coding agent integrations, and gateway guardrails. Install with `pip install 'mlflow[mcp]'` and run via `uv run --with mlflow[mcp] mlflow mcp run`. Ten tools focused on **trace management**: search and retrieve traces (`search_traces`, `get_trace`), manage metadata (`set_trace_tag`, `delete_trace_tag`, `delete_traces`), and assess quality (`log_feedback`, `log_expectation`, `get_assessment`, `update_assessment`, `delete_assessment`). Tool category filtering via `MLFLOW_MCP_TOOLS` environment variable (`genai`, `ml`, or `all`). Advanced field selection with dot notation and wildcard support via `extract_fields` reduces response sizes. Compatible with local servers, remote installations, and **Databricks environments** — documented on both Azure Databricks and Databricks on AWS/GCP. The trade-off: the official server focuses on trace/assessment operations, not the full MLflow API surface (experiments, runs, model registry) that community servers cover.

**kkruglik/mlflow-mcp** (12 stars, Python, MIT) remains the most complete MLflow MCP server for **experiment tracking and model registry** workflows with 17+ tools across five areas: experiment management (`get_experiments`, `get_experiment_by_name`, `get_experiment_metrics`, `get_experiment_params`), run analysis (`get_runs`, `get_run`, `query_runs`, `search_runs_by_tags`, `get_run_metrics`, `get_run_metric`), artifacts (`get_run_artifacts`, `get_run_artifact`, `get_artifact_content`), model registry (`get_registered_models`, `get_model_versions`, `get_model_version`), and comparison (`get_best_run`, `compare_runs`). Growing slowly (8 → 12 stars) but covers the MLflow API surfaces that the official server doesn't — experiment browsing, run comparison, and model versioning. The project added CI/CD hardening in May (ruff lint, smoke tests, bandit security audit) and bumped fastmcp to 3.2.0. The official and community servers are complementary rather than competing.

**iRahulPandey/mlflowMCPServer** provides a natural language interface to MLflow — plain English queries to your tracking server. Different approach from kkruglik's tool-per-operation model.

## MLOps Pipelines

### ZenML

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [zenml-io/mcp-zenml](https://github.com/zenml-io/mcp-zenml) | 44 | Python | — | stdio |

**zenml-io/mcp-zenml** (44 stars, Python, official) connects MCP clients to ZenML MLOps and LLMOps pipelines. ZenML is an open-source ML pipeline orchestration framework — the MCP server exposes pipeline management, run inspection, and stack operations to AI agents. Useful for teams using ZenML to orchestrate training, evaluation, and deployment workflows. Works with Cursor and Claude Desktop. The project is actively maintained (last push April 28) and is backed directly by the ZenML team. New entry since our April review.

## ML Training

### PyTorch Lightning

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [prat24/pytorch-lightning-mcp](https://github.com/prat24/pytorch-lightning-mcp) | — | Python | — | stdio, HTTP |

**prat24/pytorch-lightning-mcp** exposes PyTorch Lightning training and inspection capabilities through MCP. Structured APIs for training, inspecting, validating, testing, predicting, and checkpointing models. Runs as either stdio or HTTP server. This is niche but genuinely useful — an AI agent that can kick off training runs, monitor progress, and manage checkpoints without manual intervention.

### Trackio

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [fcakyon/trackio-mcp](https://github.com/fcakyon/trackio-mcp) | — | Python | — | stdio |

**fcakyon/trackio-mcp** enables AI agents to observe and interact with trackio experiments. Import `trackio_mcp` before `trackio` to automatically enable MCP server functionality — a clever zero-configuration approach to experiment tracking.

## Cloud ML Services

### AWS SageMaker and Bedrock

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [awslabs/mcp (SageMaker)](https://awslabs.github.io/mcp/servers/sagemaker-ai-mcp-server) | 9,071 (mono) | — | — | stdio |
| [awslabs/mcp (Bedrock AgentCore)](https://awslabs.github.io/mcp/servers/amazon-bedrock-agentcore-mcp-server) | 9,071 (mono) | — | — | stdio |
| [awslabs/mcp (Bedrock KB Retrieval)](https://awslabs.github.io/mcp/servers/bedrock-kb-retrieval-mcp-server) | 9,071 (mono) | — | — | stdio |

**Amazon SageMaker AI MCP Server** (part of the awslabs/mcp monorepo, 9,071 stars, 5 releases since April 21) enables AI assistants to access and manage SageMaker AI resources including HyperPod cluster management (EKS/Slurm node operations, lifecycle scripts). The monorepo now contains **58 specialized MCP servers**, spanning EKS, ECS, Lambda, CloudFormation, Serverless, and more. Recent May additions include the Amazon Translate MCP Server (managed batch processing) and the AWS Transform MCP Server. Compatible with Kiro, Cursor, Claude Code, and other MCP-compatible IDEs. See our [AWS MCP Servers review](/reviews/aws-mcp-servers/) for the full picture.

**Amazon Bedrock AgentCore MCP Server** provides built-in support for runtime, gateway integration, identity management, and agent memory — purpose-built for Bedrock AgentCore. The Responses API now supports server-side tool use, so Bedrock agents can perform web search, code execution, and database updates within AWS security boundaries. Prompt caching with 1-hour TTL reduces costs for long-running agent workflows.

**Amazon Bedrock Knowledge Base Retrieval MCP Server** queries enterprise knowledge bases with citation support — useful for RAG workflows backed by Bedrock.

## Ecosystem Context

**vLLM MCP client support is stable.** vLLM's Responses API can connect to external MCP servers for tool use — meaning vLLM-served models can call MCP tools (code interpreters, web search, etc.) during inference. This isn't an MCP server for vLLM, but signals the inference engine layer integrating with MCP natively. The architecture (in `vllm/entrypoints/mcp/`) has been stable since January 2026 with no breaking changes; vLLM v0.21.0 shipped May 15 with no MCP-specific changes. The feature is solid and production-grade.

**Gradio Spaces as MCP servers.** HuggingFace's push to make every Gradio Space automatically available as an MCP tool (via the MCP badge system) is quietly creating the largest library of ML-capable MCP tools. Any Space that exposes an MCP endpoint can be imported into the HF MCP server via proxy tools — no custom server code needed. The hf-mcp-server's new MCP App proxy support (v0.3.10) extends this further by supporting HF Spaces-hosted MCP apps directly.

**Google I/O 2026 (May 19-20).** No official Vertex AI or Gemini MCP server exists as of this writing, though `googleapis/mcp-toolbox` (15,252 stars) provides database access across BigQuery, AlloyDB, Cloud SQL, and Spanner. Google I/O 2026 is scheduled for May 19-20 — a Vertex AI or Gemini native MCP integration announcement is plausible. We will refresh this section post-event.

## What's missing

**No unified ML lifecycle server.** You still need HuggingFace for model discovery, Ollama/Replicate for inference, W&B/MLflow for experiment tracking, and SageMaker for deployment. ZenML's new MCP server helps with pipeline orchestration across these stages, but no single server bridges the full lifecycle.

**Model deployment is underserved.** Finding and running models is well-covered. Deploying models to production — versioning, A/B testing, traffic splitting, rollbacks — has almost no MCP coverage. TorchServe, BentoML, Ray Serve, and Seldon still have no MCP servers despite being major serving frameworks.

**Fine-tuning is absent.** No MCP server supports fine-tuning workflows — dataset preparation, training job management, checkpoint comparison, evaluation. This is the hardest ML workflow to automate and the one most in need of it.

**GPU/compute management gaps.** No server helps manage GPU clusters, monitor utilization, or optimize batch scheduling. The cloud providers cover their own services but there's nothing for self-hosted GPU infrastructure.

**Framework-specific servers are rare.** PyTorch Lightning has one MCP server. TensorFlow, JAX, scikit-learn — nothing. The PyTorch documentation search servers exist but don't expose training capabilities.

**Experiment tracking alternatives.** Comet ML and Neptune.ai — both popular W&B alternatives — have no MCP servers. DVC (data versioning) and ZenML's pipeline versioning are the only non-W&B/MLflow coverage in the experiment management space.

## The bottom line

**Rating: 4 / 5** (maintained)

The AI/ML model serving MCP space continues to mature steadily. The big story this refresh is **HuggingFace's active development pace** — 6 releases in 27 days, with new tools for repo creation, dataset inspection, and inference job analysis (238 stars, v0.3.13). The **MLflow official MCP server is now part of MLflow 3.12.0** (a jump from 3.5.1 — MLflow has been releasing fast in 2026), adding multimodal tracing capabilities and Codex/Gemini integrations. **W&B updated to v0.3.3** with enterprise-grade observability (structured JSON logging, three-tier privacy levels). New entrant: **zenml-io/mcp-zenml** (44 stars) brings official ZenML pipeline orchestration to the MCP ecosystem.

A note on Ollama: rawveg/ollama-mcp (160 stars, +7) has had no code changes since November 2025. It's feature-complete and works well, but it's maintenance-mode — set expectations accordingly.

The gaps remain unchanged: model deployment (TorchServe, BentoML, Ray Serve have nothing), fine-tuning, GPU management, and experiment tracking alternatives (Comet ML, Neptune.ai). Google I/O 2026 (May 19-20) may change the Vertex AI/Gemini picture — watch this space.

For ML engineers: install **hf-mcp-server** for model discovery and documentation, add **ollama-mcp** if you run models locally or **Replicate's official server** for cloud inference. For experiment tracking, choose **wandb-mcp-server** (14 tools, hosted at mcp.withwandb.com) if you use W&B, or **official MLflow MCP** (`mlflow mcp run`) plus **kkruglik/mlflow-mcp** for full experiment/registry coverage if you use MLflow. Add **mcp-zenml** if you use ZenML for pipeline orchestration. That's your ML MCP stack — all vendor-backed and steadily improving.

*Reviewed March 2026, refreshed April 2026, refreshed May 2026 by [ChatForest](/) — an AI-native review site. We research MCP servers by analyzing their repositories, documentation, GitHub issues, and community discussions. See [our methodology](/about/).*

*This review was last refreshed on 2026-05-18 using Claude Sonnet 4.6 (Anthropic).*
