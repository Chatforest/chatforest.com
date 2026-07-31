---
title: "Grok on Databricks Agent Bricks: xAI's First Lakehouse-Native Agent Integration"
date: 2026-06-19
description: "xAI's Grok 4.3 and grok-build-0.1 are now available natively in Databricks Agent Bricks, announced at DAIS 2026 on June 18. Grok connects directly to Lakehouse data via Genie Ontology — no exfiltration, Unity Catalog governance. Here's the builder guide."
og_description: "Grok 4.3 and grok-build-0.1 landed in Databricks Agent Bricks at DAIS 2026 on June 18. Select from AI Playground, connect to Lakehouse data via Genie Ontology, governed by Unity Catalog. Zero data retention. $1.25/$2.50/M for 4.3, $1.00/$2.00/M for build-0.1. Builder guide."
content_type: "Builder's Log"
categories: ["Model Releases", "xAI", "Databricks", "Enterprise", "Agents"]
tags: ["grok", "xai", "databricks", "agent-bricks", "lakehouse", "unity-catalog", "genie-ontology", "june-2026", "enterprise-ai", "dais-2026", "grok-4.3", "grok-build"]
author: "ChatForest"
sources_audited: 2026-07-31
---

**At a glance:** On June 18, 2026, at the [Databricks Data + AI Summit](https://www.databricks.com/blog/agent-bricks-dais-2026), xAI announced that [Grok is available natively in Databricks Agent Bricks](https://www.basenor.com/blogs/news/xai-grok-lands-on-databricks-at-the-2026-data-ai-summit). Two models: `grok-4.3` and `grok-build-0.1`. Both connect directly to your Lakehouse via [Genie Ontology](https://www.databricks.com/blog/agent-bricks-dais-2026) — agents reason over governed data without moving it. [Unity Catalog handles access control](https://developers.databricks.com/docs/agents/ai-gateway). xAI does not retain data submitted through this path. Select either model from the AI Playground UI or configure programmatically.

---

## What Was Announced

The June 18 announcement is not a generic marketplace listing. Databricks [describes it as a partnership with SpaceX](https://www.databricks.com/blog/agent-bricks-dais-2026) (xAI's parent company) to make Grok natively available inside Databricks Agent Bricks, with direct access to Lakehouse-hosted data through the same [Unity Catalog governance layer](https://developers.databricks.com/docs/agents/ai-gateway) that controls your tables, volumes, and lineage metadata.

Two models are available at launch:

| Model | Best for | Input | Output |
|---|---|---|---|
| [`grok-4.3`](https://docs.x.ai/developers/models/grok-4.3) | Reasoning, analysis, multimodal | $1.25/M | $2.50/M |
| [`grok-build-0.1`](https://docs.x.ai/developers/models/grok-build-0.1) | Code generation, technical tasks | $1.00/M | $2.00/M |

(Rates shown are the standard tier for prompts under 200K tokens; xAI charges more above that threshold.) Context windows differ between the two: `grok-4.3` runs a [1M-token context window](https://docs.x.ai/developers/models/grok-4.3) with Grok's [configurable reasoning modes](https://www.datastudios.org/post/grok-4-3-reasoning-effort-speed-depth-cost-and-output-reliability-settings-explained) (none/low/medium/high, default `low`); `grok-build-0.1` is a separate coding-focused model with a [256K-token context window](https://docs.x.ai/developers/models/grok-build-0.1), [trained specifically for agentic coding workflows](https://docs.x.ai/developers/models/grok-build-0.1).

---

## The Core Differentiator: Genie Ontology

The part that makes this integration interesting for builders is not that Grok is available on another platform. The part that matters is how Grok connects to data.

**Standard integrations** work like this: your agent calls a tool, the tool queries your database, returns results, and the model reasons over the returned text. Your data leaves its governed environment at the query boundary.

**The Databricks integration** works differently. [Genie Ontology](https://www.databricks.com/blog/agent-bricks-dais-2026) gives Grok semantic access to your Lakehouse: Databricks describes it as continuously learning an ontology on your data and incorporating human-annotated business semantics — for example, resolving questions like fiscal-year timing, sales leadership, or how "customer" is defined for your business. The model understands *what your data means*, not just what it says.

Practically, this means:

- An agent selecting `grok-4.3` in Agent Bricks can reason over your Delta tables without the data being transmitted to xAI
- The ontology layer translates natural-language queries into governed Lakehouse operations
- All reasoning traces, memory, and outputs are stored back in your Lakehouse under Unity Catalog governance
- Unity Catalog's [row- and column-level access policies](https://www.databricks.com/blog/abac-row-filtering-and-column-masking-policies-governed-tags-and-data-classification-are-now) are designed to flow through to what any downstream consumer — including an agent — can see

This is the same "governance comes for free" thesis that Agent Bricks is built on, extended to xAI's model family.

---

## Data Privacy

Per reporting on the announcement, [model partners including xAI do not retain data submitted through this integration](https://www.basenor.com/blogs/news/xai-grok-lands-on-databricks-at-the-2026-data-ai-summit), and Databricks itself does not train foundation models on customer data. [Unity Catalog handles access control](https://developers.databricks.com/docs/agents/ai-gateway) at the Databricks boundary.

For regulated industries, this matters. The data never leaves your Databricks security perimeter in a form that xAI controls. Governance is enforced before the model ever sees the data.

---

## How to Use It

### Option 1: AI Playground (low-code)

The simplest path:

1. Open [Databricks AI Playground](https://docs.databricks.com/aws/en/large-language-models/ai-playground) (`AI/ML → Playground` in the left navigation)
2. In the model dropdown, select `grok-4.3` or `grok-build-0.1`
3. Add tools using the low-code UI — connect to Lakehouse tables, Unity Catalog volumes, or Genie Spaces
4. Test the agent interactively
5. Export to code when ready for production deployment

### Option 2: Agent Bricks SDK (code-first)

For production deployments, [Agent Bricks supports LangGraph, Agno, CrewAI, the Claude Code SDK, and OpenAI Agent SDKs](https://www.databricks.com/blog/agent-bricks-dais-2026) as agent harnesses. Grok slots in as a model choice within any of these:

```python
from databricks.sdk import WorkspaceClient
from databricks_langchain import ChatDatabricks

# Point LangChain at Grok via Unity AI Gateway
llm = ChatDatabricks(
    endpoint="grok-4-3",  # or "grok-build-0-1" — confirm exact endpoint ID in your workspace
    max_tokens=4096,
)
```

Note: the LangChain integration package was renamed from `langchain-databricks` to [`databricks-langchain`](https://pypi.org/project/langchain-databricks/) (import as `databricks_langchain`); the older package name is deprecated.

The [Unity AI Gateway](https://developers.databricks.com/docs/agents/ai-gateway) tracks usage, enforces rate limits, logs payloads, and attributes cost — the same gateway layer that governs other models in your Databricks environment.

> **Note on pricing:** Databricks marketplace pricing for Grok may differ from xAI direct API pricing. The figures in this article ($1.25/$2.50/M for grok-4.3; $1.00/$2.00/M for grok-build-0.1) are xAI's published rates. Check your Databricks account for marketplace-specific pricing.

---

## Grok on Databricks vs. Grok on Bedrock

If you're evaluating where to run Grok, the core question is where your data and governance live:

**Choose Databricks if:**
- Your data is in a Databricks Lakehouse and you want agents to reason over it with Genie Ontology context
- You're already using Agent Bricks for your agent stack
- You need Unity Catalog governance to flow through to agent behavior
- You want Databricks billing consolidation

**Choose [Grok on Bedrock](/builders-log/xai-grok-4-3-amazon-bedrock-june-2026-builder-guide/) if:**
- Your workloads run on AWS and you want IAM-based access
- You're already in the Bedrock SDK ecosystem
- You want Bedrock's audit trails and CloudWatch integration
- You don't need Lakehouse-native data access

Both paths carry xAI's zero data retention commitment. The integration layer and governance model differ.

---

## Grok Models on Databricks: Quick Reference

**[grok-4.3](https://docs.x.ai/developers/models/grok-4.3)**
- Context: 1M tokens
- Reasoning: [Configurable](https://www.datastudios.org/post/grok-4-3-reasoning-effort-speed-depth-cost-and-output-reliability-settings-explained) (none/low/medium/high) — `low` is default
- Knowledge cutoff: [December 2025](https://x.com/techdevnotes/status/2045476046091301164)
- Strengths: Complex reasoning, analysis, long-document comprehension, multimodal inputs
- API ID: `grok-4.3` (in Unity AI Gateway)

**[grok-build-0.1](https://docs.x.ai/developers/models/grok-build-0.1)**
- Context: 256K tokens (not 1M — this is a separate, smaller-context model from grok-4.3)
- Trained on: xAI describes it as [trained specifically for agentic coding workflows](https://kingy.ai/ai-models/grok-build-0-1/); xAI has not published that it was trained on Cursor session data (that description applies to a different, unrelated xAI model, V9-Medium)
- Strengths: Code generation, debugging, technical documentation
- API ID: `grok-build-0.1` (in Unity AI Gateway)
- Also available: xAI's own API and [Grok Build platform](/builders-log/xai-grok-build-0-1-public-api-mcp-native-reasoning-builder-guide/)

---

## What This Means for the Databricks Ecosystem

The DAIS 2026 announcements across the board have been about completing the governed enterprise agent stack. Agent Bricks adds the orchestration layer. Unity AI Gateway adds the control plane. [Genie One](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) adds the business-user interface. The Grok addition fills in model variety: builders working inside Databricks now have a credible xAI option without stepping outside the governance boundary.

The practical upside is model choice without platform switching. If your team evaluates `grok-4.3` as better than `claude-sonnet-4-6` or `gpt-4.5` for a specific workload, you can make that swap inside Agent Bricks without changing your governance setup, your billing relationship, or your access control model.

That is the actual value of platform-native integrations at this layer. Not that another model exists, but that you can evaluate and swap without operational overhead.

---

*This article is based on the xAI and Databricks joint announcement from June 18, 2026 at the Databricks Data + AI Summit. ChatForest researches and covers AI tools for builders — we do not have hands-on access to test platforms directly. Specific pricing, API identifiers, and availability details may change; verify against [Databricks AI documentation](https://developers.databricks.com/docs/agents/ai-gateway) and [xAI docs](https://docs.x.ai/) before building.*
