<!-- pitaya template 0.1.1 · docs/agents/architecture.md -->
# Architecture

A map of the codebase, for orientation before changing it: the main modules, where they live and what each is for. Keep it short; the code is the detail.

`/setup` drafts it from the repository and the Owner corrects it. `/plan` updates it when a plan adds, removes or moves a module.

| Module | Path | Purpose |
| --- | --- | --- |
| trial | `src/trial/` | A tiny package used to try the pitaya workflow; exposes `__version__` |
| bill | `src/trial/bill.py` | `split_bill(total_cents, people)`: splits a bill into integer-cent shares that sum to the total (sensitive: money) |
| tests | `tests/` | pytest tests; `pytest.ini` puts `src/` on the import path |

## How the parts connect

Tests import `trial` and `trial.bill` from `src/`. There is no application entry point yet.
