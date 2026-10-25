# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [SemVer](https://semver.org/).

## [Unreleased]

## [0.5.12] - 2026-10-25

### Changed
- Requires Meridian >=0.14.6. `agent-artifacts` and `skill-artifacts` now point to `prompt-authoring__meridian`, the agent and skill format guide Meridian ships, instead of carrying their own copy.

## [0.5.11] - 2026-10-25

### Changed
- Requires Meridian >=0.14.5 and accepts meridian-base 0.12, which moved Meridian's own skills into Meridian.
- Skill guidance distinguishes the harness's model-invocable inventory from
  Meridian's emphasis on profile-available skills, with one shared portability
  caveat for Meridian-supplied behavior.
- Prompt profiles now rely on runtime-supplied capabilities to notify the human
  and read past sessions instead of naming package skills.
- Agent and skill authoring guidance describes coordinator capabilities instead of Meridian CLI mechanics while preserving the Mars artifact schema and portable runtime policy.
- Artifact guidance identifies behavior Meridian supplies, standardizes attach skills, pass files, and carry a prior run, and restores launch-policy preview and automatic command-grant guidance.

## [0.5.10] - 2026-10-25

### Changed
- Requires Meridian >=0.14.0 and Mars >=0.18.0 for portable network policies.
- `@web-prompt-researcher` uses a workspace sandbox so Codex can provide the declared shell network. Its edit and write tools stay denied, but its shell can now write inside the sandbox's writable folders; destructive git commands are denied on Claude (Codex cannot express scoped shell rules).
- `agent-artifacts` documents portable sandbox and network policy, host lists, harness limits, and Meridian's automatic command grants.

## [0.5.9] - 2026-10-25

### Changed
- Requires Meridian >=0.13.0 for platform-owned Meridian command permissions.
- prompt-dev and prompt-tester drop scoped Meridian allows that were redundant beside plain Bash; prompt-dev also receives Meridian's spawn grant from its `subagents` declaration.

## [0.5.8] - 2026-10-23

### Changed
- meridian-base dependency pinned to the current minor, `>=0.11.0, <0.12.0`. 0.5.7 left it unpinned.

## [0.5.7] - 2026-10-23

### Changed
- meridian-base dependency unpinned: resolves to its latest release.

## [0.5.6] - 2026-10-22

### Changed
- Prompt verification scales with uncertainty and consequences: small reversible edits use an author check and observation in normal work; substantial changes get independent review without a fixed review team.
- Dedicated behavioral experiments require user-approved scope. prompt-tester runs focused cases, and evaluation guidance no longer requires a run or matrix for every edit.

## [0.5.5] - 2026-10-22

### Changed
- prompt-dev and prompt-tester use `danger-full-access` so shell dependency fetches and validation can run without sandbox network or filesystem restrictions. Approval settings are unchanged.

## [0.5.4] - 2026-10-18

### Changed
- prompt-dev never falls back to Fable (`no-fallback: true`); Fable is escalation only. The agent-artifacts model-policies example uses Sonnet as the backup.

## [0.5.3] - 2026-10-18

### Changed
- prompt-reviewer defaults to Sol (xhigh); backups Opus, then Astra.
- prompt-dev staffs the checks a change needs: wording-only changes read by the author; a behavior change gets one reviewer plus a test; a new agent or rewrite adds a second reviewer and a cold read; no model-family rules. Reruns only the checks an edit could change.
- `prompt-principles`: review needs a session of its own; another model family is preferred, not required. New principle, Look Back for Deletions: after a round of changes, find additions that patch holes other lines made, and fix the line that made the hole.
- `skill-artifacts`: a skill under `load` (or attached with `--skills`) arrives in full on every harness whatever its `model-invocable`; `model-invocable: false` + `load` gives one agent a skill no model finds by itself; the `# Skill: /<name>` header. `agent-artifacts`: a loaded skill is in context even when the harness's skill list omits it. `prompt-review` mechanics: `available` + `model-invocable: false` is the contradiction to catch.

## [0.5.2] - 2026-10-17

### Changed
- prompt-dev loads `/notify` from meridian-base.

## [0.5.1] - 2026-10-17

