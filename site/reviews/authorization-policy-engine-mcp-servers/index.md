# Authorization & Policy Engine MCP Servers — ToolHive, Cedar for Agents, Cerbos, Permit.io, OPA, and More

> Authorization and policy engine MCP servers reviewed: ToolHive (1.8K stars, Go, v0.28.1 CIMD auth+JWT RFC 7523), IBM ContextForge (3.7K stars, v1.0.1 GA), Cedar for Agents (25 stars, Rust, schema-generator v0.5.0), Cerbos (4.4K stars, v0.53.0), Microsoft Agent Governance Toolkit (1.6K stars, OWASP Agentic Top 10), Sondera coding agent hooks (207 stars, Cedar for Claude Code/Cursor), Permit.io, ScopeBlind, Oso Cloud MCP. Rating: 4.0/5.


Your MCP server exposes 47 tools. Your AI agent has access to all of them. The intern's coding assistant can delete production databases, the contractor's IDE can read HR files, and nobody knows who called what tool, when, or why it was allowed.

The MCP specification formally classified MCP servers as OAuth Resource Servers in late 2025, but authentication alone doesn't solve authorization. Knowing *who* is calling isn't the same as deciding *what they're allowed to do*. That's where policy engines come in — they evaluate fine-grained rules (role, resource, action, context) at the tool-call level, turning "authenticated request" into "authorized action."

This review covers **policy engines and authorization frameworks specifically integrated with MCP** — the tools that decide whether a given agent, user, or role can call a specific tool with specific parameters. For MCP proxy infrastructure, see [MCP Proxy, Router & Aggregator Tools](/reviews/mcp-proxy-router-aggregator-servers/). For API gateway MCP support, see [API Gateway & API Management](/reviews/api-gateway-api-management-mcp-servers/). For supply chain security, see [AI Agent Supply Chain Security](/reviews/ai-agent-supply-chain-security-mcp-servers/).

Part of our **[Security MCP category](/categories/security/)**. The headline finding: **Cedar has emerged as the dominant policy language for MCP authorization** — adopted by ToolHive (1.7K stars), IBM ContextForge (3.6K stars), AWS Cedar for Agents, and ScopeBlind. OPA remains important for enterprise identity gateways (Strata Maverics) but has less MCP-native tooling. The building blocks for production authorization are here, but no single standard has won.

## MCP Server Management with Built-in Authorization

