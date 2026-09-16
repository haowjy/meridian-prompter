# Model Policy Patterns

Set `model` to the preferred choice. Concrete `alias` and `model` entries in
`model-policies` supply backups in declaration order; no separate fallback list
is needed. Keep that list short and use overrides only where a model needs
different settings.

```yaml
model: opus46
model-policies:
  - match: {alias: opus46}
    no-fallback: true
    override: {effort: high}
  - match: {alias: opus48}
    override: {}
  - match: {alias: sol}
    override: {effort: high}
```

Here Opus 4.6 is still the primary. Its flag means only “do not use this entry as
a backup”; it does not prevent fallback to Opus 4.8 or Sol. Flagged entries can
still provide settings when selected as the primary or explicitly.

An empty or omitted `override` still declares a candidate. Preserve these entries
when editing profiles. `model-glob` rules match settings but do not generate
launch backups. An explicit model request disables model fallback.

Changing the primary, including through a local override, does not discard the
profile's candidates. Mars scans the whole profile list, independently of which
rule supplies the primary's settings. Overlay and global rules supply settings,
not additional backup lists.

Enabled targets constrain which harnesses Mars may try before installation,
authentication and model support are assessed. Installed tools, generated target
directories and cached login state do not enable a target. A model family is not
a harness: an Anthropic model may still run through an enabled OpenCode route.
Fallback chooses a route before launch; it does not promise credits or switch
models after a runtime credit error.
