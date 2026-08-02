---
title: "Gemini CLI Authentication & Data Handling — Beginner Guide (as of 01 Aug 2026)"
date: 2026-08-01
snapshot_date: 2026-08-01
topic: gemini-cli-authentication-and-data
track: beginner
audience: "people new to AI"
description: "A beginner-friendly walkthrough of Gemini CLI's login options (API key, Google sign-in, Vertex AI), how each one affects whether Google can use your data to train models, where your login credentials are stored on your computer, and how to keep them safe — including the June 2026 retirement of personal Google sign-in."
content_type: "Best Practice"
categories: ["Gemini CLI", "Security"]
tags: ["gemini-cli", "authentication", "data-privacy", "credentials", "vertex-ai", "google"]
last_refreshed: 2026-08-01
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-08-01"
grading_result: "0 fabrications after correction; 5 KILL + 10 FIX + 8 FLAG applied across the 3-draft Gemini CLI batch (this entry: 2 KILL, 5 FIX applied, 2 facts independently re-verified by sensei); 1 gap tracked as project-33 issue (mg_api unavailable this run — tracked in WORKLOG)"
---

<!-- This file lands at content/ai/<track>/<topic>/<snapshot-date>/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->


# Gemini CLI Authentication & Data Handling — Beginner Guide (as of 01 Aug 2026)

> **Grading note.** A dated snapshot — accurate as of **01 Aug 2026**, frozen here and kept as
> a permanent archive entry. This is the beginner-track version of an entry that was researched
> by a pupil and graded by the 3-lens panel + sensei; it has been re-leveled for readers who are
> new to AI tools, Ubuntu, and the command line. No new facts were added during re-leveling —
> see the CHANGELOG at the bottom.

