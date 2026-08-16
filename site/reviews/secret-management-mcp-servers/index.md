# Secret Management MCP Servers — Vault, 1Password, Bitwarden, Infisical, and Beyond

> Secret management MCP servers let AI agents store, retrieve, rotate, and audit secrets across HashiCorp Vault, 1Password, Bitwarden, AWS Secrets Manager, Azure Key Vault


Secrets are the keys to everything — **API tokens, database passwords, TLS certificates, encryption keys**. MCP servers for secret management let AI agents store, retrieve, rotate, and audit credentials without developers copy-pasting sensitive values through chat windows or hardcoding them in config files.

The headline finding: **this category is surprisingly mature and growing**. HashiCorp has an official Vault MCP server with KV and PKI support (now ~58 stars, [Vault 2.0 released April 2026](https://www.hashicorp.com/en/blog/vault-enterprise-20-modernizes-identity-security-at-scale) under IBM lifecycle). Bitwarden shipped an official MCP server with 40+ tools covering vault management and organization administration (~231 stars). Infisical and Doppler both have official servers. CyberArk has expanded significantly — its MCP server and new Agent Guard product are now on AWS Marketplace. The major cloud providers cover their secret stores through broader platform MCP servers, with Azure Key Vault expanding to 9 tools including certificate import. And a growing sub-category of **MCP credential security tools** protects the secrets *used by* MCP servers themselves — a critical concern given GitGuardian's finding that **24,008 unique secrets were exposed in MCP configuration files** on public GitHub. The [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (beta, 2026) lists token mismanagement as the #1 risk. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**. Also part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

## The Landscape

### HashiCorp Vault (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [hashicorp/vault-mcp-server](https://github.com/hashicorp/vault-mcp-server) | ~58 | Go | 16 | Vault token | stdio, StreamableHTTP |

**HashiCorp's official Vault MCP server provides KV secret management, PKI certificate operations, and mount management.** 58 stars, 133 commits, 24 forks, beta status. Requires Go 1.24+ to build from source or Docker. Supports both stdio (local dev) and StreamableHTTP (distributed) transports. **[Vault 2.0 released April 2026](https://www.hashicorp.com/en/blog/vault-enterprise-20-modernizes-identity-security-at-scale)** — the first major version bump since 1.0, now under IBM lifecycle and versioning following the acquisition. Vault 2.0 adds IBM Passport Advantage licensing and LDAP static role support, though the MCP server tools remain unchanged at 16.

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

Configuration requires `VAULT_ADDR` and `VAULT_TOKEN` environment variables. StreamableHTTP mode adds rate limiting and CORS configuration for multi-user setups. The server includes comprehensive HTTP middleware (CORS, logging, Vault context) and session-based Vault client management with structured logging. Still beta — HashiCorp recommends local use only, not production-exposed deployments. Activity since April 2026 has been compliance-only (copyright header updates, May 15) — no new features or releases since v0.2.0 (September 2025).

**Also notable:** rccyx/vault-mcp — previously listed here as an archived 6-star TypeScript alternative. *Correction (2026-08-16): the repository now returns a 404 on GitHub — it appears to have been deleted by its owner rather than merely archived. Removed the dead link; no working primary source remains to verify current status.*

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
| [bitwarden/mcp-server](https://github.com/bitwarden/mcp-server) | ~231 | TypeScript | 40+ | BW_SESSION token | stdio |

**Bitwarden's official MCP server provides the broadest password manager feature set — covering both individual vault management and organization administration.** 231 stars, GPL-3.0, requires Node.js 22+ and the Bitwarden CLI. Install via `npx @bitwarden/mcp-server`. **[Latest version v2026.5.0 (May 20, 2026)](https://github.com/bitwarden/mcp-server/releases/tag/v2026.5.0)** — the first release since v2026.2.0 (February 2026).

Two major tool groups (40+ tools total — 20+ vault management, 20+ org administration):

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

**v2026.5.0 (May 20, 2026)** added a new secure vault unlock mechanism, container security improvements, and dependency upgrades. This is a meaningful security improvement — the previous unlock path had been unchanged since launch.

**Critical security note:** this server is designed exclusively for local use. Bitwarden emphasizes it must never be hosted publicly — granting AI access means the model can read passwords, modify vault items, and access organization secrets.

### 1Password (Community)

Two community-built servers cover 1Password, with very different scopes:

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [goodwokdev/op-mcp](https://github.com/goodwokdev/op-mcp) | 2 | Rust | 66 | 1Password CLI (biometric) | stdio |
| [CakeRepository/1Password-MCP](https://github.com/cakerepository/1password-mcp) | 19 | TypeScript | 8 | Service Account token | stdio |

**op-mcp wraps the entire 1Password CLI** — 66 tools across authentication (3), accounts (4), vaults (11), items (9), documents (5), users (8), groups (8), Connect servers (11), service accounts (2), events API (1), and secrets (3). Install via `cargo install op-mcp`. The server proxies all requests to the `op` CLI and stores nothing — biometric auth is required when integrated with the 1Password app, providing a strong security boundary. **However: this project has had zero commits since its initial drop on January 25, 2026 — it appears abandoned with no releases published.**

**1Password-MCP is the more actively used option** — 19 stars, 83 commits. 8 tools for vault listing, item management, password generation, and passphrase creation, plus 4 prompts for credential rotation workflows and vault auditing. Uses Service Account tokens, which limits scope to designated vaults only.

Both are community-built — **1Password has no dedicated MCP server for vault access yet**, though the company is clearly investing in the AI agent space. 1Password now publishes [MCP developer documentation at `1password.dev/mcp`](https://1password.dev/mcp), signaling official tooling may be in development. In March 2026, 1Password launched its **[Unified Access](https://1password.com/press/2026/mar/1password-unified-access)** platform for AI agent security, partnering with Anthropic, Cursor, GitHub, Perplexity, and Vercel. They also shipped an **[MCP Server for Trelica](https://1password.com/press/2025/jul/mcp-server-for-trelica-aws)** (their app governance solution, available on AWS Marketplace) and integrated with **[Runlayer](https://1password.com/blog/secure-mcp-credentials-1password-runlayer)** for MCP credential management. [Natoma, an MCP gateway provider, now integrates 1Password](https://natoma.ai/blog/bringing-ai-agents-into-enterprise-workflows-with-natoma-and-1password) to inject credentials into agent sessions. The direction is clear — 1Password is building the AI agent security layer rather than a standalone vault MCP server.

The security warnings are worth heeding: secrets may be retained by LLM providers, there's no end-to-end encryption during MCP transit, and Service Account tokens should be treated as master keys.

### Infisical (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Infisical/infisical-mcp-server](https://github.com/Infisical/infisical-mcp-server) | ~56 | JavaScript | 10 | Machine Identity (Universal Auth) | stdio |

**Infisical's official MCP server provides secret CRUD plus project and environment management.** 56 stars, 20 forks, Apache 2.0, install via `npx -y @infisical/mcp`. Latest version 0.0.23 (April 14, 2026) — no new releases since then. **New in 2026:** Infisical now exposes MCP tools through well-defined platform endpoints with full activity logging. Gateway support allows MCP servers in private networks to connect securely to Infisical Cloud without opening inbound access. Real-time secret mutation subscriptions via server-sent events — systems can listen for creates, updates, deletes, and imports as they happen, no polling required. Tighter RBAC conditions and OAuth improvements keep agent access scoped, explicit, and revocable.

10 tools (v0.0.23 added `list projects`):

| Tool | What it does |
|------|-------------|
| Create secret | Add a new secret to a project/environment |
| Delete secret | Remove a secret |
| Update secret | Modify an existing secret's value |
| List secrets | Browse secrets in a project/environment |
| Retrieve secret | Get a specific secret's value |
| Create project | Set up a new Infisical project |
| List projects | Browse existing Infisical projects |
| Create environment | Add an environment (dev/staging/prod) |
| Create folder | Organize secrets into folders |
| Invite member | Add team members to a project |

Authentication uses Machine Identity with Universal Auth — you provide `INFISICAL_UNIVERSAL_AUTH_CLIENT_ID` and `INFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET`. This avoids personal credentials entirely and scopes access to what the Machine Identity is allowed to see.

Infisical positions this for **developers securing MCP server configurations** — rather than hardcoding API keys in `claude_desktop_config.json`, you store them in Infisical and inject at runtime.

### Doppler (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [DopplerHQ/mcp-server](https://github.com/DopplerHQ/mcp-server) | ~5 | TypeScript | Multiple | Interactive login or service token | stdio |

**Doppler's official MCP server wraps the Doppler API for full secrets management integration.** 5 stars, 37 commits, Apache 2.0, v1.0.4 (February 2026). Still marked experimental. Supports interactive login (`npx @dopplerhq/mcp-server login`) or scoped service tokens via `DOPPLER_TOKEN`. **No activity since March 27, 2026 — the server appears dormant.**

Tool categories cover:
- **Secrets** — retrieve, list, set, delete across projects and configs
- **Projects** — create and list
- **Configs** — create and list within projects
- **Environments** — manage dev/staging/production
- **Integrations and webhooks** — connect to external services
- **Activity logging** — audit trail access

The `--read-only` flag restricts to GET operations only — useful when you want agents to read secrets but never modify them. You can also scope to a specific project (`--project`) and config (`--config`) to limit blast radius.

[Doppler's blog](https://www.doppler.com/blog/mcp-server-secure-secrets-management) has published detailed guidance on MCP credential security, noting that **approximately 48% of reviewed MCP servers recommend storing credentials in plaintext** `.env` or JSON files. Their server is designed to replace those patterns. *Correction (2026-08-16): the previous link here pointed to an unrelated Doppler product-update post that does not contain this statistic — relinked to the Doppler post that actually states it.*

### AWS Secrets Manager (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [@arvoretech/aws-secrets-manager-mcp](https://www.npmjs.com/package/@arvoretech/aws-secrets-manager-mcp) | — | TypeScript | 6 | AWS credentials | stdio |

**Community-built MCP server for AWS Secrets Manager with full CRUD operations.** Available on npm. Supports AWS profiles from `~/.aws/credentials`, environment variables, and the default SDK credential chain for EC2/ECS/Lambda.

6 tools: create secrets, update secrets, get secret values, list all secrets, delete secrets, and describe secret metadata.

AWS doesn't have a dedicated Secrets Manager MCP server in the official [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (now **~9,600 stars** — very active, daily releases). *Correction (2026-08-16): this section previously cited an uncorroborated "May 20" path-traversal patch date for `aws-transform-mcp-server` and an unverifiable "Bedrock AgentCore MCP Server v0.1.0, released May 15" — neither could be confirmed against any primary source. Replaced with a verified, current finding:* a real path-traversal vulnerability, **[CVE-2026-18953](https://aws.amazon.com/security/security-bulletins/2026-075-aws/)**, was disclosed in `aws-transform-mcp-server`'s `get_resource` tool (arbitrary file write via the `savePath` parameter) and fixed in version 0.1.5 — see the **[GitHub security advisory](https://github.com/awslabs/mcp/security/advisories/GHSA-66mr-jr63-2jgw)** for details. Secrets Manager is used *within* other AWS MCP servers (Aurora Postgres, Aurora MySQL) for credential access, but there's no standalone server for managing secrets themselves. AWS recommends storing MCP server credentials as encrypted environment variables in Lambda or retrieving them from Secrets Manager in Lambda function code — but explicitly advises against using MCP tools to *create* secrets, as this would require providing secret data to the model.

### Azure Key Vault (via Azure MCP Server)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [microsoft/mcp](https://github.com/microsoft/mcp) (Key Vault subset) | ~3,600 | C# | 9 | Azure identity | stdio |

**Azure Key Vault tools are part of the broader Azure MCP Server covering 40+ Azure services.** The Key Vault subset has expanded to **9 tools** (up from 7) across four resource types:

**Secrets** (2 tools): create and get/list secrets
**Keys** (2 tools): create and get/list cryptographic keys
**Certificates** (3 tools): create certificates, get/list certificates, and **import certificates** (PFX or PEM with private key — new)
**Administration** (1 tool): **get Managed HSM settings** including purge protection and soft-delete retention (new, Managed HSM vaults only)

Each tool has **annotation hints** indicating whether it's destructive, idempotent, read-only, or handles secrets — enabling MCP clients to apply appropriate guardrails automatically.

A notable security feature: the Azure MCP Server uses **elicitation** — tools that access sensitive data prompt the user for consent before executing. This adds a human-in-the-loop checkpoint that most other MCP servers lack.

**New in 2026:** Azure MCP Server v2.0.0-beta now available as `.mcpb` bundle (no runtime needed). Built into Visual Studio 2022 (17.14.30+) and Visual Studio 2026 natively — enabled via the Azure development workload. Also available via VS Code extension, IntelliJ IDEA, npm/pip/dotnet packages. [Azure Key Vault API v2026-02-01 makes Azure RBAC the default access control model for new vaults](https://learn.microsoft.com/en-us/azure/key-vault/general/access-control-default). **3.0.0-beta.11 (May 21, 2026)** brought Azure FileShares SDK upgrades to GA, NFS encryption-in-transit support, and improved MSAL error handling (beta.10, May 8). The project is approaching GA in the 3.0.0 series with ~3,600 stars.

### GCP Secret Manager

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [eniayomi/gcp-mcp](https://github.com/eniayomi/gcp-mcp) | ~200 | TypeScript | Multiple | GCP credentials | stdio |

**Community-built GCP MCP server covering multiple services including Secret Manager.** Supports multiple GCP projects with multi-region support. Uses local GCP credentials for authentication.

GCP Secret Manager doesn't have a dedicated MCP server — it's bundled within broader GCP platform servers. Google's own [google/mcp-security](https://github.com/google/mcp-security) focuses on Security Operations, Threat Intelligence, and Security Command Center rather than Secret Manager.

### CyberArk (Remediation + Agent Security)

*Correction (2026-08-16): CyberArk was acquired by Palo Alto Networks — the deal [closed February 11, 2026](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-cyberark-to-secure-the-ai-era) — and the CyberArk product line was [rebranded to "Idira" in May 2026](https://www.sdxcentral.com/news/palo-alto-networks-rebrands-cyberark-with-idira-platform-release/). Per Palo Alto Networks, the underlying technology and component names are unchanged, only the branding — so the MCP servers described below still function as described, but new documentation and marketing now appears under the Idira name rather than CyberArk.*

CyberArk (now part of Palo Alto Networks) significantly expanded its MCP presence starting around March 2026, offering **three distinct products** in this space:

**[Secrets Manager MCP Server](https://developer.cyberark.com/blog/from-claude-code-scan-to-automated-secret-remediation-building-a-secure-mcp-server-for-ai-agents/)** — Provides AI models with the ability to read and update Secrets Manager data. Can create workloads and secrets, assign permissions, scan source code for hardcoded credentials, and propose replacements with managed secrets. Uses OAuth with PKCE for authentication (short-lived tokens only). Available as a Docker container. See also the [official docs](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cc-mcp-server.htm).

**SCA (Secure Cloud Access) MCP Server** — Purpose-built to embed **Zero Standing Privileges** into developer tools. Enforces dynamic, scoped access for cloud resources in AI-driven workflows. Works with Amazon Q Developer, Claude for Desktop, and other MCP clients. **[Announced available on AWS Marketplace](https://www.businesswire.com/news/home/20250716008339/en/cyberark-announces-availability-of-tools-to-secure-ai-agents-in-the-new-aws-marketplace-ai-agents-and-tools-category)** (July 2025) in the AI Agents and Tools category. *Correction (2026-08-16): the original CyberArk press-release URL cited here now 301-redirects to Palo Alto Networks' Idira page post-acquisition; replaced with a stable BusinessWire copy of the same release.*

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
| [MCPGUARD](https://github.com/JulienPoitou/MCPGUARD) | Scans MCP configs for plaintext credentials, migrates them to OS keychain, injects at runtime. 4 stars, v0.1.2. Also functions as a security scanner for MCP servers. |
| [mcp-secrets-plugin](https://github.com/amirshk/mcp-secrets-plugin) | Python utility for storing MCP server credentials in system-native keychains (macOS/Windows/Linux) |
| [mcp-keyring-injector](https://github.com/astrogilda/mcp-keyring-injector) | Session-scoped credential injection — keys auto-injected at startup, auto-removed at exit. v1.1.0 adds SessionEnd cleanup hook for automatic credential removal when Claude Code exits. |
| [mcp-secrets](https://github.com/ai-mcp-garage/mcp-secrets) (new) | Cross-platform framework (Python + JS + Rust) storing secrets in system keychains with native OS dialogs for credential input. 4 stars, 12 commits. Verification codes prevent phishing. Session-based caching reduces prompt fatigue. |

The scale of the problem is now quantified: [GitGuardian's State of Secrets Sprawl 2026](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/) found **24,008 unique secrets exposed in MCP-related configuration files on public GitHub**, including **2,117 unique valid credentials** (8.8% of all MCP-related findings). The OWASP MCP Top 10 (beta, 2026) lists token mismanagement and secret exposure as **MCP01** — the #1 risk category. [MCPGUARD reports 8,000+ MCP servers publicly accessible](https://github.com/JulienPoitou/MCPGUARD) on the internet as of February 2026.

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

*This review covers MCP servers available as of May 2026. Star counts are approximate and change frequently. ChatForest researches MCP servers by analyzing GitHub repositories, documentation, and community discussions — we do not install or test these servers hands-on. For our full methodology, see our [Best MCP Servers guide](/guides/best-mcp-servers/).*

*This review was last edited on 2026-08-16 using Claude Sonnet 5 (Anthropic).*

