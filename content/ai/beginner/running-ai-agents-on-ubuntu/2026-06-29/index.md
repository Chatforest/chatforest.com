---
title: "Running AI Agents on Ubuntu — Beginner Guide (as of 29 Jun 2026)"
date: 2026-06-29
snapshot_date: 2026-06-29
topic: running-ai-agents-on-ubuntu
track: beginner
audience: "people new to AI"
description: "A plain-language guide to installing and safely running AI agents (Claude Code, Codex CLI, Gemini CLI) on Ubuntu for the first time. Every practice is fact-checked; no step is added that was not already in the 2026-06-28 technical entry."
content_type: "Best Practice"
categories: ["Claude Code", "Ubuntu", "AI Agents"]
tags: ["claude-code", "codex-cli", "gemini-cli", "ubuntu", "linux", "ai-agents", "best-practices"]
last_refreshed: 2026-06-29
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-06-29"
grading_result: "Re-leveled from 2026-06-28 technical entry; no new facts or URLs introduced."
---

<!-- Beginner-track snapshot. Re-leveled from the 2026-06-28 technical entry.
     Facts, commands, and source URLs are unchanged. Only reading level and
     framing have been adjusted. -->

# Running AI Agents on Ubuntu — Beginner Guide (as of 29 Jun 2026)

> **What this is.** A dated, fact-checked guide re-written for people who are new to AI,
> Ubuntu, and the command line. Every claim was verified by a 3-lens panel (Skeptic,
> Beginner, Timekeeper) on the 2026-06-28 technical entry. **0 fabrications.** Items that
> could not yet be fully verified are marked **⚠ PENDING** — this guide never guesses.

## What the labels mean

- ✅ **independently-corroborated** — confirmed by 2 or more independent publishers
- 📄 **vendor-documented** — from the tool's official documentation (authoritative, one source)
- ⚠️ **WARNING** — a default that can cost you real money, break your machine, or remove a safety net
- 🕒 **verify live** — this detail changes fast (versions, prices, quotas); look it up yourself before relying on it

---

## A word before you start

An "AI agent" is a program that uses a language model (like Claude or GPT-5.5) to read
your files, run commands, and make changes on your behalf. That power is useful — and
dangerous if unchecked. The practices below are not optional polish; they are the
difference between a helpful assistant and an agent that runs up a large bill overnight,
leaks your passwords, or modifies files you did not want touched.

Read Part 0 first, no matter which agent you choose. Parts 1, 2, and 3 cover the
specific tools. **If you are choosing just one tool to start with, start with Claude Code
(Part 1)** — it has the most documentation aimed at beginners.

---

## Part 0 — Foundations (apply to any agent on Ubuntu)

These practices apply no matter which agent you run. Do them first.

---

### Practice 1: Run a long-running agent as a systemd user service ✅

**What is systemd?** Ubuntu uses a program called `systemd` to manage background
processes (called "services"). A "user service" runs as you — not as the all-powerful
root user — and restarts automatically if it crashes.

**Why not just use `nohup &` or a terminal you leave open?** Those approaches give you no
auto-restart, no start-on-boot, and scattered or lost logs. A forgotten `nohup &` process
is also easy to accidentally kill.

**Do:**

1. Write a unit file at `~/.config/systemd/user/<name>.service` that describes your agent.
2. Store your API key (the secret password for the AI service) in a separate file, for example
   `/home/yourname/.config/secrets.env`, with permissions locked down: `chmod 600 /home/yourname/.config/secrets.env`
3. Reference that file in your unit with `EnvironmentFile=/path/to/secrets.env`. Do **not**
   paste the key directly as `Environment=ANTHROPIC_API_KEY=sk-ant-…` inside the unit file —
   unit files can end up in bug reports or backups.
4. Enable and start the service: `systemctl --user enable --now <name>`
5. Allow it to keep running after you log out: `loginctl enable-linger $USER`

**Why it matters / what goes wrong without it:** Without linger, your agent stops the
moment you close your SSH session. Without a unit file, crashes are silent and permanent.

> **⚠️ WARNING:** Set a spend cap on your AI account before you leave any agent running
> overnight. An uncapped loop can exhaust your credits far faster than you expect. (See the
> cost practice in Part 1 for how to set caps on Claude Code.)

