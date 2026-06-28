# Mechanics Review

Use this after the prompt-quality pass, not before it.

This is a lighter sanity check, not a full validator. Look for package mechanics that contradict the prompt's intended behavior.

Check whether referenced subagents exist, whether `available:` skills are actually loadable, whether the body tells the agent to load skills or resources it cannot reach, whether `load`, `available`, and `model-invocable` contradict each other, whether tools and permissions support the workflow, and whether model policies leave the agent brittle for users with limited model access.

If you cannot verify a mechanics issue confidently, say so instead of overclaiming certainty.
