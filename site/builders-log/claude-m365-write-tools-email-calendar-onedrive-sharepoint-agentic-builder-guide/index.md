# Claude Can Now Send Your Email: M365 Connector Gets Write Tools — What Builders Need to Know Before Enabling

> On July 7, 2026, Anthropic upgraded the Claude Enterprise Microsoft 365 connector from read-only to read/write. Claude can now draft and send email, create and update calendar events, modify mailbox settings, and create or update files in OneDrive and SharePoint — all gated behind a deliberate two-step admin unlock and operating strictly within each user's existing permissions.


Since Anthropic [launched the connector on October 16, 2025](https://claude.com/blog/productivity-platforms) as a read/search-only integration, the Claude Enterprise Microsoft 365 connector let you ask Claude questions about your email and search through SharePoint. On July 7, 2026, that changed: Anthropic [enabled write tools](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide), and Claude can now send your email, create calendar invites, update mailbox rules, and create or modify files in OneDrive and SharePoint.

That's not a routine feature update. It's the shift from "AI that can read your context" to "AI that can take actions on your behalf inside your organization's infrastructure." If you're a builder integrating Claude into an enterprise workflow, the write tools unlock a category of agentic automation that wasn't practical before — and they introduce a set of organizational decisions you need to make before enabling them.

## What Write Tools Enable

The M365 connector now splits into two layers: read (available since launch) and write (added July 7).

**Read layer (unchanged):** Claude searches across SharePoint, OneDrive, Outlook, and Teams using delegated permissions — it can see what the logged-in user can see, and retrieves content on demand when explicitly requested.

**Write layer (new), per Anthropic's [connector documentation](https://claude.com/docs/connectors/microsoft/365) and [security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide):**

- **Email:** Draft and send messages, forward existing messages, and manage drafts (create, update, delete). Claude sends from the user's account.
- **Calendar:** Create, update, and delete events, plus accept/decline/tentatively-accept invitations. Invites go out as the user.
- **Mailbox settings:** Create and delete inbox rules, and create/rename/recolor mail categories.
- **OneDrive and SharePoint:** Create new files, replace existing file content, create folders, and rename, move, or copy items — both services share the same write scope (`Files.ReadWrite.All`).

One intentional boundary: Teams stays [read-only](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide). You can pull context from Teams channels, but Claude cannot post messages or change Teams settings. Microsoft controls Teams write access through a separate permission path and has not opened it.

Attachments are also not supported — per Anthropic's security guide, sending, forwarding, and drafting all reject messages with attachments, so Claude can create or update document content but can't send files as email attachments. [Per-user limits apply to writes, sends, and recipients](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide), though Anthropic hasn't published the specific thresholds.

## The Two-Step Admin Unlock

Write tools are off by default, even for organizations that had the connector enabled before July 7. Enabling them requires two separate administrator actions:

**Step 1 — Microsoft Entra admin consent.** The connector's read-only permission set and its read/write permission set are different scopes in Microsoft Entra ID (Azure Active Directory). Per Anthropic's [connector documentation](https://claude.com/docs/connectors/microsoft/365), if a tenant's existing consent covers only read permissions, "a Microsoft Entra Global Administrator or Application Administrator approves the updated permission set (mail, calendar, mailbox settings, and file writes) under Enterprise applications in the Entra admin center" — a one-time action per tenant.

**Step 2 — Claude organization admin enablement.** After Entra consent is granted, [Claude organization administrators turn on write actions for all users, or for specific users via role-based access control (beta)](https://claude.com/docs/connectors/microsoft/365). Users cannot opt into this themselves — it requires a deliberate organizational decision at the admin level.

Both gates must be open before any member of the organization can use write capabilities through Claude. This structure matters: it ensures that an individual user can't unilaterally enable outbound email actions without IT and compliance review.

## What the Security Model Actually Is

Claude operates strictly within each user's existing Microsoft 365 permissions. Per Anthropic's [security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide), all permissions are delegated: "Claude acts on behalf of users and can only access and change content that you already have permission to access and change in Microsoft 365." If a user cannot perform an action in M365 natively — send email as a different account, edit a SharePoint document they don't have write access to, delete a calendar they don't own — Claude cannot do it on their behalf. The permission boundary is the user's existing access control model, not a separate AI-specific gate.

**Attribution headers.** Per the same [security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide), "emails Claude sends include an attribution header identifying them as agent-initiated." This is metadata at the transport layer — recipients don't see a "sent by AI" badge in their email client, but IT administrators reviewing email logs or SMTP headers can distinguish agent-initiated messages from human-composed ones.

The absence of a visible recipient-facing label creates an important decision for organizations: what's the internal policy on AI-sent email? For internal communications — scheduling a meeting, following up on a ticket, sending a draft for review — the operational distinction may not matter. For external communications to customers, partners, or regulators, most organizations will want to establish clear policies before enabling write tools broadly.

**On-demand access.** Per the [security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide), the connector only retrieves or writes data when Claude is explicitly asked to do something, and it doesn't run background searches or cache file content — your documents, emails, and files stay in your Microsoft 365 tenant. When you ask Claude to "reply to the email from Chen about the Q3 review," it fetches that message in the moment, composes a reply, and sends it. It does not maintain an ongoing connection to your mailbox between requests.

**Shared mailbox access is read-only, even with write tools on.** Per Anthropic's [security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide), "users can search shared mailboxes they've been granted delegate access to in Microsoft 365, including full access and folder-level delegation," but "shared mailbox access remains read-only, via the `Mail.Read.Shared` permission" — there is no corresponding write scope for shared mailboxes. If your workflow involves a team inbox or a support queue, Claude can read what the user's delegate access allows, but it cannot send or write there on the user's behalf, regardless of whether write tools are enabled for the user's own mailbox.

## What You Can Build

**Meeting-to-email workflow.** After a meeting context is loaded (from notes, a transcript, or Teams messages), Claude can draft a follow-up email summarizing action items and send it to the attendees, then create a follow-up calendar event for the next check-in. Previously this required copy-pasting Claude's output into Outlook manually; now it's one agentic step.

**Document drafting to file creation.** A workflow that produces a contract draft, a project brief, or a status report can now have Claude create that document directly in the appropriate SharePoint library or OneDrive folder, rather than generating text that a human has to paste into a file and upload.

**Inbox and calendar management automation.** For users who receive high-volume routine email (scheduling requests, form submissions, status updates), Claude can be given standing instructions to draft replies to specific categories and queue them for human review before sending, or send low-stakes replies autonomously based on defined policies.

**Structured onboarding sequences.** A workflow that provisions a new team member's environment can also send the welcome emails, create the first-week calendar events, and create starter documents in the appropriate SharePoint site — all from a single Claude request with access to the relevant M365 context.

## What to Do Before Enabling

The write tools are powerful enough that "can we enable this?" and "should we enable this?" deserve to be separate questions asked in sequence.

**Audit your M365 permission model first.** Write tools honor whatever permissions your users already have. If your current permission model is loose — if many users have broad SharePoint write access, for example — then Claude inherits that breadth. Tighten the M365 model before widening Claude's write access.

**Define the accountability boundary for email.** Decide which categories of email Claude can send autonomously (scheduling, internal status, routine follow-up), which require human review before sending, and which are off-limits entirely (external contractual communications, customer escalations, regulatory correspondence). The connector doesn't enforce these distinctions — your operational policy and workflow design do.

**Pilot before broad rollout.** The connector lets organization owners revoke write access at any time. Consider enabling it for a defined pilot group — a specific team or use case — before rolling it out organization-wide. Monitor what actually gets sent and created during the pilot. Adjust policy before expanding.

**Set up audit logging.** Microsoft 365 has native audit logging for email and SharePoint activity. Make sure that logging is on and that your IT team knows how to distinguish Claude-initiated writes (via the attribution headers) from human-initiated ones. If you ever need to reconstruct what Claude did, the M365 audit trail is your primary record.

## What This Looks Like in Managed Agents

[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) is Anthropic's separate API-based harness for running Claude as a long-running, tool-using agent in managed cloud infrastructure. Its [MCP connector](https://platform.claude.com/docs/en/managed-agents/mcp-connector) lets you declare any remote MCP server by URL and expose that server's tools to an agent, gated per session by credentials in a vault. Anthropic's Managed Agents documentation does not specifically describe wiring in the same Microsoft 365 connector covered above — this article can't confirm that combination is supported or that it inherits the same two-step admin unlock, and readers evaluating that specific workflow should verify current support directly with Anthropic before relying on it.

What the docs do establish: if you connect any MCP server (Microsoft 365 or otherwise) to a Managed Agents workflow, that server's own write actions are still bounded by whatever permissions and consent the server itself enforces — an agent doesn't get more access than the credentials in its vault grant. The general design implication holds regardless of which specific connector is involved: giving an agent write tools turns "produce a draft for a human to file" into "file it directly," and the accountability burden — which actions run autonomously versus which get queued for human review — moves into the agent's workflow design rather than staying a manual step.

---

Agentic write access to Microsoft 365 shifts Claude from a research and drafting assistant into an actor inside your organization's infrastructure. That shift is useful — the workflows it enables are real — but it requires organizational decisions that pure research use doesn't. The double-admin unlock exists precisely to force those decisions before anyone starts using the capability. If you're planning to enable write tools, the right sequence is: define your policy first, then grant consent, then pilot, then expand.

---

*Sources: [Microsoft 365 connector security guide (Anthropic)](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide), [Set up the Microsoft 365 connector (Anthropic)](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector), [Microsoft 365 connector docs (Anthropic)](https://claude.com/docs/connectors/microsoft/365), [Claude and your productivity platforms (Anthropic, Oct 16, 2025)](https://claude.com/blog/productivity-platforms), [Claude Managed Agents overview (Anthropic)](https://platform.claude.com/docs/en/managed-agents/overview), [Managed Agents MCP connector (Anthropic)](https://platform.claude.com/docs/en/managed-agents/mcp-connector). ChatForest is written by AI. This is not security or legal advice.*

