---
title: "AI Agent Supply Chain Verification — Cross-Platform (as of 13 Jul 2026)"
date: 2026-07-13
snapshot_date: 2026-07-13
topic: ai-agent-supply-chain-generic
track: best-practices
audience: "technically comfortable readers"
description: "Platform-agnostic practices for verifying the integrity of AI agent supply chains: model weights, containers, CI/CD pipelines, OS packages, and SBOM tooling."
content_type: "Best Practice"
categories: ["AI Security", "Supply Chain", "DevSecOps"]
tags: ["supply-chain", "model-verification", "safetensors", "slsa", "sbom", "cosign", "trivy", "grype", "syft", "air-gap", "github-actions", "dependabot"]
last_refreshed: 2026-07-13
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-13"
grading_result: "0 fabrications; 12 corrections applied; 0 gaps filed as project-33 issues"
---

<!-- Immutable dated snapshot. content/ai/best-practices/ai-agent-supply-chain-generic/2026-07-13/index.md -->

# AI Agent Supply Chain Verification — Cross-Platform (as of 13 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **13 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

AI agents pull in model weights, container images, Python packages, and CI/CD actions from many external sources. Any of those links in the chain can be poisoned — embedding malicious code in a model checkpoint, replacing a legitimate pip package with a lookalike, or hijacking an unpinned GitHub Action. This reference collects platform-agnostic controls a team can apply at each link.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Prefer safetensors format over pickle-based model files

**Do:** When downloading model weights from Hugging Face or any other registry, choose `.safetensors` files over `.bin`, `.pt`, or `.pth` files. If only a pickle-based format is available, scan it with ModelScan or Fickling before loading:

```bash
pip install modelscan
modelscan -p model.pth
```

A "Safe" result from ModelScan means no executable payloads were detected in the known patterns; an "Unsafe" result prints the detected issue and exits non-zero (suitable as a CI gate).

**Why:** Python's pickle format can embed and execute arbitrary code the moment you call `torch.load()`. An attacker who uploads a malicious checkpoint to a public registry can run any shell command on your machine just from you loading the model. SafeTensors stores only raw tensor data in a flat binary layout with a JSON header — there is no mechanism for executable code to hide in that structure. Trail of Bits audited the safetensors specification in March 2023 (commissioned by EleutherAI and Hugging Face) and found no critical security flaws (source: Hugging Face blog, Trail of Bits security review PDF). Researchers have found thousands of malicious checkpoints already on Hugging Face. Note: as of Hugging Face Transformers 5.0.0 (released January 26, 2026), safetensors is the only supported serialization format in that library — `safe_serialization=False` now raises an error; the proportion of models on Hugging Face in pickle format continues to decline. 🕒 verify live for current ecosystem stats.

⚠️ **WARNING — scanner bypass:** ModelScan and PickleScan have known bypass vulnerabilities (crafted payloads can crash the scanner without triggering detection). Treat scanner "all clear" as a raised floor, not a guarantee. 🕒 Verify scanner patch status before relying on them.

**Caveat / contested:** SafeTensors eliminates deserialization code execution, but tensor values themselves can still be tampered with to inject backdoors into model behaviour (data poisoning). Format verification alone is not a complete defence — you still need checksum verification (see next practice).

