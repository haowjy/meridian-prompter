---
name: prompt-review
description: "Load when an agent, skill, or prompt needs strict review, to find its failure modes and rank them by severity."
model-invocable: false
metadata:
  type: reference
---

# Prompt Review

Review prompt quality first, with `/prompt-principles` and `/llm-writing` as the lens. Read the `/prompt-principles` resources for what you're reviewing: `resources/agent-level.md` or `resources/skill-level.md`, and `resources/system-level.md` for leads and multi-agent flow. Load `/agent-artifacts` or `/skill-artifacts` to check the package format and runtime.

A good finding quotes the exact text, describes the run where it goes wrong, and suggests a better direction. Rank by how much it changes behavior, not by style.

After the prompt-quality pass, do a lighter mechanics pass with `resources/mechanics.md`.

## Report

Start with a short overall assessment. Then list the findings with the severity of each. End with a verdict: approve, approve with notes, or request changes.
