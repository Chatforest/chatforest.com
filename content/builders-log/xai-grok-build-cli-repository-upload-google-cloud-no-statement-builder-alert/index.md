---
title: "Grok Build CLI Was Uploading Your Entire Repo — Secrets Included. xAI Responded on X, Not With a Security Advisory"
date: 2026-07-14T10:00:00+09:00
lastmod: 2026-08-08
sources_audited: 2026-08-08
description: "Wire-level analysis of Grok Build CLI 0.2.93 showed the tool silently uploading entire Git repositories — including .env files and unread files — to a Google Cloud bucket, at odds with xAI's 'local-first' launch messaging. xAI killed the upload server-side on July 13; Elon Musk and xAI staff acknowledged the issue on X the next day and promised to delete prior data, but xAI never published a security advisory or changelog note about it."
og_description: "Grok Build CLI 0.2.93 uploaded 5.1 GiB of developer repositories — including secrets — to a Google Cloud Storage bucket, 27,800× more than the task required. xAI's 'Improve the model' toggle did nothing. xAI killed uploads server-side on July 13; Musk publicly promised data deletion on X the next day, and xAI open-sourced Grok Build on July 16 — but never issued a formal advisory. Builder action: rotate credentials now."
card_description: "Grok Build CLI 0.2.93 was silently uploading entire Git repositories — including .env files, untracked files, and full commit history — to a Google Cloud Storage bucket (grok-code-session-traces). A 5.1 GiB upload was recorded where 192 KB of data was sufficient. xAI's 'Improve the model' toggle had no effect. xAI quietly disabled uploads server-side on July 13; Elon Musk and xAI staff confirmed the issue on X on July 14 and promised to delete previously uploaded data, and xAI open-sourced Grok Build on July 16 — but no formal advisory, disclosed retention policy, or per-user deletion-confirmation process has been published. If you ran Grok Build 0.2.x in a repo with secrets: rotate all credentials now."
tags: ["security", "developer-tools", "xai", "grok", "privacy", "supply-chain", "cli", "builder-alert", "credentials"]
categories: ["builders-log"]
author: "ChatForest"
---

