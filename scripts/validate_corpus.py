#!/usr/bin/env python3
"""Corpus integrity checks. Run after parse_transcripts.py, before make_figures.py.
Fails loudly (exit 1) on: missing/extra cells, duplicate bodies within a
model/prompt/mode cell, front-matter word counts that don't match a recount,
word_counts.csv disagreeing with the response files, or malformed score rows."""
import csv, os, re, sys, hashlib, itertools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS, PROMPTS, MODES, SEEDS = ["ChatGPT", "Claude", "Gemini"], [1, 2, 3], ["normal", "laconic"], [1, 2, 3]
ITEMS = {1: ["instrument_validity", "retest_path", "o2_multigas", "loto_isolation", "engulfment_stop"],
         2: ["outlier_provenance", "reconciliation_check"],
         3: ["checklist_ne_labels", "count_honesty", "inspect_destroy_tree", "fill_vs_label_pivot"]}
errors = []

def clean_count(s):
    s = re.sub(r"https?://\S+", " ", s)
    s = re.sub(r"^\[\d+\]:.*$", " ", s, flags=re.M)
    s = re.sub(r"[|*#>`_$\\{}]", " ", s)
    s = re.sub(r"-{2,}", " ", s)
    return len([t for t in s.split() if re.search(r"[A-Za-z0-9]", t)])

# --- responses ---
resp = {}
for m, p, mo, se in itertools.product(MODELS, PROMPTS, MODES, SEEDS):
    fn = f"{ROOT}/data/responses/{m.lower()}_p{p}_{mo}_s{se}.md"
    if not os.path.exists(fn):
        errors.append(f"missing cell: {fn}"); continue
    t = open(fn, encoding="utf-8").read()
    fm, body = t.split("---\n", 2)[1], t.split("---\n", 2)[2].strip()
    meta = dict(l.split(": ", 1) for l in fm.strip().splitlines())
    if int(meta["words"]) != clean_count(body):
        errors.append(f"word-count mismatch in {fn}: fm={meta['words']} recount={clean_count(body)}")
    resp[(m, p, mo, se)] = (body, int(meta["words"]))
extra = len([f for f in os.listdir(f"{ROOT}/data/responses") if f.endswith(".md")]) - len(resp)
if extra: errors.append(f"{extra} unexpected files in data/responses/")

# --- duplicate bodies within a cell (independence check) ---
for m, p, mo in itertools.product(MODELS, PROMPTS, MODES):
    seen = {}
    for se in SEEDS:
        if (m, p, mo, se) not in resp: continue
        h = hashlib.sha256(resp[(m, p, mo, se)][0].encode()).hexdigest()
        if h in seen:
            errors.append(f"DUPLICATE bodies: {m} P{p} {mo} seeds {seen[h]} and {se} are byte-identical")
        seen[h] = se

# --- word_counts.csv agreement ---
rows = list(csv.DictReader(open(f"{ROOT}/results/word_counts.csv")))
if len(rows) != 54: errors.append(f"word_counts.csv has {len(rows)} rows, expected 54")
for r in rows:
    k = (r["model"], int(r["prompt"]), r["mode"], int(r["seed"]))
    if k not in resp: errors.append(f"word_counts.csv row for nonexistent response {k}")
    elif int(r["words"]) != resp[k][1]: errors.append(f"word_counts.csv mismatch for {k}")

# --- scores ---
srows = list(csv.DictReader(open(f"{ROOT}/results/scores_items.csv")))
if "mode" not in (srows[0] if srows else {}): errors.append("scores_items.csv missing mode column")
lac = [r for r in srows if r.get("mode") == "laconic"]
if len(lac) != 99: errors.append(f"expected 99 laconic score rows, got {len(lac)}")
nor = [r for r in srows if r.get("mode") == "normal"]
if len(nor) != 99: errors.append(f"expected 99 normal score rows, got {len(nor)}")
rr = f"{ROOT}/results/scores_response.csv"
if os.path.exists(rr):
    resp_rows = list(csv.DictReader(open(rr)))
    if len(resp_rows) != 54: errors.append(f"scores_response.csv has {len(resp_rows)} rows, expected 54")
    for r in resp_rows:
        if r["verdict_gate"] not in ("pass", "fail"): errors.append(f"bad verdict_gate: {r}")
        if r["factual_flag"] not in ("0", "1"): errors.append(f"bad factual_flag row: {r['model']} p{r['prompt']} {r['mode']} s{r['seed']}")
        if (r["model"], int(r["prompt"]), r["mode"], int(r["seed"])) not in resp:
            errors.append(f"scores_response.csv row for nonexistent response: {r}")
else:
    errors.append("results/scores_response.csv missing")
for r in srows:
    p = int(r["prompt"])
    if r["item"] not in ITEMS[p]: errors.append(f"unknown item {r['item']} for P{p}")
    if r["retained"] not in ("0", "1"): errors.append(f"bad retained value: {r}")
    if (r["model"], p, r.get("mode", "laconic"), int(r["seed"])) not in resp: errors.append(f"score row for nonexistent response: {r}")

if errors:
    print("CORPUS VALIDATION FAILED:"); [print(" -", e) for e in errors]; sys.exit(1)
tot = {m: sum(int(r["retained"]) for r in lac if r["model"] == m) for m in MODELS}
print(f"corpus OK: 54 responses, no duplicates, counts consistent; laconic retention {tot}")
