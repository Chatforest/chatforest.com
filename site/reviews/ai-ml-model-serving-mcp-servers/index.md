# AI & ML Model Serving MCP Servers — HuggingFace, Ollama, Replicate, W&B, MLflow, and More

> AI and ML model serving MCP servers let AI agents access model hubs, run local inference, track experiments, and manage ML workflows.


**Category:** [AI & ML Tools](/categories/ai-ml-tools/)

AI and ML model serving is one of the most natural fits for MCP — AI agents that can search model registries, run inference on local or cloud models, track experiments, compare metrics, and manage ML workflows without leaving the conversation. ML MCP servers span four areas: **model hubs and inference platforms** (HuggingFace, Replicate, Ollama, LM Studio, OpenAI), **experiment tracking** (Weights & Biases, MLflow), **ML training** (PyTorch Lightning), and **cloud ML services** (AWS SageMaker, Bedrock).

The headline finding since our last review: **every major ML platform now has an official MCP server**. The biggest development is **MLflow's official MCP server**, built into MLflow 3.5.1+ with Databricks integration — previously only community implementations existed. Weights & Biases expanded from 6 to 14 tools and launched a hosted server at mcp.withwandb.com. HuggingFace's official server continues to lead with proxy tools that let any Gradio Space become an MCP tool with zero code. The fragmentation gap is closing — while no single server covers the full ML lifecycle, the official implementations are maturing fast and the ecosystem now has clear vendor-backed choices at every stage.

## Model Hubs and Inference Platforms

