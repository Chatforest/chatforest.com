---
title: "MCP Security in Claude Code — Best Practices (as of 29 Jul 2026)"
date: 2026-07-29
snapshot_date: 2026-07-29
topic: mcp-security-claude-code
track: best-practices
audience: "technically comfortable readers"
description: "How to securely configure, discover, and use MCP servers when Claude Code is the client — covering permission modes, trust settings, sandboxing, tool restrictions, audit logging, the now-final 2026-07-28 protocol changes, and documented real-world incidents (CVE-2025-68143/144/145, CVE-2026-21852) — as of 29 Jul 2026."
content_type: "Best Practice"
categories: ["Claude Code", "MCP", "Security"]
tags: ["mcp", "claude-code", "security", "permissions", "sandboxing", "prompt-injection", "cve"]
last_refreshed: 2026-07-29
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-29"
grading_result: "0 fabrications; CVE-2026-21852 mislabeled-as-unpatched claim corrected (confirmed fully patched, separate unpatched npm-postinstall issue kept distinct); 5 corrections this refresh"
---

<!-- content/ai/best-practices/mcp-security-claude-code/2026-07-29/index.md — immutable dated snapshot -->

# MCP Security in Claude Code (as of 29 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **29 Jul 2026**, frozen here and kept as
> a permanent archive entry. This is a refresh of the [02 Jul 2026 snapshot](/ai/best-practices/mcp-security-claude-code/2026-07-02/),
> updated now that the MCP 2026-07-28 specification has published as final. Corrections applied
> inline; unverifiable gaps marked ⚠ PENDING — never guessed.

> ⚠️ **PROTOCOL UPDATE — the 2026-07-28 MCP specification is now FINAL.** It was a release
> candidate at the time of the previous snapshot; it published as final on 28 Jul 2026. **If and
> when your Claude Code build supports 2026-07-28** (this session could not confirm which Claude
> Code version added support — check your changelog), its MCP client is designed to absorb the
> transport-level changes (the `initialize`/`Mcp-Session-Id` removal, new required routing
> headers) for you — you should not need to change your own configuration for servers you merely
> connect to. **What matters practically:** the spec provides no automatic fallback from a legacy
> client to a server that speaks only 2026-07-28, so if your Claude Code build and a server you
> depend on are on mismatched protocol eras, that connection can fail outright rather than degrade
> gracefully. On authorization: RFC 9728 (Protected Resource Metadata — how a client discovers
> which authorization server protects a given remote MCP server) is unchanged from the prior
> spec, not new; RFC 9207 issuer validation is
> genuinely new but is an authorization-server-side/client-side plumbing detail your MCP client
> library handles, not something you configure directly. 🕒 **verify live**: confirm your Claude
> Code version's MCP client supports 2026-07-28 before assuming compatibility with an upgraded
> server.
> — [modelcontextprotocol.io — Versioning 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning) (fetched 2026-07-29) · [modelcontextprotocol.io — Authorization 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) (fetched 2026-07-29)

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving; check the current value

---

## Background: MCP in Claude Code

Claude Code can connect to external tools — databases, GitHub, Slack, internal APIs — through a system called MCP (Model Context Protocol). Each MCP "server" is a small program that gives Claude new capabilities. **stdio** servers (pronounced "standard eye-oh") run as child processes directly on your computer, launched by Claude Code, with data flowing through the program's input/output streams. Remote servers run over HTTPS and communicate via HTTP.

As of the 2026-07-28 MCP spec, the underlying protocol is stateless at the transport level: there is no more `initialize` handshake or `Mcp-Session-Id`, and every request is self-contained ([modelcontextprotocol.io — Changelog 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog), fetched 2026-07-29). This is an implementation detail Claude Code's MCP client is designed to handle for you — it should not change how you configure or use MCP servers day to day, but it does mean the *server* you connect to must speak a compatible protocol revision, or the connection fails outright rather than degrading gracefully.

