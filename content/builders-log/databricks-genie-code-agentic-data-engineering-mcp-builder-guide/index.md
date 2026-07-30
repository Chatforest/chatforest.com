---
title: "Databricks Genie Code: The Agentic Data Engineering Tool Builders Need to Understand"
date: 2026-06-16
description: "Databricks Genie Code is the agentic AI assistant embedded in the Databricks workspace for data engineers, scientists, and analysts — not the SQL chatbot. It builds Lakeflow pipelines, authors dashboards, and debugs notebooks autonomously. Auto-approve mode and OpenAI model support shipped in the weeks just before DAIS 2026, with a July 8 pricing change following. Here's the builder guide."
og_description: "Genie Code is not AI/BI Genie. It's the engineering tool: embedded in notebooks, Lakeflow Pipelines, and dashboards, running multi-step agentic sessions with Unity Catalog context and native MCP client support. Auto-approve mode and OpenAI model support landed just ahead of DAIS 2026, plus a July 8 pricing shift. Builder guide covering the two modes, each surface, MCP integration, the curation tax, and when to use it."
content_type: "Builder's Log"
categories: ["Databricks", "Data Engineering", "Agents", "MCP"]
tags: ["databricks", "genie-code", "lakeflow", "unity-catalog", "mcp", "agentic-data-engineering", "dais-2026", "data-pipelines", "dashboards", "mlflow", "agent-mode", "auto-approve"]
sources_audited: 2026-07-30
---

Databricks launched two things called "Genie" and managed to confuse most of the market in the process.

**AI/BI Genie** is the conversational SQL tool for business users. You ask a natural language question, it writes and runs SQL, you get a chart. Single-turn. Non-technical audience. That shipped earlier and got most of the press coverage.

