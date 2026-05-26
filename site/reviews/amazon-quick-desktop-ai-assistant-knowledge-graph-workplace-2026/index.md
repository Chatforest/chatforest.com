# Amazon's Answer to Copilot Isn't a Chatbot. It's a Knowledge Graph That Learns Your Job.

> Amazon Quick launched April 28 as a desktop AI assistant for macOS and Windows — with a personal knowledge graph that compounds context over time, proactive OS-level alerts, and 11+ integrations across Google Workspace, M365, Slack, Salesforce, and more. It's Amazon's answer to Copilot and Gemini, and it's deliberately priced to undercut both.


**At a glance:** Amazon Quick desktop app. Announced: April 28, 2026, at "What's Next with AWS" in San Francisco. Availability: macOS and Windows, Preview. Pricing: Free tier (no AWS account required), paid plans from $20/month. Core capability: persistent personal knowledge graph built from local files, calendar, email, and 11+ SaaS integrations — with proactive alerts and multi-step workflow automation. Enterprise customers include 3M, GoDaddy, AstraZeneca, BMW, the NFL, Southwest Airlines, and New York Life. Part of our **[AI Tools & Platforms reviews](/categories/ai-tools/)**.

---

Amazon launched Quick as a desktop application on April 28, 2026 — the same day OpenAI went live on Amazon Bedrock, and the day after Microsoft's exclusive license to OpenAI's models expired. The event was called "What's Next with AWS." The answer, evidently, was everything at once.

Quick is not a new product. AWS had been running it as a browser-based assistant for enterprise teams. What changed on April 28 was the architecture: a native app for macOS and Windows, OS-level access to local files without uploading them, background monitoring with proactive notifications, and a personal knowledge graph that persists and compounds across every session.

The pitch is direct: Copilot works inside Microsoft. Gemini works inside Google. Quick works across everything — and it doesn't care which suite you run.

## What the Knowledge Graph Actually Does

The feature AWS keeps emphasizing is the personal knowledge graph, and it's worth understanding what makes it different from a standard chat-based copilot.

Most AI assistants are stateless by session. You open a chat, provide context, get an answer, and the next session starts from zero. The AI doesn't remember that you have a Q3 pipeline review next week, that your main Salesforce contact at the BMW account is Lena Fischer, or that your team calls the internal metrics dashboard "Northstar."

Quick's knowledge graph is designed to be stateful and cumulative. It ingests from connected sources — local files, calendar, email, Slack history, Salesforce records, Google Workspace documents — and builds a continuously updated map of your people, projects, preferences, and context. The longer you use it, the more it knows. VP of Agentic AI for Business Jigar Thakkar has described the goal as an assistant that knows your brand's style guidelines, your team's terminology, and your working relationships without needing to be told each session.

In practice, this means Quick can answer questions like "What did I commit to in last week's call with GoDaddy?" or "Which tasks in Jira are blocking the Q2 close?" without requiring you to paste in context. It pulls from the graph it has already built.

The knowledge graph also powers proactive behavior. The desktop app monitors your connected sources in the background and can push OS-level notifications — not just respond when asked. A calendar conflict with a high-priority account, an action item buried in a Slack thread that was never converted to a task, a ticket that's been sitting unassigned past SLA — these are the things Quick is supposed to surface before you notice them yourself.

## Integrations

Quick connects to 11+ external services at launch, spanning consumer and enterprise ecosystems:

**Productivity:** Google Workspace (Gmail, Calendar, Drive, Docs, Sheets, Slides), Microsoft 365 (Outlook, Teams, SharePoint, OneDrive)

**Communication:** Slack, Microsoft Teams, Zoom

**Business systems:** Salesforce, ServiceNow, Asana, Jira

**Storage:** Airtable, Dropbox

**Developer tools:** Kiro CLI, Claude Code

The Kiro CLI and Claude Code integrations are notable. They position Quick not just as a business productivity assistant but as context infrastructure for developers — the knowledge graph knows your repositories, your tickets, your team conventions, and your current sprint, so Kiro and Claude Code can work with more context than they'd have in isolation.

AWS also ships two companion products: Quick Flows (multi-step workflow builder, described in plain language) and Quick Automate (background automation across connected tools). The documented example is something like: when a support ticket lands in Zendesk, pull the customer's CRM record, draft a reply, and post a summary to Slack. That's the kind of cross-app orchestration that's genuinely difficult in Copilot or Gemini today, both of which remain more deeply embedded in their respective suites.

