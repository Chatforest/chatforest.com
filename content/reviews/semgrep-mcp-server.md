---
title: "The Semgrep MCP Server — Security Scanning for AI-Generated Code"
date: 2026-03-22T23:30:00+09:00
description: "Semgrep's MCP server and plugin give AI coding agents real-time security scanning — catching vulnerabilities, supply chain risks, and leaked secrets in generated code before it ships."
og_description: "Semgrep MCP server: real-time security scanning for AI-generated code. SAST, SCA, secrets detection. 665 stars archived repo. CLI v1.161.0. Now supports Codex + VS Code. Taint engine 20-40% faster. Rating: 4/5."
content_type: "Review"
card_description: "Semgrep's MCP server scans AI-generated code for security vulnerabilities, supply chain risks, and leaked secrets in real time. 665 GitHub stars (archived). Integrated into Semgrep CLI v1.161.0. Now supports Claude Code, Cursor, Windsurf, Codex, and VS Code. New: AI-powered IDOR/broken auth detection, Autofix beta, supply chain hooks, 20-40% taint engine speedup."
last_refreshed: 2026-05-03
---

**At a glance:** Archived standalone repo (665 stars), MCP integrated into Semgrep CLI v1.161.0, 7 tools, SAST + SCA + secrets detection, now supports Claude Code, Cursor, Windsurf, Codex, and VS Code, PulseMCP #301 globally (138K all-time). Part of our **[Security & Compliance MCP category](/categories/security-compliance/)**.

*First reviewed March 22, 2026. Refreshed May 3, 2026.*

