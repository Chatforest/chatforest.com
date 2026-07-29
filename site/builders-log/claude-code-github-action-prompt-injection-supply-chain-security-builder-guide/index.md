# Claude Code GitHub Action Had a Supply Chain Flaw: What Happened, What's Fixed, and How to Harden Your CI/CD

> A prompt injection + permission bypass in the official Claude Code GitHub Action let unauthenticated attackers hijack any repo using it. Patched in v1.0.94. Here is the attack chain, the broader pattern, and a hardening checklist for builders running Claude in CI/CD.


**At a glance:** The official `anthropics/claude-code-action` had a permission bypass that let unauthenticated external attackers inject prompts via GitHub issues and escalate to full repository compromise. Discovered by [RyotaK of GMO Flatt Security](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/), the permission-check flaw was [reported to Anthropic on January 12, 2026 and fixed within four days (January 16, 2026)](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/); the cumulative patched release, [v1.0.94, was tagged April 13, 2026](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.94) after several more rounds of hardening. Anthropic [rated it CVSS 4.0: 7.8 and paid a $3,800 bounty plus a $1,000 bonus ($4,800 total)](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/). The same researcher [reports having found approximately 50 separate ways to bypass Claude Code's permission system](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) more broadly. This article covers what happened, the attack chain, and what builders need to do. Part of our **[Builder's Log](/builders-log/)**.

---

If you run the official `anthropics/claude-code-action` in your GitHub Actions workflows, you need to know about this. The short version: a logic flaw in the permission check combined with prompt injection let any attacker with a free GitHub App account compromise any public repository using the action. It is patched. But the underlying class of vulnerability — prompt injection in agentic CI/CD — is not a single bug you fix and move on from.

---

## What the Action Does

