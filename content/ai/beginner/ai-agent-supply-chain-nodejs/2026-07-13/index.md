---
title: "AI Agent Supply Chain Verification — Node.js/npm, Explained for Beginners (as of 13 Jul 2026)"
date: 2026-07-13
snapshot_date: 2026-07-13
topic: ai-agent-supply-chain-nodejs
track: beginner
audience: "people new to AI"
description: "A plain-English guide to keeping the packages your AI agent depends on safe — covering lockfiles, audits, behavioral scanners, provenance, typosquats, MCP server pinning, private registries, and safer package managers."
content_type: "Best Practice"
categories: ["Node.js", "npm", "AI Agents", "MCP", "Supply Chain Security"]
tags: ["supply-chain", "npm", "nodejs", "mcp", "provenance", "lockfile", "typosquatting", "snyk", "socket-dev", "pnpm"]
last_refreshed: 2026-07-13
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-13"
grading_result: "0 fabrications; 14 corrections applied; 0 gaps filed as project-33 issues"
---

<!-- Immutable dated snapshot. content/ai/beginner/ai-agent-supply-chain-nodejs/2026-07-13/index.md -->

# AI Agent Supply Chain Verification — Node.js/npm, Explained for Beginners (as of 13 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **13 Jul 2026**, frozen here and kept as a
> permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## What this is about (read this first)

When you build an AI agent — a program that talks to an AI model and does things on your behalf — you almost always use helper code written by other people. In Node.js (a popular way to run JavaScript programs on your computer), that helper code comes in bundles called **packages**, and they are downloaded and managed by a tool called **npm** (Node Package Manager).

The packages themselves are not magic: they are code that runs on your machine with your permissions. If any one of them is replaced by a fake or tampered version, that fake code can steal your API keys, read your files, or send your emails to an attacker — all silently, before your AI agent ever starts working.

Real attacks on AI developers have already happened. The practices below are the concrete steps that protect you. None of them require deep expertise. Each section explains what to do, what goes wrong if you skip it, and why it matters.

---

## A few terms explained

- **npm** — Node Package Manager. The tool that downloads packages when you run commands like `npm install`. It also maintains a public registry of hundreds of thousands of packages.
- **pnpm** — An alternative to npm that installs packages faster and with stricter safety defaults. Pronounced "performant npm."
- **Yarn Berry** — Another alternative package manager to npm, made by Meta. "Berry" is the modern version (v2 and later).
- **Bun** — A newer, very fast alternative runtime and package manager for JavaScript, made to be a drop-in replacement for Node.js and npm.
- **MCP server** — A plug-in that gives your AI agent a new capability (tool). MCP stands for Model Context Protocol. An MCP server is a small program that your AI agent launches and talks to; for example, one that lets the agent read and write files on your computer. Because MCP servers run as programs on your machine, a fake one can do anything you can do.
- **CI/CD** — Continuous Integration / Continuous Delivery. Automated systems that build, test, and deploy your code every time you make a change. Think of it as a robot that checks your work.
- **lockfile** — A file that records the exact version and a fingerprint (called an integrity hash) of every package your project uses. Its job is to make sure everyone — and every automated system — installs the exact same code.
- **SLSA** — Supply-chain Levels for Software Artifacts (pronounced "salsa"). A framework of security levels that describes how verifiable a software build process is.
- **OIDC** — A short-lived identity token issued by a trusted platform (like GitHub Actions) that proves "this build really ran here."
- **Sigstore** — An open-source system for signing software so you can prove who built it and from what source code.
- **Rekor** — A public, append-only audit log (part of Sigstore) where software signatures are recorded permanently.

---

## How to read the labels

- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: Commit your lockfile and use `npm ci` (not `npm install`) in every automated build

**Do:** When you start a project, your package manager creates a lockfile. Keep that file and add it to version control (Git). The lockfile is named differently depending on your tool:

- npm creates `package-lock.json`
- pnpm creates `pnpm-lock.yaml`
- Yarn Berry creates `yarn.lock`
- Bun creates `bun.lockb`

