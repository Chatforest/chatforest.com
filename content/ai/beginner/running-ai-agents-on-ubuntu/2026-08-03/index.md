---
title: "Running AI Agents on Ubuntu — Beginner Guide (as of 03 Aug 2026)"
date: 2026-08-03
snapshot_date: 2026-08-03
topic: running-ai-agents-on-ubuntu
track: beginner
audience: "people new to AI"
description: "A plain-language guide to installing and safely running AI agents (Claude Code, Codex CLI, Gemini CLI) on Ubuntu. Every fact here already exists in the fact-checked 2026-08-03 technical entry — nothing new was added or re-fetched."
content_type: "Best Practice"
categories: ["Claude Code", "Ubuntu", "AI Agents"]
tags: ["claude-code", "codex-cli", "gemini-cli", "ubuntu", "linux", "ai-agents", "best-practices"]
last_refreshed: 2026-08-03
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-08-03/04 (technical entry); beginner re-leveling pass on the same graded corpus"
grading_result: "Beginner re-leveling of the 2026-08-03 graded technical entry (0 fabrications after correction there). 0 new facts or URLs introduced in this pass — every claim, command, and source link below already appears in the technical entry."
---

<!-- Beginner-track snapshot. Re-leveled from the 2026-08-03 technical entry (itself a
     refresh of the 2026-06-29 snapshot). Facts, commands, and source URLs are unchanged
     from the technical entry. Only reading level and framing have been adjusted. -->

# Running AI Agents on Ubuntu — Beginner Guide (as of 03 Aug 2026)

> **What this is.** A dated, fact-checked guide re-written for people who are new to AI,
> Ubuntu, and the command line. Every claim was verified by a 3-lens panel (Skeptic,
> Beginner, Timekeeper) on the 2026-08-03 technical entry — 0 fabrications after
> correction. Items that could not be fully verified are marked **⚠ PENDING** or
> **🕒 verify live** — this guide never guesses.

## What the labels mean

- ✅ **independently-corroborated** — confirmed by 2 or more independent publishers
- 📄 **vendor-documented** — from the tool's official documentation (authoritative, one source)
- ⚠️ **WARNING** — a default that can cost you real money, break your machine, or remove a safety net
- 🕒 **verify live** — this detail changes fast (versions, prices, quotas); look it up yourself before relying on it

---

## A word before you start

An "AI agent" is a program that uses a language model (like Claude, GPT-5.6, or Gemini) to
read your files, run commands, and make changes on your behalf. That power is useful — and
dangerous if unchecked. The practices below are not optional polish; they are the
difference between a helpful assistant and an agent that runs up a large bill overnight,
leaks your passwords, or wipes files you did not want touched.

Read Part 0 first, no matter which agent you choose. Parts 1, 2, and 3 cover the specific
tools. **If you are choosing just one tool to start with, start with Claude Code (Part
1)** — it has the most beginner-oriented documentation and the smoothest install.

Six things in this guide are the most dangerous defaults we found. If you read nothing
else, read these warnings wherever they appear below:

1. Adding yourself to the `docker` group is effectively giving yourself root (full
   admin) access to your own machine — it is not a pure safety win, even though it's
   presented as a routine setup step for sandboxing.
2. A firewall mistake over SSH can lock you out of the only connection you have to fix
   it — there is no undo once that happens.
3. Claude Code's sandbox does **not** protect `~/.aws/credentials` or `~/.ssh/` unless
   you take an extra configuration step.
4. `--yolo` (Gemini CLI and Codex CLI) removes every safety net at once — disposable
   containers/VMs only, never your real machine.
5. Codex's saved login file (`~/.codex/auth.json`) is a plain text file by default, and
   it was the actual target of a real attack in June 2026 — treat it like a password.
6. Having an API key set alongside a paid subscription can silently switch you to
   pay-as-you-go billing instead of your plan — and, in the other direction, Gemini
   CLI's Vertex AI path has no built-in spending cap at all.

---

## Part 0 — Foundations (apply to any agent on Ubuntu)

These practices apply no matter which agent you run. Do them first.

---

### Practice 1: Run a long-running agent as a systemd user service 📄

**What is systemd?** Ubuntu uses a program called `systemd` to manage background
processes (called "services"). A "user service" runs as you — not as the all-powerful
root user — and restarts automatically if it crashes.

**Why not just use `nohup agent &` or a terminal you leave open?** Those approaches give
you no auto-restart, no start-on-boot, and no organized logs. A forgotten background
process is also easy to lose track of or accidentally kill.

**Do:**

1. Write a unit file at `~/.config/systemd/user/<name>.service` describing your agent,
   with `Restart=on-failure`, `RestartSec=5s`, and `StandardOutput=journal` /
   `StandardError=journal` so its logs land in the system journal (see Practice 7).
2. Store your API key (the secret password for the AI service) in a separate file,
   for example `/home/yourname/.config/myapp/environment`, and lock it down:
   `chmod 600 /home/yourname/.config/myapp/environment`.
3. Reference that file in your unit with `EnvironmentFile=%h/.config/myapp/environment`.
   `%h` is a systemd shorthand meaning "this user's home directory" — it expands
   automatically, you don't type in your actual path. Do **not** paste the key directly
   as `Environment=ANTHROPIC_API_KEY=sk-ant-…` inside the unit file — unit files can end
   up in bug reports, dotfile backups, or shared with a colleague via `systemctl cat`.
4. Enable and start the service: `systemctl --user enable --now <name>.service`
5. Allow it to keep running after you log out:
   `loginctl enable-linger $USER` (or `sudo loginctl enable-linger <user>`).

**Why it matters / what goes wrong without it:** Without linger, systemd normally kills
your whole user session — and anything running under it — shortly after your last login
ends, so your agent stops the moment you close your SSH session. Without a unit file,
crashes are silent and permanent.

> **⚠️ WARNING:** Set a spend cap on your AI account **before** you leave any agent
> running overnight. An uncapped loop can burn through credits far faster than you
> expect. Each tool has its own place to set this — see Claude Code's `/usage-credits`
> and Console spend limits (Part 1), OpenAI's usage limits for Codex CLI API-key auth
> (Part 2), and Google AI Studio / Cloud Billing budget alerts for Gemini CLI (Part 3).
> Set one of these *before* you start the service, not after.

