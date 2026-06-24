## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Partly Supported — runtime survey from official docs + corpus harness (Ollama); production NL shell **Unvalidated** (not implemented)
**Read with:** [Chapter 05](05-measurement-daemon-and-natural-language-shell.md) (daemon/shell split), [Chapter 18](18-local-agent-arc-b70.md) (workstation tier), [Chapter 00](00-benchmark-schema-and-measurement-validity.md) (inference sensors), [Chapter 06](06-mutation-safety-and-permission-law.md) (agent permissions)

### Authoritative for

- Runtime stack options for CursiveOS NL shell and measurement-side inference sensors
- Hard boundary: no LLM in deterministic measurement path
- Model tier mapping by hardware class

### Superseded or narrowed

- Treating any single backend (Ollama-only) as permanent — backend choice is hardware-scoped
- Using LLM-evaluated benchmark scores as sensor truth

### Open until experiment/hardware

- Arc B70 as default workstation reference (Ch18)
- Concurrent multi-request inference benchmark (Ch00 §3 item 5)
- OpenVINO/SYCL parity matrix on fleet hardware

---


## Reinforced research (2026-06-24)

- **Ollama architecture:** Ollama docs (2025) — local model serving via llama.cpp; current CursiveOS harness interface (Ch00 §1 sustained channel).
- **llama.cpp:** ggml-project (2024–2025) — GGUF quantization, batching, and GPU backend selection for workstation tier (§2).
- **Trust boundary:** Ch05 daemon/shell split — LLM in measurement path invalidates sensor integrity (VALIDATION-supported).
- **Inference validity:** Record `model_id`, `quantization`, `page_cache_state` in detail bundles (Ch00 §3 items 4–5).
- **Workstation tier:** Intel Arc Pro B70 32 GB ECC — Ch18 import; multi-step file reasoning needs containment per Ch06 before unattended use.

# Local LLM Inference Runtime Architecture

Status: First research-synthesis pass (2026-06-24). Surveys 2025–2026 local
inference stacks (Ollama, llama.cpp, OpenVINO, SYCL) and maps them to
CursiveOS's measurement daemon vs natural-language shell split.
Use it for: choosing inference substrates per tier, hardening the measurement
boundary, and aligning cold-start/sustained sensors with recorded model identity.

## Why this chapter exists

Chapter 05 defines a load-bearing split: the **measurement daemon** must remain
deterministic; the **natural-language shell** may be probabilistic. Chapter 00
shows inference sensors already run through **Ollama** but under-record model
quantization and version in structured `runs` columns. The corpus lacked a
runtime architecture chapter explaining *how* local inference is served, which
backends fit which hardware tiers, and what must never cross the daemon boundary.

## 1. Architectural split (non-negotiable)

```text
┌─────────────────────────────┐     ┌──────────────────────────────┐
│ Measurement daemon          │     │ Natural-language shell       │
│ deterministic sensors       │     │ probabilistic UX               │
│ NO LLM in evidence path     │     │ local/remote LLM allowed     │
│ writes /var/lib/cursiveos/  │     │ proposes commands, explains    │
│ submits CursiveRoot         │     │ NEVER writes sensor JSON       │
└─────────────────────────────┘     └──────────────────────────────┘
           │                                      │
           └──────── shared host, separate ───────┘
                    trust boundaries + IPC
```

| Claim | Status |
| --- | --- |
| LLM in measurement path invalidates sensor integrity | **Supported** (Ch05) |
| Shell and daemon may share GPU but not write paths | **Supported** |
| Inference benchmarks may call Ollama API mechanically | **Supported** (Ch00 harness) |

**CursiveOS implication:** benchmark scripts invoke inference **as a workload**,
not as an evaluator. Parsing TTFT/tok/s is deterministic code; the model does not
grade itself.

## 2. Runtime stack map

| Runtime | Core engine | Typical deployment | Hardware focus |
| --- | --- | --- | --- |
| **Ollama** | bundles models, serves OpenAI-compatible HTTP API | user daemon, `ollama run` | cross-vendor; uses llama.cpp/Metal/CUDA/Vulkan backends internally |
| **llama.cpp** | GGUF inference, broad backend plugins | CLI, server mode, embedded | CPU, CUDA, Vulkan, SYCL, OpenVINO, etc. |
| **OpenVINO** | Intel-optimized graph runtime | `openvino_genai`, llama.cpp OV backend | Intel CPU/iGPU/dGPU (Arc, Core Ultra) |
| **SYCL** | Intel/oneAPI path in llama.cpp | `GGML_SYCL=1` builds | Intel GPU offload, data-center Xe |

