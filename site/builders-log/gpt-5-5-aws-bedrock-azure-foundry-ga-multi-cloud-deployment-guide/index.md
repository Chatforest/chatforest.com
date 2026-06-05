# GPT-5.5 Is Now GA on AWS Bedrock and Azure Foundry: Builder Multi-Cloud Deployment Guide

> GPT-5.5 and Codex went GA on Amazon Bedrock June 1 and on Azure Foundry June 3. Pricing matches the direct OpenAI API on both platforms. Here is when to use each path.


Two platform GAs in four days. On June 1, 2026, OpenAI's GPT-5.5, GPT-5.4, and Codex became generally available on Amazon Bedrock. On June 3, GPT-5.5 reached GA in Microsoft Azure Foundry with confirmed production pricing. Both platforms price GPT-5.5 at the same rate as the direct OpenAI API: $5 per million input tokens, $30 per million output tokens.

If you are running GPT-5.5 workloads or planning to, you now have three production paths. This guide covers what each one gives you, where costs actually diverge, and how to pick without overthinking it.

---

## The Three Paths: Pricing at a Glance

| Path | GPT-5.5 Input | GPT-5.5 Output | GPT-5.5 Pro Input | GPT-5.5 Pro Output |
|---|---|---|---|---|
| **Direct OpenAI API** | $5/M | $30/M | $30/M | $180/M |
| **AWS Bedrock** | $5/M | $30/M | $30/M | $180/M |
| **Azure Foundry** | $5/M | $30/M | $30/M | $180/M |

Per-token pricing is identical across all three. The differences are not in the model cost — they are in what wraps around it.

---

## AWS Bedrock: What You Get That the Direct API Does Not

### IAM-Native Authentication

On the direct OpenAI API, you manage API keys. On Bedrock, you use AWS IAM — the same identity system that controls your S3 buckets, Lambda functions, EC2 instances, and everything else. No separate credential rotation. No API key secrets to inject into CI/CD pipelines. IAM roles, policies, and permission boundaries apply directly to model invocations.

For teams already deep in AWS, this is a meaningful operational simplification. For teams new to AWS, it is overhead.

### Billing Consolidation and MACC-Equivalent Commitments

GPT-5.5 usage on Bedrock counts toward your existing AWS committed spend. If you have AWS Reserved Instances, Savings Plans, or Enterprise Discount Programs (EDPs), model inference spend consolidates with those agreements. You get one invoice, one cost explorer dashboard, and one committed spend pool to track.

### Security and Compliance Infrastructure

Bedrock provides:
- **AWS PrivateLink** — route all inference traffic through a private VPC endpoint; no data traverses the public internet
- **AWS KMS encryption** — at rest and in transit, with customer-managed keys if required
- **AWS CloudTrail audit logging** — every model invocation logged, queryable, retainable per your compliance retention policy
- **VPC isolation** — full network-layer controls

Regulated industries that already run in AWS — healthcare (HIPAA), financial services (FINRA, SOC 2), government (FedRAMP, CMMC) — inherit those compliance postures for GPT-5.5 inference without additional integration work.

### Amazon Bedrock Managed Agents

OpenAI's Managed Agents capability is available on Bedrock alongside the model endpoints. This means persistent memory, built-in security, and enterprise-scale orchestration are part of the same API surface.

### What Bedrock Does Not Provide

Bedrock does not offer fine-tuning of GPT-5.5 (OpenAI models are not open weights). Team collaboration features, RBAC for model access, or prompt evaluation dashboards are handled by your own tooling. If your workflow requires model fine-tuning or built-in evaluation infrastructure, Bedrock leaves that to you.

---

## Azure Foundry: What You Get That the Direct API Does Not

### Microsoft Entra ID Integration

Azure Foundry authenticates through Microsoft Entra ID (formerly Azure Active Directory). For organizations already running Microsoft 365, GitHub Enterprise, or Azure infrastructure, this means the same SSO, conditional access policies, and role-based access controls that govern your documents and cloud resources now govern your GPT-5.5 API calls.

