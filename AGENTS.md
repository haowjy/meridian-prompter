# meridian-prompter

Agents and skills for writing LLM prompts.

## Releasing

Use `mars version` (or `meridian -C "$PWD" mars version`) for releases:

```bash
mars version patch --push       # 0.1.2 → 0.1.3, commit, tag, push
mars version minor --push       # 0.1.3 → 0.2.0
```

This bumps `mars.toml`, promotes CHANGELOG.md `[Unreleased]` to the new version, commits, tags, and optionally pushes. Write changelog entries under `[Unreleased]` as you work — `mars version` handles the rest.

**Meridian session roots:** Meridian spawns resolve `MERIDIAN_TASK_DIR` for the
checkout where source work happens, but `MERIDIAN_PROJECT_DIR` stays anchored to
the session control root for state, profiles, and context. Nested
`meridian ...` commands use project-root resolution, so CWD alone may not target
this package. For package releases, pass the package root explicitly:

```bash
meridian -C "$PWD" mars version patch --push
```

Use explicit `-C <package-root>` whenever running Meridian commands for this
package from an inherited Meridian environment. For task checkouts, prefer
`meridian -C "$MERIDIAN_TASK_DIR" ...`.

## Agents

```
agents/
  prompt-dev.md            # Collaborative prompt writing sessions
  prompt-reviewer.md       # Adversarial review of prompts against principles
  prompt-tester.md         # Behavioral testing of agents against sample tasks
  python-tool-writer.md    # Writes Python scripts and tools
  web-prompt-researcher.md # Researches prompting papers and patterns
```

## Skills

```
skills/
  prompt-principles/    # Research-backed prompting principles (4 levels)
  agent-artifacts/      # Agent design guidance (schema in mars docs)
  skill-artifacts/      # Skill design guidance
  prompt-review/        # Adversarial review methodology
```

See `skills/prompt-principles/resources/research.md` for citations.
