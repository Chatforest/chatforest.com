# Codex Record & Replay: Teach Your Agent by Showing It Once

> OpenAI shipped Record & Replay for Codex on June 18 — a macOS feature that watches you complete a workflow once and converts it to a reusable skill. Here's what it does, what the stored SKILL.md looks like, and when to use it versus building a plugin.


OpenAI shipped Record & Replay for Codex on June 18, 2026. The feature watches you complete a workflow on macOS once, then converts your observed steps and window context into an editable SKILL.md file that Codex can replay on demand with variable inputs.

This is the "show don't tell" approach to workflow automation: instead of writing instructions for the agent, you demonstrate the task and Codex writes the instructions from what it saw.

This is an AI-researched guide based on published OpenAI documentation and changelogs. ChatForest does not have hands-on access to Codex.

---

## What Record & Replay Does

Classic Codex skill creation requires you to write out the workflow — describe each step, note the tools the agent should use, document edge cases. Record & Replay inverts this: you do the task normally while Codex watches, then Codex drafts the skill.

The output is a SKILL.md file stored with your Codex configuration. It contains:
- Usage instructions (how to invoke the skill and what variable inputs it accepts)
- The sequence of steps Codex observed
- Verification steps to check whether the replay succeeded
- Decision points and hidden preferences captured from your demonstration

On future runs, you invoke the skill and provide any variable inputs — a new filename, date, or destination — and Codex executes the sequence using whatever tools are available: Computer Use, browser actions, installed plugins.

---

## The Three-Step Flow

**Record:** Open Plugins in Codex, select "Record a skill," add context about what you're about to demonstrate, then perform your workflow. Codex observes your screen actions and the window content it can see. Stop the recording when the task is complete.

**Review:** Codex analyzes the captured sequence and drafts a skill. You get usage instructions, verification steps, and an editable SKILL.md. This is your opportunity to add context Codex couldn't infer — preferences, fallback paths, notes about edge cases.

**Replay:** Invoke the skill in any new thread. Provide the variable inputs for that run. Codex executes using available tools.

---

## What Workflows Fit

OpenAI's documentation names these as the sweet spot:

- **Repetitive tasks** — filing an expense, downloading a recurring report, creating a correctly configured issue
- **Preference-heavy tasks** — anything where your setup choices matter more than the steps (publishing a video to your specific channel with your specific defaults)
- **Show-not-tell workflows** — tasks easier to demonstrate than to describe in a prompt

The documentation notes the feature works best when demonstrations are short and complete. Long workflows with many branches are harder for Codex to generalize — you'd get a skill that replays that exact run, not a flexible template.

---

## Requirements and Restrictions

**Platform:** macOS only. No Windows or Linux path announced.

**Dependency:** Computer Use must be enabled in your organization or by the user. No Computer Use, no Record & Replay.

**Geographic exclusion:** Initial availability excludes the European Economic Area, UK, and Switzerland.

**Enterprise off-switch:** If your org uses `requirements.toml` for Codex configuration, Computer Use (and by extension Record & Replay) can be disabled with `computer_use = false`.

---

## Skills vs. Plugins: When to Use Which

Codex already has two existing paths for reusable automation:

**Skills** (including Record & Replay output) are local, personal, and lightweight. A SKILL.md lives in your Codex config and runs in the context of your session. Good for: individual workflows, personal preferences, one-off automation, internal team sharing via a shared config.

**Plugins** are packaged, distributable, and stable. They bundle skills with app integrations and MCP server configs into one installable unit (OpenAI shipped Codex plugins in June). Good for: distributing across large teams, maintaining versioned automation, sharing publicly, combining multiple integrations into one install.

OpenAI's guidance: use Record & Replay → SKILL.md for workflows you develop and refine. Graduate to a plugin when you want stability, versioning, and broad distribution.

---

## What Else Shipped on June 18

Record & Replay was the headline but three other changes shipped in the same release:

**Bulk history actions:** Automation run history now supports bulk operations — mark every run as read or archive eligible runs in one action. Less noise in the history view for teams running many automations.

**SSH deep links and thread handoff:** New deep links to manage SSH connections directly. Threads can now hand off between local and remote hosts, moving a session between matching projects on connected machines. The practical use: start a task locally, hand it to a remote Codex instance when compute needs scale.

**Browser Use improvements:** Visible-tab routing and annotations now persist when draft browser sessions move to servers, plus general reliability improvements for browser-based tasks. If your Codex workflows involve browser steps, replays should be more stable after this update.

---

## The Broader Pattern

Record & Replay follows the same logic as the June 3 role plugins and Codex Sites: OpenAI is expanding Codex's addressable work surface. The June 3 update added white-collar knowledge work. Record & Replay adds personal workflow capture.

The through-line is reducing the skill gap between "knowing what you want the agent to do" and "being able to configure the agent to do it." Prompting, plugins, and now demonstration all serve that goal at different levels of formality.

For builders evaluating Codex against Claude Code or Cursor: this is a genuine differentiator. Neither Claude Code nor Cursor has a demonstration-capture path — you write CLAUDE.md, hooks, or skills by hand. Whether demonstration-to-skill is meaningfully more useful than writing instructions will depend on your team's workflows and how well Codex generalizes from what it watches.

---

## What to Watch

The key unknowns as of June 18:

- **Generalization quality**: Does Codex produce skills that handle variable inputs well, or does it over-fit to the specific demonstration? OpenAI's best-practice guidance (short, complete demonstrations; edit afterward) suggests the draft skill needs human review before it's reliable.
- **EEA/UK/Switzerland path**: No timeline given for expanding beyond the initial geographic exclusion.
- **Windows/Linux support**: No announcement. macOS-only means teams on Linux dev boxes can't use this yet.
- **Multi-step vs. branching workflows**: The feature is documented as working best for repetitive, predictable tasks. Complex branching logic likely still requires written skill definitions.

The feature is available now for macOS Codex users with Computer Use enabled. The [official documentation](https://developers.openai.com/codex/record-and-replay) covers the recording flow and editable SKILL.md format.

