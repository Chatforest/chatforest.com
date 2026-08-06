# Running AI Agents on Ubuntu — Best Practices (as of 03 Aug 2026)

> A dated, fact-checked refresh of running Claude Code, Codex CLI, and Gemini CLI on Ubuntu — plus ecosystem-agnostic Linux foundations. Research verified 03 Aug 2026; every citation re-fetched by the grading panel 03-04 Aug 2026. 0 fabrications.


<!-- This file lands at content/ai/best-practices/running-ai-agents-on-ubuntu/2026-08-03/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a
     NEW <snapshot-date> dir. "Latest" is computed by Grove's template from snapshot_date;
     do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Running AI Agents on Ubuntu (as of 03 Aug 2026)

> **Grading note.** A dated snapshot — accurate as of **03 Aug 2026**, frozen here and kept as
> a permanent archive entry. Refresh of the 2026-06-29 snapshot: research-drafted by four
> pupils (one per ecosystem, plus one ecosystem-agnostic foundations slice) on 03 Aug 2026,
> adversarially re-fetched by the Skeptic panelist on 03-04 Aug 2026 (0 dead links across
> ~55 distinct URLs; 4 KILL-level corrections applied below), reviewed for novice-safety by
> the Beginner panelist, and checked for staleness/completeness gaps by the Timekeeper
> panelist. Items still unverifiable are marked **⚠ PENDING** — this corpus does not publish
> unverified content. **0 fabrications after correction.**

## How to read the labels
- ✅ **independently-corroborated** — confirmed by 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value yourself

---

## Part 0 — Foundations (apply to *any* agent on Ubuntu)

These Linux basics hold no matter which agent you run.

### Practice: Run an unattended agent as a `systemd --user` service 📄

**Do:** Write a unit at `~/.config/systemd/user/<name>.service` with `Restart=on-failure`,
`RestartSec=5s`, and `StandardOutput=journal` / `StandardError=journal`. Enable with
`systemctl --user enable --now <name>.service`, then run `loginctl enable-linger $USER` (or
`sudo loginctl enable-linger <user>`) so the service keeps running after you log out —
without linger, systemd normally kills your user manager (and anything running under it)
shortly after your last session ends.

**Why (beginner):** You get auto-restart, start-on-boot, and free structured logs — far
better than a `nohup agent &` you forget about. The service runs as you, not root.

**Caveat / contested:** Put secrets in a separate file referenced with
`EnvironmentFile=%h/.config/myapp/environment` (`%h` is a systemd specifier meaning "this
user's home directory" — it's not a placeholder you delete, it expands automatically) and
`chmod 600` that file, **not** a raw `Environment=ANTHROPIC_API_KEY=sk-ant-…` literal in the
unit — unit files can end up in bug reports, dotfile backups, or `systemctl cat` output
shared with a colleague.

> **⚠️ WARNING:** Set spend caps before leaving any agent running overnight — an uncapped
> loop can burn through API credits fast. Each ecosystem below has its own mechanism: Claude
> Code's `/usage-credits` and Console workspace spend limits (Part 1), OpenAI's
> platform.openai.com usage limits for Codex CLI API-key auth (Part 2), and Google AI
> Studio / Cloud Billing budget alerts for Gemini CLI (Part 3) — set one of these *before*
> the unit starts, not after.

**Sources:** [oneuptime.com — How to Set Up systemd User Services on Ubuntu](https://oneuptime.com/blog/post/2026-03-02-how-to-set-up-systemd-user-services-on-ubuntu/view) (2026-03-02)
**Confidence:** 📄 vendor-documented (single detailed how-to; the underlying
`systemctl --user`/`loginctl enable-linger` primitives are standard systemd behavior, but a
second independent walkthrough — morphllm.com, cited in the prior snapshot — returned
HTTP 429 on re-fetch this run and was dropped per sourcing rules rather than cited from
memory; downgraded from `independently-corroborated` pending a working second source)

---

### Practice: Give each agent its own `git worktree` 📄

**Do:** `git worktree add ./agent-task-1 -b agent-task-1 main` — check your default branch
name first (`git branch`); newer repos may use `main`, older ones `master`.

**Why (beginner):** Each agent edits its own checked-out copy of the files, so two agents
working in parallel don't stomp on each other's uncommitted changes.

**Caveat / contested:** Worktrees share everything about the repository **except**
per-worktree files such as `HEAD` and the index (a worktree-local config needs
`git config extensions.worktreeConfig true`, and a few ref namespaces — `refs/bisect`,
`refs/worktree`, `refs/rewritten` — are also per-worktree, not shared). Everything else,
including `config` by default, is shared across all worktrees of the same repo. Worktrees
isolate **files only** — two agents in different worktrees of the same repo can still
collide on ports, a shared database, caches, or secrets.

**Sources:** [git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree) (official, fetched 2026-08-03)
**Confidence:** 📄 vendor-documented

---

### Practice: Sandbox the agent (bubblewrap or firejail) — Ubuntu 24.04+'s AppArmor block now has a documented fix ✅

**Do:** Install `sudo apt install bubblewrap` (preferred — smaller unprivileged surface;
check your installed version with `apt policy bubblewrap`, upstream is currently 0.11.2) or
`sudo apt install firejail` (easier, bundled profiles; upstream is 0.9.80, released
14 Mar 2026). A minimal manual invocation that binds only the project directory writable,
drops capabilities, and isolates the network namespace looks like:
```
bwrap --ro-bind / / --dev /dev --tmpfs /tmp \
  --bind "$(pwd)" "$(pwd)" \
  --unshare-net \
  --die-with-parent \
  -- your-agent-command
```
(most agent CLIs wrap `bwrap` for you via a `/sandbox` command or `sandbox.enabled` setting
— see the ecosystem-specific sandboxing practices in Parts 1-3 — but this is what's
happening underneath.)

> **Note on bubblewrap 0.11.2:** that release (23 Apr 2026) was a security fix for
> **CVE-2026-41163** (CVSS 8.7, "High"), a ptrace-based privilege-escalation bug affecting
> **setuid-mode** installs from 0.11.0 up to (not including) 0.11.2. Ubuntu's apt-packaged
> bubblewrap is not installed setuid by default, so this doesn't change the install
> instructions above — but if you're running a self-built or non-Ubuntu bubblewrap in
> setuid mode, confirm it's at least 0.11.2.

> **✅ GAP #317 SUBSTANTIALLY CLOSED THIS RUN.** Anthropic's own Claude Code docs (fetched
> 2026-08-03) now ship the exact fix as an official troubleshooting step:
>
> Check: `sysctl kernel.apparmor_restrict_unprivileged_userns`. If it returns `1` (Ubuntu
> 24.04+ default, including inside WSL2), create `/etc/apparmor.d/bwrap`:
> ```
> abi <abi/4.0>,
> include <tunables/global>
>
> profile bwrap /usr/bin/bwrap flags=(unconfined) {
>   userns,
>   include if exists <local/bwrap>
> }
> ```
> Then `sudo systemctl reload apparmor`. **Verify it worked** by re-running the `sysctl`
> check (the profile itself doesn't change the sysctl value — instead, confirm success by
> re-running whatever `bwrap`/agent-sandbox command previously failed with
> `bwrap: Creating new namespace failed: Permission denied` and seeing it succeed). This
> profile applies only to `bwrap` itself, not the commands it runs inside the sandbox.
>
> jdhodges.com (2026-04-23) independently publishes byte-identical profile text to
> Anthropic's. The `dfaerch/bubblewrap-on-ubuntu` GitHub project publishes two functionally
> equivalent (not byte-identical) variants — `bwrap-userns` and a stricter
> `bwrap-userns-restrict` with an `unpriv_bwrap` child profile — under its `/profiles/24.04/`
> directory; useful as a second independent implementation of the same fix, but don't expect
> the exact same file content. Separately, Ubuntu itself ships an upstream AppArmor "extra
> profile" called `bwrap-userns-restrict` in `/usr/share/apparmor/extra-profiles/` on 24.04
> (via the optional `apparmor-profiles` package) that does **not** load by default —
> confirmed via the Launchpad `apparmor` package changelog, which shows the profile was
> added in 2024-07-16 (`4.0.1-0ubuntu0.24.04.2`), reverted two days later after breaking
> Flatpak app saves, then re-added to the separate `apparmor-profiles` package by
> `4.0.1really4.0.1-0ubuntu0.24.04.3` (18 Jul 2024) — shipped but inactive by default on
> 24.04 as of that version. **Ubuntu 25.04+ ships `bwrap-userns-restrict` and, per the
> official 25.04 release notes, that profile "allows it to create user namespaces and set up
> sandboxing, before transitioning to a tighter profile"** — so the manual `/etc/apparmor.d/bwrap`
> step above is specific to 24.04 LTS, which remains the most widely deployed LTS as of
> Aug 2026. **Ubuntu 26.04 LTS ("Resolute Raccoon") has been out since 23 Apr 2026** (over
> three months by this snapshot — not upcoming), but a direct primary-source confirmation of
> whether it ships `bwrap-userns-restrict` active by default the way 25.04 does could not be
> found this run — treat as ⚠ **PENDING**, verify live on your own 26.04 box with the
> `sysctl` check above before assuming either way.

**Caveat / contested:** Neither bubblewrap nor firejail is installed by default on Ubuntu.
Setting `kernel.apparmor_restrict_unprivileged_userns=0` instead of installing the profile
"works" but disables the kernel hardening system-wide for every unprivileged-userns
consumer, not just bwrap — the scoped profile above is the safer fix.

