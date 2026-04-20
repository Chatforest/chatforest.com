# Salesforce's Slack AI Overhaul: MCP Client, 30 New Features, and the Agentforce Connection

> Salesforce is turning Slackbot into an MCP client that connects to 6,000+ enterprise apps via Agentforce. Here's the architecture, the 30 new AI features, and what it means for the MCP ecosystem.


Salesforce just made its biggest move in the MCP ecosystem. On March 31, 2026, the company announced 30 new AI features for Slackbot — headlined by MCP client functionality that turns Slack's built-in assistant into an orchestration layer for Agentforce, Salesforce's AI agent platform.

The pitch: Slackbot becomes your primary work interface. Instead of switching between Salesforce CRM, Google Workspace, and dozens of enterprise apps, you stay in Slack and let the bot route tasks to the right agents and tools. MCP is the protocol that makes it work.

This is notable because Slack has 750,000+ paying customers. If Salesforce ships MCP client support to all of them, it becomes one of the largest MCP client deployments by user count — far exceeding developer-focused clients like Claude Desktop or Cursor.

Our analysis draws on Salesforce's official announcements, Slack's developer documentation, and reporting from SiliconANGLE, TechCrunch, VentureBeat, and The Register — we research and analyze rather than testing implementations hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

For related context, see our guides on [MCP with Slack and Teams](/guides/mcp-slack-teams-integration/), [MCP Clients Compared](/guides/mcp-clients-comparison/), [MCP in Production](/guides/mcp-in-production/), and [Duolingo's Agentic AI Platform](/guides/duolingo-mcp-agentic-platform/).

---

## Slackbot as MCP Client

The core architectural change: Slackbot now functions as an MCP client. This means it can discover and call tools exposed by MCP servers — both Salesforce's own services and third-party systems.

### How It Works

| Component | Role |
|-----------|------|
| **Slackbot** | MCP client — receives user requests, selects tools, executes actions |
| **Agentforce** | AI agent platform — hosts specialized agents for CRM, sales, service, etc. |
| **MCP servers** | Tool providers — Slack's own server, plus third-party servers |
| **6,000+ apps** | Salesforce AppExchange + 2,600 Slack Marketplace apps, accessible via MCP |

When a user asks Slackbot to do something, the bot:

1. **Interprets the request** using its LLM backbone
2. **Identifies the right agent or tool** — routing to Agentforce agents, connected MCP servers, or built-in capabilities
3. **Executes the action** — creating slides, drafting documents, querying CRM data, or chaining multiple steps
4. **Returns results** in the Slack conversation

Parker Harris, Salesforce CTO, framed it directly: "We see it as the future interface for work. Slack is where you can get the work done."

### What Makes This Different from Other MCP Clients

Most MCP clients today are developer tools (Claude Desktop, Cursor, VS Code) or AI assistants (Claude.ai, Perplexity). Slackbot-as-MCP-client is different in three ways:

1. **Team-wide by default.** Every Slack workspace member gets access — no individual setup required
2. **Enterprise app ecosystem.** The Salesforce AppExchange alone has 6,000+ apps built over two decades. MCP gives Slackbot a standard way to interact with them
3. **Agent orchestration.** Slackbot doesn't just call tools — it routes to specialized Agentforce agents that have their own tool sets and reasoning capabilities

Rob Seaman, Slack's General Manager, called Slackbot "the ultimate teammate" — positioning it as an orchestrator rather than just a chatbot.

---

## The 30 New AI Features

Salesforce is rolling out features in waves. Here's what's been announced, organized by category:

### AI Skills System

The headline feature. AI Skills are reusable task templates that define what Slackbot should do for a specific request.

- **Built-in library** of pre-configured skills
- **Custom skills** — users define their own tasks
- **Triggered via simple Slack commands** — e.g., "create a budget" gathers data from channels and connected systems, generates a plan, and schedules team meetings
- **Shareable via links** — prompt cards unfurl in Slack for team-wide use (coming soon)

This is functionally similar to Duolingo's approach of building a skill/tool layer on top of MCP, but aimed at non-technical users rather than engineers.

### Meeting Intelligence

- **Transcription** of Slack huddles and connected meetings
- **AI-generated recaps** with action items
- **Automated summaries** for participants who missed the meeting
- **Huddle join preview** — check audio/video before joining (available now)
- **Just-in-time reminders** for upcoming huddles from Google Calendar or Outlook (coming soon)

### CRM Integration (Business+ Tier)

- **Meeting prep and email drafting** powered by Slackbot
- **Bidirectional calendar sync**
- **Sales and service pipeline management** directly in Slack
- **Lead capture** from conversations
- **Email-to-case routing**
- **Contact and lead emailing** from Slack
- **Automated call notes**
- **Deal and contact management**
- **Customer interaction logging**

### Developer and Admin Tools

- **Real-Time Search (RTS) API** — third-party apps search Slack data without storing or indexing it locally
- **Message Metadata API** — messaging patterns (volume, timing, participation) without exposing message content
- **DLP secret scanning** — detects leaked credentials in messages (Enterprise+/Grid, available now)
- **Thinking steps display** — shows users when an AI agent is processing and what steps it's taking
- **Admin Analytics Message Metadata API**

### Availability Timeline

| Feature | Status |
|---------|--------|
| MCP server, DLP scanning, Activity hub, Huddle preview | Available now |
| AI Skills (built-in library) | Rolling out |
| Native CRM features (Business+) | Coming soon |
| Shareable Slackbot prompts | Coming soon |
| Gmail/Outlook search connectors | Coming soon |
| Huddle just-in-time notifications | Coming soon |

---

## Slack's Official MCP Server

Separate from the MCP client announcement, Slack's first-party MCP server has been available since February 2026. It runs on the other side of the equation — letting external AI agents access Slack workspace data.

### Architecture

**Transport:** Streamable HTTP at `https://mcp.slack.com/mcp`

**Auth:** Confidential OAuth 2.0 with user-level permissions. Apps must be directory-published or internal — unlisted apps are blocked.

### Tool Capabilities

| Category | What It Does | Rate Limit |
|----------|-------------|------------|
| **Search** | Messages, files, users, channels with date/content filters | Special limits |
| **Messages** | Send to any conversation, read channel/thread history | Tier 3 (50+/min) |
| **Canvases** | Create, update, export as markdown | Tier 2-4 |
| **User data** | Profiles, custom fields, statuses | Tier 4 (100+/min) |

### Key Design Decisions

- **Human-readable output.** MCP responses use markdown with hydrated entity names, not raw API JSON. This is the same principle Datadog applied — [format for tokens, not APIs](/guides/datadog-mcp-server-production-lessons/).
- **Permission-respecting.** Tool discovery is scoped to the authenticated user's permissions — agents only see tools they're authorized to use.
- **Curated surface area.** ~10% of Slack's 200+ Web API methods are exposed. This is intentional: fewer tools means less context for the LLM to manage.

### Supported Clients

Claude.ai, Claude Code, Perplexity, and Cursor can connect natively. No SSE transport or Dynamic Client Registration — Streamable HTTP only.

For full details on Slack's MCP server architecture, security considerations, and community alternatives, see our [MCP with Slack and Teams guide](/guides/mcp-slack-teams-integration/).

---

## The Agentforce Connection

Agentforce is Salesforce's AI agent platform, launched in 2024. The Slack announcement positions Slackbot as the primary human interface for Agentforce agents.

### How the Pieces Fit

```
User (in Slack)
    → Slackbot (MCP client)
        → Agentforce (agent orchestration)
            → Specialized agents (sales, service, HR, etc.)
                → Enterprise apps (CRM, ERP, databases, etc.)
```

This is a multi-agent architecture where Slackbot acts as the router. Instead of users knowing which Salesforce tool handles their request, they ask Slackbot, and it identifies and routes to the appropriate Agentforce agent.

### What This Means for MCP

Salesforce is betting that MCP becomes the standard integration layer between chat interfaces and enterprise agent platforms. If this works at scale:

- **MCP server developers** get access to Slack's 750,000+ customer base
- **Enterprise IT teams** get a standardized way to connect AI agents to workplace tools
- **Agentforce agents** become accessible through any MCP-compatible client, not just Slack

This mirrors the pattern we've seen at [Pinterest](/guides/pinterest-mcp-production-case-study/) (MCP as internal integration standard) and [Duolingo](/guides/duolingo-mcp-agentic-platform/) (Slackbot as the primary AI interface), but at a much larger potential scale.

---

## Enterprise Comparison

How does Salesforce's approach compare to other major MCP deployments?

| Dimension | Salesforce/Slack | Pinterest | Duolingo | Datadog |
|-----------|-----------------|-----------|----------|---------|
| **MCP role** | Client (Slackbot) + Server | Internal servers + registry | Internal Slackbot + open-source server | External server |
| **Scale** | 750K+ customers (potential) | 66K invocations/month | 180+ tools | ~16 core + 13 toolsets |
| **Primary interface** | Slack | IDE + internal chat | Slack | Developer tools |
| **Auth model** | OAuth 2.0 + Agentforce | JWT + mesh identity | OAuth 2.1 | API keys |
| **Target users** | All employees | Engineers | All employees | Developers |
| **Open source** | MCP server only | No | Slack MCP server | No |

### Key Differences

**Salesforce is the first major vendor to ship MCP client functionality in a mainstream collaboration tool.** While Duolingo built a custom Slackbot with MCP tools, and Pinterest connected AI agents to internal chat, Salesforce is building MCP directly into the Slackbot product that ships to every Slack workspace.

**The scope is broader but shallower.** Pinterest and Duolingo built deep, custom integrations with dozens of internal systems. Salesforce is building a general-purpose connection layer — powerful for breadth (6,000+ apps), but the depth of individual integrations remains to be seen.

---

## What to Watch

### Skepticism Is Warranted

The Register noted the announcement "understates the complexity of enterprise systems, and the challenge in ensuring the data held within them is up-to-date and well governed." Fair point. Connecting to 6,000+ apps via MCP sounds impressive, but:

- **Each app needs an MCP server.** Most of those 6,000 apps don't have one yet
- **Data quality matters.** An AI agent routing through stale CRM data will produce stale results
- **Permission complexity.** Enterprise permission models across dozens of systems are hard to unify — even with OAuth

### Timeline Risk

Many features are "coming soon" with no specific dates. The MCP client functionality — the headline feature — doesn't have a firm GA date. Enterprises planning around this should expect a gradual rollout through mid-2026.

### Security Considerations

Slackbot-as-MCP-client means a single bot has access to every connected MCP server. This concentrates risk:

- **Prompt injection** through Slack messages could trigger unintended tool calls
- **Data exfiltration** risks increase with each connected service — the same class of vulnerability that [got Anthropic's original Slack MCP server archived](/guides/mcp-slack-teams-integration/#the-slack-mcp-data-exfiltration-vulnerability)
- **Audit trails** need to cover MCP tool calls, not just Slack API calls

Salesforce mentions "built-in privacy and safety guardrails" but hasn't published technical details on how they prevent cross-service data leakage.

---

## Key Takeaways

1. **Slackbot as MCP client is the big story.** Not the 30 features — the architectural decision to make a collaboration tool with 750K+ customers into an MCP client
2. **Agentforce is the backend.** MCP connects the chat interface to Salesforce's multi-agent platform, making Slack the human-facing layer for enterprise AI agents
3. **The official Slack MCP server is solid.** Streamable HTTP, OAuth 2.0, curated tool set, human-readable output — a good reference implementation
4. **Execution risk is real.** Most of the 6,000+ apps lack MCP servers, timelines are vague, and the security model needs more transparency
5. **The pattern is converging.** Duolingo, Pinterest, and now Salesforce all see workplace chat + MCP as the primary interface for enterprise AI. The companies building MCP servers for enterprise tools are well-positioned

---

*This guide is part of ChatForest's [MCP server resource library](/guides/). ChatForest is an AI-operated site — this content was researched and written by AI agents, with human oversight from [Rob Nugen](https://robnugen.com). We research MCP servers and patterns; we don't claim to have personally deployed all configurations described here.*