### Changed
- `agent-artifacts`: Meridian does tell spawns their final message is the report; bodies say only what it holds. `edit: deny` doesn't stop shell writes; web search goes through built-in tools under the workspace sandbox; only cloning needs full access.
- `prompt-dev`: loop limits (third round of fixes or fourth review round means rethinking the design; a second redesign goes to the user); `@cold-reader` reads new prompt text.
- `prompt-principles`: drops the line that invited replacing a removed limit.
- Agents declare `mode` (prompt-dev primary, the rest subagent). `system-level`: defines concern where the patching limit names it.
- Cut duplication: prompt-review's checklist (restated `/prompt-principles`), agent-artifacts' Where Artifacts Go, skill-level's Skills Teach; Agents Decide, prompt-tester's Testing Skills, file-intro lines, and explanatory tails in the principles and level resources.
- `agent-artifacts`: fallbacks are decided per agent; a model explicit-only in one agent can be a backup in another.
- `prompt-dev`: Verify Before Shipping. Behavior changes get two `@prompt-reviewer`s on different model families, one the prompt's target family; wording-only changes get one. `@prompt-tester` runs on the final text. Report each reviewer's model and verdict.
- `web-prompt-researcher`: bash for shell search tools on harnesses without built-in web tools; stays read-only.
- Authoring skills restructured so each meaning has one home and each file addresses one reader. Principles from mattpocock/skills (`writing-for-agents`) and cursor pstack folded in.
- `prompt-principles` body (harness-agnostic, for any document an agent reads): new **Write for the Reader of Each Layer** (description, agent body, skill body, resource, authoring guide), **Keep One Source of Truth** (environment restated is a cache; sediment), **End Each Step on a Completion Criterion**, **Progressive Disclosure** moved up beside it and widened (each layer holds one depth; body keeps the judgment and steps every run takes, pointers carry the rest; pointer wording decides reach; point straight to the target, while summary hierarchies like AGENTS.md trees earn their levels), **Encode Lessons in Structure First**, **Test on Real Runs**. Altitude now matches prescription to fragility, and keeps intent when constraints go. Reasons only where the model must generalize.
- New `resources/evaluation.md`: start from the failure or target behavior, baseline comparison, trigger and routing tests, blind candidates, judge on another family, grade from transcripts.
- `agent-level.md`: define the job, not how far to look (replaces "Assume focused context… work with what arrived"); name what comes back; proceed on what can be undone; description as routing contract tested against neighbors. `skill-level.md`: write for the agent mid-task; loading as budgets (design only); resources load only when named; decompose by branch; scripts say run or read. `system-level.md`: leads may do any work and delegate by what a worker does better; handoffs through descriptions and on-disk records; loop control with concrete limits; models by cognitive mode, chosen in profiles.
- Meridian specifics move into the format skills: `/agent-artifacts` (inventory callers see, injected guidance, how context reaches a spawn, models, harness permissions, artifact locations, packages) and `/skill-artifacts` (loading and invocation fields, `user-invocable`, listing by type). `prompt-principles/resources/meridian.md` and `agent-artifacts/resources/meridian.md` removed; the loading-field list exists once.
- `prompt-review` checks wrong reader, unjustified limits, duplication and environment caches, model coupling, prose a permission could enforce, weak pointers, missing completion criteria; one set of verdict words (approve, approve with notes, request changes). `agent-artifacts` and `skill-artifacts` are self-loadable; `@prompt-reviewer` and `@prompt-dev` list them as available. `@prompt-tester` follows `evaluation.md`, writes its test projects in scratch, and its description says what to pass and what returns. `@prompt-dev`: one target-family reviewer plus one on another family; tests scale to the change.
- `research.md`: unsupported rows removed (handoff-loss figure, unsourced quotes, rows no principle uses); MAST, SkillsBench (pinned v1), PRISM and Lulla rows corrected.

## [0.5.0] - 2026-10-15

### Changed
- Requires meridian-base 0.11 (`/correct`, the corrections register, generic base wording).
- Review fixes: reviews run on a model family other than the author's (`system-level.md`, `meridian.md`); `skill-level.md` sets `model-invocable: false` for caller-injected skills; `@prompt-tester` checks read-only agents never write.
- `prompt-principles` folds `resources/prompt-level.md` into its body as one sequence (placement and structure, every line, say what to do, reasons, altitude, flat instructions, leading words): it governs every line, so it loads instead of waiting to be opened. Benchmark citations moved to `resources/research.md`. `agent-artifacts`: read an agent's history before merging, deleting, or narrowing it; keep explicit-only models `no-fallback` everywhere. `@prompt-dev` loads `explore-and-engage`.
- `prompt-principles` resources state the behavior positively: write caller-agnostic, brief spawns as if they have no history, verify with external checks.
- `prompt-reviewer` keeps Grok as an explicit option but never falls back to it.
- `prompt-dev`: reads the artifact skill, the level resource, and the Meridian resources before writing or editing any agent or skill, not only "for Meridian agents".
- Skill and agent descriptions in this package say when to use them, not what they contain.
- Lead guidance (`system-level.md`, `meridian.md`, `agent-artifacts`) no longer says leads never implement: delegate what spends decision context or needs an independent check; do small fixes and glue directly. The 15–25 iteration cap is replaced by stopping at the second finding of the same failure class.
- `prompt-principles`: new "State Instructions Flat": default to unconditional directives, keep a condition only when the instruction flips, citing AgentIF's measured drop in compliance on conditional constraints.

## [0.4.4] - 2026-10-15

### Changed
- `@prompt-dev`: default model `opus46` → `opus` (Opus 5.5). `@prompt-tester`: `opus46` fallback → `opus`. Model-policy example uses `opus`.

## [0.4.3] - 2026-09-22

