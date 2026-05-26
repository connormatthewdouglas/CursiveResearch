<!--
Imported from uploaded DOCX source; wording, structure, and tables are retained in summarized Markdown form.
Source file: Local Agent Setup for Arc B70.docx
Source SHA-256: 54cde0c3dd1faf51e142b5d76d25aaedf475775995af9f6f76826117006382c5
Imported: 2026-05-26
-->

# Local Agent Setup for Arc B70

Status: Source import from uploaded DOCX. Requires source extraction and validation before being used for engineering decisions.

Validation plan: see `experiments/arc-b70-local-agent-benchmark-plan.md`. Chapter 09 performance, backend, model-selection, long-context, and tool-calling claims should not be treated as decision-grade until reproduced through that plan.

## Source Import

## Engineering Local Agent Workloads on the Intel Arc Pro B70: Hardware Architecture, Model Selection, and Software Co-Design

The source document analyzes the Intel Arc Pro B70 as a local AI and autonomous-agent workstation card. It frames the B70 as a bridge between consumer GPUs and enterprise AI accelerators, emphasizing its 32 GB GDDR6 memory pool, ECC support, Intel Battlemage architecture, Level Zero / oneAPI software stack, and usefulness for local agent orchestration.

The document claims the Arc Pro B70 is built on TSMC 5 nm using the BMG-G31 Xe2-HPG Battlemage GPU, with 32 Xe-cores, 4,096 shading units, 256 XMX AI engines, 608 GB/s bandwidth, 22.94 TFLOPS FP32, and up to 367 TOPS INT8 matrix throughput. These hardware claims must be validated against Intel, vendor, and independent benchmark sources before being used as decision-grade facts.

| Architectural Feature | Intel Arc Pro B70 Specification |
| --- | --- |
| Graphics Processor / Die Area | BMG-G31 (Xe2-HPG Battlemage) / 368 mm² |
| Process Node | TSMC 5 nm |
| Memory Capacity & Type | 32 GB GDDR6 with ECC Support |
| Memory Bus Width & Bandwidth | 256-bit / 608.0 GB/s |
| Compute Units & Engines | 32 Xe-Cores / 256 Intel XMX Engines |
| Peak AI Performance | 367 pTOPS (INT8 Matrix Math) |
| FP32 Performance | 22.94 TFLOPS |
| Base / Boost GPU Core Clock | 2280 MHz / 2800 MHz |
| Bus Interface & Power TDP | PCI-Express 5.0 x16 / 230 W to 290 W |
| Launch Pricing | 949 USD |

## The Local Software Stack: Backend Platform Choices

The source emphasizes that Intel Arc local AI deployment cannot rely on CUDA-only tooling. It states that common CUDA-first stacks such as vLLM GPU kernels, TensorRT-LLM, bitsandbytes INT4/INT8, and FlashAttention-2 do not run natively on the B70. Instead, local-agent deployment must use Intel-compatible runtimes such as llama.cpp SYCL, llama.cpp Vulkan, OpenVINO GenAI, OpenVINO Model Server, oneAPI, Level Zero, and related Intel runtimes.

Three backend options are presented:

- **Llama.cpp with SYCL:** uses Intel compilers and SYCL to target Intel Level Zero paths, offloading GGUF models to GPU execution units and XMX engines.
- **Llama.cpp with Vulkan:** uses Vulkan compute paths and Mesa developer drivers; easier to deploy than oneAPI but may differ in prefill/decode behavior.
- **OpenVINO GenAI / OVMS:** Intel's inference framework for converting PyTorch/Safetensors models into OpenVINO IR, with reported support for GGUF parsing, structured output constraints, XGrammar, and KV-cache optimizations in recent releases.

The document argues that Vulkan and SYCL involve a trade-off: Vulkan is easier to deploy and can have strong prompt-prefill throughput, while SYCL may be superior for decode generation due to Intel-specific MMVQ and reorder paths. It cites an `intel-arc-pro-b70-benchmarks` repository as evidence for a claimed 2.2x SYCL decode advantage in a Qwen 1.5B Q4_K_M test.

