---
name: agent-artifacts
type: reference
description: >
  Load when writing or reviewing agent .md files. Design guidance for
  agent definitions and meridian-specific conventions.
model-invocable: false
---

# Agent Artifacts

Agent definitions are markdown files with YAML frontmatter. For the full
frontmatter schema, see the [mars agent profile reference](https://github.com/meridian-flow/mars-agents/blob/main/docs/config/agent-profiles.md).

The body below frontmatter is the system prompt. Opening matters most — it
survives compaction and gets strongest attention. Let skills carry
methodology the agent shares with others; the body carries what's unique
to this agent.

Descriptions serve callers, not the agent. Lead with the problem it solves
and when to reach for it, then teach how to use it effectively.

Managers and leads coordinate — they don't implement. Deny direct agent-tool
execution so `meridian spawn` stays the tracked execution path.

For meridian-specific conventions (subagent design, context handoffs, model
staffing), see `resources/meridian.md`.

For fallback patterns that keep agents usable on single-subscription setups,
see `resources/model-policies.md`.