That power carries risk: a malicious or misconfigured MCP server can read your files, exfiltrate credentials, or inject hidden instructions that make Claude do things you did not ask for. The eight practices below are the most important safeguards.

---

## Practice 1: Never connect an MCP server you do not explicitly trust — treat every server as untrusted code

**Do:** Before running `claude mcp add`, verify you know who maintains the server, where its source lives, and whether it has had security issues. You may prefer servers from the Anthropic Directory (claude.ai/directory — requires sign-in; returns 403 to automated checks) — but note that Directory listing is a bar for inclusion, not a security certification or audit. Anything you connect inherits the trust you give it.

**Why:** An MCP server runs as a program on your machine. It can read files, make network requests, and feed Claude instructions through tool responses. Anthropic reviews connectors for its Directory listing criteria but does not security-audit or manage any MCP server. Independent research (cyberdesserts.com, relaying Trend Micro and BlueRock Security findings) documented over 492 MCP servers publicly reachable with zero authentication and zero encryption; BlueRock Security found 36.7% of more than 7,000 analyzed servers vulnerable to server-side request forgery.

**Caveat:** The Anthropic Directory listing review is a bar for inclusion, not a security certification. Do not conflate "listed in the Directory" with "audited and safe." See the security page: "We encourage either writing your own MCP servers or using MCP servers from providers that you trust."

