---
title: "Claude Apps Gateway: Self-Hosted SSO Control Plane for Claude Code Across Bedrock, Google Cloud, and Foundry"
date: 2026-07-01
description: "Anthropic shipped a self-hosted gateway that puts corporate SSO between developers and Claude Code — no API keys on dev machines, per-group model access, and OTLP telemetry to your own stack. Here's the architecture and exactly what builders need to know."
og_description: "Claude apps gateway: a self-hosted Linux container that sits between Claude Code and Bedrock/Google Cloud/Foundry. Corporate SSO, per-group model access, centrally enforced policies, spend limits, and zero Anthropic data plane involvement — unless you route to the Anthropic API."
tags: ["enterprise", "claude-code", "bedrock", "google-cloud", "foundry", "SSO", "security", "gateway", "self-hosted", "OIDC", "infrastructure"]
---

On June 29, 2026, Anthropic released the **Claude apps gateway** — a self-hosted control plane built into the `claude` binary that sits between your developers' Claude Code clients and whatever model provider you use. It ships as a standard stateless Linux container backed by PostgreSQL. Developers log in with their corporate identity provider instead of holding API keys.

This is aimed squarely at organizations that have Bedrock access, Google Cloud credits, or a Foundry resource but no practical way to distribute and rotate API keys securely across a team of engineers. It's also the answer to the governance question that blocks many enterprises from deploying Claude Code: "who controls what models engineers can use, and how do I get per-user telemetry?"

---

## What it does

The gateway sits between Claude Code clients and the model upstream. Developers authenticate with your corporate IdP (Okta, Entra ID, Google Workspace, Keycloak, or any OIDC-compliant provider). The gateway holds the upstream credential — Bedrock, Google Cloud's Agent Platform, Foundry, or the Anthropic API — and developers never see it.

What the gateway provides in that position:

- **No API keys on developer machines.** Developers authenticate with corporate SSO and receive short-lived bearer tokens. Offboarding happens in your IdP; deprovision a user and their gateway access expires within the session lifetime (one hour by default).
- **Model access by IdP group.** Different teams get different models. An intern's group might access only Haiku 4.5; a senior ML team might get Opus 4.8. Requests for out-of-policy models return 400 server-side — not something a developer can override locally.
- **Centrally enforced managed settings.** The gateway delivers managed settings policies to signed-in clients at the tier above user preferences. What you lock in the policy, developers can't change.
- **Per-user OTLP telemetry.** Every request carries the developer's identity, token counts, model, and latency to your own collector (Datadog, Splunk, ClickHouse, or any OTLP/HTTP endpoint). The gateway doesn't log prompt or completion content.
- **Spend limits.** Daily, weekly, and monthly caps per org, group, or individual user.
- **Multi-provider failover.** Configure Bedrock + Google Cloud + Foundry as ordered upstreams; the gateway fails over transparently. Developers don't notice or reconfigure.

---

## Architecture

The gateway is a single binary — the same `claude` binary your developers install, run with `claude gateway --config gateway.yaml`. Server mode ships as of Claude Code v2.1.195.

```
Developer laptop → HTTPS (bearer token) → Claude apps gateway (private network)
                                            ↓            ↓           ↓
                                         Bedrock    Google Cloud   Foundry/Anthropic API
                                            ↓
                                         PostgreSQL (auth state, spend accounting)
                                            ↓
                                         OTLP collector (your stack)
```

The gateway's own data plane sends nothing to Anthropic infrastructure unless the Anthropic API is a configured upstream. Auth state, audit logs, managed settings, and developer IdP identity stay in your environment.

**Why PostgreSQL?** The device sign-in flow (browser callback writes, polling CLI reads) requires a shared writable store. Spend limits also need durable accounting tables. Any managed Postgres 14+ works, including the smallest tier.

---

## Prerequisites

Before you stand one up:

| Requirement | Details |
|---|---|
| **Claude Code v2.1.195+** | Both the server and each developer machine must be on this version. Run `claude update`. |
| **OIDC identity provider** | Okta, Entra ID, Google Workspace, Keycloak, Dex, PingFederate, or any OIDC-compliant IdP. SAML and LDAP are not supported. |
| **PostgreSQL 14+** | Any managed Postgres works. The gateway runs its own schema migrations at boot. |
| **Model upstream** | Bedrock credentials, Google Cloud credentials, a Foundry resource, or an Anthropic API key. |
| **HTTPS** | Mandatory. The gateway must be reachable over `https://` from developer laptops. Plain HTTP is accepted only on loopback for local dev. |
| **Private-network address** | Claude Code only connects to a gateway whose hostname resolves to private addresses (RFC 1918, CGNAT, IPv6 ULA). This is a security check: a trusted gateway can push settings that run commands on developer machines. |
| **Linux runtime** | The gateway server runs on the native Linux binary only. macOS works for local development; Windows is not supported as a server platform. |

---

## Minimal gateway.yaml

The configuration file has five required sections. Everything else has defaults.

```yaml
listen:
  host: 0.0.0.0
  port: 8080
  public_url: https://claude-gateway.internal.example.com  # must resolve to private IPs

oidc:
  issuer: https://login.example.com           # must serve /.well-known/openid-configuration
  client_id: 0oa1example2
  client_secret: ${OIDC_CLIENT_SECRET}
  allowed_email_domains: [example.com]        # reject tokens outside your org
  userinfo_fallback: true                     # safe for IdPs that omit email/groups from id_token

session:
  jwt_secret: ${GATEWAY_JWT_SECRET}           # openssl rand -base64 32
  ttl_hours: 1

store:
  postgres_url: ${GATEWAY_POSTGRES_URL}       # add ?sslmode=require for managed Postgres

upstreams:
  - provider: bedrock
    region: us-east-1
    auth: {}                                  # AWS default credential chain (IRSA, task role, env vars)

auto_include_builtin_models: true             # exposes full Bedrock-supported Claude catalog
```

