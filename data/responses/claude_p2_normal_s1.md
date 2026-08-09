---
model: Claude
prompt: 2
prompt_slug: pallet-7
mode: normal
seed: 1
words: 539
---

Neither, yet. QC has posed this as a binary, but the pallet's disposition hinges on a factual question nobody has answered: **is the 61 ppb can on that pallet, or is it in the cull bin?** A timestamp in minute 1 is consistent with both, and the answer flips the decision cleanly.

**The reconciliation that settles it**

Your cull log has 48 case numbers spanning minutes 0–2. Multiply that by cans per case and compare against line speed × the startup window (plus ramp-up, and round the straddling case at the minute-2 boundary up to a whole case, since a good cull takes the whole case). If culled cans ≥ theoretical startup production, the window was fully contained and nothing from minute 1 reached the pallet — which means the QC can was a line pull off the filler exit, sampling product that was subsequently culled. If culled cans fall short, startup product escaped and you have a containment problem that's bigger than one pallet.

Ask QC directly where that can was pulled from — line exit or palletized case. That's a two-minute conversation and it may resolve everything before you touch the arithmetic.

**Test the population you're actually deciding about**

The 11 other cans tell you nothing about the pallet's worst case. Pull 6–10 cans from the *earliest surviving case numbers* on pallet 7 — the cases produced immediately after the cull boundary. That's the highest-TPO product you actually shipped, and it's a direct measurement rather than an inference. Run them alongside a re-test of a retained can if you kept one, and verify the piercing device seal and equilibration protocol while you're at it; bad seals on a CboxQC-type instrument bias high, and a single unreplicated 61 is thin evidence to dump a pallet on.

One thing to check on the numbers: 61 sits about 3.8σ off a mean of 38 with σ=6. If that reading is inside your 12-can dataset, the remaining 11 are tighter than σ=6 suggests, and your in-control population has real margin to the 50 ppb limit. Confirm whether 38 ± 6 includes the outlier — the statistic that matters for release is the 11 without it.

**Decision rule, set before the data comes back**

- Cull reconciles complete **and** earliest-case cans test in spec → release. Document the assignable cause (startup: bowl not purged, undercover gassing not stabilized, seamer cold), the exclusion rationale, and the confirmatory testing. An assignable-cause outlier from product you deliberately removed is not a pallet defect.
- Cull reconciles short, **or** any earliest-case can exceeds 50 → hold the pallet. Don't dump it — 61 ppb is a shelf-life risk, not a safety one, and a held pallet can be re-tested, re-dated, or diverted to a short-shelf-life channel. Dumping is irreversible and forecloses those options.
- Results ambiguous by 14:00 → hold, let the truck leave, take the late-delivery hit. That's the cheapest of the bad outcomes.

You have the morning plus early afternoon; this is comfortably doable before 15:00 if you start the pulls now.

**Regardless of outcome:** a QC can identified by timestamp alone is the root cause of this entire scramble. Marking sample cans with case number at pull is a trivial CAPA and would have made this a five-minute call. Worth filing today while the pain is fresh.
