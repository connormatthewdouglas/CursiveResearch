# Adversarial Review — Chapter 02 TDX "hardened against physical bus-level attacks"

Date: 2026-06-20
Reviewer role: Red-team / adversarial review
Disposition: **Challenge filed. Original chapter wording NOT edited.** Flagged in
`VALIDATION.md` → "Flagged for Review".

## The challenged claim

`chapters/02-market-and-viability.md`, section *Security, Attestation, and the
DePIN "Oracle Problem"* → *Transitioning from SGX to Intel TDX*:

> "For several years, Intel SGX … was the standard … However, research into the
> 'WireTap' vulnerability has demonstrated that an attacker with physical access
> to a DDR4 platform can extract SGX attestation signing keys via DRAM bus
> interposition. … In response, TAO-OS facilitates a strategic migration toward
> Intel TDX (Trust Domain Extensions) and NVIDIA Confidential Computing (CC).
> **TDX, built for the DDR5 era, is hardened against physical bus-level
> attacks** …"

and the attestation table:

| Attestation Feature | SGX (Legacy) | TDX (Next-Gen) | TAO-OS Implementation |
| --- | --- | --- | --- |
| Bus Attack Resistance | Vulnerable (WireTap) | **Hardened (DDR5)** | Hardware-Rooted |

## Why this is the most consequential weak claim in the corpus

1. **It is a security/architecture decision-driver, not a marketing aside.** The
   chapter frames hardware attestation as the answer to the DePIN "oracle
   problem" — proving off-chain work on operator-controlled hardware is genuine.
   The claim directly recommends a concrete migration (SGX → TDX + NVIDIA CC)
   and labels the target's bus-attack resistance "Hardened." Per the corpus's
   own criteria (`CORPUS_WORKFLOW.md`, `VALIDATION.md`), security claims that
   shape implementation are exactly what must be validated.
2. **The threat model is the project's own.** A DePIN node operator owns the
   physical machine and is *financially incentivized* to forge attestation or
   "game performance benchmarks" — the chapter says so itself. That is a
   physical-access DRAM-bus adversary, the precise model the claim says TDX
   defeats.
3. **The claimed property is the load-bearing one.** The whole "WireTap broke
   SGX → move to TDX" argument collapses if the successor is breakable on the
   same bus.

## External evidence that contradicts it

### TEE.Fail (October 2025) — direct contradiction, DDR5, defeats TDX *and* NVIDIA CC
Researchers at Georgia Tech and Purdue disclosed **TEE.Fail**, a practical
**DDR5** memory-bus interposer attack that extracts cryptographic keys and
**forges remote attestation against Intel SGX, Intel TDX, AND AMD SEV-SNP**,
with reporting that it also reaches **NVIDIA confidential computing**. This is
the same class of physical bus interposition as WireTap, but on DDR5 — directly
falsifying "TDX, built for the DDR5 era, is hardened against physical bus-level
attacks" and the table's "Bus Attack Resistance: Hardened (DDR5)". It also
undercuts the *second* recommended successor (NVIDIA CC) in the same chapter.
- The Hacker News, "New TEE.Fail Side-Channel Attack Extracts Secrets from Intel
  and AMD DDR5 Secure Enclaves" (2025-10):
  https://thehackernews.com/2025/10/new-teefail-side-channel-attack.html
- BleepingComputer, "TEE.Fail attack breaks confidential computing on Intel,
  AMD, NVIDIA CPUs":
  https://www.bleepingcomputer.com/news/security/teefail-attack-breaks-confidential-computing-on-intel-amd-nvidia-cpus/
- CyberSecureFox, "TEE.Fail: Practical DDR5 Memory-Bus Attack Breaks Attestation
  In Intel SGX/TDX And AMD SEV-SNP":
  https://cybersecurefox.com/en/tee-fail-ddr5-attack-intel-sgx-tdx-amd-sev-snp/

### Battering RAM (2025) — the DDR5 extension is anticipated, and TDX's only defense is non-default
**Battering RAM** (academic interposer work; durham-repository / batteringram.eu)
breaks Intel SGX and AMD SEV-SNP with a **~$50** DDR4 interposer via dynamic
memory aliasing. The authors note they could not test TDX *only because their
interposer was DDR4-limited*, and state they believe **a more advanced
interposer can attack DDR5**. Intel's response is that TDX **integrity mode**
mitigates the underlying flaw — but cryptographic memory integrity is not the
default posture for TDX on common configurations, so "hardened" overstates the
out-of-the-box guarantee.
- SecurityWeek, "Battering RAM Attack Breaks Intel and AMD Security Tech With
  $50 Device":
  https://www.securityweek.com/battering-ram-attack-breaks-intel-and-amd-security-tech-with-50-device/
- Battering RAM project page: https://batteringram.eu/
- Keysight, "Security Highlight: DRAM Interposer Attacks on Confidential
  Computing":
  https://www.keysight.com/blogs/en/tech/nwvs/2025/10/22/security-highlight-dram-interposer-attacks-on-confidential-computing

### Vendor threat model — physical access is explicitly out of scope
Intel and AMD have stated that interposer/physical-access attacks are **not in
their threat model** because they require physical access to the device. That is
the correct, honest framing — and it is the opposite of "hardened against
physical bus-level attacks." For a cloud TEE the assumption (no physical access)
is reasonable; for a **DePIN substrate where the adversary owns the box, it is
not.**

## Net assessment

- The corpus correctly identifies that WireTap broke DDR4 SGX.
- It then **overstates** the fix: DDR5-era TDX (and NVIDIA CC) are **not**
  hardened against physical DRAM-bus attacks. TEE.Fail demonstrates exactly such
  an attack on DDR5 against TDX, SEV-SNP, and NVIDIA CC and forges attestation;
  Battering RAM shows the DDR5 trajectory and that TDX's mitigation is a
  non-default mode; both vendors disclaim the physical threat model entirely.
- Status for the **physical-access (operator) threat model**, which is the one
  that matters for DePIN: **Disproven** — TEE bus-attack resistance cannot carry
  the oracle problem.

## Suggested action (no chapter edit yet — for a human/maintainer decision)

1. Keep the imported chapter text intact (it is a preserved DOCX import); resolve
   via this flag, not an in-place rewrite, unless a maintainer chooses to add a
   dated correction note in-chapter.
2. When the chapter is next revised, downgrade the TDX/NVIDIA-CC line from
   "Hardened (DDR5)" to "**physically breakable bus attacks demonstrated
   (TEE.Fail, 2025); vendors treat physical access as out of scope**."
3. Re-anchor the DePIN oracle-problem answer on defenses the project **already
   owns** and that do not assume an honest operator: population / redundant
   confirmation, hardware-fingerprint cross-checks (Chapter 02 already proposes
   microarchitectural fingerprinting), statistical anomaly detection in the
   sensor array (Chapters 10/16), and economic slashing (Chapter 11). TEEs can
   raise the cost of cheating but cannot be the root of trust against a hardware
   owner.
