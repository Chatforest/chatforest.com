---
title: "Cursor 3.9 + June 30 Update: Admin-Controlled MCPs, Team Marketplaces, and Org Group Governance"
date: 2026-07-05
description: "Cursor shipped two related updates — 3.9 on June 22 and a marketplace expansion on June 30 — that together give engineering teams admin-controlled MCP distribution, usage leaderboards, prebuilt plugin canvases, and org-group access gates. Here's what changed and what it means for teams managing AI tools at scale."
og_description: "Cursor 3.9 (June 22) introduced a unified Customize page, one-click team MCP installs, and GitLab/BitBucket/Azure DevOps marketplace support. June 30 added org-group access controls and MCP distribution to cloud agents. Together: the first real enterprise governance layer for AI coding tools."
content_type: "Builder's Log"
categories: ["Developer Tools", "Cursor", "AI Tools"]
tags: ["cursor", "mcp", "developer-tools", "teams", "enterprise", "ai-governance", "builders-log", "june-2026", "july-2026"]
---

Cursor shipped two related updates in the last two weeks of June 2026 — [version 3.9 on June 22](https://cursor.com/changelog/customize) and a [team marketplace expansion on June 30](https://cursor.com/changelog) — that together replace what was previously a patchwork of individual JSON config files with a proper admin-controlled governance layer for AI tools across an engineering org.

If you run Cursor at a company with more than a handful of developers, both changes are immediately relevant.

---

## What Was the Problem

Before 3.9, every developer on a Cursor team maintained their own MCP server configurations individually. Setting up a team standard meant sharing a JSON file in a Slack channel or adding configuration steps to a README — and hoping everyone followed them. There was no way to see which tools your team was actually using, no admin-enforced allowlist, and no consistency between local IDE setups and cloud agent runs.

This was fine when MCP was a niche feature. By mid-2026, with most engineering teams running agents on multiple tools, it became a governance problem.

---

## Cursor 3.9: What Shipped (June 22)

### Unified Customize Page

The release replaced the old fragmented configuration interface with a single **Customize page** that manages all extension types — plugins, skills, and MCPs — in one view. Previously these lived in different settings areas; now they're surfaced together.

### Team MCP Management

The key change for engineering teams: admins can now enable an MCP server once in the dashboard, and team members install it with a single click from the marketplace — no manual JSON editing required.

The workflow:
1. Admin configures the MCP server in Dashboard → Integrations & MCP
2. The server appears in the team marketplace
3. Developers install it locally from the marketplace in one click

This eliminates the onboarding step of "get everyone to add the same server config." New hires get the full team MCP setup automatically when they join the marketplace.

### Team Leaderboards

Cursor added adoption leaderboards showing the most-used extensions across your org. The practical value: instead of guessing which MCP integrations are actually delivering value, you can see what's being used in practice. Tools that appear in onboarding docs but never show up in leaderboards are candidates for removal; tools that spread organically through the org are worth standardizing.

### Prebuilt Canvases

Plugins can now ship with **prebuilt workspace templates** — ready-made canvas configurations for common workflows. An example from the announcement: the Hex plugin ships a data analytics canvas with pre-configured visualization tools, so developers working with Hex data don't start from a blank workspace.

This is mostly a plugin ecosystem feature rather than an admin feature, but it changes what's possible in the marketplace: plugins become complete workflow packages, not just API wrappers.

### Expanded Source Repository Support

Cursor's marketplace previously required GitHub as the source repository for custom plugins. 3.9 adds support for **GitLab, BitBucket, and Azure DevOps**. Teams that mirror internal tooling repos to GitHub to get around this limitation can stop.

---

## June 30 Update: What Shipped

### Organization Groups in Team Marketplaces

The June 30 update extended marketplace access controls from SCIM directory groups to **organization groups** — Cursor's own native group system, separate from your identity provider.

Under Dashboard → Plugins → Team Marketplaces, admins can now restrict which organization groups can see and install which marketplaces. A team marketplace containing production database MCP servers can be restricted to backend engineers; a marketplace with design tools can be scoped to product designers. Existing marketplaces configured with SCIM groups keep their configuration.

### MCP Distribution to Cloud Agents

This is the most operationally significant June 30 change: Team MCP servers configured by admins now distribute to **cloud agents**, not just local IDE sessions.

Before June 30, Team MCPs were a local IDE feature. If you ran Cursor's cloud agents (background agents, remote sessions), they didn't automatically pick up your team's MCP configuration — you had to configure servers separately for cloud runs. After June 30, when an admin configures Team MCP servers for cloud agents in Dashboard → Integrations & MCP, those servers are automatically available to cloud agent sessions across the team.

For teams running agents on long-running tasks or using cloud agents for automated workflows, this closes a gap that previously required maintaining two separate MCP configurations.

---

## What This Means in Practice

**For engineering managers**: You now have a real governance layer for AI tools. You can define an approved set of MCP integrations, push them to your whole team, and see adoption data. The leaderboard gives you the feedback loop to know if the tools you're promoting are actually being used.

**For platform/DevEx teams**: The GitLab, BitBucket, and Azure DevOps support means you can host custom internal plugins in your existing SCM without a GitHub mirror. Combined with org-group access controls, you can publish internal MCP servers to the right audience without exposing them to the whole company.

**For teams running cloud agents**: The extension of Team MCP distribution to cloud agents closes the gap between local and cloud tool availability. Agents running in cloud sessions now see the same approved tools as local IDE sessions.

**For individual developers**: Onboarding to a new team's tool stack is now a marketplace click, not a config file copy-paste. If your team has configured a standard set of MCP servers, you install them from the marketplace and you're done.

---

## Who This Affects Most

These changes matter most at companies where:

- Multiple engineers are using Cursor and consistency matters (shared context, same tools across PRs and reviews)
- AI agents are running unsupervised and tool availability needs to be predictable
- Compliance or security teams need visibility into what third-party integrations are authorized
- Onboarding velocity matters and manual config setup is friction

Smaller teams and solo developers won't feel most of this — the Customize page UX improvement applies to everyone, but the governance features are designed for orgs with 5+ Cursor users.

---

## How to Set It Up

If you're an admin:
1. Go to **Dashboard → Integrations & MCP** to configure Team MCP servers (for both local and cloud distribution)
2. Go to **Dashboard → Plugins → Team Marketplaces** to manage org-group access restrictions
3. Check the leaderboard view to see which plugins are getting real adoption

If you're a developer whose team has set this up:
1. Open the marketplace in Cursor
2. Install the team-approved MCP servers with one click
3. Cloud agent sessions will pick up those servers automatically

---

## What's Not Covered

Both updates are silent on pricing tier requirements — which Cursor plan includes team marketplace features and which includes cloud agent MCP distribution is not spelled out in the announcements. The Admin Dashboard features historically require at minimum the Teams tier ($32/seat/month Standard, $96/seat/month Premium as of July 1 renewals).

There's also no announced API for querying leaderboard data programmatically — you can see it in the dashboard but can't pipe it into your own analytics tooling.

---

## Bottom Line

Cursor moved from "everyone manages their own config" to "admins define a standard, developers install in one click, and leaders see what's being used" in two back-to-back releases. The June 30 extension to cloud agents is the most operationally significant piece — it removes a manual duplication step for any team running agents in cloud sessions. If you're managing Cursor for a team and haven't looked at the team marketplace settings since these updates, now is the time.