| Backend Platform | Compilation Requirements | Key Advantages | Performance Characteristics |
| --- | --- | --- | --- |
| SYCL / oneAPI | oneAPI Base Toolkit, icx / icpx compilers | Native Intel integration; optimized MMVQ and reorder paths | 2.2x faster decode generation vs Vulkan; ideal for low-latency chat |
| Vulkan | Vulkan SDK, Mesa developer drivers (Linux) | Fast deployment; does not require heavy oneAPI stack | Excellent prompt prefill; superior raw throughput under specific Windows drivers |
| OpenVINO GenAI | OpenVINO toolkit, Hugging Face model converter | XGrammar structured JSON constraint; per-channel KV cache compression | High-throughput native execution; unified scaling across CPU/GPU/NPU |

The source further claims that precompiled llama.cpp SYCL builds may ship with assertions enabled, suppressing prompt prefill speeds by up to 50%, and recommends compiling from source with explicit release flags:

```bash
cmake -B build -DGGML_SYCL=ON -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx -DCMAKE_CXX_FLAGS_RELEASE="-O3 -DNDEBUG"
```

## Model Selection for Agentic Operations: The MoE Sweet Spot

The source argues that agentic workloads require more than raw chat quality: they need reliable instruction following, multi-turn structured output, tool-call correctness, and resistance to loop states. It states that small dense models in the 3B–8B range can fail in complex agentic loops by hallucinating parameters, emitting malformed JSON, misusing tools, or looping.

The central model-selection claim is that Mixture-of-Experts models can deliver higher reasoning class at lower active-parameter cost. The document specifically emphasizes Qwen 3.5-35B-A3B and Qwen 3.6-35B-A3B style models as 35B-total / 3B-active architectures, claiming decode speeds around 54.5–54.7 tokens/sec on Arc Pro B70-class hardware. This must be validated against the named benchmark repository and independently reproduced on CursiveOS hardware.

| Model Name & Architecture | Parameter Class | Quantization Format | Static Model Size | Prefill Speed (pp512) | Decode Speed (tg128) | Operational Power |
| --- | --- | --- | --- | --- | --- | --- |
| Llama 3.1-8B (Dense) | 8 Billion | Q4_K_M | 4.6 GiB | 2,452 t/s | 82.6 t/s | 37 W |
| Qwen 3.5-9B (Dense) | 9 Billion | Q4_K_M | 5.3 GiB | 2,302 t/s | 60.2 t/s | 168 W |
| Qwen 3.5-35B-A3B (MoE) | 35 Billion (3B Active) | Q4_K_M | 20.5 GiB | 618 t/s | 54.5 t/s | 92 W |
| Qwen 3.6-35B-A3B (MoE) | 35 Billion (3B Active) | UD-Q4_K_M | 20.6 GiB | 615 t/s | 54.7 t/s | 114 W |
| Gemma 4 26B-A4B (MoE) | 26 Billion (4B Active) | Q4_K_M | 15.7 GiB | 1,129 t/s | 52.6 t/s | 102 W |
| Phi-4 14B (Dense) | 14 Billion | Q4_K_M | 8.4 GiB | 1,424 t/s | 43.7 t/s | 40 W |
| Qwen 3.5-27B (Dense) | 27 Billion | Q4_K_M | 15.6 GiB | 718 t/s | 20.4 t/s | 178 W |

The document concludes that MoE models can deliver better tokens-per-joule than equivalent dense models, while noting a behavioral trade-off: Qwen 3.6 MoE models allegedly show more tendency toward reasoning loops or malformed tool calls than Qwen 3.5 27B dense. The source recommends Qwen 3.5-35B-A3B for speed/intelligence balance and Qwen 3.5-27B dense where obedience and clean structured output matter more than speed.

## Tool-Calling Engineering: Resolving CoT Leakage and Parser Issues

The source identifies tool-call reliability as a key deployment problem for local agents. It describes "CoT leakage" as a failure mode where models output reasoning inside `<thinking>` blocks but fail to close `</thinking>` before emitting a structured `<tool_call>`, breaking regex/XML/JSON parsers.

The proposed mitigation is a custom interleaved-thinking template such as `qwen3.5-enhanced.jinja`, designed to tolerate unclosed thinking blocks and preserve downstream tool-call detection.

