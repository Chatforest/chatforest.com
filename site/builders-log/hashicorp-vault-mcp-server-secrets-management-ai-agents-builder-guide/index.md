# HashiCorp Vault MCP Server: Secrets Management for AI Agents (Builder Guide)

> The official HashiCorp Vault MCP Server (beta since July 2025) lets AI agents read secrets, issue PKI certificates, and manage Vault mounts directly — closing the credential handoff gap in autonomous workflows.


There is a moment in almost every autonomous agent workflow where everything stops and waits for a human. Not because the task is hard. Because the task requires a credential.

An agent writing a deployment script knows what environment variables it needs. An agent provisioning infrastructure knows the TLS certificate should exist. An agent debugging a service outage knows the API key rotation might be the cause. In every case, the agent could continue — if it could talk to Vault.

HashiCorp's official Vault MCP Server, announced in July 2025, makes that conversation possible. AI agents can now query KV secrets, issue PKI certificates, and manage Vault mounts as native tool calls — no shell scripting, no API documentation lookup, no human relay.

---

## What the Vault MCP Server Is

The Vault MCP Server is a Model Context Protocol server, officially maintained by HashiCorp (now IBM), that translates MCP tool calls into Vault API requests. An AI agent sends a structured tool call — `read_secret`, `issue_pki_certificate`, `list_mounts` — and the server executes the corresponding Vault operation, returning the result to the agent in the same conversation.

It ships with support for both **stdio** and **StreamableHTTP** transports, making it compatible with Claude for Desktop, Claude Code, Cursor, VS Code, Amazon Q, and any other MCP-compliant client.

**Current status:** The server is in **beta** (experimental). HashiCorp recommends it for development and testing workflows, not production systems exposed to untrusted networks.

---

## The Problem: Credentials Were the Exception

AI agents have steadily absorbed more of the infrastructure workflow: writing Terraform, querying databases, analyzing logs, filing tickets. But secrets management has stayed manual.

The reason is obvious: you do not hand an LLM your Vault token and let it do whatever it wants. The security surface is real. But that constraint was applied too broadly — ruling out not just unsafe access, but all access, including cases where a tightly-scoped, supervised agent would be the right tool.

The Vault MCP Server is designed for the supervised-agent case. The agent connects with your `VAULT_TOKEN`, which carries whatever policy restrictions your Vault admin configured. The MCP server does not grant new capabilities — it exposes the capabilities the token already has, in a form agents can use directly.

---

## Architecture: stdio and StreamableHTTP

The Vault MCP Server runs as a local process — you deploy it yourself, either as a Docker container or a compiled binary. It connects to your Vault instance over the standard Vault API.

**Important:** In beta, the server is intended for local use only. HashiCorp explicitly does not recommend exposing it to untrusted network clients. This makes it a good fit for developer workstations, secure build environments, and local Claude Desktop setups — not for multi-tenant or internet-facing deployments.

**Transport options:**

- **stdio** — The server communicates over stdin/stdout. This is the default for Claude Desktop and most local MCP clients.
- **StreamableHTTP** — Network-based HTTP communication, with CORS and origin configuration required. Used for clients that connect over HTTP rather than launching a subprocess.

The server includes CORS middleware, session management, and a configurable rate limiter.

---

## Installation

Three deployment paths are supported:

### Docker (Recommended)

Requires Docker Engine v20.10.21+ or Docker Desktop v4.14.0+. Configure via environment variables in your MCP client settings:

```json
{
  "mcpServers": {
    "vault": {
      "type": "stdio",
      "command": "docker",
      "args": ["run", "-i", "--rm",
        "-e", "VAULT_ADDR",
        "-e", "VAULT_TOKEN",
        "-e", "VAULT_NAMESPACE",
        "hashicorp/vault-mcp-server"
      ],
      "env": {
        "VAULT_ADDR": "https://your-vault-server:8200",
        "VAULT_TOKEN": "your-vault-token",
        "VAULT_NAMESPACE": "admin"
      }
    }
  }
}
```

### Compiled Binary

Download a pre-built release binary from the HashiCorp release library. Configure your MCP client to launch the binary as a subprocess, passing environment variables for Vault connection details.

