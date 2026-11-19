---
name: retro
description: Look back over recent work, find the mistakes that keep coming back, and propose for each one a rule and what should enforce it, from a test or lint rule to a hook, CI check or doc line. Also check whether any guardrail can now be retired. Proposes only; the Owner decides.
disable-model-invocation: true
argument-hint: "<optional: the period or PRs to look at>"
---

# Retro

## 1. Gather

1. Read `docs/agents/harness.md`: the level, the "Guardrails" list and the document language. If it's missing, suggest `/setup` once and continue.
2. Collect from the period (default: since the last retro, or the last 20 merged PRs):
   - verdicts, especially FAIL reasons and which fix round passed;
   - escalations to the Owner and how they were answered;
   - PR review comments and CI failures;
   - learning proposals from verdicts and hand-off notes, and `docs/agents/learnings.md`;
   - `docs/decisions.md`, when the project keeps one.

## 2. Find what repeats

Group the findings by cause, not by symptom. Keep only causes seen at least twice; a one-off is noise. For each, note the occurrences with links.

## 3. Propose a rule and an enforcer

For each repeated cause, propose one rule and the cheapest enforcer that would have stopped every occurrence:

| Enforcer | Use it when |
| --- | --- |
| A test | The mistake is wrong behaviour in the product |
| A lint or type rule | The mistake has a recognisable shape in code |
| A hook | It must never happen in a session, whatever the agent intends |
| A CI check or guardrail recipe | It must never reach `main` |
| A line in a skill or AGENTS.md | It needs judgement, so no mechanism fits |

Prefer the higher rows: prose is the last resort, not the first.

## 4. Check what can be retired

For each guardrail and hook in use, read its "When to remove" note. If the evidence it names is there (it hasn't fired in a long time, or something stronger now covers the same rule), propose removing it.

## 5. Present

Show the Owner one table in the document language, with one row per proposal: cause, occurrences, proposed rule, enforcer, cost, and "add" or "remove". Ask which to accept.

Apply only accepted proposals, each through a normal pull request. Add accepted learnings as new rows in `docs/agents/learnings.md`, and record decisions in `docs/decisions.md` when the project keeps one.

## Don't

- Don't change skills, rules, hooks or CI without the Owner's acceptance.
- Don't propose a rule for something that happened once.
