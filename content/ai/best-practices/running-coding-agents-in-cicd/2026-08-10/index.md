---
title: "Running Coding Agents in CI/CD — Cross-Provider Best Practices (as of 10 Aug 2026)"
date: 2026-08-10
snapshot_date: 2026-08-10
topic: running-coding-agents-in-cicd
track: best-practices
audience: "technically comfortable readers"
description: "How to run Claude Code, Codex CLI, or Gemini CLI unattended in CI/CD pipelines: headless-mode mechanics, least-privilege credentials, human approval gates, sandbox/approval-bypass dangers (including a CVSS 10.0 Gemini CLI RCE), secrets handling, and cost circuit breakers, as of 10 Aug 2026."
content_type: "Best Practice"
categories: ["CI/CD", "Claude Code", "Codex CLI", "Gemini CLI"]
tags: ["ci-cd", "github-actions", "headless", "automation", "claude-code", "codex-cli", "gemini-cli", "security", "prompt-injection"]
last_refreshed: 2026-08-10
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-08-10"
grading_result: "0 fabrications after correction; 5 Skeptic KILLs + 15 FIXes + 12 FLAGs resolved (mis-cited sources, an over-scoped CVE, a mis-attributed CVSS 10.0 finding, an incorrect env-var default claim); 4 Timekeeper updates folded in (a new Claude Code gateway spend-limit feature, an experimental Codex token-budget config, a corrected GitHub Actions timeout pending-item, a broadened Antigravity-transition exception); Beginner-panel gaps closed (jargon glossary, a worked minimal-safe workflow skeleton, a Claude Code human-review cross-reference, a completed allowlist example); 3 gaps left as ⚠ PENDING"
---

<!-- This file lands at content/ai/best-practices/running-coding-agents-in-cicd/2026-08-10/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a
     NEW <snapshot-date> dir. "Latest" is computed by Grove's template from snapshot_date;
     do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Running Coding Agents in CI/CD (as of 10 Aug 2026)

