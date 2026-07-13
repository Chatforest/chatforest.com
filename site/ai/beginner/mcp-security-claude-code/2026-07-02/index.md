# MCP Security in Claude Code — Best Practices (Beginner Guide) (as of 02 Jul 2026)

> How to securely configure, discover, and use MCP servers when Claude Code is the client — covering permission modes, trust settings, sandboxing, tool restrictions, audit logging, and documented real-world incidents (CVE-2025-68143/144/145, CVE-2026-21852) — as of 02 Jul 2026. Written for people new to AI, Claude Code, and the command line.


<!-- content/ai/beginner/mcp-security-claude-code/2026-07-02/index.md — immutable dated snapshot -->

# MCP Security in Claude Code — Beginner Guide (as of 02 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **02 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

> ⚠️ **Upcoming spec change:** The 2026-07-28 MCP specification finalizes July 28, 2026. This
> does not directly affect Claude Code's permission model, but any MCP server you connect to that
> implements OAuth authorization will need to update to the new spec (mandatory RFC 9728, RFC 9207
> issuer validation). 🕒 **Verify your MCP servers' auth compliance after July 28.**

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving; check the current value

---

## Background: What is MCP and why does security matter here?

Claude Code is Anthropic's AI coding assistant that you run on your own computer. By itself it can read and write files and run shell commands. But it can also connect to external tools — databases, GitHub, Slack, internal company systems — through a system called **MCP (Model Context Protocol)**.

Think of an MCP server as a plug-in that gives Claude a new capability. Each plug-in is a small program. **stdio servers** (pronounced "standard eye-oh") are plug-ins that run directly on your computer as child processes, launched by Claude Code, with data flowing through the program's input/output streams. Remote servers run over the internet (HTTPS).

**Why does this matter to you?** A plug-in that runs on your computer can read your files, access your passwords, and send data over the internet. If the plug-in is malicious — or if an attacker tricks Claude into following hidden instructions — the result can be real harm: leaked passwords, deleted files, or money spent on API calls you did not authorize. The eight practices in this guide are the most important safeguards. You do not need to be a programmer to follow them.

---

## Practice 1: Never connect an MCP server you do not explicitly trust — treat every server as untrusted code

**What this means in plain English:** Before you add any MCP plug-in to Claude Code, make sure you know who made it and whether it is safe. Do not just grab the first one you find online.

**What to do:** Before running `claude mcp add` (the command that adds a new plug-in), verify you know who maintains the server, where its source code lives, and whether it has had security issues. You may prefer servers from the Anthropic Directory (claude.ai/directory — requires sign-in). However, being listed in the Directory means Anthropic checked it meets their listing criteria — it does NOT mean Anthropic audited it for security. Treat any server you connect as if it has the same access to your computer as a program you downloaded and installed yourself.

**Why it matters for you:** An MCP server runs as a program on your machine. It can read files, make network requests, and feed Claude instructions through tool responses. Anthropic does not security-audit or manage any MCP server. Independent security researchers found more than 492 MCP servers publicly reachable with zero authentication and zero encryption. Separately, 36.7% of more than 7,000 analyzed servers were found vulnerable to a type of attack (server-side request forgery) that lets an attacker redirect the server's network requests to their own systems.

**What goes wrong if you skip this:** You install a plug-in that quietly reads your SSH keys (the files that let you log in to remote computers) or your AWS credentials (the keys that control cloud services that cost real money) and sends them to a stranger.

**Caveat:** The Anthropic Directory listing review is a bar for inclusion, not a security certification. Do not conflate "listed in the Directory" with "audited and safe." Anthropic's own guidance is: "We encourage either writing your own MCP servers or using MCP servers from providers that you trust."