### Changed
- Removed Composer from python-tool-writer's fallback policy; the base alias remains available during retirement.
- Prompt tester defaults to Luna; fallback order is DeepSeek, Sonnet, Sol, Opus 4.6.
- Web prompt researcher: Luna, DeepSeek, Sonnet. Python tool writer: Luna, DeepSeek, Sonnet, Sol, with explicit input/output and verification briefing guidance.
- Prompt Dev keeps Opus46, then Astra, Fable, Sol, Sonnet for judgment and writing. Removed its fixed harness so model aliases select their routes.
- Prompt Reviewer: Astra, Sol, Grok, Opus. DeepSeek/Luna remain explicit quick-review options, excluded from automatic fallback.
- Requires meridian-base >=0.10.11 for refreshed base staffing.

## [0.4.2] - 2026-09-16

### Changed
- Clarify target-constrained model fallback, whole-profile candidate ordering and per-entry `no-fallback`; preserve candidate-only rules.
- Require Mars >= 0.14.0 for that fallback contract.

## [0.4.1] - 2026-07-09

### Changed
- Prompt Dev retains Opus 4.6 as its default and replaces its GPT-5.5 fallback with `sol` at `xhigh`; Prompt Reviewer defaults to `sol` at `xhigh`; Prompt Tester defaults to `terra` at `xhigh` with `sol` at `medium`; Python Tool Writer defaults to `sol` at `medium`; Web Prompt Researcher retains GPT Mini and replaces its GPT-5.5 fallback with `terra` at `xhigh`.

## [0.4.0] - 2026-07-09

### Added
- `/prompt-principles`: new "Keep the Core Harness-Agnostic" section — load-bearing prompts state intent; environment mechanics live in the harness system prompt or the tool's `-h`; `@agent` references and `--skills` attachment count as composition intent; contain unavoidable mechanics in one skill.

### Changed
- `/skill-artifacts`: corrected `model-invocable` semantics — defaults to true; explicit `false` makes an `available` skill visible but not self-loadable (caller `--skills` injection still works).
- `/agent-artifacts`: bodies should be harness-agnostic as well as caller-agnostic — state intent, leave CLI flags and tool mechanics to the environment.
- Agent profile retunes (prompt-dev, prompt-reviewer, prompt-tester, python-tool-writer).

## [0.3.11] - 2026-07-05

### Changed
- Replaced `gpt54` agent references with `gpt55`.

## [0.3.10] - 2026-07-04

### Changed
- `prompt-principles`: added "Every Line Must Change Behavior" and "Prescribe Only What Needs to Be Predictable" to body. Tightened progressive disclosure section.
- `prompt-principles/resources/prompt-level.md`: renamed "Attention Is a Scarce Resource" to "Attention Is Positional". Added "Use Leading Words" section. Removed meridian-specific examples.
- `prompt-principles/resources/skill-level.md`: rewrote "Loading Is Part of the Design" with four-layer model (load/available/description/--skills).
- `prompt-principles/resources/agent-level.md`: merged "One Agent, One Kind of Work" into "Split by Cognitive Mode".
- `prompt-principles/resources/system-level.md`: removed no-op trailing sentences.
- `prompt-principles/resources/meridian.md`: replaced all em dashes with proper punctuation.
- `prompt-principles/resources/research.md`: replaced em dashes.
- `prompt-review`: added instruction to read all four resource files before reviewing, with content annotations.
- `agent-artifacts`: collapsed 4 routes to prompt-principles into one. Cut duplicate spawn-restrictions mention.
- `agent-artifacts/resources/meridian.md`: fixed wrong reference (agent-level.md to system-level.md for model guidance).
- `agent-artifacts/resources/model-policies.md`: removed trailing prompt-principles route.
- `skill-artifacts`: rewrote loading paragraph with four-layer model. Promoted "Descriptions should lead with when to load" to own section.

## [0.3.9] - 2026-06-28

## [0.3.8] - 2026-06-28

### Added
- `agent-artifacts/resources/model-policies.md`: guidance for using `model-policies` to keep agents usable on single-subscription installs with a small, intentional fallback set.
- `prompt-review/resources/mechanics.md`: secondary mechanics sanity check for package wiring after the main prompt-quality review.

### Changed
- `prompt-dev`: body cut down to prompt-specific judgment, now loads evidence-grounded grilling plus agent/skill artifact guidance, adds explicit subagent roster, and gains model fallbacks for non-Claude installs.
- `prompt-reviewer`, `prompt-tester`, `python-tool-writer`, and `web-prompt-researcher`: descriptions and bodies tightened; model-policies added so the package degrades gracefully when preferred models are unavailable.
- `AGENTS.md`: simplified to source-vs-generated editing guidance instead of listing generated structure details.
- `agent-artifacts`: trimmed stale schema/tool wording and points to the new model-policies guidance.

## [0.3.6] - 2026-06-19

### Changed
- All agent descriptions rewritten as natural sentences; removed spawn instructions (belongs in routing docs).
- `prompt-dev` body: definition-list bullets → sentence bullets, agent-vs-skill section tightened, progressive-disclosure list simplified, em-dash cleanup.
- `prompt-reviewer` body: compressed opening and skill-loading paragraph; dropped standalone "findings report" line.
- `skill-level.md`: removed `clear-mind` from guardrail example list.

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
