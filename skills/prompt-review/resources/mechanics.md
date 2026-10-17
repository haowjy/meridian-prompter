# Mechanics Review

Run this after the prompt-quality pass. It's a sanity check, not a full validator: look for package mechanics that contradict what the prompt intends.

Check that referenced subagents and skills exist; that `available` skills are loadable and the body doesn't send the agent to skills or resources it can't reach; that `load`, `available`, and `model-invocable` don't contradict each other; that `tools` and `sandbox` allow the work the prompt asks for (web search, fetching, and cloning need network access) and deny what it forbids; and that model policies don't leave the agent unusable for someone with limited model access.