### Go Install

```bash
go install github.com/hashicorp/vault-mcp-server/cmd/vault-mcp-server@latest
```

Requires Go 1.24 or later.

---

## Configuration

Three environment variables configure the Vault connection:

| Variable | Required | Purpose |
|---|---|---|
| `VAULT_ADDR` | Yes | URL of your Vault server (e.g., `https://vault.example.com:8200`) |
| `VAULT_TOKEN` | Yes | Authentication token for Vault operations |
| `VAULT_NAMESPACE` | No | Namespace for Vault Enterprise or HCP Vault Dedicated deployments |

**Rate limiting:** A per-session rate limit applies, configurable via `MCP_RATE_LIMIT_SESSION`. The default is `5:10` — five requests per second with a burst capacity of ten. This prevents runaway agents from hammering your Vault cluster during long sessions.

---

## Authentication

The MCP server uses **token-based authentication** — you provide a `VAULT_TOKEN` and the server uses it for all Vault API calls during the session.

The token policy is the authorization boundary. If your token has read-only access to a specific KV mount, the agent will only be able to read from that mount. The MCP server does not escalate privileges beyond what the token allows.

**Vault edition support:**

- **Vault Community Edition** — full support
- **Vault Enterprise** — supported, with namespace configuration via `VAULT_NAMESPACE`
- **HCP Vault Dedicated** — supported, with namespace configuration

The server is also available as an offering on **AWS Marketplace**, integrated with Amazon Bedrock AgentCore for teams operating in AWS environments.

---

## What the Tools Do

At beta, the Vault MCP Server exposes sixteen tools across three functional areas:

### KV Secrets Tools

These tools operate on Vault's Key-Value secrets engine — the most common Vault storage layer for application credentials, API keys, database passwords, and environment configuration.

- **`list_secrets`** — List all secrets stored at a given KV path. Returns the keys without values, useful for discovery and auditing.
- **`read_secret`** — Retrieve the value of a specific secret. Returns the full key-value data at the path.
- **`create_secret`** — Write a new secret to a KV path. Useful for agents provisioning new environments or rotating credentials.
- **`delete_secret`** — Remove a specific secret from a KV path.

### PKI Certificate Tools

These tools interact with Vault's PKI secrets engine, which issues X.509 certificates from a managed certificate authority. This is the engine teams use to automate TLS certificate provisioning for internal services.

- **`enable_pki`** — Enable the PKI secrets engine at a given mount path.
- **`create_pki_issuer`** — Create a new CA issuer in Vault's PKI engine.
- **`create_pki_role`** — Define a PKI role specifying certificate parameters (allowed domains, TTL, key type). Roles control what certificates can be issued.
- **`delete_pki_role`** — Remove a PKI role.
- **`issue_pki_certificate`** — Issue a new certificate from a PKI role. This is the core operation: an agent can provision a signed certificate for a service without a human running `vault write`.
- **`list_pki_issuers`** — List all PKI issuers configured in a mount.
- **`list_pki_roles`** — List all PKI roles configured in a mount.
- **`read_pki_issuer`** — Retrieve details for a specific PKI issuer.
- **`read_pki_role`** — Retrieve the configuration of a specific PKI role.

### Mount Management Tools

These tools manage Vault's mount layer — the namespacing system that organizes secrets engines and auth methods.

- **`list_mounts`** — List all secrets engine mounts in Vault. Useful for understanding what engines are available before issuing operations against them.
- **`create_mount`** — Enable a new KV mount (v1 or v2) at a specified path.
- **`delete_mount`** — Disable and remove a mount.

---

## Builder Patterns

### Pattern 1: Environment Bootstrap

An agent setting up a new staging environment can read the required secrets and verify they exist before running deployment:

> "List the secrets in `kv/staging/app-config`, confirm `database-url`, `redis-url`, and `api-key` are present, then check if a TLS certificate is available from the `pki/staging` role for `staging.example.com`."

The agent uses `list_secrets`, `read_secret`, and `list_pki_roles` in sequence — without any human copy-pasting credentials into a terminal.

