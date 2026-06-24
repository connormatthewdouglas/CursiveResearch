## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Research synthesis Supported; enforcement gates not implemented
**Read with:** [Chapter 05](05-measurement-daemon-and-natural-language-shell.md), [Chapter 16](16-security-and-hardening.md) (external threats), [Chapter 17](17-firmware-and-bios-control.md) (class 6–7 mutations)

### Authoritative for
- Mutation-class → containment-primitive matrix (sysctl through firmware)
- Inverted threat model: organism mutating its own host and measurement substrate
- Daemon/shell separation of duties for write gates

### Superseded or narrowed
- Treating Ch16 external-hardening checklist as sufficient for self-mutation — it is not

### Open until experiment/hardware
- Build and test risk-based sandbox selector before unattended host mutation
- Firmware mutation staging with measured rollback (Ch17)

---

## Reinforced research (2026-06-24)

- **Least privilege:** NIST SP 800-53 Rev. 5 access control family — baseline for mutation-class gating.
- **Linux containment:** seccomp-BPF (no pointer deref), Landlock LSM (kernel-version-scoped ABI), bubblewrap — design direction in VALIDATION Ch05 row.
- **Agentic risk:** OWASP Agentic AI (2025) — untrusted tool graphs must not receive daemon write capability regardless of sandbox tier.
- **Reversible OS tuning:** BranchFS (2024) — `papers/recursive-self-improvement/branchfs-fec/`; FEC/isolated branches for candidate presets.

---

# Mutation Safety and Permission Law

Status: First research-synthesis pass (2026-06-22). Grounds the project's
self-modification gates in external security literature (least-privilege design,
Linux containment primitives, agentic-AI risk taxonomies) and maps each
mutation class to the containment it actually requires.
Use it for: deciding what the organism's own agents, daemons, and contributors
are allowed to change, and which kernel/userspace mechanism enforces each gate.

## Why this chapter exists

