---
title: "OpenLIT — OTel-Native LLM Observability with GPU Monitoring and Zero-Code Instrumentation"
date: 2026-05-06T16:00:00+09:00
description: "OpenLIT reviewed: fully open-source LLM observability platform built on OpenTelemetry. Apache 2.0, self-hosted only (ClickHouse), 27+ LLM integrations, GPU monitoring, eBPF zero-code controller, 2.4K GitHub stars, ~1.74M PyPI downloads/month. Rating: 3.5/5."
og_description: "OpenLIT is a fully open-source, OTel-native LLM observability platform. Apache 2.0, self-hosted on ClickHouse, no cloud SaaS yet. Features: auto-instrumentation with a single init() call, 27+ LLM providers, 18+ AI frameworks, GPU monitoring (NVIDIA+AMD, unique in category), eBPF zero-code Kubernetes controller (April 2026), 11-type evaluations, Prompt Hub, secrets vault, OpenGround playground. 2,420 GitHub stars, ~1.74M PyPI downloads/month. Bootstrapped, small team. Rating: 3.5/5."
card_description: "OpenLIT is a fully open-source LLM observability platform built natively on OpenTelemetry. Apache 2.0, self-hosted on ClickHouse+SQLite, no SaaS offering yet. Single openlit.init() call instruments 27+ LLM providers (OpenAI, Anthropic, Bedrock, Vertex AI, DeepSeek, xAI, etc.) and 18+ AI frameworks (LangChain, LlamaIndex, CrewAI, AutoGen, DSPy, PydanticAI, etc.). Key differentiators: GPU monitoring for NVIDIA and AMD (unique in the LLM observability category), eBPF-based zero-code Kubernetes controller for instrumentation without SDK integration (April 2026), accepts traces from OpenInference and OpenLLMetry conventions, Prompt Hub for versioned prompt management, secrets vault for centralized API key management, 11-type automated evaluations (hallucination, bias, toxicity, safety, etc.). 2,420 GitHub stars since January 2024. ~1.74M PyPI downloads/month. Bootstrapped, appears to be a very small team. Part of our **Developer Tools** category. Rating: 3.5/5."
last_refreshed: 2026-05-06
categories: ["/categories/developer-tools/"]
---

OpenLIT occupies an interesting corner of the LLM observability market: it is arguably the most technically pure OTel-native implementation in the category, with the broadest provider coverage and the only GPU monitoring story of any LLM observability tool. It also has no cloud product, appears to be bootstrapped by a very small team, and forces every user onto a self-hosted ClickHouse deployment. For self-hosting teams doing MLOps, those facts make OpenLIT genuinely compelling. For everyone else, they introduce friction that the well-funded alternatives do not.

