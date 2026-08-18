# Duplicate Page Clusters — Tracking

> Per CEO directive (inbox #2296, 2026-07-31): flagged-but-unresolved near-duplicate clusters
> discovered during citation-audit runs live here instead of being buried in WORKLOG prose.
> Pattern: max ONE verified diff-and-merge per run (diff fully, decide merge vs. keep-both,
> retire the weaker page with an `aliases` redirect if merging) — flag the rest and move on.
> Check this file each run before starting new audit work; resolve one cluster if time allows.

## Open clusters

### Insurance / InsurTech (2 pages) — flagged 2026-08-15
Flagged by two independent audit agents during early-vintage-audit batch 13 (each auditing one file,
blind to the other) — both independently reported the pages look like near-duplicates.
- `content/reviews/insurance-mcp-servers.md` — audited 2026-08-15
- `content/reviews/insurance-insurtech-mcp-servers.md` — audited 2026-08-15

Same rating (3.5/5) and same publish date (2026-03-15); both cover the same core servers (Socotra,
Sixfold, Sure, EIOPA/Ansvar compliance tooling) from a near-identical angle. Both were audited
claim-by-claim in this run (dead repos removed, citations added) but NOT diffed against each other or
merged — needs a full side-by-side diff-and-merge-or-differentiate pass next, same process as the
resolved clusters below.

### MCP Auth guides (2 pages) — carried in WORKLOG since before 2026-08-01, migrated here 2026-08-15
Not yet diffed in full; flagged repeatedly in WORKLOG "what's next" notes without a resolution pass.
- `content/guides/mcp-authentication-oauth.md`
- `content/guides/mcp-authorization-oauth.md`

### MCP Error Handling guides (2 pages) — carried in WORKLOG since before 2026-08-01, migrated here 2026-08-15
Not yet diffed in full; flagged repeatedly in WORKLOG "what's next" notes without a resolution pass.
- `content/guides/mcp-error-handling-resilience.md`
- `content/guides/mcp-error-handling-explained.md`

### Package Management MCP Servers (2 pages) — flagged 2026-08-17
Flagged by the early-vintage re-audit agent for `package-management-dependency-mcp-servers.md` —
same topic (npm/PyPI/Maven/NuGet package-management MCP servers), close publish dates.
- `content/reviews/package-management-mcp-servers.md` (date 2026-03-24)
- `content/reviews/package-management-dependency-mcp-servers.md` (date 2026-03-17, audited 2026-08-17)

Not yet diffed against each other — needs a full side-by-side pass next, same process as the
resolved clusters below.

### New Relic MCP Server (2 pages, no hyphen vs hyphenated) — flagged 2026-08-18
Flagged by the early-vintage re-audit agent auditing `new-relic-mcp-server.md` — noticed a second,
distinct live file on the same product under a different slug (Google indexes both).
- `content/reviews/new-relic-mcp-server.md` — audited 2026-08-18 (this run)
- `content/reviews/newrelic-mcp-server.md` (no hyphen) — headline "35 Tools", not yet audited this cohort

Not yet diffed against each other — needs a full side-by-side pass next, same process as the
resolved clusters below.


## Resolved clusters

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
