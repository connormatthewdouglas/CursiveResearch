# Local Agent Safety and Operator Interfaces: Selected Sources

Intake date: `2026-05-31`

Purpose: source-backed grounding for Chapter 12's natural-language shell and
measurement-daemon separation. This digest focuses on agentic risk, prompt
injection, tool authority, sandboxing, and operator approval boundaries for a
local OS-operating assistant.

This is not an implementation spec. It is research memory for future shell,
daemon, and containment design.

## Sources Reviewed

| Source | Type | Key Takeaway for CursiveOS |
| --- | --- | --- |
| OWASP Top 10 for LLM Applications | Security risk taxonomy | Prompt injection, sensitive information disclosure, excessive agency, insecure output handling, vector/RAG weaknesses, and supply-chain risk are first-class LLM application risks. The Cursive shell should assume model outputs can be attacker-influenced and should bind tool use outside the model. |
| OWASP Agentic Skills Top 10 | Agentic-skill risk taxonomy | The intermediate skill/action layer is a distinct attack surface. Skills can smuggle authority, hide unsafe side effects, or bridge from benign natural language into dangerous operations. Cursive shell skills should be explicit, versioned, reviewable, and permission-scoped. |
| NCSC: prompt injection is not SQL injection | Government security guidance | Prompt injection should not be treated as a fully solvable input-filtering bug. LLMs do not naturally enforce a reliable instruction/data boundary, so system design must limit consequences when the model is confused. |
| Microsoft guidance on indirect prompt injection | Platform security guidance | Indirect prompt injection exploits untrusted content consumed by AI systems. Mitigation should be layered: isolate untrusted content, constrain downstream actions, and contain impact when one layer fails. |
| NIST AI Risk Management Framework | Risk-management framework | AI systems should be governed, mapped, measured, and managed across their lifecycle. For CursiveOS this supports logging, evaluation, role separation, risk ownership, and explicit controls around shell behavior. |
| Linux seccomp filter documentation | Kernel userspace API | seccomp-BPF lets a process restrict incoming system calls through a filter. Useful as a low-level deny surface for tool runners, but not sufficient alone because many dangerous operations are legal syscalls with dangerous arguments. |
| Linux Landlock documentation | Kernel userspace API / LSM | Landlock provides unprivileged access control that can restrict a process's filesystem and, on newer kernels, some network access. This is attractive for per-command and per-tool confinement without requiring root for every sandbox. |
| gVisor documentation | Container sandbox architecture | gVisor moves much of the host-kernel interface into a per-sandbox application kernel, reducing direct host kernel exposure compared with ordinary containers. Useful for high-risk command execution that needs container-like UX with a stronger syscall boundary. |
| Firecracker documentation | microVM isolation architecture | Firecracker uses KVM-backed microVMs with a small VMM, jailer process, seccomp filters, namespaces, cgroups, and privilege dropping. Useful for expensive but stronger isolation around untrusted or unattended tasks. |

## Practical Extraction

### 1. Prompt Injection Is a Consequence Problem

The strongest lesson from OWASP, NCSC, and Microsoft is that prompt injection is
not merely a string-filtering problem. A local OS agent will read logs, source
files, webpages, docs, issue comments, terminal output, and generated text. Any
of that content may contain instructions aimed at the model.

Corpus implication:

- treat every external document, terminal output, webpage, repository file, and
  tool result as potentially untrusted input;
- never let model confidence alone authorize writes, deletes, network
  exfiltration, credential use, or root actions;
- design for damage containment when prompt injection bypasses the current
  prompt, filter, or classifier.

### 2. Tool Authority Must Live Outside the Model

The model can propose intent, commands, and explanations. The enforcement layer
must decide whether a proposed action is allowed. This fits the existing
CursiveOS daemon/shell separation: the natural-language shell may interpret
human intent, but deterministic code should own permission checks, command
classification, sandbox profile selection, and confirmation requirements.

Corpus implication:

- tool manifests should declare read/write/root/network/destructive scope;
- the shell should route proposed actions through a policy engine before
  execution;
- every tool call should produce an auditable record of prompt context, user
  request, proposed action, policy decision, and result;
- root and destructive actions require explicit user confirmation even if the
  model says the action is routine.

### 3. Skills Are Supply Chain

Agentic skills sit between a model and real authority. They may look like
documentation, but they can encode dangerous workflows, broad filesystem
access, hidden network calls, or implicit trust in untrusted inputs.

Corpus implication:

- skills should be first-class artifacts with names, versions, owners, declared
  capabilities, and test cases;
- skills that can mutate host state should be reviewed like code;
- a newly installed skill should not automatically receive root, network, or
  repository-write authority;
- prompt-only skills should not be allowed to smuggle operational authority by
  instructing the model to bypass the policy layer.

### 4. Memory Is an Attack Surface

Persistent memory improves UX, but it can also preserve malicious instructions,
private data, stale assumptions, or attacker-shaped preferences. Memory poisoning
is especially relevant to a shell that may repeatedly operate on the same
machine and repositories.

Corpus implication:

- shell memory must be separate from CursiveRoot measurement truth;
- memory entries need provenance, timestamps, scope, and decay/review rules;
- memories derived from untrusted content should not be treated as operator
  preferences or policy;
- memory should never store credentials, secrets, shell history, browser
  history, clipboard contents, or sensitive file excerpts by default.

### 5. Sandboxing Is Layered, Not Singular

No single Linux containment mechanism solves agent safety. seccomp restricts
syscalls, Landlock restricts selected resource access without root, containers
add namespaces and cgroups, gVisor reduces direct host-kernel exposure, and
Firecracker adds a VM boundary at higher cost. CursiveOS should pick isolation
by task risk.

