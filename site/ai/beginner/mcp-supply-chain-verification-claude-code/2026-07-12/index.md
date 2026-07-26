# MCP Supply Chain Verification for Claude Code — Beginner Guide (as of 12 Jul 2026)

> Beginner-friendly guide to safely connecting Claude Code to MCP servers without exposing your computer to malicious code.


<!-- Immutable dated snapshot. A refresh is a NEW snapshot-date dir. "Latest" computed by Grove's template. -->

# MCP Supply Chain Verification for Claude Code — Beginner Guide (as of 12 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **12 Jul 2026**, frozen here as a permanent archive entry. Graded by the 3-lens panel (Skeptic/Beginner/Timekeeper) + sensei on 2026-07-15. Facts are unchanged from the technical entry. This version is re-levelled for readers new to AI, the command line, and Ubuntu.

> ⚠️ **PROTOCOL NOTICE — 2026-07-28:** The MCP specification 2026-07-28 release candidate (locked 2026-05-21, publishes 2026-07-28) introduces **breaking protocol changes**: it removes the `initialize`/`initialized` handshake, eliminates `Mcp-Session-Id`, and mandates OAuth 2.0/OIDC with RFC 9207 `iss` validation. The practices below describe the protocol as of **12 Jul 2026**. After 2026-07-28, verify all session management and auth practices against the updated spec before following them. 🕒 **verify live.**

---

## What you need to know before reading this guide

**Claude Code** is Anthropic's AI coding assistant that runs on your computer as a command-line program. You give it tasks, and it can read files, write code, and run commands on your behalf.

**MCP** (Model Context Protocol) is the system that lets Claude Code connect to outside plug-ins called "MCP servers." Each MCP server gives Claude Code a new set of tools — for example, the ability to search the web, send emails, or talk to GitHub. You install and run these servers yourself.

**npm** is a package manager — a tool that downloads and installs software written in JavaScript. Many MCP servers are distributed through npm. You use it on the command line with commands like `npm install`.

**The core risk:** An MCP server runs as a program on your machine with your own user account's permissions. It can read your files, run commands, and connect to the internet. If you install a malicious MCP server, it can silently steal your passwords, SSH keys, and API credentials — before you even know anything is wrong.

This guide tells you exactly what to check before connecting any MCP server to Claude Code.

---

## How to read the labels

- ✅ **independently-corroborated** — 2+ independent publishers confirmed this
- 📄 **vendor-documented** — official documentation only (authoritative, single source)
- ⚠️ **WARNING** — skipping this step can cost money, break your machine, or expose your secrets
- 🕒 **verify live** — version numbers and details change fast; check the current value before acting

---

## Practice 1: Only connect MCP servers you have personally inspected, or that come from publishers you independently trust

**Do:** Before connecting any MCP server to Claude Code, find out who published it.

- The safest choice is an official server from Anthropic's own `@modelcontextprotocol/` family of npm packages, or a server published and maintained by the actual vendor of the service you want to use (under that vendor's own verified npm organisation).
- For any other community-published server, read its source code before the first run. Confirm who the author is: look at their GitHub account history, how long it has existed, and whether it links to a real company's domain.
- If the source code is not publicly available, treat it as untrusted by default and do not connect it.

**Why (beginner):** A website you browse in a browser is sandboxed — it can only do so much. An MCP server is different: it is an executable program running under your own user account. Connecting one you have not inspected is the same as downloading a stranger's program and running it on your computer. As of March 2026, roughly 15.4% of MCP servers had no public source code at all, making them impossible to audit before use.

**What goes wrong if you skip this:** You connect a server that looks useful. Behind the scenes it reads your SSH private keys, your AWS credentials, or your password manager's vault and sends them to an attacker. You see no error; you lose access to your cloud accounts, your repositories, or your bank.

**Caveat / contested:** Anthropic maintains a connector directory that lists MCP servers. Anthropic itself states it does not security-audit those listings — the criteria are about format and metadata, not code safety. A server being "in the directory" does not mean it is safe.

