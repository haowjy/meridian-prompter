---
name: skill-artifacts
type: reference
description: >
  Load when writing or reviewing skills. Covers SKILL.md shape, loading
  mechanics, and how to structure bundled resources.
model-invocable: false
---

# Skill Artifacts

Use `/prompt-principles` for broader prompt design and loading strategy. This skill covers how skill artifacts are structured in Meridian.

A skill is a directory under `skills/` with a `SKILL.md` and optional `resources/`, `scripts/`, and `assets/` subdirectories. The description is the trigger surface. The body is the loaded instruction layer. `resources/` carry deeper content. `scripts/` are for deterministic operations that should run instead of being re-derived in context.

## Loading

Skills reach agents through four paths (see `/prompt-principles/resources/skill-level.md` for design guidance):

- **`load`**: always in the system prompt. Use for skills the agent needs every run.
- **`available`**: agent can self-load when `model-invocable: true`. Use for skills it may reach for on demand.
- **`description`**: caller discovery surface. List attachable skill names so parent agents know what to compose via `--skills`.
- **`--skills`**: caller injection at spawn time. Bypasses `available`; any bundled skill can be injected.

`model-invocable` defaults to true; an explicit `model-invocable: false` makes an `available` skill visible but not self-loadable (caller injection via `--skills` still works). Keep the global `model-invocable` pool small; each entry costs description tokens on every turn.

## Types

Set `type:` to declare the skill's role: `principle` for always-loaded thinking guidance, `guardrail` for always-loaded safety boundaries, `mode-shift` for on-demand shifts in activity, `checkpoint` for phase gates, `reference` for operational how-to.

## Descriptions

Descriptions should lead with *when to load* the skill, not just what it contains. The description is what an agent or orchestrator reads to decide whether to load. "Load when reviewing test architecture" beats "Covers test structure patterns."
