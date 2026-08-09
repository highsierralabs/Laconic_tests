# Raw transcripts (provenance)

Original pasted files, untouched. Copy-pasted from chat UIs; expect CRLF line endings,
inconsistent section markers, and one verbatim-duplicate pair (ChatGPT_v2_seeded.txt,
P1 laconic seeds 2/3 — paste artifact, resolved with an extra draw).

- ChatGPT.txt, Claude.txt, Gemini.txt, laconic_instructions_test_prompts.txt — round 1 (v1 directive, brewing prompts). Shakedown only; not scored.
- *_v2.txt, laconic_instructions_test_prompts_v2.txt — round 2 (v2 directive, scored prompts, seed 1).
- *_v2_seeded.txt — round 3 (seeds 1-3). **Claude_v2_seeded.txt is SUPERSEDED**: contaminated by account-level custom instructions (see docs/methodology.md). Retained for the contamination analysis only.
- Claude_v2_seeded_rerun.txt — clean Claude rerun. This is the Claude arm of the published corpus.
- claude_profile_instructions_contaminating.txt — the account-level custom-instruction block that contaminated Claude_v2_seeded.txt. Published so the contamination fingerprint is checkable: grep "next steps" across the seeded file (5 hits) and the rerun (0). Not a test input; it is the confound. Three document-type names from an unrelated project appear as `[REDACTED]`; they are out of scope here and carry no weight in the contamination argument.

data/responses/ holds the normalized, corrected corpus. Prefer it for analysis.
