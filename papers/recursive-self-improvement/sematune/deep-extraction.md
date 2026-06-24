# SemaTune — Deep Extraction

Source: https://arxiv.org/abs/2605.15026
Authors / Lab: Georgios Liargkovas, Mihir Nitin Joshi, Hubertus Franke, Kostis Kaffes
Year / Venue: 2026, arXiv (2605.15026v1)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (CC BY 4.0)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Motivation | Limits of black-box OS tuners on live hosts | Semantic structure needed |
| SemaTune framework | Host-side steady-state tuning with bounded LLM | Method |
| Decision context | Schemas, telemetry, history, retrieved runs | Context engineering |
| Dual loops | Fast update loop + slow strategy loop | Latency/cost control |
| Validation layer | Typed checks before sysctl/kernel apply | Safety |
| Evaluation | 13 workloads, 41 Linux params | Empirical results |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Black-box scalar-reward tuners ignore cross-knob structure and cause persistent degraded regions | Abstract | Problem analysis | High |
| SemaTune uses compact semantic context from schemas + telemetry + history | Abstract | Architecture | High |
| Fast + slow control loops with typed validation constrain model authority | Abstract | Design | High |
| 72.5% stable-phase improvement over defaults; 153.3% vs strongest non-LLM baseline (suite aggregate) | Abstract | 13 workloads | High (abstract) |
| ~$0.20 model cost per 30-window session | Abstract | Cost reporting | High |
| With only host-level metrics, beats baselines with direct app objectives by 93.7 percentage points | Abstract | Indirect signal claim | Medium |
| Avoids severe degraded regions from structure-blind exploration | Abstract | Safety/robustness | Medium |

## 3. System / Method Architecture

```
Host telemetry + knob schema + current config + action-response history + retrieved prior runs
    → compact decision context
Fast loop: propose low-latency knob updates
Slow loop: periodically revise search strategy
    → typed validation
    → apply to kernel/sysctl interfaces
    → measure stable-phase performance
```

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Semantic context | Encodes OS-control meaning | Schemas, metrics | LLM-readable state | Cross-knob reasoning |
| Dual-loop control | Separates tactics vs strategy | Timescales | Updates + plan shifts | Cost/latency bounded |
| Typed validation | Rejects illegal/harmful configs | Proposals | Safe applies | Live host safety |
| Retrieval from prior runs | Memory across sessions | Archive | Better proposals | Organism memory |
| Host-only metrics mode | Tune without app-level objectives | CPU, memory, I/O proxies | Indirect optimization | Practical deployment |

## 5. Experimental Setup

- Workloads: 13 live workloads from five benchmark suites.
- Parameters: up to 41 Linux knobs.
- Baselines: strongest non-LLM tuner + structure-blind explorers **[needs full-text names]**.
- Metrics: stable-phase performance, degraded region incidence, model cost.
- Setting: online tuning on running services.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| vs defaults | +72.5% stable-phase (aggregate) | Default configs | Large headroom | Aggregate statistic |
| vs best non-LLM | +153.3% relative | Strong baseline | LLM semantics help | Baseline identity **[needs full-text]** |
| Cost | ~$0.20 / 30 windows | N/A | Practical online use | Model pricing dependent |
| Host-only metrics | +93.7 pp vs app-objective baselines | Indirect vs direct | Works without app metrics | Surprising — verify per workload |
| Safety | Degraded region avoidance | Structure-blind methods | Validation + semantics reduce harm | **[needs full-text]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| 12 figures (noted) | Workload curves, ablations | **[needs full-text]** | Yes when retrieved |
| Per-suite breakdown | Generalization | Which domains benefit | Yes |

## 8. Limitations Stated By Authors

- **[needs full-text]** — 17 pages; likely kernel version, LLM choice, stability windows.

## 9. Limitations Inferred By Corpus

- Live-service tuning risk remains despite validation.
- Aggregate percentages may hide workload regressions.
- LLM dependency for semantic reasoning — fallback needed.

## 10. Failure Modes and Safety Concerns

- Persistent degraded regions if validation incomplete.
- Host-proxy metrics misaligned with true SLOs.
- Retrieval of bad prior runs reinforces mistakes.

## 11. What Transfers To Software Organisms

- Semantic knob schemas as genome documentation.
- Dual-loop fast/slow control for organism metabolism.
- Typed validation before any production apply.
- Cost-per-session reporting (AI Agents That Matter alignment).
- Memory of prior tuning runs in archive.

## 12. What Does Not Transfer

- Claiming 153% improvement on CursiveOS sensor composite without matching workloads.
- Removing human/population confirmation for production deploy.

## 13. CursiveOS / Corpus Implications

Strongest practical reference for online OS organism tuning with LLMs. Complements TuneAgent (RL) and SchedCP (scheduler-specific). CursiveOS should adopt semantic context + validation + dual loops as default pattern for sysctl organisms; report costs alongside sensor deltas.

## 14. Open Questions

- SemaTune controller as preset inside CursiveOS population archive?
- Cross-hardware transfer of retrieved tuning memory?

## 15. Extraction Coverage Notes

- Rich abstract extraction; full 17-page validation **[needs full-text]**

## 16. Source Reliability

2026 arXiv CS.OS with detailed abstract metrics. Credible; full peer review pending.