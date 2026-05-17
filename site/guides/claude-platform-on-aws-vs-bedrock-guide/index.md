# Claude Platform on AWS: Native Anthropic API Through Your AWS Account (And How It Differs From Bedrock)

> On May 11, 2026, Anthropic launched Claude Platform on AWS — a GA service that brings Anthropic's native API to teams via AWS billing and IAM auth. Day-one feature parity with the direct API, including Managed Agents, Skills, Remote MCP, Files API, Web Search, and Code Execution. We break down who should use it, how it differs from Bedrock, and what migration looks like.


On May 11, 2026, Anthropic reached general availability on **Claude Platform on AWS** — a service that makes Anthropic's native Claude API available through existing AWS accounts, with IAM authentication, CloudTrail audit logging, and a single consolidated AWS invoice.

The proposition for developers is straightforward: you get the complete Anthropic API — every feature, on launch day — without maintaining a separate vendor relationship. The practical question is how it differs from Claude on Amazon Bedrock, and which one you should use. The answer depends primarily on compliance requirements and whether your team needs multi-model capabilities.

This analysis draws on Anthropic's official blog post, the AWS GA announcement, the Claude API documentation, AWS docs, CloudZero's billing comparison, InfoQ, and the Classmethod engineering team's technical breakdown — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## What Claude Platform on AWS Is

Claude Platform on AWS is not a repackaged version of Bedrock. It is Anthropic's own API — the same one available at api.anthropic.com — made accessible through AWS billing and AWS IAM authentication.

The distinction matters architecturally: Claude Platform on AWS is **Anthropic-operated infrastructure**. Customer data is processed by Anthropic, outside the AWS security boundary. This is the opposite of Bedrock, where AWS is the data processor and data stays inside the AWS perimeter.

Practically, this means Claude Platform on AWS ships every new Anthropic feature on the day it launches. Features like Managed Agents, Skills, Remote MCP, Files API, and Web Search are available immediately — whereas Bedrock's integration has historically lagged Anthropic's direct API by weeks or months as features go through the Bedrock adoption process.

---

## What You Get

Every capability currently available on Anthropic's direct API is available through Claude Platform on AWS:

**Core API**
- All current Claude models (claude-opus-4-6, claude-sonnet-4-6, claude-haiku-4-5, and successors)
- Messages API with full tool use and streaming support
- Prompt caching — reduce latency and cost on repeated context
- Citations — grounded output with source attribution
- Batch processing — async jobs at 50% cost reduction
- Files API (beta) — upload documents once, reference in multiple requests

**Agentic Capabilities**
- Claude Managed Agents (beta) — Anthropic-hosted agent runtime with persistence and orchestration
- Advisor strategy (beta) — multi-step reasoning mode for complex tasks
- Skills (beta) — reusable agent capabilities that run server-side
- MCP Connector (beta) — connect agents to remote MCP servers directly from the API

**Developer Tooling**
- Web Search and Web Fetch — real-time internet access from within Claude
- Code Execution — sandboxed Python execution within API calls
- Claude Console — browser-based IDE for prompt development, evaluation, and testing

**AWS Integration**
- IAM authentication via SigV4 — use existing AWS roles and policies
- CloudTrail audit logging — every API call logged to your existing CloudTrail setup
- AWS Marketplace billing — single invoice, retires against existing AWS commitments
- No separate Anthropic contract required

---

## Claude Platform on AWS vs Bedrock vs Direct API

The three ways to access Claude serve different needs. Here is the full comparison:

| Dimension | Claude Platform on AWS | Amazon Bedrock | Direct Anthropic API |
|---|---|---|---|
| **Operated by** | Anthropic | AWS | Anthropic |
| **Data within AWS boundary** | No | Yes | No |
| **Feature parity with direct API** | Day one | Lags (weeks to months) | Reference |
| **Multi-model support** | Claude only | Claude + Meta + Mistral + Amazon + others | Claude only |
| **FedRAMP High / IL4 / IL5** | No | Yes | No |
| **HIPAA-eligible** | No | Yes | No |
| **Authentication** | AWS IAM / SigV4 | AWS IAM / SigV4 | Anthropic API key |
| **Billing** | AWS (CCUs) | AWS (tokens, provisioned throughput) | Anthropic (USD) |
| **Workspace geo** | US only (currently) | Configurable per region | Configurable |
| **Bedrock Guardrails** | No | Yes | No |
| **Bedrock Knowledge Bases** | No | Yes | No |
| **Claude Managed Agents** | Yes (beta) | No | Yes (beta) |
| **Remote MCP** | Yes (beta) | No | Yes (beta) |
| **Web Search / Web Fetch** | Yes | No | Yes |
| **Files API** | Yes (beta) | No | Yes (beta) |

The key insight: if you need features Anthropic ships this month, Claude Platform on AWS has them. If you need data to stay inside AWS or have compliance requirements like FedRAMP or HIPAA, Bedrock is the correct choice — and will remain so until Anthropic builds equivalent compliance infrastructure.

---

## Billing: Claude Consumption Units

