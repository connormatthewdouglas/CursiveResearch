# Research Index

This index is the primary navigation page for the private CursiveOS research
corpus. The initial chapter set is a faithful Markdown conversion of uploaded
source documents, organized by subject rather than by file-upload order.

## Reading Path

| Chapter | Topic | Use It For | Status |
| --- | --- | --- | --- |
| [00 - Research Master](chapters/00-research-master.md) | Collected snapshot and repo observations | Orientation and historical context | Imported; requires current verification |
| [01 - First Principles and Strategy](chapters/01-first-principles-and-strategy.md) | Foundational thesis, moat, roadmap implications | Product and strategic framing | Imported; requires review |
| [02 - Market and Viability](chapters/02-market-and-viability.md) | Crypto/decentralized compute market, system thesis, positioning | Viability analysis and competitive context | Imported; requires verification |
| [03 - Linux Kernel Optimization](chapters/03-linux-kernel-optimization.md) | Kernel changes and system tuning | Technical opportunity discovery | Imported; requires benchmark validation |
| [04 - GPU and Accelerator Tuning](chapters/04-gpu-and-accelerator-tuning.md) | AMD/Intel GPU behavior and tuning | Hardware-specific experiments | Imported; requires hardware validation |
| [05 - AI-Guided Tuning](chapters/05-ai-guided-tuning.md) | Automated tuning and agent approaches | Architecture and research backlog | Imported; requires paper/source review |
| [06 - Security and Hardening](chapters/06-security-and-hardening.md) | Linux security and operational defense | Threat model and deployment hardening | Imported; requires security review |
| [07 - Tokenomics and Incentives](chapters/07-tokenomics-and-incentives.md) | DePIN models and incentive mechanisms | Economic design research | Imported; requires economics review |

## How Content Is Classified

| Class | Meaning | Location |
| --- | --- | --- |
| Source master | An unmodified document received from a contributor. | `sources/original-docx/` |
| Imported chapter | A readable conversion that retains the source wording. | `chapters/` |
| Verified finding | A claim checked against primary/current sources and dated. | Add within a chapter under a clearly labeled verification section. |
| Decision note | A project recommendation linked back to findings and evidence. | Future `decisions/` entries under the methodology. |

## Important Boundary

These chapters preserve submitted research; inclusion does not mean every claim
has been verified. Many statements are date-sensitive or predictive. Future
updates should retain the imported record and append dated verification,
correction, or supersession notes rather than quietly rewriting history.