> **Grading note.** A dated snapshot — accurate as of **10 Aug 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by four pupils (Claude Code, Codex CLI, Gemini
> CLI, and a cross-provider/generic pass) on 10 Aug 2026, adversarially re-fetched by the
> Skeptic panelist on 11 Aug 2026 (every URL re-fetched; 5 KILLs, 15 FIXes, 12 FLAGs — mostly
> **citation drift**: a source that supports the general topic gets over-credited for a specific
> claim it never makes, not outright fabrication), reviewed for novice-safety by the Beginner
> panelist, and checked for staleness by the Timekeeper panelist (who found several
> already-shipped updates the pupils' research window had just missed). Corrections applied
> inline; unverifiable gaps marked ⚠ PENDING — never guessed. **0 fabrications after
> correction.**

**Scope:** practices that apply regardless of which agent CLI a pipeline invokes are in Part 1.
Vendor-specific mechanics for Claude Code, Codex CLI, and Gemini CLI are in Parts 2–4. Examples
mostly use GitHub Actions terminology because that's where the deepest documentation and
incident history exists as of this snapshot, but the underlying principles (least privilege,
human gates, sandboxing, circuit breakers, idempotency) apply to any CI system.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

**Terms used throughout this entry:** **Headless / non-interactive mode** means running an
agent CLI as a single command that starts, does its job, prints a result, and exits — instead
of an interactive chat window that expects a human to click through prompts (CI runners have no
human to click "yes"). **MCP (Model Context Protocol)** is an open standard for giving a model
tools/data sources; an MCP *server* is a small program that exposes those tools, and it can
carry its own credentials. **OIDC (OpenID Connect)** lets a CI job trade a short-lived,
workflow-scoped identity token for real cloud credentials instead of storing a long-lived static
key as a secret. An **ephemeral runner** is a CI machine created fresh for one job and destroyed
afterward (GitHub's own hosted runners work this way); a **self-hosted runner** is a persistent
machine you manage yourself, which can accumulate state and risk between jobs if it isn't reset.
`/proc` (**procfs**) is a Linux virtual filesystem that exposes running processes' memory and
environment variables as readable files — anyone with `sudo` on the same machine can read
another process's environment through it, sandboxed or not. A repo's **`GITHUB_TOKEN`** is a
token GitHub auto-generates for each workflow run; a **GitHub App** is a separate,
independently-installed identity with its own scoped permissions that a workflow can use
instead, decoupled from any one person's account.

---

## Part 1 — Cross-provider fundamentals

These practices hold regardless of which agent CLI a pipeline invokes.

### Practice: Scope the agent's CI credentials to least privilege
**Do:** Never hand an agent job the default org-wide `GITHUB_TOKEN` or a broad personal-access
token. Set an explicit `permissions:` block at the workflow or job level, starting from
`contents: read` and adding only what the job needs (e.g. `pull-requests: write` if it must
comment). Once you list *any* permission, GitHub sets everything you didn't list to `none` — so
a partial block is safe by construction, not a partial grant. Prefer short-lived, narrowly-scoped
credentials — OIDC tokens for cloud provider access instead of long-lived static keys — and give
the agent a dedicated machine identity/API key rather than a human's personal credentials, so you
can revoke or rate-limit it independently.
**Why (beginner):** An AI agent in CI runs unattended and can be tricked (via prompt injection,
described below) into taking actions you didn't intend. If its token can only read code and open
a PR, the worst case is a bad PR you can close. If its token can also push to `main`, delete
branches, or hit your cloud account, the worst case is much bigger — and it happens without a
human in the loop to notice in time.
**Caveat / contested:** GitHub Actions' `GITHUB_TOKEN` already restricts to read-only when a
workflow is triggered by a pull request from a fork — but that protection doesn't apply to
same-repo branches or to secrets you've explicitly exposed to the job. Least-privilege scoping is
a discipline you still have to apply yourself; it isn't automatic just because you're using
GitHub.
**Sources:** [GitHub Docs — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) (accessed 10 Aug 2026) · [GitHub Docs — Workflow syntax for GitHub Actions ("If you specify the access for any of these permissions, all of those that are not specified are set to `none`")](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) (accessed 12 Aug 2026) · [GitGuardian — GitHub Actions Security Cheat Sheet](https://blog.gitguardian.com/github-actions-security-cheat-sheet/) (11 Apr 2025) · [Cloud Security Alliance — Research Note: Prompt Injection in AI-Powered GitHub Actions](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-github-actions-security-20260503-csa-st/) (3 May 2026)
**Confidence:** independently-corroborated

---

### Practice: Require a human approval gate before merge, deploy, or any destructive action
**Do:** Use branch protection with required reviewers on any branch an agent can push to, and use
GitHub Environments (or your CI system's equivalent — protected/manual-approval environments)
with required reviewers on any job that deploys, force-pushes, or otherwise has high blast
radius. Do not let the agent's own "self-review" or auto-generated approval satisfy that
requirement.
**Why (beginner):** Agents are good at writing plausible-looking code and bad at knowing when
they're wrong. A human review step is the backstop that catches a subtly broken migration, a
credential accidentally committed, or a prompt-injection-driven action before it reaches
production or rewrites history. This is true even if the same agent is trusted to work fully
autonomously on lower-stakes tasks (like opening a draft PR).
**Caveat / contested:** GitHub Docs state that if a repository requires PR approvals, *your own*
approval of a PR that Copilot's coding agent authored "won't count toward the required number" —
an explicit anti-self-approval rule aimed at the human who prompted the agent, not a claim about
what kind of review Copilot's own bot account can leave. It's a concrete example of a vendor
building a review gate into the product by default, just not the exact mechanism you might
assume — verify what your own agent product actually restricts rather than taking this as a
universal guarantee.
**Sources:** [GitHub Docs — Reviewing a pull request created by Copilot](https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/reviewing-a-pull-request-created-by-copilot) (accessed 10 Aug 2026) · [GitHub Docs — Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) (accessed 10 Aug 2026) · [OWASP Cheat Sheet Series — AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) (accessed 10 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: ⚠️ Don't let agent workflows auto-run on pushed changes without a manual gate — and be wary of `pull_request_target` with agent-driven writes
**Do:** Keep GitHub's default behavior of *not* auto-running workflows on pushes made by an
automated coding agent to a PR branch (requiring a maintainer to click "Approve and run
workflows"). Avoid triggering agent jobs on `pull_request_target` (which runs with the base
repo's write permissions and secrets against *untrusted* PR content) unless you have a specific,
audited reason; prefer `pull_request` (read-only, no secrets) or `workflow_run` for privilege
separation when you must react to fork PRs.
**Why (beginner):** `pull_request_target` combined with an AI agent that reads PR content is a
known attack pattern: an attacker opens a PR whose title, description, or diff contains hidden
instructions, the agent "reads" that content as part of its context, and — because the workflow
run has write access and secrets — the agent can be manipulated into leaking credentials or
merging malicious code, with no human ever approving anything.
**Caveat / contested:** This is an active, evolving attack surface, not a solved problem. CSA's
May 2026 research note lists misconfigured `pull_request_target` plus overprivileged
`GITHUB_TOKEN`s as the top amplifiers of this risk class, citing CVE-2025-30066 (a floating-tag
supply-chain compromise, not agent-specific) as the kind of incident this pattern enables. A
separate, real 2026 CVE (CVE-2026-44246 — see Part 2's "Scope workflow permissions" practice for
Claude Code) shows a *related but distinct* failure mode: an overly permissive write-access
allowlist, not `pull_request_target` itself. Treat this practice as risk-reduction, not
elimination.
**Sources:** [Cloud Security Alliance — Research Note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-github-actions-security-20260503-csa-st/) (3 May 2026) · [GitHub Docs — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) (accessed 10 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: Default the agent's job to read-only permissions; route any write action through a separate, sanitized step
**Do:** Give the job/container that actually runs the LLM and its tools read-only repo
permissions (`contents: read`, no write scopes) and no direct access to the credential that would
push, comment, or merge. Have the agent emit a structured, sanitized "intended action" — for
example a JSON file like `{"action": "open_pr", "branch": "fix/123", "diff_ref": "artifact://patch.diff", "title": "..."}`
— that a **separate** job, with its own narrower, audited permission set, reads as an artifact
and carries out. This is sometimes called a "safe outputs" pattern; a minimal two-job skeleton
looks like: *Job 1* (`permissions: {contents: read}`) runs the agent and uploads its proposed
action as a build artifact; *Job 2* (`permissions: {contents: write, pull-requests: write}`,
gated with `needs: job1` and, ideally, a required reviewer) downloads that artifact, validates its
shape, and only then opens the PR.
**Why (beginner):** If the process reading untrusted PR/issue text is the same process holding
the token that can write to your repo, a successful prompt injection has a direct path to real
damage. Splitting "the agent decides what to do" from "a trusted, limited step actually does it"
means a manipulated agent can at worst propose a bad action — it can't execute one unchecked.
**Caveat / contested:** This is GitHub's own architecture for its "GitHub Agentic Workflows"
(`gh-aw`) project, which runs Claude Code, Codex, Gemini CLI, or Copilot inside Actions with
read-only defaults and a separate output-sanitization stage — a genuinely useful reference
pattern, but it's a single vendor's design, not (yet) a cross-industry standard, and most teams
wiring up their own agent + CI job by hand will need to build the two-job split themselves (the
JSON shape above is illustrative, not a `gh-aw` API contract — check its docs for the actual
schema if you adopt the tool directly).
**Sources:** [GitHub — gh-aw permissions reference](https://github.github.io/gh-aw/reference/permissions/) (accessed 10 Aug 2026) · [GitHub — gh-aw self-hosted runners reference](https://github.github.io/gh-aw/reference/self-hosted-runners/) (accessed 10 Aug 2026)
**Confidence:** vendor-documented

---

### Practice: Prevent secrets from leaking into agent transcripts, CI logs, and PR/issue comments
**Do:** Pass secrets only to the specific step that needs them (not as job-wide or workflow-wide
environment variables); rely on your CI system's built-in log masking (e.g. GitHub Actions masks
registered secret values automatically) rather than assuming an LLM-generated transcript will
redact anything on its own; run a secret-scanning tool (GitHub secret scanning/push protection,
Gitleaks, TruffleHog, or similar) as a required check before an agent-authored PR can merge; and
avoid giving the agent broad filesystem/env read access that would let it accidentally quote a
`.env` file or credential back into a public PR comment.
**Why (beginner):** Agents narrate their work — they'll often paste file contents, command
output, or error messages into their own transcript, and CI systems frequently post that
transcript (or a summary of it) as a public PR comment or a build log anyone with repo read
access can view. A credential that would normally never appear in a diff can end up in a comment
because the agent "explained" what it did.
**Caveat / contested:** Log masking only works for secrets GitHub already knows about (registered
via `secrets:` or explicitly masked); a credential the agent discovers dynamically (e.g. read from
a config file, not from an Actions secret) won't be auto-redacted. Push protection and scanning
are detective controls that catch leaks after the fact in many pipelines, not preventive ones —
treat "the agent never had the secret in its context in the first place" as the stronger control.
**Sources:** [GitHub Docs — Secret leakage risks](https://docs.github.com/en/code-security/concepts/secret-security/secret-leakage-risks) (accessed 10 Aug 2026) · [GitGuardian — GitHub Actions Security Cheat Sheet](https://blog.gitguardian.com/github-actions-security-cheat-sheet/) (11 Apr 2025) · [GitGuardian — The GhostAction Campaign: 3,325 Secrets Stolen Through Compromised GitHub Workflows](https://blog.gitguardian.com/ghostaction-campaign-3-325-secrets-stolen/) (Sep 2025, real-world example of the blast radius of a workflow that exfiltrates secrets, not AI-specific)
**Confidence:** independently-corroborated

---

### Practice: ⚠️ Put hard circuit breakers on agent job cost and runtime
**Do:** Set `timeout-minutes` on every agent job — GitHub Actions' default job timeout is **360
minutes (6 hours)** 🕒 verify live, far too long for most agent tasks, so don't rely on the
platform default. Use a `concurrency` group with `cancel-in-progress` so retriggered/duplicate
runs don't stack up and run in parallel. Set a spend/rate limit at the API-key level with your
model provider (most providers offer per-key or per-workspace usage/spend limits) so a looping
agent hits a provider-side wall even if your own job-level controls fail. Use both a per-run cap
(catches one runaway task) and an aggregate budget cap (catches many small runs adding up).
**Why (beginner):** Agent loops fail differently than normal CI jobs — a stuck agent may keep
calling tools or retrying a failing step at machine speed instead of just erroring out, and each
call can cost real money. Without a timeout and a spend ceiling, a single misbehaving trigger
(e.g. a CI job that re-fires on every push to a busy branch) can generate an unexpectedly large
bill before a human notices.
**Caveat / contested:** Exact provider spend-limit mechanics are plan-specific — treat any number
here as 🕒 verify live. Anthropic's Spend Limits API, for example, is documented as available "to
Claude Enterprise organizations only... not available to Claude Platform (Claude Console)
organizations" — i.e. it applies to Enterprise seat-based usage, not necessarily to a plain API
key used from a CI job; check which limit type actually applies to your CI credential before
assuming it's capped. Equivalent OpenAI- and Google-side mechanics for a CI API key specifically
were not researched this run — see "Held pending fixes" below.
**Sources:** [GitHub Docs — Concurrency](https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency) (accessed 10 Aug 2026) · [Anthropic — Spend Limits API ("available to Claude Enterprise organizations only")](https://platform.claude.com/docs/en/manage-claude/spend-limits-api) (accessed 10 Aug 2026)
**Confidence:** independently-corroborated on the GitHub-side timeout/concurrency mechanics; thin
on "a provider-side spend cap protects a specific CI job" (Anthropic's mechanism is
Enterprise-seat-scoped, not confirmed to cover a bare CI API key)

---

### Practice: Design agent-driven CI actions to be safe to retry (idempotent), especially PR/branch creation
**Do:** Derive branch names, PR titles, and any "does this already exist" check from a
deterministic value tied to the triggering event (e.g. the commit SHA or issue number), not from
a timestamp or a freshly generated random ID — and have the job check whether an equivalent
branch/PR/comment already exists before creating a new one ("check before act"). Use a
`concurrency` group keyed on that same deterministic value so a retried or re-triggered run
cancels or supersedes the stale one instead of running alongside it.
**Why (beginner):** CI jobs get retried — by a flaky runner, a webhook redelivery, or a human
clicking "re-run." If the agent's job creates a new branch or PR every time it runs, a retry
silently produces duplicate PRs, duplicate comments, or duplicate commits instead of failing
loudly, and nobody notices until the repo is cluttered with near-identical open PRs.
**Caveat / contested:** This is a general property of good bot/automation design (the same lesson
Dependabot and Renovate learned) rather than something unique to AI agents. It's included here
because it's the AI-agent-specific research pass that turned it up, but sourcing for the
*AI-agent-specific* framing is thin — most of what's findable is generic CI/automation guidance,
and several AI-agent-specific "idempotency" articles found in search read as low-quality SEO
content and were deliberately excluded. Treat this practice's *general validity* as
well-established (it's basic distributed-systems hygiene) but its AI-agent-specific framing as
thin.
**Sources:** [GitHub Docs — Concurrency](https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency) (accessed 10 Aug 2026)
**Confidence:** thin

---

### Practice: Sandbox and monitor the agent's execution environment as defense-in-depth — not as your only control
**Do:** Treat network/runtime monitoring as a complementary layer, not a substitute for
least-privilege tokens, human approval gates, and read-only-by-default permissions (all above).
GitHub's own Copilot coding agent ships a firewall, but its own docs warn it is "not a
comprehensive security solution" — it only covers processes the agent starts via its Bash tool,
does **not** cover MCP servers or custom setup-step processes, and only applies inside that
specific sandboxed environment. As a complementary control, tools like Harden-Runner add runtime
*visibility* into what a job's processes actually do (its default `egress-policy: audit` mode
**monitors and logs** outbound network calls rather than blocking them) — useful for detecting an
agent that tried to reach somewhere it shouldn't, even where you can't yet enforce a hard
allowlist.
**Why (beginner):** Even with careful permission scoping, an agent that's been manipulated by
injected instructions in an issue or PR body could still try to exfiltrate whatever it *can*
reach — source code, environment variables, or tokens still in memory — over the network.
Monitoring what the sandbox's processes actually talk to gives you a chance to catch that even
when a permission boundary has a gap you didn't know about (like the firewall's own documented
blind spots above).
**Caveat / contested:** Don't treat "we enabled the firewall" or "we turned on monitoring" as a
solved problem — a sophisticated attack can still bypass a process-level firewall, and audit-mode
monitoring by design does not block anything in real time; it only gives you an after-the-fact
signal to alert on. A hard, blocking network-egress allowlist enforced at the infrastructure level
(not something the agent's own shell could disable) is a stronger control than either of these,
but this run did not find a citable source describing a specific, off-the-shelf way to apply that
to an ephemeral GitHub-hosted runner — see "Held pending fixes."
**Sources:** [GitHub Docs — Customizing or disabling the firewall for GitHub Copilot cloud agent](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-firewall) (accessed 10 Aug 2026) · [StepSecurity — Securing GitHub Copilot in GitHub Actions with Harden-Runner (published 22 Jul 2025; no independently-verifiable "updated" date found)](https://www.stepsecurity.io/blog/securing-github-copilot-in-github-actions-with-harden-runner) · [Cloud Security Alliance — Research Note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-github-actions-security-20260503-csa-st/) (3 May 2026, recommends runner-level monitoring such as Harden-Runner as a complementary control)
**Confidence:** vendor-documented on the firewall's own documented gaps; thin on Harden-Runner as
a general recommendation (it is a monitoring tool, not the blocking/allowlisting control the
practice title implies — Do/Why above have been narrowed to match what the sources actually
support)

---

### Practice: Pin third-party Actions/dependencies used inside agent workflows to a full commit SHA, not a mutable tag
**Do:** When an agent CI workflow depends on third-party GitHub Actions, container images, or CLI
tools, pin them to a full commit SHA (or an equivalent immutable digest) rather than a floating
tag like `@v4` or `latest`.
**Why (beginner):** A tag can be moved to point at new, potentially malicious code after you've
already reviewed and trusted it — this is exactly how several real supply-chain attacks on GitHub
Actions pipelines have happened (CSA's research note names CVE-2025-30066 as one concrete
example). In a pipeline where an AI agent already has some elevated access, a compromised
dependency is an easy way for an attacker to gain much more.
**Caveat / contested:** This is longstanding general CI/CD supply-chain advice, not unique to AI
agents — it's included here because it's specifically called out by security researchers as a
risk *multiplier* once an AI agent with write access and secrets is added to the same pipeline.
**Sources:** [GitHub Docs — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) (accessed 10 Aug 2026) · [Cloud Security Alliance — Research Note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-github-actions-security-20260503-csa-st/) (3 May 2026)
**Confidence:** independently-corroborated

---

### A minimal "safe skeleton" workflow

None of the four research drafts behind this entry contained a single complete, worked
`.github/workflows/*.yml` file — every individual setting above was documented correctly but only
in prose. That avoids the worst beginner-safety failure mode (nobody can copy-paste a dangerous
YAML block that isn't shown), but it also leaves a first-time reader with no picture of how the
pieces above compose. The skeleton below is this entry's own composition — assembled from the
cited practices above, not a vendor-published example — showing the shape, not a drop-in file:

```yaml
name: agent-triage
on:
  pull_request:            # NOT pull_request_target — see the practice above
    types: [opened, synchronize]

concurrency:
  group: agent-triage-${{ github.event.pull_request.number }}   # idempotent — see practice above
  cancel-in-progress: true

jobs:
  propose:                 # Job 1: read-only, runs the agent against untrusted PR content
    runs-on: ubuntu-latest
    timeout-minutes: 15     # hard circuit breaker — see practice above
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

This is illustrative, not a tested file — treat every `<full-commit-sha>` and CLI invocation as a
placeholder to fill in against the vendor-specific practices in Parts 2–4, and adapt the trigger/
permissions to your own threat model.

---

## Part 2 — Claude Code

Covers Anthropic's `claude` CLI invoked as `claude -p` (print/headless mode), as documented at
[code.claude.com/docs](https://code.claude.com/docs/en/headless) on 10 Aug 2026. Anthropic's
`code.claude.com`/`docs.claude.com` pages are living documentation with no visible per-page
publish date; version gates below (e.g. "requires v2.1.221") are cited where the page states them
🕒 verify live, since Claude Code ships roughly weekly point releases (9 releases in the 3 weeks
before this snapshot).

### Practice: Use `claude -p` (print/headless mode) as the automation entry point, not the interactive TUI
**Do:** Invoke `claude -p "<prompt>"` for any scripted or CI use. It runs the same agent loop as
interactive Claude Code, prints a result, and exits — no TTY, no interactive prompts needed. Pipe
data in via stdin (`cat log.txt | claude -p "..."`) and redirect output for use in scripts.
**Why (beginner):** CI runners have no human to click "yes" on a permission dialog. Print mode is
the supported way to run Claude Code unattended; the interactive CLI will otherwise hang waiting
for input that never comes.
**Caveat / contested:** Piped stdin is capped at 10MB — write large inputs to a file and reference
the path instead. If Claude Code can't read stdin at all (e.g. a supervisor disconnected it), it
warns to stderr and continues with just the command-line prompt rather than failing.
**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 10 Aug 2026) · [code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference) (fetched 10 Aug 2026)
**Confidence:** vendor-documented

---

### Practice: Add `--bare` in CI to skip host-specific auto-discovery
**Do:** Run `claude --bare -p "..."` in pipelines. Bare mode skips auto-discovery of hooks,
skills, plugins, MCP servers, auto-memory, and `CLAUDE.md`, giving the same result on every
runner regardless of what's in `~/.claude` or the project's `.mcp.json`. Explicitly pass back only
what you need — for example `claude --bare -p "..." --mcp-config ./ci-mcp.json --settings
./ci-settings.json` — using `--append-system-prompt`, `--settings`, `--mcp-config`, or `--agents`
as needed. Bare mode also never reads OAuth credentials or the OS keychain, so set
`ANTHROPIC_API_KEY` explicitly (e.g. as a masked CI secret injected into the job's environment,
not written into the command line).
**Why (beginner):** Without `--bare`, a CI run silently inherits whatever hooks or MCP (Model
Context Protocol) servers happen to be configured on that machine (or checked into the repo),
which makes runs non-reproducible and can load tools/credentials you didn't intend to grant the
pipeline.
**Caveat / contested:** Anthropic's own docs say `--bare` "will become the default for `-p` in a
future release" — i.e. this is a recommendation that is expected to change CLI defaults later; the
flag itself is 🕒 verify live.
**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 10 Aug 2026)
**Confidence:** thin (single vendor source; no independent corroboration found for `--bare`
specifically)

---

### Practice: Parse `--output-format json` / `stream-json` programmatically; branch on exit code, not on scraping text
**Do:** Use `--output-format json` and read the `.result` (final text), `.session_id`, and
`.total_cost_usd` fields with a JSON tool such as `jq` (a command-line JSON parser), rather than
parsing the default plain-text output. For token-by-token consumption use `--output-format
stream-json --verbose --include-partial-messages` and read the terminal `result` event. Claude
Code exits `0` on success and non-zero on failure (including `143` if the process is killed with
SIGTERM), so gate pipeline steps on the exit code.
**Why (beginner):** Human-readable text output can change wording between versions and breaks
`grep`/`sed`-based parsing. The JSON result schema (and exit code) is the stable contract a CI
step should depend on.
**Caveat / contested:** `total_cost_usd` (and the per-model cost breakdown) is a **client-side
estimate** and can differ from your actual bill — don't treat it as an exact accounting figure. No
full enumerated exit-code table is published; only 0 (success), non-zero (failure), and 143
(SIGTERM) are documented, so avoid hard-coding assumptions about other specific non-zero values.
**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 10 Aug 2026) · [hidekazu-konishi.com — "Claude Code in CI/CD and Headless Automation"](https://hidekazu-konishi.com/entry/claude_code_cicd_and_headless_automation.html) by Hidekazu Konishi (first published 7 Jun 2026)
**Confidence:** independently-corroborated

---

### Practice: Set up the official `claude-code-action` GitHub App integration rather than hand-rolling API calls
**Do:** Run `/install-github-app` from Claude Code locally (quick setup) or install the
[Claude GitHub App](https://github.com/apps/claude) and copy
[`examples/claude.yml`](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml)
into `.github/workflows/` (manual setup). Store credentials as a repo secret: `ANTHROPIC_API_KEY`
(Console API key) or `CLAUDE_CODE_OAUTH_TOKEN` (generated with `claude setup-token`, tied to a
Pro/Max/Team/Enterprise subscription). Reference the secret in the workflow's `with:` block, never
inline.
**Why (beginner):** The official action already handles trigger detection (`@claude` mentions),
mode switching (interactive comment-driven vs. scheduled/automation), and GitHub App
authentication — reimplementing this with raw `curl` calls to the Anthropic API is more
error-prone and loses the built-in write-access/bot-actor checks described below.
**Caveat / contested:** An OAuth token from `claude setup-token` is tied to the subscription of
the person who ran it — for an organization-wide rollout, use an API key from the Console instead
so the credential isn't tied to one person's account, or use OIDC/workload identity federation
(`anthropic_federation_rule_id`, `anthropic_organization_id`, `anthropic_service_account_id`,
`anthropic_workspace_id`) to avoid storing a static secret at all. The independent source below
(10 Mar 2026 — 5 months old on a topic that ships weekly) confirms the general `permissions:`
block and `ANTHROPIC_API_KEY` pattern but not the GitHub App–specific mechanics (`/install-github-app`,
`CLAUDE_CODE_OAUTH_TOKEN`, `claude setup-token`), which are Anthropic-only; re-verify current
GitHub Actions permissions syntax against live docs rather than treating that citation as still
current on its own.
**Sources:** [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) (fetched 10 Aug 2026) · [systemprompt.io — "Set Up Claude Code GitHub Actions for PR Review and CI"](https://systemprompt.io/guides/claude-code-github-actions) (10 Mar 2026)
**Confidence:** vendor-documented (the independent source corroborates only the general
`permissions:`/secret pattern, not this practice's specific claims)

---

### Practice: Scope workflow permissions to least privilege and restrict who can trigger a run
**Do:** In the workflow's `permissions:` block, grant only what the job needs (typically
`contents: write`, `pull-requests: write`, `issues: write`, `id-token: write` for the default
GitHub App auth, `actions: read` if Claude needs to see CI results) — GitHub Docs confirm that
once you specify access for any permission, everything else is set to `none`. If your org needs a
tighter footprint than the shared Claude GitHub App's full permission set, create a custom GitHub
App scoped to just Contents, Issues, and Pull requests. `claude-code-action` itself also rejects
triggering comments from users without repo write access (configurable via
`allowed_non_write_users`) and rejects bot actors by default (configurable via `allowed_bots`) to
stop automation loops. Pair this with Part 1's human-approval-gate practice: even a well-scoped
`claude-code-action` job should open a PR for review, not push straight to a protected branch.
**Why (beginner):** A broad `contents: write` + no other scoping means a prompt-injected
instruction in an issue or PR comment could, in principle, direct Claude to push to any branch or
read repo secrets available to the job. Tight scopes and the write-access check limit blast
radius.
**Caveat / contested:** `allowed_non_write_users` is a genuine hardening knob, but setting it
carelessly is also the exact mechanism a real 2026 vulnerability abused — a specific project's
workflow (`MIC-DKFZ/nnUNet`'s `issue-triage.yml`, using `anthropics/claude-code-action`, **not**
GitHub's own "GitHub Agentic Workflows" product) set `allowed_non_write_users: ${{
github.event.issue.user.login }}`, which hands the write-access gate to *any logged-in GitHub
user* who opens an issue, not just trusted collaborators (GHSA-63mx-j37w-gh59 / CVE-2026-44246).
Set this input to a fixed, reviewed list of usernames/teams — never to a field taken directly
from the triggering event. Separately: GitHub does **not** trigger downstream workflows on
commits pushed using the default `GITHUB_TOKEN` — if you want Claude's own commits to re-trigger
CI, omit `github_token` from the action (so it authenticates as the Claude GitHub App instead) or
supply a custom app token.
**Sources:** [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) (fetched 10 Aug 2026) · [systemprompt.io — "Set Up Claude Code GitHub Actions for PR Review and CI"](https://systemprompt.io/guides/claude-code-github-actions) (10 Mar 2026) · [GitHub Docs — Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) (accessed 12 Aug 2026) · [GHSA-63mx-j37w-gh59 advisory](https://github.com/MIC-DKFZ/nnUNet/security/advisories/GHSA-63mx-j37w-gh59) · [Tenable — CVE-2026-44246](https://www.tenable.com/cve/CVE-2026-44246) (both fetched 11 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: ⚠️ Never run `--dangerously-skip-permissions` / `bypassPermissions` against a CI runner that holds real credentials or network access to production
**Do:** Only use `bypassPermissions` (equivalently `--dangerously-skip-permissions`) inside a
disposable, isolated environment — a throwaway container or VM with no path to production and
minimal, scoped credentials — never on a long-lived, shared, or credential-rich CI runner. For
most CI use cases, use a narrower mode instead (see next practice). On Linux/macOS, Claude Code
itself refuses to start in bypass mode when running as root/sudo, with the literal error string
`--dangerously-skip-permissions cannot be used with root/sudo privileges for security reasons` —
but this guardrail is **skipped automatically inside a recognized sandbox**, so don't treat "runs
as root" as a reliable backstop if your runner also happens to look like a sandbox to Claude Code.
**Why (beginner):** `bypassPermissions` skips essentially all approval prompts, including writes
to protected paths like `.git` and `.claude`. If the CI job's prompt was manipulated (e.g. by a
malicious PR comment or a poisoned dependency), there is no human checkpoint stopping Claude from
running destructive commands or exfiltrating any secret the job's environment can reach.
GitHub-hosted runners are not network-isolated — GitHub's own docs state runners "have access to
the public internet" by default — so treating "it's just a CI runner" as automatically safe is a
mistake.
**Caveat / contested:** Anthropic's own guidance is internally debated: the general Best Practices
docs say to use this mode only in a sandbox "without internet access," while the reference
devcontainer documentation recommends the flag for a container that *does* have outbound network
access to an allowlist (GitHub, npm, the Claude API, DNS, SSH) — a community-filed issue against
`anthropics/claude-code` (#19978, opened 22 Jan 2026) flagged this contradiction directly;
Anthropic closed it as "not planned"/stale without a public resolution. Read this as: allowlisted
egress reduces but does not eliminate exfiltration risk versus true air-gapping. **Bottom line for
a first-time reader:** if you don't already know your threat model well enough to weigh that
tradeoff, don't use this flag in CI at all, full stop — use the narrower modes in the next
practice instead.
**Sources:** [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) (fetched 10 Aug 2026) · [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 10 Aug 2026) · [github.com/anthropics/claude-code issue #19978](https://github.com/anthropics/claude-code/issues/19978) (opened 22 Jan 2026) · [GitHub Docs — Private networking with GitHub-hosted runners ("By default, GitHub-hosted runners have access to the public internet")](https://docs.github.com/en/actions/concepts/runners/private-networking) (accessed 12 Aug 2026)
**Confidence:** contested (dissent: Anthropic's own devcontainer guidance and Best Practices
guidance disagree on what counts as "isolated enough")

---

### Practice: Prefer `acceptEdits`/`dontAsk` + an explicit `--allowedTools` allowlist over `bypassPermissions` for routine CI tasks
**Do:** For a normal "run tests and fix failures" or "apply lint fixes" CI job, use
`--permission-mode acceptEdits` (auto-accepts file edits and safe filesystem commands like
`mkdir`, `mv`, `cp`) paired with an explicit allowlist for anything else Claude needs to run, e.g.
`--allowedTools "Bash(git diff *),Bash(git commit *),Bash(npm test)"` (add further
`Bash(<pattern>)` entries for anything else the job legitimately needs — don't leave a trailing
`...` in a real config). For a fully locked-down pipeline where you want to pre-approve every
capability, use `--permission-mode dontAsk`, which auto-denies any tool call not covered by your
`permissions.allow` rules or the built-in read-only command set (`ls`, `cat`, `git status`, etc.)
— there is no interactive fallback, so an unapproved action simply fails the step instead of
hanging or silently doing something unapproved.
**Why (beginner):** These modes give Claude enough autonomy to finish a well-scoped CI task
without handing it the same blanket authority as `bypassPermissions`. If the prompt is
manipulated into requesting something outside the allowlist, the run fails loudly instead of
executing it.
**Caveat / contested:** `acceptEdits` still lets other Bash commands and network requests prompt
(and therefore abort, since nothing can answer the prompt in `-p` mode) unless covered by
`--allowedTools` — a run can fail simply because you under-scoped the allowlist, which is a
usability tradeoff against `bypassPermissions`'s convenience. All three sources below are
Anthropic-hosted docs pages — treated as **one publisher**, not independent corroboration, per
this corpus's sourcing rule.
**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 10 Aug 2026) · [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 10 Aug 2026) · [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) — example job uses `--permission-mode acceptEdits` with a scoped `--allowedTools` list (fetched 10 Aug 2026)
**Confidence:** vendor-documented (all three sources are Anthropic-hosted docs pages; treated as
one publisher per the independence rule)

---

### Practice: ⚠️ Cap spend and iteration with `--max-turns` and `--max-budget-usd`
**Do:** Pass `--max-turns <N>` to bound how many agentic turns a single `-p` run can take (the run
exits with an error once the limit is reached, rather than looping indefinitely), and
`--max-budget-usd <amount>` to hard-cap API spend for that run — spend from subagents counts
toward the cap, and once the cap is hit, new subagent spawns fail with `Budget limit reached` and
in-flight background subagents are stopped (requires Claude Code v2.1.217 or later 🕒 verify
live). Also set a workflow-level timeout (GitHub Actions `timeout-minutes` / GitLab `timeout`) as
a second, independent backstop, and use CI concurrency controls to cap parallel runs.
**Why (beginner):** An unattended agent that gets stuck in a retry loop, or is asked to do
something open-ended, can otherwise keep calling the API (and consuming GitHub Actions minutes)
until someone notices — this is exactly the kind of "leave it running overnight" mistake that
generates a surprise bill.
**Caveat / contested:** Both flags are turn/spend caps on a single invocation, not an org-wide
budget; use the usage dashboard or OpenTelemetry export for fleet-wide spend tracking. **Update
(shipped 3 days before this snapshot):** Claude Code v2.1.225 (2026-08-07) added org/gateway-level
spend-limit support — when a Claude Gateway–routed org hits its configured cap, the CLI surfaces
a named limit, a reset time, and an operator message. This is a separate mechanism from the
per-invocation flags above (fleet-wide vs. single run) — relevant if you're tracking spend across
many CI jobs rather than one run. 🕒 verify live.
**Sources:** [code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference) (fetched 10 Aug 2026) · [hidekazu-konishi.com — "Claude Code in CI/CD and Headless Automation"](https://hidekazu-konishi.com/entry/claude_code_cicd_and_headless_automation.html) by Hidekazu Konishi (first published 7 Jun 2026) · [github.com/anthropics/claude-code releases — v2.1.225](https://github.com/anthropics/claude-code/releases/tag/v2.1.225) (fetched 11 Aug 2026) · [dev.classmethod.jp — v2.1.226 update roundup](https://dev.classmethod.jp/en/articles/20260808-cc-updates-v2-1-226/) (fetched 11 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: Keep secrets out of the prompt and out of the transcript; prefer CI secret stores and OIDC over static keys in the environment
**Do:** Never paste a credential into a Claude Code prompt or pipe a file containing secrets into
`claude -p` as context. Store `ANTHROPIC_API_KEY` (or cloud-provider credentials) as a masked/
protected secret in your CI provider (GitHub Actions secrets, GitLab CI/CD variables) and inject
it only into the step that needs it. Where your CI provider and Claude Code's provider both
support it (Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or Anthropic's own
workload identity federation for GitHub Actions), authenticate via OIDC instead of a stored
long-lived key.
**Why (beginner):** A CI transcript or log is often more widely readable than the secret store
itself (other maintainers, build artifacts, sometimes public logs on OSS repos) — anything that
ends up in Claude's prompt, tool output, or the `-p` transcript can leak that way even if the
underlying secret store is locked down.
**Caveat / contested:** GitHub Actions withholds repository secrets from workflow runs triggered
by a fork's pull request by default — this is a real protection, but it also means a review
workflow gated on secrets simply won't run on fork PRs (a common source of "why didn't Claude
review this PR" confusion), and `pull_request_target` reintroduces secret access to fork-triggered
runs (see Part 1), so use it cautiously.
**Sources:** [code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions) — "Protect your credentials" (fetched 10 Aug 2026) · [code.claude.com/docs/en/gitlab-ci-cd](https://code.claude.com/docs/en/gitlab-ci-cd) — "Never commit API keys or cloud credentials..." (fetched 10 Aug 2026) · [hidekazu-konishi.com — "Claude Code in CI/CD and Headless Automation"](https://hidekazu-konishi.com/entry/claude_code_cicd_and_headless_automation.html) by Hidekazu Konishi (first published 7 Jun 2026)
**Confidence:** independently-corroborated

---

### Practice: In CI, load MCP servers only via an explicit, reviewed `--mcp-config` + `--strict-mcp-config`
**Do:** Pass `claude --strict-mcp-config --mcp-config ./ci-mcp.json` so Claude Code uses **only**
the MCP servers you name in that file for the run, ignoring any other MCP configuration source
(project `.mcp.json`, user `~/.claude.json`, plugin-bundled servers, claude.ai connectors). Check
`ci-mcp.json` into version control and review changes to it like any other CI config.
**Why (beginner):** In interactive use, a project's `.mcp.json` normally requires you to approve
it before its servers connect. That approval prompt **cannot appear** in `-p`/headless mode —
project-scoped MCP servers load automatically without asking. Combined with the fact that
first-time trust verification is also disabled non-interactively, a CI job that doesn't pin its
MCP config could silently start an MCP (Model Context Protocol) server (and its tools/
credentials) that nobody explicitly approved for that pipeline. `--strict-mcp-config` closes that
gap by making the CI job's tool surface fully explicit.
**Caveat / contested:** I could not find an independent (non-Anthropic) source discussing
`--strict-mcp-config` specifically — treat this practice as sourced to Anthropic's own docs only.
An open bug (`anthropics/claude-code` #14490) reports that `--strict-mcp-config` does **not**
override a `disabledMcpServers` list already set in `~/.claude.json` — so the "fully explicit tool
surface" this flag promises can have an exception on a runner where that file happens to carry
stale disables. 🕒 verify live — check the issue's status before relying on `--strict-mcp-config`
alone. When you *do* pass `--mcp-config` with `-p`, Claude Code waits (up to the `MCP_TIMEOUT`,
30s default) for pending servers to connect before the first turn; check the `system/init`
event's `mcp_server_errors` field (requires v2.1.219+) 🕒 verify live to catch a server that
failed validation and was silently skipped, since no stderr warning prints when stderr is
captured by a CI runner.
**Sources:** [code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference) (fetched 10 Aug 2026) · [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 10 Aug 2026) · [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) — "Trust verification is disabled when running non-interactively with the -p flag" (fetched 10 Aug 2026) · [github.com/anthropics/claude-code issue #14490](https://github.com/anthropics/claude-code/issues/14490) (fetched 11 Aug 2026)
**Confidence:** thin (single publisher — all Anthropic docs — despite four separate pages)

---

### Practice: Fail the CI job explicitly when a plugin or MCP server fails to load, instead of letting the run continue silently
**Do:** With `--output-format stream-json`, read the `system/init` event's `plugin_errors` and
`mcp_server_errors` arrays. Both are non-empty only when something failed to load (the key is
omitted entirely when there are no errors); add a pipeline check that fails the job if either
array is non-empty, rather than assuming an empty tool list means "nothing was configured."
**Why (beginner):** Claude Code is deliberately fault-tolerant here — a misconfigured
`--mcp-config` entry (e.g. a `url` with no `type`) is skipped and the run continues cleanly
rather than crashing. That's the right default for interactive use, but in CI it means a broken
MCP integration can go unnoticed for a long time unless you check for it explicitly.
**Caveat / contested:** This requires Claude Code v2.1.219 or later 🕒 verify live for the
`mcp_server_errors` field; on older versions you'd only see a stderr warning, which most CI
runners capture and hide rather than surface.
**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 10 Aug 2026)
**Confidence:** thin (single vendor source, could not find independent corroboration)

---

## Part 3 — Codex CLI

Covers OpenAI's `codex exec` (non-interactive mode), as documented at
[learn.chatgpt.com/docs](https://learn.chatgpt.com/docs/non-interactive-mode) on 10 Aug 2026.
Codex CLI ships roughly weekly point releases (current at time of Timekeeper's 11 Aug 2026
re-check: `rust-v0.147.0`, well past every version gate cited below); treat version numbers as
🕒 verify live.

### Practice: Use `codex exec` for every non-interactive/CI invocation
**Do:** Invoke `codex exec "<task>"` (not the interactive `codex` TUI) for scripts, cron jobs, and
CI steps. It runs one task to completion, streams progress to **stderr**, prints only the final
agent message to **stdout**, and exits — so it composes cleanly with `grep`/`jq`/shell pipelines
(`cat prompt.txt | codex exec -`, or `curl … | codex exec "summarize this"`).
**Why (beginner):** Automation needs a command that doesn't wait for a human to click through a
chat UI and doesn't mix "thinking out loud" text into the output your pipeline parses. `codex
exec` is built specifically for that; the interactive TUI is not scriptable.
**Caveat / contested:** `--full-auto` still works but is a deprecated compatibility flag that
prints a warning — official docs say to prefer the explicit `--sandbox workspace-write` flag in
new scripts. (One independent source describes `--full-auto` as "forcing" the sandbox to
`workspace-write` and overriding `--sandbox` — that's a description of the flag's mechanics, not a
disagreement with the vendor's deprecation notice; both can be true at once.)
**Sources:** [learn.chatgpt.com/docs/non-interactive-mode](https://learn.chatgpt.com/docs/non-interactive-mode) (fetched 10 Aug 2026, vendor) · [developersdigest.tech/blog/codex-exec-ci-headless-guide](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide) (published 10 Jun 2026, updated 28 Jun 2026) · [developertoolkit.ai/en/codex/advanced-techniques/non-interactive/](https://developertoolkit.ai/en/codex/advanced-techniques/non-interactive/) (published 8 Feb 2026, updated 6 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: Rely on `codex exec`'s default read-only sandbox, and escalate access explicitly and narrowly
**Do:** Know that `codex exec` defaults to the `read-only` sandbox — no writes anywhere,
including `/tmp` — with the approval policy governing everything else. Only add `--sandbox
workspace-write` when the task genuinely needs to edit files, and treat `--sandbox
danger-full-access` as inappropriate for CI unless the runner itself is a disposable, fully
isolated container/VM.
**Why (beginner):** Unlike some agent CLIs, Codex's safe default is actually the *most*
restrictive mode — that protects you if a script forgets to pass sandbox flags. But it's easy to
accidentally widen access (e.g., copy-pasting `--sandbox workspace-write` or
`danger-full-access` from an interactive-use tutorial into a CI job) and lose that protection.
**Caveat / contested:** Vendor docs state this plainly on the page that governs non-interactive
use ("By default, `codex exec` runs in a read-only sandbox with minimal permissions"); a separate
vendor page on approvals/security phrases its non-interactive guidance as a recommendation to use
`codex exec --sandbox workspace-write` rather than as a statement of the default — read that as
advice for a specific use case, not a contradiction of the documented default. Both independent
sources below confirm the read-only default verbatim as well.
**Sources:** [learn.chatgpt.com/docs/non-interactive-mode](https://learn.chatgpt.com/docs/non-interactive-mode) (fetched 10 Aug 2026, vendor) · [learn.chatgpt.com/docs/developer-commands?surface=cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) (fetched 10 Aug 2026, vendor) · [developersdigest.tech/blog/codex-exec-ci-headless-guide](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide) (published 10 Jun 2026, updated 28 Jun 2026) · [developertoolkit.ai/en/codex/advanced-techniques/non-interactive/](https://developertoolkit.ai/en/codex/advanced-techniques/non-interactive/) (published 8 Feb 2026, updated 6 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: ⚠️ Never use `--dangerously-bypass-approvals-and-sandbox` (`--yolo`) on a shared or GitHub-hosted CI runner
**Do:** Reserve `--dangerously-bypass-approvals-and-sandbox` (aka `--yolo`) — which disables
*both* sandboxing and approval prompts — for a runner you already treat as a disposable,
single-purpose sandbox (an ephemeral container/VM with no other secrets or shared state). For
ordinary CI, use `--sandbox workspace-write` plus an explicit `--ask-for-approval never` (or the
config equivalent) so the task can run unattended without a human clicking "approve," while
file/network access stays bounded.
**Why (beginner):** This flag removes the two safety nets that stop a misbehaving or
prompt-injected agent from running arbitrary destructive commands with full filesystem and
network access. In CI, nobody is watching the run in real time, so there's no human backstop
either — a bad outcome here can mean deleted files, exfiltrated secrets, or unexpected outbound
network calls, all unattended.
**Caveat / contested:** Official docs label it verbatim "Elevated Risk... not recommended," note
it works "with all `--sandbox` modes," and give **no guidance blessing it for headless/unattended
runs specifically** — treat it as a documented-but-discouraged option, not a vendor-endorsed
headless workaround. It is still not forbidden outright, so external sandboxing (a genuinely
disposable container/VM) is the mitigation if you use it at all.
**Sources:** [learn.chatgpt.com/docs/agent-approvals-security](https://learn.chatgpt.com/docs/agent-approvals-security) (fetched 10 Aug 2026, vendor) · [vincentschmalbach.com — "How Codex CLI Flags Actually Work (Full-Auto, Sandbox, and Bypass)"](https://www.vincentschmalbach.com/how-codex-cli-flags-actually-work-full-auto-sandbox-and-bypass/) (published 15 Jan 2026)
**Confidence:** independently-corroborated (vendor + one independent source on the flag's
mechanics; the independent source does not use the `--yolo` alias)

---

### Practice: Gate pipeline steps on `codex exec`'s exit code
**Do:** Check `$?` after `codex exec` — it exits non-zero on failure (e.g., the agent errors out
or a required MCP server fails to initialize) — and branch your CI logic (rollback, alert, block
merge) accordingly, e.g. `if ! codex exec --sandbox workspace-write "run migration and verify
schema"; then echo "failed" >&2; exit 1; fi`. (A database migration is a deliberately
higher-stakes example — pair this pattern with the "require human review" practice below rather
than letting a migration apply-and-verify loop run fully unattended.)
**Why (beginner):** Automation only works if failure is machine-detectable. Without checking the
exit code, a CI step that "ran" but actually failed silently continues, and you ship a broken
change.
**Caveat / contested:** The exact taxonomy of non-zero exit codes (partial failure vs. total
failure vs. tool error) is not comprehensively documented anywhere found this run — treat exit
code as a binary success/fail signal only, don't rely on specific numeric codes.
**Sources:** [developertoolkit.ai/en/codex/advanced-techniques/non-interactive/](https://developertoolkit.ai/en/codex/advanced-techniques/non-interactive/) (published 8 Feb 2026, updated 6 Aug 2026)
**Confidence:** thin (single source confirms exit-code behavior specifically)

---

### Practice: Use `--json` for machine-parseable output instead of scraping free text
**Do:** Add `--json` to get a newline-delimited JSON event stream (thread/turn/item events) for
detailed progress parsing, or `-o/--output-last-message <path>` to capture just the final message.
Vendor docs also describe `--output-schema <path>`, which validates Codex's final answer against a
JSON Schema you provide — useful for feeding structured results (e.g. a triage report) straight
into another tool (`jq`, a ticketing API, etc.), though this specific flag was not independently
verified this run.
**Why (beginner):** Parsing an LLM's free-form prose in a script is fragile — wording changes will
silently break your pipeline. Structured/JSON output gives you a stable contract to parse against.
**Caveat / contested:** `--output-schema` validates the *final* response shape, not intermediate
tool calls — it won't stop the agent from taking unwanted actions along the way, only shape its
final answer. Treat the schema-validation claim as vendor-only-and-unchecked; `--json` itself is
independently confirmed.
**Sources:** [learn.chatgpt.com/docs/developer-commands?surface=cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) (fetched 10 Aug 2026, vendor) · [developersdigest.tech/blog/codex-exec-ci-headless-guide — confirms `--json` specifically](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide) (published 10 Jun 2026, updated 28 Jun 2026)
**Confidence:** independently-corroborated on `--json`; vendor-only (thin) on `--output-schema`

---

### Practice: Prefer the official `openai/codex-action` GitHub Action over hand-installing the CLI
**Do:** For GitHub Actions specifically, use `openai/codex-action@v1` rather than manually
installing Codex and wiring up `~/.codex/auth.json` or a raw `OPENAI_API_KEY` env var. Configure
it with a `permission-profile` (`:read-only` and `:workspace` are confirmed built-in profiles;
requires Codex CLI ≥0.138.0 — a third `:danger-full-access` value is reported in some
documentation but was **not independently confirmed** this run, so verify it exists on your
pinned version before relying on it) or the older `sandbox` input (not both — the action does not
pass `--sandbox` when `permission-profile` is set, and supplying both fails before Codex starts),
a `prompt`/`prompt-file`, and pin `codex-version` so the CLI doesn't silently drift underneath
your workflow. Explicitly rely on `safety-strategy: drop-sudo` (the action's default, which
revokes `sudo` membership on Linux/macOS before Codex runs) or `safety-strategy:
unprivileged-user` (run Codex as a separate non-privileged account) — see the next practice for
why this matters even in a read-only sandbox.
**Why (beginner):** The Action installs the CLI, starts a local Responses-API proxy that holds
your API key server-side (so it doesn't sit in a plain env var inside the job), and applies a
documented privilege-reduction strategy by default — doing all of this by hand is easy to get
wrong.
**Caveat / contested:** Permission profiles are explicitly labeled "beta" and don't compose with
the legacy `sandbox`/`sandbox_mode` settings — mixing the two is a documented misconfiguration to
avoid. 🕒 verify live: the `0.138.0` minimum version and available profile names will move as the
Action evolves. The independent source below confirms only the general "installs the CLI, starts
the Responses API proxy" pattern, not the specific `permission-profile`/version-pinning mechanics.
**Sources:** [learn.chatgpt.com/docs/github-action](https://learn.chatgpt.com/docs/github-action) (fetched 10 Aug 2026, vendor) · [github.com/openai/codex-action](https://github.com/openai/codex-action) (fetched 10 Aug 2026, vendor) · [smartscope.blog/en/generative-ai/chatgpt/codex-cli-github-actions](https://smartscope.blog/en/generative-ai/chatgpt/codex-cli-github-actions/) (published 10 Mar 2026)
**Confidence:** vendor-documented

---

### Practice: ⚠️ Don't trust the `read-only` sandbox alone to protect your API key on GitHub-hosted runners
**Do:** In `openai/codex-action`, explicitly rely on `safety-strategy: drop-sudo` or
`safety-strategy: unprivileged-user` as described above. Don't assume "read-only sandbox + no
network" is sufficient on its own.
**Why (beginner):** GitHub-hosted runners ship with **passwordless `sudo` by default**. Linux
exposes running processes' environment variables as files under `/proc` (a virtual filesystem
called procfs) — anyone with `sudo` can read them, even from a process they didn't start. So even
in a `read-only` sandbox with network disabled, a process with `sudo` can read another process's
memory/environment via `/proc`, which can expose your `OPENAI_API_KEY` even though the sandbox
never let Codex "write" anything. The read-only sandbox restricts what Codex's own shell commands
can *do*, not what a privileged process can *read* — this is exactly the kind of risk a beginner
would assume the earlier "safe default" practice already covers, and it doesn't.
**Caveat / contested:** This exact mechanism (procfs + passwordless sudo defeating read-only
sandboxing) is documented by OpenAI's own `codex-action` security doc; a second, independent
(non-OpenAI) publisher describing this specific procfs technique was not found this run — labeled
vendor-documented rather than independently-corroborated. Treat it as credible (it's the vendor
disclosing a limitation of its own product against itself) but single-sourced.
**Sources:** [github.com/openai/codex-action/blob/main/docs/security.md](https://github.com/openai/codex-action/blob/main/docs/security.md) (fetched 10 Aug 2026, vendor)
**Confidence:** vendor-documented (single publisher; flagged as a real risk despite thin sourcing
because it's a vendor security disclosure about its own defaults)

---

### Practice: Never set `OPENAI_API_KEY` or `CODEX_API_KEY` as a job-level environment variable in a workflow that runs repo-controlled code
**Do:** Avoid `env: OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}` at the job or workflow level in
any pipeline that also runs test scripts, third-party Actions, or dependency lifecycle hooks
(npm/pip install scripts) — those processes run in the same job and can read that env var too.
Prefer the official Action's proxy (key never touches the CLI process env directly), or if you
must set a key for a bare `codex exec` call, inject it inline for a single invocation only:
`CODEX_API_KEY=<key> codex exec "task"` (note: `CODEX_API_KEY` is supported only by `codex exec`,
not the interactive CLI).
**Why (beginner):** In CI, "your" job often executes code you didn't write (test suites, npm
postinstall scripts, third-party Actions) — if the API key sits in a job-wide env var, all of
that code can read and exfiltrate it, not just Codex.
**Caveat / contested:** Also treat `~/.codex/auth.json` (used for ChatGPT-account login instead of
an API key) as sensitive as a password — it's what you'd use if you ran `codex login` interactively
rather than setting an API key, and official docs explicitly say don't use that login-based auth
flow for public/open-source repos at all.
**Sources:** [learn.chatgpt.com/docs/non-interactive-mode](https://learn.chatgpt.com/docs/non-interactive-mode) (fetched 10 Aug 2026, vendor) · [eastondev.com/blog/en/posts/ai/20260726-codex-security-sandbox-permission-secrets](https://eastondev.com/blog/en/posts/ai/20260726-codex-security-sandbox-permission-secrets/) (published 26 Jul 2026)
**Confidence:** independently-corroborated

---

### Practice: 🕒 There is no *enforced* per-run spend cap in the Codex CLI today — set a usage budget at the OpenAI account/platform level
**Do:** Before scheduling any recurring/unattended Codex job (nightly cron, on every PR, etc.),
set a usage/spend limit in the OpenAI platform dashboard for the API key or project you're using,
and pick a cheaper model (e.g. a "-mini" tier) for high-frequency, low-stakes tasks (log triage,
PR summaries) versus a stronger model only for fix-generation work.
**Why (beginner):** A CI job that runs on every commit or every PR can multiply an otherwise-small
per-call cost very quickly, and a runaway loop (e.g., a retry-on-failure step that keeps calling
`codex exec`) has had no CLI-side circuit breaker — your only protection has been the
platform-level usage cap.
**Caveat / contested:** OpenAI's live config reference now documents an experimental
`[features.rollout_budget]` block (`enabled`, `limit_tokens`, `reminder_interval_tokens`, and
token-weight settings) — an official, if experimental, token-budget config surface that did not
exist (or wasn't documented) when this topic was last checked. However, the underlying
implementation pull requests explicitly state this feature "only defines and validates
configuration and does not track usage, inject reminders, or stop a rollout" — so as of this
snapshot it is tracking/reminder scaffolding, **not an enforced cap**. The headline claim above
("don't assume a flag/setting protects you") remains true today, but this is an actively-developing
area — 🕒 verify live whether `features.rollout_budget` has gained real enforcement before you rely
on the platform-dashboard workaround being your only option.
**Sources:** [developersdigest.tech/blog/codex-exec-ci-headless-guide](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide) (published 10 Jun 2026, updated 28 Jun 2026) · [learn.chatgpt.com/docs/config-file/config-reference](https://learn.chatgpt.com/docs/config-file/config-reference) (fetched 11 Aug 2026) · [github.com/openai/codex pull #28746](https://github.com/openai/codex/pull/28746), [#28494](https://github.com/openai/codex/pull/28494), [#29423](https://github.com/openai/codex/pull/29423) (fetched 11 Aug 2026)
**Confidence:** thin on the specific absence-of-enforcement claim (single source per sub-claim,
now time-sensitive)

---

### Practice: Require human review before merge even when Codex runs "unattended" in CI
**Do:** Use unattended Codex runs (autofix bots, PR review bots) to *propose* changes — open a PR,
post a review comment — rather than to push directly to a protected branch. OpenAI's own
reference autofix workflow explicitly ends with a human checking the diff before merging
("Check to see if everything looks good and then merge it").
**Why (beginner):** "Non-interactive" describes how Codex runs, not how much you should trust its
output unsupervised. An agent acting on CI failures, logs, or PR content can be steered by
injected instructions hidden in that content (prompt injection) — a human review step is your
last check before a bad or manipulated change lands in your codebase.
**Caveat / contested:** Sourcing here is vendor-documented (the official cookbook example)
reinforced by one independent source describing the same general "review the diff, run tests,
prepare a rollback plan" pattern as a second line of defense beyond the permission boundary.
**Sources:** [developers.openai.com/cookbook/examples/codex/autofix-github-actions](https://developers.openai.com/cookbook/examples/codex/autofix-github-actions) (fetched 10 Aug 2026, vendor) · [eastondev.com/blog/en/posts/ai/20260726-codex-security-sandbox-permission-secrets](https://eastondev.com/blog/en/posts/ai/20260726-codex-security-sandbox-permission-secrets/) (published 26 Jul 2026)
**Confidence:** independently-corroborated

---

## Part 4 — Gemini CLI

Covers Google's `gemini` CLI in headless mode, as documented at
[geminicli.com/docs](https://geminicli.com/docs/cli/headless/) on 10 Aug 2026. This part covers
**CI/CD and non-interactive automation only** — general Gemini CLI sandboxing, authentication
basics, and MCP/extension security are covered in RingS's existing security-fundamentals/
authentication-and-data/extensions-mcp-security entries (snapshot 2026-08-01) and are not
repeated here.

### Practice: Use headless (`-p`/`--prompt`) mode, never the interactive REPL, in CI jobs
**Do:** Invoke `gemini -p "your prompt"` (or pipe input via stdin, e.g. `git diff | gemini -p
"write a commit message"`). Headless mode is triggered automatically in any non-TTY environment,
or explicitly with `-p`/`--prompt`; it "bypasses the interactive chat interface and prints the
response to standard output." Do not attempt to run the plain interactive `gemini` REPL inside a
CI job — it expects a terminal and will not behave predictably in a runner.
**Why (beginner):** CI runners have no human to click "approve" or read a chat UI. Headless mode
is the difference between a script that finishes and exits, and a job that hangs until it times
out (and still gets billed for runner minutes).
**Caveat / contested:** Exact flag names have not always been stable across versions — a GitHub
issue from Sept 2025 (gemini-cli v0.5.4) showed `--output-format` rejected as an "unknown
argument" even though it was documented at the time. Verify against `gemini --help` for the
version you pin in CI. 🕒 verify live.
**Sources:** [geminicli.com/docs/cli/headless](https://geminicli.com/docs/cli/headless/) (Google, updated 10 Mar 2026) · [geminicli.com/docs/cli/tutorials/automation](https://geminicli.com/docs/cli/tutorials/automation/) (Google, updated 9 Mar 2026) · [github.com/google-gemini/gemini-cli issue #9009](https://github.com/google-gemini/gemini-cli/issues/9009) (opened 20 Sep 2025, historical flag-parsing bug)
**Confidence:** vendor-documented (the `-p` usage pattern is also described on a well-known Gemini
CLI blog post, but its author is a Google Director of Engineering — not an independent publisher
for a Google product, so it doesn't count as separate corroboration here)

---

### Practice: Use `--output-format json`/`stream-json` and check the exit code, not just stdout text
**Do:** For scripts that need to parse the result, pass `--output-format json` (a single JSON
object with a `response` field plus `stats`/`error` metadata) or `--output-format stream-json`
(newline-delimited JSONL events: `init`, `message`, `tool_use`, `tool_result`, `error`, `result`).
Check the process exit code rather than assuming success from non-empty output: per vendor docs,
`0` = success, `1` = general error/API failure, `42` = input error (bad prompt/args), `53` = turn
limit exceeded.
**Why (beginner):** Grepping raw text output is fragile — the model's wording changes run to run.
Structured JSON plus an exit-code check lets a pipeline reliably decide "did this succeed" without
guessing from prose.
**Caveat / contested:** This exit-code table and JSON schema come from a single vendor source and
could not be independently corroborated this run; treat the exact numeric codes as 🕒 verify live
and confirm against your pinned version before wiring pipeline logic to specific exit codes.
**Sources:** [geminicli.com/docs/cli/headless](https://geminicli.com/docs/cli/headless/) (Google, updated 10 Mar 2026)
**Confidence:** vendor-documented (thin on the specific exit-code values — single source)

---

### Practice: Authenticate CI with an API key or service account, not a personal Google login
**Do:** In pipelines, set `GEMINI_API_KEY` (from Google AI Studio) for the simplest path, or for
Vertex AI set `GOOGLE_API_KEY` + `GOOGLE_GENAI_USE_VERTEXAI=true`, or use a service-account JSON
via `GOOGLE_APPLICATION_CREDENTIALS` with `GOOGLE_CLOUD_PROJECT`/`GOOGLE_CLOUD_LOCATION`. Google's
own docs recommend the service-account/API-key path explicitly "in non-interactive environments,
CI/CD pipelines, or if your organization restricts user-based [Application Default Credentials] or
API key creation." Store the key as an encrypted repo/CI secret, never as a plaintext env line in
a checked-in workflow file.
**Why (beginner):** Interactive "Login with Google" OAuth is built for a human clicking through a
browser consent screen — it doesn't work headlessly in a runner, and using a personal account's
login in shared CI infrastructure also means every job runs "as you," which is a bad blast radius
if the job is compromised.
**Caveat / contested:** None significant found — this is consistent, vendor-and-independent-agreed
guidance. Do treat the key itself as a secret (see Part 1's secrets-handling practice).
**Sources:** [geminicli.com/docs/get-started/authentication](https://geminicli.com/docs/get-started/authentication/) (Google, updated 17 Apr 2026) · [apidog.com/blog/gemini-cli-github-actions](https://apidog.com/blog/gemini-cli-github-actions/) (Apidog, independent, 29 Jan 2026)
**Confidence:** independently-corroborated

---

### Practice: Use the official `run-gemini-cli` GitHub Action, and scope its GitHub token tightly
**Do:** Add `GEMINI_API_KEY` (or Workload Identity Federation credentials for GCP-based auth) as a
repo secret, then either run `/setup-github` from an interactive Gemini CLI session to scaffold
`.github/workflows/`, or copy examples from the action repo's `examples/workflows` directory.
Prefer a custom GitHub App over the default `GITHUB_TOKEN` when the workflow needs to comment/
label/push ("Custom GitHub App (Recommended): For the most secure and flexible authentication"),
and set an explicit minimal `permissions:` block rather than accepting the default broad token
scope. Pin the action to a specific released version rather than a floating tag.
**Why (beginner):** The GitHub token an Action gets by default can be broader than the job
actually needs. If a compromised or manipulated Gemini CLI run can use that token, tight scoping
limits what it can do — turning "attacker can do anything to your repo" into "attacker can read
issues."
**Caveat / contested:** The independent source below confirms `GEMINI_API_KEY` as a repo secret
and the general action reference, but does not corroborate the specific `permissions:`-block or
version-pinning advice (it in fact uses a floating `@v1` tag in its own example) — that half of
this practice is vendor-only. Free-tier request quotas cited by different sources vary by date
(see the quota practice below), so treat any specific numbers there as 🕒 verify live.
**Sources:** [github.com/google-github-actions/run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli) (Google, accessed 10 Aug 2026) · [blog.google — Introducing Gemini CLI GitHub Actions](https://blog.google/technology/developers/introducing-gemini-cli-github-actions/) (Google, 6 Aug 2025) · [apidog.com/blog/gemini-cli-github-actions](https://apidog.com/blog/gemini-cli-github-actions/) (Apidog, independent, 29 Jan 2026)
**Confidence:** vendor-documented (independent source corroborates only the general secret/action
setup, not the permissions-scoping or pinning specifics)

---

### Practice: ⚠️ Do not blanket-enable `--yolo` on workflows that process untrusted content (PRs/issues from outside contributors)
**Do:** Reserve `--yolo` / `--approval-mode=yolo` (auto-approve every tool call, no confirmation)
for workflows that only ever touch trusted, maintainer-authored input. For anything that reads
content an outside contributor controls (a PR body, an issue, a commit message), instead use
`--approval-mode=auto_edit` (auto-approves file edits only) or a scoped `tools.allowed` allowlist
in `settings.json` (e.g. `["run_shell_command(git)"]`) restricted to read-only tools like
`list_directory`, `read_file`, `grep_search`. Prefer maintainer-triggered workflows (manual
dispatch, or gated on a maintainer's own comment) over workflows that auto-run on any fork's PR.
**Why (beginner):** `--yolo` exists so unattended pipelines don't hang waiting for an approval
that will never come — but it also means anything the model is tricked into "deciding" to run (via
text hidden in a PR/issue) executes immediately, with no human in the loop to say no. A real,
patched advisory (GHSA-wpqr-6v78-jr5g, CVSS 10.0) confirmed that *before* the patch, `--yolo` mode
ignored the fine-grained `tools.allowed`/`tools.core` allowlist in `settings.json` entirely — so
even teams who thought they'd scoped `--yolo` down were not actually protected. (A separate,
more severe failure bundled into the same advisory — automatic command execution that doesn't
even require `--yolo` — is covered in the next practice; don't conflate the two.)
**Caveat / contested:** The GitHub Security Advisory itself (GHSA-wpqr-6v78-jr5g, published 24 Apr
2026, patched in `@google/gemini-cli` 0.39.1 / `run-gemini-cli` 0.1.22) reads verbatim "No known
CVE" in its own CVE field — a later article (The Hacker News, 7 Aug 2026, tied to a 5 Aug 2026
Black Hat USA talk) is the source that assigns **CVE-2026-12537** to this vulnerability family; if
you look up the advisory directly you will not see that CVE number on the page itself, which is
expected, not a sign the citation is wrong. `gemini-cli`'s npm package is actively maintained and
shipping fast (latest published version as of 8 Aug 2026 was 0.54.4, well past the 0.39.1 patch
floor) — confirm you are on a patched version; this whole space is 🕒 verify live.
**Sources:** [GHSA-wpqr-6v78-jr5g advisory ("No known CVE")](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g) (Google/GitHub, 24 Apr 2026) · [The Hacker News — "Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws"](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html) (independent, 30 Apr 2026, also states "No CVE identifier assigned" at that time) · [The Hacker News — "Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets" (assigns CVE-2026-12537)](https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html) (independent, 7 Aug 2026) · [penligent.ai — "Gemini CLI RCE, Workspace Trust and the CI/CD Agent Attack Surface"](https://www.penligent.ai/hackinglabs/gemini-cli-rce-workspace-trust-and-the-ci-cd-agent-attack-surface/) (independent, 28 Apr 2026)
**Confidence:** independently-corroborated (multiple non-Google publishers corroborate the
GitHub-published advisory)

---

### Practice: ⚠️ Set workspace-trust env vars deliberately — never assume a CI workspace is "trusted" by default
**Do:** Only set `GEMINI_CLI_TRUST_WORKSPACE=true` in a workflow's `env:` block when the workflow
exclusively processes trusted input (repo-owner or high-trust-collaborator authored code/prompts).
For workflows that can be triggered by outside contributors (public-repo issues/PRs), harden the
workflow first (least-privilege token permissions, tool allowlisting per the practice above, no
secrets exposed to the job) before ever setting this to true. Earlier CLI versions auto-trusted
the workspace folder in any non-interactive/CI run, which is what let a malicious `.gemini/.env`
file execute arbitrary environment-variable-driven code — the underlying vulnerability this
variable exists to let you control (CVE-2026-12537, CVSS 10.0) is a workspace-auto-trust →
OS-command-injection bug in the container launcher, reached via a crafted `.gemini/.env` file, and
fires **before the sandbox even starts** — it does not require `--yolo` at all.
**Why (beginner):** "Trusting the workspace" means letting the CLI load and act on config files/
environment variables sitting in the checked-out repo — which, in a public repo, could have been
placed there by an attacker's PR, not by you.
**Caveat / contested:** **Naming conflict, disclosed rather than papered over:** the security
advisory itself uses the variable name `GEMINI_TRUST_WORKSPACE`, while the current, actively
maintained trust-guidance documentation uses `GEMINI_CLI_TRUST_WORKSPACE` — an independent source
(Penligent) explicitly flags this discrepancy and recommends following the current official docs.
Using the wrong spelling silently no-ops a security control, so double-check the exact variable
name against live docs before relying on it. ⚠ PENDING: this run could not confirm what the
*current* default is when neither variable is set at all — the trust-guidance doc explains what to
do if you *do* set it, but does not state plainly whether an unset workspace is trusted or
untrusted today post-patch. Until that's confirmed, treat an unset workspace-trust variable as an
unknown, not a safe default, and set your posture explicitly either way.
**Sources:** [run-gemini-cli trust-guidance.md](https://github.com/google-github-actions/run-gemini-cli/blob/main/docs/trust-guidance.md) (Google, accessed 10 Aug 2026) · [GHSA-wpqr-6v78-jr5g advisory](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g) (Google/GitHub, 24 Apr 2026) · [penligent.ai](https://www.penligent.ai/hackinglabs/gemini-cli-rce-workspace-trust-and-the-ci-cd-agent-attack-surface/) (independent, 28 Apr 2026)
**Confidence:** independently-corroborated

---

### Practice: Treat AI output as untrusted before it touches secrets or merges — guard against prompt-injection secret exfiltration
**Do:** Never pipe raw untrusted content (a PR title, issue body, or commit message written by an
outside contributor) directly into a Gemini CLI prompt in a job that also has access to repository
secrets. Rotate and scope GitHub Actions secrets narrowly, keep jobs that touch untrusted input
separate from jobs that hold deployment/cloud credentials, and require human review before any
Gemini-CLI-authored change is merged or applied — don't let the CLI auto-apply changes in an
untrusted-input workflow.
**Why (beginner):** Attackers have demonstrated (a technique dubbed "PromptPwnd" in one write-up)
that hidden instructions inside a GitHub comment or issue can manipulate an AI agent running in
Actions into leaking `GEMINI_API_KEY`, `GITHUB_TOKEN`, or other secrets available to that job —
the AI doesn't know the difference between "instructions from the repo owner" and "instructions an
attacker snuck into a comment."
**Caveat / contested:** Details of exactly which secrets are exfiltrable vary by the specific bug/
version; treat this as a class of risk to design against, not a single patched CVE you can "fix
and forget." The write-up naming "PromptPwnd" (07 Dec 2025) predates the April 2026 advisory above
by four months and describes a different, earlier prompt-injection issue — cited here as
class-of-risk evidence, not as the same bug.
**Sources:** [The Hacker News — "Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets"](https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html) (independent, 7 Aug 2026) · [hoploninfosec.com — "Gemini CLI GitHub Actions Vulnerability Causing Secret Leaks"](https://hoploninfosec.com/gemini-cli-github-actions-vulnerability-fix) (independent, 7 Dec 2025) · [run-gemini-cli trust-guidance.md](https://github.com/google-github-actions/run-gemini-cli/blob/main/docs/trust-guidance.md) (Google, accessed 10 Aug 2026)
**Confidence:** independently-corroborated

---

### Practice: Budget for quota limits and rate-limit backoff before running Gemini CLI at scale in CI
**Do:** Know your tier's request limits before wiring Gemini CLI into a loop (e.g. "run once per
file" over a large repo) — as of Google's own quota page (updated 18 Jun 2026), an unpaid Gemini
API key is capped at roughly 250 model requests/user/day and restricted to the Flash-class model;
paid individual/workspace tiers scale to 1,500–2,000/day, with pay-as-you-go token billing on
Vertex AI or a paid API key for uncapped-but-metered use. Add retry/backoff for 429-style quota
errors rather than letting a CI job fail hard or silently loop-retry without delay, and prefer
precise, single-shot prompts over chatty multi-call scripts (bulk "one call per file" loops burn
quota fast).
**Why (beginner):** A CI job that fans out one Gemini CLI call per file in a large repo can blow
through a daily quota in minutes, or — on a paid key — run up an unexpectedly large bill, without
anyone noticing until later.
**Caveat / contested:** The same quota page also lists "around 1,000 requests/day" for a
Google-account/Code-Assist free-login path — but see the next practice: Google stopped serving
that exact free/personal-login path on 18 Jun 2026, the **same day** this quota page was last
updated. That row is very likely stale/unscrubbed vendor content rather than a currently-purchasable
tier; don't budget a pipeline against it. The 250/1,500/2,000 figures for API-key and paid tiers
are unaffected by that cutoff and were confirmed live as of this run. 🕒 verify live regardless —
these numbers move often.
**Sources:** [geminicli.com/docs/resources/quota-and-pricing](https://geminicli.com/docs/resources/quota-and-pricing/) (Google, updated 18 Jun 2026) · [apidog.com/blog/gemini-cli-github-actions](https://apidog.com/blog/gemini-cli-github-actions/) (Apidog, independent, 29 Jan 2026)
**Confidence:** independently-corroborated on the general practice of budgeting/backoff; the exact
numeric quotas are single-source-per-date and explicitly flagged verify-live

---

### Practice: Know the Gemini CLI → Antigravity CLI transition — CI/CD using an API key, Vertex AI, or an Enterprise Code Assist license is explicitly unaffected
**Do:** Be aware that as of 18 Jun 2026, Google stopped serving Gemini CLI / Gemini Code Assist
requests for personal "Login with Google" OAuth access — free tier, Google AI Pro, and Google AI
Ultra individual sign-in — directing those users to the new Antigravity CLI instead. Google's own
transition announcement states plainly: "Gemini CLI will remain accessible via paid Gemini and
Gemini Enterprise Agent Platform API keys" — so a pipeline authenticating with `GEMINI_API_KEY` or
a Vertex AI service account is explicitly, not just inferentially, unaffected. A third path is
also confirmed unaffected: Gemini Code Assist Standard/Enterprise licenses and Google
Cloud-based Gemini Code Assist for GitHub continue to receive updates. The `gemini-cli` npm
package / `run-gemini-cli` GitHub Action remain actively maintained as an Apache-2.0 open-source
project. If your CI pipeline was set up to log in with a personal Google account (rather than an
API key or service account), it will have already broken.
**Why (beginner):** If your team originally set up a Gemini CLI GitHub Action or script months ago
by copy-pasting `gemini login` into a runner (rather than an API key), your pipeline may have been
silently failing since mid-June 2026 — this is worth an active check, not an assumption.
**Caveat / contested:** The announcement is silent specifically on whether it covers every
possible Vertex-AI-adjacent auth configuration exhaustively — the three confirmed-unaffected paths
above (API key, Vertex AI service account, Enterprise Code Assist license) cover the mechanisms
most CI pipelines actually use, but if your setup is unusual, verify against the live announcement
rather than assuming coverage. 🕒 verify live given how fast this transition is moving.
**Sources:** [developers.googleblog.com — "An important update: Transitioning Gemini CLI to Antigravity CLI" ("Gemini CLI will remain accessible via paid Gemini and Gemini Enterprise Agent Platform API keys")](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) (Google, 19 May 2026) · [yaw.sh/blog/gemini-cli-not-free-alternatives](https://yaw.sh/blog/gemini-cli-not-free-alternatives/) (independent, 25 Jul 2026)
**Confidence:** independently-corroborated

---

### Practice: Never set `DEBUG` as an environment variable in Gemini CLI CI jobs
**Do:** Avoid setting a `DEBUG` environment variable in any CI environment running Gemini CLI. The
official Action docs warn this causes the CLI to hang waiting for a Node.js debugger to attach —
which in CI just means the job runs until it times out.
**Why (beginner):** It's an easy mistake if your pipeline already sets `DEBUG=*` for some other
tool (a common Node.js convention) — that same variable being visible to Gemini CLI's process can
silently stall an unrelated job.
**Caveat / contested:** Single-source; could not find independent corroboration this run.
**Sources:** [github.com/google-github-actions/run-gemini-cli README](https://github.com/google-github-actions/run-gemini-cli) (Google, accessed 10 Aug 2026)
**Confidence:** thin (single source, narrow but easy-to-hit footgun)

---

## Held pending fixes (not publish-ready)
- Whether the *current* default is "trusted" or "untrusted" when neither `GEMINI_TRUST_WORKSPACE`
  nor `GEMINI_CLI_TRUST_WORKSPACE` is set at all — the trust-guidance doc explains what to do if
  you *do* set it, but not the unset-default state. Set your posture explicitly rather than rely
  on an unconfirmed default. ⚠ PENDING
- Cross-provider comparison of API-key-level spend/rate-limit mechanics for OpenAI and Google
  specifically (beyond Codex's config-scaffolding and Gemini's quota page, both covered above) —
  only Anthropic's Enterprise-tier Spend Limits API was checked directly against the question "does
  this protect a bare CI API key," and the answer there was "not necessarily." ⚠ PENDING
- No independent (non-Anthropic) source verifying `--strict-mcp-config` behavior in CI specifically,
  and no citable source describing a concrete, off-the-shelf way to enforce a hard (blocking, not
  audit-only) network-egress allowlist on an ephemeral GitHub-hosted runner. ⚠ PENDING
- Whether OpenAI's `openai/codex-action` `permission-profile` truly ships a `:danger-full-access`
  value (only `:read-only` and `:workspace` were independently confirmed this run). ⚠ PENDING
- No full, officially enumerated exit-code table exists for either Claude Code (only 0/non-zero/143
  are documented) or Codex CLI (binary success/fail only) — noted as a caveat rather than a gap,
  since the absence itself is the honest answer.
- GitLab CI/CD integration for Claude Code is described as "currently in beta" and "maintained by
  GitLab" per Anthropic's own docs; no GitLab-published (truly independent-publisher) page
  confirming the same setup steps was reached this run — treated as an Anthropic-hosted vendor
  source only, not independent corroboration. ⚠ PENDING

## CHANGELOG (grading → this entry)
1. Initial pupil drafts (4: Claude Code, Codex CLI, Gemini CLI, cross-provider/generic) —
   research-only, ungraded.
2. **[Skeptic FIX-CC1]** Claude Code root/sudo refusal claim was cited to `/docs/en/permissions`,
   which does not contain it — re-cited to `/docs/en/permission-modes`, and added the material
   "skipped automatically inside a recognized sandbox" caveat the original citation omitted.
3. **[Skeptic FIX-CC2]** Dropped composio.dev as a source for the root/sudo-refusal and
   GitHub-runner-network claims in the `bypassPermissions` practice — it doesn't support either.
4. **[Skeptic FIX-CC3 + new sourcing]** The "GitHub-hosted runners have outbound network access by
   default" claim was uncited — fetched and added
   [docs.github.com — Private networking with GitHub-hosted runners](https://docs.github.com/en/actions/concepts/runners/private-networking)
   ("By default, GitHub-hosted runners have access to the public internet") as a direct citation.
5. **[Skeptic FIX-CC4]** Relabeled the `claude-code-action` GitHub App practice from
   independently-corroborated to vendor-documented — systemprompt.io corroborates only the general
   `permissions:`/`ANTHROPIC_API_KEY` pattern, not the GitHub-App-specific mechanics it was
   credited for.
6. **[Skeptic FIX-CC5]** Removed "for CI runners" from the composio.dev citation on the cap-spend
   practice — composio's actual statement is general-purpose, not CI-specific.
7. **[Skeptic FLAG-CC6]** Corrected the Konishi blog's first-published date from "6 Jun 2026" to
   "7 Jun 2026" in all three citations (byline verified).
8. **[Skeptic FLAG-CC7 / KILL-GEN2, merged]** Moved and correctly re-scoped the CVE-2026-44246
   mention from the generic cross-provider draft (where it was misattributed to `pull_request_target`
   and to "GitHub Agentic Workflows" the product) into the Claude Code `allowed_non_write_users`
   practice, where the vulnerability actually applies (a specific project's workflow, triggered by
   `issues.opened` + an overly permissive allowlist, not `pull_request_target`) — added
   GHSA-63mx-j37w-gh59 and Tenable's CVE-2026-44246 page as sources, and removed the false
   "documented exploitation in the wild for this CVE" claim (Rescana's own text says it is not in
   CISA's KEV catalog; the in-the-wild campaigns it documents are different incidents).
9. **[Skeptic FLAG-CC8 + new sourcing]** The "unnamed scopes reset to `none`" claim was uncited —
   fetched and added [docs.github.com — Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
   as a direct citation.
10. **[Skeptic — model behavior]** Kept the honest "treated as one publisher" independence notes on
    the `--strict-mcp-config` and `acceptEdits`/`dontAsk` practices as-is; the Skeptic called these
    out as the standard the rest of the corpus should copy.
11. **[Skeptic KILL-CX1]** Codex `--yolo` practice: removed the claim that vendor docs "document it
    as a real, supported option for headless runs" — they don't; replaced with the actual verbatim
    label ("Elevated Risk... not recommended," works "with all `--sandbox` modes," no headless
    endorsement). Removed developertoolkit.ai as a source (doesn't mention the bypass flag at all).
12. **[Skeptic FIX-CX2]** Downgraded the exit-code practice to thin/single-sourced —
    developersdigest.tech doesn't cover exit codes despite being cited for them.
13. **[Skeptic FIX-CX3]** Downgraded the no-spend-cap practice's sourcing to thin —
    smartscope.blog doesn't cover OpenAI platform spend/usage limits despite being cited for them.
14. **[Skeptic FIX-CX4]** Dropped smartscope.blog from the human-review practice — it doesn't
    discuss review gates before merge and its own operational advice arguably cuts the other way.
15. **[Skeptic FIX-CX5]** Relabeled the `openai/codex-action` practice to vendor-documented —
    smartscope corroborates only the general pattern, not `permission-profile`/pinning specifics —
    and flagged the `:danger-full-access` profile name as unconfirmed rather than asserting it.
16. **[Skeptic FIX-CX6]** Rewrote the read-only-sandbox-default caveat: the vendor's own
    non-interactive-mode page states the read-only default plainly; removed the framing that made
    it sound like the practice rested mainly on blogs.
17. **[Skeptic FLAG-CX7]** Split confidence on the `--json`/`--output-schema` practice —
    `--json` is independently corroborated, `--output-schema` remains vendor-only/unchecked.
18. **[Skeptic FLAG-CX8]** Clarified that vincentschmalbach's "`--full-auto` forces workspace-write"
    description and the vendor's deprecation notice are not in tension — different facts about the
    same flag, not competing claims.
19. **[Skeptic FIX-GM1]** Re-anchored the CVE-2026-12537 attribution to the 7 Aug 2026 Hacker News
    article that actually assigns it, and explicitly disclosed that the GHSA advisory itself and the
    30 Apr 2026 Hacker News piece both say "no CVE" at the time they were written.
20. **[Skeptic FIX-GM2]** Rewrote the `--yolo` practice's "Why" paragraph — the CVSS 10.0 finding is
    the workspace-auto-trust → command-injection bug (covered in its own practice), not the
    `--yolo`-ignores-allowlist finding; the two were conflated in the original draft.
21. **[Skeptic FIX-GM3]** Disclosed the `GEMINI_TRUST_WORKSPACE` (advisory) vs.
    `GEMINI_CLI_TRUST_WORKSPACE` (current docs) naming discrepancy explicitly, per Penligent's
    reporting, instead of silently picking one spelling.
22. **[Skeptic KILL-GM4]** Rewrote the Antigravity-transition caveat: the vendor announcement
    explicitly states API-key CI/CD is unaffected (a direct quote was available, contra the
    original draft's claim that this was only "read between the lines"); removed the now-resolved
    "held pending" item.
23. **[Skeptic KILL-GM5]** Relabeled the headless-mode practice to vendor-documented — the
    "independent" blog corroborating it is written by a Google Director of Engineering, not a
    second independent publisher. Dropped the DeepWiki citation on the `--yolo` practice for the
    same reason plus its own low-authority/AI-generated/wrong-vintage issues.
24. **[Skeptic FIX-GM6]** Relabeled the `run-gemini-cli` Action practice to vendor-documented —
    apidog corroborates only the general secret/action setup, not the permissions-scoping or
    version-pinning specifics.
25. **[Skeptic FIX-GM7]** Removed the false "held pending" claim that the CSA research note 404s —
    it loads fine; it just isn't cited in Part 4 since it doesn't cover this specific CVE (it is
    correctly cited in Part 1, where it does apply).
26. **[Skeptic FLAG-GM9]** Reconciled the internal contradiction between the quota practice's
    "1,000/day free tier" figure and the Antigravity practice's cutoff of that same free/personal-
    login path on the same date — annotated the quota row as likely stale rather than presenting
    both as equally current.
27. **[Skeptic FLAG-GM10]** Removed the unattributed phrase "Comment and Control" (not used by its
    cited source) and kept "PromptPwnd," which the source does use.
28. **[Skeptic FLAG-CC/GM/GEN11 + FLAG-GEN7]** Normalized all pupil-research citation dates from the
    inconsistent "accessed 2026-08-11" (a day after the pupils' actual 10 Aug 2026 research pass) to
    "10 Aug 2026," while leaving grading-panel-only citations dated 11 Aug 2026 (when the panel
    itself re-fetched them) as-is.
29. **[Skeptic KILL-GEN1]** Rewrote the Copilot-review caveat: the cited GitHub Docs page is an
    anti-self-approval rule for the human who prompted the agent, not a claim that Copilot's bot
    review "only ever leaves a Comment, never an Approve" (which the page doesn't say).
30. **[Skeptic KILL-GEN3]** Rewrote the sandboxing/monitoring practice's Do and Why to match what
    its sources actually support (Harden-Runner as audit-mode *monitoring*, not a blocking
    network-egress allowlist) and removed the unverifiable "updated 4 Aug 2026" date on the
    StepSecurity citation. Downgraded confidence accordingly and moved the "no citable source found
    for a hard egress allowlist on an ephemeral runner" gap to Held Pending.
31. **[Skeptic FIX-GEN4]** Removed the unlinked, unverifiable "GitHub Discussion — Renovate/
    Dependabot" citation from the idempotency practice; it now stands on the GitHub Concurrency doc
    alone (still labeled thin).
32. **[Skeptic FIX-GEN5]** Standardized on the `github.github.io` hostname for both `gh-aw`
    reference-doc citations (both resolve; picked one canonical host).
33. **[Timekeeper]** Added the Claude Code v2.1.225 (2026-08-07, 3 days pre-snapshot) org/gateway
    spend-limit feature to the cap-spend practice, since it postdated the pupil's research window.
34. **[Timekeeper]** Added the `--strict-mcp-config` / `disabledMcpServers` known-gap caveat
    (`anthropics/claude-code` #14490) to the MCP-config practice.
35. **[Timekeeper]** Upgraded the Codex no-spend-cap practice with the newly-documented (but
    not-yet-enforcing) `features.rollout_budget` config surface, correcting the pupil's "does not
    exist" framing to "exists but doesn't enforce yet."
36. **[Timekeeper]** Resolved the GitHub Actions 360-minute default-timeout item from ⚠ PENDING to a
    confirmed, cited fact (still 🕒 verify live per corpus convention for config defaults).
37. **[Timekeeper]** Broadened the Antigravity-transition "unaffected" list with a third confirmed
    path (Gemini Code Assist Standard/Enterprise + Google Cloud-based Code Assist for GitHub), and
    added the current `gemini-cli` npm version (0.54.4, ~8 Aug 2026) for freshness context.
38. **[Beginner panel]** Added a corpus-wide glossary (MCP, OIDC, ephemeral/self-hosted runner,
    procfs/`/proc`, GitHub App vs. `GITHUB_TOKEN`) after the labels legend.
39. **[Beginner panel]** Completed the `--allowedTools` example that previously ended in a bare
    trailing `...`, which the panel flagged as copy-pasteable-but-broken.
40. **[Beginner panel]** Added a one-line plain-language explanation of procfs/`/proc` and
    passwordless sudo at the point the Codex practice uses that jargon.
41. **[Beginner panel]** Added a concrete, illustrative worked "safe skeleton" GitHub Actions
    workflow (Part 1) tying together permissions, triggers, timeouts, pinning, and the safe-outputs
    two-job split that every individual practice covers only in prose.
42. **[Beginner panel]** Added an explicit cross-reference from the Claude Code permissions-scoping
    practice back to Part 1's human-approval-gate practice, closing the gap where Claude Code was
    the only one of the three tool-specific parts without its own "don't let this merge unattended"
    statement.
43. **[Beginner panel]** Added a one-line caveat to the Codex exit-code practice's database-migration
    example, pointing back to the human-review practice rather than implying an unattended
    migrate-and-verify loop is safe as shown.
44. **[Beginner panel]** Added a concrete illustrative example (a small JSON "intended action" blob
    and a two-job description) to the previously fully-abstract "safe outputs" practice in Part 1.
