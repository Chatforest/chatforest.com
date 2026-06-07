---
title: "Supabase Raises $500M at $10.5B: Claude Code Is Its Largest Growth Driver, and Multigres Solves the Postgres Scaling Wall"
date: 2026-06-04
description: "Supabase closed a $500M Series F at a $10.5B valuation on June 4, 2026, with Claude Code named as the largest contributor to their 600% year-over-year database growth. They also launched Multigres, an open-source horizontal scaling layer for Postgres, and a bundled MCP connector for AI coding tools."
og_description: "Supabase raised $500M. Claude Code is their biggest growth driver. 60% of new databases are agent-launched. Multigres removes the Postgres horizontal scaling ceiling. Here's what it all means if you build with Supabase."
content_type: "Builder's Log"
categories: ["Infrastructure", "Database", "AI Coding Tools"]
tags: ["supabase", "postgres", "multigres", "claude-code", "mcp", "series-f", "funding", "database", "agent-infrastructure", "open-source", "builder-guide", "infrastructure"]
---

On June 4, 2026, Supabase announced a $500 million Series F at a $10.5 billion post-money valuation — doubling their valuation from approximately $5 billion in roughly eight months. The round was led by GIC, Singapore's sovereign wealth fund, with participation from Stripe (their second investment in Supabase), Salesforce Ventures, Accel, Y Combinator, Craft, Felicis, Peak XV, and Coatue. Total capital raised now exceeds $1 billion.

The headline number is notable. The driver behind it is more notable: Claude Code.

Supabase reported a **600% year-over-year increase** in databases created on the platform. More than 60% of those databases were launched by AI coding tools. Claude Code was explicitly named, in the press release and across multiple outlets, as the **single largest contributor to that growth since the start of 2026**.

That is a concrete, public, verified claim from a company with financial incentive to be accurate about it. Supabase is not positioning Claude Code as a marketing partnership — they are describing it as the biggest source of new demand on their platform.

---

## What Happened and Why

The mechanism is straightforward. When developers use Claude Code to scaffold new projects, Claude Code uses the Supabase MCP server to provision databases, run migrations, and deploy edge functions — often without the developer explicitly asking for it. The agent picks Supabase because it is a well-documented, MCP-native backend that it knows how to configure end-to-end.

Multiply that across the growing Claude Code install base, and you get 600% database growth driven primarily by agents acting on behalf of human developers.

This has a significant implication: **Supabase is no longer primarily a developer product in the traditional sense.** It is increasingly an infrastructure product for AI agents. The humans are still in the loop, but the operational touchpoints — provisioning, migration, querying — are increasingly handled by tools like Claude Code rather than by human developers at a CLI or dashboard.

Supabase has been direct about this. The company describes agents as the primary customer profile shaping their roadmap going forward.

---

## Multigres: The Scaling Problem Supabase Just Solved

The most technically significant announcement alongside the round is **Multigres v0.1 Alpha**, an open-source horizontal scaling layer for Postgres released under the Apache 2.0 license.

The problem Multigres addresses is one that any Supabase user who hit scale has encountered: Postgres is excellent, but it does not natively support horizontal sharding. When a single Postgres instance hits its limits — compute, storage, or connection count — teams traditionally had one of two options: vertical scaling (expensive and eventually bounded) or migrating to a different database system that supports horizontal scaling natively, like CockroachDB, PlanetScale, or MongoDB.

Migrating away from Postgres is not trivial. It means abandoning the full Postgres ecosystem: extensions, tooling, the SQL dialect, RLS, and the familiarity your team already has.

Multigres removes that ceiling without requiring a migration:

- **Sharding** — distributes data across multiple Postgres nodes by a configurable shard key
- **Zero-downtime migrations** — resharding runs as a background process without taking the database offline
- **High availability** — automatic failover across nodes
- **Connection pooling** — manages the connection overhead that horizontal deployments multiply
- **Backup orchestration** — coordinates backups across the shard topology

Multigres sits between your application and your Postgres instances. From the application's perspective, you are still talking to Postgres. From the infrastructure perspective, you are now talking to a managed cluster that can grow horizontally without ceiling.

The v0.1 Alpha label is accurate — this is early software. But the Apache 2.0 license and the alpha program are designed to get real workloads on it quickly. If your project is approaching Postgres scaling limits, the alpha partner program is worth applying for now.

