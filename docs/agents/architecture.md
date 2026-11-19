<!-- pitaya template 0.1.0 · docs/agents/architecture.md -->
# Architecture

A map of the codebase, for orientation before changing it: the main modules, where they live and what each is for. Keep it short; the code is the detail.

`/setup` drafts it from the repository and the Owner corrects it. `/plan` updates it when a plan adds, removes or moves a module.

| Module | Path | Purpose |
| --- | --- | --- |
| trial | `src/trial/` | A tiny package used to try the pitaya workflow; exposes `__version__` |
| tests | `tests/` | pytest tests; `pytest.ini` puts `src/` on the import path |

## How the parts connect

Tests import `trial` from `src/`. There is no application entry point yet.
