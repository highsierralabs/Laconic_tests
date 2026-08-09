---
model: Claude
prompt: 2
prompt_slug: pallet-7
mode: normal
seed: 2
words: 460
---

**Neither, yet — the record can't support either decision, and you have time to fix that.**

The core problem: your 61 ppb can is timestamped inside a window whose entire output was supposed to be culled. That yields two incompatible readings, and nothing in what you've described distinguishes them:

1. **QC sampled off the line pre-cull.** The can is culled material that never went on pallet 7. The 61 ppb reading is a measurement of product you already threw away, and it says nothing about the pallet.
2. **The cull was incomplete.** Startup material reached the pallet, and the 61 ppb can is evidence of it.

Dumping assumes (2) without checking. Releasing assumes (1) without checking. Releasing blind is the worse of the two: you'd have a documented 61 ppb result in the file with no reconciliation behind the decision to ship.

**Resolve it with arithmetic first, in about ten minutes.** The cull log has 48 case numbers. Case numbers are sequential and your case coder should tie them to time. Compute expected case output for minutes 0–2 from line speed and cans per case. If 48 matches expected, the cull was complete. If expected is 60 and you pulled 48, roughly twelve cases of startup material are somewhere — likely the bottom of pallet 7. Then check contiguity: if the culled case numbers are a continuous block and pallet 7's lowest case number is above the highest culled one, the pallet is clean by construction.

**Then resample, by case number.** Pull six cans from pallet 7's lowest case numbers — the earliest-filled, highest-risk material — and run TPO. That's well under an hour on an Orbisphere or Haffmans, and you dock at 15:00. This is the only test that actually measures what's on the pallet.

Two supporting observations:

- Elevated TPO at startup is physically expected: fill bowl not fully purged, undercover gassing not at steady state. 61 against a run mean of 38 fits startup behavior, not a sporadic seamer or single-head fault. A persistent head fault would show up throughout the run, and your other eleven cans didn't.
- Recompute your statistics without the 61. If it's one of the twelve, the remaining eleven average about 36 ppb, with a tighter SD. As stated, 38 ± 6 puts your 2σ bound exactly at spec — Cpk around 0.67, which is marginal capability worth a separate look regardless of how pallet 7 resolves.

If reconciliation and resample both come back clean, release with the reconciliation documented. If either fails, cull the affected case-number range — not the whole pallet.

Afterward, one CAPA item: QC cans identified by fill timestamp only, with no case number, is the root cause of this entire dilemma. Record both on the sample tag and this stops being a judgment call next time.
