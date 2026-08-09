#!/usr/bin/env python3
"""Export response bodies for blinded scoring: randomized IDs, model/mode labels
stripped, URLs neutralized. Writes out/blinded/<RID>.md and
out/blinding_manifest.csv (keep the manifest away from the scorer until scoring
is complete). out/ is gitignored.

URL neutralization: in this corpus, citation URLs are model-attributable (only
one model emits them, and its links carry vendor tracking parameters), so every
http(s) URL in a body is replaced with the token [url]. Stylistic
identifiability (formatting, phrasing) cannot be stripped without destroying
the scoring target; the blind is partial by design — see docs/scoring.md."""
import csv, os, random, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = f"{ROOT}/data/responses", f"{ROOT}/out"
os.makedirs(f"{OUT}/blinded", exist_ok=True)

def neutralize_urls(body):
    body = re.sub(r"\(\s*https?://[^)\s]+\s*\)", "([url])", body)  # markdown link targets
    body = re.sub(r"https?://\S+", "[url]", body)                  # bare / footnote URLs
    return body

files = sorted(f for f in os.listdir(SRC) if f.endswith(".md"))
rng = random.Random(20260809)
rids = [f"R{n:03d}" for n in rng.sample(range(100, 999), len(files))]
rows = []
for rid, fn in zip(rids, files):
    t = open(f"{SRC}/{fn}", encoding="utf-8").read()
    body = neutralize_urls(t.split("---\n", 2)[2].strip())
    m = re.match(r"(\w+)_p(\d)_(\w+)_s(\d)\.md", fn)
    prompt = m.group(2)
    open(f"{OUT}/blinded/{rid}.md", "w", encoding="utf-8").write(f"prompt: {prompt}\n\n{body}\n")
    rows.append([rid, m.group(1), prompt, m.group(3), m.group(4)])
with open(f"{OUT}/blinding_manifest.csv", "w", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["rid", "model", "prompt", "mode", "seed"]); w.writerows(rows)
print(f"wrote {len(files)} blinded files to out/blinded/ (prompt number kept — the rubric needs it; model/mode/seed stripped; URLs neutralized)")
print("manifest: out/blinding_manifest.csv — do not open until scoring is done")
