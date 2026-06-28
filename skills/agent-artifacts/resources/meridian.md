# Meridian Agent Conventions

This resource covers Meridian-specific agent conventions. Use `/prompt-principles` for the broader design principles behind them.

## Subagents and Spawns

Subagents should be caller-agnostic. They should work from the context they receive, not from assumptions about who spawned them. When a manager or lead delegates, prefer artifact outputs over response-only outputs so the result can survive compaction and be passed forward.

Use the CLI to discover where artifacts belong. `meridian work current` gives the active work directory. `meridian context work` gives the work context root. `meridian context kb` gives the knowledge base root.

Some spawn restrictions are enforced at the Meridian layer rather than in per-agent frontmatter. For example, `meridian.toml` can deny headless harnesses with `[spawn].deny_headless_harnesses`, and hooks can block generic or expensive spawn paths.

## Handoffs

Name specific files, not categories. Concrete `-f` paths make scope visible and reduce ambiguity. Pass enough overview to orient the spawn, but prefer a small set of explicit artifacts over broad context dumps. If critical context only lives in conversation, materialize it to a file before handing work off.

Use `--from <spawn-id>` when a spawn needs reasoning from an earlier spawn. Use `--from $MERIDIAN_CHAT_ID` when it needs framing or decisions from the primary session.

## Model Staffing

Match the model to the cognitive mode the agent needs. Put defaults in the agent profile. Use faster, faithful models for clear-goal execution, more interactive models for ambiguity handling, and stronger evaluative models for judgment-heavy review.

For broader model-to-cognitive-mode guidance, use `/prompt-principles/resources/agent-level.md`.

## Package Targets

Prompt packages can copy agents into official target surfaces such as `.claude`, `.codex`, `.opencode`, `.cursor`, and `.pi` through package target settings. When reviewing an agent artifact, remember that some behavior differences come from package sync and target-specific mechanics, not only from the source markdown file.
