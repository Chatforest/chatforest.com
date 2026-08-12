# Writing Effective CLAUDE.md Files: The Complete Guide to Claude Code Project Instructions

> A practical guide to writing CLAUDE.md files that actually work.


CLAUDE.md is the single most important file in any Claude Code project. It loads at the start of every session, giving Claude persistent context about your codebase, your conventions, and how you want it to work. Get it right and Claude follows your patterns consistently. Get it wrong — or leave it empty — and every session starts from scratch.

This guide covers how CLAUDE.md works, what belongs in it, how to structure it for real projects, and the most common mistakes that undermine its effectiveness. Our advice draws on [Anthropic's official documentation](https://code.claude.com/docs/en/memory), community patterns from thousands of Claude Code users, and published analysis — including our own experience running this site with Claude Code. [Rob Nugen](https://robnugen.com) operates ChatForest, but the site's content is researched and written by AI.

## What CLAUDE.md Actually Is

CLAUDE.md is not configuration. It is not code. It is a **context injection file** — its contents are loaded as a user message after Claude Code's system prompt, shaping how Claude interprets every instruction you give it during the session.

This distinction matters. Claude does not parse CLAUDE.md for structured fields or validate its format. It reads the file as natural language and follows the instructions as best it can, the same way it follows any other instruction in conversation. This means:

- Clear, specific instructions work better than vague ones
- Fewer, stronger rules outperform long lists of guidelines
- Everything in the file consumes context tokens
- Claude's compliance with rules declines as the file grows longer

## The File Hierarchy

Claude Code reads CLAUDE.md files from multiple locations, layered from broadest to most specific, per [Anthropic's documentation](https://code.claude.com/docs/en/memory#choose-where-to-put-claude-md-files):

| Scope | Location | Purpose |
|-------|----------|---------|
| **Managed policy** | `/etc/claude-code/CLAUDE.md` (Linux/WSL), `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS), or `C:\Program Files\ClaudeCode\CLAUDE.md` (Windows) | Organization-wide standards. Cannot be excluded. |
| **User global** | `~/.claude/CLAUDE.md` | Personal preferences that apply across all projects |
| **Project root** | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared project instructions, checked into git |
| **Local (personal)** | `./CLAUDE.local.md` | Personal, project-specific preferences; gitignored |
| **Subdirectory** | `./subdir/CLAUDE.md` | Loaded on demand when Claude reads files in that directory |
| **Modular rules** | `.claude/rules/*.md` | Topic-specific instruction files, optionally path-scoped |

Anthropic's docs are explicit that these files are **concatenated into context rather than overriding one another**: content is ordered from the filesystem root down to your working directory, so local instructions simply appear later (closer to your actual request) rather than mechanically replacing broader ones. If two files genuinely conflict, Claude "may pick one arbitrarily" rather than always preferring the more local file — see [Anthropic's load-order documentation](https://code.claude.com/docs/en/memory#how-claude-md-files-load) for the exact resolution rules.

**Subdirectory files load lazily.** A CLAUDE.md in `src/api/` only loads when Claude actually reads or modifies files in that directory — it does not consume context tokens until needed. This makes subdirectory files ideal for area-specific rules that should not bloat every session. ([Confirmed in Anthropic's docs](https://code.claude.com/docs/en/memory#how-claude-md-files-load): "Claude also discovers CLAUDE.md and CLAUDE.local.md files in subdirectories... they are included when Claude reads files in those subdirectories.")

## What Belongs in CLAUDE.md

The core principle: **include what Claude cannot figure out by reading the code, and exclude what it can.**

### Include

- **Build, test, and lint commands** — especially non-obvious ones. Claude can guess `npm test` but not `make test-integration PGHOST=localhost`.
- **Code style rules that differ from convention.** If your Python project uses 120-character lines instead of the PEP 8 default, say so. If you follow standard PEP 8, do not bother.
- **Repository workflow** — branch naming conventions, PR process, commit message format, required reviewers.
- **Architectural decisions that are not obvious from the code.** Why does the auth service use a separate database? Why are all API handlers in one file? Context that would take Claude multiple rounds of exploration to discover.
- **Developer environment quirks** — required environment variables, services that must be running, platform-specific gotchas.
- **Common footguns** — mistakes that are easy to make in this codebase and hard to debug.

### Exclude

- **Anything Claude already knows.** You do not need to tell it to write clean code, handle errors, or use descriptive variable names.
- **Code style rules enforced by linters.** If ESLint catches it, CLAUDE.md does not need to mention it. Use pre-commit hooks instead.
- **Detailed API documentation.** Link to docs with `@docs/api.md` rather than embedding them.
- **File-by-file codebase descriptions.** Claude can read the directory structure. Point it to key entry points instead.
- **Information that changes frequently.** CLAUDE.md should be relatively stable. Use the auto memory system for things that evolve run to run.

## A Minimal Effective Example

Here is a CLAUDE.md that covers the essentials in under 40 lines:

```markdown
# Project: invoice-api

FastAPI REST API for invoice management. Python 3.12, PostgreSQL 16.

## Commands
uv run pytest tests/ -x                    # run tests (stop on first failure)
uv run pytest tests/integration/ -x -k db  # integration tests (needs local PG)
uv run ruff check --fix .                  # lint and auto-fix
uv run mypy src/                           # type check

## Architecture
- src/api/       → route handlers (one file per resource)
- src/models/    → SQLAlchemy models (alembic for migrations)
- src/services/  → business logic (handlers call services, never query DB directly)
- src/core/      → config, security, dependencies

## Rules
- MUST run `uv run pytest tests/ -x` and confirm all pass before committing
- MUST NOT modify migration files — generate new ones with `alembic revision --autogenerate`
- All endpoints require authentication except those in src/api/public.py
- Use `Annotated[T, Depends(...)]` for dependency injection, not default arguments

## Gotchas
- The `invoice_number` field is generated server-side. Never accept it from client input.
- PostgreSQL `BIGINT` IDs — do not use `int` in Python models, use `int` with no upper bound check
- Test database is wiped between test sessions via conftest.py fixture, not between individual tests
```

This file tells Claude exactly what it needs — commands, structure, hard rules, and non-obvious traps — without restating things Claude can infer from reading the code.

## The @import System

As projects grow, a single CLAUDE.md becomes unwieldy. The `@import` syntax lets you split instructions across files and load them selectively:

```markdown
# CLAUDE.md (root)
Invoice management API. See @README.md for project overview.

## Commands
uv run pytest tests/ -x

## Detailed guides
- Architecture: @docs/architecture.md
- Database patterns: @docs/database-conventions.md
- API design rules: @docs/api-guidelines.md
```

Imports resolve relative to the containing file, not the working directory. Absolute paths and home directory references (`@~/...`) also work. Imported files can recursively import further files, up to a maximum depth of four hops ([Anthropic's docs](https://code.claude.com/docs/en/memory#import-additional-files)).

**When to use imports vs. inline content:**
- **Inline** for rules Claude needs every session (commands, critical constraints)
- **Import** for detailed guides Claude needs only when working in specific areas
- **Subdirectory CLAUDE.md** for area-specific rules that should load automatically

## Path-Scoped Rules

The `.claude/rules/` directory supports topic-specific instruction files. Files without frontmatter load unconditionally. Files with `paths` frontmatter load only when Claude reads matching files:

```markdown
---
paths:
  - "src/api/**/*.py"
---
# API Handler Rules
- Every endpoint MUST return a Pydantic response model, never a raw dict
- Use status code 201 for creation endpoints, 200 for everything else
- Rate limiting is applied at the nginx layer — do not implement it in handlers
```

```markdown
---
paths:
  - "tests/**/*.py"
---
# Testing Rules
- Use factory_boy for test data, not raw model constructors
- Integration tests go in tests/integration/, unit tests in tests/unit/
- NEVER mock the database — use the test database fixture
```

This approach keeps your root CLAUDE.md lean while providing detailed, relevant guidance exactly when it matters.

## Progressive Disclosure

The most effective CLAUDE.md files follow a progressive disclosure pattern — essential rules at the top, deeper context available on demand:

**Level 1: Root CLAUDE.md** (under 60 lines)
Commands, stack, critical rules, pointers to deeper docs.

**Level 2: @imported documents**
Architecture guides, coding standards, onboarding docs. Loaded when referenced.

**Level 3: .claude/rules/ files**
Path-scoped rules that activate when working in specific directories.

**Level 4: Subdirectory CLAUDE.md files**
Hyper-specific context for isolated subsystems (e.g., a `mobile/CLAUDE.md` for the mobile app portion of a monorepo).

This structure keeps the always-loaded context small while making detailed guidance available when Claude needs it. Anthropic's own guidance targets under 200 lines per CLAUDE.md file, warning that longer files "consume more context and reduce adherence" ([Anthropic docs on memory](https://code.claude.com/docs/en/memory#write-effective-instructions)). Some practitioners run tighter still: HumanLayer, whose Claude Code workflow writeups are widely cited, reports keeping its own root CLAUDE.md under sixty lines ([HumanLayer](https://www.humanlayer.dev/blog/writing-a-good-claude-md)).

## Writing Rules That Stick

Not all instructions are equally effective. Claude's compliance with rules follows a pattern:

- **High compliance:** specific, verifiable instructions with clear triggers ("MUST run tests before committing," "NEVER modify files in src/generated/")
- **Medium compliance:** stylistic preferences with some ambiguity ("prefer composition over inheritance," "keep functions short")
- **Low compliance:** vague aspirational statements ("write clean code," "follow best practices")

To maximize compliance:

1. **Use strong, unambiguous imperative language** for critical rules. [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) formally defines MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY as requirement-level keywords for specifications; Claude Code community convention borrows MUST / MUST NOT and adds the everyday words NEVER and ALWAYS (which are not themselves part of RFC 2119) to flag non-negotiable constraints.
2. **Make rules verifiable.** "Use 2-space indentation" is verifiable. "Format code properly" is not.
3. **Include the trigger condition.** "When adding a new API endpoint, MUST add a corresponding test in tests/api/" is more actionable than "write tests."
4. **Keep the total instruction count reasonable.** Your CLAUDE.md competes with Claude Code's own system prompt for the model's attention. The Claude Code agent-infrastructure company HumanLayer estimates frontier models follow roughly 150-200 instructions with reasonable consistency, and that Claude Code's own system prompt already uses about 50 of that budget — leaving a working budget of roughly 100-150 for your CLAUDE.md before compliance starts to degrade ([HumanLayer, "Writing a good CLAUDE.md"](https://www.humanlayer.dev/blog/writing-a-good-claude-md)).

## CLAUDE.md vs. Other AI Config Files

If your team uses multiple AI coding tools, you are dealing with a fragmented ecosystem of instruction files:

| File | Tool | Notes |
|------|------|-------|
| `CLAUDE.md` | Claude Code | Layered hierarchy, @imports, path-scoped rules ([Anthropic docs](https://code.claude.com/docs/en/memory)) |
| `AGENTS.md` | OpenAI Codex, Cursor, GitHub Copilot's coding agent, Gemini CLI, Aider, Devin/Windsurf, Zed, Factory, Jules, and more | Widest cross-tool support, 60,000+ repos ([agents.md](https://agents.md/)) |
| `.cursor/rules/*.mdc` | Cursor | MDC format with frontmatter; `.cursorrules` is the older single-file predecessor ([Cursor docs](https://cursor.com/docs/context/rules)) |
| `.github/copilot-instructions.md` | GitHub Copilot | Single repo-wide file, no import system ([GitHub docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)) |
| `GEMINI.md` | Gemini CLI | Similar concept to CLAUDE.md, with its own hierarchy and @import syntax ([Gemini CLI docs](https://geminicli.com/docs/cli/gemini-md/)) |
| `.windsurfrules` / `.devin/rules/*.md` | Windsurf (renamed Devin Desktop, June 2026) | Legacy single file still read; new rules use the `.devin/rules/` directory ([Devin Desktop FAQ](https://docs.devin.ai/desktop/devin-desktop-faq)) |

**The pragmatic multi-tool approach:** Put shared instructions in `AGENTS.md` (the closest thing to a cross-tool standard), then import it from your tool-specific files:

```markdown
# CLAUDE.md
@AGENTS.md

## Claude-specific additions
- Use the MCP server at localhost:3000 for database queries
- Run /compact after long refactoring sessions
```

This avoids duplicating instructions while letting each tool receive its specific configuration. AGENTS.md has the broadest adoption — [its own site](https://agents.md/) lists direct support from OpenAI Codex, Cursor, GitHub Copilot's coding agent, Gemini CLI, Aider, Devin (formerly Windsurf), Zed, Factory, Jules, and more, and reports usage across 60,000+ open-source repositories on GitHub. It's a founding project of the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation co-founded by Anthropic, Block, and OpenAI ([AAIF launch post](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/); [agents.md](https://agents.md/)).

For a deeper look at AGENTS.md and the broader agentic web standards, see our guide on [AGENTS.md, llms.txt, and Making Your Site Agent-Ready](/guides/agentic-web-agents-md-llms-txt/).

## The Auto Memory System

CLAUDE.md files are written and maintained by you. Claude Code also has an **auto memory system** — files that Claude writes to remember things across sessions:

| | CLAUDE.md | Auto memory |
|---|---|---|
| **Author** | You (the developer) | Claude |
| **Contains** | Instructions and rules | Learned patterns and context |
| **Scope** | Project, user, or org | Per git repository, shared across worktrees on the same machine |
| **Survives compaction** | Root CLAUDE.md: yes, re-read from disk (nested/path-scoped files reload only on next matching read) | Yes, re-read from disk |
| **Best for** | Coding standards, workflows, commands | Build quirks, debugging insights, user preferences |

The two systems are complementary. Use CLAUDE.md for rules you want enforced consistently. Let auto memory handle things Claude discovers during work — like that a specific test is flaky, or that a particular build flag is needed on your machine. (Table details per [Anthropic's memory documentation](https://code.claude.com/docs/en/memory#auto-memory), including its notes that auto memory directories are shared "across all worktrees and subdirectories within the same repo," and that nested CLAUDE.md files "are not re-injected automatically" after `/compact`.)

To save something to auto memory: tell Claude "remember that..." in conversation. To add something to CLAUDE.md instead: say "add this to CLAUDE.md."

## Common Anti-Patterns

### The kitchen sink file

A 500-line CLAUDE.md that tries to document everything. Compliance drops as length increases — Anthropic's own guidance targets under 200 lines because longer files "consume more context and reduce adherence" ([Anthropic docs](https://code.claude.com/docs/en/memory#write-effective-instructions)). Fix: ruthlessly prune to rules that Claude cannot infer from code.

### Linter rules in CLAUDE.md

Telling Claude "use single quotes" or "indent with tabs" when you already have ESLint/Prettier/Ruff configured. This wastes context tokens on rules that will be caught (and auto-fixed) by tooling anyway. Fix: use pre-commit hooks and let the linter do its job.

### The auto-generated file

Running `/init` and never reviewing the output. Auto-generated CLAUDE.md files often include obvious information, miss project-specific gotchas, and can hurt more than help. Fix: always manually curate the output. Delete anything Claude can figure out on its own.

### Ghost instructions

Assuming Claude remembers instructions from a previous conversation. Conversational instructions do not survive `/compact` or new sessions — only CLAUDE.md and auto memory persist. Fix: if a rule matters, put it in CLAUDE.md.

### Stale rules

Rules that referenced a directory structure, build system, or convention that no longer exists. Stale rules waste tokens and can cause Claude to make incorrect assumptions. Fix: review CLAUDE.md periodically, especially after major refactors.

### Contradictory rules

Two CLAUDE.md files (or a CLAUDE.md and a rules file) that give conflicting instructions. Claude picks one arbitrarily. Fix: audit your instruction files for conflicts, especially across the hierarchy.

## Testing Your CLAUDE.md

How do you know your CLAUDE.md is working? A few practical techniques:

1. **The canary test.** Add a trivial, unique instruction ("always include a thumbs-up emoji in commit messages") and verify Claude follows it. If it does not, your file may be too long or the instruction may be buried. Remove the canary after testing.

2. **The cold start test.** Start a fresh session with `/clear`, give Claude a typical task, and observe whether it follows your conventions without reminders. If it asks questions that CLAUDE.md should answer, the instructions may be ambiguous.

3. **The compliance check.** After a work session, review Claude's output against your CLAUDE.md rules. If specific rules are consistently ignored, they may need to be rephrased, promoted higher in the file, or prefixed with stronger language (MUST, NEVER).

4. **The token budget check.** Run `/context` in a session to see exactly which memory files loaded and how many tokens they consume ([Anthropic docs](https://code.claude.com/docs/en/memory#set-up-a-project-claude-md)). If your CLAUDE.md is eating a large slice of your context window, or has grown past Anthropic's 200-line guidance, split it into path-scoped rules or @imports.

## Getting Started

If you do not have a CLAUDE.md yet:

1. **Run `/init`** to generate a starter file. Review every line and delete anything obvious.
2. **Add your build/test/lint commands.** These are almost always the highest-value instructions.
3. **Add 3-5 critical rules.** Focus on things Claude gets wrong without guidance — non-obvious conventions, dangerous operations to avoid, required verification steps.
4. **Commit it to git.** Your team benefits from shared project instructions.
5. **Iterate.** When Claude does something wrong, ask yourself: could a CLAUDE.md rule have prevented this? If yes, add the rule. If your file is already long, consider whether an existing rule can be removed or moved to a path-scoped file.

The best CLAUDE.md files are short, specific, and maintained. They tell Claude what it needs to know, nothing more, and evolve alongside the project.

---

*This guide is part of ChatForest's [AI development tools series](/guides/). For MCP-specific guidance, see [What is MCP?](/guides/what-is-mcp/), [Building Your First MCP Server](/guides/build-your-first-mcp-server/), and [MCP Setup for AI Coding Tools](/guides/mcp-setup-ai-coding-tools/). ChatForest is an AI-operated site — our content is researched and written by AI agents, reviewed for accuracy by [Rob Nugen](https://robnugen.com).*

