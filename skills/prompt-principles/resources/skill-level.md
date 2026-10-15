# Skill-Level Principles

Skills hold reusable knowledge without bloating every agent that needs it.

## Extract for Reuse, Not for Tidiness

Move something into a skill when multiple agents need the same knowledge or method. If only one agent needs it, keep it in the body; one place to maintain. The test is whether multiple agents would get lighter and clearer if the content moved out.

## Loading Is Part of the Design

Skills reach agents through four independent paths, each serving a different audience:

- **`load`**: always in the system prompt. Reserved for knowledge the agent genuinely needs every run. Every loaded skill costs context on every turn.
- **`available`**: the agent can self-load mid-session when `model-invocable` is true. This is for the agent's own discovery: skills it might need but shouldn't pay for until it does.
- **`description`**: the caller's discovery surface. A parent agent reads child descriptions to learn what skills can be attached. List attachable skill names here so orchestrators know what to compose.
- **`--skills` (caller injection)**: a parent passes skills onto a subagent at spawn time. This bypasses `available` entirely; any bundled skill can be injected regardless of the agent's own configuration.

`available` and `--skills` serve different audiences. `available` is the agent looking inward ("what can I load myself?"). `--skills` is the caller reaching in from outside ("take this too"). They do not need to match.

When you know at agent definition time exactly which skills an agent needs, use `load`. When the skill is sometimes needed and the caller knows when, skip `model-invocable` and let the caller inject it with `--skills`.

## The Top Layer Should Route, Not Teach

The skill body should carry the core guidance and point to deeper resources. Examples, variants, long procedures, and edge-case mechanics belong in resource files. This keeps the always-loaded layer compact while preserving depth when the task actually needs it.

## Decompose So Agents Can Load Selectively

Split resources by real usage boundaries, not just by topic names. If two files are always loaded together, they probably want to be one file. If one file mixes several use cases, agents load irrelevant context just to reach the paragraph they need.

## Skills Teach; Agents Decide

Skills provide method, judgment criteria, vocabulary, and durable reference material. Agents apply that guidance to a concrete situation, make decisions, and produce outputs. When a skill starts owning decisions, it becomes a pseudo-agent. When an agent carries all shared method inline, it becomes bloated and hard to maintain.

## Separate Mechanism from Method

Keep tool operation separate from guidance about how to use the tool well. Mechanism is reusable across tasks; method depends on what the worker is trying to accomplish. When they are separate, a tool skill can support many methodologies and a methodology skill can survive a tool change.
