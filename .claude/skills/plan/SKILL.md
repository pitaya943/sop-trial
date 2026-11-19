---
name: plan
description: Turn a request, spec or conversation into tickets an agent can build and verify on their own, each a thin vertical slice with completion conditions, dependencies and scope. The Owner approves the list before anything is written to the tracker.
disable-model-invocation: true
argument-hint: "<what to build: a description, a spec path or an issue>"
---

# Plan

## Before you start

1. Read `docs/agents/harness.md`: where tickets live, the level, the "Guardrails" list and the sensitive areas. If it's missing, suggest `/setup` once, then continue with GitHub Issues labelled `ticket`.
2. Read the request in full. If it's an issue or spec reference, fetch it with its comments.
3. Read `docs/agents/learnings.md`, then the parts of `docs/agents/architecture.md` and `docs/agents/glossary.md` the request touches. Explore that code too, so tickets use the glossary's terms and fit the structure.

## Ask until the goal is clear

If the goal, a constraint or "what counts as done" is unclear, ask one question at a time, leading with your recommended answer. Stop asking once you could write completion conditions a stranger could test. Don't invent requirements; anything you assume goes into the plan as an assumption the Owner can correct.

## Draft the tickets

Cut the work into **vertical slices**: each one goes through every layer it needs (data, logic, interface, tests), can be shown working on its own, and fits one fresh session.

- Put any prefactoring first, as its own ticket: make the change easy, then make the easy change.
- A wide mechanical change (a rename across the codebase) is the exception: expand (add the new form beside the old), migrate callers in batches, then contract (remove the old form), one ticket each.

Write every ticket with [ticket-template.md](ticket-template.md):

- **Goal:** one or two sentences on what becomes possible.
- **Done when:** numbered conditions, each tied to a test or a re-runnable command. A condition nobody can check isn't a condition.
- **Depends on:** the tickets that must merge first.
- **Scope:** the paths it's expected to change.

Add the Level 2 fields only for guardrails listed in the harness file: test IDs for the done-when conditions, serial resources, append-only files, screenshots required.

A ticket that touches a sensitive area must have a done-when condition that covers it. If you can't write one, that's an open question for the Owner.

## Present, then write

1. Show the Owner a numbered list: title, depends on, what it delivers, scope. Mark which tickets can run in parallel: no dependency between them and no overlapping scope.
2. Ask whether the granularity, order and conditions are right. Change the plan until the Owner approves it.
3. Only then write the tickets where the harness file says, in its document language: issues labelled `ticket`, with "Blocked by #<n>" lines for dependencies, or `docs/tickets/<id>.md` files.
4. If the Owner decided something along the way, add it to `docs/decisions.md` when the project keeps one.
5. If planning settled a new term or adds, removes or moves a module, update `docs/agents/glossary.md` or `docs/agents/architecture.md` in the same change.

## Don't

- Don't write product code or tests while planning.
- Don't decide a data-model or public-interface change the request didn't ask for: raise it with the `ask-owner` skill.
- Don't write anything to the tracker before the Owner approves the list.
