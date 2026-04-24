---
title: "Secret Management MCP Servers — Vault, 1Password, Bitwarden, Infisical, and Beyond"
date: 2026-03-15T04:22:00+09:00
description: "Secret management MCP servers let AI agents store, retrieve, rotate, and audit secrets across HashiCorp Vault, 1Password, Bitwarden, AWS Secrets Manager, Azure Key Vault"
og_description: "Secret management MCP servers: HashiCorp Vault (official, 16 tools, 44 stars), Bitwarden (official, 30+ tools, 150 stars), 1Password (community, 66 tools via op-mcp + Unified Access platform), Infisical (official, 9 tools, v0.0.23), Doppler (official), AWS Secrets Manager, Azure Key Vault (9 tools), CyberArk (AWS Marketplace + Agent Guard), Vault Radar (4 tools). 15+ servers across 10 platforms. Rating: 4.0/5."
content_type: "Review"
card_description: "Secret management MCP servers across HashiCorp Vault, 1Password, Bitwarden, Infisical, Doppler, AWS, Azure, and CyberArk. Vault's official server handles KV secrets, PKI certificates, and mount management. Bitwarden covers full vault and org administration. CyberArk now on AWS Marketplace with Agent Guard for AI agent credential security."
last_refreshed: 2026-04-25
---

Secrets are the keys to everything — **API tokens, database passwords, TLS certificates, encryption keys**. MCP servers for secret management let AI agents store, retrieve, rotate, and audit credentials without developers copy-pasting sensitive values through chat windows or hardcoding them in config files.

The headline finding: **this category is surprisingly mature and growing**. HashiCorp has an official Vault MCP server with KV and PKI support (now 44 stars, Vault 2.0 released April 2026 under IBM lifecycle). Bitwarden shipped an official MCP server with 30+ tools covering vault management and organization administration (150 stars). Infisical and Doppler both have official servers. CyberArk has expanded significantly — its MCP server and new Agent Guard product are now on AWS Marketplace. The major cloud providers cover their secret stores through broader platform MCP servers, with Azure Key Vault expanding to 9 tools including certificate import. And a growing sub-category of **MCP credential security tools** protects the secrets *used by* MCP servers themselves — a critical concern given GitGuardian's finding that **24,008 unique secrets were exposed in MCP configuration files** on public GitHub. The OWASP MCP Top 10 (beta, 2026) lists token mismanagement as the #1 risk. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**. Also part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

## The Landscape

### HashiCorp Vault (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [hashicorp/vault-mcp-server](https://github.com/hashicorp/vault-mcp-server) | ~44 | Go | 16 | Vault token | stdio, StreamableHTTP |

**HashiCorp's official Vault MCP server provides KV secret management, PKI certificate operations, and mount management.** 44 stars (+26%), 124 commits, 15 forks, beta status. Requires Go 1.24+ to build from source or Docker. Supports both stdio (local dev) and StreamableHTTP (distributed) transports. **Vault 2.0 released April 2026** — the first major version bump since 1.0, now under IBM lifecycle and versioning following the acquisition. Vault 2.0 adds IBM Passport Advantage licensing and LDAP static role support, though the MCP server tools remain unchanged at 16.

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

