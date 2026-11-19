---
name: ask-owner
description: Stop and hand a decision to the Owner instead of guessing. Use when the spec is unclear or contradicts itself, a change needs a data model or public interface the ticket didn't authorize, the fix rounds are used up, a sensitive area has no covering test, or an action can't be undone.
---

# Ask the Owner

Read `docs/agents/harness.md` for who the Owner is, the fix rounds, the sensitive areas and the document language. If it's missing, suggest `/setup` once and ask in the conversation.

## When

- The spec or ticket is unclear, or two parts of it contradict each other.
- The work needs a change the ticket didn't authorize: a data model, a public interface, a dependency, a file outside its scope.
- The verifier still says FAIL after the last fix round in `docs/agents/harness.md` (default 2).
- A sensitive area from the harness file would change with no test covering it.
- The next step can't be undone: deleting data, rewriting shared history, touching a shared or production system.

Don't use it for what you can settle by reading the spec, the code or the harness file.

## Steps

1. Stop the work the answer affects. Commit and push what's done and unaffected.
2. Find the exact source: the spec section, the ticket condition, the file and line, or the two passages that disagree.
3. Write two or three options. For each: what you'd do, what changes for users, which files and tests it touches, and how costly it is to reverse.
4. Recommend one and say why. Don't start implementing it before the Owner answers.
5. Look for an open issue labelled `needs-owner` about the same question, and add to it if there is one. Otherwise open an issue labelled `needs-owner`, in the document language, assigned to the Owner from the harness file. If there's no tracker, ask in the conversation.
6. Link the issue from the ticket or PR, then carry on with work that doesn't depend on the answer.

## A good question

> **Question:** When an account is disabled, should the records it created stay visible?
> **Source:** the spec's "Accounts" rule 4 contradicts "Retention" rule 2; ticket condition 3.
> **Option A (recommended):** keep the records visible and mark the creator as disabled. No existing test changes; cheap to reverse.
> **Option B:** hide the records too. Two new tests, and search results change.

## After the answer

1. Add the decision to `docs/decisions.md` when the project keeps one.
2. Update the ticket's conditions if the answer changes them.
3. Comment on the issue with where the decision was recorded, then close it.