Semgrep has shipped an [MCP server](https://github.com/semgrep/mcp) that gives AI coding agents the ability to scan generated code for security vulnerabilities in real time. In the age of vibe coding — where LLMs generate more code than developers type — this addresses a critical gap: **who's reviewing AI-generated code for security issues?**

The answer Semgrep proposes is: the AI itself, with Semgrep as its security tool. When integrated with MCP-compatible editors like Cursor, Claude Code, or Windsurf, the agent can scan every file it generates using Semgrep's SAST, supply chain analysis, and secrets detection — and regenerate code when issues are found, without the developer switching context.

The standalone MCP repository (665 stars, 353 commits) was archived in October 2025. MCP functionality is now integrated directly into the Semgrep binary at v1.161.0, meaning any Semgrep installation becomes MCP-capable without a separate server. Since the March review, Semgrep has expanded editor support to include Codex and VS Code, shipped AI-powered detection for complex auth flaws, launched Autofix in beta, improved taint analysis performance by 20–40%, and joined OpenAI's Trusted Access for Cyber Program.

## What It Does

The Semgrep MCP server exposes security scanning capabilities to any MCP-compatible client:

- **Security check** — scan code for vulnerabilities using Semgrep's registry of 2,800+ community rules and 20,000+ Pro rules. Covers OWASP Top 10, injection flaws, authentication issues, and language-specific pitfalls across dozens of languages.

- **Custom rule scanning** — run scans with custom Semgrep config strings or fully custom rules. Useful for enforcing organization-specific security policies through your AI agent.

- **Abstract syntax tree generation** — produce ASTs for code files, giving the LLM deeper structural understanding of the code it's analyzing. This enables more informed security assessments beyond pattern matching.

- **AppSec Platform integration** — fetch findings from the Semgrep AppSec Platform (requires authentication token). Connects agent-level scanning to your organization's centralized security dashboard.

- **Language support queries** — list all supported programming languages so the agent knows what it can scan.

- **Rule schema access** — retrieve the Semgrep rule JSON schema, enabling agents to write or validate custom rules.

## What's New Since March 2026

**Semgrep Multimodal** (March 2026) — formerly Semgrep Assistant, now rebranded. Adds AI-powered detection for complex business logic flaws including IDOR (insecure direct object reference) and broken authorization — vulnerability classes that pure static analysis struggles to catch. Semgrep reports 1.9× better recall on IDOR detection compared to standalone LLMs.

**Autofix beta** (March 2026) — formerly "Click to Fix," now in beta. Generates AI-drafted pull requests for Code findings. Your agent detects a vulnerability, Autofix proposes the remediation as a PR. Still opt-in and beta-quality, but a meaningful step toward fully automated security remediation.

**Supply chain hooks** (v1.158.0, April 9, 2026) — hooks now trigger on supply chain (SCA) findings in addition to SAST. This extends the automatic-scan-and-regenerate loop to dependency vulnerabilities, not just code pattern issues.

**Taint engine redesign** (v1.158.0, April 9, 2026) — 20–40% performance improvement on taint-based analysis. Lambda taint tracking was added in v1.157.0 (March 31). More accurate, faster scans for MCP-driven security checks.

**Codex and VS Code now supported** — The supported editor list has expanded. Codex is configured via `~/.codex/config.toml`. VS Code via `.vscode/mcp.json`. The complete list: Claude Code, Cursor (+ Cursor Plugin Marketplace), Windsurf, Codex, VS Code, and any MCP-compatible client.

**Cursor Plugin Marketplace listing** (March 11, 2026) — Semgrep is now officially listed in the Cursor Plugin Marketplace, improving discoverability for Cursor users.

**OpenAI Trusted Access for Cyber Program** (April 2026) — Semgrep was selected for this program, receiving $10M in API credits for frontier model access. Claims: 8× more true positives, 50% fewer false positives compared to LLMs alone. Signals that Semgrep is deepening its AI integration rather than treating it as a side feature.

**TeamPCP supply chain campaign** (February–March 2026) — A targeted supply chain attack campaign hit security vendors including Trivy, Checkmarx, LiteLLM, and Bitwarden. Semgrep confirmed unaffected and published detection rules within hours of each discovered attack.

## The Plugin Model

Semgrep now bundles its MCP integration as a **plugin** for supported editors. The plugin combines three components:

1. **MCP Server** — the protocol layer that lets LLMs call Semgrep tools
2. **Hooks** — automatic triggers that scan every file an agent generates, prompting regeneration when issues are detected
3. **Skills** — pre-built capabilities that teach the agent how to use Semgrep effectively

Hooks mean security scanning happens automatically — the agent doesn't need to remember to call the security_check tool. It scans code, Semgrep catches issues, and the agent fixes them in a loop until the code is clean or the developer dismisses the finding. Supply chain hooks extend this to dependency vulnerabilities as of v1.158.0.

## Setup

### Claude Code

Install the Semgrep plugin, or configure hooks and MCP manually. Hooks for Claude Code pull custom rules from the Semgrep Registry.

### Cursor

Available in the Cursor Plugin Marketplace, or add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "semgrep": {
      "command": "uvx",
      "args": ["semgrep-mcp"]
    }
  }
}
```

### Codex

Configure via `~/.codex/config.toml`.

### VS Code

Configure via `.vscode/mcp.json`.

### Windsurf

Available through the Windsurf plugin marketplace.

### Standalone (any MCP client)

```bash
# Via Python
uvx semgrep-mcp

# Via Docker
docker run -i --rm ghcr.io/semgrep/mcp -t stdio
```

### Requirements

- Python 3.10 or later (for local installation)
- Semgrep CLI installed (`brew install semgrep` or `pip install semgrep`)
- `semgrep login` for Pro features and AppSec Platform integration
- Optional: `SEMGREP_APP_TOKEN` environment variable for AppSec Platform findings

### Transport Protocols

- **stdio** (default) — local integrations via stdin/stdout
- **Streamable HTTP** — requires OAuth authentication (required as of January 2026)
- **Hosted server** — experimental at `https://mcp.semgrep.ai/`
- **Note:** SSE transport was removed from the MCP server in January 2026. If you had SSE-based integrations, migrate to stdio or Streamable HTTP.

## Who This Is For

**Developers using AI coding agents** who want automated security guardrails. If you're generating code with Cursor, Claude Code, Windsurf, Codex, or VS Code, Semgrep's plugin means every generated file gets scanned for vulnerabilities without you doing anything extra.

**Security teams** responsible for code generated by AI-augmented developers. Semgrep's MCP integration lets you enforce security policies at the point of code generation, not after the PR is submitted.

