---
title: "HashiCorp Consul MCP Server: Service Mesh Diagnostics and Service Discovery for AI Agents (Builder Guide)"
date: 2026-06-17
description: "HashiCorp's official Consul MCP Server gives AI agents 50+ read-only tools across 15 toolsets — service catalog queries, health diagnostics, ACL auditing, Connect mesh inspection, and cross-datacenter troubleshooting. Here is what builders need to wire it in."
og_description: "50+ tools, 15 toolsets, zero write operations. The Consul MCP Server turns AI agents into Consul diagnostic engines — cross-datacenter health, ACL auditing, service mesh intention review, and KV exploration without CLI gymnastics."
content_type: "Builder's Log"
categories: ["MCP", "Infrastructure", "DevOps", "AI Agents"]
tags: ["hashicorp", "consul", "mcp", "service-discovery", "service-mesh", "sre", "platform-engineering", "acl", "connect", "cross-datacenter", "claude", "claude-code", "ai-agents", "builder-guide", "infrastructure", "devops"]
---

Debugging a Consul deployment manually means knowing which CLI command retrieves health state versus catalog state, how to cross-correlate intentions against service identity, which datacenter endpoint to query for a given service, and when to reach for the API versus the UI. For teams running Consul across multiple datacenters and hundreds of services, this expertise is both deep and rare.

HashiCorp's official Consul MCP Server (v0.1.3, October 2025) makes that knowledge callable. Fifty-plus read-only tools across 15 toolsets — service catalog, health checks, KV store, ACL policies, Connect mesh, sessions, peering, discovery chains, prepared queries, namespaces — all accessible through natural language from any MCP-compatible agent.

It does not write anything. That constraint is worth understanding before you reach for it.

---

## What the Consul MCP Server Is

The Consul MCP Server is an official HashiCorp server that translates MCP tool calls into Consul HTTP API requests. It launched at HashiConf in September 2025 alongside the HashiCorp MCP suite (Terraform, Vault, and Vault Radar are the other three).

It connects to any self-managed Consul cluster — Community Edition or Enterprise — via the standard HTTP API. No special Consul configuration required. Point `CONSUL_HTTP_ADDR` at your cluster, provide an ACL token with appropriate read permissions, and it works.

**Transport:** stdio (local use with Claude Desktop, Claude Code, Cursor) and StreamableHTTP (remote/shared deployment). Both are supported from the same binary.

**License:** BSL 1.1. Same license as Consul itself since August 2023. Not OSI-approved open source.

**HCP Consul Dedicated:** Reached end-of-life November 12, 2025. This server targets self-managed Consul only.

---

## The Problem: Consul's API Surface Is Too Wide for Manual Navigation

Consul's HTTP API covers more than 150 endpoints across its functional areas. A developer debugging why two services cannot communicate through the mesh needs to query:

- The service catalog to confirm both are registered and which nodes they appear on
- Health checks to confirm both are passing
- ACL to check whether an intention exists allowing the connection
- Connect CA to confirm the certificate chain is valid
- The discovery chain to see whether traffic routing rules are interfering

That is five separate query domains, each with its own endpoint patterns and parameter conventions. For an SRE on call at 2 AM in an unfamiliar Consul deployment, it is genuinely hard.

An AI agent with the Consul MCP Server can traverse all five of those domains in a single natural language prompt. The agent knows which tools to call, in what order, and how to correlate the results.

---

## Architecture: 15 Toolsets, 50+ Tools

The Consul MCP Server organizes its tools into 15 named toolsets. Every tool is read-only (HTTP GET).

### Catalog (7 tools)

Service registration and discovery — Consul's original purpose.

| Tool | Purpose |
|------|---------|
| `get_catalog_services` | List all registered services |
| `get_catalog_nodes` | List all registered nodes |
| `get_catalog_service` | Details for a specific service (all nodes) |
| `get_catalog_connect` | List Connect-capable services |
| `get_catalog_node` | Details for a specific node (all services) |
| `get_catalog_datacenters` | List all known datacenters |
| `get_catalog_gateway_services` | Services behind a gateway |

### Health (6 tools)

`get_health_node`, `get_health_checks`, `get_health_service`, `get_health_connect`, `get_health_ingress`, `get_health_state`

`get_health_state` is particularly useful for agents: it returns all checks in a given state (passing, warning, critical) across the cluster — a fast first step in any incident investigation.

### Key-Value Store (3 tools)

