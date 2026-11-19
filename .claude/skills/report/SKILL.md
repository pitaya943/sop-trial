---
name: report
description: Summarize a batch of merged work for the Owner, built only from what the repository and GitHub show. Conclusions first, every claim linked to evidence, unfinished work stated plainly, and steps the Owner can run to check it.
disable-model-invocation: true
argument-hint: "<what to cover: a milestone, a list of PRs or tickets, or a date range>"
---

# Report

## Before you start

1. Read `docs/agents/harness.md` for the document language and whether "Learning" is on. If it's missing, suggest `/setup` once and write in the language of the conversation.
2. Settle the range with the user if the argument doesn't make it exact: which PRs or tickets, from when to when.

## Gather, don't remember

Use only sources anyone can open:

- the merged PRs and their descriptions;
- the tickets and their done-when conditions;
- the verifier's verdict comments and the CI results;
- `docs/decisions.md`, when the project keeps one.

Never write from memory of the sessions. If something isn't in those sources, it doesn't go in the report, or it goes in as "unverified".

## Write

Use [report-template.md](report-template.md), in the document language.

- **Conclusion first.** The Owner hasn't followed any ticket; open with what changed for users and whether it's ready.
- **Every claim links to evidence:** a PR, a verdict comment, a CI run, or a command with its output.
- **Numbers can be recomputed.** "47 tests pass" comes with the command that produced it.
- **How to verify** is a list of steps the Owner can run with any model or by hand: commands, expected output, manual checks.
- **Decisions the agents made** that no spec or ticket stated get their own section, even if it's "None".
- **What isn't done** is said plainly: never "could be improved later".
- Don't overstate. Passing tests mean the spec is met, not that the spec is right.

Markdown by default; HTML if the Owner asks for it.

## Deliver

Show the report in the conversation, then ask where it should live: a comment on a tracking issue, or a file under `docs/reports/` added through a pull request.

If "Learning" is on in the harness file, end by offering the `learning` review.
