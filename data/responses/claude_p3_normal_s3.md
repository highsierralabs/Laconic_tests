---
model: Claude
prompt: 3
prompt_slug: label-window
mode: normal
seed: 3
words: 552
---

**Don't ship.** The checklist doesn't do what Ops wants it to do, and the deeper problem is that manual inspection may not close the hazard either.

**Why the checklist record isn't sufficient**

The changeover checklist attests that the stout roll came off and the ale roll went on. It doesn't attest to *when* in the can stream that happened, to can-level resolution. That's precisely the thing the camera was there to establish and the thing you've lost. A roll swap that's correct in every respect can still land a few dozen cans early or late relative to the product transition, and no checklist signature resolves that.

Your count reconciliation confirms you don't have tight boundaries: 3,612 against a nominal 3,600 is 2.4 seconds of production unaccounted for. Small, but it means the window edges are soft — so whatever population you act on has to be bracketed from the last camera-verified-good can before dropout to the first verified-good can after, not from a clock arithmetic estimate.

**The part that decides between inspect and destroy**

Manual inspection verifies *labels*, not label-to-contents match. That distinction is everything here:

- If ale-labeled cans contain stout, an inspector sees a correct-looking pale ale label and passes it. Undeclared milk, Class I recall exposure.
- If stout-labeled cans contain ale, that's overdeclaration — a misbrand you can't ship, but not an allergen safety hazard. Manual inspection catches this completely, because the defect is visible on the can.

So the question you need answered before you can choose is: **was the brite can stream through the labeler homogeneous during that window?** With brite cans labeled as a separate pass, that depends on whether the stout brite pallets were physically cleared from the depalletizer, accumulation table, and infeed conveyor before ale cans were introduced, and whether that clearance is independently documented.

- **Documented clean physical separation of product** → 100% manual inspection is a valid disposition. You're only looking for stout labels in an ale-only population.
- **Any possibility stout and ale brite cans coexisted in the infeed** → inspection cannot clear the lot. Destruction, or hold pending analytical verification.

One forensic avenue worth checking before you commit to destruction: a milk stout carries substantially higher residual extract than a pale ale, so fill weights differ. If your checkweigher logged that window with enough resolution and its data is intact, it may let you demonstrate the stream was single-product. That's a data-recovery argument, not a substitute for the camera, and QA has to decide whether it's defensible.

**On the 06:00 cut**

Deviating from a written allergen-control SOP under order-cutoff pressure is the exact fact pattern that fills recall root-cause reports. It also destroys the defensibility of the record afterward — you'd be explaining to an investigator why the documented control was set aside on a supervisor's judgment. If a deviation is genuinely being considered, it needs a formal documented deviation with QA authority sign-off, not an operational decision on the floor.

Practically: 3,612 cans is a few hours for a small team at a realistic sustained inspection rate, with second-person verification and a defined defect standard. If the product-separation question can be answered in the next hour, inspection may still make the truck. If it can't be answered, the lot doesn't ship — and that decision belongs to your QA lead against your HACCP/food safety plan, not to me.
