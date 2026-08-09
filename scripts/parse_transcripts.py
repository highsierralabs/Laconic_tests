#!/usr/bin/env python3
"""Parse raw pasted transcripts in data/raw/ into data/responses/ + results/word_counts.csv.

Handles the paste quirks in the raw files: CRLF endings, case-variant markers
("Normal Mode seed 1:", "seed2"), and a mislabeled seed (assigned by section order).
Corpus rule: ChatGPT + Gemini from *_v2_seeded.txt, Claude from Claude_v2_seeded_rerun.txt
(the contaminated Claude_v2_seeded.txt is excluded; see docs/methodology.md).
One cell override: ChatGPT P1 laconic seed 3 is read from
data/raw/ChatGPT_p1_laconic_s3_replacement.txt, replacing the paste-duplicate
section in ChatGPT_v2_seeded.txt (preserved byte-for-byte as provenance).
"""
import re, csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW, OUT = f"{ROOT}/data/raw", f"{ROOT}/data/responses"
SLUGS = {1: "silo-entry", 2: "pallet-7", 3: "label-window"}

def clean_count(s):
    s = re.sub(r"https?://\S+", " ", s)
    s = re.sub(r"^\[\d+\]:.*$", " ", s, flags=re.M)
    s = re.sub(r"[|*#>`_$\\{}]", " ", s)
    s = re.sub(r"-{2,}", " ", s)
    return len([t for t in s.split() if re.search(r"[A-Za-z0-9]", t)])

def sections(path):
    t = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    parts = re.split(r"\nPrompt (\d)\b", t)
    for i in range(1, len(parts), 2):
        pnum, body = int(parts[i]), parts[i + 1]
        secs = re.split(r"\n(Normal|Laconic) [Mm]ode [Ss]eed ?(\d):\s*\n", body)
        seq = [(secs[j], secs[j + 2].strip()) for j in range(1, len(secs), 3)]
        for k, (mode, text) in enumerate(seq):  # seed by order, not label
            yield pnum, mode, k // 2 + 1, text

def main():
    os.makedirs(OUT, exist_ok=True)
    corpus = {}
    for model, fn in [("ChatGPT", "ChatGPT_v2_seeded.txt"),
                      ("Gemini", "Gemini_v2_seeded.txt"),
                      ("Claude", "Claude_v2_seeded_rerun.txt")]:
        for p, mode, seed, text in sections(f"{RAW}/{fn}"):
            corpus[(model, p, mode, seed)] = text
    assert len(corpus) == 54, f"expected 54 sections, got {len(corpus)}"
    repl = open(f"{RAW}/ChatGPT_p1_laconic_s3_replacement.txt", encoding="utf-8").read()
    body = "\n".join(l for l in repl.splitlines() if not l.startswith("#")).strip()
    corpus[("ChatGPT", 1, "Laconic", 3)] = body
    rows = []
    for (m, p, mode, s), text in sorted(corpus.items()):
        w = clean_count(text)
        rows.append([m, p, SLUGS[p], mode.lower(), s, w])
        with open(f"{OUT}/{m.lower()}_p{p}_{mode.lower()}_s{s}.md", "w", encoding="utf-8") as f:
            f.write(f"---\nmodel: {m}\nprompt: {p}\nprompt_slug: {SLUGS[p]}\n"
                    f"mode: {mode.lower()}\nseed: {s}\nwords: {w}\n---\n\n{text}\n")
    with open(f"{ROOT}/results/word_counts.csv", "w", newline="") as f:
        wtr = csv.writer(f, lineterminator="\n")
        wtr.writerow(["model", "prompt", "prompt_slug", "mode", "seed", "words"])
        wtr.writerows(rows)
    print(f"wrote {len(rows)} responses + word_counts.csv")

if __name__ == "__main__":
    main()