Official anchors:

- Ollama: [https://github.com/ollama/ollama](https://github.com/ollama/ollama) — model library, Modelfile, API
- llama.cpp backends: `docs/backend/OPENVINO.md`, `docs/backend/SYCL.md` in ggml-org/llama.cpp
- OpenVINO GenAI: [https://github.com/openvinotoolkit/openvino_genai](https://github.com/openvinotoolkit/openvino_genai)
- OpenVINO 2026.x release notes — expanded model coverage, NPU/GPU paths ([OpenVINO releases](https://github.com/openvinotoolkit/openvino/releases))

| Claim | Status |
| --- | --- |
| Ollama is the current CursiveOS harness interface | **Supported** (Ch00) |
| llama.cpp is the underlying inference workhorse for many local stacks | **Supported** |
| OpenVINO/Ollama integration exists for Intel acceleration | **Supported** (OpenVINO blog, 2025) |
| SYCL backend production-ready on all fleet GPUs | **Unvalidated** |

## 3. Daemon vs shell responsibilities

### 3.1 Measurement daemon (inference as sensor workload)

The daemon schedules:

- **Cold-start sensor** — GPU idle → first token (TTFT, load duration)
- **Sustained sensor** — warm steady-state tok/s (single-stream today)

Execution flow:

```text
daemon triggers sensor plugin
-> sensor calls inference endpoint with fixed prompt + model manifest
-> collects TTFT, tok/s, GPU freq class from sysfs phase context
-> emits schema JSON (no LLM post-processing)
-> queue -> CursiveRoot
```

Required manifest fields per sensor run:

| Field | Why |
| --- | --- |
| `model_id` | prevent silent cohort mixing |
| `quantization` | Q4_K_M vs Q8 changes tok/s |
| `ollama_version` / `llama_cpp_commit` | reproducibility |
| `gpu_offload_layers` | attribution |
| `backend` | cuda/vulkan/openvino/sycl/cpu |

| Claim | Status |
| --- | --- |
| Missing model columns corrupts fleet medians | **Supported** (Ch00 §2.3) |
| Phase context (GPU freq, governor) needed for attribution | **Validated** (Ch00 §5) |

### 3.2 Natural-language shell (operator interface)

The shell uses LLMs for:

- intent → command translation
- explaining preset diffs and benchmark results
- multi-step troubleshooting in workstation tier

It must **read** daemon outputs and CursiveRoot summaries; it must not **author**
signed sensor payloads.

| Claim | Status |
| --- | --- |
| Shell prompt injection is standing threat | **Supported** (Ch05, OWASP LLM06) |
| Root/destructive actions need confirmation boundary | **Supported** (Ch06) |

## 4. Model tiers (Chapter 05 aligned)

| Tier | Hardware sketch | Model class | Runtime posture |
| --- | --- | --- | --- |
| Entry | 8–16 GB RAM, modest CPU | 4–8B Q4 | Ollama CPU or small GPU offload |
| Workstation | dGPU 8–16+ GB VRAM (e.g. Arc A750) | 7–14B Q4–Q8; aspirational 20–30B multi-GPU | Ollama default; OpenVINO on Intel; llama.cpp server for fine control |
| Fleet edge | low-power nodes | 3–4B or remote RPC | shell thin-client → workstation inference server |
| Remote (opt-in) | any | frontier API | disclosed, not default |

| Claim | Status |
| --- | --- |
| Entry tier viable for command translation only | **Supported** (industry practice) |
| Workstation tier needed for multi-step file reasoning | **Supported** (Ch05) |
| Arc A750 runs genesis inference sensors today | **Supported** (founder rig) |
| Arc B70 as default workstation card | **Unvalidated** (Ch18) |

**CursiveOS implication:** tier selection is a **hardware-class policy** in hub
manifests, not a global default model.

## 5. Backend selection heuristics

| Hardware signal | Prefer | Avoid without testing |
| --- | --- | --- |
| Intel Arc / iGPU | OpenVINO path or Ollama+OV | assuming CUDA |
| NVIDIA discrete | Ollama CUDA / llama.cpp CUDA | — |
| AMD ROCm | Ollama ROCm builds | treating as NVIDIA |
| CPU-only laptop | small Q4, short context | 30B models |
| Mixed fleet | record `backend` per machine | fleet-wide tok/s pooling |

OpenVINO 2026.x emphasizes GenAI APIs, NPU/GPU coverage, and reduced precision
formats for throughput ([OpenVINO 2026.1 blog](https://medium.com/openvino-toolkit/openvino-2026-1-new-models-more-performance-86251cce7020)).

SYCL backend in llama.cpp targets Intel GPU offload with oneAPI; build complexity
is higher than Ollama prebuilts — acceptable for tuned distribution, not Phase 0.

| Claim | Status |
| --- | --- |
| Backend choice materially affects cold-start and sustained sensors | **Supported** |
| Single backend simplifies fleet statistics | **Supported** as ops tradeoff |
| OpenVINO always beats Vulkan on Arc | **Unvalidated** |

## 6. Serving topology

| Pattern | Use case | CursiveOS fit |
| --- | --- | --- |
| **Embedded daemon** | Ollama as systemd user service | Phase 0 founder rigs |
| **Sidecar server** | llama.cpp `server` on localhost:PORT | shell + sensors share endpoint |
| **Fleet aggregator** | one workstation serves 4–8B to edge nodes | future fleet tier |
| **Remote API** | opt-in cloud | disclosed fallback only |

Isolation requirements:

- separate Unix user or cgroup for shell vs daemon where feasible
- rate limits so shell chat does not starve scheduled sensors
- quiet hours (Ch05) defer non-critical inference

## 7. Measurement validity coupling (Chapter 00)

| Issue | Runtime link | Status |
| --- | --- | --- |
| Page-cache confounds cold-start | model weights re-read from disk vs cache | **Supported** (experiment proposed) |
| Fixed run order | tuned always second | **Supported** |
| Single-stream sustained | scheduler wins need concurrency | **Unvalidated** benchmark |
| Ollama version drift | changes load path | **Unvalidated** logging |

Recommended sensor discipline:

1. Record `page_cache_state` for model blob (Ch00 §3).
2. Counterbalance cold-start order before acceptance-grade claims.
3. Add concurrent-request sustained sensor for workstation class.
4. Pin model manifest hash in sensor plugin version string.

## 8. 2025–2026 serving literature (selected)

| Theme | Implication for CursiveOS |
| --- | --- |
| Speculative decoding / draft models | future shell latency win; not for fitness sensors |
| Continuous batching in server engines (vLLM-class) | fleet aggregator tier; overkill for Phase 0 |
| Quantization-aware kernels (Q4_K, IQ) | record quant in every run |
| NPU offload (Core Ultra, OpenVINO) | new hardware class in fingerprint + tier map |

Local-first serving surveys (2025) consistently recommend **colocated inference**
for privacy-sensitive operator tools — aligns with CursiveOS NL shell default.

| Claim | Status |
| --- | --- |
| Colocated inference fits operator privacy model | **Supported** |
| vLLM-style continuous batching needed at Phase 0 | **Unvalidated** |

## 9. CursiveOS implications

1. **Keep Ollama** for Phase 0 sensors + shell prototyping; abstract via OpenAI-compatible local URL.
2. **Add structured model identity** to `runs` / detail bundles immediately (Ch00 §3 item 4).
3. **Intel fleet** — benchmark OpenVINO backend vs default Ollama on Arc hardware before prescribing.
4. **Never** route sensor JSON through an LLM summarizer before CursiveRoot upload.
5. **Schedule** sensor inference jobs with higher priority than shell chat on shared GPU.
6. **Version** sensor plugins when model or backend changes — treat as new sensor revision.

## 10. Open research gaps

1. OpenVINO vs Ollama-default cold-start on Arc A750 and B70.
2. Concurrent sustained tok/s benchmark (multi-client) for scheduler presets.
3. NPU-present Core Ultra fingerprint subclass + tier policy.
4. llama.cpp `server` vs Ollama for reproducible CI-style sensor pinning.
5. Remote tier abuse model (credential handling, disclosure UX).
6. GPU memory fragmentation when shell and sensors alternate loads.

## 11. Citations

| Source | Use |
| --- | --- |
| Chapter 05 | daemon/shell split, tiers, permissions |
| Chapter 00 | Ollama sensors, validity gaps |
| Ollama project docs | deployment, API, Modelfile |
| llama.cpp backend docs | OpenVINO, SYCL, build flags |
| OpenVINO GenAI / 2026.1 notes | Intel acceleration path |
| OWASP Top 10 for LLM Apps 2025 | excessive agency, injection |

## Research questions answered

| Question | Answer |
| --- | --- |
| May the NL shell use an LLM? | Yes — with permission law (Ch06) |
| May the measurement daemon? | No — deterministic plugins only |
| What runs today? | Ollama-mediated inference sensors on founder hardware |
| What must be logged? | model, quant, backend, offload, runtime version |