<!--
Generated from a preserved DOCX source; wording is retained from the source.
Source: sources/original-docx/5. ai guided tuning_.docx
Git blob SHA: a17532ea3758c27bfd182795d517aee2b80be108
-->

## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Architecture partly Supported; proposer value Unvalidated (CH05-BM-002)
**Read with:** [Chapter 03](03-rsi-literature-and-organism-synthesis.md) (verifier/fitness), [Chapter 05](05-measurement-daemon-and-natural-language-shell.md) (shell vs daemon), [Chapter 00](00-benchmark-schema-and-measurement-validity.md), `experiments/proposer-vs-random-tuning-experiment.md`

Historical note: import text references **TAO-Forge**; current names are CursiveOS / CursiveRoot.

### Authoritative for

- Survey of SchedCP, OS-R1, PolicySmith, SemaTune, BranchFS — see SRC-05-* in `sources/extracted-source-index.md`
- Architectural patterns: MCP control plane, rule-based rewards, transactional rollback, workload analyzers

### Superseded or narrowed

- **"5–25% improvements"** and ranking/effort estimates are import claims — not locally reproduced.
- **Continuous unattended tuning** is Disproven safe today (Chapter 18 / VALIDATION unattended execution row). Any loop must respect Chapter 05 daemon/shell split and Chapter 06 permission law.
- The canonical falsifiable test for "does the proposer add value?" is `experiments/proposer-vs-random-tuning-experiment.md`, not generic optimism about LLM tuning.

### Open until experiment/hardware

- CH05-BM-002 proposer vs random search on cold-start channel
- Repo/license inspection for SRC-05-002, 004, 006 per extraction index

---

## Reinforced research (2026-06-24)

- **Proposer value test:** `experiments/proposer-vs-random-tuning-experiment.md` — CH05-BM-002 still **Unvalidated**; import 5–25% claims not locally reproduced.
- **SchedCP (2025):** Zheng et al., arXiv:2509.01245 — `papers/recursive-self-improvement/schedcp/`; MCP + execution verifier; kernel ≥6.12 sched_ext.
- **OS-R1 (2025):** Lin et al., arXiv:2508.12551 — `papers/recursive-self-improvement/tune-agent/`; rule-based RL rewards for valid kernel configs.
- **SemaTune:** `papers/recursive-self-improvement/sematune/` — online tuning pattern; Ch06 permission law before deployment.
- **BranchFS rollback:** `papers/recursive-self-improvement/branchfs-fec/` — transactional branches align with Ch01 reversible presets.
- **Verifier pattern:** AlphaEvolve, CodeEvolve, FunSearch intakes (Ch03) — external measurement daemon must judge improvements, not the proposer LLM.

## Classical autotuning baselines: what the proposer must beat (2026-06-25)

**Maps to:** this chapter's load-bearing claim **CH05-BM-002** and
`experiments/proposer-vs-random-tuning-experiment.md`; RESEARCH_PIPELINE P0
knowledge gap *"What kinds of recursive self-improvement are real today versus
theoretical?"* and P1 gap *"What is the right evaluation stack for OS-operating
agents?"*

