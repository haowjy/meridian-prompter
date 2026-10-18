---
name: prompt-principles
type: principle
description: "Load when writing or reviewing anything an agent reads: agent prompts, skills, AGENTS.md. The principles that make it steer behavior reliably."
model-invocable: true
---

# Prompt Principles

Use `/llm-writing` alongside this skill. `/agent-artifacts` and `/skill-artifacts` cover Meridian's formats and runtime.

## Write for the Reader of Each Layer

Each layer has one reader, and its text addresses that reader:

- A **description or pointer** is read by whoever decides whether to reach the material: a caller choosing an agent, or an agent deciding whether to load a skill or open a file. It says when to reach it, what to bring, and what comes back.
- An **agent body** is read by that agent on every run. It states the job.
- A **skill body** is read by an agent partway through some other job, and the skill can't know which agent. It gives instructions that hold in any agent that loads it.
- A **resource** is read by an agent that chose to open it, at the moment it needs that depth.
- An **AGENTS.md** is read by every agent that works in its directory, before anything else there. `/qi-layer` covers how to write one.
- An **authoring guide**, like this skill, is read by the prompt's author. It says how to write the prompt, not what the running agent should do.

Text for the wrong reader fails quietly. An authoring guide phrased as agent instructions gets copied into prompts as rules; a body that explains its design to its author spends the agent's attention on nothing.

## Progressive Disclosure

Give the agent what it needs now, and let it reach the rest. Split by need. Keep the judgment and the steps every run takes in the body. Put behind a pointer what only some runs reach (a variant, an example, a procedure for one case) and depth too long to carry every time. Keep a concept's definition, rules, and caveats under one heading wherever it lands. A document too long even when every line is live thins attention: split it by branch or by sequence.

