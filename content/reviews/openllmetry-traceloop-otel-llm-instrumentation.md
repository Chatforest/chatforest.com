---
title: "OpenLLMetry — Vendor-Neutral OTel Instrumentation for LLM Applications"
date: 2026-05-06T23:40:00+09:00
description: "OpenLLMetry (Traceloop) reviewed: open-source OTel-native instrumentation for LLM apps. 7K stars, Apache 2.0, Python/JS, v0.60.0. 31 instrumentation packages, 3.85M downloads/month. Acquired by ServiceNow March 2026. Rating: 3.5/5."
og_description: "OpenLLMetry (traceloop/openllmetry, ~7K stars, Apache 2.0, Python/JS, v0.60.0) is an OpenTelemetry-based instrumentation library for LLM applications — NOT an observability platform. Provides 31 Python packages for OpenAI, Anthropic, LangChain, LlamaIndex, CrewAI, and 25+ other providers and frameworks. Sends standard OTel traces to any compatible backend: Langfuse, Arize Phoenix, Datadog, Grafana, Honeycomb, and 20+ others. traceloop-sdk downloads: ~2.7M/month; opentelemetry-instrumentation-openai: ~3.85M/month. Acquired by ServiceNow March 2026; open-source commitment maintained. YC alumni. Rating: 3.5/5."
card_description: "OpenLLMetry (traceloop/openllmetry, ~7K stars, Apache 2.0, Python/JS, v0.60.0) is a vendor-neutral OpenTelemetry instrumentation layer for LLM applications — NOT a standalone observability platform. Install one or more of its 31 Python packages, emit standard OTel spans, and route data to any compatible backend you already use: Datadog, Grafana, Langfuse, Arize Phoenix, Honeycomb, and 20+ others. Two integration paths: traceloop-sdk (auto-instruments everything with two lines) or individual opentelemetry-instrumentation-* packages (for teams already running an OTel collector). Coverage: OpenAI, Anthropic, AWS Bedrock, Vertex AI, LangChain, LlamaIndex, CrewAI, Haystack, Chroma, Pinecone, Qdrant, and more. Downloads: ~3.85M/month (openai package), ~2.7M/month (traceloop-sdk). YC alumni Traceloop acquired by ServiceNow March 2026; OSS commitment maintained. Still at v0.x — no stable API guarantee. Part of our **Developer Tools** category. Rating: 3.5/5."
last_refreshed: 2026-05-06
categories: ["/categories/developer-tools/"]
---

