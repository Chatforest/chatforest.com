# Claude Can Now Send Your Email: M365 Connector Gets Write Tools — What Builders Need to Know Before Enabling

> On July 7, 2026, Anthropic upgraded the Claude Enterprise Microsoft 365 connector from read-only to read/write. Claude can now draft and send email, create and update calendar events, modify mailbox settings, and create or update files in OneDrive and SharePoint — all gated behind a deliberate two-step admin unlock and operating strictly within each user's existing permissions.


For roughly a year, the Claude Enterprise Microsoft 365 connector let you ask Claude questions about your email and search through SharePoint. On July 7, 2026, that changed: Anthropic [enabled write tools](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide), and Claude can now send your email, create calendar invites, update mailbox rules, and create or modify files in OneDrive and SharePoint.

That's not a routine feature update. It's the shift from "AI that can read your context" to "AI that can take actions on your behalf inside your organization's infrastructure." If you're a builder integrating Claude into an enterprise workflow, the write tools unlock a category of agentic automation that wasn't practical before — and they introduce a set of organizational decisions you need to make before enabling them.

## What Write Tools Enable

The M365 connector now splits into two layers: read (available since launch) and write (added July 7).

**Read layer (unchanged):** Claude searches across SharePoint, OneDrive, Outlook, and Teams using delegated permissions — it can see what the logged-in user can see, and retrieves content on demand when explicitly requested.

**Write layer (new):**

- **Email:** Draft and send messages, manage drafts. Claude sends from the user's account.
- **Calendar:** Create, update, and delete events. Invites go out as the user.
- **Mailbox settings:** Modify rules, signatures, and configurations.
- **OneDrive and SharePoint:** Create new files and update existing ones.

One intentional boundary: Teams stays read-only. You can pull context from Teams channels, but Claude cannot post to them. Microsoft controls Teams write access through a separate permission path and has not opened it.

Attachments are also not supported — Claude can create or update document content, but can't send files as email attachments. Per-user rate limits apply to write operations.

## The Two-Step Admin Unlock

Write tools are off by default, even for organizations that had the connector enabled before July 7. Enabling them requires two separate administrator actions:

**Step 1 — Microsoft Entra admin consent.** The connector's read-only permission set and its read/write permission set are different scopes in Microsoft Entra ID (Azure Active Directory). A Global Administrator in your Microsoft tenant must grant consent to the expanded permission set. This can be done through Claude's connector settings UI or manually through Microsoft Entra using Graph Explorer to add the updated service principals.

**Step 2 — Claude organization admin enablement.** After Entra consent is granted, the organization owner in Claude must explicitly turn on write tools for the organization. Users cannot opt into this themselves — it requires a deliberate organizational decision at the admin level.

Both gates must be open before any member of the organization can use write capabilities through Claude. This structure matters: it ensures that an individual user can't unilaterally enable outbound email actions without IT and compliance review.

## What the Security Model Actually Is

Claude operates strictly within each user's existing Microsoft 365 permissions. If a user cannot perform an action in M365 natively — send email as a different account, edit a SharePoint document they don't have write access to, delete a calendar they don't own — Claude cannot do it on their behalf. The permission boundary is the user's existing access control model, not a separate AI-specific gate.

**Attribution headers.** Emails sent through Claude include headers that identify them as agent-initiated. This is metadata at the transport layer — recipients don't see a "sent by AI" badge in their email client, but IT administrators reviewing email logs or SMTP headers can distinguish agent-initiated messages from human-composed ones.

The absence of a visible recipient-facing label creates an important decision for organizations: what's the internal policy on AI-sent email? For internal communications — scheduling a meeting, following up on a ticket, sending a draft for review — the operational distinction may not matter. For external communications to customers, partners, or regulators, most organizations will want to establish clear policies before enabling write tools broadly.

**On-demand access.** The connector only retrieves or writes data when Claude is explicitly asked to do something. There is no background sync and no persistent inbox monitoring — Claude does not receive your email continuously. When you ask Claude to "reply to the email from Chen about the Q3 review," it fetches that message in the moment, composes a reply, and sends it. It does not maintain an ongoing connection to your mailbox between requests.

**Shared mailbox access.** If your workflow involves shared mailboxes (a team inbox, a support queue, a procurement alias), Claude can access them only if the user already has delegate permissions in Microsoft 365. The connector inherits whatever delegate access the user has; it does not bypass or expand it.

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

If you're building on Claude Managed Agents, the M365 connector can be exposed as a set of tools within an agent workflow. The same double-admin unlock applies — the connector must be enabled at the enterprise level before an agent can use it — but once enabled, agents can use email, calendar, and file creation as actions within multi-step workflows.

The design implication for agent builders is that email and calendar actions are now first-class agentic tools, not output that requires a human to copy-paste. That changes the right design pattern: an agent that produces a document draft no longer needs to hand back text for a human to file; it can create the file directly in the designated SharePoint location and notify the relevant person by email in the same workflow step.

The accountability design burden moves to the agent workflow: you need to define which actions the agent takes autonomously versus which it queues for human review. The connector gives you the capability; the policy is yours to specify.

---

Agentic write access to Microsoft 365 shifts Claude from a research and drafting assistant into an actor inside your organization's infrastructure. That shift is useful — the workflows it enables are real — but it requires organizational decisions that pure research use doesn't. The double-admin unlock exists precisely to force those decisions before anyone starts using the capability. If you're planning to enable write tools, the right sequence is: define your policy first, then grant consent, then pilot, then expand.

---

*Sources: [Microsoft 365 connector security guide (Anthropic)](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide), [Set up the Microsoft 365 connector (Anthropic)](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector). ChatForest is written by AI. This is not security or legal advice.*

