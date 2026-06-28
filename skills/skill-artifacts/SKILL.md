---
name: skill-artifacts
type: reference
description: >
  Load when writing or reviewing skills. Covers SKILL.md shape, loading
  mechanics, and how to structure bundled resources.
model-invocable: false
---

# Skill Artifacts

Use this skill for how skills are structured in Meridian. Use `/prompt-principles` for broader guidance on prompt design, progressive disclosure, and when knowledge belongs in a skill.

A skill is a directory under `skills/` with a `SKILL.md` and optional `resources/`, `scripts/`, and `assets/` subdirectories.

The description is the trigger surface. The body is the loaded instruction layer. `resources/` carry deeper content. `scripts/` are for deterministic operations that should run instead of being re-derived in context.

Use `load` for skills an agent needs every run. Use `available` for skills it may reach for on demand. Use `model-invocable` when on-demand loading should actually work. An `available` skill without `model-invocable` is visible but not loadable. Keep the global model-invocable pool small. Design around `available` as the primary trigger.

Set `type:` to declare the skill's role. Use `principle` for always-loaded thinking guidance, `guardrail` for always-loaded safety boundaries, `mode-shift` for on-demand shifts in activity, `checkpoint` for phase gates, and `reference` for operational how-to.

Descriptions should lead with when to load the skill, not just what it contains. Keep the body short and route depth into `resources/`. Split resources by real usage boundaries so agents can load only what they need. Add `scripts/` when execution is better than prompt instructions.

For broader guidance on progressive disclosure, body versus resource boundaries, and when to split work into a skill instead of an agent, use `/prompt-principles` and its skill-level guidance.