**Sources:**
- [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (fetched 2026-07-02): "We encourage either writing your own MCP servers or using MCP servers from providers that you trust"
- [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-07-02): "Anthropic reviews connectors against its listing criteria before adding them to the Anthropic Directory, but does not security-audit or manage any MCP server"
- [blog.cyberdesserts.com/ai-agent-security-risks/](https://blog.cyberdesserts.com/ai-agent-security-risks/) (fetched 2026-07-02): independent security research documenting unauthenticated public MCP servers and SSRF findings (relaying Trend Micro and BlueRock Security data)
- [code.claude.com/docs/en/managed-mcp](https://code.claude.com/docs/en/managed-mcp) (fetched 2026-07-02)

**Confidence:** ✅ independently-corroborated (Anthropic docs + independent security research)

---

## Practice 2: Keep the default permission mode; know what you are giving up before changing it

**What this means in plain English:** Claude Code has a setting that controls how much freedom it has to act on its own. The safest setting asks you before doing anything significant. The most dangerous setting skips all those questions. Leave the safe setting on.

**What to do:** Leave Claude Code in `default` permission mode for normal work. Only switch to `bypassPermissions` (which can also be triggered with `--dangerously-skip-permissions`) inside an isolated container or virtual machine — a completely separate environment that is cut off from your real files and credentials. If you do not know what that means yet, do not switch away from `default`.

**The three modes most important for beginners** (there are six total — 🕒 verify live as the lineup may change across versions):

| Mode | What it does | When to use it |
|---|---|---|
| `default` | Asks before file edits and shell commands | Everyday use — recommended for most work |
| `plan` | Read-only; no file writes | When you only want Claude to look and suggest, never act |
| `bypassPermissions` | Skips ALL permission prompts | Isolated containers only — never on your real machine |

The other three modes (`acceptEdits`, `dontAsk`, `auto`) exist for more advanced or automated workflows. For a beginner, `default` for everyday work and `plan` for read-only exploration are the two you need to know.

**⚠️ WARNING — dangerous default:** `bypassPermissions` skips all permission prompts and protected-path checks. Protected paths include `.git`, `.config/git`, `.vscode`, `.idea`, `.husky`, `.cargo`, `.devcontainer`, `.yarn`, `.mvn`, `.claude` (except worktrees), shell RC files (`.bashrc`, `.zshrc`, etc.), `.npmrc`, `.mcp.json`, `.claude.json`, and others. It does NOT protect `~/.ssh` or `~/.aws` directories — those are protected by the separate sandboxing credential feature (see Practice 5). If a malicious MCP tool result injects instructions while `bypassPermissions` is active, Claude will execute them without asking. Anthropic's docs state: "`bypassPermissions` offers no protection against prompt injection or unintended actions."

**Why it matters for you:** The default mode asks you before Claude edits files or runs commands. That pause is the moment where you, as the human, catch something wrong. Removing it turns a slow-moving mistake into an instant one — if Claude is being manipulated by a bad plug-in, you lose your chance to stop it.

**What goes wrong if you skip this:** Claude follows hidden attacker instructions and deletes files, exfiltrates credentials, or makes expensive API calls — all without a single confirmation prompt.

**Sources:**
- [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) (fetched 2026-07-02): full permission mode table with all six modes; bypassPermissions warning quoted verbatim; protected paths list
- [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-07-02): specific protected paths and credential protection (sandboxing)

**Confidence:** 📄 vendor-documented

---

## Practice 3: Block specific MCP tools you do not need using deny rules

**What this means in plain English:** When you add an MCP plug-in, it often comes with many tools — some you want, some you do not. You can write a short rule in a settings file to block the tools you do not want, so Claude cannot use them even by accident.

**What to do:** You will edit a settings file called `settings.json`. There are two locations:
- `~/.claude/settings.json` — applies to all your projects (user scope)
- `.claude/settings.json` at the root of a specific project folder — applies only to that project

The `~` symbol means "your home folder" (for example, `/home/yourname/` on Linux).

If these files do not exist yet, create them: open your terminal and run:
```
mkdir -p ~/.claude && touch ~/.claude/settings.json
```
Then open the file in any text editor.

To block all tools from a specific MCP server (for example, one called `filesystem`):
```json
{
  "permissions": {
    "deny": [
      "mcp__filesystem"
    ]
  }
}
```

To block one specific tool from a server (for example, `create_repository` from `github`):
```json
{
  "permissions": {
    "deny": [
      "mcp__github__create_repository"
    ]
  }
}
```

To block all MCP tools entirely:
```json
{
  "permissions": {
    "deny": ["mcp__*"]
  }
}
```

The pattern is always `mcp__<servername>__<toolname>` for a specific tool, or `mcp__<servername>` for all tools from that server.

You can also block a tool for just one session by adding a flag when you start Claude:
```
claude --disallowedTools "mcp__filesystem__write_file"
```

**Why it matters for you:** A read-only plug-in (for example, one that looks up a Jira ticket) may also have tools that can write or delete (for example, closing that ticket). Deny rules let you take exactly the tools you need and block the rest.

**What goes wrong if you skip this:** Claude uses a write or delete tool you did not notice the plug-in had, modifying things you did not intend.

**Caveat:** Deny rules are evaluated before allow rules. A broad `mcp__*` deny cannot be overridden by a narrower allow rule — it blocks everything. Rule precedence is: deny then ask then allow. A `serverName` entry in an allowlist is NOT a security control — users can name any server anything; use `serverUrl` or `serverCommand` entries for enforcement. Cross-reference Practice 4 for scope decisions (project vs. user settings).

**Sources:**
- [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-07-02): MCP permission rule syntax, `mcp__*` wildcard behavior, deny-before-allow precedence
- [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) (fetched 2026-07-02): `disabledMcpjsonServers`, `enabledMcpjsonServers` settings reference

**Confidence:** 📄 vendor-documented

---

## Practice 4: Keep credentials out of shared project files — use environment variables instead

**What this means in plain English:** When you add an MCP plug-in that needs a password or API key, do not put the actual secret value in the project configuration file that gets shared with teammates or uploaded to the internet. Put only a placeholder name there, and store the real value separately on your own machine.

**What to do:** When adding an MCP server, choose your scope deliberately:
- `--scope local` (default): stored in `~/.claude.json` under your current project path; not shared with teammates and not checked into git.
- `--scope project`: written to `.mcp.json` in the project root and committed to version control. Every teammate who clones the repo sees it.
- `--scope user`: stored in `~/.claude.json` globally; available in all your projects but not shared.

For servers that require credentials (API keys, tokens), use `local` or `user` scope — never embed secrets in `.mcp.json`. Instead, use `${VAR}` environment variable expansion so the file contains only the variable name, not the value. For example, the file would contain `${GITHUB_TOKEN}` rather than your actual token value.

To set the actual value, add it to your shell profile before starting Claude Code. Open `~/.bashrc` or `~/.zshrc` in a text editor and add a line like:
```
export GITHUB_TOKEN=your-actual-token
```
Then either restart your terminal or run `source ~/.bashrc` (or `source ~/.zshrc`). Alternatively, if you use a tool like `direnv`, you can put this in a `.env` file in your project directory.

**⚠️ WARNING:** `.mcp.json` is committed to git by default. Any secret placed in its `env` block will be in version control history.

**Why it matters for you:** Git (version control software) keeps a permanent history of every file you commit, including deleted lines. If you put a password in `.mcp.json` and commit it — even once, then delete it — the password is still in the history. Anyone who can read the repo can find it.

**What goes wrong if you skip this:** Your API key ends up in a public GitHub repository. Automated scanners find it within minutes and start running up charges on your account.

**Caveat:** Project-scoped servers in `.mcp.json` require a workspace trust dialog before Claude Code activates them. 🕒 verify live — specific version-pinned behavior references change frequently; check the current changelog rather than relying on a pinned version for behavior verification.

**Sources:**
- [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-07-02): full scope table, environment variable expansion examples
- [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) (fetched 2026-07-02): scope priority order, `allowedMcpServers`, `deniedMcpServers`, `enableAllProjectMcpServers`

**Confidence:** 📄 vendor-documented

---

## Practice 5: Turn on sandbox mode to limit the damage if something goes wrong

**What this means in plain English:** Claude Code has a safety cage for shell commands — a "sandbox" that restricts what those commands can read or touch. It is turned off by default. Turn it on.

**What to do:** Add this to `~/.claude/settings.json` (to protect all your projects) or to `.claude/settings.json` at the root of a specific project. On Linux and Mac, open the file in a text editor and add:

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

On Linux and Mac, `~` means your home directory. On Windows with WSL2 (a way to run Linux inside Windows), use the WSL path format — for example `/home/yourname/` — rather than a Windows `C:\` path.

Replace `GITHUB_TOKEN` and `NPM_TOKEN` with the names of any secret environment variables you actually use. The `~/.aws/credentials` and `~/.ssh` paths protect your AWS cloud keys and your SSH login keys respectively.

**⚠️ WARNING — dangerous default:** Sandboxing is OFF by default. The sandbox also does not apply to Claude's built-in Read/Edit/Write file tools — only to Bash (shell) commands. Without the `credentials` block, sandboxed commands can still read `~/.aws/credentials`. Set `failIfUnavailable: true` to make missing sandbox dependencies a hard failure rather than a silent fallback to unsandboxed execution. Note: the sandbox does not run on native Windows — on native Windows this config block will silently do nothing unless `failIfUnavailable: true` is set, which will cause Claude Code to refuse to run Bash commands entirely until WSL2 is configured.

**Why it matters for you:** MCP tool results can contain hidden instructions (called prompt injection — explained in Practice 6). If Claude is tricked into running a malicious shell command, the sandbox restricts what that command can read or write. Without it, a single poisoned tool response could exfiltrate your SSH private key (the file that lets you log in to remote computers) or your AWS credentials (the keys that control cloud spending) — because the docs explicitly warn: "the default read behavior allows reading credential files such as `~/.aws/credentials` and `~/.ssh/`."

**What goes wrong if you skip this:** A malicious MCP plug-in tricks Claude into running a shell command that copies your SSH private key to a remote server. You do not know until someone logs into your accounts.

**Caveat:** The sandbox network proxy does not terminate TLS, so it cannot inspect encrypted traffic. A command with permission to reach `github.com` could use domain fronting to reach other hosts. For higher-assurance environments, configure a custom proxy with TLS inspection.

**Sources:**
- [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-07-02): full sandbox reference; credential protection, TLS caveat, `failIfUnavailable`, `allowUnsandboxedCommands`
- [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (fetched 2026-07-02): sandboxed bash tool described as a built-in protection; defense-in-depth recommendation

**Confidence:** 📄 vendor-documented

---

## Practice 6: Treat everything an MCP plug-in sends back as potentially hostile

**What this means in plain English:** When an MCP plug-in fetches data from the internet — a GitHub issue, a README file, a database row — that data might contain hidden instructions aimed at Claude. This is called **prompt injection**: an attacker plants text inside content that Claude reads, and Claude follows that text as if it were your instructions. Real CVEs (publicly documented security vulnerabilities) have been found exploiting this exact pattern.

**What to do:** Follow these precautions:
1. Review suggested commands before approving them — read what Claude wants to do before clicking yes.
2. Do not pipe untrusted external content directly to Claude.
3. Be extra cautious with MCP servers that fetch content from the web (README files, GitHub issues, external APIs) — each fetch is a potential injection vector.
4. Keep `curl`, `wget`, and network-fetching commands in the deny list (see Practice 3) unless explicitly needed; if needed, use `WebFetch(domain:...)` rules to constrain to specific domains.
5. Do not use `bypassPermissions` or `auto` mode when connected to MCP servers that read external content you do not control.

**Why it matters for you:** In January 2026, security researchers found three CVEs (published security vulnerabilities with official tracking numbers) in Anthropic's own official `mcp-server-git` plug-in. Malicious content inside a repository triggered Git operations that executed arbitrary scripts — meaning an attacker's text inside a project file made Claude run code on the researcher's machine. The three CVEs:
- **CVE-2025-68145**: path validation bypass
- **CVE-2025-68143**: unrestricted git_init (the plug-in could initialize git repositories in places it should not)
- **CVE-2025-68144**: argument injection in git_diff (attacker-controlled text was passed as a command argument)

**What goes wrong if you skip this:** You ask Claude to summarize a GitHub issue. That issue contains hidden text that instructs Claude to copy your SSH key to a remote server. Claude does it.

**Caveat:** Claude Code runs some mitigations already: an isolated context window for web fetches, trust verification dialogs for new MCP servers, and a separate server-side probe in auto mode that scans tool results before Claude reads them. But the security page explicitly states: "no system is completely immune to all attacks." Independent researchers confirm that model-level detection alone is insufficient; infrastructure-level controls are required.

**Sources:**
- [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (fetched 2026-07-02): prompt injection section, network command approval defaults, best practices list
- [theregister.com/2026/01/20/anthropic_prompt_injection_flaws/](https://www.theregister.com/2026/01/20/anthropic_prompt_injection_flaws/) (fetched 2026-07-02): CVE-2025-68143/144/145 in mcp-server-git; CVE-to-mechanism mapping: 68145=path validation bypass, 68143=unrestricted git_init, 68144=argument injection in git_diff
- [truefoundry.com/blog/claude-code-prompt-injection](https://www.truefoundry.com/blog/claude-code-prompt-injection) (fetched 2026-07-02): independent analysis; infrastructure-level controls recommended over model-level detection
- [arxiv.org/pdf/2512.08290](https://arxiv.org/pdf/2512.08290) (fetched 2026-07-02): preprint SoK — MCP trust assumptions absent, fine-grained capability control lacking (supporting citation, not peer-reviewed)

**Confidence:** ✅ independently-corroborated (Anthropic docs + The Register CVE reporting + independent security researchers)

---

## Practice 7: For teams — enforce an approved plug-in list through managed settings

**What this means in plain English:** If you work at a company with an IT team, those IT administrators can centrally control which MCP plug-ins developers are allowed to use — so one developer's mistake does not put the whole organization at risk. If you are working alone on a personal project and have no IT team, this practice is out of scope for your setup — focus on Practices 1 through 5 instead.

**What to do:** Organizations using Claude Code on Team or Enterprise plans should configure `allowedMcpServers` and `allowManagedMcpServersOnly: true` through server-managed settings or MDM. MDM stands for Mobile Device Management — software like Jamf, Intune, or Mosyle that your IT team uses to push settings to all company computers automatically.

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

**Why it matters for teams:** CVE-2026-21852 describes a documented attack with two parts: (a) an attacker overrides the `ANTHROPIC_BASE_URL` environment variable to redirect authenticated API traffic to attacker-controlled infrastructure before any consent prompt appears — this component was partially addressed in Claude Code v2.0.65+; and (b) a separate attack using malicious npm packages or hook injection to rewrite configuration files — Anthropic's stated position is that this component is "out of scope" for patching, and no patch is planned for it. A managed allowlist means that even if a developer's config is manipulated, illegitimate servers are blocked before they can connect.

**⚠️ WARNING — CVE-2026-21852 patch status is contested:** The ANTHROPIC_BASE_URL manipulation component was addressed in v2.0.65+. The config-file/hook attack chain remains unpatched by Anthropic's own statement. Do not assume the full CVE is resolved. See the "Held pending" section below.

**Caveat:** `deniedMcpServers` always merges from all settings sources, including user settings — so users can always block servers for themselves. A previously allowed server that is later blocked disappears silently from `/mcp` with no warning to the user — communicate policy changes proactively. Also: `managed-mcp.json` cannot be delivered through server-managed settings; it requires a system-level file deployed by MDM, GPO, or fleet management.

**Sources:**
- [code.claude.com/docs/en/managed-mcp](https://code.claude.com/docs/en/managed-mcp) (fetched 2026-07-02): full allowlist/denylist reference; `serverName` security warning; deployment paths
- [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings) (fetched 2026-07-02): `allowManagedMcpServersOnly`, `deniedMcpServers`, managed-only settings table
- [csoonline.com — Claude Code has an MCP security problem](https://www.csoonline.com/article/4181230/claude-code-has-an-mcp-security-problem-and-your-developers-are-already-using-it.html) (fetched 2026-07-02): CVE-2026-21852; ANTHROPIC_BASE_URL override mechanism; Anthropic's "out of scope" response
- [blog.cyberdesserts.com/ai-agent-security-risks/](https://blog.cyberdesserts.com/ai-agent-security-risks/) (fetched 2026-07-02): independent corroboration of hook injection and config-file attack vectors

**Confidence:** ✅ independently-corroborated (Anthropic docs + CSO Online incident reporting + independent security research)

---

## Practice 8: For teams with IT infrastructure — enable audit logging to record what MCP plug-ins do

**What this means in plain English:** This practice is for organizations whose IT team already runs monitoring and logging infrastructure. If you are a solo beginner on a personal project, you do not have the infrastructure this requires — you can note it exists and return to it later. The core idea: keep a permanent record of every action an MCP plug-in takes, so that if something goes wrong, you can find out exactly what happened.

**What to do:** Export MCP tool-call telemetry (detailed activity records) to a SIEM — that stands for Security Information and Event Management, a tool like Splunk, Datadog, or Elastic that stores and searches logs from many systems in one place. For personal use, a simpler alternative is redirecting the output to a local log file or a hosted log service like Grafana Cloud.

Set the following environment variables before starting Claude Code — **replace ALL placeholder values before using**:

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

**Why it matters for teams:** If an MCP server is hijacked or a developer accidentally connects a malicious one, you need a record of what it did. The Anthropic security page explicitly lists "Monitor Claude Code usage through OpenTelemetry metrics" as a team security practice. Without this, security researchers noted that "the IP address in the provider's logs resolves to Anthropic's egress range. The user is real. The session is valid" — meaning an attack looks identical to legitimate use from the outside. Without your own logs, you cannot tell the difference.

**Caveat:** Telemetry is opt-in and off by default. Prompt content and tool arguments are redacted by default even when telemetry is enabled — you must set `OTEL_LOG_TOOL_DETAILS=1` explicitly to get MCP call arguments. Telemetry goes only to your configured OTLP endpoint; it is not sent to Anthropic. 🕒 verify live: metric names, attribute names, and the truncation limit may change across Claude Code versions. Check [code.claude.com/docs/en/monitoring-usage](https://code.claude.com/docs/en/monitoring-usage) before deploying.

**Sources:**
- [code.claude.com/docs/en/monitoring-usage](https://code.claude.com/docs/en/monitoring-usage) (fetched 2026-07-02): full OTel schema; `tool_result`, `tool_decision`, `mcp_server_connection` event definitions; SIEM example
- [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (fetched 2026-07-02): "Monitor Claude Code usage through OpenTelemetry metrics" listed as a team security best practice
- [csoonline.com — Claude Code has an MCP security problem](https://www.csoonline.com/article/4181230/claude-code-has-an-mcp-security-problem-and-your-developers-are-already-using-it.html) (fetched 2026-07-02): attacker traffic indistinguishable from legitimate traffic in provider logs; audit trail motivation

**Confidence:** ✅ independently-corroborated (Anthropic docs + independent security reporting on the forensic gap)

---

## Held pending fixes (not publish-ready)

- **CVE-2026-21852 core attack — contested, unpatched:** CSO Online confirmed Anthropic's position: the npm post-install hook / config-rewrite attack vector is "out of scope" and no patch is planned. The partial fix (ANTHROPIC_BASE_URL component, addressed in v2.0.65+) does not resolve the core attack chain. This entry describes both components separately and marks the unpatched component as contested. A future snapshot should track whether Anthropic's position changes.

## CHANGELOG (grading → this entry)

1. **CC-F1** (Skeptic FIX): Practice 2 protected-paths list corrected — removed `~/.ssh` and `~/.aws` from the bypassPermissions description. Those paths are protected by the sandboxing credential feature (Practice 5), NOT by the permission-modes system. Added correct protected paths list.
2. **CC-F2** (Skeptic FIX): Practice 7 CVE-2026-21852 mechanism corrected and split. Draft conflated two distinct attacks under one CVE: (a) ANTHROPIC_BASE_URL env-var override / API-key exfil (per CSO Online; addressed in v2.0.65+) and (b) npm post-install hook / config-file rewrite (per cyberdesserts; Anthropic position: out of scope, unpatched). Now described separately with individual patch status.
3. **CC-F3** (Skeptic FIX): Practice 6 CVE-2025-68143/144/145 mechanism mapping corrected: 68145=path validation bypass, 68143=unrestricted git_init, 68144=argument injection in git_diff.
4. **CC-F4** (Skeptic FIX): Practice 1 quote de-quoted — specific sentence not found verbatim on security page re-fetch; replaced with paraphrase matching confirmed page text.
5. **B-KILL-2** (Beginner KILL): Practice 8 telemetry placeholders changed from realistic-looking values (`your-token`, `your-siem.example.com`) to angle-bracket placeholders (`<YOUR-BEARER-TOKEN>`, `<YOUR-SIEM-HOSTNAME>`) with an explicit bold warning about literal use causing silent monitoring failure.
6. **B-KILL-3** (Beginner KILL): Practice 5 sandbox config — added target file paths (`~/.claude/settings.json` or `.claude/settings.json`), promoted Windows incompatibility warning to the Do section (not buried in caveat), added path notation note for WSL2.
7. **B-FIX-5** (Beginner FIX): Practice 3 — added file creation instructions (`mkdir -p ~/.claude && touch ~/.claude/settings.json`), cross-reference to Practice 4 for scope explanation.
8. **B-FIX-6** (Beginner FIX): Practice 7 — defined MDM with examples (Jamf, Intune, Mosyle); added "if you do not have an IT team, this practice is out of scope for your setup" to prevent solo developers from attempting enterprise infrastructure.
9. **B-FIX-7** (Beginner FIX): Practice 8 — defined SIEM with examples (Splunk, Datadog, Elastic); added personal-use alternative (local log file, Grafana Cloud).
10. **B-FIX-12** (Beginner FIX): Added stdio definition to Background section at first use.
11. **B-FLAG-3** (Beginner FLAG): Practice 4 — added `export GITHUB_TOKEN=your-actual-token` example with `~/.bashrc`/`~/.zshrc` and direnv options.
12. **B-FLAG-4** (Beginner FLAG): Practice 1 — moved "listed does not mean audited" note to the practice body (not only the caveat).
13. **B-FLAG-7** (Beginner FLAG): Practice 5 — added WSL2 path notation note alongside the `~/.aws/credentials` and `~/.ssh` path examples.
14. **T-FIX-1** (Timekeeper FIX): Practice 2 — expanded permission mode list from four to all six modes (added `acceptEdits` and `plan`); `plan` mode highlighted as the safest option for read-only work; added 🕒 verify live for mode lineup.
15. **T-FIX-2** (Timekeeper FIX): Practice 4 — removed specific version number `v2.1.196` from caveat (v2.1.197 released 2026-07-01, already behind); replaced with 🕒 verify live guidance to check current changelog.
16. Added global spec-change banner for 2026-07-28 MCP RC at top of entry.
17. **BEGINNER-REWRITE** (re-leveled from the 2026-07-02 technical entry; facts unchanged): All eight practices restructured with plain-English "what this means / why it matters / what to do / what goes wrong" framing. Jargon expanded on first use (MCP server, stdio, prompt injection, SIEM, MDM, CVE, git, SSH). Practice 2 permission table simplified to three most important modes for beginners with note that six exist total. Practice 7 and Practice 8 clearly labeled as team/IT-infrastructure practices, not for solo beginners. All warnings, CVE references, and 🕒 verify live labels preserved. No new URLs or facts introduced.
18. **Link-check gate (2026-07-03):** claude.ai/directory returns 403 (requires sign-in; not a dead page). Converted Anthropic Directory hyperlink to plain text per policy; citation retained.

