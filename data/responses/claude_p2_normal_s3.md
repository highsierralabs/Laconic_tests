---
model: Claude
prompt: 2
prompt_slug: pallet-7
mode: normal
seed: 3
words: 492
---

**Release-track, but don't release yet — and don't dump.** The 61 ppb can is almost certainly telling you the SOP works, not that the pallet is bad.

**The 61 isn't from the same population as the rest.** With 11 cans at 38 ± 6, a 61 sits ~3.8σ out. That's not the tail of your normal fill distribution — it's a different regime, which is exactly what the 0–2 minute startup window is. Your SOP already anticipates this and culls it. The reading is consistent with a correctly calibrated cull threshold, not with a pallet-wide excursion.

**So the 61 is evidence about culled material, not about pallet 7.** If the cull executed completely, that can represents product that no longer exists in saleable inventory. Dumping the pallet on that number is treating a measurement of removed product as a measurement of retained product.

**The real question is narrow and answerable before 15:00:** does pallet 7 contain any case from minutes 0–2? Three checks, maybe 30 minutes of records work:

1. **Reconcile the cull count against line output.** At your fill rate and cans-per-case, what should two minutes of production have produced? If 48 cases meets or exceeds that, the cull swept the window with margin. If 48 is materially short, product escaped.
2. **Check case-number continuity.** Is pallet 7's lowest case number above the highest number in the cull log? If the culled block is contiguous and pallet 7 starts after it, you're clean.
3. **Confirm where the QC can was drawn from** — off the line at the seamer, or out of a case? If it was a line pull, it was never in a pallet at all and the whole question is about records, not that can.

**If the reconciliation is clean:** release, and document the 61 in the disposition record as startup-window material captured by the cull, with the reconciliation attached. Don't leave it as an unexplained out-of-spec reading in the file.

**If anything doesn't reconcile:** don't dump the pallet — pull six cans from the *lowest-numbered cases in pallet 7 specifically*. That's where startup product would sit if any leaked through. Targeted sampling beats random here, and TPO runs a few minutes per can. Clean results release the pallet; a hit lets you strip the earliest cases and release the balance. Pallets are splittable; the failure mode you're guarding against is geographically confined to one end of it.

Two things worth raising after the truck leaves:

**The traceability gap is the actual defect.** Identifying QC samples by timestamp only, without case number, is what turned a lookup into a three-hour fire drill. Adding case number to the QC pull sheet costs nothing and closes this permanently.

**Your capability margin is thin.** Mean 38 against a 50 ceiling with σ=6 puts the spec limit at 2σ — roughly Cpk 0.67. Even with a perfect cull you'd expect occasional in-run exceedances. That's a separate process conversation, but it's the one that will keep generating these calls.