`get_kv`, `get_kv_keys`, `get_kv_recursive`

Consul KV stores application configuration, feature flags, and distributed lock state in many organizations. `get_kv_recursive` enumerates an entire namespace prefix — useful for agents reasoning about configuration sprawl or debugging misconfigured applications.

### ACL (6 tools)

| Tool | Purpose |
|------|---------|
| `get_acl_tokens` | List all ACL tokens |
| `get_acl_policies` | List all ACL policies |
| `get_acl_roles` | List all ACL roles |
| `get_acl_auth_methods` | List configured authentication methods |
| `get_acl_binding_rules` | List ACL binding rules |
| `get_acl_templated_policies` | List templated policy definitions |

This is one of the server's strongest use cases. Consul ACL configurations accumulate complexity — tokens proliferate, policies overlap, roles inherit from roles. The six tools together give an agent enough context to reason about privilege scope, token over-provisioning, and auth method coverage across the cluster.

### Connect / Service Mesh (6 tools)

`get_connect_ca_roots`, `get_connect_ca_configuration`, `get_connect_intentions`, `get_connect_intention`, `get_connect_intention_match`, `get_connect_intention_check`

Consul Connect manages mTLS between services. These six tools expose the trust model: CA root inspection, intention listing and matching, and explicit intention checks. "Does service A have an intention allowing it to call service B?" is a question that takes 30 seconds to answer through the MCP server and 5 minutes of CLI work to answer manually.

### Agent (7 tools)

`get_agent_self`, `get_agent_config`, `get_agent_members`, `get_agent_metrics`, `get_agent_host`, `get_agent_version`, `get_agent_reload`

Agent-level diagnostics rather than service-level. Useful for verifying cluster membership, agent configuration, and runtime metrics when the Consul agent itself is suspected.

### Operator (4 tools)

Autopilot configuration, keyring management, license information, and Raft consensus state. The Raft tools (`raft_configuration`, `raft_autopilot_state`) are valuable for diagnosing split-brain scenarios and leader election issues — edge cases where the Consul cluster itself needs investigation rather than the services it manages.

### Session (3 tools)

`get_session`, `get_session_node`, `get_session_list`

Consul sessions underpin distributed locking (leader election, distributed locks for job scheduling). These tools expose current session state — which nodes hold sessions, what locks are active, TTLs. Essential for debugging distributed systems that use Consul for leader election.

### Status (2 tools)

`get_status_leader`, `get_status_peers`

Cluster status: current Raft leader and voting peers. Quick operational health check.

### Peering (3 tools)

`get_peerings`, `get_peering`, `get_peering_exported_services`

Consul Cluster Peering connects service discovery across administrative boundaries — different clusters, cloud accounts, or regions. These three tools expose peering relationships and which services are exported across them. Critical for multi-cluster and multi-cloud architectures where cross-cluster service visibility fails.

### Config Entries (2 tools)

`get_config_entries`, `get_config_entry`

Config entries define mesh-wide behavior: service defaults, proxy defaults, ingress gateways, terminating gateways, mesh policies. These tools let agents inspect what mesh-level configuration is active and its current values.

### Discovery Chain (1 tool)

`get_discovery_chain` retrieves the compiled service discovery chain for a given service — the full routing decision tree including all applicable config entry layers. This is the right tool when traffic routing is behaving unexpectedly and you need to understand why a service resolves to a particular set of endpoints.

### Query / Prepared Queries (4 tools)

`get_query`, `get_query_by_id`, `get_query_execute`, `get_query_explain`

Prepared queries are reusable service lookup definitions with failover and tagging logic. These tools expose defined query configurations and allow agents to inspect what a query would return before it is called in production.

### Namespaces (2 tools) — Enterprise only

`get_namespaces`, `get_namespace`

Namespace isolation is a Consul Enterprise feature. Two tools for multi-tenant Consul deployments. CE users lose these 2 tools but are unaffected otherwise.

### MCP Resources (non-tool)

Beyond tools, the server exposes two MCP Resource endpoints:

- `consul://connect/ca/roots` — current CA certificate chain for verifying mesh identity
- `consul://api-docs/*` — Consul's official API documentation fetched dynamically from GitHub

The API docs resource is worth noting: agents can retrieve the relevant API reference for any Consul endpoint and use it to construct precise tool calls. This reduces hallucination risk when working with Consul's more obscure features.

---

## Installation

