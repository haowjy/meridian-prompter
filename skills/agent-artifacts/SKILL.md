---
name: agent-artifacts
type: reference
description: "Load when writing or reviewing agent .md files, so frontmatter, descriptions, and what a lead does itself versus delegates follow Meridian's conventions."
model-invocable: false
---

# Agent Artifacts

Use `/prompt-principles` for broader prompt design guidance. This skill covers how agent artifacts are structured in Meridian.

Agent definitions are markdown files with YAML frontmatter. The body below the frontmatter is the system prompt. For the full frontmatter schema, see the [mars agent profile reference](https://github.com/meridian-flow/mars-agents/blob/main/docs/config/agent-profiles.md).

Descriptions serve callers: they should help someone decide when to use the agent and what to pass. Bodies should stay caller-agnostic so the agent works from whatever context it receives, and harness-agnostic so they survive a harness swap — state intent, and leave CLI flags and tool mechanics to the environment (see `/prompt-principles`).

A lead's body says which work it does itself and which it delegates; leads that implement are as valid as leads that only coordinate.

Before merging, deleting, or narrowing an agent, read its history (`git log -p` on its file). A different default model, a role the human asked for, or a job beyond what its body now says is a reason it exists; name each one in your proposal.

A model the human made an explicit option carries `no-fallback: true` in every agent that lists it. When you add a model to an agent's policies, check whether it is one of those.

Load `resources/meridian.md` for Meridian-specific subagent, handoff, staffing, and package-target conventions. Load `resources/model-policies.md` for fallback patterns that keep agents usable across different model availability.
