# GPT-5.5 Is Now GA on AWS Bedrock and Azure Foundry: Builder Multi-Cloud Deployment Guide

> GPT-5.5 and Codex went GA on Amazon Bedrock June 1; GPT-5.5 reached GA on Azure Foundry April 24. Pricing is close to the direct OpenAI API on both platforms. Here is when to use each path.


GPT-5.5 is now confirmed GA across both major clouds. [GPT-5.5 reached GA in Microsoft Azure Foundry on April 24, 2026](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/), and on June 1, 2026, OpenAI's GPT-5.5, GPT-5.4, and Codex [became generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-openai-models-codex-generally-available/) too. [Direct-API pricing for GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5) is $5 per million input tokens and $30 per million output tokens. Azure Foundry matches that rate exactly. AWS's [published Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) for GPT-5.5 is $5.50 per million input tokens and $33 per million output tokens — about 10% above the direct API rate, even though [AWS's GA announcement](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-openai-models-codex-generally-available/) describes Bedrock pricing as matching "OpenAI first-party rates."

If you are running GPT-5.5 workloads or planning to, you now have three production paths. This guide covers what each one gives you, where costs actually diverge, and how to pick without overthinking it.

---

## The Three Paths: Pricing at a Glance

| Path | GPT-5.5 Input | GPT-5.5 Output | GPT-5.5 Pro Input | GPT-5.5 Pro Output |
|---|---|---|---|---|
| **[Direct OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.5)** | $5/M | $30/M | [$30/M](https://developers.openai.com/api/docs/models/gpt-5.5-pro) | [$180/M](https://developers.openai.com/api/docs/models/gpt-5.5-pro) |
| **[AWS Bedrock](https://aws.amazon.com/bedrock/pricing/)** | $5.50/M | $33/M | Not offered | Not offered |
| **[Azure Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/)** | $5/M | $30/M | $30/M | $180/M |

Per-token pricing is close but not identical across all three: Azure Foundry matches the direct API exactly, while AWS Bedrock's [published on-demand rate](https://aws.amazon.com/bedrock/pricing/) runs about 10% higher. GPT-5.5 Pro is not currently listed among the [OpenAI models available on Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-openai.html) — only standard GPT-5.5, GPT-5.4, and Codex are. The differences beyond token cost are not in the model itself — they are in what wraps around it.

---

## AWS Bedrock: What You Get That the Direct API Does Not

### IAM-Native Authentication

On the direct OpenAI API, you manage API keys. On Bedrock, you use AWS IAM — the same identity system that controls your S3 buckets, Lambda functions, EC2 instances, and everything else. No separate credential rotation. No API key secrets to inject into CI/CD pipelines. IAM roles, policies, and permission boundaries apply directly to model invocations.

For teams already deep in AWS, this is a meaningful operational simplification. For teams new to AWS, it is overhead.

### Billing Consolidation and MACC-Equivalent Commitments

[GPT-5.5 usage on Bedrock counts toward your existing AWS committed spend](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-openai-models-codex-generally-available/). If you have AWS Reserved Instances, Savings Plans, or Enterprise Discount Programs (EDPs), model inference spend consolidates with those agreements. You get one invoice, one cost explorer dashboard, and one committed spend pool to track.

### Security and Compliance Infrastructure

Bedrock provides:
- **[AWS PrivateLink](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html)** — route inference traffic through a private VPC endpoint
- **AWS KMS encryption** — at rest and in transit, with customer-managed keys if required
- **AWS CloudTrail audit logging** — [model invocation calls are logged as CloudTrail management events](https://docs.aws.amazon.com/securityhub/latest/userguide/bedrock-controls.html) by default, queryable and retainable per your compliance retention policy
- **VPC isolation** — network-layer controls

Regulated industries that already run in AWS — healthcare ([HIPAA](https://aws.amazon.com/compliance/hipaa-compliance/)), financial services (FINRA, [SOC 2](https://aws.amazon.com/compliance/soc-faqs/)), government ([FedRAMP](https://aws.amazon.com/compliance/fedramp/), CMMC) — can generally extend those existing compliance postures to GPT-5.5 inference, per [AWS's compliance programs](https://aws.amazon.com/compliance/).

### Amazon Bedrock Managed Agents

[Amazon Bedrock Managed Agents, powered by OpenAI](https://aws.amazon.com/bedrock/openai/), is available on Bedrock alongside the model endpoints. AWS describes it as providing "persistent memory, and built-in security" as part of the same API surface, with [each agent running under its own IAM identity and logged for auditability](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/).

### What Bedrock Does Not Provide

Bedrock does not offer fine-tuning of GPT-5.5 (OpenAI models are not open weights). Team collaboration features, RBAC for model access, or prompt evaluation dashboards are handled by your own tooling. If your workflow requires model fine-tuning or built-in evaluation infrastructure, Bedrock leaves that to you.

---

## Azure Foundry: What You Get That the Direct API Does Not

### Microsoft Entra ID Integration

Azure Foundry authenticates through Microsoft Entra ID (formerly Azure Active Directory). For organizations already running Microsoft 365, GitHub Enterprise, or Azure infrastructure, this means the same SSO, conditional access policies, and role-based access controls that govern your documents and cloud resources now govern your GPT-5.5 API calls.

### RBAC and Team Governance

Foundry provides [role-based access control](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) at the resource, project, and agent level via Azure RBAC (evaluated when authenticating through Microsoft Entra ID). You can define who in your organization can invoke which models and for which projects. This is particularly relevant for large teams where governance over AI spend and capability access matters.

### Built-In Evaluation and Monitoring

[Azure Foundry includes model evaluation pipelines, tracing, and monitoring natively](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability), built on OpenTelemetry and integrated with Azure Monitor Application Insights. You can run structured evals on model outputs, trace multi-step agent behavior, and track latency, quality, and safety metrics — inside the same platform, without standing up separate infrastructure.

### Fine-Tuning and Lifecycle Management

For supported models (not GPT-5.5 specifically, since it is a closed-weight model, but for Azure Foundry's broader catalog), the platform provides [fine-tuning pipelines](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning), model registries via Azure Machine Learning, and [deployment lifecycle management](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements). If you are running a multi-model strategy that includes open or fine-tunable models alongside GPT-5.5, Foundry handles both in one place.

### Assistants API Migration Path

[OpenAI's Assistants API retires August 26, 2026](https://developers.openai.com/api/docs/deprecations). The primary forward path for Assistants API users is Azure Foundry Agent Service. If you are currently on the Assistants API, the migration target is Foundry — not a new Assistants endpoint on the direct API. This makes Azure Foundry the lowest-friction migration path for anyone running Assistants-based applications today.

### Total Cost Is Not Just Token Price

Azure Foundry's per-token pricing matches the direct API exactly. However, enterprise Azure configurations typically add [support plan costs](https://azure.microsoft.com/en-us/support/plans/) — $100/month for Standard, $1,000/month for Professional Direct — plus networking and management overhead. Foundry's additional capabilities come with Azure's enterprise pricing structure — factor this into your TCO if you are comparing against direct API at scale.

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

