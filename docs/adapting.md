# Adapting the directive

Laconicism is compression without loss: the shortest reply the recipient can act on. It is not minimalism — a short answer that drops the check you needed is the most expensive kind of short, because the cost moves from reading time to a follow-up question, or to a mistake. The directive encodes that trade. This guide tells you which lines carry it and which lines are just this author's taste.

## Clause map

| Clause | Function | Status |
|---|---|---|
| "As few words as the subject allows... state the result, then stop" | Kills preamble, restatement, sign-off padding | Tunable |
| "Lead with the number, the verdict, or the decision" | Answer-first ordering | Keep |
| "Keep any distinction, measurement, or check that would change the action" | The retention test — decides what survives | **Invariant** |
| "Prose, not lists or headers, unless structure is the answer" | Formatting style | Tunable |
| "Brevity never overrides rigor... take the length" | Escape valve for genuinely complex answers | **Invariant** |
| "Firmware label / classifier subtype / physical interpretation stay distinct" | Domain never-conflate list | **Replace with yours** |
| "Compression may drop words, never conclusions... unknowns stay unknown" | Verdict invariance — bans manufactured certainty | **Invariant** |
| "Formal artifacts follow their own structural conventions" | Scopes the mode to chat, not documents | Keep |
| "Shortest reply the recipient can execute without a follow-up question" | The sizing rule | **Invariant** |
| "End with the immediate next action(s)" | Action floor | **Invariant** |

## The invariants, and why

Every invariant exists because its absence produced a measured failure. Without verdict invariance, one model inverted a destroy/release safety call under compression and invented a probability to justify it. Without the action floor, models delivered correct verdicts with no executable step (22 words on a destroy/release decision). Without the retention test, second-tier checks vanish silently. Without the sizing rule and the rigor valve, "as few words as possible" becomes the objective instead of the constraint. Remove these and you have a brevity prompt, not a laconic one — you will get shorter replies and you will not know what they cost until one of them costs you.

## Tuning the style clauses

**Formatting.** The directive as written strips bullets, headers, and tables because its author reads dense prose faster. Most people don't. Drop-in replacement:

> Bullets, tables, and headers are allowed when they reduce scan time; never as decoration, never to pad.

**Closing summaries.** The no-summary rule assumes short replies that need no recap. If your replies run long or feed handoffs, replace with:

> A one-line closing summary is allowed when the reply exceeds a screen; otherwise stop at the last action.

**Follow-up offers.** Banned as engagement padding. If you want them for genuinely branching work:

> Offer a follow-up only when the next step forks on information you don't have.

**The domain line.** "Firmware label / classifier subtype / physical interpretation stay distinct" is this repo's origin domain (instrument telemetry: what the firmware asserted vs what physically happened). Replace it with the two or three distinctions your field must never collapse. A lawyer: holding vs dicta vs your own inference. A clinician: finding vs diagnosis vs plan. An analyst: measured vs modeled vs assumed. If you can't name yours yet, delete the line rather than keep someone else's.

**Length target.** "Without a follow-up question" is per-task sizing. For casual use you can soften to per-reply ("shortest reply that answers what was asked") — knowing you're trading away the property the invariants protect.

## Model-specific notes (from the data)

The same directive lands differently per model; tune for the one you run.

- **ChatGPT** compressed 82.7% and held verdicts and structure, but dropped companion hazards it named in its own long-form answers (O2/multi-gas 0/3, engulfment stop 0/3, fill-vs-label pivot 0/3) and defaulted conservative on release-shaped calls. It held lockout/isolation 3/3 — the companion-hazard loss is selective, not uniform. If companion checks matter to you, add: *"Name companion hazards or checks the verdict depends on, even if unasked."*
- **Gemini** compressed hardest (86.4%) and dropped the most (18/33): lockout/isolation 0/3, count honesty 0/3, engulfment stop 0/3, fill-vs-label pivot 0/3. (The *reconciliation check* is a different item, and all three models retained it 3/3.) Compression also hides reasoning errors — a hazard-direction inversion visible in its long answers disappeared from its short ones without being fixed. Spot-check its normal mode occasionally even if you only use laconic.
- **Claude** retained most (29/33) and stayed ~3x more verbose (62.1% reduction); it resolves the brevity/rigor tension toward rigor. If the length chafes, add: *"Name the check, not the mechanism"* — accepting it may cost useful inferences (e.g., "pump faults bias the reading low, so treat 1.9% as a floor").

## Where to install it

Per-chat paste is safest while tuning. Project-level instructions scope it to one workspace. Account-level custom instructions apply everywhere — **including incognito/anonymous chats** (this invalidated one arm of our own test). Before any A/B comparison of your edits, blank account-level instructions and verify with a probe: ask the model your name in a fresh session; if it knows, you're not clean.

## Re-test after editing

Never judge an instruction edit on one generation.

1. Write 2–3 prompts from your own domain where a dropped detail is costly.
2. Pre-register the key per prompt: the correct verdict, and the items a passing reply must carry.
3. Run each prompt in fresh chats, n=3 per mode (regenerate-in-thread doesn't count).
4. Score in order: verdict gate first (right decision, no manufactured certainty, unknowns stay unknown), item retention second, word count last.
5. Report cells as n/3. A directive that passes the gate 9/9 and holds your items at the lowest word count wins.

Word count is the cheapest metric and the last one that matters. The directive is working when you stop writing follow-up questions.
