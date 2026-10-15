---
name: agent-artifacts
type: reference
description: >
  Load when writing or reviewing agent .md files. Covers agent artifact
  shape, frontmatter, and Meridian-specific agent conventions.
model-invocable: false
---

# Agent Artifacts

Use `/prompt-principles` for broader prompt design guidance. This skill covers how agent artifacts are structured in Meridian.

Agent definitions are markdown files with YAML frontmatter. The body below the frontmatter is the system prompt. For the full frontmatter schema, see the [mars agent profile reference](https://github.com/meridian-flow/mars-agents/blob/main/docs/config/agent-profiles.md).

Descriptions serve callers: they say when and why to launch or spawn the agent, what to pass, and what comes back. Keep summaries of what the agent does out of the description; they belong in the body and the package README. Bodies should stay caller-agnostic so the agent works from whatever context it receives, and harness-agnostic so they survive a harness swap — state intent, and leave CLI flags and tool mechanics to the environment (see `/prompt-principles`).

A lead's body says which work it does itself and which it delegates; leads that implement are as valid as leads that only coordinate.

Load `resources/meridian.md` for Meridian-specific subagent, handoff, staffing, and package-target conventions. Load `resources/model-policies.md` for fallback patterns that keep agents usable across different model availability.