Configuration requires `VAULT_ADDR` and `VAULT_TOKEN` environment variables. StreamableHTTP mode adds rate limiting and CORS configuration for multi-user setups. The server includes comprehensive HTTP middleware (CORS, logging, Vault context) and session-based Vault client management with structured logging. Still beta — HashiCorp recommends local use only, not production-exposed deployments.

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
| [bitwarden/mcp-server](https://github.com/bitwarden/mcp-server) | ~150 | TypeScript | 30+ | BW_SESSION token | stdio |

**Bitwarden's official MCP server provides the broadest password manager feature set — covering both individual vault management and organization administration.** 150 stars (+16%), 197 commits, GPL-3.0, requires Node.js 22+ and the Bitwarden CLI. Install via `npx @bitwarden/mcp-server`. Latest version 2026.2.0.

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

Both are community-built — **1Password has no dedicated MCP server for vault access yet**, though the company is clearly investing in the AI agent space. In March 2026, 1Password launched its **Unified Access** platform for AI agent security, partnering with Anthropic, Cursor, GitHub, Perplexity, and Vercel. They also shipped an **MCP Server for Trelica** (their app governance solution, available on AWS Marketplace) and integrated with **Runlayer** for MCP credential management (March 17, 2026). Natoma, an MCP gateway provider, now integrates 1Password to inject credentials into agent sessions. The direction is clear — 1Password is building the AI agent security layer rather than a standalone vault MCP server.

The security warnings are worth heeding: secrets may be retained by LLM providers, there's no end-to-end encryption during MCP transit, and Service Account tokens should be treated as master keys.

### Infisical (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Infisical/infisical-mcp-server](https://github.com/Infisical/infisical-mcp-server) | ~44 | JavaScript | 9 | Machine Identity (Universal Auth) | stdio |

**Infisical's official MCP server provides secret CRUD plus project and environment management.** 44 stars (+19%), 29 commits, Apache 2.0, install via `npx -y @infisical/mcp`. Latest version 0.0.23 (April 14, 2026). **New in 2026:** Infisical now exposes MCP tools through well-defined platform endpoints with full activity logging. Gateway support allows MCP servers in private networks to connect securely to Infisical Cloud without opening inbound access. Real-time secret mutation subscriptions via server-sent events — systems can listen for creates, updates, deletes, and imports as they happen, no polling required. Tighter RBAC conditions and OAuth improvements keep agent access scoped, explicit, and revocable.

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
| [DopplerHQ/mcp-server](https://github.com/DopplerHQ/mcp-server) | ~2 | TypeScript | Multiple | Interactive login or service token | stdio |

**Doppler's official MCP server wraps the Doppler API for full secrets management integration.** 2 stars, 32 commits, Apache 2.0, v1.0.4 (February 2026). Still marked experimental. Supports interactive login (`npx @dopplerhq/mcp-server login`) or scoped service tokens via `DOPPLER_TOKEN`.

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

AWS doesn't have a dedicated Secrets Manager MCP server in the official [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (now 8,900 stars, +89%). Secrets Manager is used *within* other AWS MCP servers (Aurora Postgres, Aurora MySQL) for credential access, but there's no standalone server for managing secrets themselves. AWS recommends storing MCP server credentials as encrypted environment variables in Lambda or retrieving them from Secrets Manager in Lambda function code — but explicitly advises against using MCP tools to *create* secrets, as this would require providing secret data to the model.

### Azure Key Vault (via Azure MCP Server)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [microsoft/mcp](https://github.com/microsoft/mcp) (Key Vault subset) | ~3,000 | C# | 9 | Azure identity | stdio |

**Azure Key Vault tools are part of the broader Azure MCP Server covering 40+ Azure services.** The Key Vault subset has expanded to **9 tools** (up from 7) across four resource types:

**Secrets** (2 tools): create and get/list secrets
**Keys** (2 tools): create and get/list cryptographic keys
**Certificates** (3 tools): create certificates, get/list certificates, and **import certificates** (PFX or PEM with private key — new)
**Administration** (1 tool): **get Managed HSM settings** including purge protection and soft-delete retention (new, Managed HSM vaults only)

Each tool has **annotation hints** indicating whether it's destructive, idempotent, read-only, or handles secrets — enabling MCP clients to apply appropriate guardrails automatically.

A notable security feature: the Azure MCP Server uses **elicitation** — tools that access sensitive data prompt the user for consent before executing. This adds a human-in-the-loop checkpoint that most other MCP servers lack.

**New in 2026:** Azure MCP Server v2.0.0-beta now available as `.mcpb` bundle (no runtime needed). Built into Visual Studio 2022 (17.14.30+) and Visual Studio 2026 natively — enabled via the Azure development workload. Also available via VS Code extension, IntelliJ IDEA, npm/pip/dotnet packages. Azure Key Vault API v2026-02-01 makes Azure RBAC the default access control model for new vaults.

### GCP Secret Manager

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [eniayomi/gcp-mcp](https://github.com/eniayomi/gcp-mcp) | ~6 | — | Multiple | GCP credentials | stdio |

**Community-built GCP MCP server covering multiple services including Secret Manager.** Supports multiple GCP projects with multi-region support. Uses local GCP credentials for authentication.

GCP Secret Manager doesn't have a dedicated MCP server — it's bundled within broader GCP platform servers. Google's own [google/mcp-security](https://github.com/google/mcp-security) focuses on Security Operations, Threat Intelligence, and Security Command Center rather than Secret Manager.

### CyberArk (Remediation + Agent Security)

CyberArk has significantly expanded its MCP presence since March 2026, now offering **three distinct products** in this space:

**Secrets Manager MCP Server** — Provides AI models with the ability to read and update Secrets Manager data. Can create workloads and secrets, assign permissions, scan source code for hardcoded credentials, and propose replacements with managed secrets. Uses OAuth with PKCE for authentication (short-lived tokens only). Available as a Docker container.

**SCA (Secure Cloud Access) MCP Server** — Purpose-built to embed **Zero Standing Privileges** into developer tools. Enforces dynamic, scoped access for cloud resources in AI-driven workflows. Works with Amazon Q Developer, Claude for Desktop, and other MCP clients. **Now available on AWS Marketplace** in the new AI Agents and Tools category.

**CyberArk Agent Guard** (new) — Secures AI agent credential retrieval across secret providers including AWS Secrets Manager and CyberArk Secrets Manager. Acts as an **MCP proxy** that dynamically retrieves secrets, injects them into the MCP server session, and disposes them after use. Provides traceability of all AI agent MCP communications. Also **available on AWS Marketplace**.

The automated remediation workflow remains the standout:
1. Claude Code scans repositories and detects exposed credentials
2. The MCP server authenticates through CyberArk Identity (OAuth with PKCE)
3. Secrets are created in Secrets Manager SaaS with workload-specific permissions
4. Code is automatically refactored to fetch secrets via SDK instead of embedding them
5. Human reviews and merges the remediated changes

CyberArk's expansion from a single remediation server to a three-product suite on AWS Marketplace reflects the growing enterprise demand for AI agent credential security.

## MCP Credential Security Tools

A growing sub-category focuses on securing the secrets *used by MCP servers themselves* — the API keys and tokens in your `claude_desktop_config.json`:

| Tool | What it does |
|------|-------------|
| [MCPGUARD](https://github.com/JulienPoitou/MCPGUARD) | Scans MCP configs for plaintext credentials, migrates them to OS keychain, injects at runtime. 3 stars, v0.1.2. Also functions as a security scanner for MCP servers. |
| [mcp-secrets-plugin](https://github.com/amirshk/mcp-secrets-plugin) | Python utility for storing MCP server credentials in system-native keychains (macOS/Windows/Linux) |
| [mcp-keyring-injector](https://github.com/astrogilda/mcp-keyring-injector) | Session-scoped credential injection — keys auto-injected at startup, auto-removed at exit. v1.1.0 adds SessionEnd cleanup hook for automatic credential removal when Claude Code exits. |
| [mcp-secrets](https://github.com/ai-mcp-garage/mcp-secrets) (new) | Cross-platform framework (Python + JS + Rust) storing secrets in system keychains with native OS dialogs for credential input. 4 stars, 12 commits. Verification codes prevent phishing. Session-based caching reduces prompt fatigue. |

The scale of the problem is now quantified: GitGuardian's State of Secrets Sprawl 2026 found **24,008 unique secrets exposed in MCP configuration files on public GitHub**, with **2,117 still valid** at time of scan. The OWASP MCP Top 10 (beta, 2026) lists token mismanagement and secret exposure as **MCP01** — the #1 risk category. MCPGUARD reports 8,000+ MCP servers publicly accessible on the internet as of February 2026.

## What's Missing

- **1Password vault MCP server** — 1Password is investing heavily in AI agent security (Unified Access platform, Runlayer integration, Trelica MCP) but hasn't shipped a direct vault access MCP server. Two community servers exist but neither has significant adoption
- **Secret rotation automation** — Vault supports dynamic secrets and leases, but the MCP server only covers KV and PKI. No server automates credential rotation workflows
- **Cross-platform secret sync** — no MCP server bridges multiple secret stores (e.g., sync from Vault to AWS Secrets Manager)
- **GCP dedicated server** — Google's Secret Manager lacks a dedicated MCP server, unlike AWS which at least has a community option
- **LastPass, Dashlane, KeePass** — no MCP servers found for these password managers
- **Vault dynamic secrets** — the MCP server doesn't expose Vault's dynamic secret engines (database, AWS, SSH), only KV and PKI

## The Bottom Line

**Rating: 4.0 / 5** — Strong official vendor support across enterprise (Vault, Bitwarden, Infisical, Doppler, CyberArk) and cloud providers (AWS, Azure). The category is practical today for teams that need AI agents to read and manage secrets programmatically. Vault's PKI support, Bitwarden's organization tools, and CyberArk's automated remediation pipeline demonstrate real depth. CyberArk's expansion to AWS Marketplace with Agent Guard shows enterprise demand for AI agent credential security is maturing rapidly. The main gap is that consumer password managers (1Password, LastPass) lack official vault access MCP servers — though 1Password's Unified Access platform signals that a different approach (credential injection rather than vault browsing) may be the direction. No server yet handles advanced workflows like dynamic secret rotation or cross-platform sync. The MCP credential security sub-category (MCPGUARD, mcp-secrets, keyring injectors) continues to grow, addressing the documented problem of 24,000+ exposed secrets in MCP configs.

---

*This review covers MCP servers available as of April 2026. Star counts are approximate and change frequently. ChatForest researches MCP servers by analyzing GitHub repositories, documentation, and community discussions — we do not install or test these servers hands-on. For our full methodology, see our [Best MCP Servers guide](/guides/best-mcp-servers/).*

*This review was last edited on 2026-04-25 using Claude Opus 4.6 (Anthropic).*
