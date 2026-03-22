---
title: "Secret Management MCP Servers — Vault, 1Password, Bitwarden, Infisical, and Beyond"
date: 2026-03-15T04:22:00+09:00
description: "Secret management MCP servers let AI agents store, retrieve, rotate, and audit secrets across HashiCorp Vault, 1Password, Bitwarden, AWS Secrets Manager, Azure Key Vault, Infisical, Doppler, and CyberArk. We reviewed 15+ servers across 10 platforms. HashiCorp's official Vault MCP server leads enterprise users with KV, PKI, and mount management. Bitwarden's official MCP server has the broadest password manager feature set at 129 stars."
og_description: "Secret management MCP servers: HashiCorp Vault (official, 16 tools, 35 stars), Bitwarden (official, 30+ tools, 129 stars), 1Password (community, 66 tools via op-mcp), Infisical (official, 9 tools), Doppler (official), AWS Secrets Manager, Azure Key Vault (7 tools), Vault Radar (4 tools). 15+ servers across 10 platforms. Rating: 4.0/5."
content_type: "Review"
card_description: "Secret management MCP servers across HashiCorp Vault, 1Password, Bitwarden, Infisical, Doppler, AWS, Azure, and CyberArk. Vault's official server handles KV secrets, PKI certificates, and mount management. Bitwarden covers full vault and org administration. Two 1Password community servers offer 8 to 66 tools."
last_refreshed: 2026-03-15
---

Secrets are the keys to everything — **API tokens, database passwords, TLS certificates, encryption keys**. MCP servers for secret management let AI agents store, retrieve, rotate, and audit credentials without developers copy-pasting sensitive values through chat windows or hardcoding them in config files.

The headline finding: **this category is surprisingly mature**. HashiCorp has an official Vault MCP server with KV and PKI support. Bitwarden shipped an official MCP server with 30+ tools covering vault management and organization administration. Infisical and Doppler both have official servers. The major cloud providers cover their secret stores through broader platform MCP servers. And a new sub-category has emerged — **MCP credential security tools** that protect the secrets *used by* MCP servers themselves.

## The Landscape

### HashiCorp Vault (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [hashicorp/vault-mcp-server](https://github.com/hashicorp/vault-mcp-server) | ~35 | Go | 16 | Vault token | stdio, StreamableHTTP |

**HashiCorp's official Vault MCP server provides KV secret management, PKI certificate operations, and mount management.** 35 stars, beta status, requires Go 1.24+ to build from source or Docker. Supports both stdio (local dev) and StreamableHTTP (distributed) transports.

16 tools across three domains:

**KV Secret Operations** (4 tools):

| Tool | What it does |
|------|-------------|
| `list_secrets` | Browse available secret keys in KV mounts |
| `create_secret` | Write or update secrets at KV v2 paths |
| `read_secret` | Retrieve secret values by path |
| `delete_secret` | Remove secrets from KV mounts |

**PKI Certificate Management** (9 tools):

| Tool | What it does |
|------|-------------|
| `enable_pki` | Enable a PKI secrets engine at a mount path |
| `create_pki_issuer` | Create a certificate authority issuer |
| `read_pki_issuer` | Inspect issuer configuration |
| `list_pki_issuers` | Browse available issuers |
| `create_pki_role` | Define certificate issuance roles |
| `read_pki_role` | Inspect role configuration |
| `list_pki_roles` | Browse available roles |
| `delete_pki_role` | Remove a PKI role |
| `issue_pki_certificate` | Generate TLS certificates on demand |

**Mount Management** (3 tools):

| Tool | What it does |
|------|-------------|
| `list_mounts` | Browse active secret engine mounts |
| `create_mount` | Enable a new secret engine |
| `delete_mount` | Disable a secret engine mount |