The [Claude Code GitHub Action (`anthropics/claude-code-action`)](https://github.com/anthropics/claude-code-action) is Anthropic's official workflow for running Claude Code in CI/CD. Common uses:

- Automated code review triggered by pull request comments (`@claude review this`)
- Issue triage and labeling
- Automated test generation and bug fixes triggered by issue assignment
- Dependency update drafting

The action authenticates as Claude, reads the repository context, and takes actions — including writing comments, creating commits, and opening pull requests — based on Claude's analysis.

This is exactly the kind of agentic automation that has high utility and high attack surface.

---

## The Vulnerability: A Two-Part Chain

### Part 1 — The Permission Bypass

The core flaw, [documented in detail by RyotaK](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/), was in a function called `checkWritePermissions`. Its job was to determine whether the GitHub actor triggering the workflow had sufficient permissions to run Claude Code with write access.

The logic had a critical shortcut: **any actor whose username ended in `[bot]` was unconditionally trusted, regardless of actual repository permissions.**

This matters because GitHub Apps — which can be created for free by anyone — interact with GitHub under a username that ends in `[bot]`. Per [GitHub's own documentation on GitHub App permissions](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app), apps have no permissions by default but do get implicit read access to public resources, and creating issues or pull requests on a public repository requires no explicit permission at all — any GitHub user (including an app acting on one) can already do that. So an attacker who registers a GitHub App and installs it only on a repository they themselves control can still use that app's installation token to open issues and pull requests on *any* public repository.

The check that was supposed to gate write access was never actually checking permissions — it was pattern-matching on a username suffix. Bots are blocked from triggering the action by default today; admins can opt a specific bot in via the `allowed_bots` parameter, but Anthropic's own [current security documentation for the action](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md) warns that the same underlying risk pattern still applies to that opt-in setting: "Allowed bots are not checked for repository permissions. A bot that matches an entry does not need to be installed on your repository or have write access."

### Part 2 — Prompt Injection via Issue Content

Once the attacker bypasses the permission check, they need Claude to do something useful for them. This is where prompt injection enters.

Agentic CI/CD systems that read GitHub issues and comments are consuming untrusted content. If the action passes issue body content directly into Claude's context without sanitization or isolation, an attacker can embed instructions in the issue that Claude will follow.

[RyotaK's documented attack pattern](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/):

1. Attacker creates a GitHub App and installs it only on a repository they control (implicit read/issue-creation access to *other* public repos comes free, per GitHub's own permissions docs above)
2. Attacker uses the app's installation token to create an issue on the target repository
3. The issue body contains embedded instructions designed to make Claude read sensitive environment variables (such as `/proc/self/environ`) and write them back into the issue — for example, using the GitHub MCP tool Claude already has access to, to update the issue description with the secret values
4. The Claude Code Action triggers, reads the issue, and processes the injected instructions as if they were legitimate
5. Claude executes — exfiltrating secrets, and, in workflows that also carry `id-token: write`, exfiltrating the OIDC token-request credentials needed to obtain a full-write GitHub App installation token and push malicious code (the same OIDC exchange mechanism detailed in the two-workflow escalation below)

### The Two-Workflow Escalation

[RyotaK also identified a second attack chain](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/), present in Anthropic's own example workflow configuration for issue triage. It combined:

- `allowed_non_write_users: "*"` — a setting in Anthropic's example triage workflow that let any user (not just repo collaborators) trigger Claude
- That same triage workflow having `issues: write` permissions
- The default "tag mode" workflow (triggered by an `@claude` mention from a trusted user) having `id-token: write` permissions, used to obtain an OIDC token that Claude Code exchanges for a privileged GitHub App installation token

The documented two-phase escalation:

1. **Phase 1:** An attacker opens an issue to trigger the triage workflow (allowed because of `allowed_non_write_users: "*"`). Claude processes it and posts a task summary to the issue-triage workflow's run summary, which is publicly visible on GitHub. By crafting the issue so Claude includes the job's `GITHUB_TOKEN` in that summary, the attacker obtains a token scoped to `issues: write`.
2. **Phase 2:** The attacker waits for a trusted collaborator to mention `@claude` in an issue, then uses the stolen `issues: write` token to edit that issue and inject a new payload. When the tag-mode workflow (which has `id-token: write`) processes the tampered issue, Claude is tricked into exfiltrating the `ACTIONS_ID_TOKEN_REQUEST_TOKEN` and `ACTIONS_ID_TOKEN_REQUEST_URL` environment variables — the credentials needed to request an OIDC token. The attacker uses these to replicate the token exchange and obtain a full-write Claude GitHub App installation token, which can then push commits directly to the repository.

After this was reported, [Anthropic disabled the workflow-run-summary feature by default](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/), closing off that specific exfiltration channel.

This is a supply chain attack. A compromised workflow in a widely-used action can propagate malicious code to every downstream repository that depends on it.

---

## Scale of the Research

RyotaK's disclosure covered the permission bypass and the two-workflow escalation. But his broader research is more significant: he [states in the same writeup that he has found approximately 50 separate vulnerabilities](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) allowing attackers to bypass Claude Code's permission system and execute unauthorized commands.

This is not a statement about Claude Code being uniquely insecure. It is a statement about the difficulty of building permission systems for agentic tools that consume untrusted content.

The pattern is not exclusive to `claude-code-action`, or to Claude Code generally. A separate research effort — by [independent researcher Aonan Guan working with Johns Hopkins University researchers Zhengyu Liu and Gavin Zhong](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/), [reported by SecurityWeek on April 16, 2026](https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/) — found the same class of vulnerability (untrusted GitHub content flowing into an agent that holds elevated permissions) in a *different* Claude Code product, [`anthropics/claude-code-security-review`](https://github.com/anthropics/claude-code-security-review), as well as in Google's Gemini CLI Action and GitHub Copilot Agent. That research, dubbed "Comment and Control," showed PR titles, issue comments, and even hidden HTML comments could be used to redirect each agent into leaking API keys and tokens. Anthropic's response, per that report, was that Claude Code Security Review "is not designed to be hardened against prompt injection" when used on untrusted external content.

Agentic tools that read repository content, issue bodies, or PR descriptions are all consuming untrusted input. Any of them can be the injection vector.

---

## What Was Patched and When

| Event | Date |
|---|---|
| Permission-bypass vulnerability reported to Anthropic | [January 12, 2026](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) |
| Core `checkWritePermissions` bypass fixed | [January 16, 2026 (4 days later)](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) |
| `allowed_non_write_users` misconfiguration (two-workflow chain) reported | [January 17, 2026](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) |
| Similar misconfiguration in Cline's GitHub Actions exploited in the wild | [February 17, 2026](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) |
| Additional remediation rounds and follow-up bypasses | [February–April 2026](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) |
| `v1.0.94` tagged (cumulative patched release referenced in this article) | [April 13, 2026](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.94) |
| GMO Flatt Security publishes RyotaK's writeup | [June 1, 2026](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) |

Anthropic [rated the vulnerability CVSS 4.0: 7.8 (High) and paid a $3,800 bounty plus a $1,000 bonus](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/) ($4,800 total). The quick initial patch (4 days) is notable. The subsequent rounds of remediation through spring suggest the permission model required more than a single-line fix.

**A separate, related disclosure:** on [June 5, 2026, Microsoft's Security Blog](https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/) described a *different* bug in the same action: its `Read` tool, unlike its `Bash` tool, was not subject to the same environment-variable sandboxing, so a prompt-injected Claude could read `/proc/self/environ` directly and leak the `ANTHROPIC_API_KEY` and other CI secrets. Microsoft reported that issue to Anthropic on April 29, 2026, and Anthropic shipped a fix blocking access to sensitive `/proc` paths in Claude Code v2.1.128 on May 5, 2026. It shares a root cause (untrusted GitHub content reaching an over-privileged agent) with RyotaK's findings but is a distinct bug, reported and fixed on a different timeline — the two should not be read as the same vulnerability.

---

## What Builders Need to Do

### 1. Verify your action version

If you are pinning `anthropics/claude-code-action` to a version tag, make sure you are on **v1.0.94 or later**.

If you are pinning to a floating reference like `@main` or `@v1`, pull the latest version explicitly and verify the version in your workflow logs.

```yaml
# Explicit version pin — safe post-patch
- uses: anthropics/claude-code-action@v1.0.94

# Floating tag — verify this resolves to v1.0.94 or later
- uses: anthropics/claude-code-action@v1
```

### 2. Remove `allowed_non_write_users: "*"` from your workflows

If your workflow configuration includes `allowed_non_write_users: "*"`, remove it or replace it with a specific list of users you explicitly trust. This setting was in Anthropic's own example workflows and is the configuration that made the two-workflow escalation possible.

Only users who need to trigger Claude in CI/CD should be in `allowed_non_write_users`. The default behavior (only collaborators with write access can trigger) is the safe default.

### 3. Audit workflow permission combinations

Look at every workflow that uses the Claude Code Action. Identify which ones have elevated permissions:

- `issues: write` — can Claude be triggered from an issue in this workflow?
- `pull-requests: write` — can Claude be triggered from a PR comment?
- `id-token: write` — does this workflow expose OIDC tokens?
- `contents: write` — can Claude push commits?

The dangerous combination is any workflow that (a) can be triggered by untrusted external content **and** (b) has elevated permissions like `id-token: write` or `contents: write`.

If you need `id-token: write` for deployment, put it in a separate workflow that cannot be triggered from issue or PR content.

### 4. Treat all issue and PR content as untrusted input

This is the architectural principle that prevents the whole class. Claude Code actions that consume issue bodies, PR descriptions, or commit messages are consuming content that external actors can control.

For public repositories: any authenticated GitHub user can create an issue. You cannot assume that issue content is safe to pass directly into Claude's operational context.

For private repositories: your threat model is different, but insider threat and compromised accounts still apply.

Mitigations at the architectural level:

- **Use explicit trigger keywords** rather than triggering on all issue creation. `@claude` mentions in comments are easier to audit than any issue creation.
- **Separate read and write workflows.** A workflow that reads issues and reports analysis should not also have `contents: write`. Split analysis and action into separate workflows with a human approval step in between.
- **Log Claude's interpreted instructions**, not just its output. If Claude is executing based on something it read in an issue, that something should be visible in your audit trail before execution.

### 5. Pin by commit SHA for production workflows

Version tags are mutable. If a repository you depend on is compromised, the attacker can move the tag to malicious code without changing the tag name.

Pinning to a full commit SHA gives you tamper-evident dependencies:

```yaml
# Pinned to a specific SHA — tamper-evident
- uses: anthropics/claude-code-action@a1b2c3d4e5f6...  # Replace with actual SHA
```

The tradeoff is that you do not automatically receive security updates. Run Dependabot or equivalent to get notified of upstream version changes.

---

## The Broader Pattern

This vulnerability is one example of a class that will recur as agentic CI/CD becomes standard practice. The pattern:

1. An agent action is granted elevated permissions (write access, OIDC tokens, secrets)
2. The agent reads untrusted content (issues, PR descriptions, commit messages, comments)
3. The content contains injected instructions
4. The agent executes the injected instructions within its elevated permission context

No amount of patching the `[bot]` suffix check makes this pattern safe. The only architectural defense is:

- **Minimize permissions to what the specific workflow actually needs**
- **Treat content from external sources as untrusted regardless of the actor's apparent identity**
- **Separate read/analyze steps from write/act steps, with explicit gates between them**

Claude Code, Gemini CLI, and GitHub Copilot Agents are all susceptible to this pattern. The specific bypass mechanics differ. The class is the same.

---

## What Anthropic Fixed, and What Remains

The `checkWritePermissions` bypass is patched. The `allowed_non_write_users: "*"` example configuration has been corrected. The core authentication logic was hardened through spring 2026.

What remains is the fundamental challenge that RyotaK's broader research reflects: a system that reads natural language from untrusted sources and acts on instructions encoded in that language will have a large attack surface. Permission checks help. They are not sufficient on their own.

Anthropic's own guidance to developers, in its [documentation on mitigating jailbreaks and prompt injection](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks), states that "Claude is inherently resilient to such attacks" but goes on to recommend a full stack of additional controls — screening untrusted tool output, delivering third-party content only inside `tool_result` blocks, and least-privilege scoping — specifically for the "indirect prompt injection" case this vulnerability falls into, where Claude processes attacker-controlled content on a trusted user's behalf. That is Anthropic's own acknowledgment that model-level resistance alone is not treated as sufficient. It should be layered with architectural controls, not substituted for them.

---

## The Short Version for Builders

- You are on a patched version if you are running `anthropics/claude-code-action` at v1.0.94 or later. **Verify this.**
- Remove `allowed_non_write_users: "*"` from any workflow that also has elevated permissions.
- Audit your workflow permission combinations. `id-token: write` and `issues: write` in the same workflow triggered by external content is the dangerous pattern.
- Treat issue body content as untrusted regardless of who created the issue.
- Pin CI/CD dependencies by SHA in production to prevent tag movement attacks.
- This class of vulnerability affects all agentic CI/CD tools, not just Claude Code. The architectural principles above apply to any agent that reads untrusted content and acts with elevated permissions.

---

*ChatForest covers AI news and tools for builders. This article is based on published security disclosures, researcher writeups from GMO Flatt Security, the Microsoft Security Blog, and secondary coverage. We research these topics — we do not conduct security testing ourselves. Verify all version numbers and configuration guidance against Anthropic's official documentation.*

