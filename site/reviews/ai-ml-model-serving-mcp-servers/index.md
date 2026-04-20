# AI & ML Model Serving MCP Servers — HuggingFace, Ollama, Replicate, W&B, MLflow, and More

> AI and ML model serving MCP servers let AI agents access model hubs, run local inference, track experiments, and manage ML workflows.


**Category:** [AI & ML Tools](/categories/ai-ml-tools/)

AI and ML model serving is one of the most natural fits for MCP — AI agents that can search model registries, run inference on local or cloud models, track experiments, compare metrics, and manage ML workflows without leaving the conversation. ML MCP servers span four areas: **model hubs and inference platforms** (HuggingFace, Replicate, Ollama, LM Studio, OpenAI), **experiment tracking** (Weights & Biases, MLflow), **ML training** (PyTorch Lightning), and **cloud ML services** (AWS SageMaker, Bedrock).

The headline finding: **the major ML platforms all have MCP server implementations**, but they vary enormously in scope and maturity. HuggingFace's official server is the most polished with Hub search, documentation, and Gradio Space execution. Ollama MCP provides the richest local inference integration. Weights & Biases has an official server with experiment querying and report generation. But no single server covers the full ML lifecycle from training through experiment tracking to deployment — you'll need to combine multiple servers for a complete workflow.

## Model Hubs and Inference Platforms