**Sources:** [oneuptime.com — How to Set Up systemd User Services on Ubuntu](https://oneuptime.com/blog/post/2026-03-02-how-to-set-up-systemd-user-services-on-ubuntu/view) (2026-03-02)
**Confidence:** 📄 vendor-documented (a second independent source cited in the prior
snapshot could not be re-confirmed this round and was dropped rather than cited from
memory — the core `systemctl --user`/`loginctl enable-linger` commands are standard
systemd behavior either way)

---

### Practice 2: Give each agent its own git worktree 📄

**What is a git worktree?** Git (a version-control tool) normally lets you work on one
branch of your project at a time. A "worktree" creates a separate folder on disk so a
second agent can work on a different branch at the same time, without the two agents
overwriting each other's files.

**Do:**

```
git worktree add ./agent-task-1 -b agent-task-1 main
```

Before running this, check your primary branch name: `git branch`. New repos often use
`main`; older ones may use `master`.

**Why it matters / what goes wrong without it:** Two agents editing the same checked-out
files at the same time can stomp on each other's uncommitted changes.

> **Note:** Worktrees isolate **files only**. Everything else about the repository — most
> config, most refs — is shared across all worktrees by default (a small number of
> special items, like `HEAD` and the index, are per-worktree; a worktree-local config
> needs an extra setting, `git config extensions.worktreeConfig true`). Two agents in
> different worktrees of the same repo can still collide on ports, a shared database,
> caches, or secrets. A worktree is not full isolation.

**Sources:** [git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree) (official, fetched 2026-08-03)
**Confidence:** 📄 vendor-documented

---

### Practice 3: Sandbox the agent so it cannot touch the rest of your machine ✅

**What is a sandbox?** A sandbox is a cage around the agent. Inside the cage, the agent
can write to your project folder. Outside the cage — your home directory, system files,
other projects — everything is read-only or invisible.

Two tools do this on Ubuntu: **bubblewrap** (smaller, preferred) and **firejail**
(easier to configure, has bundled profiles for common programs). Neither is installed by
default.

**Do (bubblewrap — preferred):**
```
sudo apt install bubblewrap
```
**Do (firejail — easier for beginners):**
```
sudo apt install firejail
```

A minimal bubblewrap command that binds only your project folder as writable, keeps
everything else read-only, and cuts off the network looks like this (most agent tools
wrap this for you — see the per-tool sandbox practices in Parts 1-3 — but this is what's
happening underneath):
```
bwrap --ro-bind / / --dev /dev --tmpfs /tmp \
  --bind "$(pwd)" "$(pwd)" \
  --unshare-net \
  --die-with-parent \
  -- your-agent-command
```

**Why it matters / what goes wrong without it:** Without a sandbox, a misbehaving agent
(or a prompt-injection attack — where a malicious web page tricks the agent into doing
something harmful) can delete your home directory, read your SSH keys, or send your
files to an outside server.

> **⚠️ Ubuntu 24.04+ / WSL2 gotcha, now with a documented fix.** A security feature
> called AppArmor blocks bubblewrap's "user namespaces" by default on Ubuntu 24.04 and
> newer (including inside WSL2). Check whether it's active:
> ```
> sysctl kernel.apparmor_restrict_unprivileged_userns
> ```
> If it returns `0` or "No such file," you're fine — skip this step. If it returns `1`,
> create the following profile so bubblewrap can work again:
> ```
> sudo tee /etc/apparmor.d/bwrap > /dev/null <<'EOF'
> abi <abi/4.0>,
> include <tunables/global>
>
> profile bwrap /usr/bin/bwrap flags=(unconfined) {
>   userns,
>   include if exists <local/bwrap>
> }
> EOF
> sudo systemctl reload apparmor
> ```
> This is the exact fix Anthropic's own Claude Code documentation now publishes as an
> official troubleshooting step, and an independent blog (jdhodges.com) publishes the
> identical text — so this is a well-corroborated, real fix, not a guess. **Verify it
> worked** by re-running the sandbox/`bwrap` command that previously failed with
> `bwrap: Creating new namespace failed: Permission denied` and confirming it now
> succeeds (re-running the `sysctl` check above won't show a change — the profile itself
> doesn't alter that value). This profile only affects `bwrap` itself, not the commands
> that run inside the sandbox.
>
> Ubuntu also ships a similar profile of its own (`bwrap-userns-restrict`), but on
> 24.04 it exists on disk and is **not turned on by default** — confirmed via Ubuntu's
> own package changelog. Ubuntu 25.04 and newer turn a version of it on by default, per
> Ubuntu's official 25.04 release notes. Whether Ubuntu 26.04 does the same could not be
> confirmed from any official source this round — if you're on 26.04, run the `sysctl`
> check yourself rather than assuming either way.
>
> **Also worth knowing:** if you're running a self-built (not apt-installed) bubblewrap
> in "setuid" mode, make sure it's at least version 0.11.2 (released 23 Apr 2026) — that
> release fixed a real, documented security bug (CVE-2026-41163, rated "High" severity)
> in setuid-mode bubblewrap installs from 0.11.0 up to 0.11.2. Ubuntu's normal apt
> package is not installed setuid, so this doesn't change the install steps above for
> most readers.
>
> **If you're new to this and it feels like a lot:** setting
> `kernel.apparmor_restrict_unprivileged_userns=0` instead of installing the profile
> "works," but it turns off this kernel protection for your *entire machine*, not just
> for the sandbox — the profile above is the safer fix.

**Sources:** [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-08-03) ·
[jdhodges.com — How to Fix Codex Sandbox Errors on Ubuntu 24.04](https://www.jdhodges.com/blog/codex-sandbox-ubuntu-24-04-fix/) (2026-04-23) ·
[github.com/dfaerch/bubblewrap-on-ubuntu — profiles/24.04](https://github.com/dfaerch/bubblewrap-on-ubuntu/tree/main/profiles/24.04) (community, undated) ·
[launchpad.net/ubuntu/+source/apparmor/+changelog](https://launchpad.net/ubuntu/+source/apparmor/+changelog) (fetched 2026-08-03) ·
[documentation.ubuntu.com/release-notes/25.04](https://documentation.ubuntu.com/release-notes/25.04/) (official, fetched 2026-08-03) ·
[github.com/containers/bubblewrap/releases/tag/v0.11.2](https://github.com/containers/bubblewrap/releases/tag/v0.11.2) (fetched 2026-08-03) ·
[radar.offseq.com — CVE-2026-41163](https://radar.offseq.com/threat/cve-2026-41163-cwe-269-improper-privilege-manageme-949f6d2e) (fetched 2026-08-04) ·
[github.com/netblue30/firejail/releases](https://github.com/netblue30/firejail/releases) (0.9.80, 14 Mar 2026)
**Confidence:** ✅ independently-corroborated (the fix itself; the default-Ubuntu-behavior
detail is 📄 vendor-documented)

---

### Practice 4: Block outbound network traffic you did not explicitly allow ⚠️ advanced

**What is this?** By default, a program on your machine (including an AI agent) can
connect to any address on the internet. "Default-deny outbound" flips that around: the
agent can only reach addresses you've explicitly allowed. The Ubuntu tool for this is
`nftables`. (Ubuntu's older `ufw` firewall and `nftables` should not both be active at
once — Ubuntu's own docs say `ufw` "should not be used concurrently with native
`nftables` firewall rules." Pick one.)

> **⚠️ WARNING — this can lock you out of your own server, and the rollback may not
> save you.** If you apply a "deny everything" rule *before* you've added your
> allow-rules, you cut your machine off the internet immediately. If you're SSH'd into a
> remote box with no other way in (no physical keyboard, no console access) and you get
> the order wrong, **the very connection you'd need to fix it is the one you just cut
> off.** There is no escape hatch once that happens — the usual rollback command
> (`sudo nft flush ruleset`) is useless if you can no longer reach the machine to run it.
>
> **Before you try this on a remote box:** (1) test the exact rule set on a machine you
> have local or console access to first, or (2) set up a self-reverting safety net —
> for example `sudo at now + 5 minutes` running a job that flushes the rules, so a
> lockout heals itself automatically even if your SSH connection drops.
>
> **If you're new to Linux networking, skip this practice for now** and rely on the
> sandbox's own built-in network controls instead (Practice 3 above, or each tool's
> sandbox network settings in Parts 1-3).

**What a real starter rule set looks like (still needs adapting — not copy-paste-ready
for a bare machine):** One dated, independently published example (from INNOQ's
engineering blog) shows a rule set that allows DNS, an established-connections
exception, and traffic to a specific proxy, then denies everything else:
```
table inet sandbox {
  chain output {
    type filter hook output priority 0; policy drop;
    oif "lo" accept
    ct state established,related accept
    udp dport 53 accept
    tcp dport 53 accept
    ip daddr 172.17.0.0/16 accept   # Allow traffic to the proxy
    ip daddr 172.18.0.0/16 accept   # Allow traffic to the proxy
    ip daddr <proxy-host-ip> tcp dport 8888 accept
  }
}
```
**An important detail beginners often miss: nftables filters by IP address, not by
domain name.** You cannot write a rule that says "allow api.anthropic.com" — a domain
name can resolve to different IP addresses over time. The realistic options are either
(a) look up your allowed hosts once and pin those IPs, accepting that they can change
later, or (b) route the agent's traffic through a proxy that understands domain names,
and only let nftables allow traffic *to that proxy*. Even option (b) has a real limit:
it "cannot stop a process that ignores the proxy and opens a raw [network] connection,"
per one of the sources below. This example is written for a container-sandbox setup, not
a bare Ubuntu machine — you'll need to substitute your own proxy address and decide
between the two options above before using it.

**Sources:** [documentation.ubuntu.com/security/security-features/network/firewall/nftables](https://documentation.ubuntu.com/security/security-features/network/firewall/nftables/) (official, fetched 2026-08-03) ·
[documentation.ubuntu.com/security/security-features/network/firewall](https://documentation.ubuntu.com/security/security-features/network/firewall/) (official, fetched 2026-08-03) ·
[innoq.com/en/blog/2026/03/dev-sandbox-network](https://www.innoq.com/en/blog/2026/03/dev-sandbox-network/) (2026-03-03) ·
[h5i.dev/blog/sandboxing-ai-agents-h5i](https://h5i.dev/blog/sandboxing-ai-agents-h5i/) (2026-06-12, updated 2026-06-26) ·
[github.com/89luca89/clampdown](https://github.com/89luca89/clampdown) (fetched 2026-08-03, iptables not nftables — corroborates the pattern, not the exact syntax)
**Confidence:** ✅ independently-corroborated for the general pattern (three different
publishers agree); 📄 vendor-documented-adjacent for the exact nftables syntax
(one worked example) — still not a turnkey ruleset for a plain Ubuntu box

---

### Practice 5: Keep your secrets (API keys, passwords) out of the repo and away from the agent ✅

**What is a secret?** An API key is like a password that charges your account when used.
A `.env` file is a text file that stores these secrets as environment variables (named
values your programs can read).

**The hidden danger:** Adding your `.env` to `.gitignore` (so it doesn't get uploaded to
GitHub) is not enough. **Agents routinely run commands like `cat .env` or `printenv`,**
and any agent with terminal access can also read your `.bashrc`/`.zshrc`/`.zshenv`. Any
file the agent can read is a file it might paste into a shell command, send to the AI
model as output, or write into a log.

**Do:**

- Add `.env` to `.gitignore`.
- For stronger protection, store secrets in the OS keyring (GNOME Keyring) instead of a
  plain file:
  ```
  sudo apt install libsecret-tools
  secret-tool store --label="My API Token" service myapp username <you>
  ```
  and retrieve it at launch time with `secret-tool lookup service myapp username <you>`
  — rather than a value sitting in a file the agent can browse.
- `chmod 600` any on-disk secrets file you still need to keep.

**Why it matters / what goes wrong without it:** A leaked API key means someone else can
use your AI account at your expense. A leaked SSH key means someone can log in to your
server.

> **Two sources, two slightly different opinions:** one guide treats the OS keyring as
> the right Linux default and treats a dedicated secrets manager (like 1Password's CLI)
> as a *later* step you only need once you're syncing secrets across multiple machines
> or over SSH. The other recommends the keyring alone, with no external manager at all.
> Read together: the keyring is a reasonable default for a single Ubuntu box; only reach
> for a dedicated secrets manager once you need the same secret on multiple machines.

**Sources:** [rbt.rs/blog/secret-management-in-the-age-of-ai-coding-agents](https://rbt.rs/blog/secret-management-in-the-age-of-ai-coding-agents/) (2026-03, Srđan Marković/Red Black Tree) ·
[linuxjunkies.org/guides/use-keyring-and-secret-manager](https://linuxjunkies.org/guides/use-keyring-and-secret-manager) (updated 2026-06-07) ·
[manpages.debian.org secret-tool(1)](https://manpages.debian.org/testing/libsecret-tools/secret-tool.1.en.html) (command syntax reference)
**Confidence:** ✅ independently-corroborated

---

### Practice 6: Limit what parts of the filesystem the agent can write to ✅

**What is `DynamicUser`?** When you add `DynamicUser=yes` to a systemd unit file,
systemd creates a temporary, throwaway user ID just for that one service run and deletes
it when the run ends. This temporary user cannot access your home directory at all.

**Do:** In your systemd unit file, add:
```
DynamicUser=yes
ReadOnlyPaths=/
ReadWritePaths=/path/to/your/project
```

**Why it matters / what goes wrong without it:** Without these restrictions, the agent
runs as you and can read or overwrite any file you own — including other projects, SSH
keys, and browser profiles.

**Caveat:** `DynamicUser` reuses temporary IDs between runs, so don't leave files owned
by that temporary user lying around — a later run could be assigned the same ID and gain
access to them. `ReadOnlyPaths`/`ReadWritePaths` only affect the service's private view
of the filesystem, not the real files on disk, and they don't stop the service from
*connecting to* things that are already running (like a database socket) — they are not
a substitute for a real sandbox (Practice 3) if you're worried about a fully compromised
agent process.

**Sources:** [man7.org/linux/man-pages/man5/systemd.exec.5.html](https://man7.org/linux/man-pages/man5/systemd.exec.5.html) (official upstream man page, fetched 2026-08-03) ·
[redhat.com/en/blog/systemd-secure-services](https://www.redhat.com/en/blog/systemd-secure-services) (2020-05-11) ·
[nickb.dev/blog/writing-a-secure-systemd-service-with-sandboxing-and-dynamic-users](https://nickb.dev/blog/writing-a-secure-systemd-service-with-sandboxing-and-dynamic-users/) (2020-12-29; older post, re-checked this run and unchanged)
**Confidence:** ✅ independently-corroborated

---

### Practice 7: Check what the agent did by reading its logs ✅

**What is journald?** Ubuntu's `journald` is the system log collector. Logs from your
systemd user services are automatically stored there once the service logs to
`StandardOutput=journal` (Practice 1).

**Do:**

- See logs for your agent service: `journalctl --user -u <name>.service`
- Watch logs live: add `-f`
- See only recent history: `--since "1 hour ago"` or `--since today`
- Combine multiple services in one timeline:
  `journalctl -u nginx.service -u php-fpm.service --since today`

If you want to read the full *system* journal (not just your own user's logs), join the
right group first, then log out and back in:
```
sudo usermod -aG systemd-journal $USER
```

**Why it matters / what goes wrong without it:** Leaving an agent running unattended is
only safe if you can audit what it did afterward. Without logs, you have no way to know
if it silently failed, ran up a large bill, or made unexpected changes. Note that
journald doesn't keep logs forever — check the retention settings in
`/etc/systemd/journald.conf` (`SystemMaxUse=`) if you need a long audit trail.

**Sources:** [digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs) (updated 2026-04-27) ·
[dash0.com/guides/systemd-logs-linux-journalctl](https://www.dash0.com/guides/systemd-logs-linux-journalctl) (last updated 2025-07-06)
**Confidence:** ✅ independently-corroborated

---

## Part 1 — Claude Code (Anthropic)

Claude Code is Anthropic's agent for writing, editing, and running code. It is the
recommended starting point for beginners because it has the most beginner-oriented
documentation and the smoothest install process.

---

### Practice: Install with the native installer; confirm with `claude doctor` 📄

**Do:**
```
curl -fsSL https://claude.ai/install.sh | bash
```
Then check the install worked:
```
claude --version
claude doctor
```
This installs a single self-contained program (no separate Node.js install needed) at
`~/.local/bin/claude`. Minimum requirements: Ubuntu 20.04+ (also Debian 10+, Alpine
3.19+), 4 GB+ RAM, x64 or ARM64. 🕒 **verify live** — the version at this snapshot is
v2.1.220 (24-25 Jul 2026), but Claude Code ships very frequently (300+ releases so far),
so check `claude --version` yourself rather than trusting a fixed number.

**Why it matters:** One command, and native installs auto-update in the background so
you stay patched without thinking about it. `claude doctor` gives you a read-only health
check (install status, settings validity, last update result) before you waste time
debugging something else.

**Caveat:** Piping a remote script to `bash` means trusting that URL without reading it
first — the script runs with your full permissions. The alternative
`npm install -g @anthropic-ai/claude-code` route also works and installs the same
program, but requires Node.js 22 or newer as of v2.1.198. **Never run
`sudo npm install -g`** — Anthropic's own documentation warns this "can lead to
permission issues and security risks."

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-08-03) ·
[code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog) (fetched 2026-08-03, shows v2.1.220 / 25 Jul 2026)
**Confidence:** 📄 vendor-documented

---

### Practice: Prefer the signed apt repo for verified, system-managed installs 📄

**What is a signed apt repo?** `apt` is Ubuntu's built-in package manager (the same tool
behind `sudo apt install`). A "signed" repo means the software is cryptographically
signed by the vendor, so you can verify it hasn't been tampered with.

**Do:**
```bash
sudo apt install curl gnupg
sudo install -d -m 0755 /etc/apt/keyrings
sudo curl -fsSL https://downloads.claude.ai/keys/claude-code.asc -o /etc/apt/keyrings/claude-code.asc
gpg --show-keys /etc/apt/keyrings/claude-code.asc   # verify fingerprint below
echo "deb [signed-by=/etc/apt/keyrings/claude-code.asc] https://downloads.claude.ai/claude-code/apt/stable stable main" \
  | sudo tee /etc/apt/sources.list.d/claude-code.list
sudo apt update && sudo apt install claude-code
```
Check that the GPG fingerprint you see reads exactly (unchanged since the June 2026
snapshot):
```
31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE
```

> **If the fingerprint does NOT match: stop. Do not proceed with the install, and report
> it.** A mismatch means the key you downloaded isn't actually Anthropic's.

Choose the `stable` channel (about a week behind, skips major regressions) or `latest`.

**Caveat:** `apt` does **not** auto-update Claude Code — you must run
`sudo apt update && sudo apt upgrade claude-code` yourself. Only the native installer
(previous practice) auto-updates by default. Anthropic also publishes a signed
`manifest.json` (checksums per platform, GPG-signed) for every release, so you can verify
a downloaded binary's integrity independently of the package manager.

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-08-03, fingerprint re-verified verbatim against the live page)
**Confidence:** 📄 vendor-documented (a fingerprint is a security credential — only the
vendor is authoritative here)

---

### Practice: Pick an update channel and set a version floor 📄

**Do:** In `~/.claude/settings.json` (or via `/config` → Auto-update channel), set:
```json
{
  "autoUpdatesChannel": "stable"
}
```
`"latest"` is now the documented default if you don't set anything; beginners should
still consider `"stable"`. Add `minimumVersion` so a channel switch can't silently
downgrade you:
```json
{
  "autoUpdatesChannel": "stable",
  "minimumVersion": "2.1.0"
}
```
Run `claude update` to apply an update immediately. To freeze a machine (for example, a
production server) at its current version, add one of these to the `env` block in
settings:
- `DISABLE_AUTOUPDATER` — stops only the background update check (`claude update` still
  works manually)
- `DISABLE_UPDATES` — blocks every update path entirely

**Caveat:** If you installed via `apt`/`dnf`/`apk`/Homebrew, those package managers
control the update channel instead of `autoUpdatesChannel`.

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-08-03, "Configure release channel" and "Pin a minimum version" sections)
**Confidence:** 📄 vendor-documented

---

### Practice: Authenticate — and avoid the billing trap ✅

**Interactive use (normal laptop/desktop):** Run `claude` and follow the browser login
prompt.

**Over SSH (you're logged in remotely):** Press `c` to copy the login URL, or paste the
browser's login code back into the terminal — this is common when the login page can't
reach your terminal directly (SSH, WSL2, containers).

**Unattended/automated use (no human present):** Two options:
- `claude setup-token` — mints a 1-year login token
  (`CLAUDE_CODE_OAUTH_TOKEN`), drawing on your Pro/Max/Team/Enterprise subscription.
- Set `ANTHROPIC_API_KEY` — uses Anthropic Console pay-as-you-go billing (charged per
  token used).

> **⚠️ WARNING — cost trap.** If you have BOTH a subscription AND `ANTHROPIC_API_KEY`
> set, **the API key wins, and you're billed pay-as-you-go instead of drawing on your
> plan.** This is confirmed directly in Anthropic's own documentation. To check: run
> `unset ANTHROPIC_API_KEY`, then run `/status` inside Claude Code — it shows a "Login
> method" row and an "API key" row when a key is active. **Two other things can cause the
> same silent switch to pay-as-you-go billing** even after you `unset` the key: a
> cloud-provider environment variable (Bedrock/Vertex/Foundry), or a configured
> `apiKeyHelper` script. If `/status` still shows an API key active after unsetting it,
> check for one of those two next. Claude Code on the Web always uses your subscription
> and ignores these env vars inside its own sandbox — this trap is specific to running
> the CLI locally.

**On Linux, where are credentials stored?** In `~/.claude/.credentials.json` at
permission `0600` (only you can read it). Unlike macOS, there is no separate OS
keychain — that file *is* your credential. Protect it the way you'd protect a password.

**Caveat:** `--bare` mode (used for clean automated runs, see next practice) never reads
your login/keychain credentials at all — you must use `ANTHROPIC_API_KEY` or
`apiKeyHelper` there.

**Sources:** [code.claude.com/docs/en/authentication](https://code.claude.com/docs/en/authentication) (fetched 2026-08-03, "Authentication precedence" section) ·
[blog.laozhang.ai/en/posts/claude-code-api-key-vs-subscription-billing](https://blog.laozhang.ai/en/posts/claude-code-api-key-vs-subscription-billing) (accessed 2026-08-03) ·
[andrew.ooo/answers/anthropic-claude-code-june-15-billing-change-may-2026](https://andrew.ooo/answers/anthropic-claude-code-june-15-billing-change-may-2026/) (published 2026-05-28, updated 2026-07-22)
**Confidence:** ✅ independently-corroborated

---

### Practice: Run automated tasks with `claude -p`, scoped tightly 📄

**What is `claude -p`?** The `-p` flag puts Claude Code into "non-interactive" (also
called headless or print) mode: give it one prompt, it does the task, and exits. Useful
for scripts and scheduled jobs where no human is watching.

**Do:**
```
claude -p "prompt"
```
Restrict which tools it can use — always the smallest set the task needs:
```
claude -p "Read main.py and list all functions" --allowedTools "Read,Grep,Glob"
```
Get machine-readable output (includes `total_cost_usd` per run):
```
claude -p "Review this file" --output-format json
```
For clean, reproducible automated runs, add `--bare` — it skips auto-discovery of hooks,
skills, plugins, MCP servers, memory, and CLAUDE.md. Anthropic's docs say `--bare` "will
become the default for `-p` in a future release," so it's worth adopting now for
scripted/CI calls.

> **⚠️ Pre-approve tools before any unattended run.** Without `--allowedTools`, Claude
> Code pauses and waits for a permission prompt that no one is there to answer — your
> script silently stalls. Use `--permission-mode dontAsk` (deny anything not explicitly
> allowed) for locked-down automated runs.

**Caveat:** `--bare` skips your login entirely, so set `ANTHROPIC_API_KEY` or
`apiKeyHelper` for it. Piped input is capped at 10 MB (v2.1.128+) — for bigger input,
write it to a file and reference the file path instead. Interactive-only commands like
`/login` don't work in `-p` mode.

**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 2026-08-03)
**Confidence:** 📄 vendor-documented

---

### Practice: Use permission allowlists rather than bypassing permissions entirely 📄

**What are permissions?** Claude Code asks your permission before running commands it
considers risky. `/permissions` lets you pre-approve specific safe commands so you're not
interrupted constantly, without turning off all protections.

**Do:** Open `/permissions` and set rules like:
- Allow (safe, common): `Bash(npm run *)`, `Bash(git commit *)`
- Deny (protect yourself): `Bash(git push *)`, `Read(.env)`, `Read(~/.ssh/**)`

Rules are always evaluated **deny → ask → allow**, in that order, regardless of how
specific a rule is.

`auto` mode is a newer option: a separate reviewer model checks each action and blocks
only what looks risky (scope escalation, unfamiliar infrastructure), letting routine work
proceed without prompts while keeping a safety net. `dontAsk` mode auto-denies anything
not already pre-approved.

> **⚠️ AVOID `bypassPermissions` / `--dangerously-skip-permissions`** except inside a
> throwaway container or VM. Even in bypass mode, explicit "ask" rules and `rm -rf /` /
> `rm -rf ~` still trigger a prompt as a last-resort circuit breaker. **It's blocked
> outright when running as root or via `sudo` on Linux/macOS** — root access plus no
> prompts at all is considered too dangerous to allow directly.

**Caveat:** Permission rules are enforced by Claude Code itself, not by the operating
system, and only cover tools Claude Code recognizes — a Python or Node.js script that
opens files on its own bypasses Read/Edit deny rules entirely. Rules that try to
constrain command arguments (e.g. only allowing `curl` to one domain) are fragile and can
be worked around with redirects or shell variables — for real enforcement, use the
sandbox (next practice), which enforces at the OS level instead of by matching command
text.

**Sources:** [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-08-03) ·
[code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-08-03, "`--dangerously-skip-permissions` fails as root" section)
**Confidence:** 📄 vendor-documented

---

### Practice: Enable the built-in Bash sandbox (bubblewrap) — and don't skip the credentials step ✅

Claude Code has a built-in sandbox that uses bubblewrap (Part 0, Practice 3) to confine
the Bash commands it runs to your project directory. This is separate from — and in
addition to — the permission allowlists above.

**Do:** Run `/sandbox`. Install the dependencies first:
```
sudo apt-get install bubblewrap socat
```
(bubblewrap does the file isolation; socat relays the sandbox's network traffic.) Turn
sandboxing on per-project (`/sandbox` writes `.claude/settings.local.json`) or globally
via `sandbox.enabled: true` in `~/.claude/settings.json`.

> **⚠️ WARNING — the sandbox does NOT protect your credentials by default.** Even with
> `/sandbox` turned on, the default read policy still lets the agent read
> `~/.aws/credentials` and `~/.ssh/` if they exist on the machine. This is not covered by
> just turning the sandbox on — it is a separate, extra step: use `sandbox.credentials`
> to explicitly deny reading `~/.aws/credentials` and `~/.ssh`, and to deny/mask secret
> environment variables from sandboxed commands. If you keep real cloud or SSH
> credentials on the same machine you're sandboxing, this step is not optional.

> **⚠️ Ubuntu 24.04+ / WSL2 gotcha (same fix as Part 0, Practice 3):** AppArmor blocks
> bubblewrap from creating user namespaces by default. Check
> `sysctl kernel.apparmor_restrict_unprivileged_userns` — `0` or "No such file" means
> skip this step; `1` means you need the AppArmor profile shown in Part 0, Practice 3.
> An independent Linux-sandboxing blog documents this exact same failure
> (`bwrap: Creating new namespace failed: Permission denied`) and the same fix,
> confirming this is a real, common issue and not specific to Anthropic's tooling.

**Caveat:** This sandbox is a strong extra layer, not a complete boundary. By default the
built-in network proxy does not inspect the *contents* of encrypted (HTTPS) traffic —
only which domain a connection goes to. That means a broadly-allowed domain could still
be misused to send data out under cover of a trusted destination ("domain fronting").
Some tools don't work inside the sandbox at all: `watchman` (run `jest --no-watchman`
instead) and `docker` (add `docker *` to `excludedCommands`). Native Windows isn't
supported — run Claude Code inside WSL2 for sandboxing there.

**Sources:** [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-08-03) ·
[labs.esokia.com/post/sandboxing-claude-code-cli-linux-bubblewrap](https://labs.esokia.com/post/sandboxing-claude-code-cli-linux-bubblewrap/) (published 2026-03-18)
**Confidence:** ✅ independently-corroborated

---

### Practice: Never let secrets sit where the agent (or chat) can casually leak them 📄

**Do:**
- Store secrets in environment variables or a secret manager; avoid pasting secret
  values into the chat window as routine practice — treat the conversation like any
  other channel a secret shouldn't travel through.
- In MCP server config (next practice), reference credentials with `${VAR}` expansion
  rather than typing tokens directly into the file.
- `.gitignore` your `.env`.
- In `CLAUDE.md` (see below), document *which* environment variables exist — never their
  values.

**Caveat:** Claude does not automatically read environment variables into its context
window — values are only available to commands it actually runs. A subprocess can still
read secret files unless you also use the sandbox's credential-blocking controls
(previous practice) or set `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` to strip Anthropic and
cloud-provider credentials from every subprocess it launches. Network requests (`curl`,
`wget`, WebFetch) require your approval by default and aren't auto-approved — a real
safeguard against a prompt-injection attack trying to exfiltrate data, but only if you
don't blanket-allow them.

**Sources:** [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-08-03) ·
[code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-08-03)
**Confidence:** 📄 vendor-documented

---

### Practice: Add MCP servers (plug-ins) with `claude mcp add`, at the right scope 📄

**What is MCP?** MCP (Model Context Protocol) connects Claude to external tools — GitHub,
databases, Figma. Think of an MCP server as a plug-in that gives the agent a new
capability. Connect one with `claude mcp add --transport http <name> <url>` (HTTP is now
the recommended connection type; the older SSE type is deprecated).

**Do:** Choose a scope for each server:
- **local** (default) — private to you, stored in `~/.claude.json`
- **project** — stored in `.mcp.json`, checked into git, each teammate approves it on
  first use
- **user** — available in all your projects, private to you

Put credentials in environment variables or `headersHelper`, never as literal tokens
typed into `.mcp.json`.

**Why it matters / what goes wrong:** More MCP servers means more context loaded into
every conversation (which costs more tokens, and therefore more money) and more attack
surface — verify you trust a server before connecting it, since a server that fetches
external content can expose you to prompt injection. Disable servers you're not using
with `/mcp`.

**Caveat:** For many simple tasks, a plain command-line tool (`gh` for GitHub, `aws` for
AWS, `gcloud` for Google Cloud) uses less context than an MCP server doing the same job,
since it adds no per-tool listing overhead. Claude Code also warns when MCP tool output
exceeds 10,000 tokens and truncates it at 25,000 by default.

**Sources:** [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-08-03) ·
[code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 2026-08-03, "Reduce MCP server overhead")
**Confidence:** 📄 vendor-documented

---

### Practice: Use hooks for things that must happen every single time 📄

**What is a hook?** A hook is a shell command that Claude Code's harness runs
automatically at certain moments — before a tool runs, after a file is edited, when a
session ends. Unlike instructions written in CLAUDE.md (which the AI model may or may
not follow), hooks are deterministic: they always run, no matter what the model decides.

> **⚠️ WARNING:** Hooks run with YOUR shell permissions. A malicious or buggy hook is
> real code execution on your machine. Review any hook — especially one from a shared or
> project config, or a plugin — before enabling it. Hooks that `deny` an action run even
> under `bypassPermissions` / `--dangerously-skip-permissions` — good for enforcing org
> policy, but it also means a bad hook can't be worked around just by disabling
> permissions.

**Do:** Add a `hooks` block to `settings.json`. Main events:
- `PreToolUse` — runs before a tool executes; exiting with code 2 blocks the action
- `PostToolUse` — runs after a tool, e.g. run a formatter after every file edit
- `Stop` — blocks a turn from ending until a check passes (e.g. tests must pass)

You can ask Claude to write hooks for you: *"write a hook that runs eslint after every
file edit."*

**Why it matters:** If you rely on CLAUDE.md alone to enforce a rule ("always run tests
before saying you're done"), the model may skip it. A `Stop` hook makes the check
mandatory instead of advisory.

**Caveat:** When multiple hooks match the same event, they all run in parallel, and
identical handlers are automatically de-duplicated — that is the one cross-hook behavior
Anthropic's documentation confirms. `--bare` mode skips hook discovery entirely.

**Sources:** [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) (fetched 2026-08-03, full hooks reference) ·
[code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-08-03, "Extend permissions with hooks")
**Confidence:** 📄 vendor-documented

---

### Practice: Write a short, high-signal CLAUDE.md and keep it short 📄

**What is CLAUDE.md?** A special text file in your project that Claude Code reads at the
start of every session — your chance to tell Claude things it can't infer from the code
itself.

**Do:** Run `/init` to generate a starting point automatically. Keep only what Claude
genuinely can't figure out on its own: non-obvious shell commands, code-style rules that
differ from language defaults, which test runner to use, branch/PR conventions, required
environment variables (names, not values), and non-obvious gotchas. Aim under ~200 lines;
run `/context` to confirm it loaded. Move occasional or complex workflows into "skills"
(loaded on demand, not every session) instead of cramming them into CLAUDE.md. For each
line, ask: "would removing this cause Claude to make mistakes?" If not, remove it.

**Why it matters / what goes wrong:** A very long CLAUDE.md is counterproductive. If
Claude keeps violating a rule, the file is probably too long and the rule is getting lost
in the noise — the fix is usually to trim the file, not to phrase the rule more
forcefully (though you can add emphasis like "IMPORTANT" or "YOU MUST" to a rule that
really matters).

**Caveat:** Check CLAUDE.md into git so your whole team shares it. Keep personal notes in
`CLAUDE.local.md` (gitignored).

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-08-03, "Write an effective CLAUDE.md")
**Confidence:** 📄 vendor-documented

---

### Practice: Watch your costs — clear context, choose your model, and know about the pricing cliff ✅

**What is a token?** A token is roughly three-quarters of a word. Cost scales with how
many tokens are in the conversation (the "context") and which model you use. *Note: newer
models (Claude 4.7 and later, including Sonnet 5 and Opus 5) use a different counting
method that produces around 30% more tokens for the same amount of text than older
models — worth knowing if you compare cost estimates across model generations.*

**Do:**
- Check `/usage` (per-session estimate; also breaks spend down by skill, subagent,
  plugin, and MCP server) and `/context`.
- `/clear` between unrelated tasks — Claude Code resends the whole conversation history
  on every turn, so a long, cluttered session quietly multiplies your cost.
- Use **Sonnet** for most tasks; **Opus** for hard multi-step reasoning (`/model`).
- For automated `-p` runs, parse `total_cost_usd` out of `--output-format json`.
- On Pro/Max, `/usage-credits` lets you extend past your plan limit; on Console/API
  billing, set workspace spend limits at platform.claude.com.

> 🕒 **verify live — pricing cliff.** **Claude Sonnet 5 is the current default model** in
> Claude Code and carries introductory pricing of **$2/$10 per million input/output
> tokens through 31 Aug 2026**, after which it rises 50% to the standard $3/$15 per
> million. This mainly affects API/Console-billed usage — Pro/Max subscribers pay a flat
> seat price, not per-token, so this doesn't hit their bill directly, but Console/API
> teams should expect a real step change on 1 Sep 2026.
>
> **Also new since June: Claude Opus 5 (24 Jul 2026)** is now the default model on Claude
> Max and selectable on Pro, priced at $5/$25 per million tokens (unchanged from the
> previous Opus generation). If you're following the "Opus for hard reasoning" advice
> above, this is the model you'll get.
>
> **Also time-sensitive:** a temporary 50% weekly-usage-limit increase for Pro/Max/Team/
> Enterprise Claude Code users has reportedly been extended through 19 Aug 2026 — 16 days
> after this snapshot. If you're on one of these plans, you have more headroom today than
> you will after that date. This end-date comes from independent reporting, not a direct
> Anthropic changelog fetch this round — re-check before relying on it past mid-August.

**Caveat:** `/usage`'s dollar figure is computed locally at standard list prices — it
doesn't reflect promotional pricing or contracted discounts and may not match your
actual bill. Use the Console usage page for the authoritative number.

**Sources:** [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 2026-08-03) ·
[platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 2026-08-03) ·
[finopsllm.com/research/sonnet-5-intro-pricing-deadline](https://finopsllm.com/research/sonnet-5-intro-pricing-deadline) (published 2026-07-19) ·
[anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5) (24 Jul 2026) ·
axios.com — Anthropic releases new model Opus 5 (24 Jul 2026; consistently returns 403 bot-detection on re-fetch, unlinked per policy — corroborated by the Anthropic vendor link above) ·
[helpnetsecurity.com — Claude Code weekly limits promotion extended](https://www.helpnetsecurity.com/2026/07/13/claude-code-weekly-limits-promotion-extended/) (13 Jul 2026)
**Confidence:** ✅ independently-corroborated (pricing cliff, Opus 5 launch); 📄
vendor-documented (cost controls); the weekly-limit end date is 🕒 verify live

---

### Practice: Always give Claude a way to verify its own work 📄

**Do:** For every task, also give Claude a way to check whether it succeeded: a test
suite it can run, a build command whose exit code tells it pass/fail, a linter, or a diff
to review. For a whole session, `/goal` has a separate evaluator re-check a condition
after every turn. For a hard, mandatory gate on unattended runs, use a `Stop` hook (see
hooks practice above) so the session can't declare "done" until the check actually
passes. For a second opinion, ask for a fresh review (a review from a Claude instance
that wasn't the one that made the change) so the reviewer isn't biased toward agreeing
with its own prior reasoning. Ask Claude to show evidence — test output, the exact
command and result — rather than just asserting success.

**Why it matters / what goes wrong:** Without a verification step, Claude Code may
confidently report success while the code still has errors. Requiring evidence catches
this before you find out the hard way.

**Caveat:** A reviewer asked to find gaps will usually report *some*, even when the work
is sound, because that's what it was asked to do — don't chase every finding, or you'll
over-engineer the fix. Ask the reviewer to flag only gaps that affect correctness or
stated requirements.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-08-03, "Give Claude a way to verify its work" and "Add an adversarial review step")
**Confidence:** 📄 vendor-documented

---

## Part 2 — OpenAI Codex CLI

Codex CLI is a good choice if you're already paying for ChatGPT or an OpenAI API
subscription. It's open source (Apache-2.0, mostly written in Rust), still published as
`openai/codex` on GitHub.

> **What changed since the June snapshot:** OpenAI launched a new model family — Sol,
> Terra, and Luna — on 9 Jul 2026, replacing the earlier GPT-5.5 guidance (see the model
> practice below). OpenAI's documentation also moved from `developers.openai.com/codex/*`
> to `learn.chatgpt.com/docs/*` (old links still resolve, for now). And most
> importantly for safety: the previous entry said Codex's saved login was encrypted —
> that turned out to be wrong. See the auth practice below.

---

### Practice: Install via the official script, npm, Homebrew, or a prebuilt binary — never `sudo npm -g` ✅

**Do:** Install with one of:
```
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```
or
```
npm install -g @openai/codex
```
or `brew install --cask codex`, or download a prebuilt binary from GitHub Releases.
Latest stable version at this snapshot: v0.146.0 (29 Jul 2026); this project ships new
releases almost daily, so check `codex --version` yourself.

**Why it matters:** Piping a remote script into `sh` means trusting that URL completely —
the script runs with your permissions before you've read a line of it. It's a common,
accepted pattern for this kind of tool, but know what you're agreeing to.

> **⚠️ Never `sudo npm install -g`.** It creates root-owned files that break future
> updates and can leave permission problems behind. If `codex` isn't found after a plain
> `npm install -g`, fix your PATH instead:
> ```
> echo 'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.bashrc
> source ~/.bashrc
> ```
> (use `~/.zshrc` instead if you run zsh) — don't reach for `sudo`.

**Sources:** [github.com/openai/codex](https://github.com/openai/codex) (fetched 2026-08-03, v0.146.0 stable / 29 Jul 2026) ·
[itecsonline.com/post/how-to-codex-cli-linux](https://itecsonline.com/post/how-to-codex-cli-linux) (published 26 Oct 2025, updated 19 Jul 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Understand the two-layer safety model before running anything ✅

Codex CLI has two independent safety dials. Set both deliberately.

**Layer 1 — Sandbox** (what the agent can physically touch on your machine):

| Sandbox mode | What it allows |
|---|---|
| `read-only` | Agent can only read files; cannot write anything |
| `workspace-write` | Agent can write files inside your project folder |
| `danger-full-access` | Agent can do anything on your machine |

**Layer 2 — Approval policy** (when the agent stops to ask you first):

| Approval mode | What it does |
|---|---|
| `untrusted` | Asks before most actions |
| `on-request` | Asks when the agent itself requests permission |
| `never` | Never asks; acts immediately |
| `granular` | Lets you set different rules per category (sandbox escalation, MCP, skills) |

**Recommended starting combination:** `workspace-write` sandbox + `on-request` approval.
The agent can edit project files and run commands inside the project, but asks before
touching anything outside it or the network.

> **⚠️ WARNING: `danger-full-access` removes all OS-level restrictions.** OpenAI's own
> documentation labels this combination "No sandbox; no approvals (not recommended)" with
> an "Elevated Risk" label. Only use it inside a disposable container or virtual machine
> you don't care about — never on your main machine.

**Sources:** [learn.chatgpt.com/docs/agent-approvals-security](https://learn.chatgpt.com/docs/agent-approvals-security) (fetched 2026-08-03) ·
[codex.danielvaughan.com/2026/03/27/security-hardening-codex-cli](https://codex.danielvaughan.com/2026/03/27/security-hardening-codex-cli/) (published 27 Mar 2026, updated 3 Aug 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Keep the OS sandbox on; only bypass it inside a throwaway environment ✅

On Linux, Codex CLI's sandbox restricts filesystem, network, and process access
according to whichever sandbox mode you picked, using kernel-level isolation
(bubblewrap plus a filtering technology called seccomp, per current vendor
documentation — one independent source describes the underlying mechanism slightly
differently, as "Landlock and seccomp," and a third source reconciles the two by
explaining Codex likely uses bubblewrap where available and a different Linux-native
path otherwise; the exact plumbing on your machine is 🕒 verify live, but it doesn't
change the guidance below either way).

**Do:** Leave the sandbox on. If a workflow genuinely needs full, unfettered access, use
`--dangerously-bypass-approvals-and-sandbox` (short alias `--yolo`) **only inside a
disposable Docker container, devcontainer, or GitHub Codespace with no real credentials
mounted** — never on your day-to-day machine.

- A **Docker container** is a lightweight isolated environment on your machine that
  can't access the rest of your files.
- **GitHub Codespaces** gives you a cloud-hosted environment you can throw away
  afterward.

> **⚠️ The container or Codespace only protects you because it's disposable.** That's the
> whole point: once you bypass Codex's own sandbox with `--yolo`, the container boundary
> becomes your *only* remaining safety net — so it has to be something you don't mind
> destroying and recreating.

**Sources:** [learn.chatgpt.com/docs/agent-approvals-security](https://learn.chatgpt.com/docs/agent-approvals-security) (fetched 2026-08-03) ·
[cybedefend.com/en/blog/openai-codex-security-risks-best-practices](https://www.cybedefend.com/en/blog/openai-codex-security-risks-best-practices) (published Jun 2026) ·
[codex.danielvaughan.com/2026/03/27/security-hardening-codex-cli](https://codex.danielvaughan.com/2026/03/27/security-hardening-codex-cli/) (updated 3 Aug 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Sign in with ChatGPT for interactive use — and know your saved login file is a plaintext password by default ✅

**Do:** "Sign in with ChatGPT" (`codex login`) uses your Plus/Pro/Team/Business/Edu/
Enterprise subscription and is recommended for interactive local use. For scripted/CI
use, authenticate with an API key instead (see the headless practice below for the exact
setting). Either way, Codex saves your session locally at `~/.codex/auth.json`.

> **⚠️ `~/.codex/auth.json` is plaintext by default** — it contains an access token,
> refresh token, ID token, and account identifier, all readable as plain text. Current
> vendor documentation says outright to "treat `~/.codex/auth.json` like a password" and
> does **not** claim it's encrypted (an earlier version of this guide, from June, said it
> was encrypted — that was wrong, and has been corrected). To reduce the risk:
> - Set `cli_auth_credentials_store = "keyring"` in `config.toml` to store it in your OS
>   keyring instead of a plain file where supported. After enabling it, **confirm it
>   actually took effect** by checking that `~/.codex/auth.json` no longer contains a
>   live token — vendor docs don't say what happens if your system's keyring isn't
>   available, so don't just assume it worked.
> - Also lock down the file's permissions defensively either way:
>   `chmod 600 ~/.codex/auth.json`, so other accounts on a shared machine can't read it.
> - Never commit, paste, or share this file with anyone.
>
> **This isn't a hypothetical risk.** In June 2026, a malicious npm package (with roughly
> 27,000-29,000 weekly downloads) was caught silently stealing users' Codex refresh
> tokens — which don't expire — straight out of this file and sending them to an
> attacker. If you install random npm packages on a machine where you're logged in to
> Codex, that plaintext file is exactly what's exposed.

**Sources:** [learn.chatgpt.com/docs/auth.md](https://learn.chatgpt.com/docs/auth.md) (fetched 2026-08-03) ·
[labs.cloudsecurityalliance.org — CSA research note, AI Developer Supply Chain: OpenAI Codex Token Theft](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-developer-supply-chain-codexui-20260601/) (published 1 Jun 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Use `codex exec` for headless/CI runs 📄

**Do:**
```
codex exec "prompt" --json
```
`--json` streams a structured event per command/file-change/message — easy to feed into
`jq`. `--ephemeral` skips saving session files to disk, which you almost always want in
CI/automation. **`codex exec` defaults to a `read-only` sandbox** — pass
`--sandbox workspace-write` explicitly when the job needs to edit files.

For authentication in automation, use the dedicated `CODEX_API_KEY` environment variable
(only works with `codex exec`, distinct from a general `OPENAI_API_KEY`). For GitHub
Actions specifically, prefer the official `openai/codex-action@v1` action over
hand-rolling your own environment-variable auth — it proxies credentials instead of
exposing the raw key to the job, and its default setting removes elevated (sudo)
privileges before Codex runs.

> **⚠️ Don't set `CODEX_API_KEY` as a plain job-level environment variable when
> untrusted code (e.g. a pull request from a public fork) runs in the same step** — that
> exposure is exactly what the GitHub Action's proxy approach is designed to prevent.

**Sources:** [learn.chatgpt.com/docs/non-interactive-mode](https://learn.chatgpt.com/docs/non-interactive-mode) (fetched 2026-08-03) ·
[developersdigest.tech/blog/codex-exec-ci-headless-guide](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide) (published 10 Jun 2026, updated 28 Jun 2026) ·
[learn.chatgpt.com/docs/github-action](https://learn.chatgpt.com/docs/github-action) (fetched 2026-08-03)
**Confidence:** ✅ independently-corroborated

---

### Practice: Configure in `~/.codex/config.toml` 📄

**What is TOML?** A simple config file format. Each line is `key = "value"`; sections
use `[section-name]` headers.

**Do:**
- Personal settings: `~/.codex/config.toml`
- Per-project settings: `.codex/config.toml` (only honored for projects you've marked
  trusted)
- One-off override: `--profile <name>` or `-c key=value`

Order of precedence, highest to lowest: CLI flags/`-c` overrides → project config →
profile file → your personal config → system config → built-in defaults.

> **Reassuring detail:** project-level config **cannot** override certain machine-local
> or security settings — vendor documentation confirms this exclusion list includes
> **`sandbox_mode` and `approval_policy`**, so a compromised or untrusted project repo
> can't quietly loosen your sandbox or approval settings just by shipping its own
> `.codex/config.toml`.

**Sources:** [learn.chatgpt.com/docs/config-file/config-reference](https://learn.chatgpt.com/docs/config-file/config-reference) (fetched 2026-08-03) ·
[blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex) (updated 29 Jul 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Pick the model deliberately — the lineup changed on 9 Jul 2026 ✅

**Do:** OpenAI's current documentation recommends a new three-tier family — **Sol, Terra,
and Luna** (launched 9 Jul 2026, replacing GPT-5.5) — but notably does **not** name one
of them as "the" default; the vendor docs' own wording is: "If you don't specify a model,
the ChatGPT desktop app, Codex CLI, or IDE extension uses a recommended model." Treat
`gpt-5.6-sol` as the flagship/recommended choice for complex work, not a confirmed
official default:

| Model | Context | Pricing (input/output per million tokens) | Notes |
|-------|---------|----------------------------------------|-------|
| gpt-5.6-sol | 1.05M tokens | $5 / $30 | Flagship tier; complex coding |
| gpt-5.6-terra | 1.05M tokens | $2 / $12 (cut from $2.50/$15 on 30 Jul 2026) | Everyday work |
| gpt-5.6-luna | 1.05M tokens | $0.20 / $1.20 (cut from $1/$6 on 30 Jul 2026) | Fast/cheap, repeatable tasks |
| gpt-5.4 / gpt-5.4-mini | — | — | Retiring from Codex (ChatGPT sign-in) on 31 Aug 2026 🕒; still usable via API key |

🕒 **verify live — this pricing cut is confirmed, not a typo:** launch-day coverage
(9 Jul 2026) reported higher Terra/Luna prices than the table above shows. That's because
**OpenAI cut Luna pricing by 80% and Terra by 20% on 30 Jul 2026** — reported the same day
by CNBC, Axios, and VentureBeat, with matching before/after numbers. The model lineup
moves faster than most blog posts get updated, so trust the vendor's models page over
older guides for this specific fact.

**Sources:** [learn.chatgpt.com/docs/models](https://learn.chatgpt.com/docs/models) (fetched 2026-08-03) ·
[developers.openai.com/api/docs/models](https://developers.openai.com/api/docs/models) (fetched 2026-08-03) ·
[marktechpost.com — OpenAI Releases GPT-5.6](https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/) (published 9 Jul 2026) ·
[testingcatalog.com — OpenAI launches GPT-5.6 Sol, Terra, and Luna](https://www.testingcatalog.com/openai-launches-gpt-5-6-sol-terra-and-luna-on-apps-and-api/) (published 9 Jul 2026) ·
[cnbc.com — OpenAI price cut GPT](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html) (30 Jul 2026) ·
venturebeat.com — AI price wars: OpenAI cuts GPT-5.6 Luna prices by 80% (30 Jul 2026; consistently returns 429 on re-fetch, unlinked per policy — corroborated by the CNBC link above) ·
axios.com — OpenAI cuts prices on GPT Terra, Luna (30 Jul 2026; consistently returns 403 bot-detection on re-fetch, unlinked per policy — corroborated by the CNBC link above)
**Confidence:** ✅ independently-corroborated (lineup, context window, and the 30 Jul
price cut are all multiply-sourced); which model is "the default" is explicitly not
documented by the vendor — described here as a recommended tier, not a confirmed default

---

## Part 3 — Google Gemini CLI

> ## ⚠️ READ THIS FIRST — a big change happened 18 Jun 2026
>
> On **18 June 2026, Google switched off the free "Sign in with Google" login** and the
> consumer Pro/Ultra tiers for Gemini CLI, steering those users toward a separate,
> closed-source tool called **Antigravity CLI**. This is now more than six weeks in the
> past — Google's own authentication docs page, oddly, still displays the announcement
> in future tense ("Gemini CLI will be replaced by Antigravity CLI on June 18th"). **That
> banner is stale — don't trust it.** The cutoff already happened.
>
> **What this means for you:** A tutorial from even a couple of months ago will tell you
> to log in with your Google account — that no longer works for individual/free use. If
> you're setting up Gemini CLI today, you need one of: a **paid Gemini API key**, Vertex
> AI credentials, or a Code Assist organizational license.
>
> Gemini CLI itself is still open source and still works — you just need to pay or have
> the right credentials. See the auth practice below for the exact options and one
> important billing warning about the Vertex AI path.

---

### Practice: Install with Node.js 20+ via npm ✅

**Important:** Gemini CLI requires **Node.js 20.0.0 or newer**. Ubuntu's own repository
packages have historically shipped older versions on LTS releases, so check
`node --version` before relying on it.

**Do:** If you need a current Node.js on Ubuntu:
```
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs -y
```

> **⚠️ WARNING:** This command runs a remote script **as root** (`sudo -E bash`) — more
> powerful than piping a script to an unprivileged `sh`. The script can make any change
> to your system. Only run it if you trust NodeSource (a well-established, long-running
> project) — check nodesource.com yourself first if unsure.

Once you have Node 20+, install Gemini CLI:
```
npm install -g @google/gemini-cli
```
Verify with `gemini --version`; upgrade with `npm install -g @google/gemini-cli@latest`.

🕒 **verify live:** run `npm view @google/gemini-cli version` for the current release —
v0.53.1 was the current stable version at this snapshot (published 31 Jul 2026), up from
v0.49.0 in June; this project ships frequently.

**Sources:** [geminicli.com/docs/get-started/installation](https://geminicli.com/docs/get-started/installation) (fetched 03 Aug 2026) ·
[ssdnodes.com — How to Install and Use Gemini CLI on Ubuntu Linux](https://www.ssdnodes.com/blog/how-to-install-and-use-gemini-cli-on-ubuntu-linux/) (28 Apr 2026) ·
[github.com/google-gemini/gemini-cli/releases](https://github.com/google-gemini/gemini-cli/releases) (fetched 03 Aug 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Plan your authentication around who's paying — and set a budget alert if you use Vertex AI ✅

**Do:** Since 18 June 2026, the paths that still work for setting up Gemini CLI are:

1. **A paid Gemini API key** from Google AI Studio:
   `export GEMINI_API_KEY=your-key-here`
2. **Vertex AI** — using Google Cloud credentials, which requires a billing-enabled
   Google Cloud project.
3. An organization's **Gemini Code Assist Standard/Enterprise license** (Workspace/
   enterprise sign-in still works for these).

Google's own replacement for individual/free use is **Antigravity CLI** — a separate
program, installed independently of the existing `gemini` command. Several specifics
about Antigravity CLI could not be independently confirmed and should be treated as
unverified rather than relied on.

> **⚠️ WARNING — the Vertex AI path has no built-in spending cap.** If you choose option
> 2 above, **set a Google Cloud budget alert before you start**, especially if you
> haven't used Cloud billing before — a runaway automated job can generate a real bill,
> and there's nothing in Gemini CLI itself stopping it.

> **⚠️ Don't trust the tense of Google's own docs page here.** It still reads as if the
> cutoff is upcoming — it already happened. If a tutorial (including Google's own
> current page) tells you to just sign in with a personal Google account and it doesn't
> work, this transition is why.

**Caveat:** Antigravity CLI being closed-source is community pushback voiced in a
Google GitHub discussion, not a confirmed Google statement. Several users in that
discussion also report Antigravity CLI is missing features and harder to use than
Gemini CLI was — treat these as user complaints, not verified facts. Its exact free-tier
quota could not be confirmed even from Google's own current page, which only describes
it qualitatively ("meaningful quota, refreshed weekly") and explicitly says rate limits
"are not guaranteed." Treat any specific quota number you see quoted online as
unconfirmed.

**Sources:** [geminicli.com/docs/get-started/authentication](https://geminicli.com/docs/get-started/authentication/) (fetched 03 Aug 2026 — banner confirmed stale) ·
[developers.googleblog.com — An important update: transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) (19 May 2026) ·
[github.com/google-gemini/gemini-cli discussion #27274](https://github.com/google-gemini/gemini-cli/discussions/27274) (fetched 03 Aug 2026) ·
[inventivehq.com — Gemini CLI Is Being Retired on June 18](https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration) (13 Jun 2026) ·
[antigravity.google/docs/plans](https://antigravity.google/docs/plans) (fetched 2026-08-04)
**Confidence:** ✅ independently-corroborated (the 18 Jun 2026 cutoff); Antigravity CLI
specifics are unverified and lower-confidence

---

### Practice: Turn on sandboxing yourself — it is not automatic on Ubuntu ✅

**What is the Gemini CLI sandbox?** It runs your agent inside a Docker container — an
isolated environment separate from your real machine — so the agent can't damage your
files or system.

> **⚠️ WARNING: sandboxing is OFF by default.** Most beginners run Gemini CLI with no
> protection at all without realizing it. You must explicitly install a backend and turn
> it on.

**Do:** Enable it with the `-s`/`--sandbox` flag, the `GEMINI_SANDBOX` environment
variable (`true`/`docker`/`podman`/etc.), or `"sandbox": true` under `tools` in
`settings.json`. On Ubuntu the practical option is Docker or Podman:
```
sudo apt install docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```
Then log out and back in (the group change requires a new session). Once set up:
```
gemini -s "your prompt here"
```

> **⚠️ WARNING — joining the `docker` group is effectively giving yourself root.** The
> `sudo usermod -aG docker $USER` step above is a routine, commonly-recommended setup
> step — but membership in the `docker` group is a well-known way to get full
> root-equivalent access to your machine: anyone (or anything) that can run `docker` as
> you can trivially become root through a container that mounts your real filesystem.
> This matters precisely *because* this whole section is about making your machine
> safer — don't treat Docker-group membership as a free, side-effect-free path to
> sandboxing if avoiding root-equivalent access on your own account was part of the
> point.

> **One more thing that is NOT confirmed:** Google's own sandbox documentation does not
> say that `--yolo` automatically turns sandboxing on for you, even if a backend is
> already installed. **Treat `--yolo` as NOT enabling sandboxing on your behalf.** Nor is
> it documented what happens if you run `--yolo` with no sandbox backend installed at
> all — it might refuse to run, might warn and continue unsandboxed, or might silently
> proceed with zero sandbox and zero approval prompts (the worst case). Don't assume it
> fails safely — confirm your sandbox is actually active independently, regardless of
> whether you're also using `--yolo`.

**Why it matters / what goes wrong:** Nothing about running `gemini` interactively
protects your filesystem or network by default. If you're letting the agent touch a real
project, turn on Docker/Podman sandboxing first — and understand the Docker-group
tradeoff above before you do.

**Sources:** [geminicli.com/docs/cli/sandbox](https://geminicli.com/docs/cli/sandbox/) (fetched 03 Aug 2026) ·
[agent-safehouse.dev — Gemini CLI Sandbox Analysis Report](https://agent-safehouse.dev/docs/agent-investigations/gemini-cli) (12 Feb 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Know all four approval modes — `auto_edit` is not the safe middle ground it sounds like 📄

**Do:** Set with `--approval-mode` or in `settings.json`:

| Mode | Behavior |
|------|----------|
| `default` | Prompts before every file edit or shell command (start here) |
| `auto_edit` | Auto-approves file edits; still prompts for shell commands |
| `plan` | Read-only — can read files and draft a plan, cannot write or run anything until you say so |
| `yolo` | Auto-approves everything, including shell commands; no confirmation at all |

**Why it matters:** `auto_edit` still lets the agent run any shell command it wants
without asking — only file writes are gated, so it's a partial safety net, not a full
one. `yolo` removes the confirmation step entirely: if the agent misreads a file or
picks up an instruction hidden in some untrusted input, nothing catches it before it
runs. Restrict `--yolo` to disposable VMs/containers or fully-trusted, non-public CI —
never a machine with real data or credentials, and never a CI job that reacts to public
issues or pull requests.

**Caveat:** A separate write-up (dated over a year before this snapshot, before `plan`
mode existed) independently describes `yolo` mode as removing "one of the biggest
built-in safeguards" and warns it can wipe out code, run destructive commands, and
eliminate the audit trail a team relies on — that risk framing is worth taking
seriously even though the source predates the current mode list.

**Sources:** [geminicli.com/docs/reference/configuration](https://geminicli.com/docs/reference/configuration/) (fetched 03 Aug 2026) ·
[devsolus.com — Gemini CLI Permissions: Is YOLO Mode Safe?](https://devsolus.com/gemini-cli-permissions-is-yolo-mode-safe/) (10 Jul 2025)
**Confidence:** 📄 vendor-documented (mode table); ✅ independently-corroborated (risk
framing, from an older source)

---

### Practice: Script with `gemini -p` and check exit codes, not just the output 📄

**Do:**
```
gemini -p "Review this diff" --output-format json | jq '.response'
```
(`jq` isn't installed by default: `sudo apt install jq`.) Documented exit codes: `0`
success, `1` general/API error, `42` input error (bad prompt/arguments), `53` turn-limit
exceeded — check these in scripts rather than assuming success just because you got some
output back.

**Why it matters:** A script that only checks "did I get output" can silently treat a
truncated or error response as a success. Checking the exit code catches a turn-limit
cutoff (`53`) and bad input (`42`) separately from a hard failure (`1`).

**Sources:** [geminicli.com/docs/cli/headless](https://geminicli.com/docs/cli/headless/) (fetched 03 Aug 2026)
**Confidence:** 📄 vendor-documented

---

### Practice: Know which `settings.json` wins — and never copy-paste `"trust": true` for an MCP server you don't control 📄

**Do:** Settings load from multiple locations, layered lowest to highest priority:
1. Built-in defaults
2. `/etc/gemini-cli/system-defaults.json`
3. `~/.gemini/settings.json` — your personal settings (start here)
4. `.gemini/settings.json` in your project — team-shared settings
5. `/etc/gemini-cli/settings.json` — system-wide policy
6. Environment variables
7. CLI flags — always wins

Put personal preferences in `~/.gemini/settings.json`, project settings in
`.gemini/settings.json`. Check what context the agent has loaded with `/memory show`
(refresh with `/memory refresh`).

> **⚠️ WARNING:** Google's own MCP-server setup example includes `"trust": true` in the
> config. This silently disables *all* tool-approval confirmations for that server — the
> default is `false`. Only set it for a server you wrote and run yourself; never
> copy-paste it for a third-party MCP server.

**Sources:** [geminicli.com/docs/reference/configuration](https://geminicli.com/docs/reference/configuration/) (fetched 03 Aug 2026) ·
[github.com/google-gemini/gemini-cli — docs/tools/mcp-server.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md) (fetched 03 Aug 2026)
**Confidence:** 📄 vendor-documented

---

### Practice: Verify model availability and quotas before building a workflow 📄

🕒 **verify live:** This whole area is fast-moving. At this snapshot, Gemini CLI defaults
to Gemini 2.5 Flash for simple prompts and Gemini 2.5 Pro for complex ones; Gemini 3 is
opt-in, not the default. Quotas depend on which of the auth paths from the earlier
practice you're using:

| Auth path | Daily limit |
|---|---|
| Gemini Code Assist (individual, free) | 1,000 requests/user/day |
| Google AI Pro | 1,500 requests/user/day |
| Google AI Ultra | 2,000 requests/user/day |
| Gemini API key (free) | 250 requests/user/day |
| Gemini API key (pay-as-you-go) | Varies — token-based billing, no fixed daily cap |
| Vertex AI Express Mode | Varies — no fixed number published |
| Code Assist Standard (Workspace) | 1,500 requests/user/day |
| Code Assist Enterprise | 2,000 requests/user/day |

Remember: per the earlier authentication practice, the free-tier rows in this table
(Code Assist individual, and personal-account rows) stopped being reachable for new
free/Pro/Ultra personal-account sign-ups on 18 June 2026 — this table describes what
each *auth path* is entitled to, not which paths are open to a brand-new free user.

**Caveat:** One source (dated 28 Mar 2026, updated through 10 Jul 2026) states that
Gemini 3 Pro specifically went paid-only on 25 March 2026 — Google's own quota and
Gemini-3 pages don't mention that specific date. Treat that particular claim as
single-source and verify live rather than independently confirmed. Everything in this
practice is subject to change without notice — re-check the official quota page
yourself before building any automated workflow around a specific model or limit.

**Sources:** [geminicli.com/docs/resources/quota-and-pricing](https://geminicli.com/docs/resources/quota-and-pricing/) (fetched 03 Aug 2026) ·
[geminicli.com/docs/get-started/gemini-3](https://geminicli.com/docs/get-started/gemini-3/) (last updated 10 Apr 2026) ·
[codemyspec.com — Gemini CLI Pricing & Free Tier 2026](https://codemyspec.com/blog/gemini-cli-review-2026) (28 Mar 2026, updated 10 Jul 2026)
**Confidence:** 📄 vendor-documented (quota table, model-routing defaults); the "Gemini 3
Pro paid-only since 25 Mar 2026" date specifically is single-source / 🕒 verify live

---

## Held pending fixes (not yet fully closed)

- **A complete, copy-paste-ready nftables starter file for a bare Ubuntu host** — a real,
  dated example now exists (Part 0, Practice 4), but it's written for a
  container-sandbox setup and still needs you to substitute your own proxy address and
  decide between IP-pinning and a domain-aware proxy. ⚠ #318 (advanced, not closed).
- **Whether Ubuntu 26.04 LTS turns on the stricter AppArmor bwrap profile by default** —
  no official source confirms this either way yet; if you're on 26.04, run the `sysctl`
  check in Part 0, Practice 3 yourself rather than assuming.
- **Antigravity CLI specifics** — whether it's Go-built, its exact install steps, and
  whether it accepts a Gemini API key as an alternative login are all unconfirmed as of
  this snapshot.
- **Claude Code hooks: what happens when two hooks disagree** — only "hooks run in
  parallel, with identical ones automatically de-duplicated" is confirmed; no documented
  rule exists yet for what happens when different hooks return conflicting decisions on
  the same event.

---

## CHANGELOG

1. Re-leveled from the 2026-08-03 technical entry (itself a refresh of the 2026-06-29
   snapshot); facts, commands, and source URLs are unchanged — 0 new facts or URLs
   introduced in this pass.
2. All 34 practices from the technical entry kept (7 in Part 0 — foundations; 13 in
   Part 1 — Claude Code; 7 in Part 2 — Codex CLI; 7 in Part 3 — Gemini CLI) — matching
   the prior beginner snapshot's decision to cover all three ecosystems side by side
   rather than picking one. The nftables practice (Part 0) is again marked clearly as
   advanced, with beginners pointed to the sandbox alternative instead — kept in full
   because its warnings are safety-critical, not because beginners are expected to
   attempt it first.
3. All six safety-critical facts flagged for this pass survive and are made more
   explicit for a novice reader: Docker-group root-equivalence (full warning lives in
   the Gemini CLI sandboxing practice), the nftables SSH-lockout risk with a concrete
   self-reverting-timer mitigation, the Claude Code sandbox's default non-protection of
   `~/.aws/credentials`/`~/.ssh/`, the `--yolo` "disposable-only" rule (Codex CLI and
   Gemini CLI both), Codex's `~/.codex/auth.json` plaintext-by-default status plus the
   real June 2026 supply-chain attack that targeted it, and the billing-trap pair
   (Claude Code API-key-vs-subscription precedence, and Gemini CLI's uncapped Vertex AI
   path) — also summarized up front in "A word before you start."
4. Jargon expanded on first use throughout: systemd, worktree, sandbox, token, MCP
   server, TOML, Docker, context window, journald, `.env`, API key, domain fronting,
   TLS termination.
5. "Why it matters / what goes wrong" framing added or strengthened for each practice
   with concrete failure modes (unexpected charges, silent stall, credential leak,
   lockout, file corruption).
6. All ⚠️ WARNING blocks retained verbatim in substance and kept in their original
   positions relative to the practice they belong to; none softened or dropped.
7. Lead recommendation kept from the prior beginner snapshot: start with Claude Code
   (Part 1) if choosing one tool, because it has the most beginner-oriented
   documentation.
8. All source links and Confidence labels copied verbatim from the 2026-08-03 technical
   entry; no URLs added, dropped, or rewritten. Deep technical asides in the technical
   entry (e.g. fine-grained Ubuntu 24.04/25.04/26.04 AppArmor-default differences, the
   Landlock-vs-bubblewrap kernel-primitive debate) were compressed for readability but
   not removed where they affect a beginner's actual steps; their full source lists were
   kept intact regardless.
