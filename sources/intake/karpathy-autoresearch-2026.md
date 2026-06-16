# Karpathy's autoresearch (2026)

**Source type**: Practical research implementation / autonomous experiment loop  
**Primary link**: https://github.com/karpathy/autoresearch  
**Date of release**: Early March 2026  
**Author**: Andrej Karpathy

## Core Idea

`autoresearch` is a minimal, single-GPU system in which an LLM agent autonomously runs an iterative research loop on machine learning training code. The human provides high-level strategy in a `program.md` file; the agent handles code edits, short experiments, evaluation, and selection without further human intervention until morning.

## How the Loop Works

1. Human writes high-level research instructions and goals in `program.md`.
2. An LLM coding agent (Claude, etc.) is pointed at the repository.
3. The agent is only allowed to edit one file: `train.py` (model architecture, optimizer, hyperparameters, etc.).
4. It triggers a short, fixed-length training run (default: exactly 5 minutes wall-clock time, excluding startup).
5. After the run, it evaluates a clear, objective metric (`val_bpb` — validation bits-per-byte; lower is better).
6. If the new result is better than the previous best, the change is kept (committed). Otherwise it is discarded/reverted.
7. The loop repeats autonomously.
8. In the morning, the human reviews `results.tsv` (experiment log) and the final improved model.

The entire process is designed to run overnight on a single NVIDIA GPU.

## Key Design Decisions

- **Constrained mutation surface**: Only one file (`train.py`) can be edited. This keeps changes reviewable and limits the scope of possible damage.
- **Cheap, comparable experiments**: Fixed 5-minute wall-clock budget makes results comparable across runs and platforms.
- **Strong external verifier**: The metric (`val_bpb`) is objective and automatable. The agent does not judge its own success linguistically.
- **Git as memory and audit trail**: Every accepted improvement becomes a commit. Rejected attempts can also be logged. This creates a verifiable history of what was tried and why it was kept or discarded.
- **Human stays high-level**: The human defines the overall goal and success criteria in `program.md`. The agent executes the iteration loop.
- **Selection pressure via measurable improvement**: Only changes that improve the chosen metric survive.

## Relevance to Software Organisms

This project is one of the cleanest existing demonstrations of several concepts central to CursiveOS and the software organism framing:

- **Bounded recursive self-improvement in practice**: The agent improves the training process by editing its own code, but the loop is deliberately constrained and grounded.
- **Verifier as the core of safe improvement**: Success is determined by an external, objective measurement rather than the agent's self-assessment. This directly supports the "verifier as immune system" idea.
- **Cheap iteration + strong selection**: Short experiments + clear metric allow many generations of improvement with limited resources.
- **Archive and negative memory**: Git history naturally records both successful and unsuccessful mutations.
- **Human–agent division of labor**: The human owns strategy and goal definition; the agent owns execution and iteration. This is a healthy pattern for early software organisms.

## What Transfers Well to CursiveOS

- The pattern of cheap, repeatable evaluation loops for candidate presets or mutations.
- Strong emphasis on objective, automatable metrics (aligns with CursiveRoot sensor design).
- Using version control (git) as a transparent archive of accepted variants.
- Keeping mutation surfaces deliberately constrained and reviewable.
- The philosophy of letting the agent do the grunt work of iteration while the human (or higher-level system) sets direction.

## Limitations and Cautions

- The original implementation is specialized for ML training scripts on a single GPU with a fixed time budget.
- Results are tied to the specific metric and experiment length; transferring insights requires care.
- It does not yet address multi-objective fitness, hardware transfer, safety/sandboxing, or long-term organism identity — areas where CursiveOS has stricter requirements.
- Extending the idea to OS-level or runtime mutations would require richer structured feedback from experiments (beyond a single scalar) and stronger safety boundaries.

## Related Work

- Discussions around generalizing the pattern beyond ML training (e.g., to arbitrary software metrics).
- "Bilevel Autoresearch" ideas exploring meta-loops that improve the autoresearch process itself.

## Intake Notes

This source was ingested as a practical demonstration rather than a formal academic paper. The core value lies in the concrete, working example of a bounded, metric-driven self-improvement loop and its implications for verifier design and selection pressure in software organisms.
