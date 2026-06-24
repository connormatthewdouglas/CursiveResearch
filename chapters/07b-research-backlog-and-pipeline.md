## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Current synthesis Supported; priorities tracked in `RESEARCH_PIPELINE.md`
**Read with:** [Chapter 07](07-main-repo-gap-closure.md), [RESEARCH_PIPELINE.md](../RESEARCH_PIPELINE.md), [Chapter 00](00-benchmark-schema-and-measurement-validity.md)

### Authoritative for
- Next research targets after gap-closure pass (schema, shell spec, signed presets, fork obligation)
- Experimental lift queue: cold-start confound, proposer test, idle-power channel

### Superseded or narrowed
- Discovery-phase gaps â€” superseded by Ch07 gap-closure answers

### Open until experiment/hardware
- All items in RESEARCH_PIPELINE Â§3 Experimental Lift

---

## Reinforced research (2026-06-24)

- **Proposer falsifier:** `experiments/proposer-vs-random-tuning-experiment.md` (CH05-BM-002) â€” highest-leverage Ch15 validation.
- **Cold-start confound:** `experiments/cold-start-order-cache-confound-plan.md` â€” blocks acceptance-grade fleet claims.
- **Signed preset channel:** Transition 2 heart â€” deep spec still open; links Ch06 regression gates.

---
# Research Backlog and Pipeline

Status: Backlog and pipeline priorities (split from former Ch07, 2026-06-24). Gap status â†’ [Chapter 07](07-main-repo-gap-closure.md).
## What Should Be Added Next

Based on the main repo, the highest-value new research expansions are now:

> **Corpus inline (2026-06-24):** **Split from former Ch07 (2026-06-24):** tracks `RESEARCH_PIPELINE.md` experimental lift — cold-start confound, proposer-vs-random (CH05-BM-002), idle-power channel. Runnable scripts graduate to main `CursiveOS` repo per CORPUS_WORKFLOW.

### 1. Mutation Safety and Permission Law — done (2026-06-22)

Delivered as [Chapter 06](06-mutation-safety-and-permission-law.md): the formal
rulebook defining what agents, daemons, contributors, and users may change under
which gates, with each mutation class bound to the mechanism that enforces it.
Next expansions move down the list.

### 2. CursiveRoot Schema and Evidence Storage

The sensor-array theory is strong. Now the database/storage schema needs to be formalized: raw run, sensor result, variant, hardware fingerprint, confidence, confirmation set, anomaly flags, fitness ledger.

### 3. Natural-Language Shell Implementation Spec

The architecture sketch is good, but the product needs implementation details: UI, command preview, memory, model selection, permission escalation, remote-tier disclosure, and tool sandboxing.

### 4. Signed Preset Channel and Regression-Gated Update Flow

This is the heart of Transition 2. The corpus needs a deep spec on signed presets, staging, local regression, rollback, and divergence reporting.

### 5. Fork Obligation and Bitcoin-Anchored Ledger Research

This is unique and high-risk. It needs legal, technical, and adversarial analysis before being relied on as an economic primitive.

## Corpus Implication

The biggest update is that the project is farther along architecturally than the earlier research gaps implied.

The gaps are no longer:

```text
What is the organism?
What counts as truth?
How are contributors rewarded?
Where does the local agent fit?
```

The main repo answers those at architecture level.

The new gaps are implementation-level:

```text
How is the evidence stored?
How are mutations permissioned?
How are presets signed and rolled back?
How is the shell safely implemented?
How is the economic ledger enforced?
```

That is good news. The corpus should now move from discovery research to specification research.
