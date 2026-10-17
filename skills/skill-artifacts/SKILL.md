---
name: skill-artifacts
type: reference
description: >
  Load when writing or reviewing Meridian skills: the directory shape, the
  loading and invocation fields, types, and how skills appear to agents.
model-invocable: true
---

# Skill Artifacts

`/prompt-principles` `resources/skill-level.md` covers how to design a skill.

## The Directory

A skill is a directory under `skills/` with a `SKILL.md` and optional `resources/`, `scripts/`, and `assets/`. The frontmatter holds `name`, `type`, `description`, and the invocation fields; the body is what loads. The [mars skill compilation reference](https://github.com/meridian-flow/mars-agents/blob/main/docs/config/skill-compilation.md) has the full schema and how each harness receives it.

## Loading and Invocation

- **`load`** in an agent profile puts the skill in that agent's system prompt every run.
- **`available`** in an agent profile lists the skill for the agent to load itself. The harness lists every model-invocable skill with its description, which is what the agent reads to decide; Meridian also lists the agent's available skills by name, grouped by type and marked not yet loaded, to draw attention to them.
- **`--skills`** attaches skills at spawn time, whatever the agent's own lists say. A caller learns what it can attach from the agent's description.
- **`model-invocable`** (default `true`) lets the model see and load the skill itself. `false` keeps an `available` skill out of the model's reach; attaching with `--skills` still works. Every model-invocable skill costs description tokens on every turn, so keep that pool small.
- **`user-invocable`** (default `true`) lets the human trigger the skill with `/name`.

## Types

Set `type:` to declare the skill's role: `principle` for always-loaded thinking guidance, `guardrail` for always-loaded safety boundaries, `mode-shift` for on-demand shifts in activity, `checkpoint` for phase gates, `reference` for operational how-to. Meridian groups listed skills by type and prints the type's one-line header above each group of loaded skills (`principle`: "Override other guidance when loaded."; `reference` gets none), so pick the type whose header holds for the skill.
