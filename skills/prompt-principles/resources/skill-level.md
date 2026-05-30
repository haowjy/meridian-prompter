# Skill-Level Principles

When to extract shared knowledge into a skill vs keeping it in an agent body.

## Reuse Threshold

**If 2+ agents need the same knowledge, extract to a skill.**

If only one agent uses it, keep it in the agent's body. Extracting single-use knowledge creates two places to maintain with no reuse benefit.

Signs you need a skill:
- You're copy-pasting the same guidance into multiple agent bodies
- Multiple agents reference the same methodology (e.g., spawn mechanics, artifact layouts)
- Knowledge is stable across agents but agents diverge in behavior

Signs you don't need a skill:
- Only one agent uses this knowledge
- The guidance is tightly coupled to this agent's specific behavior
- Extracting would create a skill that's really "how to be this one agent"

## Loading Mechanics

Skills have three loading levels that determine whether and when content
reaches an agent at runtime:

**`load`** — skill content is always in the agent's context window. Use for
skills the agent genuinely needs every invocation. Principles and guardrails
belong here.

**`available`** — the skill name appears in the agent's system context, but
content loads only when the agent invokes it. The available list is the
primary discovery mechanism. Reinforce it with body text references:
"Use `/kb-conventions` for structural standards" gives the agent a concrete
trigger to load the skill.

**`model-invocable`** — the skill is globally discoverable by keyword
matching across all installed skills. This is the mechanism that makes
`available` work. Without `model-invocable: true`, an available skill is a
name the agent can see but never load.

### The Nudge Problem

Global model-invocable discovery without a direct reference rarely fires
reliably. The agent needs a reason to reach for a skill — either it's on
the available list, or the body text mentions it by name. Relying on
keyword matching alone means the skill competes with every other
model-invocable skill for attention.

**Design implications:**
- Put skills on agents' available lists as the primary trigger
- Reference skill names in agent body text as reinforcement
- Default most skills to `model-invocable: true` (enables the mechanism)
- Set `model-invocable: false` only for load-only skills that are never
  available on any agent
- Keep the global model-invocable pool small — every addition dilutes
  keyword matching for everything else

## Progressive Disclosure

Skills use a three-level content system:

1. **Metadata** (name + description) — Always in context (~100 words). This is the triggering surface.
2. **SKILL.md body** — Loaded when skill triggers (<100 lines ideal). The main content.
3. **Bundled resources** — Loaded as needed (unlimited size). Scripts execute without loading into context.

**Implications:**
- Keep SKILL.md under 100 lines. If approaching this limit, add hierarchy with clear pointers to resources.
- Put routing logic in the body, detailed content in resources
- For large reference files (>300 lines), include a table of contents

## Decompose for Progressive Loading

Fat skills are good — they carry the knowledge agents need. But they must
be decomposed so agents pick up only what's relevant, not the entire
domain.

**Body as router:** The SKILL.md body should contain the core principles
and route to resources for detailed content. An agent loading the skill
gets the principles; it loads specific resources only when the task
demands them.

**Resource granularity:** Each resource file should be independently useful.
`resources/unit-patterns.md` loads without requiring
`resources/integration-patterns.md`. If two resources always load together,
they should be one file.

**Progressive depth:** Structure resources by depth, not by topic:
- Body: what to do and when (principles, judgment heuristics)
- Resources: how to do it (patterns, examples, detailed procedures)

This lets an agent that just needs the judgment framework load the body
alone, while an agent doing the actual work loads the relevant resource.

## Skill Types

Skills serve different roles in an agent's cognitive process. The `type:`
field declares this role and controls injection order.

**Principle** — shapes how the agent thinks. Always loaded. `dev-principles`,
`llm-writing`. Background constraints active on every action.

**Guardrail** — safety boundary. Always loaded. `clear-mind`,
`shared-workspace`. Bright-line rules the agent must not cross.

**Mode-shift** — pivots what the agent is doing. Available, loaded on
demand. `/handoff` shifts to transition mode. `/prototype` shifts to
throwaway exploration. `/zoom-out` shifts to multi-angle orientation.
Same agent, different cognitive lens. Mode-shift skills are the
alternative to spawning a new agent — when the shift stays within the same
model's capability and doesn't need fresh context, loading a skill is
cheaper than a spawn.

**Checkpoint** — gates a phase transition. Available, loaded at boundaries.
`pre-dev` checks readiness before coding starts. `post-dev` checks
readiness before shipping. Convention: `pre-*` / `post-*` naming.

**Reference** — operational how-to. Available, loaded when needed.
`meridian-spawn`, `kb-conventions`. Stable procedures and tool mechanics.

## Skills Shape, Agents Act

Skills are reference material loaded into agents. They don't run independently.

**Agents:**
- Spawned as their own process
- Get their own context window
- Make decisions and produce output
- Run independently

**Skills:**
- Loaded into an agent's context
- Shape the agent's behavior
- Provide knowledge and methodology
- Don't run or decide anything themselves

Getting this wrong is costly:
- Skill where agent belongs → forces a single consumer to become a god-object
- Agent where skill belongs → spawns a whole process just to deliver reference material

## Domain Organization

When a skill supports multiple variants (frameworks, platforms, providers), organize by variant:

```
cloud-deploy/
├── SKILL.md (workflow + selection logic)
└── resources/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

The body routes to the relevant reference; the agent reads only what applies. This keeps context focused and avoids loading irrelevant variants.

## Separate Mechanism from Methodology

A skill should be either mechanism (how to operate a tool) or methodology (what to do with it), not both.

**Mechanism:** How to drive Playwright — commands, sessions, selectors, network mocking.

**Methodology:** What to test — visual regression, interaction flows, accessibility, viewport coverage.

Combining them couples the skill to one use case. Separated, the mechanism skill serves any agent that needs browser automation (testing, scraping, research), and the methodology skill works with any browser mechanism.

**Test:** Can you swap the underlying tool without rewriting the methodology? Can you apply the methodology through a different mechanism? If both answers are yes, they should be separate skills.
