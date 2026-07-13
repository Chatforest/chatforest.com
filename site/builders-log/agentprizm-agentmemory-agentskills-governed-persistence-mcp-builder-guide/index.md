# AgentPrizm Launched with Governed Agent Memory and a Reusable-Skills Marketplace — Here Is What Builders Need to Know

> AgentPrizm shipped July 9 with a production memory layer that adds confidence scoring, fact-validity windows, contradiction resolution, audit receipts, and GDPR alignment above standard retrieval — plus a versioned SKILL.md marketplace for reusable agent procedures. Free tier included.


**AgentPrizm** launched on July 9, 2026 with a two-product bundle targeting one of the most consistently underbuilt parts of production AI systems: memory that agents can actually trust.

The first product, **AgentMemory**, is a hosted REST + MCP service that adds confidence scoring, fact-validity windows, contradiction resolution, and auditable recall receipts on top of the vector retrieval you already get from a standard embedding store. The second, **AgentSkills**, is a versioned SKILL.md marketplace where agents can publish, discover, and reuse procedures across sessions and organizations.

Neither product is a research prototype. Both are live, with a free tier and a public pricing page.

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

Send raw conversation transcripts, tool results, CRM events, or structured documents. AgentPrizm extracts facts automatically — no manual taxonomy, no schema to maintain. The extraction layer identifies facts, lessons, preferences, and contacts from unstructured text and stores them as typed memory objects with validity timestamps.

There are six memory types: `fact`, `lesson`, `directive`, `preference`, `contact`, `bookmark`. The constrained taxonomy is intentional — AgentPrizm's design bet is that forcing memory into a small set of types makes contradiction detection and deduplication tractable at inference time.

### Recall

Query in natural language. The retrieval layer runs hybrid semantic + keyword search with reranking, then applies validity filtering (facts with `valid_to` in the past are excluded or flagged), confidence thresholding, and token budgeting so the returned context block fits a target window size.

The six primitives that run on every recall:

| Primitive | What it does |
|-----------|-------------|
| **Confidence weighting** (0–1) | Calibrates how strongly a memory influences the context block |
| **Fact-validity windows** | Tracks `valid_from` and optional `valid_to`; newer facts automatically supersede and stale-mark older ones |
| **Contradiction resolution** | When two facts conflict, the system records a supersede chain rather than silently overwriting |
| **Container scopes** | Per-user and per-org isolation; a memory in one container cannot bleed into another's recall |
| **Right-to-forget** | GDPR Article 17 compliance — delete a user's memory objects across the full store on request |
| **Audit receipts** | Every recall call returns a signed receipt listing which memories matched, their confidence scores, and why they ranked |

### Context

The output is a structured context block — the matched memories formatted and ranked, ready to prepend to your system prompt. The audit receipt ships alongside it as a separate object that your logging layer can store without polluting the prompt.

---

## AgentSkills: reusable procedures in a versioned marketplace

AgentSkills is bundled with AgentMemory. The format is SKILL.md — the same open standard used by Claude Code skills, Codex skills, and ChatGPT agent skills — which means skills are portable across any compatible MCP client.

The workflow:

1. An agent executes a procedure (a multi-step data enrichment, an escalation routing pattern, a code review checklist)
2. The developer packages it as a versioned `SKILL.md` file and publishes it to the AgentPrizm marketplace
3. Other agents can discover skills by intent (natural-language search, not exact-name lookup)
4. Consuming agents install a private read-only copy or fork and customize — with full lineage preserved

The public marketplace means skills cross organizational boundaries. A support team's escalation pattern can be discovered and adapted by a different org's support agent. The lineage chain records the fork relationship, so attribution is maintained.

This is similar in structure to what Block's open-source agent-skills repo initiated, but AgentPrizm pairs the marketplace with the memory layer so a skill's outputs can update the agent's memory store automatically.

---

## Integration paths: REST vs. MCP

AgentPrizm provides two access methods on the same backend with the same authentication:

**REST API** — Standard HTTP calls from any language. Full access to ingest, recall, and context endpoints. Better for systems where you control the full stack and want explicit logging of every call.

**MCP native** — Paste one config block into Claude Code, Cursor, Claude Desktop, or OpenClaw. Zero install. The MCP server exposes ingest and recall as named tools the model can call directly. Better for developer workflows where you want the agent to drive its own memory without wrapper code.

Both support the same feature set. There is no premium-only REST tier or MCP-only limitation.

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

| Tier | Price | Memories | Recalls/mo | Agents |
|------|-------|----------|-----------|--------|
| **Hobby** | Free | 10,000 | 4,500 | 2 |
| **Starter** | $16/mo | 100,000 | 15,000 | 5 |
| **Builder** | $66/mo | 400,000 | 65,000 | 25 |
| **Scale** | $208/mo | 1,000,000 | 225,000 | Unlimited |
| **Enterprise** | Custom | Custom | Custom | Unlimited |

Every feature — hybrid retrieval, confidence scoring, validity windows, audit receipts, right-to-forget — is available on the free tier. The tiers gate capacity, not capability.

---

## Hard limits to know before building

**No SOC 2 or HIPAA certification.** The platform cannot process protected health information. If your use case involves PHI, this is a blocker — not a tradeoff.

**No self-hosting.** AgentPrizm operates as a hosted service only. If your data governance requires on-premises deployment or VPC isolation, this does not fit.

**Hosted data residency TBD.** The published DPA and sub-processor list exist, but region-specific data residency controls are not listed on the public pricing page. Enterprise conversations would be required to clarify.

**Skills marketplace is public by default.** Published skills are discoverable by anyone on the platform. Private skills require the Starter tier or above, and AgentPrizm's pricing page lists "private skills" as an available feature — but the exact access controls are not detailed in the public documentation.

---

## Builder patterns to extract

**Pair AgentMemory with every agentic loop that reads user state.** Support agents, sales agents, and any agent that accumulates context over multiple sessions are the primary fit. The ROI case is: if your users re-explain the same context more than once per week, persistent memory pays for itself in reduced prompt length alone.

**Use audit receipts as observability infrastructure.** The recall receipt gives you a per-decision log of which memories influenced an agent response. Feed this into your existing observability stack (Langfuse, Honeycomb, custom logs) instead of building attribution tracking from scratch.

**Publish internal skills to the marketplace for reuse.** If your team has built a reliable procedure (a data enrichment pattern, a citation-formatting workflow, a test generation checklist), packaging it as a SKILL.md file and publishing it to the marketplace costs nothing on any tier. Other agents in your org can discover and use it without copy-pasting prompts.

**MCP config as the fastest evaluation path.** Before committing to the REST integration, paste the MCP config block into Claude Code or Cursor and run a session. The feature set is identical — you get the full evaluation in under five minutes.

**Know the validity-window pattern.** When you ingest a fact that supersedes an older one, the old fact is marked stale but not deleted. The supersede chain is preserved. This matters for compliance (you can show what the agent knew and when) and for debugging (you can trace why an agent used an outdated fact if validity filtering failed).

---

AgentPrizm is available at [agentprizm.com](https://agentprizm.com) with signup on the free tier today. The MCP config path is the fastest route to evaluation; the REST API documentation covers all six primitives and the full ingest and recall call signatures.

