# Claude Enterprise Gets Admin API and Self-Serve HIPAA: What Builders Need to Know

> Anthropic shipped two enterprise-grade features on July 14: a programmatic Admin API for automating member and group management, and a self-serve HIPAA enablement flow that replaces the sales/legal cycle. Here's what each unlocks for builders.


Anthropic released two enterprise features on July 14, 2026 that reduce operational friction for teams building on Claude at scale: a [User Management Admin API](https://platform.claude.com/docs/en/manage-claude/user-management) now in beta for all Claude Enterprise organizations, and a self-serve HIPAA configuration flow that eliminates the sales and legal cycle for eligible Enterprise admins.

Neither is glamorous. Both are the kind of plumbing that unlocks real workloads.

## Admin API Beta: Programmatic Member Management

The [Claude Enterprise Admin API](https://platform.claude.com/docs/en/manage-claude/user-management) gives platform and ops teams programmatic control over the people in their organization — replacing what was previously a manual, Console-only workflow.

**What you can do:**

- **List and look up members** — search by email address or enumerate all members
- **Change roles** — promote or demote members programmatically
- **Remove members** — offboard without touching the Console
- **Manage invites** — send and withdraw invitations via API
- **Manage groups** — create, update, and control group membership
- **Read custom roles** — inspect role definitions in your organization

**Access model:**

Most member and invite endpoints require no beta header — they're available today on any Admin API key.

Group and custom-role endpoints require the beta header:
```
anthropic-beta: ce-user-management-2026-07-13
```

For read-only queries across all user-management `GET` endpoints, an Admin API key with the `read:org_audit` scope is sufficient. You don't need write-capable credentials just to audit membership.

**Who this is for:**

- **IT/ops teams** provisioning seats for 50+ users: automate the member lifecycle instead of managing it through the Console
- **Platform teams** building internal tools on top of Claude Enterprise: sync your IdP or HRIS with Claude org membership
- **MSPs or consultancies** managing Claude orgs for clients: scriptable onboarding and offboarding

**What it replaces:**

The Console's admin panel still exists, but every action it supports for member management is now scriptable. Combined with [SCIM provisioning](https://platform.claude.com/docs/en/manage-claude/user-management) via Okta, Entra ID, or Google Workspace, this means you can treat Claude Enterprise membership as infrastructure — synced automatically rather than maintained manually.

Primary source: [Claude Platform release notes — July 14, 2026](https://platform.claude.com/docs/en/release-notes/api)

---

## HIPAA Self-Service: No Sales Cycle Required

Healthcare builders have long been able to run Claude under HIPAA — Anthropic has offered a Business Associate Agreement (BAA) since 2024. What changed on July 14 is how you get there: [eligible Enterprise admins can now enable HIPAA configuration](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans) through a self-serve flow, with a click-to-accept BAA, without involving a sales rep or legal team.

**Who qualifies:**

Only Claude Enterprise organizations (self-serve or sales-assisted) with a Primary Owner role can enable HIPAA through this flow. Team plans, Pro, Max, and Free plans cannot.

**How to enable:**

1. Sign in as Primary Owner
2. Go to **Organization Settings → Data and Privacy → HIPAA Compliance**
3. Download and review the BAA and Implementation Guide
4. Click **Accept and Enable HIPAA**

That's the entire process. No DocuSign, no back-and-forth, no waiting for a legal review to clear.

**What the BAA covers:**

The self-serve BAA covers:
- Messages API
- Prompt caching
- Structured outputs
- Memory
- Web search
- Bash and text-editor tools
- Token Counting, Models, Org Management, and Compliance APIs

**What it does NOT cover:**

- [Cowork](https://www.anthropic.com/product/enterprise) — explicitly excluded
- [Claude Code](https://claude.ai/code) — covered only with zero data retention (ZDR) enabled on a qualified account

**Critical caveat — this is a one-way decision:**

Once you enable HIPAA configuration and accept the BAA, the change cannot be reversed from admin settings. Enabling HIPAA also resets certain organization settings to their defaults. Test in a non-production org if you have one, or be sure before you click.

**Why this matters for health-tech builders:**

The previous path — wait for sales, negotiate a custom BAA, route through legal, get a signed agreement — added weeks to a project before you could even start processing PHI in a compliant environment. Self-serve HIPAA compresses that to an afternoon. For health-tech startups building on Claude Enterprise, faster BAA execution means faster time-to-production on anything touching protected health information.

---

## Putting Both Together

The two features compose well. A health-tech platform team can now:

1. Enable HIPAA in the afternoon (self-serve)
2. Automate member provisioning via the Admin API that same day
3. Sync Claude membership with their IdP automatically going forward

What was previously a multi-week enterprise procurement and onboarding project is now something closer to infrastructure configuration. The capability was always there — the friction wasn't.

If you're building on Claude Enterprise, check your [Admin API documentation](https://platform.claude.com/docs/en/manage-claude/user-management) and [HIPAA compliance settings](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans). Both are live today.