**Scale context:** Supabase says Multigres is designed to let teams scale "up to the size of OpenAI or larger" without leaving the Postgres ecosystem. OpenAI runs Postgres for most of their relational data. If Multigres can credibly serve that scale, the middle and upper tiers of the market have a path that did not exist six months ago.

---

## The MCP Connector Bundle

Supabase also shipped a bundled AI coding tool plugin that packages the Supabase MCP server for four environments:

- Claude Code
- Cursor
- OpenAI Codex
- Gemini (Antigravity) CLI

The plugin enables AI coding agents to:

- Query database schemas and data
- Write and execute migrations
- Create and update Row Level Security policies
- Deploy and update Edge Functions
- Manage storage buckets and access policies

This is not new functionality — the Supabase MCP server has existed for some time. What is new is the packaging: the bundle provides preconfigured manifests and tool permissions for each environment, reducing the setup from a manual configuration process to a single install step.

For Claude Code users specifically: the formal "Claude connector" relationship between Supabase and Anthropic (announced separately at `supabase.com/blog/supabase-is-now-an-official-claude-connector`) means Claude Code has tested, validated workflows for common Supabase operations. Less prompt engineering, fewer edge cases, more reliable agent behavior when touching the database.

---

## Supabase for Platforms

The third announcement is less flashy but worth tracking if you are building multi-tenant applications: **Supabase for Platforms** reported 370% customer growth in the six months ending June 2026.

Supabase for Platforms is the offering that lets you give your own users Supabase-backed databases — provisioning isolated database instances per customer, per workspace, or per project within your own product. It is the infrastructure behind AI app builders that need to spin up user-specific databases on demand.

The 370% growth is consistent with the broader pattern: AI-native applications that provision infrastructure dynamically (one database per user, one database per agent conversation, one database per generated project) are driving Supabase's growth as much as traditional software development workflows.

---

## Additional Developer Features

Two smaller but builder-relevant releases shipped alongside the round:

**RLS Tester (preview):** A tool for debugging Postgres Row Level Security policies by simulating queries as specific roles and seeing which policies are evaluated. RLS is powerful and frequently misconfigured — having a native debugger reduces the risk of security regressions when policies change.

**Supabase Edge Functions update:** Agent-authored Edge Functions now appear correctly in the dashboard with metadata (author, trigger, last modified) that identifies whether the function was created by a human or an agent workflow. Small feature, but useful when your codebase is increasingly co-authored.

---

## What Builders Should Know

**If you are starting a new project and need a database:** Supabase remains the default recommendation for Postgres-based backends. The funding gives it an extended open-source runway. The MCP connector bundle means AI coding tools will continue to improve at working with it natively. The base product has not changed — it is still open-source Postgres with a managed platform layer.

**If you are hitting Postgres scaling limits:** The Multigres alpha is worth evaluating now, before you face an emergency migration. Apply to the partner program, get it in front of your staging workloads, and understand the sharding model before you need it. The v0.1 designation means there will be rough edges, but the architecture is sound and the team has the funding to see it to GA.

**If you are building an agent-driven application:** The 60% agent-created database figure is a data point about the industry, not just Supabase. Infrastructure that is MCP-native, well-documented, and familiar to coding agents will attract more agent-driven traffic than infrastructure that is not. Supabase has an early lead here because Claude Code already knows how to work with it end-to-end.

**If you are building a multi-tenant AI product:** Supabase for Platforms is the cleanest solution currently available for per-user database isolation without running your own Postgres fleet. The 370% growth suggests the market is finding it.

**One watch item:** Multigres is Apache 2.0 and open-source. If it reaches production maturity, it will likely be available as a standalone tool independent of the Supabase managed platform. Teams that self-host Postgres for regulatory or cost reasons could eventually benefit from Multigres without migrating to Supabase's managed offering.

---

## The Bigger Picture

The Supabase round is not primarily a story about Supabase. It is a story about where AI infrastructure investment is going in 2026.

Supabase grew 600% in one year, driven by AI coding agents. GIC, one of the world's largest sovereign wealth funds, led a $500M round. Stripe invested twice. These are not speculative bets — they are reads on where the agent-driven development market is going.

The infrastructure layer of the AI stack — databases, vector stores, storage, edge compute — is being rebuilt for agent-first workloads. Products that get there earliest, with the strongest MCP integrations and the clearest agent-facing documentation, are going to capture the bulk of that demand. Supabase is making a credible case that it will be the Postgres layer for that world.

Claude Code being its largest driver is, to put it plainly, interesting context for anyone building with either product.