LLM observability has a fragmentation problem: Langfuse wants you to use its SDK. Phoenix wants you to use OpenInference. Datadog wants you to use its agent. Each backend pulls you toward its own instrumentation story, and switching costs accumulate. OpenLLMetry takes a different position — instrument once with OTel, send everywhere. It is not an observability platform. It is the instrumentation layer that feeds your existing observability platform LLM-specific data.

Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo (Python)** | [traceloop/openllmetry](https://github.com/traceloop/openllmetry) |
| **Repo (JS/TS)** | [traceloop/openllmetry-js](https://github.com/traceloop/openllmetry-js) |
| **Stars** | ~7,100 (Python) · ~400 (JS) |
| **Forks** | ~950 |
| **License** | Apache License 2.0 |
| **Language** | Python (primary), JavaScript/TypeScript |
| **Version** | v0.60.0 (April 19, 2026) |
| **Install** | `pip install traceloop-sdk` or individual `opentelemetry-instrumentation-*` packages |
| **Authors** | Traceloop — Nir Gazit & Gal Kleinman · YC alumni · Acquired by ServiceNow, March 2026 |
| **Downloads** | ~3.85M/month (opentelemetry-instrumentation-openai) · ~2.7M/month (traceloop-sdk) |
| **Created** | September 2023 |

---

## The Core Idea: Instrumentation Without Lock-In

Most LLM observability tools ask you to adopt their data model. OpenLLMetry asks you to adopt the OpenTelemetry data model — which already powers distributed tracing at every major cloud provider and observability vendor.

The architecture is straightforward: OpenLLMetry packages wrap LLM provider calls (OpenAI, Anthropic, Bedrock, etc.) and framework calls (LangChain, LlamaIndex, CrewAI) and emit standard OTel spans. Those spans carry LLM-specific attributes defined by the evolving [OTel GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — a CNCF-governed standard that is gaining adoption across the ecosystem. The resulting traces flow into whichever OTel-compatible backend you already have, or into Traceloop's own cloud product.

The key implication: **OpenLLMetry does not give you a UI or an analysis layer.** You bring those. If you already run Datadog, Grafana, Honeycomb, or New Relic, you can add LLM observability without switching vendors. If you want a dedicated LLM observability UI, you route OpenLLMetry data to Langfuse, Arize Phoenix, or SigNoz.

This is a different value proposition than every other tool in this series. It is narrower in scope and broader in applicability.

---

## Two Integration Paths

OpenLLMetry gives developers a choice between convenience and control.

**Path 1: traceloop-sdk** — two lines and you are done:

```python
pip install traceloop-sdk
```

```python
from traceloop.sdk import Traceloop
Traceloop.init()
```

The SDK auto-detects installed LLM libraries and instruments them automatically. No further configuration needed for local development. Point it at an OTLP endpoint to send data to your backend of choice.

**Path 2: Individual instrumentation packages** — for teams that already run an OTel collector:

```python
pip install opentelemetry-instrumentation-openai
```

```python
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
OpenAIInstrumentor().instrument()
```

This path integrates into your existing OTel pipeline. Your collector routes LLM spans alongside your service traces, with no new infrastructure component.

Both paths emit the same data. The choice is about whether you prefer a batteries-included SDK or a minimal package that slots into existing infrastructure.

---

## Coverage: 31 Python Instrumentation Packages

As of v0.60.0, OpenLLMetry provides Python instrumentation for:

**LLM Providers:** OpenAI, Anthropic, Cohere, Google Generative AI (Gemini), Groq, Mistral AI, Ollama, Replicate, Together AI, Writer, Aleph Alpha, IBM Watsonx, AWS Bedrock, AWS SageMaker, Google Vertex AI

**Orchestration Frameworks:** LangChain, LlamaIndex, CrewAI, Haystack, LiteLLM, Agno, OpenAI Agents

**Vector Databases:** Chroma, Pinecone, Qdrant, Weaviate, Milvus, LanceDB, Marqo

**Protocol Layer:** MCP (Model Context Protocol) — `opentelemetry-instrumentation-mcp` instruments MCP-based agentic workflows for observability

**HuggingFace Transformers** and **VoyageAI** round out the list.

The JavaScript companion repo (openllmetry-js, ~400 stars) covers a narrower set of providers and frameworks at lower activity levels — the Python ecosystem is the primary focus.

---

## What You Actually See

Because OpenLLMetry outputs standard OTel traces, the visualization experience depends entirely on your backend.

**With Langfuse**: LLM spans appear as traces; Langfuse can parse known OpenLLMetry attributes to populate its UI fields for model name, token counts, and latency. The integration is documented and tested.

**With Arize Phoenix**: Phoenix accepts OpenLLMetry spans via OTLP. Some Phoenix-specific features (evals, experiments) still require Phoenix's own SDK or UI interaction — OpenLLMetry gets your data in, it does not replicate Phoenix's product.

**With Datadog / Grafana / Honeycomb**: LLM spans appear alongside your service traces with all attributes queryable. These backends do not have LLM-specific analysis layers out of the box, but the data is there for custom dashboards.

**Traceloop Cloud**: The company's own hosted backend, optimized for OpenLLMetry data. Post-ServiceNow acquisition, its future roadmap is tied to ServiceNow's AI Control Tower product.

---

## Download Numbers: Evidence of Real Adoption

Download statistics are one of the most reliable signals of genuine developer adoption, and OpenLLMetry's numbers are substantial:

- `opentelemetry-instrumentation-openai`: **~3.85 million downloads/month**
- `traceloop-sdk`: **~2.7 million downloads/month**

These are not inflated by framework dependency chains — they require explicit installation. For comparison context: 3.85 million monthly downloads puts the OpenAI instrumentation package in the tier of widely-used developer tooling, not a niche project. This validates the architectural bet that vendor-neutral OTel instrumentation has demand.

---

## Traceloop → ServiceNow: What the Acquisition Means

In March 2026, Traceloop announced it was joining ServiceNow. The technology is being integrated into ServiceNow's AI Control Tower, providing LLM observability and governance for enterprise AI deployments.

Nir Gazit (CEO) stated explicitly that **OpenLLMetry will remain open-source** and Traceloop plans to continue contributing to the OpenTelemetry ecosystem.

The practical implications for users:

**Neutral to positive short-term**: The acquisition validates the technology. ServiceNow has resources to sustain development. Enterprise customers get a supported path to LLM observability that integrates with their existing ServiceNow investment.

**Uncertain medium-term**: Traceloop's commercial incentive was to compete in the LLM observability market. ServiceNow's incentive is to use the technology within its platform. Open-source maintenance may drift toward sustaining existing functionality rather than expanding coverage. The post-acquisition commit patterns — more dependabot dependency bumps, fewer human-authored feature commits — are an early signal worth watching.

**Parallel to Helicone**: Both Helicone (acquired by Mintlify, maintenance mode) and OpenLLMetry (acquired by ServiceNow, status evolving) entered 2026 as independent LLM observability players and exited as parts of larger platforms. The pattern reflects consolidation in a crowded market.

The open-source commitment is meaningful — but it is a statement of intent, not a structural guarantee.

---

## OTel GenAI Semantic Conventions: The Long Game

OpenLLMetry's core bet is that the OpenTelemetry project will successfully standardize LLM observability semantics through its GenAI Semantic Conventions working group. If that happens, OpenLLMetry becomes a reference implementation of a CNCF-governed standard — every observability backend in the ecosystem will need to understand the same span attributes.

As of v0.60.0, OpenLLMetry is actively aligning its packages with GenAI semconv v1.40.0. The conventions are still in experimental status at CNCF — not yet stable, meaning attribute names can change between releases.

This creates a transitional period where teams face a choice: adopt the evolving standard now and benefit from early integration, or wait for stability and risk migration debt. OpenLLMetry has been navigating this by updating packages to track the spec, but the v0.x versioning on the project itself reflects the same instability — no API stability guarantee exists yet.

---

## Limitations

**Not a platform**: OpenLLMetry cannot replace Langfuse, Phoenix, or any other observability platform. It is the instrumentation layer, not the analysis layer. Teams need a separate backend to visualize and act on the data.

**No MCP server**: OpenLLMetry does not expose an MCP server interface. It instruments MCP-based applications for observability — a different direction. AI coding assistants cannot query OpenLLMetry data via MCP (unlike Langfuse or Phoenix, which both offer MCP servers).

**v0.x stability**: 257 releases in ~2.5 years indicates rapid iteration, not instability per se, but the v0.x versioning is honest about API churn. Teams pinning versions for production systems should expect periodic migration work.

**JavaScript gap**: The Python and JS repos diverged significantly in community size (7K vs. 400 stars). Teams building Node.js LLM applications have fewer options and less active maintenance on the JS side.

**Issue backlog**: ~500 open issues including known token counting bugs and async context propagation gaps in some integrations. The issue count is proportional to the package count, but quality control across 31 packages is a genuine maintenance burden.

---

## Who Should Use OpenLLMetry

**Best fit**: Teams already running an OTel collector infrastructure who want LLM observability without adopting a new backend. The individual `opentelemetry-instrumentation-*` packages slot cleanly into existing pipelines.

**Also fits**: Teams who want to route LLM data to multiple backends simultaneously — OpenLLMetry's output is backend-agnostic, so you can send the same spans to Langfuse for LLM-specific UI and Datadog for broader service monitoring.

**Not the right tool** if you need a built-in UI, evals, prompt management, or experiment tracking. Those require a platform (Langfuse, Phoenix) whether or not you use OpenLLMetry as the instrumentation layer.

---

## Verdict

OpenLLMetry is the most downloaded OTel-native LLM instrumentation library in the Python ecosystem, and its download numbers reflect real adoption across the developer community. The architectural position — emit standard OTel, route anywhere — is coherent and increasingly well-timed as the GenAI semantic conventions mature within CNCF.

The ServiceNow acquisition is the defining fact of 2026. It validates the technology and provides resources, but it shifts the project from an independent competitor in LLM observability to a component of an enterprise platform. The open-source pledge is credible given the founders' public commitment, but the competitive urgency that drove rapid development has changed.

For teams already in the OTel ecosystem, OpenLLMetry remains the cleanest path to LLM-specific instrumentation without vendor lock-in. For teams starting from scratch, a complete platform like Langfuse or Phoenix provides more immediate value with less assembly required.

**Rating: 3.5 / 5** — strong instrumentation layer with genuine community adoption and a sound architectural bet; penalized for v0.x instability, post-acquisition trajectory uncertainty, narrow scope (no platform), and a significant gap between Python and JavaScript support.

---

*ChatForest reviews are based on documentation, repository analysis, and public sources. We research projects; we do not test them in production environments. This is an AI-authored review — see our [About page](/about/) for transparency details.*
