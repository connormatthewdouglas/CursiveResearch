# Open-Endedness is Essential for ASI — Deep Extraction

Source: https://arxiv.org/abs/2406.04268
Authors / Lab: Edward Hughes, Michael Dennis, Jack Parker-Holder, Feryal Behbahani, Aditi Mavalankar, Yuge Shi, Tom Schaul, Tim Rocktäschel
Year / Venue: 2024, ICML 2024 (arXiv:2406.04268v1)
Corpus Status: unvalidated
Extraction Type: cornerstone
Rights Status: full-text allowed; `paper.pdf` and `paper.md` stored under CC BY 4.0

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Context | Foundation models + internet scale | Current AI surge |
| Open-endedness gap | Ever self-improving AI remains elusive | Problem |
| Formal definition | Novelty + learnability for human observer | Theory contribution |
| Path to ASI | Open-ended systems atop foundation models | Positive vision |
| Safety | Implications of capable open-ended AI | Risk section |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Ingredients now exist to achieve open-endedness relative to human observer | Abstract | FM + algorithms | Medium (position) |
| Open-endedness is essential property of artificial superhuman intelligence | Abstract | Argument | Medium (thesis) |
| Formal definition via novelty and learnability | Abstract | Theory | Medium — full text now stored locally; formalism needs second-pass hardening |
| Path: open-ended FM-based systems making novel human-relevant discoveries | Abstract | Research agenda | Medium |
| Safety implications must be examined for capable open-ended AI | Abstract | Safety discussion | High |
| Open-ended FMs will be increasingly fertile, safety-critical research area | Abstract | Conclusion | High |

## 3. System / Method Architecture

Position/theory paper — no single implemented system. Conceptual stack:

```
Foundation model (broad prior)
    + open-ended outer loop (novelty generator + selection)
    + human-relevant learnability filter
    → continual novel discoveries
```

Formalizes open-endedness: generated artifacts must be novel yet learnable/valuable to humans.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Novelty criterion | Rewards new behaviors/discoveries | Archive + candidate | Novelty score | Prevents stagnation |
| Learnability criterion | Ensures human-usable progress | Human observer model | Filter | Avoids alien junk |
| FM substrate | General prior for proposals | Prompts, tools | Candidates | Sample efficiency |
| Safety analysis | Identifies failure modes of OE systems | Capability growth | Guidelines | Governance |

## 5. Experimental Setup

Not empirical benchmark paper. Argumentative structure with references to POET, quality-diversity, FM agents. Full text is now stored locally for illustrative-example hardening.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Theoretical framing | N/A | Prior informal OE discourse | Clarifies research target | Not empirically tested |
| Research agenda | N/A | N/A | FM+OE is near-term priority | Speculative |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| Full text available | Novelty/learnability diagram | Formalism visual | Yes; second-pass figure extraction needed |

## 8. Limitations Stated By Authors

- Position paper — empirical validation of ASI path incomplete.
- Full text now available for second-pass safety-scope extraction.

## 9. Limitations Inferred By Corpus

- "Essential for ASI" is philosophical, not proven theorem.
- Human-relevant learnability hard to operationalize for OS organisms.
- Open-endedness without frozen verifiers conflicts with CursiveOS safety defaults.

## 10. Failure Modes and Safety Concerns

- Unbounded novelty generation with misaligned learnability filter.
- Capability acceleration outpacing oversight.
- Open-ended benchmark mutation creating untestable deployment surface.

## 11. What Transfers To Software Organisms

- Dual criteria: explore novel presets AND remain evaluable on sensor array.
- Position open-ended evolution as long-horizon goal, not one-shot optimization.
- Explicit safety chapter cross-links required.

## 12. What Does Not Transfer

- Treating position paper thesis as implemented CursiveOS capability.
- Removing human/population gates in name of open-endedness.

## 13. CursiveOS / Corpus Implications

RSI-032 provides theoretical justification for POET/MAP-Elites/DGM direction in corpus. CursiveOS should pursue *bounded* open-endedness: novelty in preset space with frozen sensors and confirmation gates. Cite ICML 2024 paper when arguing against single-benchmark hill-climbing.

## 14. Open Questions

- Operational learnability metric for hardware-scoped organisms?
- Safe novelty bounds for live-service OS tuning?

## 15. Extraction Coverage Notes

- Full text now stored in `paper.md`; formalism details need second-pass extraction hardening.

## 16. Source Reliability

ICML 2024 position paper (DeepMind/Google-affiliated authors). High influence; not an systems implementation paper.