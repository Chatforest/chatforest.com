# Grok on Databricks Agent Bricks: xAI's First Lakehouse-Native Agent Integration

> xAI's Grok 4.3 and grok-build-0.1 are now available natively in Databricks Agent Bricks, announced at DAIS 2026 on June 18. Grok connects directly to Lakehouse data via Genie Ontology — no exfiltration, Unity Catalog governance. Here's the builder guide.


**At a glance:** On June 18, 2026, at the Databricks Data + AI Summit, xAI announced that Grok is available natively in Databricks Agent Bricks. Two models: `grok-4.3` and `grok-build-0.1`. Both connect directly to your Lakehouse via Genie Ontology — agents reason over governed data without moving it. Unity Catalog handles all access control. Zero data retention on xAI's side. Select either model from the AI Playground UI or configure programmatically.

---

## What Was Announced

The June 18 announcement is not a generic marketplace listing. This is a native integration: Grok becomes a first-class model choice inside Databricks Agent Bricks, with direct access to Lakehouse-hosted data through the same governance layer that controls your tables, volumes, and lineage metadata.

Two models are available at launch:

| Model | Best for | Input | Output |
|---|---|---|---|
| `grok-4.3` | Reasoning, analysis, multimodal | $1.25/M | $2.50/M |
| `grok-build-0.1` | Code generation, technical tasks | $1.00/M | $2.00/M |

Both run with a 1M token context window. `grok-4.3` carries Grok's configurable reasoning modes (none/low/medium/high); `grok-build-0.1` is optimized for developer workflows and was trained on real coding session data.

---

## The Core Differentiator: Genie Ontology

The part that makes this integration interesting for builders is not that Grok is available on another platform. The part that matters is how Grok connects to data.

**Standard integrations** work like this: your agent calls a tool, the tool queries your database, returns results, and the model reasons over the returned text. Your data leaves its governed environment at the query boundary.

**The Databricks integration** works differently. Genie Ontology gives Grok semantic access to your Lakehouse: not just the rows in your tables, but the business context encoded in Unity Catalog — schema definitions, lineage metadata, column-level access policies, data quality signals, and business glossary terms. The model understands *what your data means*, not just what it says.

Practically, this means:

- An agent selecting `grok-4.3` in Agent Bricks can reason over your Delta tables without the data being transmitted to xAI
- The ontology layer translates natural-language queries into governed Lakehouse operations
- All reasoning traces, memory, and outputs are stored back in your Lakehouse under Unity Catalog governance
- Column-level permissions in Unity Catalog flow through to what the agent can actually see — a user with no access to `salary` columns cannot get that data through the agent either

This is the same "governance comes for free" thesis that Agent Bricks is built on, extended to xAI's model family.

---

## Data Privacy

xAI has committed to zero data retention for this integration: data submitted through the Databricks path is not retained by xAI and is not used for model training. Unity Catalog handles all access control at the Databricks boundary.

For regulated industries, this matters. The data never leaves your Databricks security perimeter in a form that xAI controls. Governance is enforced before the model ever sees the data.

---

## How to Use It

### Option 1: AI Playground (low-code)

The simplest path:

1. Open Databricks AI Playground (`AI & Machine Learning → AI Playground`)
2. In the model dropdown, select `grok-4.3` or `grok-build-0.1`
3. Add tools using the low-code UI — connect to Lakehouse tables, Unity Catalog volumes, or Genie Spaces
4. Test the agent interactively
5. Export to code when ready for production deployment

### Option 2: Agent Bricks SDK (code-first)

For production deployments, Agent Bricks supports LangGraph, the OpenAI Agents SDK, and LlamaIndex. Grok slots in as a model choice within any of these:

```python
from databricks.sdk import WorkspaceClient
from langchain_databricks import ChatDatabricks

# Point LangChain at Grok via Unity AI Gateway
llm = ChatDatabricks(
    endpoint="grok-4-3",  # or "grok-build-0-1"
    max_tokens=4096,
)
```

The Unity AI Gateway handles routing to xAI, rate limiting, cost attribution, and audit logging — the same gateway layer that governs other models in your Databricks environment. You do not need a separate xAI account for this path; billing flows through Databricks.

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

**grok-4.3**
- Context: 1M tokens, 30K max output
- Reasoning: Configurable (none/low/medium/high) — `low` is default
- Knowledge cutoff: December 2025
- Strengths: Complex reasoning, analysis, long-document comprehension, multimodal inputs
- API ID: `grok-4.3` (in Unity AI Gateway)

**grok-build-0.1**
- Context: 1M tokens
- Trained on: Real developer coding sessions (Cursor workflow data)
- Strengths: Code generation, debugging, technical documentation
- API ID: `grok-build-0.1` (in Unity AI Gateway)
- Also available: xAI's own API and [Grok Build platform](/builders-log/xai-grok-build-0-1-public-api-mcp-native-reasoning-builder-guide/)

---

## What This Means for the Databricks Ecosystem

The DAIS 2026 announcements across the board have been about completing the governed enterprise agent stack. Agent Bricks adds the orchestration layer. Unity AI Gateway adds the control plane. Genie One adds the business-user interface. The Grok addition fills in model variety: builders working inside Databricks now have a credible xAI option without stepping outside the governance boundary.

The practical upside is model choice without platform switching. If your team evaluates `grok-4.3` as better than `claude-sonnet-4-6` or `gpt-4.5` for a specific workload, you can make that swap inside Agent Bricks without changing your governance setup, your billing relationship, or your access control model.

That is the actual value of platform-native integrations at this layer. Not that another model exists, but that you can evaluate and swap without operational overhead.

---

*This article is based on the xAI and Databricks joint announcement from June 18, 2026 at the Databricks Data + AI Summit. ChatForest researches and covers AI tools for builders — we do not have hands-on access to test platforms directly. Specific pricing, API identifiers, and availability details may change; verify against [Databricks AI documentation](https://developers.databricks.com/docs/agents/ai-gateway) and [xAI docs](https://docs.x.ai/) before building.*

