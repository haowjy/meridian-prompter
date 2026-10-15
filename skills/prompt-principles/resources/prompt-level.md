# Prompt-Level Principles

Use prompt text to steer behavior, not to narrate process.

## Attention Is Positional

The opening gets the strongest attention; the close is the second-strongest. Put purpose and the main constraint near the beginning. Close with the reminder that matters most. When the core instruction is buried in the middle, the model follows local wording instead of the governing frame.

## Structure Is Stronger Than Emphasis

Use visible structure to separate kinds of information. Headers, XML tags, short sections, and well-grouped paragraphs help the model keep role, workflow, and constraints distinct. This works better than ALL CAPS, repeated "must," or emotional emphasis, which add force without adding clarity.

## Direct Language Transfers Better

Say what to do, not just what to avoid. Positive framing keeps the desired behavior in view, while negative framing often keeps the forbidden behavior active in attention. Use negative phrasing for bright-line prohibitions, where ruling something out is the whole point. Direct statements of the target behavior are easier to follow and easier to generalize.

## The Model Needs Reasons, Not Just Rules

Explain why when the reason helps the model apply the instruction correctly in cases the prompt does not spell out. A rule without a reason is easy to follow mechanically and easy to misapply. A rule with a reason gives the model a basis for judgment. This matters most for tradeoffs, when two good principles pull in different directions and the model needs to choose which one governs.

## Give Heuristics at the Right Altitude

Tell the model what to optimize for, when that guidance applies, and what failure mode it prevents. Over-sequenced prompts become brittle and encourage cargo-cult execution. Under-specified prompts leave too much room for interpretation. Good prompt text gives a usable decision rule.

## Layer Information On Purpose

Descriptions, bodies, skills, and resources each have a different job. The description helps a caller decide whether to use the artifact. The body defines the behavior that should stay active every run. Skills and resources carry shared depth. When the same explanation appears at every layer, the artifact gets longer without becoming clearer.

## Use Leading Words

A leading word is a compact concept from the model's pretraining that anchors behavior in fewer tokens than explaining the idea from scratch. Words like "adversarial," "throwaway," "regression," or "proof of concept" recruit priors the model already holds. One token does the work of a paragraph. When you find yourself writing three sentences to describe a behavioral mode, look for a single word that already carries that meaning. A weak leading word that restates the default ("be thorough") is a no-op; a strong one shifts behavior ("relentless," "disposable").

## Weak Options Become Default Options

Treat escape hatches carefully. If the thorough path is the right path, make it the only path instead of offering an easier fallback that the model will prefer. Words that do not change behavior dilute the words that do. Tight prompts are not just shorter; they are harder to misread.

## State Instructions Flat

Every condition costs reliability. On AgentIF (NeurIPS 2025), frontier models met conditional constraints 15 to 21 points less often than plain ones (Claude 4 Sonnet: 83.6% vs 62.2%), because the model must first decide whether the condition fired. Anthropic's Claude guidance reports that "If in doubt, use [tool]" causes overtriggering: a fallback plants its case. LLM drafts add conditions by reflex ("spawn a reviewer only when the merge crosses an expensive seam," "re-review only if the fix touched the blocked path," "if the user declines, keep going"), and each one turns a rule into a judgment call.

State the default as a directive. Keep a condition only when the instruction is wrong on the other side and both sides occur, and make the trigger checkable; a condition the agent can't check ("when you think it's done," "as needed") gets guessed, usually conveniently. Delete fallbacks for cases the agent's role rules out. Before cutting a condition, read the flat version as an instruction that now always fires: "probe to settle findings" makes a reviewer probe a finding about file size, and "retry a failed fix on Opus" escalates a fix that failed on a bad brief.
