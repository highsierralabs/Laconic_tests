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
| Gemini | 3,974 | 539 | 86.4% | 18/33 | 9/9 |

Corpus reduction: 10,813 -> 2,714 words (74.9%). Laconic verdict gate: 27/27. The only
verdict-quality lapses in the corpus are in Gemini's NORMAL mode on prompt 2 (2 of 3
seeds overclaim release before the reconciliation check).

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
