# Chapter 06 Selected Sources

Date extracted: 2026-06-22
Agent / reviewer: claude-opus-4-8 (routine corpus-gap pass)
Chapter: `chapters/06-mutation-safety-and-permission-law.md`
Status: Selected high-priority extraction. Primary docs preferred; verify exact
options against the man page / spec for the target kernel and distro before any
preset becomes operational policy.

## Purpose

Records the external grounding for the mutation-safety / permission-law chapter:
the design principles (least privilege), the agentic-AI risk taxonomy (excessive
agency), and the concrete Linux/userspace containment primitives that make each
mutation-class gate enforceable.

## Selected Sources

| Source ID | Title | Author / Organization | URL | Source Type | Date | Used In | Claims Supported | Reliability Tier | Validation Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-17-001 | The Protection of Information in Computer Systems | Saltzer & Schroeder | https://www.cs.virginia.edu/~evans/cs551/saltzer/ | foundational paper | 1975 | §1 | Least privilege, fail-safe defaults, separation of privilege | A | confirmed (canonical) | Primary citation for the privilege model the law rests on. |
| SRC-17-002 | OWASP Top 10 for LLM Applications — LLM06: Excessive Agency | OWASP GenAI Security Project | https://genai.owasp.org/llm-top-10/ | standards/community taxonomy | 2025 | §1, §3 | Excessive agency failure; separate decision from execution; least-privilege tools; human approval for high-impact actions | A/B | needs periodic recheck | OWASP list versions; LLM06 is the 2025 numbering. |
| SRC-17-003 | capabilities(7) | Linux man-pages project | https://man7.org/linux/man-pages/man7/capabilities.7.html | primary documentation | rolling | §2, §4 | Root split into discrete capabilities; bounding/ambient sets | A | needs verification per kernel | Use for exact capability names per helper. |
| SRC-17-004 | seccomp(2) | Linux man-pages project | https://man7.org/linux/man-pages/man7/seccomp.2.html | primary documentation | rolling | §2, §4 | Syscall allowlisting; SIGSYS on out-of-set calls | A | needs verification | Profile must be traced from the real sensor syscall set. |
| SRC-17-005 | Landlock: unprivileged access control | Linux Kernel Documentation | https://docs.kernel.org/userspace-api/landlock.html | primary documentation | rolling (5.13+, net 6.7+) | §2, §4 | Stackable unprivileged self-sandboxing of FS/network | A | needs verification per kernel | Key primitive for self-restricting agents without root. |
| SRC-17-006 | systemd.exec(5) | systemd / freedesktop.org | https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html | primary documentation | rolling | §2, §4 | ProtectSystem, NoNewPrivileges, CapabilityBoundingSet, SystemCallFilter | A | needs verification | Declarative unit hardening for daemon and shell. |
| SRC-17-007 | polkit reference manual | freedesktop.org | https://www.freedesktop.org/software/polkit/docs/latest/polkit.8.html | primary documentation | rolling | §3 | Policy-mediated scoped privilege escalation | A/B | needs verification | For the shell's escalation broker; no credential caching. |

## Cross-references within the corpus

- Chapter 22 (Security and Hardening): external-attacker hardening; seccomp /
  Landlock / systemd already appear there for the inverse threat model.
- Chapter 06 (Firmware and BIOS Control): UEFI/Redfish staged pending-settings +
  reset-required model underpins class-6 gating.
- Chapter 15 (Measurement Daemon and Natural-Language Shell): the daemon/shell
  trust boundary this law makes enforceable.
- Chapter 07 (Gap Closure): Gap 2 and "What Should Be Added Next" #1, which this
  chapter answers.
- papers/recursive-self-improvement/godel-agent, .../ladder, reflexion;
  STOP and Voyager (pipeline): self-modification / verifier-capture failure modes.

## Extraction Caveats

- Containment-option names and defaults change across kernel and systemd
  versions; pin to the target version before writing presets.
- OWASP LLM Top 10 is re-versioned periodically; recheck the current item number
  and guidance before treating it as authoritative.