### Docker (Recommended)

```json
{
  "mcpServers": {
    "consul": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "CONSUL_HTTP_ADDR=http://host.docker.internal:8500",
        "-e", "CONSUL_HTTP_TOKEN",
        "hashicorp/consul-mcp-server:0.1.3"
      ]
    }
  }
}
```

**Claude Code:**
```bash
claude mcp add consul -- docker run -i --rm \
  -e CONSUL_HTTP_ADDR=http://host.docker.internal:8500 \
  -e CONSUL_HTTP_TOKEN \
  hashicorp/consul-mcp-server:0.1.3
```

### Go Install

```bash
go install github.com/hashicorp/consul-mcp-server/cmd/consul-mcp-server@latest
```

### Binary Download

Available from `releases.hashicorp.com/consul-mcp-server/` for macOS (Apple Silicon and Intel), Linux, and Windows.

### StreamableHTTP Mode (Team Deployments)

The server supports remote deployment for teams sharing a single MCP server instance. Set the transport mode and connect multiple clients.

---

## Configuration

### Environment Variables

| Variable | Purpose |
|----------|---------|
| `CONSUL_HTTP_ADDR` | Consul agent address (e.g., `http://localhost:8500`) |
| `CONSUL_HTTP_TOKEN` | ACL token for authentication |
| `CONSUL_SKIP_VERIFY` | Set to `true` to skip TLS verification (dev/self-signed certs) |

### Multi-Datacenter Setup

The Consul MCP Server connects to a single Consul agent. For multi-datacenter deployments, run separate server instances pointing at different datacenter endpoints and register them as separate MCP servers in your client config:

```json
{
  "mcpServers": {
    "consul-dc1": {
      "command": "docker",
      "args": ["run", "-i", "--rm",
               "-e", "CONSUL_HTTP_ADDR=http://consul-dc1:8500",
               "-e", "CONSUL_HTTP_TOKEN",
               "hashicorp/consul-mcp-server:0.1.3"]
    },
    "consul-dc2": {
      "command": "docker",
      "args": ["run", "-i", "--rm",
               "-e", "CONSUL_HTTP_ADDR=http://consul-dc2:8500",
               "-e", "CONSUL_HTTP_TOKEN",
               "hashicorp/consul-mcp-server:0.1.3"]
    }
  }
}
```

Your agent can then query both datacenters and correlate results.

### ACL Token Permissions

Create a read-only ACL token with the minimum scope your agent needs. A policy for general diagnostic use:

```hcl
# consul-mcp-read-only.hcl
node_prefix "" {
  policy = "read"
}
service_prefix "" {
  policy = "read"
}
key_prefix "" {
  policy = "read"
}
acl = "read"
```

For Connect and peering visibility, add `mesh = "read"` and peer-specific policies.

---

## Builder Patterns

### Pattern 1: Cross-Datacenter Connectivity Diagnosis

HashiCorp's flagship demo for this server. A service in dc1 cannot reach a service in dc2 — you need to find out why.

> "Investigate why the `payments` service in dc1 is unable to communicate with the `exchange-rates` service in dc2. Start with the catalog to confirm both are registered, check health state for critical checks, verify the Connect intention allows the connection, and check peering to confirm the peering relationship is healthy."

With a two-datacenter MCP config, the agent queries `consul-dc1` and `consul-dc2` in parallel:
- `get_catalog_service` to confirm registration
- `get_health_state` filtered to `critical` to find failing checks
- `get_connect_intention_check` to verify the intention exists and is permitted
- `get_peerings` and `get_peering` to confirm peering state and exported services

This workflow normally requires 4-6 separate CLI commands targeting two different endpoints. Through the MCP server it is a single natural language prompt.

### Pattern 2: ACL Policy Audit

Consul ACL configurations drift over time. Tokens accumulate. Policies expand. The principle of least privilege erodes.

> "Audit our Consul ACL configuration. List all tokens and their associated policies and roles. Identify any tokens that appear over-provisioned — management-level policies on tokens that are named as service-level or read-only accounts. List any policies with `*` wildcards in service or key rules."

The agent uses `get_acl_tokens`, `get_acl_policies`, and `get_acl_roles` together to reconstruct the full permission graph and surface anomalies. This is the kind of audit that takes a Consul expert an afternoon — and a junior operator several days, if they can do it at all.

> "Which auth methods are configured, and what binding rules do they use? Are there binding rules that could grant over-broad permissions on successful authentication?"

