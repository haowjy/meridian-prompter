# Agent-Level Principles

An agent prompt should define a clear job, a clear boundary, and a clear mode of thinking. Everything else should support that lane instead of competing with it.

## Keep the Body Focused on the Job

Use the body for the agent's purpose, boundaries, and way of engaging. Put reusable method and reference depth in skills. This makes the body easier to scan and easier to maintain, and it keeps role changes separate from shared knowledge changes. When the body starts teaching general methodology, the agent becomes harder to review and easier to duplicate badly.

## One Agent, One Kind of Work

Agents work best when they do one kind of job well. If the prompt asks the same agent to create, critique, coordinate, and recover context all at once, attention splinters and success criteria blur. Splitting the work gives each lane a cleaner context window and lets each agent optimize for one mode instead of juggling several incompatible ones.

## Describe the Work, Not a Persona

Behavioral instructions are more reliable than identity framing. Tell the agent what to pay attention to, how to judge success, what to question, and what to produce. Persona language often adds flavor without adding control, and it can crowd out the actual decision rules the model needs.

## Split by Cognitive Mode

The best agent boundaries usually come from how the work thinks, not from what file or domain it touches. Execution, judgment, synthesis, ambiguity handling, and coordination each want different kinds of attention. When agents are split by domain alone, boundary cases get messy. When they are split by cognitive mode, routing gets clearer because the question becomes what kind of thinking the task needs.

## Spawn When the Work Needs Fresh Capability

Spawn a new agent when the work needs a different model or a clean context window. Use a mode-shift skill when the shift stays within the current agent's lane. This keeps spawning tied to real changes in capability or attention budget instead of using new agents as a substitute for prompt discipline.

## Write for Reuse Upstream and Downstream

Bodies should stay caller-agnostic so the agent can work from whatever context it receives. Descriptions should teach callers when to use the agent, what to pass, and what to expect back. If the specialization lives entirely in the caller's framing, keep one generic agent rather than creating many narrow variants. New agents earn their existence when they carry a distinct mode of thought, toolset, or durable operating method.
