---
title: "AgentPrizm Launched with Governed Agent Memory and a Reusable-Skills Marketplace — Here Is What Builders Need to Know"
description: "AgentPrizm shipped July 9 with a production memory layer that adds confidence scoring, fact-validity windows, contradiction resolution, audit receipts, and GDPR alignment above standard retrieval — plus a versioned SKILL.md marketplace for reusable agent procedures. Free tier included."
date: 2026-07-11
lastmod: 2026-07-11
categories: ["builders-log"]
tags: ["agent-memory", "mcp", "production-agents", "skills-marketplace", "governance", "persistence", "agentprizm"]
sources_audited: 2026-08-05
---

**AgentPrizm** launched on [July 9, 2026](https://www.digitaljournal.com/pr/news/access-newswire/agentprizm-launches-governed-ai-agent-1203883901.html) with a two-product bundle targeting one of the most consistently underbuilt parts of production AI systems: memory that agents can actually trust. AgentPrizm is built by VUGA Enterprises; the launch was announced via a company [press release](https://finance.yahoo.com/technology/ai/articles/agentprizm-launches-governed-ai-agent-154500272.html) distributed the same day.

The first product, **[AgentMemory](https://agentprizm.com/)**, is a hosted REST + MCP service that adds confidence scoring, fact-validity windows, contradiction resolution, and auditable recall receipts on top of the vector retrieval you already get from a standard embedding store. The second, **[AgentSkills](https://agentprizm.com/skills)**, is a versioned SKILL.md marketplace where agents can publish, discover, and reuse procedures across sessions and organizations.

Neither product is a research prototype. Both are live, with a [free tier and a public pricing page](https://agentprizm.com/pricing).

---

## The actual problem AgentPrizm is solving

Every stateless agent session starts with the same blank slate. In toy demos this is fine. In production it creates three compounding failure modes:

**Repeated context burden.** Users re-explain preferences, prior decisions, and project state at the start of every conversation. Agents that surface policies or customer records have to be re-briefed through prompt engineering or long retrieval chains on every turn.

**Stale fact syndrome.** A customer changes their subscription tier. A codebase shifts to a new framework. A regulation updates. The agent's embedded memory doesn't know. It confidently uses the old fact.

**No accountability trail.** When an agent makes a decision influenced by a remembered fact, there is no record of which memory matched, how confident the system was in it, or when that fact was ingested. Debugging is archaeology.

These are not edge cases. They are the modal failure mode for any agent that needs to remember things across sessions — support agents, sales agents, coding agents, legal research agents.

---

## What AgentPrizm shipped

The memory pipeline has three stages:

### Ingest

Send raw conversation transcripts, tool results, CRM events, or structured documents. AgentPrizm's own [product marketing](https://agentprizm.com/) puts it as: "Send a transcript, tool result, CRM event, ticket, or doc. AgentPrizm extracts facts, lessons, and preferences automatically" — "0 Lines of taxonomy you maintain. We extract, dedupe, and file." The extraction layer identifies facts, lessons, preferences, and contacts from unstructured text and stores them as typed memory objects with validity timestamps.

There are six memory types: `fact`, `lesson`, `directive`, `preference`, `contact`, `bookmark`, [as AgentPrizm defines them](https://agentprizm.com/blog/six-memory-types-ai-agents). The constrained taxonomy is intentional — AgentPrizm's design bet is that forcing memory into a small set of types makes contradiction detection and deduplication tractable at inference time.

### Recall

Query in natural language. Per the [API reference](https://agentprizm.com/api-reference), the retrieval layer runs hybrid semantic + keyword search (`searchMode: hybrid` by default) with optional reranking, then applies validity filtering (facts outside the `valid_from`/`valid_to` window are excluded or flagged), confidence thresholding (`minConfidence`), and reports token counts in the response metadata so the returned context block can be sized to a target window.

The six primitives that run on every recall, per AgentPrizm's [docs](https://agentprizm.com/api-reference) and [security page](https://agentprizm.com/security):

| Primitive | What it does |
|-----------|-------------|
| **Confidence weighting** (0–1) | Calibrates how strongly a memory influences the context block |
| **Fact-validity windows** | Tracks `valid_from` and optional `valid_to`; newer facts automatically supersede and stale-mark older ones |
| **Contradiction resolution** | When two facts conflict, the system records a supersede chain rather than silently overwriting |
| **Container scopes** | Per-user and per-org isolation; a memory in one container cannot bleed into another's recall |
| **Right-to-forget** | AgentPrizm's [DPA](https://agentprizm.com/dpa) commits to self-service deletion via a `POST /api/v1/agent/forget` endpoint to help customers fulfill data-subject deletion requests (the substantive right this maps to is [GDPR Article 17](https://gdpr-info.eu/art-17-gdpr/), though AgentPrizm's own materials frame it as general data-subject-rights support rather than citing Article 17 by name) |
| **Audit receipts** | Every recall call returns a receipt listing which memories matched, their confidence scores, and why they ranked — this is an audit-trail record, not a cryptographically signed one; AgentPrizm's published [API schema](https://agentprizm.com/api-reference) has no signature field |

### Context

The output is a structured context block — the matched memories formatted and ranked, ready to prepend to your system prompt. The audit receipt ships alongside it as a separate object that your logging layer can store without polluting the prompt.

---

## AgentSkills: reusable procedures in a versioned marketplace

AgentSkills is bundled with AgentMemory. The format is SKILL.md — the same [open standard](https://agentskills.io/) originally developed by Anthropic and adopted, per the standard's own client list, by Claude Code, Codex, ChatGPT, Cursor, and dozens of other agent tools — which means skills are portable across any compatible MCP client.

The workflow, per AgentPrizm's [skills marketplace](https://agentprizm.com/skills) and [product pages](https://agentprizm.com/):

1. An agent executes a procedure (a multi-step data enrichment, an escalation routing pattern, a code review checklist)
2. The developer packages it as a versioned `SKILL.md` file and publishes it to the AgentPrizm marketplace, where secrets and PII are "scanned and blocked before anything ships"
3. Other agents can discover skills by intent — AgentPrizm advertises semantic search for queries like "fill a PDF form" or "reconcile a Stripe payout," scoped to your containers
4. Consuming agents install a private copy or fork and customize; per AgentPrizm, "install makes a private copy; forking stays public and credits its source," with "git-style lineage, moderation, and takedown built in"

The public marketplace means skills cross organizational boundaries. A support team's escalation pattern can be discovered and adapted by a different org's support agent. The lineage chain records the fork relationship, so attribution is maintained.

This is similar in structure to what [Block's open-source agent-skills repo](https://github.com/block/agent-skills) initiated, but AgentPrizm pairs the marketplace with the memory layer so a skill's outputs can update the agent's memory store automatically.

---

## Integration paths: REST vs. MCP

AgentPrizm provides two access methods on the same backend with the same authentication:

**REST API** — Standard HTTP calls from any language. Full access to ingest, recall, and context endpoints. Better for systems where you control the full stack and want explicit logging of every call.

**MCP native** — Paste one config block into Claude Code, Cursor, Claude Desktop, or OpenClaw. Zero install. AgentPrizm's own site lists it as [working with](https://agentprizm.com/) "Claude Code, Cursor, Claude Desktop, OpenClaw, and any MCP-capable agent." The MCP server exposes ingest and recall as named tools the model can call directly. Better for developer workflows where you want the agent to drive its own memory without wrapper code.

Both support the same feature set. Per AgentPrizm's [pricing page](https://agentprizm.com/pricing), every tier including the free one gets API and MCP access — there is no premium-only REST tier or MCP-only limitation.

---

## AgentPrizm vs. a DIY vector store

The comparison that keeps coming up in the MCP community is: why not just use Pinecone or Qdrant directly? The answer depends on what problem you are actually solving.

A vector database does **retrieval**: stores embeddings, returns nearest neighbors by cosine similarity. That is it. Everything else — extracting facts from raw transcripts, deduplicating overlapping memories, tracking when a fact expires, generating audit trails, enforcing right-to-forget — you build yourself.

AgentPrizm's bet is that this extraction-and-governance layer is where most teams give up and ship something that quietly hallucinates stale facts. The platform absorbs:

- Embedding and chunking strategy
- Deduplication and contradiction detection logic
- Validity tracking and expiration
- Confidence calibration
- Audit log format and storage
- GDPR deletion workflows

If you have the infrastructure team to build and maintain all of that, a raw vector store is cheaper and more controllable. If you do not, AgentPrizm trades cost for velocity.

---

## Pricing

Per [AgentPrizm's pricing page](https://agentprizm.com/pricing) (checked 2026-08-05 — the launch-week price points were lower, $16/$66/$208/mo for Starter/Builder/Scale; AgentPrizm has since raised prices, so confirm current rates before building a budget around this table):

| Tier | Price | Memories | Recalls/mo | Agents |
|------|-------|----------|-----------|--------|
| **Hobby** | Free | 10,000 | 4,500 | 2 |
| **Starter** | $19/mo | 100,000 | 15,000 + $1.10/1k overage | 5 |
| **Builder** | $79/mo | 400,000 | 65,000 + $1.10/1k overage | 25 |
| **Scale** | $249/mo + usage | 1,000,000 | 225,000 + $1.10/1k overage | Unlimited |
| **Enterprise** | Custom | Custom | Custom | Unlimited |

Every recall feature — hybrid retrieval, confidence scoring, validity windows, audit receipts, right-to-forget — is available on the free tier, per AgentPrizm's own [feature copy](https://agentprizm.com/): "every recall feature on every plan — including the free tier." The tiers gate capacity, not capability.

---

## Hard limits to know before building

**No SOC 2 or HIPAA certification.** AgentPrizm's [security page](https://agentprizm.com/security) states plainly: "We don't currently hold SOC 2, HIPAA BAA, ISO 27001, or FedRAMP certifications, and we don't claim to," and warns customers not to submit PHI because "AgentPrizm is not HIPAA-compliant." The [pricing page](https://agentprizm.com/pricing) lists SOC 2 Type II as "on our roadmap, not yet certified." If your use case involves PHI, this is a blocker — not a tradeoff.

**No self-hosting today, but a source-available release is planned.** AgentPrizm operates as a hosted service only as of this writing — the security page describes hosted infrastructure only, with no on-premises or VPC-isolation option. However, the company's own [launch announcement](https://finance.yahoo.com/technology/ai/articles/agentprizm-launches-governed-ai-agent-154500272.html) says it "plans to release a source-available version of its memory engine later this summer" (2026); that release had not shipped as of this audit.

**Hosted data residency mostly Enterprise-only.** AgentPrizm publishes a [DPA](https://agentprizm.com/dpa) and [sub-processor list](https://agentprizm.com/subprocessors), but the [pricing page](https://agentprizm.com/pricing) lists "custom DPAs, residency, retention" as an Enterprise-tier feature — region-specific data residency controls are not available on the Hobby/Starter/Builder/Scale tiers. Enterprise conversations would be required to get residency guarantees.

**Skills marketplace is public by default, but private skills are not gated behind a paid tier.** Published skills are discoverable by anyone on the platform. Private skills, however, are available from the free tier: per the [pricing page](https://agentprizm.com/pricing), the free Hobby tier includes "10 private + 10 public skills," and every paid tier (Starter and above) includes "unlimited public + private skills." The exact access controls beyond the numeric caps are not detailed in the public documentation.

---

## Builder patterns to extract

**Pair AgentMemory with every agentic loop that reads user state.** Support agents, sales agents, and any agent that accumulates context over multiple sessions are the primary fit. The ROI case is: if your users re-explain the same context more than once per week, persistent memory pays for itself in reduced prompt length alone.

**Use audit receipts as observability infrastructure.** The recall receipt gives you a per-decision log of which memories influenced an agent response. Feed this into your existing observability stack (Langfuse, Honeycomb, custom logs) instead of building attribution tracking from scratch.

**Publish internal skills to the marketplace for reuse.** If your team has built a reliable procedure (a data enrichment pattern, a citation-formatting workflow, a test generation checklist), packaging it as a SKILL.md file and publishing it to the marketplace costs nothing on any tier. Other agents in your org can discover and use it without copy-pasting prompts.

**MCP config as the fastest evaluation path.** Before committing to the REST integration, paste the MCP config block into Claude Code or Cursor and run a session. The feature set is identical — you get the full evaluation in under five minutes.

**Know the validity-window pattern.** When you ingest a fact that supersedes an older one, the old fact is marked stale but not deleted. The supersede chain is preserved. This matters for compliance (you can show what the agent knew and when) and for debugging (you can trace why an agent used an outdated fact if validity filtering failed).

---

AgentPrizm is available at [agentprizm.com](https://agentprizm.com) with signup on the free tier today. The MCP config path is the fastest route to evaluation; the [REST API documentation](https://agentprizm.com/api-reference) covers all six primitives and the full ingest and recall call signatures.
