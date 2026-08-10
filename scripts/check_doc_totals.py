#!/usr/bin/env python3
"""Cross-check totals asserted in prose against the shipped CSVs.
Catches the defect class where authored numbers drift from data."""
import csv, os, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
flags = 0; gate = collections.defaultdict(lambda: [0, 0]); items = collections.defaultdict(int)
pm = collections.defaultdict(lambda: [0, 0])
for r in csv.DictReader(open(f"{ROOT}/results/scores_response.csv")):
    flags += int(r["factual_flag"])
    gate[r["mode"]][0] += (r["verdict_gate"] == "pass"); gate[r["mode"]][1] += 1
    pm[(r["model"], r["mode"])][0] += (r["verdict_gate"] == "pass"); pm[(r["model"], r["mode"])][1] += 1
for r in csv.DictReader(open(f"{ROOT}/results/scores_items.csv")):
    items[(r["model"], r["mode"])] += int(r["retained"])

must_contain = {
    f"{ROOT}/results/summary.md": [f"{flags} of\n54 responses", f"laconic {gate['laconic'][0]}/27, normal {gate['normal'][0]}/27"],
    f"{ROOT}/docs/methodology.md": [f"8 to {flags} of 54"],
    f"{ROOT}/results/reconciliation.md": [f"Consensus flag total: {flags}/54"],
    f"{ROOT}/README.md": [f"{gate['laconic'][0]}/27", f"| Gemini | 86.4% | {items[('Gemini','laconic')]}/33 | {pm[('Gemini','laconic')][0]}/9 |"],
}
errors = []
for path, needles in must_contain.items():
    t = open(path, encoding="utf-8").read()
    for n in needles:
        if n not in t: errors.append(f"{os.path.basename(path)}: expected '{n}' derived from CSVs")
if errors:
    print("DOC-TOTALS CHECK FAILED:"); [print(" -", e) for e in errors]; sys.exit(1)
print(f"doc totals OK: flags {flags}/54, gate laconic {gate['laconic'][0]}/27 normal {gate['normal'][0]}/27, laconic items {items[('ChatGPT','laconic')]}/{items[('Claude','laconic')]}/{items[('Gemini','laconic')]}")
