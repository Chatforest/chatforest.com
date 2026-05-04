---
title: "The HashiCorp Consul MCP Server — Service Discovery, KV Store, and Mesh Diagnostics for AI Agents"
date: 2026-05-05T12:00:00+09:00
description: "HashiCorp's official Consul MCP server exposes 50+ read-only tools across 15 toolsets covering service discovery, KV store, ACLs, Connect service mesh, sessions, peering, and cluster operations. Works with self-managed Consul CE and Enterprise."
og_description: "HashiCorp's official Consul MCP server: 50+ tools across 15 toolsets — service catalog, health, KV store, ACL management, Connect mesh, sessions, peering, operator tools, prepared queries, namespaces. Read-only. Self-managed Consul CE and Enterprise. BSL 1.1 license. v0.1.3. Rating: 3.5/5."
content_type: "Review"
card_description: "HashiCorp's official Consul MCP server gives AI agents comprehensive read-only access to Consul's full platform: service discovery, health monitoring, KV store exploration, ACL auditing, Connect service mesh, sessions, peering, and cluster operations — across 15 toolsets and 50+ tools. Works with self-managed Consul CE and Enterprise. Read-only for now, with write operations on the roadmap. BSL 1.1 license. v0.1.3 (October 2025)."
last_refreshed: 2026-05-05
---

Part of our **[Service Mesh & Network Infrastructure MCP Servers roundup](/reviews/service-mesh-network-infrastructure-mcp-servers/)**.

**At a glance:** 2 GitHub stars, Go, BSL 1.1 license. v0.1.3 (October 1, 2025). Available as binary download, Go install, or Docker image. Announced September 25, 2025 at HashiConf.

HashiCorp Consul manages service discovery, service mesh, distributed configuration, and access control across enterprise infrastructure at companies like Expedia and Workday. Its HTTP API is comprehensive but complex: querying cross-datacenter health, understanding service intention graphs, auditing ACL token permissions, and tracing discovery chains all require knowing specific endpoints and parameter combinations. The Consul MCP server brings all of that under an AI interface — letting agents and developers query Consul's full observability surface in plain English.

The server launched at HashiConf in September 2025 as part of HashiCorp's broader MCP strategy — they also shipped Terraform and Vault MCP servers the same year. It's 100% official, maintained by the Consul engineering team, and covers 15 toolsets with 50+ tools. The defining constraint: everything is read-only. You can diagnose but not remediate — no service registration, no KV writes, no intention management, no ACL token creation. HashiCorp has flagged write operations as a future roadmap item.

Note: HCP Consul Dedicated reached end-of-life November 12, 2025. This server targets self-managed Consul deployments — CE (Community Edition) or Enterprise.

## What It Does

The server organizes tools into 15 named toolsets. All operations are read-only (GET).

### Catalog (7 tools)

| Tool | Purpose |
|------|---------|
| `get_catalog_services` | List all registered services |
| `get_catalog_nodes` | List all registered nodes |
| `get_catalog_service` | Get details for a specific service |
| `get_catalog_connect` | List Connect-capable services |
| `get_catalog_node` | Get details for a specific node |
| `get_catalog_datacenters` | List all known datacenters |
| `get_catalog_gateway_services` | List services behind a gateway |

Service discovery is Consul's original purpose. These tools let agents query what's registered, where, and in which datacenter — the foundation for cross-datacenter troubleshooting.

### Health (6 tools)

`get_health_node`, `get_health_checks`, `get_health_service`, `get_health_connect`, `get_health_ingress`, `get_health_state`

Health check queries across nodes, services, and mesh connections. `get_health_state` returns all checks in a given state (passing, warning, critical) — a fast way for an agent to surface what's currently unhealthy.

### Key-Value Store (3 tools)

`get_kv`, `get_kv_keys`, `get_kv_recursive`

Consul KV is widely used as a distributed configuration store. These three tools cover single-key lookup, listing keys under a prefix, and recursive enumeration. Teams that store application configuration, feature flags, or distributed locks in Consul KV can query the entire structure through natural language.

### ACL (6 tools)

| Tool | Purpose |
|------|---------|
| `get_acl_tokens` | List all ACL tokens |
| `get_acl_policies` | List all ACL policies |
| `get_acl_roles` | List all ACL roles |
| `get_acl_auth_methods` | List configured auth methods |
| `get_acl_binding_rules` | List ACL binding rules |
| `get_acl_templated_policies` | List templated policy definitions |

ACL policy auditing is one of the strongest use cases for this server. Consul ACL configurations are notoriously complex — token permission scopes, policy inheritance, and role-based access layers combine into configurations that are hard to reason about manually. An AI agent with these tools can answer questions like "Is this token over-privileged for KV read-only operations?" or "Which tokens have write access to the services namespace?"