**Sources:**
- [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (fetched 2026-07-02): "We encourage either writing your own MCP servers or using MCP servers from providers that you trust"
- [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-07-02): "Anthropic reviews connectors against its listing criteria before adding them to the Anthropic Directory, but does not security-audit or manage any MCP server"
- [blog.cyberdesserts.com/ai-agent-security-risks/](https://blog.cyberdesserts.com/ai-agent-security-risks/) (fetched 2026-07-02): independent security research documenting unauthenticated public MCP servers and SSRF findings (relaying Trend Micro and BlueRock Security data)
- [code.claude.com/docs/en/managed-mcp](https://code.claude.com/docs/en/managed-mcp) (fetched 2026-07-02)

**Confidence:** ✅ independently-corroborated (Anthropic docs + independent security research)

---

## Practice 2: Keep the default permission mode; understand exactly what bypassPermissions removes before using it

**Do:** Leave Claude Code in `default` permission mode for normal work. Only switch to `bypassPermissions` (also invoked with `--dangerously-skip-permissions`) inside an isolated container or VM where Claude cannot reach your host filesystem, credentials, or the internet.

**Claude Code permission modes (six total):** 🕒 verify live — mode lineup may change across versions.
- `default` — asks before file edits and shell commands; recommended for most work
- `acceptEdits` — auto-approves file edits but still asks for shell commands
- `plan` — read-only; no file writes; safest option for exploratory or audit work
- `dontAsk` — runs only pre-approved tools without prompting; suited for CI pipelines
- `auto` — adds a background classifier that reviews tool calls; fewer interruptions than default
- `bypassPermissions` — skips all permission prompts; for isolated environments only

**⚠️ WARNING — dangerous default:** `bypassPermissions` skips all permission prompts and protected-path checks. Protected paths include `.git`, `.config/git`, `.vscode`, `.idea`, `.husky`, `.cargo`, `.devcontainer`, `.yarn`, `.mvn`, `.claude` (except worktrees), shell RC files (`.bashrc`, `.zshrc`, etc.), `.npmrc`, `.mcp.json`, `.claude.json`, and others. It does NOT protect `~/.ssh` or `~/.aws` directories — those are protected by the separate sandboxing credential feature (see Practice 5). If a malicious MCP tool result injects instructions while `bypassPermissions` is active, Claude will execute them without asking. Anthropic's docs state: "`bypassPermissions` offers no protection against prompt injection or unintended actions."

**Why:** The default mode asks you before Claude edits files or runs commands. That pause is the moment where you, as the human, catch something wrong. Removing it turns a slow-moving mistake into an instant one. For CI pipelines that need unattended operation, `dontAsk` mode (only pre-approved tools run) is safer than `bypassPermissions`. `plan` mode is the safest option when you only need read access. Administrators can block `bypassPermissions` org-wide with `permissions.disableBypassPermissionsMode: "disable"` in managed settings.

**Sources:**
- [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) (fetched 2026-07-02): full permission mode table with all six modes; bypassPermissions warning quoted verbatim; protected paths list
- [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-07-02): specific protected paths and credential protection (sandboxing)

**Confidence:** 📄 vendor-documented

---

## Practice 3: Use `mcp__*` deny rules and `--disallowedTools` to limit which MCP tools Claude can call

**Do:** In `.claude/settings.json` (project scope) or `~/.claude/settings.json` (user scope — applies to all your projects), add deny rules for MCP servers or tools you want to block.

If these files do not exist yet, create them: on Linux/Mac, run `mkdir -p ~/.claude && touch ~/.claude/settings.json` in your terminal, then open the file in any text editor. For project-level rules, create `.claude/settings.json` at the root of your project directory.

Use the pattern `mcp__<servername>__<toolname>` to target specific tools, or `mcp__<servername>` to deny all tools from a server:

```json
{
  "permissions": {
    "deny": [
      "mcp__filesystem",
      "mcp__github__create_repository"
    ]
  }
}
```

To deny all MCP tools entirely:
```json
{
  "permissions": {
    "deny": ["mcp__*"]
  }
}
```

The `--disallowedTools` CLI flag achieves the same effect for a single session:
```
claude --disallowedTools "mcp__filesystem__write_file"
```

**Why:** You may connect an MCP server for a read-only capability (e.g., checking a Jira ticket) but not want Claude to use its write tools (e.g., closing that ticket). Deny rules let you take exactly the tools you need and block the rest.

**Caveat:** Deny rules are evaluated before allow rules. A broad `mcp__*` deny cannot be overridden by a narrower allow rule — it blocks everything. Rule precedence is: deny → ask → allow. A `serverName` entry in an allowlist is NOT a security control — users can name any server anything; use `serverUrl` or `serverCommand` entries for enforcement. Cross-reference Practice 4 for scope decisions (project vs. user settings).

**Sources:**
- [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-07-02): MCP permission rule syntax, `mcp__*` wildcard behavior, deny-before-allow precedence
- [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) (fetched 2026-07-02): `disabledMcpjsonServers`, `enabledMcpjsonServers` settings reference

**Confidence:** 📄 vendor-documented

---

## Practice 4: Scope MCP servers to the narrowest config level possible — prefer local or user scope over project scope for sensitive credentials

**Do:** When adding an MCP server, choose your scope deliberately:
- `--scope local` (default): stored in `~/.claude.json` under your current project path; not shared with teammates and not checked into git.
- `--scope project`: written to `.mcp.json` in the project root and committed to version control. Every teammate who clones the repo sees it.
- `--scope user`: stored in `~/.claude.json` globally; available in all your projects but not shared.

For servers that require credentials (API keys, tokens), use `local` or `user` scope — never embed secrets in `.mcp.json`. Use `${VAR}` environment variable expansion so the file contains only the variable name, not the value. To set the variable, add it to your shell profile before starting Claude Code — for example, `export GITHUB_TOKEN=your-actual-token` in `~/.bashrc` or `~/.zshrc`, or use a `.env` file loaded by a tool like `direnv`.

**⚠️ WARNING:** `.mcp.json` is committed to git by default. Any secret placed in its `env` block will be in version control history.

**Why:** A `.mcp.json` in a public repository teaches every person who forks it exactly which MCP servers you trust — and attackers can craft servers at those same names or URLs to intercept connections. Keeping secrets out of committed files is a baseline for any software project.

**Caveat:** Project-scoped servers in `.mcp.json` require a workspace trust dialog before Claude Code activates them. The exact version of Claude Code that enforced this behavior most recently is available in the changelog. 🕒 verify live — specific version-pinned behavior references change frequently; check the current changelog rather than relying on a pinned version for behavior verification.

**Sources:**
- [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-07-02): full scope table, environment variable expansion examples
- [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) (fetched 2026-07-02): scope priority order, `allowedMcpServers`, `deniedMcpServers`, `enableAllProjectMcpServers`

**Confidence:** 📄 vendor-documented

---

## Practice 5: Enable sandbox mode to contain the blast radius of a compromised MCP chain

**Do:** Enable Claude Code's built-in Bash sandbox with `/sandbox` or by setting `sandbox.enabled: true` in your settings. **On Linux and Mac, add this to `~/.claude/settings.json` (user-wide) or `.claude/settings.json` in your project root.** The sandbox does not run on native Windows — use WSL2.

In the sandbox configuration, explicitly deny reads of credential files and unset secret environment variables:

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowUnsandboxedCommands": false,
    "credentials": {
      "files": [
        { "path": "~/.aws/credentials", "mode": "deny" },
        { "path": "~/.ssh", "mode": "deny" }
      ],
      "envVars": [
        { "name": "GITHUB_TOKEN", "mode": "deny" },
        { "name": "NPM_TOKEN", "mode": "deny" }
      ]
    }
  }
}
```

On Linux and Mac, `~` means your home directory. On Windows with WSL2, use the WSL path (e.g., `/home/yourname/`) rather than a Windows `C:\` path.

**Why:** MCP tool results can contain hidden instructions (prompt injection). If Claude is tricked into running a malicious shell command, the sandbox restricts what that command can read or write. Without it, a single poisoned tool response could exfiltrate your SSH private key or AWS credentials — because the docs explicitly warn: "the default read behavior allows reading credential files such as `~/.aws/credentials` and `~/.ssh/`."

**⚠️ WARNING — dangerous default:** Sandboxing is OFF by default. The sandbox also does not apply to Claude's built-in Read/Edit/Write file tools, only to Bash commands. Without the `credentials` block, sandboxed commands can still read `~/.aws/credentials`. Set `failIfUnavailable: true` to make missing sandbox dependencies a hard failure rather than a silent fallback to unsandboxed execution. Note: the sandbox does not run on native Windows — on native Windows this config block will silently do nothing unless `failIfUnavailable: true` is set, which will cause Claude Code to refuse to run Bash commands entirely until WSL2 is configured.

**Caveat:** The sandbox network proxy does not terminate TLS, so it cannot inspect encrypted traffic. A command with permission to reach `github.com` could use domain fronting to reach other hosts. For higher-assurance environments, configure a custom proxy with TLS inspection.

**Sources:**
- [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-07-02): full sandbox reference; credential protection, TLS caveat, `failIfUnavailable`, `allowUnsandboxedCommands`
- [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (fetched 2026-07-02): sandboxed bash tool described as a built-in protection; defense-in-depth recommendation

**Confidence:** 📄 vendor-documented

---

## Practice 6: Treat MCP tool results as untrusted content — never disable prompt-injection protections

**Do:** Follow the documented prompt-injection mitigations:
1. Review suggested commands before approval.
2. Do not pipe untrusted external content directly to Claude.
3. Be extra cautious with MCP servers that fetch content from the web (README files, GitHub issues, external APIs) — each fetch is a potential injection vector.
4. Keep `curl`, `wget`, and network-fetching commands in the deny list unless explicitly needed; if needed, use `WebFetch(domain:...)` rules to constrain to specific domains.
5. Do not use `bypassPermissions` or `auto` mode when connected to MCP servers that read external content you do not control.

**Why:** Prompt injection means an attacker plants instructions inside content that Claude reads — a GitHub issue, a README, a database row, a ticket description — and Claude follows those instructions as if they were yours. In January 2026, Cyata researchers found three CVEs in Anthropic's own `mcp-server-git` that enabled remote code execution through this attack: malicious content in a repository triggered Git operations that executed arbitrary scripts. The three CVEs: CVE-2025-68145 (path validation bypass), CVE-2025-68143 (unrestricted git_init), CVE-2025-68144 (argument injection in git_diff).

**Caveat:** Claude Code runs some mitigations already: an isolated context window for web fetches, trust verification dialogs for new MCP servers, and a separate server-side probe in auto mode that scans tool results before Claude reads them. But the security page explicitly states: "no system is completely immune to all attacks." Independent researchers (TrueFoundry) confirm that model-level detection alone is insufficient; infrastructure-level controls are required. The 2026-07-28 spec's own text carries the core tool-safety principle ("descriptions of tool behavior... should be considered untrusted, unless obtained from a trusted server") forward verbatim — it is accurate to say the revision adds no *new* tool-poisoning/prompt-injection countermeasures, not accurate to say the topic goes unaddressed.

**Sources:**
- [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (fetched 2026-07-02): prompt injection section, network command approval defaults, best practices list
- [theregister.com/2026/01/20/anthropic_prompt_injection_flaws/](https://www.theregister.com/2026/01/20/anthropic_prompt_injection_flaws/) (fetched 2026-07-02): CVE-2025-68143/144/145 in mcp-server-git; CVE-to-mechanism mapping: 68145=path validation bypass, 68143=unrestricted git_init, 68144=argument injection in git_diff
- [truefoundry.com/blog/claude-code-prompt-injection](https://www.truefoundry.com/blog/claude-code-prompt-injection) (fetched 2026-07-02): independent analysis; infrastructure-level controls recommended over model-level detection
- [arxiv.org/pdf/2512.08290](https://arxiv.org/pdf/2512.08290) (fetched 2026-07-02): preprint SoK — MCP trust assumptions absent, fine-grained capability control lacking (supporting citation, not peer-reviewed)

**Confidence:** ✅ independently-corroborated (Anthropic docs + The Register CVE reporting + independent security researchers)

---

## Practice 7: For teams, enforce an MCP server allowlist through managed settings — do not rely on per-developer discipline alone

**Do:** Organizations using Claude Code on Team or Enterprise plans should configure `allowedMcpServers` + `allowManagedMcpServersOnly: true` through server-managed settings or MDM (Mobile Device Management — software like Jamf, Intune, or Mosyle that your IT team uses to push settings to all company computers). If you do not have an IT team, this practice is out of scope for your personal setup — focus on Practices 1–5 instead.

To disable MCP entirely for a team:
```json
{ "mcpServers": {} }
```

To restrict to an allowlist of approved remote servers:
```json
{
  "allowManagedMcpServersOnly": true,
  "allowedMcpServers": [
    { "serverUrl": "https://api.githubcopilot.com/*" },
    { "serverUrl": "https://mcp.sentry.dev/*" }
  ]
}
```

Use `serverUrl` or `serverCommand` entries — not `serverName` — for enforcement. The server name is user-assignable and not a security control.

**Why:** CVE-2026-21852 covers ANTHROPIC_BASE_URL environment variable manipulation — an attacker overrides this variable to redirect authenticated API traffic to attacker-controlled infrastructure before any consent prompt appears. **Correction from the previous snapshot:** CVE-2026-21852 is fully patched (v2.0.65+); it is not contested or partially resolved. A *separate*, distinct vulnerability — disclosed by Mitiga Labs, with no CVE number assigned — involves malicious npm postinstall hooks rewriting `~/.claude.json`; Anthropic's response to that disclosure was that it is "out of scope," reasoning that the attack requires prior code execution through a package installation the user already consented to. As of the CSO Online article's publication, no patch exists for that separate, unnamed issue. A managed allowlist protects against both: even if a developer's config is manipulated by either attack, illegitimate servers are blocked before they can connect.

**⚠️ WARNING — a separate, unpatched npm-postinstall attack exists (not CVE-2026-21852):** Do not conflate the two. CVE-2026-21852 (ANTHROPIC_BASE_URL override) is fully patched — treat it as resolved. The Mitiga-disclosed npm-postinstall/`~/.claude.json`-rewrite attack has no CVE number and, per Anthropic's own stated position, no patch is planned. Do not install untrusted npm packages in a project you open with Claude Code, since package installation is exactly the prerequisite Anthropic's "out of scope" reasoning depends on. See the "Held pending" section below.

**Caveat:** `deniedMcpServers` always merges from all settings sources, including user settings — so users can always block servers for themselves. A previously allowed server that is later blocked disappears silently from `/mcp` with no warning to the user — communicate policy changes proactively. Also: `managed-mcp.json` cannot be delivered through server-managed settings; it requires a system-level file deployed by MDM, GPO, or fleet management.

**Sources:**
- [code.claude.com/docs/en/managed-mcp](https://code.claude.com/docs/en/managed-mcp) (fetched 2026-07-02): full allowlist/denylist reference; `serverName` security warning; deployment paths
- [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) (fetched 2026-07-02): `allowManagedMcpServersOnly`, `deniedMcpServers`, managed-only settings table
- [csoonline.com — Claude Code has an MCP security problem](https://www.csoonline.com/article/4181230/claude-code-has-an-mcp-security-problem-and-your-developers-are-already-using-it.html) (fetched 2026-07-29, re-verified this refresh): "Anthropic patched those vulnerabilities after Check Point's disclosure" (CVE-2026-21852); separately, Anthropic's response to the Mitiga-disclosed npm-postinstall issue: "the issue was out of scope, reasoning that the attack requires prior code execution through a package installation that the user consented to" — "As of this writing, no patch exists. The attack chain is live."
- [research.checkpoint.com — RCE and API token exfiltration through Claude Code project files (CVE-2025-59536)](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/) (fetched 2026-07-29): independent confirmation — "All reported issues have been successfully patched prior to this publication," describing the ANTHROPIC_BASE_URL/CVE-2026-21852 component as resolved
- [blog.cyberdesserts.com/ai-agent-security-risks/](https://blog.cyberdesserts.com/ai-agent-security-risks/) (fetched 2026-07-02): independent corroboration of hook injection and config-file attack vectors

**Confidence:** ✅ independently-corroborated (Anthropic docs + CSO Online incident reporting + independent security research)

---

## Practice 8: Enable OpenTelemetry audit logging for MCP tool calls — do not fly blind in production

**Do:** Export MCP tool-call telemetry to a SIEM (Security Information and Event Management — a tool like Splunk, Datadog, or Elastic that stores and searches logs from many systems in one place; for personal use, a simpler alternative is redirecting OTLP output to a local log file or a hosted log service like Grafana Cloud). Set the following environment variables — **replace ALL placeholder values before using**:

```bash
CLAUDE_CODE_ENABLE_TELEMETRY=1
OTEL_LOGS_EXPORTER=otlp
OTEL_LOG_TOOL_DETAILS=1
OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=http/protobuf
OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=https://<YOUR-SIEM-HOSTNAME>:4318/v1/logs
OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer <YOUR-BEARER-TOKEN>"
```

Replace `<YOUR-SIEM-HOSTNAME>` with your actual log endpoint and `<YOUR-BEARER-TOKEN>` with your actual bearer token. Using these placeholder values literally will result in silent monitoring failure — logs will appear to send but arrive nowhere, and you will believe you have audit coverage when you do not.

With `OTEL_LOG_TOOL_DETAILS=1`, every MCP tool call emits a `tool_result` event including `mcp_server_name`, `mcp_tool_name`, and `tool_input` (truncated at approximately 4 KB). `tool_decision` events record whether each call was allowed or denied and why.

**Why:** If an MCP server is hijacked or a developer accidentally connects a malicious one, you need a record of what it did. The Anthropic security page explicitly lists "Monitor Claude Code usage through OpenTelemetry metrics" as a team security practice. Without this, the CSO Online researchers noted that "the IP address in the provider's logs resolves to Anthropic's egress range. The user is real. The session is valid" — the attack looks identical to legitimate use from the provider's side.

**Caveat:** Telemetry is opt-in and off by default. Prompt content and tool arguments are redacted by default even when telemetry is enabled — you must set `OTEL_LOG_TOOL_DETAILS=1` explicitly to get MCP call arguments. Telemetry goes only to your configured OTLP endpoint; it is not sent to Anthropic. 🕒 verify live: metric names, attribute names, and the truncation limit may change across Claude Code versions. Check [code.claude.com/docs/en/monitoring-usage](https://code.claude.com/docs/en/monitoring-usage) before deploying.

**Sources:**
- [code.claude.com/docs/en/monitoring-usage](https://code.claude.com/docs/en/monitoring-usage) (fetched 2026-07-02): full OTel schema; `tool_result`, `tool_decision`, `mcp_server_connection` event definitions; SIEM example
- [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (fetched 2026-07-02): "Monitor Claude Code usage through OpenTelemetry metrics" listed as a team security best practice
- [csoonline.com — Claude Code has an MCP security problem](https://www.csoonline.com/article/4181230/claude-code-has-an-mcp-security-problem-and-your-developers-are-already-using-it.html) (fetched 2026-07-02): attacker traffic indistinguishable from legitimate traffic in provider logs; audit trail motivation

**Confidence:** ✅ independently-corroborated (Anthropic docs + independent security reporting on the forensic gap)

---

## Held pending fixes (not publish-ready)

- **CVE-2026-21852 core attack — contested, unpatched:** CSO Online confirmed Anthropic's position: the npm post-install hook / config-rewrite attack vector is "out of scope" and no patch is planned. The partial fix (ANTHROPIC_BASE_URL component, addressed in v2.0.65+) does not resolve the core attack chain. This entry describes both components separately and marks the unpatched component as contested. A future snapshot should track whether Anthropic's position changes.
- **Claude Code MCP client 2026-07-28 support ⚠ #pending (new this refresh):** Could not confirm from Anthropic's own docs whether/when Claude Code's MCP client added support for the final 2026-07-28 spec (stateless transport, RFC 9728/9207). Readers connecting Claude Code to a server that has already upgraded to 2026-07-28-only should verify compatibility directly rather than assume it.

## CHANGELOG (grading → this entry)

Carried forward from 2026-07-02 snapshot (unchanged content, items 1–17 — see prior snapshot's CHANGELOG for full detail). New items for this 2026-07-29 refresh:

18. **Refresh trigger:** MCP 2026-07-28 spec confirmed published as FINAL (was RC at time of prior snapshot). Banner rewritten to reflect final status and to clarify the client-side impact on Claude Code users is limited (transport details are SDK-internal) but connection *compatibility* with upgraded servers needs verification.
19. Background section: added note that the protocol is now stateless at the transport level and that this is transparent to day-to-day Claude Code usage.
20. Practice 6: caveat updated to flag tool-poisoning-vs-2026-07-28 as unresearched rather than silently carrying forward old text.
21. Added new pending item: Claude Code's own MCP-client support timeline for 2026-07-28 could not be confirmed this session.
22. **Skeptic FIX-10 — corrected (had been missed in the first correction pass):** Practice 6's caveat wrongly said the 2026-07-28 spec's effect on tool-poisoning/prompt-injection guidance was "unresearched." Corrected: the core tool-safety principle is confirmed carried forward verbatim; the revision adds no new countermeasures, but the topic is not unaddressed.