Pointers carry the design. Material behind a pointer (a skill's description, a line naming a resource or file) is reached only when the pointer's wording fires, so the wording decides reach. Say what the material is, put the word that should trigger it first, and give one trigger per distinct case; synonyms for one case are one trigger written twice. A must-have target behind a weak pointer is a variance bug: sharpen the pointer before inlining the material. Point straight to the target: a layer whose only job is routing to other layers costs navigation and rarely pays. A level earns its place when it carries content the agent acts on at that level, as in a tree of AGENTS.md files where each level summarizes its children.

## Place What Matters First

Placement and structure tell an agent what matters most. The opening gets the strongest attention and the close the second-strongest, so put purpose and the main constraint first and the reminder that matters most last; an instruction buried in the middle loses to local wording. Separate kinds of information with headers, XML tags, and short sections. Structure works where ALL CAPS, repeated "must," and emotional emphasis only add force.

## Every Line Must Change Behavior

Test each line: does removing it change how the model behaves? If not, delete the whole sentence. Models already know how to code, review, write tests, and follow instructions. Write only what steers the model away from its default or toward something non-obvious. Words that change nothing dilute the words that do. Whether a line is a no-op depends on the model's default, so settle a disagreement by running the prompt.

## Keep One Source of Truth

Put each meaning in one place, so changing a behavior is a one-place edit. The same rule in a description, a body, and a resource costs tokens, drifts apart, and weighs more than its rank; point to its home instead. The environment is a source of truth too: config, the directory layout, a tool's `--help`, guidance the harness injects. A prompt that restates it is a cache that goes stale. Write down what the agent can't find by looking: the unwritten convention, the reason behind a choice, the gotcha nothing documents. A line that no longer bears on the work is sediment; delete it when you find it, since adding feels safe and removing feels risky.

## Say What to Do

State the target behavior. Positive framing keeps the desired behavior in view; negative framing keeps the forbidden behavior active in attention. Use a prohibition for a bright line, where ruling something out is the whole point, and pair it with what to do instead.

## Give the Reason

Give the reason when the model has to apply the instruction to cases the prompt doesn't spell out. A rule without a reason is easy to follow mechanically and easy to misapply. Reasons matter most for tradeoffs, where two good principles pull apart and the model has to choose which governs. An instruction that is clear on its own needs no reason.

## Prescribe at the Right Altitude

Match prescription to fragility. Give exact steps where a mistake is irreversible or easy to make and hard to see: a destructive command, a release, output another program parses. Elsewhere, state what to optimize for, the boundaries that matter, and what done looks like, then let the model choose the path.

Fixed counts, required file names, scope fences, and procedures that always run box the model in on the work they don't fit; each one needs a reason the work supplies.

## End Each Step on a Completion Criterion

A completion criterion tells the agent when a step is done. Make it clear: a vague bound ("once you understand it") invites stopping early, pulled by the steps still ahead. Make it demanding where thoroughness matters: "every changed caller accounted for" drives work that "list the changes" doesn't. The strongest criteria are checkable and exhaustive.

## State Instructions Flat

Every condition costs reliability: the model must first decide whether it fired, and it misses conditional constraints far more often than plain ones. A fallback plants its case ("if in doubt, use X" overtriggers X), and LLM drafts add conditions by reflex.

State the default as a directive. Keep a condition only when the instruction is wrong on the other side and both sides occur, and make its trigger checkable; a condition the agent can't check ("when you think it's done," "as needed") gets guessed, usually conveniently. Delete fallbacks for cases the agent's role rules out. If the thorough path is right, make it the only path: a weaker option offered beside it becomes the default. Before cutting a condition, read the flat version as an instruction that always fires: "probe to settle findings" makes a reviewer probe a finding about file size.

## Use Leading Words

A leading word recruits a concept the model already holds, in fewer tokens than explaining it: "adversarial," "throwaway," "regression," "proof of concept." When three sentences describe a behavioral mode, look for the word that already means it. A word that restates the default ("be thorough") does nothing; a strong one shifts behavior ("relentless," "disposable"). Repeat the word, not its explanation; the same word in prompts, docs, and code also helps the agent find the material behind it.

## Encode Lessons in Structure First

A prompt line is the weakest guard: nothing fails when an agent skips it. Before writing a rule, look for a stronger home: a permission that denies the action, a frontmatter field, a script that does the step the same way every time, a check that fails loudly. When a structural fix exists, use it alone. Write the rule when the lesson needs judgment.

## Look Back for Deletions

Fixes accrete into lines that patch holes earlier lines made: an exemption
for cases a broad rule got wrong, a rule that counters another, a pointer to
a copy that drifted. After a round of changes, check each addition for this
and fix the line that made the hole; the patch goes with it.

## Keep the Core Harness-Agnostic

Load-bearing prompts (agent bodies, core skills) state intent: what to delegate, what context to pass, what the result must satisfy. Environment mechanics (CLI flags, tool names, launch commands) belong to the environment: the harness's own system prompt, or the tool's help surface the agent reads at runtime.

The test: would this prompt survive a harness swap unchanged? "Spawn a researcher in the background and collect the result before your verdict" ports; a flag plus a wait command does not. Naming *what* to compose is intent, not mechanics: the agent to staff and the skills it should carry declare the staffing and survive the test. When mechanics must be written down, contain them in one skill so a new environment swaps that skill, not every agent.

## Test on Real Runs

Review finds design flaws; only runs show behavior. Change a prompt for a failure seen in a real run or a behavior the work now needs, test the change on that task against the prompt without it, and scale the test to the change. Before testing a prompt change, load `resources/evaluation.md`: trigger tests, routing tests, and blind comparisons.

## Deeper Resources

When writing an agent (role, boundary, description, cognitive mode), load `resources/agent-level.md`. When writing a skill (its reader, extraction, loading, resources), load `resources/skill-level.md`. When writing leads or multi-agent flow (handoffs, verification, loop control, model staffing), load `resources/system-level.md`. To check the evidence behind a principle, open `resources/research.md`.