Chapter 07 (Gap 2, "What Should Be Added Next" #1) flagged that the corpus had
the *pieces* of a mutation-safety model — reversible presets, regression gates,
the daemon/shell split (Chapter 05) — but no consolidated, source-backed
**permission law**. Chapter 16 is the closest neighbor, but it solves the
opposite problem: hardening a host against *external* attackers and untrusted
DePIN workloads. CursiveOS faces an additional, inverted threat: its **own**
self-improvement loop intentionally mutates the host (sysctl, GPU power,
scheduler/eBPF, kernel, firmware) under the direction of a probabilistic agent.
The danger is not only an intruder but the organism corrupting itself or its
measurement substrate. This chapter is the missing rulebook for that risk.

## 1. The self-mutation threat model

A self-improving system that can change the machine it runs on collapses the
usual boundary between "the program" and "the administrator." Two foundational
results bound how to handle this safely:

- **Least privilege and fail-safe defaults.** Saltzer and Schroeder's 1975
  design principles still govern: every entity should hold the *minimum*
  privilege needed for its function, access decisions should default to denial,
  and high-impact authority should require *separation of privilege* (more than
  one condition or actor). ([Saltzer & Schroeder, *The Protection of
  Information in Computer Systems*, 1975](https://www.cs.virginia.edu/~evans/cs551/saltzer/))
- **Excessive agency is the named failure.** The OWASP Top 10 for LLM
  Applications (2025) lists **LLM06: Excessive Agency** — damage caused when an
  LLM-driven system is granted excessive functionality, permissions, or
  autonomy and then acts on ambiguous, hallucinated, or manipulated output. The
  prescribed mitigations are precisely the ones CursiveOS needs: minimize tools
  and permissions, require human approval for high-impact actions, *separate
  decision-making from execution*, allowlist approved actions, and block
  irreversible operations by default. ([OWASP GenAI Security Project, LLM Top
  10 (2025)](https://genai.owasp.org/llm-top-10/))

The corpus's own RSI literature confirms the risk is concrete, not theoretical.
Self-modifying scaffolds (STOP) and self-referential agents (Gödel Agent) can
reward-hack their own objective or disable their own safety checks when the
loop that grants improvement is the same loop the agent can edit; Voyager-style
skill accumulation only stays safe because the environment, not the agent,
adjudicates success. The lesson for CursiveOS: **the actor proposing a mutation
must never be the actor that authorizes or verifies it.**

## 2. The mutation-class → containment matrix

Chapter 07 defined a seven-class mutation taxonomy. The new contribution here is
binding each class to the *specific* enforcement mechanism that makes its gate
real, rather than aspirational.

| Class | Mutation type | Example | Enforcement primitive (how the gate is real) | Authorizer |
| --- | --- | --- | --- | --- |
| 0 | Read-only observation | hardware probe, sensor read | Drop all capabilities; `ProtectSystem=strict`, read-only bind mounts; seccomp allowlist excludes write/mount syscalls | none (log only) |
| 1 | User/service config | agent runtime setting | Per-service user (no root); before/after snapshot; reversible write to a scoped path via Landlock ruleset | daemon, auto |
| 2 | Reversible OS tuning | sysctl / sysfs value | Allowlisted key set; `CAP_SYS_ADMIN`-scoped helper (not ambient root); regression sensor + automatic revert | daemon + regression gate |
| 3 | GPU runtime tuning | power / clock profile | Device-node-scoped helper; telemetry watchdog; crash-recovery revert; rate-limited | daemon + regression gate |
| 4 | Scheduler / eBPF | `sched_ext` policy | Isolated test first; verifier (eBPF verifier + project verifier); `kernel.unprivileged_bpf_disabled` stays on for the *shell* | daemon + verifier + gate |
| 5 | Kernel / package / base image | kernel config, ISO build | VM/lab validation; boot test; **signed** artifact (`module.sig_enforce`, cosign); no in-place host edit | offline build + human |
| 6 | Firmware / BMC / BIOS | UEFI / Redfish setting | Staged "pending settings" + reboot semantics; out-of-band recovery path; mandatory human approval | human (always) |

The rule that falls out of the matrix: **privilege required to apply a mutation
rises with its blast radius and reversibility cost, and the authorizing party
shifts from the deterministic daemon (low classes) to a human (high classes).**
No class is ever applied by the probabilistic shell agent directly.

## 3. Separation of duties: deterministic daemon vs probabilistic shell

Chapter 05 established the daemon/shell trust boundary; the permission law makes
it enforceable. The natural-language shell may *propose* a mutation and explain
it, but it must call a narrow, audited interface to enact anything — it never
holds ambient privilege. This is OWASP LLM06's "separate decision-making from
execution" realized as an OS boundary:

- The **measurement daemon** runs deterministic, allowlisted sensor and
  mutation helpers, each launched with the minimum capability set for its class.
- The **shell agent** runs with no mutating capabilities, behind
  `NoNewPrivileges=yes`, and reaches privileged actions only through a scoped
  escalation broker (e.g., a `polkit`-mediated action with its own policy and
  authentication), never cached credentials. ([polkit reference](https://www.freedesktop.org/software/polkit/docs/latest/polkit.8.html))
- High-impact actions (class ≥5) require an out-of-band confirmation the agent
  cannot fabricate.

## 4. Linux containment primitives this law depends on

These are the concrete, well-documented mechanisms that turn the matrix from
policy into code, and the level of trust each warrants:

- **Capabilities** — split root into ~40 distinct privileges so a helper can be
  granted, e.g., only `CAP_SYS_NICE` or `CAP_SYS_ADMIN` for one operation
  instead of full root; pair `CapabilityBoundingSet` with `AmbientCapabilities`
  to cap children. ([capabilities(7)](https://man7.org/linux/man-pages/man7/capabilities.7.html))
- **seccomp** — restrict a process to an explicit syscall allowlist; out-of-set
  calls terminate the process (`SIGSYS`). The deterministic sensor path is an
  ideal seccomp candidate because its syscall set is fixed and known.
  ([seccomp(2)](https://man7.org/linux/man-pages/man7/seccomp.2.html))
- **Landlock** — a *stackable, unprivileged* LSM (Linux 5.13+, network ports
  6.7+) letting a process sandbox its **own** filesystem/network access. This is
  the key primitive for an agent that should restrict itself without needing
  root to do so. ([Landlock, kernel.org](https://docs.kernel.org/userspace-api/landlock.html))
- **systemd sandboxing** — declarative unit hardening: `ProtectSystem=strict`
  (read-only OS tree), `NoNewPrivileges=yes`, `CapabilityBoundingSet=`,
  `SystemCallFilter=`, private namespaces. These give the daemon and shell
  units defense-in-depth without custom code. ([systemd.exec(5)](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html))
- **Firmware staging** — class-6 changes use the platform's pending-settings +
  reset-required model (UEFI/Redfish, see Chapter 06) so firmware mutation is
  always staged, reboot-gated, and out-of-band recoverable, never live-poked.

## 5. Failure modes to design against

- **Verifier capture** — the agent edits or games the sensor/regression gate
  that judges it (the STOP/Gödel-Agent failure). Mitigation: sensors and gates
  live outside the agent's writable scope (class-0 read-only enforcement);
  measurement code is signed and integrity-checked.
- **Privilege creep via tool chaining** — many individually-safe class-1 actions
  composing into a class-3+ effect. Mitigation: blast-radius accounting at the
  broker, not per-call.
- **Irreversibility by default** — a mutation with no clean revert path. The
  reversibility gate is a *precondition* for classes 1–4; classes 5–6 substitute
  staged artifacts + OOB recovery because in-place reversal is unsafe.
- **Confused-deputy escalation** — the shell tricks the daemon's scoped helper
  into acting beyond intent. Mitigation: helpers take typed, allowlisted
  arguments only, never free-form command strings.

## 6. Open research / next actions

1. Specify the scoped-helper IPC contract (typed actions, per-class capability
   sets) before any host mutation is re-enabled in the main repo.
2. Build a class-0 containment prototype (read-only sensor run under
   Landlock + seccomp + `ProtectSystem=strict`) and measure overhead.
3. Define the blast-radius accounting model that prevents class-1 chaining into
   higher-class effects.
4. Decide the human-approval UX for classes 5–6 and how the shell *cannot*
   satisfy it autonomously.
5. Pressure-test the law against the metabolic/economic layer: a mutation that
   pays a contributor must clear the same gates as one that does not, or fitness
   becomes an incentive to bypass safety.

See [sources/chapter-17-selected-sources.md](../sources/chapter-17-selected-sources.md)
for the source register.
