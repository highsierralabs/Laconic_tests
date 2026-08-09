---
model: Claude
prompt: 3
prompt_slug: label-window
mode: normal
seed: 2
words: 510
---

**Inspect — but only if the inspection can actually discriminate product, not just label.** Shipping on the checklist isn't an available option, and destruction is premature.

**Why the checklist can't carry this.** It attests that an action was performed, not that the outcome was correct on each can. It doesn't cover labels left in the web path downstream of the splice, the tail of the stout roll, or — most importantly — whether the label change was synchronized with the product change at the filler. That gap is precisely what the camera exists to close, which is why your SOP names this exact scenario. Shipping creates a documented decision to release product you knew was unverified across an allergen changeover; that record is far worse in a recall than the missed order cut.

**The trap in "manual inspection."** On brite cans, the pressure-sensitive label is the only product identity on the container. A human checking labels will confirm that ale-labeled cans say "pale ale" — and will not catch the one hazardous failure mode, which is stout in an ale-labeled can. That's the undeclared-milk direction. The reverse (ale in a stout-labeled can) is misbranding, not an allergen safety hazard.

So inspection is only valid if you have a second identity marker:

- **Date/lot code.** If the inkjet coder ran product-distinct codes and was changed at the fill point rather than the labeling point, you can verify code-to-label agreement can by can. That is a real inspection.
- **If codes don't discriminate** — same code across both products, or coder changed with the labeler — manual inspection cannot discharge the SOP's intent. Destroy the ale-labeled cans in the window. The stout-labeled cans in the window can be held for relabel or dump at leisure; they carry no allergen exposure.

**On the count.** Don't treat 3,612 vs ~3,600 as reconciliation. 300/min is a nominal rate, so a 12-can delta is line noise — and the case-packer counts cans, not label-to-product pairs. If you want genuine reconciliation, pull stout labels consumed (label counter or remaining web length) against stout cans filled.

**Practical path to 06:00.** ~3,612 cans is roughly 150 cases. That is inspectable in a few hours with three or four people, so the cut is likely still makeable if you start now rather than arguing.

1. Hold at case level, and widen the window past the 12 minutes — go from the last camera-verified good can to the first verified good can after recovery, plus a buffer. Dropout log boundaries are coarser than they look.
2. Account for conveyor lag between the labeler and the case packer so you're holding the right cases.
3. Verify label-to-code on 100% of the ale-labeled cans; segregate anything ambiguous into the destroy pile rather than adjudicating it at 03:00.
4. Log the deviation and the disposition rationale regardless of outcome.

One structural note: this disposition belongs to QA, not Ops. If Ops is pushing to ship, the release signature should still be your qualified individual's, and the fact that a release was requested on the checklist alone is itself worth capturing in the deviation record.
