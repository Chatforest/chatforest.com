# Microsoft Scout: The First Autopilot Agent and What It Means for Builders

> Microsoft announced Scout at Build 2026 — the first agent in a new category called Autopilots. It runs persistently in the background, has its own Entra identity, performs multi-step tasks across Microsoft 365 and Windows desktop, and ships a developer SDK for custom skills. Here's what builders need to understand.


**At a glance:** Microsoft [announced Scout at Build 2026 on June 2, 2026](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) — the first agent in a new category Microsoft is calling Autopilots. Scout runs persistently in the background with its own [governed Entra identity](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/), connects to Microsoft 365 and Windows desktop, and operates on a [heartbeat schedule](https://learn.microsoft.com/en-us/microsoft-scout/faq) rather than waiting for user prompts. At launch, Microsoft opened Scout to [custom skills authored as markdown `SKILL.md` files, plus bundled MCP servers](https://learn.microsoft.com/en-us/microsoft-scout/overview) that developers can extend. The preview is available to organizations enrolled in Microsoft's [Frontier program](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview). Part of our **[Builder's Log](/builders-log/)**.

---

## The Category: Autopilots vs. Agents vs. Chatbots

Microsoft has been careful to [distinguish three things](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) at Build 2026:

- **Chatbots** — respond when you ask, do nothing when you don't
- **Task agents** — you invoke them, they complete a task, they stop
- **Autopilots** — always on, operating continuously in the background on your behalf, with their own persistent identity

Scout is the first Autopilot. It doesn't wait for you to open a chat window. It runs on a schedule, monitors signals in your work environment, and takes action when something meets the criteria you've configured. You set the scope, permissions, and autonomy levels. Scout handles the routine execution.

This is a different architecture than most AI agents builders have been working with. The user is not in the loop on every action. The agent has its own identity in the directory. Governance becomes a product feature rather than an afterthought.

---

## How Scout Works

### Work IQ as the context layer

Scout's understanding of your work environment comes from **Work IQ** — the Microsoft 365 intelligence layer announced at Build 2026 as part of [Microsoft IQ](/builders-log/microsoft-iq-work-foundry-fabric-web-context-layer-build-2026-builder-guide/). Microsoft describes Work IQ as [learning how you work, what you care about, and what needs to happen next](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/), becoming more useful over time as it reads signals already present in Microsoft 365.

For Scout specifically, Microsoft says Work IQ enables the agent to [identify deliverables and spot risks like stalled decisions](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/). Rather than you telling Scout what to monitor, it learns your patterns from the signals already present in M365.

### OpenClaw as the execution layer

Scout runs on **OpenClaw**, the open-source autonomous agent framework that [accumulated 180,000 GitHub stars within three months of its January 2026 launch](https://decrypt.co/369781/microsoft-scout-openclaw-enterprise-ai-agent). OpenClaw [enables desktop UI automation](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042) — meaning Scout can interact with Windows applications, including legacy systems that expose no modern API, by operating through the UI layer similar to robotic process automation tools.

This is worth flagging for builders: if your enterprise has line-of-business applications that predate REST APIs, OpenClaw-based automation reaches them. Microsoft has demonstrated Scout [filling out a purchase order form in a Windows desktop application from the 2000s](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042) and described it working with custom ERP systems, older CRM tools, and terminal emulators. The trade-off is that UI-layer automation is brittle when applications update their interfaces.

Microsoft's enterprise build is not the same as running community OpenClaw. Scout's OpenClaw runtime [runs inside Microsoft Execution Containers (MXC)](https://www.agenticwire.news/article/scout-openclaw-windows-agent-os), a policy-driven, OS-level sandboxing layer Microsoft [announced at Build 2026](https://github.com/microsoft/mxc) that adds containment the open-source version lacks. If you've been following our earlier [OpenClaw security coverage](/builders-log/openclaw-454-cve-clawhub-malicious-skills-builder-security-guide/) — [454+ CVEs](https://github.com/jgamblin/OpenClawCVEs), [1,184 malicious marketplace skills](https://cybersecuritynews.com/clawhavoc-poisoned-openclaws-clawhub/) — that additional sandboxing and vetting layer doesn't eliminate risk, but it's a different risk profile than running community OpenClaw directly.

### On-device execution

Scout [runs locally on the user's device inside a secure sandbox; all UI interactions are monitored and logged](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042). Sensitive fields can be [masked to prevent data leakage](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042) before they leave the device. Microsoft provides a [prominent taskbar icon that shows when Scout is actively performing desktop automation](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042), giving users immediate visibility and the ability to pause or stop it instantly.

---

## Heartbeat Mode and Persistence

Scout doesn't run continuously consuming CPU. It operates on what Microsoft calls **Heartbeat mode**: [configurable background check intervals of 15 minutes, 30 minutes, 1 hour, or 2 hours](https://learn.microsoft.com/en-us/microsoft-scout/faq). At each heartbeat, Scout runs a prompt you configure — for example, triaging your inbox or checking for schedule conflicts — without waiting for you to send a message.

This model matters architecturally, with one important caveat for builders: Microsoft's own documentation notes that [the application must remain open and the device must stay awake for heartbeat and automations to run — there is no true background service](https://learn.microsoft.com/en-us/microsoft-scout/overview) that survives a sleeping machine. What does persist is:

- [Configurable interval and work-hours settings](https://learn.microsoft.com/en-us/microsoft-scout/faq) per use case (high-frequency for urgent tracking, low-frequency for ambient awareness), each with its own permission policy
- Memory: Scout [remembers your preferences, decisions, and context across conversations](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- Actions happening asynchronously from the user's active work — you come back from a meeting and Scout has already scheduled the follow-up, blocked focus time, or flagged the deliverable that went silent, as long as the app was open and the device awake while it ran

---

## Governance: Per-Agent Entra Identity

Every Scout instance operates under [**its own governed Entra ID** — "not a shared, anonymous service account"](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/). Every action Scout takes is attributable to a known actor your directory already understands.

The practical consequences for builders and IT:

**Auditability**: All agent actions appear in your existing audit log infrastructure under the Scout instance's identity. You can tell what the agent did, when, to what, and under whose authorization.

**Policy enforcement**: Microsoft says [sensitivity labels and data-loss-prevention protections "are enforced in the moment"](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) against Scout's actions.

**Task-scoped credentials**: Microsoft says credentials used for specific tasks are [scoped to that task and redacted from logs or diagnostics](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) after use.

**Human sign-off gates**: Microsoft says [sensitive actions can require a human to sign off before they proceed](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/). Microsoft's own documentation confirms the mechanism: before a sensitive action such as [sending an email or running a command that requires approval, Scout pauses and shows exactly what it plans to do](https://learn.microsoft.com/en-us/microsoft-scout/faq), and you can approve, always-allow, or deny it.

**Explicit resource approval**: Scout [accesses only services and data your account is permitted to use](https://learn.microsoft.com/en-us/microsoft-scout/faq), and by default can't access files outside your configured workspace directory unless you explicitly grant permission.

---

## What Scout Does Today

Current Autopilot capabilities Microsoft has described in preview:

**Scheduling and time management**
- [Proactively scheduling meetings across time zones](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)
- [Blocking calendar focus time](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) for heads-down work
- [Flagging important meetings and generating preparation materials](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)

**Project and workflow tracking**
- [Identifying deliverables](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) to maintain a picture of what's expected and when
- [Spotting risks like stalled decisions](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)
- Cross-platform coordination: Scout [connects to Teams, Outlook, OneDrive, and SharePoint](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)

**Legacy application automation** (via OpenClaw desktop)
- [Form filling in Windows desktop applications](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042), including software from the 2000s
- Navigation in [terminal emulators and legacy ERP or CRM interfaces](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042)
- Multi-step workflows spanning modern web apps and older desktop software

These are the built-in capabilities. The extensibility story is the more interesting one for builders.

---

## Developer SDK: Building Custom Scout Skills

At Build 2026, Microsoft opened Scout to custom skills built by third-party developers.

### What the skill model enables

Microsoft's skill mechanism is markdown, not code: a skill is a [`SKILL.md` file — a YAML frontmatter block with a name and description, followed by instructions in Markdown](https://learn.microsoft.com/en-us/microsoft-scout/faq) — placed in a skills directory (`~/.copilot/skills/` for a single machine, or a workspace-synced folder for team distribution). Scout [automatically discovers custom skills at the start of each conversation](https://learn.microsoft.com/en-us/microsoft-scout/faq); there's no compilation or registration step. Alongside custom skills, Scout also [ships bundled MCP servers](https://learn.microsoft.com/en-us/microsoft-scout/faq) — including `@microsoft/workiq` for Microsoft 365 context and `@playwright/mcp` for browser automation — and developers can wire in additional MCP servers for external tools and data sources.

Skill authoring [borrows from OpenClaw's open-source skill model](https://www.aguidetocloud.com/blog/microsoft-scout-mcp-servers-and-custom-skills/): if you've already written OpenClaw skills, the pattern is familiar.

### What builders can build

The skill model opens several categories:

**Industry-specific applications**: Skills that teach Scout to navigate factory-floor systems, clinical EHR interfaces, legal document management platforms, or financial trading tools. These are the legacy environments with no modern API that OpenClaw UI automation was built for.

**Specialized enterprise software**: If your organization runs a custom internal application, you can build a Scout skill that lets the agent interact with it. Early partners at Build 2026 [demonstrated integrations with SAP, ServiceNow, and mainframe terminal emulators](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042).

**Custom business processes**: Skills encoding your organization's specific workflows, such as a multi-step vendor onboarding process or an expense approval chain that requires extracting data from PDFs.

### Publishing and distribution

There's no public Scout skills marketplace yet. For team distribution today, Microsoft's own skills-folder model already supports a private-catalog approach: alongside skills scoped to a single machine, [workspace skills placed in a synced folder are available across your devices](https://learn.microsoft.com/en-us/microsoft-scout/faq) — no public marketplace infrastructure required.

---

## The OpenClaw Question

Builders who've been following OpenClaw's security trajectory will want to understand where Microsoft Scout sits relative to the open-source version.

Microsoft's enterprise build is not community OpenClaw. Key differences:

- Scout's OpenClaw runtime runs inside **[Microsoft Execution Containers (MXC)](https://github.com/microsoft/mxc)** — a policy-driven sandboxing layer that Microsoft [confirms Scout's OpenClaw node and gateway run inside on Windows](https://www.agenticwire.news/article/scout-openclaw-windows-agent-os), with [multiple containment backends spanning process isolation up to VM-level isolation](https://github.com/microsoft/mxc). Community OpenClaw has no equivalent built-in containment layer.
- The **skill distribution path** for Scout goes through Microsoft-vetted channels, not ClawHub. The [1,184 malicious skills planted in ClawHub's public marketplace](https://cybersecuritynews.com/clawhavoc-poisoned-openclaws-clawhub/) are not a vector for Scout-delivered skills (they remain a concern for anyone running community OpenClaw and pulling from ClawHub directly).
- **All UI interactions are monitored and logged** in Scout, with masking available for sensitive fields (see [Microsoft's description](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042) above). Community OpenClaw has no equivalent built-in requirement.

This doesn't make Scout immune to supply chain risk. But the threat model is materially different from deploying raw community OpenClaw in an enterprise context. If your security team [blocked OpenClaw based on Gartner's advisory to block downloads and traffic](https://www.csoonline.com/article/4129867/what-cisos-need-to-know-about-clawdbot-i-mean-moltbot-i-mean-openclaw.html), the Scout risk assessment requires a separate conversation — the surface area is different.

---

## Availability: What the Preview Requires

Scout's preview is gated through Microsoft's **[Frontier program](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)**, the experimental track for early access to advanced Microsoft 365 AI capabilities. Per Microsoft's own admin documentation, the requirements are:

1. **Frontier program enrollment** — an admin turns on Copilot Frontier for the organization in the Microsoft 365 admin center
2. **Intune policy configuration** — an IT admin must configure a Microsoft Scout Intune policy on target devices before sign-in will succeed
3. **Opt-in attestation** — because Scout [can route data outside Microsoft 365 to third-party inference paths, admins must explicitly attest and opt in](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)
4. **GitHub Copilot license** — each user needs an active [GitHub Copilot Business or Enterprise license](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview) (not Copilot Pro — Microsoft's docs are explicit that "a GitHub Copilot license alone doesn't grant Frontier access, and Frontier access alone doesn't work without a Copilot license")

This is not something that activates for all Microsoft 365 users automatically. It's a deliberate enrollment process designed for organizations that want to run on the bleeding edge and accept the experimental stability trade-off.

The skill-building capabilities are available in conjunction with preview access — you don't need to be an end user of Scout to build skills for it, but testing them requires a Frontier-enrolled environment.

---

## Builder Decision Guide

**If you're an enterprise M365 shop actively piloting AI agents**: Scout's preview is worth enrolling for. The governance model — per-agent Entra identity, Purview integration, human sign-off gates — is the most coherent enterprise agent identity story Microsoft has shipped. Even if you don't adopt Scout broadly, running the preview gives you concrete data on the Autopilot pattern and its operational implications.

**If you build enterprise software (ERP, vertical apps, specialized tools)**: Building custom Scout skills is a distribution opportunity. An SAP skill, a ServiceNow skill, a clinical EHR skill — these are high-value integrations that your customers will want, and Microsoft [already named three partners in this category at Build 2026](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042). The private folder-based distribution path means you don't need marketplace approval to ship.

**If you build on OpenClaw and are concerned about the CVE situation**: Microsoft's Scout is not a solution to your existing community OpenClaw security posture. These are different deployment environments. If you're running community OpenClaw, the [security remediation checklist](/builders-log/openclaw-454-cve-clawhub-malicious-skills-builder-security-guide/) still applies.

**If you're building your own always-on background agents**: Scout is the reference implementation for the governance pattern. Per-agent identity, configurable heartbeat, explicit resource approval, human sign-off gates — these aren't Microsoft-specific inventions. They're the right architecture for ambient autonomous agents operating in enterprise environments. Whether you build on Microsoft's stack or not, these design decisions apply.

**If you're watching and waiting**: Frontier program enrollment is low-cost to evaluate. The bigger question is whether your organization's security team will approve the enrollment terms and the expanded agent permissions. That conversation is worth having now, before there's timeline pressure.

---

## What to Watch

- **No public skill marketplace yet**: Today's distribution is limited to synced skill folders and private enterprise catalogs. If Microsoft builds a public marketplace, it would create a distribution channel comparable to the App Store model for enterprise agent skills — but as of this writing there's no confirmed plan or date for one.
- **[Work IQ APIs GA on June 16](https://decrypt.co/369781/microsoft-scout-openclaw-enterprise-ai-agent)**: If you're building skills that rely on M365 context, the June 16 GA date for Work IQ APIs is the relevant milestone. Scout itself uses Work IQ as its intelligence layer.
- **Frontier program expansion**: General availability depends on Frontier feedback. Microsoft hasn't given a timeline, but the preview enrollment process gives a clear signal that this is a real product, not a concept.
- **OpenClaw governance trajectory**: Microsoft's enterprise hardening of OpenClaw, combined with its contribution of policy controls back upstream, could change the community security posture over time. Track whether the CVE closure rate improves as Microsoft's influence increases.

---

*Microsoft announced Scout on June 2, 2026, at Build 2026. Skill-building is available to Frontier-enrolled organizations. This article is based on Build 2026 announcements, the [Microsoft 365 Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/), [Microsoft Learn's Microsoft Scout documentation](https://learn.microsoft.com/en-us/microsoft-scout/faq), [msftnewsnow.com](https://msftnewsnow.com/microsoft-scout-autopilot-agent-for-microsoft-365/), [windowsnews.ai](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042), and [Decrypt](https://decrypt.co/369781/microsoft-scout-openclaw-enterprise-ai-agent).*