## Pricing and Access

Quick starts free — no AWS account required, just an email address. Paid plans start at $20/month, which AWS has positioned deliberately below the $30/user/month band that both Microsoft Copilot and Google Gemini Workspace have settled into.

The free plan is notable because it lowers the evaluation barrier significantly. Most enterprise AI assistants require IT procurement, identity federation, and admin setup before an individual user can try them. Quick's on-ramp is closer to a consumer app: download, sign up with email, start connecting services.

Whether enterprises can actually adopt it at scale through that path, with their own data governance and SSO requirements, is a different question — one AWS hasn't fully answered publicly.

## Enterprise Adoption

The customer list AWS cited at launch is established, not hypothetical: 3M, GoDaddy, AstraZeneca, BMW, Mondelēz International, the NFL, Southwest Airlines, and New York Life. These are not early-stage design partners. Several of these organizations have been running Quick in some capacity before the desktop launch — the April 28 announcement extended the product's footprint to local desktop access, not introduced the first enterprise deployments.

That said, the desktop app itself is in Preview. Production deployments at scale presumably run on the existing browser/API surface; the desktop experience is where AWS is gathering feedback on local file access, proactive notifications, and OS-level integration.

## The Vendor Lock-In Irony

AWS's core positioning for Quick is freedom from vendor lock-in. The argument is that Copilot works best if you're all-in on Microsoft, and Gemini works best if you're all-in on Google — and if your organization runs a mix (Slack + Salesforce + Outlook + Notion + Zendesk, for instance), neither option covers you cleanly. Quick, in this framing, is the neutral layer that works across the whole stack.

The irony is worth naming: "escape vendor lock-in" being sold by Amazon, the world's largest cloud provider and the company running the infrastructure for most of those apps anyway. AWS has plenty of its own lock-in dynamics once an organization is deeply in — IAM, Bedrock, S3, CloudFront, and now Quick as the orchestration layer.

That doesn't mean Quick isn't genuinely useful for cross-vendor shops. It may well be. But the positioning requires some scrutiny, especially as AWS adds Quick Flows and Quick Automate as automation surfaces where your workflow logic increasingly lives on Amazon's infrastructure.

An emerging pattern worth watching: some large enterprises are apparently running both. Copilot or Gemini for productivity inside a suite (Excel, Docs), and Quick for orchestration across tools. The use cases may be complementary enough that this isn't absurd — Copilot inside a spreadsheet and Quick routing a Salesforce ticket to Jira are different jobs. Whether the cost of two $20-30/user/month subscriptions justifies the coverage is an ROI question each organization has to answer.

## What Quick Is and Isn't

The knowledge graph concept is genuinely differentiated from what Copilot and Gemini offer today. Stateful, cumulative context that compounds over time — rather than resetting each session — would be a meaningful improvement to how AI assistants work in practice. Whether Quick actually delivers this in production, and how well the knowledge graph holds up as it grows, are things that will emerge from real deployment data, not launch announcements.

The proactive notifications model is also a real bet. Most enterprise AI tools are reactive: you ask, they answer. Building an assistant that surfaces things before you ask is a harder problem and requires the system to be meaningfully accurate about what actually needs your attention. Too many false positives and users turn it off. Too few and it's just a fancier search box.

Quick Flows and Quick Automate add workflow automation that Microsoft and Google are still maturing in their own platforms. This is the most ambitious part of the product story — and the one with the most distance to go before it's enterprise-production-ready across the heterogeneous app stacks it's targeting.

## Bottom Line

Amazon Quick launched on April 28 with a clear thesis: your AI assistant should know who you are, what you're working on, and what needs your attention — across every tool you use, not just one vendor's suite.

The knowledge graph approach is the right architectural bet for a cross-vendor AI layer. The integrations list is broad enough to cover most enterprise software stacks. The pricing undercuts the established competition. And the free tier removes the friction that usually delays evaluation.

What's unproven is whether the knowledge graph actually works as described at scale, whether proactive notifications hit the right threshold of useful vs. noisy, and whether organizations will add Amazon as a third major AI vendor alongside whatever Microsoft and Google subscriptions they already run.

Amazon Quick is available now in Preview at no cost. That's the lowest-friction way to find out.

---

*Amazon Quick is a commercial product from Amazon Web Services. ChatForest researched this article from published sources and has not tested Quick directly. This article is part of our ongoing coverage of [AI tools and platforms](/categories/ai-tools/).*

