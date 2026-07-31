---
title: "Anthropic WIF Is GA: Replace Static API Keys with OIDC Tokens in Your Claude Agents"
date: 2026-06-19
description: "Anthropic's Workload Identity Federation is now generally available on the Claude Platform. Replace long-lived sk-ant- API keys with short-lived OIDC tokens from AWS IAM, GCP, GitHub Actions, Azure, Kubernetes, or any standards-compliant identity provider."
og_description: "No more static API keys for production Claude deployments. Anthropic WIF (Workload Identity Federation) is GA: authenticate with short-lived OIDC tokens from AWS IAM, GCP, GitHub Actions, Azure, or Kubernetes. Complete builder guide."
content_type: "Builder's Log"
categories: ["Anthropic", "Security", "Infrastructure", "Developer Tools"]
tags: ["anthropic", "wif", "workload-identity-federation", "api-keys", "oidc", "aws-iam", "github-actions", "kubernetes", "security", "service-accounts", "june-2026", "builders-log"]
sources_audited: 2026-07-31
---

[Anthropic made Workload Identity Federation (WIF) generally available on the Claude Platform on June 17, 2026.](https://claude.com/blog/workload-identity-federation) The short version: your production Claude agents no longer need a long-lived `sk-ant-` API key sitting in an environment variable or a secrets manager. Instead, they authenticate with a short-lived token issued by an identity provider you already operate. See also [Anthropic's WIF documentation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation). Part of our **[Builder's Log](/builders-log/)**.

---

## What WIF Is

Workload Identity Federation is a method for letting a workload — a Lambda function, a GitHub Actions runner, a Kubernetes pod, a VM — prove its identity to the Claude API using a cryptographically signed token (a JWT) from a trusted identity provider (IdP), rather than a static secret. [Anthropic's docs describe the mechanism as: your workload presents a signed JWT from your identity provider, Anthropic validates it against trust rules you configure in the Claude Console, and returns a short-lived Anthropic access token bound to a service account in your organization.](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation)

The token is short-lived — [Anthropic's reference docs put the default token lifetime at 3,600 seconds (1 hour), configurable between 60 seconds and 24 hours](https://platform.claude.com/docs/en/manage-claude/wif-reference#validation-rules). It carries claims about the workload's identity. Anthropic validates those claims against **federation rules** you configure in the Claude Console or the [Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api), then issues a short-lived Anthropic access token (prefixed `sk-ant-oat01-`) scoped to a **service account** you control.

**No static credentials are ever stored, rotated, or leaked.**

---

## Supported Identity Providers

WIF works with any OIDC-compliant identity provider. Anthropic publishes dedicated setup guides for these providers:

| Provider | Workload type |
|---|---|
| **[AWS](https://platform.claude.com/docs/en/manage-claude/wif-providers/aws)** | Lambda, EC2, ECS, and EKS, via STS-issued web identity tokens (EKS pods can alternatively use projected Kubernetes service-account tokens) |
| **[Google Cloud](https://platform.claude.com/docs/en/manage-claude/wif-providers/gcp)** | Cloud Run, Cloud Functions, App Engine, Compute Engine, and GKE with Workload Identity |
| **[Microsoft Entra ID](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure)** (formerly Azure AD) | Managed identities on VMs, VM Scale Sets, App Service, Functions, and Container Apps; Entra Workload Identity on AKS |
| **[GitHub Actions](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions)** | CI/CD jobs with the `id-token: write` permission |
| **[Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes)** | Self-managed clusters (kubeadm, k3s, OpenShift, on-prem) using projected service-account tokens |
| **[SPIFFE](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe)** | Workloads with JWT-SVIDs issued by SPIRE or another SPIFFE-conformant issuer |
| **[Okta](https://platform.claude.com/docs/en/manage-claude/wif-providers/okta)** | Okta service applications using the OAuth 2.0 `client_credentials` grant |
| Any standards-compliant OIDC issuer | Custom or self-hosted IdPs that issue JWTs, via Custom OIDC setup |

---

## How It Works

The authentication flow is three steps:

1. **Your workload requests a token from its IdP.** An AWS Lambda, EC2 instance, or ECS task, for example, [calls the AWS STS `GetWebIdentityToken` API](https://platform.claude.com/docs/en/manage-claude/wif-providers/aws) and gets a JWT signed by AWS. A GitHub Actions job [requests a token from the OIDC endpoint built into the runner](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions), gated by the `id-token: write` workflow permission.

2. **Your workload presents that token to the Claude Platform.** The SDK posts the JWT to [`POST /v1/oauth/token`](https://platform.claude.com/docs/en/manage-claude/wif-reference#token-exchange-request), using the [RFC 7523](https://www.rfc-editor.org/rfc/rfc7523) `jwt-bearer` grant.

3. **Anthropic validates the token and returns a short-lived access token.** [Validation checks](https://platform.claude.com/docs/en/manage-claude/wif-reference#jwt-verification) include: the JWT signature against the issuer's published JWKS, the token's `aud` claim against the rule's configured audience, and any `subject_prefix`, `claims`, or CEL `condition` matchers in your federation rule. If valid, Anthropic issues a short-lived (`sk-ant-oat01-...`) access token bound to a service account in your org.

The resulting access token works exactly like an API key for the duration of the request or session. It carries the same rate limits and permissions as the service account it's bound to.

---

## Service Accounts

[WIF introduces service accounts as a new primitive on the Claude Platform](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#service-accounts) — "a named, non-human identity inside your Anthropic organization." Rather than a single shared API key for all your workloads, you create one service account per workload (or per role) and bind it to a federation rule.

**What service accounts give you:**

- **Per-workload identity**: Your prod agent and your staging agent are different identities with different roles.
- **Scoped permissions**: The rule's [OAuth scope](https://platform.claude.com/docs/en/manage-claude/wif-reference#oauth-scopes) (for example `workspace:inference` versus `workspace:developer`) caps what a minted token can call, regardless of the service account's underlying role.
- **Clean audit trail**: You can audit which workloads acted as which service account.
- **Independent revocation**: Compromise one workload? [Archive its service account](https://platform.claude.com/docs/en/manage-claude/wif-admin-api#pagination-and-archiving) (a soft delete) via the Console or Admin API. Nothing else is affected.

---

## Setting Up WIF

**Option 1 — Claude Console (UI)**

[Per Anthropic's setup walkthrough](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#set-up-federation):

1. Go to **Settings → Workload identity** and select **Connect workload**.
2. Choose your provider's tile (or **Custom OIDC**). The wizard creates the federation issuer (your IdP's issuer URL), the match conditions for incoming JWTs — for example `subject_prefix` matching a specific AWS IAM role ARN, or a `claims` entry matching GitHub's `repository` claim to `your-org/your-repo` — and names for the service account and federation rule.
3. Optionally verify the issuer, then test the connection: the wizard listens for a successful token exchange from your workload for 15 minutes.
4. Done. Your workload exchanges its IdP token for a Claude access token at runtime.

**Option 2 — Admin API (programmatic)**

For organizations with many workloads, [Anthropic's Admin API supports managing WIF resources](https://platform.claude.com/docs/en/manage-claude/wif-admin-api) under the `/v1/organizations` path (not the data-plane API):

- `POST https://api.anthropic.com/v1/organizations/service_accounts` — create a service account
- `POST https://api.anthropic.com/v1/organizations/federation_issuers` — register an identity provider
- `POST https://api.anthropic.com/v1/organizations/federation_rules` — create a federation rule binding an issuer to a service account
- `POST https://api.anthropic.com/v1/organizations/service_accounts/{id}` — update a service account (Anthropic's API uses `GET`/`POST` for reads and updates on these resources, not `PATCH`)
- `POST https://api.anthropic.com/v1/organizations/service_accounts/{id}/archive` — archive (soft-delete) a service account; there is no hard-delete endpoint

This means WIF setup can live in Terraform, Pulumi, or your org's IaC pipeline alongside the rest of your infrastructure.

---

## Builder Trade-offs

WIF is the right choice for production Claude deployments in most organizations. It isn't the right choice for every scenario.

**When to use WIF:**

- Any Claude API call made from a machine identity (Lambda, pod, CI job, VM)
- Organizations that already enforce no-static-secrets policies in CI/CD
- Teams that need per-workload audit trails for compliance
- Any workload on AWS, GCP, or Azure — the IdP is already there

**When a static API key is still fine:**

- Local development (your laptop, a dev environment)
- Quick prototypes and research scripts where rotation overhead isn't worth the setup
- Environments without an OIDC-compatible IdP
- Projects where a single developer is the only user

**The setup cost to be honest about:**

WIF requires that your workload has an identity in an OIDC-capable IdP. If you're already on AWS/GCP/Azure or using GitHub Actions, you almost certainly do — but you'll still need to:
- Configure an IAM role or service account that issues OIDC tokens with the right claims
- Create the federation rule in Claude Console (mapping those claims to a Claude service account)
- Update your workload's auth code to do the token exchange before calling Claude

For a Lambda calling Claude, that's roughly 20 lines of Python/Node and one Console configuration step. For a Kubernetes cluster with SPIFFE, the initial setup is heavier — but it then covers every pod in the cluster.

---

## What This Replaces (and What It Doesn't)

**Replaces:**
- `ANTHROPIC_API_KEY=sk-ant-...` in Lambda environment variables — [note that a leftover `ANTHROPIC_API_KEY` sits above the federation tiers in SDK credential precedence and silently shadows WIF](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#credential-precedence), so migrating means unsetting it everywhere, not just adding federation alongside it
- API keys stored in AWS Secrets Manager, GCP Secret Manager, Azure Key Vault
- Manual key rotation schedules

**Does not replace:**
- The Claude API itself — WIF is an authentication layer, not a new API surface
- Rate limits and quotas — those still apply per service account
- The need to monitor API usage — audit logs are better with WIF, but still require monitoring

---

## The Relationship to Claude Platform on AWS

Don't confuse this with **[Claude Platform on AWS](https://docs.aws.amazon.com/claude-platform/latest/userguide/authentication.html)** (Anthropic's separate inference stack, billed through AWS Marketplace, reached at its own `aws-external-anthropic` regional endpoint). It is a distinct product from the direct Claude API (`api.anthropic.com`) that this article covers, and as of this writing it does **not** use WIF's federation-rules/service-account model at all. Its documented authentication paths are:

- **SigV4 request signing** — the primary, "enterprise-native" path, using the standard AWS credential provider chain (env vars, `~/.aws/credentials`, SSO, web identity via `AWS_WEB_IDENTITY_TOKEN_FILE`/`AWS_ROLE_ARN` for IRSA and GitHub Actions, ECS container credentials, or EC2 instance metadata).
- **API key authentication** — a separate key type generated in the AWS Console under **Claude Platform on AWS → API keys** (these do not work against the direct Claude API, and direct-API keys don't work here either). Anthropic also publishes [token-generator libraries](https://docs.aws.amazon.com/claude-platform/latest/userguide/authentication.html) that mint short-term (12-hour default) API keys from AWS IAM credentials, for teams that want to avoid long-lived keys without adopting SigV4.

Both paths avoid a permanently static Anthropic credential, but neither is "WIF" in the OIDC/JWT-bearer sense described above — that mechanism is specific to the direct Claude API.

---

## Summary

| | Static API key | WIF (OIDC token) |
|--|---|---|
| Lifespan | Months to years | Minutes |
| Storage requirement | Yes (env var, secrets manager) | No |
| Per-workload identity | No (shared key) | Yes (service accounts) |
| Audit trail granularity | Request-level, shared key | Per-service-account |
| Setup complexity | Minimal | Moderate (OIDC infrastructure required) |
| Best for | Dev/local, simple scripts | Production, CI/CD, cloud workloads |

WIF removes one of the most common credentials-leak vectors in AI application security. If you're deploying Claude agents in any production environment, this is the right auth model. The setup cost is front-loaded, and you pay it once.

*We research and analyze official documentation and public announcements. We don't run production Claude Platform deployments.*
