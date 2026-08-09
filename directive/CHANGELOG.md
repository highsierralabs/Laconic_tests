# Directive changelog

## v1 -> v2 (four amendments, motivated by round-1 failures)

1. **Verdict invariance** — "Compression may drop words, never conclusions..."
   Round 1: one model inverted a destroy/release safety verdict under compression and
   fabricated a probability ("well below the 1% threshold"). This clause makes that a
   rule violation, not a style choice.
2. **Action floor** — "End with the immediate next action(s)..."
   Round 1: two laconic replies delivered verdicts with no executable protocol
   (one was 22 words for a destroy/release decision).
3. **Sharpened retention test** — "Keep any distinction, measurement, or check that
   would change the action" replaces the vaguer "caveats survive only when load-bearing."
4. **Sufficiency target** — "the shortest reply the recipient can execute without a
   follow-up question" converts "as few words as the subject allows" from a
   minimization target into a sufficiency floor.

## v2 (frozen)

A proposed v3 flip-guard clause ("name any single unstated assumption that could flip
the verdict") was dropped: its motivating example dissolved at n=3 (the flagged check
appeared in 1 of 6 generations — sampling variance, not a compression loss).
