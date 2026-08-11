---
title: "Running Coding Agents in CI/CD — Beginner's Guide (as of 10 Aug 2026)"
date: 2026-08-10
snapshot_date: 2026-08-10
topic: running-coding-agents-in-cicd
track: beginner
audience: "people new to AI"
description: "A plain-language walkthrough for first-timers on running Claude Code, Codex CLI, or Gemini CLI unattended in a CI/CD pipeline: what CI/CD even is, least-privilege credentials, human approval gates, the dangers of skipping sandbox/approval checks (including a CVSS 10.0 Gemini CLI bug), keeping secrets out of logs, and stopping a runaway agent from running up your bill — as of 10 Aug 2026."
content_type: "Best Practice"
categories: ["CI/CD", "Claude Code", "Codex CLI", "Gemini CLI"]
tags: ["ci-cd", "github-actions", "headless", "automation", "claude-code", "codex-cli", "gemini-cli", "security", "prompt-injection", "beginner"]
last_refreshed: 2026-08-10
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-08-10 (technical entry); re-leveled for the beginner track by The Translator, 2026-08-12"
grading_result: "Re-leveled from the 10 Aug 2026 technical entry (0 fabrications after correction): no new facts, claims, or sources added or changed. Same practices, reordered to lead with cross-provider fundamentals and a worked 'safe skeleton' workflow; per-tool sections condensed by merging closely related practices (Claude Code 11→8 headings, Codex CLI 10→8, Gemini CLI 10→8, with one niche Gemini practice dropped as too advanced for a first pipeline). All 8 ⚠️ WARNINGS and every 🕒 verify-live flag kept."
---

<!-- This file lands at content/ai/beginner/running-coding-agents-in-cicd/2026-08-10/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a
     NEW <snapshot-date> dir. "Latest" is computed by Grove's template from snapshot_date;
     do not add a "latest" flag. This is the beginner-track re-leveling of the same-dated
     best-practices/running-coding-agents-in-cicd/2026-08-10 technical entry — same facts,
     plainer language, shorter per-tool sections. -->

# Running Coding Agents in CI/CD — A Beginner's Guide (as of 10 Aug 2026)

> **Grading note.** This is the beginner version of a dated technical snapshot — accurate as of
> **10 Aug 2026**. The technical entry it's based on was researched by four pupils (one per AI
> tool, plus a cross-provider pass), fact-checked line-by-line by a Skeptic panelist who re-fetched
> every source, reviewed for staleness by a Timekeeper panelist, and reviewed for novice-safety by
> a Beginner panelist — ending at **0 fabrications after correction**. This guide does not add any
> new facts, commands, or sources of its own. It only simplifies the language, shortens the
> per-tool sections, and reorders things so the most useful, most concrete material (the shared
> rules and a worked example workflow) comes first.

## Before you start: what is CI/CD, anyway?

**CI/CD** stands for **Continuous Integration / Continuous Deployment** — most people just call it
"a pipeline." It's a robot that watches your code repository and automatically runs a set of steps
(build it, test it, maybe deploy it) every time something happens: you push code, you open a pull
request, or a clock ticks. You write those steps once, as a config file, and the pipeline runs them
with nobody clicking anything. This guide's examples use **GitHub Actions**, a popular CI/CD system
where you add a `.yml` file under `.github/workflows/` in your repo, and GitHub runs it on a fresh,
disposable machine (a "runner") whenever your trigger fires.

Why does that matter for an AI coding agent? Normally, a tool like Claude Code, Codex CLI, or
Gemini CLI is interactive: you type a request, it thinks, it asks "should I run this command?", and
a human clicks yes or no. A CI/CD pipeline has no human sitting there to click yes — so before an
agent can run inside one, it has to run in **headless mode**: one command that starts, does the
job, prints a result, and exits, with no back-and-forth. Every practice below is about doing that
*safely*, because "safely" is not the default. An unattended agent with too much access, no
spending limit, or no human checkpoint before it can push code is a real, concrete danger — not
just an inconvenience — and this guide exists to walk through exactly why, with the same
receipts (sources) as the technical entry it's built from.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

## Terms used in this guide
- **Headless / non-interactive mode** — running an agent CLI as a single command that starts, does
  its job, prints a result, and exits, instead of an interactive chat window waiting for a human to
  click through prompts. CI runners have no human to click "yes."
- **MCP (Model Context Protocol)** — an open standard for giving a model new tools or data sources.
  An **MCP server** is a small plug-in program that provides those tools, and it can carry its own
  credentials.
- **OIDC (OpenID Connect)** — lets a CI job trade a short-lived, workflow-scoped identity token for
  real cloud credentials, instead of storing a long-lived static key as a secret.
- **Ephemeral runner** — a CI machine created fresh for one job and destroyed right after (GitHub's
  own hosted runners work this way). A **self-hosted runner** is a persistent machine you manage
  yourself, which can build up leftover state and risk between jobs if it isn't reset.
- **`/proc` (procfs)** — a Linux virtual filesystem that exposes every running process's memory and
  environment variables as readable files. Anyone with `sudo` on the same machine can read another
  process's environment through it, sandboxed or not.
- **`GITHUB_TOKEN`** — a token GitHub auto-generates for each workflow run. A **GitHub App** is a
  separate, independently-installed identity with its own scoped permissions that a workflow can
  use instead, decoupled from any one person's account.

---

## Part 1 — The rules that apply no matter which AI tool you use

Read this part first. It's the same whether you're using Claude Code, Codex CLI, or Gemini CLI —
and it's the most concrete, most actionable material in this guide.

