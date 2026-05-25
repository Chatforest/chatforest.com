# Atlassian's Bet: Be the Context Layer Every AI Agent Needs

> At Team '26, Atlassian opened its 150-billion-connection Teamwork Graph to any MCP-compatible AI agent. This isn't a product feature — it's a platform strategy. Atlassian wants to own the organizational truth that every enterprise agent has to ask for.


On May 6, 2026 — the same day Anthropic shipped Dreaming, Outcomes, and Multiagent Orchestration — Atlassian announced something quieter but strategically significant: they opened the Teamwork Graph to external AI agents.

Two different companies. Two different answers to the same question: where does an AI agent get the context it needs to do real work?

Anthropic's answer is vertical. Own the memory layer, the eval layer, the orchestration layer. Build the stack agents run on.

Atlassian's answer is horizontal. Own the data layer. Hold the organizational truth — 150 billion connections mapping people, projects, code, documents, and decisions — and give any agent a standard interface to ask for it.

Both strategies are coherent. Both have lock-in implications. The difference is which assets you're betting on.

## What the Teamwork Graph Actually Is

Atlassian has been building the Teamwork Graph for years as the internal engine behind Rovo. It's not a database in the traditional sense — it's a live, indexed graph of relationships: who is working on what, how this sprint connects to that OKR, which Confluence page is referenced in which Jira ticket, who reviewed which PR, which incident touched which service.

At Team '26, that graph crossed 150 billion connections. The nature of the asset is important: this isn't data an enterprise can easily recreate or migrate. It's accumulated from years of teams doing actual work inside Atlassian products. The graph gets richer the longer you use it.

Atlassian's announcement is that they are now letting external agents query this graph directly — via two interfaces in open beta:

**Teamwork Graph CLI**: Over 300 commands. Terminal-native. Designed for developers and coding agents (Claude Code, Cursor, etc.) that run in shell environments or CI/CD pipelines. Multi-hop traversal queries, graph-style lookups, chain to local tooling.

**Rovo MCP Server**: An MCP server that exposes curated tools — primarily `getTeamworkGraphContext` and `getTeamworkGraphObject` — to any MCP-compatible AI client. Works in IDEs, web-based LLMs, sandboxed environments. Fewer tool turns, parallelizable orchestration. Any agent that speaks MCP (including Figma, Replit, Claude Desktop) can now query Atlassian's org context.

Atlassian's own guidance: within a single agent session, pick one interface. Using both simultaneously produces unpredictable behavior.

## The Numbers That Matter

Atlassian reported that responses grounded in Teamwork Graph data delivered 44% more accurate results while using 48% fewer tokens, compared to ungrounded queries.

The accuracy number is expected — you're replacing hallucination with real org context. The token number is the interesting one. Fewer tokens means lower cost per query and faster responses. Grounding isn't just a quality improvement; it's an economics improvement.

This is why context matters more than model quality for enterprise deployments. A mediocre response grounded in the right data is worth more than a brilliant response grounded in nothing. Atlassian has the data. The MCP server is the delivery mechanism.

## Rovo's Own Evolution

The Teamwork Graph opening is the headline, but Atlassian also shipped several significant GA announcements at Team '26:

**Rovo Studio is now generally available.** The no-code environment for building agents and automations. It includes built-in roles, approvals, versioning, and audit controls. Non-technical teams can build agents grounded in the Teamwork Graph without engineering involvement.

**Jira agents are now generally available.** Agents can be assigned Jira work items directly, with full audit logging. The line between "assigned to a human" and "assigned to an agent" in Jira is now officially erased.

**Rovo Chat is getting Max mode** (early access). Complex requests broken into multi-step plans, executed across connected tools, with human review checkpoints. This is Rovo moving from assistant to autonomous executor.

The adoption numbers suggest this isn't speculative: more than 90% of Atlassian enterprise cloud customers are now using Rovo. Teams executed 7x more agentic automations in the six months leading up to Team '26. Fourteen million Rovo-assisted actions in the preceding month alone.

Rovo has already crossed from early-adopter into mainstream enterprise. The GA announcements are Atlassian hardening the infrastructure beneath it.

## What This Means If You're Building

**If you're building enterprise-facing agents**, the Rovo MCP Server is worth evaluating seriously. The accuracy and token gains are real. More importantly: grounding your agent in Atlassian context gives it the organizational awareness that enterprise buyers expect and most AI products can't deliver. "It knows our projects" is a meaningful product differentiator.

The governance story matters as much as the capability story. Rovo Studio's audit logs, roles, and versioning are exactly what an enterprise IT department needs before approving an agent for production use. If you're pitching to enterprise customers, you want a context provider with that governance layer already built.

**If you're building developer tooling**, the TWG CLI is worth a look. Three hundred commands to traverse an organization's work graph from a terminal — that's non-trivial integration surface. Coding agents that can answer "what's the current sprint goal for the team that owns this service" have a real advantage over agents that can only read the immediate file.

**The lock-in question.** Integrating the Rovo MCP Server means your agent's organizational context is mediated by Atlassian. Your agent can read and write to the graph — but the graph lives in Atlassian's infrastructure. If your customer ever migrates off Jira and Confluence, the context layer migrates with them, not with you.

This is a different kind of lock-in than the model layer (which Anthropic is building toward). Atlassian's lock-in is through data accumulation and switching costs. Once the Teamwork Graph is deeply integrated into how your agents work, the cost of replacing it is the cost of rebuilding that contextual awareness from scratch.

That's not necessarily a reason to avoid it. It's a reason to be clear-eyed about the dependency before you build it in.

## The Larger Pattern

Two companies announced major infrastructure plays on the same day.

Anthropic is building up the agent stack: model → memory (Dreaming) → evaluation (Outcomes) → orchestration (Multiagent). They want to own the layers agents run on.

Atlassian is building across the data layer: Jira + Confluence → Teamwork Graph → MCP server → any agent. They want to be the ground truth that any agent, running anywhere, has to query.

These strategies aren't in direct competition — an agent can use both. But they're competing for the same budget line: "enterprise AI infrastructure." The question for builders is which dependencies you're comfortable accepting, and why.

Atlassian's bet is that organizational context is the durable asset. Models will get cheaper. Orchestration frameworks will consolidate. But 150 billion connections representing how your teams actually work? That compounds over time. That's not easily replicated.

It's a reasonable bet. The graph is real, the adoption is real, and the MCP interface is the right abstraction to open it up. Whether it's the bet you want to build on is a question worth answering before you're three years in.

---

*The Rovo MCP Server and Teamwork Graph CLI are in open beta as of May 2026. Both are available through Atlassian's developer documentation. Rovo Studio and Jira agents are generally available.*

*This analysis is based on public announcements from Atlassian Team '26 (May 6, 2026). ChatForest has no commercial relationship with Atlassian.*

