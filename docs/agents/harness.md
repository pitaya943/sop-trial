# Harness

Read by every pitaya skill before it plans, builds, verifies or reports. Written by `/setup`; edit it by hand or re-run `/setup`.

## Level

- Level: 1. What it includes: `docs/levels.md` in the pitaya plugin; what each part achieves: `docs/suggestion.md`. Raise it by adding guardrail recipes; record each under "Guardrails" below.
- Templates: pitaya 0.1.1. The version `/setup` installed; re-run `/setup` to find stale copies.

## People and accounts

- Owner: pitaya943.
- Machine account: bullet-bots. Agents push, open PRs and comment as this account.
- Autonomy: Only the Owner merges `main`.

## Work

- Issue tracker: GitHub Issues in this repo.
- Tickets: GitHub Issues labelled `ticket`.
- Milestones: `docs/milestones/M<n>.md`, written by `/plan --roadmap`; one is active at a time. None yet.
- Test command: `.venv/bin/python -m pytest -q`. Recorded exactly as it runs here; create the venv first with `python3 -m venv .venv && .venv/bin/pip install pytest`.
- Document language: zh-TW. Used for PRs, issues, comments and reports. Code, identifiers and commit messages stay in English.

## Review

- Verification: a fresh subagent, started by `/verify`.
- Fix rounds: 2. Round 1 in the builder's session, the rest in fresh sessions; still failing after the last round means escalating to the Owner.
- Autopilot: off.
- Learning: off.

## Records

- Decisions: `docs/decisions.md`. Append only: add new entries, never rewrite old ones.
- Glossary: `docs/agents/glossary.md`. The project's words; `/plan` keeps it current.
- Learnings: `docs/agents/learnings.md`. Append only; `/retro` adds what the Owner accepts.
- Architecture: `docs/agents/architecture.md`. The module map; `/plan` keeps it current.

## Sensitive areas

Areas where a change needs a covering test before it starts, otherwise escalate to the Owner.

- Money calculations: amounts are integers in cents, never floats.

## Guardrails

Guardrails in place. Skills rely on these being enforced by hooks or CI rather than re-checking them by hand.

- Level 1 hooks: no pushes to `main` or force pushes, no destructive commands, ask before editing rule files, ask before merging a PR. They look inside `sh -c` and `eval`.
- Level 1 permissions: `.claude/settings.json` denies reading secrets, including `.env` files in subdirectories.
- Level 1 CI: the `tests` workflow, required on `main`.
- protect-main: ruleset on `main` (PR required, no force push, no deletion, `tests` required).
- scope (Level 2): `.github/workflows/scope.yml` fails a ticket PR that changes files outside its "## Scope". Not a required check (PR #11 merged with it red).
