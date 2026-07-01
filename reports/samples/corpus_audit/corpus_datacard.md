# Corpus data card — combined (4 sources)

## Sources

- **advbench** (504 cases) — pinned 098262edf85f
- **agentdojo** (949 cases) — pinned 18b501a630db
- **harmbench** (342 cases) — pinned 8e1604d1171f
- **jailbreakbench** (88 cases) — pinned 886acc352a31

## Composition

- Total cases: **1883**
- Categories: harmful_content (934), prompt_injection_indirect (949)
- Severity: high (1605), medium (278)
- Prompt length (chars): min 23, median 912, mean 656.1, max 1814

## Languages

Script-based classification (coarse): distinguishes ja/ko/zh and non-Latin scripts, flags code-switching, but does **not** resolve languages that share a script (e.g. English vs French, Simplified vs Traditional Chinese) — that needs a language-ID model (Phase 4).

- Coverage: latin (1883)
- Code-switching (mixed-script) prompts: **0**

## Attack families

Heuristic surface markers (high-precision patterns). A match is a strong hint; a non-match means no known marker was found, not that the prompt is benign.

- Markers: indirect_injection (950), instruction_override (0), obfuscation (0), roleplay_persona (0)
- Prompts with no marker matched: **933**

## Duplicate analysis

- Exact-duplicate cases: **23** (1.2%) across 21 group(s).
- Cross-source duplicate groups: **16** (the same prompt appearing in more than one upstream dataset).
- Near-duplicate pairs (Jaccard ≥ 0.85): **6046**, of which 1 are cross-source.

## Label quality

- Integrity issues found: **0** (empty/trivial prompts, duplicate ids).
- Language coverage and attack-family markers are summarised above; both are coarse/heuristic (see `docs/ROADMAP.md`, Phase 4 for a language-ID model and richer taxonomy).

## Known limitations

- Near-duplicate detection is a token-Jaccard heuristic; it can miss paraphrases that share few tokens and over-flag heavily templated prompts.
- Duplicate/overlap counts mean concatenating these corpora without de-duplication double-counts attack success — split or dedupe before reporting a single ASR over the union.

## Unsafe content handling

- Cases are post-exclusion-filter (CSAM / WMD-synthesis / detailed self-harm methods dropped at load time; see `ETHICS.md`).
- This card and the quality report quote only truncated prompt previews, never full adversarial prompts.

## Recommended use

- Benchmark research and defence comparison.
- **Not** a standalone safety certification, and not a deployment approval signal (see the README positioning).
