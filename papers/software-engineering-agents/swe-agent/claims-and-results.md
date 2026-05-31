# SWE-agent — Claims and Results

## Decision-Relevant Claims

| Claim | Status In Corpus | Evidence | CursiveOS Use |
| --- | --- | --- | --- |
| Agent-computer interface design materially affects agent performance. | Supported | SWE-agent improves over RAG and shell-only baselines. | Treat Cursive shell UX/tool design as a research variable. |
| Raw human-oriented shell interaction is not always agent-friendly. | Supported | Shell-only and search ablations show inefficiency and context waste. | Do not expose root terminal power as the default model action space. |
| Simple, bounded tools plus concise feedback help agents recover. | Supported | Search/edit/context ablations. | Build explicit Cursive shell tools with policy metadata. |
| Better ACI increases capability but does not itself solve safety. | Corpus inference | Paper is performance-oriented, not a complete safety framework. | Pair ACI with deterministic policy and sandboxing. |

## Key Results

| Result | Number / Observation | Notes |
| --- | --- | --- |
| Full SWE-bench result | GPT-4 Turbo SWE-agent resolves 12.47% | Reported on 2,294 tasks. |
| SWE-bench Lite result | GPT-4 Turbo SWE-agent resolves 18.00% | Compared to shell-only 11.00% and RAG 2.67%. |
| Claude transfer | Claude 3 Opus SWE-agent resolves 10.46% full / 13.00% Lite | ACI is not single-model-only. |
| HumanEvalFix | About 88.3% pass@1 overall | Narrower debugging setting. |
| Search lesson | Iterative search underperforms summarized search | Human UI patterns can be bad for agents. |
| Context lesson | Full-file context underperforms focused windows | More context is not automatically better. |
