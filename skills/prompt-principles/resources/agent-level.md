# Agent-Level Principles

An agent prompt should define a clear job, a clear boundary, and a clear mode of thinking.

## Keep the Body Focused on the Job

Use the body for the agent's purpose, boundaries, and way of engaging. Put reusable method in skills. This keeps role changes separate from shared knowledge changes and makes the body easier to scan.

## Split by Cognitive Mode

The best agent boundaries come from how the work thinks, not from what domain it touches. Execution, judgment, synthesis, and coordination each want different kinds of attention. When agents are split by domain alone, boundary cases get messy. When they are split by cognitive mode, routing gets clearer because the question becomes what kind of thinking the task needs. If the prompt asks one agent to create, critique, coordinate, and recover context all at once, attention splinters and success criteria blur.

## Describe the Work, Not a Persona

Behavioral instructions are more reliable than identity framing. Tell the agent what to pay attention to, how to judge success, what to question, and what to produce. Persona language adds flavor without adding control.

## Spawn When the Work Needs Fresh Capability

Spawn a new agent when the work needs a different model or a clean context window. Use a mode-shift skill when the shift stays within the current agent's lane. This keeps spawning tied to real changes in capability or attention budget.

## Write for Reuse Upstream and Downstream

Bodies should stay caller-agnostic so the agent can work from whatever context it receives. Descriptions should teach callers when to use the agent, what to pass, and what to expect back. If the specialization lives entirely in the caller's framing, keep one generic agent rather than creating many narrow variants. New agents earn their existence when they carry a distinct mode of thought, toolset, or durable operating method.
