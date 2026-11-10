---
name: prompt-principles
description: "Load when writing or reviewing anything an agent reads: agent prompts, skills, AGENTS.md. The principles that make it steer behavior reliably."
model-invocable: true
metadata:
  type: principle
---

# Prompt Principles

Use `/llm-writing` alongside this skill. `/agent-artifacts` and `/skill-artifacts` cover the package formats and runtime.

These principles assume a strong model: one that already codes, reviews, plans, interviews and tests well, and follows what it reads closely and as written. Most of the work is deleting what such a model doesn't need, and saying the rest so it can't be misread.

## Write for the Reader of Each Layer

Each layer has one reader, and its text addresses that reader:

- A **description or pointer**: whoever decides whether to reach the material. It says when to reach it, what to bring, and what comes back.
- An **agent body**: that agent, every run. It states the job.
- A **skill body**: an agent partway through some other job, which the skill can't know. Its instructions hold in any agent that loads it.
- A **resource**: an agent that chose to open it, when it needs that depth.
- An **AGENTS.md**: every agent working in its directory, first (`/qi-layer`).
- An **authoring guide**, like this skill: the prompt's author. It says how to write the prompt, not what the running agent does.

Text for the wrong reader fails quietly: an authoring guide phrased as agent instructions gets copied into prompts as rules, and a body that explains its design to its author spends the agent's attention on nothing.

## Progressive Disclosure

Keep in the body the judgment and the steps every run takes. Put behind a pointer what only some runs reach (a variant, an example, a procedure for one case) and depth too long to carry every time. Keep a concept's definition, rules and caveats under one heading wherever it lands.

Material behind a pointer is reached only when the pointer's wording fires, so the wording decides reach. Say what the material is, put the word that should trigger it first, and give one trigger per distinct case. A must-have target behind a weak pointer is a variance bug: sharpen the pointer before inlining the material. Point straight to the target; a layer whose only job is routing to other layers costs navigation and rarely pays.

## Place What Matters First

The opening gets the strongest attention and the close the second-strongest, so put purpose and the main constraint first and the reminder that matters most last; an instruction buried in the middle loses to local wording. Separate kinds of information with headers, XML tags and short sections. Structure adds weight where ALL CAPS, repeated "must" and "CRITICAL" don't: on current models that emphasis makes an instruction overtrigger.

## Every Line Must Change Behavior

Test each line: does removing it change what the model does? If not, delete the whole sentence. Write only what steers the model away from its default or toward something non-obvious; words that change nothing dilute the words that do. Whether a line is a no-op depends on the model's default, so settle disagreements with observed behavior.

Fixes accrete into lines that patch holes earlier lines made: an exemption for cases a broad rule got wrong, a rule that counters another, a pointer to a copy that drifted. After a round of changes, fix the line that made the hole, and the patch goes with it.

## Keep One Source of Truth

Put each meaning in one place, so changing a behavior is a one-place edit. The same rule in a description, a body and a resource costs tokens, drifts apart, and weighs more than its rank; point to its home instead. The environment is a source of truth too: config, the directory layout, a tool's `--help`, guidance the harness injects. A prompt that restates it is a cache that goes stale. Write down what the agent can't find by looking: the unwritten convention, the reason behind a choice, the gotcha nothing documents.

## Name What to Do, and What to Avoid Exactly

State the target behavior. When something must be ruled out, name it exactly: current models avoid a named pattern ("no pill-shaped buttons," "don't end the turn by announcing the next step"), while a vague prohibition ("avoid a generic look") only swaps one default for another.

## Give the Reason

Give the reason when the model has to apply the instruction to cases the prompt doesn't spell out, and above all for tradeoffs, where two good principles pull apart. An instruction that is clear on its own needs no reason.

A rule without its scope and reason is followed everywhere. Cautions pile up in notes, memory and instruction files, and current models obey them: they ask for approvals they don't need and hold back routine work. Write an absolute rule with the scope it covers and why, write its exception into the rule itself, and name the exact actions an approval rule covers. Delete a caution whose reason no longer holds.

## Prescribe at the Right Altitude

Give exact steps where a mistake is irreversible or easy to make and hard to see: a destructive command, a release, output another program parses. Elsewhere, state what to optimize for, the boundaries that matter, and what done looks like, then let the model choose the path. Fixed counts, required file names, scope fences and procedures that always run box the model in on the work they don't fit; each one needs a reason the work supplies.

## End Each Step on a Completion Criterion

A completion criterion tells the agent when a step is done. Make it clear: a vague bound ("once you understand it") invites stopping early. Make it demanding where thoroughness matters: "every changed caller accounted for" drives work that "list the changes" doesn't.

## State Instructions Flat

The model must first decide whether a condition fired, and it misses conditional constraints far more often than plain ones. A fallback plants its case ("if in doubt, use X" overtriggers X). State the default as a directive. Keep a condition only when the instruction is wrong on the other side and both sides occur, and make its trigger checkable; "when you think it's done" gets guessed, usually conveniently. If the thorough path is right, make it the only path: a weaker option offered beside it becomes the default. Before cutting a condition, read the flat version as an instruction that always fires.

## Use Leading Words

A leading word recruits a concept the model already holds, in fewer tokens than explaining it: "adversarial," "throwaway," "regression," "proof of concept." When three sentences describe a mode, look for the word that already means it. Repeat the word, not its explanation.

## Say Who Owns the Work

Told nothing about ownership, a coding agent adds beside the existing structure and reports nearby problems; told the code is its own, it merges repeats and fixes what it finds, at more tokens and with some changes nobody asked for. State ownership where you want restructuring, and leave it out where the owner wants minimal change.

A prompt that invites subagents gets them, and they can be most of a session's cost. Ask for one where the work needs it, and say what it adds.

## Encode Lessons in Structure First

A prompt line is the weakest guard: nothing fails when an agent skips it. Before writing a rule, look for a stronger home: a permission that denies the action, a frontmatter field, a script that does the step the same way every time, a check that fails loudly. When a structural fix exists, use it alone. Write the rule when the lesson needs judgment.

## Keep the Core Harness-Agnostic

Agent bodies and core skills state intent: what to delegate, what context to pass, what the result must satisfy. CLI flags, tool names and launch commands belong to the harness's own prompt or the tool's help. The test: would the prompt survive a harness swap unchanged? When mechanics must be written down, contain them in one skill.

## Verify Proportionally

Read the final diff and the instructions around it for contradictions, broken pointers and unintended scope; for a small, reversible edit that read is the check. Real-task runs are the behavioral evidence: name what to watch on the next relevant task, and keep behavior seen in a transcript apart from behavior not yet exercised. A dedicated experiment needs the user's approval of its question and scope; to design one, open `resources/evaluation.md`.

## Deeper Resources

When writing an agent (role, boundary, description, cognitive mode), load `resources/agent-level.md`. When writing a skill (its reader, extraction, loading, resources), load `resources/skill-level.md`. When writing leads or multi-agent flow (handoffs, verification, loop control, model staffing), load `resources/system-level.md`. For the evidence behind a principle, open `resources/research.md`.
