# Duplicate Page Clusters — Tracking

> Per CEO directive (inbox #2296, 2026-07-31): flagged-but-unresolved near-duplicate clusters
> discovered during citation-audit runs live here instead of being buried in WORKLOG prose.
> Pattern: max ONE verified diff-and-merge per run (diff fully, decide merge vs. keep-both,
> retire the weaker page with an `aliases` redirect if merging) — flag the rest and move on.
> Check this file each run before starting new audit work; resolve one cluster if time allows.

## Framework change (CEO ruling, inbox #2379, 2026-08-20)

**The pre-collapse "keep both, different angles" precedents documented below no longer bind.**
Post-June-2026-spam-update, the presumption for same-topic siblings is **MERGE**; keep-both now
requires genuinely different **topics** (like the Bedrock-deployment page in the Sonnet-5 cluster),
not merely different angles on the same topic. Two templated pages competing for one search query is
precisely the scaled-content-abuse shape that got the site classified. Applies to all remaining open
clusters and any newly flagged ones going forward.

## Open clusters

### MCP Auth guides (2 pages) — carried in WORKLOG since before 2026-08-01, migrated here 2026-08-15
Not yet diffed in full; flagged repeatedly in WORKLOG "what's next" notes without a resolution pass.
- `content/guides/mcp-authentication-oauth.md`
- `content/guides/mcp-authorization-oauth.md`

### MCP Error Handling guides (2 pages) — carried in WORKLOG since before 2026-08-01, migrated here 2026-08-15
Not yet diffed in full; flagged repeatedly in WORKLOG "what's next" notes without a resolution pass.
- `content/guides/mcp-error-handling-resilience.md`
- `content/guides/mcp-error-handling-explained.md`

## Resolved clusters

### Insurance / InsurTech (2 pages) — resolved 2026-08-21
Flagged 2026-08-15 by two independent audit agents during early-vintage-audit batch 13 (each auditing
one file, blind to the other) — both independently reported the pages look like near-duplicates. Per
CEO ruling #2379: **MERGE** — same rating (3.5/5), same publish date (2026-03-15), overlapping core
servers (Socotra, Sure, EIOPA/Ansvar compliance tooling).

- `content/reviews/insurance-mcp-servers.md` — 74 impr/90d. **Survivor.**
- `content/reviews/insurance-insurtech-mcp-servers.md` — 17 impr/90d. **Merged into survivor, then
  deleted.**

Diffed both files in full. The InsurTech-angle page had five genuinely additive items the survivor
lacked entirely — pulled in and re-verified live 2026-08-21 rather than trusted from either page's
2026-08-15 audit:
- **Root Platform MCP (official, Root Insurance)** — the survivor never mentioned Root at all, despite
  it being a publicly-traded InsurTech's official npm-distributed server. Re-verified current npm
  version live: still **v1.7.1** (published April 21, 2026, unchanged since the last audit).
- **Fenris MCP Server** — commercial insurance data-intelligence layer, absent from the survivor.
  Re-verified the March 11, 2026 launch date and the "tens of millions of insurance transactions
  annually" figure directly against Fenris's press release (einpresswire.com), not just the marketing
  page, which doesn't state a launch date on its own.
- **mcp-lemonade** — a Lemonade insurance connector, absent from the survivor. Re-verified live via
  GitHub API: 0 stars, not archived.
- **Unstract MCP** — commercial ACORD-form document-processing server, absent from the survivor. This
  also required updating the survivor's "What's Missing" section, which had claimed no ACORD
  extraction existed at all — corrected to reflect Unstract handles document-level extraction (while
  still correctly noting no server implements ACORD *messaging* standards for system-to-system
  exchange).
- **ComplianceCow/cow-mcp** — GRC automation server, absent from the survivor. Re-verified live via
  GitHub API: 12 stars, 19 forks, 361 commits (last push 2026-08-20).
- Also pulled a specific, re-verified detail into the survivor's existing Apify underwriting entry:
  the 8 underlying data-source actors are a mix of US and UK government feeds (FEMA/USGS/NOAA vs. UK
  Environment Agency/Police/Land Registry), confirmed live against the Apify listing — a materially
  useful detail (US-only underwriters get partial coverage from the UK-sourced categories) that the
  survivor's generic bullet list didn't convey.
- Did **not** pull Ansvar-Systems/US_Compliance_MCP — both pages agree this repo no longer exists
  (confirmed dead in the InsurTech page's own 2026-08-15 audit), so there was nothing live to add.
- Updated front matter (title, description, og_description, card_description), the "landscape divides
  into X areas" and headline-findings intro paragraphs, "What's Missing," and "The Bottom Line" to
  reflect the merged content. Added an `aliases` redirect to the retired page's URL.
- Repointed 3 other live pages that linked the retired URL or carried a stale rating/version:
  `content/guides/best-mcp-servers.md` (2 spots — one updated to 3.5/5 with current Root/Fenris/Socotra
  key servers, the duplicate "Insurance / InsurTech" row removed entirely rather than repointed, since
  it was a straight duplicate of the "Insurance" row once both point at one survivor),
  `content/categories/finance-fintech/index.md` (collapsed two rows into one, 3.5/5),
  `content/reviews/automotive-vehicle-mcp-servers.md` (1 spot).
- `hugo --minify --cleanDestinationDir --quiet` clean; confirmed the alias redirect (200) and survivor
  (200, correct 3.5/5 rating) in the built site before deploying.

### New Relic MCP Server (2 pages, no hyphen vs hyphenated) — resolved 2026-08-21
Flagged 2026-08-18 by the early-vintage re-audit agent (noticed a second, distinct live file on the
same product under a different slug). CEO ruling (#2379, 2026-08-20): **MERGE**, second item in the
ordered queue after package-management.
- `content/reviews/newrelic-mcp-server.md` (no hyphen) — 816 impr/90d vs 133. **Survivor.**
  `sources_audited`/`last_refreshed` bumped to 2026-08-21. Added `aliases` redirect to the retired
  page's URL.
- `content/reviews/new-relic-mcp-server.md` (hyphenated) — audited 2026-08-18, rated 3.0/5 after a
  downgrade for the same unresolved OAuth/SSO bug this merge confirms is still open. **Merged into
  survivor, then deleted.**

Diffed both files in full. The two pages disagreed on basic facts — tool count (survivor's body said
35, the retired page said 30+, the survivor's own title said 27), GitHub stars (survivor's "What's
Not" section said 5 vs 7 everywhere else on the same page), and rating (4/5 vs 3.0/5) — so rather than
trust either page's numbers, re-verified everything live 2026-08-21:
- **Tool count: 27**, confirmed by parsing the raw HTML of the live
  [tool reference](https://docs.newrelic.com/docs/agentic-ai/mcp/tool-reference/) (not just an AI
  summary of it) for every `<code>` tool-name element. Rewrote the survivor's tool tables to match —
  dropped two tools neither current (`list_entity_types`, `query_logs`), renamed
  `get_entity_error_groups` to the live name `list_entity_error_groups`, and added a genuinely new
  tool neither review had documented (`list_entity_performance_risk_groups`).
- **GitHub repo stats re-verified via API**: 7 stars, 0 forks, 2 commits, 4 open issues (2026-08-21).
  Pulled full issue history including two the survivor never mentioned: Issue #6 (self-hosted/Helm
  request, open) and **Issue #7** (filed May 27, 2026) — a **second, distinct OAuth bug** (flow
  completes but never redirects back for custom connectors), still open. Combined with Issue #4
  (OAuth fails completely for SSO-enforced orgs, filed April 8, 2026, still open >4 months later —
  confirmed via the GitHub API today, no new comments since June 21), that's two independently-filed
  open OAuth bugs, not one.
- **Rating changed from 4/5 to 3.5/5** on the survivor (not the retired page's 3.0/5 — the free-tier
  and ecosystem-integration strengths are real and independently verified, but two confirmed-open
  OAuth bugs are a real regression from the original 4/5 call).
- **FedRAMP/HIPAA claim corrected**: the survivor quoted New Relic's docs as prohibiting "FedRAMP or
  HIPAA compliance mandates" as if verbatim. Re-fetched the live source — only FedRAMP is stated;
  no HIPAA-specific wording exists on any New Relic-owned page. Corrected in three spots (What's Not,
  Who Should Use This, verdict) to state FedRAMP as confirmed and HIPAA as unconfirmed, matching the
  more careful phrasing the retired page already had.
- **Pulled from the retired page**: company background (founding 2008, 2023 $6.5B take-private,
  headcount estimates, CTO appointment, IDC MarketScape Leader placement) — the survivor had none of
  this. Also pulled cloudbring/newrelic-mcp's community-alternative star count, re-verified live at
  14 stars / 8 forks / 58 commits (survivor had 11/7/57, all stale).
- Repointed 4 other live pages that cited the survivor's old 4/5 or 4.5/5 rating and 35-tool count:
  `content/guides/best-observability-mcp-servers.md` (2 spots), `content/guides/best-mcp-servers.md`
  (2 spots), `content/reviews/pagerduty-mcp-server.md`, `content/reviews/honeycomb-mcp-server.md`,
  `content/reviews/datadog-mcp-server.md`, `content/reviews/monitoring-observability-mcp-servers.md`
  (2 spots, comparison table + prose).
- Fixed `content/categories/observability-monitoring/index.md`'s comparison table, which had been
  carrying **both** pages as separate rows ("New Relic" and "New Relic NRQL & Alerts") since before
  this cluster was even flagged — collapsed to one row, corrected "five vendors" to "four" in the
  section intro to match.
- `hugo --minify --cleanDestinationDir --quiet` clean; confirmed the alias redirect (200 via
  meta-refresh) and survivor (200, correct 3.5/5 rating) in the built site before deploying.

### Package Management MCP Servers (2 pages) — resolved 2026-08-20
Flagged 2026-08-17 by the early-vintage re-audit agent. CEO ruling (#2379, 2026-08-20): **MERGE**
under the new framework above — survivor chosen by traffic + depth (382 impr/90d vs 198).
- `content/reviews/package-management-mcp-servers.md` — dated 2026-03-24. **Survivor.**
  `sources_audited` bumped to 2026-08-20 for this merge; `last_refreshed` bumped to match. Added an
  `aliases` redirect to the retired page's URL (CEO-authorized exception to the no-mass-redirects
  rule — this is a genuine merge, not a bulk prune).
- `content/reviews/package-management-dependency-mcp-servers.md` — dated 2026-03-17, audited
  2026-08-17 (manifest row 847 of `prune-wave1-manifest.csv`). **Merged into survivor, then deleted.**

Diffed both files in full. Pulled and re-verified (fresh star counts + primary-source checks against
live GitHub API / Microsoft Learn, 2026-08-20 — all matched the retired page's 2026-08-17 audit
exactly, no drift found):
- **WinGet MCP Server (official, Microsoft)** — the survivor had zero mention of it. Added its own
  section (search/install/upgrade-detection via `find-winget-packages?upgradeable=true`, introduced
  WinGet 1.29.240), re-verified live against
  [learn.microsoft.com/.../mcp-server-overview](https://learn.microsoft.com/en-us/windows/package-manager/winget/mcp-server-overview)
  and [microsoft/winget-cli#6259](https://github.com/microsoft/winget-cli/discussions/6259).
- **sammcj/mcp-devtools** — the survivor named mcp-package-version's archival but never named its
  actual successor. Added a dedicated section (158 stars, verified live via GitHub API 2026-08-20,
  already surpassing mcp-package-version's peak 122 stars); corrected the survivor's "Known Issues"
  #1 and "Bottom Line" text, which had said the archived server had "no clear successor."
- **MShekow/package-version-check-mcp** (7 stars) and **Tripletex/mcp-dependency-version** (4 stars,
  OSV-database vulnerability scanning across 12 registries) — added as the vulnerability-scanning
  angle the survivor was missing; both star counts re-verified live, matched exactly.
- Did **not** pull Artmann/package-registry-mcp or niradler/dependency-mcp — both already present in
  the survivor's "Multi-Registry and Other Servers" section at comparable or greater detail than the
  retired page had; re-adding would have been redundant, not additive.
- Updated the survivor's front-matter (title/description/og_description/card_description), "Known
  Issues" #1, "Notable Gaps" (closed-gaps list + "still missing" line, which had wrongly implied
  winget lacked any MCP server), the "Developer Tools MCP Comparison" table's package-row cell, and
  the "Bottom Line" section to reflect all of the above.
- Repointed internal links in 3 other live pages that linked the retired URL with a stale 3.5/5 rating
  (`content/reviews/logging-tracing-mcp-servers.md`, `content/reviews/api-development-mcp-servers.md`,
  `content/guides/best-mcp-servers.md` — 2 rows) and `content/categories/developer-tools/index.md`, all
  now pointing at the survivor's URL with the correct 3/5 rating.
- Retired page's title/H1 framing (25+ servers, "official vendor servers" section) was otherwise a
  near-total content overlap with the survivor once the above was pulled — nothing else worth saving.

**Net effect:** wave-1 prune manifest closes at true 907/907 (this deletion was the held row 847).

### Sonnet 5 launch / agentic upgrade (5 pages) — resolved 2026-08-08
Flagged Run 3611486 (2026-07-31) as an open cluster; the earlier "both kept, both cited" note on
`claude-sonnet-5-launch-agentic-*` was a quick triage, not a full diff — re-examined this run with a
full read of all 5 candidate pages plus the exact merge precedent (commit `a7299d1171`).

- `content/builders-log/anthropic-claude-sonnet-5-agentic-builder-migration-guide/index.md` — dated
  2026-06-30. **Survivor.** Already the survivor of one prior merge; sources_audited bumped to
  2026-08-08 for this second merge pass.
- `content/builders-log/claude-sonnet-5-launch-agentic-upgrade-migration-guide-builder-decision/index.md`
  — dated 2026-07-01. **Merged into survivor, then deleted.** Same three breaking changes (identical
  code samples), same tokenizer framing, same cybersecurity-refusal section, same migration checklist,
  same availability section as the survivor — genuinely redundant prose, not just a similar title.
  Pulled in and re-verified: the "When to Use Sonnet 5 vs. Opus 4.8" decision-framework section
  (synthesizes facts already cited on the survivor, no new sourcing needed) and the TechCrunch
  Zapier-engineer (Daniel Shepard) anecdote quote, re-verified live against
  https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/.
  Nothing cut — both pulled claims checked out. Alias added on survivor; directory deleted; 6 internal
  links across 5 sibling pages repointed to the survivor's URL.
- `content/builders-log/claude-sonnet-5-1m-context-adaptive-thinking-migration-builder-guide/index.md`
  — dated 2026-07-01. **Merged into survivor, then deleted.** Same redundant structure as above. Pulled
  in and re-verified two claims not on the survivor: the June 2, 2026 billing change (no charge for a
  refusal with zero generated output — confirmed verbatim in Anthropic's release notes at
  https://platform.claude.com/docs/en/release-notes/overview) and Anthropic's own recommendation to use
  Opus 4.8 for cybersecurity work needing reduced guardrails (verbatim quote confirmed live against
  https://www.anthropic.com/news/claude-sonnet-5). Cut a tangential "1M context since Sonnet 4.6,
  March 13, 2026" historical aside as low-value padding rather than force it in. Alias added on
  survivor; directory deleted.
- `content/builders-log/claude-sonnet-5-adaptive-thinking-new-tokenizer-migration-builder-guide/index.md`
  — dated 2026-07-07, already audited (sources_audited: 2026-08-04, including a real fabrication fix
  that run). **Kept separate — no merge.** Has a genuinely distinct "Benchmark Surprise" section
  (explicit Sonnet-5-vs-Opus-4.8 Terminal-Bench/OSWorld comparison numbers not spelled out on the
  survivor, with a different editorial thesis: Sonnet 5 outright *beats* Opus 4.8 on agentic terminal
  work rather than merely narrowing the gap) plus a corrected, more precise `output_config.effort`
  top-level-field code sample the other pages don't have. Consistent with the SnapLogic/H1-2026-VC
  counter-precedent: real distinct content, not just a similar title.
- `content/builders-log/claude-sonnet-5-bedrock-deployment-always-on-thinking-inference-paths-builder-guide/index.md`
  — dated 2026-07-01, already audited (sources_audited: 2026-07-31). **Kept separate — no merge.**
  Entirely different subject matter (Bedrock-specific deployment: 5 model IDs/residency profiles,
  3 API paths, prompt-caching parameter changes, service tiers, computer-use setup) and already
  explicitly cross-links to the survivor as the API-level companion piece. Not a duplicate by any
  reading.

Also out of scope, not opened this run per the task brief (distinct angles: pricing deadline, effort
tuning, GPT-5.6 comparison): `claude-sonnet-5-august-31-pricing-cliff-tokenizer-compound-budget-action-guide`,
`claude-sonnet-5-effort-levels-thinking-token-overhead-practical-tuning-guide`,
`claude-sonnet-5-migration-guide-adaptive-thinking-tokenizer-breaking-changes-builder-guide`,
`claude-sonnet-5-vs-gpt-56-terra-benchmark-cost-context-window-builder-decision-july-2026`.

### Kimi K3 launch cluster (3 pages) — resolved 2026-08-08
Flagged for review this run (not previously tracked in this file). Same July 16, 2026 Moonshot AI
Kimi K3 launch, all three already independently sources_audited: 2026-08-08.
- `content/builders-log/kimi-k3-2-8t-open-moe-frontier-mcp-atlas-builder-guide/index.md` — MCP-Atlas-
  centric builder guide: architecture (KDA/AttnRes/Stable LatentMoE), MCP Atlas category breakdown,
  access paths, a "Builder Decision Matrix," and an "End of Cheap Chinese AI" pricing-inflection angle.
- `content/builders-log/kimi-k3-moonshot-ai-2-8t-moe-open-weights-builder-guide/index.md` — broader
  benchmark/open-weights builder guide with substantial content absent from the sibling above: the
  **K3 Swarm Max** variant (an entirely different product SKU), the **Arena Frontend Code #1 ranking**
  beating Claude Fable 5 (a significant fact the MCP-Atlas guide never mentions), a Terminal-Bench 2.1
  score, GDPval-AA Elo trend vs. K2.6, and a launch-promotion bonus-credits detail.
- `content/reviews/moonshot-kimi-k3-2-8t-open-weight-china-frontier-ai-july-2026.md` — a genuinely
  different format (rated review, not a builder guide) with an entirely different subject focus:
  US-China chip-sanctions policy, the Trump administration's revived ban push, a David Sacks quote,
  and the Nvidia/Z.ai/MiniMax stock-market reaction — none of which appears in either builders-log
  piece.

**Decision: keep all three, no merge.** Same underlying launch event and some overlapping core specs
(2.8T params, KDA/AttnRes, 1M context, $3/$15 pricing), but each carries a full section's worth of
content the other two lack — consistent with the SnapLogic/H1-2026-VC/Claude-Apps-Gateway
counter-precedent, not the Sonnet-5-launch-day merge precedent.

### Claude Apps Gateway (3 pages) — resolved 2026-08-06
Flagged Run 3611486 (2026-07-31), never diffed until this run. Note: the file's own bookkeeping was
stale — the note that the `bedrock-google-cloud-sso-spend-caps` page was "not yet audited" was wrong;
git history (`fb1ebc435f`) shows it was already audited 2026-08-04, before this run started. Also, the
directory name for the "self-hosted" page differs from what earlier notes here recorded: it's
`content/builders-log/claude-apps-gateway-self-hosted-sso-bedrock-google-foundry-enterprise-builder-guide/index.md`,
not `.../claude-apps-gateway-self-hosted/index.md`.
- `content/builders-log/claude-apps-gateway-self-hosted-sso-bedrock-google-foundry-enterprise-builder-guide/index.md` — dated 2026-07-01, audited (sources_audited: 2026-07-31). **Technical implementation guide**: prerequisites table, full `gateway.yaml` example, MDM push config, a Docker Compose quickstart, and an "enforced vs. not enforced" limitations table.
- `content/builders-log/claude-apps-gateway-enterprise-bedrock-google-cloud-microsoft-foundry-builder-guide/index.md` — dated 2026-07-03, audited (sources_audited: 2026-08-01). **News-cycle/context piece**: bundles the gateway with the same-week Microsoft Foundry GA of Claude Sonnet 5 on Azure, and ties spend caps to the broader Tesla/Uber/Walmart/Meta/Amazon enterprise-AI-budget story (cross-links the sibling Tesla $200/week article).
- `content/builders-log/claude-apps-gateway-bedrock-google-cloud-sso-spend-caps-enterprise-builder-guide/index.md` — dated 2026-07-07, audited (sources_audited: 2026-08-04). **Overview + protocol-interoperability piece**: covers the published wire protocol, third-party gateway compliance (LiteLLM/TrueFoundry), and an operational "gotchas" list (spend-cap timing, IdP downtime, policy-poll delay).

Diffed all three in full. Same underlying June 29, 2026 Anthropic announcement and much of the same
core factual surface (stateless container + Postgres, OIDC/SSO, spend caps, data residency), but three
genuinely different angles at three different depths published on three different days in the week
after launch — consistent with the SnapLogic/H1-2026-VC/LongCat precedents above. Spot-checked the
protocol-interoperability page's unique "Open Protocol" section against the live
`code.claude.com/docs/en/llm-gateway-protocol` and `claude-apps-gateway-deploy` docs during this run;
citations hold up. **Decision: keep all three, no merge.**

### SK Hynix Nasdaq ADR: $29B filing vs $28B/$26.5B debut (2 pages) — resolved 2026-08-05
Flagged during citation audit of the 2026-07-10 `skhy-nasdaq-debut` page (this run, 2026-08-05).
- `content/builders-log/sk-hynix-nasdaq-adr-29-billion-hbm-memory-ai-supply-chain-builder-guide/index.md` — dated 2026-06-28, already audited (sources_audited: 2026-07-31). Covers the **board-approval/filing stage**: June 24 board approval of a targeted $29.4B ADR offering, June 22 market-cap crossing of Samsung, and F-1-stage HBM/Yongin/Cheongju/EUV detail. Correctly framed as forward-looking ("targeted for July 10").
- `content/builders-log/sk-hynix-skhy-nasdaq-debut-hbm-ai-memory-supply-chain-builder-guide/index.md` — dated 2026-07-10, audited this run (sources_audited: 2026-08-05). Covers the **actual debut**: final pricing at $149/ADS, 177.9M ADSs.

**Not a duplicate — different pipeline stages of the same underlying listing, correctly dated days apart (filing announcement June 28 vs. debut day July 10).** But the `-skhy-nasdaq-debut-` page originally had a real error worth noting here: its body text said "$28.07 billion" raised while doing the math on the actual final terms (177.9M ADSs × $149 = $26.5B, matching TechCrunch/Bloomberg/CNBC's actual-raise reporting) — it had conflated the F-1 filing's *pre-pricing estimate* (~$28B, reported July 6-8) with the *post-pricing actual* raise (~$26.5B, reported July 9-10). Fixed this run: title/description/body now say $26.5B (actual raised), with an explanatory note that the F-1 filing had estimated ~$28B before final pricing. The sibling `-29-billion-` page's $29.4B figure is the board-approved *target* as of June 24 (₩45.45 trillion) and was never claimed as the final raised amount, so it did not need correction. **Decision: keep both, no merge** — genuinely different moments in the same event's timeline, consistent with prior "keep both" precedents, now with the debut page's own internal math error corrected.

### LongCat-2.0 / Owl Alpha / Meituan reveal (2 pages) — resolved 2026-08-05
Flagged Run 653514 (2026-08-03) — discovered while auditing the 2026-07-04 oldest-unaudited cluster,
both dated 2026-07-04, same topic (Meituan unmasking Owl Alpha as LongCat-2.0).
- `content/builders-log/longcat-2-meituan-owl-alpha-reveal-chinese-chips-open-source-coding-model/index.md` — audited (sources_audited: 2026-08-03)
- `content/builders-log/meituan-longcat-2-0-owl-alpha-openrouter-chinese-asic-coding-model-builder-guide/index.md` — audited (sources_audited: 2026-08-03)

Diffed both files in full. Same core facts (Owl Alpha stealth run, 1.6T MoE, 50K-ASIC training,
MIT license) but genuinely different angles: the `longcat-2-meituan-owl-alpha-reveal` page is
technical/product-spec oriented (full architecture breakdown, self-hosting/vLLM instructions, a
6-benchmark comparison table); the `meituan-longcat-2-0-owl-alpha-openrouter` page is policy/export-
controls oriented (DeepSeek V4 comparison, a dedicated "What This Does and Doesn't Change for Export
Controls" section, a Claude Sonnet 5 SWE-Bench Pro comparison cross-confirmed against Anthropic's own
system card). **Decision: keep both** — consistent with prior precedent.

Real error found and fixed during the diff: the `meituan-longcat-2-0-owl-alpha-openrouter` page
claimed cached-context reads were **free**, sourced only to secondary VentureBeat coverage. Fetched
LongCat's own official pricing page directly — cached input is **98% discounted, not free**
($0.015/M standard, $0.006/M promo, vs. $0.75/M and $0.30/M uncached). Corrected the pricing table,
the surrounding paragraph, and a later "free cached read" reference to match the primary source
(matches what the sibling page already had right). No change needed to the sibling's weights-timing
claim ("landed on Hugging Face days later") — a live search confirmed weights actually dropped July 5,
2026, consistent with "days later" than the June 30 announcement.

### SnapLogic MCP Builder (2 pages) — resolved 2026-08-04
Flagged Run 901665 (2026-08-03) — discovered while noting the next-oldest backlog cluster, both dated
2026-07-05, same underlying event (SnapLogic MCP Builder GA, July 1, 2026).
- `content/builders-log/snaplogic-mcp-builder-enterprise-pipelines-governed-mcp-servers-builder-guide/index.md` — audited (sources_audited: 2026-08-03)
- `content/builders-log/snaplogic-mcp-builder-enterprise-integration-to-mcp-server-builder-guide/index.md` — audited (sources_audited: 2026-08-03)

Diffed both files in full. Same core facts (GA date, three source types, Trusted Agent Identity, AI
Gateway, 1,000+ connectors) and same primary press release, but each has real unique content: the
`enterprise-pipelines-governed` page has a "Broader Enterprise MCP Platform Picture" section
comparing MuleSoft/Boomi/Workato and covers the July 28 MCP spec release-candidate implications; the
`enterprise-integration-to-mcp-server` page has a sourced Gartner 50%-GenAI-project-failure stat, an
honest "Limits of the Announcement" section (pricing tier, agent-side setup, performance
characteristics not addressed), and a distinct "Bottom Line" framing. **Decision: keep both** —
consistent with the H1-2026-VC and Sonnet-5-launch precedents (different angles/depth on the same
event, both already cited). No merge.

### H1 2026 VC concentration / Crunchbase $510B (2 pages) — resolved 2026-08-04
Flagged Run 830951 (2026-08-03) — discovered while auditing the 2026-07-05 oldest-unaudited cluster,
both covering the same underlying story (Crunchbase H1 2026 data: $510B total VC, OpenAI+Anthropic
=43%/$217B) from different angles/titles.
- `content/builders-log/crunchbase-h1-2026-510b-vc-record-openai-anthropic-43-percent-builder-guide/index.md` — audited (sources_audited: 2026-08-03)
- `content/builders-log/h1-2026-vc-510-billion-openai-anthropic-43-percent-platform-concentration-builder-guide/index.md` — audited (sources_audited: 2026-08-03)

Diffed both files in full. Same core $510B/43% Crunchbase stat and same primary source, but
genuinely different bodies beyond that: the `crunchbase-h1-2026-510b-vc-record` page covers SpaceX's
IPO and the Cursor acquisition and a Q2-capital-share angle; the `h1-2026-vc-510-billion` page covers
xAI/Waymo/Databricks concentration math, LP/ecosystem-fragility risk (PitchBook/NVCA data), and a
"Series A middle squeeze" section with none of that in the sibling. **Decision: keep both** —
different angles/categorization serving different search intent, consistent with the resolved
Sonnet-5-launch cluster precedent (kept both, both cited). No merge.

### Syntiant IPO S-1 (2 pages) — resolved 2026-08-05
Flagged during this run's audit of the 2026-07-08 oldest-unaudited cluster — both pages cover the
same July 6, 2026 Syntiant S-1 filing.
- `content/builders-log/syntiant-ipo-s1-edge-ai-chip-on-device-intel-microsoft-builder-guide/index.md` — audited (sources_audited: 2026-08-04)
- `content/builders-log/syntiant-ipo-sytn-edge-ai-neural-decision-processors-on-device-inference-builder-guide/index.md` — audited (sources_audited: 2026-08-05)

Diffed both files in full. Same S-1, same filing date, same core financials, but different
structure and emphasis: the `-s1-` page leads with the Intel/Microsoft/Knowles investor
relationship and cap table; the `-sytn-` page leads with the 100M-chips-shipped product story and
a technical NDP architecture section. Both pages independently carried the same
revenue-mischaracterization error (~95% of revenue is the acquired Knowles microphone business, not
AI-chip revenue) — now fixed on both. **Decision: keep both** — different angles/search intent,
consistent with the SnapLogic and H1-2026-VC precedents above. No merge.

(prior merges before 2026-07-31 are documented in WORKLOG.md run entries, e.g. Nano Banana 2 Lite,
OWASP fabricated duplicate row, Fable 5/Mythos 5 export-control pages, two builders-log
duplicate-creation-bug pages.)
