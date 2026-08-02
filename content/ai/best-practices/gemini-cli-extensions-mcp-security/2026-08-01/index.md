---
title: "Gemini CLI Security Practices: Extensions & MCP Integration (as of 01 Aug 2026)"
date: 2026-08-01
snapshot_date: 2026-08-01
topic: gemini-cli-extensions-mcp-security
track: best-practices
audience: "technically comfortable readers"
description: "How Gemini CLI's extension system and MCP (Model Context Protocol) server integration handle trust, permissions, and third-party risk — vetting gaps, the CVSS-disputed CI/CD RCE, and safe-default settings, as of August 2026."
content_type: "Best Practice"
categories: ["Gemini CLI", "MCP"]
tags: ["gemini-cli", "mcp", "extensions", "supply-chain", "prompt-injection", "security"]
last_refreshed: 2026-08-01
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-08-01"
grading_result: "0 fabrications after correction; 5 KILL + 10 FIX + 8 FLAG applied across the 3-draft Gemini CLI batch (this entry: 0 KILL, 5 FIX applied); 2 gaps tracked as project-33 issues (mg_api unavailable this run — tracked in WORKLOG)"
---

<!-- This file lands at content/ai/<track>/<topic>/<snapshot-date>/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->


# Gemini CLI Security Practices: Extensions & MCP Integration (as of 01 Aug 2026)

> **Grading note.** A dated snapshot — accurate as of **01 Aug 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

