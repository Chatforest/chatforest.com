---
title: "AI Agent Supply Chain Verification — What Every Beginner Needs to Know (as of 13 Jul 2026)"
date: 2026-07-13
snapshot_date: 2026-07-13
topic: ai-agent-supply-chain-generic
track: beginner
audience: "people new to AI"
description: "Plain-English guide to checking that the AI model files, containers, and code tools you download are safe and unmodified — no prior security knowledge required."
content_type: "Best Practice"
categories: ["AI Security", "Supply Chain", "DevSecOps"]
tags: ["supply-chain", "model-verification", "safetensors", "slsa", "sbom", "cosign", "trivy", "grype", "syft", "air-gap", "github-actions", "dependabot"]
last_refreshed: 2026-07-13
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-13"
grading_result: "0 fabrications; 12 corrections applied; 0 gaps filed as project-33 issues"
---

<!-- Immutable dated snapshot. content/ai/beginner/ai-agent-supply-chain-generic/2026-07-13/index.md -->

# AI Agent Supply Chain Verification — What Every Beginner Needs to Know (as of 13 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **13 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## Why this matters before you read anything else

When you build an AI agent, it downloads pieces from many different places on the internet: the AI model's "brain" (called model weights), packaged software containers, helper code libraries, and automated build tools. Any one of those pieces can be secretly swapped for a harmful version — a trick attackers call a **supply chain attack**.

This guide walks you through the key checks, one by one, in plain English. You do not need to be a security expert. You do need to follow each step carefully, because the failure modes are serious: a poisoned model file can run any command on your computer the moment you load it; a tampered container can leak your passwords; a hijacked build tool can steal your cloud credentials.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers agree on this
- 📄 **vendor-documented** — comes from the official maker's own documentation
- ⚠️ **WARNING** — skipping this can cost money, break your machine, or expose your secrets
- 🕒 **verify live** — version numbers and details change fast; check the current value before acting

---

## Practice 1: Choose the safer model file format (safetensors instead of pickle)

### What this means in plain English

When you download an AI model, the model's learned data (called "weights") is stored in a file. There are two common file formats:

- **Pickle format** — files ending in `.bin`, `.pt`, or `.pth`. These files use Python's "pickle" serialization system, which was designed to save and reload any Python object. The problem is that a pickle file can contain hidden instructions that execute automatically the moment you call `torch.load()` on the file. An attacker who uploads a malicious `.pth` file to a public model registry can run any shell command on your machine just from you opening that file. You would not even see an error — the attack happens silently during loading.

- **SafeTensors format** — files ending in `.safetensors`. This format stores only the raw numbers (the tensor data) in a flat binary layout with a plain-text header. There is no mechanism for executable code to hide inside a safetensors file. Trail of Bits (a security firm) audited the safetensors specification in March 2023 (commissioned by EleutherAI and Hugging Face) and found no critical security flaws.

**The concrete failure this prevents:** You download what looks like a helpful AI model. It is actually a weapon. The moment your code loads it, an attacker's script runs on your machine — potentially stealing files, installing malware, or exfiltrating your API keys.

**Do:** When downloading model weights from Hugging Face or any other registry, always choose `.safetensors` files. If only a pickle-based format is available, scan it with ModelScan before loading. Here is how to install and run ModelScan:

```bash
# Step 1: Install ModelScan (only needed once)
pip install modelscan

# Step 2: Scan the file before loading it
modelscan -p model.pth
```

**What the output means:**
- A "Safe" result means ModelScan found no executable payloads matching its known patterns. The file is probably okay to use — but read the warning below.
- An "Unsafe" result means ModelScan found something suspicious. It will print a description of the problem and exit with an error code. Do not load the file.

Note: As of Hugging Face Transformers version 5.0.0 (released January 26, 2026), safetensors is the only supported format in that library. If you try to use `safe_serialization=False`, you will get an error. 🕒 Verify live for the current state of the ecosystem.

⚠️ **WARNING — scanner bypass:** ModelScan and PickleScan have known bypass vulnerabilities. A specially crafted malicious file can crash the scanner without triggering a detection alert, meaning you would see no warning even though the file is dangerous. Treat a "Safe" scan result as a raised floor, not a guarantee. Never rely on the scanner as your only defense — also use checksum verification (see Practice 2 below). 🕒 Verify scanner patch status before relying on them.