Corpus implication:

| Risk Class | Example | Suggested Containment |
| --- | --- | --- |
| Read-only inspection | `ls`, `cat`, `journalctl --no-pager`, hardware inventory | direct execution with read-mode allowlist and logging |
| User-file edit | editing a project file or config in an approved workspace | workspace-scoped filesystem policy, diff preview, undo path |
| Network read | fetching docs, package metadata, API docs | network allowlist, no credential forwarding, logged URL/domain |
| Build/test command | package install, compiler, test runner | container or Landlock profile; no broad home-directory access |
| Untrusted code execution | downloaded script, benchmark harness, unknown repo | gVisor or microVM; clean filesystem; no secrets; egress controls |
| Root/system mutation | package manager, kernel/sysctl, service changes | explicit confirmation, narrow helper, reversible plan, post-check |
| Measurement truth | sensor execution and CursiveRoot submission | deterministic daemon path only; no LLM write authority |

### 6. Human Confirmation Needs Specificity

Confirmation UX should not ask the user to approve vague intent. It should show
the concrete command, target files/devices/services, privilege level, network
destinations, reversibility, and expected effect.

Corpus implication:

- bad confirmation: "Allow the agent to fix networking?"
- better confirmation: "Run `sudo sysctl -w net.ipv4.tcp_congestion_control=bbr`
  until reboot; affects kernel network behavior; rollback command is
  `sudo sysctl -w net.ipv4.tcp_congestion_control=cubic`."

The shell should also distinguish ordinary confirmation from high-risk
confirmation. A root action that can break boot, delete data, move funds, expose
secrets, or alter measurement truth should require a stronger confirmation
boundary than editing a Markdown file.

## CursiveOS Design Consequences

1. The existing daemon/shell split is strongly supported by agent-safety
   literature.
2. The shell should be an intent translator and operator interface, not a
   trusted authority.
3. Tool execution should pass through deterministic policy and a risk-based
   sandbox selector.
4. Persistent memory should be scoped, inspectable, and excluded from measurement
   truth.
5. Unattended host mutation should remain disabled until containment and
   confirmation boundaries exist.

## Suggested Source URLs

- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OWASP Agentic Skills Top 10: https://owasp.org/www-project-agentic-skills-top-10/
- NCSC prompt injection guidance: https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
- Microsoft indirect prompt injection guidance: https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- Linux seccomp filter: https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html
- Linux Landlock: https://www.kernel.org/doc/html/latest/userspace-api/landlock.html
- gVisor documentation: https://gvisor.dev/docs/
- Firecracker design: https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md
- Firecracker jailer: https://github.com/firecracker-microvm/firecracker/blob/main/docs/jailer.md

## Containment Primitive Deep-Dive Sources (2026-06-20)

Added to ground Chapter 12's "Containment Primitive Characterization" subsection,
which deepens the previously named-only sandboxing primitives into a
property-level selector for unattended/untrusted execution (Chapter 12 Open
Research Gap #4; RESEARCH_PIPELINE P1 "Sandboxing and least privilege"; P0
knowledge gap "How do current agent systems fail under privilege?").

| Source | Retrieved fact used | URL |
| --- | --- | --- |
| Linux kernel seccomp_filter docs / community write-ups | BPF filters may not dereference pointers, so seccomp can match syscall number and scalar args (e.g. forbid `dup2` to fd 2) but cannot restrict `open()` to a path allowlist; value-by-inspection also makes it immune to TOCTOU argument swaps. | https://docs.kernel.org/userspace-api/seccomp_filter.html ; https://blog.yadutaf.fr/2014/05/29/introduction-to-seccomp-bpf-linux-syscall-filter/ |
| Linux kernel Landlock docs; Phoronix | Landlock merged in 5.13 (ABI v1, filesystem self-restriction, unprivileged); TCP bind/connect added in 6.7 (ABI v4); ABI-versioned and best-effort, so capability depends on the running kernel. | https://docs.kernel.org/userspace-api/landlock.html ; https://www.phoronix.com/news/Landlock-Networking-Linux-6.7 |
| containers/bubblewrap README; systemshardening | bubblewrap is the unprivileged namespace+bind-mount+seccomp engine behind Flatpak; requires unprivileged user namespaces (default on most distros since ~2024, but admins can disable); unprivileged user namespaces are themselves a recurring kernel attack surface. | https://github.com/containers/bubblewrap ; https://www.systemshardening.com/articles/linux/linux-unprivileged-namespace-restriction/ |
| gVisor platform & systrap docs | Sentry re-implements Linux syscalls in Go (memory-safe); platforms are systrap (current default, `SECCOMP_RET_TRAP`/`SIGSYS`), KVM, and deprecated ptrace; overhead negligible for CPU-bound and significant for syscall-heavy workloads; not 100% syscall-compatible. | https://gvisor.dev/docs/architecture_guide/platforms/ ; https://gvisor.dev/blog/2023/04/28/systrap-release/ |
| Firecracker design/spec docs | KVM-backed microVM; ≤125 ms from InstanceStart to guest `/sbin/init`; <5 MiB VMM memory overhead per microVM; `jailer` sets up cgroup/chroot/seccomp/namespaces then drops privileges; powers AWS Lambda and Fargate; host needs KVM and kernel ≥4.14. | https://github.com/firecracker-microvm/firecracker/blob/main/SPECIFICATION.md ; https://firecracker-microvm.github.io/ |