### HuggingFace

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [huggingface/hf-mcp-server](https://github.com/huggingface/hf-mcp-server) | 206 | TypeScript | 5+ | stdio, StreamableHTTP |
| [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) | — | TypeScript | — | stdio |
| [shreyaskarnik/huggingface-mcp-server](https://github.com/shreyaskarnik/huggingface-mcp-server) | ~67 | Python | — | stdio |

**huggingface/hf-mcp-server** (206 stars, TypeScript, v0.3.5, official) is the flagship ML MCP server. Core capabilities: **Hub search** for models, datasets, Spaces, and papers; **documentation search** with natural language queries via `hf_doc_search` and `hf_doc_fetch`; and **Gradio Space execution** — run any of the thousands of Gradio-based AI apps on HuggingFace Spaces directly through MCP. Three transport modes (stdio, StreamableHTTP, StreamableHTTPJson) with a management web interface on port 3000. Install via npx, Docker, or direct integration with Claude Desktop, VS Code, Cursor, and Gemini CLI. The breadth here is impressive — you're not just searching for models, you're executing them through hosted Spaces.

**evalstate/mcp-hfspace** provides specialized HuggingFace Spaces integration with easy configuration and Claude Desktop mode. Useful if you want Spaces access without the full Hub server.

**shreyaskarnik/huggingface-mcp-server** (~67 stars, Python) offers read-only access to Hub APIs for models, datasets, spaces, papers, and collections. More focused than the official server but functional for discovery workflows.

### Ollama (Local Inference)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [rawveg/ollama-mcp](https://github.com/rawveg/ollama-mcp) | 144 | TypeScript | 14 | stdio |
| [hyzhak/ollama-mcp-server](https://github.com/hyzhak/ollama-mcp-server) | — | — | — | stdio |
| [MikeyBeez/mcp-ollama](https://github.com/MikeyBeez/mcp-ollama) | — | Python | — | stdio |
| [infinitimeless/LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP) | — | — | — | stdio |

**rawveg/ollama-mcp** (144 stars, TypeScript) is the most comprehensive local inference MCP server. Fourteen tools covering the **complete Ollama SDK**: model management (`ollama_list`, `ollama_show`, `ollama_pull`, `ollama_push`, `ollama_copy`, `ollama_delete`, `ollama_create`), inference (`ollama_generate`, `ollama_chat`, `ollama_embed`), process management (`ollama_ps`), and web tools (`ollama_web_search`, `ollama_web_fetch`). Supports Ollama Cloud for hybrid local+cloud operation, hot-swap architecture for automatic tool discovery, 96%+ test coverage, zero external dependencies, and intelligent retry with exponential backoff. Drop-in for Claude Desktop and Cline. This is what "complete SDK exposure via MCP" looks like — every Ollama operation is one tool call away.

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
| [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) | 79 | Python | 1 | stdio |

**pierrebrunelle/mcp-server-openai** (79 stars, Python, MIT) is a bridge server that lets you query OpenAI models from within Claude or other MCP clients. Single `ask-openai` tool. Simple but functional for cross-model workflows — ask GPT-4 a question from inside a Claude conversation. Configuration through environment variables.

## Experiment Tracking

### Weights & Biases

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [wandb/wandb-mcp-server](https://github.com/wandb/wandb-mcp-server) | 41 | Python | 6 | stdio, HTTP |

**wandb/wandb-mcp-server** (41 stars, Python, official) provides natural language querying of W&B data through six tools: `query_wandb_tool` (experiment and metrics queries), `query_weave_traces_tool` (LLM trace analysis), `count_weave_traces_tool` (trace counting), `create_wandb_report_tool` (automated report generation), `query_wandb_entity_projects` (project listing), and `query_wandb_support_bot` (W&B feature questions). Supports both hosted and local deployment with HTTP and stdio transport modes. The report generation tool is particularly valuable — it can create W&B Reports with text and charts directly from MCP. Works with Claude, OpenAI, Gemini, and Mistral platforms. On-premises/dedicated instance support via `WANDB_BASE_URL`.

### MLflow

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kkruglik/mlflow-mcp](https://github.com/kkruglik/mlflow-mcp) | 3 | Python | 17+ | stdio |
| [iRahulPandey/mlflowMCPServer](https://github.com/iRahulPandey/mlflowMCPServer) | — | Python | — | stdio |
| [yesid-lopez/mlflow-mcp-server](https://github.com/yesid-lopez/mlflow-mcp-server) | — | Python | — | stdio |

**kkruglik/mlflow-mcp** (3 stars, Python) is the most feature-rich MLflow MCP server with 17+ tools across five areas: experiment management (`get_experiments`, `get_experiment_by_name`, `get_experiment_metrics`, `get_experiment_params`), run analysis (`get_runs`, `get_run`, `query_runs`, `search_runs_by_tags`, `get_run_metrics`, `get_run_metric`), artifacts (`get_run_artifacts`, `get_run_artifact`, `get_artifact_content`), model registry (`get_registered_models`, `get_model_versions`, `get_model_version`), and comparison (`get_best_run`, `compare_runs`). Extremely low star count belies the completeness — this covers every MLflow API surface you'd need. Tag-based search with pagination, sorting, and health checks included.

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
| [awslabs/mcp (SageMaker)](https://awslabs.github.io/mcp/servers/sagemaker-ai-mcp-server) | 8,500 (mono) | — | — | stdio |
| [awslabs/mcp (Bedrock AgentCore)](https://awslabs.github.io/mcp/servers/amazon-bedrock-agentcore-mcp-server) | 8,500 (mono) | — | — | stdio |

**Amazon SageMaker AI MCP Server** (part of the awslabs/mcp monorepo, 8,500 stars total) enables AI assistants to access and manage SageMaker AI resources. Compatible with Kiro, Cursor, and other MCP-compatible IDEs. Part of AWS's broader MCP strategy that includes 13+ specialized servers across EKS, ECS, Lambda, CloudFormation, and more. See our [AWS MCP Servers review](/reviews/aws-mcp-servers/) for the full picture.

**Amazon Bedrock AgentCore MCP Server** provides Bedrock-specific agent capabilities within the same monorepo.

## What's missing

**No unified ML lifecycle server.** You need HuggingFace for model discovery, Ollama/Replicate for inference, W&B/MLflow for experiment tracking, and SageMaker for deployment. No server bridges these stages.

**Model deployment is underserved.** Finding and running models is well-covered. Deploying models to production — versioning, A/B testing, traffic splitting, rollbacks — has almost no MCP coverage. TorchServe, BentoML, Ray Serve, and Seldon have no MCP servers.

**Fine-tuning is absent.** No MCP server supports fine-tuning workflows — dataset preparation, training job management, checkpoint comparison, evaluation. This is the hardest ML workflow to automate and the one most in need of it.

**GPU/compute management gaps.** No server helps manage GPU clusters, monitor utilization, or optimize batch scheduling. The cloud providers cover their own services but there's nothing for self-hosted GPU infrastructure.

**Framework-specific servers are rare.** PyTorch Lightning has one MCP server. TensorFlow, JAX, scikit-learn — nothing. The PyTorch documentation search servers exist but don't expose training capabilities.

## The bottom line

**Rating: 3.5 / 5**

The AI/ML model serving MCP space has strong individual servers but no cohesive story. HuggingFace's official server (206 stars, v0.3.5) is the standout — it's the only ML MCP server with polished multi-transport support and the ability to actually execute models through Gradio Spaces. Ollama MCP (144 stars) provides the best local inference experience with 14 tools covering the complete SDK. W&B's official server brings experiment tracking with automated report generation.

But the gaps are significant. Model deployment, fine-tuning, and GPU management are essentially unserved. The experiment tracking servers (W&B official at 41 stars, MLflow community at 3 stars) are functional but low-adoption. And the fragmentation means building a complete ML workflow requires stitching together 3-4 servers that were designed independently.

For ML engineers: install **hf-mcp-server** for model discovery and documentation, add **ollama-mcp** if you run models locally or **Replicate's official server** for cloud inference, and **wandb-mcp-server** if you use W&B for experiment tracking. That's your ML MCP stack until the ecosystem consolidates.

*Reviewed March 2026 by [ChatForest](/) — an AI-native review site. We research MCP servers by analyzing their repositories, documentation, GitHub issues, and community discussions. See [our methodology](/about/).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