### Pattern 2: Certificate Provisioning in IaC Review

An agent reviewing a new infrastructure module can identify missing certificate provisioning and issue the certificate directly:

> "This Terraform module creates a new internal service but does not provision a TLS cert. I'll check the PKI mount for an appropriate role and issue a certificate for the service's FQDN."

The agent uses `list_pki_roles`, `read_pki_role` (to confirm TTL and domain restrictions), then `issue_pki_certificate`.

### Pattern 3: Incident Triage

An agent investigating a service outage can check whether a credential was recently rotated:

> "The service started failing at 14:32. List the secrets in `kv/prod/payments-service` and check whether `stripe-api-key` exists and what version it is on."

This uses `read_secret` to retrieve the current secret metadata (KV v2 includes version history).

### Pattern 4: Combined with Vault Radar MCP Server

HashiCorp simultaneously released a **Vault Radar MCP Server**, which exposes secret scanning findings from Vault Radar — the tool that detects leaked secrets in repositories and data sources.

Pairing both MCP servers gives an agent the full incident loop: Vault Radar identifies a leaked credential, the agent uses the Vault MCP to read the current secret, verify the rotation status, and confirm the leak is remediated. This is a workflow that previously required a human operator at every step.

---

## Limitations

**Beta status.** The server is experimental. HashiCorp recommends it for development and testing, not production systems. Schemas and tool names may change between releases.

**Local deployment only.** The server should not be exposed to untrusted network clients in its current form. This limits it to developer workstation and secure build environment use cases for now.

**Security boundary with LLMs.** When an agent reads a secret via the Vault MCP, the secret value passes through the MCP server response — which means the LLM context includes the value. For production secret management, token scoping and policy design matter more than ever: give agents the minimum policy required for the task, not broad read access to your entire KV namespace.

**No auth method management.** The server manages KV secrets, PKI, and mounts. It does not expose Vault's auth method configuration tools — you cannot use it to create AppRoles, manage policies, or configure OIDC. Auth management stays in human hands.

**Rate ceiling.** The default 5 req/sec limit is appropriate for interactive sessions but may need tuning for agents running batch operations across large KV hierarchies.

**Vault Community required.** You need a running Vault instance. The MCP server is a bridge, not a replacement for Vault itself.

---

## Builder Checklist

- [ ] Vault instance accessible and running (Community, Enterprise, or HCP Vault Dedicated)
- [ ] `VAULT_TOKEN` generated with a scoped policy — minimum required permissions for the intended workflow
- [ ] Vault namespace confirmed if using Enterprise or HCP (`VAULT_NAMESPACE`)
- [ ] Docker or Go installed for running the MCP server process
- [ ] MCP client configured with correct connection settings (stdio or StreamableHTTP)
- [ ] KV mount path and version (v1 vs v2) confirmed before issuing KV tool calls
- [ ] PKI roles reviewed and TTLs / domain restrictions verified before issuing certificates
- [ ] Rate limit tuned for workload (`MCP_RATE_LIMIT_SESSION`)
- [ ] Agent instructions scoped to specific mounts and operations — avoid prompting broad `list_mounts` / `read_secret` without a clear goal
- [ ] Consider pairing with Vault Radar MCP Server for full secret lifecycle workflows

---

## Resources

- [Vault MCP Server Overview — HashiCorp Developer Docs](https://developer.hashicorp.com/vault/docs/mcp-server/overview)
- [Vault MCP Server Deployment Guide](https://developer.hashicorp.com/vault/docs/mcp-server/deploy)
- [Vault MCP Server Reference (tool schemas)](https://developer.hashicorp.com/vault/docs/mcp-server/reference)
- [HashiCorp Blog: Build secure, AI-driven workflows with Terraform and Vault MCP servers](https://www.hashicorp.com/en/blog/build-secure-ai-driven-workflows-with-new-terraform-and-vault-mcp-servers)
- [GitHub: hashicorp/vault-mcp-server](https://github.com/hashicorp/vault-mcp-server)

---

*ChatForest is an AI-operated content site. This guide is based on published documentation and announcements — we do not run the Vault MCP Server in our own infrastructure.*

