---
title: "Anthropic Gives MCP Builders a Dashboard: Connector Observability and In-App Directory Submission"
date: 2026-06-16
description: "Anthropic launched connector observability (public beta) on June 8, 2026, giving MCP server owners a dashboard to monitor adoption, errors, latency, and usage across Claude, Claude Code, and Cowork. In-app directory submission went live at the same time. Here's what each feature does and what builders need to know before submitting."
og_description: "Anthropic's new connector observability dashboard gives MCP developers visibility into active users, tool call counts, error rates, latency, and per-surface usage breakdowns. Directory submission is now in-app. Builder guide with submission requirements, 11-step walkthrough, and common rejection reasons."
content_type: "Builder's Log"
categories: ["MCP", "Developer Tools", "Anthropic"]
tags: ["anthropic", "mcp", "claude-connectors", "connector-directory", "observability", "mcp-server", "claude-cowork", "enterprise", "developer-tools", "directory-submission"]
---

Anthropic shipped two related capabilities for MCP connector developers on June 8, 2026: a **connector observability dashboard** (public beta) and **in-app directory submission**. If you have a connector in the Claude Connector Directory, or you're building one, both matter.

This guide covers what each feature does, the requirements to use them, and what to prepare before submitting to the directory.

---

## What Was Announced

**Connector Observability** is a new admin dashboard visible inside Claude under Organization settings → Directory. It shows connector owners real-time metrics on how their published connectors are performing across Claude product surfaces: how many users are calling them, which tools are failing, how fast they respond, and where in the product stack (Claude vs. Claude Code vs. Cowork) tool calls are landing.

**In-App Directory Submission** replaces or supplements the previous external submission flow. Connector owners can now initiate and track a directory submission without leaving Claude.

Both features are in **public beta**. Access requires Admin or Owner access on a Team or Enterprise plan.

---

## The Observability Dashboard

The dashboard surfaces three views:

### 1. Adoption Tracking

- Active users over time
- Total tool calls
- Directory rank over time

Directory rank is surfaced as a metric — Anthropic is explicitly telling developers that their connector competes for visibility in a ranked directory. Optimizing call quality and reliability directly affects rank.

### 2. Error and Performance Diagnostics

- Composite health score (a single number combining error rate + latency)
- Raw error rates
- Latency at the tool level, not just the connector level
- Per-tool error breakdowns

The per-tool breakdown is the most actionable piece. A connector with 12 tools might have 11 that work fine and 1 that throws errors on 40% of calls. Without per-tool visibility, that failure is invisible in aggregate metrics.

### 3. Product-Level Usage Breakdown

Tool calls are segmented by product surface:

- **Claude** (claude.ai consumer / team interface)
- **Claude Code** (agentic terminal / IDE extension)
- **Cowork** (collaborative workspace product)
- Other surfaces as they emerge

This matters for prioritization. If 85% of your connector's usage comes from Claude Code and 10% from Claude, your tool annotations and documentation should be optimized for agentic, automated workflows — not conversational prompts.

### Who Can Access It

- Admin or Owner role on a Team or Enterprise plan
- On Enterprise: custom roles with "Directory management" or "Libraries" permission can also access it
- Location: Claude → Organization settings → Directory

Individual plan users do not have access to the observability dashboard.

---

## In-App Directory Submission

The directory now hosts over 300 third-party connectors used by millions of people across Claude products. Until June 8, submission was handled through an external process. Now it runs inside Claude through an 11-step portal that saves progress automatically.

### The 11-Step Submission Flow

**Step 1 — Introduction**
Overview of what listing in the directory provides: surface area across Claude, Claude Code, and Cowork; trust signals from Anthropic review.

**Step 2 — Connection**
Your server's HTTPS URL and transport method. HTTP is not accepted — HTTPS is required.

**Step 3 — Tools**
The portal auto-syncs your tools, prompts, and resources from the live server. What it reads is what reviewers will evaluate.

**Step 4 — Listing**
Public-facing presentation: name, tagline, description, categories, icon. This is what users see when browsing the directory.

**Step 5 — Use Cases**
Primary use cases your connector serves and the scope of data it handles. Vague answers here are flagged.

**Step 6 — Company**
Organization info and a primary contact. Reviewers use this contact for questions and for ongoing compliance.

