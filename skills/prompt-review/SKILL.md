---
name: prompt-review
type: reference
description: "Load when an agent, skill, or prompt needs strict review, to find its failure modes and rank them by severity."
model-invocable: false
---

# Prompt Review

Review prompt quality first. Use `/prompt-principles` and `/llm-writing` as the default lens.

## What to Look For

Apply the prompt-text principles in the `/prompt-principles` body to every line. Read its three level resources before reviewing:

- `resources/skill-level.md`: loading model, extraction, decomposition
- `resources/agent-level.md`: cognitive mode, body focus, reuse
- `resources/system-level.md`: handoffs, verification, what leads delegate

Review against each layer that applies. Focus on high-leverage issues: no-op lines, misplaced knowledge, overloaded bodies, weak routing, brittle prescription, and missing reasons. A good finding points to the exact text, explains the failure mode, and suggests a better direction.

After the prompt-quality pass, do a lighter mechanics pass when relevant. For that second angle, load `resources/mechanics.md`.

## Report

Start with a short overall assessment. Then list the findings and include the severity of each. End with a verdict: approve, approve with notes, or request changes.