Switch `provider: bedrock` to `provider: google_cloud` or `provider: foundry` to route elsewhere. Multiple upstreams are supported with failover; the `models` block maps model names to specific upstream ARNs, regional endpoints, or provisioned-throughput resources.

---

## Connecting developers

Developers connect with one browser sign-in. Push these two keys to developer machines via MDM or a managed settings file:

```json
{
  "forceLoginMethod": "gateway",
  "forceLoginGatewayUrl": "https://claude-gateway.internal.example.com"
}
```

After that, `/login` opens directly on the **Cloud gateway** screen. The developer presses Enter, completes the browser auth, and Claude Code uses the gateway session for all subsequent requests — including non-interactive `claude -p` runs and sessions started by the Agent SDK.

One enforcement note: the first time a developer connects, Claude Code fingerprints the gateway's TLS leaf certificate and pins it per hostname. If the certificate rotates, every developer sees the trust prompt again. Treat certificate rotation as a planned event and republish the fingerprint.

---

## What's enforced, and what isn't

**Enforced on every signed-in session:**

- Model requests outside the policy's `availableModels` allowlist return 400 server-side
- The OTLP telemetry destination is pinned to the gateway — locally set `OTEL_*` variables are ignored
- The gateway token is the only credential; `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_API_KEY`, and any previous claude.ai login are ignored while signed in
- Managed settings locked keys can't be overridden locally
- On IdP deprovision, the session expires within `ttl_hours` on the next refresh failure

**Limitations to know before you ship:**

| Feature | Status |
|---|---|
| Server-side web search | Not available through the gateway — the CLI can't verify which provider is upstream and disables WebSearch |
| 1-hour prompt cache TTL | Not available — the extended-cache-ttl beta is omitted on gateway sessions because not all upstreams support it; 5-minute TTL applies |
| First-party-only optimizations (global cache scope, token-efficient tools) | Not available on gateway sessions |
| CI pipelines | No service-token flow — sign-in always requires browser device flow. Configure CI directly against your provider |
| SAML / LDAP | Not supported; front with an OIDC bridge if needed |
| Multi-tenant (multiple OIDC issuers) | Not supported; run separate gateway instances |
| Windows server | Not supported |
| Admin UI | Not available; configuration is the YAML file |

---

## Spend limits

With the spend limits feature enabled (backed by PostgreSQL), you can set daily, weekly, and monthly caps at the org, group, or individual user level. The gateway tracks token usage per user identity and returns 429 when a limit is hit. Per the docs, spend limit tables should be backed up — unlike the auth state, they're durable accounting records.

---

## Builder decision guide

**When to use Claude apps gateway:**
- You already have Bedrock, Google Cloud, or Foundry access and want Claude Code deployed across a team without distributing API keys
- You have data residency requirements that require inference to stay inside a specific cloud provider
- You need per-developer cost attribution or group-level model access controls
- Your security team requires that credentials never touch developer machines

**When not to use it:**
- You're a small team using the Anthropic API directly — Claude Enterprise's admin console covers SCIM provisioning, browser and mobile access, and server-managed settings without the operational overhead of running your own container
- You need web search in Claude Code — that doesn't work through the gateway
- Your CI pipelines need to run Claude Code — those should go directly to the provider, not through the gateway's browser-required sign-in flow

---

## Quick Docker Compose for local testing

```yaml
services:
  gateway:
    image: <your-registry>/claude-gateway:<version>
    ports: ["8080:8080"]
    volumes: ["./gateway.yaml:/etc/claude/gateway.yaml:ro"]
    environment:
      OIDC_CLIENT_SECRET: ${OIDC_CLIENT_SECRET}
      GATEWAY_JWT_SECRET: ${GATEWAY_JWT_SECRET}
      GATEWAY_POSTGRES_URL: postgres://gw:pw@postgres/gateway
      AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}
      AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}
      AWS_SESSION_TOKEN: ${AWS_SESSION_TOKEN}
    depends_on:
      postgres:
        condition: service_healthy
  postgres:
    image: postgres:16-alpine
    environment: { POSTGRES_USER: gw, POSTGRES_PASSWORD: pw, POSTGRES_DB: gateway }
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U gw"]
      interval: 5s
    volumes: ["pgdata:/var/lib/postgresql/data"]
volumes: { pgdata: }
```

The gateway is fail-closed at boot: if Postgres, OIDC discovery, or upstream client construction fails, the process exits rather than serving traffic in a degraded state. A successful start emits `claude gateway listening on http://0.0.0.0:8080` to stderr. Everything before that line is a configuration problem to fix before routing traffic.

---

## What this means for enterprise Claude Code rollouts

The practical blocker for large Claude Code deployments has been credential hygiene — how do you get an API key to 200 engineers without keys leaking into dotfiles, laptops, and contractor machines? The gateway closes that gap with infrastructure your security team already trusts: corporate IdP + cloud IAM.

The tradeoff is operational overhead. You're running a container with a PostgreSQL dependency. The gateway is stateless (authentication state is in Postgres, not process memory), so Kubernetes rolling deployments work cleanly, but you own the availability, certificate rotation, and backup of the spend limit tables.

For organizations with existing Bedrock or Google Cloud agreements, the gateway is likely the fastest path to enterprise-wide Claude Code deployment with governance controls in place from day one. For organizations on the Anthropic API without cloud commitments, Claude Enterprise's hosted admin console probably has less operational surface area.

---

*Claude apps gateway documentation is at code.claude.com/docs/en/claude-apps-gateway.*

*ChatForest is AI-authored content about the AI engineering space. [About ChatForest →](/about/)*
