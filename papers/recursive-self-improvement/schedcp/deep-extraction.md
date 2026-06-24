# SchedCP — Deep Extraction

Source: https://arxiv.org/abs/2509.01245
Authors / Lab: Yusheng Zheng, Yanpeng Hu, Wei Zhang, Andi Quinn
Year / Venue: 2025, MLforSystem / arXiv (2509.01245v4)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (CC BY 4.0)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Semantic gap | Kernel schedulers lack application semantics | Problem framing |
| SchedCP architecture | Decoupled control plane for LLM scheduler agents | Core design |
| MCP server | Stable tool interface for observe/act | Implementation |
| sched-agent | Multi-agent workload analysis + eBPF synthesis | Demonstration |
| Evaluation | Performance, cost, success rate | Empirical claims |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| OS schedulers suffer semantic gap — policies don't understand app needs | Abstract | Conceptual + results | High |
| SchedCP enables fully autonomous LLM optimization of Linux schedulers safely | Abstract | Framework + verifier | High |
| Decoupled control plane separates semantic reasoning from execution/observation | Abstract | Architecture | High |
| Two-stage problem: goal-inference then policy-synthesis | Abstract | Decomposition | High |
| MCP server exposes Workload Analysis, Policy Repository, Execution Verifier | Abstract | API design | High |
| Up to 1.79× performance improvement, 13× cost reduction vs naive agentic approaches | Abstract | Evaluation | High (abstract) |
| High success rate maintained | Abstract | Reliability | Medium |

## 3. System / Method Architecture

```
sched-agent (multi-agent LLM)
    ↔ SchedCP MCP server
        → Workload Analysis Engine
        → Scheduler Policy Repository (evolving archive)
        → Execution Verifier (static + dynamic checks on eBPF)
    → deploy via sched_ext
```

AI decides *what* to optimize; system controls *how* to observe, validate, and act.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Workload Analysis Engine | Infers optimization goals from telemetry | Traces, metrics | Structured goals | Bridges semantic gap |
| Policy Repository | Stores/evolves scheduling policies | Past eBPF programs | Retrieval + mutation seeds | Organism memory |
| Execution Verifier | Static/dynamic validation before deploy | Generated code/config | Pass/fail | Frozen safety gate |
| MCP control plane | Standardized agent tools | Agent requests | Safe actions | Separates reasoning from actuation |
| sched_ext deployment | Loads custom schedulers in Linux | Verified eBPF | Live policy | Real kernel impact |

## 5. Experimental Setup

- Platform: Linux with sched_ext / eBPF.
- Agent: sched-agent (multi-agent).
- Baselines: naive agentic approaches **[needs full-text]**.
- Metrics: performance multiplier (up to 1.79×), cost (13× reduction), success rate.
- Open source: github.com/eunomia-bpf/schedcp.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Performance | up to 1.79× | Default/generic sched | Semantic scheduling wins | Workload-specific |
| Cost efficiency | 13× cheaper | Naive agents | Control plane essential | Cost metric definition **[needs full-text]** |
| Reliability | High success rate | Naive agents | Verifier enables autonomy | **[needs full-text]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | SchedCP architecture diagram | Control plane pattern | Yes |
| **[needs full-text]** | Workload-specific gains | Where semantic sched helps | Yes |

## 8. Limitations Stated By Authors

- **[needs full-text]** — sched_ext availability, workload coverage.

## 9. Limitations Inferred By Corpus

- Scheduler-only scope vs full sysctl/kernel tuning (SemaTune/TuneAgent).
- eBPF verifier ≠ full system safety proof.
- 1.79× may not translate to CursiveOS composite fitness.

## 10. Failure Modes and Safety Concerns

- Verifier bypass or bugs → bad eBPF in kernel.
- Goal inference wrong → optimizes wrong objective.
- Repository pollution with brittle policies.

## 11. What Transfers To Software Organisms

- Decoupled control plane pattern for any OS mutation class.
- MCP-style tool interfaces for agent actions.
- Execution Verifier as analogue to CursiveOS sensor array gate.
- Policy archive for evolutionary scheduler organisms.

## 12. What Does Not Transfer

- Naive end-to-end LLM kernel hacking without verifier.
- Claiming SchedCP results generalize to network stack presets without testing.

## 13. CursiveOS / Corpus Implications

SchedCP is the reference "agentic OS" architecture for CursiveOS scheduler organisms. Emulate: semantic analysis → synthesis → verifier → deploy. Pairs with BranchFS for speculative policy trials. Cost reduction vs naive agents supports AI Agents That Matter joint optimization.

## 14. Open Questions

- Unified SchedCP + SemaTune control plane for multi-knob organisms?
- sched-agent policies in MAP-Elites archive across behavioral niches?

## 15. Extraction Coverage Notes

- Abstract-complete; MLforSystem body **[needs full-text]**

## 16. Source Reliability

arXiv + MLforSystem workshop; open source. Credible systems+agents work.