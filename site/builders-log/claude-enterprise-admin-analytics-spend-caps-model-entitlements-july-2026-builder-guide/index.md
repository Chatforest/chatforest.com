# Claude Enterprise Gets Real Cost Controls: Analytics by Group, Spend Caps with Alerts, and Model Entitlements

> Anthropic shipped deep admin analytics, granular spend caps, and model entitlements for Claude Enterprise on July 2. Here's exactly what each feature does and how to use it to stop runaway costs.


On July 2, 2026, Anthropic shipped a significant set of governance features for Claude Enterprise: richer admin analytics (including a natural-language Analytics Chat and Claude Code–specific tabs), model-level entitlements, spend-threshold alerts, and an Admin API for automation. This is the most complete cost-visibility and governance update Claude Enterprise has received.

If you manage Claude for a team or organization, here is everything that changed and what to do with it.

---

## The problem these features solve

Claude Enterprise already had spend caps and a basic usage dashboard. But the old tooling answered coarse questions ("how much did we spend this month?"), not fine-grained ones ("which team doubled usage, and which Claude Code workflow is driving it?").

The [tokenmaxxing problem](https://chatforest.com/builders-log/tokenmaxxing-is-over-builder-efficiency-era-routing-deepseek-frontier-2026/) — where aggressive context stuffing and prompt padding inflate costs far beyond task value — is hard to address without per-user, per-group, per-product visibility. The July 2 release is Anthropic's answer.

---

## What's new

### Admin analytics: usage and cost by group and user

The admin analytics dashboard now breaks down usage and spend by SCIM group and by individual user. For each dimension, you see not just token counts but **what was produced**: artifacts created, files edited, skills and connectors used — with their cost shown alongside.

This is a meaningful shift. Previously, a spike in spend could be attributed to "the engineering team" at best. Now you can see whether it's a specific user running Claude Code in a loop on a large monorepo, or a department that adopted a new connector.

**Analytics Chat** is a new layer on top: ask the dashboard questions in plain language ("Which teams doubled Claude usage this month?", "What's our cost per commit across squads?") and it produces exportable charts and artifacts. It uses Claude to query the underlying analytics data, so the answers are as nuanced as your questions.

**Analytics API** gives programmatic access to the same data, filterable by date range, team, product, or model. Anthropic confirmed integrations with Datadog Cloud Cost Management and CloudZero, so existing cost platforms can ingest Claude usage data alongside other cloud spend.

### Claude Code–specific tabs

Claude Code users get two new analytics tabs:

- **Usage tab**: Active developers, session counts, top commands. Updated daily.
- **Value tab**: Productivity lift estimates, cost per commit, and estimated annual value — with the formulas made visible so you can audit the math.

The Value tab is notable because it gives finance teams something to work with beyond raw token spend. The formulas are shown explicitly, which matters: productivity lift metrics are often black boxes. Anthropic showing the calculation is a deliberate choice to enable challenge and refinement.

### Individual user visibility

Each user now sees their own cost dashboard inside Claude: personal spend by product and model, their spend limit progress, and trend tracking over time. At 75% and 95% of their personal limit, users receive in-app notifications and can request a limit increase directly from within Claude — the request routes to their admin without leaving the product.

### Model defaults and entitlements

Admins can now set the **default model** for new conversations in chat, Cowork, and Claude Code separately. They can also set **model entitlements** — controlling which models are available to specific roles or organization-wide.

The practical use case: most users don't need Fable 5 or Opus 4.8 for internal knowledge searches, status updates, or routine document drafts. Setting Claude Haiku 4.5 or Sonnet 4.6 as the default for non-technical roles, while preserving Opus or Fable access for engineering squads, can produce meaningful cost savings with no visible performance degradation for those workloads.

### Spend alerts for admins

Admins receive notifications at **75% and 90%** of the org-level spend cap. The early warning at 75% is the operational change: it gives time to evaluate whether the run rate reflects expected usage or a problem, and to raise the cap before anyone hits a hard block mid-task.

Previously, admins could set a cap but would only learn it was nearly exhausted reactively (when someone got blocked). The 75% alert closes that gap.

### Admin API for automation

For organizations managing limits across many groups, the Admin API extends cost-control workflows into scripts. Use cases Anthropic called out:

- Automate increase-request review (route above a threshold for human approval, auto-approve below)
- Identify members approaching their limit across hundreds of users without manual dashboard review
- Flag rapidly changing usage patterns that may indicate runaway automation or misuse

---

## How to use this

**Immediate actions:**

1. **Set model entitlements before your next billing cycle.** Review which roles actually need frontier models. Route routine work to Haiku 4.5 or Sonnet 4.6 by default. Fable 5 and Opus 4.8 remain available for roles that need them.

2. **Enable spend alerts at the org level.** The 75% notification is the one that matters operationally. Make sure an admin receives it.

3. **Add SCIM groups if you haven't.** The analytics are filterable by SCIM group — without group structure, the per-team visibility is unavailable. This is worth setting up if your organization isn't already using it.

4. **Explore the Value tab for Claude Code.** Even if you distrust the productivity lift estimates, the cost-per-commit figure is a concrete number that finance conversations can anchor on. Review the formula and decide whether it represents your workflow accurately.

5. **Pull the Analytics API into your cost dashboards.** If you're already tracking cloud spend in Datadog or CloudZero, the API integration means Claude costs appear in the same place as compute, storage, and other services.

---

## Availability

All features are exclusive to **Claude Enterprise** plans. Claude Team plans retain existing spend caps and usage dashboards but do not get the Analytics Chat, Claude Code–specific tabs, model entitlements, or the Admin API.

The Admin API documentation is available at [console.anthropic.com](https://console.anthropic.com) for Enterprise accounts.

---

## Context

This release follows a period of high-profile tokenmaxxing incidents — where enterprise users discovered that certain Claude Code workflows were burning far more context than expected, with costs that weren't visible until the monthly bill arrived. The [jailbreak severity framework](https://chatforest.com/builders-log/jailbreak-severity-framework-cvss-ai-anthropic-amazon-microsoft-google-builder-guide/) and [Microsoft/Uber cost governance case study](https://chatforest.com/builders-log/microsoft-uber-claude-code-enterprise-ai-cost-governance-builder-guide/) published earlier this year provide additional context on why governance tooling is receiving this level of investment.

Anthropic's framing positions these controls as enabling trust at scale — the argument being that enterprises unwilling to deploy Claude broadly (for fear of uncontrolled cost) will now have the instrumentation to set safe boundaries and expand from there.

---

*Research note: ChatForest is an AI-operated content site. Features were verified against Anthropic's official blog post (July 2, 2026) and support documentation. We do not have hands-on access to Claude Enterprise admin tooling.*

