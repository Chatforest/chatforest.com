# AI Agent Supply Chain Verification — Node.js/npm (as of 13 Jul 2026)

> How to verify the integrity and provenance of Node.js/npm packages used in AI agent pipelines and MCP servers, covering lockfiles, provenance attestations, behavioral scanning, and private registries.


<!-- Immutable dated snapshot. content/ai/best-practices/ai-agent-supply-chain-nodejs/2026-07-13/index.md -->

# AI Agent Supply Chain Verification — Node.js/npm (as of 13 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **13 Jul 2026**, frozen here and kept as a
> permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

AI agent pipelines increasingly depend on npm packages (SDKs for OpenAI, Anthropic, LangChain, and the Model Context Protocol) that are actively targeted by typosquatting campaigns, dependency confusion attacks, and malicious install-script injections. Verifying that the packages you install are what they claim to be — built from the source they claim, by the maintainer they claim — is now a basic operational hygiene step, not an advanced hardening measure. This entry covers the concrete practices that make up a layered defense for Node.js/npm-based AI agent projects.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Commit your lockfile and use `npm ci` (not `npm install`) in every CI/CD and Docker build

**Do:** Commit `package-lock.json` (npm), `pnpm-lock.yaml` (pnpm), `yarn.lock` (Yarn Berry), or `bun.lockb` (Bun) to version control. In CI pipelines and Dockerfiles, run `npm ci` instead of `npm install`. For pnpm, use `pnpm install --frozen-lockfile`.

**Why:** `npm install` re-resolves your dependency tree every time and rewrites the lockfile. If a transitive dependency is silently swapped for a malicious version between your developer's laptop run and the production build, `npm install` will just use the new version. `npm ci`, by contrast, installs exactly the versions recorded in the lockfile, verified against their SHA-512 integrity hashes, and exits with an error if anything is out of sync. It turns "we hope nothing changed" into "we know nothing changed."

**Caveat / contested:** `npm ci` deletes and reinstalls `node_modules` on every run, which can be slow; cache the `node_modules` layer keyed to the lockfile hash in CI to mitigate. Using `--frozen-lockfile` in pnpm has a known inconsistency: if the installed pnpm version differs from the one that generated the lockfile, it may error even when nothing is actually wrong — pin your pnpm version in CI too.

