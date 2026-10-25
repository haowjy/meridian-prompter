---
name: skill-artifacts
type: reference
description: >
  Load when writing or reviewing skills: the directory shape, the
  loading and invocation fields, types, and how skills appear to agents.
model-invocable: true
---

# Skill Artifacts

`/prompt-principles` `resources/skill-level.md` covers how to design a skill.

## The Directory

A skill is a directory under `skills/` with a `SKILL.md` and optional `resources/`, `scripts/`, and `assets/`. The frontmatter holds `name`, `type`, `description`, and the invocation fields; the body is what loads. The [mars skill compilation reference](https://github.com/meridian-flow/mars-agents/blob/main/docs/config/skill-compilation.md) has the full schema and how each harness receives it.

## Loading and Invocation

- **`load`** in an agent profile puts the skill's full text in that agent's system prompt every run, on every harness, whatever its `model-invocable`. A skill with `model-invocable: false` under one agent's `load` is how you give that agent a skill no model finds or loads by itself.
- **`available`** in an agent profile lists the skill for the agent to load itself. The runtime lists every model-invocable skill with its description, which is what the agent reads to decide; it can also call attention to that agent's available skills by name and type.
- **Caller-attached** skills arrive at delegation time the same way `load` does, whatever the agent's own lists say. A caller learns what it can attach from the agent's description.
- **`model-invocable`** (default `true`) puts the skill in the runtime's skill list, where any model can find and load it by itself. `false` takes it off that list: `load` and caller attachment still deliver it in full, but an `available` listing of it is a name the agent can't load. Every model-invocable skill costs description tokens on every turn, so keep that pool small.
- **`user-invocable`** (default `true`) lets the human trigger the skill with `/name`.

A loaded skill arrives headed `# Skill: /<name>` with a line saying its text is already loaded, so a body can tell the agent to follow `/<name>` even when the harness's skill list omits it.

## Types

Set `type:` to declare the skill's role: `principle` for always-loaded thinking guidance, `guardrail` for always-loaded safety boundaries, `mode-shift` for on-demand shifts in activity, `checkpoint` for phase gates, `reference` for operational how-to. The runtime groups listed skills by type and prints the type's one-line header above each group of loaded skills (`principle`: "Override other guidance when loaded."; `reference` gets none), so pick the type whose header holds for the skill.
