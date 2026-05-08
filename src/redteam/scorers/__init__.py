"""Scorer registry.

Two scorers ship as of Phase 4:

  - rule-based refusal-keyword detector — cheap, free, brittle (Lesson L6).
  - LLM-judge with Claude Haiku 4.5 — nuanced, ~$0.001/case, validated
    against a 5% human spot-check via Cohen's kappa (Phase 4 batch 2).
"""

from __future__ import annotations

from redteam.scorers._judge_schema import JudgeVerdict
from redteam.scorers.judge_claude import (
    JUDGE_ID,
    JUDGE_MODEL,
    ClaudeJudge,
    JudgeError,
)
from redteam.scorers.judge_human import (
    KappaReport,
    KappaScore,
    compute_kappa,
    export_for_human_review,
)
from redteam.scorers.refusal_keywords import RefusalScore, score_refusal

__all__ = [
    "JUDGE_ID",
    "JUDGE_MODEL",
    "ClaudeJudge",
    "JudgeError",
    "JudgeVerdict",
    "KappaReport",
    "KappaScore",
    "RefusalScore",
    "compute_kappa",
    "export_for_human_review",
    "score_refusal",
]
