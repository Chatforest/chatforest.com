---
title: "MCP AI Safety: Guardrails, Content Filtering, Sandboxing, and Responsible AI Patterns"
date: 2026-03-28T21:00:00+09:00
description: "A comprehensive guide to implementing AI safety with MCP — covering guardrail frameworks (Guardrails AI, NeMo Guardrails, OpenGuardrails), content filtering (Presidio, Skyflow"
content_type: "Guide"
card_description: "MCP gives AI agents real-world capabilities — database access, file operations, API calls, code execution. This guide covers the safety patterns you need: guardrail frameworks, content filtering, sandboxing, human-in-the-loop approvals, permission systems, audit logging, and lessons from real-world incidents."
last_refreshed: 2026-03-28
sources_audited: 2026-08-11
---

MCP gives AI agents the ability to read files, query databases, execute code, send messages, and modify infrastructure. Every tool an MCP server exposes is a capability that can be used correctly — or catastrophically. In early 2026, security researchers [documented 30+ CVEs filed against MCP servers in a single 60-day window](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/). A single vulnerability in `mcp-remote` ([CVE-2025-6514](https://jfrog.com/blog/2025-6514-critical-mcp-remote-rce-vulnerability/), CVSS 9.6) affected over 437,000 downloads with a remote code execution flaw. [Asana's MCP server leaked customer data across organization boundaries](https://www.bleepingcomputer.com/news/security/asana-warns-mcp-ai-feature-exposed-customer-data-to-other-orgs/) in a real production incident, and security researchers at Invariant Labs built proof-of-concept attacks demonstrating how [a poisoned GitHub issue could leak private repository data](https://invariantlabs.ai/blog/mcp-github-vulnerability) and [a malicious MCP tool could exfiltrate WhatsApp message history](https://invariantlabs.ai/blog/whatsapp-mcp-exploited) — all through MCP tool manipulation.

The safety challenge with MCP is unique. Traditional API security assumes the caller understands the API contract. MCP callers are language models that can be manipulated through prompt injection, confused by ambiguous tool descriptions, or tricked into calling tools with malicious parameters. Defending MCP systems requires a layered approach: protocol-level safety features, guardrail frameworks, content filtering, sandbox isolation, fine-grained permissions, human-in-the-loop approvals, audit logging, and cost controls.

This guide covers the patterns, tools, and frameworks for building safe MCP systems. Our analysis draws on published documentation, security research, CVE databases, and vendor materials — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## The MCP Safety Landscape

Before diving into tools and patterns, it helps to understand the threat model. The [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/) (released December 10, 2025), the [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (a draft standard, MCP01:2025–MCP10:2025, still in beta/pilot testing as of mid-2026), [CoSAI's "Securing the AI Agent Revolution" MCP security whitepaper](https://www.coalitionforsecureai.org/securing-the-ai-agent-revolution-a-practical-guide-to-mcp-security/) (released January 27, 2026, ~40 threats across 12 categories), and [Adversa AI's MCP Security TOP 25](https://adversa.ai/mcp-security-top-25-mcp-vulnerabilities/) (launched September 18, 2025) collectively paint a picture of the attack surface.

**Key threat categories:**

| Threat | Description | Real Example |
|--------|-------------|-------------|
| **Tool poisoning** | Malicious tool descriptions manipulate agent behavior | GitHub MCP demo: hidden instructions in issue text leaked private repo data via a public PR |
| **Prompt injection via tools** | External data returned by tools contains injected instructions | Supabase/Cursor demo: support ticket text triggered data exfiltration |
| **Rug pull** | Tool descriptions change after initial trust is established | Tools behave safely during review, then change behavior post-approval |
| **Cross-tenant leakage** | MCP server shares state between users | [Asana MCP leaked data across ~1,000 customer accounts](https://www.bleepingcomputer.com/news/security/asana-warns-mcp-ai-feature-exposed-customer-data-to-other-orgs/) |
| **Token amplification** | Adversarial tools consume excessive tokens | [Research showed 142.4x token amplification via "overthinking loops"](https://arxiv.org/abs/2602.14798) |
| **Credential theft** | MCP servers receive OAuth tokens that can be misused | Stolen tokens used for lateral movement across connected services |
| **Shadow tool execution** | Hidden tool calls embedded in responses | Tool annotations misused to execute actions users didn't approve |

The core insight from these frameworks: **MCP safety is not just API security with a new name.** The presence of a language model in the loop creates attack vectors that don't exist in traditional service-to-service communication.

## Protocol-Level Safety Features

The [MCP specification](https://modelcontextprotocol.io/specification/2025-06-18) (2025-03-26 and 2025-06-18 revisions; a newer [2025-11-25 revision](https://modelcontextprotocol.info/specification/2025-11-25/changelog/) has since shipped, adding OpenID Connect Discovery, incremental OAuth scope consent, and tool-calling in sampling, among other changes not covered in depth here) includes four built-in safety mechanisms discussed below. These form the foundation that external tools build upon.

### Tool Annotations

MCP tool annotations provide metadata hints about what a tool does:

```json
{
  "name": "delete_user",
  "annotations": {
    "readOnlyHint": false,
    "destructiveHint": true,
    "idempotentHint": false,
    "openWorldHint": true
  }
}
```

**Critical caveat:** The [spec explicitly states these annotations are **untrusted hints**](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool-annotations). Clients SHOULD NOT make security decisions based solely on annotations because a malicious server can lie about them. They're useful for UI presentation (showing a warning icon for destructive tools) but not for enforcement. A [Tool Annotations Interest Group](https://modelcontextprotocol.io/community/interest-groups/tool-annotations) was proposed in a [March 16, 2026 MCP blog post](https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/) and formally chartered April 20, 2026, to potentially strengthen these guarantees.

**What annotations provide today:**
- `readOnlyHint` — suggests the tool doesn't modify state (display only, no confirmation needed)
- `destructiveHint` — suggests the tool may cause irreversible damage (prompt for confirmation)
- `idempotentHint` — suggests calling the tool multiple times has the same effect
- `openWorldHint` — suggests the tool interacts with external entities beyond its server

### Sampling: Two-Checkpoint Human Approval

[MCP sampling](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling) allows a server to request an LLM completion from the client, but with a crucial safety feature: the spec requires clients to implement **two checkpoints** where a human can intervene:

1. **Before sending** — the human reviews the prompt the server wants to send to the LLM
2. **After receiving** — the human reviews the LLM response before it goes back to the server

This prevents MCP servers from using the client's LLM access for unauthorized purposes. A data-analysis MCP server requesting a sampling call to "summarize this financial data" can be reviewed by the user before the LLM processes potentially sensitive information.

### Elicitation: Structured User Input

Added in the [2025-06-18 revision](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), elicitation lets MCP servers request structured input from users during operations. Servers can define JSON schemas for the input they need, and the client presents an appropriate form. This enables consent flows, parameter confirmation, and explicit user choices mid-operation.

### OAuth 2.1 with Resource Indicators

MCP mandates OAuth 2.1 with PKCE and [requires Resource Indicators for OAuth 2.0 (RFC 8707)](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) for scoping tokens to specific MCP servers. This means a token issued for a filesystem MCP server cannot be replayed against a database MCP server — the audience is bound into the token. (Corrected 2026-08-11: an earlier version of this guide cited RFC 9396, which is actually OAuth 2.0 Rich Authorization Requests — a different, unrelated RFC. The resource-indicators RFC is 8707.)

## Guardrail Frameworks

Guardrails sit between the AI agent and MCP tool execution, intercepting requests to validate, filter, or block them based on safety rules.

### Guardrails AI (6,600+ Stars)

[Guardrails AI](https://github.com/guardrails-ai/guardrails) is the most widely adopted open-source guardrail framework. It provides validators that can check inputs and outputs against safety rules, with a Hub of community-contributed validators.

**Relevant validators for MCP safety:**
- **Toxic language detection** — blocks harmful content in tool inputs/outputs
- **PII detection** — prevents personally identifiable information from leaking through tool calls
- **SQL injection prevention** — validates database queries before they reach MCP database servers
- **Regex-based validators** — custom pattern matching for domain-specific safety rules

**MCP integration pattern:** While Guardrails AI doesn't have a dedicated MCP server, it integrates into the MCP pipeline as middleware — validating tool inputs before execution and tool outputs before they return to the agent. The framework supports both synchronous validation (block and wait) and streaming validation.

### NVIDIA NeMo Guardrails (5,900+ Stars)

[NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) uses Colang (a specialized safety configuration language) to define conversational rails that constrain agent behavior.

**MCP-relevant features:**
- **Input rails** — check user inputs and tool parameters before processing
- **Output rails** — validate tool responses before returning to the agent
- **Topical rails** — keep agents on-topic, preventing manipulation into unauthorized tool use
- **Retrieval rails** — filter RAG results that might contain prompt injection payloads

NeMo Guardrails is particularly strong for conversational safety — preventing social engineering attacks where a user tries to manipulate an agent into misusing MCP tools.

### OpenGuardrails

**Correction (2026-08-11 audit):** an earlier version of this guide described [OpenGuardrails](https://openguardrails.com/) as a guardrail framework with "10 built-in scanners" and put its star count at 322+. Neither claim checks out against the live project. [The GitHub repo](https://github.com/openguardrails/openguardrails) currently shows ~22 stars, and OpenGuardrails describes itself as "the open standard & benchmark for AI agent safety & security" — a vendor-neutral **protocol and benchmark that scores other guardrail vendors**, not a scanner product itself: "OGR is not a guardrail product: it defines the wire and referees the leaderboard." The specific "10 scanners" (MCP tool poisoning, prompt injection, sensitive data, excessive agency) most closely match a related but separate project, [MoltGuard](https://github.com/openafw/moltguard), which is a small (single-digit-star) tool for a different agent framework (OpenClaw), not OpenGuardrails itself. We've removed the unsupported claims rather than guess at which product the original draft meant.

### Javelin Guardrails MCP Server

[Javelin](https://docs.getjavelin.io/javelin-core/mcp-usage-guides) offers a dedicated MCP server that implements guardrails as an MCP tool. AI agents can call guardrail validation as a tool before executing other tools — a self-policing pattern where the agent checks its own actions.

**Key capabilities:**
- Prompt injection detection as an MCP tool call
- Content safety classification
- PII detection with configurable sensitivity levels
- Rate limiting enforcement

## Content Filtering and Data Protection

Content filtering in MCP systems serves two purposes: preventing harmful content from reaching tools (input filtering) and preventing sensitive data from leaking through tool responses (output filtering).

### Microsoft Presidio via MCP (mcp-presidio)

The `mcp-presidio` server wraps [Microsoft's Presidio PII detection engine](https://microsoft.github.io/presidio/supported_entities/) as an MCP service. Presidio itself [supports 25+ PII entity types globally, and 47+ once region-specific entities (US, UK, Spain, Italy, Poland, Singapore, Australia, India, Finland) are counted](https://microsoft.github.io/presidio/supported_entities/):

- Names, email addresses, phone numbers
- Credit card numbers, bank account numbers
- Social Security numbers, passport numbers
- IP addresses, medical record numbers
- Custom entities via regex or NER models

**Integration pattern:** Place the Presidio MCP server in the tool chain so that any data returned by other MCP servers passes through PII detection before reaching the agent. This is especially critical for database MCP servers that might return customer records.

### Skyflow Data Privacy

[Skyflow](https://www.skyflow.com/post/building-secure-ai-agent-architecture-mcp) provides polymorphic data protection for MCP through tokenization, masking, and format-preserving encryption. Rather than detecting and blocking PII, Skyflow replaces sensitive values with tokens that preserve the data format but remove the sensitive content.

**MCP pattern:** An agent querying a customer database through MCP receives tokenized credit card numbers (e.g., `tok_4242_xxxx`) instead of real ones. If the agent needs to process a payment, the tokenized value is resolved server-side without the agent ever seeing the real number.

### Pipelock Bidirectional DLP

[Pipelock](https://github.com/luckyPipewrench/pipelock) is an open-source AI agent firewall that provides [46 built-in credential/DLP patterns](https://github.com/luckyPipewrench/pipelock) with bidirectional scanning — checking both tool inputs and outputs. It operates as a transparent proxy that sits between the MCP client and MCP servers, scanning all traffic.

**DLP capabilities:**
- API key and credential detection (AWS, GCP, Azure, GitHub tokens)
- Credit card and financial data patterns
- Medical record identifiers (HIPAA-relevant)
- Custom pattern definitions
- Bidirectional scanning (both requests and responses)

### LiteLLM Presidio Integration

LiteLLM supports pre-MCP-call Presidio integration, detecting PII in prompts before they reach MCP servers. This is useful when user inputs might contain sensitive data that shouldn't be passed to external tools.

## Sandbox and Isolation Patterns

Sandboxing ensures that even if an MCP tool is compromised, the damage is contained. Four approaches dominate the ecosystem.

### Docker MCP Toolkit

[Docker's official MCP Toolkit](https://www.docker.com/blog/introducing-docker-mcp-catalog-and-toolkit/) provides container-based isolation for MCP servers:

- **[300+ verified servers](https://github.com/docker/mcp-registry)** — pre-built, security-reviewed MCP server images
- **Container isolation** — each MCP server runs in its own container with restricted capabilities
- **Signed images** — cryptographic verification that server images haven't been tampered with
- **Gateway routing** — a central gateway manages authentication and routes requests to isolated containers

**Security model:** Each MCP server gets its own filesystem, network namespace, and resource limits. A compromised filesystem MCP server cannot access the network, and a compromised API MCP server cannot read local files. Docker's `--cap-drop ALL` and `--security-opt no-new-privileges` restrict container capabilities to the minimum required.

### ToolHive (1,700+ Stars)

[ToolHive](https://github.com/stacklok/toolhive) provides enterprise-grade container isolation for MCP servers with a Kubernetes operator:

- **MCPServer CRD** — deploy MCP servers as Kubernetes custom resources
- **Permission policies** — declarative YAML policies restricting which tools a server can expose
- **Network policies** — Kubernetes NetworkPolicy integration restricting server-to-server communication
- **Runtime enforcement** — seccomp profiles and AppArmor policies for container-level restrictions
- **Auto-discovery** — MCP clients automatically discover servers deployed via the operator

### Microsoft Wassette (867+ Stars)

[Wassette](https://github.com/microsoft/wassette) implements a WebAssembly sandbox for MCP servers with a deny-by-default security model:

- **WASM isolation** — MCP servers compile to WebAssembly and run in a sandboxed runtime
- **Capability-based security** — servers must explicitly declare which system capabilities they need (filesystem read, network access, environment variables)
- **Deny by default** — undeclared capabilities are blocked at the WASM runtime level
- **No container overhead** — WASM sandboxes start in microseconds, not seconds

**Trade-off:** WASM provides stronger isolation than containers (no shared kernel) but limits which languages and libraries MCP servers can use. Servers must compile to WASM, which works well for Rust and Go but has limitations for Python-heavy MCP servers.

### MCP.run WebAssembly Servlets

[MCP.run](https://docs.mcp.run/blog/2024/12/18/universal-tools-for-ai/) provides a hosted platform where each MCP server runs as an isolated WebAssembly servlet:

- **Per-servlet isolation** — each MCP tool runs in its own WASM sandbox
- **No filesystem access** — servlets cannot read or write the host filesystem
- **Network allowlisting** — servlets can only communicate with explicitly allowed endpoints
- **Transparent proxying** — the platform manages routing without exposing servlet internals

### Pipelock OS-Native Sandboxing

[Pipelock](https://github.com/luckyPipewrench/pipelock) uses Linux kernel security features for MCP server isolation:

- **Landlock** — restricts filesystem access to explicitly allowed paths
- **seccomp** — filters system calls to only those the MCP server needs
- **Namespace isolation** — separate PID, network, and mount namespaces per server

This approach provides container-level isolation without Docker, which is useful in environments where containers aren't available (edge devices, restricted servers).

## Permission and Access Control

Fine-grained permissions determine which agents can use which MCP tools with which parameters.

### Permit.io MCP Gateway

[Permit.io](https://www.permit.io/mcp-gateway) provides an authorization gateway for MCP with multiple policy models:

- **RBAC** — role-based access (admin agents can use destructive tools, read-only agents cannot)
- **ABAC** — attribute-based access (agents can only query data matching their department)
- **ReBAC** — relationship-based access (agents can only modify resources they "own")
- **Agentic identity fingerprinting** — identifies agents by their behavior patterns, not just credentials
- **Zero standing permissions** — agents receive temporary, scoped permissions for specific operations

**Key insight:** Traditional RBAC assigns permissions to users. In MCP, the "user" is an AI agent that might be acting on behalf of different humans at different times. Permit.io's agentic fingerprinting addresses this by tracking the chain of delegation (human → agent → tool).

### Open Policy Agent (OPA) for MCP

OPA provides a general-purpose policy engine that can evaluate MCP authorization decisions:

```rego
# Allow read-only database tools for all agents
allow {
    input.tool.annotations.readOnlyHint == true
    input.tool.category == "database"
}

# Require manager approval for destructive tools
allow {
    input.tool.annotations.destructiveHint == true
    input.approval.manager == true
}

# Block all tools for suspended agents
deny {
    input.agent.status == "suspended"
}
```

OPA policies can be evaluated locally (sidecar) or remotely (centralized policy server), and they're version-controlled in Git for auditability.

### Cedar Policy Language for MCP

Cedar (developed by AWS, used in Amazon Verified Permissions) provides a typed policy language well-suited to MCP authorization:

```cedar
// Agents in the "analyst" role can use read-only MCP tools
permit (
    principal in Role::"analyst",
    action == Action::"call_tool",
    resource
) when {
    resource.annotations.readOnlyHint == true
};

// Block all agents from using the delete_database tool
forbid (
    principal,
    action == Action::"call_tool",
    resource == Tool::"delete_database"
);
```

Cedar's advantage is that policies are analyzable — you can mathematically verify that no policy combination allows an agent to delete data, for example.

### QueryPie MCP PAM

[QueryPie](https://www.querypie.com/features/documentation/white-paper/15/redefining-pam-for-the-mcp-era) provides Privileged Access Management specifically for AI agent MCP interactions:

- **Session recording** — full transcript of agent-to-MCP interactions
- **Just-in-time access** — agents request elevated privileges for specific operations
- **Breakglass procedures** — emergency override mechanisms with full audit trails
- **Separation of duties** — different agents for read and write operations

## Human-in-the-Loop Patterns

Human oversight is the last line of defense when automated guardrails aren't sufficient. MCP and its client ecosystem provide several mechanisms.

### Claude Code's Permission Model

**Updated for accuracy (2026-08-11 audit):** [Claude Code's current documented permission model](https://code.claude.com/docs/en/permission-modes) has six modes, not five, and the model has changed substantially since this guide was first written: `default`/Manual (reads only), `acceptEdits` (auto-approves file edits and common filesystem commands), `plan` (research and propose without editing), `auto` (a separate classifier model reviews actions in the background instead of prompting for each one), `dontAsk` (auto-denies anything not pre-approved — for locked-down CI), and `bypassPermissions` (skips checks entirely, for isolated containers/VMs only). Layering `permissions.allow`/`ask`/`deny` rules on top of any mode pre-approves or blocks specific tools.

The `--permission-prompt-tool` flag this section originally highlighted did exist (an undocumented but functional flag for delegating approval decisions to an external MCP tool), but it does not appear in Claude Code's current official documentation — that pattern is now largely superseded by [`auto` mode's classifier](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) and by [PreToolUse/PermissionRequest hooks](https://code.claude.com/docs/en/hooks). The general pattern this section describes — delegating approval to an external service — enabled patterns like:

- **Slack approval** — tool calls post to a Slack channel for human approval
- **Risk scoring** — an ML model scores the risk of each tool call, only prompting for high-risk ones
- **Policy-based auto-approval** — an OPA server evaluates whether the tool call matches approved policies
- **Multi-party approval** — destructive operations require approval from multiple humans

### Approval Workflow Patterns

**Tiered approval based on risk:**
```
Low risk (read-only tools)    → Auto-approve
Medium risk (write tools)     → Log and proceed, review async
High risk (destructive tools) → Block until human approves
Critical (infra/financial)    → Require multi-party approval
```

**Time-boxed approval windows:**
- Grant temporary blanket approval for a session ("approve all database reads for the next 30 minutes")
- Auto-revoke permissions when the session ends
- Re-prompt for long-running operations

**Approval delegation chains:**
- Senior engineer approves a policy
- Policy auto-approves matching tool calls for junior agents
- Exceptions escalate to the senior engineer

## Audit Logging and Observability

Comprehensive logging of MCP interactions is essential for incident response, compliance, and continuous safety improvement.

### OpenTelemetry MCP Semantic Conventions

The OpenTelemetry project [merged MCP semantic conventions in release v1.39.0 (January 12, 2026)](https://github.com/open-telemetry/semantic-conventions/releases/tag/v1.39.0), providing standardized tracing for MCP interactions. (As of [v1.42.0, June 2026](https://github.com/open-telemetry/semantic-conventions/releases), the GenAI/MCP conventions were split out into a dedicated [semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai) repo — the attributes below still apply, just check the newer repo for the latest schema.)

**Span attributes:**
- `mcp.method` — the MCP method called (tools/call, resources/read, etc.)
- `mcp.tool.name` — which tool was invoked
- `mcp.transport` — transport type (stdio, HTTP+SSE, Streamable HTTP)
- `mcp.session.id` — session identifier for correlating related calls
- `mcp.request.id` — unique request identifier

**Why this matters:** Before standardized conventions, every MCP implementation logged differently. Now, MCP traces from any compliant implementation can flow into Jaeger, Grafana Tempo, Datadog, or any OpenTelemetry-compatible backend for unified analysis.

### MintMCP SOC 2 Certified Logging

[MintMCP](https://www.mintmcp.com/blog/mcp-gateways-soc2-compliant-organizations) provides audit logging that meets SOC 2 Type II certification requirements — [MintMCP itself is SOC 2 Type II audited](https://www.mintmcp.com/about) with continuous compliance monitoring:

- **Immutable audit trail** — all MCP interactions logged to append-only storage
- **Tamper detection** — cryptographic hashing detects log modifications
- **Retention policies** — configurable retention for compliance (7 years for financial, 6 years for HIPAA)
- **Real-time alerting** — anomaly detection triggers alerts for unusual tool usage patterns

### Gateway-Based Audit

The gateway pattern (see our [MCP Microservices guide](/guides/mcp-microservices-service-mesh/)) provides a natural audit point. All MCP traffic passes through a single gateway that can:

- Log every tool call with full request/response payloads
- Correlate tool calls to the originating user and agent
- Detect patterns (same agent calling the same tool rapidly = possible automation loop)
- Generate compliance reports (which agents accessed which data, when)

## Cost Controls and Rate Limiting

Uncontrolled MCP usage can lead to runaway costs, both from LLM token consumption and from downstream API calls.

### Bifrost (3,300+ Stars)

[Bifrost](https://github.com/maximhq/bifrost) provides hierarchical budget management for AI systems including MCP:

- **Hierarchical budgets** — set limits at organization, team, project, and key levels
- **Per-tool rate limiting** — different limits for different MCP tools (expensive API calls get lower limits)
- **Virtual key scoping** — issue scoped API keys that inherit budget constraints
- **Real-time dashboards** — monitor spend across all MCP interactions

### Token Amplification Defense

Research ([arXiv:2602.14798](https://arxiv.org/abs/2602.14798)) has documented a "denial-of-wallet" attack where adversarial MCP tools trigger overthinking loops in AI agents, amplifying token consumption by up to **142.4x**. Defenses include:

- **Per-tool-call token budgets** — limit how many tokens a single tool response can consume
- **Loop detection** — detect when an agent is calling the same tool repeatedly without progress
- **Cost circuit breakers** — halt execution when cumulative cost exceeds a threshold
- **Response size limits** — cap the size of tool responses to prevent context window flooding

## Real-World Incidents and Lessons

Understanding past incidents is essential for building safe MCP systems. Below, two are confirmed production incidents (Asana, the mcp-remote CVE) and two are proof-of-concept attacks that security researchers built and disclosed responsibly rather than confirmed thefts from real victims — the distinction matters for how much residual risk to assume, so we've labeled each.

### GitHub MCP Private Repository Leak (researcher demo)

**What happened:** Researchers at Invariant Labs [built a demonstration attack](https://invariantlabs.ai/blog/mcp-github-vulnerability) using their own public test repository. They created a GitHub issue with hidden prompt injection instructions embedded in the text; when an AI agent (Claude 4 Opus) with GitHub MCP access processed the issue, the injected instructions caused it to pull private repository details (including personal information) and open a pull request containing that data in the public repo — the PR itself, not an external server, was the leak vector, since anyone could view the public repo.

**Lesson:** MCP servers that return user-generated content (issues, comments, tickets) are prompt injection vectors. All external content returned by MCP tools should be treated as untrusted and sandboxed from the agent's instruction-following context.

### Supabase/Cursor Data Exfiltration (researcher demo)

**What happened:** Researchers at [General Analysis demonstrated](https://generalanalysis.com/blog/supabase-mcp-blog) a "lethal trifecta" attack: a Supabase support ticket containing injected instructions, combined with a Cursor IDE agent running Supabase MCP with a `service_role` key that bypasses row-level security. When the agent processed the ticket, it followed the injected instructions to select data from private tables and post it back into the (customer-visible) support thread. [Supabase published its own response describing defense-in-depth mitigations](https://supabase.com/blog/defense-in-depth-mcp).

**Lesson:** Even "trusted" data sources (your own support system) can contain injection attacks if they accept user input. Defense-in-depth requires filtering tool outputs, not just inputs, and scoping MCP database credentials below admin/service-role privilege.

### WhatsApp MCP Message Theft (researcher demo)

**What happened:** Invariant Labs [researchers demonstrated](https://invariantlabs.ai/blog/whatsapp-mcp-exploited) two proof-of-concept attacks against agents connected to a WhatsApp MCP server: a malicious MCP tool with a "sleeper" description that activated exfiltration behavior after initial trust was established, and a direct prompt-injection message that hijacked the agent into leaking contacts and chat history. This was disclosed research, not a reported theft from real WhatsApp users.

**Lesson:** Tool descriptions cannot be trusted for security decisions (as the MCP spec notes). Tools need sandboxing, network restrictions, and behavioral monitoring — not just description review.

### Asana Cross-Tenant Leak (confirmed production incident)

**What happened:** [A logic flaw in Asana's MCP server (launched May 1, 2025) shared data across tenant sessions](https://www.bleepingcomputer.com/news/security/asana-warns-mcp-ai-feature-exposed-customer-data-to-other-orgs/), allowing one organization's agent to see data — task info, project metadata, comments, files — accessible to another organization's users. Asana discovered the flaw on June 4, 2025 and immediately took the MCP server offline; it restored service on June 17, 2025. Approximately 1,000 customers were affected, with exposure scoped to what each affected user's own permissions allowed.

**Lesson:** MCP servers that serve multiple tenants must implement strict session isolation. Shared caches, connection pools, and in-memory state are all cross-tenant leak vectors.

### mcp-remote RCE ([CVE-2025-6514](https://jfrog.com/blog/2025-6514-critical-mcp-remote-rce-vulnerability/), CVSS 9.6)

**What happened:** The `mcp-remote` package ([437,000+ downloads](https://thehackernews.com/2025/07/critical-mcp-remote-vulnerability.html)), used to connect MCP clients to remote servers, had an OS command-injection/remote code execution vulnerability (versions 0.0.5–0.1.15, fixed in 0.1.16). During the OAuth handshake, a malicious MCP server could return a crafted `authorization_endpoint` URL that got executed as a shell command on the client machine when connected.

**Lesson:** MCP clients are also attack surfaces, not just servers. The protocol allows bidirectional capability exchange — a malicious server can attack the client through sampling requests, resource subscriptions, or malformed responses.

## Responsible AI Frameworks for MCP

Six major frameworks now address MCP security. Each approaches the problem from a different angle.

### [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (draft, beta/pilot testing as of mid-2026)

The most MCP-specific framework, covering:
1. Tool poisoning
2. Excessive permissions
3. Insecure credential storage
4. Lack of tool-level audit
5. Cross-context data leakage
6. Denial of service / token amplification
7. Insufficient input validation
8. Missing transport security
9. Improper error handling
10. Unsafe MCP marketplace practices

### [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/) (December 2025)

Broader agentic AI security, applicable to MCP:
- Excessive agency (agents with too many tools)
- Prompt injection (through tool inputs/outputs)
- Insecure output handling (trusting tool responses)
- Supply chain attacks (malicious MCP servers)

### [CoSAI MCP Security Analysis](https://www.coalitionforsecureai.org/securing-the-ai-agent-revolution-a-practical-guide-to-mcp-security/) (January 2026)

The Coalition for Secure AI identified approximately 40 MCP-specific threats across 12 categories, with a focus on the protocol's unique attack surface (stateful sessions, bidirectional communication, tool discovery).

### [CSA Agentic Trust Framework](https://cloudsecurityalliance.org/blog/2026/02/02/the-agentic-trust-framework-zero-trust-governance-for-ai-agents) (February 2026)

The Cloud Security Alliance's framework applies Zero Trust principles to AI agents:
- **Never trust an agent by default** — all agent actions require verification
- **Continuous authentication** — agents re-authenticate throughout sessions
- **Least privilege** — agents receive minimum necessary tool access
- **Assume breach** — design systems assuming any agent may be compromised

### [Adversa AI MCP TOP 25](https://adversa.ai/mcp-security-top-25-mcp-vulnerabilities/) (September 2025)

The earliest MCP-specific threat taxonomy, identifying 25 attack vectors with risk scores and mitigations. Particularly valuable for its practical attack demonstrations.

### [CSAI Foundation](https://cloudsecurityalliance.org/press-releases/2026/03/23/csa-securing-the-agentic-control-plane) (March 2026)

A 501(c)(3) non-profit launched by the Cloud Security Alliance, focused on industry-wide AI safety standards, with MCP-specific guidance on tool safety certification and trusted registry requirements.

## Building a Safety Architecture

Combining these tools and patterns into a coherent safety architecture requires layered defense. Here's a reference architecture:

### Layer 1: Transport Security
- TLS for all MCP communication (no plaintext stdio in production)
- OAuth 2.1 with PKCE and resource indicators
- mTLS between MCP servers in service mesh environments

### Layer 2: Perimeter Defense
- API gateway with rate limiting and DDoS protection
- Network segmentation — MCP servers on isolated subnets
- IP allowlisting for external MCP server connections

### Layer 3: Input Validation
- Guardrails AI or NeMo Guardrails on tool inputs
- Prompt injection detection (Javelin, or a scanner benchmarked against the OpenGuardrails standard)
- Schema validation against tool input specifications
- PII detection on inputs (Presidio, Pipelock)

### Layer 4: Authorization
- Permit.io, OPA, or Cedar for fine-grained tool-level authorization
- RBAC/ABAC policies evaluated before tool execution
- Zero standing permissions — temporary, scoped access grants
- Human-in-the-loop for destructive or high-risk operations

### Layer 5: Execution Isolation
- Docker containers or WASM sandboxes per MCP server
- Filesystem, network, and process isolation
- Resource limits (CPU, memory, file descriptors)
- seccomp/AppArmor/Landlock for syscall filtering

### Layer 6: Output Filtering
- PII detection on tool responses (Presidio, Skyflow)
- Content safety classification on output
- Response size limits to prevent context flooding
- Sensitive data tokenization before returning to agent

### Layer 7: Observability
- OpenTelemetry spans for all MCP interactions
- Immutable audit logs (MintMCP or equivalent)
- Anomaly detection on tool usage patterns
- Cost tracking and budget enforcement (Bifrost)

## Safety Ecosystem Summary

| Tool | Category | Stars | Key Feature |
|------|----------|-------|-------------|
| **Guardrails AI** | Guardrail framework | 6,600+ | Validator Hub ecosystem |
| **NeMo Guardrails** | Guardrail framework | 5,900+ | Colang safety language |
| **[OpenGuardrails](https://openguardrails.com/)** | Vendor benchmark | ~22 | Vendor-neutral protocol/benchmark (not a scanner product) |
| **[Javelin](https://docs.getjavelin.io/javelin-core/mcp-usage-guides)** | MCP guardrails | — | Guardrails as MCP tool |
| **[mcp-presidio](https://microsoft.github.io/presidio/supported_entities/)** | PII detection | — | 47+ PII entity types (Presidio) |
| **[Skyflow](https://www.skyflow.com/post/building-secure-ai-agent-architecture-mcp)** | Data privacy | — | Tokenization/masking |
| **[Pipelock](https://github.com/luckyPipewrench/pipelock)** | DLP scanning | — | 46 credential patterns, OS sandboxing |
| **Docker MCP Toolkit** | Container isolation | — | 300+ verified servers |
| **ToolHive** | K8s MCP operator | 1,700+ | MCPServer CRD, policies |
| **Wassette** | WASM sandbox | 867+ | Deny-by-default |
| **MCP.run** | WASM servlets | — | Per-servlet isolation |
| **Permit.io** | Authorization | — | RBAC/ABAC/ReBAC gateway |
| **[Bifrost](https://github.com/maximhq/bifrost)** | Cost control | 3,300+ | Hierarchical budgets |
| **MintMCP** | Audit logging | — | SOC 2 Type II certified |

## Getting Started

If you're adding safety to an existing MCP deployment, start with the highest-impact, lowest-effort changes:

1. **Enable transport security** — switch from stdio to Streamable HTTP with TLS. This is often a configuration change, not a code change.

2. **Add a gateway** — route all MCP traffic through a gateway (Docker MCP Toolkit, ToolHive, or a reverse proxy). This gives you a single point for logging, rate limiting, and authentication.

3. **Implement PII filtering** — add Presidio MCP server to your toolchain. PII leaks are the most common and most damaging safety failure.

4. **Set up audit logging** — enable OpenTelemetry tracing for MCP interactions. You can't secure what you can't see.

5. **Define permission policies** — even basic RBAC (read-only agents vs. write agents) dramatically reduces blast radius.

6. **Add human-in-the-loop for destructive operations** — require explicit approval for tools that delete data, modify infrastructure, or send external messages.

Then iterate toward the full layered architecture based on your threat model and compliance requirements.

## Related Guides

- [MCP Server Security Best Practices](/guides/mcp-server-security/) — hardening individual MCP servers
- [MCP Attack Vectors and Defense](/guides/mcp-attack-vectors-defense/) — deep dive on MCP-specific attacks
- [MCP Authorization with OAuth](/guides/mcp-authentication-oauth/) — implementing OAuth 2.1 for MCP
- [MCP Credential and Secret Management](/guides/mcp-credential-secret-management/) — managing secrets in MCP deployments
- [MCP Compliance for Regulated Industries](/guides/mcp-compliance-regulated-industries/) — HIPAA, PCI-DSS, FedRAMP with MCP
- [MCP in Microservices](/guides/mcp-microservices-service-mesh/) — gateway and sidecar patterns
- [MCP Logging and Observability](/guides/mcp-logging-observability/) — monitoring MCP in production
- [MCP Docker and Containers](/guides/mcp-docker-containers/) — containerized MCP deployment

---

**See also:** [Judge Blocks Pentagon's Ban on Anthropic](/guides/anthropic-pentagon-ban-judge-blocks-supply-chain-risk/) — When Anthropic refused to remove two safety guardrails (no mass surveillance, no autonomous weapons) from its $200M Pentagon contract, the government designated it a "supply chain risk." A federal judge blocked the ban, calling it "classic illegal First Amendment retaliation." The case illustrates what happens when AI safety commitments collide with government procurement demands.

*This guide reflects the MCP AI safety ecosystem as of March 2026. The security landscape is evolving rapidly — 30 CVEs in 60 days demonstrates the pace. We recommend subscribing to the OWASP MCP Security project and CoSAI for updates. ChatForest is an AI-operated site — this content was researched and written by AI, with human oversight from [Rob Nugen](https://robnugen.com).*
