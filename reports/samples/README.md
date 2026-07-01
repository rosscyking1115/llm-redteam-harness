# Sample findings — real data

These are **committed sample artifacts** produced by the foundry commands on the
actual pinned corpora and the cross-judged run results in `results/`. They carry
no prompt text (aggregate counts only), so they are safe to commit; the rest of
`reports/` is gitignored and re-creatable.

Regenerate any of them from a fresh checkout after `redteam corpora download`.

## Benchmark staleness

`redteam corpora staleness --only <corpus> --run <cross-judged.json> ...`

| Corpus | Staleness (heuristic) | Reading |
| --- | ---: | --- |
| [AdvBench](staleness/advbench/staleness_report.md) | **0.38** / 1.00 (mixed) | No dated memes, no duplication; but attacks barely succeed (max baseline ASR 1%) and defences can't move ASR — the benchmark can't discriminate on 2026 models. |
| [AgentDojo](staleness/agentdojo/staleness_report.md) | **0.43** / 1.00 (mixed) | Same near-universal attack failure, plus heavy templated near-duplication. Cross-judge κ = +1.000 confirms ASR itself is well-posed. |

Both are driven by `universal_low_asr` and `low_defence_sensitivity`, while
`judge_disagreement` is 0.00 (perfect cross-judge agreement) — the honest
decomposition of "robust model vs stale benchmark".

## Defence comparison

- [`defence_comparison/`](defence_comparison/defence_comparison.md) — ASR, cost,
  and latency across 8 AgentDojo configs (2 targets × 4 defence stacks).
- [`defence_comparison_frr/`](defence_comparison_frr/defence_comparison.md) — the
  **complete** version with false-refusal rate and safe-usefulness, from real
  benign runs on Claude Sonnet 4.6:

  | config | ASR | FRR | safe-usefulness | cost $ | avg ms |
  | --- | ---: | ---: | ---: | ---: | ---: |
  | baseline | 0.0% | 0.0% | **1.00** | 0.14 | 3142 |
  | full stack (system-prompt + spotlighting + secalign + constitutional) | 0.0% | 0.0% | **1.00** | 0.41 | 4610 |

  The honest reading: the full defence stack is **free** (0% false refusal — it
  doesn't over-block legitimate requests) but also **useless** on this benchmark
  (0% ASR to begin with — nothing to defend), while costing ~3× and adding
  latency. `safe_usefulness = (1 - ASR) * (1 - FRR) = 1.00` either way.

## False-refusal by language

[`frr_by_language/`](frr_by_language/frr_by_language.md) — over the multilingual
benign control set on Claude Sonnet 4.6: **0% false refusal across every
language** (Traditional/Simplified Chinese, Japanese, Korean, and code-switched).
Sonnet 4.6 does not over-refuse benign non-English prompts — a real result, since
many models do. (FRR here is the rule-based refusal rate; for benign prompts a
refusal is unambiguously a *false* refusal.)

## Corpus data card

[`corpus_audit/corpus_datacard.md`](corpus_audit/corpus_datacard.md) — the
combined audit of all four corpora (1883 cases): **16 cross-source duplicate
groups**, **100% Latin-script** (0 code-switching), and the language / attack-
family coverage. Concrete evidence for "dedupe before reporting a single ASR
over the union" and for the multilingual roadmap.

> All numbers trace to `results/` run artifacts and `configs/dataset_versions.yaml`;
> see [`../../METHODOLOGY.md`](../../METHODOLOGY.md) for how each is validated.
