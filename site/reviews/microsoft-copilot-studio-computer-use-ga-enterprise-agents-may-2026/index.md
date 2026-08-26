# Microsoft Copilot Studio Computer Use Is Now GA — What Enterprises Need to Know

> Microsoft made computer use agents generally available in Copilot Studio on May 13, 2026. Agents now navigate any browser or desktop app using vision and reasoning — no API required. Here's what it does, what it can't do yet, and what the governance story looks like.


**At a glance:** Microsoft made computer use agents generally available in Copilot Studio on [May 13, 2026](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) ([confirmed](https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new) in Microsoft's own changelog). Agents can now see a screen, reason about what's on it, and take actions — click, type, scroll — across any browser or desktop application, without needing an API. Enterprise governance features (DLP, Purview integration, session replay, Azure Key Vault) ship at GA. Desktop app success rates ([~35%, per Microsoft's own FAQ](https://learn.microsoft.com/en-us/microsoft-copilot-studio/faqs-computer-use)) and handling of dynamic UI elements remain real limitations.

---

Every enterprise has applications that haven't shipped an API. Some of those applications run mission-critical workflows — HR systems, legacy ERPs, procurement portals, internal tools built on platforms that were never designed to be automated. For years, the answer was robotic process automation: record a macro, specify exactly which pixel to click, hope the UI doesn't change.

Computer use in Copilot Studio takes a different approach. Instead of recording exact coordinates, the agent looks at the screen, understands what it sees, and decides what to do next — the way a person would. It's a vision-and-reasoning approach; [Anthropic shipped a similar computer-use capability in Claude 3.5 Sonnet in October 2024](https://www.anthropic.com/news/3-5-models-and-computer-use), and Copilot Studio's GA build gives makers a choice between an OpenAI model and Anthropic's Claude Sonnet 4.5 to drive the underlying agent (see Model Choice below).

With GA on [May 13](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427), this is no longer a preview experiment. It's a production-ready capability with enterprise governance built in.

---

## What Computer Use Actually Does

When you add the computer use tool to a Copilot Studio agent, you give it four things: a browser, a screen, a keyboard, and the ability to read what's on the page and take the next logical step.

The agent doesn't navigate via selectors. Per [Microsoft's own FAQ for the tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/faqs-computer-use), it follows an iterative perception-reasoning-action loop: it captures a screenshot, processes what it sees using a vision model, decides what action to take (click, type, scroll, or wait), executes that action, and repeats until the task is done or it needs human input. The workflow branches naturally around what's actually on screen at each moment — not what the developer expected to be there when they built the automation.

This matters in practice because UIs change. A button moves. A workflow gets an extra confirmation screen. A vendor updates their portal layout. Selector-based automation breaks when this happens; computer use adapts.

### Setup

Getting started is intentionally low-friction. Per [Microsoft's setup documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use#add-computer-use-to-your-agent): create or open an agent in Copilot Studio, go to **Tools → Add tool → New tool → Computer use**, and describe the task in natural language. The agent handles the rest. There's no macro recording, no XPath selectors, no coordinate capture.

---

## The Governance Story

Microsoft has put substantial work into making computer use acceptable to enterprise IT and compliance teams, not just power users.

**DLP and environment isolation.** Copilot Studio agents generally — computer use included — run inside the same [data loss prevention (DLP) policy and environment-boundary framework](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) that governs the rest of Power Platform, configured through [data policies in the Power Platform admin center](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention). If your DLP policy blocks a connector or data domain, that restriction applies here too.

**Purview and Dataverse integration.** Every run is logged. Per [Microsoft's monitoring documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/monitor-computer-use), computer-use logs are stored in Dataverse by default, and admins can separately turn on **Send audit logs to Microsoft Purview** so run logs appear there under the activity term `CUAOperation`. For regulated industries, this changes the feasibility calculus significantly.

**Session replay.** Administrators and makers can watch exactly what the agent did during a run. [Microsoft's documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/monitor-computer-use) describes a session-replay screenshot series plus a per-step activity log of action types, action coordinates, user context used, and timestamps. This is the kind of observability that traditional RPA tools have provided for years, now available for AI agents.

**Run summaries.** Each run produces a structured summary — per the same documentation, this includes instruction text, inputs, total duration and number of actions, average time per action, number of screenshots, human escalation count, and machine/login details. Useful for both debugging and capacity planning.

---

## Credentials and Security

Computer use agents often need to authenticate into systems — which creates an obvious question about how credentials are handled.

Microsoft [provides two options](https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use#configure-optional-settings):

- **Internal storage**: credentials encrypted within Power Platform. Lower friction, appropriate for most scenarios.
- **Azure Key Vault**: enterprise-grade secret management with your existing key infrastructure.

In both cases, [Microsoft states that credentials are encrypted and never exposed to the AI model](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/computer-using-agents-now-deliver-more-secure-ui-automation-at-scale/) — the model sees the screen; it doesn't see the password. Authentication happens at the infrastructure layer.

---

## Human-in-the-Loop

Computer use doesn't have to run fully autonomously. Copilot Studio supports human-in-the-loop checkpoints — moments in the workflow where the agent pauses, describes what it's about to do, and waits for approval before proceeding.

Per [Microsoft's documentation on the feature](https://learn.microsoft.com/en-us/microsoft-copilot-studio/human-supervision-computer-use), these checkpoints trigger automatically when the model determines it needs confirmation or is missing information — Microsoft describes the trigger as "probabilistic AI model behavior" rather than a maker-configurable confidence threshold, and [its own FAQ warns](https://learn.microsoft.com/en-us/microsoft-copilot-studio/faqs-computer-use) this isn't a guaranteed safety fail-safe: it might not trigger in every situation a person would want a pause, and it might also trigger unnecessarily.

This is meaningful for high-stakes workflows. A computer use agent filing expense reports or updating inventory records can be configured to pause before any write operation, turning what might be an autonomous action into a supervised one.

---

## Model Choice

Copilot Studio's computer use supports multiple underlying vision models. Per [Microsoft's model table](https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use#add-computer-use-to-your-agent), OpenAI's Computer-Using Agent (CUA) and Anthropic's Claude Sonnet 4.5 are generally available at GA, with Claude Sonnet 4.6 and Claude Opus 4.6 available as experimental options (Opus 4.6 is billed at a premium rate). This gives organizations flexibility to align model choice with existing vendor relationships or compliance requirements.

---

## Where It Works Well — and Where It Doesn't

The honest performance picture is a wide gap between browser-based and desktop tasks.

### Web apps: ~80% success

For browser-accessible workflows — pulling data from a vendor portal, submitting a form, navigating an HR system's web interface — computer use performs reliably. [Microsoft's own FAQ for the tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/faqs-computer-use) puts web-based task success at "about 80%." The vision model handles layout changes well. This is where the legacy-software use case is strongest — internal intranets and procurement portals with no API of their own. If a person can access it through a browser, the agent generally can too.

### Desktop apps: ~35% success

Native desktop applications are harder. Rendering is more variable, accessibility APIs are inconsistent, and the agent has less surface area to reason about. The [same Microsoft FAQ](https://learn.microsoft.com/en-us/microsoft-copilot-studio/faqs-computer-use) puts desktop success at "about 35%" — meaningful enough to be useful for specific tasks, not reliable enough to replace human-operated workflows end to end.

### Dynamic UI elements

Dropdowns, date pickers, multi-select widgets, and custom-built interface components cause problems across both environments. [Microsoft's FAQ lists this explicitly](https://learn.microsoft.com/en-us/microsoft-copilot-studio/faqs-computer-use) as a known limitation: these elements behave differently from what the model was trained on, and the agent can enter a loop or get stuck if the screen doesn't respond the way it expected.

### Rate limits

Computer use runs are billed as Copilot Studio "agent actions," so they count against the same [generative-AI message quotas](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas) that apply to the rest of the platform — Microsoft's documented quotas are defined in requests per minute (RPM) and requests per hour (RPH) per Dataverse environment, and scale with how many prepaid message packs a tenant has purchased. When a tenant hits its quota, further messages fail until the window resets. For high-volume automation scenarios, this requires capacity planning.

---

## Use Cases Worth Taking Seriously

**Legacy ERP data extraction.** An agent that logs into SAP, navigates to a report view, extracts data into a table, and closes the session — without any SAP API integration — is a genuinely valuable automation for finance and supply chain teams.

**Application-to-application data transfer.** Moving data between systems that have no integration and no API: pull from system A, paste into system B. Not elegant, but it replaces a human doing the same task.

**Process compliance documentation.** An agent that walks through a workflow in a regulated system and produces a screenshot-by-screenshot audit trail of what was done, by whom (or what), and when.

**Web-based vendor workflows.** Submitting orders, checking shipment status, pulling invoices from supplier portals — all without waiting for a vendor to build an API.

---

## What This Is Not

Computer use is not a replacement for proper API integration where APIs exist. An API call is faster, more reliable, and more auditable than a vision-based UI interaction. If the system you're automating has an API, use it.

It's also not a general-purpose robotic process automation platform replacement yet. The desktop success rate is too low to confidently replace existing RPA deployments without significant testing.

What it is: an escape hatch for everything that falls outside what APIs and RPA can reach. That's a large and valuable category.

---

## Pricing

Computer use bills against Copilot Studio's usage currency, Copilot Credits, at the "Agent action" rate. Per [Microsoft's published billing rates](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management#copilot-credits-billing-rates), each step (one click, type, or navigation in the perception-reasoning-action loop) costs 5 Copilot Credits on a standard model (OpenAI CUA or Claude Sonnet 4.5) or 15 Copilot Credits on the premium model (Claude Opus 4.6); [Computer-Using Agent usage is explicitly not included in the Microsoft 365 Copilot per-user license](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management#copilot-credits-billing-rates), unlike some other agent actions.

Copilot Credits can be acquired several ways — a standalone Copilot Studio subscription, a Microsoft 365 Copilot license, prepaid Copilot Credit packs, or pay-as-you-go metering — and [only the pay-as-you-go option requires linking an Azure subscription](https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing); it is not a blanket requirement for using computer use. Organizations already paying for Power Platform or Microsoft 365 Copilot licenses should check their existing Copilot Credit allocation against projected computer use volume before provisioning additional capacity.

---

## Bottom Line

Computer use in Copilot Studio GA is a real enterprise capability, not a demo. The governance story — DLP, Purview, session replay, Key Vault, human checkpoints — is mature enough for production deployment in regulated environments. The web-based performance is solid.

The desktop gap (35% success) is the honest limitation that most coverage skips over. If your automation target is a native Windows application that doesn't render in a browser, computer use is not a reliable solution yet.

For organizations with legacy web-based workflows and no API access — which describes a large share of enterprise software estates — this is worth evaluating now.

**Rating: 3.5 / 5** — Production-ready for web workflows. Early-stage for desktop. The governance story is genuinely good.

---

*Computer use in Copilot Studio reached GA in [all commercial Power Platform geographies](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) (sovereign clouds — GCC, GCC High, DoD — were not part of the initial GA rollout, [per third-party coverage of the announcement](https://www.digitalapplied.com/blog/copilot-studio-computer-use-agents-ga-deep-dive)). An Azure subscription is needed only if you choose pay-as-you-go billing or Azure Key Vault for credentials — see Pricing above. For setup documentation, see [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use). This review is based on publicly available documentation and third-party coverage; ChatForest has not independently tested the product.*