**Prerequisite — what's an MCP server?** MCP (Model Context Protocol) is an open standard that lets an AI agent like Gemini CLI connect to external "servers" that add new abilities — reading a database, calling an API, running shell commands. An MCP server is a program that can act on the model's behalf; if it's malicious or compromised, it can do anything its granted tools allow, on your machine, without you writing that code yourself. Gemini CLI extensions are a packaging layer on top of this — an extension can bundle one or more MCP servers plus custom commands. Install Gemini CLI itself with `npm install -g @google/gemini-cli` (requires Node.js) if you haven't already.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Never set `trust: true` on an MCP server (or run `--yolo`) unless you fully control that server/host
**Do:** In `settings.json` (or an extension's `gemini-extension.json`), leave MCP server entries at the default `trust: false` so every tool call gets a confirmation prompt. Only set `trust: true` — for example, `gemini mcp add my-internal-server --trust --url http://localhost:8080` for a server you personally wrote and run on `localhost` — for servers you personally control. Avoid `--yolo` (auto-approve-everything) entirely on any machine that touches untrusted input — including CI.
**Why (beginner):** `trust: true` means Gemini CLI will run that server's tools — which can mean shell commands, file writes, or network calls — without ever asking you first. Google's own docs call this out explicitly: use it "cautiously and only for servers you completely control." A real-world example of what goes wrong when this is ignored: Google shipped `--yolo` mode so that it silently ignored your fine-grained tool allowlist, and combined with a second bug (headless/CI mode auto-trusting whatever folder it was pointed at), this became a maximum-severity remote-code-execution bug that let an attacker who could merely open a public GitHub issue reach code execution on CI runners. Google fixed it in `@google/gemini-cli` 0.39.1 and `run-gemini-cli` GitHub Action 0.1.22 (24 Apr 2026); it was later tracked as **CVE-2026-12537** (published 24 Jun 2026 — NVD and CIRCL confirm this is the same bug as GHSA-wpqr-6v78-jr5g, though the original April write-ups predate the CVE assignment).
**Caveat / contested:** 🕒 verify live — version numbers and the exact allowlist-under-yolo semantics are still evolving; check you're on a current release. The CVSS score for this bug is contested across scoring systems: Google's CNA rates it 10.0 (CVSS 4.0); NIST independently scores it 7.8 HIGH (CVSS 3.1). Separately, this is not the only recent trust-boundary finding: Pillar Security's "Week of Sandbox Escapes" (20–23 Jul 2026) disclosed a new Docker-socket escape hitting Gemini CLI (since fixed) and an unpatched macOS Seatbelt/`.vscode`-task-config bypass affecting Google's Antigravity "Secure Mode" — see the security-fundamentals entry for the full writeup. Also note: an *extension's* `gemini-extension.json` cannot itself set `trust: true` for the MCP servers it bundles (only `settings.json` can), so a malicious/compromised extension can't silently self-escalate to no-confirmation mode — but if you separately hand-set `trust: true` for its server, that protection is gone.
**Sources:** [Gemini CLI docs — MCP servers](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md) (fetched 01 Aug 2026) · [GBHackers — Critical Gemini CLI Flaw Raises Supply Chain Security Concerns](https://gbhackers.com/critical-gemini-cli-flaw/) (27 Apr 2026) · [Pillar Security — My Agentic Trust Issues](https://www.pillar.security/blog/my-agentic-trust-issues-from-prompt-injection-to-supply-chain-compromise-on-gemini-cli) (5 May 2026) · [NVD — CVE-2026-12537](https://nvd.nist.gov/vuln/detail/CVE-2026-12537) (CVSS scoring dispute + CVE↔GHSA link) · [GitHub Advisory Database — GHSA-wpqr-6v78-jr5g](https://github.com/advisories/GHSA-wpqr-6v78-jr5g) · [Pillar Security — The Week of Sandbox Escapes](https://www.pillar.security/blog/the-week-of-sandbox-escapes) (Jul 2026)
**Confidence:** independently-corroborated

---

## Practice: Don't assume Trusted Folders is on by default — Google's own docs disagree; verify or turn it on, and read the trust dialog before accepting
**Do:** Google's documentation is internally inconsistent about whether the Trusted Folders feature is on or off by default (see the security-fundamentals entry for the full conflict between its two docs) — don't assume either reading. When Gemini CLI shows the first-run trust dialog for a new folder, actually read the "discovery" summary (it lists any MCP servers, custom commands, hooks, and skills the folder would activate) before choosing "Trust folder." Don't choose "Trust parent folder" broadly, and don't set a repo to trusted just because a prompt is annoying — especially not on a machine that also runs CI jobs against untrusted PRs. If you never see a trust prompt at all, that's a sign the feature may be defaulting to on for your build — check `/permissions` and explicitly set `"security": {"folderTrust": {"enabled": true}}` if you want to be sure the dialog is active.
**Why (beginner):** In an untrusted folder, Gemini CLI refuses to auto-connect MCP servers, blocks extension management, and requires explicit approval for tool calls — this is your safety net against a repo (or a PR you're reviewing) that ships a poisoned `.gemini/` config or MCP server definition. The CVE above existed specifically because *headless* mode skipped this trust check and auto-trusted whatever folder it was pointed at, loading a malicious `.gemini/.env` file before the sandbox even started.
**Caveat / contested:** This mainly protects interactive/local use; the documented bypass was in headless/non-interactive mode, so CI pipelines need the version fix, not just correct trust settings — trust settings and a patched version are both required.
**Sources:** [Gemini CLI docs — Trusted Folders](https://geminicli.com/docs/cli/trusted-folders/) (fetched 01 Aug 2026) · [github.com/google-gemini/gemini-cli — docs/cli/trusted-folders.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/trusted-folders.md) ("disabled by default" — contradicts the settings-reference table's stated `true` default; fetched 01 Aug 2026) · [The Hacker News — Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws Enable Code Execution](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html) (30 Apr 2026) · [Cloud Security Alliance Labs — Gemini CLI CVSS 10.0: RCE in AI Developer Tools](https://labs.cloudsecurityalliance.org/research/csa-research-note-gemini-cli-rce-cvss10-ai-tool-security-202/) (2 May 2026)
**Confidence:** independently-corroborated

---

## Practice: Treat every extension in the marketplace as unaudited third-party code — including Google's own — and read the source before installing
**Do:** Before running `gemini extensions install <github-url>` (e.g. `gemini extensions install https://github.com/gemini-cli-extensions/security`), open the repo and skim the `gemini-extension.json` (what MCP servers/tools does it add?) and any bundled server source, especially if it runs on files you don't control (PR diffs, issue text, etc.). Don't assume "official-looking" or "Google-authored" means audited.
**Why (beginner):** Google's own extension gallery carries this disclaimer: it does **not** vet, endorse, or guarantee the security of listed extensions, and tells users to "carefully inspect any extension and its source code before installing." This isn't just caution-language — Google's own official "security" extension (which scans PRs for vulnerabilities) shipped an MCP server with a **prototype-pollution bug** (a class of JavaScript bug where a crafted input corrupts an object's shared base template, letting an attacker's data override the behavior of unrelated code): a PR containing a single line with the word `constructor` could trigger the pollution, which researchers escalated into command execution and used to hide findings from the very tool meant to catch them (CVSS 7.1, CWE-1321 — the standard catalog ID for this bug class). Google fixed it by replacing a plain object with a `Map` (merged 15 Oct 2025); the bug was publicly written up in March 2026, about five months later. The lesson: extension code runs full-privilege on your machine, official label or not.
**Caveat / contested:** ⚠ PENDING — whether the "security extension" bug was ever independently reproduced/confirmed beyond the one write-up plus the merged fix PR is not something we could verify with a second independent researcher; treat the specific bug detail as reported by one research firm, corroborated only by the vendor's own merged fix commit (which confirms the bug existed but isn't a second independent security analysis) — labeled `thin` rather than `independently-corroborated` to reflect that honestly, since two Google pages plus one researcher is one independent publisher, not two.
**Sources:** [Gemini CLI Extensions Gallery](https://geminicli.com/extensions/) (fetched 01 Aug 2026) · [Symbiotic Security — Who Scans the Scanners? Uncovering a Critical Bug in Gemini's Security CLI](https://www.symbioticsec.ai/blog/who-scans-the-scanners-uncovering-a-critical-bug-in-geminis-security-cli) (13 Mar 2026) · [gemini-cli-extensions/security PR #91](https://github.com/gemini-cli-extensions/security/pull/91) (merged 15 Oct 2025)
**Confidence:** thin <!-- two Google pages + one independent researcher = one independent publisher, not independently-corroborated -->

---

## Practice: Use `excludeTools` to hard-block dangerous shell/file operations from extensions and MCP servers, not just rely on the confirmation prompt
**Do:** In `gemini-extension.json` or `settings.json`, explicitly list high-risk tool patterns you never want auto-suggested, e.g. `"excludeTools": ["run_shell_command(rm -rf *)"]`, in addition to leaving `trust: false`. Use `includeTools`/`excludeTools` per-MCP-server (documented on the MCP-servers reference page) to scope what each server can actually call.
**Why (beginner):** A confirmation prompt only helps if you read it carefully every time; under time pressure it's easy to click "yes" on a destructive command. `excludeTools` removes the tool from what the model can even offer, so there's no prompt to misread.
**Caveat / contested:** Google's own docs describe this pattern at two levels — extension-level `excludeTools` and per-MCP-server `includeTools`/`excludeTools` — but both live only on official documentation pages (two Google pages, one vendor); we found no independent security research testing real-world effectiveness against a determined malicious server (a compromised server could in principle rename/alias a tool to dodge a pattern match).
**Sources:** [Gemini CLI docs — Extensions best practices](https://geminicli.com/docs/extensions/best-practices/) (fetched 01 Aug 2026) · [Gemini CLI docs — MCP servers](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md) (fetched 01 Aug 2026) · [Gemini CLI docs — Extension reference](https://github.com/google-gemini/gemini-cli/blob/main/docs/extensions/reference.md) (fetched 01 Aug 2026)
**Confidence:** vendor-documented

---

## Practice: Know that explicitly-configured MCP server environment variables bypass Gemini CLI's automatic secret redaction
**Do:** Don't put a real API key or token directly as a literal value in an MCP server's `env` block in `settings.json`/`gemini-extension.json` unless you mean to hand that exact value to that exact server. Prefer variable expansion (e.g. `"MY_KEY": "$MY_KEY"`) so the secret lives in your shell environment, not in a config file that might get committed or shared — and remember that once you list a variable in `env`, the CLI treats that as informed consent and skips the redaction it would otherwise apply.
**Why (beginner):** Gemini CLI auto-redacts variables matching patterns like `*TOKEN*`, `*SECRET*`, `*PASSWORD*`, `*KEY*`, `*AUTH*`, `*CREDENTIAL*`, `GEMINI_API_KEY`, and `GOOGLE_API_KEY` from the base environment passed to MCP servers/extensions — good, but that automatic protection stops the moment you explicitly name a variable for a server. Extensions also don't inherit your full shell environment by default; only allowlisted variables reach them, which is a safety net, but it's a net you can turn off yourself without realizing it.
**Caveat / contested:** Single (vendor) source; we could not find independent security research specifically testing this redaction mechanism for bypasses.
**Sources:** [Gemini CLI docs — MCP servers](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md) (fetched 01 Aug 2026) · [Gemini CLI docs — Extension reference](https://github.com/google-gemini/gemini-cli/blob/main/docs/extensions/reference.md) (fetched 01 Aug 2026)
**Confidence:** vendor-documented

---

## Practice: ⚠️ Avoid underscores in MCP server names — they can make wildcard/security-policy rules fail silently
**Do:** Name MCP servers with dashes, not underscores (e.g. `my-server`, not `my_server`), when configuring them in `settings.json` or an extension manifest.
**Why (beginner):** Gemini CLI's own docs warn that an underscore in a server name confuses the config parser's identity matching, which "can cause wildcard rules and security policies to fail silently" — meaning a tool-restriction rule you think is active may simply not apply, with no error shown. That's the dangerous part: it fails quietly, not loudly.
**Caveat / contested:** Single (vendor) source; treat as `thin` until independently reproduced, but it's a low-cost precaution (just a naming convention) so it's worth following even unverified.
**Sources:** [Gemini CLI docs — MCP servers](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md) (fetched 01 Aug 2026)
**Confidence:** thin

---

## Practice: Treat MCP tool descriptions and tool output as untrusted content, even though Gemini CLI's docs don't flag this explicitly the way some other MCP clients do
**Do:** Assume any text returned by an MCP tool call (or embedded in a tool's own description/schema) could contain hidden instructions aimed at the model, not at you — this is called **"tool poisoning"** or indirect prompt injection via tool metadata: a malicious or compromised MCP server writes instructions into what looks like ordinary data, and the model, unable to tell data from instructions, may follow them. Be extra cautious with MCP servers that ingest attacker-reachable content (GitHub issues/PRs, web pages, emails, files from a repo you don't control) and feed results back to the model.
**Why (beginner):** This isn't hypothetical for Gemini CLI: independent researchers (the "Comment and Control" study, disclosed 15 Apr 2026) demonstrated hijacking Gemini CLI — along with Claude Code and GitHub Copilot — by embedding malicious instructions in GitHub issue bodies, PR titles, and comments that the agent read as part of its task context, leading to exfiltration of CI secrets in vulnerable configurations. Separately, a CSO Online-reported flaw let malicious instructions hidden in a repo's README get executed as if they were legitimate CLI commands (fixed in Gemini CLI 0.1.14, 25 Jul 2025). The general "tool poisoning" attack class — where a malicious or compromised MCP server's tool description instructs the model to misbehave — is well documented across the MCP ecosystem broadly, not unique to Gemini CLI.
**Caveat / contested:** We could not find Gemini-CLI-specific documentation or independent research that directly compares how well Gemini CLI's UI surfaces a warning for untrusted/injected tool descriptions versus other MCP clients (one academic paper tested Gemini CLI among seven MCP clients for tool-poisoning resistance, but its results section was inaccessible to verify claims from, even on a fresh check 01 Aug 2026). Treat the "does Gemini CLI warn you the way some other clients do" question as unresolved — we found no evidence either way in the official docs.
**Sources:** [Aptible — Prompt Injection in MCP: Tool Poisoning and Blast Radius](https://www.aptible.com/mcp-security/mcp-prompt-injection) (fetched 01 Aug 2026) · [CSO Online — Google patches Gemini CLI tool after prompt injection flaw uncovered](https://www.csoonline.com/article/4030700/google-patches-gemini-cli-tool-after-prompt-injection-flaw-uncovered.html) (29 Jul 2025) · [SecurityWeek — Claude Code, Gemini CLI, GitHub Copilot Agents Vulnerable to Prompt Injection via Comments](https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/) (15 Apr 2026, "Comment and Control" research) · [Cloud Security Alliance Labs research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-gemini-cli-rce-cvss10-ai-tool-security-202/) (2 May 2026)
**Confidence:** contested

---

## Practice: Don't trust search-engine results for "install Gemini CLI" — install only via the official npm package or Google's documented instructions
**Do:** Install with `npm install -g @google/gemini-cli` (or another method linked from Google's own docs), typed directly rather than copy-pasted from a random blog or ad. Never paste a one-line PowerShell/curl "installer" command from a page you found via search without checking the domain is genuinely Google's.
**Why (beginner):** In a campaign identified around March–May 2026, attackers used SEO poisoning to rank fake domains (e.g. `geminicli[.]co[.]com`) above the real Gemini CLI docs. The fake page's copy-paste command *did* install the real, uncompromised `@google/gemini-cli` package from npm — masking the attack — while quietly also running (via a hidden `Shell.Application` COM call) an in-memory PowerShell infostealer that harvested browser cookies, OAuth tokens, CI/CD credentials, and VPN keys. This is a risk in the install/distribution layer around Gemini CLI, not a flaw in the extension or MCP system itself, but it's the same "don't blindly run code from an untrusted third party" muscle you need for vetting extensions.
**Caveat / contested:** This specific campaign targeted the base CLI installer, not the extension marketplace directly. Also, our second source (GBHackers) explicitly states it is reporting on EclecticIQ's original research rather than an independent investigation — so despite being two different publishers, this is really one underlying finding reported twice, not two independent confirmations. Labeling `thin`, not `independently-corroborated`, to reflect that honestly.
**Sources:** [EclecticIQ — SEO poisoning campaign leverages Gemini and Claude Code impersonation to deliver infostealer](https://blog.eclecticiq.com/seo-poisoning-campaign-leverages-gemini-and-claude-code-impersonation-to-deliver-infostealer) (21 May 2026) · [GBHackers — Hackers Use SEO Poisoning to Fake Gemini CLI, Claude Installers](https://gbhackers.com/seo-poisoning-gemini-cli-claude-installers/) (23 May 2026, derivative of EclecticIQ's research per its own text)
**Confidence:** thin

---

## Practice: In team/enterprise settings, use the admin MCP-server allowlist rather than relying on every developer to configure trust correctly themselves — but know that admin-forced trust removes the user confirmation prompt for everyone
**Do:** If you administer Gemini CLI for an organization via Google's Management Console (Gemini Enterprise / Workspace admin), define an explicit allowlist of approved MCP servers rather than leaving it to individual `settings.json` files, and disable the extensions feature org-wide for users who don't need it. Be deliberate before setting an allowlisted server's `trust` to `true` at the admin level — it removes the confirmation prompt for every user in the org, not just you.
**Why (beginner):** Admin-level settings override local `url`, connection type, and `trust` values and can't be overridden by an individual user — good for consistency, but it means a misconfigured admin allowlist (or one server wrongly marked trusted) is an org-wide blast radius, not a single laptop.
**Caveat / contested:** Single (vendor) source; this is an enterprise-tier feature, not something most individual/beginner users will touch, so its relevance depends heavily on whether you're in a managed environment.
**Sources:** [Gemini CLI docs — Enterprise Admin Controls](https://geminicli.com/docs/admin/enterprise-controls/) (fetched 01 Aug 2026)
**Confidence:** vendor-documented

---

## Held pending fixes (not publish-ready)
- Whether Gemini CLI's UI shows any explicit "this tool description may contain untrusted/injected instructions" warning (the way some other MCP clients do) — official docs didn't confirm or deny this either way, and the results section of the one academic paper testing this (arXiv:2603.22489) remained inaccessible even on a fresh check. ⚠ #TBD (project-33 issue to be filed once mg_api access is confirmed)
- No CVE or public disclosure specific to a *malicious* (as opposed to merely buggy) third-party (non-Google) Gemini CLI extension was found this run — the one concrete extension-level bug sourced (prototype pollution in the official `security` extension's MCP server) was in a Google-authored extension. Risk category remains plausible/consistent with Google's own vetting disclaimer but undocumented as an actual incident. ⚠ #TBD

## CHANGELOG (grading → this entry)
1. **FIX (Skeptic):** The security-extension practice was labeled `independently-corroborated` despite resting on two Google pages plus one researcher (one independent publisher, not two). Relabeled `thin`.
2. **FIX (Skeptic):** "Remote code execution" overstated the security-extension bug's own scored vector (CVSS 7.1, low confidentiality impact); reworded to "prototype pollution... escalated to command execution," and defined prototype pollution and CWE-1321 for readers unfamiliar with the term.
3. **FIX (Skeptic):** Dropped the "after the 90-day disclosure window" rationale for the 5-month fix-to-writeup gap — the stated math (Oct 2025 + 90 days ≈ mid-Jan 2026) doesn't reach the actual March 2026 writeup date, so we state the gap without asserting an unverified explanation for it.
4. **FIX (Skeptic):** Practice 7's headline claim (PR-title hijacking across Gemini CLI/Claude Code/Copilot) was supported by none of its three originally-cited sources — the cited SecurityWeek article never mentions this research; it appeared only as an unrelated footer link. Swapped in the correct SecurityWeek article covering the actual "Comment and Control" research, and broadened "PR titles" to "issue bodies, PR titles, and comments" to match what the research actually covers.
5. **FIX (Skeptic):** CVE ID was asserted without support from its cited sources (all predate the CVE assignment). Added NVD/CIRCL citations for the CVE↔GHSA link and the CVSS 10.0-vs-7.8 scoring dispute, matching the fundamentals entry.
6. **FLAG (Skeptic):** "Keep Trusted Folders on" implicitly assumed on-by-default, contradicting the sibling fundamentals entry's finding that Google's own docs disagree on the default. Rewritten to state the contested default explicitly and give an actionable verification step.
7. **FLAG (Skeptic):** `excludeTools` practice caveat said "a single (official) source" while citing two Google URLs; reworded to "two Google pages, one vendor" for accuracy.
8. **FIX (Timekeeper):** Added a cross-reference to the July 2026 "Week of Sandbox Escapes" disclosures in the trust/yolo practice, since they postdate every source originally cited here.
9. **Beginner-panel FIX (elevated):** Added a top-of-entry plain-language definition of MCP and MCP servers — the single biggest comprehension gap in the original batch, since the whole entry assumed this understanding.
10. **Beginner-panel FIX:** `gemini mcp add ... --trust` and the extension-install command were shown as bare syntax fragments; both now include one complete, concrete worked example.
11. **Beginner-panel FIX:** Added the shared install-prerequisite note (`npm install -g @google/gemini-cli`, requires Node.js) to the top of this entry, matching the other two entries in this batch, since it had previously been the only place in the 3-entry set showing an install command at all.