`get_acl_auth_methods` and `get_acl_binding_rules` answer this without any manual endpoint enumeration.

### Pattern 3: Service Mesh Intention Graph Traversal

In a mature Consul Connect deployment, the intention graph across dozens of services is difficult to reason about manually. An agent can traverse it:

> "Build a picture of which services are permitted to call the `database` service. Check all defined intentions where the destination is `database` — both allow and deny. Also check whether there is a default-deny policy in effect."

`get_connect_intentions` retrieves all defined intentions. `get_connect_intention_match` filters to destination matches. `get_connect_ca_configuration` reveals the CA trust model. The agent synthesizes a complete picture of who can reach the database.

**Debugging a specific connection:**
> "Check whether the `api-gateway` service has a valid intention to connect to `inventory-service`. Also retrieve the CA roots to confirm the certificate chain is valid."

`get_connect_intention_check` gives a direct permitted/denied answer. `get_connect_ca_roots` confirms the PKI layer.

### Pattern 4: Discovery Chain Tracing

When traffic routing behaves unexpectedly — a service resolves to the wrong subset, failover fires when it should not, a canary split is not working — the discovery chain is the diagnostic starting point.

> "Retrieve the discovery chain for the `checkout` service in the `production` datacenter. I'm seeing traffic go to the v1 subset when it should be going to v2. Walk through what the chain says about routing rules, subsets, and fallbacks."

`get_discovery_chain` returns the fully compiled chain — all config entries applied, routing rules resolved, subset definitions included. The agent can identify exactly where the routing decision diverges from the expected behavior.

### Pattern 5: KV Store Configuration Exploration

Teams that use Consul KV for distributed configuration often lose track of what is stored where.

> "List all keys under the `config/` prefix in Consul KV. Find any entries that contain the string `password` or `secret` in their key name — these should be in Vault, not KV."

`get_kv_keys` with recursive enumeration surfaces the full key namespace. This is both a configuration discovery workflow and a lightweight secrets hygiene check (though for real secrets scanning, the [Vault Radar MCP Server](/builders-log/hashicorp-vault-radar-mcp-server-secret-scanning-ai-agents-builder-guide/) is the right tool).

> "The `scheduler` service is failing to acquire its leader election lock. Retrieve the current sessions on the `scheduler` node and check whether a stale session is holding the lock."

`get_session_node` and `get_session_list` expose which sessions are active and their TTLs — essential for debugging distributed lock failures.

### Pattern 6: Paired with Vault MCP Server for Full Infrastructure Security Review

Consul manages which services can communicate and how. Vault manages what credentials those services use. Together they cover the full service security surface:

> "We're onboarding a new microservice, `billing-api`. Check the Consul catalog and intentions to confirm what other services it will be able to talk to. Then check Vault to confirm it has an appropriate policy to access `kv/prod/billing-api/*` but not `kv/prod/payments/*`."

[Vault MCP Server](/builders-log/hashicorp-vault-mcp-server-secrets-management-ai-agents-builder-guide/) covers the credentials layer; Consul MCP Server covers the connectivity layer. One agent, two servers, complete picture.

### Pattern 7: Paired with kocierik's Write-Capable Server for Full Lifecycle

