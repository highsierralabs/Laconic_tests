---
model: Claude
prompt: 1
prompt_slug: silo-entry
mode: normal
seed: 1
words: 537
---

**Hold.** Not a close call, and the reason isn't the numbers — it's that you don't currently have valid atmospheric data from either instrument.

**Neither reading is admissible right now**

- The fixed sensor failed its bump test 12 days ago and was never re-verified. Under any confined-space program, a failed functional check invalidates that instrument's output from the last known-good verification forward. It isn't reading 0.38% — it's reading nothing. "Always been reliable" is a statement about the past that the bump failure directly contradicts; historical performance is not a verification method.
- The portable logged pump faults. Critically, the dominant failure mode for a sample-draw pump is *insufficient flow* — which biases the reading **low**. So the instrument that reported 1.9% is the one whose fault mode suggests the true value could be higher, not lower.

So the convenient reading is the invalid one, and the alarming reading is the one that may be understated. Do not average them, and do not treat 0.38% as a tiebreaker.

**What the 5x spread is actually telling you**

A fixed sensor and a hatch reading differing by that much is consistent with a stratified atmosphere — which is exactly what you'd expect if grain is respiring or spoiling. CO₂ at 1.9% is well below the 4% IDLH on its own, but CO₂ accumulation in a silo headspace is primarily a *proxy indicator* for oxygen displacement, and oxygen deficiency is what actually kills people in bins. Nothing in your description includes an O₂ reading. That alone stops the entry.

**Before anyone goes through that hatch**

1. Bump and calibrate a second, known-good portable with fresh cal gas. Verify pump flow and the sample line.
2. Test remotely from outside, top to bottom in roughly 4-ft increments, allowing full sample-line lag at each depth. Log the profile, not a single number.
3. Full parameter set: O₂ (19.5–23.5%), CO₂, CO, H₂S, LEL. If the bin has been fumigated within the re-entry interval, screen for phosphine specifically — a 4-gas won't see it.
4. Ventilate, re-test, then continuous monitoring on the entrant throughout.
5. Zero-energy state on every grain-moving device — augers, conveyors, the gate actuator itself. Clearing a stuck slide gate puts a person directly in the flow path; this is an engulfment job as much as an atmospheric one. Harness, lifeline, dedicated attendant, retrieval system, no walking down bridged grain.

**Two things worth pushing on**

Try to clear that gate without entry at all — pole, air lance, external vibrator, actuator work from outside. Most stuck-gate entries are avoidable, and the safest permit is the one you don't write.

And the 14:00 transfer is not a safety input. Forty minutes is genuinely enough to bump a good instrument and run a proper stratified profile — so the schedule may survive this — but if it doesn't, the transfer moves. Schedule pressure at the hatch is the single most common thread running through grain-entry fatality investigations.

Separately, worth a corrective action: a monthly-bump instrument sitting 12 days in failed status without being tagged out is a program gap that will show up again on a worse day.

I'd treat this as general guidance rather than a substitute for your entry supervisor's call under your site permit program and 29 CFR 1910.272(g) / 1910.146.