**Sources:** [dev.to/lukehinds — Understanding SafeTensors](https://dev.to/lukehinds/understanding-safetensors-a-secure-alternative-to-pickle-for-ml-models-o71) (fetched 2026-07-13) · [huggingface.co/blog — SafeTensors security audit](https://huggingface.co/blog/safetensors-security-audit) (fetched 2026-07-13) · [infosec.qa — AI Supply Chain Attacks](https://infosec.qa/blog/ai-supply-chain-attacks/) (fetched 2026-07-13) · [isc.sans.edu — ModelScan diary](https://isc.sans.edu/diary/31692) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (four independent publishers: DEV Community, Hugging Face blog with Trail of Bits audit reference, infosec.qa, SANS ISC)

---

## Practice: Verify SHA-256 checksums for every downloaded model file

**Do:** After downloading any model weight file, compute its SHA-256 hash locally and compare it byte-for-byte against the checksum published by the original source:

```bash
# Linux/macOS
sha256sum model.safetensors

# Windows
certutil -hashfile model.safetensors SHA256
```

On Hugging Face, checksums appear on the "Files and versions" tab. Obtain checksums over HTTPS from a source separate from the download link itself — never from the same page that served the file.

⚠️ **WARNING — dangerous default:** Platforms like Hugging Face do not automatically re-validate cached model files. `hf_hub_download()` checks the server-published checksum at download time, but does not re-check the local cache on subsequent loads — a file corrupted in `~/.cache/huggingface` will pass silently. Build a periodic re-verification step into your deployment workflow.

**Why:** A hash mismatch means the file you received is not the file the publisher intended to share. This catches network corruption, CDN substitution attacks, and modified mirrors.

**Caveat / contested:** If the registry itself is compromised, published checksums may also be updated; treat out-of-band checksum sources (a signed release page, a reproducible build) as stronger evidence than a checksum displayed on the same download page.

**Sources:** [qwe.edu.pl — How to Verify AI Model Downloads](https://www.qwe.edu.pl/tutorial/how-to-verify-ai-model-download/) (fetched 2026-07-13) · [aisecurityandsafety.org — AI Supply Chain Security Guide](https://aisecurityandsafety.org/en/guides/ai-supply-chain-security/) (fetched 2026-07-13) · [infosec.qa — AI Supply Chain Attacks](https://infosec.qa/blog/ai-supply-chain-attacks/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (three independent publishers: QWE Academy, AI Safety Directory, infosec.qa)

---

## Practice: Sign and verify container images with Cosign (Sigstore)

**Do:** Add a Cosign signing step to your CI/CD release workflow. After building an AI workload container, sign it with `cosign sign` using keyless OIDC signing (no long-lived key to manage). In any deployment pipeline that pulls the image, run `cosign verify` against the expected signer identity before allowing the image to run. Attach SLSA provenance and SBOM attestations to the same OCI tag using `cosign attest`.

🕒 **Cosign version:** Current release is v3.1.1 (June 2026). Cosign v3.x deprecated several v2-era flags related to verification material input and bundle format; v4 is expected to remove them. If your CI scripts use `--attachment sig` or other deprecated v2 flags, update before upgrading to v4.

**Why:** A container image without a signature can be silently replaced in a registry (by a compromised registry account, a poisoned cache, or a man-in-the-middle). Cosign's keyless signing ties the signature to an OIDC identity (e.g., a GitHub Actions workload) and records every signature in Sigstore's Rekor append-only transparency log.

**Caveat / contested:** Keyless signing requires an OIDC provider (GitHub Actions, Google Cloud, etc.) in your CI/CD environment. Self-hosted or air-gapped pipelines need extra configuration to reach the Fulcio CA and Rekor log, or to operate a private Sigstore deployment. 🕒 Verify Cosign version compatibility with your OCI registry before adopting.

**Sources:** [edu.chainguard.dev — How to Sign a Container with Cosign](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/) (fetched 2026-07-13) · [aquilax.ai — Supply Chain Artifact Signing SLSA](https://aquilax.ai/blog/supply-chain-artifact-signing-slsa) (fetched 2026-07-13) · [github.com/sigstore/cosign — Releases](https://github.com/sigstore/cosign/releases) (fetched 2026-07-13)

**Confidence:** 📄 vendor-documented — both Chainguard (Cosign's primary maintainer) and AquilaX support this, but they share commercial alignment with the Sigstore ecosystem.

---

## Practice: Generate and scan SBOMs for every AI container image

**Do:** Use Syft to generate a Software Bill of Materials (SBOM) for your AI container image at build time: `syft myapp:latest -o cyclonedx-json > sbom.cyclonedx.json`. Store the SBOM alongside the image. Then feed that SBOM to Grype for vulnerability scanning: `grype sbom:sbom.cyclonedx.json --fail-on high`. Run Trivy independently on the image for a second-opinion OS-level scan: `trivy image --severity CRITICAL,HIGH myapp:latest`.

⚠️ **WARNING — Syft installer:** The standard install method for Syft on Linux is piping a remote shell script to `sh` (`curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh`). On shared or production machines, verify the script's SHA-256 checksum against the Syft GitHub release before running it.

⚠️ **WARNING — Trivy supply chain attack (March 2026):** Trivy itself was the target of a confirmed supply chain attack on March 19, 2026 — malicious Trivy binary v0.69.4 was published to GitHub Releases, and the `aquasecurity/trivy-action` and `aquasecurity/setup-trivy` GitHub Actions were both compromised (exposure window ~12 hours; 45 repositories had runs with compromised action versions; ~5 had secrets directly exposed). **Always pin trivy-action to a commit SHA** rather than a mutable version tag. Safe versions: `trivy-action@0.35.0` (commit `57a97c7e`) or later; `setup-trivy@v0.2.6` (commit `3fb12ec`) or later. Current safe Trivy binary: v0.72.0 (released June 30, 2026).

**Why:** An SBOM is a machine-readable ingredient list — every OS package, Python library, and runtime bundled in your image. When a new CVE drops (like Log4Shell), you can instantly query all your SBOMs to answer "which of our deployed images contains this package?" Syft and Trivy use independent vulnerability databases, so running both widens coverage.

**Caveat / contested:** ⚠️ **Noise vs. signal:** Setting fail-thresholds too low (failing on every LOW CVE) produces alert fatigue that causes teams to disable scanning entirely. Set explicit thresholds (CRITICAL and HIGH are the practical default) and document exceptions with justification and re-evaluation dates. Syft and Trivy can produce different package counts for the same image — treat a significant discrepancy as a signal to investigate. 🕒 Trivy and Grype update their vulnerability databases frequently; scan results from a cached database older than 24 hours may miss recent CVEs.

**Sources:** [opscart.com — Docker Supply Chain Security](https://opscart.com/guides-tutorials/docker-security-guide/docker-supply-chain-security/) (fetched 2026-07-13) · [vucense.com — Container Vulnerability Scanning 2026](https://vucense.com/dev-corner/container-vulnerability-scanning-2026/) (fetched 2026-07-13) · [appsecsanta.com — Syft vs Trivy 2026](https://appsecsanta.com/sca-tools/syft-vs-trivy) (fetched 2026-07-13) · [stepsecurity.io — Trivy compromised: malicious v0.69.4 release](https://www.stepsecurity.io/blog/trivy-compromised-a-second-time---malicious-v0-69-4-release) (fetched 2026-07-13) · [github.com/aquasecurity/trivy — GHSA-69fq-xp46-6x23](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (three independent publishers for SBOM practice; Trivy incident confirmed by StepSecurity and Aqua Security advisory)

---

## Practice: Pin GitHub Actions to commit SHAs and use OIDC instead of stored credentials

**Do:** Replace any floating version tag in a GitHub Actions workflow (e.g., `uses: actions/checkout@v4`) with the full commit SHA (e.g., `uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683`). Set `permissions: {}` at the top of every workflow and add back only the minimum scopes each job requires. Replace AWS/GCP/Azure long-lived keys stored as repository secrets with OIDC-based short-lived token exchange. Enforce a 7–14 day cooldown before adopting newly released action versions in production.

The March 2026 Trivy supply chain attack (see SBOM practice above) is a direct example: teams using `aquasecurity/trivy-action@v*` (mutable tag) during the exposure window ran the compromised action. SHA-pinned installations were unaffected.

**Why:** A floating tag like `@v4` can be moved by anyone with write access to the action's repo. The tj-actions/changed-files supply chain attack (CVE-2025-30066, March 2025) affected 23,000+ repositories using mutable tags — workflow logs in those repos captured runner secrets.

⚠️ **WARNING — dangerous default:** GitHub's default `GITHUB_TOKEN` has write permissions in many repository configurations. If you do not explicitly set `permissions: {}` (read-only), a compromised workflow step can push commits, create releases, or modify repository settings. Check your organization-level defaults under Settings > Actions > General > Workflow permissions. SHA pinning requires ongoing maintenance; Dependabot can automate SHA updates if configured for Actions.

**Sources:** [docs.github.com — Secure use of GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use) (fetched 2026-07-13) · [wiz.io — GitHub Actions supply chain attack: tj-actions CVE-2025-30066](https://www.wiz.io/blog/github-action-tj-actions-changed-files-supply-chain-attack-cve-2025-30066) (fetched 2026-07-13) · [cisa.gov — CVE-2025-30066 alert](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) (fetched 2026-07-13) · [corgea.com — GitHub Actions Security Checklist](https://corgea.com/learn/github-actions-security-checklist) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (GitHub official docs + Wiz incident post + CISA advisory + independent security guide)

---

## Practice: Adopt SLSA Build Level 2 as a minimum for AI artifact releases

**Do:** For any model checkpoint, container image, or Python package your team releases, target SLSA Build Level 2: build on a hosted CI platform (GitHub Actions, GitLab CI, Google Cloud Build), configure that platform to generate signed provenance automatically (GitHub's `actions/attest-build-provenance` or the `slsa-framework/slsa-github-generator`), and distribute the signed provenance alongside the artifact. Consumers should verify provenance with the SLSA verifier tool before deploying.

**Why:** SLSA (Supply-chain Levels for Software Artifacts, pronounced "salsa") is an open framework from Google/OpenSSF that defines four levels of build integrity guarantees. Level 2 adds signed provenance generated by a hosted platform, making post-build tampering detectable — an attacker who modifies the artifact after build cannot forge a valid provenance signature. Level 3 adds build isolation. Most teams can reach Level 2 in an afternoon with modern GitHub tooling. SLSA provenance extends naturally to AI artifacts: a signed record of which training code, dataset commit, and base model version produced a given checkpoint.

**Caveat / contested:** SLSA provenance proves build integrity, not correctness of the model or safety of training data. A cleanly-built model trained on a poisoned dataset has perfect SLSA provenance. 🕒 The current SLSA specification is **v1.2** (announced November 2025) — verify the current version and tooling support at [slsa.dev/spec/v1.2/](https://slsa.dev/spec/v1.2/).

**Sources:** [slsa.dev/spec/v1.2/ — SLSA Levels specification v1.2](https://slsa.dev/spec/v1.2/) (fetched 2026-07-13) · [aquilax.ai — Supply Chain Artifact Signing and SLSA](https://aquilax.ai/blog/supply-chain-artifact-signing-slsa) (fetched 2026-07-13) · [wiz.io — SLSA Framework](https://www.wiz.io/academy/application-security/slsa-framework) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (SLSA official spec + two independent publishers: AquilaX, Wiz)

---

## Practice: Enable Dependency Review Action and Dependabot for AI Python libraries

**Do:** In your GitHub repository, enable the dependency graph and activate Dependabot security alerts. Add the `dependency-review-action` as a required status check on pull requests (it blocks merges when a PR introduces a dependency with a known CVE). For Python AI projects, use `pip install --require-hashes` with a pinned `requirements.txt` to prevent silent version drift. As of April 7, 2026, Dependabot alerts can also be assigned to AI coding agents (GitHub Copilot, Claude, Codex) to draft fix PRs automatically.

**Why:** AI/ML projects pull in dozens of Python packages (transformers, torch, diffusers, langchain, etc.) that are updated frequently and have had serious CVEs. Without automated alerts, teams often discover vulnerabilities only after a public incident. Python pip auto-submission for the dependency graph shipped in July 2025, completing transitive dependency tracking for the ecosystem.

**Caveat / contested:** Dependabot generates many PRs in active AI projects with fast-moving dependencies; without triage discipline, teams disable it or let PRs pile up unreviewed. Establish a severity triage policy (auto-merge patch updates in a staging branch; require human review for minor/major). 🕒 Verify current pip ecosystem coverage at the GitHub changelog.

**Sources:** [docs.github.com — About Dependency Review](https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) (fetched 2026-07-13) · [github.blog changelog — Dependency auto-submission now supports Python (2025-07-08)](https://github.blog/changelog/2025-07-08-dependency-auto-submission-now-supports-python/) (fetched 2026-07-13) · [github.blog changelog — Dependabot alerts assignable to AI agents (2026-04-07)](https://github.blog/changelog/2026-04-07-dependabot-alerts-are-now-assignable-to-ai-agents-for-remediation/) (fetched 2026-07-13)

**Confidence:** 📄 vendor-documented — all three sources are GitHub official documentation and GitHub Blog.

---

## Practice: Verify model and container integrity end-to-end in air-gapped deployments

**Do:** For deployments in restricted or air-gapped networks: (1) Download all artifacts (model weights, container images, Python packages, OS packages) in a connected staging environment. (2) Compute SHA-256 hashes for every artifact and store them in a GPG-signed manifest (`sha256sum *.safetensors *.tar.gz > manifest.sha256`, then `gpg --detach-sign manifest.sha256`). (3) Transfer artifacts via write-once or write-protected media (DVD-R, hardware-locked USB). (4) On arrival in the air-gapped environment, mount media read-only, verify the GPG signature (`gpg --verify manifest.sha256.sig manifest.sha256`), then run `sha256sum -c manifest.sha256` against every artifact before importing to the internal registry (Harbor, Artifactory, or a self-hosted OCI registry). (5) Log all verification events with timestamps and operator identity.

⚠️ **WARNING:** If the GPG signing key used to sign the manifest is stored on the same media as the artifacts, the verification chain is broken — an attacker who controls the media can replace both. Keep signing keys on a separate, online (but secured) system. Also: air-gapped AI deployments typically lag public model capabilities by months due to update friction; factor this into threat modelling.

**Why:** In an air-gapped environment you cannot fall back to pulling fresh images or re-downloading models if something looks suspicious. Every byte must be accountable before it crosses the air gap, because there is no patch path once inside.

**Caveat / contested:** Periodic re-verification of already-imported artifacts (quarterly at minimum) is recommended — files in internal registries can be tampered with post-import. Private Python mirrors (bandersnatch, devpi) and container registries are themselves a new attack surface and require access controls.

**Sources:** [localaimaster.com — Air-Gapped AI Deployment Guide](https://localaimaster.com/blog/air-gapped-ai-deployment) (fetched 2026-07-13) · medium.com/@sivakiran.nandipati — Deploying AI Models in Air-Gapped Environments (fetched 2026-07-13; confirmed live via WebFetch but returns 403 to automated checks — unlinked per gate policy)

**Confidence:** ✅ independently-corroborated (two independent publishers: Local AI Master, Siva Kiran Nandipati / Medium)

---

## Practice: Scan AI container base images for OS-level CVEs before every release

**Do:** Run `trivy image --severity CRITICAL,HIGH <image>:<tag>` as a required CI gate before pushing any AI workload image to your production registry. Use distroless or minimal base images (e.g., `gcr.io/distroless/python3`) to reduce the OS package surface. Enforce a registry-level policy (Harbor's "Prevent vulnerable images from running" feature, or equivalent in AWS ECR Inspector / Docker Hub paid plans) to block deployment of images that fail the scan threshold.

⚠️ **WARNING — Trivy supply chain incident:** Trivy's own GitHub Action was compromised in March 2026 (see SBOM practice above). Always pin `trivy-action` to a commit SHA. Safe versions: `aquasecurity/trivy-action@0.35.0` (commit `57a97c7e`) or later. Safe binary version: Trivy v0.72.0+ (released June 30, 2026). 🕒 Verify current safe versions at [github.com/aquasecurity/trivy/releases](https://github.com/aquasecurity/trivy/releases).

**Why:** AI workload containers inherit all the CVEs of the underlying OS packages (libc, openssl, curl, etc.) plus GPU drivers if included. A newly discovered OpenSSL critical CVE can make thousands of AI inference containers vulnerable overnight. Distroless images ship without a shell or package manager, eliminating entire categories of OS-level attack surface.

**Caveat / contested:** Trivy produces false positives, especially on edge-case packages or when distro-specific patches are applied upstream but not yet reflected in NVD. Review findings before acting on them, and document exceptions with expiration dates. GPU driver containers (NVIDIA Container Runtime) need explicit scans or vendor security advisories as they use unusual packaging. 🕒 Trivy vulnerability database updates frequently; scan results from a cached database older than 24 hours may miss recent CVEs.

**Sources:** [opscart.com — Docker Supply Chain Security](https://opscart.com/guides-tutorials/docker-security-guide/docker-supply-chain-security/) (fetched 2026-07-13) · [vucense.com — Container Vulnerability Scanning 2026](https://vucense.com/dev-corner/container-vulnerability-scanning-2026/) (fetched 2026-07-13) · [aisecurityandsafety.org — AI Supply Chain Security Guide](https://aisecurityandsafety.org/en/guides/ai-supply-chain-security/) (fetched 2026-07-13) · [aquasec.com — Trivy supply chain attack: what you need to know](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (three independent publishers for Trivy scanning; Aqua Security advisory for incident detail)

---

## Held pending fixes
- ModelScan/PickleScan bypass vulnerability patch status: scanner bypass research is fast-moving; exact current fix state not fully verified as of 2026-07-13 — add a `verify live` caveat before relying on scanners as sole defense ⚠ (no project issue filed — already caveated inline)

## CHANGELOG (grading → this entry)
1. Skeptic FIX: Removed ">80% of models on public registries still use pickle-based formats" — no cited source stated any percentage; replaced with factual description of pickle prevalence and Transformers 5.0 context.
2. Skeptic FIX: Fixed Trail of Bits safetensors audit citation — corrected from dev.to (which does not mention Trail of Bits) to the Hugging Face blog that references the actual audit.
3. Skeptic FIX: Removed "Grype tends toward precision and low false positives; Trivy casts a wider net" — appsecsanta.com does not make this precision/false-positive comparison; replaced with what the source actually states.
4. Skeptic FIX: Fixed tj-actions "23,000+ repositories" citation — changed from Wiz general security guide (says "thousands") to the Wiz incident-specific post and CISA CVE-2025-30066 advisory (both confirm 23,000+).
5. Skeptic FLAG: Reworded "leaked secrets from 23,000+ repositories" → "affected 23,000+ repositories" — the action ran in 23,000+ repos but ~218 repos had real secrets exposed in workflow logs; no confirmed external exfiltration.
6. Beginner KILL: Added ModelScan install command (`pip install modelscan`) and run command (`modelscan -p model.pth`) with description of safe vs. unsafe output — readers previously had no instruction on actually running the scanner.
7. Beginner KILL: Added WARNING about Syft's remote-pipe install method being itself a risky pattern; instructed readers to verify the installer against official Syft release checksums.
8. Timekeeper KILL: Updated SLSA specification from v1.1 to v1.2 — v1.2 was announced November 2025 and is the current version at slsa.dev/spec/v1.2/. Updated citation.
9. Timekeeper KILL: Added comprehensive Trivy March 2026 supply chain attack WARNING — both in the SBOM practice and the OS CVE scanning practice; added safe version pins (trivy-action@0.35.0 commit 57a97c7e; binary v0.72.0+); cross-referenced practices.
10. Timekeeper FIX: "80% of models use pickle" reframed — Transformers 5.0.0 (released Jan 26, 2026) removed pickle support entirely from HF Transformers; the raw percentage claim was unsupported and likely stale; replaced with directional statement and verify-live note.
11. Timekeeper FIX: Added Cosign v3.x deprecation note — v3.1.1 (June 2026) deprecated several v2-era verification flags; v4 will remove them; teams on CI scripts using old flags need to update before the major version bump.
12. Link-check gate (2026-07-14): medium.com/@sivakiran.nandipati/deploying-ai-models-in-air-gapped-environments-... confirmed live via WebFetch (article exists, April 2025) but returns 403 to automated curl — unlinked to plain text per gate policy. Citation retained.
