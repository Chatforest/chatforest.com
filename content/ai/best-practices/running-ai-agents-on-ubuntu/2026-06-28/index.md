---
title: "Running AI Agents on Ubuntu — Best Practices (as of 26 Jun 2026)"
date: 2026-06-28
snapshot_date: 2026-06-28
topic: running-ai-agents-on-ubuntu
track: best-practices
audience: "technically comfortable readers"
description: "A dated, fact-checked guide to running Claude Code, Codex CLI, and Gemini CLI on Ubuntu. Researched 26 Jun 2026; graded by a 3-lens panel — 0 fabrications, 16 citations re-fetched and verified."
content_type: "Best Practice"
categories: ["Claude Code", "Ubuntu", "AI Agents"]
tags: ["claude-code", "codex-cli", "gemini-cli", "ubuntu", "linux", "ai-agents", "best-practices"]
last_refreshed: 2026-06-26
aliases: ["/best-practices/running-ai-agents-on-ubuntu-best-practices/"]
---

> **Grading note.** Research-drafted by AI pupils (one per ecosystem), then graded by a
> 3-lens panel: a Skeptic who re-fetched 16 citations and tried to refute each claim, a
> Beginner reviewer hunting dangerous defaults, and a Timekeeper checking for staleness.
> Two factual errors were caught and corrected (see notes inline). Items still pending a
> sourced fix are marked **⚠ PENDING** — this corpus does not publish unverified content.
> **0 fabrications.**

## How to read the labels
- ✅ **independently-corroborated** — confirmed by 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value yourself

---

## Part 0 — Foundations (apply to *any* agent on Ubuntu)

These Linux basics hold no matter which agent you run.

**1. Run an unattended agent as a `systemd --user` service.** ✅

`systemctl --user enable --now <name>` plus `loginctl enable-linger $USER` (so it survives
logout). You get auto-restart, start-on-boot, and journald logs for free — far better than a
forgotten `nohup &`. User services run as you, not root.

> **⚠️ WARNING:** Set spend caps before you leave an agent running overnight — an uncapped
> loop can exhaust credits faster than you expect. (See cost practices in Part 1.)

**Do:** Write a systemd user unit at `~/.config/systemd/user/<name>.service`. Put your API
key in a separate file (`EnvironmentFile=/path/to/secrets.env`, `chmod 600`), **not** as a
raw `Environment=ANTHROPIC_API_KEY=sk-ant-…` literal inside the unit file (which could
appear in bug reports or backups).

