# Results summary

Final corpus: 54 responses — ChatGPT and Gemini original seeded runs, Claude clean rerun
(see docs/methodology.md, "Contamination and rerun"). Word counts are prose tokens with
markdown, tables, and URLs stripped (scripts/parse_transcripts.py). ChatGPT P1 laconic seed 3 is the independent replacement
for a paste-duplicated draw (see data/raw/README.md).

## Totals (9 responses per mode per model)

| Model | Normal words | Laconic words | Reduction | Retention | Verdict gate (laconic) |
|---|---|---|---|---|---|
| ChatGPT | 2,171 | 407 | 81.3% | 22/33 | 9/9 |
| Claude | 4,668 | 1,768 | 62.1% | 29/33 | 9/9 |
| Gemini | 3,974 | 539 | 86.4% | 18/33 | 6/9 |

Corpus reduction: 10,813 -> 2,714 words (74.9%). Verdict gate under two-scorer
consensus: laconic 24/27, normal 24/27 — all six failures are Gemini prompt 2 (both
modes, all seeds): release announced with verification framed as execution rather than
as a gate, plus manufactured certainty in the rationale. Factual-integrity flags: 17 of
54 responses (Gemini 10, Claude 6, ChatGPT 1); per-response notes are in
results/scores_response.csv, and the full reconciliation record is
results/reconciliation.md.

## Figures

**Figure 1 (fig1_word_totals.png).** Total word count across the nine responses per
mode. Claude's normal baseline is the longest of the three; its laconic bar remains
~3x the others'.

**Figure 2 (fig2_tradeoff.png).** Word reduction (x) vs share of the 33 tracked
item-observations delivered in laconic replies (y). Higher = more of the checklist
survives; further right = fewer words. With these three models on these prompts the upper-right corner stays empty:
no model achieves both.

**Figure 3 (fig3_retention_heatmap.png).** The 11 rubric items by model, cell = seeds
retained of 3. The pale cells in the ChatGPT and Gemini columns are the content
Claude's extra ~145 words per reply are carrying (196 words/reply vs 45 and 60); the
uniform top rows show all three models agree on the verdict-critical core. 27 of the 33
model-item cells are unanimous across seeds; the six split cells (1/3 or 2/3) are
ChatGPT count honesty, Claude lockout / engulfment stop / fill-vs-label pivot, and
Gemini O2-multi-gas / inspect-destroy tree. Items are unweighted.

## Paired normal-vs-laconic retention (two-scorer consensus)

| Model | Normal items | Laconic items | Lost under compression | Gained | Loss rate |
|---|---|---|---|---|---|
| ChatGPT | 27/33 | 22/33 | 5 | 0 | 18.5% |
| Claude | 33/33 | 29/33 | 4 | 0 | 12.1% |
| Gemini | 25/33 | 18/33 | 8 | 1 | 32.0% |

Loss rate = item-observations present in normal but absent in laconic, over those
present in normal. The compression-loss claim is now quantitative: e.g., Gemini's
laconic replies lose 8 of the 25 item-observations its normal mode carries — O2/multi-gas
(-2), lockout (-2), engulfment (-3), inspect/destroy tree (-1) — and gain one, the
prompt-2 reconciliation check its normal seed 1 lacked. Claude loses least in both
absolute and rate terms; its four losses are lockout (-2), engulfment (-1), and the
fill-vs-label pivot (-1). ChatGPT's five losses concentrate in O2/multi-gas (-3).
Item-level detail: results/scores_items.csv.
