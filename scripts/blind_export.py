#!/usr/bin/env python3
"""Export response bodies for blinded scoring: randomized IDs, model/mode labels
stripped. Writes out/blinded/<RID>.md and out/blinding_manifest.csv (keep the
manifest away from the scorer until scoring is complete). out/ is gitignored."""
import csv, os, random, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = f"{ROOT}/data/responses", f"{ROOT}/out"
os.makedirs(f"{OUT}/blinded", exist_ok=True)
files = sorted(f for f in os.listdir(SRC) if f.endswith(".md"))
rng = random.Random(20260809)
rids = [f"R{n:03d}" for n in rng.sample(range(100, 999), len(files))]
rows = []
for rid, fn in zip(rids, files):
    t = open(f"{SRC}/{fn}", encoding="utf-8").read()
    body = t.split("---\n", 2)[2].strip()
    m = re.match(r"(\w+)_p(\d)_(\w+)_s(\d)\.md", fn)
    prompt = m.group(2)
    open(f"{OUT}/blinded/{rid}.md", "w", encoding="utf-8").write(f"prompt: {prompt}\n\n{body}\n")
    rows.append([rid, m.group(1), prompt, m.group(3), m.group(4)])
with open(f"{OUT}/blinding_manifest.csv", "w", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["rid", "model", "prompt", "mode", "seed"]); w.writerows(rows)
print(f"wrote {len(files)} blinded files to out/blinded/ (prompt number kept — the rubric needs it; model/mode/seed stripped)")
print("manifest: out/blinding_manifest.csv — do not open until scoring is done")