The **PKI support is the standout feature** — no other secret management MCP server offers certificate lifecycle management. An agent can enable a PKI engine, create a CA, define roles, and issue certificates all through MCP tool calls. This fills a gap that most teams handle through manual `vault` CLI commands or Terraform.

Configuration requires `VAULT_ADDR` and `VAULT_TOKEN` environment variables. StreamableHTTP mode adds rate limiting and CORS configuration for multi-user setups. The server is still beta — HashiCorp recommends local use only, not production-exposed deployments.

**Also notable: [rccyx/vault-mcp](https://github.com/rccyx/vault-mcp)** — 6 stars, TypeScript, MIT, 4 KV v2 tools plus policy management and resource browsing via `vault://secrets` and `vault://policies` URIs. Archived as of February 2026.

### HashiCorp Vault Radar

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Vault Radar MCP](https://developer.hashicorp.com/hcp/docs/vault-radar/mcp-server/overview) | — | — | 4 | HCP credentials | stdio |

**A separate MCP server focused on secret detection and leak monitoring** through HCP Vault Radar. This doesn't manage secrets — it finds exposed ones.

4 tools:

| Tool | What it does |
|------|-------------|
| `query_vault_radar_data_sources` | List monitored data sources |
| `query_vault_radar_resources` | Browse project resources |
| `query_vault_radar_events` | Pull secret exposure events |
| `list_vault_radar_secret_types` | Identify detected secret types |

Useful for security teams running automated secret scanning — an agent can query what types of secrets have been detected across repositories and data sources. Beta status, like the main Vault MCP server.

### Bitwarden (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [bitwarden/mcp-server](https://github.com/bitwarden/mcp-server) | ~129 | TypeScript | 30+ | BW_SESSION token | stdio |

**Bitwarden's official MCP server provides the broadest password manager feature set — covering both individual vault management and organization administration.** 129 stars, GPL-3.0, requires Node.js 22+ and the Bitwarden CLI. Install via `npx @bitwarden/mcp-server`.

Two major tool groups:

**Vault Management:**
- Session control — lock, sync, status checks
- Item CRUD — create, read, update, delete, restore
- Folder and attachment management
- Password generation and TOTP code retrieval
- Bitwarden Send for ephemeral secret sharing
- Device approval workflows

**Organization Administration:**
- Collection and member management
- Group-based access controls
- Policy configuration and enforcement
- Audit log retrieval
- Subscription management
- Bulk user and group imports

The **organization administration tools** are what set this apart from community password manager MCP servers. An agent can manage team access, enforce security policies, pull audit logs, and handle member onboarding — tasks that usually require the Bitwarden web admin console.

**Critical security note:** this server is designed exclusively for local use. Bitwarden emphasizes it must never be hosted publicly — granting AI access means the model can read passwords, modify vault items, and access organization secrets.

### 1Password (Community)

Two community-built servers cover 1Password, with very different scopes:

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [goodwokdev/op-mcp](https://github.com/goodwokdev/op-mcp) | 0 | Rust | 66 | 1Password CLI (biometric) | stdio |
| [CakeRepository/1Password-MCP](https://github.com/cakerepository/1password-mcp) | 3 | TypeScript | 8 | Service Account token | stdio |

**op-mcp wraps the entire 1Password CLI** — 66 tools across authentication (3), accounts (4), vaults (11), items (9), documents (5), users (8), groups (8), Connect servers (11), service accounts (2), events API (1), and secrets (3). Install via `cargo install op-mcp`. The server proxies all requests to the `op` CLI and stores nothing — biometric auth is required when integrated with the 1Password app, providing a strong security boundary.

**1Password-MCP is more focused** — 8 tools for vault listing, item management, password generation, and passphrase creation, plus 4 prompts for credential rotation workflows and vault auditing. Uses Service Account tokens, which limits scope to designated vaults only.

Both are community-built — **1Password has no official MCP server yet**. The security warnings are worth heeding: secrets may be retained by LLM providers, there's no end-to-end encryption during MCP transit, and Service Account tokens should be treated as master keys.

### Infisical (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Infisical/infisical-mcp-server](https://github.com/Infisical/infisical-mcp-server) | ~37 | JavaScript | 9 | Machine Identity (Universal Auth) | stdio |

**Infisical's official MCP server provides secret CRUD plus project and environment management.** 37 stars, Apache 2.0, install via `npx -y @infisical/mcp`. Latest version 0.0.22.

9 tools:

| Tool | What it does |
|------|-------------|
| Create secret | Add a new secret to a project/environment |
| Delete secret | Remove a secret |
| Update secret | Modify an existing secret's value |
| List secrets | Browse secrets in a project/environment |
| Retrieve secret | Get a specific secret's value |
| Create project | Set up a new Infisical project |
| Create environment | Add an environment (dev/staging/prod) |
| Create folder | Organize secrets into folders |
| Invite member | Add team members to a project |

Authentication uses Machine Identity with Universal Auth — you provide `INFISICAL_UNIVERSAL_AUTH_CLIENT_ID` and `INFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET`. This avoids personal credentials entirely and scopes access to what the Machine Identity is allowed to see.

Infisical positions this for **developers securing MCP server configurations** — rather than hardcoding API keys in `claude_desktop_config.json`, you store them in Infisical and inject at runtime.

### Doppler (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [DopplerHQ/mcp-server](https://github.com/DopplerHQ/mcp-server) | 0 | TypeScript | Multiple | Interactive login or service token | stdio |

**Doppler's official MCP server wraps the Doppler API for full secrets management integration.** Apache 2.0, v1.0.4. Supports interactive login (`npx @dopplerhq/mcp-server login`) or scoped service tokens via `DOPPLER_TOKEN`.

Tool categories cover:
- **Secrets** — retrieve, list, set, delete across projects and configs
- **Projects** — create and list
- **Configs** — create and list within projects
- **Environments** — manage dev/staging/production
- **Integrations and webhooks** — connect to external services
- **Activity logging** — audit trail access

The `--read-only` flag restricts to GET operations only — useful when you want agents to read secrets but never modify them. You can also scope to a specific project (`--project`) and config (`--config`) to limit blast radius.

Doppler's blog has published detailed guidance on MCP credential security, noting that **48% of reviewed MCP servers recommend storing credentials in plaintext** `.env` or JSON files. Their server is designed to replace those patterns.

### AWS Secrets Manager (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [@arvoretech/aws-secrets-manager-mcp](https://www.npmjs.com/package/@arvoretech/aws-secrets-manager-mcp) | — | TypeScript | 6 | AWS credentials | stdio |

**Community-built MCP server for AWS Secrets Manager with full CRUD operations.** Available on npm. Supports AWS profiles from `~/.aws/credentials`, environment variables, and the default SDK credential chain for EC2/ECS/Lambda.

6 tools: create secrets, update secrets, get secret values, list all secrets, delete secrets, and describe secret metadata.

AWS doesn't have a dedicated Secrets Manager MCP server in the official [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (4,700 stars). Secrets Manager is used *within* other AWS MCP servers (Aurora Postgres, Aurora MySQL) for credential access, but there's no standalone server for managing secrets themselves.

### Azure Key Vault (via Azure MCP Server)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [microsoft/mcp](https://github.com/microsoft/mcp) (Key Vault subset) | ~2,800 | C# | 7 | Azure identity | stdio |

**Azure Key Vault tools are part of the broader Azure MCP Server covering 40+ Azure services.** The Key Vault subset provides 7 tools across three resource types:

**Secrets** (3 tools): create, retrieve, and list secrets
**Keys** (3 tools): create, retrieve, and list cryptographic keys
**Certificates** (1 tool): create certificates using default policy

A notable security feature: the Azure MCP Server uses **elicitation** — tools that access sensitive data prompt the user for consent before executing. This adds a human-in-the-loop checkpoint that most other MCP servers lack.

Install via VS Code extension, Visual Studio 2026, IntelliJ IDEA, or npm/pip/dotnet packages.

### GCP Secret Manager

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [eniayomi/gcp-mcp](https://github.com/eniayomi/gcp-mcp) | ~6 | — | Multiple | GCP credentials | stdio |

**Community-built GCP MCP server covering multiple services including Secret Manager.** Supports multiple GCP projects with multi-region support. Uses local GCP credentials for authentication.

GCP Secret Manager doesn't have a dedicated MCP server — it's bundled within broader GCP platform servers. Google's own [google/mcp-security](https://github.com/google/mcp-security) focuses on Security Operations, Threat Intelligence, and Security Command Center rather than Secret Manager.

### CyberArk (Remediation-Focused)

CyberArk has built an MCP server that takes a different approach — **rather than just managing secrets, it automatically remediates hardcoded credentials**.

The workflow:
1. Claude Code scans repositories and detects exposed credentials
2. The MCP server authenticates through CyberArk Identity (OAuth with PKCE)
3. Secrets are created in Secrets Manager SaaS with workload-specific permissions
4. Code is automatically refactored to fetch secrets via SDK instead of embedding them
5. Human reviews and merges the remediated changes

The server never stores secrets, uses only short-lived tokens, and requires human approval before merging changes. Available as a Docker container in beta. This is the most opinionated server in the category — it's not a general-purpose secret store interface but an automated security remediation pipeline.

## MCP Credential Security Tools

A growing sub-category focuses on securing the secrets *used by MCP servers themselves* — the API keys and tokens in your `claude_desktop_config.json`:

| Tool | What it does |
|------|-------------|
| [MCPGUARD](https://github.com/JulienPoitou/MCPGUARD) | Scans MCP configs for plaintext credentials, migrates them to OS keychain, injects at runtime |
| [mcp-secrets-plugin](https://github.com/amirshk/mcp-secrets-plugin) | Python utility for storing MCP server credentials in system-native keychains (macOS/Windows/Linux) |
| [mcp-keyring-injector](https://github.com/astrogilda/mcp-keyring-injector) | Session-scoped credential injection — keys auto-injected at startup, auto-removed at exit |

MCPGUARD highlights the problem well: **53% of MCP servers use plaintext API keys stored in config files**. These tools address the meta-problem — securing the credentials that MCP servers need to function.

## What's Missing

- **1Password official server** — the most popular consumer password manager has no official MCP server. Two community servers exist but neither has significant adoption
- **Secret rotation automation** — Vault supports dynamic secrets and leases, but the MCP server only covers KV and PKI. No server automates credential rotation workflows
- **Cross-platform secret sync** — no MCP server bridges multiple secret stores (e.g., sync from Vault to AWS Secrets Manager)
- **GCP dedicated server** — Google's Secret Manager lacks a dedicated MCP server, unlike AWS which at least has a community option
- **LastPass, Dashlane, KeePass** — no MCP servers found for these password managers

## The Bottom Line

**Rating: 4.0 / 5** — Strong official vendor support across enterprise (Vault, Bitwarden, Infisical, Doppler) and cloud providers (AWS, Azure). The category is practical today for teams that need AI agents to read and manage secrets programmatically. Vault's PKI support and Bitwarden's organization tools demonstrate real depth. The main gap is that consumer password managers (1Password, LastPass) lack official support, and no server yet handles advanced workflows like rotation or cross-platform sync. The emerging MCP credential security sub-category (MCPGUARD, keyring injectors) addresses a real and underserved problem.

---

*This review covers MCP servers available as of March 2026. Star counts are approximate and change frequently. ChatForest researches MCP servers by analyzing GitHub repositories, documentation, and community discussions — we do not install or test these servers hands-on. For our full methodology, see our [Best MCP Servers guide](/guides/best-mcp-servers/).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
