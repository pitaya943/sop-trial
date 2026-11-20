<!-- pitaya template 0.1.1 · AGENTS.md -->
# AGENTS.md

A short map for coding agents. Details live in the files it points to; read them when you need them.

## Start here

- Read `docs/agents/harness.md` first: the level, who the Owner is, who may merge, where tickets live, how work is verified.
- Before planning or building, read `docs/agents/learnings.md`, and the parts of `docs/agents/architecture.md` and `docs/agents/glossary.md` your work touches.
- Work on a branch, never on `main`.

## Commands

- Test: `.venv/bin/python -m pytest -q`. Run it after every change and before saying anything is done.

## Done means

1. The completion conditions of the ticket each have a test that went red first, then green.
2. The full test command passes locally and in CI.
3. The pull request shows evidence: the commands you ran and their real output.
4. A fresh verifier, not the session that wrote the code, judged it PASS.
5. Whoever `docs/agents/harness.md` names under Autonomy merges it.

## Never

- Push to `main`, force-push, or delete remote branches. A hook blocks these; open a pull request instead.
- Merge a pull request unless `docs/agents/harness.md` says agents merge. A hook asks the user first.
- Skip, delete or loosen a test to get green.
- Read, print or commit secrets (`.env`, keys, credentials).
- Change this file, `docs/agents/harness.md`, `.claude/` or CI workflows unless the user asked. A hook asks the user first.
- Connect to shared or production systems. Use local, throwaway resources.

## When unsure

Stop and ask the Owner, with two or three options, their consequences and your recommendation. Don't guess.

## Where things are

- `docs/agents/harness.md`: this project's harness settings.
- `docs/agents/architecture.md`: the module map. Read it before changing the structure.
- `docs/agents/glossary.md`: the project's words. Use them in code, tests and tickets.
- `docs/agents/learnings.md`: what earlier work learned the hard way. Read it before planning or building.
- `docs/decisions.md`: the Owner's decisions, append only.
- Skills (the `pitaya` plugin): `/pitaya:setup`, `/pitaya:build`, `/pitaya:verify` and the rest.
