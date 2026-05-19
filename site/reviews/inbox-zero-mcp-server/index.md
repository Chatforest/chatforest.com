# Inbox Zero MCP Server — Open-Source AI Email Assistant for Gmail and Outlook

> Inbox Zero is an open-source AI email assistant that helps you reach inbox zero with automated triage, smart replies, and bulk unsubscribe. 10.7K GitHub stars, MCP integration for Claude and Cursor. Now supports Gmail and Microsoft Outlook.


Part of our **[Communication MCP category](/categories/communication/)**.

*At a glance: 10,717 GitHub stars, 1,329 forks, actively maintained (daily commits as of May 2026), v2.30.0 (May 18, 2026), TypeScript/Next.js, 15K+ signups, hosted version at getinboxzero.com. Now supports Gmail and Microsoft Outlook. Founded by Elie Steinbock. Not listed on PulseMCP.*

Inbox Zero is a full-featured AI email assistant that happens to also be an MCP server. Unlike most MCP servers that are purpose-built protocol adapters, Inbox Zero is a standalone web application — a Next.js app with a PostgreSQL backend, Redis caching, and its own web UI — that exposes MCP tools as one of several integration surfaces.

The key differentiator: while raw email MCP servers give AI agents IMAP/SMTP access and let them figure out what to do, Inbox Zero layers AI intelligence on top. Its MCP tools expose *high-level operations* — "which emails need my reply?" and "draft a response to this thread" — rather than raw message fetching. The AI logic lives in Inbox Zero's backend, not in the consuming agent.

## What It Does

### AI Personal Assistant

The core feature is a plain-text prompt system where you describe how your email should be handled in natural English:

> "Archive newsletters I haven't opened in 2 weeks. Label anything from my team as 'Priority'. Draft polite declines for cold outreach."

The assistant then processes incoming email against these rules, taking actions a human assistant would: drafting replies, labeling, archiving, replying, forwarding, marking spam, and triggering webhooks. This is closer to a virtual assistant than a mail filter.

### MCP Tools

Inbox Zero exposes several high-level tools via MCP:

- **getEmailsNeedingReply** — identifies messages in your inbox that require a response, using AI to distinguish between FYI emails and action items
- **getEmailsToFollowUpOn** — tracks sent emails where you're waiting for a reply
- **draftReply** — generates contextual email responses using the AI backend
- **summarizeThread** — condenses email conversation threads into concise summaries

These tools are designed for use from Cursor, Windsurf, or Claude Desktop. The MCP server connects to your Inbox Zero account (hosted or self-hosted) and exposes these capabilities through the standard MCP protocol.

### Reply Zero

Tracks two things: emails that need your reply (inbox obligations) and sent emails awaiting responses (follow-up tracking). This is the "accountability layer" — it won't let important threads slip through the cracks.

### Smart Categories

Automatically categorizes every sender who's ever emailed you based on patterns — not just folder rules, but AI-driven sender classification that adapts over time.

### Bulk Unsubscriber

One-click unsubscribe from newsletters and marketing emails in bulk, with analytics showing which subscriptions you actually open.

### Cold Email Blocker

Identifies and filters unsolicited outreach — sales emails, recruitment spam, and vendor pitches — before they clutter your inbox.

### Email Analytics

Dashboard showing email volume, response times, top senders, and activity patterns. Useful for understanding where your email time actually goes.

## Technical Architecture

Inbox Zero is a substantial application, not a lightweight MCP adapter:

- **Frontend:** Next.js with Tailwind CSS and shadcn/ui
- **Backend:** Next.js API routes with Prisma ORM
- **Database:** PostgreSQL
- **Caching:** Upstash (serverless Redis)
- **Monorepo:** Turborepo
- **Email:** OAuth integration with Google (Gmail) and Microsoft (Outlook/Microsoft 365) — both now supported
- **Analytics:** PostHog, Tinybird
- **AI:** OpenAI for classification and generation

The MCP integration is one layer on top of this stack. Your AI agent talks to the MCP server, which talks to the Inbox Zero backend, which talks to Gmail via OAuth.

## Who Built It

**Elie Steinbock** (elie222) — solo founder based in Tel Aviv. Cursor Ambassador. Also created Draft Fantasy (250K+ users) and Skilled (Israeli freelance developer platform). Active YouTube channel about open source and AI coding. Inbox Zero was #1 on GitHub Trending. Indie hacker, not VC-backed (no public funding rounds).

## Pricing

**Self-hosted:** Free and open source. Requires running your own Next.js app, PostgreSQL database, Redis instance, and configuring OAuth credentials with Google.

**Hosted (getinboxzero.com):**
- **Starter:** $18/month (annual) / $20/month (monthly) — AI assistant, Smart Categories, bulk tools, analytics, Meeting Briefs
- **Plus:** $28/month (annual) / $35/month (monthly) — 2 email accounts, Slack integration, auto-file attachments, unlimited knowledge base, email digests
- **Professional:** $42/month (annual) / $50/month (monthly) — team analytics, priority support, dedicated onboarding
- **Enterprise:** Custom pricing — SSO, SCIM, on-premise deployment
- 7-day free trial on all plans (no free tier — the $6-12/month individual plan was discontinued)
- Student/nonprofit/open-source discounts available on request

## What's Good

**High-level intelligence, not raw access.** MCP tools expose AI-processed results — "emails needing reply" is more useful than "fetch all messages." The agent-facing interface is simpler and more actionable than working with raw IMAP.

**Full application behind the MCP.** The web UI, analytics, and rule engine mean you're not dependent on the MCP client for everything. You can configure rules in the browser and let the AI run in the background, then use MCP for ad-hoc queries from your IDE.

