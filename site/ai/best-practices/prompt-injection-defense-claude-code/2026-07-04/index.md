# Prompt Injection Defense — Claude & Anthropic Platform (as of 04 Jul 2026)

> How Anthropic documents and implements defenses against prompt injection in Claude-based agentic systems: threat model, six permission modes, built-in controls, deployment patterns, and known CVEs — sourced from official Anthropic engineering publications as of July 2026.


<!-- content/ai/best-practices/prompt-injection-defense-claude-code/2026-07-04/index.md — immutable snapshot.
     All sources are Anthropic unless explicitly noted. Multiple Anthropic publications count as ONE
     source for independence; this entry is therefore vendor-documented throughout unless an independent
     third party is explicitly noted. -->

# Prompt Injection Defense — Claude & Anthropic Platform (as of 04 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **04 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Understand Anthropic's three-tier threat model before deploying a Claude agent

**Do:** Before building any agent, read Anthropic's documented threat model. It divides threats into three buckets: (1) **user misuse** — a real user instructing Claude to do something harmful; (2) **model misbehavior** — Claude taking unintended actions autonomously; and (3) **external attackers** — malicious instructions hidden in web pages, emails, tool results, or other third-party content that Claude processes. Prompt injection is in bucket 3 and is hardest to detect because it arrives through channels you would normally trust.

**Why:** If you think only about what your users type, you will miss the attack that actually hurts most Claude agents: an attacker hiding instructions in a webpage Claude visits, a file it reads, or a result a tool returns. That hidden instruction can redirect Claude to exfiltrate data, delete files, or call external servers — all without the user asking for it.

**Caveat:** Anthropic's categorisation is their own framing. The OWASP Agentic Top 10 2026 (December 2025) ranks "Agent Goal Hijacking" (ASI01) as the number-one agentic risk — consistent with Anthropic's threat model but framed by a separate standards body.

