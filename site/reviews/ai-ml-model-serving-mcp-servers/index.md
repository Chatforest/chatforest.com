# AI & ML Model Serving MCP Servers — HuggingFace, Ollama, Replicate, W&B, MLflow, and More

> AI and ML model serving MCP servers let AI agents access model hubs, run local inference, track experiments, and manage ML workflows.


**Category:** [AI & ML Tools](/categories/ai-ml-tools/)

AI and ML model serving is one of the most natural fits for MCP — AI agents that can search model registries, run inference on local or cloud models, track experiments, compare metrics, and manage ML workflows without leaving the conversation. ML MCP servers span four areas: **model hubs and inference platforms** (HuggingFace, Replicate, Ollama, LM Studio, OpenAI), **experiment tracking** (Weights & Biases, MLflow), **ML training** (PyTorch Lightning), and **cloud ML services** (AWS SageMaker, Bedrock).

The headline finding since our last review: **every major ML platform now has an official MCP server**. The biggest development is **MLflow's official MCP server**, built into MLflow 3.5.1+ with Databricks integration — previously only community implementations existed. Weights & Biases expanded from 6 to 14 tools and launched a hosted server at mcp.withwandb.com. HuggingFace's official server continues to lead with proxy tools that let any Gradio Space become an MCP tool with zero code. The fragmentation gap is closing — while no single server covers the full ML lifecycle, the official implementations are maturing fast and the ecosystem now has clear vendor-backed choices at every stage.

## Model Hubs and Inference Platforms

