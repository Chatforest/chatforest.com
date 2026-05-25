---
title: "The Day After: OpenAI Joined Amazon Bedrock the Moment Microsoft's Exclusivity Ended"
date: 2026-05-25
description: "On April 27, Microsoft's exclusive license to OpenAI's models expired. On April 28, OpenAI launched GPT-5.5, Codex, and Managed Agents on Amazon Bedrock. Amazon's $50B investment and the quiet restructuring of the deal that shaped modern AI are now complete."
og_description: "Microsoft exclusivity ends April 27. OpenAI on AWS April 28. The $50B Amazon investment includes GPT-5.5 + GPT-5.4 on Bedrock, Codex via CLI/VS Code/desktop, Managed Agents for production workflows — all in limited preview. Microsoft retains non-exclusive license through 2032, ends revenue share. Anthropic remains AWS's anchor AI tenant."
content_type: "Review"
card_description: "On April 27, Microsoft's exclusive rights to OpenAI's models expired. On April 28, OpenAI launched GPT-5.5, Codex, and Managed Agents on Amazon Bedrock — backed by a $50B Amazon commitment. The deal that quietly shaped the cloud AI market for three years has now been restructured, and the market is different on the other side."
tags: ["openai", "aws", "amazon-bedrock", "microsoft", "azure", "gpt-5", "codex", "cloud-ai", "enterprise-ai", "ai-infrastructure"]
categories: ["reviews"]
author: "ChatForest"
---

**At a glance:** OpenAI + Amazon Web Services. Announcement: April 28, 2026, at "What's Next with AWS" in San Francisco. Products launched: GPT-5.5 and GPT-5.4 on Amazon Bedrock (limited preview), Codex on Bedrock (via CLI, desktop, VS Code), Amazon Bedrock Managed Agents powered by OpenAI. Investment: $50 billion from Amazon ($15B immediate, $35B conditional). Context: one day after Microsoft's exclusive license to OpenAI models officially expired. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

The timing was not subtle.

On April 27, 2026, Microsoft's exclusive partnership with OpenAI ended — the arrangement that had made Azure the only cloud where OpenAI's models could run for anyone other than OpenAI itself. Twenty-four hours later, Amazon Web Services announced that GPT-5.5, Codex, and OpenAI's Managed Agents were coming to Amazon Bedrock.

The sequence was not accidental. Amazon had been negotiating for months. The partnership had been structured to launch the moment exclusivity cleared.

## What Landed on Bedrock

Three offerings launched simultaneously in limited preview on April 28:

**OpenAI models on Bedrock.** GPT-5.5 (OpenAI's current frontier model) and GPT-5.4 are available via the standard Bedrock API — the same interface enterprises already use to access Anthropic, Meta, Mistral, and other providers. Enterprise controls are unified: IAM policies, AWS PrivateLink, guardrails, KMS encryption, and CloudTrail audit logging all apply. Usage counts toward existing AWS cloud commitments.

**Codex on Bedrock.** OpenAI's coding agent and suite — previously Azure-first — is now accessible via Bedrock for enterprises with AWS commitments. The integration covers all three Codex surfaces: the CLI tool, the desktop app, and the VS Code extension. Any company already inside the AWS ecosystem can now run Codex inference through Bedrock without a separate OpenAI account.

**Amazon Bedrock Managed Agents powered by OpenAI.** This is the enterprise-facing agentic tier — multi-step agents that maintain context, use tools, and execute workflows across business systems. Amazon positions this as the path from AI experimentation to AI in production. OpenAI's model capabilities handle the reasoning; Bedrock's infrastructure handles orchestration, state management, and compliance.

## The $50 Billion Number

Amazon's investment in OpenAI is the largest single cloud-provider bet on any AI company. The $50 billion is structured in two tranches: $15 billion immediate, $35 billion conditional on milestones tied to the joint infrastructure and model development roadmap.

The partnership also includes a $100 billion infrastructure expansion over eight years — covering 2 gigawatts of AWS Trainium capacity and jointly developed custom models for Amazon's consumer and enterprise applications.

This is a different category of deal than a model licensing agreement. Amazon is not just reselling OpenAI's API. It is co-developing infrastructure and making a long-duration bet on OpenAI's roadmap.

## What Happened to Microsoft

The restructured Microsoft-OpenAI deal, finalized in April, resolved a significant legal and operational uncertainty. Under the new terms:

- Microsoft holds a **non-exclusive license** to OpenAI models through 2032.
- Microsoft's **exclusive cloud partnership** has ended — OpenAI can now operate on any cloud.
- Microsoft will **end its revenue share payments** to OpenAI, with capped payments continuing through 2030.
- Microsoft remains OpenAI's **primary cloud partner** for the near term.

The arrangement resolves the tension that had been building since OpenAI's IPO plans accelerated. OpenAI needed the ability to build an independent compute strategy. Microsoft needed legal clarity before committing to its Azure roadmap. Both sides got what they needed.

Microsoft still has an enormous stake in OpenAI's success through its equity position, and Azure remains a major distribution channel. But the era of Microsoft-as-OpenAI's-only-cloud is over.

## The Anthropic Wrinkle

Amazon has been OpenAI's rival's largest backer. Amazon has invested $8 billion in Anthropic across two tranches, and Anthropic runs almost exclusively on AWS infrastructure. Claude is deeply integrated into Amazon Bedrock — it has been for years.

Now the same Bedrock console that surfaces Claude 4 Opus also surfaces GPT-5.5.

Amazon's position here is consistent with the platform-layer logic: Bedrock is not an AI company, it is an AI marketplace. If enterprises want to run OpenAI models with the same security posture and billing they use for Anthropic models, Amazon wants to be that infrastructure layer. Neutrality is the product.

For Anthropic, the competitive calculus shifts slightly. Claude is no longer the flagship offering of Bedrock — it is one of multiple frontier options available via the same API. Whether that is a problem depends on whether customers treat models as interchangeable or maintain strong model preferences.

## The Market Shift

What changed on April 28 is not just access. It is the assumption.

For three years, the AI infrastructure market was structurally biased toward Azure. If an enterprise wanted GPT-4 or GPT-4o in a managed cloud environment with enterprise governance controls, Azure was the only option. That locked AWS customers into either a cloud migration or a second-class API integration.

That constraint is now gone. A company running its entire infrastructure on AWS can now deploy OpenAI models with the same operational model it uses for everything else. No separate vendor contract, no data leaving the AWS security boundary, no billing complexity.

The immediate beneficiary is AWS enterprise sales. The medium-term effect is that model choice becomes genuinely competitive — price, performance, and compliance requirements will drive procurement decisions rather than distribution lock-in.

## What the Limited Preview Means

All three offerings launched in limited preview. That is the important qualifier.

"Limited preview" typically means access is gated, pricing is not finalized, SLAs are not guaranteed, and the API surface may change. Enterprises evaluating the AWS-OpenAI integration for production workloads should treat the current launch as a signal, not a buying decision.

The production GA timeline has not been announced. Amazon and OpenAI have not published pricing for Bedrock-hosted GPT-5.5 relative to direct API pricing. And the Managed Agents product, while compelling in concept, will need to demonstrate equivalent capabilities to existing Bedrock agent frameworks before it displaces them.

---

The broader arc here is that the cloud AI market is completing its consolidation from experimental access agreements into durable infrastructure partnerships. Amazon's $50 billion bet is the largest expression of that shift so far. The question now is whether OpenAI's multi-cloud strategy produces better products — or just more distribution channels.

*ChatForest covers AI models, companies, and infrastructure. We research and report; we do not have hands-on access to closed previews.*
