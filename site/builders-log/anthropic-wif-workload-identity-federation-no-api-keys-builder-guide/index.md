# Anthropic WIF Is GA: Replace Static API Keys with OIDC Tokens in Your Claude Agents

> Anthropic's Workload Identity Federation is now generally available on the Claude Platform. Replace long-lived sk-ant- API keys with short-lived OIDC tokens from AWS IAM, GCP, GitHub Actions, Azure, Kubernetes, or any standards-compliant identity provider.


Anthropic has made Workload Identity Federation (WIF) generally available on the Claude Platform. The short version: your production Claude agents no longer need a long-lived `sk-ant-` API key sitting in an environment variable or a secrets manager. Instead, they authenticate with a short-lived token issued by an identity provider you already operate. Part of our **[Builder's Log](/builders-log/)**.

---

## What WIF Is

Workload Identity Federation is a method for letting a workload — a Lambda function, a GitHub Actions runner, a Kubernetes pod, a VM — prove its identity to the Claude API using a cryptographically signed token from a trusted identity provider (IdP), rather than a static secret.

The token is short-lived (minutes, not months). It carries claims about the workload's identity. Anthropic validates those claims against federation rules you configure in the Claude Console or the Admin API, then issues a short-lived Anthropic access token scoped to a service account you control.

**No static credentials are ever stored, rotated, or leaked.**

---

## Supported Identity Providers

WIF works with any OIDC-compliant identity provider. Anthropic officially supports and tests against:

| Provider | Workload type |
|---|---|
| **AWS IAM** | Lambda, ECS tasks, EC2 instances, EKS pods |
| **Google Cloud** | GCP service accounts, GKE workload identity |
| **Azure** | Managed identities, Azure AD workload identity |
| **GitHub Actions** | CI/CD jobs with the `id-token: write` permission |
| **Kubernetes (SPIFFE/SPIRE)** | Pods, microservices in any k8s cluster |
| **Okta** | Enterprise workloads using Okta as the IdP |
| Any standards-compliant OIDC issuer | Custom or self-hosted IdPs that issue JWTs |

---

## How It Works

The authentication flow is three steps:

1. **Your workload requests a token from its IdP.** An AWS Lambda, for example, calls `sts:AssumeRoleWithWebIdentity` and gets a JWT. A GitHub Actions job requests a token via the OIDC provider built into the runner.

2. **Your workload presents that token to the Claude Platform.** The Claude API accepts it at the standard token exchange endpoint.

3. **Anthropic validates the token and returns a short-lived access token.** Validation checks: the JWT signature (against the IdP's public keys), the token's `aud` claim matches your configured audience, and any claim conditions you've added in your federation rules. If valid, Anthropic issues a short-lived access token bound to a service account in your org.

The resulting access token works exactly like an API key for the duration of the request or session. It carries the same rate limits and permissions as the service account it's bound to.

---

## Service Accounts

WIF introduces service accounts as a new primitive on the Claude Platform. Rather than a single shared API key for all your workloads, you create one service account per workload (or per role) and bind it to a federation rule.

**What service accounts give you:**

- **Per-workload identity**: Your prod agent and your staging agent are different identities with different roles.
- **Scoped permissions**: A read-only workload can't be misconfigured to run expensive operations.
- **Clean audit trail**: The Claude Console and Compliance API log which service account made which API calls, not just "someone used this API key."
- **Independent revocation**: Compromise one workload? Revoke its service account. Nothing else is affected.

---

## Setting Up WIF

**Option 1 — Claude Console (UI)**

1. Go to **Settings → Workload Identity Federation**.
2. Create a federation rule: name it, paste in your IdP's issuer URL, set the claim conditions you want to enforce (e.g., `sub` must match a specific AWS role ARN, or `repository` must match `your-org/your-repo`).
3. Create a service account and link it to the rule.
4. Done. Your workload exchanges its IdP token for a Claude access token at runtime.

**Option 2 — Admin API (programmatic)**

For organizations with many workloads, Anthropic added new Admin API endpoints:

- `POST /admin/v1/federation_rules` — create a rule
- `POST /admin/v1/service_accounts` — create a service account
- `PATCH /admin/v1/service_accounts/{id}` — update roles or link to a rule
- `DELETE /admin/v1/service_accounts/{id}` — revoke

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
- `ANTHROPIC_API_KEY=sk-ant-...` in Lambda environment variables
- API keys stored in AWS Secrets Manager, GCP Secret Manager, Azure Key Vault
- Manual key rotation schedules

**Does not replace:**
- The Claude API itself — WIF is an authentication layer, not a new API surface
- Rate limits and quotas — those still apply per service account
- The need to monitor API usage — audit logs are better with WIF, but still require monitoring

---

## The Relationship to Claude Platform on AWS

If you're using **Claude Platform on AWS** (Anthropic's inference stack billed through AWS Marketplace), note that it supports two distinct authentication paths:

- **SigV4 / AWS IAM** — authentication via the AWS Marketplace integration, before WIF existed
- **Native WIF** — the new path, where your workload's IAM role identity is federated directly into a Claude service account

The end state is similar — no static API keys — but the mechanisms are different. WIF is the more general, provider-agnostic option. See our [Claude Platform on AWS guide](/builders-log/claude-platform-aws-iam-auth-bedrock-vs-native-builder-guide/) for the full AWS-specific decision tree.

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