In any automated build — a CI/CD pipeline or a Dockerfile — run `npm ci` instead of `npm install`. If you use pnpm, run `pnpm install --frozen-lockfile`.

A complete example for npm in a CI step:
```
npm ci
```

**Why (beginner):** `npm install` re-checks the internet every time and can quietly download a newer version of a package, even one that was just replaced by an attacker. `npm ci` reads the lockfile instead. It installs exactly the versions recorded there, checks each one against its stored fingerprint (SHA-512 integrity hash), and stops with an error if anything does not match. The difference is: `npm install` says "give me something that fits," and `npm ci` says "give me exactly what I recorded, or stop."

**What goes wrong if you skip this:** A malicious package version is slipped in between your test run and your production deploy. Nothing warns you. Your AI agent runs with attacker-controlled code.

**Caveat / contested:** `npm ci` deletes and reinstalls all packages on every run, which is slower. Speed this up by caching the packages folder in CI, keyed to the lockfile. Also, if you use pnpm and the version of pnpm running in CI differs from the version that created the lockfile, `--frozen-lockfile` may error even when nothing is wrong — pin your pnpm version in CI as well.

**Sources:** [the-practical-developer.online — npm Supply Chain Security: Auditing Dependencies](https://the-practical-developer.online/posts/npm-supply-chain-security-audit-ci/) (fetched 2026-07-13) · [armorcode.com — Defending Against NPM Supply Chain Attacks](https://www.armorcode.com/blog/defending-against-npm-supply-chain-attacks-a-practical-guide) (fetched 2026-07-13) · [pkgpulse.com — How to Secure Your npm Supply Chain in 2026](https://www.pkgpulse.com/guides/how-to-secure-npm-supply-chain-2026) (fetched 2026-07-13) · [pnpm.io — pnpm install docs](https://pnpm.io/cli/install) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice 2: Run `npm audit` as a blocking check in every automated build

**Do:** Add this command as a required step in your CI/CD pipeline. It must fail the build if it finds high or critical problems:

```
npm audit --audit-level=high
```

If you use pnpm, the equivalent is:
```
pnpm audit
```

Schedule a full audit to run automatically once a week. If some alerts are genuinely not relevant to your project, create an allowlist with expiration dates — do not silence all alerts at once.

⚠️ **WARNING:** Suppressing `npm audit` output entirely — for example by adding `--no-audit` to your install command, or adding `|| true` after the audit command so it never fails — removes this safety net completely. If the alerts feel noisy, narrow which severity levels block your build by adjusting `--audit-level`. Never just make the errors go away.

**Why (beginner):** npm keeps a database of known security problems in packages. `npm audit` checks your installed packages against that database. If a vulnerability was publicly reported, this command will catch it. Think of it as a spell-checker for known security holes.

**What it cannot do:** `npm audit` only knows about problems that someone has already reported and catalogued. A brand-new malicious package published this morning will not be in the database yet. That gap is addressed by the behavioral scanner in Practice 3.

**Sources:** [the-practical-developer.online — npm Supply Chain Security: Auditing Dependencies](https://the-practical-developer.online/posts/npm-supply-chain-security-audit-ci/) (fetched 2026-07-13) · [anavem.com — How to Audit and Secure npm Dependencies](https://www.anavem.com/en/tutorials/how-to-audit-and-secure-npm-dependencies-against-supply-chain-attacks) (fetched 2026-07-13) · [pkgpulse.com — How to Secure Your npm Supply Chain in 2026](https://www.pkgpulse.com/guides/how-to-secure-npm-supply-chain-2026) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice 3: Add a behavioral scanner (Socket.dev or Snyk) that checks packages before you install them

**Do:** Install the Socket.dev GitHub app (there is a free tier) or the `socket` command-line tool. Once set up, every time a pull request adds or upgrades a package, Socket.dev automatically analyzes the new package's code before it reaches your machine. Before adding any new dependency locally, you can also run:

```
socket npm install <package-name>
```

Alternatively, integrate Snyk's `snyk test` command as a CI step. Both Socket.dev and Snyk work with pnpm workflows as well as npm.

**Why (beginner):** `npm audit` (Practice 2) is like checking a list of already-caught criminals. A behavioral scanner is like a security guard who watches what the newcomer actually does — looks for suspicious network calls, hidden code, obfuscated strings, new install scripts that weren't there before, and sudden changes in who maintains the package.

This matters because of real attacks. In February 2026, a campaign called SANDWORM_MODE published fake AI tool packages named `claud-code`, `cloude`, and `opencraw` — clearly designed to be mistaken for real tools. These packages contained hidden code that ran at install time to read your API keys from environment variables and `.env` files, and also injected rogue MCP server entries (fake plug-ins) into Claude Desktop, Cursor, VS Code Continue, and Windsurf. Nine different AI providers were targeted. The `npm audit` database had no record of any of these packages when they were published. Socket.dev's behavioral signals caught them.

**What goes wrong if you skip this:** A malicious package is published in the morning; your developer adds it to the project by afternoon; `npm audit` sees nothing wrong because the CVE database hasn't been updated yet. The package runs at install time, steals your API keys, and adds fake AI plug-ins to your editor.

**Caveat / contested:** Behavioral scanners surface false positives. Many legitimate AI SDK packages intentionally access the network or your filesystem — that is their job. Treat a flag as "needs human review," not "auto-blocked." Socket.dev is a commercial product; the free tier has rate limits. 🕒 Verify current pricing and tier limits at [socket.dev/pricing](https://socket.dev/pricing).

**Sources:** [docs.socket.dev — Supply Chain Risk signals](https://docs.socket.dev/docs/supply-chain-risk) (fetched 2026-07-13) · [socket.dev — SANDWORM_MODE: npm Worm AI Toolchain Poisoning](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning) (fetched 2026-07-13) · [snyk.io — Detect and Prevent Dependency Confusion Attacks on npm](https://snyk.io/blog/detect-prevent-dependency-confusion-attacks-npm-supply-chain-security/) (fetched 2026-07-13) · [anavem.com — How to Audit and Secure npm Dependencies](https://www.anavem.com/en/tutorials/how-to-audit-and-secure-npm-dependencies-against-supply-chain-attacks) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice 4: Verify npm package provenance with `npm audit signatures`

**Do:** After installing your dependencies, run:

```
npm audit signatures
```

This requires npm version 9.5.0 or later. The current release of npm is 11.17.0 as of mid-2026. 🕒 Verify the current version before relying on this.

When you publish your own packages, use npm's Trusted Publishing feature with GitHub Actions or GitLab CI/CD. This automatically generates provenance (a signed receipt of where and how the package was built) at SLSA Build Level 2. If you publish from CircleCI instead, provenance is NOT generated automatically — you must add the `--provenance` flag yourself. When using `--provenance` manually on GitHub Actions, also add `permissions: id-token: write` to your workflow and make sure you are running on GitHub-hosted runners.

Before adding a critical dependency, visit its page on npmjs.com and look for a provenance badge.

⚠️ **WARNING:** A provenance badge proves where and how a package was built. It does NOT prove that the source code itself is safe. If the repository that built the package was already compromised before the build ran, the provenance will still be valid. Provenance is one important layer — not the whole answer.

**Why (beginner):** Imagine you order a product and receive a certificate saying "this was made in factory X, by worker Y, at 3pm on this date." That is what npm provenance does for a package. It creates a cryptographically signed link between the package file you downloaded and the exact source code commit and CI workflow that produced it. The signature is created using Sigstore's Fulcio CA (a certificate authority for software) and an OIDC identity token from the build platform, then permanently recorded in Rekor (a public, append-only audit log). If someone swapped the real package for a fake at the registry level, `npm audit signatures` will detect that the signature does not match.

**What goes wrong if you skip this:** A registry-level substitution attack replaces a legitimate package with a tampered one. Without provenance verification, you install and run it with no warning.

**Caveat / contested:** Many packages in the npm ecosystem do not yet publish with provenance. Not having a badge is not automatically suspicious — the practice is still being adopted. But when a badge is present, it is a meaningful sign of supply chain care. 🕒 Adoption numbers change; verify live.

**Sources:** [docs.npmjs.com — Generating provenance statements](https://docs.npmjs.com/generating-provenance-statements/) (fetched 2026-07-13) · [docs.npmjs.com — Viewing package provenance](https://docs.npmjs.com/viewing-package-provenance/) (fetched 2026-07-13) · [docs.npmjs.com — Trusted publishers](https://docs.npmjs.com/trusted-publishers/) (fetched 2026-07-13) · [github.blog — Introducing npm package provenance](https://github.blog/security/supply-chain-security/introducing-npm-package-provenance/) (fetched 2026-07-13) · [mondoo.com — npm Supply Chain Security: Package Manager Defenses 2026](https://mondoo.com/blog/npm-supply-chain-security-package-manager-defenses-2026) (fetched 2026-07-13)

**Confidence:** 📄 vendor-documented (npm official docs corroborated by GitHub Blog and Mondoo analysis; SLSA Build Level 2 attribution confirmed by mondoo.com and docs.npmjs.com)

---

## Practice 5: Always check the exact package name against official docs before installing any AI package

**Do:** Before adding any AI SDK or MCP server package (a plug-in that gives your AI agent a new tool), look up the exact package name in the vendor's official documentation. Do not search npm and install the first result. Start from the vendor's own getting-started page.

The confirmed correct npm package names for the major AI libraries are:

- `openai` — OpenAI's official SDK
- `@anthropic-ai/sdk` — Anthropic's official SDK
- `@modelcontextprotocol/sdk` — the official MCP (Model Context Protocol) SDK
- `@modelcontextprotocol/server-*` — official MCP reference servers (made by the Agentic AI Foundation)
- `langchain` and `@langchain/*` — LangChain's packages

⚠️ **WARNING:** Install-time scripts (called lifecycle scripts — small programs that run automatically the moment `npm install` finishes downloading a package) execute before your own code ever runs. A malicious package can steal your API keys the instant you install it, before you have even started your AI agent. To block all lifecycle scripts persistently across every install, add this line to your `.npmrc` file (a configuration file in your project's root folder):

```
ignore-scripts=true
```

Adding `--ignore-scripts` only to a single `npm install` command is not enough — one missed install leaves the door open. Putting it in `.npmrc` makes it the default for every install in that project. Packages that legitimately need lifecycle scripts (some native modules do) must then be allowed individually.

**Why (beginner):** Attackers deliberately choose package names that look like the real thing. In February 2026, the SANDWORM_MODE campaign published `claud-code`, `cloude`, `cloude-code`, and `opencraw` — names that look like common typos of real AI tool names. When installed, these packages ran scripts at install time that stole API keys and injected fake MCP servers (fake AI agent plug-ins) into popular coding tools.

**What goes wrong if you skip this:** You search for "claude sdk" on npm, install the first result (a fake), and it reads your API keys before you notice anything is wrong. Because it also adds a fake MCP server to your editor's configuration, every future AI session may be monitored or manipulated.

**Caveat / contested:** Checking package names protects against fakes. It does not protect you if the real, legitimate package is taken over by an attacker. Combine this with behavioral scanning (Practice 3).

**Sources:** [socket.dev — SANDWORM_MODE: npm Worm AI Toolchain Poisoning](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning) (fetched 2026-07-13) · [toolradar.com — MCP Server Security Best Practices](https://toolradar.com/blog/mcp-server-security-best-practices) (fetched 2026-07-13) · [mondoo.com — npm Supply Chain Security: Package Manager Defenses 2026](https://mondoo.com/blog/npm-supply-chain-security-package-manager-defenses-2026) (fetched 2026-07-13) · [csoonline.com — From typos to takeovers: Inside the industrialization of npm supply chain attacks](https://www.csoonline.com/article/4117139/from-typos-to-takeovers-inside-the-industrialization-of-npm-supply-chain-attacks.html) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice 6: Pin MCP server packages to exact versions — never use bare `npx -y <package>` without a version number

**Do:** An MCP server is a plug-in program that your AI agent launches each time it starts, giving the agent a new capability. Many MCP servers are launched using `npx`, a tool that downloads and runs an npm package on the fly.

In your AI tool's configuration file (for Claude Desktop, Cursor, or any MCP host), always include an exact version number when specifying an MCP server:

```json
"args": ["-y", "@modelcontextprotocol/server-filesystem@<version>"]
```

Replace `<version>` with the current stable release. 🕒 Look up the current version on npmjs.com (search `@modelcontextprotocol/server-filesystem`) before using — do not copy a version from a blog post or older guide.

Before installing any MCP server package, inspect it first:

```
npm pack <package-name>
```

This downloads the package as a compressed file without running it, so you can look inside for unexpected `postinstall` scripts before they can execute.

**Why the `-y` flag is safe only with a version pin — and dangerous without one:**

`npx -y <package>` (without a version number) tells npm: "download whatever the latest version of this package is right now, and run it — without asking me to confirm." Every time your AI agent restarts, it silently fetches whatever the current "latest" version is. If an attacker publishes a malicious new version, your agent will run it the next time it starts up, with no warning.

The recommended form — `npx -y @package@<version>` (with the `@<version>` pin) — is safe because the exact version anchor specifies precisely which code will run. The `-y` flag here just skips a confirmation prompt for that specific, locked version. Remove the version pin and `-y` becomes a silent auto-updater: convenient for attackers, dangerous for you.

⚠️ **WARNING:** Every MCP server in your AI agent's configuration must have an exact version number pinned. Even pinned versions need monitoring — check for security reports and review the changelog before bumping to a newer version.

**Why (beginner):** MCP servers run with the same privileges as the program that launched them — typically full access to your filesystem and network. In 2026, a package called "Postmark MCP server" published 15 clean versions to build trust, then version 1.0.16 silently copied (BCC'd) every outgoing email to an attacker. Nobody noticed until analysis of the new version. Pinning means you choose when to update and can review what changed first.

**What goes wrong if you skip this:** Your AI agent restarts on Monday morning and silently downloads a new, malicious version of an MCP server plug-in. It now has full access to your files and network — and you have no idea.

**Sources:** [toolradar.com — MCP Server Security Best Practices](https://toolradar.com/blog/mcp-server-security-best-practices) (fetched 2026-07-13) · [snyk.io — Malicious MCP server on npm: Postmark MCP harvests emails](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/) (fetched 2026-07-13) · [socket.dev — SANDWORM_MODE: npm Worm AI Toolchain Poisoning](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice 7: Use scoped package names for internal packages and configure your private registry to block public fallback

**Do:** If your team builds internal packages (code you write yourselves, not published publicly), give every one a scoped name: `@yourorg/package-name` instead of just `package-name`. Register that `@yourorg` scope on npmjs.com even if you never intend to publish anything publicly — this blocks someone else from claiming the name.

Point your project and CI pipeline to your private registry by adding this to your `.npmrc` file:

```
@yourorg:registry=https://registry.your-private-registry.internal/
```

In your private registry (tools like Verdaccio or Nexus/Artifactory), configure your internal scope with no upstream proxy:

```
proxy: []
```

This means: for packages under `@yourorg`, never go looking on the public npm registry. If an attacker publishes `@yourorg/payment-client` to the public internet, your registry will never touch it.

⚠️ **WARNING:** Simply having a private registry is not enough protection. If a developer's machine or a CI runner is missing the `.npmrc` configuration file, npm silently falls back to downloading from the public `registry.npmjs.org`. That silent fallback is exactly what the attack exploits. Make the presence of `.npmrc` a required check before CI runs, and include it in your base Docker image.

**Why (beginner):** This type of attack is called dependency confusion. The idea: your team has an internal package called `@yourorg/payment-client`. An attacker registers that same name on the public npm registry with a higher version number. If your package manager is configured to check the public registry (which is the npm default), it may download the attacker's version because a higher version number looks like a newer release. Research in 2021 demonstrated this worked against Yelp, Tesla, Apple, Microsoft, and others.

**What goes wrong if you skip this:** Your CI system installs the attacker's impersonation of your own internal package instead of the real one. The impersonation contains malicious code. It runs in your production environment.

**Caveat / contested:** Scoped names only protect packages that have the scope prefix. Unscoped internal packages (without `@yourorg/`) remain vulnerable. If you have any unscoped internal packages, migrate them to scoped names before relying on this defense. Snyk's `snync` tool can scan your codebase for unscoped internal package names that are not yet registered on the public registry.

**Sources:** [snyk.io — Detect and Prevent Dependency Confusion Attacks on npm](https://snyk.io/blog/detect-prevent-dependency-confusion-attacks-npm-supply-chain-security/) (fetched 2026-07-13) · [systemshardening.com — Dependency Confusion Attack Defence](https://www.systemshardening.com/articles/cross-cutting/dependency-confusion-defence/) (fetched 2026-07-13) · [verdaccio.org](https://www.verdaccio.org/) (fetched 2026-07-13) · [pkgpulse.com — How to Secure Your npm Supply Chain in 2026](https://www.pkgpulse.com/guides/how-to-secure-npm-supply-chain-2026) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice 8: Consider pnpm v11 for new AI agent projects — it blocks install scripts by default

**Do:** For brand-new AI agent projects, consider using pnpm (version 11 or later) as your package manager instead of npm.

When you start a new pnpm project, it comes with `strictDepBuilds: true` turned on by default. This means: no package you install is allowed to run lifecycle scripts (automatic programs that run at install time) unless you explicitly say so.

**What are lifecycle scripts?** When npm installs a package, it can also run small programs that the package author included — named things like `postinstall` or `preinstall`. These scripts run automatically, with your permissions, the moment the download finishes. Legitimate uses include compiling native code. Malicious uses include stealing your API keys. By default, npm runs all of them without asking. pnpm v11 blocks them all unless you add the package to an allowlist.

When a package you trust legitimately needs to run a build script — for example, `esbuild` or `sharp` (which are real packages that need to compile native code) — you add it to the allowlist in a file called `pnpm-workspace.yaml` in your project root. This is the only supported location for this setting in pnpm v11:

```yaml
# pnpm-workspace.yaml
strictDepBuilds: true
allowBuilds:
  esbuild: true
  sharp: true
```

You can also set a release cooldown. This tells pnpm not to install any package version that was published fewer than N minutes ago. The default is 1440 minutes (one day). For more sensitive environments, consider 10080 minutes (seven days). This is available in npm 11.10.0 or later and in pnpm via `pnpm-workspace.yaml`. 🕒 Verify current release dates before relying on this.

⚠️ **WARNING:** Switching an existing project from npm to pnpm is not a simple swap. pnpm stores packages differently (using symlinks from a central store instead of copying files into each project's `node_modules` folder). Some packages that expect npm's layout will break. Test thoroughly in a separate branch before switching any production AI agent project.

**Why (beginner):** The core problem with npm's default behavior is that it trusts every package to run whatever code it wants at install time. pnpm v11 flips that default: packages are not trusted to run scripts unless you explicitly approve them. This is a much safer starting position — especially for AI agent projects, which use many packages from many sources.

The release cooldown adds another layer: most malicious packages are caught and removed within hours or days of publication. A one-day or seven-day delay means you are unlikely to install a package during its "active malicious" window.

**What goes wrong if you skip this:** A package you install runs a `postinstall` script that reads your `.env` file (which contains your API keys) and sends the contents to an attacker. This happens silently during `npm install`. You see no error. Your AI agent starts normally. You only discover the problem when you get billed for API usage you did not make.

**Caveat / contested:** With `strictDepBuilds: true`, packages that legitimately need build scripts will fail to install until you add them to `allowBuilds`. If your project uses many native modules (GPU libraries, database drivers), budget time to build that list correctly.

**Sources:** [mondoo.com — npm Supply Chain Security: Package Manager Defenses 2026](https://mondoo.com/blog/npm-supply-chain-security-package-manager-defenses-2026) (fetched 2026-07-13) · [armorcode.com — Defending Against NPM Supply Chain Attacks](https://www.armorcode.com/blog/defending-against-npm-supply-chain-attacks-a-practical-guide) (fetched 2026-07-13) · [pnpm.io/settings](https://pnpm.io/settings) (fetched 2026-07-13) · [socket.dev — npm introduces minimumReleaseAge](https://socket.dev/blog/npm-introduces-minimumreleaseage-and-bulk-oidc-configuration) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice 9: Check lockfile integrity hashes and block non-registry dependency sources in automated builds

**Do:** Add a step near the start of your CI pipeline that checks three things:

1. Your `package-lock.json` file exists and is committed to the repository.
2. Every package entry in the lockfile has a `integrity` field (a SHA-512 fingerprint).
3. No dependency points to a `git+`, `github:`, or `file:` address instead of the official npm registry.

For npm, running `npm ci --audit` handles the first two automatically. The third check — blocking non-registry sources — requires a separate policy step or linting of the lockfile.

For pnpm, `pnpm install --frozen-lockfile` handles the lockfile consistency check; add a separate policy check for non-registry sources.

**Why (beginner):** Normally, packages are downloaded from the npm registry, which keeps records of every version and its fingerprint. A `git:` or `github:` dependency bypasses the registry entirely. It pulls code directly from a Git repository. That code has no fingerprint, is not logged in any transparency system, and can change without any version number changing. If an attacker compromises the GitHub repository being referenced, your next build silently runs their code — and your lockfile shows no change at all.

**What goes wrong if you skip this:** A developer adds a dependency on a GitHub repository fork while testing something. The fork is later compromised. Every build after that installs and runs the attacker's code. Nothing in `npm audit` or the lockfile flags a problem because there is no version to audit.

**Caveat / contested:** Some legitimate development workflows — for example, testing a local fix to `@modelcontextprotocol/sdk` before the official patch is released — intentionally use `file:` or `git:` references. The policy here should block these in your production CI pipeline, while allowing a documented exception process for development branches.

**Sources:** [the-practical-developer.online — npm Supply Chain Security: Auditing Dependencies](https://the-practical-developer.online/posts/npm-supply-chain-security-audit-ci/) (fetched 2026-07-13) · [endorlabs.com — How to Defend Against NPM Software Supply Chain Attacks](https://www.endorlabs.com/learn/how-to-defend-against-npm-software-supply-chain-attacks) (fetched 2026-07-13) · [systemshardening.com — Dependency Confusion Attack Defence](https://www.systemshardening.com/articles/cross-cutting/dependency-confusion-defence/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## CHANGELOG

- Re-leveled from technical entry (snapshot_date: 2026-07-13) by rings-beginner-author. Facts, commands, warnings, sources, and confidence labels are unchanged from the graded technical entry. Changes made: track set to beginner; audience set to "people new to AI"; title rephrased for novices; added plain-English glossary of terms (npm, pnpm, Yarn Berry, Bun, MCP server, CI/CD, lockfile, SLSA, OIDC, Sigstore, Rekor); expanded "Why" sections with concrete failure scenarios; added explicit "What goes wrong if you skip this" for every practice; clarified the lifecycle scripts concept and why blocking them by default matters (Practice 8); clarified why `-y` in `npx -y @package@<version>` is safe with a version pin but dangerous without one (Practice 6); all warnings moved to be prominent; all 9 practices from the technical entry are kept — none dropped.
- Link-check gate (2026-07-14): socket.dev/ (homepage) replaced with socket.dev/pricing (200). npmjs.com/org/modelcontextprotocol unlinked to plain text (403, bot-protection). Citations retained.