### RBAC and Team Governance

Foundry provides role-based access control at the model and deployment level. You can define who in your organization can invoke which models, with what rate limits, for which projects. This is particularly relevant for large teams where governance over AI spend and capability access matters.

### Built-In Evaluation and Monitoring

Azure Foundry includes model evaluation pipelines, tracing, and monitoring natively. You can run structured evals on GPT-5.5 outputs, track latency and quality metrics, and set up alerting — inside the same platform, without standing up separate infrastructure.

### Fine-Tuning and Lifecycle Management

For supported models (not GPT-5.5 specifically, since it is a closed-weight model, but for Azure Foundry's broader catalog), the platform provides fine-tuning pipelines, model registries, and deployment lifecycle management. If you are running a multi-model strategy that includes open or fine-tunable models alongside GPT-5.5, Foundry handles both in one place.

### Assistants API Migration Path

OpenAI's Assistants API retires August 26, 2026. The primary forward path for Assistants API users is Azure Foundry Agent Service. If you are currently on the Assistants API, the migration target is Foundry — not a new Assistants endpoint on the direct API. This makes Azure Foundry the lowest-friction migration path for anyone running Assistants-based applications today.

### Total Cost Is Not Just Token Price

Azure Foundry's per-token pricing matches the direct API exactly. However, enterprise Azure configurations typically add support plan costs ($100–$1,000+/month depending on tier), plus networking and management overhead. Foundry's additional capabilities come with Azure's enterprise pricing structure — factor this into your TCO if you are comparing against direct API at scale.

---

## Direct OpenAI API: When to Stay

The direct API remains the right choice for most teams that do not have specific reasons to move to a cloud platform:

**Use the direct API if:**
- You are not already in AWS or Azure
- You need day-one access to new OpenAI capabilities — new model versions, experimental endpoints, and features land on the direct API first and propagate to Bedrock and Foundry afterward, sometimes with a lag of days to weeks
- Your team is small and the operational overhead of a cloud platform is not justified
- You are prototyping or in early development and want the simplest possible path

The direct API has no minimum spend commitments, no account configuration overhead, and the most up-to-date model availability. For independent builders and small teams, starting here is usually correct.

---

## Decision Framework

**You are already in AWS and run production workloads there →** Bedrock. IAM, billing consolidation, and the compliance posture you have already established carry over without new integration work.

**You are already in Microsoft 365 / Azure / GitHub Enterprise →** Azure Foundry. Entra ID, RBAC, and monitoring integrate with your existing stack. If you are also migrating off the Assistants API before August 26, Foundry is the natural landing spot.

**You are running a regulated workload and not in either cloud →** Evaluate which cloud's compliance posture matches your regulatory requirements. Bedrock and Foundry both support HIPAA, FINRA, and FedRAMP, but if you have existing certified infrastructure in one cloud, stay there rather than adding a second compliance surface.

**You are an independent builder or small team →** Direct OpenAI API. No overhead, day-one feature access, immediate start.

**You need fine-tuning or built-in evaluation pipelines →** Azure Foundry (supports these for eligible models) or your own tooling alongside any platform.

---

## What to Do Now

**If you are already on Bedrock preview:** GPT-5.5 is now GA. Remove any preview feature flags or waitlist conditions from your integration. Production SLAs apply.

**If you are on Azure Foundry preview:** Same — GA means production SLAs and stable endpoints.

**If you are on the Assistants API:** August 26, 2026 is the retirement date. Azure Foundry Agent Service is the documented migration path. Start the migration now rather than in late August.

**If you are on the direct API and it is working:** There is no urgency to move. Evaluate whether your team size, compliance requirements, or cloud commitments justify a platform shift at your next infrastructure review.

The multi-cloud availability of GPT-5.5 does not change what the model can do. It changes where you can run it, what wraps around it, and how it integrates with the rest of your infrastructure. Pick the path that matches where your team already operates.