### Practice: Give the agent's CI credentials the least access possible
**Do:** Never hand an agent's CI job the default, all-repo `GITHUB_TOKEN` or a broad personal
access token. Add an explicit `permissions:` block to your workflow, starting from `contents: read`
and adding only what the job truly needs — for example `pull-requests: write` if it must leave a
comment. The moment you list *any* permission, GitHub automatically sets everything you didn't list
to `none` — so a short, partial list is already safe by construction, not "half-protected." Where
you can, prefer short-lived credentials (an OIDC token instead of a long-lived static key), and give
the agent its own dedicated machine identity/API key rather than a person's own login, so you can
shut it off independently of that person.
**Why (beginner):** An AI agent running in CI is unattended, and it can be tricked — via "prompt
injection," covered below — into doing something you never intended. If its token can only read
code and open a pull request, the worst case is a bad PR you close. If its token can also push to
`main`, delete branches, or reach your cloud account, the worst case is much bigger, and it happens
with nobody watching in real time.
**Caveat / contested:** GitHub Actions already makes `GITHUB_TOKEN` read-only when a workflow is
triggered by a pull request from a fork — but that protection does not apply to branches inside
your own repo, or to secrets you've explicitly exposed to the job. You still have to apply
least-privilege scoping yourself; it isn't automatic just because you're using GitHub.
**Sources:** [GitHub Docs — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) (accessed 10 Aug 2026) · [GitHub Docs — Workflow syntax for GitHub Actions ("If you specify the access for any of these permissions, all of those that are not specified are set to `none`")](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) (accessed 12 Aug 2026) · [GitGuardian — GitHub Actions Security Cheat Sheet](https://blog.gitguardian.com/github-actions-security-cheat-sheet/) (11 Apr 2025) · [Cloud Security Alliance — Research Note: Prompt Injection in AI-Powered GitHub Actions](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-github-actions-security-20260503-csa-st/) (3 May 2026)
**Confidence:** independently-corroborated

---

### Practice: Require a human to approve anything that merges, deploys, or destroys
**Do:** Turn on branch protection with required reviewers on any branch the agent can push to. Use
GitHub Environments (or your CI system's equivalent — a protected, manual-approval environment) on
any job that deploys, force-pushes, or otherwise carries big risk. Don't let the agent's own
"self-review," or an auto-generated approval, count as satisfying that requirement.
**Why (beginner):** Agents are good at writing plausible-looking code and bad at knowing when
they're wrong. A human review step is the backstop that catches a subtly broken database migration,
an accidentally-committed credential, or a prompt-injection-driven action before it reaches
production or rewrites your history — even if the same agent is trusted to work fully on its own
for lower-stakes tasks, like opening a draft PR.
**Caveat / contested:** GitHub's own docs say that if a repo requires PR approvals, *your own*
approval of a PR that GitHub Copilot's coding agent authored "won't count toward the required
number" — that's a rule aimed at the human who prompted the agent, not a promise about what kind of
review the agent's own bot account can leave. It's a real example of a vendor building a review
gate in by default, just not necessarily the exact mechanism you'd assume — check what your own
agent product actually restricts rather than treating this as a universal guarantee.
**Sources:** [GitHub Docs — Reviewing a pull request created by Copilot](https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/reviewing-a-pull-request-created-by-copilot) (accessed 10 Aug 2026) · [GitHub Docs — Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) (accessed 10 Aug 2026) · [OWASP Cheat Sheet Series — AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) (accessed 10 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: ⚠️ Don't auto-run agent jobs on pushed changes without a manual gate — and be careful with `pull_request_target`
**Do:** Keep GitHub's default behavior: workflows do **not** auto-run on changes an automated
coding agent pushes to a PR branch, until a maintainer clicks "Approve and run workflows." Avoid
triggering agent jobs on the `pull_request_target` event (which runs with your base repo's write
permissions and secrets, against *untrusted* PR content) unless you have a specific, reviewed
reason. Prefer `pull_request` (read-only, no secrets) instead, when you need to react to PRs from
forks.
**Why (beginner):** `pull_request_target` plus an AI agent that reads PR content is a known attack
pattern: an attacker opens a PR whose title, description, or diff contains hidden instructions; the
agent reads that content as part of its job; and because the workflow run has write access and
secrets, the agent can be manipulated into leaking credentials or merging malicious code — with no
human ever approving anything.
**Caveat / contested:** This is an active, evolving danger, not a solved problem. Security
researchers point to misconfigured `pull_request_target` combined with an overprivileged
`GITHUB_TOKEN` as one of the biggest amplifiers of this risk. A separate, real 2026 vulnerability
(covered in Part 2's Claude Code section) shows a related but different failure — an overly
permissive allowlist, not `pull_request_target` itself. Treat this practice as risk-reduction, not
elimination.
**Sources:** [Cloud Security Alliance — Research Note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-github-actions-security-20260503-csa-st/) (3 May 2026) · [GitHub Docs — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) (accessed 10 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: Keep the agent read-only, and route any write action through a separate, checked step
**Do:** Give the job that actually runs the LLM read-only repo permissions (`contents: read`, no
write scopes) and no direct access to the credential that would push, comment, or merge. Have the
agent write out a small, structured "here's what I want to do" file instead — for example
`{"action": "open_pr", "branch": "fix/123", "diff_ref": "artifact://patch.diff", "title": "..."}`
— and let a **separate** job, with its own narrower permissions, read that file and actually carry
out the action. This is sometimes called a "safe outputs" pattern, and it's exactly what the
worked example below does.
**Why (beginner):** If the same process reading untrusted PR or issue text is also the process
holding the token that can write to your repo, a successful prompt injection has a direct path to
real damage. Splitting "the agent decides what to do" from "a separate, limited step actually does
it" means a manipulated agent can, at worst, propose a bad action — it can't execute one unchecked.
**Caveat / contested:** This is GitHub's own architecture for its "GitHub Agentic Workflows"
project (which can run Claude Code, Codex, Gemini CLI, or Copilot). It's a genuinely useful pattern
to copy, but it's one vendor's design, not yet an industry standard — most teams wiring up their
own agent by hand will need to build this two-job split themselves.
**Sources:** [GitHub — gh-aw permissions reference](https://github.github.io/gh-aw/reference/permissions/) (accessed 10 Aug 2026) · [GitHub — gh-aw self-hosted runners reference](https://github.github.io/gh-aw/reference/self-hosted-runners/) (accessed 10 Aug 2026)
**Confidence:** vendor-documented

---

### Practice: Keep secrets out of the agent's transcript, CI logs, and PR/issue comments
**Do:** Pass secrets only into the specific step that needs them — never as job-wide or
workflow-wide environment variables. Rely on your CI system's built-in log masking (GitHub Actions
automatically masks registered secret values) rather than assuming an AI-generated transcript will
redact anything on its own. Run a secret-scanning tool (GitHub secret scanning/push protection,
Gitleaks, TruffleHog, or similar) as a required check before an agent-authored PR can merge, and
don't give the agent broad filesystem access that would let it accidentally quote a `.env` file
back into a public PR comment.
**Why (beginner):** Agents narrate their work — they'll often paste file contents, command output,
or error messages into their own transcript, and CI systems often post that transcript (or a
summary of it) as a public PR comment or a build log anyone with repo read access can see. A
credential that would never normally appear in a code diff can end up in a comment simply because
the agent "explained" what it did.
**Caveat / contested:** Log masking only works for secrets your CI system already knows about; a
credential the agent discovers dynamically (say, by reading a config file, not from a registered
secret) won't be auto-redacted. Scanning tools catch leaks *after the fact* in many pipelines, not
before — the strongest control is making sure the agent never had the secret in its context in the
first place.
**Sources:** [GitHub Docs — Secret leakage risks](https://docs.github.com/en/code-security/concepts/secret-security/secret-leakage-risks) (accessed 10 Aug 2026) · [GitGuardian — GitHub Actions Security Cheat Sheet](https://blog.gitguardian.com/github-actions-security-cheat-sheet/) (11 Apr 2025) · [GitGuardian — The GhostAction Campaign: 3,325 Secrets Stolen Through Compromised GitHub Workflows](https://blog.gitguardian.com/ghostaction-campaign-3-325-secrets-stolen/) (Sep 2025, real-world example of the blast radius of a workflow that exfiltrates secrets, not AI-specific)
**Confidence:** independently-corroborated

---

### Practice: ⚠️ Put a hard ceiling on how long and how much an agent job can run
**Do:** Set `timeout-minutes` on every agent job — GitHub Actions' default job timeout is **360
minutes (6 hours)** 🕒 verify live, far too long for most agent tasks, so don't rely on the
platform default. Use a `concurrency` group with `cancel-in-progress: true` so a re-triggered or
duplicate run doesn't stack up alongside the old one. Set a spend/rate limit at the API-key level
with your model provider, so a looping agent hits a provider-side wall even if your own job-level
controls fail. Use both a per-run cap (catches one runaway task) and an aggregate budget cap
(catches many small runs adding up).
**Why (beginner):** Agent loops fail differently than normal CI jobs — a stuck agent may keep
calling tools or retrying a failing step at machine speed instead of just erroring out, and every
call can cost real money. Without a timeout and a spend ceiling, one misbehaving trigger (say, a job
that re-fires on every push to a busy branch) can generate a genuinely surprising bill before anyone
notices.
**Caveat / contested:** Exact provider spend-limit mechanics are plan-specific — treat any number
here as 🕒 verify live. Anthropic's own Spend Limits API, for example, is documented as available
"to Claude Enterprise organizations only," not to a plain Console API key used from a CI job — check
which limit type actually applies to your CI credential before assuming it's capped. Equivalent
OpenAI- and Google-side mechanics for a specific CI API key weren't confirmed this run (see "Held
pending fixes" below).
**Sources:** [GitHub Docs — Concurrency](https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency) (accessed 10 Aug 2026) · [Anthropic — Spend Limits API ("available to Claude Enterprise organizations only")](https://platform.claude.com/docs/en/manage-claude/spend-limits-api) (accessed 10 Aug 2026)
**Confidence:** independently-corroborated on the GitHub-side timeout/concurrency mechanics; thin
on "a provider-side spend cap protects a specific CI job"

---

### Practice: Design agent-driven CI actions to be safe to run twice by accident
**Do:** Base branch names, PR titles, and "does this already exist" checks on something fixed and
tied to the triggering event (the commit SHA, or the issue number) — not a timestamp or a randomly
generated ID. Have the job check whether an equivalent branch/PR/comment already exists before
creating a new one. Use a `concurrency` group keyed on that same fixed value, so a retried or
re-triggered run cancels or replaces the stale one instead of running alongside it.
**Why (beginner):** CI jobs get retried — by a flaky runner, a redelivered webhook, or a human
clicking "re-run." If the agent's job creates a brand-new branch or PR every time it runs, a retry
silently produces duplicate PRs, duplicate comments, or duplicate commits instead of failing
loudly — and nobody notices until the repo is cluttered with near-identical open PRs.
**Caveat / contested:** This is a general rule of good bot/automation design (the same lesson tools
like Dependabot and Renovate learned long ago), not something unique to AI agents. It's worth
knowing specifically for AI-driven pipelines because a misbehaving agent is more likely to trigger
it than a simple script would be — but be aware that AI-agent-specific sourcing for this particular
lesson is thin; treat the underlying rule as solid, well-established practice.
**Sources:** [GitHub Docs — Concurrency](https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency) (accessed 10 Aug 2026)
**Confidence:** thin

---

### Practice: Treat sandboxing and monitoring as a backup layer, not your only control
**Do:** Treat network/runtime monitoring as a complementary layer on top of least-privilege tokens,
human approval gates, and read-only-by-default permissions — never as a replacement for them.
GitHub's own Copilot coding agent ships a firewall, but its own docs warn it is "not a
comprehensive security solution": it only covers processes the agent starts through its command-line
tool, it does **not** cover MCP servers or custom setup-step processes, and it only applies inside
that one specific sandboxed environment. Complementary tools like Harden-Runner add visibility into
what a job's processes actually do — its default mode *monitors and logs* outbound network calls
rather than blocking them, which is still useful for spotting an agent that tried to reach somewhere
it shouldn't.
**Why (beginner):** Even with careful permission scoping, an agent that's been manipulated by
instructions hidden in an issue or PR body could still try to send out whatever it *can* reach —
source code, environment variables, or tokens still in memory. Watching what the sandbox's
processes actually talk to gives you a chance to catch that, even when a permission boundary has a
gap you didn't know about.
**Caveat / contested:** Don't treat "we turned on a firewall" or "we turned on monitoring" as a
solved problem — a sophisticated attack can still slip past a process-level firewall, and
monitoring-only tools don't block anything in real time; they only give you an after-the-fact
signal to alert on. A hard, blocking network allowlist enforced outside the agent's own reach would
be stronger than either of these, but no specific, ready-to-use way to do that on a disposable
GitHub-hosted runner was found this run (see "Held pending fixes").
**Sources:** [GitHub Docs — Customizing or disabling the firewall for GitHub Copilot cloud agent](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-firewall) (accessed 10 Aug 2026) · [StepSecurity — Securing GitHub Copilot in GitHub Actions with Harden-Runner (published 22 Jul 2025; no independently-verifiable "updated" date found)](https://www.stepsecurity.io/blog/securing-github-copilot-in-github-actions-with-harden-runner) · [Cloud Security Alliance — Research Note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-github-actions-security-20260503-csa-st/) (3 May 2026, recommends runner-level monitoring such as Harden-Runner as a complementary control)
**Confidence:** vendor-documented on the firewall's own documented gaps; thin on Harden-Runner as a
general recommendation (it's a monitoring tool, not a blocking control)

---

### Practice: Pin any third-party Action or tool your workflow uses to an exact version
**Do:** When an agent CI workflow depends on third-party GitHub Actions, container images, or CLI
tools, pin them to a full commit SHA (or an equivalent unchangeable identifier) rather than a
floating tag like `@v4` or `latest`.
**Why (beginner):** A tag can be moved to point at new, potentially malicious code even after
you've already reviewed and trusted it — this is exactly how several real supply-chain attacks on
GitHub Actions pipelines have happened. In a pipeline where an AI agent already has some elevated
access, a compromised dependency is an easy way for an attacker to gain much more.
**Caveat / contested:** This is longstanding, general CI/CD advice, not unique to AI agents — it's
included here because security researchers specifically call it out as a risk *multiplier* once an
AI agent with write access and secrets shares the same pipeline.
**Sources:** [GitHub Docs — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) (accessed 10 Aug 2026) · [Cloud Security Alliance — Research Note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-github-actions-security-20260503-csa-st/) (3 May 2026)
**Confidence:** independently-corroborated

---

### A worked, minimal "safe workflow" example

Every setting above is a separate rule in prose — here's how they fit together in one small,
illustrative GitHub Actions file. This isn't a vendor-published example or a drop-in file (it wasn't
tested); it's this guide's own composition, assembled from the practices above, to show the shape
of a safe pipeline rather than leaving you to guess how the pieces connect.

```yaml
name: agent-triage
on:
  pull_request:            # NOT pull_request_target — see the practice above
    types: [opened, synchronize]

concurrency:
  group: agent-triage-${{ github.event.pull_request.number }}   # safe to retry — see practice above
  cancel-in-progress: true

jobs:
  propose:                 # Job 1: read-only, runs the agent against untrusted PR content
    runs-on: ubuntu-latest
    timeout-minutes: 15     # hard ceiling — see practice above
    permissions:
      contents: read        # least privilege — see practice above; no write scopes at all
    steps:
      - uses: actions/checkout@<full-commit-sha>   # pinned, not @v4 — see practice above
      - name: Run agent (produces a proposal artifact, does not write to the repo)
        run: |
          # your chosen CLI here, e.g. `claude -p`, `codex exec`, or `gemini -p`
          # writes its proposed diff/action to ./proposal.json — never pushes/comments directly
        env:
          MODEL_API_KEY: ${{ secrets.MODEL_API_KEY }}   # scoped to this step only — see secrets practice
      - uses: actions/upload-artifact@<full-commit-sha>
        with:
          name: proposal
          path: proposal.json

  apply:                   # Job 2: separate, narrower-scoped, gated — reads the artifact, does the write
    needs: propose
    runs-on: ubuntu-latest
    environment: agent-writes   # required-reviewer gate — see human-approval-gate practice above
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/download-artifact@<full-commit-sha>
        with:
          name: proposal
      - name: Validate proposal.json, then open the PR
        run: |
          # validate shape/contents of proposal.json before acting on anything in it
```

Treat every `<full-commit-sha>` and CLI invocation above as a placeholder you fill in against the
tool-specific practices in Parts 2–4, and adapt the trigger and permissions to your own situation.

---

## Part 2 — Claude Code, the short version

Covers Anthropic's `claude` CLI run as `claude -p` (print/headless mode). Claude Code ships roughly
weekly point releases, so treat any version number below (e.g. "requires v2.1.221") as 🕒 verify
live — check it against current docs before relying on it.

### Practice: Run `claude -p`, and read the JSON result and exit code — not the plain text
**Do:** Invoke `claude -p "<prompt>"` for any scripted or CI use — it runs the same agent loop as
interactive Claude Code, prints a result, and exits, with no TTY and no interactive prompts needed.
Pipe data in via stdin (`cat log.txt | claude -p "..."`, capped at 10MB — write larger inputs to a
file and reference the path instead). For a script to act on the result reliably, add
`--output-format json` and read the `.result` (final text), `.session_id`, and `.total_cost_usd`
fields with a JSON tool like `jq`, rather than parsing the plain-text output. Claude Code exits `0`
on success and non-zero on failure (including `143` if it's killed with SIGTERM) — gate your
pipeline step on that exit code.
**Why (beginner):** CI runners have no human to click "yes" on a permission dialog, so the
interactive CLI will just hang forever — print mode is the supported way to run Claude Code
unattended. And human-readable text output changes wording between versions, which silently breaks
a script that greps for specific phrases; the JSON result and exit code are the stable contract a
CI step should depend on instead.
**Caveat / contested:** `total_cost_usd` is a **client-side estimate** and can differ from your
actual bill — don't treat it as exact accounting. No full exit-code table is published; only `0`
(success), non-zero (failure), and `143` (killed) are documented, so don't hard-code assumptions
about other specific non-zero values. If Claude Code can't read stdin at all, it warns to stderr and
continues with just the command-line prompt, rather than failing outright.
**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 10 Aug 2026) · [code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference) (fetched 10 Aug 2026) · [hidekazu-konishi.com — "Claude Code in CI/CD and Headless Automation"](https://hidekazu-konishi.com/entry/claude_code_cicd_and_headless_automation.html) by Hidekazu Konishi (first published 7 Jun 2026)
**Confidence:** vendor-documented on the `-p` flag itself; independently-corroborated on the JSON
output/exit-code behavior

---

### Practice: Add `--bare` so CI doesn't silently inherit local machine settings
**Do:** Run `claude --bare -p "..."` in pipelines. Bare mode skips auto-discovery of hooks, skills,
plugins, MCP servers, auto-memory, and `CLAUDE.md`, so you get the same result on every runner
regardless of what happens to be configured on that machine or checked into the repo. Explicitly
pass back only what you need — for example `claude --bare -p "..." --mcp-config ./ci-mcp.json
--settings ./ci-settings.json`. Bare mode also never reads OAuth credentials or the OS keychain, so
set `ANTHROPIC_API_KEY` explicitly (as a masked CI secret injected into the job's environment, not
written into the command line).
**Why (beginner):** Without `--bare`, a CI run silently inherits whatever hooks or MCP (Model
Context Protocol) servers happen to be configured on that machine or checked into the repo — which
makes runs non-reproducible and can load tools or credentials you never intended to grant the
pipeline.
**Caveat / contested:** Anthropic's own docs say `--bare` "will become the default for `-p` in a
future release" — this recommendation is expected to become the built-in default later, so the flag
itself is 🕒 verify live. This is currently sourced only to Anthropic's own docs, with no
independent corroboration found for `--bare` specifically.
**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 10 Aug 2026)
**Confidence:** thin (single vendor source)

---

### Practice: Use the official GitHub integration, and scope its permissions tightly
**Do:** Run `/install-github-app` from Claude Code locally for quick setup, or install the
[Claude GitHub App](https://github.com/apps/claude) and copy
[`examples/claude.yml`](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml)
into `.github/workflows/` for manual setup. Store credentials as a repo secret — `ANTHROPIC_API_KEY`
(a Console API key, better for an organization-wide rollout since it isn't tied to one person) or
`CLAUDE_CODE_OAUTH_TOKEN` (generated with `claude setup-token`, tied to one person's
subscription) — and reference it in the workflow's `with:` block, never inline. In the workflow's
`permissions:` block, grant only what the job needs (typically `contents: write`,
`pull-requests: write`, `issues: write`, `id-token: write` for the default GitHub App auth) —
remember that listing any permission sets everything else to `none`. `claude-code-action` itself
also rejects triggering comments from users without repo write access, via `allowed_non_write_users`
(configure this to a fixed, reviewed list of usernames or teams — **never** to a field taken
directly from the triggering event; more on why below).
**Why (beginner):** The official Action already handles trigger detection, mode switching, and
GitHub App authentication — reimplementing this by hand with raw API calls is more error-prone and
loses the built-in write-access checks. And a broad `contents: write` with no other scoping means a
prompt-injected instruction hidden in an issue or PR comment could, in principle, direct Claude to
push to any branch or read secrets the job can see — tight scopes limit the blast radius. Pair this
with Part 1's human-approval-gate practice: even a well-scoped Claude Code job should open a PR for
review, not push straight to a protected branch.
**Caveat / contested:** A real 2026 vulnerability (GHSA-63mx-j37w-gh59 / CVE-2026-44246) shows
exactly what goes wrong if you get `allowed_non_write_users` wrong: one project's workflow set it to
`${{ github.event.issue.user.login }}` — which hands the write-access gate to *any logged-in GitHub
user* who simply opens an issue, not just trusted collaborators. This is the concrete, real-world
reason the setting above says "never a field taken from the triggering event." Separately: GitHub
does **not** trigger downstream workflows on commits pushed using the default `GITHUB_TOKEN` — if
you want Claude's own commits to re-trigger CI, omit `github_token` from the action so it
authenticates as the Claude GitHub App instead, or supply a custom app token. Note that the
independent source below confirms only the general `permissions:`/`ANTHROPIC_API_KEY` pattern, not
the GitHub-App-specific mechanics.
**Sources:** [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) (fetched 10 Aug 2026) · [systemprompt.io — "Set Up Claude Code GitHub Actions for PR Review and CI"](https://systemprompt.io/guides/claude-code-github-actions) (10 Mar 2026) · [GitHub Docs — Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) (accessed 12 Aug 2026) · [GHSA-63mx-j37w-gh59 advisory](https://github.com/MIC-DKFZ/nnUNet/security/advisories/GHSA-63mx-j37w-gh59) · [Tenable — CVE-2026-44246](https://www.tenable.com/cve/CVE-2026-44246) (both fetched 11 Aug 2026)
**Confidence:** vendor-documented on the setup mechanics (the independent source corroborates only
the general permissions pattern); independently-corroborated on the CVE-2026-44246 lesson

---

### Practice: ⚠️ Never run `--dangerously-skip-permissions` on a CI runner with real credentials
**Do:** Only use `--dangerously-skip-permissions` (also called `bypassPermissions`) inside a
throwaway, isolated environment — a disposable container or VM with no path to production and
minimal, scoped credentials. Never use it on a long-lived, shared, or credential-rich CI runner. For
most CI use cases, use the narrower modes in the next practice instead. **If you don't already know
your threat model well enough to weigh the tradeoffs described below, don't use this flag in CI at
all — full stop.**
**Why (beginner):** This flag skips essentially every approval prompt, including writes to
protected paths. If the CI job's prompt was manipulated — say, by a malicious PR comment or a
poisoned dependency — there is no human checkpoint stopping Claude from running destructive commands
or leaking any secret the job's environment can reach. GitHub-hosted runners are not
network-isolated by default — GitHub's own docs state runners "have access to the public internet"
— so "it's just a CI runner" is not automatically safe.
**Caveat / contested:** On Linux/macOS, Claude Code refuses to start in this mode when running as
root/sudo — but that guardrail is **automatically skipped inside a recognized sandbox**, so don't
treat "runs as root" as a reliable backstop if your runner also happens to look like a sandbox to
Claude Code. Anthropic's own guidance is internally inconsistent here: its general Best Practices
docs say to use this mode only in a sandbox "without internet access," while a separate reference
devcontainer page recommends the flag for a container that *does* have outbound network access to an
allowlist. A community-filed bug report flagged this contradiction directly; Anthropic closed it
without a public resolution. Read this as: allowlisted network access reduces but does not eliminate
the risk of a secret being leaked, compared to a truly air-gapped sandbox.
**Sources:** [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) (fetched 10 Aug 2026) · [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 10 Aug 2026) · [github.com/anthropics/claude-code issue #19978](https://github.com/anthropics/claude-code/issues/19978) (opened 22 Jan 2026) · [GitHub Docs — Private networking with GitHub-hosted runners ("By default, GitHub-hosted runners have access to the public internet")](https://docs.github.com/en/actions/concepts/runners/private-networking) (accessed 12 Aug 2026)
**Confidence:** contested (Anthropic's own devcontainer guidance and its Best Practices guidance
disagree on what counts as "isolated enough")

---

### Practice: For routine CI tasks, use a safer allowlist mode instead
**Do:** For a normal "run tests and fix failures" or "apply lint fixes" job, use
`--permission-mode acceptEdits` (auto-accepts file edits and safe filesystem commands like `mkdir`,
`mv`, `cp`) paired with an explicit allowlist for anything else, e.g. `--allowedTools "Bash(git diff
*),Bash(git commit *),Bash(npm test)"` — add further `Bash(<pattern>)` entries for anything else the
job legitimately needs; don't leave a trailing `...` in a real config. For a fully locked-down
pipeline where you want to pre-approve every capability, use `--permission-mode dontAsk`, which
auto-denies anything not covered by your allow rules or the built-in read-only command set (`ls`,
`cat`, `git status`, etc.) — there's no interactive fallback, so an unapproved action simply fails
the step instead of hanging or silently doing something you didn't approve.
**Why (beginner):** These modes give Claude enough freedom to finish a well-scoped CI task without
handing it the blanket authority of `bypassPermissions`. If the prompt is manipulated into
requesting something outside the allowlist, the run fails loudly instead of executing it.
**Caveat / contested:** `acceptEdits` still lets other Bash commands and network requests prompt for
approval (and therefore abort, since nothing can answer that prompt in headless mode) unless
they're covered by `--allowedTools` — a run can fail simply because you under-scoped the allowlist,
which is a usability tradeoff against `bypassPermissions`'s convenience.
**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 10 Aug 2026) · [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 10 Aug 2026) · [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) — example job uses `--permission-mode acceptEdits` with a scoped `--allowedTools` list (fetched 10 Aug 2026)
**Confidence:** vendor-documented (all three sources are Anthropic-hosted docs pages, treated as one
publisher)

---

### Practice: ⚠️ Cap spend and iteration with `--max-turns` and `--max-budget-usd`
**Do:** Pass `--max-turns <N>` to bound how many agentic turns a single `-p` run can take — it exits
with an error once the limit is reached, instead of looping indefinitely — and `--max-budget-usd
<amount>` to hard-cap API spend for that run (spend from subagents counts toward the cap; once it's
hit, new subagent spawns fail and in-flight background subagents are stopped; requires Claude Code
v2.1.217 or later 🕒 verify live). Also set a workflow-level timeout as a second, independent
backstop, and use CI concurrency controls to cap parallel runs.
**Why (beginner):** An unattended agent that gets stuck in a retry loop, or is asked to do something
open-ended, can otherwise keep calling the API — and consuming GitHub Actions minutes — until
someone notices. This is exactly the kind of "left it running overnight" mistake that generates a
surprise bill.
**Caveat / contested:** Both flags cap a single invocation, not an org-wide budget; use a usage
dashboard for fleet-wide spend tracking. **Update (shipped 3 days before this snapshot):** Claude
Code v2.1.225 (2026-08-07) added org/gateway-level spend-limit support — when a Claude
Gateway–routed org hits its configured cap, the CLI surfaces a named limit, a reset time, and an
operator message. That's a separate mechanism from the per-invocation flags above (fleet-wide vs.
single run) — relevant if you're tracking spend across many CI jobs rather than one. 🕒 verify live.
**Sources:** [code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference) (fetched 10 Aug 2026) · [hidekazu-konishi.com — "Claude Code in CI/CD and Headless Automation"](https://hidekazu-konishi.com/entry/claude_code_cicd_and_headless_automation.html) by Hidekazu Konishi (first published 7 Jun 2026) · [github.com/anthropics/claude-code releases — v2.1.225](https://github.com/anthropics/claude-code/releases/tag/v2.1.225) (fetched 11 Aug 2026) · [dev.classmethod.jp — v2.1.226 update roundup](https://dev.classmethod.jp/en/articles/20260808-cc-updates-v2-1-226/) (fetched 11 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: Keep secrets out of the prompt and the transcript
**Do:** Never paste a credential into a Claude Code prompt or pipe a file containing secrets into
`claude -p` as context. Store `ANTHROPIC_API_KEY` (or cloud-provider credentials) as a masked,
protected secret in your CI provider and inject it only into the step that needs it. Where both your
CI provider and Claude Code's provider support it, authenticate via OIDC instead of a stored
long-lived key.
**Why (beginner):** A CI transcript or log is often more widely readable than the secret store
itself — other maintainers, build artifacts, sometimes public logs on open-source repos. Anything
that ends up in Claude's prompt, tool output, or transcript can leak that way, even if the
underlying secret store is locked down.
**Caveat / contested:** GitHub Actions withholds repository secrets from workflow runs triggered by
a fork's pull request by default — a real protection, but it also means a review workflow gated on
secrets simply won't run on fork PRs (a common source of "why didn't Claude review this PR"
confusion). And `pull_request_target` reintroduces secret access to fork-triggered runs (see Part
1), so use it cautiously.
**Sources:** [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) — "Protect your credentials" (fetched 10 Aug 2026) · [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) — "Never commit API keys or cloud credentials..." (fetched 10 Aug 2026) · [hidekazu-konishi.com — "Claude Code in CI/CD and Headless Automation"](https://hidekazu-konishi.com/entry/claude_code_cicd_and_headless_automation.html) by Hidekazu Konishi (first published 7 Jun 2026)
**Confidence:** independently-corroborated

---

### Practice: Pin exactly which MCP servers can load, and fail loudly if one breaks
**Do:** Pass `claude --strict-mcp-config --mcp-config ./ci-mcp.json` so Claude Code uses **only**
the MCP (Model Context Protocol) servers you name in that file, ignoring any other configuration
source. Check `ci-mcp.json` into version control and review changes to it like any other CI config.
Then, with `--output-format stream-json`, read the `system/init` event's `plugin_errors` and
`mcp_server_errors` arrays (both are non-empty only when something failed to load) and fail the job
if either is non-empty — don't assume an empty tool list means "nothing was configured."
**Why (beginner):** In interactive use, a project's `.mcp.json` normally requires you to approve it
before its servers connect — but that approval prompt **cannot appear** in headless mode, so
project-scoped MCP servers load automatically without asking. A CI job that doesn't pin its MCP
config could silently start a server (and its tools and credentials) that nobody explicitly approved
for that pipeline. Separately, Claude Code is deliberately fault-tolerant about a misconfigured MCP
entry — it skips it and continues cleanly rather than crashing. That's the right default for
interactive use, but in CI it means a broken integration can go unnoticed for a long time unless you
check for it explicitly.
**Caveat / contested:** All the sources for this practice are Anthropic's own docs, with no
independent (non-Anthropic) corroboration found. An open bug report says `--strict-mcp-config` does
**not** override a `disabledMcpServers` list already set on the runner — so the "fully explicit tool
surface" this flag promises can have an exception if that file carries stale disables. 🕒 verify
live — check the issue's status before relying on `--strict-mcp-config` alone. Reading
`mcp_server_errors` requires Claude Code v2.1.219+ 🕒 verify live; on older versions you'd only see
a stderr warning, which most CI runners capture and hide rather than surface.
**Sources:** [code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference) (fetched 10 Aug 2026) · [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 10 Aug 2026) · [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) — "Trust verification is disabled when running non-interactively with the -p flag" (fetched 10 Aug 2026) · [github.com/anthropics/claude-code issue #14490](https://github.com/anthropics/claude-code/issues/14490) (fetched 11 Aug 2026) · [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 10 Aug 2026)
**Confidence:** thin (single publisher — all Anthropic docs — despite several pages)

---

## Part 3 — Codex CLI, the short version

Covers OpenAI's `codex exec` (non-interactive mode). Codex CLI ships roughly weekly point releases,
so treat any version number below as 🕒 verify live.

### Practice: Use `codex exec`, and check its exit code and JSON output
**Do:** Invoke `codex exec "<task>"` — not the interactive `codex` TUI — for scripts, cron jobs, and
CI steps. It runs one task to completion, streams progress to **stderr**, and prints only the final
agent message to **stdout**, so it composes cleanly with `grep`/`jq`/shell pipelines. Check `$?`
after it runs (it exits non-zero on failure, such as the agent erroring out or a required MCP server
failing to start) and branch your pipeline logic on that. Add `--json` for a newline-delimited JSON
event stream you can parse in detail, or `-o/--output-last-message <path>` to just capture the final
message.
**Why (beginner):** Automation only works if failure is machine-detectable, and if the output your
pipeline reads is stable across versions. `codex exec` is built specifically for scripting — the
interactive TUI is not; and parsing an LLM's free-form prose is fragile, since wording changes will
silently break a script, while structured JSON and the exit code give you a stable contract.
**Caveat / contested:** `--full-auto` still works but is a deprecated compatibility flag that prints
a warning — official docs say to prefer the explicit `--sandbox workspace-write` flag in new
scripts. The exact taxonomy of non-zero exit codes (partial failure vs. total failure vs. tool
error) isn't comprehensively documented anywhere found this run — treat the exit code as a binary
success/fail signal only. Vendor docs also mention `--output-schema <path>` (validates Codex's final
answer against a JSON Schema you provide), but this specific flag was not independently verified
this run — treat it as vendor-only/unchecked, unlike `--json` itself, which is confirmed
independently.
**Sources:** [learn.chatgpt.com/docs/non-interactive-mode](https://learn.chatgpt.com/docs/non-interactive-mode) (fetched 10 Aug 2026, vendor) · [developersdigest.tech/blog/codex-exec-ci-headless-guide](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide) (published 10 Jun 2026, updated 28 Jun 2026) · [developertoolkit.ai/en/codex/advanced-techniques/non-interactive/](https://developertoolkit.ai/en/codex/advanced-techniques/non-interactive/) (published 8 Feb 2026, updated 6 Aug 2026) · [learn.chatgpt.com/docs/developer-commands?surface=cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) (fetched 10 Aug 2026, vendor)
**Confidence:** independently-corroborated on `codex exec` itself and `--json`; thin (single source)
on the exact exit-code behavior and on `--output-schema`

---

### Practice: Trust Codex's safe default (read-only), and widen access only on purpose
**Do:** Know that `codex exec` defaults to the `read-only` sandbox — no writes anywhere, including
`/tmp` — with the approval policy governing everything else. Only add `--sandbox workspace-write`
when the task genuinely needs to edit files, and treat `--sandbox danger-full-access` as
inappropriate for CI unless the runner itself is a disposable, fully isolated container or VM.
**Why (beginner):** Unlike some agent CLIs, Codex's safe default is actually the *most* restrictive
mode — that protects you if a script forgets to pass sandbox flags at all. But it's easy to
accidentally widen access, for example by copy-pasting `--sandbox workspace-write` or
`danger-full-access` from an interactive-use tutorial into a CI job, and lose that protection without
realizing it.
**Caveat / contested:** Vendor docs state this plainly on the page governing non-interactive use; a
separate vendor page on approvals/security phrases its guidance as a recommendation to use `codex
exec --sandbox workspace-write` for a specific use case, not as a contradiction of the documented
default.
**Sources:** [learn.chatgpt.com/docs/non-interactive-mode](https://learn.chatgpt.com/docs/non-interactive-mode) (fetched 10 Aug 2026, vendor) · [learn.chatgpt.com/docs/developer-commands?surface=cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) (fetched 10 Aug 2026, vendor) · [developersdigest.tech/blog/codex-exec-ci-headless-guide](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide) (published 10 Jun 2026, updated 28 Jun 2026) · [developertoolkit.ai/en/codex/advanced-techniques/non-interactive/](https://developertoolkit.ai/en/codex/advanced-techniques/non-interactive/) (published 8 Feb 2026, updated 6 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: ⚠️ Never use `--yolo` on a shared or GitHub-hosted CI runner
**Do:** Reserve `--dangerously-bypass-approvals-and-sandbox` (aka `--yolo`), which disables *both*
sandboxing and approval prompts, for a runner you already treat as disposable and single-purpose —
an ephemeral container or VM with no other secrets or shared state. For ordinary CI, use `--sandbox
workspace-write` plus an explicit `--ask-for-approval never` so the task can run unattended without
needing a human to click "approve," while file/network access stays bounded.
**Why (beginner):** This flag removes the two safety nets that stop a misbehaving or
prompt-injected agent from running arbitrary destructive commands with full filesystem and network
access. In CI, nobody is watching the run in real time, so there's no human backstop either — a bad
outcome here can mean deleted files, leaked secrets, or unexpected outbound network calls, all
unattended.
**Caveat / contested:** Official docs label it verbatim "Elevated Risk... not recommended," note it
works "with all `--sandbox` modes," and give **no guidance blessing it for headless/unattended runs
specifically** — treat it as a documented-but-discouraged option, not a vendor-endorsed headless
workaround. It's still not forbidden outright, so a genuinely disposable container or VM is the
mitigation if you use it at all.
**Sources:** [learn.chatgpt.com/docs/agent-approvals-security](https://learn.chatgpt.com/docs/agent-approvals-security) (fetched 10 Aug 2026, vendor) · [vincentschmalbach.com — "How Codex CLI Flags Actually Work (Full-Auto, Sandbox, and Bypass)"](https://www.vincentschmalbach.com/how-codex-cli-flags-actually-work-full-auto-sandbox-and-bypass/) (published 15 Jan 2026)
**Confidence:** independently-corroborated

---

### Practice: Use the official `openai/codex-action`, and rely on its `drop-sudo` protection
**Do:** For GitHub Actions specifically, use `openai/codex-action@v1` instead of manually installing
Codex and wiring up your own credentials file or raw `OPENAI_API_KEY` env var. Configure it with a
`permission-profile` (`:read-only` and `:workspace` are confirmed built-in; requires Codex CLI
≥0.138.0) or the older `sandbox` input (not both — supplying both fails before Codex even starts),
give it a `prompt`, and pin `codex-version` so the CLI doesn't silently drift under your workflow.
Explicitly rely on `safety-strategy: drop-sudo` (the action's default, which revokes `sudo`
membership on Linux/macOS before Codex runs) or `safety-strategy: unprivileged-user` — see the next
practice for exactly why this matters even in a read-only sandbox.
**Why (beginner):** The Action installs the CLI, keeps your API key server-side in a local proxy
instead of a plain environment variable inside the job, and applies a documented privilege-reduction
strategy by default — doing all of this by hand is easy to get wrong.
**Caveat / contested:** Permission profiles are explicitly labeled "beta" and don't combine with the
legacy `sandbox` settings. 🕒 verify live: the `0.138.0` minimum version and available profile names
will move as the Action evolves — a third `:danger-full-access` profile value is reported in some
documentation but wasn't independently confirmed this run, so verify it exists on your pinned
version before relying on it.
**Sources:** [learn.chatgpt.com/docs/github-action](https://learn.chatgpt.com/docs/github-action) (fetched 10 Aug 2026, vendor) · [github.com/openai/codex-action](https://github.com/openai/codex-action) (fetched 10 Aug 2026, vendor) · [smartscope.blog/en/generative-ai/chatgpt/codex-cli-github-actions](https://smartscope.blog/en/generative-ai/chatgpt/codex-cli-github-actions/) (published 10 Mar 2026)
**Confidence:** vendor-documented

---

### Practice: ⚠️ Don't assume "read-only sandbox" alone protects your API key
**Do:** In `openai/codex-action`, explicitly rely on `safety-strategy: drop-sudo` or
`safety-strategy: unprivileged-user` as described above. Don't assume "read-only sandbox + no
network" is sufficient on its own.
**Why (beginner):** GitHub-hosted runners ship with **passwordless `sudo` by default**. Linux
exposes running processes' environment variables as files under `/proc` (procfs) — anyone with
`sudo` can read them, even from a process they didn't start. So even in a `read-only` sandbox with
network disabled, a process with `sudo` can read another process's memory and environment through
`/proc`, which can expose your `OPENAI_API_KEY` even though the sandbox never let Codex "write"
anything. The read-only sandbox restricts what Codex's own shell commands can *do*, not what a
privileged process can *read* — this is exactly the risk a beginner would assume the earlier "safe
default" practice already covers, and it doesn't.
**Caveat / contested:** This exact mechanism (procfs plus passwordless sudo defeating read-only
sandboxing) is documented by OpenAI's own `codex-action` security doc; a second, independent
publisher describing this specific technique wasn't found this run, so it's labeled
vendor-documented rather than independently-corroborated. Treat it as credible — it's the vendor
disclosing a limitation of its own product — but single-sourced.
**Sources:** [github.com/openai/codex-action/blob/main/docs/security.md](https://github.com/openai/codex-action/blob/main/docs/security.md) (fetched 10 Aug 2026, vendor)
**Confidence:** vendor-documented (single publisher; flagged as a real risk despite thin sourcing
because it's a vendor disclosure about its own defaults)

---

### Practice: Never put your API key in a job-wide environment variable
**Do:** Avoid setting `OPENAI_API_KEY` or `CODEX_API_KEY` at the job or workflow level in any
pipeline that also runs test scripts, third-party Actions, or dependency install scripts — those
processes run in the same job and can read that env var too. Prefer the official Action's proxy (the
key never touches the CLI process's environment directly), or if you must set a key for a bare
`codex exec` call, inject it inline for a single invocation only:
`CODEX_API_KEY=<key> codex exec "task"`.
**Why (beginner):** In CI, "your" job often executes code you didn't write — test suites, npm
postinstall scripts, third-party Actions. If the API key sits in a job-wide environment variable,
all of that code can read and leak it, not just Codex.
**Caveat / contested:** Also treat `~/.codex/auth.json` (used for ChatGPT-account login instead of
an API key) as sensitive as a password — official docs explicitly say don't use that login-based
auth flow for public or open-source repos at all.
**Sources:** [learn.chatgpt.com/docs/non-interactive-mode](https://learn.chatgpt.com/docs/non-interactive-mode) (fetched 10 Aug 2026, vendor) · [eastondev.com/blog/en/posts/ai/20260726-codex-security-sandbox-permission-secrets](https://eastondev.com/blog/en/posts/ai/20260726-codex-security-sandbox-permission-secrets/) (published 26 Jul 2026)
**Confidence:** independently-corroborated

---

### Practice: 🕒 Codex CLI has no built-in per-run spend cap — set one yourself on the OpenAI platform
**Do:** Before scheduling any recurring or unattended Codex job (a nightly cron, a run on every PR,
etc.), set a usage/spend limit in the OpenAI platform dashboard for the API key or project you're
using, and pick a cheaper model for high-frequency, low-stakes tasks (log triage, PR summaries)
versus a stronger model only for actual fix-generation work.
**Why (beginner):** A CI job that runs on every commit or every PR can multiply an otherwise-small
per-call cost very quickly, and a runaway loop — say, a retry-on-failure step that keeps calling
`codex exec` — has had no CLI-side circuit breaker; your only protection has been the
platform-level usage cap.
**Caveat / contested:** OpenAI's live config reference now documents an experimental
`[features.rollout_budget]` config block, but its own implementation notes explicitly state it
"only defines and validates configuration and does not track usage, inject reminders, or stop a
rollout" — so as of this snapshot it's scaffolding, **not an enforced cap**. The headline advice
above ("don't assume a setting protects you") remains true today, but this is an actively-developing
area — 🕒 verify live whether this feature has gained real enforcement before relying on the
platform-dashboard workaround being your only option.
**Sources:** [developersdigest.tech/blog/codex-exec-ci-headless-guide](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide) (published 10 Jun 2026, updated 28 Jun 2026) · [learn.chatgpt.com/docs/config-file/config-reference](https://learn.chatgpt.com/docs/config-file/config-reference) (fetched 11 Aug 2026) · [github.com/openai/codex pull #28746](https://github.com/openai/codex/pull/28746), [#28494](https://github.com/openai/codex/pull/28494), [#29423](https://github.com/openai/codex/pull/29423) (fetched 11 Aug 2026)
**Confidence:** thin on the specific absence-of-enforcement claim

---

### Practice: Require a human to review the diff before merge, even in "unattended" mode
**Do:** Use unattended Codex runs (autofix bots, PR review bots) to *propose* changes — open a PR,
post a review comment — rather than push directly to a protected branch. OpenAI's own reference
autofix workflow explicitly ends with a human checking the diff before merging ("Check to see if
everything looks good and then merge it").
**Why (beginner):** "Non-interactive" describes how Codex runs, not how much you should trust its
output unsupervised. An agent acting on CI failures, logs, or PR content can be steered by
instructions hidden in that content — a human review step is your last check before a bad or
manipulated change lands in your codebase.
**Caveat / contested:** Sourcing here is vendor-documented (the official cookbook example),
reinforced by one independent source describing the same general "review the diff, run tests,
prepare a rollback plan" pattern as a second line of defense beyond the permission boundary.
**Sources:** [developers.openai.com/cookbook/examples/codex/autofix-github-actions](https://developers.openai.com/cookbook/examples/codex/autofix-github-actions) (fetched 10 Aug 2026, vendor) · [eastondev.com/blog/en/posts/ai/20260726-codex-security-sandbox-permission-secrets](https://eastondev.com/blog/en/posts/ai/20260726-codex-security-sandbox-permission-secrets/) (published 26 Jul 2026)
**Confidence:** independently-corroborated

---

## Part 4 — Gemini CLI, the short version

Covers Google's `gemini` CLI in headless mode. This part covers **CI/CD and non-interactive
automation only** — general Gemini CLI sandboxing, authentication basics, and MCP/extension
security have their own RingS entries and aren't repeated here.

### Practice: Use headless mode (`-p`), and check the exit code and JSON output
**Do:** Invoke `gemini -p "your prompt"` (or pipe input via stdin, e.g. `git diff | gemini -p "write
a commit message"`). Headless mode triggers automatically in any non-TTY environment, or explicitly
with `-p`/`--prompt`. Never run the plain interactive `gemini` REPL inside a CI job — it expects a
terminal and won't behave predictably in a runner. For scripts that need to parse the result, pass
`--output-format json` (a single JSON object with a `response` field plus metadata) or
`--output-format stream-json` for a full event stream. Check the process exit code rather than
assuming success from non-empty output: per vendor docs, `0` = success, `1` = general error/API
failure, `42` = input error (bad prompt/args), `53` = turn limit exceeded.
**Why (beginner):** CI runners have no human to click "approve" or read a chat window — headless
mode is the difference between a script that finishes and exits, and a job that hangs until it times
out (and still gets billed for runner minutes). Grepping raw text output is also fragile, since the
model's wording changes run to run; structured JSON plus an exit-code check lets a pipeline reliably
decide "did this succeed" without guessing from prose.
**Caveat / contested:** Exact flag names haven't always been stable across versions — one GitHub
issue from Sept 2025 showed `--output-format` rejected as an "unknown argument" even though it was
documented at the time. Verify against `gemini --help` for the version you pin in CI. 🕒 verify
live. This exit-code table and JSON schema come from a single vendor source and couldn't be
independently corroborated this run — treat the exact numeric codes as 🕒 verify live too.
**Sources:** [geminicli.com/docs/cli/headless](https://geminicli.com/docs/cli/headless/) (Google, updated 10 Mar 2026) · [geminicli.com/docs/cli/tutorials/automation](https://geminicli.com/docs/cli/tutorials/automation/) (Google, updated 9 Mar 2026) · [github.com/google-gemini/gemini-cli issue #9009](https://github.com/google-gemini/gemini-cli/issues/9009) (opened 20 Sep 2025, historical flag-parsing bug)
**Confidence:** vendor-documented (the `-p` pattern also appears on a well-known blog post, but its
author is a Google Director of Engineering, not an independent publisher for a Google product)

---

### Practice: Authenticate CI with an API key or service account, never a personal Google login
**Do:** In pipelines, set `GEMINI_API_KEY` (from Google AI Studio) for the simplest path, or for
Vertex AI set `GOOGLE_API_KEY` plus `GOOGLE_GENAI_USE_VERTEXAI=true`, or use a service-account JSON
via `GOOGLE_APPLICATION_CREDENTIALS`. Google's own docs recommend this explicitly "in
non-interactive environments, CI/CD pipelines, or if your organization restricts user-based [access]
or API key creation." Store the key as an encrypted repo/CI secret, never as a plaintext line in a
checked-in workflow file.
**Why (beginner):** Interactive "Login with Google" OAuth is built for a human clicking through a
browser consent screen — it doesn't work headlessly in a runner. And using a personal account's
login in shared CI infrastructure means every job runs "as you," which is a bad blast radius if the
job is compromised.
**Caveat / contested:** None significant found — vendor and independent sources agree here. Do treat
the key itself as a secret, per Part 1's secrets-handling practice.
**Sources:** [geminicli.com/docs/get-started/authentication](https://geminicli.com/docs/get-started/authentication/) (Google, updated 17 Apr 2026) · [apidog.com/blog/gemini-cli-github-actions](https://apidog.com/blog/gemini-cli-github-actions/) (Apidog, independent, 29 Jan 2026)
**Confidence:** independently-corroborated

---

### Practice: Use the official `run-gemini-cli` Action, and scope its GitHub token tightly
**Do:** Add `GEMINI_API_KEY` (or Workload Identity Federation credentials for GCP-based auth) as a
repo secret, then either run `/setup-github` from an interactive Gemini CLI session to scaffold
`.github/workflows/`, or copy examples from the action repo. Prefer a custom GitHub App over the
default `GITHUB_TOKEN` when the workflow needs to comment, label, or push, and set an explicit
minimal `permissions:` block rather than accepting the default broad token scope. Pin the action to
a specific released version rather than a floating tag.
**Why (beginner):** The GitHub token an Action gets by default can be broader than the job actually
needs. If a compromised or manipulated Gemini CLI run can use that token, tight scoping limits what
it can do — turning "attacker can do anything to your repo" into "attacker can read issues."
**Caveat / contested:** The independent source below confirms `GEMINI_API_KEY` as a repo secret and
the general action reference, but not the specific `permissions:`-block or version-pinning advice
(its own example actually uses a floating `@v1` tag) — that half of this practice is vendor-only.
**Sources:** [github.com/google-github-actions/run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli) (Google, accessed 10 Aug 2026) · [blog.google — Introducing Gemini CLI GitHub Actions](https://blog.google/technology/developers/introducing-gemini-cli-github-actions/) (Google, 6 Aug 2025) · [apidog.com/blog/gemini-cli-github-actions](https://apidog.com/blog/gemini-cli-github-actions/) (Apidog, independent, 29 Jan 2026)
**Confidence:** vendor-documented (independent source corroborates only the general secret/action
setup, not the permissions-scoping or pinning specifics)

---

### Practice: ⚠️ Never blanket-enable `--yolo` on workflows that read untrusted content
**Do:** Reserve `--yolo` / `--approval-mode=yolo` (auto-approve every tool call, no confirmation)
for workflows that only ever touch trusted, maintainer-authored input. For anything that reads
content an outside contributor controls — a PR body, an issue, a commit message — instead use
`--approval-mode=auto_edit` (auto-approves file edits only) or a scoped `tools.allowed` allowlist in
`settings.json` restricted to read-only tools. Prefer maintainer-triggered workflows (manual
dispatch, or gated on a maintainer's own comment) over workflows that auto-run on any fork's PR.
**Why (beginner):** `--yolo` exists so unattended pipelines don't hang waiting for an approval that
will never come — but it also means anything the model is tricked into "deciding" to run, via text
hidden in a PR or issue, executes immediately, with no human in the loop to say no. A real, patched
security advisory (CVSS 10.0 — the maximum possible severity score) confirmed that *before* the
patch, `--yolo` mode ignored the fine-grained tool allowlist in `settings.json` entirely — so even
teams who thought they'd scoped `--yolo` down were not actually protected. (A separate, even more
severe issue bundled into the same advisory — automatic command execution that doesn't even require
`--yolo` — is covered in the next practice; don't conflate the two.)
**Caveat / contested:** The security advisory itself, published 24 Apr 2026 and patched in
`@google/gemini-cli` 0.39.1 / `run-gemini-cli` 0.1.22, originally listed "No known CVE" — a later
article (7 Aug 2026, tied to a Black Hat USA talk) is the source that assigns it CVE-2026-12537; if
you look up the advisory directly you won't see that CVE number on the page itself, which is
expected, not a sign the citation is wrong. `gemini-cli` ships fast (latest published version as of
8 Aug 2026 was 0.54.4, well past the 0.39.1 patch floor) — confirm you're on a patched version; this
whole space is 🕒 verify live.
**Sources:** [GHSA-wpqr-6v78-jr5g advisory ("No known CVE")](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g) (Google/GitHub, 24 Apr 2026) · [The Hacker News — "Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws"](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html) (independent, 30 Apr 2026, also states "No CVE identifier assigned" at that time) · [The Hacker News — "Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets" (assigns CVE-2026-12537)](https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html) (independent, 7 Aug 2026) · [penligent.ai — "Gemini CLI RCE, Workspace Trust and the CI/CD Agent Attack Surface"](https://www.penligent.ai/hackinglabs/gemini-cli-rce-workspace-trust-and-the-ci-cd-agent-attack-surface/) (independent, 28 Apr 2026)
**Confidence:** independently-corroborated (multiple non-Google publishers corroborate the
GitHub-published advisory)

---

### Practice: ⚠️ Set workspace-trust settings deliberately — never assume a CI workspace is "trusted" by default
**Do:** Only set `GEMINI_CLI_TRUST_WORKSPACE=true` in a workflow's `env:` block when that workflow
exclusively processes trusted input (repo-owner or high-trust-collaborator authored code/prompts).
For workflows that outside contributors can trigger (public-repo issues/PRs), harden the workflow
first — least-privilege token permissions, tool allowlisting per the practice above, no secrets
exposed to the job — before ever setting this to true.
**Why (beginner):** "Trusting the workspace" means letting the CLI load and act on config files and
environment variables sitting in the checked-out repo — which, in a public repo, could have been
placed there by an attacker's PR, not by you. Earlier CLI versions auto-trusted the workspace folder
in any non-interactive/CI run, which is what let a malicious `.gemini/.env` file execute arbitrary
environment-variable-driven code. The underlying vulnerability this setting exists to let you
control (CVE-2026-12537, CVSS 10.0 — the maximum possible severity score) is a
workspace-auto-trust-to-command-execution bug in the container launcher, reached via a crafted
`.gemini/.env` file, and it fires **before the sandbox even starts** — it does not require `--yolo`
at all.
**Caveat / contested:** **Naming conflict, disclosed rather than papered over:** the security
advisory itself uses the variable name `GEMINI_TRUST_WORKSPACE`, while the current, actively
maintained guidance documentation uses `GEMINI_CLI_TRUST_WORKSPACE` — an independent source
explicitly flags this discrepancy and recommends following the current official docs. Using the
wrong spelling silently no-ops a security control, so double-check the exact variable name against
live docs before relying on it. ⚠ PENDING: this run could not confirm what the *current* default is
when neither variable is set at all — the guidance doc explains what to do if you *do* set it, but
doesn't state plainly whether an unset workspace is trusted or untrusted today, post-patch. Until
that's confirmed, treat an unset workspace-trust variable as an unknown, not a safe default, and set
your posture explicitly either way.
**Sources:** [run-gemini-cli trust-guidance.md](https://github.com/google-github-actions/run-gemini-cli/blob/main/docs/trust-guidance.md) (Google, accessed 10 Aug 2026) · [GHSA-wpqr-6v78-jr5g advisory](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g) (Google/GitHub, 24 Apr 2026) · [penligent.ai](https://www.penligent.ai/hackinglabs/gemini-cli-rce-workspace-trust-and-the-ci-cd-agent-attack-surface/) (independent, 28 Apr 2026)
**Confidence:** independently-corroborated

---

### Practice: Treat AI output as untrusted before it ever touches a secret
**Do:** Never pipe raw untrusted content — a PR title, issue body, or commit message written by an
outside contributor — directly into a Gemini CLI prompt in a job that also has access to repository
secrets. Rotate and scope GitHub Actions secrets narrowly, keep jobs that touch untrusted input
separate from jobs that hold deployment/cloud credentials, and require human review before any
Gemini-CLI-authored change is merged or applied — don't let the CLI auto-apply changes in a workflow
that processes untrusted input.
**Why (beginner):** Attackers have demonstrated that hidden instructions inside a GitHub comment or
issue can manipulate an AI agent running in Actions into leaking `GEMINI_API_KEY`, `GITHUB_TOKEN`,
or other secrets available to that job — the AI doesn't know the difference between "instructions
from the repo owner" and "instructions an attacker snuck into a comment."
**Caveat / contested:** Details of exactly which secrets are exfiltrable vary by the specific bug or
version; treat this as a class of risk to design against, not a single patched vulnerability you can
"fix and forget." One write-up describing this technique predates the April 2026 advisory above by
four months and describes a different, earlier prompt-injection issue — cited here as evidence of
the class of risk, not as the same bug.
**Sources:** [The Hacker News — "Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets"](https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html) (independent, 7 Aug 2026) · [hoploninfosec.com — "Gemini CLI GitHub Actions Vulnerability Causing Secret Leaks"](https://hoploninfosec.com/gemini-cli-github-actions-vulnerability-fix) (independent, 7 Dec 2025) · [run-gemini-cli trust-guidance.md](https://github.com/google-github-actions/run-gemini-cli/blob/main/docs/trust-guidance.md) (Google, accessed 10 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: Budget for quota limits before running Gemini CLI at scale
**Do:** Know your tier's request limits before wiring Gemini CLI into a loop (e.g. "run once per
file" over a large repo). As of Google's own quota page (updated 18 Jun 2026), an unpaid Gemini API
key is capped at roughly 250 model requests per user per day and restricted to the Flash-class
model; paid individual/workspace tiers scale to 1,500–2,000/day, with pay-as-you-go token billing
for uncapped-but-metered use. Add retry/backoff for quota-error responses rather than letting a CI
job fail hard or silently loop-retry without delay, and prefer precise, single-shot prompts over
chatty multi-call scripts.
**Why (beginner):** A CI job that fans out one Gemini CLI call per file in a large repo can blow
through a daily quota in minutes, or — on a paid key — run up an unexpectedly large bill, without
anyone noticing until later.
**Caveat / contested:** The same quota page also lists "around 1,000 requests/day" for a
Google-account/Code-Assist free-login path — but Google stopped serving that exact free/personal
login path on 18 Jun 2026, the **same day** this quota page was last updated. That figure is very
likely stale, unscrubbed vendor content rather than a currently-purchasable tier — don't budget a
pipeline against it. The other figures for API-key and paid tiers are unaffected by that cutoff. 🕒
verify live regardless — these numbers move often.
**Sources:** [geminicli.com/docs/resources/quota-and-pricing](https://geminicli.com/docs/resources/quota-and-pricing/) (Google, updated 18 Jun 2026) · [apidog.com/blog/gemini-cli-github-actions](https://apidog.com/blog/gemini-cli-github-actions/) (Apidog, independent, 29 Jan 2026)
**Confidence:** independently-corroborated on the general practice of budgeting/backoff; the exact
numeric quotas are single-source-per-date and explicitly flagged verify-live

---

### Practice: Know about the Gemini CLI → Antigravity CLI transition
**Do:** Be aware that as of 18 Jun 2026, Google stopped serving Gemini CLI / Gemini Code Assist
requests for personal "Login with Google" access — free tier, Google AI Pro, and Google AI Ultra
individual sign-in — directing those users to the new Antigravity CLI instead. Google's own
transition announcement states plainly that "Gemini CLI will remain accessible via paid Gemini and
Gemini Enterprise Agent Platform API keys" — so a pipeline authenticating with `GEMINI_API_KEY` or a
Vertex AI service account is explicitly, not just inferentially, unaffected. Gemini Code Assist
Standard/Enterprise licenses and Google Cloud-based Gemini Code Assist for GitHub also continue to
receive updates, and the `gemini-cli` package remains actively maintained as an open-source project.
If your CI pipeline was originally set up to log in with a personal Google account rather than an
API key or service account, it will have already broken.
**Why (beginner):** If your team set up a Gemini CLI GitHub Action or script months ago by
copy-pasting `gemini login` into a runner, instead of using an API key, your pipeline may have been
silently failing since mid-June 2026 — worth an active check, not an assumption.
**Caveat / contested:** The announcement doesn't say explicitly whether it covers every possible
Vertex-AI-adjacent auth configuration — the three confirmed-unaffected paths above (API key, Vertex
AI service account, Enterprise Code Assist license) cover what most CI pipelines actually use, but
if your setup is unusual, verify against the live announcement. 🕒 verify live given how fast this
transition is moving.
**Sources:** [developers.googleblog.com — "An important update: Transitioning Gemini CLI to Antigravity CLI" ("Gemini CLI will remain accessible via paid Gemini and Gemini Enterprise Agent Platform API keys")](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) (Google, 19 May 2026) · [yaw.sh/blog/gemini-cli-not-free-alternatives](https://yaw.sh/blog/gemini-cli-not-free-alternatives/) (independent, 25 Jul 2026)
**Confidence:** independently-corroborated

---

## Held pending fixes (things nobody could confirm yet)

These are honest gaps the technical entry's research couldn't close — not guesses, and not swept
under the rug.

- Nobody could confirm whether a Gemini CLI CI workspace is "trusted" or "untrusted" by default
  today, when you don't set either the old or new workspace-trust variable at all. Set your posture
  explicitly rather than relying on an unconfirmed default. ⚠ PENDING
- A side-by-side comparison of API-key-level spend/rate-limit controls for OpenAI and Google
  (similar to what exists for Anthropic) wasn't done this run — only Anthropic's Enterprise-tier
  Spend Limits API was checked directly against the question "does this protect a bare CI API key,"
  and the answer there was "not necessarily." ⚠ PENDING
- No independent (non-Anthropic) source could confirm exactly how Claude Code's `--strict-mcp-config`
  behaves in CI, and no source describes a concrete, off-the-shelf way to enforce a hard, blocking
  network allowlist (rather than just monitoring) on a disposable GitHub-hosted runner. ⚠ PENDING
- Whether OpenAI's `openai/codex-action` truly ships a `:danger-full-access` permission profile
  couldn't be confirmed — only `:read-only` and `:workspace` were independently confirmed this run.
  ⚠ PENDING
- Neither Claude Code nor Codex CLI publishes a full, enumerated table of every possible exit code
  (Claude Code documents only 0/non-zero/143; Codex CLI documents binary success/fail only) — this
  is noted as a caveat rather than a gap, since "it isn't published" is the honest answer.
- Claude Code's GitLab CI/CD integration is described by Anthropic as "currently in beta" and
  "maintained by GitLab," but no GitLab-published page confirming the same setup steps was found
  this run — treated as a vendor-only source, not independent corroboration. ⚠ PENDING

## CHANGELOG (technical entry → this beginner guide)

1. **Re-leveled, not re-researched.** This guide is a plain-language rewrite of the graded,
   0-fabrication technical entry at the same `snapshot_date` (10 Aug 2026). No new facts, commands,
   version numbers, or sources were added, and no URL was changed — every `**Sources:**` line above
   reuses the technical entry's links verbatim (merged/deduplicated where two practices were
   combined into one heading, never rewritten).
2. **Added a "Before you start: what is CI/CD, anyway?" section.** The technical entry assumes the
   reader already knows what a CI/CD pipeline is; this guide defines CI/CD, "a pipeline," GitHub
   Actions, and why headless mode matters, before the first practice.
3. **Reordered to lead with Part 1 and the safe-skeleton example.** The cross-provider fundamentals
   and the worked "safe skeleton" workflow are the most concrete, most immediately useful material
   for a first-timer, so they now come first and are presented in full (all 9 fundamentals kept).
4. **Condensed the Claude Code section from 11 practices to 8 headings**, by merging closely related
   practices that cover the same underlying action: the invocation command was merged with the
   JSON-output/exit-code practice, and the GitHub App setup practice was merged with the
   permissions-scoping/CVE-2026-44246 practice. All facts and sources from both merged practices are
   preserved.
5. **Condensed the Codex CLI section from 10 practices to 8 headings**, merging the `codex exec`
   invocation, exit-code, and `--json`/`--output-schema` practices into one "run it and check the
   result" heading. All facts and sources preserved.
6. **Condensed the Gemini CLI section from 10 practices to 8 headings**, merging the headless-mode
   invocation practice with the JSON-output/exit-code practice, and **dropped one practice outright**
   ("Never set `DEBUG` as an environment variable") as a narrow, single-sourced footgun that's too
   advanced/niche for a first CI/CD pipeline — its source was removed along with it, per RingS
   convention for dropped practices.
7. **Kept every ⚠️ WARNING and 🕒 verify-live flag from the technical entry**, including both
   Part 1 warnings (auto-run gating, cost/runtime circuit breakers), both Claude Code warnings
   (`bypassPermissions`, spend/turn caps), both Codex CLI warnings (`--yolo`, the procfs/sudo
   API-key risk), and both Gemini CLI warnings (`--yolo`, workspace-trust settings) — softened
   nowhere, none dropped.
8. **Kept the full "Held pending fixes" list**, rephrased in plain language, including the ⚠ PENDING
   items — beginners need to know what's still an open question at least as much as what's settled.
9. **Rewrote every glossary term and inline jargon expansion** (headless mode, MCP, OIDC, ephemeral
   vs. self-hosted runner, procfs, `GITHUB_TOKEN` vs. GitHub App, "safe outputs" pattern) into a
   scannable bullet list at the top, so a reader hits the definition before the practice that needs
   it, instead of mid-paragraph.
10. **Did not reuse the technical entry's 44-item CHANGELOG.** That changelog documents the Skeptic/
    Timekeeper/Beginner-panel grading process that produced the technical entry; this changelog
    documents only the re-leveling step from that already-graded entry to this beginner version, per
    RingS convention.
