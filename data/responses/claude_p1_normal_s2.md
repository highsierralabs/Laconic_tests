---
model: Claude
prompt: 1
prompt_slug: silo-entry
mode: normal
seed: 2
words: 564
---

**Hold.** Not a close call, and the reason isn't which reading you believe — it's that you don't currently have a valid reading at all.

**Both instruments are disqualified as evidence.**

The fixed sensor failed its bump test 12 days ago and was never re-verified. Under any standard entry program, that instrument is out of service until it's calibrated and passes. Its 0.38% isn't a low reading — it's not data. "Always been reliable" is exactly the argument that shows up in incident reports; a device that has failed its verification check has no track record to lean on. The ±0.05% spec is also meaningless on an uncalibrated unit, since a failed bump test usually means drift or a fouled sensor, and drift on an electrochemical/NDIR CO₂ cell most often trends *low*.

The portable read 1.9% but threw two pump faults. That doesn't let you dismiss the number — pump failure starves the sensor of sample, which biases readings **low**, not high. So the most defensible interpretation is that 1.9% at the hatch is a floor, not a ceiling.

Two instruments disagreeing by a factor of five, with the discordance resolving toward the hazardous direction, is a hold condition on its own.

**What's missing is bigger than what's disputed.**

- **No oxygen reading is mentioned.** CO₂ at 1.9% in a grain headspace is a spoilage signature — microbial and grain respiration producing CO₂ while consuming O₂. The CO₂ number is a symptom; O₂ deficiency is what kills. You need O₂ before anything else.
- **No stratified readings.** CO₂ is denser than air and pools. A hatch-level reading of 1.9% implies substantially higher concentrations at depth. Testing needs to happen top, mid, and bottom before and continuously during entry.
- **A stuck slide gate before a transfer is the engulfment scenario**, not an atmospheric one. Stuck flow usually means bridged or crusted grain with a void underneath. Manual clearing is the single most lethal task in grain handling. That requires all filling and emptying equipment locked and tagged out, no walking down grain, work from outside the bin with a pole if at all possible, harness and lifeline, an attendant in constant contact, and rescue capability on site — not "on call."

**To clear it, you'd need:**

1. A third, independently calibrated instrument — fresh-air zeroed and bump-tested at the hatch right now. That's your tiebreaker, and it's the fastest path.
2. The fixed sensor formally tagged out of service, then calibrated with span gas or replaced. It doesn't come back into the decision until it passes.
3. O₂ plus CO₂ (and whatever else your permit specifies) logged at multiple depths.
4. Mechanical ventilation and re-test to acceptable levels, sustained — not a single passing reading.
5. Full LOTO and engulfment controls in place before anyone approaches the gate.

**On the 14:00 transfer:** move it. Forty minutes of schedule pressure is the variable that turns a monitoring problem into a fatality, and it's the one factor here that's fully within your control. The transfer slipping an hour costs you an hour; the alternative failure mode doesn't have a recovery path.

This should go to your entry supervisor and be decided under your written permit program — I'm working from what you've described, not from your procedures or the bin itself. If you're US-based, the grain-specific requirements in 29 CFR 1910.272(g) are the ones your program should be tracking, and they're stricter than the general confined-space rule.