**The gap this fills.** Everything above surveys *LLM-driven* tuners (SchedCP,
OS-R1/TuneAgent, PolicySmith, AutoOS, Liargkovas' always-on agent). But the
corpus's canonical falsifiable test — CH05-BM-002 — is not "does the LLM tune
well?"; it is "does the LLM proposer beat **blind random search over the same
allowlist at equal evaluation budget**, scored only on the clean cold-start
channel?" (`experiments/proposer-vs-random-tuning-experiment.md`, H1). Until
this section, the chapter never grounded *what the classical baselines actually
are* or *why random search is a deceptively strong one*. Without that grounding
it is easy to credit the proposer for a win that a one-line baseline (or pure
chance over a small allowlist) would have captured anyway — the exact failure
mode that sank the "+246% network tuning" result (whole real-path win was
`tcp_congestion_control=bbr`; Ch09 / VALIDATION). The black-box optimization
literature is decades deep; CursiveOS does not get to ignore it just because its
proposer is an LLM.

### The baseline landscape

- **Random search (Bergstra & Bengio 2012, *JMLR* 13:281–305).** The reference
  baseline, and a strong one. The paper shows empirically and theoretically
  that randomly sampled trials find models *as good or better* than grid search
  "within a small fraction of the computation time." The mechanism is **low
  effective dimensionality**: on most problems only a few knobs actually matter,
  and random search samples more *distinct* values along each individual
  dimension than a grid does, so it spends fewer evaluations on knobs that don't
  move the metric. This is precisely the regime of a small CursiveOS allowlist
  seeded with inert decoy knobs — which is why the proposer-vs-random experiment
  uses random search, not grid search, as H0. [retrieval: abstract + JMLR
  summary; full text not fetched]

- **Bayesian optimization (Snoek, Larochelle & Adams 2012, *NeurIPS 25*).**
  Models the objective as a draw from a Gaussian process and picks the next
  trial by an acquisition function, trading exploration for exploitation. More
  sample-efficient than random search *when the surrogate fits* — but the paper's
  own headline finding is that GP kernel choice and the treatment of its
  hyperparameters "play a crucial role," i.e. BO is fragile to misspecification.
  This is the baseline the chapter already references indirectly: Liargkovas
  *et al.* report their always-on LLM agent beating Bayesian optimization by only
  ~5–7% on CFS hyperparameters (see "Top 5 Approaches" §4) — a *few-percent* edge,
  not a category difference, and within the range where measurement noise must be
  ruled out first. [retrieval: NeurIPS abstract + summary]

- **OpenTuner (Ansel *et al.*, PACT 2014; MIT-licensed,
  [github.com/jansel/opentuner](https://github.com/jansel/opentuner)).** The
  program-autotuning analogue closest to CursiveOS's problem (tuning real system
  knobs, not ML hyperparameters). Its central lesson: **no single search
  technique wins across domains**, so it runs an *ensemble* — differential
  evolution, Torczon/Nelder-Mead simplex methods, and greedy evolutionary
  techniques — under an **AUC-Bandit meta-technique** that treats each technique
  as a multi-armed-bandit arm, reallocating the evaluation budget toward
  techniques recently producing speedups and disabling those that don't. Reported
  speedups of up to **~2.8×** over prior techniques across its benchmark suite
  (including searching the GCC `-O` flag space). The transferable point for
  CursiveOS: a credible autotuner is itself a *portfolio with online credit
  assignment*; "an LLM proposer" is one arm in that portfolio, not a replacement
  for it. [retrieval: secondary summaries quoting the paper; PACT PDF returned
  403 — **needs full-text confirmation** of the 2.8× figure and AUC-Bandit
  formula]

- **Hyperband (Li *et al.*, *JMLR* 2017, 18:6765–6816).** Reframes tuning as a
  pure-exploration bandit problem and speeds up random search via **adaptive
  resource allocation + successive halving**: sample many random configs, give
  them a small budget, kill the worst, and reinvest the budget in survivors. It
  beats plain random search precisely *because* it spends almost nothing on bad
  configs. The CursiveOS-relevant caveat: Hyperband assumes a cheap low-fidelity
  proxy that correlates with the full evaluation. The cold-start channel is
  already cheap and the harness already reverts presets between runs, so a
  successive-halving wrapper is a plausible *budget-saver*, but only if a partial
  measurement predicts the confirmed one — untested here. [retrieval: JMLR
  abstract + summary]

- **Google Vizier (Golovin *et al.*, KDD 2017).** Evidence that black-box
  optimization is a *solved, productionized service* problem at scale: Vizier has
  tuned 70M+ objectives at Google, defaults to a Gaussian-process-bandit
  algorithm, and ships transfer learning and automated early stopping. It is the
  "what good looks like" reference for the measurement-daemon side of CursiveOS —
  the optimizer is infrastructure, deterministic and auditable, separate from
  whatever proposes candidates. [retrieval: research.google + KDD summaries]

### CursiveOS implications

| Baseline | What it is | What it implies for CursiveOS |
| --- | --- | --- |
| Random search (Bergstra & Bengio) | Uniform sampling; strong under low effective dimensionality | The honest H0 for CH05-BM-002. If the proposer can't beat it past the cold-start noise floor (CV 0.002, Ch00/Ch22), the proposer adds no value. |
| Bayesian optimization (Snoek) | GP surrogate + acquisition function; sample-efficient but kernel-fragile | A stronger optional baseline arm; the existing ~5–7% LLM-over-BO edge (Liargkovas) is small enough to be noise until verified. |
| OpenTuner (Ansel) | Ensemble of search techniques + AUC-Bandit credit assignment | The right architecture is a *portfolio with online credit assignment*; the LLM proposer is one arm, the measurement daemon is the verifier (Ch05). |
| Hyperband (Li) | Bandit + successive halving over evaluation budget | A budget-saver for the proposer test *if* a cheap partial measurement predicts the confirmed cold-start delta — currently untested. |
| Vizier (Golovin) | Productionized GP-bandit black-box service | "What good looks like" for the daemon-side optimizer: deterministic, auditable infrastructure, decoupled from candidate generation. |

**Net guidance.** (1) The proposer-vs-random experiment is using the *correct*
H0; random search is a strong baseline, not a strawman. (2) The proposer's only
honest justification is beating these classical methods **at equal evaluation
budget on a verifier-clean channel** — anything else risks crediting the LLM for
luck or for a one-knob effect. (3) Architecturally, CursiveOS should treat "LLM
proposer" as one arm in an OpenTuner-style portfolio judged by the external
measurement daemon (Ch05/Ch06), not as a self-grading optimizer. This does
**not** upgrade CH05-BM-002 — it remains **Unvalidated** until the experiment
runs; this section only grounds the baselines the experiment compares against.

**Retrieval caveats.** All five items were retrieved at abstract / publisher-
summary level via web search; no full texts were fetched in this pass. The
OpenTuner 2.8× speedup and AUC-Bandit formula come from secondary summaries
quoting the paper (the PACT 2014 PDF returned HTTP 403) and are marked **[needs
full-text]** above. Numbers are reported as the sources state them and are not
locally reproduced on the CursiveOS harness.

# AI-Guided Tuning

## Corpus integration notes (2026-06-24)

Targeted narrowing for the DOCX import below. TAO-Forge references in the import map to **CursiveOS / CursiveRoot**.

1. **Performance magnitudes (5–25%, 1.79×, ranking table):** Import survey claims — **Unvalidated** on CursiveOS harness. Run `experiments/proposer-vs-random-tuning-experiment.md` before trusting proposer over random search (CH05-BM-002).
2. **Continuous always-on tuning:** Disproven safe for current local agent stack (VALIDATION Ch18 unattended execution). Online agents (Liargkovas et al., NeurIPS ML-Systems 2025 workshop) require MCP commit/revert + Ch06 containment before production.
3. **Daemon/shell boundary:** Tuning agents may *propose* presets; only the measurement daemon may write sensor truth to CursiveRoot (Ch05). Shell LLM must not grade its own mutations.
4. **Paper intakes aligned to import systems:** SchedCP, OS-R1, SemaTune, BranchFS — see `papers/recursive-self-improvement/` and Ch03 cross-link table.
5. **Selection-grade channel:** Cold-start (CV 0.002 on Stardust) is the current highest-confidence tuning target; network magnitude is not quoteable (Ch00/Ch09).

5. Ai guided Linux tuning Executive Summary

This report surveys recent advances (2024–2026) in AI-driven Linux kernel tuning that could be adapted into a self-improving TAO-Forge loop. We identified five leading works: **SchedCP**, **OS-R1**, **PolicySmith**, **LLM Agents for Always-On OS Tuning**, and **AutoOS**. SchedCP (2025) and OS-R1 (2025) are agentic frameworks using LLMs and RL to tune scheduler policies and kernel configs, respectively. PolicySmith (HotNets 2025) uses LLMs plus evolutionary search to *generate* optimal system heuristics (e.g. caching, congestion control). Liargkovas *et al.* (NeurIPS workshop 2025) demonstrate an online LLM agent that continuously tunes Linux CFS scheduler hyperparameters (outperforming Bayesian optimization by a few percent). AutoOS (ICML 2024) is an LLM-driven framework that iteratively compiles and adjusts kernel configurations via an “observe-prune-propose-act-correct” loop. Each approach is open-source (except the NeurIPS workshop paper) and uses novel combinations of LLMs, RL, and search. Key attributes of these approaches are summarized in Table 1.

All identified systems show promising tuning performance (5–25% improvements) on benchmarks【66†L75-L83】【91†L63-L70】【59†L53-L61】. They require (and produce) extensive telemetry (performance counters, workload profiles, output metrics) and substantial compute for LLM inference or RL training.

> **Corpus inline (2026-06-24):** The **5–25%** survey magnitudes are **Unvalidated** on CursiveOS. Canonical falsifier: `experiments/proposer-vs-random-tuning-experiment.md` (CH05-BM-002). Proposers may suggest presets; only the measurement daemon writes sensor truth (Ch05). Continuous unattended tuning **Disproven** safe (VALIDATION Ch18). Common limitations include LLM hallucinations or invalid configurations (addressed via rule-based checking or rollback), high computational cost, and limited generalization. We propose concrete adaptations for each approach to integrate TAO-Forge data (e.g. using TAO’s eBPF instrumentation and metrics as observations), design appropriate rewards and safety guards (e.g. transactional kernel branching【50†L95-L103】), and close the loop in continuous learning. Estimated engineering efforts range from a few to many person-months per approach, with early prototypes achievable in quarters. We conclude with a prioritized roadmap: start with **OS-R1** and **AutoOS** for quick proof-of-concept (they already tune general configs), followed by **SchedCP** and **PolicySmith** for richer scheduling/heuristic generation, and finally full integration with TAO’s continuous data and safety framework. Research risks include LLM reliability and evaluation overhead; however, these can be mitigated by careful reward design and sandboxing (e.g. branch contexts for rollback).

### Top 5 Approaches

1. **SchedCP (Zheng *et al.*, arXiv 2509.01245, 2025; [GitHub, MIT](https://github.com/eunomia-bpf/schedcp))** – An *agentic* LLM framework to tune Linux scheduler policies. SchedCP implements a decoupled control plane (using the Model Context Protocol) with separate components for workload analysis, a policy repository, and an execution verifier【91†L50-L58】【91†L63-L71】. An LLM-driven “sched-agent” uses these components to profile the workload, search or synthesize custom eBPF scheduler policies, and deploy them via the `sched_ext` interface【91†L50-L58】【91†L63-L70】. It achieved up to **1.79× speedup** and **13× lower exploration cost** over naïve agents while maintaining high success rates【91†L63-L70】. Under the hood it uses multi-agent reasoning: an LLM plans and generates code (possibly with chains-of-thought), and Rust components execute and verify performance. Required data includes per-core CPU usage, runnable-queue lengths, and latency/throughput metrics (collected via eBPF). Compute involves heavy LLM queries (e.g. GPT-4 or Claude) and static/dynamic analysis of generated policies. Maturity: code is open-source (MIT license【96†L1-L7】) and tested on benchmarks (e.g. build and synthetic loads), but only experimental so far. **Limitations**: currently focuses on CPU scheduling (requires kernel ≥6.12 with sched-ext), and LLMs may propose invalid policies (mitigated by the Execution Verifier). It also does not yet learn continuously (policies are synthesized per workload). **TAO-Forge adaptation**: SchedCP can be extended to use TAO’s instrumentation (e.g. L3 cache, branch misses) as additional workload features. The MCP server can consume TAO’s JSON/YAML monitoring logs to seed observations. Safety can leverage the proposed *branch context* mechanism (FEC-CTTX【50†L95-L103】) to sandbox kernel policy changes. The reward signal could combine TAO metrics (tail latency, throughput) as in the original paper. Because SchedCP already has a fallback revert strategy (first-commit-wins), it fits well with TAO’s need for transactional updates. **Effort/Cost**: Adapting SchedCP would require ~3–6 months (prototype), including integrating TAO metrics into the workload analyzer and verifying compatibility with TAO kernels. Development of additional scheduler policies (e.g. NUMA-aware) adds more. Compute cost is moderate (LLM calls + eBPF testing); estimate ~$5k–$10k in cloud GPU/API for development, more at scale.

2. **OS-R1 (Lin *et al.*, arXiv 2508.12551, 2025; [GitHub, MIT](https://github.com/LHY-24/OS-R1))** – A rule-based reinforcement learning framework for tuning *general* Linux kernel configurations. OS-R1 formulates kernel tuning as an RL environment for an LLM agent【66†L76-L84】. It uses **Generalized Regularized Policy Optimization (GRPO)** (a PPO variant) via the verl library to train GPT-style agents【66†L76-L84】. The approach decomposes tuning into multi-turn prompts and actions (each action changes one config option). Novel *rule-based rewards* ensure valid config syntax and stable performance improvement【66†L80-L88】. A two-phase training pipeline (warm-up then exploration) leverages a curated kernel-tuning dataset. Data required: initial workload characterization (e.g. via `perf` metrics), performance results for each config set (throughput, latency), and validity checks (compile/boot success). OS-R1 demonstrates ~5.6% improvement over heuristic baselines with high data efficiency【66†L85-L93】. Maturity: published ICML workshop/arXiv, MIT-licensed code【66†L76-L84】【95†L19-L22】, with experiments on web serving and filesystem scenarios. **Limitations**: Training is compute-intensive (requiring many LLM rollouts), and LLMs can hallucinate invalid configs (though the system filters these via the format reward). It currently assumes a relatively stable workload and offline training (not live). **TAO-Forge adaptation**: OS-R1 is well-suited to use TAO-Forge’s rich telemetry. The RL agent’s observations can include TAO-exposed metrics (CPU, I/O, GPU usage). The reward can be defined in terms of TAO goals (e.g. latency SLAs, or energy efficiency metrics). Incorporating TAO data formats (JSON metrics, time-series logs) would enable end-to-end integration. Instrumentation (via BPF) already exists in TAO, so we’d hook these into the RL observations. For safety, we would wrap config changes in a branch context (commit/rollback) to avoid bricking the system. **Effort/Cost**: Modifying OS-R1 to a specific TAO workload is ~2–4 months: reuse its RL engine but supply TAO metrics and reward. Major effort is labeling TAO workloads and possibly retraining. Compute cost is high – expect on the order of $10k+ in GPU/LLM API spend for training prototypes.

3. **PolicySmith (Dwivedula *et al.*, arXiv 2510.08803, HotNets 2025; [GitHub](https://github.com/ldos-project/policysmith))** – An LLM-driven *heuristic synthesis* framework. Rather than tuning parameters, PolicySmith **automatically writes new policies** for system components. It uses large language models (LLMs) guided by **evolutionary search** to generate candidate C/C++ code for, e.g., caching and congestion control heuristics【59†L53-L61】. The system iterates (LLM propose → compile/test → score → evolve) to discover “instance-optimal” code. In caching, it found replacement policies outperforming classic algorithms; for TCP congestion control, it generated safe algorithms that can be inserted into the Linux kernel【59†L53-L61】. Required data: realistic workload traces (e.g. web request logs, network traces) for evaluation, and reward signals (hit rate, throughput, etc.). Compute: very heavy (hundreds of LLM queries and heavy compile/profile loops). Maturity: HotNets paper (2025) with code released, but early stage – tested on specific domains. License: code exists but no explicit license file (likely internal). **Limitations**: Computational cost is very high. The search may get stuck in local optima; ensuring safety is nontrivial (though authors checked correctness and bounded policies). Generated code can have bugs, so rigorous validation (like their static/dynamic analysis) is needed. **TAO-Forge adaptation**: PolicySmith’s approach could generate new OS heuristics tailored to TAO workloads. For example, it could evolve a NUMA-aware scheduling or cache policy using TAO’s performance traces as fitness. We would integrate TAO trace data as inputs, and use TAO’s performance harness (benchmarks, profilers) for scoring. Safety: all synthesized code would run in an isolated environment (e.g. QEMU or container) before merge. Effort: This is a large project. Building a full evolutionary synthesis for TAO (likely requiring dozens of GPUs and months of tuning) is on the order of **6–12 engineering months** for a prototype. Compute cost is substantial (tens of thousands of dollars in GPU/LLM usage).

4. **LLM Agents for Always-On OS Tuning (Liargkovas *et al.*, NeurIPS ML-Systems 2025)** – A continuous online tuning approach using LLM agents. This workshop paper designs an **LLM agent-in-the-loop** for the Linux CFS scheduler. In experiments the agent tunes one or two parameters (like `sched_latency_ns` and `sched_wakeup_granularity`), adapting to changing workloads in real time. It outperforms Bayesian optimization by ~5–7% and even slightly beats a human expert【82†L231-L239】. Key idea: the LLM reasons over recent performance metrics (e.g. tail latency, IPC proxy) and proposes gradual adjustments. When hardware counters aren’t available, it uses system-level proxies like IPC to preserve latency【82†L231-L239】. The authors also propose architectural features: use the Model Context Protocol (MCP) for tool integration, and enforce *transactional apply/commit/revert* semantics and human-in-the-loop approval gates for safety【82†L239-L247】. Data: relies on continuous metrics (latency histograms, throughput counters) from TAO-style instrumentation. Compute: relatively light (the LLM makes single-shot or few-shot decisions per tuning interval). Maturity: concept demonstrated on an academic rig (no public code). **Limitations**: So far only single-subsystem (CFS hyperparameters) and small scale. It assumes the LLM generalizes from its prompts (no RL training). **TAO-Forge adaptation**: This maps directly to TAO’s vision of “always-on” tuning. We can implement this agent to tune any tunable OS knob in TAO (CFS, VM, I/O). The MCP and commit/revert features they suggest (atomic commit with first-commit-wins) align with TAO’s safety needs【82†L239-L247】【50†L95-L103】. Integrate by feeding TAO’s real-time metrics into the agent’s prompts and logging agent actions in the TAO evaluation harness. Since it’s online, this loop runs continuously on the TAO control plane. **Effort/Cost**: Moderate. A prototype agent for a handful of parameters can be built in ~1–2 months, using OpenAI API (4K-8K token prompts) and TAO’s metric APIs. Compute cost is low per tuning step (cent-scale per LLM call). Building a robust continuous service (with rollback) may take ~3–6 months.

5. **AutoOS (Chen *et al.*, ICML 2024; [GitHub](https://github.com/xuewuyinhe/AutoOS), license unspecified)** – An LLM-guided kernel configuration optimizer for AIoT scenarios. AutoOS models the Linux Kconfig hierarchy as a dynamic tree and uses a prompt-driven state-machine loop (“observe→prune→propose→act→correct”)【77†L27-L36】. At each step, GPT-3.5-turbo is queried to suggest which config options to enable/disable, given compile errors or performance feedback. Invalid subtrees are pruned, and the LLM is re-prompted on failures (using “correction” prompts). In experiments AutoOS automatically finds custom kernel configs outperforming vendor defaults by up to **25%** in embedded benchmarks【77†L33-L37】. Data: just the kernel’s text-based compile output and simple performance stats (binary search fallback monitors successful boot). Compute: moderate (LLM calls plus repeated kernel compiles). Maturity: peer-reviewed (ICML), code available (no explicit license). **Limitations**: LLM hallucinations can propose syntactically invalid configs; the paper needed multiple LLM passes and binary-search fallback to handle boot failures【13†L367-L374】. It’s also offline (not continuous). **TAO-Forge adaptation**: AutoOS could use TAO’s data as the “workload description” – e.g. give the LLM a summary of TAO’s collected metrics and targets. The pruning/correction mechanism aligns with TAO safety: any config that fails can be rolled back. To make it continuous, we would periodically re-run the loop as hardware or workloads change. **Effort/Cost**: Low to moderate. A baseline AutoOS agent can be prototyped in ~1–2 months using TAO’s build/test environment. The LLM costs are similar to OS-R1 (hundreds of API calls). Tuning it to specific TAO workloads (and adding TAO performance metrics into the loop) is straightforward once the framework is in place.

**Comparison Table.** Key attributes of the five approaches are summarized below:

| Approach                           | Technique           | Data & Compute Needs                 | License   | Maturity (2025)           | Effort/Cost Estimate       |

|------------------------------------|---------------------|--------------------------------------|-----------|---------------------------|----------------------------|

| **SchedCP** (Zheng *et al.*, 2025) | Multi-agent LLM + eBPF; MCP control plane【91†L50-L58】【91†L63-L71】 | Workload profiles (perf/eBPF), multi-LLM queries; custom static/dynamic analysis | MIT【96†L1-L7】 | ArXiv+GitHub; demonstrated on schedulers (1.79× perf)【91†L63-L70】 | ~3–6 dev-months; moderate GPU/LLM cost (~$5–10k) |

| **OS-R1** (Lin *et al.*, 2025)     | Rule-based RL (GRPO/PPO) over LLM agent【66†L76-L84】 | Kernel metrics & build feedback; many LLM rollouts; verl RL library | MIT【95†L19-L22】 | ArXiv+GitHub; tested on real workloads (5.6% gain)【66†L85-L93】 | ~2–4 dev-months; high training cost (~$10k+ GPU/APIs) |

| **PolicySmith** (Dwivedula *et al.*, 2025) | LLM + Genetic search for code synthesis【59†L53-L61】 | OS traces (cache, network) and performance scores; vast LLM+compilation loops | (none)   | ArXiv+GitHub; early HotNets demo; caching and TCP examples【59†L53-L61】 | ~6–12 dev-months; very high compute (~$20k+ GPUs/APIs) |

| **Always-On LLM** (Liargkovas *et al.*, 2025) | Online LLM agent (few-shot); MPC loop (apply/commit)【82†L231-L239】 | Live system metrics (latency, IPC proxies); few LLM calls per interval | (none)   | Workshop poster; tuned CFS hyperparams (5–7% better)【82†L231-L239】 | ~1–2 dev-months; low cost (mostly API calls, <$1k) |

| **AutoOS** (Chen *et al.*, 2024)   | Iterative LLM-driven config loop【77†L27-L36】 | Kernel compile logs, boot success; moderate LLM + build cycles | (none)   | ICML paper; code available; >25% perf gain on IoT configs【77†L33-L37】 | ~2–3 dev-months; moderate cost (LLM+compiles, ~$5k) |

### Limitations and Failure Modes

- **Invalid proposals:** LLMs may hallucinate invalid configs or policies. Each approach mitigates this differently (e.g. OS-R1 uses rule-based formatting rewards【66†L80-L88】; SchedCP uses an Execution Verifier【91†L50-L58】; AutoOS prunes failing subtrees【77†L27-L36】). Still, invalid proposals can waste time or crash the kernel.

- **High compute:** OS-R1 and PolicySmith in particular require substantial compute (LLM training or search). This may limit real-time use. Offline RL training (OS-R1) or very long evolutionary runs (PolicySmith) are expensive.

- **Narrow domain/generalization:** SchedCP is currently limited to CPU schedulers; Liargkovas only explored CFS hyperparams; AutoOS targeted AIoT kernels. Adapting to new subsystems (e.g. VM, I/O) may require new modeling.

- **Data requirements:** RL methods need representative workloads and metrics. Without good data, learned policies may not generalize.

- **Safety and stability:** Even if performance improves, unintended side-effects are possible (e.g. new schedulers that starve threads). The proposed transactional branching (e.g. BranchFS【50†L95-L103】) or human approval gates【82†L241-L247】 are essential.

### Integration with TAO-Forge

To integrate these approaches into **TAO-Forge**, we propose the following common adaptations:

- **Data formats:** TAO-Forge instruments Linux via eBPF and exports metrics (e.g. CPU/memory/GPU utilization, tail latencies). All agents should consume these in their native format (JSON or in-memory). For example, the LLM prompts can include key metrics (encoded or tabulated) as context. Agents should output actions (e.g. config changes or new code) in a defined schema. TAO’s **evaluation harness** (scripts that apply config, run benchmarks, record results) can serve as the environment.

- **Instrumentation hooks:** Use TAO’s existing probes for performance counters. SchedCP already uses BPF to measure scheduling; OS-R1 can use `perf` counters. AutoOS will rely on the TAO kernel build logs.

- **Reward design:** Define rewards in terms of TAO goals. For latency-sensitive workloads, reward could be negative tail latency or SLA violations. For throughput, use normalized throughput gains. Combine multiple metrics (e.g. energy vs. performance) as weighted sums. Liargkovas suggests surrogate metrics (IPC) if fine-grained counters are unavailable【82†L231-L239】.

- **Safety/Rollback:** Employ transactional branching as in “Fork, Explore, Commit”【50†L95-L103】. For every agentic action, record a shadow copy of state. On failure or degraded performance, rollback to the last safe state. TAO could integrate BranchFS or a similar sandbox to isolate trials. Agents should be restricted to *off-critical-path* operations with explicit commit after validation (as Liargkovas propose【82†L241-L247】).

- **Continuous learning loop:** Instead of one-shot tuning, create a feedback loop. For RL (OS-R1), continuously retrain with fresh TAO data (fine-tuning on new workloads). For Always-On and AutoOS, schedule periodic re-optimization (e.g. after each major workload shift or nightly). Tie the agents to TAO’s version-control for kernel parameters to log changes and outcomes.

- **Evaluation harness:** Leverage TAO-Forge’s benchmarking suite: run standardized tests after each adaptation. Use TAO’s metrics to automatically compare performance before/after. This harness closes the loop, feeding results back into the agents (for RL, fine-tuning; for LLMs, as new examples or prompt context).

### Estimated Engineering Effort and Timeline

| Adaptation Task                          | Prototype Timeline | Prod Timeline | Effort/Cost                                 |

|------------------------------------------|--------------------|---------------|---------------------------------------------|

| **SchedCP → TAO integration:** Integrate TAO metrics into workload analyzer; extend to other schedulers/heuristics. | 3–6 mo | 6–12 mo     | 3–4 dev-months; ~GPU/LLM rent for testing ($5–10K) |

| **OS-R1 → TAO integration:** Wrap TAO’s autotune harness as the RL environment; fine-tune agent on TAO workloads. | 2–4 mo | 6–9 mo      | 2–3 dev-months; high LLM training cost ($10K+)    |

| **PolicySmith → TAO:** Use TAO trace data and evaluation for code-gen; sandbox compile and test new policies. | 6–12 mo | 12–18 mo    | 6–10 dev-months; very high compute ($20K+)       |

| **Always-On LLM Agent:** Connect TAO metric APIs to LLM prompts; implement commit/revert hook. | 1–2 mo | 3–6 mo      | 1–2 dev-months; low API cost (<$1K)             |

| **AutoOS → TAO:*

> **Corpus note (2026-07-06, truncation confirmed at source):** The import ends mid-row above because the preserved source DOCX (`sources/original-docx/5. ai guided tuning_.docx`, blob a17532ea) is itself truncated at exactly this point — verified by unpacking the DOCX: its final paragraph is the literal fragment `| **AutoOS → TAO:*` followed by the document close. The import is faithful; no fuller source exists in the repo. The missing row's substance is recoverable from this same chapter: Table 1 gives AutoOS ~2–3 dev-months at moderate cost (~$5k), and §Top 5 item 5 gives a ~1–2 month prototype path. Keep the partial row as-is (import fidelity); do not delete it.