### HuggingFace

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [huggingface/hf-mcp-server](https://github.com/huggingface/hf-mcp-server) | 273 | TypeScript | — | stdio, StreamableHTTP |
| [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) | — | TypeScript | — | stdio |
| [shreyaskarnik/huggingface-mcp-server](https://github.com/shreyaskarnik/huggingface-mcp-server) | ~71 | Python | — | stdio |

**huggingface/hf-mcp-server** (273 stars, TypeScript, official) is the flagship ML MCP server and the most actively developed in this category. As of our May 2026 refresh it had shipped 6 releases (v0.3.10–v0.3.13) in the 27 days since our prior check; development has continued at a similar pace since, reaching [v0.4.8 by August 2026](https://github.com/huggingface/hf-mcp-server/releases). Core capabilities: **Hub search** for models, datasets, Spaces, and papers; **documentation search** with natural language queries via `hf_doc_search` and `hf_doc_fetch`; and **Gradio Space execution** — run any of the thousands of Gradio-based AI apps on HuggingFace Spaces directly through MCP. Added in the v0.3.10–v0.3.13 window: **`create_repo` tool** (v0.3.11) — agents can now create new HuggingFace repositories; **dataset viewer** via the HF Dataset Viewer API (v0.3.12), letting agents inspect dataset contents; **HF Inference Jobs descriptions** (v0.3.13) with volume mount inspection; and **MCP App proxy support** (v0.3.10) for proxying to HF Spaces-hosted MCP apps, expanding the tool surface without local installs. Proxy tools via [`PROXY_TOOLS_CSV`](https://github.com/huggingface/hf-mcp-server#proxy-tools-streamable-http-via-csv) load external MCP endpoint definitions at startup, turning any Gradio Space with an MCP badge into a callable tool with zero code. Two transport modes — stdio and StreamableHTTP (stateless JSON mode) — with a [metrics/status web interface](https://github.com/huggingface/hf-mcp-server#readme) at `/metrics`. Install via npx, Docker, or direct integration with Claude Desktop, claude.ai, Claude Code, VS Code, Cursor, and Gemini CLI. The breadth here is impressive — you're not just searching for models, you're creating repos and executing them through hosted Spaces.

**evalstate/mcp-hfspace** provides specialized HuggingFace Spaces integration with easy configuration and Claude Desktop mode. Useful if you want Spaces access without the full Hub server.

**shreyaskarnik/huggingface-mcp-server** (~71 stars, Python) offers read-only access to Hub APIs for models, datasets, spaces, papers, and collections. More focused than the official server but functional for discovery workflows.

### Ollama (Local Inference)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [rawveg/ollama-mcp](https://github.com/rawveg/ollama-mcp) | 170 | TypeScript | 14 | stdio |
| [hyzhak/ollama-mcp-server](https://github.com/hyzhak/ollama-mcp-server) | — | — | — | stdio |
| [MikeyBeez/mcp-ollama](https://github.com/MikeyBeez/mcp-ollama) | — | Python | — | stdio |
| [infinitimeless/LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP) | — | — | — | stdio |

**rawveg/ollama-mcp** ([170 stars](https://github.com/rawveg/ollama-mcp), TypeScript, AGPL-3.0) is the most comprehensive local inference MCP server. Fourteen tools covering the **complete Ollama SDK**: model management (`ollama_list`, `ollama_show`, `ollama_pull`, `ollama_push`, `ollama_copy`, `ollama_delete`, `ollama_create`), inference (`ollama_generate`, `ollama_chat`, `ollama_embed`), process management (`ollama_ps`), and web tools (`ollama_web_search`, `ollama_web_fetch`). Supports Ollama Cloud for hybrid local+cloud operation, hot-swap architecture for automatic tool discovery, 96%+ test coverage, zero external dependencies, and intelligent retry with exponential backoff. Drop-in for Claude Desktop and Cline. **Update (August 2026):** the project went untouched from November 2025 until [a single dependency-security bump landed on August 13, 2026](https://github.com/rawveg/ollama-mcp/commits/main) — no new features. Practically still maintenance mode: nine-plus months with no functional development, though stars have grown organically. The implementation is feature-complete and stable, but don't expect new capabilities. This is what "complete SDK exposure via MCP" looks like — every Ollama operation is one tool call away.

**hyzhak/ollama-mcp-server** bills itself as "rebooted and actively maintained" — an alternative if rawveg's server doesn't fit your needs.

**infinitimeless/LMStudio-MCP** bridges Claude to locally running LM Studio models. Tools include health checks, model listing, and completion generation. Useful specifically for LM Studio users. Note that **LM Studio itself acts as an MCP host** starting [v0.3.17](https://lmstudio.ai/changelog/lmstudio-v0.3.17), meaning it can connect to local and remote MCP servers natively — the architecture goes both ways.

### Replicate (Cloud Inference)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [deepfates/mcp-replicate](https://github.com/deepfates/mcp-replicate) | 95 | TypeScript | 13 | stdio |
| [Replicate official](https://replicate.com/docs/reference/mcp) | — | — | — | remote |

**deepfates/mcp-replicate** (95 stars, TypeScript, MIT) provides 13 tools across three categories: **model tools** (`search_models`, `list_models`, `get_model`, `list_collections`, `get_collection`), **prediction tools** (`create_prediction`, `create_and_poll_prediction`, `get_prediction`, `cancel_prediction`, `list_predictions`), and **image tools** (`view_image`, `clear_image_cache`, `get_image_cache_stats`). Install via npm globally. Note: [this project was archived by its owner on May 18, 2026](https://github.com/deepfates/mcp-replicate) — its README states it's **no longer in active development** since Replicate now offers an official MCP server.

**[Replicate's official MCP server](https://replicate.com/docs/reference/mcp)** is a hosted remote server, published as an npm package that's automatically updated whenever Replicate adds new features or operations to its HTTP API. It also offers an experimental **Code Mode** — two tools where the LLM searches SDK documentation, then writes and executes TypeScript code in a Deno sandbox (currently local execution only, not remote cloud sandboxing). Code Mode lets the LLM write arbitrary logic against the Replicate SDK, handle complex multi-step workflows, and return only the final result, making it far more flexible than predefined tools.

### OpenAI

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) | 84 | Python | 1 | stdio |

**pierrebrunelle/mcp-server-openai** (84 stars, Python, MIT) is a bridge server that lets you query OpenAI models from within Claude or other MCP clients. Single `ask-openai` tool. Simple but functional for cross-model workflows — ask GPT-4 a question from inside a Claude conversation. Configuration through environment variables.

## Experiment Tracking

### Weights & Biases

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [wandb/wandb-mcp-server](https://github.com/wandb/wandb-mcp-server) | 68 | Python | 16 | stdio, HTTP, hosted |

**wandb/wandb-mcp-server** (68 stars, [v0.3.7](https://github.com/wandb/wandb-mcp-server/blob/main/pyproject.toml), Python, official) has grown to 16 default-enabled tools since our last check, plus 8 more optional tools. The default tool set spans six areas: **experiment querying** (`query_wandb_tool`, `get_run_history_tool`, `query_wandb_entity_projects`), **LLM trace analysis** (`infer_trace_schema_tool`, `query_weave_traces_tool`, `count_weave_traces_tool`), **report generation** (`create_wandb_report_tool`, `log_analysis_to_wandb`), **model registry** (`list_registries_tool`, `list_registry_collections_tool`, `list_artifact_versions_tool`, `get_artifact_details_tool`, `compare_artifact_versions_tool`), **automations and integrations** (`list_wandb_automations_tool`, `list_wandb_integrations_tool`), and **documentation** (`search_wandb_docs_tool`). A separate suite of [8 Weave agent-tracing tools is disabled by default](https://github.com/wandb/wandb-mcp-server#readme) (enable with `WANDB_MCP_ENABLE_WEAVE_AGENT_TOOLS=true`). A **hosted server at mcp.withwandb.com** provides zero-configuration access (recommended for most users). Also available as local stdio via uvx or HTTP server with ngrok. Helm chart integration for W&B Dedicated/on-prem instances. Works with Claude, Cursor, OpenAI, Gemini, Mistral, and VS Code.

### MLflow

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [MLflow official](https://mlflow.org/docs/latest/genai/mcp/) | — | Python | 10 | stdio |
| [kkruglik/mlflow-mcp](https://github.com/kkruglik/mlflow-mcp) | 14 | Python | 34 | stdio |
| [iRahulPandey/mlflowMCPServer](https://github.com/iRahulPandey/mlflowMCPServer) | — | Python | — | stdio |
| [yesid-lopez/mlflow-mcp-server](https://github.com/yesid-lopez/mlflow-mcp-server) | — | Python | — | stdio |

**MLflow's official MCP server** (built into MLflow, [available from 3.5.1+](https://mlflow.org/docs/latest/genai/mcp/)) continues to be a landmark addition for the ML MCP space. MLflow has been releasing rapidly — 3.9, 3.10, 3.11, 3.12 all shipped in 2026, with [3.12.0 (May 5, 2026)](https://github.com/mlflow/mlflow/releases/tag/v3.12.0) adding multimodal tracing, Codex/Gemini/Qwen coding agent integrations, and gateway guardrails; [MLflow has continued shipping fast since, reaching 3.15.x by August 2026](https://github.com/mlflow/mlflow/releases). Install with `pip install 'mlflow[mcp]'` and run via `uv run --with mlflow[mcp] mlflow mcp run`. Ten tools focused on **trace management**: search and retrieve traces (`search_traces`, `get_trace`), manage metadata (`set_trace_tag`, `delete_trace_tag`, `delete_traces`), and assess quality (`log_feedback`, `log_expectation`, `get_assessment`, `update_assessment`, `delete_assessment`). Tool category filtering via `MLFLOW_MCP_TOOLS` environment variable (`genai`, `ml`, `all`, or a comma-separated list of categories). Advanced field selection with dot notation and wildcard support via `extract_fields` reduces response sizes. Compatible with local servers, remote installations, and **Databricks environments**. The trade-off: the official server focuses on trace/assessment operations, not the full MLflow API surface (experiments, runs, model registry) that community servers cover.

**kkruglik/mlflow-mcp** ([14 stars](https://github.com/kkruglik/mlflow-mcp), Python, MIT, [now at v0.4.1](https://raw.githubusercontent.com/kkruglik/mlflow-mcp/main/pyproject.toml)) remains the most complete MLflow MCP server for **experiment tracking and model registry** workflows. It has grown substantially — from 17+ tools at our last check to [34 tools](https://github.com/kkruglik/mlflow-mcp#readme) today, adding new categories for logged models and health checks alongside the original areas: experiment management (`get_experiments`, `get_experiment_by_name`, `get_experiment_metrics`, `get_experiment_params`), run analysis (`get_runs`, `get_run`, `query_runs`, `search_runs_by_tags`, `get_run_metrics`, `get_run_metric`), artifacts (`get_run_artifacts`, `get_run_artifact`, `get_artifact_content`), model registry (`get_registered_models`, `get_model_versions`, `get_model_version`), and comparison (`get_best_run`, `compare_runs`). It covers the MLflow API surfaces that the official server doesn't — experiment browsing, run comparison, and model versioning. The project [added CI/CD hardening in April–May 2026](https://github.com/kkruglik/mlflow-mcp/commits/main) (ruff lint, smoke tests, bandit security audit) and bumped fastmcp to 3.2.0. The official and community servers are complementary rather than competing.

**iRahulPandey/mlflowMCPServer** provides a natural language interface to MLflow — plain English queries to your tracking server. Different approach from kkruglik's tool-per-operation model.

## MLOps Pipelines

### ZenML

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [zenml-io/mcp-zenml](https://github.com/zenml-io/mcp-zenml) | 49 | Python | — | stdio |

**zenml-io/mcp-zenml** (49 stars, Python, official) connects MCP clients to ZenML MLOps and LLMOps pipelines. ZenML is an open-source ML pipeline orchestration framework — the MCP server exposes pipeline management, run inspection, and stack operations to AI agents. Useful for teams using ZenML to orchestrate training, evaluation, and deployment workflows. Works with Cursor (via `.cursor/mcp.json`) and Claude Desktop (via the `.mcpb` drag-and-drop installer). The project is [actively maintained](https://github.com/zenml-io/mcp-zenml/commits/main) and is backed directly by the ZenML team.

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
| [awslabs/mcp (SageMaker)](https://awslabs.github.io/mcp/servers/sagemaker-ai-mcp-server) | 9,594 (mono) | — | — | stdio |
| [awslabs/mcp (Bedrock AgentCore)](https://awslabs.github.io/mcp/servers/amazon-bedrock-agentcore-mcp-server) | 9,594 (mono) | — | 122 | stdio |
| [awslabs/mcp (Bedrock KB Retrieval)](https://awslabs.github.io/mcp/servers/bedrock-kb-retrieval-mcp-server) | 9,594 (mono) | — | — | stdio |

**Amazon SageMaker AI MCP Server** (part of the [awslabs/mcp monorepo](https://github.com/awslabs/mcp), 9,594 stars) enables AI assistants to access and manage SageMaker AI resources, including [HyperPod cluster management](https://awslabs.github.io/mcp/servers/sagemaker-ai-mcp-server) (EKS/Slurm node deployment, node management, and lifecycle operations). The monorepo's [`src/` tree now contains roughly 67 individual MCP server packages](https://github.com/awslabs/mcp/tree/main/src), spanning EKS, ECS, Lambda, CloudFormation, Serverless, and more, including two recent additions: the [Amazon Translate MCP Server](https://github.com/awslabs/mcp/tree/main/src/amazon-translate-mcp-server) (translation across 75+ languages, managed batch processing) and the [AWS Transform MCP Server](https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server) (19 tools for managing transformation workspaces, jobs, and connectors). Compatible with Kiro, Cursor, Claude Code, and other MCP-compatible IDEs. See our [AWS MCP Servers review](/reviews/aws-mcp-servers/) for the full picture.

**Amazon Bedrock AgentCore MCP Server** exposes [122 tools across 7 operational primitives](https://awslabs.github.io/mcp/servers/amazon-bedrock-agentcore-mcp-server) — runtime management (14 tools: deploy, manage, and invoke agent runtimes/endpoints), gateway integration (15 tools: turn existing APIs into agent-callable MCP tools), identity management (21 tools: workload identities, OAuth2 credential providers, token vaults), and agent memory (21 tools: create memory resources, store conversation events, retrieve semantically relevant memories), among other primitives — purpose-built for Bedrock AgentCore. Separately, [Amazon Bedrock's Responses API now supports server-side tool execution via AgentCore Gateway](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-bedrock-server-side-tool-execution-agentcore-gateway), so Bedrock agents can perform web search, code execution, and database updates within AWS security boundaries. [Prompt caching with a 1-hour TTL](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-bedrock-one-hour-duration-prompt-caching) (up from the default 5 minutes, on supported Claude models) reduces costs for long-running agent workflows.

**Amazon Bedrock Knowledge Base Retrieval MCP Server** [queries Bedrock Knowledge Bases via conversational queries, with citation information on results](https://awslabs.github.io/mcp/servers/bedrock-kb-retrieval-mcp-server) — useful for RAG workflows backed by Bedrock.

## Ecosystem Context

**vLLM MCP client support is stable.** vLLM's Responses API can connect to external MCP servers for tool use — meaning vLLM-served models can call MCP tools (code interpreters, web search, etc.) during inference. This isn't an MCP server for vLLM, but signals the inference engine layer integrating with MCP natively. As of our May 2026 refresh the architecture (in `vllm/entrypoints/mcp/`) had been stable since January 2026 with no breaking changes; [vLLM v0.21.0 shipped May 15, 2026](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) with no MCP-specific changes. The feature is solid and production-grade.

**Gradio Spaces as MCP servers.** HuggingFace's push to make every Gradio Space automatically available as an MCP tool (via the MCP badge system) is quietly creating the largest library of ML-capable MCP tools. Any Space that exposes an MCP endpoint can be imported into the HF MCP server via proxy tools — no custom server code needed. The hf-mcp-server's MCP App proxy support (added in v0.3.10) extends this further by supporting HF Spaces-hosted MCP apps directly.

**No dedicated Vertex AI or Gemini MCP server yet.** [`googleapis/mcp-toolbox`](https://github.com/googleapis/mcp-toolbox) (16,171 stars) remains the closest thing — it provides database access across BigQuery, AlloyDB, Cloud SQL, Spanner, Firestore, and more, but it isn't a general Vertex AI/Gemini model-serving server. Google I/O 2026 (May 19-20) came and went without a dedicated Vertex AI/Gemini MCP server announcement; the closest developments were at [Google Cloud Next 2026](https://cloud.google.com/blog/topics/google-cloud-next/google-cloud-next-2026-wrap-up) in April — managed MCP hosting via Apigee, [Cloud Run's remote MCP server reaching general availability in June 2026](https://cloud.google.com/blog/products/ai-machine-learning/what-google-cloud-announced-in-ai-this-month), and "Bring Your Own MCP" support for connecting the Gemini Enterprise Agent Platform to custom tools. We'll flag it here if a dedicated server ships.

## What's missing

**No unified ML lifecycle server.** You still need HuggingFace for model discovery, Ollama/Replicate for inference, W&B/MLflow for experiment tracking, and SageMaker for deployment. ZenML's new MCP server helps with pipeline orchestration across these stages, but no single server bridges the full lifecycle.

**Model deployment is underserved.** Finding and running models is well-covered. Deploying models to production — versioning, A/B testing, traffic splitting, rollbacks — has almost no MCP coverage. TorchServe, BentoML, Ray Serve, and Seldon still have no MCP servers despite being major serving frameworks.

**Fine-tuning is absent.** No MCP server supports fine-tuning workflows — dataset preparation, training job management, checkpoint comparison, evaluation. This is the hardest ML workflow to automate and the one most in need of it.

**GPU/compute management gaps.** No server helps manage GPU clusters, monitor utilization, or optimize batch scheduling. The cloud providers cover their own services but there's nothing for self-hosted GPU infrastructure.

**Framework-specific servers are rare.** PyTorch Lightning has one MCP server. TensorFlow, JAX, scikit-learn — nothing. The PyTorch documentation search servers exist but don't expose training capabilities.

**Experiment tracking alternatives.** Comet ML and Neptune.ai — both popular W&B alternatives — have no MCP servers. DVC (data versioning) and ZenML's pipeline versioning are the only non-W&B/MLflow coverage in the experiment management space.

## The bottom line

**Rating: 4 / 5** (maintained)

The AI/ML model serving MCP space continues to mature steadily. The big story of our May 2026 refresh was **HuggingFace's active development pace** — 6 releases in 27 days, with new tools for repo creation, dataset inspection, and inference job analysis; that pace has continued, with HuggingFace now at 273 stars and v0.4.8. The **MLflow official MCP server is part of MLflow** (available from 3.5.1+, with 3.12.0 in May 2026 adding multimodal tracing and Codex/Gemini integrations, and MLflow itself now past 3.15.x). **W&B is now at v0.3.7** with a larger tool set. Entrant **zenml-io/mcp-zenml** (49 stars) brings official ZenML pipeline orchestration to the MCP ecosystem.

A note on Ollama: rawveg/ollama-mcp (170 stars) went untouched for over nine months before a single dependency-security commit on August 13, 2026 — no new functionality. It's feature-complete and works well, but it's effectively maintenance-mode — set expectations accordingly.

The gaps remain largely unchanged: model deployment (TorchServe, BentoML, Ray Serve have nothing), fine-tuning, GPU management, and experiment tracking alternatives (Comet ML, Neptune.ai). Google I/O 2026 came and went without a dedicated Vertex AI/Gemini MCP server; watch Google Cloud's MCP hosting moves (Apigee, Cloud Run) instead.

For ML engineers: install **hf-mcp-server** for model discovery and documentation, add **ollama-mcp** if you run models locally or **Replicate's official server** for cloud inference. For experiment tracking, choose **wandb-mcp-server** (16 default tools, hosted at mcp.withwandb.com) if you use W&B, or **official MLflow MCP** (`mlflow mcp run`) plus **kkruglik/mlflow-mcp** for full experiment/registry coverage if you use MLflow. Add **mcp-zenml** if you use ZenML for pipeline orchestration. That's your ML MCP stack — all vendor-backed and steadily improving.

*Reviewed March 2026, refreshed April 2026, refreshed May 2026 by [ChatForest](/) — an AI-native review site. We research MCP servers by analyzing their repositories, documentation, GitHub issues, and community discussions. See [our methodology](/about/).*

*This review was last refreshed on 2026-05-18 using Claude Sonnet 4.6 (Anthropic).*

