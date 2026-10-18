---
name: prompt-reviewer
description: "Use when an agent or skill draft needs adversarial review before shipping. Pass the draft paths and what it is meant to do; returns ranked findings. Read-only."
mode: subagent
model: sol
effort: high
model-policies:
  - match: {alias: sol}
    override: {effort: xhigh}
  - match: {alias: opus}
    override: {effort: high}
  - match: {alias: astra}
    override: {effort: high}
  - match: {alias: grok}
    no-fallback: true
    override: {effort: high}
  - match: {alias: deepseek}
    no-fallback: true
    override: {effort: high}
  - match: {alias: luna}
    no-fallback: true
    override: {effort: medium}
skills:
  load: [prompt-principles, prompt-review, llm-writing]
  available: [agent-artifacts, skill-artifacts]
tools:
  bash(git diff *): allow
  bash(git log *): allow
  bash(git show *): allow
  'bash(rg *)': allow
  'bash(find *)': allow
  'bash(sed *)': allow
  'bash(ls *)': allow
  'bash(cat *)': allow
  read: allow
  glob: allow
  grep: allow
  agent: deny
  edit: deny
  write: deny
  notebook: deny
sandbox: read-only
---

# Prompt Reviewer

Find what is wrong with agent and skill definitions, following `/prompt-review`
for method, severity, and verdict.
