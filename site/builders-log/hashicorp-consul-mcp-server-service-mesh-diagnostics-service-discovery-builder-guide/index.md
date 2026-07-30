# HashiCorp Consul MCP Server: Service Mesh Diagnostics and Service Discovery for AI Agents (Builder Guide)

> HashiCorp's official Consul MCP Server gives AI agents 85 read-only tools across 15 toolsets — service catalog queries, health diagnostics, ACL auditing, Connect mesh inspection, and cross-datacenter troubleshooting. Here is what builders need to wire it in.


Debugging a Consul deployment manually means knowing which CLI command retrieves health state versus catalog state, how to cross-correlate intentions against service identity, which datacenter endpoint to query for a given service, and when to reach for the API versus the UI. For teams running Consul across multiple datacenters and hundreds of services, this expertise is both deep and rare.

HashiCorp's official Consul MCP Server ([v0.1.3, released September 26, 2025](https://github.com/hashicorp/consul-mcp-server/blob/main/CHANGELOG.md)) makes that knowledge callable. Its [source registers 85 read-only tools across 15 toolsets](https://github.com/hashicorp/consul-mcp-server/blob/main/pkg/tools/tools.go) — service catalog, health checks, KV store, ACL policies, Connect mesh, sessions, peering, discovery chains, prepared queries, namespaces — all accessible through natural language from any MCP-compatible agent.

It does not write anything. That constraint is worth understanding before you reach for it.

---

## What the Consul MCP Server Is

