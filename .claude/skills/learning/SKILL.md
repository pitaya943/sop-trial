---
name: learning
description: Optional review that helps the Owner understand and challenge what the agents did, rather than just accept it. The Owner answers four questions first; then the agent gives its own answers, compares, and records the result. Use only when the harness file turns Learning on or the Owner asks.
---

# Learning review

Only run this when `docs/agents/harness.md` says "Learning: on", or the Owner asks for it. If the harness file is missing, suggest `/setup` once; Learning then counts as off unless the Owner asks. Typical moments: after `/report`, or after an important decision.

## Steps

1. Pick the subject with the Owner: a report, a decision, or a piece of shipped work. Link it.
2. Ask the Owner to answer these four questions **first**, in their own words, in the document language:
   1. What was built, and why?
   2. Why this approach rather than the alternatives?
   3. Under what conditions does it break?
   4. What did you learn?
3. **Wait for the answers.** Don't show yours before the Owner has answered: the point is the Owner's own reasoning, not agreement with yours.
4. Then write your answer to each question, grounded in the subject's sources (PRs, verdicts, decisions). For each question, point out where the Owner's answer differs from yours.
   - A difference isn't automatically the Owner's mistake. Explain where it comes from, citing the sources, and say plainly when the Owner's answer is the better one.
5. Record the result where the Owner prefers: a comment on the report or tracking issue, or a dated section in `docs/learning.md` (append only). Include the Owner's final answers, the main differences, and what was concluded.

## Don't

- Don't answer the questions for the Owner, or hint at your answers before they reply.
- Don't treat the review as a test the Owner passes or fails.
