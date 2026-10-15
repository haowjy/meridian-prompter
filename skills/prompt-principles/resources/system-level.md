# System-Level Principles

Multi-agent systems are useful when they create better focus, better verification, or real parallelism. They are costly when they only redistribute vague work across more prompts.

## Start with the Simplest System That Can Hold the Work

Default to one agent, then add more only when the split earns its overhead. Every extra agent adds handoff cost, debugging cost, coordination risk, and opportunities for silent scope loss. Multi-agent structure is worthwhile when one context window is not enough, when different kinds of thinking need different workers, or when independent work can proceed in parallel.

## Leads Spend Context on Decisions

A lead's scarce resource is the context it uses for decisions across a long task. Delegate work that would spend that context or that needs an independent check: broad exploration, large implementation, review. Do small fixes and glue directly when briefing a worker costs more than the change. A lead that implements large pieces loses the vantage point to notice drift; one that delegates a two-line fix pays for a briefing and a cold worker to save nothing.

## Handoffs Are a First-Class Design Problem

The caller owns the handoff. Pass objectives, constraints, prior decisions, and concrete artifacts instead of making the receiving agent rediscover context that already exists upstream. Name explicit files and outputs rather than broad categories. Weak handoffs waste time and silently drop requirements at exactly the points where the workflow is narrowing.

## Verification Must Come from Outside the Worker

Verify with external checks (tests, builds, search, review), not self-critique alone, and separate the implementer from the reviewer when the task calls for real verification. A worker judging its own output is too likely to reproduce its own blind spots.

## Loop Control Belongs Outside the Prompt

Iteration limits, termination conditions, and convergence checks belong to the system or to the coordinating agent, not to the worker prompt. Agents are poor judges of when to stop, especially when they are asked both to keep working and to decide whether more work is needed.

## Alignment Fails at Narrowings

The dangerous points in a workflow are the narrowings, where wide exploration collapses into a smaller artifact such as a plan, a decision, or an implementation brief. That is where requirements disappear. Verify alignment at those transitions before moving on, because end-of-pipeline review catches drift only after downstream work has already amplified it.

## Model Choice Is Part of the System Design

Choose models for the kind of thinking each agent needs, not just for price or speed. A good match strengthens the intended lane of work. A bad match produces either shallow judgment where depth was needed or expensive overthinking where straightforward execution would have been better.
