# Agent-Level Principles

## Keep the Agent a Thin Wrapper Over Skills

An agent is a model, its permissions, and the skills it loads. Its body holds only what those can't carry: the job, its boundaries, its way of engaging, and what it returns. Put method, procedure, and domain knowledge in skills, even when only one agent uses them.

The reason is portability. Agent bodies don't travel: some harnesses' plugin formats carry skills but not agents (Codex and OpenCode plugins), so method written into a body never reaches those users, while the same method in a skill does. A body that keeps growing is the sign; when you would add method to one, write it as a skill and have the agent load it.

## Split by Cognitive Mode

The best agent boundaries come from how the work thinks, not from what domain it touches. Execution, judgment, synthesis, and coordination each want different kinds of attention. When agents are split by domain alone, boundary cases get messy. When they are split by cognitive mode, routing gets clearer because the question becomes what kind of thinking the task needs. If the prompt asks one agent to create, critique, coordinate, and recover context all at once, attention splinters and success criteria blur.

## Describe the Work, Not a Persona

Behavioral instructions are more reliable than identity framing. Tell the agent what to pay attention to, how to judge success, what to question, and what to produce. Persona language adds flavor without adding control.

## Define the Job, Not How Far to Look

A body that fences the agent to its brief ("stay in scope", "only the diff", "work with what arrived") makes it report a cause it finds outside the brief as an aside, or drop it. Say what the job is and what success looks like; ownership limits, such as which files a worker may edit, belong in the brief, where they fit the task.

## Name What Comes Back

Have the agent write results that outlive the conversation to files, which survive compaction and can be passed to the next agent, and say what its final report holds: what it found or changed, where it wrote it, and what it left unverified.

## Spawn When the Work Needs Fresh Capability

Spawn a new agent when the work needs a different model or a clean context window. Use a skill that shifts the agent's mode when the shift stays within the current agent's lane.

## Proceed on What Can Be Undone

Write agents to make reversible decisions within what they were asked to do and report what they chose, and to stop before an irreversible action (deleting data, pushing, sending something outside) or an action beyond what they were authorized to do. A spawned agent usually has no human to ask, so a question it can't send either stalls it or turns into an unstated guess.

## Write the Description Against Its Neighbors

A caller chooses among agents by their descriptions. Beyond when to use it, what to pass, and what comes back, write the description in words that tell the agent apart from its neighbors; persona or "helps with X" give a caller nothing to route on. For an approved experiment on caller selection, use the routing test in `evaluation.md`.

## Write for Reuse Upstream and Downstream

Bodies should stay caller-agnostic so the agent can work from whatever context it receives. If the specialization lives entirely in the caller's framing, keep one generic agent rather than creating many narrow variants. Before splitting off a new agent, sharpen the descriptions and tools of the existing ones; a misrouted job is often a description problem. New agents earn their existence when they carry a distinct mode of thought, toolset, or durable operating method. Before merging, deleting, or narrowing an agent, read its history: a different default model, a role the human asked for, or a job beyond what its body now says is a reason it exists, so name each one in the proposal.