**Organizations adopting vibe coding** at scale. When developers increasingly accept AI-generated code with minimal review, automated security scanning becomes essential. Semgrep's hook-based approach means security checks happen whether the developer remembers to ask for them or not.

**Open-source maintainers** accepting AI-generated contributions. The free tier (10 contributors) makes it practical for open-source projects to add automated security scanning to their AI-assisted development workflow.

## What's Good

**Addresses the right problem at the right time.** AI-generated code is shipping faster than humans can review it. Semgrep's MCP integration puts a production-grade security scanner directly in the generation loop.

**Expanding editor support.** The move to include Codex and VS Code means a meaningful portion of the developer population now has Semgrep MCP available natively in their toolchain.

**AI-powered detection for complex flaws.** Semgrep Multimodal adds detection for IDOR and broken auth — vulnerability classes that traditional static analysis misses. The 1.9× recall improvement on IDOR is a concrete data point.

**Performance gains.** The 20–40% taint engine speedup and lambda taint tracking in April 2026 make agent-driven security scans faster and more accurate.

**Generous free tier.** Semgrep's Team plan is free for up to 10 contributors on private repos. The Community Edition is fully open-source (LGPL-2.1). For individual developers and small teams, this costs nothing.

**Massive rule coverage.** 2,800+ community rules and 20,000+ Pro rules across dozens of languages. Cross-file dataflow analysis, supply chain reachability, and semantic secrets detection.

**The hook model is smart.** Automatic scanning via hooks — now extended to supply chain findings — eliminates the "agent forgot to check" failure mode.

**Supply chain attack resilience.** Semgrep's rapid response to the TeamPCP campaign (detection rules published within hours) demonstrates the team takes its own security seriously.

## What's Not

**The standalone repo is archived.** The PyPI `semgrep-mcp` package is frozen at v0.9.0 (September 2025). Workflows built around it need to migrate to the main `semgrep` binary.

**SSE transport removed.** January 2026 change: SSE support was dropped from the MCP server. If any of your integrations relied on SSE, you'll need to switch to stdio or Streamable HTTP with OAuth.

**Plugin setup varies by editor.** Each supported editor has a different setup path. The plugin model simplifies things within supported editors, but unsupported clients use the standalone server configuration.

**Pro features require authentication.** Free Community Edition covers core scanning, but cross-file dataflow analysis, supply chain reachability, and the full 20,000+ Pro rule set require `semgrep login`.

**Community rule count may have decreased.** Multiple sources indicate roughly 2,800+ community rules — down from the "5,000+" figure in our original review. This may reflect a Registry reorganization or counting methodology change; the Pro rule count (20,000+) is consistent across sources.

**Pricing is now à la carte.** Teams pricing dropped from $35 to $30/month per contributor, but Code, Supply Chain, and Secrets are now priced separately. Large organizations with multiple product modules may see higher total costs.

**Static analysis has limits in agentic pipelines.** Semgrep can catch vulnerable code patterns but has no visibility into what a remote MCP server returns at runtime. Dynamic payload injection from a compromised MCP server is outside Semgrep's detection scope — a limitation analysts have flagged in the context of the OWASP MCP Top 10 (currently in beta at v0.1).

## The Bottom Line

Semgrep's MCP integration continues to be the strongest security scanning option for AI coding workflows. Since the March review: editor support has expanded to five platforms, AI-powered detection for complex auth flaws has shipped, the taint engine is meaningfully faster, and supply chain hooks now cover dependency vulnerabilities too. The OpenAI partnership adds credibility.

The SSE deprecation and à la carte pricing restructuring require attention if you're migrating from older setups, but neither is a blocker.

The hook model — where Semgrep scans every generated file automatically and triggers regeneration on findings, now including supply chain — is still the right architecture for security in the vibe coding era.

**Rating: 4 / 5** — Production-grade security scanning for AI-generated code, now across five editors, with meaningful capability additions in AI-powered detection and supply chain coverage. The archived standalone repo, SSE removal, and à la carte pricing require migration attention but don't change the fundamental value proposition.

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*
