# OSWorld — Claims and Results

## Decision-Relevant Claims

| Claim | Status In Corpus | Evidence | CursiveOS Use |
| --- | --- | --- | --- |
| Real desktop/OS tasks remain hard for current agents. | Supported | Human performance about 72.36%; best reported model about 12.24% in paper table | Do not assume a shell agent is ready for unattended OS control. |
| Execution-based VM evaluation is a strong pattern for OS agents. | Supported | OSWorld task setup, VM state, and 134 evaluation functions | Use VM snapshots and post-checks for Cursive shell testing. |
| GUI grounding and operational knowledge are bottlenecks. | Supported | Low screenshot/hybrid performance and qualitative analysis | Keep conventional terminal fallback and CLI-first safe paths. |
| Workflow tasks are harder than single-app tasks. | Supported | Category analysis shows weak agent performance on workflow tasks | Treat cross-app shell workflows as higher risk. |

## Key Results

| Result | Number / Observation | Notes |
| --- | --- | --- |
| Ubuntu tasks | 369 | Main benchmark suite. |
| Windows analytic tasks | 43 | Require activation/copyright handling. |
| Initial states | 302 | Supports midstream task starts. |
| Evaluation functions | 134 unique functions | Shows execution-based desktop evaluation cost. |
| Human performance | 72.36% overall | CS-student annotators unfamiliar with tasks/software. |
| Best model in table | 12.24% overall | GPT-4 with accessibility tree input in reported table. |
| Workflow tasks | 101 tasks / 27.4% | Important for Cursive shell realism. |