**One more limit to know:** SafeTensors prevents code execution during loading, but an attacker can still tamper with the numbers themselves to subtly change how the model behaves (called a backdoor or data poisoning attack). Format checking alone is not a complete defense — you still need checksum verification (Practice 2).

**Sources:** [dev.to/lukehinds — Understanding SafeTensors](https://dev.to/lukehinds/understanding-safetensors-a-secure-alternative-to-pickle-for-ml-models-o71) (fetched 2026-07-13) · [huggingface.co/blog — SafeTensors security audit](https://huggingface.co/blog/safetensors-security-audit) (fetched 2026-07-13) · [infosec.qa — AI Supply Chain Attacks](https://infosec.qa/blog/ai-supply-chain-attacks/) (fetched 2026-07-13) · [isc.sans.edu — ModelScan diary](https://isc.sans.edu/diary/31692) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (four independent publishers: DEV Community, Hugging Face blog with Trail of Bits audit reference, infosec.qa, SANS ISC)

---

## Practice 2: Verify SHA-256 checksums for every downloaded model file

### What this means in plain English

A SHA-256 checksum (also called a hash or fingerprint) is a short string of letters and numbers that is mathematically derived from the full contents of a file. If even one byte of the file changes — even a single character — the SHA-256 output changes completely. This makes it an excellent tamper detector.

When you download a model file, the original publisher computes its SHA-256 and posts that value somewhere (for example, on Hugging Face's "Files and versions" tab). After your download finishes, you compute the SHA-256 of the file you actually received and compare the two values. If they match, you have the correct, unmodified file. If they do not match, something went wrong — network corruption, a bad mirror, or an attacker substituting a different file.

**The concrete failure this prevents:** You download a model file. Without checking, you would never know if it was silently swapped for a different file somewhere between the server and your hard drive. With checksum verification, a mismatch immediately tells you something is wrong before you run anything.

**Do:** After downloading any model weight file, run the appropriate command for your operating system and compare the result against the publisher's published checksum:

```bash
# Linux or macOS
sha256sum model.safetensors

# Windows
certutil -hashfile model.safetensors SHA256
```

Get the expected checksum from the Hugging Face "Files and versions" tab (or the equivalent on whatever registry you are using). Important: fetch the checksum value over HTTPS from a source that is separate from the file download itself — never trust a checksum that appears on the exact same page that served you the download link, because an attacker who controls that page can change both.

⚠️ **WARNING — dangerous default:** Platforms like Hugging Face do not automatically re-check model files that are already saved on your computer. `hf_hub_download()` checks the checksum at the moment of the original download, but does not re-check the saved file on future loads. A file that gets corrupted or tampered with inside your `~/.cache/huggingface` folder will be loaded silently without any warning. Build a periodic re-verification step into your workflow so you catch any changes after the initial download.

**One more limit to know:** If the registry itself is compromised, the published checksums may also be replaced. A checksum on a separate, signed release page is stronger evidence than a checksum displayed on the same download page.

**Sources:** [qwe.edu.pl — How to Verify AI Model Downloads](https://www.qwe.edu.pl/tutorial/how-to-verify-ai-model-download/) (fetched 2026-07-13) · [aisecurityandsafety.org — AI Supply Chain Security Guide](https://aisecurityandsafety.org/en/guides/ai-supply-chain-security/) (fetched 2026-07-13) · [infosec.qa — AI Supply Chain Attacks](https://infosec.qa/blog/ai-supply-chain-attacks/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (three independent publishers: QWE Academy, AI Safety Directory, infosec.qa)

---

## Practice 3: Sign and verify container images with Cosign

### What this means in plain English

A container image is like a complete, self-contained package that holds your AI workload — all its software, dependencies, and configuration — so it runs the same way everywhere. Think of it as a shipping container for software.

The problem is that a container image stored in a registry (an online warehouse for images) can be silently swapped for a different image if someone breaks into the registry account, poisons a cache, or intercepts the network traffic. You would pull what you think is your trusted image and run someone else's malicious one instead.

**Cosign** is a tool that lets you attach a cryptographic signature to a container image. A signature is a mathematical proof that a specific, trusted source (like your CI/CD build system) produced exactly this image. Before running an image, you verify the signature. If it does not match, you refuse to run the image.

**Keyless OIDC signing** means you do not have to manage a long-lived secret signing key yourself. Instead, your CI/CD platform (for example GitHub Actions) temporarily proves its identity using a short-lived identity token called an OIDC token (Open ID Connect — a standard way for a trusted platform to vouch for who is making a request). Cosign uses that identity to create the signature and records it in Sigstore's Rekor log, which is an append-only public record — once something is written there, it cannot be deleted or altered.

**SBOM** stands for Software Bill of Materials — a machine-readable list of every component inside the container (explained more in Practice 4). **SLSA** stands for Supply-chain Levels for Software Artifacts (pronounced "salsa") — a framework for proving how an artifact was built (explained more in Practice 5). **OCI** stands for Open Container Initiative — the standard format for container images. When this guide says "OCI tag," it means the label attached to a container image in a registry.

**The concrete failure this prevents:** An attacker gains brief access to your container registry and replaces your AI workload image with one that phones home with your users' data. Without signature verification, your deployment pipeline pulls and runs the malicious image without noticing. With Cosign verification, the pipeline rejects any image whose signature does not match the expected signer identity.

**Do:** Add a Cosign signing step to your CI/CD release workflow. After building an AI workload container, sign it with `cosign sign` using keyless OIDC signing (no long-lived key to manage). In any deployment pipeline that pulls the image, run `cosign verify` against the expected signer identity before allowing the image to run. Attach SLSA provenance and SBOM attestations to the same OCI tag using `cosign attest`.

🕒 **Cosign version:** The current release is v3.1.1 (June 2026). Cosign v3.x deprecated several flags that existed in v2 related to how verification material is supplied and how bundle formats work. A v4 release is expected to remove those deprecated flags entirely. If your CI scripts use `--attachment sig` or other v2-era flags, update them before upgrading to v4.

**One limit to know:** Keyless signing requires an OIDC provider (such as GitHub Actions or Google Cloud) in your CI/CD environment. Self-hosted or air-gapped pipelines need extra configuration to reach the Fulcio certificate authority and Rekor log, or to run a private Sigstore deployment. 🕒 Verify Cosign version compatibility with your OCI registry before adopting.

**Sources:** [edu.chainguard.dev — How to Sign a Container with Cosign](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/) (fetched 2026-07-13) · [aquilax.ai — Supply Chain Artifact Signing SLSA](https://aquilax.ai/blog/supply-chain-artifact-signing-slsa) (fetched 2026-07-13) · [github.com/sigstore/cosign — Releases](https://github.com/sigstore/cosign/releases) (fetched 2026-07-13)

**Confidence:** 📄 vendor-documented — both Chainguard (Cosign's primary maintainer) and AquilaX support this, but they share commercial alignment with the Sigstore ecosystem.

---

## Practice 4: Generate and scan SBOMs for every AI container image

### What this means in plain English

An **SBOM** (Software Bill of Materials — pronounced "S-bomb") is exactly what it sounds like: a complete ingredient list for a software package. Just as a food product lists every ingredient on the label, an SBOM lists every OS package, Python library, and runtime component bundled inside your container image, along with version numbers.

Why does this matter? When a serious security vulnerability is discovered in a widely used library (for example, a flaw in OpenSSL or Log4j), you need to quickly answer "do any of my deployed containers include this library?" Without an SBOM, you would have to open every container and look manually. With an SBOM stored alongside each image, you can run a single query across all of them in seconds.

**CVE** stands for Common Vulnerabilities and Exposures — the standard catalog of publicly known security flaws, each with a unique ID number (like CVE-2021-44228 for Log4Shell).

**The concrete failure this prevents:** A critical CVE is published for a library your AI container uses. Without an SBOM and scanner, you might not discover the exposure for days or weeks — plenty of time for an attacker to exploit it. With an SBOM and automated scanning, you know within hours.

**Do:** Use three tools together. Here is what each one does and how to run it:

**Syft** generates the SBOM (the ingredient list):
```bash
syft myapp:latest -o cyclonedx-json > sbom.cyclonedx.json
```
Store the resulting `sbom.cyclonedx.json` file alongside your image.

**Grype** reads that SBOM and checks every ingredient against a vulnerability database:
```bash
grype sbom:sbom.cyclonedx.json --fail-on high
```
The `--fail-on high` flag means the command will exit with an error (blocking your CI pipeline) if any HIGH or CRITICAL severity vulnerability is found.

**Trivy** performs an independent second-opinion scan directly on the image at the OS level:
```bash
trivy image --severity CRITICAL,HIGH myapp:latest
```
Running two tools (Grype and Trivy) catches more vulnerabilities because they use different databases.

⚠️ **WARNING — Trivy supply chain attack (March 2026):** Trivy itself was the target of a confirmed supply chain attack on March 19, 2026. A malicious Trivy binary version v0.69.4 was published to GitHub Releases, and the `aquasecurity/trivy-action` and `aquasecurity/setup-trivy` GitHub Actions (the automated steps that run Trivy in your CI pipeline) were both compromised. The exposure window was approximately 12 hours. During that window, 45 repositories had runs with the compromised action versions, and approximately 5 had secrets directly exposed.

**What this means for you:** Always pin trivy-action to a commit SHA (a permanent fingerprint for an exact version of code — explained more in Practice 5) rather than a mutable version tag. Safe versions to use: `trivy-action@0.35.0` (commit `57a97c7e`) or later; `setup-trivy@v0.2.6` (commit `3fb12ec`) or later. Safe Trivy binary version: v0.72.0 (released June 30, 2026). 🕒 Verify current safe versions at [github.com/aquasecurity/trivy/releases](https://github.com/aquasecurity/trivy/releases).

⚠️ **WARNING — Syft installer:** The standard install method for Syft on Linux involves downloading a shell script from the internet and running it directly (`curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh`). Running an unverified script from the internet is itself a risk. On shared or production machines, verify the installer script's SHA-256 checksum (see Practice 2 for how to compute one) against the checksum published on the Syft GitHub release page before running it.

**One limit to know:** Setting the failure threshold too strict (for example, failing your pipeline on every LOW severity CVE) creates so many alerts that teams start disabling scanning entirely to get work done. Set explicit thresholds (CRITICAL and HIGH are the practical default used here) and document any exceptions with a justification and a re-evaluation date. Also note that Syft and Trivy can produce different package counts for the same image — a significant discrepancy between them is itself a signal worth investigating. 🕒 Trivy and Grype update their vulnerability databases frequently; scan results from a cached database older than 24 hours may miss recently published CVEs.

**Sources:** [opscart.com — Docker Supply Chain Security](https://opscart.com/guides-tutorials/docker-security-guide/docker-supply-chain-security/) (fetched 2026-07-13) · [vucense.com — Container Vulnerability Scanning 2026](https://vucense.com/dev-corner/container-vulnerability-scanning-2026/) (fetched 2026-07-13) · [appsecsanta.com — Syft vs Trivy 2026](https://appsecsanta.com/sca-tools/syft-vs-trivy) (fetched 2026-07-13) · [stepsecurity.io — Trivy compromised: malicious v0.69.4 release](https://www.stepsecurity.io/blog/trivy-compromised-a-second-time---malicious-v0-69-4-release) (fetched 2026-07-13) · [github.com/aquasecurity/trivy — GHSA-69fq-xp46-6x23](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (three independent publishers for SBOM practice; Trivy incident confirmed by StepSecurity and Aqua Security advisory)

---

## Practice 5: Pin GitHub Actions to commit SHAs and use OIDC instead of stored credentials

### What this means in plain English

**GitHub Actions** is a system that automatically runs tasks (like building your software, running tests, or scanning for vulnerabilities) whenever you push code to GitHub. Each task uses a reusable "action" — a small program someone else wrote that you include in your workflow file.

The standard way to include an action looks like this:
```yaml
uses: actions/checkout@v4
```

The `@v4` part is a version tag. Here is the problem: version tags are not permanent. Anyone with write access to the action's repository can move the `v4` tag to point to a completely different version of the code — including a malicious one. Your workflow would then automatically run that new, malicious version the next time it triggers.

**A commit SHA** is a permanent, unique fingerprint for one specific version of code. It looks like a long string of letters and numbers, for example `11bd71901bbe5b1630ceea73d27597364c9af683`. Unlike a version tag, a commit SHA can never be moved or reused — it always and forever refers to that exact version of the code. Pinning to a commit SHA means your workflow will only ever run the specific version you reviewed.

**The concrete failure this prevents:** The March 2026 Trivy supply chain attack (described in Practice 4) is a real example. Teams using `aquasecurity/trivy-action@v*` (a mutable tag) during the 12-hour exposure window automatically ran the compromised, malicious version of the action. Teams that had pinned to a commit SHA ran the safe version they had originally approved and were completely unaffected.

An earlier, larger example: the tj-actions/changed-files supply chain attack (CVE-2025-30066 — assigned March 2025) affected 23,000+ repositories using mutable tags. Workflow logs in those repositories captured runner secrets.

**Do:** Replace any floating version tag in your GitHub Actions workflow with the full commit SHA. For example, change:
```yaml
uses: actions/checkout@v4
```
to:
```yaml
uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
```

Also, set `permissions: {}` at the top of every workflow file and add back only the minimum permissions each job actually needs. Replace any long-lived AWS, GCP, or Azure keys stored as repository secrets with OIDC-based short-lived token exchange (OIDC = a short-lived identity token issued by a trusted platform, so you never have a permanent secret that can be stolen). Wait 7–14 days before adopting newly released action versions in production, so the community has time to catch problems.

⚠️ **WARNING — dangerous default:** GitHub's default `GITHUB_TOKEN` has write permissions in many repository configurations. If you do not explicitly set `permissions: {}` (which makes it read-only), a compromised workflow step can push commits, create releases, or change repository settings using your repository's own token. Check your organization-level defaults under Settings > Actions > General > Workflow permissions. Note that SHA pinning requires ongoing maintenance as new versions of actions are released; Dependabot (described in Practice 6) can automate SHA updates if configured for Actions.

**Sources:** [docs.github.com — Secure use of GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use) (fetched 2026-07-13) · [wiz.io — GitHub Actions supply chain attack: tj-actions CVE-2025-30066](https://www.wiz.io/blog/github-action-tj-actions-changed-files-supply-chain-attack-cve-2025-30066) (fetched 2026-07-13) · [cisa.gov — CVE-2025-30066 alert](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) (fetched 2026-07-13) · [corgea.com — GitHub Actions Security Checklist](https://corgea.com/learn/github-actions-security-checklist) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (GitHub official docs + Wiz incident post + CISA advisory + independent security guide)

---

## Practice 6: Aim for SLSA Build Level 2 for any AI artifact your team releases

### What this means in plain English

**SLSA** stands for Supply-chain Levels for Software Artifacts. It is pronounced "salsa." It is an open framework created by Google and the OpenSSF (Open Source Security Foundation) that defines four levels of build integrity guarantees for software you release.

Think of SLSA levels like food safety certifications: Level 1 is a basic label saying what is inside; Level 2 adds a signed document proving where it came from and how it was made; Level 3 adds a sealed, isolated production environment. For most teams, **Level 2 is the practical goal** and can be reached in an afternoon using modern GitHub tooling.

At SLSA Level 2, every artifact (model checkpoint, container image, Python package) you release comes with a **signed provenance record** — a cryptographically verified document that records which exact code, on which exact platform, at which exact time, produced this artifact. Anyone who receives your artifact can verify the provenance record and confirm it was not tampered with after the build finished. An attacker who modifies the artifact after the build cannot forge a valid provenance signature.

SLSA provenance applies naturally to AI artifacts: it creates a signed record of which training code, which dataset commit, and which base model version produced a given model checkpoint.

**Do:** For any model checkpoint, container image, or Python package your team releases, target SLSA Build Level 2: build on a hosted CI platform (GitHub Actions, GitLab CI, or Google Cloud Build), configure that platform to generate signed provenance automatically using `actions/attest-build-provenance` or the `slsa-framework/slsa-github-generator`, and distribute the signed provenance alongside the artifact. Consumers should verify provenance with the SLSA verifier tool before deploying.

**One important limit to know:** SLSA provenance proves that the build process was intact and untampered. It does not prove that the model is safe or that the training data was clean. A model trained on a poisoned dataset will have perfect SLSA provenance — the build was honest, but the inputs were bad. SLSA is one layer of a defense, not the whole defense.

🕒 The current SLSA specification is **v1.2** (announced November 2025). Verify the current version and tooling support at [slsa.dev/spec/v1.2/](https://slsa.dev/spec/v1.2/).

**Sources:** [slsa.dev/spec/v1.2/ — SLSA Levels specification v1.2](https://slsa.dev/spec/v1.2/) (fetched 2026-07-13) · [aquilax.ai — Supply Chain Artifact Signing and SLSA](https://aquilax.ai/blog/supply-chain-artifact-signing-slsa) (fetched 2026-07-13) · [wiz.io — SLSA Framework](https://www.wiz.io/academy/application-security/slsa-framework) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (SLSA official spec + two independent publishers: AquilaX, Wiz)

---

## Practice 7: Enable Dependency Review and Dependabot for your AI Python libraries

### What this means in plain English

AI and machine learning projects use many Python packages — libraries like `transformers`, `torch`, `diffusers`, and `langchain`. Each of these packages has its own version history, and new security vulnerabilities (CVEs — Common Vulnerabilities and Exposures) are discovered in them regularly. Without an automated alert system, you might not hear about a serious flaw in a library your project uses until long after attackers have already exploited it elsewhere.

GitHub provides two free tools to help:

- **Dependabot** monitors your project's dependencies and automatically opens a pull request (a proposed code change) whenever a new security fix is available for a library you use. You review and merge it, and your project is patched.

- **Dependency Review Action** is a check that runs on every proposed code change (pull request). If someone tries to add a new library that already has a known CVE, the check blocks the merge and shows you the problem.

**The concrete failure this prevents:** A CVE is published for a version of `langchain` that your project uses. Without Dependabot, you might not notice for weeks. With Dependabot, you receive an alert and a ready-made fix within hours.

**Do:** In your GitHub repository, enable the dependency graph and activate Dependabot security alerts. Add the `dependency-review-action` as a required status check on pull requests — this blocks merges when a PR introduces a dependency with a known CVE. For Python AI projects, use `pip install --require-hashes` with a pinned `requirements.txt` to prevent silent version drift (where a library silently updates to a newer version you did not approve). As of April 7, 2026, Dependabot alerts can also be assigned to AI coding agents (GitHub Copilot, Claude, Codex) to draft fix pull requests automatically. 🕒 Verify current pip ecosystem coverage at the GitHub changelog.

**One limit to know:** Dependabot generates many pull requests in active AI projects because the libraries update frequently. Without a plan for handling them, the PRs pile up unreviewed and teams start ignoring or disabling the tool — which defeats the purpose entirely. Establish a triage policy before you turn it on: for example, auto-merge patch-level updates in a staging branch, but require a human to review minor and major version updates.

Note: Python pip automatic dependency submission for GitHub's dependency graph shipped in July 2025, completing transitive dependency tracking for the Python ecosystem.

**Sources:** [docs.github.com — About Dependency Review](https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) (fetched 2026-07-13) · [github.blog changelog — Dependency auto-submission now supports Python (2025-07-08)](https://github.blog/changelog/2025-07-08-dependency-auto-submission-now-supports-python/) (fetched 2026-07-13) · [github.blog changelog — Dependabot alerts assignable to AI agents (2026-04-07)](https://github.blog/changelog/2026-04-07-dependabot-alerts-are-now-assignable-to-ai-agents-for-remediation/) (fetched 2026-07-13)

**Confidence:** 📄 vendor-documented — all three sources are GitHub official documentation and GitHub Blog.

---

## Practice 8: Verify model and container integrity in air-gapped deployments

### What this means in plain English

An **air-gapped** environment is a computer or network that has no connection to the public internet. Air-gapped deployments are common in hospitals, government facilities, financial institutions, and other places where security or regulations require total network isolation.

Deploying AI in an air-gapped environment creates a specific problem: you cannot re-download a file if something looks wrong, and you cannot automatically get security patches. Everything you bring in must be verified before it crosses the air gap, because there is no patch path once inside.

**GPG** stands for GNU Privacy Guard. It is a free tool for digitally signing files. When you GPG-sign a manifest (a list of files and their checksums), you are creating a mathematical proof that you — specifically you, with your private GPG key — reviewed and approved that list at that moment in time. Anyone with your public GPG key can later verify that the manifest has not been changed since you signed it. If an attacker tampers with the manifest or swaps a file for a different one, the signature verification will fail.

**The concrete failure this prevents:** You carefully download and verify a set of model files in your connected environment, then transfer them to the air-gapped system. Without GPG signing, there is no way to prove the files on the transfer media were not tampered with between the two environments. With GPG signing, verification failure on arrival means you know immediately that something changed in transit.

**Do:** For deployments in restricted or air-gapped networks, follow these steps in order:

1. **Download** all artifacts (model weights, container images, Python packages, OS packages) in a connected staging environment.

2. **Compute SHA-256 checksums** for every artifact and store them in a GPG-signed manifest:
   ```bash
   sha256sum *.safetensors *.tar.gz > manifest.sha256
   gpg --detach-sign manifest.sha256
   ```
   This creates `manifest.sha256` (the list of checksums) and `manifest.sha256.sig` (the GPG signature proving you approved that list).

3. **Transfer artifacts** using write-once or write-protected media (DVD-R or a hardware-locked USB drive) so the files cannot be modified after you wrote them.

4. **On arrival in the air-gapped environment**, mount the media as read-only, then verify the GPG signature first, then verify all the checksums:
   ```bash
   gpg --verify manifest.sha256.sig manifest.sha256
   sha256sum -c manifest.sha256
   ```
   Only import to your internal registry (Harbor, Artifactory, or a self-hosted OCI registry) if both checks pass.

5. **Log** all verification events with timestamps and the identity of the operator who performed the verification.

⚠️ **WARNING:** If the GPG signing key used to sign the manifest is stored on the same physical media as the artifacts themselves, the verification chain is broken. An attacker who controls the media can replace both the files and the key used to approve them. Keep your signing key on a separate, secured online system — never on the transfer media. Also be aware that air-gapped AI deployments typically fall behind current public model capabilities by months because of the friction involved in updates; factor this lag into your security planning.

**One limit to know:** Files already imported into your internal registry can be tampered with after import. Periodic re-verification of already-imported artifacts (quarterly at minimum) is recommended. Your internal Python mirrors and container registries are also a new attack surface and need their own access controls.

**Sources:** [localaimaster.com — Air-Gapped AI Deployment Guide](https://localaimaster.com/blog/air-gapped-ai-deployment) (fetched 2026-07-13) · medium.com/@sivakiran.nandipati — Deploying AI Models in Air-Gapped Environments (fetched 2026-07-13; confirmed live via WebFetch but returns 403 to automated checks — unlinked per gate policy)

**Confidence:** ✅ independently-corroborated (two independent publishers: Local AI Master, Siva Kiran Nandipati / Medium)

---

## Practice 9: Scan AI container base images for OS-level CVEs before every release

### What this means in plain English

Your AI workload runs inside a container that includes a full operating system environment — low-level libraries like `libc`, `openssl`, `curl`, and potentially GPU drivers. These OS-level components have their own CVEs (security flaws), completely separate from your Python libraries or your model files. A critical new flaw in OpenSSL can instantly make thousands of AI inference containers vulnerable across the industry — overnight.

A **distroless** image is a container base image that has been stripped down to contain only what is absolutely necessary to run your application. There is no shell (`bash`), no package manager (`apt`), and no extra utilities. This means an attacker who somehow gets code execution inside your container has far fewer tools to work with.

This practice is closely related to Practice 4 (SBOM scanning), but focuses specifically on OS-level vulnerabilities found by scanning the image directly, in addition to the SBOM-based approach.

**The concrete failure this prevents:** Your AI service runs in a container built on a standard Ubuntu base image. A critical CVE is published for `openssl`. Without a scanning gate, that vulnerable container continues running in production. With a required scan before every release, the build pipeline rejects the image until you update the base image.

**Do:** Run Trivy as a required check before pushing any AI workload image to your production registry:
```bash
trivy image --severity CRITICAL,HIGH <image>:<tag>
```

Use distroless or minimal base images (for example `gcr.io/distroless/python3`) to reduce the number of OS packages that can have CVEs in the first place. Enforce a policy at the registry level to block deployment of images that fail the scan threshold. Harbor has a built-in "Prevent vulnerable images from running" feature; AWS ECR Inspector and Docker Hub paid plans have equivalent capabilities.

⚠️ **WARNING — Trivy supply chain incident:** Trivy's own GitHub Action was compromised in March 2026 (described in detail in Practice 4 above). Always pin `trivy-action` to a commit SHA. Safe versions: `aquasecurity/trivy-action@0.35.0` (commit `57a97c7e`) or later. Safe binary version: Trivy v0.72.0 or later (released June 30, 2026). 🕒 Verify current safe versions at [github.com/aquasecurity/trivy/releases](https://github.com/aquasecurity/trivy/releases).

**One limit to know:** Trivy produces false positives — it sometimes flags vulnerabilities that have already been patched by your Linux distribution but whose fix has not yet been reflected in the national vulnerability database (NVD). Review findings before acting on them and document exceptions with expiration dates so you revisit them. GPU driver containers (NVIDIA Container Runtime) use unusual packaging and may need explicit scans or vendor security advisories from NVIDIA rather than relying solely on Trivy. 🕒 Trivy's vulnerability database updates frequently; scan results from a cached database older than 24 hours may miss recently published CVEs.

**Sources:** [opscart.com — Docker Supply Chain Security](https://opscart.com/guides-tutorials/docker-security-guide/docker-supply-chain-security/) (fetched 2026-07-13) · [vucense.com — Container Vulnerability Scanning 2026](https://vucense.com/dev-corner/container-vulnerability-scanning-2026/) (fetched 2026-07-13) · [aisecurityandsafety.org — AI Supply Chain Security Guide](https://aisecurityandsafety.org/en/guides/ai-supply-chain-security/) (fetched 2026-07-13) · [aquasec.com — Trivy supply chain attack: what you need to know](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (three independent publishers for Trivy scanning; Aqua Security advisory for incident detail)

---

## Held pending fixes
- ModelScan/PickleScan bypass vulnerability patch status: scanner bypass research is fast-moving; exact current fix state not fully verified as of 2026-07-13 — add a `verify live` caveat before relying on scanners as sole defense (no project issue filed — already caveated inline)

## CHANGELOG
Re-leveled from technical entry (snapshot 2026-07-13) by rings-beginner-author. Facts, statistics, commands, URLs, source lines, Confidence labels, and all ⚠️ WARNING and 🕒 verify live markers are unchanged from the graded technical entry. Changes made in re-leveling:
- Added "Why this matters before you read anything else" introduction for complete newcomers.
- Expanded every practice with a "What this means in plain English" section.
- Defined all acronyms on first use: SBOM, SLSA, OCI, OIDC, SHA-256, GPG, CVE, pickle format.
- Added "The concrete failure this prevents" for each practice to make real-world stakes explicit.
- Explained what ModelScan "Safe" and "Unsafe" output means in plain English.
- Explained what pickle format is and why `torch.load()` is dangerous on untrusted files.
- Explained what GPG signing means (creating a digital signature that proves files have not been changed).
- Explained what a commit SHA is (a unique, permanent fingerprint for a specific version of code).
- Moved all ⚠️ WARNING blocks to prominent positions within each practice. No warnings were softened or dropped.
- Kept all 🕒 verify live caveats verbatim.
- Track changed from `best-practices` to `beginner`; audience changed to `people new to AI`.
- Title updated to include beginner framing.
- No new facts, statistics, CVE numbers, URLs, or claims were introduced.
- Link-check gate (2026-07-14): medium.com/@sivakiran.nandipati/deploying-ai-models-in-air-gapped-environments-... confirmed live via WebFetch but returns 403 to automated curl — unlinked to plain text per gate policy. Citation retained.