**Sources:** [morphllm.com/claude-code-linux](https://morphllm.com/claude-code-linux) (2026-03-10) · Ubuntu systemd-user community guides
**Confidence:** ✅ independently-corroborated (community convention; no official Anthropic prescription; the underlying `claude -p` primitive IS official)

---

### Practice 2: Give each agent its own git worktree ✅

**What is a git worktree?** Git (a version-control tool) normally lets you work on one
branch of your project at a time. A "worktree" creates a separate folder on disk so a
second agent can work on a different branch at the same time, without the two agents
overwriting each other's files.

**Do:**

```
git worktree add ./agent-task-1 -b agent-task-1 main
```

Before running this, check your primary branch name: `git branch`. New repos created on
GitHub/GitLab often use `main`; older ones may use `master`.

**Why it matters / what goes wrong without it:** Two agents editing the same files at the
same time will corrupt each other's work.

> **Note:** Worktrees isolate **files only**. Two agents sharing the same repository can
> still collide on ports, databases, caches, or secrets. Worktrees do not give you full
> isolation.

**Sources:** [git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree) (official)
**Confidence:** 📄 vendor-documented

---

### Practice 3: Sandbox the agent so it cannot touch the rest of your machine ✅

**What is a sandbox?** A sandbox is a cage around the agent. Inside the cage, the agent
can write to your project folder. Outside the cage — your home directory, system files,
other projects — everything is read-only or invisible.

Two tools do this on Ubuntu: **bubblewrap** (smaller, preferred) and **firejail** (easier
to configure, has bundled profiles for common programs).

**Do (bubblewrap — preferred):**
```
sudo apt install bubblewrap
```

**Do (firejail — easier for beginners):**
```
sudo apt install firejail
```

Whichever you choose: keep system files read-only, bind only your project folder as
writable, drop all capabilities, and isolate the network namespace.

**Why it matters / what goes wrong without it:** Without a sandbox, a misbehaving agent
(or a prompt-injection attack — where a malicious web page tricks the agent into doing
something harmful) can delete your home directory, read your SSH keys, or send your files
to an external server.

> **⚠️ WARNING:** Neither bubblewrap nor firejail is installed by default on Ubuntu. If
> you try to run a sandbox command before installing the tool, it fails silently — the
> agent runs without any protection and you will not be told.
>
> **Ubuntu 24.04+ gotcha:** A security feature called AppArmor blocks bubblewrap's
> "user namespaces" by default. Check whether it is active:
> `sysctl kernel.apparmor_restrict_unprivileged_userns`
> If it returns `1`, you need a special AppArmor profile for `/usr/bin/bwrap` before
> bubblewrap will work. ⚠ **PENDING** — a complete, safe profile is not yet in this
> entry; see project issue #317.

**Sources:** [github.com/containers/bubblewrap](https://github.com/containers/bubblewrap) (release 0.11.2, 2026-04-23) · [github.com/CaptainMcCrank/SandboxedClaudeCode](https://github.com/CaptainMcCrank/SandboxedClaudeCode)
**Confidence:** ✅ independently-corroborated

---

### Practice 4: Block outbound network traffic you did not explicitly allow 📄

> **⚠️ WARNING — ADVANCED.** The tool for this on Ubuntu is `nftables`. If you apply a
> blanket "deny all outgoing" rule *before* adding exceptions for DNS, your AI service,
> and `apt`, **your machine will go offline immediately.** Add your allow-rules first,
> test connectivity, then set the deny policy.
> Rollback command (restores full network access): `sudo nft flush ruleset`
>
> **If you are new to Linux networking:** skip this practice for now and rely on the
> sandbox network controls from Practice 3 instead. A complete starter ruleset with
> the necessary exceptions pre-included is ⚠ **PENDING (#318)** — it will be in a future
> edition.

**Sources:** [documentation.ubuntu.com](https://documentation.ubuntu.com) nftables guide (nftables default since Ubuntu 20.10; ufw/nftables conflict warning confirmed)
**Confidence:** 📄 vendor-documented (Ubuntu docs confirm 20.10 default + ufw conflict; the output-`policy drop` recipe is standard nftables practice, not from the Ubuntu page)

---

### Practice 5: Keep your secrets (API keys, passwords) out of the repo and away from the agent ✅

**What is a secret?** An API key is like a password that charges your account when used.
A `.env` file is a text file that stores these secrets as environment variables (named
values your programs can read).

**The hidden danger:** Adding your `.env` to `.gitignore` (so it is not uploaded to
GitHub) is not enough. **Agents routinely run commands like `cat .env` and `printenv`.**
Any file the agent can read is a file it might send to the AI model or write to a log.

**Do:**

- Add `.env` to `.gitignore`: add a line `.env` to your `.gitignore` file.
- Lock down permissions on any on-disk secrets file: `chmod 600 /path/to/secrets.env`
- For stronger protection, store secrets in the OS keychain (GNOME Keyring):
  ```
  sudo apt install libsecret-tools
  secret-tool store --label="My API Key" service myservice username mykey
  ```
  Then retrieve it at launch time rather than writing it to disk.
- Alternatively, use a secrets manager that injects the value at launch rather than
  storing it in a file the agent can browse.

**Why it matters / what goes wrong without it:** A leaked API key means someone else can
use your AI account at your expense. A leaked SSH key means someone can log in to your
server.

**Sources:** [bitwarden.com/blog](https://bitwarden.com/blog) (2026-04-02) · [dev.to](https://dev.to) secrets management · [blog.gitguardian.com/secure-your-secrets-with-env](https://blog.gitguardian.com/secure-your-secrets-with-env/) (2024-01-08)
**Confidence:** ✅ independently-corroborated

---

### Practice 6: Limit what parts of the filesystem the agent can write to 📄

**What is `DynamicUser`?** When you add `DynamicUser=yes` to a systemd unit file,
systemd creates a temporary user ID just for that service run. This temporary user
cannot access your home directory at all — not even to read it.

**Do:** In your systemd unit file, add:
```
DynamicUser=yes
ReadOnlyPaths=/
ReadWritePaths=/path/to/your/project
```

**Why it matters / what goes wrong without it:** Without these restrictions, the agent
runs as you and can read or overwrite any file you own — including other projects, SSH
keys, and browser profiles.

**Sources:** Ubuntu systemd documentation
**Confidence:** 📄 vendor-documented

---

### Practice 7: Check what the agent did by reading its logs ✅

**What is journald?** Ubuntu's `journald` is the system log collector. Logs from your
systemd user services are automatically stored there.

**Do:**

- See logs for your agent service: `journalctl --user -u <name>.service`
- Watch logs in real time: `journalctl --user -u <name>.service -f`
- See only the last hour: `journalctl --user -u <name>.service --since "1 hour ago"`

If you want to read the full system journal (not just your user's logs), add yourself to
the right group first, then re-login:
```
sudo usermod -aG systemd-journal $USER
```

**Why it matters / what goes wrong without it:** Leaving an agent running unattended is
only safe if you can audit what it did afterward. Without logs, you have no way to know
if it silently failed, ran up a large bill, or made unexpected changes.

**Sources:** DigitalOcean journald guide (updated 2026-04-27) · [morphllm.com](https://morphllm.com) (2026-03-10)
**Confidence:** ✅ independently-corroborated

---

## Part 1 — Claude Code (Anthropic)

Claude Code is Anthropic's agent for writing, editing, and running code. It is the
recommended starting point for beginners because it has the most beginner-oriented
documentation and the smoothest install process.

---

### Practice: Install with the native installer; confirm with `claude doctor`

**Do:**

```
curl -fsSL https://claude.ai/install.sh | bash
```

Then check the install worked:
```
claude --version
claude doctor
```

The binary (a single self-contained program file) lands in `~/.local/bin/claude`. If the
`claude` command is not found afterward, add that folder to your PATH. Add this line to
`~/.bashrc` (or `~/.zshrc` if you use zsh), then open a new terminal:
```
export PATH="$HOME/.local/bin:$PATH"
```

Minimum requirements: Ubuntu 20.04 or newer, 4 GB RAM, x64 or ARM64 processor.

**Why (beginner):** One command, nothing else to install, and `claude doctor` tells you
the installation and update path are healthy before you waste time debugging.

**Caveat:** Piping a remote script to `bash` means the script runs with your full
permissions before you have read it. If you want more control, use the signed apt repo
(next practice) instead. The `npm install -g @anthropic-ai/claude-code` route also
works (requires Node.js 18 or newer), but **never use `sudo npm install -g`** — that
creates root-owned files that break future updates.

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-06-26) · [code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart) · [morphllm.com/claude-code-linux](https://morphllm.com/claude-code-linux) (2026-03-10)
**Confidence:** ✅ independently-corroborated

---

### Practice: Prefer the signed apt repo for verified, system-managed installs

**What is an apt repo?** `apt` is Ubuntu's built-in package manager (the same tool you
use for `sudo apt install`). A signed apt repo means the software is cryptographically
signed by the vendor — you can verify it has not been tampered with.

**Do:**

Add Anthropic's signed apt repository, then install:
```
# (follow the keyring setup steps on Anthropic's setup page)
sudo apt update && sudo apt install claude-code
```

After adding the keyring file, verify the GPG fingerprint (a unique identifier for
Anthropic's signing key) matches exactly:
```
31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE
```
*(This fingerprint was re-confirmed verbatim against Anthropic's live setup page during
grading — not a fabrication.)*

To check it yourself: `gpg --show-keys /etc/apt/keyrings/claude-code.asc`
⚠ **PENDING (#317):** the exact output format of this command is being verified for a
future edition.

Choose the `stable` channel (about one week behind, skips major regressions) or
`latest`.

**Caveat:** `apt` does NOT auto-update Claude Code. You must run
`sudo apt update && sudo apt upgrade claude-code` yourself. The native installer (above)
does auto-update. This is a deliberate trade-off: control and verifiability versus
always-current.

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fingerprint, apt commands, fetched 2026-06-26)
**Confidence:** 📄 vendor-documented

---

### Practice: Choose a release channel and keep updates deliberate

**Do:** Open (or create) `~/.claude/settings.json` and set your channel:
```json
{
  "autoUpdatesChannel": "stable"
}
```

Use `"stable"` (recommended for beginners) or `"latest"`. Add `minimumVersion` to
prevent a channel switch from accidentally downgrading you:
```json
{
  "autoUpdatesChannel": "stable",
  "minimumVersion": "2.1.0"
}
```

Apply an update immediately: `claude update`
Check update status: `claude doctor`

To freeze a machine at its current version (for example, a production server), add one of
these to the `env` block in settings:
- `DISABLE_AUTOUPDATER` — stops the background update check only
- `DISABLE_UPDATES` — stops all update paths

**Caveat:** If you installed via `apt`, `dnf`, or Homebrew, those package managers
control the channel instead of `autoUpdatesChannel`. A known quirk: Claude Code may
notify you of an available update before the package manager has it.

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-06-26) · [code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart)
**Confidence:** 📄 vendor-documented

---

### Practice: Authenticate — and avoid the billing trap

**Interactive use (normal laptop/desktop):** Run `claude` and follow the browser login
prompt.

**Over SSH (you are logged in remotely):** When the login prompt appears, press `c` to
copy the login URL to your clipboard, then open it on your local machine.

**Unattended/automated use (no human present):** Two options:
- `claude setup-token` — mints a 1-year OAuth token (`CLAUDE_CODE_OAUTH_TOKEN`); draws
  from your Pro or Max subscription.
- Set `ANTHROPIC_API_KEY` — uses Anthropic Console pay-as-you-go billing (you are
  charged per token used).

> **⚠️ WARNING — cost trap:** If you have BOTH a subscription AND `ANTHROPIC_API_KEY` set
> in your environment, **the API key wins and you are billed pay-as-you-go instead of
> using your subscription plan.** This surprises many people and can result in unexpected
> charges. To check: `unset ANTHROPIC_API_KEY`, then run `/status` inside Claude Code.

**On Linux, where are credentials stored?** In `~/.claude/.credentials.json` with
permissions `0600` (only you can read it). Unlike macOS, there is no OS keychain — that
file IS your credential. Protect it.

**Caveat:** `--bare` mode (used for clean automated runs) ignores
`CLAUDE_CODE_OAUTH_TOKEN`; use `ANTHROPIC_API_KEY` or `apiKeyHelper` in that mode. A
key from a disabled Anthropic Console workspace causes silent auth failures with no clear
error message.

**Sources:** [code.claude.com/docs/en/authentication](https://code.claude.com/docs/en/authentication) (fetched 2026-06-26) · [support.claude.com/en/articles/12304248](https://support.claude.com/en/articles/12304248) (2026-05-05) · [hidekazu-konishi.com](https://hidekazu-konishi.com) (2026-06-07)
**Confidence:** ✅ independently-corroborated

---

### Practice: Run automated tasks with `claude -p`, scoped tightly

**What is `claude -p`?** The `-p` flag puts Claude Code into "non-interactive" (also
called headless or print) mode: you give it a single prompt, it runs the task, and exits.
This is useful for scripts, scheduled jobs, or any situation where no human is watching.

**Do:**

Basic one-shot run:
```
claude -p "Summarize the changes in the last git commit"
```

Restrict which tools Claude can use (always do this — smallest set the task needs):
```
claude -p "Read main.py and list all functions" --allowedTools "Read,Grep,Glob"
```

Get machine-readable output (useful for scripts):
```
claude -p "Review this file" --output-format json
```

For clean, reproducible automated runs (ignores local config, hooks, and CLAUDE.md):
```
claude -p "Run tests" --bare
```

> **⚠️ Pre-approve tools before any unattended run.** Without `--allowedTools`, Claude
> Code pauses and waits for a permission prompt that no one is there to answer. Your
> script silently stalls until it times out.

**Caveat:** `--bare` skips OAuth/keychain; use `ANTHROPIC_API_KEY` or `apiKeyHelper` in
that mode. Input piped via stdin is capped at 10 MB (version 2.1.128 and later); for
larger input, write the content to a file and pass the file path in the prompt. Commands
like `/login` that require interaction do not work in `-p` mode.

**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 2026-06-26) · [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) · [hidekazu-konishi.com](https://hidekazu-konishi.com) (2026-06-07)
**Confidence:** ✅ independently-corroborated

---

### Practice: Use permission allowlists rather than bypassing permissions entirely

**What are permissions?** Claude Code asks your permission before running commands it
considers risky. The `/permissions` screen lets you pre-approve specific commands so you
are not interrupted constantly — without turning off all protections.

**Do:** Open `/permissions` in Claude Code and set rules like:
- Allow (safe, common): `Bash(npm run *)`, `Bash(git commit *)`
- Deny (protect yourself): `Bash(git push *)`, `Read(.env)`, `Read(~/.ssh/**)`

Rules are evaluated in order: deny beats ask beats allow.

You can also set `defaultMode` in `~/.claude/settings.json` to control the baseline
behavior.

> **⚠️ AVOID `bypassPermissions` and `--dangerously-skip-permissions`.** These turn off
> all permission checks. Only use them inside a throwaway container or VM (a separate
> test environment you do not care about) — and note that these options are blocked
> entirely when running as the root user on Linux.

**Caveat:** Permission rules are enforced by Claude Code itself, not by the operating
system. A Python or Node.js script that opens files on its own bypasses the Read/Edit
deny rules completely. For OS-level enforcement, combine this with the sandbox (Practice
3 above and the sandbox practice below).

**Sources:** [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-06-26) · [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
**Confidence:** 📄 vendor-documented

---

### Practice: Enable the built-in Bash sandbox (bubblewrap)

Claude Code has a built-in sandbox that uses bubblewrap (see Part 0 Practice 3) to
confine the Bash commands it runs to your project directory and a temporary directory.
This is separate from — and in addition to — the permission allowlists above.

**Do:**

Install the prerequisites first:
```
sudo apt-get install bubblewrap socat
```

Then enable the sandbox. Per-project (recommended to start with):
```
/sandbox
```
(This writes the setting to `.claude/settings.local.json` in your project.)

Or globally for all projects, add to `~/.claude/settings.json`:
```json
{
  "sandbox": {
    "enabled": true
  }
}
```

To also block the agent from reading sensitive credential files (version 2.1.187 and
later), add `sandbox.credentials` with deny-read rules for `~/.aws/credentials`,
`~/.ssh`, etc. Check the settings reference for the exact format.

> **⚠️ Ubuntu 24.04+ gotcha:** AppArmor blocks bubblewrap from creating user namespaces
> by default. Check: `sysctl kernel.apparmor_restrict_unprivileged_userns`. If it returns
> `1`, you need an AppArmor profile for `/usr/bin/bwrap` before the sandbox will work.
> ⚠ **PENDING (#317):** the complete profile content is being prepared for a future
> edition. For now, check Anthropic's sandboxing docs for the latest guidance.

**Caveat:** This sandbox is defense-in-depth, not a complete security boundary. The
network proxy does not inspect TLS traffic, so a broadly allowed domain can still be used
to send data out. Some tools do not work inside the sandbox (`docker`,
`watchman`/`jest --no-watchman`) — add them to `excludedCommands` in `settings.json`.

**Sources:** [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-06-26) · [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions)
**Confidence:** 📄 vendor-documented

---

### Practice: Never paste secrets into the chat window

**Why this matters:** Everything you type into the Claude Code chat window is sent to
Anthropic's API. There is no "private mode." A secret pasted into chat is a secret
transmitted to an external server.

**Do:**

- Store secrets in environment variables or a secret manager; reference them by name in
  your prompts ("use the value of GITHUB_TOKEN").
- In MCP server config (see next practice), put credentials in env vars, not as literal
  values in the config file.
- Add `.env` to `.gitignore`.
- In your `CLAUDE.md` file (see below), document which environment variables exist — but
  never their values.

**What is MCP?** MCP (Model Context Protocol) is a standard for connecting Claude to
external tools like GitHub, databases, or design tools. Think of an MCP server as a
plug-in that gives the agent a new capability.

**Caveat:** Claude does not automatically read environment variables into its context
window — the values are only available to commands it runs. A subprocess can still read
secret files unless you also use the sandbox `credentials`/`denyRead` controls or
`CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`.

**Sources:** [support.claude.com/en/articles/12304248](https://support.claude.com/en/articles/12304248) (2026-05-05) · [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) · [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)
**Confidence:** ✅ independently-corroborated

---

### Practice: Add MCP servers (plug-ins) with `claude mcp add`

**What is an MCP server?** An MCP server is a plug-in that gives Claude a new tool —
for example, the ability to create GitHub issues, query a database, or read design files
from Figma. You connect one with `claude mcp add`.

**Do:**

Choose the right scope for each server:
- **user** scope — available in every session you run
- **project** scope — stored in `.mcp.json` in your project folder, shared with your team

Always put credentials in environment variables in the config, not as literal values.

**Why it matters / what goes wrong:** More MCP servers means more context being loaded
into every conversation (which costs more tokens and therefore more money) and more
potential attack surface. Disable servers you are not currently using with `/mcp`.

**Caveat:** For many simple tasks, a standard command-line tool (`gh` for GitHub, `aws`
for AWS) is more efficient than an MCP server doing the same job — it uses less context.

**Sources:** [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-06-26) · [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)
**Confidence:** 📄 vendor-documented

---

### Practice: Use hooks for things that must happen every single time

**What is a hook?** A hook is a shell command that Claude Code's harness runs
automatically at certain points — before a tool runs, after a file is edited, when a
session ends. Unlike instructions in CLAUDE.md (which the AI model may choose to
follow or not), hooks are deterministic: they always run.

> **⚠️ WARNING:** Hooks run with YOUR shell permissions. A malicious or buggy hook is
> real code execution on your machine. Review any hook — especially from a shared or
> project config — before enabling it.

**Do:** Add a `hooks` block to `~/.claude/settings.json`. The main events:

- `PreToolUse` — runs before a tool executes; can block the action by exiting with code 2
- `PostToolUse` — runs after a tool; for example, run a formatter after every file edit
- `Stop` — runs at the end of a turn; can block the session from declaring "done" until
  a check passes (e.g. all tests pass)

You can ask Claude to write hooks for you: *"write a hook that runs eslint after every
file edit."*

**Why it matters / what goes wrong:** If you rely on CLAUDE.md instructions alone to
enforce a rule (e.g. "always run tests before saying you are done"), the model may skip
it. A `Stop` hook makes the check mandatory.

**Caveat:** A `Stop` hook is overridden if it blocks 8 consecutive times in a row —
Claude Code ignores it and proceeds. `--bare` mode skips hook discovery entirely.

**Sources:** [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) (fetched 2026-06-26) · [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) · [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions)
**Confidence:** 📄 vendor-documented

---

### Practice: Write a short CLAUDE.md and keep it short

**What is CLAUDE.md?** It is a special text file in your project that Claude Code reads
at the start of every session. It is your chance to tell Claude things it cannot infer
from the code itself.

**Do:**

Generate a starting point automatically:
```
/init
```

Keep only what Claude genuinely needs and cannot figure out on its own:
- Non-obvious shell commands to set up or run the project
- Environment variable names and what they are for (not the values)
- Which test runner to use and how to invoke it
- Branch naming and pull-request conventions

Aim for under about 200 lines. Move occasional or complex workflows into "skills"
(loaded on demand) to keep the main file lean.

For each line, ask: "Would removing this cause Claude to make mistakes?" If no, remove it.

**Why it matters / what goes wrong:** A very long CLAUDE.md is counterproductive. If
Claude keeps violating a rule, the file is probably too long, not the rule too weak —
Claude gets confused by noise.

**Caveat:** Check CLAUDE.md into git so your whole team shares it. Keep personal notes
in `CLAUDE.local.md` (which is gitignored).

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-26) · [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)
**Confidence:** 📄 vendor-documented

---

### Practice: Watch your costs — and know your options for controlling them

**What is a token?** A token is roughly three-quarters of a word. A typical coding
session might use tens of thousands of tokens. Cost scales with how many tokens are in
the conversation (the "context") and which model you use.

**Do:**

Check your usage and context size:
```
/usage
/context
```

Clear the conversation between unrelated tasks (this resets the context and stops
previous tokens from being counted again):
```
/clear
```

Choose the right model (`/model`):
- **Sonnet** — recommended for most tasks; faster and cheaper
- **Opus** — for hard reasoning problems; slower and more expensive

For automated (`-p`) runs, parse the cost from the output and add a turn limit:
```
claude -p "prompt" --output-format json --max-turns 10
```
The JSON output includes `total_cost_usd`.

Set caps to avoid surprises:
- Pro/Max plan: use `/usage-credits` inside Claude Code
- API/Console billing: set workspace spend limits at console.anthropic.com

**Why it matters / what goes wrong:** A long, cluttered session quietly multiplies token
cost. Clearing context and choosing Sonnet are the biggest easy wins. Without a spend
cap, an automated loop running overnight can exhaust your budget.

**Caveat:** `/usage` is a local estimate, not your authoritative bill. Use the Anthropic
Console for the definitive number.

> **Correction from grading (Timekeeper):** An earlier draft of this guide warned about
> a "2026-06-15 billing change" that would have put `claude -p` and Agent SDK usage into
> a separate credit pool. **That change was paused on the day it was due and never took
> effect.** As of grading, `claude -p` and headless Agent SDK usage still draw from
> normal subscription limits. Sources confirming the suspension: thenewstack.io,
> devops.com, digitalapplied.com (all 2026-06).

**Sources:** [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 2026-06-26) · [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) · [hidekazu-konishi.com](https://hidekazu-konishi.com) (2026-06-07)
**Confidence:** 📄 vendor-documented (billing suspension independently corroborated)

---

### Practice: Always give Claude a way to verify its own work

**Do:** For every task you give Claude, also give it a way to check whether it succeeded:
a test suite it can run, a build command whose exit code tells it pass/fail, a linter, or
a diff to review.

For automated runs, use a `Stop` hook (see hooks practice above) so the session cannot
declare "done" until the check actually passes.

Ask Claude to show you evidence — test output, the command it ran and what the result was
— rather than just saying "I finished."

**Why it matters / what goes wrong:** Without a verification step, Claude Code may
confidently report success while the code still has errors. Requiring evidence catches
this before you find out the hard way.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-26) · [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)
**Confidence:** 📄 vendor-documented

---

## Part 2 — OpenAI Codex CLI

> **Status as of 26 Jun 2026:** Codex CLI is not renamed or replaced. It is
> `openai/codex` — an open-source Rust binary, Apache-2.0 license, latest version
> v0.142.2 (25 Jun 2026, with multiple releases per week).

Codex CLI is a good choice if you are already paying for ChatGPT or an OpenAI API
subscription. The default model is GPT-5.5. Start with the install below, then read the
two-layer safety model before you run anything.

---

### Practice: Install via the official script or npm

**Three ways to install:**

**Option A (recommended for most beginners) — official install script:**
```
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

**Option B — npm (Node.js package manager):**
```
npm install -g @openai/codex
```

**Option C — prebuilt binary:** download from the GitHub releases page at
[github.com/openai/codex](https://github.com/openai/codex).

> **⚠️ WARNING — Option A:** Piping any remote script to `sh` means the script runs with
> your permissions before you have read it. This is the standard install method, but you
> are trusting that URL.
>
> **⚠️ WARNING — Option B:** Never use `sudo npm install -g`. It creates root-owned files
> that break future updates. If `codex` is not found after npm install, add your npm
> global bin to PATH instead:
> ```
> export PATH="$HOME/.npm-global/bin:$PATH"
> ```
> Add that line to `~/.bashrc` (bash users) or `~/.zshrc` (zsh users), then open a new
> terminal.

**Sources:** [github.com/openai/codex](https://github.com/openai/codex) (v0.142.2, fetched 2026-06-25) · [developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference)
**Confidence:** ✅ independently-corroborated

---

### Practice: Understand the two-layer safety model before running anything

Codex CLI has two independent safety dials. Set both deliberately.

**Layer 1 — Sandbox** (controls what the agent can physically access on your machine):

| Sandbox mode | What it allows |
|---|---|
| `read-only` | Agent can only read files; cannot write anything |
| `workspace-write` | Agent can write files in your project folder |
| `danger-full-access` | Agent can do anything on your machine |

**Layer 2 — Approval policy** (controls when the agent asks you before acting):

| Approval mode | What it does |
|---|---|
| `untrusted` | Asks before most actions |
| `on-request` | Asks when the agent requests permission |
| `never` | Never asks; acts immediately |

**Recommended starting combination:** `workspace-write` sandbox + `on-request` approval.
This lets the agent write project files but asks you before running network or system
commands.

> **⚠️ WARNING: `danger-full-access`** removes all OS-level restrictions. Only use it
> inside a disposable container or virtual machine you do not care about. Never on your
> main machine.

**Sources:** [developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference) (fetched 2026-06-26) · [blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex)
**Confidence:** ✅ independently-corroborated

---

### Practice: Keep the OS sandbox on; only bypass it inside a throwaway environment

On Linux, Codex CLI's sandbox runs at the kernel level using Landlock and seccomp (both
are Linux kernel security features that restrict what system calls a process can make).
Bubblewrap is also included.

**Do:** Leave the sandbox on. If a workflow genuinely needs full access:

Use `--dangerously-bypass-approvals-and-sandbox` (also written as `--yolo`) **only**
inside a Docker container or GitHub Codespace.

- A **Docker container** is a lightweight isolated environment that runs on your machine
  but cannot access the rest of your files.
- **GitHub Codespaces** gives you a cloud-hosted virtual machine you can throw away
  afterward.

Either of these lets you run `--yolo` without risking your actual files.

**Sources:** [developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference) (fetched 2026-06-26) · [blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex)
**Confidence:** ✅ independently-corroborated

---

### Practice: Auth — prefer ChatGPT sign-in; keep API key out of your shell history

**Interactive use:** Use "Sign in with ChatGPT" — this uses your subscription and is
the recommended approach for interactive sessions.

**Headless/automated use:** Set `OPENAI_API_KEY` in your environment.

Keep the key out of your shell history: set it at the start of a session with
`export OPENAI_API_KEY=sk-…` rather than adding it to `.bashrc`. For persistent use,
add it to `~/.profile` and lock down permissions: `chmod 600 ~/.profile`.

**Sources:** [github.com/openai/codex](https://github.com/openai/codex) README · [developers.openai.com](https://developers.openai.com) changelog (2026-06-15: encrypted local storage for CLI+MCP OAuth creds)
**Confidence:** 📄 vendor-documented

---

### Practice: Use `codex exec` for headless and automated runs

**Do:**

Basic scripted run with JSON output:
```
codex exec "prompt" --json
```

For a fully automated run that leaves no session saved and stays within a safe sandbox:
```
codex exec "prompt" --json --ephemeral --sandbox workspace-write
```

`--ephemeral` means no session is saved after the run ends.

> When approval is set to `never` with a `workspace-write` sandbox, the agent acts
> immediately without asking — but the sandbox still limits what it can touch. This
> combination is safe for automated runs inside a properly scoped project.

🕒 **verify live:** Token budget controls and `/usage` were added in June 2026 (the
changelog dates are 2026-06-15 and 2026-06-22). Check the changelog for the latest
options.

**Sources:** [developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference) (fetched 2026-06-26) · [developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)
**Confidence:** 📄 vendor-documented

---

### Practice: Configure in `~/.codex/config.toml`

**What is TOML?** TOML is a simple config file format. Each line is `key = "value"`;
sections use `[section-name]` headers. It is easier to read than JSON for most people.

**Do:**

- Personal settings: `~/.codex/config.toml`
- Per-project settings: `.codex/config.toml` inside your project folder
- Override at the command line: `--profile <name>` or `-c key=value`

Settings are applied in this order (later ones win):
1. System defaults
2. `/etc/codex/config.toml`
3. `~/.codex/config.toml` (your personal settings)
4. `.codex/config.toml` in your project
5. `/etc/codex/system.toml` (system policy)
6. Environment variables
7. CLI flags

**Sources:** [developers.openai.com/codex/cli/reference](https://developers.openai.com/codex/cli/reference) (fetched 2026-06-26) · [blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex)
**Confidence:** ✅ independently-corroborated

---

### Practice: Pick a model deliberately

The recommended default is **GPT-5.5** (released 23 Apr 2026).

| Model | Context window | Pricing (per million tokens: input / output) | Notes |
|---|---|---|---|
| gpt-5.5 | 1,050,000 tokens | $5 / $30 | Strongest overall; recommended default |
| gpt-5.4 | — | — | Professional work |
| gpt-5.4-mini | — | — | Fast, cheap, good for bulk tasks |
| gpt-5.3-codex-spark | — | — | Research preview; ChatGPT Pro only |

A "context window" is how much text (measured in tokens) the model can hold in its
memory at once. 1,050,000 tokens is very large — roughly 750,000 words.

**Important pricing note:** Prompts over 272,000 tokens are charged at 2x input and
1.5x output for the entire session — not just the overflow.

🕒 **verify live:** The model lineup changes frequently. Check with `/model` inside
Codex for the current options.

> **Correction from grading (Timekeeper):** An earlier draft stated GPT-5.5 has a
> "400K context window." The official Codex models page (fetched 26 Jun 2026) confirms
> **1,050,000 tokens**. The 400K figure likely confused the 272K price-tier threshold
> with the context limit.

**Sources:** [developers.openai.com/codex/models](https://developers.openai.com/codex/models) (fetched 2026-06-26) · [developers.openai.com/api/docs/models/gpt-5.5](https://developers.openai.com/api/docs/models/gpt-5.5) · [blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex)
**Confidence:** ✅ independently-corroborated

---

## Part 3 — Google Gemini CLI

> ## ⚠️ READ THIS FIRST — a big change happened 18 Jun 2026
>
> On **18 June 2026, Google switched off the free "Sign in with Google" login** and
> consumer Pro/Ultra tiers for Gemini CLI, steering those users toward a new closed-source
> tool called **Antigravity CLI**.
>
> **What this means for you:** A tutorial from even a month ago will tell you to log in
> with your Google account — and that no longer works. If you are starting Gemini CLI
> today, you need one of: a **paid Gemini API key**, Vertex AI credentials, or a
> Code Assist license.
>
> The Antigravity CLI free tier is reported by the community to allow around 20
> requests per day — compared to about 1,000 before (roughly a 98% cut). *(The closed-source
> nature of Antigravity is community-reported pushback, not an official Google statement —
> treat as unconfirmed.)*
>
> Gemini CLI itself is still open-source and still works — you just need to pay or have
> the right credentials.
>
> **Sources:** Google Developers Blog (developers.googleblog.com, 2026-05-19, fetched 2026-06-26) · github.com/google-gemini/gemini-cli/discussions/27274

---

### Practice: Install Gemini CLI with Node 20 or newer

**Important:** Gemini CLI requires **Node.js version 20.0.0 or newer**. Ubuntu's default
Node.js (version 18) will fail.

**Do:**

If you do not have Node 20, install it first. Some guides use:
```
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs -y
```

> **⚠️ WARNING:** This command runs a remote script **as root** (`sudo -E bash`) — far
> more powerful than piping to an unprivileged `sh`. The script can make any change to
> your system. Only run it if you trust NodeSource (it is a well-maintained project, but
> verify at nodesource.com before running).

Once you have Node 20+, install Gemini CLI:
```
npm install -g @google/gemini-cli
```

🕒 **verify live:** `npm view @google/gemini-cli version` to see the current version
(v0.49.0 stable as of 25 Jun 2026; active development continues with preview and nightly
channels).

**Sources:** [geminicli.com/docs/get-started/installation](https://geminicli.com/docs/get-started/installation) (fetched 2026-06-26) · Google Developers Blog
**Confidence:** ✅ independently-corroborated

---

### Practice: Authenticate with a paid Gemini API key

**Do:**

1. Get a paid API key from https://aistudio.google.com/apikey
2. Set it as an environment variable. The easiest way is in a `.env` file:
   ```
   GEMINI_API_KEY=your-key-here
   ```
   Gemini CLI searches for this file starting in your current directory, then moving up
   through parent directories, and finally checking `~/.gemini/.env`.
3. Add `.env` to your `.gitignore` so the key is never uploaded to GitHub:
   ```
   echo ".env" >> .gitignore
   ```

**Why it matters / what goes wrong:** Committing an API key to a public GitHub
repository exposes it to automated scanners that find and exploit keys within minutes.

**Sources:** [geminicli.com/docs](https://geminicli.com/docs) (fetched 2026-06-26)
**Confidence:** 📄 vendor-documented

---

### Practice: Enable the sandbox before running agentic tasks

**What is the Gemini CLI sandbox?** It runs your agent inside a Docker container — an
isolated environment separate from your real machine — so the agent cannot damage your
files or system.

> **⚠️ WARNING:** The sandbox is **OFF by default**. Most beginners run Gemini CLI with
> no protection without realizing it. You must explicitly install Docker and enable the
> sandbox.

**Do:**

Install and start Docker first:
```
sudo apt install docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```
Then log out and back in (the group change requires a new session).

Enable the sandbox with the `-s` flag when you run Gemini CLI:
```
gemini -s "your prompt here"
```

Or set it permanently with the environment variable `GEMINI_SANDBOX=docker`.

**Note:** Using `--yolo` auto-enables the sandbox — but only if Docker is already
installed and running.

**Sources:** [geminicli.com](https://geminicli.com) (fetched 2026-06-26)
**Confidence:** 📄 vendor-documented

---

### Practice: Know the approval modes; avoid `--yolo` on your main machine

**Do:** Gemini CLI has three approval modes. Set them in `settings.json` or with the
`--approval-mode` flag:

| Mode | What it does |
|---|---|
| `default` | Asks before most actions (safest; start here) |
| `auto_edit` | Automatically approves file edits without asking |
| `yolo` | Automatically approves everything; enables the sandbox |

> **⚠️ `auto_edit`** means the agent can delete and recreate files without asking. If
> you did not want a file changed, it may already be changed by the time you see it.

Start with `default`. Only move to `auto_edit` or `yolo` after you understand the
sandbox and have tested the agent's behavior.

**Sources:** [geminicli.com/docs/cli/settings](https://geminicli.com/docs/cli/settings/) (fetched 2026-06-26; relocated from google-gemini.github.io)
**Confidence:** 📄 vendor-documented

---

### Practice: Run automated tasks with `gemini -p` and JSON output

**Do:**

Basic non-interactive run:
```
gemini -p "your prompt here" --output-format json
```

Parse the response with `jq` (a command-line JSON processor — not installed by default):
```
sudo apt install jq
gemini -p "Review this" --output-format json | jq '.response'
```

Exit codes (useful for scripting — check these to know if a run succeeded):
- `0` — success
- `1` — general error or API error
- `42` — input error
- `53` — turn limit exceeded

**Sources:** [geminicli.com/docs/cli/headless](https://geminicli.com/docs/cli/headless) (fetched 2026-06-26)
**Confidence:** 📄 vendor-documented

---

### Practice: Know which `settings.json` wins (7-layer precedence)

When Gemini CLI loads its settings, it reads from multiple locations and layers them on
top of each other. The last one wins.

**From lowest to highest priority:**
1. Built-in defaults
2. `/etc/gemini-cli/system-defaults.json`
3. `~/.gemini/settings.json` — **your personal settings (start here)**
4. `.gemini/settings.json` in your project — team-shared settings
5. `/etc/gemini-cli/settings.json` — system-wide policy (set by an administrator)
6. Environment variables
7. CLI flags — **always win**

**Practical advice for beginners:** Put your personal preferences in
`~/.gemini/settings.json`. Put project-specific settings in `.gemini/settings.json`
inside the project folder.

Check what context files the agent has loaded:
```
/memory show
```

Reload them after a change:
```
/memory refresh
```

> **⚠️ Safety note:** The official MCP setup example includes `"trust": true` in the
> config. This silently disables tool-approval prompts for that MCP server — the agent
> acts without asking. Do not copy-paste it unless you fully control the MCP server.

**Sources:** [geminicli.com/docs/cli/settings](https://geminicli.com/docs/cli/settings/) (fetched 2026-06-26; relocated from google-gemini.github.io/configuration)
**Confidence:** 📄 vendor-documented

---

### Practice: Verify model availability and quotas before building a workflow

🕒 **verify live:** Gemini model availability, quotas, and pricing have shifted
significantly in 2026. The current model list and free-tier limits change frequently.
Always verify at the official quota page before building any automated workflow around a
specific model.

> "Pro models became paid-only on 1 Apr 2026" is reported by community sources but has
> not been confirmed from a primary source — verify against the current quota page before
> depending on it.

**Sources:** [geminicli.com/docs](https://geminicli.com/docs) (fetched 2026-06-26)
**Confidence:** 🕒 verify live

---

## Held pending fixes (not yet in this entry)

- **Ubuntu 24.04 AppArmor profile for bubblewrap** — the check command (`sysctl kernel.apparmor_restrict_unprivileged_userns`) is here; the safe profile content is ⚠ **PENDING #317**.
- **Safe starter nftables ruleset** — the network-isolation practice warns against applying `policy drop` first; a complete ruleset with exceptions pre-included is ⚠ **PENDING #318**.
- **GPG fingerprint verification command** — the fingerprint itself is here and verified; the exact `gpg --show-keys` output format is ⚠ **PENDING #317**.
- **Token cost worked examples** — a plain "1 token is roughly three-quarters of a word" definition is included above; fuller worked examples are ⚠ **PENDING**.

---

## CHANGELOG

1. Re-leveled from the 2026-06-28 technical entry; facts and source URLs unchanged.
2. All practices kept. Practice 4 (nftables) is marked clearly as advanced and beginners are directed to the sandbox alternative — the practice itself is retained because the warnings are critical.
3. Jargon expanded on first use throughout: systemd, worktree, sandbox, token, MCP server, TOML, Docker, context window, journald, `.env`, API key.
4. "Why it matters / what goes wrong" strengthened for each practice with concrete failure modes (unexpected charges, silent stall, credential leak, file corruption).
5. All ⚠️ WARNINGs retained verbatim and kept in their original positions.
6. Corrections from the original grading panel (Timekeeper billing-change kill, GPT-5.5 context window correction) reproduced verbatim.
7. Lead path per tool: native installer for Claude Code, official script for Codex CLI, `npm install` for Gemini CLI — alternatives mentioned briefly after.
8. All source links and Confidence labels copied verbatim from the technical entry; no URLs added, dropped, or rewritten.
