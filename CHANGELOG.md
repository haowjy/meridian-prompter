# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [SemVer](https://semver.org/).

## [Unreleased]

## [0.3.5] - 2026-06-17

## [0.3.4] - 2026-06-17

## [0.3.3] - 2026-06-14

### Changed
- `prompt-principles/resources/skill-level.md`: `kb-conventions` → `knowledge-layers` in examples.
- `@prompt-dev`: default model `opus46` → `opus48`.

## [0.3.2] - 2026-05-31

### Changed
- Agent model assignments tuned: `prompt-dev` pinned to `opus46` (intent inference for the interactive lead), `prompt-reviewer` `gpt` → `gpt54` (thorough adversarial review), `prompt-tester` `sonnet` → `deepseek` (cheaper behavioral testing), `python-tool-writer` `codex` → `gpt54` (stronger all-around tool authoring).
- Removed tracked `mars.lock`; lock is generated local state and ignored.

## [0.3.1] - 2026-05-30

## [0.3.0] - 2026-05-30

### Changed
- `skill-artifacts`: loading mechanics (load/available/model-invocable), skill types (principle/guardrail/mode-shift/checkpoint/reference), pollution/nudge guidance, scripts and split thresholds.
- `prompt-principles` skill-level: loading mechanics, nudge problem, decompose-for-progressive-loading, skill types as cognitive lane shifts. Body threshold 500 → 100 lines.
- `prompt-principles` agent-level: light bodies/fat skills principle, model-as-highway (model personality shifts the cognitive lane), agent-vs-skill decision for cognitive shifts.

## [0.2.2] - 2026-05-22

## [0.2.1] - 2026-05-16

## [0.2.0] - 2026-05-11

## [0.1.14] - 2026-05-09

## [0.1.13] - 2026-05-09

### Changed
- `python-tool-writer`: replaced SOLID reference with separation-of-concerns language.
- All skills: added `type:` field (principle, reference) for ordered injection consistency with meridian-base and meridian-dev-workflow.
- `skill-artifacts`: documents the `type:` field (principle, guardrail, reference) and its injection ordering.

## [0.1.12] - 2026-05-06

## [0.1.11] - 2026-05-06

### Changed
- `prompt-dev` opening now centers reliable agent behavior, context use, and model/harness capability tradeoffs.

## [0.1.10] - 2026-05-04

### Changed
- Bumped meridian-base to v0.2.6.

## [0.1.9] - 2026-05-04

## [0.1.8] - 2026-05-03

### Changed
- Skill schema: migrated from `invocation: explicit` to `model-invocable: false`. `skill-artifacts` body text updated to reference new field name.
- Bumped meridian-base to v0.2.4.

## [0.1.7] - 2026-05-03

### Changed
- Bumped meridian-base dep to v0.2.2.

### Removed
- Model catalog (`opus`, `gpt`) — now lives in meridian-base.

## [0.1.6] - 2026-05-03

## [0.1.5] - 2026-05-03

## [0.1.4] - 2026-05-02

### Changed
- Skill frontmatter: migrated all skills from legacy `disable-model-invocation`/`allow_implicit_invocation` to canonical `invocation: explicit`.
- `skill-artifacts`: updated guidance to reference `invocation: explicit` instead of legacy fields.
- Bumped meridian-base dependency to v0.2.1.

## [0.1.3] - 2026-05-02

### Added
- `intent-modeling` and `llm-writing` skills pulled from meridian-base. `prompt-dev` loads both; `prompt-reviewer` loads `llm-writing`.
- `prompt-review`: LLM writing patterns (overcorrection, contrastive definitions, conversational mode leaking) as review targets.
- `python-tool-writer`: web search tools for self-serve library research.

