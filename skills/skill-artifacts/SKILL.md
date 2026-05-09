---
name: skill-artifacts
type: reference
description: >
  Load when writing or reviewing skills. Design guidance for SKILL.md
  files and bundled resources.
model-invocable: false
---

# Skill Artifacts

Skills are reference material loaded into agents. Each skill is a directory
under `skills/` with a `SKILL.md` and optional `resources/`, `scripts/`,
and `assets/` subdirectories.

Descriptions lead with when to load the skill, not what it contains. Most
skills should set `model-invocable: false` — only exempt skills that serve as
safety nets an agent might need to discover mid-task.

Set `type:` to control injection order — `principle` loads first (highest
attention), `guardrail` second (safety boundaries), `reference` last
(operational how-to). Omit for skills where order doesn't matter.

Keep the body under 500 lines. Put deep or variant-specific content in
`resources/` and route to it from the body.
