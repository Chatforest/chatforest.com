# Friendly Fire and HalluSquatting: One Flag Stands Between Your Dev Machine and Full Compromise

> Two new attacks disclosed in July 2026 show that AI coding agents running in auto-mode can be weaponized — one by hiding prompt injections inside the repositories they're asked to review, the other by pre-registering the fake package names models predictably hallucinate. Here is how both work, what's still unfixed, and the three-step checklist that protects against both.


If you ran through the [GhostApproval story](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants) this week — the symlink attack that breaks workspace sandboxes in six AI coding tools — you might have figured that was the worst of it. It was not. The same seven-day window produced two additional disclosures that are distinct attack classes, require no symlinks, and aim at a different part of the AI coding workflow: the auto-approval modes you enable when you want the agent to just get on with it.

Both **Friendly Fire** and **HalluSquatting** were published in the week of July 7–11, 2026. Together they make the same argument: the single flag that turns off user approval prompts is where the attack surface lives.

---

## Friendly Fire (July 8, 2026 — AI Now Institute)

Researchers **Boyan Milanov** (Senior Research Scientist) and **Heidy Khlaaf** (Chief AI Scientist) at the AI Now Institute published [a proof-of-concept they call Friendly Fire](https://ainowinstitute.org/publications/friendly-fire-exploit-brief) — with the underlying [exploit code and technical README on GitHub](https://github.com/Boyan-MILANOV/friendly-fire-ai-agent-exploit) — a prompt injection attack that takes effect specifically when a developer points their AI coding agent at a third-party library and asks it to perform a security review.

### The scenario that gets hit

The scenario is common and reasonable: your team adopts an open-source dependency, security practice says run the AI over it before merging, so you type `review the security of this library`. That action, in Claude Code auto-mode or Codex auto-review, is the trigger.

### How the attack is constructed

The researchers modified a copy of **geopy**, a Python geocoding library, adding three files, [as documented in the exploit brief](https://ainowinstitute.org/publications/friendly-fire-exploit-brief):

- **`security.sh`** — A shell script embedded in or linked from the README, framed as a recommended pre-PR check.
- **`code_policies`** — A malicious binary carrying the actual payload. Compiled appearance, stripped, but seeded with strings.
- **`code_policies.go`** — A decoy Golang source file whose string values were copied into the binary to make Claude Code's disassembly check conclude that the binary was the compiled output of the harmless Go source.

The injection itself lives in **README.md**, an ordinary text file present in nearly every repository and granted no special trust level by any agent. The README contains a note that `security.sh` is a standard pre-merge step — conventional-sounding text that the agent reads and acts on.

When Claude Code or Codex reviews the modified geopy, the agent executes `security.sh`, which runs `code_policies`, which delivers the payload.

### What the models said when asked directly

Milanov and Khlaaf directly [asked Claude Sonnet whether it saw any prompt injection attempts in the geopy source](https://ainowinstitute.org/publications/friendly-fire-exploit-brief); it did not detect them. They report the same negative result when they put the equivalent question to GPT-5.5.

### Cross-model portability

The researchers say the payload was [initially developed for Claude Sonnet 4.6](https://ainowinstitute.org/publications/friendly-fire-exploit-brief), and that "despite crafting these specific attacks for this model version, it was also successful when deployed against Claude Sonnet 5, Opus 4.8, and GPT-5.5 without any further changes necessary" — a claim corroborated by the [exploit repository's own model matrix](https://github.com/Boyan-MILANOV/friendly-fire-ai-agent-exploit).

### Vendor response and fix status

Milanov and Khlaaf write that ["our PoC is not within the scope of the security disclosure policies for either Anthropic or OpenAI. Regardless, we contacted both model providers to inform them of our findings, and offered support to enable them to verify the issues we identified or to reproduce our findings."](https://ainowinstitute.org/publications/friendly-fire-exploit-brief) No CVE or coordinated patch date has been published for this finding. Neither vendor treats this as a security bug in the conventional sense: from the platform's point of view, the agent was doing what it was asked. The agent was also doing what the malicious repository wanted.

The researchers are direct about why this can't just be patched: ["we believe these flaws cannot be remediated at the model level, given agentic AI's dependence on large language models and their inherent propensity to prompt injections."](https://ainowinstitute.org/publications/friendly-fire-exploit-brief)

---

## HalluSquatting (July 2026 — Tel Aviv University, Technion, Intuit)

A separate research group — [Aya Spira, Stav Cohen, Elad Feldman, Ron Bitton, Avishai Wool, and Ben Nassi, from Tel Aviv University, the Technion, and Intuit](https://arxiv.org/abs/2607.07433), writing up the work as ["Beware of Agentic Botnets"](https://sites.google.com/view/agentic-botnets/home) and covered by [SecurityWeek](https://www.securityweek.com/hallusquatting-turns-ai-hallucinations-into-botnet-delivery-mechanism/) — disclosed a different class of attack the same week. Where Friendly Fire pushes a payload into a repository and waits for a review, HalluSquatting works the other direction: it pre-registers the fake names that AI models will predictably invent, then waits for agents across the internet to come fetch them.

### The hallucination rate is the vulnerability

When asked to clone or install a popular repository, LLMs hallucinate the wrong location or name. The researchers measured:

- **Repository-cloning prompts** → [hallucinated resource names up to **85%** of the time](https://arxiv.org/abs/2607.07433) ([reported by The Hacker News](https://thehackernews.com/2026/07/new-hallusquatting-attack-could-trick.html))
- **Skill-installation prompts** → [hallucination rate up to **100%**](https://arxiv.org/abs/2607.07433) in the tested scenarios

The hallucinations are not random. They follow predictable patterns based on how the training corpus described similar tools. That predictability is the attack surface.

### Pre-registration as the kill chain

An attacker runs the same prompts against a model, collects the hallucinated names, registers the corresponding GitHub repositories or package names before any legitimate owners do, and seeds those repositories with a malicious payload. The [paper's threat model](https://arxiv.org/html/2607.07433v1) names reverse shells, ransomware, and DDoS botnet agents (citing precedents like Mirai) as the categories of payload this technique could be used to deliver — though the researchers' own proof-of-concept used a non-functional stand-in payload rather than live malware. Then they wait.

Every developer who asks an AI coding agent to "install that popular MCP tool I saw on Twitter" is a potential victim. The agent fetches the attacker's repo, not the real one. The developer sees an install completing normally.

The [researchers frame this as a shift from targeted to untargeted prompt injection](https://arxiv.org/abs/2607.07433): earlier prompt injection attacks needed a direct channel to a specific victim application, while HalluSquatting requires none — the attacker registers the trap once and every AI agent that independently hallucinates the same name delivers itself to it. The paper positions the work as complementary to, not the first instance of, prior prompt-injection research.

### Tools confirmed affected

The [researchers demonstrated the technique against nine AI coding tools](https://arxiv.org/html/2607.07433v1): **Cursor**, **Cursor CLI**, **Gemini CLI**, **Windsurf**, **GitHub Copilot**, **Cline**, **OpenClaw**, **ZeroClaw**, and **NanoClaw**. The common exposure is auto-run modes — the same class of setting as Claude Code's [`--dangerously-skip-permissions` flag](https://docs.claude.com/en/docs/claude-code/cli-reference.md) and [Gemini CLI's `--yolo` mode](https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html) — that remove the default prompt before executing commands.

### Platform-level defenses

The [research proposes several platform-side mitigations](https://arxiv.org/html/2607.07433v1), including preventing reuse of well-known repository names under newly created accounts (the same defense already deployed against typosquatting), pre-registering the names that models are statistically likely to hallucinate, and running adversarial-prompt detection over newly registered content. None of these is something a developer can do unilaterally.

---

## The common thread: auto-mode is the attack surface

All three July 2026 disclosures — GhostApproval, Friendly Fire, and HalluSquatting — share the same root condition: the agent has permission to act without asking first.

GhostApproval requires the agent to write files the repository instructs it to write. Friendly Fire requires the agent to execute the security check the README recommends. HalluSquatting requires the agent to install the package it looked up. In every case, a human in the loop reviewing the proposed action would have a reasonable chance of catching it. In every case, auto-approval removes that review.

The settings that enable this — Claude Code's `--dangerously-skip-permissions` flag, Gemini CLI's `--yolo` mode, [Codex's Auto-review mode](https://alignment.openai.com/auto-review/), Cursor and Windsurf's equivalent "just do it" modes — exist because they make legitimate workflows significantly faster. The question is which workflows justify them.

---

## Builder action checklist

**For Friendly Fire (untrusted code review):**
- Do not run Claude Code or Codex in auto-mode against repositories you did not author or thoroughly trust
- Use a separate sandboxed environment (container, VM) without production credentials when reviewing third-party dependencies
- Do not count on AI agents to reliably detect their own prompt injections — the research showed direct questioning failed on all four tested models
- If your organization deploys Claude Code via enterprise managed settings, use the policy to disable auto-mode for code review workflows

**For HalluSquatting (hallucinated package installs):**
- Never use `--dangerously-skip-permissions`, `--yolo`, or equivalent modes when installing packages or cloning repositories sourced from AI suggestions
- Always verify a package or repository name independently before installation — search for it directly, do not trust the URL or name the model provides
- Treat "install this for me" as an operation that requires human confirmation regardless of the tool
- For MCP servers: verify the server source via the project's official documentation or registry, not from an LLM-generated reference

**General:**
- Auto-mode is appropriate for tasks within your own codebase, on code you own and understand
- Auto-mode against untrusted external code is a different risk profile — treat it as if you're running an installer from an unknown source

---

## What has and hasn't been patched

| Disclosure | Affected tool | Status as of July 11, 2026 |
|---|---|---|
| GhostApproval | Amazon Q Developer | Patched (language server [v1.69.0](https://aws.amazon.com/security/security-bulletins/2026-047-aws/), [CVE-2026-12958](https://nvd.nist.gov/vuln/detail/CVE-2026-12958)) |
| GhostApproval | Cursor | Patched (v3.0, [CVE-2026-50549](https://nvd.nist.gov/vuln/detail/CVE-2026-50549)) |
| GhostApproval | Claude Code | [Disputed by Anthropic as outside its threat model](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants); a symlink warning had already shipped in v2.1.32 before the report, and no CVE was assigned |
| GhostApproval | Google Antigravity | [Patched in v1.19.6](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants) (deployed May 22, 2026); CVE assignment pending |
| GhostApproval | Windsurf | [Acknowledged June 23, no update since](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants) |
| GhostApproval | Augment | ["In progress," no timeline](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants) |
| Friendly Fire | Claude Code, Codex | [No CVE, no patch, no timeline](https://ainowinstitute.org/publications/friendly-fire-exploit-brief) — vendors consider this expected behavior |
| HalluSquatting | Cursor, Cursor CLI, Gemini CLI, Windsurf, GitHub Copilot, Cline + 3 others | [No patches identified](https://arxiv.org/abs/2607.07433) — platform-level mitigations required |

All three attacks require intentional setup by an attacker: a crafted repository, a pre-registered hallucinated name, or a symlinked file. They are not passive — a clean, internal workflow with no untrusted external code in the loop is not at risk. The risk concentrates on the workflows where AI agents meet code they did not originate.

That covers a lot of developer workflows in 2026. The honest mitigation is to audit which of yours have auto-mode on and why.