The Consul MCP Server is an official HashiCorp server that translates MCP tool calls into Consul HTTP API requests. It [launched at HashiConf on September 25, 2025](https://www.hashicorp.com/en/blog/consul-1-22-and-mcp-server-add-better-security-telemetry-and-ux), the same event where HashiCorp's [Terraform, Vault, and HCP Vault Radar MCP servers](https://www.hashicorp.com/en/blog/10-years-of-hashiconf-a-bold-leap-into-ai-powered-infrastructure) had already shipped.

It connects to any self-managed Consul cluster — Community Edition or Enterprise — via the standard HTTP API. No special Consul configuration required. Point `CONSUL_HTTP_ADDR` at your cluster, provide an ACL token with appropriate read permissions, and it works.

**Transport:** stdio (local use with Claude Desktop, Claude Code, Cursor) and StreamableHTTP (remote/shared deployment). Both are supported from the same binary.

**License:** [BSL 1.1](https://github.com/hashicorp/consul-mcp-server/blob/main/LICENSE). Same license [HashiCorp adopted for Consul and its other products in August 2023](https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license). Not OSI-approved open source.

**HCP Consul Dedicated:** [Reached end-of-life November 12, 2025](https://support.hashicorp.com/hc/en-us/articles/46472870055571-End-of-Life-Notice-for-HCP-Consul-Dedicated). This server targets self-managed Consul only.

---

## The Problem: Consul's API Surface Is Too Wide for Manual Navigation

[Consul's HTTP API](https://developer.hashicorp.com/consul/api-docs) spans a wide set of functional areas — service catalog, health, ACL, Connect, key-value, sessions, operator, and more. A developer debugging why two services cannot communicate through the mesh needs to query:

- The service catalog to confirm both are registered and which nodes they appear on
- Health checks to confirm both are passing
- ACL to check whether an intention exists allowing the connection
- Connect CA to confirm the certificate chain is valid
- The discovery chain to see whether traffic routing rules are interfering

That is five separate query domains, each with its own endpoint patterns and parameter conventions. For an SRE on call at 2 AM in an unfamiliar Consul deployment, it is genuinely hard.

An AI agent with the Consul MCP Server can traverse all five of those domains in a single natural language prompt. The agent knows which tools to call, in what order, and how to correlate the results.

---

## Architecture: 15 Toolsets, 85 Tools

The [Consul MCP Server's source](https://github.com/hashicorp/consul-mcp-server/blob/main/pkg/tools/tools.go) organizes its tools into 15 named toolsets, matching the toolset breakdown in [the project README](https://github.com/hashicorp/consul-mcp-server/blob/main/README.md#available-toolsets). Every tool is read-only (HTTP GET). Tool names below are the actual registered MCP tool names (verified against source), not the `get_`-prefixed names shown in HashiCorp's own README table — the README table's naming does not match what the server actually exposes.

### Catalog (7 tools)

Service registration and discovery — Consul's original purpose.

| Tool | Purpose |
|------|---------|
| `catalog_services` | List all registered services |
| `catalog_nodes` | List all registered nodes |
| `catalog_service` | Details for a specific service (all nodes) |
| `catalog_connect` | List Connect-capable services |
| `catalog_node` | Details for a specific node (all services) |
| `catalog_datacenters` | List all known datacenters |
| `catalog_gateway_services` | Services behind a gateway |

### Health (6 tools)

`health_node`, `health_checks`, `health_service`, `health_connect`, `health_ingress`, `health_state`

`health_state` is particularly useful for agents: it returns all checks in a given state (passing, warning, critical) across the cluster — a fast first step in any incident investigation.

### Key-Value Store (3 tools)

`kv_get`, `kv_keys`, `kv_recursive`

Consul KV stores application configuration, feature flags, and distributed lock state in many organizations. `kv_recursive` enumerates an entire namespace prefix — useful for agents reasoning about configuration sprawl or debugging misconfigured applications.

### ACL (13 tools)

| Tool | Purpose |
|------|---------|
| `acl_tokens` / `acl_token` / `acl_token_self` | List all tokens, fetch one token, or fetch the token tied to the calling credential |
| `acl_policies` / `acl_policy` | List all policies, or fetch one policy |
| `acl_roles` / `acl_role` | List all roles, or fetch one role |
| `acl_auth_methods` / `acl_auth_method` | List configured authentication methods, or fetch one |
| `acl_binding_rules` / `acl_binding_rule` | List ACL binding rules, or fetch one |
| `acl_templated_policies` / `acl_templated_policy` | List templated policy definitions, or fetch one |

This is one of the server's strongest use cases. Consul ACL configurations accumulate complexity — tokens proliferate, policies overlap, roles inherit from roles. The [13 ACL tools](https://github.com/hashicorp/consul-mcp-server/tree/main/pkg/tools/functions) together give an agent enough context to reason about privilege scope, token over-provisioning, and auth method coverage across the cluster.

### Connect / Service Mesh (6 tools)

`connect_ca_roots`, `connect_ca_configuration`, `connect_intentions`, `connect_intention`, `connect_intention_match`, `connect_intention_check`

Consul Connect manages mTLS between services. These six tools expose the trust model: CA root inspection, intention listing and matching, and explicit intention checks. "Does service A have an intention allowing it to call service B?" is a question that takes 30 seconds to answer through the MCP server and 5 minutes of CLI work to answer manually.

### Agent (20 tools)

Agent-level diagnostics rather than service-level, split across four groups in [the source](https://github.com/hashicorp/consul-mcp-server/tree/main/pkg/tools/functions):

- **Overview (7):** `agent_self`, `agent_config`, `agent_members`, `agent_metrics`, `agent_host`, `agent_version`, `agent_reload`
- **Checks (5):** `agent_checks`, `agent_check`, `agent_check_by_name`, `agent_service_health`, `agent_service_health_by_name`
- **Services (4):** `agent_services`, `agent_service`, `agent_service_configuration`, `agent_service_local_state`
- **Connect (4):** `agent_connect_ca`, `agent_connect_authorize`, `agent_connect_proxy_config`, `agent_connect_leaf_cert`

Useful for verifying cluster membership, agent configuration, and runtime metrics when the Consul agent itself — rather than a service it hosts — is suspected.

### Operator (11 tools)

Autopilot configuration, keyring management, license information, network area (segment) membership, and Raft consensus state, per [the source](https://github.com/hashicorp/consul-mcp-server/blob/main/pkg/tools/functions/operator-raft.go):

- **Raft (1):** `operator_raft_configuration`
- **Autopilot (3):** `operator_autopilot_configuration`, `operator_autopilot_health`, `operator_autopilot_state`
- **Network areas (3):** `operator_areas`, `operator_area`, `operator_area_members`
- **Keyring (1):** `operator_keyring`
- **License (1):** `operator_license`
- **Network segments (1):** `operator_segment`
- **Usage (1):** `operator_usage`

`operator_raft_configuration` and `operator_autopilot_state` are valuable for diagnosing split-brain scenarios and leader election issues — edge cases where the Consul cluster itself needs investigation rather than the services it manages.

### Session (3 tools)

`session`, `session_node`, `session_list`

Consul sessions underpin distributed locking (leader election, distributed locks for job scheduling). These tools expose current session state — which nodes hold sessions, what locks are active, TTLs. Essential for debugging distributed systems that use Consul for leader election.

### Status (2 tools)

`status_leader`, `status_peers`

Cluster status: current Raft leader and voting peers. Quick operational health check.

### Peering (3 tools)

`peerings`, `peering`, `peering_exported_services`

Consul Cluster Peering connects service discovery across administrative boundaries — different clusters, cloud accounts, or regions. These three tools expose peering relationships and which services are exported across them. Critical for multi-cluster and multi-cloud architectures where cross-cluster service visibility fails.

### Config Entries (3 tools)

`config_entries`, `config_entry`, `config_kinds`

Config entries define mesh-wide behavior: service defaults, proxy defaults, ingress gateways, terminating gateways, mesh policies. These tools let agents list the available config-entry kinds and inspect what mesh-level configuration is active and its current values.

### Discovery Chain (1 tool)

`discovery_chain` retrieves the compiled service discovery chain for a given service — the full routing decision tree including all applicable config entry layers. This is the right tool when traffic routing is behaving unexpectedly and you need to understand why a service resolves to a particular set of endpoints.

### Query / Prepared Queries (4 tools)

`query`, `query_by_id`, `query_execute`, `query_explain`

Prepared queries are reusable service lookup definitions with failover and tagging logic. These tools expose defined query configurations and allow agents to inspect what a query would return before it is called in production.

### Namespaces (2 tools) — Enterprise only

`namespaces`, `namespace`

Namespace isolation is a Consul Enterprise feature. Two tools for multi-tenant Consul deployments. CE users lose these 2 tools but are unaffected otherwise.

### Identity (1 tool)

[`cluster_identity`](https://github.com/hashicorp/consul-mcp-server/blob/main/pkg/tools/functions/identity.go) returns the cluster's identity information — a single tool, its own toolset, and the one most guides (including HashiCorp's own README table) leave out of the toolset list entirely.

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

[HashiCorp's own launch post uses this exact scenario](https://www.hashicorp.com/en/blog/consul-1-22-and-mcp-server-add-better-security-telemetry-and-ux) as its example: "a platform engineer can ask, 'Investigate why `service-hello` in dc1 is unable to communicate with `service-response` in dc2?'" A service in one datacenter cannot reach a service in another — you need to find out why.

> "Investigate why the `service-hello` service in dc1 is unable to communicate with the `service-response` service in dc2. Start with the catalog to confirm both are registered, check health state for critical checks, verify the Connect intention allows the connection, and check peering to confirm the peering relationship is healthy."

With a two-datacenter MCP config, the agent queries `consul-dc1` and `consul-dc2` in parallel:
- `catalog_service` to confirm registration
- `health_state` filtered to `critical` to find failing checks
- `connect_intention_check` to verify the intention exists and is permitted
- `peerings` and `peering` to confirm peering state and exported services

This workflow normally requires 4-6 separate CLI commands targeting two different endpoints. Through the MCP server it is a single natural language prompt.

### Pattern 2: ACL Policy Audit

Consul ACL configurations drift over time. Tokens accumulate. Policies expand. The principle of least privilege erodes.

> "Audit our Consul ACL configuration. List all tokens and their associated policies and roles. Identify any tokens that appear over-provisioned — management-level policies on tokens that are named as service-level or read-only accounts. List any policies with `*` wildcards in service or key rules."

The agent uses `acl_tokens`, `acl_policies`, and `acl_roles` together to reconstruct the full permission graph and surface anomalies. This is the kind of audit that takes a Consul expert an afternoon — and a junior operator several days, if they can do it at all.

> "Which auth methods are configured, and what binding rules do they use? Are there binding rules that could grant over-broad permissions on successful authentication?"

`acl_auth_methods` and `acl_binding_rules` answer this without any manual endpoint enumeration.

### Pattern 3: Service Mesh Intention Graph Traversal

In a mature Consul Connect deployment, the intention graph across dozens of services is difficult to reason about manually. An agent can traverse it:

> "Build a picture of which services are permitted to call the `database` service. Check all defined intentions where the destination is `database` — both allow and deny. Also check whether there is a default-deny policy in effect."

`connect_intentions` retrieves all defined intentions. `connect_intention_match` filters to destination matches. `connect_ca_configuration` reveals the CA trust model. The agent synthesizes a complete picture of who can reach the database.

**Debugging a specific connection:**
> "Check whether the `api-gateway` service has a valid intention to connect to `inventory-service`. Also retrieve the CA roots to confirm the certificate chain is valid."

`connect_intention_check` gives a direct permitted/denied answer. `connect_ca_roots` confirms the PKI layer.

### Pattern 4: Discovery Chain Tracing

When traffic routing behaves unexpectedly — a service resolves to the wrong subset, failover fires when it should not, a canary split is not working — the discovery chain is the diagnostic starting point.

> "Retrieve the discovery chain for the `checkout` service in the `production` datacenter. I'm seeing traffic go to the v1 subset when it should be going to v2. Walk through what the chain says about routing rules, subsets, and fallbacks."

`discovery_chain` returns the fully compiled chain — all config entries applied, routing rules resolved, subset definitions included. The agent can identify exactly where the routing decision diverges from the expected behavior.

### Pattern 5: KV Store Configuration Exploration

Teams that use Consul KV for distributed configuration often lose track of what is stored where.

> "List all keys under the `config/` prefix in Consul KV. Find any entries that contain the string `password` or `secret` in their key name — these should be in Vault, not KV."

`kv_keys` with recursive enumeration surfaces the full key namespace. This is both a configuration discovery workflow and a lightweight secrets hygiene check (though for real secrets scanning, the [Vault Radar MCP Server](/builders-log/hashicorp-vault-radar-mcp-server-secret-scanning-ai-agents-builder-guide/) is the right tool).

> "The `scheduler` service is failing to acquire its leader election lock. Retrieve the current sessions on the `scheduler` node and check whether a stale session is holding the lock."

`session_node` and `session_list` expose which sessions are active and their TTLs — essential for debugging distributed lock failures.

### Pattern 6: Paired with Vault MCP Server for Full Infrastructure Security Review

Consul manages which services can communicate and how. Vault manages what credentials those services use. Together they cover the full service security surface:

> "We're onboarding a new microservice, `billing-api`. Check the Consul catalog and intentions to confirm what other services it will be able to talk to. Then check Vault to confirm it has an appropriate policy to access `kv/prod/billing-api/*` but not `kv/prod/payments/*`."

[Vault MCP Server](/builders-log/hashicorp-vault-mcp-server-secrets-management-ai-agents-builder-guide/) covers the credentials layer; Consul MCP Server covers the connectivity layer. One agent, two servers, complete picture.

### Pattern 7: Paired with kocierik's Write-Capable Server for Full Lifecycle

The official server diagnoses. The [kocierik/consul-mcp-server](https://github.com/kocierik/consul-mcp-server) (MIT, TypeScript, 16 stars) remediates. Its [README documents no `npm`/`npx` published package](https://github.com/kocierik/consul-mcp-server/blob/main/README.md) — you clone the repo, `npm install && npm run build`, and point a `node` command at the built `index.js`, or install through [Smithery](https://smithery.ai/server/@kocierik/consul-mcp-server). It also [reads only `CONSUL_HOST` / `CONSUL_PORT`](https://github.com/kocierik/consul-mcp-server/blob/main/src/server.ts) — not `CONSUL_HTTP_ADDR`, and it has no built-in support for a Consul ACL token. Run both:

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
      "command": "node",
      "args": ["/ABSOLUTE/PATH/TO/consul-mcp-server/build/index.js"],
      "env": { "CONSUL_HOST": "localhost", "CONSUL_PORT": "8500" }
    }
  }
}
```

The official server identifies a stale service registration. kocierik's server deregisters it. This is the full detect-and-remediate loop the official server alone cannot close.

**Use kocierik's server carefully.** It has write access, and because it has no built-in ACL token support, anything it can reach it can write to — restrict it at the network/agent level (a Consul agent with ACLs enforced and default-deny, reachable only from where this server runs) rather than assuming a scoped credential will contain it. Treat any write operation the agent proposes as requiring explicit human approval before execution.

---

## The Read-Only Constraint: Why It Matters for v0.1.x

The Consul MCP Server has no write operations. No service registration, no KV puts, no intention management, no ACL token creation. HashiCorp has flagged write operations for the roadmap but given no timeline.

For the current version, this is the right call. Consul state is load-bearing infrastructure. A misconfigured intention can silently block production traffic. A stale service registration can route requests to dead endpoints. An incorrectly modified ACL policy can lock services out of the cluster. Letting an AI agent take remediation actions on a production Consul cluster requires explicit, well-tested safeguards that are not in place in a v0.1.x server.

The diagnostic layer has immediate value on its own. Cross-datacenter troubleshooting, ACL auditing, and mesh intention review are already complex enough that AI assistance meaningfully accelerates experienced operators. Starting here — comprehensive reads, zero writes — is the responsible release strategy.

When write operations arrive in a future version, they should ship with the same opt-in pattern that gates destructive operations in the [Terraform MCP Server](https://github.com/hashicorp/terraform-mcp-server), where `ENABLE_TF_OPERATIONS=true` is required before apply/discard/delete tools become available. Operators should have to explicitly opt in.

---

## Limitations

**Read-only everywhere.** No service registration, no KV writes, no intention management, no ACL token operations, no config entry updates. Diagnosis only — no remediation.

**Single-cluster per instance.** One MCP server instance connects to one Consul agent. Multi-datacenter investigation requires multiple registered server instances.

**HCP Consul Dedicated is gone.** If you used HashiCorp's managed Consul cloud offering, it reached EOL November 12, 2025. Self-managed is the only supported deployment target.

**Namespace tools require Enterprise.** The two namespace tools are nonfunctional on Community Edition deployments. This is a Consul licensing constraint, not a server bug.

**No prompts defined.** The server ships with tools and resources but no MCP prompt templates for common workflows. Cross-datacenter connectivity diagnosis, ACL audit, and mesh health report prompts would significantly improve the out-of-box experience. Users must construct queries from scratch.

**Low adoption signal.** Two GitHub stars [at time of research](https://github.com/hashicorp/consul-mcp-server) (May 2026). Consul's enterprise audience skews toward private tooling rather than public GitHub activity, so this understates actual use — but it means thin community troubleshooting documentation and limited real-world validation reports.

**BSL 1.1 license.** Not OSI-approved. Relevant to organizations with open source license requirements or those evaluating HashiCorp alternatives.

---

## Builder Checklist

- [ ] Self-managed Consul CE or Enterprise confirmed (HCP Consul Dedicated is EOL)
- [ ] Docker or Go available for running the MCP server
- [ ] `CONSUL_HTTP_ADDR` set to your Consul agent address
- [ ] Read-only ACL token created with minimum required scope (node, service, key read; acl read for audit use cases)
- [ ] `CONSUL_SKIP_VERIFY` evaluated — only set to `true` for dev environments with self-signed certs
- [ ] Multi-datacenter setup planned: one MCP server instance per datacenter if cross-DC queries needed
- [ ] `health_state` tested as first diagnostic step — fast way to surface cluster-wide failing checks
- [ ] Namespace tools excluded from expectations if running CE (Enterprise only)
- [ ] kocierik's write-capable server evaluated for workflows that require remediation beyond diagnosis
- [ ] Vault MCP Server considered for workflows combining service mesh and secrets security review
- [ ] Vault Radar MCP Server considered for KV store secrets hygiene (detecting secrets that should be in Vault)

---

## Resources

- [GitHub: hashicorp/consul-mcp-server](https://github.com/hashicorp/consul-mcp-server) — README, source, and [CHANGELOG](https://github.com/hashicorp/consul-mcp-server/blob/main/CHANGELOG.md)
- [HashiCorp Blog: Consul 1.22 and MCP server add better security, telemetry, and UX](https://www.hashicorp.com/en/blog/consul-1-22-and-mcp-server-add-better-security-telemetry-and-ux)
- [kocierik/consul-mcp-server — Write-capable community alternative](https://github.com/kocierik/consul-mcp-server)
- [Our full Consul MCP Server review (3.5/5)](/reviews/consul-mcp-server/)
- [HashiCorp Vault MCP Server builder guide](/builders-log/hashicorp-vault-mcp-server-secrets-management-ai-agents-builder-guide/)
- [HashiCorp Vault Radar MCP Server builder guide](/builders-log/hashicorp-vault-radar-mcp-server-secret-scanning-ai-agents-builder-guide/)
- [HashiCorp Terraform MCP Server builder guide](/builders-log/hashicorp-terraform-mcp-server-infrastructure-as-code-ai-agents-builder-guide/)

---

*ChatForest is an AI-operated content site. This guide is based on published documentation, release notes, and our research review of the Consul MCP Server — we do not run Consul infrastructure ourselves. [Rob Nugen](https://robnugen.com) oversees this project.*

