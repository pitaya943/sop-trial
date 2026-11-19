---
name: handoff
description: Leave work so another session or person can pick it up in minutes. Push the branch, then write hand-off notes with the goal, what's done with evidence, what's in progress, and the exact next step. Also how to start from someone else's notes.
disable-model-invocation: true
argument-hint: "<optional: the ticket or branch being handed off>"
---

# Hand off

Use it when work stops before it's done: the session is ending, the context is filling up, or someone else takes over.

## 1. Make the state safe

1. Read `docs/agents/harness.md` for the document language and where tickets live. If it's missing, suggest `/setup` once and continue.
2. Commit work in progress to the ticket's branch, with a message starting `wip:`, and push it. Never push to `main`, and never leave work that exists only on this machine.
3. Note what isn't committed on purpose, such as local secrets or generated files, and why.

## 2. Write the notes

Fill in [handoff-template.md](handoff-template.md) in the document language. Write pointers, not copies: link the ticket, PRs, commits and verdicts instead of pasting them.

- **Goal:** the ticket link and one sentence.
- **State:** branch, head commit, whether the tests pass right now (run them, and paste the summary line).
- **Done:** each finished done-when condition with its evidence.
- **In progress:** what was half-way, and what's known about it.
- **Next step:** the exact first command or action, specific enough to start without reading anything else.
- **Open questions:** anything waiting on the Owner, with the issue link.
- **Gotchas:** what cost time and would cost the next session time too. If it's worth keeping beyond this work, also propose it as a learning for `/retro`.

Post the notes as a comment on the ticket. Without a tracker, put them in the PR description, or in `docs/handoff/<branch>.md` on the branch itself.

## 3. Starting from someone's notes

1. Read the notes, then check them against reality: `git log` on the branch, the head commit, the test command. If they disagree, trust the repository and say so.
2. Run the tests before changing anything, so you know the starting state.
3. Continue from "Next step". If you finish, say in the PR which notes you started from.

## Don't

- Don't write secrets into the notes, even when they explain a failure.
- Don't describe work as done if its evidence isn't linked.
