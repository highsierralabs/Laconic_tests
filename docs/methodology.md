# Methodology and decision log

How the directive and the numbers in this repo were produced. Distilled from the working
sessions in which the directive was iterated; chronological.

## Round 1 — v1 shakedown (brewing prompts)

Three decision prompts, one normal + one laconic generation per model (ChatGPT 5.5 Sol
High, Claude Opus 5 High, Gemini 3.1 Pro Extended thinking; "High"/extended-thinking
settings throughout). Corpus reduction 66.8%. Two failure classes surfaced, both in the
hardest-compressing models: (1) a verdict inversion — one laconic reply flipped a
destroy/release call relative to its own normal-mode analysis and fabricated a
probability; (2) protocol-free verdicts — right call, no executable next step (one
destroy/release answer was 22 words). The best-retaining model showed the opposite
failure: barely compressing (7.6% on one prompt).

## v1 -> v2 amendments

Four line-level changes (see directive/CHANGELOG.md): verdict invariance, an action
floor, a sharpened retention test, and a sufficiency target. One design note: the
round-1 test directive lacked a next-steps clause; its absence plausibly explains the
missing protocols.

## Round 2 — fresh prompts, pre-specified keys

Three new prompts (silo / pallet / label) engineered so dropped details are expensive,
with scoring keys written before the runs and keyed verdicts spanning hold, release,
and a rule-prescribed middle path. Result: 9/9 laconic verdict-match, zero flips, zero
fabricated certainty, 9/9 action floors. One model's laconic reply was MORE correct
than its own normal (the normal overclaimed; the laconic restored the conditional) —
which is why scoring is key-anchored rather than normal-vs-laconic consistency.

## Round 3 — seeded replication (n=3 per cell)

Two additional independent draws per cell (fresh chats; regenerate-in-thread does not
count). 54 generations. Verdict gate 27/27 laconic. Second-tier drops proved stable per
model across the observed draws rather than random: 27 of the 33 model-item cells are unanimous
across seeds (0/3 or 3/3), and each model's zeros are stable — ChatGPT 0/3 on
O2/multi-gas, engulfment stop, and fill-vs-label pivot; Gemini 0/3 on lockout, count
honesty, engulfment stop, and fill-vs-label pivot; Claude zero items at 0/3. The six
split cells (1/3 or 2/3) are listed in results/scores_items.csv and mark where seed
variance is real. The corresponding presence of dropped items in the same models'
normal-mode replies is a reading of the transcripts, not scored data; see
docs/scoring.md, "Known limitations." A proposed v3 clause was dropped when its
motivating example proved to be sampling variance (1 of 6 generations). One
verbatim-duplicate pair flagged a data-quality issue, resolved by an independent replacement draw (data/raw/ChatGPT_p1_laconic_s3_replacement.txt), substituted by the parser for seed 3.

## Contamination and rerun

The original Claude arm was invalidated: the account's profile-level custom instructions
contained an earlier laconic block closely related to the one being tested, and per
Anthropic's documentation, preferences apply even in incognito chats. The contaminating
block is published as data/raw/claude_profile_instructions_contaminating.txt so the
fingerprint below is checkable.

Fingerprint in the data: that block instructs the model to "instruct Kris on the next
steps with recommended actions," and the corresponding scaffolding appears **5 times in
Claude_v2_seeded.txt and 0 times in Claude_v2_seeded_rerun.txt** — a "normal mode"
baseline reproducing the phrasing of the very preferences the test assumed were absent.
(The by-name form is visible in the round-1 file, Claude.txt: "Next steps for Kris.")

The Claude arm was rerun with custom instructions blanked (verified by a name probe), fresh
incognito chats, 18 generations. Effect: the normal baseline grew 54% (it had been
prefs-deflated), measured compression moved 32.8% -> 62.1%, retention 29/33, verdicts
9/9. The compression-vs-retention trade-off survived the correction. The published
corpus (data/responses/) is the clean set: ChatGPT + Gemini original seeded runs,
Claude rerun.

## Protocol lessons worth stealing

Pre-specify keys before generating — and commit them publicly before the runs so the claim is independently auditable. Score key-anchored, both modes. Seed n>=3 in fresh
chats before concluding anything from a single draw. Probe for instruction-layer
contamination (ask the model your name in a supposedly clean session). Report cells as
n/3, not pass/fail.

## Blinded two-scorer pass and consensus

Normal-mode responses were item-scored (and all 54 responses gate- and flag-scored) in
a blinded two-scorer design. Scorer 1 (the Claude chat instance that authored the
rubric) scored all 54 blinded, URL-neutralized bodies and sealed its sheets with
published SHA-256 hashes before scorer 2 ran. Scorer 2 was a fresh ChatGPT instance —
cross-family to decorrelate errors — given a self-contained packet (definitions, keys,
corpus, templates) with browsing off; the previously used ChatGPT review thread was
excluded as contaminated by the published scores.

Agreement: 11-item rubric 96.0% raw, Cohen's kappa 0.890 (8/198 disagreements);
verdict gate 87.0%, kappa 0.323; factual flag 70.4%, kappa 0.357. Scorer 2 was stricter
in 30 of 31 disagreements and showed no same-family leniency; the one generous call was
correct (an engulfment reference scorer 1 missed — conceded without adjudication). The
Director adjudicated the remainder as six principle rulings; the record, both raw
sheets, and the rid manifest are in results/scoring/.

Consensus effects: the previously published laconic verdict gate of 27/27 was corrected
to 24/27 (Gemini's prompt-2 release-then-verify constructions were ruled insufficiently
conditional; its normal mode fails the same cells, so the earlier claim that lapses were
normal-mode-only also falls). Factual-integrity flags rose from 8 to 17 of 54 under the
stricter consensus reading of statistical assumptions and implicit
inspection-sufficiency claims. Item retention totals changed by one observation
(a conceded engulfment credit in one Gemini normal).

Known limitations, on the record: scorer 1's blind was procedural (it had read the
corpus repeatedly); both scorers belong to model families under test, since no untested
frontier family exists; the corpus is public, so blinding holds only against a scorer
that does not go looking; and the factual-flag axis showed the lowest agreement — its
definition (claim vs omission, treatment of confidently stated conservative
heuristics) is the first thing to sharpen before the next round. The two scorers also
exhibited characterizable styles — scorer 1 credits hazard-model substance, scorer 2
reads definitions literally and penalizes claims that outrun the stated evidence — and
the adjudicated rulings split between them (four to scorer 1's readings, three to
scorer 2's, one conceded).
