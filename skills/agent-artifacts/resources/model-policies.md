# Model Policy Patterns

Use `model-policies` to keep an agent usable when the preferred model is not available.

Start with the model that best matches the agent's cognitive mode. Then add a small fallback set that keeps the agent usable for real users, including users with only one subscription.

Keep the preferred model explicit, keep the fallback set short, and raise `effort` when a weaker or less aligned model needs more help. Do not add policies for symmetry. Each fallback should earn its place.

Typical pattern:

```yaml
model: opus46
model-policies:
  - match: {alias: opus46}
    override: {}
  - match: {alias: opus48}
    override: {}
  - match: {alias: gpt54}
    override: {effort: high}
```

For broader model-to-cognitive-mode guidance, use `/prompt-principles` and `resources/agent-level.md`.