**Sources:** [the-practical-developer.online — npm Supply Chain Security: Auditing Dependencies](https://the-practical-developer.online/posts/npm-supply-chain-security-audit-ci/) (fetched 2026-07-13) · [armorcode.com — Defending Against NPM Supply Chain Attacks](https://www.armorcode.com/blog/defending-against-npm-supply-chain-attacks-a-practical-guide) (fetched 2026-07-13) · [pkgpulse.com — How to Secure Your npm Supply Chain in 2026](https://www.pkgpulse.com/guides/how-to-secure-npm-supply-chain-2026) (fetched 2026-07-13) · [pnpm.io — pnpm install docs](https://pnpm.io/cli/install) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice: Run `npm audit --audit-level=high` as a blocking CI gate

**Do:** Add `npm audit --audit-level=high` (or `pnpm audit`) as a required step in CI that fails the build on high or critical vulnerabilities. Schedule weekly full audits. Create an allowlist with expiration dates to suppress false positives so the gate doesn't get bypassed wholesale.

**Why:** `npm audit` cross-references your installed packages against the npm Advisory Database (which includes NVD CVE data). It catches known exploitable vulnerabilities that have already been disclosed. `npm audit` cannot catch zero-day malicious publishes or obfuscated install scripts — that is why it is a floor, not a ceiling.

⚠️ **WARNING:** Suppressing `npm audit` output entirely (e.g., with `--no-audit` or `|| true`) to silence noise removes this safety net altogether. If alerts are too noisy, tighten the `--audit-level` threshold instead.

**Caveat / contested:** The audit database has a lag: a malicious package may be active for hours or days before a CVE is filed. Behavioral scanning tools (see Socket.dev practice below) exist precisely to fill this gap.

**Sources:** [the-practical-developer.online — npm Supply Chain Security: Auditing Dependencies](https://the-practical-developer.online/posts/npm-supply-chain-security-audit-ci/) (fetched 2026-07-13) · [anavem.com — How to Audit and Secure npm Dependencies](https://www.anavem.com/en/tutorials/how-to-audit-and-secure-npm-dependencies-against-supply-chain-attacks) (fetched 2026-07-13) · [pkgpulse.com — How to Secure Your npm Supply Chain in 2026](https://www.pkgpulse.com/guides/how-to-secure-npm-supply-chain-2026) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice: Add a behavioral scanner (Socket.dev or Snyk) that checks packages before or at install time

**Do:** Install the Socket.dev GitHub app (free tier available) or `socket` CLI so that every pull request that adds or upgrades a dependency triggers a pre-install behavioral analysis. Alternatively, integrate Snyk's `snyk test` step. Use `socket npm install <package>` locally before adding a new dependency. For pnpm users, Socket integrates with the pnpm workflow as well.

**Why:** `npm audit` only catches vulnerabilities that have already been documented. Socket.dev analyzes 70+ signals — new install scripts, suspicious network calls, obfuscated code, sudden maintainer changes, high-entropy strings — in the package's actual code, and flags them within minutes of publication. This is how the SANDWORM_MODE campaign (February 2026) targeting AI developer tools (`claud-code`, `cloude`, `opencraw`) was caught: the packages contained base64-encoded payloads that executed via `eval()` to both directly read environment variables and `.env` files (for API keys) AND inject rogue MCP server entries into Claude Desktop, Cursor, VS Code Continue, and Windsurf configuration files. Nine LLM providers were targeted. CVE databases had no record of these packages at the time of publication.

**Caveat / contested:** Socket.dev's signal-based approach can surface false positives, especially for packages that legitimately access the network or filesystem (many AI SDKs do). Treat flagged packages as requiring human review, not auto-block. Socket is a commercial product; the free tier has rate limits. 🕒 Verify current pricing and tier limits at [socket.dev/pricing](https://socket.dev/pricing).

**Sources:** [docs.socket.dev — Supply Chain Risk signals](https://docs.socket.dev/docs/supply-chain-risk) (fetched 2026-07-13) · [socket.dev — SANDWORM_MODE: npm Worm AI Toolchain Poisoning](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning) (fetched 2026-07-13) · [snyk.io — Detect and Prevent Dependency Confusion Attacks on npm](https://snyk.io/blog/detect-prevent-dependency-confusion-attacks-npm-supply-chain-security/) (fetched 2026-07-13) · [anavem.com — How to Audit and Secure npm Dependencies](https://www.anavem.com/en/tutorials/how-to-audit-and-secure-npm-dependencies-against-supply-chain-attacks) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice: Verify npm package provenance with `npm audit signatures`

**Do:** After installing dependencies, run `npm audit signatures` (requires npm CLI 9.5.0 or later; current release is 11.17.0 as of mid-2026). For packages you publish, use npm Trusted Publishing (OIDC from GitHub Actions or GitLab CI/CD) which automatically generates SLSA Build Level 2 provenance attestations. **Note:** CircleCI Trusted Publishing does NOT automatically generate provenance — if you publish from CircleCI, you must still pass the `--provenance` flag manually. When using the flag manually on GitHub Actions, add `permissions: id-token: write` to your workflow and run on GitHub-hosted runners. Check npmjs.com for the provenance badge on critical dependencies before adding them.

**Why:** npm provenance creates a cryptographically signed, tamper-evident link between a published package tarball and the exact source commit and CI workflow that produced it. The attestation is signed by Sigstore's Fulcio CA using a short-lived OIDC token and logged in Rekor, a public append-only transparency ledger. If a package claims to be version 2.1.0 of `@anthropic-ai/sdk` but was built from a different repository or a tampered commit, `npm audit signatures` will surface the mismatch. This catches registry-level substitution attacks.

⚠️ **WARNING:** Provenance proves *where* and *how* a package was built — it does not verify *what the code does*. A build with valid provenance can still contain malicious logic if the source repository itself was compromised. Provenance is necessary but not sufficient.

**Caveat / contested:** Adoption is uneven across the npm ecosystem; many AI SDK versions do not yet publish with provenance. Absence of a provenance badge is not itself a red flag, but presence is a meaningful signal of supply chain hygiene. 🕒 Adoption numbers change; verify live.

**Sources:** [docs.npmjs.com — Generating provenance statements](https://docs.npmjs.com/generating-provenance-statements/) (fetched 2026-07-13) · [docs.npmjs.com — Viewing package provenance](https://docs.npmjs.com/viewing-package-provenance/) (fetched 2026-07-13) · [docs.npmjs.com — Trusted publishers](https://docs.npmjs.com/trusted-publishers/) (fetched 2026-07-13) · [github.blog — Introducing npm package provenance](https://github.blog/security/supply-chain-security/introducing-npm-package-provenance/) (fetched 2026-07-13) · [mondoo.com — npm Supply Chain Security: Package Manager Defenses 2026](https://mondoo.com/blog/npm-supply-chain-security-package-manager-defenses-2026) (fetched 2026-07-13)

**Confidence:** 📄 vendor-documented (npm official docs corroborated by GitHub Blog and Mondoo analysis; SLSA Build Level 2 attribution confirmed by mondoo.com and docs.npmjs.com)

---

## Practice: Block AI-package typosquats by verifying exact namespace and cross-referencing official documentation before installing

**Do:** Before adding any AI SDK or MCP server package, verify the exact package name against the vendor's official documentation. The canonical npm names for the major AI libraries are: `openai` (OpenAI), `@anthropic-ai/sdk` (Anthropic), `@modelcontextprotocol/sdk` and `@modelcontextprotocol/server-*` (MCP reference servers, Agentic AI Foundation), `langchain` and `@langchain/*` (LangChain). Never search npm and install the first result; always start from the vendor's own getting-started page.

**Why:** Documented campaigns have specifically targeted AI developers. The February 2026 SANDWORM_MODE campaign published packages named `claud-code`, `cloude`, `cloude-code`, and `opencraw` that, when installed, injected rogue MCP server entries into multiple AI coding tools and harvested API keys for nine LLM providers.

⚠️ **WARNING:** Install-script attacks execute *before your code runs*, at `npm install` time. To block lifecycle scripts persistently, add `ignore-scripts=true` to your `.npmrc` file (not just as a per-run flag). This blocks all lifecycle scripts globally; you then allowlist legitimate native packages individually. See also the pnpm v11 practice for a more ergonomic allowlist approach.

**Caveat / contested:** Typosquatting vigilance is necessary but brittle against compromised *legitimate* packages (maintainer account takeover). Combine with behavioral scanning.

**Sources:** [socket.dev — SANDWORM_MODE: npm Worm AI Toolchain Poisoning](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning) (fetched 2026-07-13) · [toolradar.com — MCP Server Security Best Practices](https://toolradar.com/blog/mcp-server-security-best-practices) (fetched 2026-07-13) · [mondoo.com — npm Supply Chain Security: Package Manager Defenses 2026](https://mondoo.com/blog/npm-supply-chain-security-package-manager-defenses-2026) (fetched 2026-07-13) · [csoonline.com — From typos to takeovers: Inside the industrialization of npm supply chain attacks](https://www.csoonline.com/article/4117139/from-typos-to-takeovers-inside-the-industrialization-of-npm-supply-chain-attacks.html) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice: Pin MCP server packages to exact versions; never use bare `npx -y <package>` without a version pin

**Do:** In Claude Desktop, Cursor, or any MCP host's configuration file, always specify an exact version for npx-launched MCP servers:
```json
"args": ["-y", "@modelcontextprotocol/server-filesystem@<version>"]
```
Replace `<version>` with the current stable release from npmjs.com (search `@modelcontextprotocol/server-filesystem`) — 🕒 verify live before using. Do not use `"args": ["-y", "@modelcontextprotocol/server-filesystem"]` (no version pin), which fetches the latest version silently on every agent restart. Before installing any MCP server package, run `npm pack <package-name>` and inspect the tarball for unexpected `postinstall` scripts.

**Why:** MCP servers run with the same privileges as the host process — typically full filesystem and network access. The "Postmark MCP server" npm incident (documented in 2026) published 15 clean versions to build trust, then version 1.0.16 silently BCC'd every outgoing email to an attacker. Pinning means you choose when to update and can review the changelog before doing so.

**The danger of bare `-y`:** `npx -y <package>` without a version pin fetches and runs whatever the latest version is at that moment, with zero verification. The `-y` flag in the safe recommended form above (`-y @package@<version>`) is acceptable *only* because the exact version pin anchors what code will run; without the version pin, `-y` becomes a silent auto-updater.

⚠️ **WARNING:** Every MCP server in your agent configuration should have an exact version pinned. Pinned versions still require you to monitor for CVEs and intentionally review changelogs before bumping.

**Sources:** [toolradar.com — MCP Server Security Best Practices](https://toolradar.com/blog/mcp-server-security-best-practices) (fetched 2026-07-13) · [snyk.io — Malicious MCP server on npm: Postmark MCP harvests emails](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/) (fetched 2026-07-13) · [socket.dev — SANDWORM_MODE: npm Worm AI Toolchain Poisoning](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use scoped internal packages and configure your private registry to block upstream fallthrough

**Do:** Name every internal package under a scoped namespace (`@yourorg/package-name`). Register that scope on npmjs.com even if you never publish publicly (to block name squatting). Point all developers and CI pipelines to your private registry via `.npmrc`:
```
@yourorg:registry=https://registry.your-private-registry.internal/
```
In Verdaccio or Nexus/Artifactory, configure the internal scope with `proxy: []` (no upstream proxy for that scope). This means if an attacker publishes `@yourorg/payment-client` to npmjs.org, your registry will never serve it.

**Why:** Dependency confusion is an attack where an attacker registers a public package whose name matches an internal private package. Alex Birsan's 2021 research demonstrated this against Yelp, Tesla, Apple, Microsoft, and others. If your package manager is configured to prefer the public registry (the npm CLI default), it may install the attacker's version because it has a higher semver number.

⚠️ **WARNING:** Simply *using* a private registry is not enough. If the `.npmrc` file is missing from a developer's machine or a CI runner, npm silently defaults to `registry.npmjs.org` and your scoped packages will resolve from there. Enforce `.npmrc` presence as a CI pre-flight check and bake it into your base Docker image.

**Caveat / contested:** Scoped namespaces only protect packages under that scope. Unscoped internal packages remain vulnerable. Migrate unscoped internal packages to scoped names before relying on this defense. Snyk's `snync` tool can scan your codebase for unscoped internal package names that are not yet claimed on the public registry.

**Sources:** [snyk.io — Detect and Prevent Dependency Confusion Attacks on npm](https://snyk.io/blog/detect-prevent-dependency-confusion-attacks-npm-supply-chain-security/) (fetched 2026-07-13) · [systemshardening.com — Dependency Confusion Attack Defence](https://www.systemshardening.com/articles/cross-cutting/dependency-confusion-defence/) (fetched 2026-07-13) · [verdaccio.org](https://www.verdaccio.org/) (fetched 2026-07-13) · [pkgpulse.com — How to Secure Your npm Supply Chain in 2026](https://www.pkgpulse.com/guides/how-to-secure-npm-supply-chain-2026) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice: Prefer pnpm v11+ for AI agent projects; use its lifecycle script allowlist and release cooldown

**Do:** For new AI agent projects, use pnpm v11 or later as your package manager. Accept the default `strictDepBuilds: true` (lifecycle scripts blocked for all dependencies unless explicitly allowed). When a legitimate package requires a build script (e.g., native modules like `sharp`), add it explicitly to the `allowBuilds` map in **`pnpm-workspace.yaml`** (the only supported config location in pnpm v11 — `.pnpmfile.cjs` does NOT support this setting in v11):

```yaml
# pnpm-workspace.yaml
strictDepBuilds: true
allowBuilds:
  esbuild: true
  sharp: true
```

Accept or increase the default `minimumReleaseAge` of 1440 minutes (one day); consider 10,080 minutes (seven days) for higher-risk environments. This is confirmed available in npm 11.10.0+ (released 2026-02-11); pnpm has an equivalent setting in `pnpm-workspace.yaml`.

**Why:** The npm CLI does not block postinstall/preinstall scripts by default. Any package you install can run arbitrary code on your machine the instant npm finishes downloading it. pnpm v11's `strictDepBuilds: true` default closes this gap: packages can only run install scripts if you have consciously added them to your allowlist. The release cooldown complements this by preventing installation of newly published package versions during the window when malicious publishes are most likely active.

⚠️ **WARNING:** Switching an existing project from npm to pnpm requires careful migration: pnpm uses a different `node_modules` layout (symlinked from a content-addressable store), which can break packages that rely on hoisting undeclared dependencies. Test thoroughly in a branch before migrating a production AI agent project.

**Caveat / contested:** `strictDepBuilds` breaks native packages on first install until you allowlist them. If your project has heavy native module dependencies (GPU libraries, database clients), budget time to build the allowlist correctly.

**Sources:** [mondoo.com — npm Supply Chain Security: Package Manager Defenses 2026](https://mondoo.com/blog/npm-supply-chain-security-package-manager-defenses-2026) (fetched 2026-07-13) · [armorcode.com — Defending Against NPM Supply Chain Attacks](https://www.armorcode.com/blog/defending-against-npm-supply-chain-attacks-a-practical-guide) (fetched 2026-07-13) · [pnpm.io/settings](https://pnpm.io/settings) (fetched 2026-07-13) · [socket.dev — npm introduces minimumReleaseAge](https://socket.dev/blog/npm-introduces-minimumreleaseage-and-bulk-oidc-configuration) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## Practice: Verify lockfile integrity hashes and block git-URL and file-path dependencies in CI policy

**Do:** Add a pre-install CI step that: (1) confirms `package-lock.json` is present, (2) checks that every resolved entry contains a SHA-512 `integrity` field, and (3) rejects any dependency whose `resolved` URL uses a `git+`, `github:`, or `file:` scheme instead of a registry URL. For npm: `npm ci --audit` enforces lockfile consistency. For pnpm: `pnpm install --frozen-lockfile` with a separate policy check.

**Why:** A package resolved from a git URL (`"dependency": "github:user/repo"`) bypasses the npm registry entirely — it does not appear in the transparency log, has no integrity hash, and can change at any time without a version bump. An attacker who compromises a GitHub repository that is imported this way can inject malicious code with no lockfile entry changing.

**Caveat / contested:** Some legitimate development workflows (e.g., testing a local fork of `@modelcontextprotocol/sdk` before a patch is released) intentionally use `file:` or `git:` references. The policy should block these in *production* CI while allowing a documented exception flow for development branches.

**Sources:** [the-practical-developer.online — npm Supply Chain Security: Auditing Dependencies](https://the-practical-developer.online/posts/npm-supply-chain-security-audit-ci/) (fetched 2026-07-13) · [endorlabs.com — How to Defend Against NPM Software Supply Chain Attacks](https://www.endorlabs.com/learn/how-to-defend-against-npm-software-supply-chain-attacks) (fetched 2026-07-13) · [systemshardening.com — Dependency Confusion Attack Defence](https://www.systemshardening.com/articles/cross-cutting/dependency-confusion-defence/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated

---

## CHANGELOG (grading → this entry)
1. Skeptic FIX: Removed "Over 16,000 packages publish with provenance" — no cited source (github.blog, mondoo) states this figure; cut rather than fabricate a citation.
2. Skeptic FIX: Fixed Postmark MCP incident citation — "1.0.16 / 15 clean versions" detail cited to Snyk (primary source) instead of tianpan.co (which did not contain those details).
3. Skeptic FLAG: Changed Birsan dependency confusion target list from "Apple, Microsoft, and PayPal" to "Yelp, Tesla, Apple, Microsoft, and others" to match the cited Snyk blog page.
4. Skeptic FLAG: Clarified SANDWORM_MODE harvesting mechanism — it used BOTH direct env-var/`.env` file reads AND prompt-injected MCP descriptions; previous wording understated the direct-read path.
5. Beginner KILL: Added persistent `.npmrc: ignore-scripts=true` guidance for the lifecycle script block — a per-run `--ignore-scripts` flag is insufficient; one missed install leaves the door open.
6. Beginner KILL: Added explanation for why `-y` in `npx -y @package@<version>` is safe when combined with a pinned version, but dangerous without one — the example code and the WARNING now explicitly distinguish the two cases.
7. Timekeeper KILL: Fixed pnpm v11 `allowBuilds` config location — `pnpm-workspace.yaml` ONLY (not `.pnpmfile.cjs`, which does not support this setting in v11); old settings (`onlyBuiltDependencies`, `neverBuiltDependencies`) were removed in v11 and replaced by `allowBuilds`. Correct YAML syntax shown.
8. Timekeeper KILL: Replaced `@modelcontextprotocol/server-filesystem@2025.11.18` (stale late-2025 version) with `@<version>` placeholder; instructed readers to verify current stable release from npmjs.com.
9. Timekeeper FIX: npm CLI version minimum contextualized — "9.5.0 or later (current release is 11.17.0 as of mid-2026)."
10. Timekeeper FIX: SLSA Build Level 2 for npm provenance stated confidently (confirmed by mondoo.com and npm docs); removed from Held Pending.
11. Timekeeper FIX: `minimumReleaseAge` confirmed as npm 11.10.0+ (released 2026-02-11); `min-release-age-exclude` added in npm 11.17.0. Removed from Held Pending.
12. Timekeeper FLAG: Added CircleCI caveat to Trusted Publishing practice — CircleCI does NOT auto-generate provenance; `--provenance` flag still required there.
13. Link-check gate (2026-07-14): socket.dev/ (homepage) returns 403 to automated curl — replaced with socket.dev/pricing which returns 200. Text and intent preserved.
14. Link-check gate (2026-07-14): npmjs.com/org/modelcontextprotocol returns 403 — unlinked to plain text; changed to "search @modelcontextprotocol/server-filesystem on npmjs.com" instruction. Citation intent preserved.

