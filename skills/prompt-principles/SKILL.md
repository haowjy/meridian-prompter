---
name: prompt-principles
type: principle
description: "Load when writing or reviewing prompts, skills, or agents: the heuristics that make a prompt steer LLM behavior reliably."
model-invocable: true
---

# Prompt Principles

Use `/llm-writing` alongside this skill.

## Write for an Agent

An agent sees a frozen prompt and a bounded context window. It will not reliably infer which parts are foundational, optional, or incidental unless the prompt makes that hierarchy clear. Make the task, boundaries, and success criteria explicit. Use structure and placement to keep governing instructions easy to find.

## Every Line Must Change Behavior

Test each line: does removing it change how the model behaves? If not, delete it. Models already know how to code, review, write tests, and follow instructions. Write only what steers the model away from its default or toward something non-obvious.

## Prescribe Only What Needs to Be Predictable

Detailed steps produce consistent behavior; use them when predictability matters. But prescription crowds out the model's judgment. When you want the model to think or adapt, state the goal and the reasoning, then let it work. The right amount of prescription depends on what the task needs, not on how thorough the prompt feels.

## Progressive Disclosure

The body carries what the agent needs every run. Resources carry depth it reaches when the task demands it. If something is situational, it belongs in a resource, not the always-loaded layer.

## Make Scope and Success Easy to Verify

Name explicit artifacts. Say what the agent should produce. State what success looks like. When independence matters, verify in a separate spawn.

## Keep the Core Harness-Agnostic

Load-bearing prompts — agent bodies, core skills — state intent: what to delegate, what context to pass, what the result must satisfy. Environment mechanics (CLI flags, tool names, launch commands) belong to the environment: the harness's own system prompt, or the tool's `-h`/help surface the agent reads at runtime.

The test: would this prompt survive a harness swap unchanged? "Spawn a researcher in the background and collect the result before your verdict" ports; a flag plus a wait command does not. Naming *what* to compose is intent, not mechanics: `@agent` references and skill attachments (`@coder --skills testing`) declare the staffing and survive the test. When mechanics must be written down, contain them in one skill so a new environment swaps that skill, not every agent.

## Deeper Resources

Load `resources/prompt-level.md` for prompt text, attention, structure, and explanation. Load `resources/skill-level.md` for skill boundaries, loading, and progressive disclosure. Load `resources/agent-level.md` for agent role, boundary, description, and cognitive mode. Load `resources/system-level.md` for handoffs, verification, model staffing, and multi-agent coordination.
