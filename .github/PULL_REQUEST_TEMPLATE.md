<!-- One focused change per PR. Thanks for contributing! -->

## What & why

<!-- What does this change do, and why? -->

## Checklist

- [ ] `scripts/ci_local.sh` (or `.ps1`) is green — ruff, ruff format, mypy `--strict`, pytest
- [ ] New behaviour has a unit test (pure / no-network where possible)
- [ ] Touches corpora or prompts? No raw harmful content committed, and the
      exclusion-filter tests were updated if needed (see `CONTRIBUTING.md` → Ethics)
- [ ] `CHANGELOG.md` updated if the change is user-facing
