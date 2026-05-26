# Validation Note: Chapter 09 Local Agent Setup for Arc B70

Date checked: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: targeted validation of highest-risk Chapter 09 claims
Status: partially supported; several benchmark/model/tool-calling claims require local reproduction
Source IDs: SRC-09-001 through SRC-09-009

## Summary

Chapter 09 is valuable and directly relevant to the CursiveOS local-agent/home-rack roadmap, but it is not yet decision-grade. The broad software architecture is supported: Intel Arc local inference requires non-CUDA backends such as llama.cpp SYCL, Vulkan, OpenVINO, oneAPI, Level Zero, or IPEX-LLM. The llama.cpp SYCL documentation supports Intel GPU / Arc-family backend claims, and llama.cpp function-calling docs support the use of `llama-server --jinja` for OpenAI-style tool/function calling.

However, several of the chapter's most specific claims depend on community benchmarks, Reddit/Medium reports, or unverified model-specific behavior. Those should be treated as hypotheses until reproduced on the actual CursiveOS B70 hardware.

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-09-001 | Intel Arc local AI deployment cannot rely on CUDA-only software paths and should prioritize Intel-compatible runtimes such as SYCL/oneAPI, Level Zero, Vulkan, and OpenVINO. | supported | SRC-09-003, SRC-09-005 | This is architecturally sound. Keep. |
| CL-09-002 | llama.cpp has a SYCL backend for Intel GPUs and documents build/install commands using oneAPI/Intel tooling. | supported | SRC-09-003 | The official llama.cpp docs verify SYCL backend support for Intel GPUs. |
| CL-09-003 | llama.cpp SYCL docs directly validate Arc Pro B70-specific throughput. | disputed / unsupported as written | SRC-09-003 | Official docs support Intel Arc family and list B580 support, but do not validate B70-specific benchmark claims. B70 throughput must come from reproducible benchmarks. |
| CL-09-004 | `llama-server --jinja` supports OpenAI-compatible function calling. | supported | SRC-09-004 | Official function-calling docs validate general support. |
| CL-09-005 | The chapter's Qwen 3.5/3.6 parser guidance (`qwen3_xml`, `qwen3_coder`, `preserve_thinking`, enhanced Jinja incompatibility) is verified. | unverified | SRC-09-004 plus community sources not yet normalized | Needs direct validation against llama.cpp/vLLM docs, Qwen templates, and local tests. Keep as field report/hypothesis until reproduced. |
| CL-09-006 | OpenVINO 2025.3 includes relevant LLM features such as GGUF preview support, XGrammar/tool-guided generation, Qwen3 support, and KV/key-cache compression work. | supported | SRC-09-005 | Intel release notes support these feature areas for OpenVINO 2025.3. |
| CL-09-007 | Arc Pro B70 has 32GB GDDR6, 256-bit bus, 608 GB/s bandwidth, 32 Xe2 cores, 256 XMX engines, and 367 INT8 TOPS. | partially supported | SRC-09-001, SRC-09-002, SRC-09-008, SRC-09-009 | Multiple technical/reporting sources agree, but primary Intel product documentation was not located in this pass. Mark as partially supported until official Intel/product documentation is added. |
| CL-09-008 | Arc Pro B70 has ECC support. | partially supported | SRC-09-001, SRC-09-008, SRC-09-009 | Supported by reporting/spec sources; still needs primary Intel or board-vendor doc. |
| CL-09-009 | Qwen 3.5/3.6 MoE models deliver the listed token/sec and power results on Arc Pro B70. | unverified | SRC-09-007 | Depends on the benchmark repository and/or local tests. Must verify methodology, commit, driver, llama.cpp version, command line, power measurement method, and model file hashes. |
| CL-09-010 | MoE models are categorically preferable for local agents on B70. | partially supported / requires narrowing | SRC-09-007, SRC-09-006 | MoE speed/VRAM logic is plausible, but tool reliability and quality must be evaluated. Rewrite as a hypothesis or workload-specific recommendation, not a universal conclusion. |
| CL-09-011 | 16k context can reduce decode performance by 30-40% due to KV-cache scaling. | unverified | No primary source validated in this pass | Plausible general inference behavior, but needs local benchmark across context lengths. |
| CL-09-012 | Hermes Agent / OpenClaw / Bifrost / Clanker Cloud stack is stable enough for CursiveOS local-agent deployment. | unverified | Chapter sources include project/community docs but not validated | Treat as ecosystem lead only. Validate repos, licenses, maintenance status, security model, and API compatibility before adopting. |

## Required Corpus Changes

### Wording changes recommended for Chapter 09

1. Replace hard claims like `SYCL is 2.2x faster than Vulkan` with `one cited B70 benchmark repository reports a 2.2x decode advantage for SYCL in a specific test; this requires reproduction on target hardware`.
2. Replace `Qwen 3.5-35B-A3B should be deployed` with `Qwen 3.5-35B-A3B is a strong candidate for evaluation`.
3. Mark Qwen parser/template guidance as `field report / needs local test` until verified against actual server behavior.
4. Mark B70 raw specifications as `partially supported pending Intel primary source`.
5. Separate `supported stack architecture` from `unverified performance table`.

## Implications for CursiveOS

- Chapter 09 should remain in the P0 validation queue because it affects hardware and local-agent architecture decisions.
- The immediate engineering experiment should be a reproducible B70 benchmark matrix: llama.cpp SYCL vs Vulkan, Qwen dense vs MoE, 8k/16k/32k context, tool-call reliability, and power draw.
- The corpus should not use Chapter 09 performance numbers as design baselines until they are reproduced internally or validated from a well-documented benchmark repo.

## Suggested Benchmark Matrix

| Dimension | Values |
| --- | --- |
| Backend | llama.cpp SYCL, llama.cpp Vulkan, OpenVINO GenAI/OVMS |
| Model | Llama 3.1 8B Q4, Qwen dense 27B Q4, Qwen MoE 35B-A3B Q4, Hermes 3 8B Q4 |
| Context | 8k, 16k, 32k |
| Metrics | prefill tok/s, decode tok/s, time-to-first-token, tool-call success rate, JSON validity, power draw, VRAM usage, crash/deadlock rate |
| Environment | kernel version, Mesa version, Level Zero version, oneAPI version, llama.cpp commit, model hash, driver version |

## Follow-up

- Add all 39 works-cited items to `sources/extracted-source-index.md`, but classify Reddit/Medium/forum sources as Tier C/D unless independently corroborated.
- Inspect `PMZFX/intel-arc-pro-b70-benchmarks` in detail and extract exact test methodology.
- Locate official Intel Arc Pro B70 product documentation or board-vendor data sheet.
- Create `experiments/arc-b70-local-agent-benchmark-plan.md` before using this chapter for implementation choices.