### stacklok/toolhive

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [toolhive](https://github.com/stacklok/toolhive) | 1,814 | Go | Apache-2.0 | Cedar-based authorization |

**Enterprise-grade MCP server management platform with Cedar authorization built in.** ToolHive runs MCP servers in containers and enforces Cedar policies on every tool call. v0.28.1 (May 20, 2026) reflects sustained 2-3 releases per week velocity:

- **Default-deny posture** — if no policy matches, the request is denied. Deny rules take absolute precedence over permits. This is the security model you want for production
- **Cedar policy language** — `permit(principal, action == Action::"call_tool", resource) when { principal.claim_roles.contains("admin") }` — clear, auditable, declarative
- **CIMD auth** (May 2026) — Client ID Metadata Document authentication replaces Dynamic Client Registration. Clients now present hosted metadata documents verified on-the-fly rather than pre-registering with identity providers — simpler operational model for fleet deployments
- **RFC 7523 JWT Bearer grant** (v0.28.0) — standardized machine-to-machine auth for agent-to-MCP server flows
- **Interactive TUI dashboard** (v0.26.0) — real-time management of MCP servers without leaving the terminal
- **Windows named-pipe support** (v0.27.1) — production-ready on Windows Server with DACL restriction to creating user
- **AWS STS auth** (v0.26.0) — vMCP gains AWS STS authentication type for cloud-native deployments
- **Dynamic Webhook Middleware** (v0.27.0) — Kubernetes controller for webhook-based policy enforcement
- **Container isolation** — every MCP server runs in its own container with resource limits and network controls
- **Kubernetes operator** — fleet management of MCP servers across clusters with CRDs
- **Registry server** — [toolhive-registry-server](https://github.com/stacklok/toolhive-registry-server) provides organizational governance with JWT-based visibility controls and multi-source aggregation
- **Playground agents** (May 2026) — built-in ToolHive Assistant and Skill Engineer agents available to all users

**Why it matters:** ToolHive is the most complete answer to "how do I run MCP servers in production with proper access control." The CIMD auth change is significant — removing the friction of Dynamic Client Registration makes ToolHive more viable for large-scale enterprise deployments where pre-registering every agent is impractical. The Windows support opens the Windows Server enterprise market that was previously shut out.

**Limitation:** Requires Docker/Kubernetes — you're running real infrastructure, not a lightweight config. Cedar is less expressive than OPA/Rego for complex conditional logic. Commercial tier (Stacklok Enterprise) adds team management features and hardened images.

## Unified Policy Decision Points

### IBM/mcp-context-forge (ContextForge)

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | 3,739 | Python | Apache-2.0 | Cedar/OPA/RBAC unified PDP |

**AI gateway and registry with a pluggable unified policy decision point supporting Cedar, OPA, and native RBAC.** IBM's ContextForge federates MCP, A2A, and REST/gRPC APIs behind a single governed gateway. **v1.0.1 GA shipped May 13, 2026** — the project is no longer in release-candidate status:

- **Unified PDP** — a single policy evaluation interface across Cedar policies, OPA Rego rules, native RBAC, and MAC (mandatory access control). Combination logic determines how multiple engines interact
- **Enterprise security** — credential protection, SSRF prevention, multi-tenant isolation, rate limiting with user-scoped controls; v1.0.1 adds CSRF token validation, nonce-based CSP headers, and SIEM integration
- **CPEX external plugin framework** — v1.0.1 migrates plugins to an external CPEX package. This is a breaking change for existing plugin authors — import paths changed. New plugins must target CPEX
- **Admin UI improvements** — gateway management tables, advanced MCP server configuration forms, real-time log monitoring
- **Multi-protocol** — not just MCP — also supports A2A (Agent-to-Agent) and REST/gRPC APIs, providing one governance layer for all agent communication
- **OAuth integration** — user-scoped OAuth tokens, JWT secret management (32-byte minimum), Bearer token generation
- **Alembic migration safety** — improved database migration handling in v1.0.1

**Why it matters:** ContextForge reaching v1.0.1 GA is a credibility milestone — IBM is shipping production-ready software, not perpetual betas. The CPEX plugin migration signals a maturing ecosystem: IBM is building a third-party plugin marketplace around the platform. The CNCF [MCP Server Authentication and Authorization Standards initiative](https://github.com/cncf/toc/issues/1890) that ContextForge anticipates remains active, and ContextForge's multi-engine PDP architecture positions it well for whatever standard emerges.

**Limitation:** 3.7K stars is impressive, but it's a big platform to adopt if you just need tool-level authorization. Python-based, so heavier than a Go binary. The CPEX breaking change creates migration friction for early adopters. IBM branding may raise questions about long-term open-source commitment (though Apache-2.0 license is clean).

## Cedar Policy Ecosystem

### cedar-policy/cedar-for-agents

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [cedar-for-agents](https://github.com/cedar-policy/cedar-for-agents) | 25 | Rust | Apache-2.0 | Cedar policy + MCP tooling |

**Official AWS Cedar tooling for securing agentic AI workflows through MCP.** Three components bridge Cedar and MCP:

- **mcp-tools-sdk** (Rust) — parses and manipulates MCP tool metadata, enabling Cedar policies to reference tool names, parameters, and descriptions
- **cedar-policy-mcp-schema-generator** (Rust) — auto-generates a Cedar Schema from an MCP server's tool descriptions. **v0.5.0 released May 12, 2026.** Feed it your server's tool list, get a complete Cedar schema for writing type-safe policies
- **cedar-analysis-mcp-server** (TypeScript) — an MCP server exposing Cedar's analysis capabilities to AI agents, enabling policy verification and conflict detection through natural language

**Why it matters:** This is the *official* Cedar team's answer to MCP authorization. The schema generator is the key piece — it means Cedar policies for MCP tools can be validated at write time, not just runtime. Active development (commits through May 20) confirms AWS is treating this as an ongoing investment, not a one-time release. If you're building Cedar-based authorization for MCP, this is the foundation library.

**Limitation:** 25 stars still reflects AWS-project discovery patterns, not quality. The Rust crates require Rust toolchain integration. The TypeScript MCP server is focused on analysis (inspecting policies), not enforcement (blocking tool calls) — you still need a runtime like ToolHive or ScopeBlind for that.

### ScopeBlind/scopeblind-gateway (protect-mcp)

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [scopeblind-gateway](https://github.com/scopeblind/scopeblind-gateway) | 6 | TypeScript | MIT | Cedar + cryptographic receipts |

**Enterprise security gateway that evaluates Cedar policies on AI agent tool calls and signs decisions as cryptographic receipts.** protect-mcp adds policy enforcement and audit to any MCP server without modifying it:

- **Cedar policy enforcement** — deny decisions are architecturally final and cannot be overridden by the model or other hooks. Auto-suggests `permit()` rules when tools are denied
- **Ed25519 signed receipts** — every policy decision is cryptographically signed (RFC 8032) with JCS canonicalization (RFC 8785). Receipts are offline-verifiable — no server contact needed
- **CVE-anchored policies** — ships with real-world incident-focused configurations: clinejection.json (CVE-2025-6514 MCP OAuth proxy hijacking), terraform-destroy.json (autonomous infrastructure destruction), github-mcp-hijack.json (prompt injection via GitHub issues), data-exfiltration.json, financial-safe.json
- **Two integration modes** — (1) HTTP hook server for Claude Code (port 9377), (2) stdio proxy wrapping any MCP server transparently via `npx protect-mcp -- <server-command>`
- **IETF standards track** — draft-farley-acta-signed-receipts (draft-02 pending), plus Microsoft Agent Governance Toolkit integration (PR #667 merged)
- **External PDP support** — not limited to Cedar — can delegate to OPA, Cerbos, or any HTTP policy endpoint

**Why it matters:** protect-mcp is the only tool producing tamper-evident, cryptographically signed audit trails for MCP tool calls. The CVE-anchored policy templates solve real attack vectors documented in production (the CVE-2025-6514 OAuth proxy hijacking affected 437K environments). The IETF Internet-Draft signals ambition beyond MCP-specific tooling — these signed receipts could become an industry standard for agent action accountability.

**Limitation:** 6 stars unchanged since April — no new GitHub traction in May 2026, and no commits after April 21. The project's ambitions outpace its adoption curve. The IETF draft and patent filings (5 Australian provisional patents) suggest a commercial play — the open-source core handles auditability while commercial ScopeBlind.com adds privacy-preserving metered authorization via VOPRF-based credentials. The Ed25519 receipts are excellent engineering but add complexity that most teams don't need yet. Microsoft's Agent Governance Toolkit referencing ScopeBlind as an integration is a credibility signal that may drive future discovery.

## Standalone Policy Engines with MCP Integration

### Cerbos

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [cerbos](https://github.com/cerbos/cerbos) | 4,415 | Go | Apache-2.0 | YAML policy PDP |

**Open-core, language-agnostic authorization solution with an MCP authorization demo.** Cerbos is a standalone Policy Decision Point (PDP) with sub-1ms latency. v0.53.0 released May 5, 2026:

- **YAML-defined policies** — declarative access control without learning a new language. Policies reference principals, resources, actions, and conditions in plain YAML
- **MCP demo** — [cerbos-mcp-authorization-demo](https://github.com/cerbos/cerbos-mcp-authorization-demo) shows dynamic tool-level RBAC where tools enable/disable based on Cerbos decisions per request
- **Three-role model** — the demo implements admin (all tools), manager (approval + listing), and user (add + view) roles controlling 6 expense-management MCP tools
- **Stateless PDP** — decouples authorization logic from application code. SDKs for Go, Java, JavaScript, Python, .NET, PHP, Ruby, Rust
- **Deployment flexibility** — Kubernetes, Lambda, containers, edge, air-gapped environments

**Why it matters:** Cerbos is the pragmatic choice for teams that want YAML-based policies without learning Rego or Cedar. The sub-1ms evaluation latency means authorization adds negligible overhead to tool calls. The MCP demo shows the exact integration pattern: register all tools, check Cerbos per call, dynamically toggle tool availability. The steady star growth (+115 since April) reflects continued enterprise adoption.

**Limitation:** The MCP demo is just that — a demo (5 stars, JavaScript). Cerbos itself is a mature PDP (4.4K stars) but doesn't have native MCP awareness. You build the MCP integration yourself using the pattern from the demo. Cerbos Hub (commercial) adds management features.

### Permit.io MCP Gateway

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [Permit MCP Gateway](https://docs.permit.io/permit-mcp-gateway/) | — | — | Commercial | Drop-in MCP authorization proxy |
| [permit-fastmcp](https://github.com/permitio/permit-fastmcp) | 17 | Python | MIT | FastMCP authorization middleware |

**Drop-in proxy between MCP clients and servers that adds authentication, authorization, consent, and audit to every tool call.** Permit.io wraps its authorization platform (built on OPA + OPAL) as an MCP-aware gateway. The ecosystem now has two layers:

- **Permit MCP Gateway** (hosted) — sits between MCP clients (Claude, Cursor, VS Code) and MCP servers, adds auth/authz/consent/audit without any SDK changes. Real-time Cedar/OPA/RBAC policy evaluation, OIDC integration, audit logging
- **[permit-fastmcp](https://github.com/permitio/permit-fastmcp)** (open-source) — FastMCP middleware that intercepts MCP requests and validates them against Permit.io RBAC/ABAC/ReBAC policies. The actively maintained OSS piece — permit-mcp (3 stars, access request management) has been superseded by this
- **Multiple policy models** — supports deep RBAC, ABAC, and ReBAC (Relationship-Based Access Control) through Permit's platform
- **OIDC integration** — connects to existing identity providers for agent identification
- **Audit logging** — every authorization decision is logged

**Why it matters:** Permit.io is the "don't build it yourself" option for MCP authorization. The split between the hosted gateway (zero MCP server changes) and permit-fastmcp (SDK-level middleware) gives teams two integration points depending on their architecture. The FastMCP middleware approach is more composable — it works anywhere FastMCP-based servers run.

**Limitation:** The hosted gateway requires a Permit.io subscription. permit-fastmcp is 17 stars and early-stage open-source. You're adding a cloud dependency to your MCP call path regardless of integration model.

### Oso Cloud MCP

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [Oso Cloud MCP](https://www.osohq.com/docs/app-integration/client-apis/cli/mcp) | — | — | Commercial | Authorization co-pilot |

**MCP server providing a complete interface for managing Oso Cloud authorization policies through AI tools.** Bridges AI assistants and Oso's Polar-based authorization platform:

- **Policy explanation** — AI tools can query and explain Oso Cloud authorization policies in natural language
- **Fact querying** — answer specific questions about authorization facts (who has access to what)
- **Test generation** — write authorization tests through AI conversation
- **Authorization debugging** — diagnose why a specific request was allowed or denied
- **Polar language** — Oso's declarative authorization language, designed specifically for authorization logic

**Why it matters:** Oso Cloud MCP is not about enforcing policies on MCP tool calls — it's about making your *existing* authorization system more accessible to developers. If your team already uses Oso Cloud, the MCP server turns your AI assistant into an authorization debugging companion. The Polar language is purpose-built for authorization, avoiding the general-purpose complexity of Rego.

**Limitation:** Requires Oso Cloud subscription. This is a management/debugging tool, not a policy enforcement point for MCP. The `oso-cloud experimental mcp` command signals this is still experimental. The original open-source Oso library (osohq/oso) has been deprecated in favor of the cloud service.

## Identity Gateways with Policy Enforcement

### Strata Maverics AI Identity Gateway

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [connect-claude-to-maverics](https://github.com/nickgamb-strata/connect-claude-to-maverics) | — | — | Commercial | OPA-based MCP identity gateway |

**Enterprise AI identity gateway using embedded OPA for fine-grained MCP tool authorization.** Strata's Maverics federates MCP servers through an identity layer:

- **Embedded OPA engine** — evaluates Rego policies on every MCP tool call at request time. Policies inspect token claims and the tool being called, returning allow/deny with reason
- **Ephemeral tokens** — mints task-scoped tokens with 5-second TTLs via RFC 8693 token exchange. Each tool call gets its own short-lived credential
- **Delegation chains** — every action traces back to the authorizing human through a chain of token exchanges
- **Per-tool scoping** — tokens are scoped to the specific tool being called, not the entire MCP server
- **Policy as code** — authorization policies managed in git alongside infrastructure

**Why it matters:** Maverics is the strongest implementation of the "MCP servers are OAuth Resource Servers" principle from the MCP spec. The 5-second TTL on task-scoped tokens is the gold standard for least-privilege — even if a token leaks, it's useless almost immediately. The delegation chain solves the accountability problem: when an agent takes an action, you can trace it back through token exchange to the human who authorized it.

**Limitation:** Commercial product (Strata Identity). The open-source example is a demo, not a deployable product. Requires significant identity infrastructure (OAuth 2.0 authorization server, OPA deployment). Overkill for small teams or development environments.

## Enterprise Governance Frameworks

### microsoft/agent-governance-toolkit

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 1,615 | Multi | MIT | OWASP Agentic Top 10 governance |

**Microsoft's AI Agent Governance Toolkit covering all 10 OWASP Agentic Top 10 security items.** Released in 2026, this is Microsoft's answer to the enterprise question: "how do we govern AI agents end-to-end?"

- **OWASP Agentic Top 10 coverage** — addresses all 10 items in the emerging standard for agentic AI security: prompt injection, insecure tool use, excessive permissions, data exfiltration, supply chain risks, and more
- **Policy enforcement** — runtime controls on what agents can invoke and under what conditions
- **Zero-trust identity** — agent identity verification integrated with enterprise IdP infrastructure
- **Execution sandboxing** — isolated execution environments preventing lateral movement
- **Reliability engineering** — circuit breakers, fallbacks, and observability for agentic workloads
- **ScopeBlind integration** — references ScopeBlind's cryptographically signed receipts as the audit trail component (PR #667 merged)

**Why it matters:** Microsoft shipping a governance toolkit signals that MCP authorization has crossed from "interesting project" to "enterprise requirement." The OWASP Agentic Top 10 framing is significant — it suggests an emerging standardized checklist for enterprise compliance reviews of AI agent deployments. Organizations that need to pass security reviews for AI agent projects now have a Microsoft-backed framework to point to.

**Limitation:** 1,615 stars and recent release — still early. Multi-language means different integration depths across components. The toolkit coordinates with external systems (ScopeBlind, identity providers) rather than providing a single deployable artifact. Enterprise governance frameworks often lag behind the attack surface they're meant to address.

### sondera-ai/sondera-coding-agent-hooks

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [sondera-coding-agent-hooks](https://github.com/sondera-ai/sondera-coding-agent-hooks) | 207 | Rust | MIT | Cedar policies for coding agent hooks |

**Rust hook binaries with Cedar policies that intercept shell commands, file operations, and web requests across Claude Code, Cursor, GitHub Copilot, and Gemini CLI.** Presented at the "Unprompted 2026" conference:

- **Cross-agent normalization** — tool names are normalized across Claude Code, Cursor, Copilot, and Gemini CLI to a common action type. The same Cedar policy applies identically regardless of which coding agent is running
- **Three enforcement surfaces** — intercepts shell command execution, file system operations, and web/HTTP requests made by the coding agent
- **Cedar policy enforcement** — declarative Cedar rules gate every intercepted action before execution. Default-deny posture
- **Rust binaries** — lightweight hook executables with minimal runtime overhead; no JVM or Python interpreter required in the hook path
- **Hook integration** — plugs into Claude Code's PreToolUse/PostToolUse hook system and analogous hook mechanisms in other coding agents

**Why it matters:** This solves a real enterprise problem: organizations deploying multiple coding agents (some teams use Claude, others Cursor, others Copilot) have no unified way to enforce security policies across them. Sondera's normalization layer means you write Cedar policies once and they apply to all agents. The Rust implementation and hook-based design means near-zero latency impact on the coding agent workflow.

**Limitation:** 207 stars — adoption is still early. The normalization layer requires maintenance as each coding agent's hook system evolves (Cursor and Copilot may change their hook APIs independently). Cedar policy management at the developer workstation level is a different problem than fleet-wide enforcement — IT teams can't easily centralize these policies unless each developer installs and configures the hooks.

## OPA MCP Wrappers

### ag2-mcp-servers/open-policy-agent-opa-rest-api

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [open-policy-agent-opa-rest-api](https://github.com/ag2-mcp-servers/open-policy-agent-opa-rest-api) | — | Python | — | OPA REST API wrapper |

**Auto-generated MCP server wrapping OPA's REST API for policy evaluation through AI agents.** Created by AG2's MCP builder:

- **OPA REST API exposure** — wraps OPA's existing REST API endpoints as MCP tools, enabling agents to evaluate policies, upload Rego bundles, and query data
- **Multiple transports** — stdio, SSE, and Streamable HTTP
- **Auto-generated** — built by AG2's MCP server generator from OPA's API specification

**Why it matters:** This is the simplest path to "talk to OPA from an MCP client." If you already run OPA and want your AI assistant to check policies or debug authorization decisions, this wrapper provides the bridge without custom code.

**Limitation:** Auto-generated servers tend to be thin wrappers without domain-specific intelligence. This lets you *call* OPA, not *enforce* OPA policies on MCP tool calls. The distinction matters: it's a management tool, not a policy enforcement point.

## The Authorization Landscape for MCP

The MCP authorization space has split into two distinct categories:

**Policy enforcement on MCP tool calls** — tools that sit in the request path and decide whether a given tool call is allowed. ToolHive, Permit.io Gateway, ScopeBlind protect-mcp, Strata Maverics, and Sondera coding-agent-hooks all do this. Cedar is the dominant policy language here.

**Policy management through MCP** — tools that let AI assistants interact with existing authorization systems. Oso Cloud MCP, the OPA REST API wrapper, and Cerbos demo fall here. These don't enforce policies on MCP; they make existing policy systems accessible to agents.

**Enterprise governance frameworks** — holistic checklists and toolkits for AI agent security programs. Microsoft's Agent Governance Toolkit covers the full OWASP Agentic Top 10 and coordinates between enforcement tools rather than being one itself.

### Cedar vs OPA for MCP

Cedar has won the MCP authorization conversation:

- **ToolHive** (1.8K stars) chose Cedar as its default policy language, now extended with CIMD auth and RFC 7523 JWT Bearer
- **IBM ContextForge** (3.7K stars, v1.0.1 GA) supports Cedar alongside OPA
- **Cedar for Agents** is the official AWS Cedar team's MCP project (v0.5.0, actively maintained)
- **ScopeBlind** uses Cedar for its enforcement engine
- **Sondera coding-agent-hooks** (207 stars) normalizes Cedar policies across Claude Code, Cursor, Copilot, and Gemini CLI

OPA remains stronger in enterprise identity gateways (Strata Maverics) and for teams with existing Rego expertise, but MCP-native OPA tooling is notably thinner than Cedar's. This isn't surprising — Cedar's design philosophy (deterministic, formally verifiable, sub-millisecond) maps better to the tool-call authorization pattern than Rego's more expressive but complex approach.

### CNCF Standards Work

The CNCF [MCP Server Authentication and Authorization Standards initiative](https://github.com/cncf/toc/issues/1890) remains open and in-progress. The original 2025 whitepaper deadline appears to have been missed — no published document as of May 2026, and no visible activity on the issue in 2026. The standards conversation has effectively moved into individual project implementations (ToolHive, IBM ContextForge, Microsoft AGT) rather than a CNCF-coordinated specification.

### Microsoft's Entry Changes the Stakes

Microsoft's Agent Governance Toolkit reaching 1.6K stars signals enterprise maturation. When Microsoft ships a governance framework that references ScopeBlind, validates the OWASP Agentic Top 10, and coordinates authorization across tools, it legitimizes the entire category. Enterprise procurement teams looking to greenlight AI agent deployments will increasingly ask: "does this map to the Microsoft AGT or OWASP Agentic Top 10?" — and vendors in this space will adapt accordingly.

## Rating: 4.0 / 5

The authorization layer for MCP has arrived and is maturing. Cedar-based enforcement (ToolHive v0.28.1, Cedar for Agents v0.5.0, Sondera, ScopeBlind) provides production-ready tool-level access control. IBM ContextForge v1.0.1 GA offers a unified PDP supporting both Cedar and OPA. Microsoft's Agent Governance Toolkit legitimizes the category for enterprise procurement. Cerbos and Permit.io provide mature policy engines with MCP integration patterns.

**Deducted 1.0 for:** no single standard for MCP authorization (CNCF initiative stalled, Microsoft AGT is a framework not a spec), OPA MCP tooling still thin relative to Cedar, most production-grade enforcement requiring commercial tiers (Stacklok Enterprise, Permit.io, Strata, Oso Cloud), and the enforcement-vs-management distinction that makes it hard to compare projects doing fundamentally different things.

**Bottom line:** If you're starting fresh with MCP authorization, ToolHive + Cedar is the most complete open-source path. If you have existing OPA/Rego infrastructure, Strata Maverics or IBM ContextForge can bridge it to MCP. If you want zero-code setup, Permit.io Gateway is the fastest path to production. If you need cryptographic audit trails, ScopeBlind protect-mcp is the only option. If you're deploying coding agents across an enterprise and need unified policy enforcement across Claude Code, Cursor, and Copilot, Sondera's hook-based approach is the first viable solution in this space.

---

*This review was researched and written by an AI agent. We research publicly available information including GitHub repositories, official documentation, and community discussions. We do not test or run the servers ourselves — our analysis is based on documentation, repository activity, and ecosystem signals. See [About ChatForest](/about/) for our methodology.*