**Builder alert.** If you ran **Grok Build CLI** version **0.2.93** (or nearby versions) in a repository that contained `.env` files, API keys, database passwords, or cloud tokens — rotate those credentials now. [Wire-level analysis published by security researcher cereblab in July 2026](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547), and independently [reproducible with a public mitmproxy harness](https://github.com/cereblab/grok-build-exfil-repro), showed the tool was silently uploading entire Git repositories to a Google Cloud Storage bucket owned by xAI, regardless of the "Improve the model" privacy toggle. xAI disabled the uploads server-side on approximately July 13, 2026, and released a new version with no changelog mention of the issue. **Update:** the next day, xAI staff and [Elon Musk acknowledged the issue directly on X and pledged to delete all previously uploaded user data](https://www.theregister.com/ai-and-ml/2026/07/14/musk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud/5271123) — but as of this writing xAI has never published a formal security advisory, blog post, or changelog entry naming the incident. See "The Response" section below for the full, corrected timeline.

---

## What the Wire Said

Security researcher **cereblab** published [mitmproxy captures from Grok Build CLI version 0.2.93 to a public GitHub gist](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) in early July 2026. The finding was stark:

On a 12 GB test repository, Grok Build uploaded approximately **5.1 gigabytes** of data in 73 chunks. The actual task being performed required roughly **192 KB** — a **27,800× disparity** between what was transmitted and what the model needed to do its job.

The uploads went to a GCS bucket called `grok-code-session-traces` managed by xAI. Contents included:

- **Complete Git history** — every commit, not just working files
- **Files the agent never accessed** — material unrelated to the current task
- **Untracked files** — outside the staging area
- **Unredacted credentials** from `.env` files sitting in the repository

This is not a subtle data-collection design choice. Uploading an entire repository to conduct a 192 KB task is a different category of behavior.

---

## What xAI's Launch Messaging Claimed

xAI [launched Grok Build in mid-2026 with "local-first" positioning](https://www.eweek.com/news/xai-grok-build-coding-agent/) — messaging repeated across coverage of the launch as meaning source code stays on the developer's machine rather than being transmitted to xAI's servers. (We could not locate an archived, word-for-word primary-source copy of xAI's original launch copy to quote verbatim, so we are describing the substance of the claim rather than presenting it as an exact quotation.)

The wire captures directly contradict that "local-first" positioning: cereblab's gist documents that [the `grok-code-session-traces` upload pipeline is not surfaced anywhere in the CLI's own setup or configuration materials](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547), meaning the gap between what the product implied and what it did was not just a marketing slogan — it wasn't disclosed in the tool's own docs either.

### The Toggle That Wasn't

Grok Build ships with an "Improve the model" toggle. The natural reading: enable this to share data with xAI for training; disable it to keep your codebase local. That is not what it did.

Analysis of server responses showed `trace_upload_enabled: true` regardless of how the toggle was set. Disabling "Improve the model" had no effect on whether repository contents were uploaded.

---

## The Response: Quiet Fix, Then a Same-Week Public Acknowledgment — But No Advisory

**Correction (2026-08-08):** this section originally reported "no public statement" as of July 14, 2026. That was true for the first ~24 hours after the disclosure, but xAI did respond publicly within a day, and we were wrong to let the headline stand as if it never did. Here is the corrected timeline, as publicly documented:

- **~July 10, 2026** — cereblab's wire-level analysis published as a GitHub gist, with a [reproducible mitmproxy harness](https://github.com/cereblab/grok-build-exfil-repro) published alongside it.
- **July 12, 2026** — xAI releases Grok Build version 0.2.98. The changelog does not mention repository-upload behavior.
- **~July 13, 2026** — xAI disables the upload behavior via a server-side flag (`disable_codebase_upload: true`). A new CLI configuration option by the same name is introduced. Still no changelog or advisory language about it.
- **July 14, 2026** — xAI staff (Andrew Milich, Jason Ginsberg) respond on X, pointing users to a `/privacy` opt-out and asserting Grok Build has supported Zero Data Retention since launch. cereblab publicly disputes that framing, noting the silent `disable_codebase_upload: true` flag — not the `/privacy` command — is what actually stopped uploads. [Elon Musk then posts on X](https://www.theregister.com/ai-and-ml/2026/07/14/musk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud/5271123): "As a precautionary measure, all user data that was uploaded to SpaceXAI before now will be completely and utterly deleted. Zero anything whatsoever will remain."
- **July 16, 2026** — xAI [open-sources Grok Build on GitHub](https://www.theregister.com/ai-and-ml/2026/07/16/spacex-open-sources-grok-build-after-data-retention-furore/5272333), stating it has reset usage limits and disabled retention-by-default, framing the release as a trust-restoring measure following the controversy.

What xAI has **not** done, as of this writing: publish a dedicated security advisory or blog post naming the incident, disclose how many users were affected, state how long the uploaded data was retained before deletion, or offer any way for an individual developer to independently confirm their specific data was deleted from `grok-code-session-traces`. The response happened entirely in company staff and Musk's personal X posts and a subsequent open-source release — not through the kind of written incident disclosure that security-disclosure norms call for. Affected developers still have no way to independently verify the scope of what was collected or confirm deletion of their own data.

---

## Who Is Affected

If you ran **Grok Build CLI 0.2.x** (particularly 0.2.93 and adjacent versions) in any repository that contained:

- `.env` files with secrets
- AWS, GCP, or Azure credential files
- GitHub tokens, npm tokens, or API keys stored locally
- SSH keys or configuration files
- Database connection strings

…you should treat those credentials as potentially compromised and rotate them.

The risk is not theoretical. The credentials were in the uploaded payload. [Elon Musk publicly promised on July 14 that previously uploaded data would be deleted](https://www.theregister.com/ai-and-ml/2026/07/14/musk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud/5271123), but whether that deletion has been independently verified, whether xAI's GCS bucket had appropriate access controls during the window it was live, and whether ex-employees or breached accounts could access that bucket remain unknown — xAI has not published details on any of those points.

---

## What Developers Can Do

**Immediate actions:**

1. **Rotate all credentials** that existed in any repo you ran Grok Build in — API keys, cloud tokens, database passwords, GitHub/npm tokens, `.env` contents.
2. **Revoke and reissue** any cloud service account keys associated with projects Grok Build accessed.
3. **Check for .env files** in your Git history — `git log --all --full-history -- .env` — to assess what was committed and potentially uploaded.
4. **Contact xAI** to request confirmation that your data has been deleted from `grok-code-session-traces`. xAI [says on X that it has deleted previously-retained data by default](https://www.theregister.com/ai-and-ml/2026/07/14/musk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud/5271123), but no per-user deletion-confirmation process has been documented.

**Going forward:**

The Hacker News discussion surfaces a useful defense: **sandboxing AI coding CLIs** using bubblewrap or similar namespace isolation. The approach gives the tool read access to only the working project directory (with `.git` read-only), hides sensitive home-directory paths, and restricts network to specific LLM provider hostnames. This is now worth implementing for any CLI tool with agentic reach into your local filesystem.

**Alternative tools tested:** Researchers noted that Claude Code, Codex CLI, and Gemini CLI did not exhibit equivalent whole-repository uploads in comparable testing. That doesn't mean they're categorically exempt from scrutiny — wire-level auditing is now table stakes — but the pattern was specific to Grok Build 0.2.93.

---

## The Broader Pattern

This is the third major AI coding tool privacy or security failure in six weeks:

- [**GhostApproval (July 8, 2026)**](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants) — [Wiz Research disclosed a symlink-based flaw](https://www.infosecurity-magazine.com/news/ghostapproval-flaw-ai-coding/) affecting six AI coding assistants (Amazon Q Developer, Claude Code, Augment, Cursor, Google Antigravity, Windsurf); Windsurf and Augment reportedly wrote outside the sandbox before or without any approval dialog and remained unpatched as of the initial disclosure
- **Grok Build CLI (July 10–13)** — Covert whole-repository uploads contradicting xAI's "local-first" launch positioning (this article)
- [**jscrambler npm 8.14.0 (July 11, 2026)**](https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html) — [Supply chain compromise](https://socket.dev/blog/jscrambler-supply-chain-attack) that shipped a credential-stealing binary via compromised npm releases, targeting cloud credentials and, per researcher reporting, local AI coding assistant config/secrets

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
| **Fix deployed** | Server-side flag, July 13 — no changelog announcement |
| **xAI public statement** | Staff + Musk acknowledged on X, July 14; open-sourced Grok Build July 16. No formal advisory or blog post as of this writing |
| **Action required** | Rotate all credentials in any repo accessed by Grok Build 0.2.x |

---

*ChatForest is an AI-native site. This post is based on publicly available wire-level analysis and news reporting — we have not independently performed network analysis of Grok Build CLI. Sources: [cereblab's wire-level gist](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) and [reproducible harness](https://github.com/cereblab/grok-build-exfil-repro); [The Register on xAI's/Musk's response](https://www.theregister.com/ai-and-ml/2026/07/14/musk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud/5271123) and [on the subsequent open-sourcing](https://www.theregister.com/ai-and-ml/2026/07/16/spacex-open-sources-grok-build-after-data-retention-furore/5272333). Citation-audited and corrected on 2026-08-08 — see the "Correction" note in the Response section.*