**Sources:**
[code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (Anthropic, fetched 2026-07-12) · [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (Anthropic, fetched 2026-07-12) · [nimblebrain.ai/blog/state-of-mcp-security-2026/](https://nimblebrain.ai/blog/state-of-mcp-security-2026/) (NimbleBrain, March 2026) · [toolradar.com/blog/mcp-server-security-best-practices](https://toolradar.com/blog/mcp-server-security-best-practices) (Toolradar, 2026)

**Confidence:** ✅ independently-corroborated

---

## Practice 2: Always pin MCP server versions — never let npm fetch "whatever is newest"

**What "pinning a version" means:** When you install a package with npm, you can tell it to get a specific numbered release (for example `2025.11.25`) instead of automatically grabbing the newest one. Locking to a specific number is called "pinning."

**Do:** Instead of running:

```
npx -y @modelcontextprotocol/server-filesystem
```

run this instead, with the explicit version number you have already inspected:

```
npx -y @modelcontextprotocol/server-filesystem@2025.11.25
```

In your `.mcp.json` configuration file (the file that tells Claude Code which MCP servers to use), write the version number in the `args` line:

```json
"args": ["-y", "@modelcontextprotocol/server-filesystem@2025.11.25"]
```

Also commit your `package-lock.json` file to version control (git). This file records the exact checksum of every package downloaded, so future installs match what you inspected.

🕒 **verify live:** As of this snapshot's research date, the current latest version of `@modelcontextprotocol/server-filesystem` is `2026.1.14`. Pin the version you have personally audited — not whichever version is newest at the moment you run the command.

**Why (beginner):** Attackers exploit version ranges by publishing a tiny "patch" release that adds malicious code. npm's default behaviour silently upgrades to the newest version every time you run a command. The Mastra npm supply chain attack (June 2026, attributed to an attacker group called Sapphire Sleet) infected over 140 packages this way by pushing a malicious dependency update through a compromised maintainer account; every version of Mastra after 1.13.0 was affected. Pinning means you only get the code you reviewed.

**What goes wrong if you skip this:** You install an MCP server, review it, and decide it is safe. Three weeks later npm silently upgrades it to a new version that contains a hidden payload. Your credentials are stolen from a version you never read.

**Caveat / contested:** Pinning stops silent upgrades, but if the version you pinned was already malicious at publish time, the pinned hash still matches — pinning alone is not a complete guarantee. Combine it with code inspection and run `npm audit` every time you bump to a new version.

**Sources:**
[stacklok.com/blog/examining-the-impact-of-npm-supply-chain-attacks-on-mcp/](https://stacklok.com/blog/examining-the-impact-of-npm-supply-chain-attacks-on-mcp/) (Stacklok, 2025) · [microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/) (Microsoft Security, June 2026) · [toolradar.com/blog/mcp-server-security-best-practices](https://toolradar.com/blog/mcp-server-security-best-practices) (Toolradar, 2026)

**Confidence:** ✅ independently-corroborated

---

## Practice 3: Use `--ignore-scripts` when installing any new MCP server package for the first time

**What "install scripts" means:** npm packages can include small shell scripts that run automatically the moment you install the package — before you have read any of the code. These are called lifecycle hooks, with names like `postinstall`. They are meant for legitimate purposes like compiling native code, but a malicious package uses them to steal your secrets the instant you run `npm install`.

**Do:** When evaluating a new MCP server package for the first time, install it like this:

```
npm install --ignore-scripts <package-name>@<version>
```

The `--ignore-scripts` flag tells npm to download the files but not run any of the package's shell scripts. Then read the package contents — especially the `scripts` section of `package.json` and any file it references in a `postinstall` entry — before deciding whether to trust and run the server.

⚠️ **WARNING:** If you run a plain `npm install` without `--ignore-scripts`, the package's `postinstall` code runs the moment installation begins — before you have seen what it does. Both the Sapphire Sleet / Mastra attack (June 2026) and the "postmark-mcp" backdoor (see Practice 8 below) delivered their malicious payloads through `postinstall` hooks. The attack executes silently the moment you run `npm install` — installation alone is enough; you do not need to import or use the package in your code.

**Why (beginner):** Imagine opening an envelope and having it spray poison gas before you can read the letter inside. That is what a malicious `postinstall` hook does. The `--ignore-scripts` flag lets you open the envelope safely and read what is inside before deciding whether it is safe.

**What goes wrong if you skip this:** Your SSH private key (`~/.ssh/id_rsa`), API keys stored in environment variables, and credential files are silently sent to an attacker the moment you run `npm install`. You see no error message. The theft happens in milliseconds.

**Caveat / contested:** `--ignore-scripts` prevents the hooks from running, but it does not prevent the malicious source code from being placed on your disk. You still need to read the code. Also, some legitimate packages genuinely need `postinstall` to compile native components. Once you have read the code and decided you trust it, you can run the hooks deliberately with `npm rebuild`.

**Sources:**
[microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/) (Microsoft Security, May 2026) · [microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/) (Microsoft Security, June 2026) · [checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (Checkmarx, 2025–2026)

**Confidence:** ✅ independently-corroborated

---

## Practice 4: Read the tool descriptions an MCP server gives Claude Code before trusting them — look for hidden instructions

**What "tool poisoning" means:** When an MCP server connects to Claude Code, it sends a list of tools along with text descriptions of what each tool does. Claude Code reads those descriptions the same way it reads your own instructions. A malicious server can hide extra commands inside those descriptions — for example, an instruction to also send a copy of your SSH key to an attacker's website. This attack is called "tool poisoning."

**Do:** When you connect a new MCP server, type `/mcp` directly in Claude Code's chat input (that is a forward-slash followed by `mcp` — it is a slash command, not a terminal command). This shows you the list of tools the server has sent. Read the descriptions yourself before Claude Code acts on them. Watch for:

- Unusually long or complex descriptions that seem like instructions rather than explanations
- Phrases like "you must" or "you must not" directed at Claude
- Instructions to read files that have nothing to do with the server's stated purpose
- Any instruction to "ignore prior instructions"
- Strange symbols or characters that look like garbled text (these may be encoded hidden commands)

**Why (beginner):** Think of tool descriptions as messages in a bottle coming from an outside server. If the server is malicious, those messages can contain hidden orders to Claude Code — orders you never wrote and never approved. A November 2025 attack on a WhatsApp MCP integration used exactly this technique to exfiltrate entire message histories. Academic research (arXiv 2603.22489, March 2026) rates this kind of attack as Critical severity.

**What goes wrong if you skip this:** Claude Code receives a hidden instruction from a malicious server telling it to read your `~/.ssh/id_rsa` file and send its contents to `attacker.example.com`. Claude Code follows the instruction as though you asked for it. You lose your SSH access.

**Caveat / contested:** Claude Code has some built-in analysis to detect harmful instructions, but Anthropic does not claim this is a complete defence. Research notes that "client implementations remain largely undefended against sophisticated metadata manipulation attacks." Reading the descriptions yourself is an important extra layer.

**Sources:**
[owasp.org/www-project-mcp-top-10/2025/MCP03-2025–Tool-Poisoning](https://owasp.org/www-project-mcp-top-10/2025/MCP03-2025%E2%80%93Tool-Poisoning) (OWASP MCP Top 10 beta v0.1, 2025) · [arxiv.org/html/2603.22489v1](https://arxiv.org/html/2603.22489v1) (academic paper, March 2026) · [truefoundry.com/blog/blog-mcp-tool-poisoning-gateway-defense](https://www.truefoundry.com/blog/blog-mcp-tool-poisoning-gateway-defense) (TrueFoundry, 2025–2026) · [code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) (Anthropic, fetched 2026-07-12)

**Confidence:** ✅ independently-corroborated

---

## Practice 5: Limit what each MCP server is allowed to do using Claude Code's permission rules

**What permissions mean here:** Claude Code has a settings file called `.claude/settings.json` (inside your home directory). In it you can write rules that control which MCP tools Claude Code is allowed to call automatically, and which ones it must ask you about first. This is called "least-privilege" — giving each server only the minimum access it actually needs.

**Do:** Open `.claude/settings.json` and use these rules:

- To block all MCP tools as a starting point (then allow only what you need), put `"mcp__*"` in the `deny` array.
- To allow all tools from one specific server (for example, Puppeteer), use `"mcp__puppeteer__*"` in the `allow` array.
- To allow only the read-only tools from a specific server (for example, GitHub), use `"mcp__github__get_*"`.

Never give an MCP server access to filesystem folders wider than the single project it needs to work with. When a server needs a password or token (such as a GitHub token or Jira API key), request the minimum permission level that server actually needs — not administrator access.

⚠️ **WARNING:** There is a mode called `bypassPermissions` (and a related flag `--dangerously-skip-permissions` sometimes mentioned for automated use). Turning this on skips **all** permission prompts — including MCP tool calls. This means Claude Code will read, write, delete, and execute shell commands across your entire home directory with no confirmation prompts at all. Anthropic's own documentation states: "Only use this mode in isolated environments like containers or VMs where Claude Code can't cause damage." Do not use `bypassPermissions` on your normal working computer. If you enable it and a malicious MCP server is connected, it can delete everything in your home directory or send all your files to an attacker, and Claude Code will not stop to ask you.

**Why (beginner):** Without permission rules, every MCP server you connect can ask Claude Code to do anything your user account can do. If one server is compromised or malicious, it can abuse those permissions to touch files and services that have nothing to do with its stated purpose. Permission rules act like a bouncer — the server can only do what you specifically approved.

**What goes wrong if you skip this:** A server you connected for one purpose (say, sending emails) uses its inherited permissions to also read files in your project folder, your home directory, and your credential files. You never notice because no permission prompt appears.

**Caveat / contested:** These permission rules are enforced by Claude Code itself, not by the operating system. A malicious MCP server running as a separate process can still make direct system calls regardless of what Claude Code's rules say. The next practice (sandboxing) adds the OS-level enforcement layer that catches this.

**Sources:**
[code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (Anthropic, fetched 2026-07-12) · [checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (Checkmarx, 2025–2026) · [stacklok.com/blog/the-enterprise-it-security-guide-to-claude-and-mcp/](https://stacklok.com/blog/the-enterprise-it-security-guide-to-claude-and-mcp/) (Stacklok, 2025–2026)

**Confidence:** ✅ independently-corroborated

---

## Practice 6: Run MCP servers inside a container or sandbox to cage them at the operating system level

**What a sandbox / container means:** A sandbox is a cage at the operating system level — the kernel itself (the core of Linux) enforces what the caged program can and cannot do. A container (such as Docker) is a similar idea: the program runs in an isolated box where it cannot see your real home directory or make arbitrary network connections. Both make it much harder for a malicious server to do damage even if it tries.

**Do:** Pick at least one of these layers and enable it:

**Option A — Claude Code's built-in sandbox (easiest starting point).**
In your Claude Code settings, set `"sandbox": {"enabled": true}`. On Ubuntu this uses a tool called `bubblewrap` (which must be installed: `sudo apt install bubblewrap socat`) to restrict Bash commands and child processes to your project's working directory and approved network domains. Also set `"failIfUnavailable": true` so Claude Code refuses to run at all if the sandbox cannot start, and `"allowUnsandboxedCommands": false` so nothing escapes the cage.

**Option B — Dev containers (stronger isolation).**
Run Claude Code inside a Docker container using a `.devcontainer/devcontainer.json` file with the Claude Code Dev Container Feature. This isolates Claude Code and all MCP servers from your real host filesystem. Add a startup script (`init-firewall.sh`, included in the reference container) to block unexpected outbound network connections.

**Option C — Stacklok ToolHive (open-source, per-server cages).**
An external tool that wraps each MCP server in its own container with configurable network and filesystem permissions. 🕒 **verify live** — confirm current availability and version before using.

⚠️ **WARNING:** Claude Code's built-in sandbox does NOT isolate the built-in Read, Edit, and Write file tools — only Bash commands and child processes. Also, `--dangerously-skip-permissions` (sometimes recommended for CI pipelines) bypasses the permission system entirely. Only use it inside a container where an escape causes no damage to your real machine.

**Why (beginner):** The MCP protocol itself does not sandbox servers. Without OS-level containment, a compromised server subprocess can read `~/.aws/credentials`, `~/.ssh/id_rsa`, and any other file your user account can access, then send it over a network connection. Sandboxing means the server is caged at the kernel level regardless of what Claude Code decides to do.

**What goes wrong if you skip this:** A malicious MCP server bypasses Claude Code's permission rules by making direct operating-system calls. Without a sandbox, the kernel has no fence to enforce. The server reads and exfiltrates your credentials directly.

**Caveat / contested:** The Linux bubblewrap sandbox requires the `bubblewrap` and `socat` packages and does not work on native Windows (you need WSL2 on Windows). The sandbox documentation also notes that allowing broad domains such as `github.com` can create paths for data exfiltration via domain fronting; a custom TLS-terminating proxy is needed for strict network inspection.

**Sources:**
[code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (Anthropic, fetched 2026-07-12) · [code.claude.com/docs/en/devcontainer](https://code.claude.com/docs/en/devcontainer) (Anthropic, fetched 2026-07-12) · [stacklok.com/blog/examining-the-impact-of-npm-supply-chain-attacks-on-mcp/](https://stacklok.com/blog/examining-the-impact-of-npm-supply-chain-attacks-on-mcp/) (Stacklok, 2025) · [nimblebrain.ai/blog/state-of-mcp-security-2026/](https://nimblebrain.ai/blog/state-of-mcp-security-2026/) (NimbleBrain, March 2026)

**Confidence:** ✅ independently-corroborated

---

## Practice 7: Treat `.claude/settings.json` and `.mcp.json` as executable code — review them carefully when you clone any project

**What these files do:** `.claude/settings.json` is Claude Code's configuration file. `.mcp.json` lists which MCP servers a project uses. Claude Code reads these files and acts on them. "Hooks" in `settings.json` are shell commands that Claude Code runs automatically. A malicious version of these files is effectively a program that runs on your computer.

**Do:**

- **Every time you clone a repository from the internet:** Before opening the project in Claude Code, open `.claude/settings.json` and `.mcp.json` in a plain text editor and read them. Look for MCP server entries you did not put there and hooks running commands you do not recognise.
- **In team projects:** Set up branch protection rules or CI checks so that any pull request modifying these files requires a human reviewer before it can be merged. Treat a new MCP server entry in `.mcp.json` the same way you would treat adding a new production software dependency.
- If API keys were ever pushed or exposed through these files by an untrusted contributor, rotate (replace) those keys immediately.

⚠️ **WARNING:** A real vulnerability, CVE-2025-59536 (CVSS score 8.7 out of 10 — rated "High"), allowed remote code execution through a malicious `.claude/settings.json` committed to a repository. Claude Code executed hooks defined in that file before the user saw any trust dialog. This was patched in Claude Code version **v1.0.111** and later (patch released October 2025). 🕒 **verify live** — check Anthropic's current security advisories page to confirm the minimum safe version, as it will advance over time. (The current Claude Code version as of July 2026 is v2.1.208.)

**Why (beginner):** Most people think of JSON files as harmless data. Claude Code treats `.claude/settings.json` as active logic: hooks run shell commands, MCP entries launch server processes, and permission allow-rules expand what the AI can do without asking you. A single pull request from a compromised contributor can install a persistent backdoor that runs every time you open the project.

**What goes wrong if you skip this:** You clone a repository from a colleague or from the internet. It contains a `.mcp.json` that points to a malicious MCP server. The next time you open the project in Claude Code, that server connects automatically and begins stealing your credentials. You never added it yourself; it was already there.

**Caveat / contested:** The workspace trust dialog that Anthropic added after CVE-2025-59536 provides an extra checkpoint, but the CVE itself demonstrated it can be bypassed in certain flows. Insider threats and compromised CI/CD pipelines remain attack vectors regardless of the dialog.

**Sources:**
[mintmcp.com/blog/claude-code-supply-chain-attacks](https://www.mintmcp.com/blog/claude-code-supply-chain-attacks) (MintMCP, 2026) · [mintmcp.com/blog/claude-code-cve](https://www.mintmcp.com/blog/claude-code-cve) (MintMCP, 2026) · [csoonline.com/article/4181230/claude-code-has-an-mcp-security-problem-and-your-developers-are-already-using-it.html](https://www.csoonline.com/article/4181230/claude-code-has-an-mcp-security-problem-and-your-developers-are-already-using-it.html) (CSO Online / Mitiga Labs research, 2026)

**Confidence:** ✅ independently-corroborated

---

## Practice 8: Check the exact npm package name and publisher before installing — attackers use look-alike names

**What typosquatting means:** Attackers publish packages with names that look almost identical to legitimate ones, hoping you misread or mistype. For example, a legitimate package might be `@modelcontextprotocol/server-filesystem` (with the `@` scope prefix) and an attacker publishes `modelcontextprotocol-server-filesystem` (without the `@`, so it looks similar but is a completely different, unreviewed package).

**Do:** Before installing any npm-distributed MCP server, check all four of these things:

1. **The exact namespace.** Official MCP reference servers are under `@modelcontextprotocol/`. Vendor servers should be under the vendor's own verified npm organisation (for example `@sentry/mcp-server-sentry`). A package without an `@` scope that claims to be an official server is suspicious.

2. **The publish date and version history.** A package with very few releases, or dozens of releases squeezed into a short time window, deserves extra scrutiny.

3. **The download count.** A package claiming to be a popular service's official MCP server but with almost no downloads is a red flag.

4. **The vendor's own documentation.** Find the vendor's official website and check what package name they list there. Do not rely on the npm page alone.

**Why (beginner):** The "postmark-mcp" attack is a real example of how patient and clever these attacks can be. An attacker published a package matching the legitimate Postmark MCP server name. For 15 releases the package was completely clean — nothing suspicious. Then in **version 1.0.16 only**, the package silently BCCed (blind carbon copied) every outgoing email to an attacker-controlled domain. The clean history of the first 15 releases made the malicious version much harder to detect. A separate report from Antiy CERT found 1,184 malicious packages in one marketplace at peak.

**What goes wrong if you skip this:** You install what you believe is the official email-sending MCP server. Every email Claude Code sends on your behalf is also secretly copied to an attacker. Your business emails, password reset links, and confidential correspondence are exposed.

**Caveat / contested:** Typosquatting detection is inherently reactive — the attacker publishes first, and detection comes later. `npm audit` catches known CVEs but will not flag a newly published malicious package that has a clean history. Cross-referencing vendor documentation is a useful check but not a guarantee. Registry-level provenance attestations (technologies called SLSA and sigstore) are emerging but not yet widely adopted in the MCP ecosystem.

**Sources:**
[checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (Checkmarx, 2025–2026) · [microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/) (Microsoft Security, May 2026) · [blog.cyberdesserts.com/ai-agent-security-risks/](https://blog.cyberdesserts.com/ai-agent-security-risks/) (CyberDesserts, 2026) · [toolradar.com/blog/mcp-server-security-best-practices](https://toolradar.com/blog/mcp-server-security-best-practices) (Toolradar, 2026)

**Confidence:** ✅ independently-corroborated

---

## Advanced practice (summary only): Team-wide allowlists using managed MCP configuration

If you are setting up Claude Code for a team, Anthropic provides a `managed-mcp.json` file that can be deployed to every developer's machine through device management software (Jamf, Intune, or similar fleet tools). When this file is present, Claude Code only connects to the servers it lists — individual developers cannot add their own. The file locations are:

- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `/etc/claude-code/managed-mcp.json`
- Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

Do not store API keys or credentials inside `managed-mcp.json` — any local user can read the file. Use environment variable expansion (`${VAR}`), OAuth flows, or a `headersHelper` to inject credentials at connection time.

This practice requires familiarity with device management tools and is best handled by someone with IT or DevOps experience. The sources below have full details.

**Sources:**
[code.claude.com/docs/en/managed-mcp](https://code.claude.com/docs/en/managed-mcp) (Anthropic, fetched 2026-07-12) · [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (Anthropic, fetched 2026-07-12) · [stacklok.com/blog/the-enterprise-it-security-guide-to-claude-and-mcp/](https://stacklok.com/blog/the-enterprise-it-security-guide-to-claude-and-mcp/) (Stacklok, 2025–2026)

**Confidence:** ✅ independently-corroborated (Anthropic docs + independent Stacklok analysis)

---

## Held pending fixes

- Anthropic connector directory review criteria page (`claude.ai/docs/connectors/building/review-criteria`): HTTP 403 during research run. Practice 1 caveat describes scope based on the MCP docs page; verify against the live page before citing directly. ⚠ #pending

---

## CHANGELOG

1. Re-levelled from the 2026-07-12 technical entry; facts unchanged.
2. Added a "What you need to know" section defining Claude Code, MCP, npm, and the core risk for readers with no prior background.
3. Each practice now opens with a plain-language definition of any technical term it introduces (pinning, lifecycle hooks, sandbox, container, typosquatting, tool poisoning).
4. Each practice now includes a "What goes wrong if you skip this" paragraph describing the concrete failure in everyday terms (lost account access, stolen emails, deleted files).
5. Team managed-MCP practice retained but moved to a summary-only section flagged as requiring IT/DevOps experience, rather than being dropped entirely.
6. All ⚠️ WARNING blocks retained verbatim, including the `bypassPermissions` WARNING with its specific consequence (reads, writes, deletes, executes across entire home directory with no prompts) and the PROTOCOL NOTICE block at the top.
7. The postmark-mcp incident is preserved accurately: 15 clean releases, malicious code introduced only in v1.0.16, BCCing outgoing emails to an attacker-controlled domain.
8. All source URLs and Confidence labels kept verbatim from the technical entry. No new facts or URLs introduced.