**Active development.** Daily commits, v2.30.0 (May 18, 2026) — three minor version bumps since January. This isn't a weekend project — it's a maintained product with a real user base (15K+ signups).

**Self-hostable.** Full open source, you can run everything on your own infrastructure for zero cost. Important for email, which is among the most sensitive data you have.

**Outlook support live.** Microsoft Outlook and Microsoft 365 are now fully supported alongside Gmail. This was the most notable gap in the initial review — it's resolved.

**Meeting Briefs.** Pre-meeting briefings (launched January 2026) pull context from your email and calendar before scheduled calls. MCP tools were added to surface meeting briefs to AI agents. Available on all paid tiers.

**Pipedream integration.** Added January 2026: a single OAuth connection unlocks 10,000+ tools from 3,000+ apps via Pipedream. This extends the range of actions the AI assistant can take well beyond email.

**MCP security grade A.** loaditout scanned the MCP server in April 2026 and assigned an A security grade (issue #2192).

**Plain-text rule system.** Describing email rules in natural English is genuinely easier than configuring filter chains. The prompt-based approach matches how people actually think about email management.

## What's Not

**Limited provider support.** Gmail and Microsoft Outlook are both now supported (Outlook was in-progress at the time of initial review). General IMAP/SMTP support (other providers) remains an open issue — issue #925 is still being tracked.

**Heavy self-hosting requirements.** Running Next.js + PostgreSQL + Redis + OAuth setup is significantly more complex than most MCP servers, which are typically single-binary or `npx` installs. This is a full web application, not a lightweight tool.

**Limited MCP tool count.** Only 4 MCP tools exposed. Compared to dedicated email MCP servers like darinkishore/Inbox-MCP (6 tools, including send/search/archive) or AgentMail (62 tools), the MCP surface area is narrow. You can't send emails or manage labels directly via MCP.

**No PulseMCP listing.** Absent from the PulseMCP directory entirely, which suggests limited MCP-specific adoption despite the main project's popularity.

**Pricing jumped.** The $6-12/month individual tier and free tier are gone. Entry is now $18/month (Starter) or $20/month monthly, putting it firmly in competition with Superhuman ($30/month) — a polished commercial product with years of optimization. The pricing shift signals a move upmarket but removes accessibility for individual users on a budget.

**Single maintainer risk.** Despite 9,915 commits, this is primarily a solo project. The CLA requirement and contributor guidelines suggest some community involvement, but bus factor is a concern for an application handling your email.

## Security Considerations

- OAuth tokens encrypted with `EMAIL_ENCRYPT_SECRET` and `EMAIL_ENCRYPT_SALT` in the database
- SECURITY.md exists in the repository (responsible disclosure process)
- "Human in the loop" design — MCP actions require host application consent before execution
- Self-hosting keeps all email data on your infrastructure
- No Inbox Zero-specific CVEs found; loaditout assigned Grade A to the MCP server (April 2026, issue #2192)
- The broad attack surface of a full web application (Next.js, PostgreSQL, Redis, OAuth) is inherently larger than a minimal MCP adapter — more components means more potential vectors
- PostHog and Tinybird analytics integrations mean some usage data flows to third parties on the hosted version

## The Competition

**darinkishore/Inbox-MCP** — Nylas-based email MCP server. 6 tools (filter, triage, batch archive, search, read, send). Supports Gmail, Outlook, iCloud, Yahoo, and IMAP through Nylas API abstraction. Simpler, more tools, multi-provider. Free for up to 5 accounts.

**AgentMail** — YC S25, $6M seed (March 2026). 62 MCP tools. Gives AI agents their own email inboxes with disposable addresses, structured parsing, and webhook notifications. Purpose-built for agent workflows, not human email management. Different use case.

**Cloudflare Agentic Inbox** — Self-hosted email client with built-in AI agent running entirely on Cloudflare Workers. MCP server at `/mcp` endpoint. Open source, serverless, no database needed. Early stage.

**patrickfreyer/apple-mail-mcp** — Apple Mail integration for macOS users. Read, search, compose, organize via natural language. macOS only.

**codefuturist/email-mcp** — Full IMAP + SMTP support. Raw email access (read, search, send, manage). Provider-agnostic. Low-level but flexible.

## Bottom Line

Inbox Zero occupies an unusual position in the MCP ecosystem: it's primarily an email productivity application that happens to expose MCP tools, rather than an MCP server that happens to handle email. The 10.5K stars reflect its value as an email app, not as an MCP integration.

The MCP tools themselves are limited (4 tools, read-only) but intelligently designed — they expose AI-processed insights rather than raw data. If you already use Inbox Zero for email management, the MCP integration is a nice bonus. If you're specifically looking for an MCP server to give your AI agent comprehensive email control (send, search, label, archive), dedicated email MCP servers like Inbox-MCP or AgentMail offer more.

**Rating: 3.5/5** — A strong email productivity application with a narrow but well-designed MCP integration. Since the initial review, Outlook support has launched (key gap resolved), Meeting Briefs is now a built-in feature with MCP tools, and Pipedream adds 10,000+ external tool integrations. The MCP security posture earned a Grade A. On the other hand, the $6-12/month individual tier is gone — entry is now $18/month, pricing it out of reach for casual individual users. The MCP layer remains limited (4 core tools) compared to dedicated email MCP servers, and it's still absent from PulseMCP. Worth it if you want an AI-layered view of your email with Outlook or Gmail; dedicated email MCP servers offer more breadth if raw access and multi-provider coverage are priorities.

---

*This review is part of ChatForest's [MCP server directory](/reviews/). We research publicly available information — GitHub repos, documentation, registries, and community discussions. We do not test MCP servers hands-on. Corrections welcome.*

