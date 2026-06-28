---
name: prompt-principles
type: principle
description: >
  Load when writing or reviewing prompts, skills, or agents. Gives the
  core heuristics for writing prompts that steer LLM behavior reliably.
model-invocable: true
---

# Prompt Principles

Use this skill to write prompts that keep the target behavior obvious, cut irrelevant context, and give the model reasons it can apply.

Use `/llm-writing` alongside this skill.

## Write for an Agent

Write for an agent, not a human teammate. An agent sees a frozen prompt and a bounded context window. It will not reliably infer which parts are foundational, optional, or incidental unless the prompt makes that hierarchy clear. Make the task, boundaries, and success criteria clear. Use structure and placement to keep the governing instructions easy to find.

Context is not free. Cut repeated summaries, stale history, decorative explanation, and edge-case policy that does not apply. Keep what changes behavior: the task, constraints, governing reasoning, relevant artifacts, and checks for success. Give a brief reason when it helps the model apply the rule.

## Use Progressive Disclosure and Keep Focus

Keep the loaded layer dense and high-signal, then push depth into skills and resources. The body should carry the operating frame that must stay active every run. Resources should carry deeper variants, examples, and mechanics. Extract reusable knowledge into skills. Keep single-agent-specific method in the agent body. Split agents by cognitive mode when the work needs a different frame, a different model, or a fresh context window.

Use headers, sections, XML tags, and visible grouping when they help separate purpose, constraints, workflow, and routing. Prefer direct statements of what to do. Use negatives mainly for bright-line prohibitions.

## Make Scope and Success Easy to Verify

Name explicit artifacts. Say what the agent should produce. State what success looks like. When independence matters, verify in a separate spawn.

## When to Load the Deeper Resources

Load `resources/prompt-level.md` for prompt text, attention, structure, and explanation. Load `resources/skill-level.md` for skill boundaries, loading, and progressive disclosure. Load `resources/agent-level.md` for agent role, boundary, description, and cognitive mode. Load `resources/system-level.md` for handoffs, verification, model staffing, and multi-agent coordination.
