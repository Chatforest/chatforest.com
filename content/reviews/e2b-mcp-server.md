---
title: "E2B MCP Server — Secure AI Code Execution in Cloud Sandboxes (Archived)"
date: 2026-04-20T11:00:00+09:00
description: "E2B's MCP server enabled Claude and other AI assistants to execute code in secure Firecracker microVM sandboxes. Archived April 16, 2026 after E2B integrated MCP support directly into their sandbox platform via Docker partnership. 390 GitHub stars."
og_description: "E2B MCP Server: 390 stars, archived April 2026. Secure code execution via Firecracker microVMs. Replaced by native sandbox MCP integration with 200+ Docker catalog tools. Rating: 2.5/5."
content_type: "Review"
card_description: "E2B's standalone MCP server gave AI assistants the ability to execute Python and JavaScript code in secure Firecracker microVM sandboxes. Archived on April 16, 2026 — E2B shifted to native MCP support inside sandboxes via a Docker partnership, making the standalone server redundant. The parent E2B platform (11.8K stars, $43.8M raised) remains actively developed."
last_refreshed: 2026-04-20
---

Part of our **[Code Execution & Sandbox MCP category](/categories/code-execution-sandbox/)**.

*At a glance: 390 GitHub stars, 67 forks, 67 commits, Apache-2.0 license, JavaScript (52.8%) + Python (41.5%). **Archived April 16, 2026.** npm package `@e2b/mcp-server`. Parent company E2B raised $43.8M ($21M Series A from Insight Partners). PulseMCP: 38.4K all-time visitors (#691 globally), 193 weekly.*

E2B's MCP server was a straightforward tool: it let Claude Desktop (and other MCP clients) execute code inside E2B's cloud sandboxes. The pitch was security — instead of running AI-generated code on your local machine, it ran inside Firecracker microVMs with hardware-level isolation. Each sandbox got its own dedicated kernel, started in ~150ms, and was destroyed after use.

On April 16, 2026, E2B archived the repository. The standalone MCP server is no longer maintained.

## What Happened

E2B didn't abandon MCP — they absorbed it. In October 2025, E2B partnered with Docker to integrate MCP support directly into the E2B Sandbox platform. Instead of a standalone server that only let you run code, the new approach gives every E2B sandbox access to 200+ verified MCP tools from Docker's catalog (GitHub, Stripe, Notion, Grafana, Browserbase, and many more) — plus the ability to run custom MCP servers inside the sandbox.

The standalone `mcp-server` repository became redundant. Why maintain a separate MCP server for code execution when the sandbox itself is now an MCP-native environment?

This is actually a healthy engineering decision. The standalone server had only 3 open issues and minimal community engagement. The parent platform (11.8K stars, 4,768 commits, active daily development) is where the real investment is.

## What the Standalone Server Did

The archived MCP server provided code interpreting capabilities via E2B Sandbox:

- **Python execution** in isolated Firecracker microVMs
- **JavaScript execution** via Node.js
- **File operations** (create, read, list files within sandbox)
- **Package installation** (pip/npm inside sandbox)
- **Automatic cleanup** after session completion

Setup was via Smithery (`npx @smithery/cli install e2b --client claude`) or manual Claude Desktop configuration with an E2B API key.

Both JavaScript and Python implementations were included in a monorepo structure (`packages/js` and `packages/python`).

## The Parent Platform: E2B

E2B (the company) is doing well despite archiving this one repo:

- **Main SDK** (`e2b-dev/E2B`): 11,800 stars, 861 forks, 4,768 commits, v2.20.0 (April 2, 2026)
- **Code Interpreter SDK** (`e2b-dev/code-interpreter`): 2,300 stars, 206 forks, 859 commits
- **Funding**: $43.8M total — $21M Series A led by Insight Partners (2025), with Decibel, Sunflower Capital, Kaya
- **Revenue**: $1.5M ARR as of mid-2025 with a 14-person team
- **PyPI**: e2b-code-interpreter ~1.46M downloads/month; e2b SDK ~624K npm downloads/month
- **Firecracker microVMs**: Sub-200ms cold starts, hardware-level isolation, dedicated kernel per sandbox

### Pricing

- **Hobby (Free)**: One-time $100 credit, 1-hour max sessions, 20 concurrent sandboxes
- **Pro ($150/month)**: 24-hour sessions, 100 concurrent sandboxes, custom CPU/RAM
- **Enterprise**: Custom pricing, BYOC, on-prem, self-hosted
- **Usage**: ~$0.05/hour for 1 vCPU sandbox (billed per second, RAM included)

## What's Good

**The archival itself is honest** — E2B didn't silently abandon the repo. They marked it as deprecated with a clear notice. The strategic shift to native sandbox MCP integration makes more sense than maintaining a separate server.

**E2B's core platform is strong** — 11.8K stars, active daily commits, well-funded ($43.8M), growing revenue. Firecracker microVM isolation is genuinely more secure than container-based alternatives (Docker uses shared kernel; Firecracker provides hardware-level isolation per sandbox).

**Docker MCP catalog integration** — Access to 200+ verified MCP tools inside sandboxes is a significant upgrade from a standalone code execution server.

**Pricing is accessible** — $100 free credit with no credit card is generous for getting started. Per-second billing at ~$0.05/hour is competitive.

## What's Not

**The standalone MCP server is dead** — If you had it configured in Claude Desktop, it no longer receives updates or security patches. You need to migrate to E2B's SDK-based approach.

**3 open issues will never be fixed** — Issues #6 (timeouts), #7 (CSV data), and #17 (Claude Desktop installation error) are frozen. The repo is read-only.

**The replacement is SDK-first, not MCP-first** — E2B's new approach requires using their Python or JavaScript SDK to spin up sandboxes with MCP tools inside. It's more powerful but also more complex than pointing Claude Desktop at an MCP server config.

**No free tier for ongoing use** — The $100 credit is one-time. After that, you need the $150/month Pro plan or pay-as-you-go. For casual use, this may be expensive.

**Vendor lock-in** — E2B sandboxes are cloud-only (AWS or GCP). Self-hosting requires Terraform setup and Enterprise tier. Unlike local sandbox solutions, you can't run E2B without internet access.

## Community Alternatives

With the official server archived, community-built E2B MCP servers exist but are minimal:

- **HeurisTech/e2b-sandbox-mcp** — 4 stars, 4 commits, desktop automation focus (VNC streaming, mouse/keyboard control). MIT license. More of a computer-use wrapper than a code execution server.
- **parth012001/e2b-mcp-server** — 0 stars, 4 commits, built as a coding assignment. Python/JavaScript execution with file operations. Not production-grade.

Neither is a viable replacement for the official server.

## Competitive Landscape

The AI sandbox market has heated up significantly in 2026:

| Platform | Cold Start | Isolation | GPU | MCP Support | Starting Price |
|----------|-----------|-----------|-----|-------------|---------------|
| **E2B** | ~150ms | Firecracker microVM | No | Native (200+ tools) | $100 free credit |
| **Daytona** | ~90ms | Docker container | Yes | No native MCP | $200 free credit |
| **Modal** | Sub-second | gVisor | Yes (A100/H100) | No native MCP | $0.000014/core/sec |
| **Blaxel** | Varies | VM | No | MCP-native | Free tier available |

E2B's Firecracker isolation is the strongest security boundary in the group. Daytona is fastest and cheapest for persistent environments. Modal wins for GPU workloads. None of the competitors match E2B's native MCP integration depth.

## Who's Behind It

E2B was founded by **Vasek Mlejnsky** (CEO) in the Czech Republic. The company has 14 employees and is backed by Insight Partners, Decibel, Sunflower Capital, and other investors across $43.8M in total funding.

The MCP server was primarily maintained by **mishushakov** (Mish Ushakov), who handled most of the repository's 67 commits. The broader E2B platform has a larger engineering team.

## Bottom Line

The E2B MCP server was a clean, simple tool that did one thing: let AI assistants run code in secure cloud sandboxes. Its archival isn't a failure — it's a sign that E2B integrated MCP capabilities more deeply into their core platform, making the standalone server unnecessary.

If you need sandboxed code execution for AI agents, the E2B platform itself (via their SDK) is still a strong choice. The Firecracker microVM isolation is genuinely superior to container-based alternatives, the pricing is accessible, and the Docker MCP catalog integration gives you far more than the old standalone server ever offered.

But the standalone MCP server? It's done. If you're configuring MCP servers in Claude Desktop and want code execution, look at alternatives like the Desktop Commander MCP (local, free, but less secure) or use E2B's SDK directly in your application code.

**ChatForest rating: 2.5 out of 5**

The low rating reflects the archived status of the standalone MCP server, not E2B as a platform. A deprecated server with no future updates, 3 unresolved issues, and a migration path that requires SDK integration rather than MCP configuration earns a below-average score. The parent platform would rate much higher.

*We research MCP servers from public sources — GitHub repos, documentation, issue trackers, npm/PyPI registries, PulseMCP analytics, and security advisories. We don't test servers hands-on. Ratings reflect our assessment of maintenance quality, security posture, community traction, and practical utility based on available evidence. See our [methodology](/about/methodology/) for details.*