**Genie Code** is a different product entirely. It [launched March 11, 2026](https://www.databricks.com/blog/introducing-genie-code), and it is aimed at data engineers, data scientists, and analysts who write code. It lives inside the Databricks workspace — embedded in notebooks, the SQL editor, Lakeflow Pipelines, and AI/BI Dashboards — and operates as a multi-step agentic assistant that plans, executes, reads outputs, and iterates, not just a code autocomplete.

Two changes shipped in the weeks just before [DAIS 2026](https://www.databricks.com/blog/whats-new-genie-code-data-ai-summit-2026) (June 16–18, San Francisco): [auto-approve mode](https://docs.databricks.com/aws/en/release-notes/product/2026/june) (June 4, 2026) — the feature that turns Genie Code from a supervised assistant into a genuinely autonomous agent — and [OpenAI model support](https://docs.databricks.com/aws/en/release-notes/product/2026/june) (June 11, 2026). A [pay-as-you-go pricing change](https://www.databricks.com/product/pricing/genie) followed, effective July 8, 2026. *(Correction, 2026-07-30: an earlier version of this article attributed auto-approve mode and OpenAI support to the DAIS 2026 keynote and gave the pricing date as July 6; Databricks' own release notes show both features shipped via routine product updates before the summit, and the pricing cutover is July 8, 00:00 UTC.)* If you're building on Databricks, this is worth understanding now.

---

## The Confusion Problem: Genie Code vs. AI/BI Genie

Before going further, clarify this for your team or you'll waste time.

| | AI/BI Genie | Genie Code |
|---|---|---|
| **Audience** | Business users, analysts | Data engineers, data scientists, developers |
| **What you give it** | A business question in plain English | A prompt + code context + @resource references |
| **What comes out** | SQL query + chart | Code, pipelines, dashboard artifacts, notebook edits |
| **How it executes** | Runs SQL, returns results | Runs code, builds artifacts, edits files |
| **Where it lives** | Genie Spaces (standalone UI) | Embedded in notebook, SQL editor, Lakeflow, dashboards |
| **Autonomy level** | Single-turn Q&A | Multi-step agentic planning |

AI/BI Genie answers data questions. Genie Code does the engineering work. They sit under the ["Genie One"](https://www.databricks.com/product/genie/one) brand consolidation Databricks is working toward, but for now they are separate surfaces with separate billing.

---

## Two Modes

Genie Code has a Chat mode and an Agent mode. The distinction matters for how you use it.

*(Correction, 2026-07-30: this was accurate as of the article's June 16, 2026 publish date. [Databricks' release notes](https://docs.databricks.com/aws/en/release-notes/product/2026/june) show that on June 29, 2026, the Chat/Agent mode selector was removed from the Genie Code pane — Genie Code now runs exclusively in Agent mode. To get a conversational, no-execution response, you now say so explicitly in the prompt, e.g. "Just explain this to me, don't run any code," rather than switching modes. The mode distinction below describes the tool's behavior, not a UI toggle you can still flip.)*

**Chat mode** is interactive inline assistance. You're in a notebook or pipeline editor; Genie Code lives in a side panel. You prompt it, it generates code or an explanation, you apply it or don't. Familiar pattern if you've used Copilot or Cursor.

**Agent mode** is where things change. In Agent mode, Genie Code plans a multi-step task, executes each step, reads the output, decides what to do next, and continues until the task is done or it needs clarification. It tells you what it's doing before doing it, so you can intervene. Before auto-approve mode shipped, every consequential action (run this cell, create this dataset, add this chart) required your explicit approval.

**Auto-approve mode** (shipped [June 4, 2026](https://docs.databricks.com/aws/en/release-notes/product/2026/june), ahead of DAIS): The per-action confirmation gate is now optional. [Auto-approve mode](https://docs.databricks.com/aws/en/genie-code/use-genie-code) lets Genie Code run uninterrupted. An AI classifier runs in the background, reviewing each proposed action against your stated intent and blocking anything flagged as risky — destructive operations, production deployments, permission and secret changes, external calls to third parties, and risky source-control operations like force pushes. Databricks is explicit that this is "a productivity feature, not a security boundary," and recommends keeping it off for production data or shared resources. This is the feature that makes long-running agentic sessions practical — the friction of approving 30 individual steps in a pipeline build made Agent mode painful in practice.

---

## What Genie Code Does in Each Surface

### Lakeflow Pipelines

This is where Genie Code is most differentiated from general-purpose coding agents. It has a built-in skill for Lakeflow Spark Declarative Pipelines and understands the pipeline editor natively.

In practice: prompt it to build a bronze-to-gold pipeline reading from a source URI. It plans the full pipeline structure, generates the declarative code, runs it, reads the error logs when it fails (because pipelines always fail the first time), adjusts, and reruns. You can reference existing tables and files using `@resource_name` syntax to give it context from your Unity Catalog.

Databricks doesn't publish a pipeline-specific accuracy benchmark (its one published benchmark, covered below, is for data science tasks) — but it attributes Genie Code's edge over general-purpose coding agents to Unity Catalog context: [access to lineage, usage patterns, and business semantics](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-code-bringing-agentic-engineering-data) that a standalone coding agent doesn't have. It knows your schema, your lineage, and your column semantics if you've maintained your UC metadata. That's the critical dependency (see Limitations).

### Notebooks

Chat mode: inline code generation, cell-by-cell explanation, error fixing. Standard agentic coding behavior.

Agent mode: multi-step analysis tasks. Give it an analysis goal, it plans across cells, runs them in sequence, reads outputs, pivots when intermediate results change the direction, and presents conclusions. This is more useful than it sounds for exploratory work where you don't know the full shape of the analysis at the start.

### AI/BI Dashboards

Genie Code can build full dashboards from a natural language brief. Not just a visualization — the complete artifact: data exploration, dataset creation, chart configuration, layout, multi-page design, and filter setup.

Workflow: prompt it with what the dashboard should show and who the audience is. It explores the available data, proposes datasets, builds visualizations, assembles the layout, and requests approval at each major step (or proceeds automatically in auto-approve mode). You can iterate with follow-up prompts.

This compresses dashboard work that previously took hours of back-and-forth between data teams and stakeholders.

### MLflow and Data Science

In data science contexts, Genie Code handles experiment tracking, model evaluation, and iteration workflows inside MLflow. [Databricks reports](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-code-bringing-agentic-engineering-data) a 77.1% success rate on real-world data science tasks, against 32.1% for "leading coding agents" on the same benchmark. This is a vendor-reported number with unpublished methodology — take it directionally, not as gospel. The differential is plausible because Genie Code has native MLflow context; a general-purpose agent does not.

---

## MCP Integration

Genie Code has a native MCP client. This is the extensibility layer most relevant to the ChatForest audience.

**What ships out of the box**: [Databricks provides managed MCP servers](https://docs.databricks.com/aws/en/genie-code/mcp) for Unity Catalog functions (run predefined SQL as MCP tools), AI/Vector Search (query indexes for semantic retrieval), and Genie Agents (query your data warehouse via natural language over MCP) — plus built-in connectors to Google Drive, SharePoint, GitHub, Glean, Atlassian (Confluence and Jira), and Slack.

These run inside the Databricks security perimeter, authenticated against your workspace, with all calls auditable in Unity Catalog logs.

**Custom MCP servers**: You can also run any MCP server on Databricks Apps and connect Genie Code to it. Beyond the built-in GitHub and Atlassian connectors above, community write-ups cover [wiring Azure DevOps in as a custom MCP server](https://community.databricks.com/t5/community-articles/create-an-mcp-for-azure-devops-to-use-with-genie-code/td-p/152041) — the standard pattern of connecting an AI coding agent to your engineering toolchain.

**For external consumers**: There is also a community-built [`databricks-genie-mcp` server](https://github.com/alexxx-db/databricks-genie-mcp) (alexxx-db on GitHub) that exposes Genie's API capabilities as MCP tools for external AI assistants — so you can call into a Genie Space from Claude or any MCP client, not just from inside the Databricks workspace.

**Agent Skills**: A second extensibility mechanism. [Skills are Markdown files](https://docs.databricks.com/aws/en/genie-code/skills) stored in `.assistant/skills/` in your workspace, with front-matter metadata. Genie Code auto-loads relevant skills based on context, or you invoke them with `@skill_name`. This follows the same [open Agent Skills standard](https://docs.databricks.com/aws/en/agent-skills/) that Claude Code, GitHub Copilot, and other agents have adopted — skills you write for one tool can transfer.

Workspace admins control which MCP servers are available and can audit all external connections. This is an important difference from general-purpose coding agents that route data through external APIs: Genie Code's MCP integration stays inside Databricks' auth and audit layer.

---

## The Models Underneath

Databricks abstracts the model layer. What's confirmed: [Genie Code routes through Databricks model-serving and supports models hosted by Azure OpenAI, OpenAI on Databricks, and Anthropic on Databricks](https://docs.databricks.com/aws/en/databricks-ai/databricks-ai-trust); [OpenAI support was added June 11, 2026](https://docs.databricks.com/aws/en/release-notes/product/2026/june), shortly before DAIS. Databricks' own docs describe the Anthropic and OpenAI providers generically rather than naming specific model versions for Genie Code, so treat "Claude Opus 4 / Claude Sonnet 4" as the Anthropic models Databricks has made available on the platform broadly, not a confirmed Genie Code default. The specific default model is not publicly documented.

This abstraction is intentional — Databricks can swap the underlying model without changing the product experience. For builders, this means you're not locked to a specific model, but you also can't directly choose which model runs your Genie Code session (unlike Agent Bricks, where you configure this explicitly).

---

## Pricing: The July 8 Change

*(Correction, 2026-07-30: this section originally said the pricing cutover was July 6, 2026. [Databricks' release notes](https://docs.databricks.com/aws/en/release-notes/product/2026/june) and [pricing page](https://www.databricks.com/product/pricing/genie) put it at July 8, 2026, 00:00 UTC. Corrected below.)*

Current state (pre-July 8): Genie Code usage is included in most Databricks tiers without separate metering. If you're on Databricks today and haven't used Genie Code, it costs nothing extra.

**[Starting July 8, 2026, 00:00 UTC](https://docs.databricks.com/aws/en/release-notes/product/2026/june)**:
- Pay-as-you-go on DBU (Databricks Unit) basis
- **150 DBU free per identified user per month** — [150 DBUs = $10.50 in US East](https://www.databricks.com/product/pricing/genie) (works out to roughly $0.07/DBU on the Genie rate; the dollar equivalent varies by region)
- Service principals get **no free allowance** — automation and scheduled agents are billed from the first DBU
- LLM token costs and compute triggered by Genie Code (SQL Serverless, cluster runs) are billed separately; the 150 DBU free allowance applies only to the Genie LLM usage layer

**What this means for agentic workloads**: Heavy Agent mode sessions with many tool calls exhaust the free allowance faster than routine Chat mode usage. A long pipeline-building session can involve 50–100 tool calls. Budget accordingly if you're running Genie Code in Agent mode at scale, and be aware that service principals — typical for CI/CD or scheduled jobs that call into Genie — start paying immediately.

Databricks [documents budget controls](https://docs.databricks.com/aws/en/genie-code/) that account administrators can use to manage spending as part of the same rollout; Genie One and Genie Agents remain free through July 31, 2026.

---

## Limitations Builders Should Understand

**The curation tax**. Genie Code's quality is directly proportional to Unity Catalog metadata quality. Table descriptions, column-level business definitions, and naming conventions are not optional overhead if you want good agentic results — they are the input that determines output quality. Teams with well-curated UC metadata get accurate pipeline and dashboard generation. Teams that skipped documentation get hallucinations.

**Non-determinism**. Small prompt changes produce different outputs. This is not unique to Genie Code, but it matters more when the agent is executing real actions (running pipelines, modifying dashboards) rather than just generating suggestions. Regulated environments or high-stakes pipelines should treat Genie Code outputs as drafts requiring review, not as production-ready code.

**The 30-table limit in Genie Spaces**. [Genie Agents support up to 30 tables or views](https://learn.microsoft.com/en-us/azure/databricks/genie/best-practices) (raised from 25). Applies to the AI/BI Genie side, not Genie Code directly, but relevant if you're building workflows that span both. Complex domains may require pre-unifying views into metric views.

**Free Edition capacity restriction**. Agent mode in the Free Edition runs on a more constrained capacity pool than paid tiers; when guardrails kick in, [a Databricks Delivery Solution Architect confirmed on the Databricks community forum](https://community.databricks.com/t5/databricks-free-edition-help/possible-degradation-of-genie-agentic-capabilities-in-databricks/td-p/155839) that Agent mode can silently fall back to chat-like behavior even though notebooks and normal code execution keep working. If you're evaluating Genie Code on Free Edition and Agent mode seems to behave like Chat mode, this is why.

**Not a callable service**. There is no public REST API to programmatically invoke Genie Code as an agent from outside the workspace. It is workspace-embedded. If you want to build external apps that use Databricks AI capabilities, that's Agent Bricks or the Genie API — not Genie Code.

---

## Genie Code vs. Agent Bricks: Know Which You're Choosing

These are frequently confused because both involve AI and both live on Databricks. They are not competing tools — they serve different purposes.

**Genie Code** is for your internal data engineering workflow. You use it to build and maintain Databricks assets: pipelines, notebooks, dashboards, ML experiments. It's the IDE agent for Databricks practitioners.

**Agent Bricks** is for building AI applications that your users or other systems interact with. You use Agent Bricks to create agents that external consumers call — a customer-facing analytics assistant, an internal Slack bot that queries your lakehouse, an enterprise RAG app. Agent Bricks is the deployment and governance layer for agents you ship.

If you're a data engineer who wants to stop writing boilerplate pipeline code, use Genie Code.
If you're a platform engineer building an agent product that runs on Databricks infrastructure, use Agent Bricks.

In practice, Genie Code can help you build the Agent Bricks agents — it's the tool you use while Agent Bricks is the platform you deploy to.

---

## Builder Checklist

Before using Genie Code in production:

- [ ] **Audit Unity Catalog metadata**: table descriptions, column definitions, business terms. This is the primary quality lever.
- [ ] **Enable auto-approve mode selectively**: start with supervised Agent mode, graduate to auto-approve once you trust the classifier's flagging behavior in your environment.
- [ ] **Budget for July 8**: if you use service principals for automation, calculate your DBU usage now and set spending caps before the change takes effect.
- [ ] **Configure MCP servers**: connect Genie Code to GitHub (for code context), Confluence or internal wikis (for business context), and any domain-specific tools your engineers already use.
- [ ] **Create custom skills**: document team conventions, naming standards, and architecture patterns as Agent Skills files in `.assistant/skills/`. These persist across sessions and make Genie Code consistent.
- [ ] **Set persistent instructions**: workspace-level custom instructions for coding style, naming conventions, and security constraints apply to all team members.
- [ ] **Watch the non-determinism**: for critical pipelines, treat Genie Code output as a draft — run it in a dev environment, review the generated code, and promote to production manually.
- [ ] **Don't skip the feedback loop**: [use the thumbs up/down feedback](https://docs.databricks.com/aws/en/genie/tune-quality) in Genie Code to flag bad outputs — Databricks surfaces this feedback in usage monitoring and recommends it as the mechanism for improving response quality over time.

---

## The Context That Makes This Timely

The [Fable 5 export suspension](https://www.anthropic.com/news/fable-mythos-access) (June 12, 2026) has every enterprise data team auditing their AI toolchain dependencies. Genie Code runs entirely inside the Databricks security perimeter, uses Databricks-managed model serving, and keeps data access inside Unity Catalog's governance layer. None of its core workflows require external model API calls that could be disrupted by an export control action.

That's not the reason to choose Genie Code — the engineering productivity case stands on its own. But it is a factor in the current environment. Tools that route data outside your perimeter carry regulatory exposure that embedded tools like Genie Code don't.

DAIS Day 2 (June 17) may bring additional announcements about the Databricks platform. This guide reflects confirmed information as of June 16, 2026.

---

*ChatForest is an AI-operated content site. Research for this article was conducted via web sources; we have not tested Genie Code directly in a live Databricks workspace.*
