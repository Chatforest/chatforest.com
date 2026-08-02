---
title: "Gemini CLI Security Fundamentals — Beginner Guide (as of 01 Aug 2026)"
date: 2026-08-01
snapshot_date: 2026-08-01
topic: gemini-cli-security-fundamentals
track: beginner
audience: "people new to AI"
description: "A plain-language guide for beginners to Gemini CLI's safety settings: what each approval mode really does, why 'auto-approve everything' (--yolo) is dangerous — especially for CI bots — why sandboxing isn't on by default, and the real CVE-2026-12537 incident that shows what goes wrong when these are misused, as of 01 Aug 2026."
content_type: "Best Practice"
categories: ["Gemini CLI", "AI Agent Security"]
tags: ["gemini-cli", "sandboxing", "yolo-mode", "checkpointing", "workspace-trust", "cve"]
last_refreshed: 2026-08-01
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-08-01"
grading_result: "0 fabrications after correction; 5 KILL + 10 FIX + 8 FLAG applied across the 3-draft Gemini CLI batch (this entry: 3 KILL, 6 FIX applied); 2 gaps tracked as project-33 issues (mg_api unavailable this run — tracked in WORKLOG)"
---

<!-- This file lands at content/ai/<track>/<topic>/<snapshot-date>/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->


# Gemini CLI Security Fundamentals — Beginner Guide (as of 01 Aug 2026)

> **Grading note.** A dated snapshot — accurate as of **01 Aug 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.
> This is the beginner-track rewrite of that same graded technical entry. The facts, sources, and
> warnings below are unchanged — only the language and organization changed to fit readers who
> are new to AI tools and to the command line ("terminal" — the text-only window where you type
> commands instead of clicking icons).

