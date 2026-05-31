# SWE-bench — Claims and Results

## Decision-Relevant Claims

| Claim | Status In Corpus | Evidence | CursiveOS Use |
| --- | --- | --- | --- |
| Real-world software issue resolution is much harder than code-completion benchmarks. | Supported | 2,294 real GitHub issue tasks; low baseline resolve rates | Use realistic task reconstruction for shell/agent evaluation. |
| Execution-based validation is essential for coding agents. | Supported | Benchmark accepts patches based on test outcomes | Prefer sensors/tests/post-checks over model self-report. |
| Long context can distract rather than help. | Supported | Larger BM25 retrieval context can improve recall while lowering resolution | Keep shell context minimal and task-specific. |
| Passing tests is not full proof of quality. | Supported | Authors' limitations note generated solutions may be less comprehensive/efficient/readable | Add review, regression, and safety checks for consequential changes. |

## Key Results

| Result | Number / Observation | Notes |
| --- | --- | --- |
| Full task count | 2,294 task instances | From real Python repositories. |
| Lite task count | 300 instances | Easier/faster iteration subset. |
| BM25 baseline best result | Claude 2 about 1.96% resolved | Establishes difficulty for direct patch generation. |
| Oracle-collapsed improvement | Claude 2 5.93%, GPT-4 3.40% in reported table | Shows value of relevant context compression. |
| Main limitation | Python-only and tests insufficient for full quality | Important when transferring to CursiveOS. |
