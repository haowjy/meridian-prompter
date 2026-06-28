# Mechanics Review

Use this after the prompt-quality pass, not before it.

This is a lighter sanity check, not a complete validator. Flag obvious
contradictions in the package mechanics that would undermine the intended
behavior.

Look for:

- referenced subagents that do not exist or are not available in this package stack
- skills listed in `available:` that are not loadable on demand
- body instructions that tell the agent to load skills or resources it cannot reach
- `load`, `available`, and `model-invocable` combinations that contradict each other
- tools or permissions that do not support the workflow the prompt describes
- model policies that leave the agent brittle for users with limited model access

If the mechanics look incomplete but you cannot verify them confidently, say so
as a limitation rather than overclaiming certainty.