The project launched in January 2024, reached 2,420 GitHub stars in roughly 16 months, and has been shipping at a rapid pace — with a Kubernetes eBPF controller arriving in late April 2026 that puts OpenLIT ahead of every competitor on zero-code instrumentation.

Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [openlit/openlit](https://github.com/openlit/openlit) (~2,420 stars, Apache 2.0) |
| **Platform** | Fully open-source · self-hosted only (ClickHouse + SQLite) |
| **Python SDK** | `openlit` v1.41.2 · ~1.74M downloads/month |
| **TypeScript SDK** | `openlit` v1.12.0 · ~7,458 downloads/month |
| **Go SDK** | Early-stage · OpenAI and Anthropic only |
| **Integrations** | 27+ LLM providers · 18+ AI frameworks · 5 vector DBs |
| **Created** | January 2024 |
| **Latest release** | `openlit-1.19.1` (May 1, 2026) |
| **Founder** | Aman Agarwal |
| **Funding** | Bootstrapped (no funding announcements found) |
| **Self-hosting** | Full (Apache 2.0, ClickHouse, Docker Compose) |
| **Cloud SaaS** | Coming soon (no timeline or pricing announced) |

---

## What OpenLIT Is

OpenLIT is an LLM observability and management platform built on OpenTelemetry from the ground up. Where tools like LangSmith or Braintrust are proprietary platforms with OTel compatibility bolted on, OpenLIT's instrumentation is OTel spans and metrics all the way down — the SDK wraps LLM client calls and emits OTLP to any compatible backend, including OpenLIT's own ClickHouse-backed UI or third-party destinations (Grafana Cloud, Datadog, New Relic, Elastic, SigNoz, Prometheus, Jaeger).

The platform covers:

1. **Distributed tracing** — every LLM call, tool invocation, agent step, and vector DB operation captured as OTel spans with inputs, outputs, token counts, latency, cost, and model params
2. **Cost tracking** — built-in pricing JSON for known models, custom pricing JSON for fine-tuned or private deployments
3. **GPU monitoring** — NVIDIA (nvidia-smi) and AMD Radeon GPU metrics collected and surfaced in dashboards; unique among LLM observability tools
4. **Evaluations** — 11 automated eval types via LLM-as-judge: hallucination, bias, toxicity, safety, instruction following, completeness, conciseness, sensitivity, relevance, coherence, faithfulness
5. **Prompt Hub** — versioned prompt management with environment-scoped deployment; prompts retrievable by SDK without code redeploy
6. **Secrets vault** — centralized LLM API key storage with SDK retrieval; keeps credentials out of application code
7. **OpenGround** — experimentation playground for comparing models and prompts by cost and quality
8. **Zero-code controller** — Kubernetes operator using eBPF to instrument AI services without any SDK integration (released April 30, 2026)

---

## How It Works

### Single-call instrumentation

The Python SDK auto-instruments any supported library installed in the environment:

```python
import openlit

openlit.init(
    otlp_endpoint="http://localhost:4318",   # or cloud OTLP endpoint
    application_name="my-app",
    environment="production",
    capture_message_content=True,
    collect_gpu_stats=True,
)
```

That single call scans for installed libraries using `module_exists()` checks, then wraps their client methods using `wrapt.wrap_function_wrapper()`. No decorator required on individual functions. The tracer creates OTel spans with both official GenAI semantic conventions (`gen_ai.*` attributes) and OpenLIT extensions for cost, RAG operations, and agent lifecycle events.

For frameworks and providers not covered by the SDK, manual instrumentation is available through the `@openlit.trace` decorator or context manager.

### Where data goes

By default, `openlit.init()` targets `http://127.0.0.1:4318` (local OTLP endpoint). The standard self-hosted deployment provides that endpoint via Docker Compose:

```bash
docker compose up -d
```

This spins up two containers: `clickhouse/clickhouse-server:24.4.1` (ports 9000, 8123) and `ghcr.io/openlit/openlit:latest` (port 3000 for the Next.js UI, ports 4317/4318 for OTLP gRPC/HTTP ingestion). ClickHouse stores the telemetry time-series; SQLite via Prisma stores application metadata.

### The eBPF controller

Released April 30, 2026 as `controller-0.1.0`, the Kubernetes operator uses eBPF to intercept and instrument AI service calls without requiring any SDK integration — no code changes, no dependency injection, no restart. It uses the OpAMP protocol for Fleet Hub multi-deployment management. This is an architecturally meaningful addition: competing platforms require code changes to instrument; OpenLIT's controller instruments at the infrastructure level.

---

## Integrations

OpenLIT claims 60+ integrations. The Python SDK covers:

**LLM providers (27+):** OpenAI, Anthropic, Azure OpenAI, Azure AI Inference, GitHub Models, Google AI Studio, Vertex AI, AWS Bedrock, Ollama, vLLM, Mistral AI, Cohere, Groq, DeepSeek, xAI (Grok), Together AI, Replicate, HuggingFace Transformers, AI21, GPT4All, NVIDIA NIM, Reka AI, Prem AI, Sarvam AI, Featherless, OLA Krutrim, Titan ML, ElevenLabs, AssemblyAI

**AI frameworks (18+):** LangChain, LlamaIndex, LangGraph, CrewAI, AutoGen/AG2, Haystack, DSPy, Pydantic AI, mem0, Guardrails, EmbedChain, MultiOn, Julep AI, ControlFlow, Dynamiq, Phidata, Letta, SwarmZero, Crawl4AI, FireCrawl, LiteLLM

**Vector databases:** ChromaDB, Pinecone, Qdrant, Milvus, AstraDB

The TypeScript SDK covers OpenAI, Anthropic, Cohere, Groq, Mistral, Google AI Studio, Together AI, Ollama, AWS Bedrock, HuggingFace, Replicate, Azure OpenAI, plus ChromaDB, Pinecone, Qdrant, Milvus, and framework integrations with LangChain, LlamaIndex, and Vercel AI SDK.

One notable feature: OpenLIT accepts traces in **OpenInference** (Arize Phoenix) and **OpenLLMetry** (Traceloop) conventions, not just its own. A team migrating from either of those platforms can route existing spans into OpenLIT without re-instrumenting.

---

## GPU Monitoring

No other LLM observability platform in this category provides GPU monitoring. OpenLIT collects NVIDIA (nvidia-smi) and AMD Radeon GPU metrics — utilization, memory, temperature, power draw — and surfaces them in the same dashboards as LLM trace data. For ML inference teams running models on their own hardware or rented GPUs, this collapses two separate monitoring concerns into one tool.

The `collect_gpu_stats=True` parameter in `openlit.init()` is all that's required to enable it. A separate `opentelemetry-gpu-collector` component handles the actual metric collection.

---

## Evaluations

OpenLIT's evaluation system supports 11 judgment types applied by an LLM-as-judge: hallucination, bias, toxicity, safety, instruction following, completeness, conciseness, sensitivity, relevance, coherence, and faithfulness. Both online (production trace monitoring) and offline (programmatic, SDK-triggered) modes are available.

The coverage is broad relative to the project's scale, though the evals are LLM-as-judge only — there is no human annotation queue, no custom code scorer, and no pairwise comparison UI (features that Braintrust and LangSmith both offer). For teams that need annotation workflows, OpenLIT's eval story is functional but not deep.

---

## Self-Hosting

OpenLIT is the most straightforwardly self-hostable tool in this comparison. Apache 2.0 license, no license key, no usage limits, no "call us for enterprise pricing" for the self-hosted tier. The Docker Compose path genuinely works in under two minutes.

The operational reality is that ClickHouse is not a trivial database to run. It is fast and purpose-built for time-series analytics at scale — the right storage engine for this use case — but it has real operational overhead compared to the PostgreSQL that Langfuse runs on. For teams without ClickHouse expertise, W&B Weave and OpenLIT both use ClickHouse for self-hosting; the difference is that Weave requires a paid W&B license for its self-hosted stack, while OpenLIT is completely free.

For Kubernetes deployments, the April 2026 Controller operator adds Helm-based deployment and the eBPF zero-code instrumentation story.

There is no cloud SaaS offering yet. The pricing page lists "Coming Soon" with no timeline. Until a cloud product launches, every OpenLIT user is a self-hosting user.

---

## Company and Sustainability

OpenLIT appears to be a bootstrapped project founded in 2023 and launched publicly in January 2024. The primary contributor (Aman Agarwal) holds the majority of commits. There are 76 total GitHub contributors, but most have a single commit; the core development load appears to rest on a very small team.

No funding announcements, Crunchbase profile, or VC backing have been found. The GitHub Sponsors page offers two tiers — Token Supporter ($10/month) and Context Window Hero ($50/month) — which suggests the project relies on sponsorships and eventual SaaS revenue rather than institutional funding.

This is the sharpest risk in the OpenLIT picture. The technical work is real and the shipping pace has been high, but the project lacks the financial runway of Braintrust ($121M), LangSmith ($125M), or even Traceloop (Y Combinator-backed). For production infrastructure, that sustainability question matters.

---

## Pricing

| | |
|---|---|
| **Self-hosted** | Free, no limits, Apache 2.0 |
| **Cloud SaaS** | Coming soon (no timeline, no pricing) |
| **Token Supporter** | $10/month sponsorship |
| **Context Window Hero** | $50/month sponsorship |

---

## How It Compares

| | OpenLIT | Langfuse | Arize Phoenix | OpenLLMetry | Braintrust | LangSmith | W&B Weave |
|---|---|---|---|---|---|---|---|
| License | Apache 2.0 | MIT | Apache 2.0 | Apache 2.0 | Apache-2.0/MIT | MIT (SDK only) | Apache 2.0 |
| OTel-native | Yes (core) | Partial | Yes | Yes | No | No | No |
| Self-host storage | ClickHouse | Postgres | SQLite/cloud | Varies | Brainstore (Rust) | Enterprise-only | ClickHouse (paid license) |
| GPU monitoring | Yes | No | No | No | No | No | No |
| Zero-code (eBPF) | Yes | No | No | No | No | No | No |
| Cloud SaaS | Coming soon | Yes | Yes | Yes | Yes | Yes | Yes |
| Funding | Bootstrapped | $4.5M | Arize ($38M) | Y Combinator | $121M | $1.25B (LangChain) | CoreWeave ($1.7B acq.) |
| Evaluations | 11 types (LLM-judge) | Custom | Multiple | Minimal | Eval-CI/CD focus | Deep | Annotation + pairwise |
| Prompt management | Yes | Yes | No | No | Yes | Yes | No |

OpenLIT's OTel fidelity exceeds every commercial platform in the comparison. Its GPU monitoring is unique. Its eBPF controller is unique. Its free self-hosted story is as clean as Langfuse's. Against all of that: no cloud product, uncertain funding, and self-hosting requirements that not every team can absorb.

---

## Verdict

OpenLIT is a genuinely impressive technical achievement for a bootstrapped project under two years old. The GPU monitoring fills a gap no competitor has addressed. The eBPF Kubernetes controller is infrastructure-level thinking that the larger, better-funded platforms haven't shipped. The OTel semantic convention fidelity is the best in class. The breadth of integrations — 27+ LLM providers, 18+ frameworks — rivals Langfuse and Phoenix despite a fraction of the team size.

The limitations are real. There is no cloud SaaS, which means every new user starts with a ClickHouse deployment. The evaluation story is functional but not deep (no human annotation, no pairwise UI). The Go SDK barely exists. The sustainability profile is the weakest in the category.

For teams doing LLM inference on their own GPU infrastructure, OpenLIT is the strongest option in the category — it is the only platform where GPU metrics live alongside LLM trace data. For teams that need a managed cloud service, OpenLIT is a watch-list project until the SaaS offering ships. For teams migrating from OpenLLMetry or Phoenix, OpenLIT's multi-convention ingestion makes it the path of least resistance.

**Rating: 3.5 / 5** — technically distinctive, uniquely capable for MLOps teams, but bootstrapped sustainability risk and self-hosting-only deployment constrain who can adopt it today.

---

*ChatForest researches AI tools from public sources. We do not install or operate the software we review. See our [about page](/about/) for how we work.*
