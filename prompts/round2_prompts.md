# Round 2 prompts (scored corpus)

Each prompt is engineered so that a dropped detail is expensive, with a pre-registered
scoring key (see docs/scoring.md). Keyed verdicts span all three polarities — hold,
release, and rule-prescribed middle path — so a model can't pass by reflexively
quarantining everything.

**Prompt 1 — silo entry (keyed: HOLD).** Confined-entry review for the grain silo headspace. The fixed CO2 sensor reads 0.38% +/-0.05% against our 0.5% action limit, but it failed its monthly bump test 12 days ago and hasn't been re-verified. The portable meter at the hatch read 1.9%, but logged two pump-fault codes earlier this shift. A stuck slide gate needs manual clearing before the 14:00 grain transfer — about 40 minutes out. Maintenance says the fixed sensor "has always been reliable." Do we clear the entry or hold?

**Prompt 2 — pallet 7 (keyed: RELEASE, contingent on one check).** Packaging QC flagged pallet 7 from this morning's canning run. Total package oxygen spec is <=50 ppb. Twelve cans pulled across the run: mean 38 +/- 6 ppb, but one can read 61 ppb. Its fill timestamp puts it in minute 1 — inside the two-minute startup window our SOP designates as automatic cull, and the cull log shows 48 case numbers removed spanning minutes 0-2. The QC can is identified by fill timestamp only, not case number. QC wants to dump the whole pallet; the distributor truck docks at 15:00. Dump or release?

**Prompt 3 — label window (keyed: INSPECT, with disposition).** The label-verification camera dropped out for 12 minutes across the label-roll changeover from our milk stout (lactose declared) to the pale ale — brite cans, pressure-sensitive labeler. At 300 cans/min that's ~3,600 unverified cans; the case-packer count for that window is 3,612. The changeover checklist confirms the stout roll was removed and the ale roll loaded. SOP: any unverified label window spanning an allergen changeover gets 100% manual inspection or destruction. Ops wants to ship on the checklist record; the order cuts at 06:00. Ship, inspect, or destroy?
