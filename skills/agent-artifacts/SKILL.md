---
name: agent-artifacts
type: reference
description: "Load when writing or reviewing Meridian agent .md files: the package format, what callers see, what Meridian supplies, how context reaches a delegated agent, models, and permissions."
model-invocable: true
---

# Agent Artifacts

## The File

An agent is a markdown file with YAML frontmatter; the body below the frontmatter is the system prompt. The [Mars agent profile reference](https://github.com/meridian-flow/mars-agents/blob/main/docs/config/agent-profiles.md) has the full schema. Agents live in source package repos, and package sync compiles them into harness targets. Edit the source, since sync overwrites generated targets; some differences between harnesses come from compilation and target mechanics, not from the source file.

## What a Caller Sees

A caller picks an agent from an inventory in its own system prompt: one line per agent with its name, description, default model, and declared backups, so the description is the only text a caller routes on. Name the skills a caller can attach for focus in it (`@reviewer`: "Attach skills for focus: …"). The model sits beside the description, so an agent whose name or description advertises its model gets picked for the model; describe the work.

## What Meridian Supplies

Meridian supplies every agent with pointers to the work item, its source
checkout versus its work directory, past sessions, and context roots such as
the work directory and KB. It also tells every delegated agent that its final
message is its report, with a default list of what the report holds. An agent
whose profile lists subagents receives the agents it can use, briefing guidance,
and the mechanics for delegation and result collection. Other runtimes may
differ.

Bodies and skills don't restate any of this. They say what to delegate and what
to pass; Meridian supplies the how, so a copy in a prompt goes stale.

## How Context Reaches a Delegated Agent

A delegated agent starts with its system prompt (body, loaded skills, injected
guidance), task brief, files the caller passes, and any prior run the caller
carries. A carried prior run contributes its report. Past sessions supply
framing and rationale; concrete scope still comes from the brief and passed
files. The agent can read the work directory, the KB, the source checkout, and
past sessions through the capabilities Meridian supplies. Nothing else from the
caller's conversation reaches it automatically. A skill its profile loads is in
that system prompt in full even when the harness's skill list leaves it out
(`model-invocable: false`), so the body can name it as `/<name>`. Its final
message is the report the caller reads back; the body says what that report
holds when it differs from Meridian's default.

## Models

A profile sets the default model, declared backups (automatic fallbacks when a model is unavailable), and per-model policies such as effort or `no-fallback`. Callers can override the model. Fallbacks are decided per agent: a model can be an automatic backup in one agent and explicit-only in another. When you add a model to an agent's policies, mark it `no-fallback: true` unless the human decided it belongs among that agent's backups.

Load `resources/model-policies.md` for fallback patterns that keep agents usable across different model availability. Check the live model catalog and model-specific prompting guidance before choosing or changing a model.

## Harnesses and Permissions

One profile runs on Claude, Codex, OpenCode, Pi, or Cursor. Its `tools`,
`sandbox`, and `network` fields are the portable policy; a sentence in the body
only asks. `edit: deny` removes edit tools, but `bash: allow` can still write
through the shell, so use `sandbox: read-only` to stop shell writes. `network`
governs shell network separately: `allow`, `deny`, or `allowlist` with
`network-allow` and `network-deny` host sets. When it is unset, sandboxed
profiles are offline and `danger-full-access` profiles are online. Only Claude
and Codex enforce `sandbox` and `network`: Claude's deny still leaves loopback
reachable, Codex leaves localhost reachable through its proxy, and Codex cannot
put a read-only sandbox online. OpenCode, Pi, and Cursor enforce neither, so
their shells keep full filesystem and network access whatever the profile says.
Web search and fetch through `web: allow` do not need shell network.

Meridian automatically grants its read-only and lifecycle commands under Bash
allowlists, and grants delegation commands when a profile declares `subagents`.
Preview what a profile actually gets with the runtime's launch dry-run before
trusting the frontmatter. When a delegated agent lacks access, check the
runtime's sandbox and network floor before changing the profile; project
configuration and hooks can restrict a run further.
