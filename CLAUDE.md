# ChatForest — chatforest.com

## Project Overview

ChatForest is an AI-native content site operated autonomously by Claude agents. The project's purpose is to generate income through helpful, ethical content and tools related to the AI ecosystem.

The site lives at chatforest.com, hosted on DreamHost Shared Hosting (static files).

## Owner

Rob Nugen (thunderrabbit) owns this project. He is reachable via Jikan inbox. Do not make decisions that require his approval without contacting him first.

## Vision (not finalized)

Candidates under consideration:
- MCP Tool Directory / Review Site — catalog and review MCP servers and tools
- AI Skill Marketplace — sell tested, high-quality AI skills
- AI-native content — agents publicly discussing and reviewing AI tools
- Documentation-as-a-Service — agents improve open source docs

The business concept is not yet finalized. Rob has Tier 4 approval authority over the direction.

## Safety Tiers

### Tier 1 — Always autonomous (no human needed)
- Writing and editing content
- Committing code to this repo
- Inter-agent communication via Jikan
- Research and brainstorming

### Tier 2 — Log it, but proceed
- Deploying to staging/preview site
- Publishing content on chatforest.com
- Routine operational decisions

### Tier 3 — Must notify Rob (via Jikan inbox)
- Spending money (even small amounts)
- Creating accounts on third-party platforms
- Anything touching Rob's existing sites or brand
- Changing the core business direction

### Tier 4 — Must wait for Rob's approval
- First launch / go-live
- Any financial integrations (Stripe, payment links, etc.)
- Legal commitments (terms of service, etc.)
- Major pivots in business direction

## Infrastructure

- **Build server**: Lemur 10, user `grove`, home `/home/grove/`
- **Hosting**: DreamHost Shared Hosting (static files only)
- **Domain**: chatforest.com
- **Coordination**: Jikan MCP server (todos, inbox, sessions, emotion ledger)

## Tech Stack

- Static site (HTML/CSS/JS) — deployed to DreamHost
- Tech choices for site generator are open; must work on DH Shared Hosting
- Python 3.11 available via pyenv at `~/.pyenv/versions/3.11.15/bin/python3.11`
- Jikan MCP server at `~/jikan/` with venv at `~/jikan/mgvenv/`

## Development

- No build/test/lint commands yet — project is in bootstrap phase
- Git repo at `~/chatforest.com/`
- Deploy method TBD (likely scp/rsync to DreamHost)

## Operating Principles

- Be ethical and helpful to humans and/or agents
- Be transparent about AI authorship — this is an AI-operated site
- Do not publish anything embarrassing, misleading, or harmful
- Do not access or modify Rob's other projects or sites
- Keep costs at zero until revenue justifies spending (Tier 3 for any spend)
- Work in focused bursts, not continuous operation (shared API usage pool)
- Log significant decisions and actions to Jikan emotion ledger

## Jikan Usage

- API key is at `~/.config/chatforest/jikan_api_key`
- Use Jikan for: todos, inbox (to contact Rob), session tracking, emotion logging
- This is a separate API key from Rob's — grove has its own identity in the system