Claude Platform on AWS uses a different billing unit than either Bedrock or the direct API. Usage is denominated in **Claude Consumption Units (CCUs)**, metered hourly and invoiced monthly in arrears on your AWS bill.

The conversion rate: **$0.01 per CCU** (100 CCUs = $1.00 USD). Anthropic converts your token usage to CCUs at this fixed rate after applying any negotiated discounts.

**US-only inference pricing:** If your workspace is configured for US-only inference (currently the only available workspace geo), pricing is at **1.1× the standard rate** across all token categories. This reflects routing overhead for regional constraint.

For teams with large existing AWS commitments, the CCU-based billing retires against those commitments — a meaningful simplification for finance teams managing AWS enterprise agreements. For smaller teams without negotiated AWS discounts, the direct Anthropic API may offer simpler pricing.

---

## Who Should Use Claude Platform on AWS

**Best fit:**
- Teams heavily invested in AWS infrastructure who want API feature parity with the direct API, without a separate vendor relationship or billing relationship with Anthropic
- Organizations using Claude Code who want development and production API usage on a single AWS bill
- Enterprises running AWS IAM governance who want Claude API access within their existing permission model
- Teams that need Managed Agents, Skills, or Remote MCP today, not on Bedrock's adoption timeline

**Not a fit:**
- Regulated industries requiring FedRAMP High, IL4, IL5, or HIPAA — stay on Bedrock
- Teams requiring data to remain within the AWS security boundary
- Multi-model workflows mixing Claude with Meta Llama, Mistral, Amazon Titan, or other Bedrock-available models
- Teams that need Bedrock-specific features: Guardrails, Knowledge Bases, or configurable regional data residency

---

## Regional Availability

Claude Platform on AWS is available in 17 regions at GA:

- **North America:** US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central)
- **South America:** São Paulo
- **Europe:** Dublin, London, Frankfurt, Milan, Zurich, Paris, Stockholm
- **Asia Pacific:** Tokyo, Seoul, Jakarta, Sydney, Melbourne

Note: workspace geo is US-only at launch — inference may route to Anthropic's primary infrastructure regardless of which AWS region you're working from. Regional endpoint selection for billing and latency purposes differs from data residency guarantees.

---

## Migration from Bedrock

If your team is already using Claude on Amazon Bedrock, the migration path to Claude Platform on AWS is documented. The request body format is already the Anthropic Messages API — the changes are:

1. **Update the base URL** — from the Bedrock endpoint to the Claude Platform on AWS endpoint
2. **Update the SigV4 service name** — from `bedrock-runtime` to the Claude Platform service name
3. **Update model IDs** — Claude Platform uses Anthropic's native model IDs (e.g., `claude-sonnet-4-6`) rather than Bedrock's ARN-style identifiers
4. **Add the `anthropic-workspace-id` header** — required for Claude Platform on AWS routing

If you're on the legacy Bedrock `InvokeModel` or `Converse` API (rather than the Messages API), the migration also requires rewriting request and response shapes to match the Messages API format — a larger change but one that gains you full compatibility with every subsequent Anthropic API update.

Anthropic's documentation at [platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) covers the migration with code examples.

---

## Compliance Considerations

Claude Platform on AWS is explicitly **not** a compliance replacement for Bedrock in regulated industries:

- **FedRAMP, IL4, IL5:** Not available. Bedrock runs on AWS-controlled infrastructure; Claude Platform on AWS does not. Teams with federal compliance requirements must use Bedrock.
- **HIPAA:** Bedrock has a HIPAA Business Associate Agreement available. Claude Platform on AWS does not.
- **GDPR / EU data residency:** Claude Platform on AWS processes data at Anthropic, not within AWS. Organizations with EU data residency requirements should verify whether this meets their DPA obligations.
- **Data boundary:** Data processed by Claude Platform on AWS flows to Anthropic's infrastructure. CloudTrail logs the API calls, but the data itself is outside the AWS security perimeter.

This is a meaningful distinction for enterprise procurement teams: AWS and Anthropic are separate vendors, and choosing Claude Platform on AWS means your AI processing relationship is with Anthropic, not AWS.

---

## Why This Matters

The Claude Platform on AWS launch solves a real friction point for engineering teams: the gap between "we want all the Anthropic features" and "we can't maintain three separate vendor contracts, billing systems, and IAM configurations."

Features like Managed Agents and Remote MCP are architecturally significant — they represent Anthropic's bet that the future of AI in production is server-side, persistent agent runtimes rather than stateless API calls. Having those features available on day one, via AWS billing, removes a decision delay that previously pushed teams toward either the direct API (separate contract) or Bedrock (feature lag).

Bedrock remains the right answer for regulated industries and multi-model deployments. But for the large number of AWS-native teams building Claude-based applications who do not have FedRAMP or HIPAA requirements, Claude Platform on AWS closes a meaningful organizational gap.

---

*This guide reflects the GA launch state of Claude Platform on AWS as of May 11, 2026. Feature availability, billing, regional support, and compliance coverage may change as the service matures. Check [platform.claude.com](https://platform.claude.com) and [aws.amazon.com/claude-platform](https://aws.amazon.com/claude-platform) for current documentation.*

