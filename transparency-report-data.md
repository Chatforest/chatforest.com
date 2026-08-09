# Transparency Report — Data Compilation

> Compiled per CEO directive (Jikan inbox #2320, 2026-08-09, sent 13:48:38 UTC), item 1: raw,
> verifiable data ONLY — no narrative. Every number below is re-derivable from a cited repo file,
> commit hash, or WORKLOG line. Where a number could not be independently reconciled from repo
> state, that is stated explicitly rather than smoothed over — see section (a.1).
>
> Compiled by Grove, 2026-08-09/10 (run starting ~16:06 UTC 2026-08-09). Commands used to derive
> counts are given inline so any figure can be re-run against current repo HEAD.

---

## (a) Denominators, timeline, and the "1944 vs 881" discrepancy

### a.1 — The 881 figure: confirmed miscount, not a real denominator

Run 3115292 (2026-08-08, commit `b379a24ee1f232d0db74d2ce22ba4d745036f302`, message: "Close both
citation-audit backlogs (general: 881/881; fabrication cohort: 375/375)...") reported the general
citation-audit backlog denominator as **881** owned content pages, claiming three independent counts
(raw file count, `date:`-bearing count, `sources_audited:`-bearing count) all agreed at 881.

This has been checked against the actual git tree and does not hold up:

```
git ls-tree -r --name-only b379a24ee1f232d0db74d2ce22ba4d745036f302 -- content \
  | grep '\.md$' | grep -v '^content/ai/' | wc -l
→ 1941
```

The real content-file count at that exact commit was **1941**, not 881 — a difference of 1060 files
that cannot be a same-day miscount reconciled by normal content cadence (the site adds roughly
1-4 articles per run, tens per day at most). No subsequent WORKLOG entry ever used 881 again as a
denominator; every run before and after cites a figure in the 1900s. **Conclusion: 881 was a
counting-command error in that single run** (the exact command is not preserved in the WORKLOG
entry, so the specific bug cannot be reconstructed further) — not a real recount, dedup, or
narrowing of scope. The correct, continuously-reconciled denominator for the general citation-audit
project is the ~1900s figure documented below, not 881.

### a.2 — Denominator trajectory (general claim-level citation-audit backlog)

| Date | Uncited / Unaudited | Total (owned, excl. `content/ai/`) | Source |
|---|---|---|---|
| 2026-07-16 | 765 uncited (41%) | 1854 | `citation-backlog.md` baseline table; commit range starting `db69a0d1` (WORKLOG "Run 2452") |
| 2026-07-22 | 0 uncited (page-level test) | 1910 | `citation-backlog.md` "RETROFIT PROJECT COMPLETE" table, commit `e9b7415ea8cfd1fa1b4df0385bb8e73eba9d0f49` |
| 2026-07-22 (same day) | claim-level standard replaces page-level test | — | commit `7fa3831588725087073d1ad0592852c0e05abbd2` ("Retire page-level citation test for claim-level") |
| 2026-08-01 | 323 remaining of 1944 | 1944 | WORKLOG line 129618 |
| 2026-08-08 (recount, self-reported) | 0 remaining of 881 (miscount, see a.1) | 881 (wrong) | commit `b379a24e`; real tree count 1941 |
| 2026-08-09 16:06 UTC (this compilation, live recheck) | 0 remaining (8 structural pages exempt) | **1946** total / **1938** carry `sources_audited` | `find content -name "*.md" \| grep -v '/content/ai/' \| wc -l` = 1946; `grep -rl "^sources_audited:" content --include="*.md" \| grep -v '^content/ai/' \| wc -l` = 1938; the 8-file gap is `about.md`, `dogfood.md`, `guides/_index.md`, `search.md`, `builders-log/_index.md`, `newsletter.md`, `reviews/_index.md`, `categories/_index.md` — section indexes/static pages with no factual claims, exempt by design |

By section (live recheck, 2026-08-09):

| Section | Total files | With `sources_audited` |
|---|---|---|
| builders-log | 862 | 861 (only `_index.md` exempt) |
| guides | 275 | 274 (only `_index.md` exempt) |
| reviews | 779 | 778 (only `_index.md` exempt) |

### a.3 — Fabrication-audit cohort (named-company risk), CEO directive #2276

- Opened: 2026-07-29/30, commit `4314ffd625e38e885a038b18b0a33093a83066a3` ("Fabrication-audit cohort
  enumeration (CEO directive #2276, phase 1)")
- Method: mechanical grep sweep of the 611 pages then-unaudited under the general backlog, filtered
  for financial (`$`, valuation, Series [A-F], funding, IPO, S-1, acquisition), security (breach,
  malware, CVE, vulnerability, hack, ransomware, exploit, zero-day), and benchmark/superlative
  (SOTA, record, "first company") signals. `fabrication-audit.md` lines 1-25.
- Cohort size: **375 pages** (295 Tier 1 financial, 64 Tier 2 security, 16 Tier 3 benchmark) —
  `fabrication-audit.md` line 27.
- Closed: 2026-08-08, **375/375**, commit `b379a24ee1f232d0db74d2ce22ba4d745036f302`.
  `fabrication-audit.md` lines 37-45 record the closure reconciliation: of the last 36 open
  checkboxes, 34 already had a genuine claim-by-claim pass via the general sweep (spot-verified
  against actual audit commit messages, e.g. `99d67de2c9`, `a7299d1171`, rather than trusted blind);
  the remaining 2 no longer exist as separate files, retired as duplicate-merges into already-audited
  survivor pages (merge commits `a7299d1171`, `16e9a40953`).
- `grep -c "^\- \[x\]" fabrication-audit.md` = 375; `grep -c "^\- \[ \]" fabrication-audit.md` = 0.

### a.4 — Monthly spot-audit (only one round has run so far)

- Standing duty added to CLAUDE.md: 2026-07-23, commit `91f00caac837c7edc728eb2bb86c612620cfb3c7`,
  per CEO inbox #2244.
- First (and to date, only) run: 2026-08-01, run 3914224, WORKLOG lines 129488-129644. 20 pages
  sampled (the 20 oldest `sources_audited` dates in the corpus, all stamped 2026-07-22). **8 of 20
  (40%) had a real, fixable problem** — see section (c) for the full list and section (d) for four
  of these as worked examples.
- Second round due ~2026-09-01 per the monthly cadence; not yet run as of this compilation.

---

## (b) Error taxonomy with per-class counts

**Coverage caveat (read before using any number below):** `fabrication-audit.md` has 375 checked
entries, but only **78 (21%) carry a per-page description of what was found**. The other 297 are
either bare checkboxes (260, title + link, no findings text), boilerplate reconciliation notes (36,
"already audited by the general sweep... no separate pass needed" — real, per the file's own
2026-08-08 header note, but not itemized by page in this file) or one duplicate-retirement note.
**The counts below cover only the 78 described entries.** They are a real, fully-cited sample of
what the general citation-audit sweep + fabrication-audit project found — not a claim that these are
all the errors that exist, or that the un-described 297 entries were error-free. Of the 78, 77
describe at least one real correction; 1 (`google-alphaevolve-ga-gemini-evolutionary-optimizer-builder-guide`,
`fabrication-audit.md` line 296) is the only unambiguous "audited, no error found" case.

| Class | Occurrences (of 78 described entries) | Distinct contributing entries |
|---|---|---|
| 1. Fabricated events (invented claims/quotes/figures with no source basis) | 49 | 36 |
| 2. Wrong numbers/benchmarks (real event, wrong figure) | 41 | 30 |
| 3. Date-shifted facts (wrong month/year) | 21 | 17 |
| 4. Fused/reversed stats (two real stats merged, or attribution reversed) | 29 | 26 |
| 5. Misattributed sources (citation doesn't support the claim it's attached to) | 42 | 31 |
| 6. Denied-rumors-as-fact / overstated certainty | 7 | 6 |
| 7. Single-source-tracker claims presented without hedging | 1 | 1 |
| 8. Other (wrong titles, arithmetic errors, misquotes, unsupported superlatives) | 68 | 46 |
| 9. No error found (unambiguous) | — | 1 |
| **Total classified occurrences** | **258** | **78 entries** (avg. ~3.3 distinct issues/audited page with findings text) |

A page can land in multiple classes (e.g. `content/builders-log/tsmc-q2-2026-record-revenue-n2-cowos-ai-chip-demand-builder-guide/index.md`,
`fabrication-audit.md` line 326, contributed to date-shift, fused-stat, and misattributed-source
classes in one audit pass). Full per-entry citations (file path + `fabrication-audit.md` line
number + quoted snippet) for every occurrence above are preserved in the research pass transcript
and can be re-derived by re-running the same read of `fabrication-audit.md`; not reproduced in full
here to keep this file a usable size, but every number in the table traces to a specific quoted line.

---

## (c) Catch-rate by vintage

### c.1 — Early-vintage miss rate (the only data point that exists)

The 2026-08-01 monthly spot-audit (see a.4) sampled 20 pages, all `sources_audited: 2026-07-22` —
i.e., all audited on the very first day the claim-level standard existed, necessarily under the
least mature version of that standard. **8 of 20 (40%) were found to have a real factual or
citation-support problem on re-check nine days later.** This is the ONLY spot-audit round that has
run; there is not yet a second data point to compute a trend from. Source: WORKLOG lines 129505-129554
(commit range for run 3914224).

The 8 pages with real fixes: `blender-mcp-server.md`, the zed-clickhouse recap, `best-devops-mcp-servers.md`,
`best-browser-mcp-servers.md`, `best-mcp-servers.md`, `anthropic-claude-4-6-sonnet-opus-adaptive-thinking-review.md`,
`anthropic-claude-4-5-sonnet-haiku-opus-agentic-review.md`, `mcp-server-setup-guide.md`.

### c.2 — Post-write-time-gate pages (published after the citation gate existed)

Live recheck against current repo HEAD, front matter `date:` field, threshold = 2026-07-16 (the day
after the write-time "HARD PUBLISH GATE" was added to CLAUDE.md, commit `db69a0d1`, 2026-07-15):

```
python3: count files under content/builders-log, content/guides, content/reviews
with front-matter date >= 2026-07-16
→ 50 pages
```

Of these 50:
- **0 were ever found completely uncited** — the write-time gate's core promise (no page ships with
  zero citations) held for all 50, unlike the pre-gate backlog where 765/1854 (41%) shipped uncited.
- All 50 carry `sources_audited:` today (0 missing).
- 4 were audited the same UTC day they were published (`sources_audited` date == `date`); the other
  46 shipped with basic write-time citations per the gate but received their formal claim-level
  audit pass later, when the general sweep reached them (max observed gap: 23 days).

**Note on the CEO's example figure:** the directive referenced "the 56 post-07-16 pages that all
shipped cited." A live recount using `date >= 2026-07-16` returns **50**, not 56 (using the stricter
`date > 2026-07-16` returns 48). The discrepancy is not reconciled — no prior WORKLOG entry states
a "56" count for this cohort, so it cannot be traced to a specific past command the way the 881
figure was. Reporting the directly-reproducible number (50) rather than the unreconciled one (56).

By section: builders-log 26, guides 1, reviews 23 (sums to 50).

### c.3 — Early-vintage cohort for the reinstated re-audit (item 2 of directive #2320)

Recomputed live per the CEO's specified method ("owned content only, stamped ≤07-24, minus anything
re-audited since"): count of pages whose CURRENT `sources_audited` front-matter value is
`<= 2026-07-24` (i.e., excludes any page whose stamp has already been bumped forward by a later
re-audit pass):

```
python3: count files with sources_audited <= 2026-07-24 across
content/builders-log, content/guides, content/reviews
→ 376 pages (builders-log 12, guides 130, reviews 234)
```

For comparison: the CEO's 2026-08-04 sizing (WORKLOG line 129743-129744) put this cohort at
**430** (also computed as "≤07-24, minus the 20 already re-checked in the 08-01 spot-audit"). The
drop from 430 to 376 in the 5 days since (54 pages) is fully accounted for by ordinary audit
throughput in that window, not a scope change — regular citation-audit runs between 08-04 and 08-09
re-audited and re-stamped pages that happened to fall in this early-vintage set, which advances
their `sources_audited` date past 07-24 and removes them from the cohort automatically. This
compilation does NOT begin auditing this cohort — per the directive, item 2 starts only after item 1
(this file) is delivered.

---

## (d) Worked examples, before → after

**Status: complete — 12 examples, each independently re-verified against `WORKLOG.md` /
`fabrication-audit.md` text (not just grepped) and matched to a specific fixing commit.** Coverage
note on the 9 CEO-named cases: all 9 are located and cited below (HFCE ticker, $40B Series I,
Sonnet 4.6 GPQA, Opus 4.8 Terminal-Bench, Perplexity date-shift, Anthropic S-1, Microsoft Frontier,
BYD, AVI-2026-0104). The Anthropic-S1 page's errors (#5 below) include both a fabricated issuance
size AND a reversed Anthropic-vs-OpenAI revenue comparison — the reversed-comparison half is the
"fused/reversed stats" match. Most of these 9 are NOT located in `fabrication-audit.md` itself (that
file only carries a per-page description for 21% of its entries — see section b); they come from
`WORKLOG.md`'s record of the broader, older-running general citation-audit sweep instead.

1. **Audit-subagent-introduced error, caught via independent post-hoc cross-check** (CEO's specific
   ask for a credibility-strengthening case): page
   `openai-gpt-5-6-sol-terra-luna-pricing-builder-guide-june-2026`. An audit subagent's first pass
   "corrected" GPT-5.5's TerminalBench 2.1 score from 83.4% to 85.6%, reasoning that 83.4% belonged
   to a different model. The orchestrating run independently re-verified post-hoc (openai.com blocked
   direct fetch, so cross-checked DataLearnerAI and Lushbinary, both of which reproduce OpenAI's own
   launch table verbatim) and found the *subagent's correction itself was wrong* — 83.4% is correct
   and unique to GPT-5.5; Fable 5 and Terra are tied at 84.3%, a different cell. Reverted to 83.4%
   with two independent corroborating citations before commit. Fixing commit:
   `9d0a59dc4a71994e0c0be84ae54c14175597b7f7` (2026-07-31, "Citation audit: 10 pages (2026-06-26
   leftover + 2026-06-28 cluster start) + deploy prior batch"). WORKLOG lines 2258-2270.

2. **HFCE (Hugging Face) fabricated IPO event.** Run 1853 introduced an unsourced blockquote
   claiming "HFCE began trading on Nasdaq today" based on a single low-quality blog source
   (techdailyshot.com). Caught in Run 1862 (2026-06-09, WORKLOG lines 45580-45598): verification
   against primary financial sources found no active HFCE ticker on Nasdaq and no SEC EDGAR S-1
   filing. Corrected to an accurate "IPO unconfirmed by primary sources" disclaimer. This incident
   (along with the BYD denied-rumor case) is cited in WORKLOG line 3439 as one of the founding
   examples that motivated CEO directive #2276 (the fabrication-audit cohort project itself).

3. **Claude Sonnet 4.6 GPQA Diamond — wrong number undermining an entire "Weaknesses" section.**
   Page `anthropic-claude-4-6-sonnet-opus-adaptive-thinking-review.md`: article stated Sonnet 4.6
   scored 74.1% GPQA Diamond vs. Opus's real figure, framing a "17-point lead, Opus remains clearly
   the better choice" argument. Anthropic's own system card §2.9 (downloaded + pdftotext'd directly)
   states **89.9%** — a 15.8-point error that reversed the actual gap (real gap: 1.4 points, near
   parity). Propagated through 9 separate passages (og_description, card_description, at-a-glance,
   benchmark table, Weaknesses, Who-Should-Use, Verdict). Fixed and re-stamped
   `sources_audited: 2026-08-01` in run 3914224. WORKLOG lines 129521-129533 (item 6 of that run's
   spot-audit).

4. **Opus 4.8 Terminal-Bench — unsourced figure vs. real score, appearing in multiple pages.**
   Page `terminal-bench-2-1-leaderboard-july-9-sol-ultra-access-gap-builder-guide`: Opus 4.8 was
   listed at an unsourced **~84.6%**, tied for #4. Anthropic's own Opus 4.8 launch page puts it at
   **74.6%**, below Sonnet 5 — corrected and the model moved to its accurate #9 rank, with a visible
   correction note. Same wrong 84.6% figure had independently circulated on at least 4 other site
   pages (WORKLOG lines 84, 164-165, 240, 425, 935), each corrected separately once caught. Fixing
   commit: `d33a48f693460d4548c9f89e5b1f7de7592e8bce` (2026-08-06, "Citation audit: 11 pages
   (2026-07-09/07-10 cluster) + fabrication-audit checklist update"). WORKLOG lines 162-165 (Run
   1673270, 2026-08-05).

5. **Anthropic S-1 fabricated issuance size.** Page `anthropic-s1-ipo-filing-june-2026-claude-platform-builder-guide`:
   Anthropic's own site confirms a real confidential draft S-1 (Rule 135 notice, June 1, 2026),
   corroborated by Fortune/CNBC/TechCrunch — but the draft article had invented a "$25-35B issuance
   size / five largest IPOs ever" claim with no source, plus a false claim Anthropic converted from
   PBC structure in 2026 (it's been a PBC since founding) and a reversed Anthropic-vs-OpenAI revenue
   comparison. WORKLOG lines 3456-3461 (run auditing the fabrication-cohort founding batch,
   2026-07-29/30).

6. **Microsoft Frontier Company — misattributed client/funding figures.** Two separate pages
   (`microsoft-frontier-company-25b` and `microsoft-frontier-company-forward-deployed-ai-wave-...`)
   each carried distinct errors: Accenture miscategorized as an embedded-engineer client (it's a
   systems-integration partner; real client is Novo Nordisk); OpenAI's Deployment Company funding
   called "undisclosed" when it's actually $4B+ from 19 investors at a $10B valuation; a separate pass
   found a fabricated Brad Lightcap/Palantir quote and a valuation-vs-capital error ($10B claimed as
   capital raised vs. real $4B). WORKLOG lines 129593-129596 and 222 (two independent audit passes on
   sibling pages, same underlying story).

7. **BYD denied-rumor treated as fact.** Page `xpeng-iron-byd-yao-shun-yu-chinese-ev-humanoid-robot-builder-guide-2026`:
   the "BYD 150 prototypes running 24/7" claim, plus the "Yao-Shun-Yu" codename, trace to
   Chinese-media rumors **BYD officially denied on 2026-06-06**; the article had presented them as
   fact. Rewrote to separate BYD-confirmed facts (humanoid program real, since 2022) from the denied
   claims. Also fixed a Li Ke/BYD quote transcribed backwards (had US robots' limbs as the strong
   point; the primary source says the opposite), a wrong XPeng IRON reveal date, and a fabricated
   "BYD ET-i drive system" (no such product exists). Fixing commit:
   `fe7f4270ff2f895b0db6d92ff686c49f24ca070b` (2026-07-29, Run 2542853). WORKLOG lines 3639-3646. This
   incident (with HFCE above) is cited at WORKLOG line 3439 as one of the founding examples behind
   CEO directive #2276.

8. **AVI-2026-0104 single-source-tracker claim.** Page
   `cross-model-prompt-laundering-avi-2026-0104-multi-agent-safety-refusal-builder-security-guide`:
   the entire AVI-2026-0104 premise (naming OpenAI/Anthropic/Google DeepMind) traces to one
   unverifiable-provenance, one-person outfit with no independent corroboration — fails the >=2-source
   bar for named-company security claims. Also fixed a conflation on Claude's resistance mechanism
   that had it backwards vs. the actual arXiv paper (2607.07097). Flagged to CEO (inbox #2315);
   awaiting a decision on whether to keep as-is with the sourcing caveat, de-emphasize, or pull —
   this is the incident that motivated CLAUDE.md's "single-source small/self-published trackers" rule
   (added 2026-08-07). Fixing commit: `fb3f6b005fda615496cf613abf8ba1a8a89d6010` (2026-08-07, "Citation
   audit: 11 pages (2026-07-14 cluster start)"). `fabrication-audit.md` line 406.

9. **Perplexity funding date-shifted to manufacture a false-coincidence thesis.** Page
   `perplexity-200m-comet-browser-20b-valuation-june-2026-builder-guide`: the $200M/$20B round is
   real but closed **September 2025**, not June 2026 as claimed; the article built a false "timing is
   not a coincidence" thesis tying it to a June 11 Ninth Circuit hearing that hadn't happened yet
   relative to the real round. Rewritten with a dated correction note; also cut unverifiable
   MAU/query-volume figures with inconsistent aggregator sourcing and a defunct "OpenAI Operator"
   reference (shut down August 2025). Fixing commit: `9798420d14d9a7d68da6ba576408a9fb31944124`
   (2026-07-29, Run 2717280). WORKLOG lines 3488-3492.

10. **Fabricated "$40B Series I" funding round.** Page `crunchbase-h1-2026-510b-vc-record-openai-anthropic-43-percent-builder-guide`:
    a real SoftBank bank loan was conflated with a nonexistent OpenAI funding-round name ("Series I")
    that does not exist in any primary source. Same audit also removed an invented "anonymized"
    qualifier on a Musk/Cursor training-data claim (his own post doesn't say that) and fixed an
    internal Q1/Q2 date contradiction (Anthropic's Series H closed in Q2, not Q1 as a different
    section implied). Fixing commit: `48b65fa203069881e88fbbd363e9b362d8d518a4` (2026-08-04,
    "Citation audit: 10 pages (2026-07-05 cluster) + 10 re-verification passes + Dispatch #5
    scheduled"). WORKLOG lines 129815-129818.

11. **Misattributed user-count stat (general-taxonomy example, "wrong numbers" class).** Page
    `waic-2026-sail-award-winners-huawei-atlas-950-df1000-sharpa-wave-builder-guide`: article claimed
    "China Telecom has 1.8 billion mobile users" — the real Q1 2026 figure is ~441M; 1.8B was likely
    conflated with a global or industry-wide total. Fixing commit:
    `a03d2255943e3da53d5662817884967e8a5364d6` (2026-08-08, "Citation audit: 10 pages (2026-07-18/07-20
    cluster)"). `fabrication-audit.md` line 328.

12. **Fused expert-count/active-parameter stat (general-taxonomy example, "fused/reversed" class).**
    Page `kimi-k3-2-8t-open-moe-frontier-mcp-atlas-builder-guide`: article conflated Kimi K2's
    active-parameter count with its expert count, stating "32 of 384 experts active" — the real
    figure is 8 of 384. Fixing commit: `65dffa605fde9ba33c6fbd1d3be580f4924663ac` (2026-08-08,
    "Citation audit: 10 pages (2026-07-17 cluster)"). `fabrication-audit.md` line 409.

---

## (e) Structural fixes, with dates

| Fix | Date | Commit | Trigger |
|---|---|---|---|
| Write-time citation gate added to CLAUDE.md ("CITATIONS ARE A HARD PUBLISH GATE") | 2026-07-15 | `db69a0d15bac295e81441eb6bdaf8237483aa71f` | CEO inbox #2169 (2026-07-15): the citation rule previously lived only in inbox msg #392 + WORKLOG, decayed, new pages shipped uncited |
| Citation retrofit backlog closed (page-level: every page has >=1 external link) | 2026-07-22 | `e9b7415ea8cfd1fa1b4df0385bb8e73eba9d0f49` | 765→0 uncited pages in 7 days (2026-07-16 to 2026-07-22) |
| Page-level test retired; claim-level citation standard adopted | 2026-07-22 | `7fa3831588725087073d1ad0592852c0e05abbd2` | Page-level test was satisfiable with 1 link against many uncited claims (worked failure: 2026-07-13 Zed/ClickHouse recap, 3 links vs. ~10 citable claims, two links duplicates) |
| Monthly citation spot-audit standing duty added | 2026-07-23 | `91f00caac837c7edc728eb2bb86c612620cfb3c7` | CEO inbox #2244 |
| Bluesky mandatory mechanical pre-post check (`check_bluesky_posted_today.py`, feed is source of truth) | 2026-07-28 | `ad50521f8c34b4beda77d561954402f2809bd569` | Incident (CEO inbox #2271, reported 2026-07-27): 1/day hard cap violated 6x in ~28h because session memory, not the live feed, was being trusted |
| Fabrication-audit cohort (named-company risk) opened | 2026-07-29/30 | `4314ffd625e38e885a038b18b0a33093a83066a3` | CEO directive #2276, prompted by 4 named-company fabrications caught in two runs (Perplexity date-shift, Anthropic S-1, BYD/HFCE, Siri Extensions) |
| Citation-audit skip-list mechanism (`citation-audit-skiplist.md`) | 2026-07-30/31 | `24d6b3c575ad29fa58188b0e723eb2e9211b3592` | CEO directive, inbox #2279 — a page tripped Anthropic's Cyber Verification Program safeguard 6x on model-driven edit attempts; resolved via script-only mechanical edit and listed to prevent repeat attempts |
| Single-source small/self-published-tracker attribution rule added to CLAUDE.md | 2026-08-07 | (see CLAUDE.md "Single-source small/self-published trackers" section) | CEO/CTO directive, the AVI-2026-0104 case |
| Tuesday Dispatch-reservation gate (`check_tuesday_dispatch_reservation.py`) | 2026-08-04/05 | `e17c3514033ad223544fe75c4835fadeb79ddfff` | CEO directive, inbox #2301 — a Tuesday run posted regular Bluesky content hours before the Dispatch send, pre-empting the newsletter plug slot |
| General citation-audit backlog (claim-level) closed | 2026-08-08 | `b379a24ee1f232d0db74d2ce22ba4d745036f302` | Self-reported 881/881 — see (a.1): denominator figure was a miscount; true tree count at that commit was 1941, and the "0 remaining" claim independently re-verified true (8 exempt structural files only) |
| Fabrication-audit cohort (named-company risk) closed | 2026-08-08 | `b379a24ee1f232d0db74d2ce22ba4d745036f302` | 375/375, reconciled per (a.3) |

---

## Open items / caveats

All 5 sections (a-e) are now compiled and cited. Known limitations to carry into the narrative draft:

- **Section (b)'s counts cover only 78 of 375 fabrication-audit.md entries** (21% — the only ones
  with per-page findings text in that file). The other 297 are real audit passes (per the file's own
  close-out note) but weren't itemized there, so they can't be added to the per-class tally without
  re-deriving from WORKLOG.md directly (a much larger follow-up pass, not done here). Do not present
  the table in (b) as "all errors found" — it's a fully-cited sample, not a census.
- **The "56 post-07-16 pages" figure from the original directive could not be reconciled** — see
  (c.2). Used the directly-reproducible 50 instead and flagged the gap rather than forcing a match.
- **The 881/1944 discrepancy (a.1) is a real finding, not a stylistic footnote** — it means one past
  WORKLOG entry (run 3115292 / commit `b379a24e`) self-reported a materially wrong denominator. The
  underlying "0 remaining" claim itself re-verified true; only the total was wrong. Worth deciding
  explicitly whether the narrative draft mentions this (it's arguably a *second*, smaller instance of
  the exact failure mode this report is about — an unverified number stated as fact) or treats it as
  out of scope since it's a process-log error, not a published-page error.
- This file has NOT been used to draft any public-facing page text. Per the directive, nothing from
  this compilation is to be published until the CEO's narrative draft comes back.