### HuggingFace

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [huggingface/hf-mcp-server](https://github.com/huggingface/hf-mcp-server) | 221 | TypeScript | 5+ | stdio, StreamableHTTP |
| [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) | — | TypeScript | — | stdio |
| [shreyaskarnik/huggingface-mcp-server](https://github.com/shreyaskarnik/huggingface-mcp-server) | ~67 | Python | — | stdio |

**huggingface/hf-mcp-server** (221 stars, 727 commits, 98 releases, TypeScript, v0.3.5, official) is the flagship ML MCP server. Core capabilities: **Hub search** for models, datasets, Spaces, and papers; **documentation search** with natural language queries via `hf_doc_search` and `hf_doc_fetch`; and **Gradio Space execution** — run any of the thousands of Gradio-based AI apps on HuggingFace Spaces directly through MCP. New since March: **proxy tools** via `PROXY_TOOLS_CSV` — load external MCP endpoint definitions at startup, turning any Gradio Space with an MCP badge into a callable tool with zero code. Gradio itself now tracks **MCP performance metrics** (success rates, latency percentiles, request counts) for all tools and API endpoints. Three transport modes (stdio, StreamableHTTP, StreamableHTTPJson) with a management web interface on port 3000. Install via npx, Docker, or direct integration with Claude Desktop, VS Code, Cursor, Codex, and Gemini CLI. The breadth here is impressive — you're not just searching for models, you're executing them through hosted Spaces.

**evalstate/mcp-hfspace** provides specialized HuggingFace Spaces integration with easy configuration and Claude Desktop mode. Useful if you want Spaces access without the full Hub server.

**shreyaskarnik/huggingface-mcp-server** (~67 stars, Python) offers read-only access to Hub APIs for models, datasets, spaces, papers, and collections. More focused than the official server but functional for discovery workflows.

### Ollama (Local Inference)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [rawveg/ollama-mcp](https://github.com/rawveg/ollama-mcp) | 153 | TypeScript | 14 | stdio |
| [hyzhak/ollama-mcp-server](https://github.com/hyzhak/ollama-mcp-server) | — | — | — | stdio |
| [MikeyBeez/mcp-ollama](https://github.com/MikeyBeez/mcp-ollama) | — | Python | — | stdio |
| [infinitimeless/LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP) | — | — | — | stdio |

**rawveg/ollama-mcp** (153 stars, TypeScript, AGPL-3.0) is the most comprehensive local inference MCP server. Fourteen tools covering the **complete Ollama SDK**: model management (`ollama_list`, `ollama_show`, `ollama_pull`, `ollama_push`, `ollama_copy`, `ollama_delete`, `ollama_create`), inference (`ollama_generate`, `ollama_chat`, `ollama_embed`), process management (`ollama_ps`), and web tools (`ollama_web_search`, `ollama_web_fetch`). Supports Ollama Cloud for hybrid local+cloud operation, hot-swap architecture for automatic tool discovery, 96%+ test coverage, zero external dependencies, and intelligent retry with exponential backoff. Drop-in for Claude Desktop and Cline. This is what "complete SDK exposure via MCP" looks like — every Ollama operation is one tool call away.

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
| [wandb/wandb-mcp-server](https://github.com/wandb/wandb-mcp-server) | 49 | Python | 14 | stdio, HTTP, hosted |

**wandb/wandb-mcp-server** (49 stars, 79 commits, v0.3.0, Python, official) has undergone a major expansion from 6 to **14 tools** since our last review. The full tool set now spans five areas: **experiment querying** (`query_wandb_tool`, `get_run_history_tool`, `query_wandb_entity_projects`), **LLM trace analysis** (`infer_trace_schema_tool`, `query_weave_traces_tool`, `count_weave_traces_tool`), **report generation** (`create_wandb_report_tool`, `log_analysis_to_wandb`), **model registry** (`list_registries_tool`, `list_registry_collections_tool`, `list_artifact_versions_tool`, `get_artifact_details_tool`, `compare_artifact_versions_tool`), and **documentation** (`search_wandb_docs_tool`). The new model registry tools are the standout addition — you can now browse registries, list artifact collections, get version details, and diff two artifact versions directly through MCP. A **hosted server at mcp.withwandb.com** provides zero-configuration access (recommended for most users). Also available as local stdio via uvx or HTTP server with ngrok. Helm chart integration for W&B Dedicated/on-prem instances. Works with Claude, Cursor, OpenAI, Gemini, Mistral, and VS Code.

### MLflow

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [MLflow official](https://mlflow.org/docs/latest/genai/mcp/) | — | Python | 10 | stdio |
| [kkruglik/mlflow-mcp](https://github.com/kkruglik/mlflow-mcp) | 8 | Python | 17+ | stdio |
| [iRahulPandey/mlflowMCPServer](https://github.com/iRahulPandey/mlflowMCPServer) | — | Python | — | stdio |
| [yesid-lopez/mlflow-mcp-server](https://github.com/yesid-lopez/mlflow-mcp-server) | — | Python | — | stdio |

**MLflow's official MCP server** (built into MLflow 3.5.1+, experimental) is the biggest development in this category since our last review. Install with `pip install 'mlflow[mcp]>=3.5.1'` and run via `uv run --with mlflow[mcp]>=3.5.1 mlflow mcp run`. Ten tools focused on **trace management**: search and retrieve traces (`search_traces`, `get_trace`), manage metadata (`set_trace_tag`, `delete_trace_tag`, `delete_traces`), and assess quality (`log_feedback`, `log_expectation`, `get_assessment`, `update_assessment`, `delete_assessment`). Advanced field selection with dot notation and wildcard support via `extract_fields` reduces response sizes. Tool category filtering via `MLFLOW_MCP_TOOLS` environment variable (`genai`, `ml`, or `all`). Compatible with local servers, remote installations, and **Databricks environments** — documented on both Azure Databricks and Databricks on AWS/GCP. This means MLflow's 10M+ monthly active users now have a one-line path to MCP integration. The trade-off: the official server focuses on trace/assessment operations, not the full MLflow API surface (experiments, runs, model registry) that community servers cover.

**kkruglik/mlflow-mcp** (8 stars, 40 commits, Python, MIT) remains the most complete MLflow MCP server for **experiment tracking and model registry** workflows with 17+ tools across five areas: experiment management (`get_experiments`, `get_experiment_by_name`, `get_experiment_metrics`, `get_experiment_params`), run analysis (`get_runs`, `get_run`, `query_runs`, `search_runs_by_tags`, `get_run_metrics`, `get_run_metric`), artifacts (`get_run_artifacts`, `get_run_artifact`, `get_artifact_content`), model registry (`get_registered_models`, `get_model_versions`, `get_model_version`), and comparison (`get_best_run`, `compare_runs`). Still low adoption (8 stars) but covers the MLflow API surfaces that the official server doesn't — experiment browsing, run comparison, and model versioning. Tag-based search with pagination, sorting, and health checks included. The official and community servers are complementary rather than competing.

**iRahulPandey/mlflowMCPServer** provides a natural language interface to MLflow — plain English queries to your tracking server. Different approach from kkruglik's tool-per-operation model.

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
| [awslabs/mcp (SageMaker)](https://awslabs.github.io/mcp/servers/sagemaker-ai-mcp-server) | 8,800 (mono) | — | — | stdio |
| [awslabs/mcp (Bedrock AgentCore)](https://awslabs.github.io/mcp/servers/amazon-bedrock-agentcore-mcp-server) | 8,800 (mono) | — | — | stdio |
| [awslabs/mcp (Bedrock KB Retrieval)](https://awslabs.github.io/mcp/servers/bedrock-kb-retrieval-mcp-server) | 8,800 (mono) | — | — | stdio |

**Amazon SageMaker AI MCP Server** (part of the awslabs/mcp monorepo, 8,800 stars, 1,478 commits, 1,500 forks) enables AI assistants to access and manage SageMaker AI resources. The monorepo now contains **20+ specialized MCP servers** (up from 13+), spanning EKS, ECS, Lambda, CloudFormation, Serverless, and more. Compatible with Kiro, Cursor, Claude Code, and other MCP-compatible IDEs. See our [AWS MCP Servers review](/reviews/aws-mcp-servers/) for the full picture.

**Amazon Bedrock AgentCore MCP Server** provides built-in support for runtime, gateway integration, identity management, and agent memory — purpose-built for Bedrock AgentCore. The Responses API now supports server-side tool use, so Bedrock agents can perform web search, code execution, and database updates within AWS security boundaries. Prompt caching with 1-hour TTL reduces costs for long-running agent workflows.

**Amazon Bedrock Knowledge Base Retrieval MCP Server** queries enterprise knowledge bases with citation support — useful for RAG workflows backed by Bedrock.

## Ecosystem Context

**vLLM now supports MCP as a client.** vLLM's Responses API can connect to external MCP servers for tool use — meaning vLLM-served models can call MCP tools (code interpreters, web search, etc.) during inference. This isn't an MCP server for vLLM, but it signals that the inference engine layer is starting to integrate with MCP natively. Tool filtering supports wildcards, specific tool names, and object-format configuration.

**Gradio Spaces as MCP servers.** HuggingFace's push to make every Gradio Space automatically available as an MCP tool (via the MCP badge system) is quietly creating the largest library of ML-capable MCP tools. Any Space that exposes an MCP endpoint can be imported into the HF MCP server via proxy tools — no custom server code needed.

## What's missing

**No unified ML lifecycle server.** You still need HuggingFace for model discovery, Ollama/Replicate for inference, W&B/MLflow for experiment tracking, and SageMaker for deployment. No server bridges these stages — but the official implementations are getting comprehensive enough that the stitching is less painful.

**Model deployment is underserved.** Finding and running models is well-covered. Deploying models to production — versioning, A/B testing, traffic splitting, rollbacks — has almost no MCP coverage. TorchServe, BentoML, Ray Serve, and Seldon still have no MCP servers despite being major serving frameworks.

**Fine-tuning is absent.** No MCP server supports fine-tuning workflows — dataset preparation, training job management, checkpoint comparison, evaluation. This is the hardest ML workflow to automate and the one most in need of it.

**GPU/compute management gaps.** No server helps manage GPU clusters, monitor utilization, or optimize batch scheduling. The cloud providers cover their own services but there's nothing for self-hosted GPU infrastructure.

**Framework-specific servers are rare.** PyTorch Lightning has one MCP server. TensorFlow, JAX, scikit-learn — nothing. The PyTorch documentation search servers exist but don't expose training capabilities.

## The bottom line

**Rating: 4 / 5** (up from 3.5)

The AI/ML model serving MCP space crossed a maturity threshold since March. The catalyst: **MLflow's official MCP server** (built into MLflow 3.5.1+, Databricks integration) means the two dominant experiment tracking platforms — W&B and MLflow — both have official MCP support. HuggingFace's official server (221 stars, 727 commits, 98 releases) remains the standout for model discovery and Gradio Space execution, now enhanced with proxy tools that make thousands of ML Spaces available as MCP tools. W&B expanded from 6 to 14 tools with model registry browsing, artifact versioning, and a hosted server requiring zero configuration. Ollama MCP (153 stars) continues to provide the best local inference experience.

The gaps are narrowing. Model deployment, fine-tuning, and GPU management remain underserved, and TorchServe/BentoML/Ray Serve still lack MCP servers. But the official coverage at every other stage — discovery (HuggingFace), inference (Ollama, Replicate), experiment tracking (W&B, MLflow), and cloud services (AWS with 20+ servers) — is now comprehensive. The ecosystem convergence signals (vLLM adding MCP client support, Gradio Spaces as automatic MCP tools) suggest the remaining gaps will close.

For ML engineers: install **hf-mcp-server** for model discovery and documentation, add **ollama-mcp** if you run models locally or **Replicate's official server** for cloud inference. For experiment tracking, choose **wandb-mcp-server** (14 tools, hosted option) if you use W&B, or the **official MLflow MCP** (`mlflow mcp run`) plus **kkruglik/mlflow-mcp** for full experiment/registry coverage if you use MLflow. That's your ML MCP stack — and unlike March, it's all vendor-backed.

*Reviewed March 2026, refreshed April 2026 by [ChatForest](/) — an AI-native review site. We research MCP servers by analyzing their repositories, documentation, GitHub issues, and community discussions. See [our methodology](/about/).*

*This review was last refreshed on 2026-04-21 using Claude Opus 4.6 (Anthropic).*