**Step 7 — Authentication**
Authentication method. OAuth 2.0 is required for any connector that accesses authenticated user services. Unauthenticated connectors for local/public data have different requirements.

**Step 8 — Data Handling**
Whether your connector owns the underlying API or is a third-party integration. Special data types (PII, financial data, health data) must be declared here.

**Step 9 — Test and Launch**
Complete access instructions for reviewers. Reviewers run your connector end-to-end before approving. If they cannot test it, the submission fails.

**Step 10 — Compliance**
Seven mandatory policy acknowledgments. All seven must be accepted. This is not optional.

**Step 11 — Review**
Final verification before submission. Progress saved throughout.

Track status and reviewer feedback at: `claude.ai/admin-settings/directory/submissions`

For escalations: `mcp-review@anthropic.com`

---

## What Gets Rejected

Based on the submission documentation, the most common failure modes are:

### Missing or incomplete privacy policy

This is an immediate rejection. Your privacy policy must explicitly cover:
- What data is collected
- How it is used and stored
- Third-party sharing
- Data retention periods
- Contact information

A link to a generic company privacy page that doesn't specifically address your connector's data practices does not pass. If you're building an MCP server for the first time and don't have a standalone privacy policy, write one before submitting.

### Missing tool annotations

All tools must include a `title`. Any tool with side effects must include the correct hint:
- `readOnlyHint: true` for read-only operations
- `destructiveHint: true` for operations that modify or delete data

Reviewers check annotations for completeness and accuracy. A tool that deletes files but doesn't carry `destructiveHint: true` is a rejection.

### Insufficient test instructions

Reviewers test your connector end-to-end. If your connector requires credentials, you must provide working test credentials (or a sandbox account) with enough access to demonstrate all listed tools. Connectors that cannot be tested are not approved.

### Vague use-case descriptions

Step 5 asks for primary use cases and data handling scope. Answers that consist of generic descriptions ("helps users do AI-powered tasks") are flagged as insufficient. Reviewers want to understand specifically what your connector does and what data it touches.

---

## Builder Decision Guide

**Should you submit your MCP server to the directory?**

Submit if:
- Your connector is genuinely useful to Claude users, not just an internal integration you've made public
- You have a privacy policy that covers your connector's specific data practices
- Your tools have complete annotations (`title`, and appropriate `readOnlyHint`/`destructiveHint`)
- You can provide working test credentials to reviewers
- You want visibility across Claude, Claude Code, and Cowork without managing your own distribution

Don't submit yet if:
- You're still iterating on the tool schema — changes after submission require re-review
- You're relying on HTTP instead of HTTPS
- Your connector handles PII or sensitive data but you haven't written specific data handling documentation
- You don't have a primary contact who can respond to reviewer questions within a reasonable window

**On the observability dashboard:** If your connector is already in the directory, go check the dashboard immediately. Per-tool error breakdowns and product-surface segmentation are the most actionable data points — they will tell you where to focus your next maintenance cycle.

---

## Context: Why This Matters Now

The Claude Connector Directory launched with the Claude Connectors program and has grown to 300+ third-party integrations. Until June 8, connector owners had no visibility into whether their connector was actually being used, which tools were failing, or where in the product stack usage was concentrated.

That's a meaningful gap for a tool distribution channel being positioned against the App Store / VS Code Marketplace / npm model. Observatory-grade tooling for MCP server operators is table stakes for that positioning. The June 8 release closes the gap between shipping a connector and operating one.

The in-app submission flow is a quality-of-life change more than a structural one, but it signals that Anthropic is investing in reducing friction for the connector developer path — which is the right place to invest if the goal is 3,000+ connectors, not 300.

---

## Summary

| Feature | Status | Access |
|---|---|---|
| Connector observability dashboard | Public beta | Admin/Owner, Team or Enterprise |
| Per-tool error breakdown | Included | Same |
| Product-surface usage breakdown | Included | Same |
| In-app directory submission | Live | Admin/Owner, Team or Enterprise |
| Submission tracking dashboard | Live | `claude.ai/admin-settings/directory/submissions` |

The submission portal is always open. Review timelines vary with queue volume. Contact `mcp-review@anthropic.com` for escalations.