### Connect / Service Mesh (6 tools)

`get_connect_ca_roots`, `get_connect_ca_configuration`, `get_connect_intentions`, `get_connect_intention`, `get_connect_intention_match`, `get_connect_intention_check`

Six tools for Consul Connect, the service mesh layer that manages mTLS between services. CA root inspection, intention listing, and intention match/check queries give agents visibility into the mesh trust model. Asking "Does service A have an intention allowing it to call service B?" is the kind of mesh question that typically requires CLI gymnastics — here it's a natural language query.

### Agent (7 tools)

`get_agent_self`, `get_agent_config`, `get_agent_members`, `get_agent_metrics`, `get_agent_host`, `get_agent_version`, `get_agent_reload`

Agent-level diagnostics: cluster members, agent configuration, runtime metrics, host information, and version details. Useful for health checks on the Consul agent itself rather than the services it tracks.

### Operator (4 tools)

Autopilot configuration, keyring management, license information, and Raft consensus state. For platform teams managing Consul clusters, the Raft tools are particularly useful for diagnosing split-brain scenarios or leader election issues.

### Session (3 tools)

`get_session`, `get_session_node`, `get_session_list`

Consul sessions are the foundation for distributed locking. These tools expose current session state — which nodes hold sessions, what locks are active, session TTLs. Useful for debugging distributed systems that rely on Consul for leader election.

### Status (2 tools)

`get_status_leader`, `get_status_peers`

Cluster status: who is the current Raft leader, and who are the voting peers. Quick operational checks.

### Peering (3 tools)

`get_peerings`, `get_peering`, `get_peering_exported_services`

Consul Cluster Peering enables service discovery across administrative boundaries (different Consul clusters, different cloud accounts). These tools expose peering relationships and which services are exported across them — critical for multi-cluster and multi-cloud architectures.

### Config Entries (2 tools)

`get_config_entries`, `get_config_entry`

Configuration entries define mesh-wide behavior — service defaults, proxy defaults, ingress gateways, terminating gateways, mesh policies. Query what's defined and its current values.

### Discovery Chain (1 tool)

`get_discovery_chain` — retrieves the compiled service discovery chain, showing how traffic is routed for a given service including all applicable config entry layers. Useful for diagnosing why traffic isn't routing as expected.

### Query / Prepared Queries (3 tools)

`get_query`, `get_query_by_id`, `get_query_execute`, `get_query_explain`

Consul prepared queries are reusable service lookup definitions with failover and tagging logic. These tools let agents inspect and execute defined queries.

### Namespaces (2 tools) — Enterprise only

`get_namespaces`, `get_namespace`

Namespace isolation requires Consul Enterprise. Two tools for listing and inspecting namespace definitions.

### MCP Resources (non-tool)

Beyond tools, the server exposes two MCP Resource endpoints:

- `consul://connect/ca/roots` — the current CA certificate chain, for verifying mesh identity
- `consul://api-docs/*` — dynamic access to Consul's official API documentation fetched from GitHub

The API docs resource is particularly useful for building complex queries — an agent can retrieve the relevant API reference and use it to construct precise tool calls.

---

**Total: 50+ tools across 15 toolsets.** All read-only.

## Setup

**Binary download** from HashiCorp releases:

```bash
# Download from releases.hashicorp.com/consul-mcp-server/
# Available for macOS (Apple Silicon / Intel), Linux, and Windows
```

**Go install:**

```bash
go install github.com/hashicorp/consul-mcp-server/cmd/consul-mcp-server@latest
```

**Docker:**

```bash
docker run -i --rm \
  -e CONSUL_HTTP_ADDR=http://host.docker.internal:8500 \
  hashicorp/consul-mcp-server
```

**MCP client config** (Claude Code, Claude Desktop, Cursor, VS Code):

```json
{
  "mcpServers": {
    "consul": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "CONSUL_HTTP_ADDR=http://host.docker.internal:8500",
        "hashicorp/consul-mcp-server"
      ]
    }
  }
}
```

**Environment variables:**

| Variable | Purpose |
|----------|---------|
| `CONSUL_HTTP_ADDR` | Consul agent address (e.g., `http://localhost:8500`) |
| `CONSUL_HTTP_TOKEN` | ACL token for authentication |
| `CONSUL_SKIP_VERIFY` | Set to `true` to skip TLS verification (dev/self-signed) |

No API key provisioning process, no cloud account — point it at your Consul cluster, provide an ACL token with appropriate read permissions, and connect. For **multi-datacenter** setups, run separate MCP server instances pointing at different datacenter addresses, then connect multiple MCP servers in your client configuration.

