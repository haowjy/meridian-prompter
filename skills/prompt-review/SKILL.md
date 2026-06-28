---
name: prompt-review
type: reference
description: >
  Load when an agent, skill, or prompt needs strict review. Focuses on
  failure modes, severity, and clear feedback.
model-invocable: false
---

# Prompt Review

Review prompt quality first. Use `/prompt-principles` and `/llm-writing` as the default lens.

## What to Look For

Look for violations of the prompt, skill, agent, and system-level principles in `/prompt-principles`. Focus on high-leverage issues such as ambiguity, duplication, brittle instructions, weak routing, misplaced knowledge, and overloaded bodies. A good finding points to the exact text, explains the failure mode, and suggests a better direction.

After the prompt-quality pass, do a lighter mechanics pass when relevant. For that second angle, load `resources/mechanics.md`.

## Report

Start with a short overall assessment. Then list the findings and include the severity of each. End with a verdict: approve, approve with notes, or request changes.
