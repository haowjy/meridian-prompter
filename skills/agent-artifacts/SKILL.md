---
name: agent-artifacts
type: reference
description: >
  Load when writing or reviewing agent .md files. Covers agent artifact
  shape, frontmatter, and Meridian-specific agent conventions.
model-invocable: false
---

# Agent Artifacts

Use this skill for how agent artifacts are structured in Meridian. Use `/prompt-principles` for broader guidance on writing good prompts and shaping agent behavior.

Agent definitions are markdown files with YAML frontmatter. For the full frontmatter schema, see the [mars agent profile reference](https://github.com/meridian-flow/mars-agents/blob/main/docs/config/agent-profiles.md).

The frontmatter defines configuration. The body below it is the system prompt. Keep artifact mechanics here and broader prompt design in `/prompt-principles`.

Descriptions serve callers. They should help someone decide when to use the agent and what to expect. For broader description and body design, use `/prompt-principles` and its agent-level guidance.

Managers and leads coordinate through spawns. They should not implement directly. Some spawn restrictions are enforced outside the agent artifact itself, through Meridian config and hooks.

Load `resources/meridian.md` for Meridian-specific subagent, handoff, staffing, and package-target conventions. Load `resources/model-policies.md` for fallback patterns that keep agents usable across different model availability constraints.