Consul CE and Enterprise both work. v0.1.3 fixed a CE compatibility bug present in earlier releases — use v0.1.3 or later with Community Edition.

## What's Good

**Official HashiCorp server with full platform coverage.** This isn't a community experiment — it's from the team that builds Consul. The 15-toolset coverage maps directly to Consul's actual API surface: catalog, health, KV, ACL, Connect, agent, operator, sessions, status, peering, config entries, discovery chain, prepared queries, namespaces, and MCP resources. Other MCP servers typically cherry-pick 5-10 endpoints; this one covers the whole platform.

**Works with self-managed Consul everywhere.** Point `CONSUL_HTTP_ADDR` at any accessible Consul cluster — on-premise, Kubernetes, cloud VMs, Docker — and it works. No cloud account required, no vendor lock-in path. The v0.1.3 CE fix means Community Edition users are equally well-served as Enterprise users.

**Dual transport support.** stdio (for local use with Claude Desktop and Claude Code) and StreamableHTTP (for remote/server-side deployment) are both supported. This covers the full range of deployment patterns from individual developer workstations to centralized MCP server infrastructure.

**ACL security auditing is genuinely useful.** Consul ACL configurations accrete complexity over time — tokens proliferate, policies overlap, roles inherit from roles. Having an AI agent reason over your entire token and policy set against least-privilege principles is a meaningful capability for security audits and compliance reviews.

**Cross-datacenter troubleshooting.** HashiCorp's own demo scenario captures the value: "Investigate why service-hello in dc1 is unable to communicate with service-response in dc2?" — a query that spans catalog, health, Connect intentions, and peering state across multiple datacenters. Answering this manually requires CLI commands against multiple endpoints. Through the MCP server and a multi-datacenter configuration, it's a single natural language question.

**API docs resource is a smart addition.** The `consul://api-docs/*` resource gives agents access to Consul's reference documentation on demand. This helps agents construct accurate queries without hallucinating API behavior — an underappreciated safety improvement.

**KV store exploration without CLI.** Consul KV stores application configuration, feature flags, and distributed lock state across many organizations. The recursive enumeration tool (`get_kv_recursive`) lets agents explore the entire KV namespace and reason about configuration values — useful for debugging misconfigured applications.

## What's Not

**Read-only is the fundamental constraint.** You cannot register services, deregister nodes, write KV values, create or update intentions, manage ACL tokens, modify config entries, or change any Consul state. The server is entirely diagnostic. HashiCorp has acknowledged write operations as a future roadmap item — the blog post frames it as "foundational work" — but there's no timeline. For teams that want AI agents to take remediation actions (registering a replacement service, updating a failed intention, cleaning up stale sessions), this server doesn't yet deliver.

**2 GitHub stars at time of research.** Announced at HashiConf in September 2025, but adoption is essentially zero outside of early evaluators. This is partly a reflection of Consul's enterprise audience (less active on GitHub than startup ecosystems) and partly a sign that the MCP ecosystem hasn't widely discovered this server yet. Low stars mean thin community documentation, few troubleshooting reports, and limited real-world validation.

**BSL 1.1 license.** HashiCorp changed Consul's license from MPL to Business Source License 1.1 in August 2023 — this server inherits the same licensing. BSL is not open source: it restricts production use by "competitors" and grants a time-delayed conversion to Apache 2.0 (four years after each release). For most users this is irrelevant, but organizations that require OSI-approved open source licenses — or that are evaluating HashiCorp alternatives like OpenTofu — will note it.

**No write operations means no automation workflows.** The most compelling use of AI agents in infrastructure is the ability to detect an issue and remediate it in one loop. The Consul MCP server supports the detection half but not the remediation half. An agent can tell you which services have failing health checks and diagnose why — but it can't deregister a stale service entry, update a misconfigured intention, or rotate a compromised ACL token.

**No prompts defined.** The server ships with tools and resources but no MCP prompt templates. Users must construct their own queries from scratch. Purpose-built prompts for common scenarios (service mesh health report, ACL audit, cross-datacenter connectivity diagnosis) would dramatically improve the out-of-box experience.

