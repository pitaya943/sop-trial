# Harness

Read by every sop-v2 skill before it plans, builds, verifies or reports. Written by `/setup`; edit it by hand or re-run `/setup`.

## People and accounts

- Owner: pitaya943. Only the Owner merges `main`.
- Machine account: bullet-bots. Agents push, open PRs and comment as this account.

## Work

- Issue tracker: GitHub Issues in this repo.
- Tickets: GitHub Issues labelled `ticket`.
- Test command: `python3 -m pytest -q` (install pytest first, for example in a `.venv`).
- Document language: zh-TW. Used for PRs, issues, comments and reports. Code, identifiers and commit messages stay in English.

## Sensitive areas

Areas where a change needs a covering test before it starts, otherwise escalate to the Owner.

- 金額計算（money calculations）：金額一律用整數「分」計算，不使用浮點數。

## Guardrails

Guardrails in place, from the sop-v2 recipes. Skills rely on these being enforced by CI rather than re-checking them by hand.

- (none yet)