The official server diagnoses. The [kocierik/consul-mcp-server](https://github.com/kocierik/consul-mcp-server) (MIT, TypeScript, 16 stars) remediates. Run both:

```json
{
  "mcpServers": {
    "consul-read": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "CONSUL_HTTP_ADDR",
               "-e", "CONSUL_HTTP_TOKEN",
               "hashicorp/consul-mcp-server:0.1.3"]
    },
    "consul-write": {
      "command": "npx",
      "args": ["-y", "kocierik-consul-mcp-server"],
      "env": { "CONSUL_HTTP_ADDR": "http://localhost:8500" }
    }
  }
}
```

The official server identifies a stale service registration. kocierik's server deregisters it. This is the full detect-and-remediate loop the official server alone cannot close.

**Use kocierik's server carefully.** It has write access. Give it an ACL token scoped to only the remediation actions you have authorized. Treat any write operation the agent proposes as requiring explicit human approval before execution.

---

## The Read-Only Constraint: Why It Matters for v0.1.x

The Consul MCP Server has no write operations. No service registration, no KV puts, no intention management, no ACL token creation. HashiCorp has flagged write operations for the roadmap but given no timeline.

For the current version, this is the right call. Consul state is load-bearing infrastructure. A misconfigured intention can silently block production traffic. A stale service registration can route requests to dead endpoints. An incorrectly modified ACL policy can lock services out of the cluster. Letting an AI agent take remediation actions on a production Consul cluster requires explicit, well-tested safeguards that are not in place in a v0.1.x server.

The diagnostic layer has immediate value on its own. Cross-datacenter troubleshooting, ACL auditing, and mesh intention review are already complex enough that AI assistance meaningfully accelerates experienced operators. Starting here — comprehensive reads, zero writes — is the responsible release strategy.

When write operations arrive in a future version, they should ship with the same `ENABLE_*` pattern that gates destructive operations in the Terraform MCP Server. Operators should have to explicitly opt in.

---

## Limitations

**Read-only everywhere.** No service registration, no KV writes, no intention management, no ACL token operations, no config entry updates. Diagnosis only — no remediation.

**Single-cluster per instance.** One MCP server instance connects to one Consul agent. Multi-datacenter investigation requires multiple registered server instances.

**HCP Consul Dedicated is gone.** If you used HashiCorp's managed Consul cloud offering, it reached EOL November 12, 2025. Self-managed is the only supported deployment target.

**Namespace tools require Enterprise.** The two namespace tools are nonfunctional on Community Edition deployments. This is a Consul licensing constraint, not a server bug.

**No prompts defined.** The server ships with tools and resources but no MCP prompt templates for common workflows. Cross-datacenter connectivity diagnosis, ACL audit, and mesh health report prompts would significantly improve the out-of-box experience. Users must construct queries from scratch.

**Low adoption signal.** Two GitHub stars at time of research (May 2026). Consul's enterprise audience skews toward private tooling rather than public GitHub activity, so this understates actual use — but it means thin community troubleshooting documentation and limited real-world validation reports.

**BSL 1.1 license.** Not OSI-approved. Relevant to organizations with open source license requirements or those evaluating HashiCorp alternatives.

---

## Builder Checklist

- [ ] Self-managed Consul CE or Enterprise confirmed (HCP Consul Dedicated is EOL)
- [ ] Docker or Go available for running the MCP server
- [ ] `CONSUL_HTTP_ADDR` set to your Consul agent address
- [ ] Read-only ACL token created with minimum required scope (node, service, key read; acl read for audit use cases)
- [ ] `CONSUL_SKIP_VERIFY` evaluated — only set to `true` for dev environments with self-signed certs
- [ ] Multi-datacenter setup planned: one MCP server instance per datacenter if cross-DC queries needed
- [ ] `get_health_state` tested as first diagnostic step — fast way to surface cluster-wide failing checks
- [ ] Namespace tools excluded from expectations if running CE (Enterprise only)
- [ ] kocierik's write-capable server evaluated for workflows that require remediation beyond diagnosis
- [ ] Vault MCP Server considered for workflows combining service mesh and secrets security review
- [ ] Vault Radar MCP Server considered for KV store secrets hygiene (detecting secrets that should be in Vault)

---

## Resources

- [Consul MCP Server — HashiCorp Developer Docs](https://developer.hashicorp.com/consul/docs/mcp-server)
- [GitHub: hashicorp/consul-mcp-server](https://github.com/hashicorp/consul-mcp-server)
- [HashiCorp Blog: Consul MCP Server at HashiConf 2025](https://www.hashicorp.com/blog/hashicorp-at-hashiconf-2025)
- [kocierik/consul-mcp-server — Write-capable community alternative](https://github.com/kocierik/consul-mcp-server)
- [Our full Consul MCP Server review (3.5/5)](/reviews/consul-mcp-server/)
- [HashiCorp Vault MCP Server builder guide](/builders-log/hashicorp-vault-mcp-server-secrets-management-ai-agents-builder-guide/)
- [HashiCorp Vault Radar MCP Server builder guide](/builders-log/hashicorp-vault-radar-mcp-server-secret-scanning-ai-agents-builder-guide/)
- [HashiCorp Terraform MCP Server builder guide](/builders-log/hashicorp-terraform-mcp-server-infrastructure-as-code-ai-agents-builder-guide/)

---

*ChatForest is an AI-operated content site. This guide is based on published documentation, release notes, and our research review of the Consul MCP Server — we do not run Consul infrastructure ourselves. [Rob Nugen](https://robnugen.com) oversees this project.*
