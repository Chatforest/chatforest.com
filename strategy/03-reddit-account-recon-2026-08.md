# Reddit Account Recon — 2026-08-06

*Research only, per CEO directive (inbox #2310, 2026-08-05). No posting, commenting, voting, or
following performed. All access below was read-only, unauthenticated (public RSS/HTML), from the
build server — no login attempted, no code from any peer agent executed.*

## 1. Account standing

**There is no "key" to test.** The only credential on file
(`~/.config/chatforest/ChatForest_password_on_reddit`) is a plaintext account password. Reddit's
API requires OAuth2 (a registered app's `client_id` + `client_secret`), which does not exist for
this account and can only be created by logging into reddit.com/prefs/apps in a real browser
session — something Grove cannot do (no browser, no login capability from this build server). So
"verify the key still authenticates" isn't answerable as asked; there is no API key, only a
password with nothing to present it to.

What I *could* check, unauthenticated:
- **Every JSON-shaped endpoint is hard-blocked.** `/user/ChatForest/about.json`,
  `/r/mcp/about/rules.json`, etc. all return HTTP 403 with an anti-bot challenge page, regardless
  of User-Agent. This is not specific to this account — it's Reddit blocking unauthenticated
  API-style access sitewide.
- **The HTML profile page is gated behind a JS proof-of-work challenge** (`js_challenge` form,
  solves via JS in a real browser) — can't be resolved without a browser engine, so no karma/
  cake-day/suspension data was retrievable that way either.
- **Public RSS feeds work** (no auth, no challenge) and are the only channel that returned real
  data: `https://www.reddit.com/user/ChatForest.rss` returned HTTP 200 with real entries. This
  confirms the account **exists, is not suspended, and is not banned** — a dead/suspended account's
  RSS returns empty/error, not live entries.

## 2. History — the account has posted before

`submitted.rss` returned 0 entries — **the account has never submitted a link or text post.**

The overview RSS (`user/ChatForest.rss`) surfaced **2 comments**, both found, neither previously
logged anywhere in WORKLOG/RUNLOG that I can find:

| Date (UTC) | Subreddit | Comment |
|---|---|---|
| 2026-03-13 23:00:04 | r/isthisAI | "I keep my glue bottles upside down so I don't have to wait for them each time." (reply on a post about an AI-generated dollhouse image) |
| 2026-06-14 19:52:53 | r/ClaudeAI | "Wow dedege. This is amazing. Thank you indeed for the idea, the website, the post. I'm digging it and digging in!" (reply on a post about Claude writing a book) |

**Flagging this, not accusing:** neither comment is promotional, on-brand, or related to
ChatForest content — they read as off-topic, personal-toned test replies, not marketing spam. But:
- The 2026-03-13 comment lands the day before the memory-recorded 2026-03-14 archive decision, so
  it may predate the "don't touch Reddit" policy and be harmless.
- The **2026-06-14 comment is ~3 months *after* the archive decision** and does not match anything
  in WORKLOG.md that I could find. This is either an out-of-policy action taken under a
  misconfigured or stale session, or activity from outside Grove's own runs. I can't determine
  which from here. **Recommend Rob/CEO look into how this comment was posted**, independent of
  the Reddit ROI question below — the content itself is harmless, but an unexplained post under
  the site's account, made against a standing "do not touch" directive, is a process gap worth
  closing regardless of what we decide about Reddit strategy.

No sign of over-posting, vote manipulation, or spam patterns — 2 comments in 5 months is not the
"scar tissue" that killed dev.to/Hashnode.

## 3. Subreddit rules inventory — could not get primary-sourced rule text

I was not able to pull verbatim rule text directly from Reddit for any subreddit. Every
`/about/rules.json`-style endpoint 403's (see §1), and the plain HTML page for r/mcp loaded but its
accessible sidebar fragment (unauthenticated old.reddit view) did not contain the moderator-set
rules widget — likely because full community rules only render for logged-in sessions in the
current Reddit frontend. This itself is a data point: **even simple, honest rule-checking requires
a login we don't have.**

What follows is from secondary aggregator sites (redship.io, launchwake.com, and similar
Reddit-strategy blogs) via search — **treat as unverified paraphrase, not quoted primary source**,
until someone with real Reddit login access confirms it directly:

| Subreddit | Self-promo | AI content | Bot accounts |
|---|---|---|---|
| r/mcp | Not independently confirmed — our March 2026 plan (`strategy/02-traffic-promotion-plan.md`) recorded "1:10 rule" from an earlier check, unverified today | Not confirmed | Not confirmed |
| r/LocalLLaMA | ~10% self-promo ceiling per aggregators; vendor/tool posts tolerated if framed as genuinely useful, not a pitch | Aggregators report "LLM-based bots / primarily LLM-generated content disallowed unless transparently used" | Implied disallowed per above |
| r/ClaudeAI | Not independently confirmed this run | Not confirmed | Not confirmed |
| r/artificial | General 90/10 rule cited (sitewide norm, not sub-specific) | Not confirmed | Not confirmed |
| r/selfhosted | One aggregator claims "promotion allowed when relevant" | Not confirmed | Not confirmed |

I'm not comfortable calling this an actual rules inventory — it's a set of secondhand claims I
could not verify against the primary source. If Reddit engagement is ever seriously considered,
someone with real browser/login access needs to pull the actual sidebar/wiki rules text for each
target sub before anything is posted.

## 4. Sitewide policy — the situation has gotten worse since March 2026, not better

- **Reddit's November 2025 "Responsible Builder Policy" closed self-service API registration.**
  Even the free, non-commercial API tier now requires manual pre-approval with a stated 2–4 week
  review timeline — this is new since the archive memory was written and materially raises the
  bar versus "just register an app."
- **Commercial API pricing is ~$0.24/1,000 calls, with a practical floor around $12,000/month**
  for a 50M-call contract (no smaller commercial plan). The archived-project memory recorded
  "$12K/year" — the real commercial floor is **$12K/*month***, an order of magnitude worse than
  what we had on file. ChatForest, as a site with monetization intent, would very plausibly need
  to register as commercial use, not the free personal/non-commercial tier — Reddit's own
  free-tier terms explicitly exclude commercial use.
- **Reddit began mandatory `[App]` labeling for automated/bot accounts starting 2026-03-31**, plus
  a new human-verification system triggered by suspicious account signals. Reddit CEO Steve
  Huffman: "Our aim is to confirm there is a person behind the account, not who that person is."
  (via TechCrunch, 2026-03-25 coverage of Reddit's announcement — I could not reach Reddit's own
  announcement page directly, blocked at the tool/network level same as the rest of reddit.com's
  domains.) This directly undercuts a "clearly-AI-labeled participation" strategy: an account that
  is both self-disclosed-AI *and* platform-labeled `[App]` gets double-flagged, which historically
  correlates with reduced organic reach and higher moderator scrutiny — the opposite of what we'd
  need for this to be worth the effort.

## 5. Recommendation: still a write-off, and more clearly so than in March 2026

Nothing found this run weakens the March 2026 decision — several things strengthen it:

- We have no functioning credential path to the API at all (no client_id/secret, no browser to
  create one), and even if we had one, non-commercial approval is now a discretionary 2-4 week
  review, and commercial pricing (the tier we'd likely actually need) starts at ~$12K/**month**,
  not the $12K/year on file.
- Reddit has gotten *more* bot-hostile since the archive decision (App-labels, human verification),
  not less — the platform is moving in the wrong direction for any bot-run account, however
  honestly disclosed.
- The account itself is clean (2 harmless comments, no spam pattern, not suspended) — so there's no
  reputational cleanup needed if we keep waiting. But one of those two comments is unexplained and
  postdates the "do not touch" directive; that's a process question for Rob/CEO, separate from
  the strategy question.

**My recommendation: no viable path today.** Keep the March 2027 revisit date. Before that
revisit, the two things that would actually change the calculus are (a) Reddit's Responsible
Builder Policy opening back up to easier non-commercial approval, or (b) ChatForest's
revenue/traffic reaching a point where a five-figure-per-month commercial API line item is
rational — neither is close. Recommend also asking Rob directly about the 2026-06-14 comment,
since I can't determine its origin from the build server.
