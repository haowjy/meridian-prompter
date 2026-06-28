# Model Policy Patterns

Use `model-policies` to keep an agent usable when the preferred model is not
available.

Start with the model that best matches the agent's cognitive mode. Then add a
small fallback set that can still do the job well enough on real installs,
including users who only have one subscription.

Good `model-policies` do three things:

- keep the preferred model explicit
- name a small number of realistic fallbacks
- adjust `effort` when a weaker or less naturally aligned model needs more help

Do not add policies just for symmetry. Each fallback should earn its place by
keeping the agent usable under a realistic availability constraint.

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

Use pinned aliases when the cognitive differences between model variants
matter. Keep the list short. The goal is graceful degradation, not a giant
catalog.
