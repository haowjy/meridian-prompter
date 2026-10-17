---
name: agent-artifacts
type: reference
description: "Load when writing or reviewing Meridian agent .md files: the file format, what callers see, what Meridian injects, how context reaches a spawn, models, and permissions."
model-invocable: true
---

# Agent Artifacts

## The File

An agent is a markdown file with YAML frontmatter; the body below the frontmatter is the system prompt. The [mars agent profile reference](https://github.com/meridian-flow/mars-agents/blob/main/docs/config/agent-profiles.md) has the full schema. Agents live in source package repos, and `meridian mars sync` copies them into harness targets (`.claude/`, `.codex/`, `.opencode/`, `.cursor/`, `.pi/`). Edit the source, since sync overwrites the targets; some differences between harnesses come from sync and target mechanics, not from the source file.

## What a Caller Sees

A caller picks an agent from an inventory in its own system prompt: one line per agent with its name, description, default model, and declared backups, so the description is the only text a caller routes on. Name the skills a caller can attach for focus in it (`@reviewer`: "Attach skills for focus: …"). The model sits beside the description, so an agent whose name or description advertises its model gets picked for the model; describe the work.

## What Meridian Injects

Every agent receives pointers to work items (`meridian work`), its source-edit directory versus its work directory, past session transcripts (`meridian session`), and the context roots (work, KB) as environment variables. Every spawned agent is also told it is a subagent and that its final message is its report, with a default list of what the report holds. An agent whose profile lists subagents also receives the agent inventory, briefing guidance (what a brief carries and leaves open, `--skills`, `-m`, `--from`, `--task-dir`), and the spawn mechanics (background launch, waiting for results).

Bodies and skills don't restate any of this. They say what to delegate and what to pass; the injected guidance carries the how, and it changes with Meridian, so a copy in a prompt goes stale.

## How Context Reaches a Spawn

A spawn starts with its system prompt (body, loaded skills, injected guidance) and its prompt, plus files passed with `-f` and transcripts passed with `--from`; an earlier spawn passed with `--from` brings its report. `--from` supplies framing and rationale; concrete scope still comes from `-f` files and the prompt. A directory passed with `-f` gives the spawn a map of the tree, so a brief can pass the structure and name the few files whose content matters. It can read the work directory, the KB, the source, and past sessions on its own. Nothing else from the caller's conversation reaches it. Its final message is the report the caller reads back; the body says what that report holds when it differs from Meridian's default.

## Models

A profile sets the default model, declared backups (automatic fallbacks when a model is unavailable), and per-model policies such as effort or `no-fallback`. Callers override with `-m`. Fallbacks are decided per agent: a model can be an automatic backup in one agent and explicit-only in another. When you add a model to an agent's policies, mark it `no-fallback: true` unless the human decided it belongs among that agent's backups.

Load `resources/model-policies.md` for fallback patterns that keep agents usable across different model availability. `meridian mars models list` shows the live catalog, and `meridian mars models prompting <model>` gives model-specific prompting guidance.

## Harnesses and Permissions

One profile runs on Claude, Codex, or OpenCode. Its `tools` and `sandbox` fields decide what the agent can do, and they hold where a sentence in the body only asks: `edit: deny` removes the edit tools that "never edit" in the body only asks the agent not to use, but an agent with `bash: allow` can still write through the shell; a read-only sandbox is what stops writes. Harnesses enforce them differently. Codex's workspace sandbox blocks network access and writes outside the workspace. Web search and fetch go through the harness's built-in tools (`web: allow`), which need no local network; shell web tools that call local services or write caches outside the workspace fail there. An agent that clones repositories needs `bash: allow` and `sandbox: danger-full-access`. `meridian.toml` (`[spawn].deny_headless_harnesses`) and hooks can restrict spawns outside the profile; check both before concluding the frontmatter explains an agent's behavior.