**Sources:**
- [anthropic.com/engineering/how-we-contain-claude](https://www.anthropic.com/engineering/how-we-contain-claude) (Anthropic, published 2026-05-25, fetched 2026-07-04)
- [anthropic.com/research/trustworthy-agents](https://www.anthropic.com/research/trustworthy-agents) (Anthropic, published 2026-04-09, fetched 2026-07-04)

**Confidence:** 📄 vendor-documented

---

## Practice: Deliver third-party content only in `tool_result` blocks, never in the system prompt

**Do:** When your Claude agent fetches web pages, reads emails, processes documents, or calls external APIs, deliver that content inside `tool_result` blocks in the API conversation structure — not in `system` or `user` text blocks. Also tell Claude in your system prompt that tool-result content is untrusted data and must not override your instructions. Optionally JSON-encode untrusted strings so an attacker cannot use quotes or tags to "break out" of the data context.

Anthropic's platform docs provide this example structure in JSON form: the `tool_result` block type delivers the untrusted payload, while a preceding system prompt instructs Claude to treat it as data only.

**Why:** Claude is trained to treat instructions that appear in `tool_result` blocks with extra scepticism compared to instructions in the system prompt. Putting an attacker-controlled email body in the system prompt gives it the same authority as your own instructions. The structural separation is the single most actionable change you can make to reduce indirect prompt injection risk.

**Caveat:** This is a mitigation, not a guarantee. Anthropic's own research notes that "no browser agent is immune to prompt injection." The structural separation helps Claude's training-based defences work better, but a sufficiently crafted injection may still succeed.

**Sources:**
- [platform.claude.com/docs/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks](https://platform.claude.com/docs/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) (Anthropic platform docs, fetched 2026-07-04 — provides exact JSON-encode example and `tool_result` guidance)

**Confidence:** 📄 vendor-documented

---

## Practice: Apply a lightweight classifier screen to tool outputs before they reach Claude

**Do:** After each tool call returns, run a small, fast model as a classifier to check whether the output contains injection-like instructions. Use structured output (a boolean `injection_suspected` field) so your application can branch: if `true`, return an error or stripped summary to the agent instead of the raw content. Anthropic's platform docs describe this pattern and suggest using a Claude Haiku model for the classifier role. 🕒 **verify live** — the specific recommended model name may change with new releases; check the current mitigate-jailbreaks page before implementing.

**Why:** Claude's training teaches it to be sceptical of tool outputs, but that scepticism is probabilistic — not a wall. A second model looking specifically for injection patterns adds a layer that doesn't depend on the same neural network being fooled. Think of it as a security guard at the door who has a different job from the person inside the room.

**Caveat:** The classifier can itself be fooled by sufficiently obfuscated injections, and adds latency and cost. Anthropic's auto-mode classifier (a related but distinct mechanism) reports a 17% false-negative rate on real overeager actions 🕒 **verify live** (auto mode is a research preview; these figures are from the March 2026 engineering blog and may change with model releases). Treat it as defence-in-depth, not a primary control.

**Sources:**
- [platform.claude.com/docs/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks](https://platform.claude.com/docs/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) (Anthropic platform docs, fetched 2026-07-04 — injection-screen pattern with example prompts)
- [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) (Anthropic, published 2026-03-25, fetched 2026-07-04 — auto-mode classifier architecture and false-negative rates)

**Confidence:** 📄 vendor-documented

---

## Practice: Run Claude agents in a sandbox with both filesystem AND network isolation

**Do:** Always run Claude agents in a sandboxed environment: a virtual machine, gVisor container, or OS-level sandbox (Linux bubblewrap / macOS Seatbelt). Enforce **both** filesystem isolation (Claude can only read/write specific directories) and network egress controls (only explicitly allowed domains). Anthropic uses this pattern internally: gVisor for claude.ai, OS-level sandboxes for Claude Code on the web, and full VMs for Claude Cowork.

**Why:** Sandbox isolation is the safety net that catches everything the model-level defences miss. If a prompt injection succeeds and Claude is told to send credentials to an attacker's server, egress controls block the data from leaving. If Claude is tricked into reading system files, filesystem isolation prevents it from reaching them.

**Caveat:** ⚠️ **WARNING — both layers required.** Without network controls, agents can exfiltrate data through approved channels even if filesystem access is restricted — exactly what happened in the "Claudy Day" incident (March 2026; see separate practice below). Without filesystem controls, agents can access sensitive credentials and reach the network through them. Real vulnerabilities have bypassed individual layers (see CVE-2025-59536 note in the CLAUDE.md practice below). Always combine both. Note: the `how-we-contain-claude` page confirms Anthropic's sandbox architecture but the specific CVE details are documented by Check Point Research, not that page.

**Sources:**
- [anthropic.com/engineering/claude-code-sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing) (Anthropic, published 2025-10-20, fetched 2026-07-04 — confirms filesystem isolation, network isolation, and credentials never inside sandbox)
- [anthropic.com/engineering/how-we-contain-claude](https://www.anthropic.com/engineering/how-we-contain-claude) (Anthropic, published 2026-05-25, fetched 2026-07-04 — documents sandbox architecture; gVisor/Seatbelt/bubblewrap; MITM proxy for Cowork)
- [platform.claude.com/docs/en/docs/build-with-claude/computer-use](https://platform.claude.com/docs/en/docs/build-with-claude/computer-use) (Anthropic platform docs, fetched 2026-07-04 — explicit Warning block recommending dedicated VM/container)

**Confidence:** 📄 vendor-documented

---

## Practice: Use Claude Code's six permission modes; do not use auto mode as a substitute for human review on high-stakes infrastructure

**Do:** Claude Code has **six distinct permission modes** (as of the live docs fetched 2026-07-04):

| Mode | What it does |
|------|-------------|
| `default` | User approves each potentially sensitive action |
| `acceptEdits` | Automatically accepts file edits; still prompts for shell commands |
| `plan` | Read-only planning phase; presents proposed action plan for review before execution |
| `auto` | A classifier determines whether each action needs user approval |
| `dontAsk` | Never asks for permission (no human approval) |
| `bypassPermissions` | Bypasses all permission checks |

For most work, start with `default` to build intuition. Use `plan` to review high-stakes changes before committing. Use `auto` only for low-stakes work and only after reading its documented limitations. Never use `dontAsk` or `bypassPermissions` on shared infrastructure, production databases, or systems with irreversible consequences.

The **auto mode classifier** is designed to see user messages, tool calls, and CLAUDE.md content — it does NOT see Claude's own internal reasoning (intentionally, to prevent Claude from "reasoning itself into" a bad decision), and tool results are stripped.

**Why:** In internal Anthropic testing, users approved roughly 93% of permission prompts — indicating approval fatigue was already setting in. Auto mode exists to reduce this friction, but it has a 17% false-negative rate on real overeager actions 🕒 **verify live** (auto mode is a research preview; performance figures are from the March 2026 blog and change with model releases).

**Caveat:** ⚠️ **WARNING:** Auto mode is documented as a research preview, not a production-grade safety gate. The classifier makes probabilistic approvals — it looks for approval-shaped signals in tool calls, not a verified understanding of the action's full consequences. For CI/CD pipelines, production systems, or anything touching secrets, use `plan` mode or `default` with allowlists — not `auto` alone.

**Sources:**
- [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) (Anthropic Claude Code docs, fetched 2026-07-04 — complete six-mode table; classifier scope)
- [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) (Anthropic, published 2026-03-25, fetched 2026-07-04 — 93% approval rate, false-negative rates, explicit limitations)

**Confidence:** 📄 vendor-documented

---

## Practice: Keep Claude's footprint minimal — request only the permissions and tools needed for the current task

**Do:** When configuring a Claude agent or Claude Code session, give Claude access only to the tools, files, and services it actually needs for the current task. Do not give it write access if it only needs to read. Do not give it database write permissions for a code-review task. If you are using the Agent SDK, use `allowed_tools` to restrict which tools are available.

**Why:** A prompt injection can only do what Claude is allowed to do. Anthropic's empirical data (October 2025 – January 2026 sample) shows that in practice only 0.8% of Claude agent actions involve irreversible consequences and 80% of tool calls come from agents with at least one safeguard — but this is average-case data across all deployments; high-stakes environments have a different risk profile.

**Caveat:** Restricting permissions does not prevent the injection from reaching Claude — it limits the blast radius when it does.

**Sources:**
- [platform.claude.com/docs/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks](https://platform.claude.com/docs/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) (Anthropic platform docs, fetched 2026-07-04)
- [anthropic.com/research/measuring-agent-autonomy](https://www.anthropic.com/research/measuring-agent-autonomy) (Anthropic, fetched 2026-07-04 — 0.8% irreversible actions, 80% safeguard coverage)

**Confidence:** 📄 vendor-documented

---

## Practice: Require human confirmation before Claude takes irreversible or high-impact actions

**Do:** Design agent workflows to pause and ask for human confirmation before any action that cannot be undone: sending emails, executing database migrations, committing to shared branches, deleting files, making financial transactions. Claude Code implements this as "plan mode" — Claude shows the intended action plan for user review before executing. For computer use, Anthropic's classifiers detect suspected injections and steer Claude to ask for confirmation before acting.

**Why:** An injected instruction can only cause lasting damage if Claude acts on it without a human in the loop. A confirmation step gives the human a chance to notice something unexpected.

**Caveat:** Human-in-the-loop protection has practical limits. Anthropic's containment paper documents a February 2026 red-team exercise in which social engineering caused an employee to provide a malicious prompt — Claude then completed the credential exfiltration 24 out of 25 times. Human confirmation is the most reliable mitigation but is not immune to social engineering.

**Sources:**
- [anthropic.com/research/trustworthy-agents](https://www.anthropic.com/research/trustworthy-agents) (Anthropic, published 2026-04-09, fetched 2026-07-04 — plan mode description)
- [platform.claude.com/docs/en/docs/build-with-claude/computer-use](https://platform.claude.com/docs/en/docs/build-with-claude/computer-use) (Anthropic platform docs, fetched 2026-07-04 — classifier steers Claude to ask for confirmation when injection suspected)
- [anthropic.com/engineering/how-we-contain-claude](https://www.anthropic.com/engineering/how-we-contain-claude) (Anthropic, published 2026-05-25, fetched 2026-07-04 — February 2026 24/25 incident)

**Confidence:** 📄 vendor-documented

---

## Practice: Treat Claude's built-in training-based defences as one layer, not the whole defence

**Do:** Anthropic trains Claude to resist prompt injection using reinforcement learning on simulated injections. Claude Opus 4.5 achieved approximately 1% attack success rate against their internal "Best-of-N" adaptive attacker; Claude Opus 4.7 reaches roughly 0.1% on single attempts on the Gray Swan benchmark. 🕒 **verify live** — model versions and benchmark scores change with each model release; these figures are from the November 2025 and May 2026 papers and may already be superseded by Opus 4.8.

Use these defences as a foundation, but layer environment controls, classifier screens, and human oversight on top. Do not treat model-level training as sufficient on its own. Anthropic explicitly states in their containment paper: "protection in the model layer will never be 100% effective, which is why it can't stand alone."

**Why:** A 1% attack success rate sounds good until you realise your agent may process thousands of documents. At 1% success rate, an attacker who can plant injected content in 100 documents your agent reads expects to succeed at least once.

**Caveat:** Anthropic's benchmark numbers are self-reported against their own internal attacker. Independent evaluation found that 12 published defences were bypassed at >90% success rate by adaptive attacks (Zylos Research, April 2026, citing "The Attacker Moves Second" paper). Claude's figures have not been independently replicated to the panel's knowledge.

**Sources:**
- [anthropic.com/research/prompt-injection-defenses](https://www.anthropic.com/research/prompt-injection-defenses) (Anthropic, published ~2025-11-24, fetched 2026-07-04 — 1% attack success rate; RL training approach)
- [anthropic.com/engineering/how-we-contain-claude](https://www.anthropic.com/engineering/how-we-contain-claude) (Anthropic, published 2026-05-25, fetched 2026-07-04 — 0.1% single-attempt rate for Opus 4.7; "protection in the model layer will never be 100% effective")
- [zylos.ai/research/2026-04-12-indirect-prompt-injection-defenses-agents-untrusted-content/](https://zylos.ai/research/2026-04-12-indirect-prompt-injection-defenses-agents-untrusted-content/) (Zylos Research, published 2026-04-12, fetched 2026-07-04 — independent evaluation; "Attacker Moves Second" finding)

**Confidence:** ✅ independently-corroborated (Anthropic docs + Zylos Research as independent third-party evaluator; Zylos is a small research org — weight accordingly)

---

## Practice: Only load Agent Skills from trusted sources; audit all bundled scripts before use

**Do:** Claude's "Agent Skills" system allows Skills — packages of instructions and executable scripts — to be installed and run automatically when Claude judges them relevant. Anthropic's official docs warn: "Use Skills only from trusted sources: those you created yourself or obtained from Anthropic." Before installing any third-party Skill, audit every file it contains: SKILL.md, any additional markdown files, and especially any executable scripts. Be especially alert to Skills that fetch external URLs (the fetched content may itself contain injections) and Skills that request broad tool access.

**Why:** A malicious Skill is a pre-installed prompt injection. It is installed before any conversation begins and its instructions arrive in Claude's context with elevated trust (it is part of the configuration, not a tool result). A malicious Skill that can call the `Bash` tool can execute arbitrary commands on your machine.

**Caveat:** ⚠️ **WARNING:** In Claude Code, Skills run with full network access — the same network access as any other program on your computer. In the Claude API, Skills have no network access. The risk level of a Skill differs dramatically depending on which surface you install it on.

**Sources:**
- [platform.claude.com/docs/en/agents-and-tools/agent-skills/overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) (Anthropic platform docs, fetched 2026-07-04 — "Use Skills only from trusted sources"; "malicious Skill can direct Claude to invoke tools or execute code in ways that don't match the Skill's stated purpose"; network access differences by surface)

**Confidence:** 📄 vendor-documented

---

## Practice: Treat tool outputs from sub-agents with the same scepticism as external content

**Do:** When building multi-agent Claude systems, do not automatically grant a sub-agent's output higher trust than other tool results. A sub-agent that was initially benign can be compromised mid-run by prompt injection after it was delegated a task but before it returns results. Claude Code's auto-mode classifier runs a separate check on sub-agent return results specifically because of this risk. Apply the same filtering to sub-agent outputs that you would to external content.

**Why:** In a chain of agents, a successful injection anywhere in the chain can propagate to every downstream agent. Treating a sub-agent's output as authoritative without checking it is like trusting a forwarded email without asking whether it was tampered with in transit.

**Caveat:** Anthropic flags "multi-agent trust escalation" as an emerging risk in their May 2026 containment paper but does not yet publish specific mitigations beyond the auto-mode classifier check. This is a thin guidance area — the practice is implied by documented risks, not explicitly prescribed.

**Sources:**
- [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode) (Anthropic, published 2026-03-25, fetched 2026-07-04 — "a subagent that was benign at delegation could be compromised mid-run by prompt injection")
- [anthropic.com/engineering/how-we-contain-claude](https://www.anthropic.com/engineering/how-we-contain-claude) (Anthropic, published 2026-05-25, fetched 2026-07-04 — multi-agent trust escalation flagged as emerging risk)

**Confidence:** 📄 vendor-documented (thin — practice implied by documented risks; no explicit step-by-step guidance yet)

---

## Practice: Apply Anthropic's shared responsibility model — the model layer is Anthropic's job; harness, tools, and environment are yours

**Do:** Understand which part of the security stack is Anthropic's responsibility and which is yours. Anthropic's documented four-layer model is: (1) **Model** — Anthropic trains Claude for injection resistance; (2) **Harness** — you write system prompts, guardrails, and approval workflows; (3) **Tools** — you configure which MCP servers, APIs, and plugins Claude can reach; (4) **Environment** — you control where the agent runs and what data it can access. A well-trained model can still be exploited through a poorly configured harness, an overly permissive tool, or an exposed environment.

**Why:** If you give Claude access to your entire file system and no egress controls, and a webpage it visits contains a hidden instruction to send your SSH key to an attacker's server — that is not Anthropic's failure to fix; it is a deployment decision you made.

**Caveat:** The Backslash Security blog (April 2026) independently analyses the four-layer model and notes a gap in NIST SP 800-61 incident response coverage for this shared-responsibility model — standard IR frameworks don't yet account for AI-layer responsibility assignment. Note: an earlier draft claimed Backslash also cited OWASP LLM Top 10, NIST AI RMF, and ISO 42001 as inadequate; Skeptic verified this is not what the Backslash page says. Only the NIST SP 800-61 gap claim is supported by that source.

**Sources:**
- [anthropic.com/research/trustworthy-agents](https://www.anthropic.com/research/trustworthy-agents) (Anthropic, published 2026-04-09, fetched 2026-07-04 — four-layer model: model, harness, tools, environment)
- [backslash.security/blog/anthropics-shared-responsibility-security-model-for-ai-agents](https://www.backslash.security/blog/anthropics-shared-responsibility-security-model-for-ai-agents) (Backslash Security, published 2026-04-29, fetched 2026-07-04 — independent analysis of the four-layer model; confirms NIST SP 800-61 gap)

**Confidence:** ✅ independently-corroborated (Anthropic + Backslash Security as independent publisher; Backslash is a security vendor with its own product interests — weight accordingly)

---

## Practice: Watch for the "Claudy Day" class of attack — injection via allowlisted egress channels

**Do:** When configuring network egress allowlists for Claude agents, do not assume that only-allowlisted-domains egress is safe. The March 2026 "Claudy Day" attack on claude.ai demonstrated that an attacker can supply their own API key embedded in content, then instruct Claude to upload stolen data to the attacker's Anthropic account via the Files API using the attacker-embedded key. The allowlist sees a legitimate destination (`api.anthropic.com`); the credential check was what failed. Defense: use a MITM proxy inside your sandbox that validates not just the destination but also rejects attacker-embedded authentication credentials. Anthropic fixed this in Claude Cowork by deploying a MITM proxy that blocks server-side fetch headers carrying attacker-embedded keys.

**Why:** Egress allowlists block traffic to unknown destinations. They do not stop an attacker who knows which destinations you trust and provides their own credentials to use them.

**Caveat:** The specific Claudy Day vulnerability in claude.ai's public chat interface was patched (Oasis Security confirmed, March 2026). The underlying architectural pattern (allowlist bypass via attacker-controlled credentials) remains a general risk for anyone building similar egress architectures. Note: Oasis's post states "the prompt injection issue has been fixed, and the remaining issues are currently being addressed" — so not all legs of the attack chain were fully resolved at time of publication.

**Sources:**
- [oasis.security/blog/claude-ai-prompt-injection-data-exfiltration-vulnerability](https://www.oasis.security/blog/claude-ai-prompt-injection-data-exfiltration-vulnerability) (Oasis Security, published 2026-03-18, updated 2026-05-27, fetched 2026-07-04 — full attack chain: attacker uploads to their own Anthropic account via Files API; Anthropic confirmed fix of injection leg)
- [anthropic.com/engineering/how-we-contain-claude](https://www.anthropic.com/engineering/how-we-contain-claude) (Anthropic, published 2026-05-25, fetched 2026-07-04 — MITM proxy fix for Claude Cowork)

**Confidence:** ✅ independently-corroborated (Oasis Security as independent publisher + Anthropic engineering blog; Oasis did responsible disclosure and Anthropic confirmed the findings)

---

## Practice: Treat CLAUDE.md and project config hooks as a security surface — audit them as code

**Do:** Claude Code reads `CLAUDE.md` and `.claude/settings.json` at startup and uses them as authoritative instructions. CVE-2025-59536 (patched in Claude Code 1.0.111, approximately February 2026, per Check Point Research) allowed project-local configuration hooks to execute code before the user accepted the trust dialog — meaning an attacker who could plant a `.claude/settings.json` in a repository could run code before the user had a chance to review anything. A related vulnerability, CVE-2026-21852 (fixed in Claude Code 2.0.65+, January 2026), allowed API key exfiltration via manipulation of the `ANTHROPIC_BASE_URL` variable.

Now: treat `CLAUDE.md` and `.claude/settings.json` the same way you would treat a Makefile or CI configuration — review changes in code review, never blindly run `git clone && claude` in unfamiliar repositories.

**Why:** When you open a project in Claude Code, it reads configuration files before you type anything. Those files can contain instructions that shape what Claude does — or, if maliciously crafted, instructions that exploit the agent loop. This is the same threat model as supply-chain attacks in software: a compromised dependency configuration can hijack the tool.

**Caveat:** Anthropic patched the pre-trust execution vulnerability (CVE-2025-59536) in Claude Code 1.0.111. The current ongoing risk is not the specific bug — it is that the design (Claude reads project config as trusted instructions) remains a supply-chain attack surface. Auditing the config is the ongoing practice.

**Sources:**
- [research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/) (Check Point Research, fetched 2026-07-04 — CVE-2025-59536 full technical disclosure, patched in Claude Code 1.0.111)
- [anthropic.com/engineering/how-we-contain-claude](https://www.anthropic.com/engineering/how-we-contain-claude) (Anthropic, published 2026-05-25, fetched 2026-07-04 — project config as security surface, general guidance)

**Confidence:** ✅ independently-corroborated (Check Point Research as independent security publisher + Anthropic engineering blog on design implications)

---

## Practice: Keep secrets outside the Claude agent's context; use scoped tokens, not ambient credentials

**Do:** Never place API keys, database passwords, SSH keys, or cloud credentials directly in Claude's context window, system prompt, or in files Claude has unrestricted read access to. Instead: (a) pass credentials through environment variables injected at runtime by your infrastructure, (b) use scoped-down per-session tokens with minimum permissions needed, and (c) keep credential files outside the directories Claude can read. Claude Code on the web keeps git credentials outside the sandbox specifically for this reason.

**Why:** If Claude's context contains a secret and a prompt injection succeeds, the injected instruction can ask Claude to repeat or transmit that secret.

**Caveat:** ⚠️ **WARNING:** Keeping secrets "out of the context" is not sufficient if Claude has the permissions to access credential files. A February 2026 red-team exercise demonstrated that even without pre-placed secrets, a malicious prompt can instruct Claude to read `~/.aws/credentials` if Claude has bash access and file system read permissions (24 out of 25 retries succeeded). Both the secret handling AND the filesystem permissions must be restricted.

**Sources:**
- [anthropic.com/engineering/claude-code-sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing) (Anthropic, published 2025-10-20, fetched 2026-07-04 — "Sensitive credentials (such as git credentials or signing keys) are never inside the sandbox with Claude Code")
- [anthropic.com/engineering/how-we-contain-claude](https://www.anthropic.com/engineering/how-we-contain-claude) (Anthropic, published 2026-05-25, fetched 2026-07-04 — February 2026 `~/.aws/credentials` exfiltration incident, 24/25 retries)

**Confidence:** 📄 vendor-documented (both Anthropic sources)

---

## Held pending fixes

- **Constitutional AI as a prompt injection defence layer:** Could not locate a fetchable Anthropic source specifically describing Constitutional AI's role in injection defence (vs. general harmlessness). ⚠ PENDING
- **Cryptographic enforcement of the operator/user trust hierarchy:** Anthropic's documentation describes the hierarchy but acknowledges it is not cryptographically enforced. No Anthropic source describing planned cryptographic enforcement was found. ⚠ PENDING
- 🕒 **verify live:** Model version numbers (Opus 4.5, 4.7, Sonnet 4.6) and associated benchmark figures change with each model release. All version-specific attack success rate figures should be re-verified before republication.

## CHANGELOG (grading → this entry)

1. **Timekeeper KILL → rewrite (P5):** Removed "three permission tiers: (1) manual approval, (2) allowlist, (3) auto mode" — this was factually wrong. Replaced with the accurate six-mode model (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`) from the live docs fetched 2026-07-04. The draft's "allowlist tier" does not correspond to any named mode.
2. **Skeptic KILL → fix (P4 and P12):** Removed CVE-2025-59536 citation from Practice 4 (the cited `how-we-contain-claude` page does not mention this CVE). Removed TrueFoundry citation for CVE-2025-59536 — TrueFoundry's page documents CVE-2025-54794/54795 (InversePrompt), not -59536. Replaced with Check Point Research as the correct source. Fixed patch date from "January 2026" to "approximately February 2026."
3. **Skeptic KILL → fix (P4):** Removed "SOCKS5 null-byte bypass affecting ~130 versions" — no fetched source was found for this claim. Removed entirely.
4. **Skeptic FIX (P4):** Removed the verbatim quote "even a successful prompt injection is fully isolated, and cannot impact overall user security" — Skeptic could not find this exact phrasing on the attributed page (`how-we-contain-claude`). Replaced with non-verbatim summary of the same concept.
5. **Skeptic FIX (P5):** Removed verbatim quote "approval-shaped evidence and stops short of checking whether it's consent for the blast radius of the action" — Skeptic could not confirm this exact phrase on any page. Replaced with paraphrase of the documented limitation.
6. **Skeptic FIX (P5, classifier scope):** Changed "only tool calls" → "user messages, tool calls, and CLAUDE.md content (tool results stripped)" per live docs fetched 2026-07-04 by Timekeeper.
7. **Skeptic FIX (P7, phishing):** Softened "phishing" to "social engineering" — Skeptic could not confirm "phishing" specifically (the source describes a red-team social engineering scenario; "phishing" is a narrower claim).
8. **Skeptic FIX (P8):** Fixed quote attribution: "protection in the model layer will never be 100% effective, which is why it can't stand alone" is on `how-we-contain-claude` (cited), not on `prompt-injection-defenses` (where draft placed it). Updated citation pointer.
9. **Skeptic FIX (P8):** Added inline 🕒 **verify live** next to benchmark figures (17%, 1%, 0.1%) — auto mode is a "research preview" per current docs; figures change with model releases.
10. **Skeptic FLAG → FIX (P11, Backslash):** Removed claim that Backslash source "notes that OWASP LLM Top 10, NIST AI RMF, and ISO 42001 do not yet account for this model" — Skeptic confirmed Backslash page discusses only NIST SP 800-61 gap, not OWASP/RMF/ISO 42001. Trimmed caveat to match actual source.
11. **Skeptic FIX + Timekeeper FIX (P12, Claudy Day):** Changed mechanism description from "upload to api.anthropic.com using attacker's credentials" → "upload to the attacker's Anthropic account via the Files API using the attacker-embedded key." Fixed fix-status from "Anthropic confirmed fix" to "the prompt injection leg was fixed; remaining issues were still being addressed at publication."
12. **Timekeeper FIX (P3, Haiku):** Added `verify live` caveat next to "Claude Haiku" model name — auto-mode docs show Haiku is NOT supported in auto mode. The classifier pattern in mitigate-jailbreaks uses a Haiku model but this should be verified against current docs before implementation.
13. **Timekeeper FIX (P13, CLAUDE.md):** Added patch version (Claude Code 1.0.111); added CVE-2026-21852 (ANTHROPIC_BASE_URL exfiltration, fixed in 2.0.65+, January 2026); corrected Timekeeper's confirmation of February 2026 (not January) as the patch date for CVE-2025-59536.
14. **Beginner FIX (P5, CI/CD):** Added parenthetical explanation of what CI/CD means for readers unfamiliar with the acronym.