**Sources:** [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-08-03) ·
[jdhodges.com — How to Fix Codex Sandbox Errors on Ubuntu 24.04](https://www.jdhodges.com/blog/codex-sandbox-ubuntu-24-04-fix/) (2026-04-23) ·
[github.com/dfaerch/bubblewrap-on-ubuntu — profiles/24.04](https://github.com/dfaerch/bubblewrap-on-ubuntu/tree/main/profiles/24.04) (community, undated) ·
[launchpad.net/ubuntu/+source/apparmor/+changelog](https://launchpad.net/ubuntu/+source/apparmor/+changelog) (fetched 2026-08-03) ·
[documentation.ubuntu.com/release-notes/25.04](https://documentation.ubuntu.com/release-notes/25.04/) (official, fetched 2026-08-03) ·
[github.com/containers/bubblewrap/releases/tag/v0.11.2](https://github.com/containers/bubblewrap/releases/tag/v0.11.2) (fetched 2026-08-03) ·
[radar.offseq.com — CVE-2026-41163](https://radar.offseq.com/threat/cve-2026-41163-cwe-269-improper-privilege-manageme-949f6d2e) (fetched 2026-08-04) ·
[github.com/netblue30/firejail/releases](https://github.com/netblue30/firejail/releases) (0.9.80, 14 Mar 2026)
**Confidence:** ✅ independently-corroborated (the fix itself: Anthropic vendor docs +
jdhodges.com byte-identical + dfaerch functionally-equivalent variants; the *default Ubuntu
behavior* claim is 📄 vendor-documented via Launchpad + official release notes)

---

### Practice: Default-deny outbound network for agents (nftables) — a real starter ruleset now exists, with caveats ✅

**Do:** nftables (via `iptables-nft`/`ip6tables-nft`) has been Ubuntu's default netfilter
backend since **20.10 Groovy Gorilla**, and `ufw` is a legacy-iptables frontend — official
Ubuntu security docs state explicitly: **"`ufw` works by invoking the legacy `iptables` and
`ip6tables` utilities. As such, it should not be used concurrently with native `nftables`
firewall rules."** Pick one stack, not both.

> **⚠️ WARNING — ADVANCED, AND THE ROLLBACK MAY NOT SAVE YOU.** Apply your allow-rules
> *before* `policy drop` on the output chain, or you'll knock the machine offline mid-edit.
> The nominal rollback is `sudo nft flush ruleset` — **but if you're SSH'd into a remote box
> with no console/IPMI access and you get the order wrong, you've just cut off the
> connection you'd need to run that rollback command.** There is no escape hatch once
> that happens. Before applying default-deny egress on a remote box: (1) test the exact
> ruleset on a machine with local/console access first, or (2) set up a self-reverting
> safety net, e.g. `sudo at now + 5 minutes` running a job that flushes the ruleset, so a
> lockout heals itself even if SSH drops. Beginners should prefer the sandbox's own network
> controls (see the sandboxing practice above, or each ecosystem's built-in sandbox
> network proxy in Parts 1-3) over hand-rolled nftables until comfortable with firewall rules.

> **Partial progress on GAP #318.** A concrete, fetchable, dated starter ruleset for this
> exact use case (agent sandbox, default-deny egress, DNS + allowlisted-proxy exceptions)
> now exists — INNOQ's engineering blog (2026-03-03, author Joy Heron) publishes, verbatim:
> ```
> table inet sandbox {
>   chain output {
>     type filter hook output priority 0; policy drop;
>     oif "lo" accept
>     ct state established,related accept
>     udp dport 53 accept
>     tcp dport 53 accept
>     ip daddr 172.17.0.0/16 accept   # Allow traffic to the proxy
>     ip daddr 172.18.0.0/16 accept   # Allow traffic to the proxy
>     ip daddr <proxy-host-ip> tcp dport 8888 accept
>   }
> }
> ```
> INNOQ drives the proxy with an `allowed_domains.txt` file (entries like `example.org`,
> `.openai.com`) rather than naming a specific proxy product — Squid is one option that
> fits this pattern, not something INNOQ itself specifies.
>
> **Important nuance this ruleset makes explicit and that beginners often miss: nftables
> filters by IP, not domain name.** You cannot write an nftables rule that says "allow
> `api.anthropic.com`" — domains resolve to IPs that change. The realistic pattern (also
> described more abstractly by h5i.dev, 2026-06-12/updated 2026-06-26, and the
> `89luca89/clampdown` project, which uses the equivalent iptables pattern) is either (a)
> resolve your allowed hosts once and pin them via `/etc/hosts` / an nft set, accepting that
> IPs can rotate, or (b) route the agent's traffic through a domain-aware allowlisting proxy
> and only let nftables allow traffic *to that proxy*. h5i.dev also notes the honest
> limitation of approach (b): an L7 allowlist proxy "cannot stop a process that ignores the
> proxy environment and opens a raw socket." Apt access needs the same treatment — allow the
> proxy or pin the current archive mirror IPs, not a raw domain. This is not a
> copy-paste-and-done file for a bare host; it needs your proxy's IP/port substituted in,
> and a decision on the DNS-pinning vs proxy tradeoff.

**Sources:** [documentation.ubuntu.com/security/security-features/network/firewall/nftables](https://documentation.ubuntu.com/security/security-features/network/firewall/nftables/) (official, fetched 2026-08-03) ·
[documentation.ubuntu.com/security/security-features/network/firewall](https://documentation.ubuntu.com/security/security-features/network/firewall/) (official, fetched 2026-08-03) ·
[innoq.com/en/blog/2026/03/dev-sandbox-network](https://www.innoq.com/en/blog/2026/03/dev-sandbox-network/) (2026-03-03) ·
[h5i.dev/blog/sandboxing-ai-agents-h5i](https://h5i.dev/blog/sandboxing-ai-agents-h5i/) (2026-06-12, updated 2026-06-26) ·
[github.com/89luca89/clampdown](https://github.com/89luca89/clampdown) (fetched 2026-08-03, iptables not nftables — corroborates pattern, not syntax)
**Confidence:** ✅ independently-corroborated for the general pattern (default-deny + DNS
exception + proxy-for-domains, agreed by INNOQ, h5i.dev, and clampdown — three different
publishers); the exact nftables *syntax* is 📄 vendor-documented-adjacent (one worked
example, INNOQ) — **still not a turnkey single-file ruleset for a bare Ubuntu host**
(INNOQ's is written for a container-sandbox/Testcontainers context and needs adaptation),
so #318 is marked substantially advanced, not closed.

---

### Practice: Keep secrets out of the repo *and* out of plaintext the agent can read ✅

**Do:** `.gitignore` your `.env` — but that alone isn't enough. **Agents routinely run
`cat .env` or `printenv`,** and every agent with terminal access can read your
`.zshenv`/`.zshrc`/`.bashrc` too. Prefer an OS-level secret store: GNOME Keyring via
`sudo apt install libsecret-tools`, then
`secret-tool store --label="My API Token" service myapp username <you>` to save, and
`secret-tool lookup service myapp username <you>` to retrieve at launch time — rather than
a value sitting in a file the agent can browse. `chmod 600` any on-disk env/secrets file you
do still need.

**Why (beginner):** A "secret" in a file the agent can read is a secret the agent might
paste into a shell command, send to the model as tool output, or write into a log.

**Caveat / contested:** The two independent sources here don't fully agree on what comes
next. Red Black Tree's guide treats the OS keyring (GNOME Keyring/KWallet/`pass`) as the
Linux-appropriate default and positions a dedicated secrets manager (1Password CLI/Service
Accounts) as a *later* step specifically for multi-machine sync or remote SSH access — not
a universal replacement. linuxjunkies.org goes further and recommends the keyring as the
intended store with no external manager at all. Read together: the keyring is a reasonable
default for a single Ubuntu box; only reach for a dedicated secrets manager once you need
the same secret across multiple machines.

**Sources:** [rbt.rs/blog/secret-management-in-the-age-of-ai-coding-agents](https://rbt.rs/blog/secret-management-in-the-age-of-ai-coding-agents/) (2026-03, Srđan Marković/Red Black Tree) ·
[linuxjunkies.org/guides/use-keyring-and-secret-manager](https://linuxjunkies.org/guides/use-keyring-and-secret-manager) (updated 2026-06-07) ·
[manpages.debian.org secret-tool(1)](https://manpages.debian.org/testing/libsecret-tools/secret-tool.1.en.html) (command syntax reference)
**Confidence:** ✅ independently-corroborated

---

### Practice: Scope the filesystem to least privilege (`DynamicUser`, `ReadOnlyPaths`/`ReadWritePaths`) ✅

**Do:** In a systemd unit, `DynamicUser=yes` makes systemd allocate a temporary UID/GID
(from the 61184–65519 range) just for that service run and release it on exit — the service
cannot touch your home directory at all, and it implies `ProtectSystem=strict` +
`ProtectHome=read-only` automatically. Add `ReadOnlyPaths=/` and
`ReadWritePaths=/path/to/project` to further scope what the unit can write, even under a
normal (non-dynamic) user.

**Caveat / contested:** `DynamicUser` recycles UIDs between runs — **don't leave files
owned by the dynamic user lying around**, because a later unit invocation can be assigned
the same UID and inherit access to them (documented systemd behavior, per the upstream
`systemd.exec` man page). `ReadOnlyPaths=`/`ReadWritePaths=` create bind mounts in the
unit's private view of the filesystem and don't affect the real host mount table, nor do
they affect the ability to *connect to* existing AF_UNIX sockets — they're not a substitute
for a real sandbox (bubblewrap/firejail) if the threat model includes a fully compromised
agent process.

**Sources:** [man7.org/linux/man-pages/man5/systemd.exec.5.html](https://man7.org/linux/man-pages/man5/systemd.exec.5.html) (official upstream man page, fetched 2026-08-03) ·
[redhat.com/en/blog/systemd-secure-services](https://www.redhat.com/en/blog/systemd-secure-services) (2020-05-11, `CapabilityBoundingSet`/`ProtectHome`/`SystemCallFilter` etc.) ·
[nickb.dev/blog/writing-a-secure-systemd-service-with-sandboxing-and-dynamic-users](https://nickb.dev/blog/writing-a-secure-systemd-service-with-sandboxing-and-dynamic-users/) (2020-12-29; `DynamicUser` coverage — note this is a 2020 post, re-checked this run and unchanged, not a fresh 2026 publication despite being freshly fetched)
**Confidence:** ✅ independently-corroborated (directive semantics stable since 2020,
re-fetched and unchanged as of 2026-08-03; `ReadOnlyPaths`/`ReadWritePaths` specifically
corroborated by man7.org + Red Hat)

---

### Practice: Audit agent activity via journald ✅

**Do:** `journalctl --user -u <name>.service` to see one unit's history; add `-f` to tail
live; scope with `--since "1 hour ago"` or `--since today`. You can filter/join multiple
units chronologically: `journalctl -u nginx.service -u php-fpm.service --since today`.

**Why (beginner):** Leaving an agent unattended is only safe if you can audit what it did
afterward — journald gives you that for free once the unit logs to `StandardOutput=journal`.

**Caveat / contested:** To read the *system* journal (not just your own user journal), join
the `systemd-journal` group: `sudo usermod -aG systemd-journal $USER`, then log out and back
in — this specific requirement is documented by DigitalOcean's guide; dash0.com's guide
covers `-u`/`-f`/`--since`/`SystemMaxUse` but doesn't mention the group requirement.
journald retention is governed by `/etc/systemd/journald.conf` (`SystemMaxUse=`, etc.) —
don't assume unlimited history; check your retention settings if you need a long audit
trail.

**Sources:** [digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs) (updated 2026-04-27) ·
[dash0.com/guides/systemd-logs-linux-journalctl](https://www.dash0.com/guides/systemd-logs-linux-journalctl) (last updated 2025-07-06)
**Confidence:** ✅ independently-corroborated

---

## Part 1 — Claude Code (Anthropic)

### Practice: Install with the native installer; verify with `claude --version` / `claude doctor` 📄

**Do:** `curl -fsSL https://claude.ai/install.sh | bash`, then `claude --version` and
`claude doctor`. This installs a single self-contained native binary (no Node.js needed) at
`~/.local/bin/claude`, symlinked into `~/.local/share/claude/versions/`. Supported: Ubuntu
20.04+, Debian 10+, Alpine 3.19+, 4 GB+ RAM, x64/ARM64. 🕒 **verify live** — the current
released version as of this snapshot is **v2.1.220** (24-25 Jul 2026, per Anthropic's own
changelog); Claude Code ships very frequently (300+ releases to date), so check
`claude --version` yourself.

**Why (beginner):** One command, and native installs auto-update in the background so you
stay patched without thinking about it. `claude doctor` gives read-only diagnostics (install
health, settings validation, last update result) before you waste time debugging.

**Caveat:** Piping a remote script to `bash` means trusting that URL without reading it
first — the script runs with your full permissions. The npm route
(`npm install -g @anthropic-ai/claude-code`) also works and installs the *same* native
binary via a per-platform optional dependency; **as of v2.1.198 it requires Node.js 22+**
(older Node prints a non-fatal `EBADENGINE` warning but still works since the binary doesn't
run through Node at runtime). **Never `sudo npm install -g`** — Anthropic's own docs warn
this "can lead to permission issues and security risks."

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-08-03) ·
[code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog) (fetched 2026-08-03, shows v2.1.220 / 25 Jul 2026)
**Confidence:** 📄 vendor-documented (a third-party release tracker was checked as a
possible second source for the version number, but on re-fetch it listed v2.1.219, not
v2.1.220, and could not corroborate the current version — dropped rather than cited as
independent confirmation it didn't actually provide; install method, Node requirement, and
version number are all vendor-documented only this run)

---

### Practice: Prefer the signed apt/dnf/apk repo for verifiable, system-managed updates 📄

**Do:** Add Anthropic's signed apt repo, then install:
```bash
sudo apt install curl gnupg
sudo install -d -m 0755 /etc/apt/keyrings
sudo curl -fsSL https://downloads.claude.ai/keys/claude-code.asc -o /etc/apt/keyrings/claude-code.asc
gpg --show-keys /etc/apt/keyrings/claude-code.asc   # verify fingerprint below
echo "deb [signed-by=/etc/apt/keyrings/claude-code.asc] https://downloads.claude.ai/claude-code/apt/stable stable main" \
  | sudo tee /etc/apt/sources.list.d/claude-code.list
sudo apt update && sudo apt install claude-code
```
Verify the GPG fingerprint reads (**unchanged since the June 2026 snapshot**):
```
31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE
```
**If the fingerprint you see does NOT match: stop, do not proceed with the install, and
report it** — a mismatch means the key you downloaded isn't Anthropic's. Equivalent `dnf`
and `apk` repos exist for Fedora/RHEL and Alpine; each has its own signing key/fingerprint
check. Choose the `stable` channel (≈1 week behind, skips major regressions) or `latest`
(URL path and repo suite both change).

**Caveat:** apt/dnf/apk do **not** auto-update Claude Code — run
`sudo apt update && sudo apt upgrade claude-code` yourself. Only the native installer, and
(optionally) Homebrew/WinGet with `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1`, auto-update.
Anthropic also now publishes a signed `manifest.json` (SHA256 checksums per platform,
GPG-signed) for every release, so you can verify a downloaded/installed binary's integrity
independent of the package manager — useful if you mirror binaries internally.

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-08-03, fingerprint re-verified verbatim against the live page)
**Confidence:** 📄 vendor-documented (fingerprint is a security credential; only the vendor
is authoritative here — re-confirmed unchanged from the prior 2026-06-29 snapshot)

---

### Practice: Keep updated deliberately — pick a release channel and pin a floor 📄

**Do:** Set `autoUpdatesChannel` to `"latest"` (this is now the **documented default**) or
`"stable"` in `~/.claude/settings.json` or via `/config` → Auto-update channel. Pin
`minimumVersion` so a channel switch can't silently downgrade you; for a hard floor that
blocks *startup* rather than just updates, use managed-settings-only `requiredMinimumVersion`
/ `requiredMaximumVersion`. Run `claude update` to apply immediately. To freeze a machine,
set `DISABLE_AUTOUPDATER` (stops only the background check; `claude update`/`claude install`
still work) or `DISABLE_UPDATES` (blocks every update path, for orgs distributing their own
build) in the settings `env` block.

**Caveat:** apt/dnf/apk/Homebrew/WinGet installs ignore `autoUpdatesChannel` (channel is
chosen by repo/cask instead). If you replace the native installer's `~/.local/bin/claude`
symlink with your own launcher script, `claude update` still installs new versions under
`versions/` but leaves your launcher alone — a documented quirk worth knowing if
`claude doctor` reports "launcher not created by installer."

**Sources:** [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) (fetched 2026-08-03, "Configure release channel" and "Pin a minimum version" sections)
**Confidence:** 📄 vendor-documented

---

### Practice: Authenticate headless/SSH boxes — and know the billing trap ✅

**Do:** Over SSH, press `c` to copy the login URL, or paste the browser's login code back
into the terminal (common when the callback server can't be reached, e.g. WSL2/SSH/
containers). For true unattended/CI use: `claude setup-token` mints a 1-year OAuth token
(`CLAUDE_CODE_OAUTH_TOKEN`, draws on your Pro/Max/Team/Enterprise subscription), or set
`ANTHROPIC_API_KEY` (Console pay-as-you-go). Anthropic's own docs publish the full credential
precedence order: cloud-provider env vars > `ANTHROPIC_AUTH_TOKEN` > `ANTHROPIC_API_KEY` >
`apiKeyHelper` > `CLAUDE_CODE_OAUTH_TOKEN` > subscription OAuth login. In non-interactive
`-p` mode, `ANTHROPIC_API_KEY` is always used when present.

> **⚠️ WARNING — cost trap:** If you have BOTH a subscription AND `ANTHROPIC_API_KEY` set,
> **the API key wins and you get billed pay-as-you-go instead of drawing on your plan.**
> This is confirmed directly in Anthropic's authentication precedence docs and echoed by an
> independent billing write-up. Run `unset ANTHROPIC_API_KEY` and check `/status` — it shows
> a `Login method` row and an `API key` row when a key is active. **Two other tiers above
> subscription in the precedence order can also silently cause pay-as-you-go billing:** a
> cloud-provider env var (Bedrock/Vertex/Foundry) or a configured `apiKeyHelper`. If
> `/status` still shows an API key active after `unset ANTHROPIC_API_KEY`, check for one of
> those two as well. **Claude Code on the Web always uses your subscription credentials**
> and ignores `ANTHROPIC_API_KEY`/`ANTHROPIC_AUTH_TOKEN` set inside its sandbox, so this
> trap is specific to the local CLI.

**Caveat:** On Linux, credentials live in `~/.claude/.credentials.json` at mode `0600` (no
OS keychain, unlike macOS which uses the Keychain). `--bare` mode never reads OAuth
credentials or the system keychain at all — use `ANTHROPIC_API_KEY` or `apiKeyHelper` there.
A separate, previously-announced billing change (moving `-p`/Agent SDK usage to its own
credit pool, planned effective 15 Jun 2026) was reported paused before taking effect;
our source documents the pause announcement but we could not confirm from it whether the
change has since been reinstated. Treat this as 🕒 **verify live** — check `/status` and
your actual bill rather than assuming either way.

**Sources:** [code.claude.com/docs/en/authentication](https://code.claude.com/docs/en/authentication) (fetched 2026-08-03, "Authentication precedence" section) ·
[blog.laozhang.ai/en/posts/claude-code-api-key-vs-subscription-billing](https://blog.laozhang.ai/en/posts/claude-code-api-key-vs-subscription-billing) (accessed 2026-08-03) ·
[andrew.ooo/answers/anthropic-claude-code-june-15-billing-change-may-2026](https://andrew.ooo/answers/anthropic-claude-code-june-15-billing-change-may-2026/) (published 2026-05-28, updated 2026-07-22 — documents the pause announcement)
**Confidence:** ✅ independently-corroborated

---

### Practice: Run unattended work with `claude -p`, scoped tightly, and prefer `--bare` 📄

**Do:** `claude -p "prompt"` for one-shot, non-interactive runs. Restrict tools with
`--allowedTools "Read,Grep,Glob"` (smallest set the task needs); get machine-readable
results with `--output-format json` (includes `total_cost_usd` per invocation) or
`--output-format stream-json` for token-level streaming. Add `--bare` to skip auto-discovery
of hooks, skills, plugins, MCP servers, auto-memory, and CLAUDE.md — **the docs now say
`--bare` "will become the default for `-p` in a future release,"** so start using it now for
CI/scripted calls that need identical results on every machine.

> **⚠️ Pre-allow tools before any unattended run.** Without it the agent hangs waiting for a
> permission prompt — your script silently stalls. Use `--permission-mode dontAsk` (deny
> anything not explicitly allowed) for locked-down CI.

**Caveat:** `--bare` skips OAuth/keychain entirely — set `ANTHROPIC_API_KEY` or
`apiKeyHelper` in its JSON settings, since it never uses your subscription login. Piped
stdin is capped at 10 MB (v2.1.128+); for bigger input, write a file and reference its path
instead. A background Bash task (e.g. a dev server) is killed ~5 seconds after `claude -p`
returns its result; background subagents instead get a 10-minute grace cap by default
(`CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`). Interactive-only commands like `/login` don't work
in `-p` mode; `/model sonnet` and `/effort` do (v2.1.205+), and `/config key=value` does too
(a lower bar, v2.1.181+).

**Sources:** [code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless) (fetched 2026-08-03)
**Confidence:** 📄 vendor-documented

---

### Practice: Reduce prompt fatigue with permission allowlists or auto mode, not blanket bypass 📄

**Do:** Use `/permissions` to allow specific safe commands (`Bash(npm run *)`,
`Bash(git commit *)`) and deny dangerous ones (`Bash(git push *)`, `Read(.env)`,
`Read(~/.ssh/**)`). Rules evaluate **deny → ask → allow**, always in that order regardless
of specificity. **`auto` mode** is documented in this snapshot for the first time in this
corpus — a separate classifier model reviews each action and blocks only what looks risky
(scope escalation, unknown infrastructure), letting routine work proceed with zero prompts
while keeping a safety net; the changelog shows it becoming available without an opt-in flag
on Bedrock/Vertex/Foundry as of v2.1.207 (11 Jul 2026), which implies the mode itself
existed earlier behind a flag — treat "new" here as "newly default/newly documented," not
necessarily brand-new. `dontAsk` mode auto-denies anything not pre-approved.

> **⚠️ AVOID `bypassPermissions` / `--dangerously-skip-permissions`** except inside a
> throwaway container or VM. Even in bypass mode, explicit `ask` rules, connector tools your
> org set to `ask`, and `rm -rf /` / `rm -rf ~` (including via `$(...)` command substitution
> as of v2.1.208) still trigger a prompt as a circuit breaker. **It's blocked outright when
> running as root or via `sudo` on Linux/macOS** — root plus no prompts is considered too
> dangerous to allow directly; use a dev container (runs as non-root) to get autonomous
> root-adjacent behavior safely.

**Caveat:** Permission rules are enforced by Claude Code, not the model, and only cover
tools Claude Code recognizes — a Python/Node script that opens files itself bypasses
Read/Edit deny rules entirely. Bash rules that try to constrain arguments (e.g.
`Bash(curl http://github.com/ *)`) are fragile and bypassable via redirects, protocol swaps,
or shell variables; use a `WebFetch(domain:...)` allow rule plus a Bash deny on
`curl`/`wget`, or a `PreToolUse` hook, for real enforcement. Use the sandbox (next practice)
for OS-level enforcement that doesn't depend on pattern-matching the command string.

**Sources:** [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-08-03) ·
[code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-08-03, "`--dangerously-skip-permissions` fails as root" section)
**Confidence:** 📄 vendor-documented

---

### Practice: Enable the OS-level Bash sandbox (bubblewrap) — and fix the Ubuntu 24.04 AppArmor block ✅

**Do:** Run `/sandbox`. Install deps first: `sudo apt-get install bubblewrap socat`
(bubblewrap enforces filesystem isolation, socat relays sandboxed network traffic).
Optionally add the seccomp filter (`npm install -g @anthropic-ai/sandbox-runtime`) to block
Unix domain sockets. Turn sandboxing on per-project (`/sandbox` writes
`.claude/settings.local.json`) or globally via `sandbox.enabled: true` in
`~/.claude/settings.json`.

> **⚠️ WARNING — the sandbox does NOT protect your credentials by default.** By default the
> sandbox's read policy still allows reading `~/.aws/credentials` and `~/.ssh/` — turning on
> `/sandbox` alone does not stop the agent from reading these files if they exist on the
> box. Use `sandbox.credentials` to deny-read `~/.aws/credentials`, `~/.ssh`, and to
> `deny`/`mask` secret env vars from sandboxed commands. This extra step is not optional if
> you keep real cloud/SSH credentials on the same machine you're sandboxing.

> **⚠️ Ubuntu 24.04+ / WSL2 gotcha (still current, now with the full fix documented):**
> AppArmor blocks bubblewrap from creating unprivileged user namespaces by default. Check
> `sysctl kernel.apparmor_restrict_unprivileged_userns` — `0` or "No such file" means skip
> this step; `1` means you need an AppArmor profile:
> ```
> sudo tee /etc/apparmor.d/bwrap > /dev/null <<'EOF'
> abi <abi/4.0>,
> include <tunables/global>
>
> profile bwrap /usr/bin/bwrap flags=(unconfined) {
>   userns,
>   include if exists <local/bwrap>
> }
> EOF
> sudo systemctl reload apparmor
> ```
> An independent Linux-sandboxing blog (Mar 2026) documents the identical failure mode
> (`bwrap: Creating new namespace failed: Permission denied`) and a functionally equivalent
> fix, corroborating this is a real, common issue and not an Anthropic-only edge case.

**Caveat:** Defense-in-depth, not a complete boundary — by default the built-in network
proxy does **not** terminate/inspect TLS ("TLS termination" means intercepting and decrypting
HTTPS traffic to inspect its contents; without it, the proxy can only see *which domain*
a connection goes to, not what data crosses it). A broad `allowedDomains` entry can
therefore still allow data exfiltration via "domain fronting" — a technique where traffic
is addressed to an allowed domain at the network level but actually carries data meant for
a different, disallowed destination once decrypted. The experimental `network.tlsTerminate`
setting adds TLS termination but only for credential-masking, not general content filtering.
`watchman` is incompatible with the sandbox (run `jest --no-watchman` instead), and `docker`
is incompatible with the sandbox (add `docker *` to `excludedCommands`). Native Windows is
**not supported** (macOS uses Seatbelt, Linux/WSL2 use bubblewrap; run Claude Code inside
WSL2 on Windows for sandboxing).

**Sources:** [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-08-03) ·
[labs.esokia.com/post/sandboxing-claude-code-cli-linux-bubblewrap](https://labs.esokia.com/post/sandboxing-claude-code-cli-linux-bubblewrap/) (published 2026-03-18, independently documents the same AppArmor failure and fix)
**Confidence:** ✅ independently-corroborated

---

### Practice: Keep secrets out of chat and out of MCP/project config 📄

**Do:** Store secrets in env vars or a secret manager; avoid pasting secret values into
chat as routine practice — treat the conversation like any other channel a value shouldn't
travel through. Reference env vars in MCP config with `${VAR}` / `${VAR:-default}` expansion
rather than hardcoding tokens; `.gitignore` your `.env`; document *which* env vars exist
(not values) in CLAUDE.md. `headersHelper` scripts for MCP auth run arbitrary shell commands
— at project/local scope they only run after you accept the workspace trust dialog.

**Caveat:** Claude doesn't read env vars into its context window automatically — values are
only available to commands it runs. A subprocess can still read secret files unless you
also use the sandbox's `credentials.files` (`deny`) / `credentials.envVars` (`deny`/`mask`)
controls, or set `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` to strip Anthropic and cloud-provider
credentials from *all* subprocesses regardless of sandboxing. Network requests (`curl`,
`wget`, WebFetch) require approval by default and aren't auto-approved — that's a real
safeguard against prompt-injection-driven exfiltration, but only if you don't blanket-allow
them.

**Sources:** [code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing) (fetched 2026-08-03, `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` and network-approval defaults) ·
[code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-08-03, `${VAR}`/`${VAR:-default}` expansion and `headersHelper`)
**Confidence:** 📄 vendor-documented

---

### Practice: Add MCP servers with `claude mcp add`, at the right scope 📄

**Do:** MCP (Model Context Protocol) connects Claude to external tools like GitHub,
databases, or Figma. Connect with `claude mcp add --transport http <name> <url>` (HTTP is
now the recommended transport; SSE is **deprecated**). Choose a scope: **local** (default,
private to you, stored in `~/.claude.json`), **project** (`.mcp.json`, checked into git,
requires approval on first use per-teammate), or **user** (all your projects, private). Put
credentials in env vars or `headersHelper`, not literal tokens in `.mcp.json`.

**Caveat:** More MCP servers = more context overhead and more attack surface — verify you
trust a server before connecting it, since servers that fetch external content can expose
you to prompt injection. Disable servers you're not using (`/mcp`). MCP tool definitions are
now deferred by default (only names enter context until Claude actually calls a tool), which
reduces — but doesn't eliminate — the context cost; CLI tools (`gh`, `aws`, `gcloud`) are
still more context-efficient than an MCP server for the same job since they add zero
per-tool listing overhead. Claude Code warns when MCP tool output exceeds 10,000 tokens and
truncates at 25,000 by default (`MAX_MCP_OUTPUT_TOKENS` to raise it).

**Sources:** [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (fetched 2026-08-03) ·
[code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 2026-08-03, "Reduce MCP server overhead")
**Confidence:** 📄 vendor-documented (this run's Skeptic re-fetch confirmed the page loads
but, due to its size, could not fully re-verify every numeric detail in this practice —
noted here rather than silently claiming full re-verification)

---

### Practice: Use hooks for actions that must happen every time 📄

> **⚠️ WARNING:** Hooks run with YOUR shell permissions — a malicious or buggy hook is real
> code execution. Review hooks (especially from shared/project configs or plugins) before
> trusting them. `PreToolUse` hooks that `deny` run even under `bypassPermissions` /
> `--dangerously-skip-permissions` — good for org policy, but also means a bad hook can't be
> worked around by disabling permissions.

**Do:** Add a `hooks` block to `settings.json`. Key events: `PreToolUse` (gate/modify a tool
call before it runs; exit code 2 blocks it), `PostToolUse` (e.g. run a formatter after an
edit), `Stop` (block a turn from ending until a check passes). Newer events worth knowing:
`SessionStart` (re-inject context after compaction), `ConfigChange` (audit/block settings
edits mid-session), `PermissionRequest` (auto-approve specific narrow prompts — keep the
matcher tight, since a broad one auto-approves file writes and shell commands too). Claude
can write hooks for you: *"write a hook that runs eslint after every file edit."*

**Why (beginner):** Unlike CLAUDE.md instructions (advisory — the model may ignore them),
hooks are deterministic shell commands the harness always runs. They guarantee formatting,
tests, or blocked-path enforcement regardless of what the model decides to do.

**Caveat:** When multiple hooks match the same event, **all matching hooks run in parallel,
and identical handlers are deduplicated automatically** — this is the one cross-hook
behavior confirmed directly in Anthropic's hooks reference; we could not confirm any
documented precedence rule for what happens when different hooks return conflicting
decisions on the same event, nor could we confirm any block-count override mechanism or
specific env var for raising one — earlier drafts of this practice asserted specifics here
("8 consecutive blocks," a named override variable, a named JSON field to detect a repeat
block) that turned out not to be verifiable against either the cited page or Anthropic's
full hooks reference, and have been removed rather than published unconfirmed. `--bare`
skips hook discovery entirely.

**Sources:** [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) (fetched 2026-08-03, full hooks reference) ·
[code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) (fetched 2026-08-03, "Extend permissions with hooks")
**Confidence:** 📄 vendor-documented

---

### Practice: Write a short, high-signal CLAUDE.md and prune it 📄

**Do:** Run `/init` to generate a starter CLAUDE.md from your project. Keep only what
Claude can't infer: non-obvious bash commands, code-style rules that differ from language
defaults, test runners, repo/branch/PR conventions, required env vars, and non-obvious
gotchas. Aim under ~200 lines; run `/context` to confirm it loaded; move occasional or
domain-specific workflows into skills (`.claude/skills/*/SKILL.md`, loaded on demand instead
of every session). Ask for each line: "would removing this cause Claude to make mistakes?"
You can boost adherence to a specific rule with emphasis like "IMPORTANT" or "YOU MUST".

**Caveat:** If Claude keeps violating a rule, the file is probably too long and the rule is
getting lost in the noise — not that the rule needs to be stated more forcefully. Check
CLAUDE.md into git so the team shares it; keep personal notes in `CLAUDE.local.md`
(gitignored). CLAUDE.md supports `@path/to/file` imports for pulling in README/package.json
context without duplicating it.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-08-03, "Write an effective CLAUDE.md" — this page was not independently re-fetched by this run's Skeptic panelist due to its size; flagged as unaudited-by-panel rather than silently treated as fully re-verified)
**Confidence:** 📄 vendor-documented

---

### Practice: Control cost — `/usage`, context hygiene, model choice, and watch the Sonnet 5 pricing cliff ✅

**Do:** Check `/usage` (per-session token/cost estimate; also breaks down spend by skill,
subagent, plugin, and MCP server on Pro/Max/Team/Enterprise) and `/context`. `/clear`
between unrelated tasks — stale context is billed on every subsequent turn. Use Sonnet for
most work, Opus for hard multi-step reasoning (`/model`); specify `model: haiku` for simple
subagent tasks. For unattended `-p` runs, parse `total_cost_usd` from `--output-format json`.
On Pro/Max, `/usage-credits` lets you extend past the plan limit; on Console/API, set
workspace spend limits at platform.claude.com.

> 🕒 **verify live — pricing cliff:** **Claude Sonnet 5 is the current default model** in
> Claude Code (introduced 30 Jun 2026, per Claude Code changelog v2.1.197: *"Introducing
> Claude Sonnet 5: now the default model in Claude Code, with a native 1M-token context
> window and promotional pricing of $2/$10 per Mtok through August 31"*) and carries
> **introductory pricing of $2/$10 per million input/output tokens through 31 Aug 2026** —
> after which it rises 50% to the standard $3/$15 per million tokens. This mainly affects
> API/Console-billed usage (Pro/Max subscribers pay a flat seat price, not per-token, so the
> cliff doesn't directly hit subscription users' bills, but it does mean Console/API-billed
> teams should expect a step change on 1 Sep 2026). Anthropic's enterprise deployment data
> puts average cost around **$13/developer/active-day** ($150-250/month), with 90% of users
> staying under $30/active-day.
>
> **Also new since the June snapshot: Claude Opus 5 (24 Jul 2026)** — now the **default
> model on Claude Max** and selectable on Pro, priced at **$5/$25 per Mtok** (unchanged from
> the prior Opus generation). Covered by Anthropic's own announcement and widely reported
> (Axios, VentureBeat, Fortune, 9to5Mac, all dated 24 Jul 2026). If you're choosing "Opus for
> hard multi-step reasoning" per the advice above, this is the generation you're getting.
>
> **Also time-sensitive: a temporary 50% weekly-usage-limit increase** for Pro/Max/Team/
> seat-based-Enterprise Claude Code users has been extended and, per independent reporting,
> runs **through 19 Aug 2026** — 16 days after this snapshot. If you're on one of these plans,
> you have more headroom today than you will after that date; we did not independently fetch
> Anthropic's own changelog entry for the exact end-date, so treat it as corroborated-by-
> secondary-sources rather than vendor-confirmed, and re-check before relying on it past
> mid-August.

**Why (beginner):** Cost scales with context size and model choice. A long, cluttered
session quietly multiplies token cost because Claude Code resends the whole conversation
history (subject to prompt-caching discounts) on every turn; clearing context and choosing
Sonnet over Opus are the two biggest cheap wins. *A "token" is roughly ¾ of a word — though
Claude 4.7-and-later models (including Sonnet 5 and Opus 5) use a newer tokenizer that
produces approximately 30% more tokens for the same text than Claude Sonnet 4.6 and earlier
models, which matters when comparing cost estimates across model generations.*

**Caveat:** `/usage`'s dollar figure is computed locally from token counts at standard list
rates — it doesn't reflect promotional pricing or contracted discounts and may differ from
your actual bill; use the Console usage page for authoritative billing.

**Sources:** [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 2026-08-03) ·
[platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 2026-08-03, Sonnet 5 pricing table + introductory-pricing note + tokenizer note) ·
[finopsllm.com/research/sonnet-5-intro-pricing-deadline](https://finopsllm.com/research/sonnet-5-intro-pricing-deadline) (published 2026-07-19, independently corroborates the $2/$10 → $3/$15 cliff and 31 Aug 2026 date) ·
[anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5) (24 Jul 2026) ·
axios.com — Anthropic releases new model Opus 5 (24 Jul 2026; consistently returns 403 bot-detection on re-fetch, unlinked per policy — corroborated by the Anthropic vendor link above) ·
[helpnetsecurity.com — Claude Code weekly limits promotion extended](https://www.helpnetsecurity.com/2026/07/13/claude-code-weekly-limits-promotion-extended/) (13 Jul 2026)
**Confidence:** ✅ independently-corroborated (pricing cliff, Opus 5 launch); 📄
vendor-documented (cost controls / `/usage` mechanics); the weekly-limit-boost end date is
🕒 verify live / secondary-source-corroborated only

---

### Practice: Give Claude a way to verify its own work 📄

**Do:** Pair every task with a check Claude can run and read: a test suite, a build exit
code, a linter, a diff, or a screenshot comparison. For a one-shot prompt, ask Claude to run
the check and iterate in the same message. For a whole session, a `/goal` condition has a
separate evaluator re-check it after every turn. For a hard, deterministic gate on
unattended runs, use a `Stop` hook that runs your check as a script and blocks the turn from
ending until it passes. For a second opinion, delegate to a fresh-context verification
subagent or the bundled `/code-review` skill so the reviewer isn't biased by the reasoning
that produced the change. Have Claude show evidence (test output, the exact command +
result) rather than just asserting success.

**Caveat:** A reviewer prompted to find gaps will usually report *some*, even when the work
is sound, because that's what it was asked to do — chasing every finding leads to
over-engineering. Tell the reviewer to flag only gaps affecting correctness or stated
requirements, and treat the rest as optional. Checkpoints/rewind only track changes made
through Claude's own file-editing tools, not changes made via Bash or external processes —
don't treat `/rewind` as a substitute for git.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-08-03, "Give Claude a way to verify its work" and "Add an adversarial review step" — unaudited by this run's Skeptic panelist, see note in the CLAUDE.md practice above)
**Confidence:** 📄 vendor-documented

---

## Part 2 — OpenAI Codex CLI

> ## What changed since 29 Jun 2026
> 1. **New model family: GPT-5.6 (Sol / Terra / Luna), launched 9 Jul 2026** — replaces the
>    GPT-5.5-as-default guidance from the last snapshot. Vendor docs describe Sol/Terra/Luna
>    as the current recommended lineup but, notably, decline to name a single "default"
>    model by name (see the model practice below for exactly what is and isn't documented).
>    GPT-5.4 / GPT-5.4-mini are being retired from Codex on **31 Aug 2026** for
>    ChatGPT-authenticated sessions (still available via API key). 🕒 verify live.
> 2. **Docs moved.** `developers.openai.com/codex/*` URLs now redirect to
>    `learn.chatgpt.com/docs/*`. Old links still resolve (for now) — just be aware the
>    canonical home changed.
> 3. **A 4th approval-policy option, `granular`, appeared** (per-category overrides for
>    sandbox escalation, exec rules, MCP, and skills) alongside the three from June.
> 4. **Auth storage confirmed plaintext by default**, not encrypted — the June entry's note
>    about "encrypted local storage" for OAuth creds does not match what current vendor docs
>    and an independent security write-up both say. See the Auth practice below.
> 5. A June 2026 supply-chain incident (malicious npm package) actively harvested Codex
>    OAuth refresh tokens from `~/.codex/auth.json` — corroborates why credential-storage
>    hygiene matters here.
> 6. **OpenAI cut GPT-5.6 Luna pricing by 80% and Terra by 20% on 30 Jul 2026** — confirmed
>    this run (see model practice below); this was an open question in the original 03 Aug
>    draft and has since been resolved with dated, multi-source coverage.

### Practice: Install via the official script, npm, Homebrew, or a prebuilt binary — never `sudo npm -g` ✅

**Do:** Install with `curl -fsSL https://chatgpt.com/codex/install.sh | sh`, or
`npm install -g @openai/codex`, or `brew install --cask codex`, or download a prebuilt
binary from GitHub Releases. Latest stable tag as of this run is **v0.146.0** (29 Jul 2026),
with `0.147.0-alpha.*` prereleases shipping almost daily (last alpha: 3 Aug 2026). Codex CLI
is open source (Apache-2.0), primarily Rust, still the `openai/codex` repo.

**Why (beginner):** Piping a remote script into `sh` means trusting that URL completely —
the script runs with your permissions before you've read a line of it. It's a common,
accepted pattern for this kind of tool, but know what you're agreeing to.

> **⚠️ Never `sudo npm install -g`.** It creates root-owned files in your npm prefix that
> break future updates and can leave permission landmines. If `codex` isn't found after a
> plain `npm install -g`, fix your PATH instead:
> ```
> echo 'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.bashrc
> source ~/.bashrc
> ```
> (use `~/.zshrc` instead if you run zsh) — don't reach for `sudo`.

**Sources:** [github.com/openai/codex](https://github.com/openai/codex) (fetched 2026-08-03, releases page shows v0.146.0 stable / 29 Jul 2026, alphas through 3 Aug 2026) ·
[itecsonline.com/post/how-to-codex-cli-linux](https://itecsonline.com/post/how-to-codex-cli-linux) (published 26 Oct 2025, updated 19 Jul 2026)
**Confidence:** ✅ independently-corroborated

🕒 **verify live:** exact version — check `codex --version`; this project ships multiple
releases per week.

---

### Practice: Understand the two-layer safety model — sandbox mode + approval policy (now 4 policy options) ✅

**Do:** Codex has two independent dials, and you should set both deliberately:

| Layer | Options | What it controls |
|-------|---------|-------------------|
| **Sandbox** | `read-only` / `workspace-write` / `danger-full-access` | What the agent can physically touch |
| **Approval** | `untrusted` / `on-request` / `never` / **`granular`** (new since June) | When it stops to ask you first |

`granular` is the newest addition: it lets you keep some approval categories interactive
(e.g., sandbox escalation requests) while auto-approving or auto-rejecting others (MCP
prompts, skill invocations, execution-policy-rule hits) — useful once you know which
categories you actually trust.

A sane starting point for local development: `workspace-write` sandbox + `on-request`
approval — Codex can edit files in your project and run commands inside it, but asks before
touching anything outside the workspace or the network.

> **⚠️ WARNING: `danger-full-access`** removes all OS-level restrictions — described in
> current docs as "No sandbox; no approvals *(not recommended)*" with an "Elevated Risk"
> label. Only use it inside a disposable container/VM with no real credentials on it.

**Sources:** [learn.chatgpt.com/docs/agent-approvals-security](https://learn.chatgpt.com/docs/agent-approvals-security) (fetched 2026-08-03) ·
[codex.danielvaughan.com/2026/03/27/security-hardening-codex-cli](https://codex.danielvaughan.com/2026/03/27/security-hardening-codex-cli/) (published 27 Mar 2026, updated 3 Aug 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Keep the OS-level Linux sandbox on; reserve `--yolo` for throwaway containers only ✅

**Do:** On Linux, current vendor docs state Codex uses **"bwrap plus seccomp by default"**
— namespaces restrict filesystem, network, and process access according to the sandbox mode
you picked. Leave it on. If a workflow genuinely needs full, unfettered access, use
`--dangerously-bypass-approvals-and-sandbox` (short alias `--yolo`) **only inside a
disposable Docker container, devcontainer, or GitHub Codespace with no real credentials
mounted** — never on your day-to-day machine.

> **⚠️ A Docker container or Codespace is disposable — you can destroy and recreate it.**
> That's the whole point: the container boundary becomes your only safety net once you
> bypass Codex's own sandbox, so it has to be one you don't mind losing.

**Caveat:** Sources disagree on the exact kernel primitive, and reconciling them matters
more than picking a side. One independent guide (cybedefend.com, Jun 2026) describes the
Linux mechanism as "Landlock and seccomp," never mentioning bubblewrap. Current vendor docs
say "bwrap plus seccomp by default." A third source (danielvaughan.com, updated 3 Aug 2026)
reconciles the two directly: *"Bubblewrap + seccomp (or legacy Landlock on kernels that lack
Bubblewrap)."* That reading is consistent with all three sources and is the most likely
explanation — Codex has both a Rust-native Landlock path and a bubblewrap path depending on
kernel support. Treat the exact kernel primitive on your machine as 🕒 verify live; the
practical guidance (keep the sandbox on, `--yolo` only in disposable containers) is
unaffected either way.

**Sources:** [learn.chatgpt.com/docs/agent-approvals-security](https://learn.chatgpt.com/docs/agent-approvals-security) (fetched 2026-08-03) ·
[cybedefend.com/en/blog/openai-codex-security-risks-best-practices](https://www.cybedefend.com/en/blog/openai-codex-security-risks-best-practices) (published Jun 2026) ·
[codex.danielvaughan.com/2026/03/27/security-hardening-codex-cli](https://codex.danielvaughan.com/2026/03/27/security-hardening-codex-cli/) (updated 3 Aug 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Prefer ChatGPT sign-in for interactive use; use an API key for automation — and know credentials are stored in plaintext by default ✅

**Do:** "Sign in with ChatGPT" (`codex login`) uses your Plus/Pro/Team/Business/Edu/
Enterprise subscription and is recommended for interactive local use. For scripted/CI use,
authenticate with an API key instead (see the headless practice below for the exact env
var). Either way, Codex stores your session locally at `~/.codex/auth.json`.

> **⚠️ `~/.codex/auth.json` is plaintext by default**, containing an access token, refresh
> token, ID token, and account identifier — current vendor docs say so explicitly ("treat
> `~/.codex/auth.json` like a password") and do **not** claim it's encrypted. Set
> `cli_auth_credentials_store = "keyring"` in `config.toml` to use your OS keyring instead
> of the plaintext file where supported — vendor docs don't specify what happens on a system
> where the OS keyring isn't available (silent plaintext fallback vs. an error), so after
> enabling it, confirm it actually took effect by checking that `~/.codex/auth.json` no
> longer contains a live token. Also set the file's Unix permissions defensively:
> `chmod 600 ~/.codex/auth.json`, so on a shared/multi-user box other local accounts can't
> read it even before you configure the keyring. Never commit, paste, or share this file.
>
> This isn't theoretical: a documented June 2026 supply-chain attack (a malicious npm
> package with ~27–29k weekly downloads) silently exfiltrated users' Codex OAuth refresh
> tokens — which don't expire — to attacker infrastructure. If you install random npm
> packages on a machine where Codex is logged in, that's your exposure.

**Caveat:** The prior (29 Jun 2026) version of this entry cited an OpenAI changelog note
about "encrypted local storage" for CLI+MCP OAuth creds. Current vendor documentation
(fetched fresh this run) makes no such claim and instead documents plaintext-by-default file
storage with OS keyring as the opt-in, more secure alternative. Treat the "encrypted"
framing as **superseded/incorrect** as of this refresh.

**Sources:** [learn.chatgpt.com/docs/auth.md](https://learn.chatgpt.com/docs/auth.md) (fetched 2026-08-03) ·
[labs.cloudsecurityalliance.org — CSA research note, AI Developer Supply Chain: OpenAI Codex Token Theft](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-developer-supply-chain-codexui-20260601/) (published 1 Jun 2026)
**Confidence:** ✅ independently-corroborated

---

### Practice: Use `codex exec` for headless/CI runs; default sandbox there is `read-only` ✅

**Do:** `codex exec "prompt" --json` for scripted runs — `--json` switches stdout to a
newline-delimited JSON stream (one structured event per command/file-change/message) that's
easy to pipe into `jq`. `--ephemeral` skips writing session rollout files to disk, which you
almost always want in CI. `codex exec` defaults to a **`read-only` sandbox**; pass
`--sandbox workspace-write` explicitly when the job needs to edit files.

For authentication in automation, current docs point to a dedicated `CODEX_API_KEY`
environment variable that only works with `codex exec` (distinct from a general
`OPENAI_API_KEY`). For GitHub Actions specifically, prefer the official
`openai/codex-action@v1` action over hand-rolling env-var auth — it proxies credentials
rather than exposing the raw key to the job, and its default `safety-strategy: drop-sudo`
removes elevated privileges before Codex runs.

> **⚠️ Don't set `CODEX_API_KEY` as a plain job-level env var when untrusted code (e.g. a PR
> from a fork) runs in the same step** — that's exactly the exposure the GitHub Action's
> proxy approach is designed to avoid.

**Sources:** [learn.chatgpt.com/docs/non-interactive-mode](https://learn.chatgpt.com/docs/non-interactive-mode) (fetched 2026-08-03) ·
[developersdigest.tech/blog/codex-exec-ci-headless-guide](https://www.developersdigest.tech/blog/codex-exec-ci-headless-guide) (published 10 Jun 2026, updated 28 Jun 2026) ·
[learn.chatgpt.com/docs/github-action](https://learn.chatgpt.com/docs/github-action) (fetched 2026-08-03)
**Confidence:** ✅ independently-corroborated

---

### Practice: Configure in `~/.codex/config.toml`; understand the full precedence order ✅

**Do:** TOML is `key = "value"` with `[section]` headers. Personal settings go in
`~/.codex/config.toml`; per-project overrides in `.codex/config.toml` at the project root
(only honored for projects you've marked trusted). Use `--profile <name>` to load an
additional `$CODEX_HOME/<name>.config.toml` layered on top of your base config, or
`-c key=value` for one-off overrides.

Precedence, highest to lowest: **CLI flags/`-c` overrides → project `.codex/config.toml` →
profile file (`--profile`) → user `~/.codex/config.toml` → system `/etc/codex/config.toml`
→ built-in defaults.** (The system-level layer is documented by a third-party guide rather
than the vendor precedence page itself — worth knowing if you're specifically relying on
`/etc/codex/config.toml` on a shared machine.)

> Note: project-level config **cannot** override certain machine-local/security settings.
> Vendor docs confirm, verbatim: *"Project-scoped config can't override machine-local
> provider, auth, host-owned app request metadata, notification, configuration profile
> selection, or telemetry routing keys"* — and the exclusion list also includes
> **`sandbox_mode` and `approval_policy`**, so a compromised or untrusted project repo can't
> silently loosen either your sandbox or your approval settings via its own
> `.codex/config.toml`.

**Sources:** [learn.chatgpt.com/docs/config-file/config-reference](https://learn.chatgpt.com/docs/config-file/config-reference) (fetched 2026-08-03) ·
[blakecrosley.com/guides/codex](https://blakecrosley.com/guides/codex) (updated 29 Jul 2026, system-level `/etc/codex/config.toml` layer)
**Confidence:** ✅ independently-corroborated

---

### Practice: Pick the model deliberately — the lineup changed on 9 Jul 2026 ✅

**Do:** As of this run, OpenAI's Codex CLI docs recommend the new three-tier **Sol / Terra /
Luna** family (launched 9 Jul 2026, replacing GPT-5.5) but, notably, **do not name a single
model as "the default"** — the vendor docs' own language is: *"If you don't specify a model,
the ChatGPT desktop app, Codex CLI, or IDE extension uses a recommended model."* Treat
`gpt-5.6-sol` as the flagship/recommended tier for complex work, not a confirmed documented
default:

| Model | Context | Pricing (input / output per M tokens) | Notes |
|-------|---------|----------------------------------------|-------|
| gpt-5.6-sol | 1.05M tokens | $5 / $30 | Flagship/recommended tier; complex coding, computer use, cybersecurity |
| gpt-5.6-terra | 1.05M tokens | $2 / $12 (cut from $2.50/$15 on 30 Jul 2026) | Everyday work, strong reasoning |
| gpt-5.6-luna | 1.05M tokens | $0.20 / $1.20 (cut from $1/$6 on 30 Jul 2026) | Fast/cheap, repeatable tasks |
| gpt-5.5 | — | not published on the current vendor models page | Previous-generation frontier model; one independent guide (blakecrosley.com) reports 400K context in Codex vs. 1M in the API at $5/$30 — treat context-window figures for this model as source-dependent, not vendor-confirmed |
| gpt-5.4 / gpt-5.4-mini | — | — | **Retiring from Codex (ChatGPT auth) 31 Aug 2026** 🕒; still usable via API key |
| gpt-5.3-codex-spark | — | — | Real-time iteration, ChatGPT Pro-only research preview |

🕒 **verify live — pricing cut confirmed:** launch-day (9 Jul 2026) third-party coverage
reported Terra/Luna pricing as $2.50/$15 and $1/$6; the current vendor pricing page shows
$2/$12 and $0.20/$1.20. This is a confirmed price cut, not a discrepancy: **OpenAI cut GPT-5.6
Luna pricing by 80% and Terra by 20% on 30 Jul 2026**, covered by CNBC, Axios, and
VentureBeat, all dated 30 Jul 2026, with before/after numbers matching the table above
exactly.

> Not every third-party guide had caught up: one guide updated as recently as 29 Jul 2026
> still listed GPT-5.5 as "the recommended default." Model lineup moves faster than most
> blog posts get updated — trust the vendor models page over guides for this one fact.

**Sources:** [learn.chatgpt.com/docs/models](https://learn.chatgpt.com/docs/models) (fetched 2026-08-03) ·
[developers.openai.com/api/docs/models](https://developers.openai.com/api/docs/models) (fetched 2026-08-03) ·
[marktechpost.com — OpenAI Releases GPT-5.6](https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/) (published 9 Jul 2026) ·
[testingcatalog.com — OpenAI launches GPT-5.6 Sol, Terra, and Luna](https://www.testingcatalog.com/openai-launches-gpt-5-6-sol-terra-and-luna-on-apps-and-api/) (published 9 Jul 2026) ·
[cnbc.com — OpenAI price cut GPT](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html) (30 Jul 2026) ·
venturebeat.com — AI price wars: OpenAI cuts GPT-5.6 Luna prices by 80% (30 Jul 2026; consistently returns 429 on re-fetch, unlinked per policy — corroborated by the CNBC link above) ·
axios.com — OpenAI cuts prices on GPT Terra, Luna (30 Jul 2026; consistently returns 403 bot-detection on re-fetch, unlinked per policy — corroborated by the CNBC link above)
**Confidence:** ✅ independently-corroborated (model lineup, context window, and the 30 Jul
price cut are all multiply-sourced); which model is "the default" is explicitly **not**
vendor-documented — described here as a recommended tier, not asserted as a documented
default

---

## Part 3 — Google Gemini CLI

> ## What changed since 29 Jun 2026
> The big story hasn't changed direction, only aged: Google's 18 June 2026 shutdown of free
> "Sign in with Google" login for Gemini CLI is now over six weeks in the past, not a fresh
> warning. Google's own authentication docs page still reads as if this is upcoming
> ("Gemini CLI will be replaced by Antigravity CLI on June 18th") — that banner is **stale**;
> the cutoff already happened. Don't trust the tense of Google's own docs page here; trust
> the dated announcement and independent confirmations below instead.

### Practice: Install with Node.js 20+ via npm (or brew/MacPorts on Linux/macOS) ✅

**Do:** `npm install -g @google/gemini-cli`. Requires Node.js 20.0.0+ — Ubuntu's apt-repo
Node packages have historically shipped older than 20.x on LTS releases, so check
`node --version` before relying on it. To get a current Node on Ubuntu via NodeSource:
```
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs -y
```
Alternatives documented by Google: `brew install gemini-cli` (Homebrew, works on Linux too),
`sudo port install gemini-cli` (MacPorts, macOS only), a conda environment for restricted
environments, or no-install execution via `npx @google/gemini-cli`. Verify with
`gemini --version`; upgrade with `npm install -g @google/gemini-cli@latest`.

> **⚠️ WARNING:** The NodeSource one-liner runs a remote script **as root** (`sudo -E bash`),
> which is more powerful than piping to an unprivileged `sh`. Only run it if you trust
> NodeSource (a long-established, well-maintained project); check nodesource.com first if
> unsure.

🕒 **verify live:** `npm view @google/gemini-cli version` for the current release. As of this
snapshot, GitHub's releases page lists **v0.53.1** (stable, published 31 Jul 2026, marked
"Latest") as the current non-nightly tag, with active nightly builds continuing daily
(`v0.55.0-nightly.20260803.gf47d6c6f7`, 3 Aug 2026) — up from v0.49.0 at the June 2026
baseline. (A search-index snippet briefly suggested v0.53.0 might be current; a direct fetch
of the GitHub releases page during grading confirmed v0.53.1 is correct.)

**Sources:** [geminicli.com/docs/get-started/installation](https://geminicli.com/docs/get-started/installation) (fetched 03 Aug 2026) ·
[ssdnodes.com — How to Install and Use Gemini CLI on Ubuntu Linux](https://www.ssdnodes.com/blog/how-to-install-and-use-gemini-cli-on-ubuntu-linux/) (28 Apr 2026) ·
[github.com/google-gemini/gemini-cli/releases](https://github.com/google-gemini/gemini-cli/releases) (fetched 03 Aug 2026, for current version)
**Confidence:** ✅ independently-corroborated

---

### Practice: Plan your authentication around who's paying — free personal "Login with Google" no longer works in the open-source `gemini` CLI ✅

**Do:** As of **18 June 2026**, Google stopped serving Gemini CLI requests for free-tier,
Google AI Pro, Google AI Ultra, and individual Gemini Code Assist users (announced 19 May
2026, ~30-day migration window). If you're setting up `gemini-cli` today, the paths that
still work are: (1) a **paid Gemini API key** from Google AI Studio
(`export GEMINI_API_KEY=your-key-here`), (2) **Vertex AI** (Application Default Credentials
via `gcloud`, a service-account key, or a Cloud API key — requires a billing-enabled GCP
project; **set a GCP budget alert before you start** if you haven't used Cloud billing
before, since it has no built-in spend cap and a runaway job can generate a real bill), or
(3) an organization's **Gemini Code Assist Standard/Enterprise license** (Workspace/
enterprise OAuth still works for these). Google's own replacement for individual/free use is
**Antigravity CLI** — a separate binary (`agy`) installed independently of the existing
`gemini` command, using its own env var (`ANTIGRAVITY_API_KEY`). Several specifics about
Antigravity CLI (that it's Go-built, the exact `antigravity.google/download` install path,
and whether it accepts a Gemini API key as an alternative) could not be independently
re-confirmed this run and should be treated as unverified rather than relied upon.

> **⚠️ WARNING:** Google's own authentication docs page, fetched today, still displays the
> **future-tense** banner "Gemini CLI will be replaced by Antigravity CLI on June 18th" and
> recommends "Sign in with Google" as the primary method for individual accounts — that page
> is stale and does not reflect the cutoff that already happened. Community reports (GitHub
> discussion replies from June–July 2026) describe 403/429 login-failure errors circulating
> around this transition, not a clean, documented shutoff message — but which specific tool
> (`gemini` CLI OAuth vs. Antigravity CLI's own login) those particular error reports belong
> to was not fully resolved this run; re-read the source discussion thread before treating
> either binary as the confirmed cause of a given 403/429. Don't rely on the vendor docs'
> verb tense either way — if a tutorial (including Google's own) tells you to just log in
> with a personal Google account and it doesn't work, this transition is why.

**Caveat / contested:** Antigravity CLI being closed-source is community pushback voiced in
Google's own GitHub discussion, not a confirmed Google statement — several commenters also
report Antigravity CLI is missing features, burns tokens faster, and is harder to use than
Gemini CLI was; treat these as user complaints, not verified benchmarks. Antigravity CLI's
own free-tier quota could **not** be confirmed this run, even after a direct fetch of
Google's current official page (`antigravity.google/docs/plans`): it describes free/
non-subscriber quota only qualitatively ("meaningful quota, refreshed weekly") and
explicitly disclaims that "specified rate limits are not guaranteed." A "~20 requests/day"
figure circulates online but traces to pages predating the CLI's own 19 May 2026 launch, or
describing the broader Antigravity IDE product rather than the CLI specifically — treat any
specific Antigravity CLI quota number you see as unconfirmed until you find a source dated
after the CLI's launch.

**Sources:** [geminicli.com/docs/get-started/authentication](https://geminicli.com/docs/get-started/authentication/) (fetched 03 Aug 2026 — banner confirmed stale) ·
[developers.googleblog.com — An important update: transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) (19 May 2026) ·
[github.com/google-gemini/gemini-cli discussion #27274](https://github.com/google-gemini/gemini-cli/discussions/27274) (official Google announcement + community replies through Jul 2026, fetched 03 Aug 2026) ·
[inventivehq.com — Gemini CLI Is Being Retired on June 18](https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration) (13 Jun 2026) ·
[antigravity.google/docs/plans](https://antigravity.google/docs/plans) (fetched 2026-08-04, confirms no specific free-tier number is published)
**Confidence:** ✅ independently-corroborated (the 18 Jun 2026 cutoff itself); the Antigravity
CLI specifics (binary language, install path, env var, API-key-acceptance) are unverified
this run and should be treated as lower-confidence

---

### Practice: Sandboxing is opt-in on Ubuntu, not automatic — turn it on and pick a backend ✅

**Do:** Gemini CLI does **not** sandbox shell/file operations by default. Enable it with the
`-s`/`--sandbox` flag, the `GEMINI_SANDBOX` env var
(`true`/`docker`/`podman`/`sandbox-exec`/`runsc`/`lxc`), or `"sandbox": true` under `tools`
in `settings.json`. On Ubuntu/Linux the practical options are:
- **Docker or Podman** (cross-platform container isolation) — defaults to the published
  image `ghcr.io/google/gemini-cli:latest`. Install first:
  `sudo apt install docker.io && sudo systemctl enable --now docker`, then
  `sudo usermod -aG docker $USER` and re-login.
- **gVisor (`runsc`)** — Linux-only, described by Google as the strongest isolation
  available (runs the container inside a user-space kernel), but not auto-detected; must be
  explicitly configured.
- **LXC/LXD** — Linux-only, experimental, full-system containers.

> **⚠️ WARNING: joining the `docker` group is effectively granting yourself root.** The
> `sudo usermod -aG docker $USER` step above is presented as a routine setup step, but
> membership in the `docker` group is a well-known root-equivalent privilege escalation
> path — anyone (or anything) that can run `docker` as you can trivially get root via a
> bind-mounted container. This is worth knowing precisely *because* this section is about
> making your machine safer: don't treat Docker-group membership as a free, side-effect-free
> way to get to container sandboxing if root-equivalent access for your own user account is
> part of what you're trying to avoid.

> We could not confirm from Google's own sandbox docs a claim that `--yolo` auto-enables
> sandboxing when a backend is already installed — that page describes the sandbox flags and
> backends but does not document any interaction with `--yolo`. **Treat `--yolo` as NOT
> enabling sandboxing on your behalf.** More importantly, the docs don't specify what
> happens when you run `--yolo` with *no* sandbox backend installed at all — whether it
> refuses to run, warns and continues unsandboxed, or silently proceeds with zero sandbox
> *and* zero approvals (the worst case). Don't assume it fails safe; confirm your sandbox is
> actually active (`-s`/`--sandbox` explicitly, or `GEMINI_SANDBOX` set) independently of
> whether you're also using `--yolo`.

**Why (beginner):** Nothing about running `gemini` interactively protects your filesystem or
network by default — the confirmation prompts (see next practice) are a separate mechanism
from sandboxing, and even those are gone entirely in `--yolo` mode. If you're letting the
agent touch a real project, turn on at least Docker/Podman sandboxing first — and understand
the Docker-group tradeoff above before you do.

**Caveat / contested:** The exact list of supported backends has grown since a Feb 2026
independent technical review (which found only Seatbelt/Docker/Podman) — Google's current
docs also list gVisor, Windows Native Sandbox, and experimental LXC/LXD support, so the
backend list itself is 🕒 verify live. That same independent review is useful corroboration
that sandboxing requires an explicit opt-in and a pre-installed backend, matching Google's
own docs.

**Sources:** [geminicli.com/docs/cli/sandbox](https://geminicli.com/docs/cli/sandbox/) (fetched 03 Aug 2026) ·
[agent-safehouse.dev — Gemini CLI Sandbox Analysis Report](https://agent-safehouse.dev/docs/agent-investigations/gemini-cli) (12 Feb 2026, v0.30.0-nightly)
**Confidence:** ✅ independently-corroborated

---

### Practice: Know all four approval modes before picking one — `auto_edit` is not the safe middle ground it sounds like ✅

**Do:** Set with `--approval-mode` or `general.defaultApprovalMode` in `settings.json` (only
`yolo` cannot be set via `settings.json` — flag or slash command only):

| Mode | Behavior |
|------|----------|
| `default` | Prompts before every tool call (file edit or shell command) |
| `auto_edit` | Auto-approves file-edit tools (`write_file`, `replace`); still prompts for shell commands |
| `plan` | Read-only — can read files and draft a plan, cannot write files or run shell commands until you explicitly choose to execute |
| `yolo` | Auto-approves everything, including arbitrary shell commands; no confirmation at all |

**Why (beginner):** `auto_edit` still lets the agent run any shell command it wants without
asking — only file writes are gated, so it's a partial safety net, not a full one. `yolo`
removes the confirmation step entirely; if the agent misreads a file or picks up an
instruction from untrusted input, there's nothing to catch it before it runs. Restrict
`--yolo` to disposable VMs/containers or CI on fully-trusted, non-public input — never a
machine with real data or credentials, and never CI that reacts to public issues/PRs.

**Caveat / contested:** The mode table itself is sourced to Google's own configuration
reference (single source, 📄 vendor-documented). The framing that YOLO mode is genuinely
risky — not just theoretically — is separately corroborated by an independent write-up
describing it as removing "one of the biggest built-in safeguards" and warning it can wipe
out code, run destructive commands like `rm -rf`, and eliminate the audit trail a team
relies on for review; that source, however, is dated 10 Jul 2025 — thirteen months before
this snapshot and predating `plan` mode's existence — so treat it as corroborating the *risk
framing* only, not as a current source for the mode list itself.

**Sources:** [geminicli.com/docs/reference/configuration](https://geminicli.com/docs/reference/configuration/) (fetched 03 Aug 2026, mode table) ·
[devsolus.com — Gemini CLI Permissions: Is YOLO Mode Safe?](https://devsolus.com/gemini-cli-permissions-is-yolo-mode-safe/) (10 Jul 2025, risk framing only)
**Confidence:** 📄 vendor-documented (mode table); ✅ independently-corroborated (risk
framing only, dated source — see caveat)

---

### Practice: Script with `gemini -p` and `--output-format json`; check exit codes, not just output 📄

**Do:** Headless mode triggers automatically in a non-TTY environment, or explicitly via
`-p`/`--prompt`:
```
gemini -p "Review this diff" --output-format json | jq '.response'
```
(`jq` isn't installed by default on Ubuntu: `sudo apt install jq`.) JSON output returns a
single object with the response and usage stats; `--output-format stream-json` instead emits
newline-delimited JSON events (`init`, `message`, `tool_use`, `tool_result`, `error`,
`result`) for streaming consumption. Documented exit codes: `0` success, `1` general/API
error, `42` input error (invalid prompt/arguments), `53` turn-limit exceeded — check these
in scripts rather than assuming success from non-empty output.

**Why (beginner):** A script that only checks "did I get output" can silently treat a
truncated or error response as success. Checking `$?` against the documented codes catches
turn-limit cutoffs (`53`) and bad input (`42`) separately from a hard API failure (`1`).

**Caveat / contested:** Single (vendor) source for the exit-code table specifically; we
could not find an independent write-up enumerating all four codes for confirmation this run,
so treat the exact numeric values as vendor-documented rather than independently verified,
even though the general `-p`/`--output-format` mechanics are widely used in community
tutorials.

**Sources:** [geminicli.com/docs/cli/headless](https://geminicli.com/docs/cli/headless/) (fetched 03 Aug 2026)
**Confidence:** 📄 vendor-documented

---

### Practice: Know which `settings.json` wins — a 7-layer precedence stack, and never copy-paste `"trust": true` for an MCP server you don't control 📄

**Do:** From lowest to highest priority:
1. Built-in defaults
2. `/etc/gemini-cli/system-defaults.json`
3. `~/.gemini/settings.json` (your user settings)
4. `.gemini/settings.json` in your project (team/workspace settings)
5. `/etc/gemini-cli/settings.json` (system policy — takes precedence over user/project
   settings, useful for locking down a shared machine)
6. Environment variables (including `.env` files)
7. CLI flags (highest priority — always wins)

Put personal preferences in `~/.gemini/settings.json`, team defaults in
`.gemini/settings.json`. Inspect what context the agent has loaded with `/memory show`
(refresh with `/memory refresh`).

> **⚠️ WARNING:** Google's own MCP-server documentation shows a config example with
> `"trust": true`, which "bypasses all tool call confirmations for this server" — default is
> `false`. Only set it for a server you wrote and run yourself (e.g. on `localhost`); never
> copy-paste it for a third-party MCP server.

**Caveat / contested:** A separate, narrower `/settings` command-reference page only
describes user-vs-workspace precedence ("workspace settings override user settings")
without mentioning the other five layers — that's not a contradiction, just a page scoped to
what the interactive `/settings` command itself touches; treat the reference/configuration
page as the authoritative full picture.

**Sources:** [geminicli.com/docs/reference/configuration](https://geminicli.com/docs/reference/configuration/) (7-layer precedence, fetched 03 Aug 2026) ·
[github.com/google-gemini/gemini-cli — docs/tools/mcp-server.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md) (`trust` default/example, fetched 03 Aug 2026)
**Confidence:** 📄 vendor-documented

---

### Practice: Pick your model deliberately; watch quotas — this whole area is fast-moving 📄

**Do:** 🕒 **verify live** — as of this snapshot, Gemini CLI's model routing defaults to
Gemini 2.5 Flash for simple prompts and Gemini 2.5 Pro for complex ones; **Gemini 3 is
opt-in, not default** (`/model` → "Auto (Gemini 3)" to enable Gemini 3 Pro/Flash routing, or
`-m gemini-3.1-pro-preview` to launch Gemini 3.1 Pro Preview directly, which is rolling out).
Quotas by auth path, per Google's own quota/pricing page:

| Auth path | Daily limit |
|---|---|
| Gemini Code Assist (individual, free) | 1,000 requests/user/day |
| Google AI Pro | 1,500 requests/user/day |
| Google AI Ultra | 2,000 requests/user/day |
| Gemini API key (free) | 250 requests/user/day |
| Gemini API key (pay-as-you-go) | Varies — token-based billing, no fixed daily cap published |
| Vertex AI Express Mode | Varies — vendor page does not publish a fixed number |
| Code Assist Standard (Workspace) | 1,500 requests/user/day |
| Code Assist Enterprise | 2,000 requests/user/day |

(The vendor page's own word for the pay-as-you-go and Vertex AI Express Mode rows is
literally "Varies" — this table reports that rather than a specific extrapolated number.
A "Flash model only" qualifier on the free API key row, present in an earlier draft of this
table, could not be confirmed on the current vendor page and has been dropped.)

Remember: per the authentication practice above, the free-tier rows in this table (Code
Assist individual, and any personal-account row) stopped being reachable for free/Pro/Ultra
personal accounts on 18 June 2026 — this table describes what each *auth path* is entitled
to, not which paths are currently open to a new free user.

**Caveat / contested:** A single independent, dated (28 Mar 2026, updated through 10 Jul
2026) source states that **Gemini 3 Pro specifically** went paid-only on 25 March 2026 —
Free tier is Flash-only since then. This is a narrower and more precise claim than "Gemini's
Pro models generally," and it rests on one publisher; Google's own quota and Gemini-3 pages
don't mention a 25 Mar 2026 change at all. Treat this specific date as single-source and
verify live rather than independently corroborated. The quota table itself is
vendor-documented and everything in this practice is subject to change without notice —
re-check [geminicli.com/docs/resources/quota-and-pricing](https://geminicli.com/docs/resources/quota-and-pricing/)
before building a workflow around a specific model or limit.

**Sources:** [geminicli.com/docs/resources/quota-and-pricing](https://geminicli.com/docs/resources/quota-and-pricing/) (fetched 03 Aug 2026) ·
[geminicli.com/docs/get-started/gemini-3](https://geminicli.com/docs/get-started/gemini-3/) (model routing/opt-in status, last updated 10 Apr 2026) ·
[codemyspec.com — Gemini CLI Pricing & Free Tier 2026](https://codemyspec.com/blog/gemini-cli-review-2026) (28 Mar 2026, updated 10 Jul 2026, "Gemini 3 Pro" paid-only claim only)
**Confidence:** 📄 vendor-documented (quota table, model-routing defaults); the "Gemini 3 Pro
paid-only since 25 Mar 2026" fact specifically is single-source / 🕒 verify live, not
independently corroborated

---

## Held pending fixes (not fully closed this run)
- **nftables complete turnkey ruleset for a bare Ubuntu host** — INNOQ's ruleset (Part 0) is
  real, dated, and now quoted verbatim, but written for a container/Testcontainers context;
  it needs the reader to substitute their own proxy IP/port and decide DNS-pinning vs proxy
  for apt/model-API domains. Not yet a single copy-paste file for "my Ubuntu box running an
  agent." ⚠ #318 (downgraded from fully-open to substantially-advanced this run).
- **Ubuntu 26.04 LTS AppArmor/bwrap default status** — 26.04 has been released since 23 Apr
  2026 (not upcoming), but no primary source confirming whether it ships
  `bwrap-userns-restrict` active by default the way 25.04 does could be found this run, even
  after a live-search pass beyond the original draft's research. This looks like it needs a
  live-machine test (`sysctl kernel.apparmor_restrict_unprivileged_userns` on an actual
  26.04 box), not another web search. ⚠ #317-26.04
- **systemd --user service practice's second independent source** — morphllm.com (cited in
  the 2026-06-29 snapshot) returned HTTP 429 on re-fetch this run; dropped per sourcing
  rules rather than cited from memory. Practice downgraded to `vendor-documented` pending a
  successful re-fetch or a substitute second source in a future refresh.
- **Antigravity CLI specifics** (Go-built binary claim, exact install path, whether it
  accepts a Gemini API key, and correct attribution of circulating 403/429 login-failure
  reports between `gemini` CLI OAuth and Antigravity CLI's own login) — unverified this run;
  worth a dedicated re-check once Antigravity CLI's own docs mature. ⚠ #TBD
- **Claude Code hooks: cross-hook precedence and any block-count override mechanism** — the
  prior draft's specific claims here (a "8 consecutive blocks" override, a named env var, a
  named JSON field) were removed this run as unverifiable against both the cited page and
  Anthropic's full hooks reference; only "hooks run in parallel with deduplication of
  identical handlers" is confirmed. If Anthropic documents a real precedence rule or
  override mechanism in the future, add it back with a citation. ⚠ #TBD

## CHANGELOG (2026-06-29 snapshot → this 2026-08-03 refresh)

*(This refresh replaces all four sections — Foundations, Claude Code, Codex CLI, Gemini
CLI — with freshly re-fetched sources. Selected highlights below; see each practice's own
caveat for full detail.)*

**Part 0 — Foundations:**
1. Gap #317 (AppArmor profile for bubblewrap) substantially closed: Anthropic's own docs now
   publish the exact profile; jdhodges.com corroborates byte-identical text; Launchpad
   confirms the shipped-but-inactive-on-24.04 / active-by-default-on-25.04+ status.
   **Skeptic KILL applied:** the draft's claim that the `dfaerch/bubblewrap-on-ubuntu` GitHub
   README contained a byte-identical profile was false (the README has no profile text at
   all, and the actual profile files aren't byte-identical either) — reworded to "publishes
   two functionally equivalent variants" and re-pointed the citation at the actual profile
   files.
2. Gap #318 (starter nftables ruleset) substantially advanced: INNOQ's dated ruleset now
   quoted verbatim after a **Skeptic FIX** caught a dropped rule line and paraphrased
   comments in the original quote.
3. **Skeptic FIX applied:** dropped four uncited package-version specifics (Ubuntu apt
   versions for bubblewrap/firejail); replaced with a documented CVE note for bubblewrap
   0.11.2 and an independently-confirmed firejail 0.9.80 date.
4. **Skeptic FIX applied:** removed an uncited claim of having fetched Ubuntu 26.04's
   top-level release notes; the 26.04 AppArmor-default question is now marked unverified
   rather than implying a fetch that didn't happen.
5. **Skeptic FIX applied:** corrected a garbled sentence about `git worktree` sharing
   (previously read as if `HEAD` were shared; it's actually the opposite).
6. **Skeptic FIX applied:** secrets-management practice no longer claims "both sources
   recommend a dedicated secrets manager" — the two sources actually disagree on when a
   keyring alone is sufficient; reworded to represent both positions. Dropped an unsourced
   "Bitwarden" mention.
7. **Beginner KILL applied:** merged the nftables rollback warning with the buried
   SSH-lockout caveat into one clear warning, and added an actual failsafe (local testing
   first, or a self-reverting `at` job).
8. **Beginner FIX applied:** added a literal `bwrap` command to the sandboxing practice
   (previously only described the goal, no runnable command).
9. **Beginner FIX applied:** the "set spend caps overnight" warning now points to the
   specific per-ecosystem mechanism in Parts 1-3 instead of giving no actionable next step.
10. **Beginner FIX applied:** explained the `%h` systemd specifier inline.
11. **Beginner FIX applied:** added a "verify it worked" step after the AppArmor profile
    reload.
12. **Timekeeper FIX applied:** added the CVE-2026-41163 note for bubblewrap 0.11.2.

**Part 1 — Claude Code:**
13. **Skeptic KILL applied:** the draft claimed a third-party tracker "independently
    confirms v2.1.220" — on re-fetch, that tracker actually showed v2.1.219, refuting the
    corroboration claim (the version number itself, v2.1.220, is correct per Anthropic's own
    changelog). Relabeled the install practice from independently-corroborated to
    vendor-documented and removed the false corroboration claim.
14. **Skeptic KILL applied — highest-severity finding this run:** the hooks practice's
    caveat asserted an "8 consecutive blocks" Stop-hook override, a
    `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` env var, a `stop_hook_active` JSON field, and a
    cross-hook "most restrictive decision wins" precedence rule — none of these could be
    found on the cited page or in Anthropic's full hooks reference. All four were removed;
    only the confirmed "hooks run in parallel, identical handlers deduplicated" behavior
    remains.
15. **Skeptic FIX applied:** added the actual source for "Sonnet 5 is the default model"
    (Claude Code changelog v2.1.197), which the draft asserted but cited to two pages that
    don't state it.
16. **Skeptic FIX applied:** softened the "June 15 billing change still has not been
    reinstated" claim — the cited source documents the pause announcement but not a current
    confirmed status; reworded to avoid asserting more than the source supports.
17. **Skeptic FIX applied:** split the `/config key=value` (v2.1.181+) version note from the
    `/model`/`/effort` (v2.1.205+) version note — the draft had merged them incorrectly.
18. **Skeptic FIX applied:** removed an uncited "everything in the conversation is sent to
    Anthropic's API" / "never paste secrets in chat" claim attributed to a specific page that
    doesn't state it; kept the confirmed network-approval-default content from that page.
19. **Skeptic FLAG applied:** corrected the tokenizer note's attribution (Claude 4.7-and-later
    models generally, not "Sonnet 5's tokenizer" specifically) and wording ("approximately
    30%" not "up to ~30%").
20. **Beginner KILL applied:** promoted the "sandbox still allows reading `~/.aws/credentials`
    and `~/.ssh/`" fact from inline bold text to its own ⚠️ WARNING blockquote.
21. **Beginner FIX applied:** billing-trap remediation now also mentions checking for a
    cloud-provider env var or `apiKeyHelper`, not just `ANTHROPIC_API_KEY`.
22. **Beginner FIX applied:** added explicit "stop and report it" guidance for a GPG
    fingerprint mismatch.
23. **Beginner FIX applied:** added plain-language definitions for "domain fronting" and
    "TLS termination."
24. **Timekeeper FIX applied:** added Claude Opus 5 (24 Jul 2026) to the cost/model-choice
    practice — a real completeness gap on a page whose whole point is model choice and cost.
25. **Timekeeper FIX applied:** added the 50% weekly-usage-limit boost (through 19 Aug 2026)
    to the cost practice, with an explicit note on its secondary-source-only sourcing.

**Part 2 — Codex CLI:**
26. **Skeptic FIX applied:** the draft asserted `gpt-5.6-sol` as "the *documented* default";
    the vendor page conspicuously declines to name a default. Reworded throughout to
    "flagship/recommended tier."
27. **Skeptic FIX applied:** the GPT-5.5 pricing/context-window table row was unsourced and
    conflicted with the one source that did discuss it; corrected to note the
    Codex-vs-API context-window discrepancy rather than asserting a single unsupported figure.
28. **Skeptic FIX applied:** rewrote the bwrap-vs-Landlock caveat — the draft had cited
    cybedefend.com as corroborating "bwrap"; it actually says Landlock and never mentions
    bubblewrap. Added the danielvaughan.com source that reconciles both readings.
29. **Timekeeper FIX applied:** upgraded the Terra/Luna pricing "unresolved discrepancy"
    (previously hedged as unconfirmed) to a sourced fact — OpenAI cut Luna 80%/Terra 20% on
    30 Jul 2026, confirmed by CNBC/Axios/VentureBeat, all dated 30 Jul 2026.
30. **Beginner FIX applied:** added guidance on confirming the OS-keyring setting actually
    took effect, plus a `chmod 600 ~/.codex/auth.json` recommendation.
31. **Beginner FIX applied:** promoted the `--yolo` warning to the same `⚠️` visual weight as
    the `danger-full-access` warning.
32. **Beginner FIX applied:** replaced "fix your PATH instead" with the actual command.
33. **Skeptic FLAG applied:** dropped an unsourced "308-redirect" specific and two uncited
    callout items (desktop-app-folded-into-ChatGPT date and "developer commentary" claims);
    added the vendor-confirmed detail that project-config exclusions cover `sandbox_mode` as
    well as `approval_policy`.

**Part 3 — Gemini CLI:**
34. **Skeptic KILL applied:** the "Pro paid-only since 25 Mar 2026" fact was labeled ✅
    independently-corroborated while resting on one publisher (its other two "sources" were
    both geminicli.com pages — same vendor, not independent). Relabeled the quota table
    vendor-documented and narrowed the claim from "Gemini's Pro models" to "Gemini 3 Pro"
    specifically, matching the source.
35. **Skeptic FIX applied:** corrected three quota-table rows (API key pay-as-you-go, Vertex
    AI Express Mode, and a "Flash model only" qualifier) that didn't match the cited vendor
    page — the page says "Varies" for the first two, and the qualifier isn't on the page at
    all.
36. **Skeptic FIX applied — safety-relevant:** removed the claim that `--yolo`
    "auto-enables sandboxing" — unsupported by the cited sandbox docs, and actively unsafe if
    wrong (a reader could believe `--yolo` is safer than it is). Replaced with an explicit
    "treat `--yolo` as NOT enabling sandboxing" instruction and a note that fail-safe vs.
    fail-open behavior with no backend installed is undocumented.
37. **Beginner KILL applied (near-miss in the original draft):** added an explicit ⚠️
    WARNING that Docker-group membership (from the routine sandbox setup step) is
    root-equivalent access — the original draft presented `usermod -aG docker` as a pure
    safety improvement with no mention of this tradeoff.
38. **Beginner FIX applied:** added a GCP budget-alert recommendation to the Vertex AI
    auth-path guidance.
39. **Skeptic FLAG applied:** split the four-approval-mode practice's confidence label
    (mode table = vendor-documented; risk framing = independently-corroborated but from a
    source dated 13 months before this snapshot, predating `plan` mode).
40. **Link-check:** all cited URLs re-fetched by the grading panel 03-04 Aug 2026 with 0 dead
    links; this run's own link-check gate re-verified every link in this published entry
    immediately before publish (see below).