### Changed
- All skill descriptions: trigger-first ("Load when...") instead of content-first.
- `agent-artifacts`: schema removed — points to [mars agent profile reference](https://github.com/meridian-flow/mars-agents/blob/main/docs/config/agent-profiles.md). Body is now design guidance only.
- `agent-artifacts/resources/meridian.md`: trimmed to design patterns (subagent design, handoffs, model staffing). Schema and permission tables removed.
- `skill-artifacts`: trimmed from schema template to three design principles.
- `prompt-reviewer`: trimmed body — skills carry methodology, body sets adversarial stance.
- `prompt-tester`: trimmed prescriptive checklists to principles.
- `prompt-review`: cut "What wastes time" (negative framing), compressed adversarial mindset checklist to principle-level guidance.
- `python-tool-writer`: folded `python-tools` methodology into agent body.
- `python-tools/SKILL.md`: trimmed redundant "When Tool > Agent" list, "Quality Bar" checklist.
- `system-level.md`: cut antipatterns table (negative framing, covered by positive principles).
- `mars.toml`: pinned meridian-base to v0.1.3.

### Removed
- `python-tools` skill — only one agent used it, content was generic. Conda/mamba preference folded into `python-tool-writer` body.

## [0.1.2] - 2026-05-01

### Added
- `prompt-principles`: cognitive mode discovery methodology in agent-level resource. Ask the user, research the domain, study solo vs team decomposition, collapse test. SKILL.md bullet updated to hint at discovery steps.

## [0.1.1] - 2026-05-01

### Removed
- `meridian-cli` from `mars.toml` skills filter (skill deleted from meridian-base).
- `meridian-cli` row from `agent-artifacts/resources/meridian.md` base skills table.

## [0.1.0] - 2026-04-30

### Changed
- `prompter-orchestrator` → `prompt-dev`. Role rename — real-world title primes for collaborative iteration over mechanical orchestration.
- All skills get explicit invocation-control flags (`disable-model-invocation`, `allow_implicit_invocation`). Skills only load when listed in an agent's `skills:` field, not from description matching.
- `skill-artifacts`: documents invocation-control fields in frontmatter schema.
- `agent-artifacts`, `prompt-principles` resources: "orchestrator" role references → "manager/lead" throughout. "Orchestrator pattern" (the design pattern) unchanged.
- `prompt-reviewer`, `prompt-tester`: updated to use manager/lead terminology for role labels.
- `meridian.toml`: primary agent → `prompt-dev`.
- `mars.toml` opus model description updated.
- `prompt-dev`: added `mars version` release guidance.

## [0.0.7] - 2026-04-28

### Added
- **prompt-principles (prompt-level)**: "Escape hatches get used" — optional easier paths become de facto defaults; don't offer shortcuts when the hard path is the right path
- **prompt-principles (prompt-level)**: "Every word carries decision weight" — filler dilutes the words that matter; cut what doesn't change behavior
- **prompt-principles (agent-level)**: "Descriptions serve callers" — teach usage (when, how to invoke, what to pass, how to prompt, what to expect), not just purpose
- **prompt-principles (agent-level)**: "Route by cognitive mode" — decompose by thinking type (faithful execution vs aesthetic judgment vs ambiguity handling), not file type
- **prompt-principles (agent-level)**: "Generic over specialized" — if specialization lives entirely in the caller's prompt, keep the agent generic
- **prompt-principles (skill-level)**: "Separate mechanism from methodology" — how to operate a tool vs what to do with it; separation enables reuse across use cases
- **prompt-principles (system-level)**: "Explicit handoff content" — name specific file paths at every handoff, not categories
- **prompt-principles (system-level)**: "Verify alignment at narrowings" — pipeline hourglass loses scope at each narrowing; verify coverage before it compounds
- **prompt-principles (system-level)**: "Match model to cognitive mode" — clear-goal execution, ambiguity handling, and nuanced judgment need different models
- **prompt-principles (meridian)**: Pipeline handoff patterns — name upstream artifacts explicitly at each transition
- **prompt-principles (meridian)**: Model staffing guidance — match profile model to agent's cognitive mode
- **prompt-principles (meridian)**: `--from $MERIDIAN_CHAT_ID` pattern for primary session context
- **agent-artifacts (meridian)**: Description pattern extended with "How to prompt it" — tell callers what to include in the task prompt
- **prompter-orchestrator**: Renamed from prompt-writer, rewritten with dev-orchestrator style — collaborative sessions, active engagement, iterative drafting
- **web-prompt-researcher**: New agent for researching prompting papers and patterns

### Changed
- **prompt-principles**: Replaced `$MERIDIAN_WORK_DIR` guidance with CLI discovery — `meridian context work|kb|work.archive` for roots, `meridian work current` for session work dir (empty = no work attached). `MERIDIAN_*` vars marked internal; warn against `MERIDIAN_FS_DIR` (legacy) and against treating `MERIDIAN_PROJECT_ROOT` as repo root.
- **prompt-principles**: Added "Be concise, expand for emphasis" as core principle
- **prompt-principles**: Rewrote "repetition" principle — repetition improves compliance within artifacts
- **prompt-principles**: Applied positive framing throughout, removed negative explanations
- **prompt-principles**: Removed folklore section from research.md and split direct empirical support from operational guidance
- **prompt-principles**: Tightened prompt-level.md for token efficiency
- **prompt-review**: Added positive framing check to adversarial review
- **AGENTS.md**: Rewrote to reflect actual agent/skill structure

### Removed
- Dependency on `meridian-dev-workflow` (was only used for internet-researcher)

### Fixed
- Consistent use of `resources/` directory name (was mixed with `references/`)
- Removed false "empirical" claims for practitioner heuristics (3-5 function limit)

## [0.0.2] - 2026-04-17

### Changed
- Renamed `review` skill to `prompt-review` to avoid collision with `meridian-dev-workflow`'s review skill.

## [0.0.1] - 2026-04-17

### Added
- Initial release of meridian-prompter — workflow for creating and improving LLM agents and skills from first principles.
- `@prompter-orchestrator`: user-facing entry point with first principles problem breakdown, routes to writers/reviewers/testers.
- `@agent-writer`: drafts agent definitions from requirements, applies `/agent-principles`.
- `@skill-writer`: drafts skill definitions with progressive disclosure structure.
- `@tool-writer`: creates Python scripts for scientific/data analysis, receives research from orchestrator.
- `@agent-reviewer`: adversarial review of agents against principles.
- `@skill-reviewer`: review of skill definitions.
- `@agent-tester`: behavioral testing of agents.
- `agent-principles` skill: research-backed 4-level framework (prompt, skill, agent, system).
- `agent-artifacts` skill: frontmatter schema and artifact conventions.
- `skill-artifacts` skill: skill structure and conventions.
- `review` skill: local review methodology (does not depend on dev-workflow).
- Dependencies: `meridian-base` (spawn, cli), `meridian-dev-workflow` (internet-researcher).
