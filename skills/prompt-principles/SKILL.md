---
name: prompt-principles
type: principle
description: "Load when writing or reviewing prompts, skills, or agents: the heuristics that make a prompt steer LLM behavior reliably."
model-invocable: true
---

# Prompt Principles

Use `/llm-writing` alongside this skill.

## Write for an Agent

An agent sees a frozen prompt and a bounded context window. It will not reliably infer which parts are foundational, optional, or incidental unless the prompt makes that hierarchy clear. Make the task, boundaries, and success criteria explicit: name the artifacts it produces and what success looks like. When independence matters, verify in a separate spawn.

Placement and structure carry the hierarchy. The opening gets the strongest attention and the close the second-strongest, so put purpose and the main constraint first and the reminder that matters most last; an instruction buried in the middle loses to local wording. Separate kinds of information with headers, XML tags, and short sections. Structure works where ALL CAPS, repeated "must," and emotional emphasis only add force.

## Every Line Must Change Behavior

Test each line: does removing it change how the model behaves? If not, delete it. Models already know how to code, review, write tests, and follow instructions. Write only what steers the model away from its default or toward something non-obvious: prompt text steers behavior rather than narrating process. Words that change nothing dilute the words that do.

## Say What to Do

State the target behavior. Positive framing keeps the desired behavior in view; negative framing keeps the forbidden behavior active in attention. Use negative phrasing for bright-line prohibitions, where ruling something out is the whole point.

## Give the Reason

Explain why when the reason helps the model apply the instruction in cases the prompt doesn't spell out. A rule without a reason is easy to follow mechanically and easy to misapply. Reasons matter most for tradeoffs, where two good principles pull apart and the model has to choose which governs.

## Prescribe at the Right Altitude

Detailed steps produce consistent behavior; use them where predictability matters. Elsewhere, state what to optimize for, when it applies, and what failure it prevents, then let the model work. Over-sequenced prompts turn brittle and invite cargo-cult execution; under-specified ones leave too much to interpretation. Good prompt text gives a usable decision rule.

## State Instructions Flat

Every condition costs reliability: the model must first decide whether it fired, and it misses conditional constraints far more often than plain ones. A fallback plants its case ("if in doubt, use X" overtriggers X), and LLM drafts add conditions by reflex.

State the default as a directive. Keep a condition only when the instruction is wrong on the other side and both sides occur, and make its trigger checkable; a condition the agent can't check ("when you think it's done," "as needed") gets guessed, usually conveniently. Delete fallbacks for cases the agent's role rules out. If the thorough path is right, make it the only path: a weaker option offered beside it becomes the default. Before cutting a condition, read the flat version as an instruction that always fires: "probe to settle findings" makes a reviewer probe a finding about file size.

## Use Leading Words

A leading word recruits a concept the model already holds, in fewer tokens than explaining it: "adversarial," "throwaway," "regression," "proof of concept." When three sentences describe a behavioral mode, look for the word that already means it. A word that restates the default ("be thorough") does nothing; a strong one shifts behavior ("relentless," "disposable").

## Progressive Disclosure

Each layer has one job. The description helps a caller decide whether to use the artifact. The body carries what the agent needs every run. Skills and resources carry shared and situational depth it reaches when the task demands it. The same explanation at every layer makes the artifact longer without making it clearer.

## Keep the Core Harness-Agnostic

Load-bearing prompts — agent bodies, core skills — state intent: what to delegate, what context to pass, what the result must satisfy. Environment mechanics (CLI flags, tool names, launch commands) belong to the environment: the harness's own system prompt, or the tool's `-h`/help surface the agent reads at runtime.

The test: would this prompt survive a harness swap unchanged? "Spawn a researcher in the background and collect the result before your verdict" ports; a flag plus a wait command does not. Naming *what* to compose is intent, not mechanics: `@agent` references and skill attachments (`@coder --skills testing`) declare the staffing and survive the test. When mechanics must be written down, contain them in one skill so a new environment swaps that skill, not every agent.

## Deeper Resources

Load `resources/skill-level.md` for skill boundaries, loading, and progressive disclosure. Load `resources/agent-level.md` for agent role, boundary, description, and cognitive mode. Load `resources/system-level.md` for handoffs, verification, model staffing, and multi-agent coordination. `resources/research.md` holds the evidence behind these principles.
