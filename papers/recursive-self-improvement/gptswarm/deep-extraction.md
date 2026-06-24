# GPTSwarm (Language Agents as Optimizable Graphs) — Deep Extraction

Source: https://arxiv.org/abs/2402.16823
Authors / Lab: Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, Jürgen Schmidhuber
Year / Venue: 2024, ICML 2024 (arXiv:2402.16823v3)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (CC BY-NC-SA 4.0)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Unification | LLM agents as computational graphs | Consolidate disparate prompt pipelines |
| Node optimization | Refine per-node LLM prompts | Local improvement operator |
| Edge optimization | Change graph connectivity / orchestration | Global structure search |
| Hierarchy | Composite graphs for multi-agent collaboration | Scaling agent systems |
| Experiments | Automatic improvement of various agents | Empirical validation |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| LLM agents can be represented as optimizable computational graphs | Abstract | Formalism + code | High |
| Nodes process multimodal data / query LLMs; edges define information flow | Abstract | Architecture | High |
| Automatic optimizers improve node prompts and edge connectivity | Abstract | Optimizer algorithms | Medium |
| Framework develops, integrates, and automatically improves diverse LLM agents | Abstract | Experiments | Medium |
| Graphs compose recursively for inter-agent hierarchies | Abstract | Design | High |

## 3. System / Method Architecture

```
Graph G = (V, E)
  Node v: function (LLM call, tool, multimodal op)
  Edge e: routes outputs → inputs
Optimizer:
  node_opt: tune prompts per node
  edge_opt: add/remove/rewire edges
Evaluation on task metric → update graph
Composite graphs: subgraph agents nested
```

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Node optimization | Prompt/program refinement | Node + task loss | Better local node | Fine-grained control |
| Edge optimization | Topology search | Graph + task loss | Better orchestration | Multi-agent structure evolution |
| Graph composition | Hierarchical swarms | Subgraphs | Larger agent systems | Modular evolution |
| Automatic optimizer | Search over graph space | Metrics | Improved agent graph | Meta-level RSI on orchestration |

## 5. Experimental Setup

- Tasks: multiple LLM agent benchmarks **[needs full-text list]**.
- Optimizers: node + edge variants.
- Baselines: hand-designed prompt graphs.
- Open source: github.com/metauto-ai/gptswarm.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Automatic graph optimization improves task performance | Task accuracy | Manual graphs | Structure search pays off | **[needs full-text numbers]** |
| Edge optimization contributes beyond node-only | Ablation | Node-only vs full | Topology matters | **[needs full-text]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | Example agent graphs | Node/edge semantics | Yes |
| **[needs full-text]** | Optimization trajectories | Convergence behavior | Optional |

## 8. Limitations Stated By Authors

- **[needs full-text]**

## 9. Limitations Inferred By Corpus

- Search space explosion for large graphs.
- Optimizing on benchmark may overfit graph topology to holdout leakage without discipline.
- NC-SA license affects derivative redistribution.

## 10. Failure Modes and Safety Concerns

- Edge rewiring can route around safety nodes.
- Optimizer may add cost-increasing nodes for marginal accuracy (see AI Agents That Matter).

## 11. What Transfers To Software Organisms

- Represent organism agent pipelines as mutable graphs (bounded presets).
- Separate node (local prompt/tool) vs edge (control flow) mutation operators.
- Hierarchical swarms for population of specialists.

## 12. What Does Not Transfer

- Unconstrained graph self-modification of verifier subgraphs.
- Assuming ICML task gains transfer to kernel tuning without new evaluators.

## 13. CursiveOS / Corpus Implications

RSI-007 provides formalism for evolving orchestration without touching base model weights — analogous to STOP/Gödel Agent but graph-structured. Use for local multi-agent preset evolution with frozen sensor leaf nodes.

## 14. Open Questions

- Which graph nodes must remain immutable in CursiveOS (sensors, deployment gates)?
- Joint graph + preset genome encoding?

## 15. Extraction Coverage Notes

- Abstract-grounded; full ICML body **[needs full-text]**

## 16. Source Reliability

ICML 2024 peer-reviewed; open codebase. High methodological credibility.