# Google Managed Agents API Review — Full Agent Sandbox in One API Call

> Google launched the Managed Agents API in preview at Google I/O 2026. It provisions a full agent sandbox — ephemeral Linux environment, code execution, web browsing, MCP servers, and file access — with a single Gemini API call. We cover the architecture, AGENTS.md configuration, pricing model, ADK 2.0 context, and the real limitations before production deployment.


Google shipped **Managed Agents** in the Gemini API at Google I/O 2026 on May 19, 2026. The proposition is direct: one API call, and Google provisions a full agent — with an ephemeral Linux sandbox, live web access, Python execution, file system operations, and MCP server support — without the developer building any orchestration layer.

This is Google's answer to a specific and real problem in agent deployment. Building an agent that reasons, plans, executes code, browses the web, and calls external tools requires substantial infrastructure: sandboxing the execution environment, managing state across turns, provisioning tool access, handling scaling, and containing failures. Managed Agents abstracts all of that. You send a task description. Google handles everything underneath.

The catch, as always, is in what "preview" means in practice — and in this case, it means several important production questions remain open. This review covers the architecture, configuration model, pricing, where it fits against ADK 2.0, and the limitations to understand before building on it.

---

## What Managed Agents Actually Does

The API creates an **ephemeral, sandboxed execution environment** for each interaction. The environment is isolated per call, spun up on demand, and terminated automatically when execution completes.

Within that environment, every Managed Agent has access to the following out of the box:

- **Google Search** — live web access for real-time retrieval
- **Python code execution** — arbitrary code runs inside the sandbox
- **Filesystem operations** — read, write, edit, search, and list files
- **URL reader** — fetch and parse web page content
- **Bash terminal** — arbitrary shell commands within the sandbox
- **State persistence** — multi-turn interaction state is maintained within a session
- **MCP server support** — external MCP servers can be connected to the agent

The underlying model is **Gemini 3.5 Flash**. The agent is powered by the same Antigravity engine that runs Google's own agent desktop product — Managed Agents exposes that engine as a programmatic API.

The basic API call looks like:

```python
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="[task description]",
    environment="remote"
)
```

The call blocks until autonomous execution completes and returns results. The sandbox terminates afterward.

That is, deliberately, close to the simplest possible interface for a capable agent. The orchestration complexity — how the agent plans, how it sequences tool calls, how it handles failures — is handled by Google's infrastructure rather than by the caller.

---

## Three Configuration Levels

The API offers three levels of agent definition, from simplest to most controlled:

### 1. Inline Configuration

Pass system instructions and tool selections directly in the `create()` call. No files, no setup — the configuration is in the call. Appropriate for one-off tasks and exploration.

### 2. File-Based Configuration (AGENTS.md)

Define agent behavior in a versionable markdown file. The structure:
- **`AGENTS.md`** — behavioral instructions, persona, constraints, task framing
- **`workspace/`** — reference data the agent can read and operate on
- **`.agents/skills/`** — custom SKILL.md files defining reusable agent capabilities

The AGENTS.md pattern is the same configuration format used across Google's agent tooling. It is also the same format Claude Code uses for project instructions (CLAUDE.md). If you have existing AGENTS.md or CLAUDE.md files from other agent systems, the format is directly transferable.

Skills defined in SKILL.md are callable sub-behaviors: the agent can invoke a named skill during execution rather than rediscovering the same behavior each time. This matters for agent pipelines that need consistent, repeatable tool use patterns.

### 3. Named Registry

Register an agent configuration once and invoke it by name in subsequent calls. This is the production pattern: version your configuration, register it, and all calls to that name get the same defined behavior without re-specifying configuration on each call.

---

## ADK 2.0: The Alternative to Managed Agents

Google also shipped **Agent Development Kit (ADK) 2.0** at I/O 2026. Understanding the difference is important before choosing which to use.

**ADK 2.0** is a code-first framework for building custom agent systems with full architectural control. Key features:
- Unified graph-based engine supporting both dynamic, model-led reasoning and deterministic, scripted workflows
- Collaborative workflows with multiple subagent coordination modes: chat, task, and single-turn
- Language support: Python, Go, Java, and Kotlin (beta for Android and mobile-agent scenarios)

**When to use ADK 2.0 instead of Managed Agents:**
- You need custom orchestration logic or deterministic workflow paths
- Your agent must run on-premises or in your own cloud infrastructure
- You need specific dependency versions in the execution environment
- Your security or compliance requirements prohibit Google-hosted execution
- You are building a mobile agent that needs to coordinate with backend systems (Kotlin)

**When to use Managed Agents instead of ADK 2.0:**
- You want an agent that works immediately without infrastructure setup
- The task is exploratory, one-off, or low-volume
- You are prototyping before committing to a full ADK implementation
- You want MCP server connectivity without building a hosting layer

