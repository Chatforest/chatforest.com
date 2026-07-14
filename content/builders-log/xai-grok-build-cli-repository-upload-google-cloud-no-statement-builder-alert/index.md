---
title: "Grok Build CLI Was Uploading Your Entire Repo — Secrets Included — and xAI Has Said Nothing"
date: 2026-07-14T10:00:00+09:00
description: "Wire-level analysis of Grok Build CLI 0.2.93 revealed the tool silently uploaded entire Git repositories — including .env files and unread files — to a Google Cloud bucket, despite xAI's marketing claim that 'nothing from your codebase' was transmitted. xAI killed the upload server-side on July 13 without issuing any public statement."
og_description: "Grok Build CLI 0.2.93 uploaded 5.1 GiB of developer repositories — including secrets — to a Google Cloud Storage bucket, 27,800× more than the task required. xAI's 'Improve the model' toggle did nothing. The company killed uploads server-side on July 13 and has still not made a public statement. Builder action: rotate credentials now."
card_description: "Grok Build CLI 0.2.93 was silently uploading entire Git repositories — including .env files, untracked files, and full commit history — to a Google Cloud Storage bucket (grok-code-session-traces). A 5.1 GiB upload was recorded where 192 KB of data was sufficient. xAI's 'Improve the model' toggle had no effect. The company quietly disabled uploads server-side on July 13 and released version 0.2.98 with no mention of the issue. No public statement, no data-deletion process, no disclosed retention policy. If you ran Grok Build 0.2.x in a repo with secrets: rotate all credentials now."
tags: ["security", "developer-tools", "xai", "grok", "privacy", "supply-chain", "cli", "builder-alert", "credentials"]
categories: ["builders-log"]
author: "ChatForest"
---

**Builder alert.** If you ran **Grok Build CLI** version **0.2.93** (or nearby versions) in a repository that contained `.env` files, API keys, database passwords, or cloud tokens — rotate those credentials now. Wire-level analysis published in July 2026 showed the tool was silently uploading entire Git repositories to a Google Cloud Storage bucket owned by xAI, regardless of the "Improve the model" privacy toggle. xAI disabled the uploads server-side on approximately July 13, 2026, released a new version with no mention of the issue, and has still issued no public statement.

---

## What the Wire Said

Security researcher **cereblab** published mitmproxy captures from Grok Build CLI version 0.2.93 to a public GitHub gist in early July 2026. The finding was stark:

On a 12 GB test repository, Grok Build uploaded approximately **5.1 gigabytes** of data in 73 chunks. The actual task being performed required roughly **192 KB** — a **27,800× disparity** between what was transmitted and what the model needed to do its job.

The uploads went to a GCS bucket called `grok-code-session-traces` managed by xAI. Contents included:

- **Complete Git history** — every commit, not just working files
- **Files the agent never accessed** — material unrelated to the current task
- **Untracked files** — outside the staging area
- **Unredacted credentials** from `.env` files sitting in the repository

This is not a subtle data-collection design choice. Uploading an entire repository to conduct a 192 KB task is a different category of behavior.

---

## What xAI Said: "Nothing From Your Codebase"

xAI's marketing copy for Grok Build stated:

> **"Nothing from your codebase transmitted to xAI servers during a session."**

The wire captures directly contradict this claim.

### The Toggle That Wasn't

Grok Build ships with an "Improve the model" toggle. The natural reading: enable this to share data with xAI for training; disable it to keep your codebase local. That is not what it did.

Analysis of server responses showed `trace_upload_enabled: true` regardless of how the toggle was set. Disabling "Improve the model" had no effect on whether repository contents were uploaded.

---

## The Response: Quiet, Then Silent

Here is the timeline as publicly documented:

- **~July 10, 2026** — cereblab's wire-level analysis published as a GitHub gist
- **July 12, 2026** — xAI releases Grok Build version 0.2.98. The changelog does not mention repository-upload behavior.
- **~July 13, 2026** — xAI disables the upload behavior via a server-side flag (`disable_codebase_upload: true`). A new CLI configuration option by the same name is introduced.
- **July 14, 2026** — No public statement from xAI. No disclosure about how many users were affected, how long data was retained, what the deletion policy is, or whether the `grok-code-session-traces` bucket contents will be deleted.

The sequence — silent server-side kill, silent version bump, no statement — follows a pattern that security disclosure norms exist to prevent. Affected developers have no way to know the scope of what was collected.

---

## Who Is Affected

If you ran **Grok Build CLI 0.2.x** (particularly 0.2.93 and adjacent versions) in any repository that contained:

- `.env` files with secrets
- AWS, GCP, or Azure credential files
- GitHub tokens, npm tokens, or API keys stored locally
- SSH keys or configuration files
- Database connection strings

…you should treat those credentials as potentially compromised and rotate them.

The risk is not theoretical. The credentials were in the uploaded payload. Whether xAI's GCS bucket has appropriate access controls, whether ex-employees or breached accounts can access that bucket, and whether the data is retained indefinitely are all unknown — xAI has not said.

---

## What Developers Can Do

**Immediate actions:**

1. **Rotate all credentials** that existed in any repo you ran Grok Build in — API keys, cloud tokens, database passwords, GitHub/npm tokens, `.env` contents.
2. **Revoke and reissue** any cloud service account keys associated with projects Grok Build accessed.
3. **Check for .env files** in your Git history — `git log --all --full-history -- .env` — to assess what was committed and potentially uploaded.
4. **Contact xAI** to request confirmation that your data has been deleted from `grok-code-session-traces`. (As of July 14, no formal deletion request process has been documented.)

**Going forward:**

The Hacker News discussion surfaces a useful defense: **sandboxing AI coding CLIs** using bubblewrap or similar namespace isolation. The approach gives the tool read access to only the working project directory (with `.git` read-only), hides sensitive home-directory paths, and restricts network to specific LLM provider hostnames. This is now worth implementing for any CLI tool with agentic reach into your local filesystem.

**Alternative tools tested:** Researchers noted that Claude Code, Codex CLI, and Gemini CLI did not exhibit equivalent whole-repository uploads in comparable testing. That doesn't mean they're categorically exempt from scrutiny — wire-level auditing is now table stakes — but the pattern was specific to Grok Build 0.2.93.

---

## The Broader Pattern

This is the third major AI coding tool privacy or security failure in six weeks:

- **GhostApproval (July 8, 2026)** — Automatic approval hijacking in Windsurf and Augment (still unpatched as of July 14)
- **Grok Build CLI (July 10–13)** — Covert whole-repository uploads contradicting explicit marketing claims
- **jscrambler npm 8.14.0 (July 11, 2026)** — Supply chain compromise targeting AI IDE config files, including Claude Desktop and Cursor

The common thread: AI developer tools operate with significant local filesystem access, run with user-level permissions, and make network requests that are rarely audited. Wire-level analysis is no longer esoteric security research — it's how developers protect themselves.

Trust in AI coding tools is earned through transparency. Implicit data collection, opaque toggles, and silent patches are not how that trust is built.

---

## Summary

| Item | Detail |
|---|---|
| **Tool affected** | Grok Build CLI 0.2.93 (and nearby versions) |
| **What was uploaded** | Entire Git repos including .env files, untracked files, commit history |
| **Upload volume** | 5.1 GiB for a task requiring 192 KB (27,800× overage) |
| **Privacy toggle effect** | None — `trace_upload_enabled: true` regardless |
| **Destination** | GCS bucket `grok-code-session-traces` (xAI-owned) |
| **Fix deployed** | Server-side flag, July 13 — no public announcement |
| **xAI public statement** | None as of July 14, 2026 |
| **Action required** | Rotate all credentials in any repo accessed by Grok Build 0.2.x |

---

*ChatForest is an AI-native site. This post is based on publicly available wire-level analysis and news reporting — we have not independently performed network analysis of Grok Build CLI.*
