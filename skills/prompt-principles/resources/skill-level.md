# Skill-Level Principles

## Write for the Agent Mid-Task

Write the method, criteria, and vocabulary for the work the skill covers, as instructions that hold in any agent that loads it. Leave the agent's job and delegation to the agent's body: a skill that assumes its caller ("the orchestrator", "your lead") or restates a role breaks in every other agent that loads it. A skill can define what its method produces, such as a review's findings and verdict; the agent's body owns its overall report.

## Extract for Reuse, Not for Tidiness

Move something into a skill when multiple agents need the same knowledge or method. If only one agent needs it, keep it in the body; one place to maintain. The test is whether multiple agents would get lighter and clearer if the content moved out.

## Choose How It Loads

Each way a skill reaches an agent spends a different budget:

- **Always loaded** costs context on every turn of every run. Reserve it for what the agent needs every run.
- **Self-loaded on demand** costs one description line on every turn, and that line's wording decides whether the agent ever loads it.
- **Attached by a caller** costs nothing until a caller that knows the work needs it attaches it.
- **Invoked only by a human** costs no context and spends the human's memory instead: they have to know it exists.

Pick the cheapest path that still reaches the agent when the work needs it. `/skill-artifacts` maps each path to its fields.

## Disclose Progressively

`/prompt-principles` covers what goes in the body and what goes behind a pointer. Inside a skill, a resource loads only when the agent opens it, so the body names each resource with when to open it; a resource nothing names is rarely read. Split resources by the cases that use them: if two files always load together, merge them; if one file mixes cases, agents load irrelevant context to reach the paragraph they need.

## Separate Mechanism from Method

Keep tool operation separate from guidance about how to use the tool well. Mechanism is reusable across tasks; method depends on what the worker is trying to accomplish. When they are separate, a tool skill can support many methodologies and a methodology skill can survive a tool change. Put a deterministic step in a script, and say whether the agent runs it or reads it. A script that handles ordinary errors itself keeps them out of the agent's context.