**Prerequisite:** Gemini CLI is Google's free, open-source AI coding assistant that you run from a terminal (a text-only window where you type commands instead of clicking icons). You install it with the command `npm install -g @google/gemini-cli` — `npm` is a tool that comes bundled with Node.js and downloads and installs software packages like this one. This guide assumes Gemini CLI is already installed and walks you through picking a login method and keeping it safe.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Start with the simplest login method — a Gemini API key
**Do:** Gemini CLI supports three different ways to log in, but for someone new the simplest is a **Gemini API key** — a long text string you generate for free at Google AI Studio (a Google website). Once you have a key, tell your terminal about it with:
```
export GEMINI_API_KEY=your-key-here
```
(this exact command works on Linux/macOS; use the equivalent for your shell if you're on something else). This method needs no Google Cloud project and no billing account set up, and it has its own separate free and paid quota. The other two login methods exist for different situations, and this guide covers them further down: "Sign in with Google" (see the next practice — it mostly only works for company/school Google accounts now, not personal ones) and Vertex AI, Google Cloud's enterprise option, which needs a multi-step setup and is marked "advanced" below.
**Why (beginner):** These three login methods aren't interchangeable conveniences — each one comes with a different set of rules about what Google is allowed to do with the text you send it (see the data-handling practices below). Picking "whichever login is easiest" without checking is really picking "whose privacy terms I'm accepting" without reading them.
**Caveat / contested:** 🕒 verify live — daily/rate quotas per path change; the free API key tier was 250 requests/day, Flash-model-only, at time of writing (re-confirmed live 01 Aug 2026 against the vendor quota page). If Vertex AI setup is a multi-step Cloud Console/`gcloud` process, not a single command — it's aimed at companies and CI/CD pipelines, not casual personal use; see the advanced practice further down if you're curious.
**Sources:** [geminicli.com/docs/get-started/authentication](https://geminicli.com/docs/get-started/authentication/) (fetched 01 Aug 2026) · [geminicli.com/docs/resources/quota-and-pricing](https://geminicli.com/docs/resources/quota-and-pricing/) (fetched 01 Aug 2026)
**Confidence:** vendor-documented

---

## Practice: If a tutorial says to click "Login with Google," check that it still applies to you
**Do:** Many existing blog posts, videos, and even some cached docs still tell you to run `gemini` and click "Login with Google." As of **18 June 2026**, that no longer works for a free, Google AI Pro, or Google AI Ultra **personal** account in the open-source `gemini` CLI. Google announced the change on 19 May 2026 and gave a roughly 30-day migration window. It still works if you have a Workspace/company/school Google account, if your organization has a Gemini Code Assist Standard/Enterprise license, or if you're authenticating with a **paid** Gemini API key (see the practice above). Google's replacement for personal accounts is a separate, closed-source tool called **Antigravity CLI** — command `agy`, not the same program as `gemini-cli` — with its own login method (environment variable `ANTIGRAVITY_API_KEY`; as of this writing a maintainer has said a Gemini API key is not currently an alternative there) and its own usage limits. Any scripts, cron jobs, or CI pipelines that still rely on personal-account "Login with Google" will simply keep failing — there is no grace period.
**Why (beginner):** If you followed an older guide and "Login with Google" won't authenticate, you haven't done anything wrong — that path was retired out from under existing tutorials. Use the API key method from the practice above instead.
**Caveat / contested:** Access is **not** cut off for everyone: organizations with a Gemini Code Assist Standard/Enterprise license, Google Cloud/Vertex AI users, and anyone using a **paid** Gemini API key still get full `gemini-cli` access. 🕒 verify live — Google has not published an end date for that enterprise/API-key access window, so check current status before relying on it long-term. Re-checked live 01 Aug 2026: no reversal or extension found; the cutoff still stands.
**Sources:** [github.com/google-gemini/gemini-cli discussion #27274 (official Google announcement)](https://github.com/google-gemini/gemini-cli/discussions/27274) (19 May 2026) · [developers.googleblog.com — An important update: transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) (19 May 2026, primary source) · [inventivehq.com — Gemini CLI Is Being Retired on June 18](https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration) (13 Jun 2026) · [securityonline.info — Gemini CLI Deprecation](https://securityonline.info/gemini-cli-deprecation-antigravity-cli/) (22 Jun 2026) · [github.com/google-antigravity/antigravity-cli issue #78](https://github.com/google-antigravity/antigravity-cli/issues/78) (confirms `ANTIGRAVITY_API_KEY`, binary `agy`)
**Confidence:** independently-corroborated

---

## Practice: On the free tier, assume Google can use what you type to train its models
**Do:** Under Google's Gemini API Additional Terms of Service, **Unpaid Services** (Google AI Studio, and the free/unpaid quota of the Gemini API — what an un-billed personal API key or free Code Assist login uses) let Google "use the content you submit ... and any generated responses to provide, improve, and develop Google products and services and machine learning technologies," and "human reviewers may read, annotate, and process" your inputs/outputs (Google says it disconnects this from your account/API key/project first). The terms explicitly instruct: don't submit sensitive, confidential, or personal information to Unpaid Services. Once you turn on a Cloud Billing account, **all** use of the Gemini API and AI Studio becomes a "Paid Service" for data-handling purposes — even calls that don't cost money — and Google states "Google doesn't use your prompts or responses to improve our products," with prompts/responses logged only temporarily for abuse detection/legal compliance.
**Why (beginner):** If you're thinking about pasting real client code, a private repository, or anything you're not allowed to share (like something under an NDA) into `gemini-cli`, check this first: are you on a billing-enabled (paid) project, or the free quota? On the free tier, what you type could end up training Google's models and could be read by a human reviewer. The free path is fine for learning and public/toy code — it is not designed for confidential work.
**Caveat / contested:** If you're in the **European Economic Area, Switzerland, or the UK**, Google applies the paid-tier ("no training") data terms to *all* services, including the free/unpaid tier, as a regional commitment — so the free-tier training risk described above mainly applies outside those regions. Also note: enabling billing is what flips the switch, not simply "having a paid subscription" — see the next practice for a documented gap around Google AI Pro/Ultra personal subscriptions specifically.
**Sources:** [ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms) (last updated 28 Apr 2026, re-confirmed unchanged 01 Aug 2026)
**Confidence:** vendor-documented

---

## Practice: Paying for a Google AI Pro/Ultra subscription is not the same as paying for the API, and it doesn't guarantee "no training"
**Do:** Google's Gemini API FAQ says paid usage isn't used for training. But Gemini CLI's own official comparison table, which maps each login method to a privacy policy, lists a **Google AI Pro/Ultra personal account** (used via "Login with Google" for Gemini Code Assist) under Google's general **Privacy Policy** — not under the Gemini API's "Paid Services" no-training rule. Someone raised this exact contradiction with the `gemini-cli` maintainers on GitHub, asking Google to confirm that paid Pro/Ultra subscribers get the same protection as paid API users. Google closed the request **"not planned"** without publishing a clarifying statement. Until Google says otherwise, treat "I pay for AI Pro/Ultra, so my code isn't used for training" as **unconfirmed**, not confirmed.
**Why (beginner):** It's a very reasonable, common assumption — "I pay for it, so it must be private" — and Google's own marketing FAQ reads that way. But the CLI team's own reference table doesn't back that up for personal Pro/Ultra subscriptions, and Google chose not to resolve the ambiguity when directly asked. If keeping your code private really matters to you, use a billing-enabled API key or Vertex AI instead (see the advanced practices below), where the "no training" language unambiguously applies.
**Caveat / contested:** This is somewhat overtaken by the June 2026 retirement of personal OAuth login in the open-source `gemini-cli` (see the practice above) — the ambiguity still matters for the Gemini Code Assist IDE extensions / Antigravity and other Google AI products tied to the same Pro/Ultra account, just not for the `gemini-cli` program itself going forward. 🕒 verify live — Antigravity is a newer, evolving product and its own privacy-policy mapping could not be independently confirmed as of this snapshot (searched 01 Aug 2026, no primary source found addressing it specifically); this is a genuine open gap, not a guess.
**Sources:** [github.com/google-gemini/gemini-cli issue #20569](https://github.com/google-gemini/gemini-cli/issues/20569) (closed, not planned) · [github.com/google-gemini/gemini-cli — docs/resources/tos-privacy.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/resources/tos-privacy.md) (official terms/privacy matrix, fetched 01 Aug 2026)
**Confidence:** contested (Google's Gemini API FAQ language vs. the `gemini-cli` team's own ToS/privacy matrix and their refusal to reconcile the two)

---

## Practice: Advanced option — Vertex AI (skip this unless your organization needs it)
**Do:** Vertex AI is Google Cloud's enterprise login option for Gemini CLI, and setting it up is a genuine multi-step process, not one command: install the `gcloud` CLI, run `gcloud auth application-default login`, create or select a Google Cloud project, turn on billing and the Vertex AI API for that project, give your account or service account the `Vertex AI User` IAM role, then set the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` environment variables. See [Google's Vertex AI quickstart](https://docs.cloud.google.com/vertex-ai/docs/start) if you want to go this route. This is overkill for casual/personal use — it exists for CI/CD pipelines and enterprise deployments where a company wants centralized billing and access control.
**Why (beginner):** You do not need this to try Gemini CLI. If you're an individual learning or experimenting, the API key from the first practice above is enough — come back to this only if a company or organization requires it.
**Caveat / contested:** 🕒 verify live — daily/rate quotas per path change; check the current vendor quota page before relying on any specific number.
**Sources:** [geminicli.com/docs/get-started/authentication](https://geminicli.com/docs/get-started/authentication/) (fetched 01 Aug 2026) · [geminicli.com/docs/resources/quota-and-pricing](https://geminicli.com/docs/resources/quota-and-pricing/) (fetched 01 Aug 2026)
**Confidence:** vendor-documented

---

## Practice: Advanced/enterprise option — Zero Data Retention (ZDR), only if you have a specific compliance need
**Do:** These are advanced/enterprise-tier options — skip this practice if you're on the free or personal-paid tier and don't have a specific compliance requirement. On the paid Gemini Developer API, you can request **Zero Data Retention (ZDR)** approval for a specific Cloud project. Once approved, prompts/responses and identifiable metadata (IP address, Google Account ID) are stripped before any logging happens, instead of being retained in identifiable form for the standard abuse-monitoring window. On Google Cloud / Vertex AI, Google's Gemini-for-Google-Cloud data-governance page states plainly: "Gemini doesn't use your prompts or its responses as data to train its models," backed by Google Cloud's published AI/ML Privacy Commitment not to train foundation models on customer data without permission.
**Why (beginner):** If you're evaluating Gemini CLI for real work at a company, Vertex AI + ZDR (or a billing-enabled API key + ZDR) is the combination with the clearest paper trail — useful when you need to answer a security questionnaire, not just a blog post's opinion. Most individual, learning-focused users will never need this.
**Caveat / contested:** ZDR has real exceptions: it does **not** cover Grounding with Google Search or Maps (30-day retention), the Interactions API (must separately opt out with `store: false`), or the Live API (unless session resumption is left unconfigured) — and you must also avoid explicit context caching and manage file deletion yourself for a genuinely zero footprint. 🕒 verify live — ZDR is an approval-gated feature; confirm current eligibility before relying on it.
**Sources:** [ai.google.dev/gemini-api/docs/zdr](https://ai.google.dev/gemini-api/docs/zdr) (fetched 01 Aug 2026) · [docs.cloud.google.com/gemini/docs/discover/data-governance](https://docs.cloud.google.com/gemini/docs/discover/data-governance) (last updated 17 Jul 2026)
**Confidence:** vendor-documented

---

## Practice: Know where Gemini CLI stores your login info on disk, and lock those files down yourself
**Do:** Gemini CLI's Google sign-in session is cached in a file at `~/.gemini/oauth_creds.json`; API keys are commonly saved in `~/.gemini/.env` (or a project-local `.env`) or in shell profile exports; Vertex AI service-account and Application Default Credentials are plain JSON files (exact path varies by OS, set via `GOOGLE_APPLICATION_CREDENTIALS`). None of these are protected by your operating system's built-in password vault (a "keychain") by default on Linux — they are readable, plain JSON/text files. A previously-filed bug (issue #6170, opened 13 Aug 2025) noted that Google's fix to set `oauth_creds.json` to owner-only permissions (`600`) on creation didn't retroactively fix files created *before* the patch; that gap was itself closed by a merged fix (PR #6662, merged 29 Aug 2025) that added an explicit `chmod` step so existing files get corrected too. As a costless defense-in-depth habit regardless, you can always run `chmod 600 ~/.gemini/oauth_creds.json` (and any `.env` file with keys in it) yourself after any upgrade — this command tells Linux "only the file's owner may read or write this file." Separately, a feature request to add Linux keyring (Secrets API / GNOME Keyring / KWallet) support for API keys was closed **"not planned."**
**Why (beginner):** Don't assume "logged in" means "protected like a password manager entry." Anyone else with read access to your home directory — a shared machine, a misconfigured container, malware that steals files — can potentially open these files directly and read your login token or key, no password needed. Running `chmod 600 ~/.gemini/oauth_creds.json` costs nothing and removes any doubt about your current file's permissions.
**Caveat / contested:** Independent researchers (Netwrix) surveying 14 AI coding tools found this plaintext-credential pattern is common industry-wide, not unique to Gemini CLI — but they specifically flagged Gemini's Application Default Credentials files as unencrypted JSON across Linux, macOS, and Windows.
**Sources:** [github.com/google-gemini/gemini-cli issue #6170](https://github.com/google-gemini/gemini-cli/issues/6170) (opened 13 Aug 2025, closed) · [github.com/google-gemini/gemini-cli PR #6662](https://github.com/google-gemini/gemini-cli/pull/6662) (merged 29 Aug 2025, verified fetched 01 Aug 2026 — adds explicit `chmod` for pre-existing files) · [github.com/google-gemini/gemini-cli issue #10232](https://github.com/google-gemini/gemini-cli/issues/10232) (closed, not planned) · [netwrix.com — AI coding assistants are leaking credentials](https://netwrix.com/en/resources/blog/ai-coding-assistant-credential-storage-risks/) (12 May 2026)
**Confidence:** independently-corroborated

---

## Practice: Treat your Gemini API key like a password — know how to turn it off if it leaks
**Do:** Google's own docs explicitly warn: "Treat API keys ... as sensitive credentials. Protect them to prevent unauthorized access and potential misuse of the service under your account," and similarly for Vertex AI service-account key files ("provides access to your resources"). Inside `gemini-cli`, the interactive `/auth` slash command (typed while `gemini` is running) opens a dialog to change your authentication method. If you set up the advanced Vertex AI path above with a **personal user account**, run `gcloud auth revoke user@example.com` (Google Cloud SDK) to invalidate that token both locally and on Google's servers — but note this does **not** apply to service-account or external-account credentials: per Google's own docs, those tokens "are not revocable" via this command, so a compromised service-account key must instead be disabled/deleted at its source (IAM). For an API key, rotate/delete it from Google AI Studio rather than just removing it from your shell — the key itself stays valid until revoked at the source.
**Why (beginner):** An API key or token left in a `.env` file, a shell history, or a leaked screenshot keeps working for anyone who has it, until *you* revoke it — deleting the local file alone does not disable the credential on Google's servers. And "I ran `gcloud auth revoke`" doesn't help much if the credential was actually a service account key, which that command can't revoke.
**Caveat / contested:** Also avoid exporting keys via `~/.bashrc`/`~/.zshrc`/`$PROFILE` for convenience — Google's own docs note this makes the key readable to any process spawned from that shell, which is a broader exposure surface than a `.env` file scoped to one directory.
**Sources:** [geminicli.com/docs/reference/commands/](https://geminicli.com/docs/reference/commands/) (`/auth` command, fetched 01 Aug 2026) · [google-gemini.github.io/gemini-cli/docs/get-started/authentication](https://google-gemini.github.io/gemini-cli/docs/get-started/authentication.html) (fetched 01 Aug 2026) · [docs.cloud.google.com/sdk/gcloud/reference/auth/revoke](https://docs.cloud.google.com/sdk/gcloud/reference/auth/revoke) (Google Cloud SDK reference, fetched 01 Aug 2026 — confirms service/external-account tokens "are not revocable")
**Confidence:** vendor-documented

---

## Practice: ⚠️ Never run Gemini CLI in auto-approve ("YOLO") mode against a repo or issue tracker you don't control
**Do:** Two separately discovered, now-patched security bugs show what goes wrong when Gemini CLI is given broad trust: (1) **Pillar Security** (reported 16 Apr 2026, advisory GHSA-wpqr-6v78-jr5g published 24 Apr 2026, writeup published 5 May 2026, rated CVSS 4.0 10.0 — the maximum possible score — by Google, or 7.8 by NIST on a different scale) found that a Gemini-powered GitHub issue-triage bot running in `--yolo` (auto-approval) mode could be hijacked by a hidden instruction planted inside a public GitHub issue. This let an attacker steal the CI pipeline's secrets and Git tokens that had already been written to disk by `actions/checkout` — even after the workflow's `GITHUB_TOKEN` environment variable was unset, because the token file on disk itself wasn't protected. Patched in v0.39.1 / v0.40.0-preview.3. (2) **Tracebit** (discovered 27 Jun 2025, published 28 Jul 2025) found that simply asking Gemini CLI to analyze an untrusted local repository — no special flags needed — could trigger silent execution of a shell command disguised as an already-whitelisted `grep`, exfiltrating all of the user's environment variables (potentially including API keys/secrets) to a remote server, with no visible warning. Patched in v0.1.14.
**Why (beginner):** These weren't hypothetical — both were real, working exploits against the default or auto-approve configuration, targeting exactly the credentials this guide is about (API keys, Git tokens, environment variables). Never point Gemini CLI's auto-approve/`--yolo` mode at a repository or issue tracker you don't control, and keep the CLI updated — both bugs are fixed in current releases, but a similar type of attack (called "prompt injection," where hidden text tricks the AI into doing something it shouldn't) could happen again in a different form.
**Caveat / contested:** Both were responsibly disclosed and patched before public write-ups; there is no evidence either was exploited in the wild against real users before the fix shipped. Confirm you're on a version at or after the patched releases above. Note these are two independently-discovered, single-sourced incidents (Pillar found the CI/CD one; Tracebit found the grep-whitelist one) — each is individually well-documented, but the two sources don't corroborate each other's specific finding, so treat this as two solid single-source reports rather than one doubly-corroborated claim.
**Sources:** [pillar.security — My Agentic Trust Issues](https://www.pillar.security/blog/my-agentic-trust-issues-from-prompt-injection-to-supply-chain-compromise-on-gemini-cli) (5 May 2026) · [tracebit.com — Code Execution Through Deception](https://tracebit.com/blog/code-exec-deception-gemini-ai-cli-hijack) (28 Jul 2025)
**Confidence:** thin <!-- two individually solid but each single-sourced findings, not mutually corroborating -->

---

## Held pending fixes (not publish-ready)
- Exact current daily/rate quotas for each tier (Code Assist personal 1,000–2,000/day; API free 250/day Flash-only; Vertex Express Mode 90-day trial) are cited from a single vendor page and change often — flagged 🕒 verify live throughout rather than held, but a future refresh should re-check numbers directly rather than trust this snapshot.
- Whether Gemini CLI's Google sign-in flow also uses your operating system's built-in password vault (macOS Keychain / Windows Credential Manager), and not just the plain-text `~/.gemini/oauth_creds.json` file described above, could not be confirmed from an official, directly-fetched source this run — search-engine summaries suggested this happens on some platforms, but no fetched primary source confirmed it, so it was deliberately left out rather than guessed. ⚠ #TBD (project-33 issue to be filed once mg_api access is confirmed)
- Antigravity CLI's own privacy-policy mapping for Pro/Ultra personal accounts is unresolved — no primary source found as of this snapshot. ⚠ #TBD

## CHANGELOG (grading → this entry)
1. **Re-leveled** from the 2026-08-01 technical (best-practices) entry for readers new to AI, Ubuntu, and the command line. No new facts, claims, or sources were added or removed — all `**Sources:**` links, `**Confidence:**` labels, and the ⚠️ WARNING are reused verbatim from the technical entry.
2. **Reordered** to lead with the single simplest login path (a free Gemini API key + `export GEMINI_API_KEY=...`) instead of presenting all three auth methods side by side. "Sign in with Google" retirement details and Vertex AI/Zero Data Retention setup are now explicitly labeled "advanced" and moved later in the document, with a "skip this unless you need it" framing kept intact from the source entry.
3. **Simplified language** throughout (e.g. explained `npm`, `chmod 600`, "prompt injection," and "keychain" in plain words on first use) and strengthened each "Why (beginner)" with the concrete, plain-language failure it prevents (e.g. "anyone else with read access to your computer could open this file and read your login token").
4. Verified the technical entry's post-grading fixes were carried through unchanged: the working `export GEMINI_API_KEY=your-key-here` command, the explicit Vertex AI setup step list, the full `gcloud auth revoke user@example.com` syntax, and the "advanced/enterprise, skip if you're on the free tier" framing on the Zero Data Retention practice.
