---
name: prompt-review
description: "Load when an agent, skill, or prompt needs strict review, to find its failure modes and rank them by severity."
model-invocable: false
metadata:
  type: reference
---

# Prompt Review

Review prompt quality first, with `/prompt-principles` and `/llm-writing` as the lens. Read the `/prompt-principles` resources for what you're reviewing: `resources/agent-level.md` or `resources/skill-level.md`, and `resources/system-level.md` for leads and multi-agent flow. Load `/agent-artifacts` or `/skill-artifacts` to check the package format and runtime.

These prompts run on strong models that already do most work well, so every line has to earn its words. A finding names a run that is likely, not merely possible, where a strong model given the prompt as written does something the owner would care about, and a fix worth its words. Quote the exact text and propose the edit; a deletion counts as a finding as much as an addition. A fix that adds a condition or caveat for a rare case usually costs more than the case: list those in one line each under "Considered, not worth a line." Rank by how much each finding changes behavior.

After the prompt-quality pass, do a lighter mechanics pass with `resources/mechanics.md`.

## Report

Start with a short overall assessment. Then list the findings with the severity of each. End with a verdict: approve, approve with notes, or request changes.
