---
name: prompt-principles
type: principle
description: >
  Load when writing, reviewing, or improving any prompt artifact.
  Research-backed principles across four levels: prompt craft, skill
  extraction, agent design, and multi-agent coordination.
model-invocable: false
---

# Prompt Principles

Principles for writing effective prompts. See `resources/research.md` for citations where available.

Four levels of prompt design, each with distinct concerns. Load the relevant reference when working at that level.

## Prompt-Level

How to write the text of a prompt. Attention is finite.

- **Be concise, expand for emphasis** — Default to short what and why. When something matters, repeat it or explain it more.
- **Primacy and recency** — Beginning and end get strongest attention; middle gets lost. Put purpose and constraints up front, critical reminders at the end.
- **Structure over emphasis** — XML tags, headers, and clear sections outperform ALL CAPS and "MUST".
- **Positive framing** — Tell the model what TO do, not what to avoid. Positive language directs attention to target behavior; negative instructions keep prohibited behavior in attention and often produce acknowledgments ("we won't do X") instead of omission.
- **Hard boundaries are exceptions** — Negatives work for bright-line prohibitions on protected resources: "Don't modify .agents/" or "Never commit secrets."
- **Explain why** — Reasoning transfers to novel cases. The model applies principles to new situations when it understands the underlying logic.
- **Right altitude** — Behavioral heuristics, not brittle if-then rules or vague hand-waving. Tell the model what to do, when, and why — trust it to sequence.
- **Repetition improves compliance** — Restate key principles at opening and closing of the same artifact. Keep repetition within artifacts; skills are already loaded into context.
- **Escape hatches get used** — Optional easier paths become de facto defaults. If the hard path is the right path, don't offer an easier one.
- **Every word carries decision weight** — If removing a word doesn't change what the model does, cut it. Filler dilutes the words that matter.

See `resources/prompt-level.md` for detail.

## Skill-Level

When to extract shared knowledge into a skill vs keeping it in an agent body.

- **Reuse threshold** — If 2+ agents need the same knowledge, extract to a skill. If only one agent uses it, keep it in the body.
- **Loading mechanics** — `load` (always in context), `available` (name visible, loaded on demand), `model-invocable` (enables the loading mechanism). Available-list nudges are the primary discovery mechanism; global keyword matching alone rarely works.
- **Skill types** — `principle` (shapes thinking, always loaded), `guardrail` (safety, always loaded), `mode-shift` (pivots activity, on demand), `checkpoint` (gates transitions), `reference` (how-to, on demand).
- **Decompose for progressive loading** — Body routes to resources. Each resource independently useful. Agents pick up only the arteries they need.
- **Skills shape, agents act** — Skills provide knowledge and methodology. They don't run independently or make decisions.
- **Separate mechanism from methodology** — A skill is either how to operate a tool or what to do with it, not both. Separation enables reuse across use cases.

See `resources/skill-level.md` for detail.

## Agent-Level

How to design a single agent's role and prompt.

- **Light bodies, fat skills** — Agent bodies define the cognitive highway (which lane of thinking). Skills carry the knowledge that feeds it. Keep bodies thin; make skills fat and decomposed.
- **Single focus** — Each agent does one job well. Context window is the attention budget; multiple responsibilities compete for it.
- **No role identity** — Skip personas ("you are a senior engineer"). PRISM research shows personas interfere with knowledge retrieval. Describe behavior directly.
- **Route by cognitive mode** — Decompose agents by thinking type (faithful execution vs aesthetic judgment vs ambiguity handling), not by file type or domain. The model shapes the highway — its personality biases bend the cognitive lane toward dialogue, execution, or deep analysis.
- **Agent vs skill for cognitive shifts** — Different model needed or fresh context needed → new agent. Same model, current context works → mode-shift skill.
- **Descriptions serve callers** — Teach usage: when to use, how to invoke, what to pass, how to prompt, what to expect.
- **Generic over specialized** — If specialization lives entirely in the caller's prompt, keep the agent generic. One @browser beats three domain-specific browser agents.

See `resources/agent-level.md` for detail.

## System-Level

How to coordinate multiple agents.

- **Agent management pattern** — Managing agent spawns sub-agents, evaluates output, drives convergence. Described by its domain job, not coordination mechanism. Sub-agents execute focused tasks, don't coordinate with each other.
- **Context handoff is caller's job** — Pass structured briefing (objectives, constraints, decisions, evidence), not raw history. ~2% context loss per handoff with naive approaches.
- **External verification required** — Self-critique without external tools (tests, compilers, search) doesn't work. Reviewer must be separate from implementer.
- **Loop guards are external** — The system enforces termination, not the agent. Max iterations (15-25 typical), convergence detection, explicit deferral as valid exit.
- **Start simple** — Default to single agent. Add multi-agent only when evidence shows complexity delivers proportional value.
- **Explicit handoff content** — Name specific artifacts (file paths) at every handoff, not categories. "Implement per `design/spec/auth.md`" beats "based on the design."
- **Verify alignment at narrowings** — Pipeline hourglass: wide design → narrow plan → wide implementation. Verify coverage at each narrowing before scope loss compounds.
- **Match model to cognitive mode** — Clear-goal execution, ambiguity handling, and nuanced judgment need different models. Mismatches waste cost or produce shallow output.

See `resources/system-level.md` for detail.

