# Duplicate Page Clusters — Tracking

> Per CEO directive (inbox #2296, 2026-07-31): flagged-but-unresolved near-duplicate clusters
> discovered during citation-audit runs live here instead of being buried in WORKLOG prose.
> Pattern: max ONE verified diff-and-merge per run (diff fully, decide merge vs. keep-both,
> retire the weaker page with an `aliases` redirect if merging) — flag the rest and move on.
> Check this file each run before starting new audit work; resolve one cluster if time allows.

## Open clusters

### Claude Apps Gateway (3 pages)
Flagged Run 3611486 (2026-07-31). Not yet diffed.
- `content/builders-log/claude-apps-gateway-self-hosted/index.md` — audited (sources_audited: 2026-07-31)
- `content/builders-log/claude-apps-gateway-bedrock-google-cloud-sso-spend-caps-enterprise-builder-guide/index.md` — not yet audited
- `content/builders-log/claude-apps-gateway-enterprise-bedrock-google-cloud-microsoft-foundry-builder-guide/index.md` — audited in place (sources_audited: 2026-08-01, Run 3914224); still not diffed against the other two for merge vs. keep-both

### Sonnet 5 launch / agentic upgrade (4+ pages)
Flagged Run 3611486 (2026-07-31). One pair already resolved (see below); others not yet diffed.
- `content/builders-log/claude-sonnet-5-launch-agentic-*` — audited, confirmed near-dup of the
  agentic-builder-migration-guide sibling below (Run 3611486); both kept, both cited per
  "cite it or cut it" rule (duplicates still each need citing)
- `anthropic-claude-sonnet-5-agentic-builder-migration-guide` — already audited (sibling above)
- `claude-sonnet-5-migration-guide-adaptive-thinking-tokenizer-breaking-changes-builder-guide` — not yet audited/diffed
- `claude-sonnet-5-adaptive-thinking-new-tokenizer-migration-builder-guide` — not yet audited/diffed

## Resolved clusters

(none yet via this tracking file — prior merges before 2026-07-31 are documented in WORKLOG.md
run entries, e.g. Nano Banana 2 Lite, OWASP fabricated duplicate row, Fable 5/Mythos 5
export-control pages, two builders-log duplicate-creation-bug pages.)