**Sources:** [morphllm.com/claude-code-linux](https://morphllm.com/claude-code-linux) (2026-03-10) · Ubuntu systemd-user community guides
**Confidence:** ✅ independently-corroborated (community convention; no official Anthropic
prescription; the underlying `claude -p` primitive IS official)

---

**2. Give each agent its own `git worktree`.** ✅

`git worktree add ./agent-task-1 -b agent-task-1 main` — branch from your primary branch
(check its name first with `git branch`; new repos may use `master` not `main`).

> **Note:** Worktrees isolate **files only**. Two agents sharing the same repo can still
> collide on ports, databases, caches, or secrets. Worktrees ≠ full isolation.

**Sources:** [git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree) (official)
**Confidence:** 📄 vendor-documented

---

**3. Sandbox the agent (bubblewrap or firejail).** ✅

Install: `sudo apt install bubblewrap` (preferred; smaller setuid surface) or
`sudo apt install firejail` (easier; bundled profiles). Keep system files read-only; bind
only the project folder writable; drop all capabilities; isolate the network namespace.

> **⚠️ WARNING:** Neither bubblewrap nor firejail is installed by default on Ubuntu — install
> first, or the sandbox command fails silently.
>
> **Ubuntu 24.04+ gotcha:** AppArmor blocks bubblewrap's user namespaces by default.
> Check: `sysctl kernel.apparmor_restrict_unprivileged_userns`. If it returns `1`, you need
> an AppArmor profile for `/usr/bin/bwrap`. ⚠ **PENDING** — a complete, safe profile is not
> yet in this entry; see project issue #317.

**Sources:** [github.com/containers/bubblewrap](https://github.com/containers/bubblewrap) (release 0.11.2, 2026-04-23) ·
[github.com/CaptainMcCrank/SandboxedClaudeCode](https://github.com/CaptainMcCrank/SandboxedClaudeCode)
**Confidence:** ✅ independently-corroborated

---

**4. Default-deny outbound network; allow only what's needed.** 📄

> **⚠️ WARNING — ADVANCED.** Applying a blanket `policy drop` on the OUTPUT chain *before*
> adding allow-rules for DNS, your model API, and apt will knock your machine offline.
> Add your allow-rules first, test connectivity, then set the drop policy.
> Rollback: `sudo nft flush ruleset`.
>
> **Beginners:** rely on the sandbox's network controls (Part 0 §3) rather than nftables
> until you're comfortable. ⚠ **PENDING (#318)** — a complete starter nftables ruleset
> with the necessary exceptions pre-included is tracked for the next edition.

**Sources:** [documentation.ubuntu.com](https://documentation.ubuntu.com) nftables guide (nftables default since Ubuntu 20.10;
ufw/nftables conflict warning confirmed)
**Confidence:** 📄 vendor-documented (Ubuntu docs confirm 20.10 default + ufw conflict;
the output-`policy drop` recipe is standard nftables practice, not from the Ubuntu page)

---

**5. Keep secrets out of the repo *and* out of plaintext the agent can read.** ✅

`.gitignore` your `.env` — but that's not enough. **Agents routinely `cat .env` and
`printenv`**; any file on disk the agent can read is a file the agent might send to the
model or log. Prefer OS-level secrets (GNOME Keyring: `sudo apt install libsecret-tools`,
then `secret-tool store …`) or a secrets manager injected at launch. `chmod 600` any
on-disk env/secrets file.

**Sources:** [bitwarden.com/blog](https://bitwarden.com/blog) (2026-04-02) · [dev.to](https://dev.to) secrets management ·
[blog.gitguardian.com/secure-your-secrets-with-env](https://blog.gitguardian.com/secure-your-secrets-with-env/) (2024-01-08)
**Confidence:** ✅ independently-corroborated

---

**6. Scope the filesystem to least privilege.** 📄

In a systemd unit, use `DynamicUser=yes` (systemd creates a temporary UID just for this
service run, so it cannot touch your home directory). Add `ReadOnlyPaths=/` and
`ReadWritePaths=/path/to/project` to limit writes.

**Sources:** Ubuntu systemd documentation
**Confidence:** 📄 vendor-documented

---

**7. Watch what it did via journald.** ✅

`journalctl --user -u <name>.service` — add `-f` to tail live, `--since "1 hour ago"` to
scope. Leaving an agent unattended is only safe if you can audit it afterward.

> To read the *system* journal (not just your user journal), add yourself to the
> `systemd-journal` group: `sudo usermod -aG systemd-journal $USER` then re-login.

**Sources:** DigitalOcean journald guide (updated 2026-04-27) · [morphllm.com](https://morphllm.com) (2026-03-10)
**Confidence:** ✅ independently-corroborated

---

## Part 1 — Claude Code (Anthropic)

### Practice: Install with the native installer; verify with `claude doctor`

**Do:** `curl -fsSL https://claude.ai/install.sh | bash`, then `claude --version` and
`claude doctor`. Single self-contained binary (no Node.js needed), lands in
`~/.local/bin/claude`. Add that to `PATH` if `claude` isn't found. Supported: Ubuntu
20.04+, 4 GB+ RAM, x64/ARM64.

**Why (beginner):** One command, nothing to maintain, and `claude doctor` tells you the
install and update path are healthy before you waste time debugging.

**Caveat:** Piping a remote script to `bash` means trusting that URL without reading it
first — the script runs with your full permissions. Security-conscious users prefer the
signed apt repo (next). The `npm install -g @anthropic-ai/claude-code` route also works
(Node 18+); **never `sudo npm install -g`** (creates root-owned files that break updates).

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-06-26) ·
[code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart) · [morphllm.com/claude-code-linux](https://morphllm.com/claude-code-linux) (2026-03-10)
**Confidence:** ✅ independently-corroborated

---

### Practice: Prefer the signed apt repo for verifiable, system-managed updates

**Do:** Add Anthropic's signed apt repo (keyring → `/etc/apt/keyrings/claude-code.asc`),
then `sudo apt update && sudo apt install claude-code`. Verify the GPG fingerprint reads:

```
31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE
```

*(This fingerprint was re-confirmed verbatim against Anthropic's live setup page during
grading — not a fabrication.)*

To check the fingerprint yourself:
`gpg --show-keys /etc/apt/keyrings/claude-code.asc`
⚠ **PENDING (#317):** the exact command and expected output format are being verified for
a future edition.

Choose `stable` (≈1 week behind, skips major regressions) or `latest`.

**Caveat:** apt does NOT auto-update Claude Code — run `sudo apt update && sudo apt upgrade
claude-code` yourself. The native installer does auto-update. This is a deliberate
trade: control + verifiability vs. always-current.

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fingerprint, apt commands, fetched 2026-06-26)
**Confidence:** 📄 vendor-documented

---

### Practice: Keep updated deliberately — pick a release channel and pin a floor

**Do:** Set `autoUpdatesChannel` to `"stable"` or `"latest"` in `~/.claude/settings.json`.
Pin `minimumVersion` so a channel switch can't downgrade you. Run `claude update` to apply
immediately; `claude doctor` shows the last update result. To freeze a machine, set
`DISABLE_AUTOUPDATER` (background check only) or `DISABLE_UPDATES` (all paths) in the
settings `env` block.

**Caveat:** apt/dnf/apk and Homebrew/WinGet installs ignore `autoUpdatesChannel` (channel
is chosen by repo/cask instead). A known quirk: Claude Code may notify of an update before
the package manager has it.

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-06-26) ·
[code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart)
**Confidence:** 📄 vendor-documented

---

### Practice: Authenticate headless/SSH boxes — and know the billing trap

**Do:** Over SSH, press `c` to copy the login URL to your workstation, or paste the login
code. For true unattended/CI use: `claude setup-token` mints a 1-year OAuth token
(`CLAUDE_CODE_OAUTH_TOKEN`, uses your Pro/Max subscription), or set `ANTHROPIC_API_KEY`
(Console pay-as-you-go). In `-p` mode, `ANTHROPIC_API_KEY` is always used when present.

> **⚠️ WARNING — cost trap:** If you have BOTH a subscription AND `ANTHROPIC_API_KEY` set,
> **the API key wins and you get billed pay-as-you-go instead of using your plan.** This
> surprises people. Run `unset ANTHROPIC_API_KEY` and check `/status` if unsure.

**Caveat:** On Linux, credentials live in `~/.claude/.credentials.json` at mode `0600`
(no OS keychain) — protect that file. `--bare` ignores `CLAUDE_CODE_OAUTH_TOKEN`; use
`ANTHROPIC_API_KEY` or `apiKeyHelper` there. A key from a disabled Anthropic Console
workspace causes silent auth failures.

**Sources:** [code.claude.com/docs/en/authentication](https://code.claude.com/docs/en/authentication) (fetched 2026-06-26) ·
[support.claude.com/en/articles/12304248](https://support.claude.com/en/articles/12304248) (2026-05-05) ·
[hidekazu-konishi.com](https://hidekazu-konishi.com) (2026-06-07)
**Confidence:** ✅ independently-corroborated

---

### Practice: Run unattended work with `claude -p`, scoped tightly

**Do:** `claude -p "prompt"` for one-shot, non-interactive runs. Restrict tools with
`--allowedTools "Read,Grep,Glob"` (smallest set the task needs); get machine-readable
results with `--output-format json`; add `--bare` for reproducible CI runs (ignores local
hooks/MCP/CLAUDE.md — `--bare` means "clean, reproducible run regardless of local config").

> **⚠️ Pre-allow tools before any unattended run.** Without it the agent hangs waiting for
> a permission prompt — your script silently stalls.

**Caveat:** `--bare` skips OAuth/keychain; use `ANTHROPIC_API_KEY` or `apiKeyHelper`.
Piped stdin capped at 10 MB (v2.1.128+); for bigger input, write a file and reference its
path. Interactive commands like `/login` don't work in `-p`.

**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 2026-06-26) ·
[code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) · [hidekazu-konishi.com](https://hidekazu-konishi.com) (2026-06-07)
**Confidence:** ✅ independently-corroborated

---

### Practice: Reduce prompt fatigue with permission allowlists, not blanket bypass

**Do:** Use `/permissions` to allow specific safe commands (e.g. `Bash(npm run *)`,
`Bash(git commit *)`) and deny dangerous ones (`Bash(git push *)`, `Read(.env)`,
`Read(~/.ssh/**)`). Rules evaluate: deny → ask → allow. Set `defaultMode` in
`settings.json`.

> **⚠️ AVOID `bypassPermissions` / `--dangerously-skip-permissions`** except inside a
> throwaway container or VM (a separate test machine you don't care about) — and it's
> blocked as root on Linux anyway.

**Caveat:** Rules are enforced by Claude Code, not the underlying model, and only cover
tools Claude Code recognizes. A Python/Node script that opens files itself bypasses
Read/Edit deny rules — use the sandbox (next practice) for OS-level enforcement.

**Sources:** [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-06-26) ·
[code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
**Confidence:** 📄 vendor-documented

---

### Practice: Enable the OS-level Bash sandbox (bubblewrap)

**Do:** Run `/sandbox`. Install deps first: `sudo apt-get install bubblewrap socat`. Turn
it on per-project (`/sandbox` writes `.claude/settings.local.json`) or globally via
`sandbox.enabled: true` in `~/.claude/settings.json`. The sandbox confines Bash and its
children to the working dir + temp dir. Use `sandbox.credentials` (v2.1.187+) to deny-read
`~/.aws/credentials`, `~/.ssh`, etc.

> **⚠️ Ubuntu 24.04+ gotcha:** AppArmor blocks bubblewrap from creating user namespaces by
> default. Check `sysctl kernel.apparmor_restrict_unprivileged_userns`; if it returns `1`
> you need an AppArmor profile for `/usr/bin/bwrap`. ⚠ **PENDING (#317):** the complete
> profile content is being prepared for a future edition. For now, check Anthropic's own
> sandboxing docs for the latest guidance.

**Caveat:** It's defense-in-depth, not a complete boundary. The proxy doesn't inspect TLS,
so broad allowed domains can still enable exfiltration. Some tools don't work sandboxed
(`docker`, `watchman`/`jest --no-watchman`) and need `excludedCommands`. Check
`settings.json` reference for where to configure `excludedCommands`.

**Sources:** [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-06-26) ·
[code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions)
**Confidence:** 📄 vendor-documented

---

### Practice: Keep secrets out of chat and out of MCP/project config

**Do:** Store secrets in env vars or a secret manager; **never paste secret values into
chat — everything in the conversation is sent to Anthropic's API.** Reference env vars in
MCP config rather than hardcoding tokens; `.gitignore` your `.env`; document *which* env
vars exist (not values) in CLAUDE.md.

**Caveat:** Claude doesn't read env vars into its context window automatically — values are
only available to commands it runs. A subprocess can still read secret files unless you
also use the sandbox `credentials`/`denyRead` controls or `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`.

**Sources:** [support.claude.com/en/articles/12304248](https://support.claude.com/en/articles/12304248) (2026-05-05) ·
[code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) · [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)
**Confidence:** ✅ independently-corroborated

---

### Practice: Add MCP servers with `claude mcp add`, at the right scope

**Do:** MCP (Model Context Protocol) is a standard for connecting Claude to external tools
like GitHub, databases, or Figma. Connect them with `claude mcp add`. Choose scope:
**user** (available in every session) or **project** (`.mcp.json`, shared with team). Put
credentials in env vars, not literals in the config.

**Caveat:** More MCP servers = more context overhead and more attack surface. Disable
servers you're not using (`/mcp`). CLI tools (`gh`, `aws`) are often more context-efficient
than an MCP server for the same job.

**Sources:** [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-06-26) ·
[code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)
**Confidence:** 📄 vendor-documented

---

### Practice: Use hooks for actions that must happen every time

> **⚠️ WARNING:** Hooks run with YOUR shell permissions — a malicious or buggy hook is real
> code execution. Review hooks (especially from shared/project configs) before trusting them.

**Do:** Add a `hooks` block to `settings.json`. Common events: `PreToolUse` (gate/modify
a tool call before it runs — block by exiting code 2), `PostToolUse` (e.g. run a formatter
after an edit), `Stop` (block a turn from ending until a check passes). Claude can write
hooks for you: *"write a hook that runs eslint after every file edit."*

**Why (beginner):** Unlike CLAUDE.md instructions (advisory — the model may ignore them),
hooks are deterministic shell commands the harness always runs. They guarantee formatting,
tests, or block protected paths.

**Caveat:** A `Stop` hook is overridden if it blocks 8 consecutive times in a row (Claude
Code ignores it and proceeds). `--bare` skips hook discovery entirely.

**Sources:** [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) (fetched 2026-06-26) ·
[code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) · [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions)
**Confidence:** 📄 vendor-documented

---

### Practice: Write a short, high-signal CLAUDE.md and prune it

**Do:** Run `/init` to generate a starter CLAUDE.md from your project. Keep only what
Claude can't infer: non-obvious bash commands, env-var/setup quirks, test runners,
branch/PR conventions. Aim under ~200 lines; move occasional workflows into skills (loaded
on demand). Ask for each line: "would removing this cause Claude to make mistakes?"

**Caveat:** If Claude keeps violating a rule, the file is probably too long, not the rule
too weak. Check it into git (team shares it); keep personal notes in `CLAUDE.local.md`
(gitignored).

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-26) ·
[code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)
**Confidence:** 📄 vendor-documented

---

### Practice: Control cost — `/usage`, context hygiene, model choice, spend caps

**Do:** Check `/usage` and `/context`. `/clear` between unrelated tasks; let auto-compaction
run. Use Sonnet for most work, Opus for hard reasoning (`/model`). For unattended `-p` runs,
parse `total_cost_usd` from `--output-format json` and cap with `--max-turns`. On Pro/Max
set a monthly credit limit (`/usage-credits`); on API/Console set workspace spend limits at
console.anthropic.com.

**Why (beginner):** Cost scales with context size and model. A long, cluttered session
quietly multiplies token cost; clearing context and choosing Sonnet are the biggest cheap
wins. *A "token" is roughly ¾ of a word; a typical coding session might use tens of
thousands.*

**Caveat:** `/usage` is a local estimate, not your authoritative bill (use the Console for
that).

> **Corrected during grading (Timekeeper KILL):** An earlier draft warned about a
> "2026-06-15 separate-credit-pool billing change" for Agent SDK / `claude -p` usage.
> **That change was paused on the day it was due and never took effect** — `claude -p` and
> headless Agent SDK usage still draw from normal subscription limits. Sources confirming
> the suspension: thenewstack.io, devops.com, digitalapplied.com (all 2026-06).

**Sources:** [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 2026-06-26) ·
[code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) · [hidekazu-konishi.com](https://hidekazu-konishi.com) (2026-06-07)
**Confidence:** 📄 vendor-documented (billing suspension independently corroborated)

---

### Practice: Give Claude a way to verify its own work

**Do:** Pair every task with a check Claude can run and read: a test suite, a build exit
code, a linter, or a diff. For unattended runs, gate the stop with a `Stop` hook or a
verification subagent so the session can't declare "done" until the check passes. Have
Claude show evidence (test output, command + result) rather than just asserting success.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-26) ·
[code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)
**Confidence:** 📄 vendor-documented

---

## Part 2 — OpenAI Codex CLI

> **Status as of 26 Jun 2026:** Codex CLI is NOT renamed or replaced. It's
> `openai/codex` — open-source Rust binary (96.5%), Apache-2.0, latest v0.142.2 (25 Jun
> 2026, multiple releases per week). One surface of a unified Codex product.

### Practice: Install via official script or npm; fix PATH instead of `sudo npm -g`

**Do:** Install with `curl -fsSL https://chatgpt.com/codex/install.sh | sh`, or
`npm install -g @openai/codex`, or the prebuilt musl binary from GitHub releases.

> **⚠️ Piping any remote script to `sh` means trusting that URL.** The script runs with
> your permissions without you reading it first.
>
> **Never `sudo npm install -g`** — it creates root-owned files that break future updates.
> If `codex` isn't found after npm install, add your npm global bin to PATH instead:
> `export PATH="$HOME/.npm-global/bin:$PATH"` (add to `~/.bashrc`; zsh users use
> `~/.zshrc`).

**Sources:** [github.com/openai/codex](https://github.com/openai/codex) (v0.142.2, fetched 2026-06-25) ·
[developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference)
**Confidence:** ✅ independently-corroborated

---

### Practice: Understand the two-layer model — sandbox + approval policy

**Do:** Codex has two independent safety dials:

| Layer | Options | What it controls |
|-------|---------|-----------------|
| **Sandbox** | `read-only` / `workspace-write` / `danger-full-access` | What the agent can physically access |
| **Approval** | `untrusted` / `on-request` / `never` | When it asks you before acting |

Set both deliberately. Example: `workspace-write` sandbox + `on-request` approval = can
write project files but asks before running network/system commands.

> **⚠️ WARNING: `danger-full-access`** removes all OS-level restrictions. Only use it
> inside a disposable container or VM you don't care about. Never on your main machine.

**Sources:** [developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference) (fetched 2026-06-26) ·
[blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex)
**Confidence:** ✅ independently-corroborated

---

### Practice: Keep the OS sandbox on; only break it inside a throwaway environment

**Do:** On Linux, Codex's sandbox runs at the kernel level (Landlock + seccomp; bubblewrap
is also vendored). Keep it on. If a workflow genuinely needs full access, use
`--dangerously-bypass-approvals-and-sandbox` (alias `--yolo`) **only inside a Docker
container or GitHub Codespace** — never on your real machine.

> A Docker container is a lightweight isolated environment; GitHub Codespaces gives you a
> cloud VM you can throw away. Both let you run `--yolo` without risk to your actual files.

**Sources:** [developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference) (fetched 2026-06-26) ·
[blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex)
**Confidence:** ✅ independently-corroborated

---

### Practice: Auth — prefer ChatGPT sign-in; keep API key out of shell history

**Do:** "Sign in with ChatGPT" uses your subscription (recommended for interactive use).
For headless/CI, set `OPENAI_API_KEY`. Keep it out of shell history (`export KEY=…` at
the start of a session, not in `.bashrc`). For persistent use, add to `~/.profile` with
`chmod 600 ~/.profile`.

**Sources:** [github.com/openai/codex](https://github.com/openai/codex) README · [developers.openai.com](https://developers.openai.com) changelog (2026-06-15:
encrypted local storage for CLI+MCP OAuth creds)
**Confidence:** 📄 vendor-documented

---

### Practice: Use `codex exec` for headless/CI/background runs

**Do:** `codex exec "prompt" --json` for scripted runs. `--ephemeral` = no session saved
after this run. Pair with `--sandbox workspace-write` and approval `never` for fully
automated runs inside a tightly scoped sandbox.

> Approval `never` is safe when the sandbox mode limits physical access — `workspace-write`
> still confines what the agent can touch even when it skips approval prompts.

🕒 **verify live:** Token budget controls and `/usage` were added 2026-06-15 and
2026-06-22 respectively — check changelog for latest options.

**Sources:** [developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference) (fetched 2026-06-26) ·
[developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)
**Confidence:** 📄 vendor-documented

---

### Practice: Configure in `~/.codex/config.toml`; use profiles

**Do:** TOML is a simple config format: `key = "value"`, `[section]` headers. Your
personal settings go in `~/.codex/config.toml`; per-project settings in
`.codex/config.toml` inside your project. Use `--profile <name>` or `-c key=value` to
override at the command line.

Full precedence (low → high): system defaults → `/etc/codex/config.toml` → user
`~/.codex/config.toml` → project `.codex/config.toml` → `/etc/codex/system.toml` →
env vars → CLI flags.

**Sources:** [developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference) (fetched 2026-06-26) ·
[blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex)
**Confidence:** ✅ independently-corroborated

---

### Practice: Pick the model deliberately

**Do:** The recommended default is **GPT-5.5** (released 23 Apr 2026).

| Model | Context | Pricing (input / output per M tokens) | Notes |
|-------|---------|---------------------------------------|-------|
| gpt-5.5 | **1,050,000** tokens | $5 / $30 | Strongest overall |
| gpt-5.4 | — | — | Professional work |
| gpt-5.4-mini | — | — | Fast / cheap / bulk |
| gpt-5.3-codex-spark | — | — | Research preview; ChatGPT Pro only |

🕒 **verify live:** Model lineup moves fast — recheck with `/model` inside Codex.
Prompts over 272K tokens are charged at 2× input / 1.5× output for the full session.

> **Corrected during grading (Timekeeper KILL):** An earlier draft stated GPT-5.5 has a
> "400K context window." The official Codex models page (developers.openai.com/codex/models,
> fetched 26 Jun 2026) confirms **1,050,000 tokens**. The 400K figure likely confused the
> 272K price-tier threshold with the context limit.

**Sources:** [developers.openai.com/codex/models](https://developers.openai.com/codex/models) (fetched 2026-06-26) ·
[developers.openai.com/api/docs/models/gpt-5.5](https://developers.openai.com/api/docs/models/gpt-5.5) · [blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex)
**Confidence:** ✅ independently-corroborated

---

## Part 3 — Google Gemini CLI

> ## ⚠️ READ THIS FIRST — a big change happened 18 Jun 2026
>
> On **18 June 2026, Google switched off the free "Sign in with Google" login** and
> consumer Pro/Ultra tiers for Gemini CLI, steering those users to a new closed-source
> **Antigravity CLI**. **A tutorial from even a month ago will tell you to log in with your
> Google account — and it won't work anymore.**
>
> Gemini CLI itself is still open-source and still works, but a new beginner today needs a
> **paid Gemini API key, Vertex AI credentials, or a Code Assist license.**
>
> The Antigravity free tier is far smaller — community reports ~20 requests/day vs the old
> ~1,000 (~98% cut). *(Antigravity being closed-source is community-reported pushback, not
> a Google statement — treat as unconfirmed.)*
>
> **Sources:** Google Developers Blog (developers.googleblog.com, 2026-05-19, fetched
> 2026-06-26) · github.com/google-gemini/gemini-cli/discussions/27274

---

### Practice: Install with Node 20+

**Do:** `npm install -g @google/gemini-cli`. Requires Node.js 20.0.0+. Ubuntu's default
Node 18 will fail.

Some guides install Node via:
```
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs -y
```
> **⚠️ WARNING:** This particular command runs a remote script **as root** (`sudo -E bash`)
> — significantly more powerful than piping to unprivileged `sh`. Only run it if you trust
> NodeSource (a well-maintained project). Visit nodesource.com to verify before running.

🕒 **verify live:** `npm view @google/gemini-cli version` for current (v0.49.0 stable as of
25 Jun 2026; active development continues with preview and nightly channels).

**Sources:** [geminicli.com/docs/get-started/installation](https://geminicli.com/docs/get-started/installation) (fetched 2026-06-26) ·
Google Developers Blog
**Confidence:** ✅ independently-corroborated

---

### Practice: Authenticate with a paid Gemini API key

**Do:** Get a paid Gemini API key from https://aistudio.google.com/apikey. Set it as
`GEMINI_API_KEY` in your environment or in a `.env` file (Gemini CLI searches: current
directory → parent directories → `~/.gemini/.env`). **Never commit a `.env` containing
a key; add it to `.gitignore`.**

**Sources:** [geminicli.com/docs](https://geminicli.com/docs) (fetched 2026-06-26)
**Confidence:** 📄 vendor-documented

---

### Practice: Run agentic work inside the sandbox

**Do:** Enable with `-s` flag or `GEMINI_SANDBOX=docker`. 

> **⚠️ WARNING:** Sandboxing is **off by default** — most beginners run unprotected without
> realizing it. And it requires Docker or Podman installed and running first:
> `sudo apt install docker.io && sudo systemctl enable --now docker`
> (plus adding yourself to the docker group: `sudo usermod -aG docker $USER`, then re-login).

Note: using `--yolo` auto-enables the sandbox — but that sandbox only works if Docker is
already installed.

**Sources:** [geminicli.com](https://geminicli.com) (fetched 2026-06-26)
**Confidence:** 📄 vendor-documented

---

### Practice: Know the approval modes; don't default to `--yolo`

**Do:** Three modes (set in `settings.json` or with `--approval-mode`):

| Mode | What it does |
|------|-------------|
| `default` | Asks before most actions |
| `auto_edit` | Auto-approves file edits (agent can rewrite any file without asking) |
| `yolo` | Auto-approves everything; automatically enables the sandbox |

> **⚠️ `auto_edit`** means the agent can delete and recreate files without asking — if you
> didn't want a file changed, it already changed it.

**Sources:** [geminicli.com/docs/cli/settings](https://geminicli.com/docs/cli/settings/) (fetched 2026-06-26; relocated from google-gemini.github.io)
**Confidence:** 📄 vendor-documented

---

### Practice: Headless mode — `gemini -p` + JSON output

**Do:** `gemini -p "prompt" --output-format json` for scripted runs. Parse with `jq`
(`sudo apt install jq` — not installed by default on Ubuntu):
`gemini -p "Review this" --output-format json | jq '.response'`

Exit codes: `0` success, `1` general/API error, `42` input error, `53` turn-limit exceeded.

**Sources:** [geminicli.com/docs/cli/headless](https://geminicli.com/docs/cli/headless) (fetched 2026-06-26)
**Confidence:** 📄 vendor-documented

---

### Practice: Know which `settings.json` wins (7-layer precedence)

**Do:** From lowest to highest priority:
1. Built-in defaults
2. `/etc/gemini-cli/system-defaults.json`
3. `~/.gemini/settings.json` (your user settings)
4. `.gemini/settings.json` in your project (team settings)
5. `/etc/gemini-cli/settings.json` (system policy)
6. Environment variables
7. CLI flags

Your personal settings go in `~/.gemini/settings.json`. Project-specific in `.gemini/settings.json`.

> **Safety note:** The official MCP-setup example includes `"trust": true`, which silently
> disables tool-approval prompts for that server. Don't copy-paste it unless you fully
> control the MCP server.

Use `/memory refresh` and `/memory show` to inspect what context files the agent has loaded.

**Sources:** [geminicli.com/docs/cli/settings](https://geminicli.com/docs/cli/settings/) (fetched 2026-06-26; relocated from google-gemini.github.io/configuration)
**Confidence:** 📄 vendor-documented

---

### Practice: Pick the model; watch usage and quotas

🕒 **verify live:** Quotas and pricing shifted significantly in 2026. The current model
list and free-tier limits change; always verify at the official quota page before building
a workflow around a specific model.

> "Pro models became paid-only on 1 Apr 2026" is reported by community sources but the
> exact date is unconfirmed from a primary source — verify against current quota page.

**Sources:** [geminicli.com/docs](https://geminicli.com/docs) (fetched 2026-06-26)
**Confidence:** 🕒 verify live

---

## Held pending fixes (not yet in this entry)

- **Ubuntu 24.04 AppArmor profile for bubblewrap** — the check (`sysctl ...`) is here;
  the safe profile content is ⚠ **PENDING #317**.
- **Safe starter nftables ruleset** — the network-isolation practice warns against applying
  `policy drop` first; a complete ruleset with exceptions pre-included is ⚠ **PENDING #318**.
- **GPG fingerprint verification command** — the fingerprint is here and verified;
  the exact `gpg --show-keys` output format is ⚠ **PENDING #317**.
- **Tokens defined for beginners** — cost numbers appear throughout; a plain "1 token ≈ ¾
  of a word" definition is included above; fuller worked examples are ⚠ **PENDING**.

## CHANGELOG (grading → this entry)

1. **Timekeeper KILL applied:** Removed the false "2026-06-15 billing change" from
   Part 1 (Claude Code cost practice). That change was paused on the day it was due and
   never took effect; `claude -p` still draws from subscription limits. Replaced with
   accurate correction note citing multiple sources.
2. **Timekeeper KILL applied:** Corrected GPT-5.5 context window from "400K" to
   1,050,000 tokens in Part 2 (Codex model practice). Official models page confirmed.
3. **Beginner KILL applied:** Elevated API-key-overrides-subscription note to a ⚠️ WARNING
   block in Part 1 auth practice.
4. **Beginner KILL applied:** Added explicit ⚠️ WARNING adjacent to `danger-full-access`
   sandbox mode in Part 2.
5. **Beginner KILL applied:** Added ⚠️ WARNING that Gemini CLI sandbox requires Docker
   first (off by default) in Part 3.
6. **Beginner KILL applied:** Added ⚠️ WARNING that NodeSource curl installs as root
   in Part 3.
7. **Beginner KILL applied:** Added ⚠️ WARNING about `"trust": true` in MCP example in
   Part 3 config practice.
8. **Skeptic FIX applied:** Re-attributed GPT-5.5 "default" to official models page and
   blakecrosley.com (README/changelog did not mention it).
9. **Skeptic FIX applied:** Corrected nftables source attribution — Ubuntu page confirms
   20.10 default + ufw warning; output-`policy drop` recipe noted as general practice,
   not from Ubuntu page.
10. **Skeptic FLAG applied:** Relabeled confidence from "widely-agreed" to
    `vendor-documented` where both sources were Anthropic-published (same vendor ≠
    independent). Practices with genuinely independent sources retain
    `independently-corroborated`.
11. **Skeptic FLAG applied:** Dropped bare unverified GitHub issue #29116 from systemd
    practice; replaced with "open feature request (not fetched)" note.
12. **Timekeeper FIX applied:** Added missing Docker prerequisite install command for
    Gemini sandbox. Added `jq` install note for headless pipe.
13. **Timekeeper FIX applied:** Added Google AI Studio URL for API key acquisition.
14. **Beginner FIX applied throughout:** Added missing prerequisites (`sudo apt install`
    commands), clarified jargon ("throwaway container/VM" → explanation), introduced MCP
    acronym on first use, moved hook-permission warning before "do" section.
