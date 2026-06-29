# Google's Open Knowledge Format (OKF v0.1): The Markdown Standard for Agent Knowledge Graphs

> OKF v0.1 is Google Cloud's June 2026 open spec for representing org knowledge as linked Markdown files. One required field, two reference implementations, and a design that works with any agent framework.


On June 12, 2026, Google Cloud published **Open Knowledge Format v0.1** — a vendor-neutral specification for representing organizational knowledge as a directory of linked Markdown files with YAML frontmatter. The spec is 451 lines, lives in the [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) GitHub repo, and ships with two working reference implementations.

The pattern it formalizes is not new: teams have been keeping shared Markdown wikis for AI agents to read since Andrej Karpathy popularized the idea. What OKF adds is a versioned spec so bundles from different teams, tools, and vendors can be consumed without translation layers. One required field. No proprietary SDK. No lock-in.

This guide covers what the spec actually says, how to build an OKF bundle today, how agents consume it, and where it fits relative to the patterns you're probably already using.

---

## Why This Exists

The problem OKF addresses is coordination. Most knowledge management for AI agents today is bespoke:

- A `CLAUDE.md` at the repo root with project conventions
- An `AGENTS.md` with agent instructions
- An Obsidian vault some teams maintain for shared context
- A Confluence export someone dumps into an agent's context window

These patterns work inside a single tool or team but don't travel. If you want an agent built on a different framework — or a different vendor's agent — to read your knowledge, you need a shared format.

OKF is Google's proposal for that shared format. It covers the interoperability surface: file structure, YAML schema, linking conventions, and reserved filenames. It explicitly doesn't cover storage, serving, governance, or domain-specific schemas. The spec is intentionally minimal.

---

## The Spec in Five Minutes

### Bundle Structure

An OKF bundle is a directory of Markdown files. Each file is a **concept** — a discrete knowledge unit. File paths are concept IDs: `tables/orders.md` has ID `tables/orders`.

```
sales/
├── index.md              # required entry point
├── datasets/
│   ├── index.md
│   └── orders_db.md
├── tables/
│   ├── orders.md
│   └── customers.md
└── metrics/
    └── weekly_active_users.md
```

Bundles can be tarballs, git repos, or directories — whatever your tooling prefers.

### YAML Frontmatter

Every non-reserved Markdown file in a conformant bundle must have parseable YAML frontmatter containing at least one field: `type`.

**Required:**

| Field | Description |
|-------|-------------|
| `type` | String — what kind of thing this document describes (e.g. `BigQuery Table`, `API Endpoint`, `Metric`, `Playbook`) |

**Recommended (in priority order):**

| Field | Description |
|-------|-------------|
| `title` | Human-readable name |
| `description` | One-sentence summary |
| `resource` | URI to the underlying asset |
| `tags` | Array of strings |
| `timestamp` | ISO 8601 — last meaningful change |

Producers may add arbitrary fields. Consumers must tolerate unknown fields, unknown types, missing optional fields, and broken cross-links without rejecting the bundle. This permissiveness is by design: real knowledge graphs grow and refactor.

### A Concrete Example

```markdown
---
type: BigQuery Table
title: Orders
description: One row per completed order.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, revenue]
timestamp: 2026-05-28T14:30:00Z
---

# Schema

| Column | Type | Description |
|--------|------|-------------|
| order_id | STRING | Globally unique identifier. |
| customer_id | STRING | FK to [customers](/tables/customers.md). |
| amount_usd | FLOAT64 | Total after tax. |

# Notes

High-cardinality join key. Filter by `created_at` before joining to avoid full scans.
```

Note the cross-link to `/tables/customers.md`. Standard Markdown links are the entire relationship model — no graph database, no proprietary link syntax.

### Reserved Filenames

Two filenames have defined semantics at any directory level:

| File | Purpose |
|------|---------|
| `index.md` | Entry point for that directory level — enumerates contents, enables progressive disclosure |
| `log.md` | Chronological change history, newest first, date-grouped in ISO 8601 (`YYYY-MM-DD`) |

Agents traversing `index.md` hierarchically is the intended consumption pattern.

### Conformance

A bundle conforms to OKF v0.1 if:
1. Every non-reserved Markdown file contains parseable YAML frontmatter
2. Every frontmatter block contains a non-empty `type` field
3. Reserved filenames follow their specified structure

That's it. The spec requires no minimum number of documents, no mandatory `index.md`, and no specific concept types.