Key engineering claims:

- **Parser engine choice:** Qwen 3.5 may work better with `qwen3_xml`, while Qwen 3.6 may require a more permissive `qwen3_coder` parser when strict XML parsing fails on incomplete structures.
- **Thinking preservation:** Qwen 3.6 has a native `preserve_thinking` configuration. The document says custom `qwen3.5-enhanced.jinja` is incompatible with native `preserve_thinking=true`; when using the custom template, force `preserve_thinking=false`. Without a custom template, use official template plus `preserve_thinking=true` to stabilize tool calls via prefix caching.
- **Output limits:** Large tool payloads can exceed local model output limits. Raising maximum output token parameter is a mandatory client-side configuration to prevent argument truncation in complex environments.

These claims are high-value for local-agent engineering but need validation against llama.cpp, vLLM, Qwen templates, and actual local test runs.

## Context Window Architecture and VRAM Budgeting

The source explains that local agent VRAM usage comes from static model weights plus dynamic KV cache. It describes KV-cache memory as dependent on attention layers, heads, head dimension, sequence length, and batch size.

The document gives example memory estimates for 32 GB Arc Pro B70 operation:

| Model Name & Format | VRAM Allocation (Weights) | Context Target | KV Cache Memory | Total VRAM Footprint | Remaining VRAM Headroom |
| --- | --- | --- | --- | --- | --- |
| Qwen 3.5-27B (Q4_K_M) | 15.6 GiB | 8,000 Tokens | ~2.5 GiB | 18.1 GiB | 13.9 GiB |
| Qwen 3.5-27B (Q4_K_M) | 15.6 GiB | 16,000 Tokens | ~5.0 GiB | 20.6 GiB | 11.4 GiB |
| Qwen 3.5-27B (Q4_K_M) | 15.6 GiB | 32,000 Tokens | ~10.0 GiB | 25.6 GiB | 6.4 GiB |
| Qwen 3.6-35B (Q4_K_M) | 20.6 GiB | 8,000 Tokens | ~3.0 GiB | 23.6 GiB | 8.4 GiB |
| Qwen 3.6-35B (Q4_K_M) | 20.6 GiB | 16,000 Tokens | ~6.0 GiB | 26.6 GiB | 5.4 GiB |
| Llama 3.1-8B (FP16) | 16.0 GiB | 16,000 Tokens | ~4.0 GiB | 20.0 GiB | 12.0 GiB |
| Llama 3.1-8B (Q4_K_M) | 4.6 GiB | 16,000 Tokens | ~1.0 GiB | 5.6 GiB | 26.4 GiB |

The source recommends limiting real-time personal agent assistants to around 8,000 operational tokens for responsiveness, even where larger contexts are technically possible. It claims 16,000-token contexts can reduce decode performance by roughly 30% to 40% because KV-cache reads expand with context length.

## Deploying the Hermes Agent Framework Locally

The source describes Hermes Agent, attributed to Nous Research, as an autonomous, self-improving agent with persistent memory and an internal-monologue → tool-call → observation → reflection loop. It claims Hermes can operate across multiple messaging platforms and generate reusable skills.

The document recommends running local execution in hardened containers with read-only roots, dropped capabilities, PID limits, and restricted system calls, especially for shell/code execution.

It further describes an architecture where OpenClaw or Bifrost AI Gateway acts as local orchestration middleware, connecting a local Ollama or llama-server model endpoint to external protocols such as MCP servers. It gives `http://127.0.0.1:11434` as the local endpoint shape and describes mapping tools such as `clanker_route_question` and `clanker_run_command` into the agent context.

These claims are especially important to validate because some Hermes/OpenClaw/Bifrost/Clanker references may be project-specific, community-level, or unstable.

## Architectural Conclusions and Implementation Roadmap

The document proposes this local Arc Pro B70 agent setup path:

1. **Hardware preparation and driver verification:** install latest Intel discrete GPU stack and the oneAPI Base Toolkit on a host operating system such as Ubuntu 22.04 with Linux kernel 6.5. Ensure that the graphics card is recognized and the execution units are mapped within the Level Zero system runtime.
2. **Runtime compilation:** build llama.cpp with SYCL and Intel compiler toolchain, using `-O3 -DNDEBUG` to strip assertions.
3. **Model selection:** download the Qwen 3.5 35B-A3B Mixture-of-Experts model in Q4_K_M GGUF format as a balance of intelligence and execution speed.
4. **API hosting:** launch `llama-server` with native Jinja processing and a 16,000-token context window.
5. **Hermes orchestration:** point `~/hermes/config.yaml` at the local OpenAI-compatible llama.cpp endpoint.
6. **Execution containment:** run execution tools in hardened Docker containers to isolate shell, compiler, and code-patching actions from the host.

Example server command from the source:

```bash
./build/bin/llama-server -m models/qwen3.5-35b-a3b-q4_k_m.gguf -c 16384 -ngl 99 --jinja --host 127.0.0.1 --port 11434
```

## Works cited

1. Intel Arc Pro B70 Specs | TechPowerUp GPU Database — https://www.techpowerup.com/gpu-specs/arc-pro-b70.c4388
2. Intel Arc Pro B70 Single-Fan AI & Workstation Graphics Card — Micro Center — https://www.microcenter.com/product/709007/intel-arc-pro-b70-single-fan-ai-workstation-graphics-card
3. Intel Arc Pro B70 Graphics Card — B&H Photo — https://www.bhphotovideo.com/c/product/1959142-REG/intel_33p01ib0bb_arc_pro_b70_32gb.html
4. Intel Arc Pro B70 Review — Puget Systems — https://www.pugetsystems.com/labs/articles/intel-arc-pro-b70-review/
5. LLM Inference on Intel Arc Pro B60: IPEX-LLM and LlamaCPP SYCL — https://gigagpu.com/intel-arc-pro-b60-llm-inference/
6. Arc Pro B70 Review: The best graphics card Intel has to offer — Reddit — https://www.reddit.com/r/hardware/comments/1tax6jn/arc_pro_b70_review_the_best_graphics_card_intel/
7. llama.cpp for SYCL — GitHub — https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/SYCL.md
8. AUR: llama.cpp-sycl — Arch Linux — https://aur.archlinux.org/packages/llama.cpp-sycl
9. I made an AUR package llama.cpp-sycl to use the Intel B70 — Reddit — https://www.reddit.com/r/IntelArc/comments/1tlcvbi/i_made_an_aur_package_llamacppsycl_to_use_the/
10. How to Run Qwen3.6–27B Locally on Intel Arc Pro B70 — Medium — https://bibek-poudel.medium.com/how-to-run-qwen3-6-27b-locally-on-intel-arc-pro-b70-what-actually-works-c96dec67c6f7
11. OpenVINO Model Hub — Intel — https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/models.html
12. Unified interface to run local LLMs on Intel Arc hardware acceleration using OpenVINO — Reddit — https://www.reddit.com/r/IntelArc/comments/1r4jy0y/unified_interface_to_run_local_llms_on_intel_arc/
13. Release Notes for Intel Distribution of OpenVINO Toolkit 2025.3 — Intel — https://www.intel.com/content/www/us/en/developer/articles/release-notes/openvino/2025-3.html
14. OpenVINO Model Server + GPT-OSS 20B and Intel Arc A770 — Reddit — https://www.reddit.com/r/IntelArc/comments/1sfme8u/openvino_model_server_gptoss_20b_and_intel_arc/
15. Intel Arc Pro B70 Benchmarks & Performance Data — GitHub — https://github.com/PMZFX/intel-arc-pro-b70-benchmarks
16. Building Agentic Multi-Agent System with AutoGen and Ollama — Medium — https://medium.com/executeautomation/building-agentic-multi-agent-system-with-autogen-and-ollama-472bab920150
17. Breaking the Chains of Walled-Garden AI: Why I Built with Hermes Agent — DEV Community — https://dev.to/moni121189/breaking-the-chains-of-walled-garden-ai-why-i-built-with-hermes-agent-and-how-to-run-it-globally-3nn0
18. CrewAI agent framework with local models — Reddit — https://www.reddit.com/r/LocalLLaMA/comments/18v527r/crewai_agent_framework_with_local_models/
19. Local tool calling agents using LangChain and Ollama are inexplicably poorly performing — Reddit — https://www.reddit.com/r/LocalLLaMA/comments/1hbx96u/local_tool_calling_agents_using_langchain_and/
20. NousResearch/DeepHermes-3-Llama-3-8B-Preview-GGUF — Hugging Face — https://huggingface.co/NousResearch/DeepHermes-3-Llama-3-8B-Preview-GGUF
21. How to Build a Self-Hosted AI Agent (2026 Stack Guide) — Petronella Technology Group — https://petronellatech.com/blog/hermes-agent-ai-guide/
22. Qwen3.6-35B-A3B: Agentic Coding Power, Now Open to All — Qwen — https://qwen.ai/blog?id=qwen3.6-35b-a3b
23. Qwen 3.6-35B-A3B: Reddit Asked, So I Tested If the 3.5 Tool Calling Fixes Carry Over — Reddit — https://www.reddit.com/r/LocalLLM/comments/1sqpsut/qwen_3635ba3b_reddit_asked_so_i_tested_if_the_35/
24. Qwen 3.5 Tool Calling Fixes for Agentic Use — Reddit — https://www.reddit.com/r/LocalLLaMA/comments/1sdhvc5/qwen_35_tool_calling_fixes_for_agentic_use_whats/
25. Tested tool calling fixes for Qwen 3.6‑27B‑FP8 — Reddit — https://www.reddit.com/r/LocalLLM/comments/1sv6cqk/follow_up_tested_tool_calling_fixes_for_qwen/
26. Recommendations for running custom tools with local Ollama models — CrewAI Community — https://community.crewai.com/t/recommendations-for-running-custom-tools-with-local-ollama-models-having-function-calling-capabilities/5777
27. Qwen3.5 Tool Calling finally fixed — NVIDIA Developer Forums — https://forums.developer.nvidia.com/t/qwen3-5-tool-calling-finally-fixed-possibly/366451
28. Introducing Tool Eval Bench CLI — NVIDIA Developer Forums — https://forums.developer.nvidia.com/t/introducing-tool-eval-bench-cli/366903/82
29. Qwen 3/3.5/3.6 tool calling is broken — Reddit — https://www.reddit.com/r/Vllm/comments/1suasv2/qwen_33536_tool_calling_is_broken_even_worse_with/
30. The Complete Guide to Hermes Agent — Kimi — https://www.kimi.com/resources/hermes-agent
31. Hermes Agent Documentation — https://hermes-agent.nousresearch.com/docs/
32. Hermes Agent — Open-Source AI Agent with Persistent Memory — https://hermes-agent.org/
33. AI-Ecosystem: BiFrost, OpenClaw, Hermes3 — Medium — https://medium.com/@ion.stefanache0/bifrost-ai-gw-openclaw-orchestrator-and-hermes-3-gguf-format-worhing-togeter-on-ollama-rtx-4060-333b85a5d15f
34. Using Hermes Agent to Manage Your Infrastructure with Clanker Cloud — https://clankercloud.ai/blog/hermes-agent-clanker-cloud-infrastructure-management
35. NousResearch/Hermes-3-Llama-3.1-8B-GGUF — Hugging Face — https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
36. Hermes Agent: The Self-Improving AI That Grows With You — https://atalupadhyay.wordpress.com/2026/04/07/hermes-agent-the-self-improving-ai-that-grows-with-you/
37. Install IPEX-LLM on Linux with Intel GPU — GitHub — https://github.com/intel/ipex-llm/blob/main/docs/mddocs/Quickstart/install_linux_gpu.md
38. IPEX-LLM on Intel GPU — LlamaIndex Developer Documentation — https://developers.llamaindex.ai/python/framework/integrations/llm/ipex_llm_gpu/
39. llama.cpp function calling docs — GitHub — https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md

## Initial Validation Notes

This chapter is high-value for the CursiveOS home-rack/local-agent roadmap but should be treated as unverified until checked against primary sources and reproduced on target hardware. Several sources are low-confidence community sources such as Reddit, Medium, and third-party guides. Validation should prioritize Intel, llama.cpp, OpenVINO, Qwen, Hugging Face, and reproducible benchmark repositories first.
