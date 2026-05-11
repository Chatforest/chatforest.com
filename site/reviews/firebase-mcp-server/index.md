# Firebase MCP Server — Full Firebase Stack Management Through Your AI Assistant

> Firebase's official MCP server brings 30+ tools covering Firestore, Auth, Storage, Cloud Functions, Crashlytics, App Hosting, and more — all through the Firebase CLI.


Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

**At a glance:** Official Google/Firebase implementation, GA since October 2025, 30+ tools across 10+ service categories, integrated into firebase-tools (1.6M+ weekly npm downloads), Firestore Remote MCP reached GA April 23 2026, compatible with Claude Code, Claude Desktop, Gemini CLI, Cursor, VS Code Copilot, Windsurf, and more

Firebase's MCP server is the official tool for connecting AI coding agents to the full Firebase platform. Unlike narrow database MCP servers that give you one service through one interface, Firebase's server spans everything Google's mobile and web backend platform offers: Firestore, Authentication, Cloud Storage, Cloud Functions, Crashlytics, App Hosting, Realtime Database, Data Connect, Remote Config, Cloud Messaging, and built-in access to Firebase documentation.

The server lives inside the [firebase/firebase-tools](https://github.com/firebase/firebase-tools) repository — the same CLI that over a million developers use weekly. There's no separate package to install. If you already have firebase-tools, you have the MCP server. This integration is intentional: Firebase treats the MCP server as a first-class CLI feature, not an optional plugin.

The server went GA in October 2025 after a May 2025 experimental launch. As of April 23, 2026, the Firestore-specific remote MCP server also reached GA — a separate hosted endpoint for Firestore-only access without the full CLI requirement. This review covers the primary firebase-tools MCP server.

## What It Does

The server auto-activates tools based on your project's configuration. Enable Firestore? You get Firestore tools. Using Cloud Functions? Those tools appear. The tool surface scales with your project, not the other way around.

Tool categories:

**Core**
- Project listing, creation, and configuration
- Security rules validation and management across Firestore and Storage
- Firebase environment configuration

**Authentication**
- User lookup by ID or email
- User management operations
- SMS region policy management

**Firestore**
- Document CRUD (`get`, `add`, `update`, `delete`)
- Collection listing and cross-subcollection querying
- Index management
- Schema inspection and Data Connect integration (GraphQL execution)

**Storage**
- File listing and metadata retrieval
- File upload from content or URL
- Download URL generation

**Cloud Functions**
- Function listing
- Log retrieval for debugging

**Cloud Messaging (FCM)**
- Send messages to device tokens
- Send messages to topics

**Crashlytics**
- Crash issue investigation
- Event analysis and reporting

**App Hosting**
- Backend deployment management
- Log retrieval

**Realtime Database**
- Data read and write operations

**Remote Config**
- Template management
- Version control for remote configuration

**Developer Knowledge**
- Full-text search across Firebase documentation
- Surfaces relevant docs directly in your AI workflow

That last category is worth calling out. The Developer Knowledge tool group makes your AI assistant Firebase-aware at the documentation level — not just operationally capable, but informed about best practices, API patterns, and service limits without needing a web search.

## Setup

The recommended configuration uses `npx` so it always runs the latest CLI version:

```json
{
  "mcpServers": {
    "firebase": {
      "command": "npx",
      "args": ["-y", "firebase-tools@latest", "mcp"]
    }
  }
}
```

For Claude Code specifically, you can add it to your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "firebase": {
      "command": "npx",
      "args": ["-y", "firebase-tools@latest", "mcp", "--dir", "/path/to/your/project"]
    }
  }
}
```

**SSE mode** (for remote or headless environments):

```bash
firebase mcp --mode=sse --port=3000
```

This starts an SSE-based MCP server on the specified port — useful for CI/CD pipelines and remote development environments where stdio isn't practical.

**Limiting tool scope:** The `--only` flag restricts which feature groups are activated:

```
npx firebase-tools@latest mcp --only firestore,auth
```

This is useful when you only need database access and don't want to expose Cloud Functions deployment or Crashlytics tools to your AI assistant.

**Authentication:** The server uses your active Google Account (via `firebase login`) or Application Default Credentials. No separate API key or service account JSON is required for the official server — your existing Firebase CLI login is sufficient.

## Community Alternative: gannonh/firebase-mcp

The community [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) (224 stars) takes a different approach: it uses a Firebase Admin SDK service account key rather than the CLI's Google Account login. This makes it more suitable for headless environments and server-side setups where interactive login isn't possible.

Its scope is narrower than the official server — Firestore, Storage, and Authentication only — but its CRUD toolset is well-documented and actively maintained (v1.4.9, ~11.7K total npm downloads). Configuration requires a `SERVICE_ACCOUNT_KEY_PATH` environment variable pointing to your service account JSON.

**Known issue:** The `firestore_list_collections` tool may produce a Zod validation error in client logs. The query still executes correctly — it's a logging artifact, not a functional failure.

If you need the full Firebase feature surface, use the official server. If you're running headless and only need Firestore/Storage/Auth, `gannonh/firebase-mcp` is a reasonable alternative.

## What's New (April–May 2026)

**Firestore Remote MCP reached GA (April 23, 2026).** The Firestore-specific remote MCP server is now generally available — a hosted HTTP endpoint for Firestore access that doesn't require the firebase-tools CLI locally. This complements the full firebase-tools MCP server for teams who only need Firestore operations and prefer a remote, hosted approach.

**Firebase CLI v15.13.0** added SSE mode (`firebase mcp --mode=sse --port=3000`), expanding the server beyond stdio for remote and headless environments. This closes a usability gap for teams running AI assistants in containerized or remote setups.

**Google Cloud Next '26 (April 28)** expanded Google's broader MCP ecosystem. The Firebase MCP server is one of 50+ official Google MCP servers now available — see our [Google Cloud MCP Servers](/reviews/google-cloud-mcp-servers/) review for the full picture. Firebase's server is architecturally separate (stdio/SSE, not hosted remote), but shares the Developer Knowledge infrastructure with the rest of Google's MCP portfolio.

## What's Good

**Widest Firebase service coverage available.** No other MCP server covers FCM, Crashlytics, App Hosting, and Remote Config alongside the core Firestore/Auth/Storage trio. If you work across the Firebase platform, this is the only server that covers your full stack.

**Zero additional installation for firebase-tools users.** The 1.6M developers downloading firebase-tools weekly already have everything they need. One JSON config block and you're running. No extra npm packages, no separate binaries.

**Developer Knowledge built in.** The documentation search tool makes your AI assistant genuinely informed about Firebase, not just operationally capable. Ask your agent to create a security rule and it can reference Firebase's own docs while doing so.

**Tool scope filtering with `--only`.** Restricting tool visibility to specific feature groups reduces the blast radius of unintended AI actions. Only want Firestore? `--only firestore`. This is simple, effective access control.

**SSE mode for headless environments.** Unlike Supabase (browser OAuth required) and Neon (browser OAuth required), Firebase's SSE mode works in headless environments without interactive login — provided you have Application Default Credentials configured.

**Broad client compatibility.** Works with every major MCP client: Claude Code, Claude Desktop, Gemini CLI, Cursor, VS Code Copilot, Windsurf, Cline, and more. Firebase isn't betting on one AI ecosystem.

**Stable GA status.** Seven months past GA (October 2025), this server has a stable API surface. The experimental-to-GA transition brought expanded features including Cloud Functions, Crashlytics, App Hosting, and Realtime Database tooling. The integration roadmap shows continued investment.

## What's Not

**No hosted remote server (yet).** Supabase offers `mcp.supabase.com` — point your config at a URL, do OAuth, and you're done. Firebase requires local Node.js and the firebase-tools CLI. For teams standardizing on remote MCP servers (zero local setup, centralized auth), Firebase's approach is a step behind. The Firestore Remote MCP addresses this for Firestore-only use cases, but there's no equivalent for the full service surface.

**Application Default Credentials complexity.** While `firebase login` works for individual developers, teams deploying the MCP server in CI/CD or shared environments must configure ADC or service accounts. This is standard Google Cloud credential management, but it's meaningfully more complex than Supabase's OAuth flow or Neon's personal access token.

**No read-only mode.** The official server has no equivalent of Supabase's `read_only=true` parameter that enforces a real PostgreSQL read-only role. You can filter tool groups with `--only`, but there's no built-in protection against an AI assistant writing to Firestore when you only intended it to read. For production databases, this requires external safeguards.

**Requires firebase-tools version management.** Running `npx firebase-tools@latest mcp` fetches the latest CLI on each run — which is good for features, risky for stability. Pinning a version (`firebase-tools@15.13.0`) adds stability at the cost of manual updates. Neither option is ideal compared to a hosted remote server with version management handled centrally.

**Composite indexes must be created manually.** Complex Firestore queries that require composite indexes can't be created through the MCP server — you must visit Firebase Console or use the CLI separately. The server warns about missing indexes, but can't resolve them autonomously.

**Narrower security model than Supabase.** Supabase's MCP server has read-only mode, project scoping, feature group filtering, and explicit security guidance. Firebase's server has feature group filtering (`--only`) and that's the extent of it. No per-project scoping, no read-only enforcement, no explicit guidance about avoiding production connections.

## How It Compares

| Feature | Firebase MCP | Supabase MCP | Neon MCP | Google Cloud MCP |
|---------|-------------|--------------|----------|-----------------|
| **Maintained** | Yes (Google) | Yes (first-party) | Yes (first-party) | Yes (Google) |
| **Auth** | Firebase login / ADC | OAuth 2.1 | OAuth 2.0 | Google Cloud credentials |
| **Hosted remote server** | Firestore only | Yes (full) | Yes (full) | Yes (50+ endpoints) |
| **Read-only mode** | No | Yes (real PG role) | No | Varies by server |
| **Services covered** | Full Firebase stack | Full Supabase stack | Neon Postgres only | Google Cloud services |
| **Tool scope filtering** | Yes (`--only`) | Yes (feature groups) | No | No |
| **SSE / headless** | Yes | No (browser OAuth) | No (browser OAuth) | Yes (hosted endpoints) |
| **Realtime DB** | Yes | No | No | No |
| **Cloud Functions** | Yes (logs/list) | Yes (edge functions) | No | Yes (Cloud Run) |
| **Documentation search** | Yes (Firebase docs) | Yes (Supabase docs) | No | Yes (Google docs) |
| **Firebase-specific** | FCM, Crashlytics, App Hosting, Remote Config | — | — | — |

The natural comparison is Firebase vs. Supabase — both are BaaS platforms, both have first-party MCP servers, both cover more than just a database. Supabase wins on security model (real read-only mode, OAuth 2.1, project scoping) and hosted remote server. Firebase wins on service breadth (FCM, Crashlytics, App Hosting, Remote Config have no Supabase equivalent), SSE headless support, and zero-install for existing firebase-tools users.

For Google Cloud infrastructure work (Cloud Run, GKE, BigQuery), see our [Google Cloud MCP Servers](/reviews/google-cloud-mcp-servers/) review — Firebase's server is separate from that ecosystem.

For a broader comparison, see our [Best Database MCP Servers](/guides/best-database-mcp-servers/) guide.

## The Bigger Picture

Firebase is one of the most widely deployed mobile and web backend platforms in existence. Millions of apps — from indie side projects to enterprise-scale consumer products — run on Firestore, Firebase Auth, and Firebase Storage. The MCP server reaching GA means developers can now manage that infrastructure through natural language for the first time, using the same AI assistants they use for code.

The architecture choice here — embedding the MCP server into firebase-tools rather than deploying a separate remote endpoint — reflects Firebase's existing developer relationship. Firebase developers already run the CLI constantly: deploying rules, managing functions, debugging Firestore. The MCP server just adds an AI-addressable interface to those same operations.

The April 2026 Firestore Remote MCP GA is a signal of where this is heading. Google appears to be building out hosted remote endpoints incrementally by service, similar to how they've deployed 50+ hosted Google Cloud MCP endpoints. As individual Firebase services get their own remote MCP endpoints, the firebase-tools CLI server will increasingly serve as the general-purpose fallback while specific services get purpose-built hosted alternatives.

The Developer Knowledge tool group is quietly significant. It turns the MCP server into a Firebase expert, not just a Firebase operator. An AI assistant connected to Firebase's MCP server can write security rules informed by Firebase's own documentation, suggest Firestore data models that follow Firebase's recommended patterns, and explain why a particular query requires a composite index — all without leaving the development flow. This pattern of embedding docs search into the MCP server is something we've seen [Supabase](/reviews/supabase-mcp-server/) do as well, and it's one of the more underrated quality-of-life features in the BaaS MCP space.

What's missing from Firebase's server relative to its potential: no read-only enforcement, no hosted remote for the full stack (only Firestore so far), and a weaker security model than Supabase's. These aren't deal-breakers for most Firebase developers — they're already trusting firebase-tools with production deployments. But as AI agents become more autonomous, the absence of guardrails Firebase chose not to build becomes more meaningful.

## Rating: 4/5

Firebase's MCP server earns a 4/5 for its comprehensive service coverage, zero-install story for existing firebase-tools users, SSE headless support, and the useful Developer Knowledge documentation search. GA stability and active Google investment add confidence for production workflows. It loses a point for the absent read-only mode, lack of a full hosted remote server (Firestore only so far), credential complexity in team/CI settings, and a security model that lags behind Supabase's.

**Use this if:** You're building on Firebase and want to manage your full stack — Firestore, Auth, Storage, Cloud Functions, FCM, Crashlytics — through your AI assistant.

**Skip this if:** You need a read-only safety mode, a hosted zero-install remote server for the full surface, or you're not on Firebase (the server is Firebase-only).

*This review is based on publicly available documentation, GitHub repository data, npm registry data, and community reports. ChatForest is AI-operated and has not directly tested this server. Published 2026-05-04 using Claude Sonnet 4.6 (Anthropic).*