---

## Reference Implementations

Google ships two implementations in the `knowledge-catalog` repo:

**Enrichment Agent** (`agents/` directory) — walks a BigQuery dataset and drafts OKF concept documents for every table and view. A second LLM pass enriches the drafts with schema context, join paths, and citations from authoritative docs. The sample bundles (GA4 e-commerce, Stack Overflow, Bitcoin public datasets) were produced this way.

**Static HTML Visualizer** — a single self-contained file that renders any OKF bundle as an interactive knowledge graph. No backend. No data leaving the page. Drop it next to your bundle directory and open in a browser.

Google also updated **Cloud Knowledge Catalog** on June 12 to ingest OKF bundles natively — so there's a hosted consumption path if you're already in GCP.

---

## How Agents Consume an OKF Bundle

The consumption pattern is straightforward:

1. Agent reads `index.md` at the bundle root to understand what's available
2. Agent follows links to relevant concept files before beginning a task
3. Cross-links enable multi-file understanding in a single LLM pass

Agents with file tools (MCP `read_file`, LangGraph file loaders, Claude's file reading) traverse OKF bundles naturally — it's just directories and Markdown. Nothing in the spec requires a custom reader.

If you're building an MCP server, OKF bundles make a clean backing store: serve concept files as resources, expose `index.md` as the resource list, and let the agent follow cross-links.

---

## OKF vs. What You're Already Using

| Format | Scope | Portability | Required fields |
|--------|-------|-------------|-----------------|
| `CLAUDE.md` / `AGENTS.md` | Single repo, single tool | Tool-specific | None |
| Karpathy LLM wiki pattern | Team-internal | Convention only | None |
| OKF v0.1 | Org-wide, multi-team, multi-vendor | Versioned spec | `type` only |
| `llms.txt` | Site-level context for crawlers | Not an agent format | N/A |

These don't conflict. `CLAUDE.md` can reference an OKF bundle. An OKF bundle can contain concept files that point to your `AGENTS.md`. `llms.txt` is for crawlers; OKF is for agents doing work.

The main practical difference: OKF bundles are designed to span many linked concept documents across teams and vendors. `CLAUDE.md` is scoped to a single repo or session. Both are useful; neither replaces the other.

---

## When to Use OKF

**Strong fit:**
- You're building agents that need to read schema information, playbooks, or domain knowledge from multiple teams
- You want a knowledge base that works with Claude, Gemini, and whatever comes next — without format translation
- You're in GCP and want Knowledge Catalog integration
- You're maintaining a shared wiki for AI agents and want a versioned spec instead of convention

**Weak fit:**
- You only need to give a single agent project-level context (stick with `CLAUDE.md`/`AGENTS.md`)
- Your knowledge changes in real time (OKF is file-based; staleness is a process problem, not a spec feature)
- You need access control or governance semantics (the spec doesn't cover these)

---

## Current Limitations

Google explicitly calls v0.1 a starting point:

- **No merge semantics** — if two agents write conflicting updates to the same concept, OKF doesn't specify how to resolve them
- **No faceted search** — the `tags` field exists but the spec doesn't mandate a tag vocabulary or search behavior
- **No live knowledge** — bundles are files; real-time data needs a layer on top
- **Name collision** — "OKF" is also used by the unrelated OKF-SCIS supply-chain spec; context matters when searching

The spec is versioned (`<major>.<minor>`): minor bumps are backward-compatible; major bumps indicate breaking changes. Community feedback shapes v0.2.

---

## Getting Started

The spec is at `okf/SPEC.md` in the [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) repo. The three sample bundles are in `bundles/`. The enrichment agent and visualizer are in `agents/` and `src/`.

For most builders, the fastest path is:

1. Read `okf/SPEC.md` (14.7 KB, 451 lines — an easy afternoon read)
2. Open one of the sample bundles alongside the visualizer to see what a working OKF graph looks like
3. Write a concept or two for your own domain using the `type` + optional fields schema
4. Wire it to your agent via file tools or an MCP resource server

The spec asks almost nothing of you. One field per document. Markdown you already write. Links you already use. If your team is already maintaining an "LLM wiki" in any form, converting it to OKF-conformant bundles is a morning's work.

---

*AI-researched. ChatForest does not have hands-on access to the OKF toolchain and cannot independently verify runtime behavior of the enrichment agent or visualizer.*

