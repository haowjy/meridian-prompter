---
name: skill-artifacts
type: reference
description: >
  Load when writing or reviewing skills. Design guidance for SKILL.md
  files, loading mechanics, and bundled resources.
model-invocable: false
---

# Skill Artifacts

Skills are shared knowledge loaded into agents. Each skill is a directory
under `skills/` with a `SKILL.md` and optional `resources/`, `scripts/`,
and `assets/` subdirectories.

## Loading Mechanics

Three levels determine when and how a skill reaches an agent:

- **`load`** — always in context. Use for skills the agent needs every run.
  Principle and guardrail skills belong here.
- **`available`** — name visible to agent, content loaded on demand. The
  agent sees the skill name and can invoke it when relevant. This is the
  primary discovery mechanism — body text references and available lists
  are how agents find skills.
- **`model-invocable`** — globally discoverable by keyword match. Required
  for `available` to work (it's the loading mechanism). Without
  model-invocable, an available skill is a name the agent can see but
  never load.

**Practical reality:** global model-invocable discovery without an
available-list nudge rarely works. Too many model-invocable skills dilutes
keyword matching. Design for the available list as the primary trigger,
model-invocable as the enabling mechanism.

**Defaults:**
- Most skills: `model-invocable: true` (enables the loading mechanism)
- Load-only skills that are never available: `model-invocable: false`
  (no reason to pollute the global pool)
- Keep the global model-invocable pool as small as practical

## Skill Types

Set `type:` to declare the skill's role. Type controls injection order —
principles load first (highest attention), guardrails second, references
last.

| Type | Role | Loading pattern |
|---|---|---|
| `principle` | Shapes HOW the agent thinks | Always loaded |
| `guardrail` | Safety boundary | Always loaded |
| `mode-shift` | Pivots WHAT the agent is doing | Available, loaded on demand |
| `checkpoint` | Gates a phase transition | Available, loaded at boundaries |
| `reference` | Operational how-to | Available, loaded when needed |

**Mode-shift skills** are the alternative to spawning a new agent. When the
cognitive shift stays within the same model's capability and doesn't need
fresh context, a skill is cheaper than a spawn. `/handoff` shifts to
transition mode. `/prototype` shifts to throwaway exploration. Same agent,
different lens. When the shift needs a different model or fresh attention
budget, spawn instead.

## Structure

Descriptions lead with when to load the skill, not what it contains.

Keep the body under 100 lines. Put deep or variant-specific content in
`resources/` and route to it from the body. Decompose aggressively —
agents should pick up only the knowledge they need, not the entire skill's
domain.

## When to Add Scripts

Add `scripts/` when an operation is deterministic — validation, formatting,
transformation. Scripts execute without loading into context and produce
reliable results. Same code generated repeatedly by agents is a sign it
should be a script instead.

## When to Split into Resources

Split when:
- SKILL.md exceeds ~100 lines of instructional content
- Content addresses distinct variants (frameworks, platforms)
- Advanced features are rarely needed by most consumers

Each resource file should be independently useful — loadable without
requiring other resources from the same skill.