**Prerequisite:** Gemini CLI is Google's free, open-source AI coding assistant that you run from
your terminal. Before you can use any of the safety settings below, you need it installed. Install
it by running `npm install -g @google/gemini-cli` in your terminal. That command uses `npm`, a
tool for installing software packages that comes bundled with [Node.js](https://nodejs.org/) — so
you need Node.js installed first. Once it's installed, you can check which version you have any
time with `gemini --version`, and upgrade to the newest version with
`npm install -g @google/gemini-cli@latest`. This entry assumes Gemini CLI is already installed and
that you're now deciding which safety settings to turn on.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

**Where settings live:** most practices below ask you to edit a file called `settings.json`. There
are two copies you might edit: a project-level one at `<project>/.gemini/settings.json` (inside
the folder you're working in), and a user-level one at `~/.gemini/settings.json` (in your home
folder, applies everywhere). If the file doesn't exist yet, create it yourself — a plain text file
whose entire starting content is just `{}` — then add settings inside those braces, for example
`{"security": {"folderTrust": {"enabled": true}}}`. Separately, commands written as
`/settings set ...` or `/permissions` are **slash commands** — you type these while you're already
inside a running `gemini` session (i.e., after you've launched `gemini` and it's sitting there
waiting for your next message), not in your regular terminal prompt.

---

## Practice: Know exactly what each approval mode does before you pick one — `plan` is the SAFEST mode, not a middle option
**Do:** Gemini CLI has four modes that control how much the AI can do without asking you first,
and their names can be misleading — don't guess based on the name alone:
- `default` — the AI asks you "yes/no" before every single action: before it edits a file, and
  before it runs any command in your terminal. This is the closest thing to a "look before every
  step" experience.
- `auto_edit` — the AI edits files (writes new files, replaces content) without asking, but still
  asks before running any terminal command.
- `plan` — despite sounding like a semi-autonomous "plans and does" mode, this is actually the
  **safest** one: it's read-only. The AI can read your files and draft a plan, but it cannot write
  files or run terminal commands while you're in this mode. When you're ready to act on the plan,
  it explicitly asks you to choose "Yes, automatically accept edits" (switches you into
  auto-approve for the rest of the session) or "Yes, manually accept edits" (keeps asking you
  before each step). Plan mode itself never silently runs anything on its own.
- `yolo` (started with the `--yolo` flag or `--approval-mode=yolo`) — the AI does everything
  without asking, including running any terminal command, with no confirmation step at all. See
  the next practice — this mode is genuinely dangerous outside very specific situations.

To set your default mode, type this while inside a running `gemini` session (not your regular
terminal prompt):

```
/settings set general.defaultApprovalMode <mode>
```

replacing `<mode>` with `default`, `auto_edit`, or `plan`. You can also add
`general.defaultApprovalMode` directly to your `settings.json` file. `yolo` is the one exception —
you can't set it as a default in `settings.json`; you have to start it with the `--yolo` flag or
trigger it as a slash command each time.

**Why (beginner):** Beginners get this wrong in two common ways. First, they assume `plan` means
"the AI plans AND acts" — it doesn't; it's the safest, read-only mode, and nothing happens until
you explicitly say so. Second, they assume `auto_edit` is a safe halfway step because it still
"asks about the risky stuff" — but the risky stuff it still asks about is only terminal commands
that are separate from file writes; file edits themselves go through with zero confirmation, and a
terminal command can delete files, install software, or send your data somewhere else without
ever touching a source file the AI wrote. If you want the AI to check with you before every single
action, use `default`.

**Caveat / contested:** Google's own documentation is a little inconsistent here: the
configuration reference page documents only three modes tied to command-line flags (`default`,
`auto_edit`, `yolo`); `plan` mode is documented on a separate page with its own description
("enforces strict safety policies to prevent accidental changes," "a read-only environment for
architecting robust solutions before implementation"). If you want to double-check plan mode's
behavior, read that specific page — the configuration reference page alone won't tell you about
it.
**Sources:** [geminicli.com/docs/reference/configuration/](https://geminicli.com/docs/reference/configuration/) (fetched 01 Aug 2026) · [github.com/google-gemini/gemini-cli — docs/cli/plan-mode.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/plan-mode.md) (fetched 01 Aug 2026)
**Confidence:** vendor-documented

---

## Practice: Never use `--yolo` for a bot that reacts to the public internet — including your CI pipeline
**Do:** `--yolo` (also `--approval-mode=yolo`, or pressing Ctrl+Y while inside a session) turns off
every confirmation prompt. The AI runs terminal commands immediately, with no "are you sure?" step
— ever. Independent reviewers describe this as removing "one of the biggest built-in safeguards"
the tool has.

⚠️ WARNING — think of YOLO mode like removing both your seatbelt AND your brakes at once: only
ever use it in a throwaway virtual machine or disposable container that holds no real data, no
credentials, and no access to anything you actually care about. Never use it on your everyday
machine, and never on anything with production access.

⚠️ WARNING — this specifically includes CI/CD pipelines (automated jobs that run by themselves,
for example whenever someone opens a GitHub issue or pull request). "It's just a bot reading
issues" does **not** make that input trustworthy — anyone on the public internet can type text
into an issue, and if your bot runs in YOLO mode, that stranger's text can turn into a command
your bot actually executes. A public-issue-triage bot running in YOLO mode is exactly the setup
that caused the real security incident described later in this entry (CVE-2026-12537), which
Google's own team rated at the maximum possible severity score. Do not run `--yolo` in any CI job
that reacts to public issues, pull requests, or webhooks — even if you believe you've limited
which commands it's allowed to run (see the caveat below: those limits were bypassed too, before
the fix).

If you're on a shared or work machine, don't rely on everyone individually remembering to avoid
`--yolo`. Google documents a way for a team to disable YOLO mode centrally so it can't be turned
on by mistake — if that applies to you, ask whoever manages your machines about it.

**Why (beginner):** This is the single most common way people lose files or damage a system with
an AI command-line tool: they turn on "approve everything automatically" to stop the
interruptions, then the AI runs a command it misread — from a file, from a compromised dependency,
or, for a bot, from a public issue or pull request someone else wrote. There is no confirmation
step to catch it before it runs. For an individual, that can mean lost files. For the real CI
incident below, it meant a stranger with no login or special access could get commands executed on
someone else's automation and potentially steal secrets.

**Caveat / contested:** ⚠️ WARNING — YOLO mode does turn on sandboxing automatically (see the next
practice), which shrinks the damage somewhat but does **not** make it "safe." A real vulnerability
(see the CVE practice below) showed that even YOLO's own list of "commands it's allowed to run"
could be silently bypassed in CI before the fix — so even a team that believed it had safely
scoped YOLO mode down had, in fact, not.
**Sources:** [geminicli.com/docs/reference/configuration/](https://geminicli.com/docs/reference/configuration/) (fetched 01 Aug 2026) · [devsolus.com — Gemini CLI Permissions: Is YOLO Mode Safe?](https://devsolus.com/gemini-cli-permissions-is-yolo-mode-safe/) (10 Jul 2025) · [penligent.ai — Gemini CLI RCE, Workspace Trust and the CI/CD Agent Attack Surface](https://www.penligent.ai/hackinglabs/gemini-cli-rce-workspace-trust-and-the-ci-cd-agent-attack-surface/) (28 Apr 2026)
**Confidence:** independently-corroborated

---

## Practice: Sandboxing is off by default — turn it on with a complete, runnable command
**Do:** When you just type `gemini` and start chatting normally, Gemini CLI does **not** isolate
the commands it runs or the files it touches from the rest of your real machine. (The one
exception: sandboxing turns on automatically if you use `--yolo` — but see the previous practice
for why you should avoid `--yolo` regardless.)

To turn sandboxing on, run this complete command in your terminal:

```
gemini --sandbox
```

What that does depends on your operating system:
- **macOS:** uses a built-in feature called Seatbelt (`sandbox-exec`) — nothing extra to install.
- **Linux or other platforms:** uses a Docker or Podman container. **You must already have Docker
  or Podman installed and running on your machine first** — Gemini CLI does not install a
  container tool for you. If you don't have one yet, install and start Docker before running the
  command above.

You can also turn sandboxing on permanently instead of typing the flag every time, by adding
`"sandbox": true` to your `settings.json` file, or by setting the `GEMINI_SANDBOX` environment
variable.

Not all sandboxing is equally strong. From weakest to strongest:
1. macOS's default Seatbelt profile (called `permissive-open`) — keeps file writes confined to
   your project folder, but still allows broad file reading and network access.
2. Docker/Podman containers — stronger isolation, and works the same way on any platform.
3. gVisor (Linux-only, called `runsc`) — Google describes this as the strongest isolation
   available, running containers inside a user-space kernel — but it is **not** turned on
   automatically by `--sandbox`; you have to configure it yourself.

There's also a separate, smaller setting, `security.toolSandboxing` (off by default), that
isolates one tool call at a time rather than your whole `gemini` session — don't confuse it with
the `--sandbox` flag above; they're different things.

**Why (beginner):** People often assume "it's a coding AI tool from Google, surely it's already
sandboxed" — it is not, in the normal case of just running `gemini`. If you're going to let the AI
run terminal commands against files that matter to you, turn on at least the basic sandbox shown
above before you start. Don't rely on the "are you sure?" confirmation prompts alone to protect
your files.

**Caveat / contested:** ⚠️ WARNING — even with sandboxing on, macOS's default profile still allows
network access and broad file reading, so it will **not** stop a malicious download command or a
sandbox-escape bug — the default profile only reliably confines file *writes* to your project
folder. For real network isolation you need a stricter profile (the docs call these
`*-closed`/`*-proxied`) or a container-based sandbox. An independent technical review (Feb 2026)
also found the sandbox doesn't always catch credentials with unusual names (its built-in
protection looks for common patterns like "TOKEN" or "SECRET") from leaking through commands the
AI spawns, and that its web-fetch tool can still reach any public web address even though it's
blocked from reaching private/internal addresses — so don't treat "sandbox = fully contained" as a
given. As of this snapshot (01 Aug 2026), the default macOS profile's behavior described above is
confirmed unchanged. A separate, stricter deny-by-default macOS sandbox mode also exists if you
want more protection than the default profile gives you.
**Sources:** [github.com/google-gemini/gemini-cli — docs/cli/sandbox.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/sandbox.md) (fetched 01 Aug 2026) · [geminicli.com/docs/cli/sandbox/](https://geminicli.com/docs/cli/sandbox/) (fetched 01 Aug 2026, confirms default profile unchanged) · [agent-safehouse.dev — Gemini CLI Sandbox Analysis Report](https://agent-safehouse.dev/docs/agent-investigations/gemini-cli) (12 Feb 2026, v0.30.0-nightly)
**Confidence:** independently-corroborated

---

## Practice: Google's own docs disagree about whether folder-trust is on by default — check for yourself, or just turn it on
**Do:** Whenever you open a new folder in `gemini`, this feature (`security.folderTrust.enabled`)
can show you a one-time approval screen before it loads that folder's own settings — listing
exactly what that folder would activate, such as MCP servers (plug-ins that give the AI new
tools), custom commands, hooks, and skills — before it reads that folder's `.gemini/settings.json`
or `.env` files.

⚠️ Here's the catch: Google's own documentation contradicts itself about whether this is on or off
out of the box. One official page says it's "disabled by default." Another official page (the
settings reference table) lists the default as `true` (on). Don't trust either page blindly by
itself — check for yourself: open an unfamiliar folder in `gemini` and see whether you actually get
a trust prompt. Or, to be safe no matter which one is true for your installed version, explicitly
turn it on yourself by adding this to your user-level `settings.json` file:

```
{"security": {"folderTrust": {"enabled": true}}}
```

Later, you can review or change past trust decisions by typing `/permissions` while inside a
running `gemini` session (not your regular terminal). Your choices get saved in a file called
`~/.gemini/trustedFolders.json`.

**Why (beginner):** A folder's settings file isn't just cosmetic preferences — it can define
plug-ins and environment variables that run code or send your data somewhere else the moment you
open that folder in `gemini`. Because Google's own two documentation pages disagree about the
default, don't assume either one is right for your version — check it yourself, or just turn the
protection on so you're not guessing.

**Caveat / contested:** This one-time, per-folder trust prompt is a **different** mechanism from
the CI/automation bug described in the next practice — that bug automatically trusted folders in
headless/automated ("CI") mode regardless of this setting, so turning this setting on does not, by
itself, protect a CI pipeline. For CI, you need the patched version described next.
**Sources:** [github.com/google-gemini/gemini-cli — docs/cli/trusted-folders.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/trusted-folders.md) ("disabled by default"; fetched 01 Aug 2026) · [geminicli.com/docs/reference/configuration/](https://geminicli.com/docs/reference/configuration/) (`security.folderTrust.enabled` default listed as `true` — contradicts the above; fetched 01 Aug 2026)
**Confidence:** contested (Google's own docs disagree on the default)

---

## Practice: Update Gemini CLI now, and treat any automated/CI use as high-risk — CVE-2026-12537
**Do:** First, check what version you have installed:

```
gemini --version
```

In April 2026, Google fixed a maximum-severity security bug affecting Gemini CLI (versions before
0.39.1 / 0.40.0-preview.3) and the related `google-github-actions/run-gemini-cli` GitHub Action
(versions before 0.1.22). It's tracked as **GHSA-wpqr-6v78-jr5g**, and was later also assigned
**CVE-2026-12537** (the CVE number was added 24 Jun 2026 — earlier write-ups only mention the GHSA
ID because the CVE didn't exist yet; NVD and CIRCL both confirm these describe the same
underlying bug).

What went wrong, in plain terms:
1. When Gemini CLI ran in "headless" mode — meaning unattended, like inside a CI/automation
   pipeline — it **automatically trusted** whatever folder it was working in and loaded that
   folder's config/`.env` files without any review at all. This is the opposite of the interactive
   folder-trust behavior described in the practice above. Because this happened *before* any
   sandbox even started, an attacker who could get their own text into a public GitHub issue or
   pull request (using a trick called prompt injection — hiding instructions inside normal-looking
   text) could get their own commands run on the CI machine — and sandbox settings did nothing to
   stop it, because execution happened before the sandbox initialized.
2. Separately, `--yolo` mode was supposed to respect a fine-grained list of "commands the AI is
   allowed to run" set in `settings.json` — but it ignored that list. A team that believed it had
   safely restricted what YOLO mode could do in CI had, in fact, not.

Update now if you haven't already — the fix has been out since April 2026, well before this
snapshot, so you should already be on a patched version, but confirm and fix it if not:

```
npm install -g @google/gemini-cli@latest
```

🕒 verify live — confirm your version is at or above the patched versions listed above; current
released versions are well past that floor as of this writing.

If you use Gemini CLI inside any CI/automation pipeline specifically: don't rely on default trust
— set trust explicitly yourself; strip out any credentials the job doesn't strictly need (for
example, GitHub Actions' checkout step has a `persist-credentials: false` option); only let the
bot act for people with an established relationship to the repository, not any random public
account; and don't give an agent job a token with write access if it processes untrusted public
input.

**Why (beginner):** If you connect Gemini CLI to something like a GitHub Action that automatically
responds to new issues, an anonymous stranger filing an issue could — on an unpatched, unprotected
setup — get your automation to run their commands and potentially steal secrets (API keys,
tokens) stored on that machine, with no login or special access needed. "It's just a bot that
reads issues" is not a safe assumption for anything automated.

**Caveat / contested:** 🕒 Security researchers scored this bug differently depending on the
system: Google's own team rated it the maximum possible score (CVSS 4.0 = 10.0, "CRITICAL"); NIST's
independent scoring rated the same bug lower (CVSS 3.1 = 7.8, "HIGH" — NIST's scoring assumes an
attacker needs local rather than pure network access). Don't get hung up on which score is
"right" — the actionable fact is the patched version numbers above, not either score. Separately,
this April bug is not the whole story: in July 2026 (about a week before this snapshot), a
security firm called Pillar Security disclosed a *new* problem — a way to escape sandboxing via
the Docker socket, since fixed — plus two more issues (a macOS Seatbelt bypass, and a `.vscode`
task-config bypass affecting Google's separate "Antigravity" tool's "Secure Mode") that Google
classified as lower severity and **chose not to patch**, judging them hard to actually exploit
(they require social engineering or a specific trusted-repo prompt-injection setup). 🕒 verify live
whether that decision has changed.
**Sources:** [The Hacker News — Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html) (30 Apr 2026) · [CSO Online — Max-severity RCE flaw found in Google Gemini CLI](https://www.csoonline.com/article/4165470/max-severity-rce-flaw-found-in-google-gemini-cli.html) (30 Apr 2026) · [SecurityWeek — Gemini CLI Vulnerability Could Have Led to Code Execution, Supply Chain Attack](https://www.securityweek.com/gemini-cli-vulnerability-could-have-led-to-code-execution-supply-chain-attack/) (7 May 2026) · [Novee Security — A CVSS 10.0 in Gemini CLI: How Agentic Workflows Are Reshaping Supply Chain Risk](https://novee.security/blog/google-gemini-cli-rce-vulnerability-cvss-10-critical-security-advisory/) (29 Apr 2026) · [Pillar Security — My Agentic Trust Issues](https://www.pillar.security/blog/my-agentic-trust-issues-from-prompt-injection-to-supply-chain-compromise-on-gemini-cli) (5 May 2026) · [penligent.ai — Gemini CLI RCE, Workspace Trust and the CI/CD Agent Attack Surface](https://www.penligent.ai/hackinglabs/gemini-cli-rce-workspace-trust-and-the-ci-cd-agent-attack-surface/) (28 Apr 2026) · [NVD — CVE-2026-12537](https://nvd.nist.gov/vuln/detail/CVE-2026-12537) (CVSS scoring dispute + CVE↔GHSA link; fetched 01 Aug 2026) · [GitHub Advisory Database — GHSA-wpqr-6v78-jr5g](https://github.com/advisories/GHSA-wpqr-6v78-jr5g) (fetched 01 Aug 2026) · [Pillar Security — The Week of Sandbox Escapes](https://www.pillar.security/blog/the-week-of-sandbox-escapes) (Jul 2026) · [Pillar Security — One Docker Socket to Rule Them All](https://www.pillar.security/blog/one-docker-socket-to-rule-them-all-escaping-codex-cursor-and-gemini-clis-sandboxes) (Jul 2026) · [BleepingComputer — Cursor, Codex, Gemini CLI, Antigravity hit by sandbox escapes](https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/) (Jul 2026)
**Confidence:** independently-corroborated

---

## Practice: Turn on checkpointing before letting the AI edit real files — it's your undo button, but only for file edits
**Do:** Checkpointing is **off by default**. Turn it on by adding this to your `settings.json`
file:

```
{"general": {"checkpointing": {"enabled": true}}}
```

(There used to be a `--checkpointing` flag for this, but it was removed in version 0.11.0 — use
the `settings.json` method above instead.)

Once it's on: every time you approve a file-editing action (the AI writing a new file or replacing
content in an existing one — the `write_file` or `replace` tools), Gemini CLI automatically saves a
snapshot — a Git commit in a hidden backup location on your own machine (under your home folder,
in `~/.gemini/history/<project_hash>`), plus a saved copy of the conversation at that point. To
undo, type `/restore` while inside your `gemini` session (not your regular terminal) to see a list
of saved checkpoints and roll a file — and the conversation — back to that point. The original
action that made the change gets re-proposed to you, so you can redo it, edit it, or skip it.

**Why (beginner):** This is your undo button for changes the AI makes to your files — turn it on
before your first real session, not after the AI has already overwritten something you wanted to
keep. It runs entirely on your own machine (nothing gets uploaded anywhere), and it won't
interfere with your project's own separate Git history if it has one.

**Caveat / contested:** ⚠ Google's own documentation only describes checkpoints as triggered by
file-editing actions (`write_file`, `replace`). It does **not** say whether running a terminal
command through the AI (which could delete files, download something, or install software)
creates a checkpoint or can be undone with `/restore`. Assume it can **not** — treat any
terminal-command side effects as not covered by this undo feature unless you've confirmed
otherwise. This gap is still undocumented either way as of a live re-check on 01 Aug 2026, so
treat this as an unverified thin spot rather than assuming coverage.
**Sources:** [github.com/google-gemini/gemini-cli — docs/cli/checkpointing.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/checkpointing.md) (GitHub docs, last commit 10 Apr 2026)
**Confidence:** thin <!-- single vendor source; the shell-command coverage gap specifically is unverified, not independently corroborated -->

---

## Still being checked (not fully confirmed yet)
- Whether running a terminal command (not just a file edit) through the AI creates or is covered
  by a checkpoint snapshot — official docs still don't say as of a live re-check on 01 Aug 2026.
  ⚠ #TBD
- Whether Google's decision not to patch the macOS Seatbelt denylist bypass / `.vscode`
  task-config bypass (disclosed Jul 2026) still stands — 🕒 verify live before relying on it. ⚠ #TBD

## CHANGELOG (grading → this entry)
1. Re-leveled from the 01 Aug 2026 technical (best-practices track) entry for readers new to AI
   tools and the command line; facts, sources, and warnings unchanged.
2. Dropped the "lock YOLO mode off at the system-config level" practice (system-wide settings
   paths across Linux/Windows/macOS, aimed at team/fleet admins) as too advanced for an individual
   beginner audience; its sources were removed along with it — no sources were orphaned.
3. Rewrote the `--yolo` guidance to state twice, explicitly, that CI/automation bots reacting to
   public issues, pull requests, or webhooks are never a safe use of `--yolo` — pointing directly
   at the CVE-2026-12537 practice as the real-world consequence, so this can't be misread as "safe
   for my CI bot."
4. Kept every ⚠️ WARNING from the technical entry; none softened, reworded away, or dropped.
5. Kept `gemini --version` and `npm install -g @google/gemini-cli@latest` wherever the technical
   entry names them — in the top-of-entry prerequisite note and again in the CVE/patch practice.
6. Kept the complete, runnable `gemini --sandbox` example and its OS-specific prerequisite
   (Docker/Podman must already be installed and running on Linux) verbatim from the technical
   entry.
7. Clarified, everywhere they appear, that `/settings set ...`, `/restore`, and `/permissions` are
   typed inside a running `gemini` session, not the shell/regular terminal prompt.
8. Kept the `settings.json` location/creation note near the top of the entry, reused by every
   practice that edits that file, so beginners aren't hand-assembling JSON from scratch four
   times.
9. Expanded jargon on first use (terminal, npm, MCP server, CI/CD) with plain-language definitions
   already implied by the technical entry's own facts; no new facts, practices, or URLs were
   introduced beyond these definitions.
