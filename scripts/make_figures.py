#!/usr/bin/env python3
"""Regenerate figures/ from results/word_counts.csv and results/scores_items.csv."""
import csv, os, collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLUE, ORANGE, GREEN, GRID = "#2a78d6", "#eb6834", "#1baf7a", "#d9d8d2"
MODELS = ["ChatGPT", "Claude", "Gemini"]
plt.rcParams.update({"font.size": 11, "axes.edgecolor": "#898781", "axes.labelcolor": "#3d3d3a",
                     "xtick.color": "#3d3d3a", "ytick.color": "#3d3d3a"})

words = collections.defaultdict(int)
for r in csv.DictReader(open(f"{ROOT}/results/word_counts.csv")):
    words[(r["model"], r["mode"])] += int(r["words"])

item_order = ["instrument_validity", "retest_path", "o2_multigas", "loto_isolation", "engulfment_stop",
              "outlier_provenance", "reconciliation_check", "checklist_ne_labels", "count_honesty",
              "inspect_destroy_tree", "fill_vs_label_pivot"]
labels = ["Instrument validity", "Re-test path", "O2 / multi-gas", "LOTO / isolation", "Engulfment stop",
          "Outlier provenance", "Reconciliation check", "Checklist \u2260 labels", "Count honesty",
          "Inspect/destroy tree", "Fill-vs-label pivot"]
scores = collections.defaultdict(int)
for r in csv.DictReader(open(f"{ROOT}/results/scores_items.csv")):
    if r["mode"] == "laconic":
        scores[(r["model"], r["item"])] += int(r["retained"])
totals = {m: sum(scores[(m, it)] for it in item_order) for m in MODELS}

# Fig 1
fig, ax = plt.subplots(figsize=(7, 4.2), dpi=200)
x, w = np.arange(3), 0.34
normal = [words[(m, "normal")] for m in MODELS]
laconic = [words[(m, "laconic")] for m in MODELS]
for bars in (ax.bar(x - w/2, normal, w, color=BLUE, label="Normal mode"),
             ax.bar(x + w/2, laconic, w, color=ORANGE, label="Laconic mode")):
    for b in bars:
        ax.annotate(f"{int(b.get_height()):,}", (b.get_x() + b.get_width()/2, b.get_height()),
                    ha="center", va="bottom", fontsize=9, color="#3d3d3a")
ax.set_xticks(x); ax.set_xticklabels(MODELS)
ax.set_ylabel("Total words (9 responses)")
ax.set_title("Figure 1 \u2014 Total word count, normal vs laconic mode", fontsize=12)
ax.yaxis.grid(True, color=GRID); ax.set_axisbelow(True)
ax.spines[["top", "right"]].set_visible(False); ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(f"{ROOT}/figures/fig1_word_totals.png"); plt.close(fig)

# Fig 2
fig, ax = plt.subplots(figsize=(6.5, 4.6), dpi=200)
for m, c in zip(MODELS, (BLUE, ORANGE, GREEN)):
    red = 100 * (1 - words[(m, "laconic")] / words[(m, "normal")])
    ret = 100 * totals[m] / 33
    ax.scatter(red, ret, s=160, color=c, edgecolors="white", linewidths=1.5, zorder=3)
    ax.annotate(m, (red, ret), xytext=(0, 12), textcoords="offset points",
                ha="center", fontsize=10, color="#3d3d3a")
ax.set_xlim(0, 100); ax.set_ylim(0, 105)
ax.set_xlabel("Word reduction (%)"); ax.set_ylabel("Tracked content retained (%)")
ax.set_title("Figure 2 \u2014 Compression vs retention trade-off", fontsize=12)
ax.grid(True, color=GRID); ax.set_axisbelow(True); ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig(f"{ROOT}/figures/fig2_tradeoff.png"); plt.close(fig)

# Fig 3
ramp = {0: "#F1EFE8", 1: "#E1F5EE", 2: "#5DCAA5", 3: "#0F6E56"}
txt = {0: "#5F5E5A", 1: "#085041", 2: "#04342C", 3: "#E1F5EE"}
fig, ax = plt.subplots(figsize=(6.8, 6.2), dpi=200)
for i, it in enumerate(item_order):
    for j, m in enumerate(MODELS):
        v = scores[(m, it)]
        ax.add_patch(plt.Rectangle((j, 10 - i), 0.94, 0.94, color=ramp[v]))
        ax.text(j + 0.47, 10 - i + 0.47, f"{v}/3", ha="center", va="center", color=txt[v], fontsize=10)
ax.set_xlim(0, 3); ax.set_ylim(0, 11)
ax.set_xticks([0.47, 1.47, 2.47]); ax.set_xticklabels(MODELS)
ax.set_yticks([10.47 - i for i in range(11)]); ax.set_yticklabels(labels, fontsize=9.5)
ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
ax.set_title("Figure 3 \u2014 Item retention in laconic replies (seeds retained of 3)\n"
             f"Totals: ChatGPT {totals['ChatGPT']}/33 \u00b7 Claude {totals['Claude']}/33 \u00b7 Gemini {totals['Gemini']}/33",
             fontsize=11)
fig.tight_layout(); fig.savefig(f"{ROOT}/figures/fig3_retention_heatmap.png"); plt.close(fig)
print("figures regenerated from results/*.csv")