The two approaches are not mutually exclusive. Managed Agents is explicitly intended as an easier entry point; ADK 2.0 is the path for teams that have graduated past that constraint.

---

## Pricing: Free Now, Unknown Later

During the preview period, **compute is free**. CPU time, memory allocation, and sandbox execution do not add charges. Billing applies only to token usage and tool calls, at standard Gemini 3.5 Flash rates: **$1.50 per million input tokens, $9.00 per million output tokens**.

The critical cost consideration for agentic workloads: Managed Agents run through multiple autonomous reasoning loops. A single interaction can generate thousands of tokens internally as the agent plans, executes, checks results, and iterates. This is not unique to Managed Agents — it is true of any agentic system — but it is worth calibrating in testing before production deployment. A task that looks like a small request at the input level can consume substantial tokens across the full reasoning trace.

**Preview compute pricing is not yet announced.** When the Managed Agents API exits preview, Google will begin charging for sandbox compute. The compute pricing structure is not published. This is the most significant unanswered production question for teams evaluating the API today.

---

## Limitations

### Google-Hosted Only

The execution environment is Google infrastructure. There is no option to run Managed Agents on-premises or in a private cloud. For organizations with data residency requirements, regulated workloads requiring air-gapped environments, or security policies that prohibit third-party code execution of sensitive data, Managed Agents is not a viable option in its current form.

### No Dependency Version Control

The sandbox environment is managed by Google. Developers cannot pin specific library versions or install arbitrary dependencies. The execution environment is consistent and maintained, but it is not customizable at the dependency level. Workloads with strict version requirements for Python packages or system libraries need ADK 2.0 with self-hosted infrastructure instead.

### Token Cost Requires Testing

The free compute preview can mask the real operational cost of an agentic workload. Multi-step agent loops that look inexpensive at the surface — a single input prompt — can generate substantial token usage in the agent's internal reasoning trace. Testing under realistic workload conditions before production deployment is necessary to build accurate cost models.

### Preview Stability

The API is in preview. Production stability, SLA commitments, and the compute pricing structure when it exits preview are not yet published. Teams requiring production-grade SLAs should not build mission-critical pipelines on preview infrastructure.

### A2A Integration: Forthcoming

Full integration with the Agent-to-Agent (A2A) protocol and the enterprise Agent Platform governance features is listed as forthcoming. This means multi-agent systems that need A2A coordination between Managed Agents and other agent systems (including third-party agents) are not fully supported at launch.

---

## Enterprise Track

For enterprise deployments, Google has a separate offering: **Gemini Enterprise Agent Platform**, which includes Managed Agents support in **private preview**. The enterprise track adds:
- Agent Platform governance and security controls
- Integration with Google Cloud enterprise infrastructure
- Support for enterprise compliance requirements

Private preview means this is not generally available. Enterprise teams interested in Managed Agents at scale should contact Google Cloud for access.

---

## Who Should Use This

**Good fit:**
- Developers prototyping agentic workflows who want immediate capability without infrastructure setup
- Teams exploring MCP-connected agents without building a hosting layer for MCP servers
- Organizations already running on Google Cloud who want to extend existing systems with agent capabilities
- High-throughput use cases where Google's infrastructure management reduces operational overhead — once compute pricing is known

**Wait or consider alternatives:**
- Workloads with data residency, compliance, or on-premises requirements — use ADK 2.0 with self-hosted infrastructure
- Production systems requiring stable SLAs before preview exits — the compute pricing is not yet defined
- Multi-agent workflows requiring A2A coordination — the full A2A integration is not yet available
- Workloads with specific dependency requirements — the managed environment does not support dependency pinning
- Teams who need to understand total cost before committing — test thoroughly against realistic workloads before the free compute preview ends

---

## Summary

Managed Agents is a genuine developer convenience. The single-API-call model for a full agent sandbox — with web access, code execution, file operations, and MCP support — removes real friction from agent prototyping and deployment. The AGENTS.md configuration format is portable and version-controllable. The connection to Gemini 3.5 Flash's agentic benchmark leadership means the underlying model is appropriate for the workloads the API targets.

The preview-period constraints are the primary hold. Compute pricing after preview is unknown, A2A integration is forthcoming, enterprise governance is in private preview, and the Google-hosted constraint is a firm limitation for certain workloads. These are solvable problems — Google has clear incentive to address them — but they are real questions for teams evaluating production use today.

For exploration, prototyping, and workloads that fit the Google-hosted constraint, Managed Agents is worth building on now. For production commitments at scale, wait for the compute pricing announcement and the A2A integration before finalizing architectural decisions.

**Rating: 3/5** — Compelling one-API-call agent sandbox with native MCP support and solid model foundation. Preview status, unknown post-preview compute pricing, and the Google-hosted-only constraint limit the production verdict. Reassess when compute pricing is announced and A2A integration ships.

