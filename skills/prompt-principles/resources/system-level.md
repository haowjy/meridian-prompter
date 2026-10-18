# System-Level Principles

## Start with the Simplest System That Can Hold the Work

Default to one agent, then add more only when the split earns its overhead. Every extra agent adds handoff cost, debugging cost, coordination risk, and opportunities for silent scope loss. Multi-agent structure is worthwhile when one context window is not enough, when different kinds of thinking need different workers, or when independent work can proceed in parallel.

## Leads Spend Context on Decisions

A lead's scarce resource is the context it uses for decisions. Write leads to delegate work that would spend that context, work that can run in parallel, work that needs a different model, and work that needs an independent check (broad exploration, large implementation, review), and to do the rest themselves. Write no rule that makes a lead spawn for every piece of work: delegating a two-line fix pays for a briefing and a cold worker to save nothing. The tradeoff runs both ways, since a lead deep in a large implementation loses the vantage point to notice drift.

## Handoffs Are a First-Class Design Problem

The caller owns the handoff. Write leads to pass objectives, constraints, prior decisions, and concrete artifacts, named as explicit files and outputs rather than broad categories, so the receiving agent doesn't rediscover context that already exists upstream. Weak handoffs waste time and silently drop requirements at exactly the points where the workflow is narrowing.

Design for the handoff on both sides. Descriptions name the inputs an agent needs, so a caller can brief it. Leads record decisions, plans, and findings on disk as they go, so each handoff can name its inputs: context that lives only in a conversation is lost at compaction and can't be passed.

## Verification Must Come from Outside the Worker

Write verification as external checks (tests, builds, search), not self-critique alone, and put review in a session of its own: a worker judging its own output carries the assumptions that produced the mistake. A reviewer on another model family adds a second set of blind spots and is usually the better pick, but a fresh session on the worker's model is an independent check too. A reviewer on the family the work targets adds a reading as the running agent would.

## Loop Control Belongs Outside the Prompt

Iteration limits, termination conditions, and convergence checks belong to the system or to the coordinating agent, not to the worker prompt. Agents are poor judges of when to stop, especially when they are asked both to keep working and to decide whether more work is needed. Give the coordinating agent:

- a definition of convergence, such as no blocking findings
- a concrete limit for each loop, and where the impasse goes at that limit: the coordinator's caller
- a patching limit: a concern (the code behind one responsibility) that would need a third round of fixes ends patching, and the coordinator looks for the shared cause or a redesign
- explicit deferral as a valid exit

## Alignment Fails at Narrowings

The dangerous points in a workflow are the narrowings, where wide exploration collapses into a smaller artifact such as a plan, a decision, or an implementation brief. That is where requirements disappear. Write leads to verify alignment at those transitions before moving on, because end-of-pipeline review catches drift only after downstream work has already amplified it. At each narrowing the lead tells parallel workers what each owns, so they don't collide, and gives a reviewer the source alongside the output, since alignment review needs both.

## Model Choice Is Part of the System Design

Choose models for the kind of thinking each agent needs, not just for price or speed.

- **Clear-goal execution** (coders, testers, builders with clear specs): fast, instruction-faithful models. They excel when the target is unambiguous and overthink when it isn't.
- **Ambiguity handling** (primary agents, leads, design exploration, user-facing roles): models that push back, ask questions, and iterate, for tasks where the right answer emerges through dialogue.
- **Judgment and review** (adversarial review, architectural decisions, tradeoff analysis): models with evaluation depth.

Put default models in agent definitions and model choice in the skills that guide staffing, not in bodies. When work needs more depth, change the model rather than the agent: an agent picked for its model brings its whole procedure along.
