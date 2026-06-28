# Prompt-Level Principles

Use prompt text to steer behavior, not to narrate process. A good prompt keeps the target behavior easy to notice, the boundaries easy to remember, and the tradeoffs easy to apply in nearby cases.

## Attention Is a Scarce Resource

Keep prompts concise because every extra sentence competes with the instructions that matter. Add detail when it changes behavior, clarifies a boundary, or reinforces something the model is likely to miss. Put purpose and the main constraint near the beginning, because the opening gets the strongest attention, and close with the reminder that matters most. If the core instruction is buried in the middle, the model often follows local wording instead of the governing frame.

## Structure Is Stronger Than Emphasis

Use visible structure to separate kinds of information. Headers, XML tags, short sections, and well-grouped paragraphs help the model keep role, workflow, and constraints distinct. This works better than ALL CAPS, repeated "must," or emotional emphasis, which add force without adding clarity. When a prompt feels like one long blob, the model has to infer the structure for itself, and that is where drift starts.

## Direct Language Transfers Better

Say what to do, not just what to avoid. Positive framing keeps the desired behavior in view, while negative framing often keeps the forbidden behavior active in attention and produces acknowledgment instead of omission. Use negative phrasing for bright-line prohibitions and protected boundaries, where ruling something out is the whole point. In most other cases, direct statements of the target behavior are easier to follow and easier to generalize.

## The Model Needs Reasons, Not Just Rules

Explain why when the reason helps the model apply the instruction correctly in cases the prompt does not spell out. A rule without a reason is easy to follow mechanically and easy to misapply. A rule with a reason gives the model a basis for judgment. This is especially important for tradeoffs such as staying concise, keeping orchestration altitude, or preferring explicit artifacts at handoff boundaries.

## Give Heuristics at the Right Altitude

Tell the model what to optimize for, when that guidance applies, and what failure mode it prevents. That is usually better than either writing a rigid script or staying at the level of slogans. Over-sequenced prompts become brittle and encourage cargo-cult execution. Under-specified prompts leave too much room for interpretation. Good prompt text gives a usable decision rule.

## Layer Information On Purpose

Descriptions, bodies, skills, and resources each have a different job. The description helps a caller decide whether to use the artifact. The body defines the behavior that should stay in the active prompt. Skills and resources carry shared depth. When the same explanation is repeated at every layer, the artifact gets longer without becoming clearer. When the layers are too thin, the model loses the reasoning it needs to transfer the guidance.

## Weak Options Become Default Options

Treat escape hatches carefully. If the thorough path is the right path, make it the only path instead of offering an easier fallback that the model will prefer. The same rule applies to filler. Words that do not change behavior dilute the words that do. Tight prompts are not just shorter; they are harder to misread.
