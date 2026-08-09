---
model: Claude
prompt: 3
prompt_slug: label-window
mode: normal
seed: 1
words: 478
---

**Don't ship. Hold the whole window, then split it — inspect what you can verify, destroy what you can't.**

The core reason ops' argument fails: the checklist isn't your preventive control, the camera is. Under a FSMA allergen preventive control, the checklist is a setup record, not monitoring of label application. A camera dropout across an allergen changeover is a preventive-control deviation, and product produced during it can't be released until it's evaluated (21 CFR 117.150). Overriding a written allergen SOP on a paper record — with no signed deviation — is the exact finding that costs you a warning letter and your SQF/BRC cert even if the cans turn out fine.

**The asymmetry that actually matters**

Two failure directions, wildly different consequences:

- **Stout label on a pale ale can** — over-declaration. Mislabeled, non-saleable, not a safety event.
- **Ale label on a stout can** — undeclared milk. Class I recall, Reportable Food Registry, real anaphylaxis exposure.

Only the second one should drive your decision, and it's the one 100% *visual label* inspection cannot catch. You can't see lactose through an aluminum can. So "100% manual inspection" only discharges the SOP for cans you can independently establish were pale-ale-filled.

**What to do before 06:00**

1. **Bracket wider than 12 minutes.** Use the camera's last verified PASS record and first PASS after recovery — not the estimated dropout duration. The 3,612 vs ~3,600 gap tells you your 300 cpm assumption is approximate; don't let an approximation define an allergen hold.
2. **Establish the *fill* changeover point**, not just the label changeover. Date/lot inkjet codes, filler CIP/purge records, brite tank turnover time, and FIFO through any accumulator between filler and labeler. This is the whole ballgame.
3. **Segregate:**
   - Cans positively confirmed ale-filled → 100% manual label check clears them. Pull any stout labels found.
   - Cans that could be stout-filled, or where fill sequence can't be reconstructed → **destroy**. No inspection resolves these.
4. **Run label reconciliation on the pulled stout roll** — labels issued minus labels remaining vs. stout cans produced. Treat a clean reconciliation as corroborating evidence, never as the release basis.
5. **Check the labeler itself** — splice area, magazine, any stout web left in the path. Pressure-sensitive roll changes are exactly where stray labels survive.

**On the clock**

~3,612 cans is roughly 150 cases. De-case, inspect, re-case with 4–6 people is a 2–3 hour job. If you start now you likely make 06:00 on the ale-confirmed portion. If the fill sequence can't be reconstructed in time, destroy that subset and ship short — a partial order is a conversation with a customer, a stout-filled can labeled pale ale is a recall.

Two last things: this release decision belongs to QA/your PCQI, not ops — get it signed either way. And file the deviation with a root cause on the camera dropout regardless of outcome, because "camera goes down during changeovers" is the finding an auditor will pull the thread on.
