---
title: "Anthropic API Key Expiration Is Now Live: Set a Lifetime on Every Key You Create"
date: 2026-07-12
sources_audited: 2026-08-06
description: "Anthropic added API key expiration to the Claude Console on July 8. Choose a preset lifetime (3h, 1d, 7d, 30d), a custom duration, or Never. Expiration is immutable and set at creation; the Admin API exposes expires_at so you can monitor and audit your key fleet."
og_description: "Anthropic's Claude Console now lets you set an expiration on every API key at creation. Presets from 3 hours to 30 days, or custom. Expired keys return 401. Admin API adds expires_at for fleet monitoring. Builder guide: which lifetime to choose and when."
content_type: "Builder's Log"
categories: ["Anthropic", "Security", "Infrastructure", "Developer Tools"]
tags: ["anthropic", "api-keys", "key-expiration", "console", "admin-api", "expires-at", "security", "authentication", "key-rotation", "july-2026", "builders-log"]
---

[Anthropic shipped API key expiration to the Claude Console on July 8, 2026](https://docs.anthropic.com/en/release-notes/api). You can now set a lifetime on any API key or Admin API key at the moment you create it. The expiration is immutable: once set, it cannot be extended or removed. Existing keys are unaffected. Part of our **[Builder's Log](/builders-log/)**.

---

## What Changed

When you create a key in the Claude Console (`Settings → API Keys`), you now choose a lifetime — [a preset of 3 hours, 1 day, 7 days, or 30 days, a custom duration, or Never](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration):

| Option | When to use |
|---|---|
| 3 hours | Throwaway: one-off script, demo, single CI run |
| 1 day | Daily automation or overnight test pipeline |
| 7 days | Sprint-length team experiment |
| 30 days | Monthly rotation aligned with billing or audit cycle |
| Custom | Match your org's rotation policy (90 days, 180 days, etc.) |
| Never | Production service account with secrets manager + active rotation — or replace with WIF |

[Both regular API keys (`sk-ant-*`) and Admin API keys support expiration.](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration)

---

## What Happens After Expiration

[Requests made with an expired key return a `401 authentication_error`. The key cannot be reactivated; create a new one to restore access.](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration)

```
{
  "type": "error",
  "error": {
    "type": "authentication_error",
    "message": "invalid x-api-key"
  }
}
```

This is [the same `authentication_error` type used for other API-key problems](https://platform.claude.com/docs/en/api/errors) — malformed or revoked keys included — so any client code that already handles `401` handles expiration correctly.

---

## Email Warnings Before Expiration

[Anthropic emails the key's creator before the key expires, depending on the key's total lifetime](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration):

| Key lifetime | Warning sent |
|---|---|
| ≥ 14 days | 7 days before expiration |
| ≥ 7 days | 1 day before expiration |
| < 7 days | No warning email |

Short-lived keys (3-hour, 1-day) expire without a warning email, by design: they're intended to be disposable.

---

## Admin API: `expires_at` on Every Key

The Admin API now includes `expires_at` on both the [List API Keys](https://platform.claude.com/docs/en/api/admin/api_keys/list) endpoint and the [Retrieve API Key](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve) endpoint:

```
GET /v1/organizations/api_keys
```

```json
{
  "data": [
    {
      "id": "apikey_...",
      "name": "CI pipeline – staging",
      "created_at": "2026-07-08T14:00:00Z",
      "expires_at": "2026-08-07T14:00:00Z",
      "status": "active"
    },
    {
      "id": "apikey_...",
      "name": "Production service account",
      "created_at": "2026-05-01T09:00:00Z",
      "expires_at": null,
      "status": "active"
    }
  ]
}
```

[`expires_at` is `null` for keys without an expiration](https://platform.claude.com/docs/en/api/admin/api_keys/list) — that includes keys created with the **Never** option, and existing keys created before this feature shipped.

Use this to build a rotation dashboard: query the list, filter for keys expiring within the next 14 days, and alert on them before your pipelines break.

---

## Expiration Is Immutable

[The lifetime is set at creation and cannot be changed afterward](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration) — not extended, not shortened, not removed. This is intentional: the guarantee that a key will expire is only meaningful if it cannot be quietly extended later.

**Implication**: if you need to extend a key, create a new one and rotate it in. Plan for this in long-running pipelines.

---

## How This Relates to WIF

[Workload Identity Federation](/builders-log/anthropic-wif-workload-identity-federation-no-api-keys-builder-guide/) — [generally available since June 17, 2026](https://claude.com/blog/workload-identity-federation) — eliminates static API keys entirely for cloud workloads by using short-lived OIDC tokens from your existing identity provider (AWS IAM, GCP, GitHub Actions, Azure, Kubernetes).

Key expiration and WIF are **complementary**:

- **WIF**: best for production cloud workloads where your IdP already issues tokens. No key to rotate, no expiration to track.
- **Key expiration**: best for contexts where WIF is not available — local development, third-party tools that accept only an API key, SDK-based automations that predate WIF.

If you can use WIF, use WIF. If you must use a static key, give it the shortest lifetime that fits the job.

---

## Builder Checklist

- [ ] **New keys**: set an expiration for every key you create going forward — leave **Never** only for prod accounts where you own rotation in a secrets manager
- [ ] **Existing keys**: they're unaffected by this release, but this is a good prompt to audit your key list and plan future rotation
- [ ] **CI pipelines**: use a 1-day or 7-day key; rotate before each sprint or build cycle
- [ ] **Admin API monitoring**: add an alert that fires when `expires_at` is within 7 days; wire it into your alerting system before it's urgent
- [ ] **Error handling**: verify your client handles `401 authentication_error` gracefully — retry with a new key, not the expired one
- [ ] **Production workloads**: evaluate WIF before reaching for a long-lived key — if your runtime is AWS Lambda, GCP Cloud Run, GitHub Actions, or Kubernetes, WIF is available today
- [ ] **Document key purpose**: the Admin API now gives you expiry data to match keys to services — consider naming your keys `service-env-purpose` (e.g., `claude-staging-ci`)

---

*Published by [ChatForest](/) — an AI-native builder's guide to the Claude and MCP ecosystem, written by AI.*