**HCP Consul Dedicated is dead.** If you were using HCP Consul Dedicated (HashiCorp's managed Consul cloud offering), it reached EOL on November 12, 2025. There is no HCP replacement to point this server at. Self-managed is the only path.

**Enterprise namespace tools require Consul Enterprise.** The namespace toolset is useful for multi-tenant Consul deployments but requires a paid Consul Enterprise license. Community Edition users lose these 2 tools.

## Community Alternatives

Three community Consul MCP servers predate or complement the official server:

| Server | Stars | Language | License | Key Differentiator |
|--------|-------|----------|---------|-------------------|
| [kocierik/consul-mcp-server](https://github.com/kocierik/consul-mcp-server) | 16 | TypeScript | MIT | **Write operations** — service registration, KV put/delete, session management |
| [3loka/consul-mcp-server](https://github.com/3loka/consul-mcp-server) | 2 | TypeScript | MIT | **Service diagram generation** — visual service connection maps |
| [kswap/consul-mcp](https://github.com/kswap/consul-mcp) | 0 | Python | unspecified | Minimal; natural language service discovery |

**kocierik's server** (16 stars, on PulseMCP) is the most important alternative — it's the only Consul MCP server that supports write operations. Service registration and deregistration, KV store put and delete, session creation, and event publishing are all available. The tradeoff: narrower read coverage than the official server. If your use case requires AI-assisted Consul management rather than pure diagnostics, kocierik's MIT-licensed server fills the gap the official server leaves.

**3loka's server** is interesting for a different reason — it generates service mesh architecture diagrams, creating visual maps of service connections. This observability angle (understanding *how* services connect visually) complements the official server's operational diagnostic focus.

## How It Compares to the HashiCorp Vault MCP Server

HashiCorp shipped both a Consul MCP server and a Vault MCP server in 2025. The pattern is similar: official, Go, BSL 1.1, read-oriented diagnostic tooling, comprehensive platform coverage. Consul's server covers service mesh and discovery infrastructure; Vault's covers secrets management. If you're already using one, the other follows the same conventions and deployment model.

The broader HashiCorp MCP pattern — comprehensive official coverage, BSL license, read-only in v0.1.x, write operations on roadmap — suggests this is a deliberate strategy for the HashiCorp product suite. Terraform's MCP server follows the same arc.

## The Bigger Picture

Consul sits at one of the most critical intersection points in enterprise infrastructure: it controls which services can talk to which other services, stores distributed configuration, and enforces security through ACLs and mTLS. Getting these configurations right across dozens of services and multiple datacenters is hard; debugging them when something goes wrong is harder.

The MCP server's value proposition is clearest for platform engineering and SRE teams managing complex Consul deployments. Cross-datacenter service health diagnosis, ACL policy auditing, service mesh intention review, and KV configuration exploration — these are the everyday tasks that require deep Consul CLI knowledge and context-switching between multiple endpoints. Having an AI agent that can query the full Consul API surface in natural language genuinely accelerates this work.

The read-only constraint is real, but it's the right constraint for v0.1.x. Consul state is sensitive — unintended service deregistrations, ACL token deletions, or intention changes can disrupt production traffic. Starting with a comprehensive diagnostic layer and adding write operations incrementally (with appropriate safeguards) is the responsible approach.

For teams already running Consul, this server deserves evaluation now. The setup is lightweight (Docker or a single binary), the breadth is genuinely comprehensive, and the diagnostic use cases are immediately applicable. The 2 GitHub stars reflect early awareness, not actual utility — this is a case where the official stamp and platform coverage matter more than the adoption signal.

## Rating: 3.5/5

The HashiCorp Consul MCP server earns 3.5/5 for delivering comprehensive, official coverage of Consul's full platform across 15 toolsets and 50+ tools — with dual transport support, CE/Enterprise compatibility, and multi-datacenter capability. For platform engineering and SRE teams running Consul, it's a genuinely useful diagnostic layer that makes cross-datacenter troubleshooting, ACL auditing, and service mesh inspection conversationally accessible.

The rating is held back by the read-only constraint (which limits use to diagnostics, not remediation), minimal adoption signal (2 stars), BSL 1.1 licensing, and the absence of write operations that would unlock automation workflows. The community kocierik server (MIT, write-capable) fills the write gap for teams that need it.

**Use this if:** You run self-managed Consul (CE or Enterprise) and want AI-assisted service catalog queries, health diagnostics, KV exploration, ACL auditing, Connect intention review, or cross-datacenter troubleshooting. The diagnostic depth across all 15 toolsets is unmatched.

**Skip this if:** You need write operations (use kocierik's MIT-licensed alternative), your organization requires OSI-approved open source licenses, you used HCP Consul Dedicated (EOL — you'll need to migrate first), or you need AI agents that can remediate Consul issues rather than just diagnose them.

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) and has not been independently verified by a human editor. We have not tested this MCP server hands-on. All claims are based on publicly available documentation, GitHub data, and community sources as of May 2026. [Rob Nugen](https://robnugen.com) oversees this project.*
