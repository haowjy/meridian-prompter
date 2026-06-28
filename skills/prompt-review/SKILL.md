---
name: prompt-review
type: reference
description: >
  Load when reviewing agent definitions or skill content. Adversarial
  review methodology — finding quality, severity, and structured reporting.
model-invocable: false
---

# Prompt Review

Find what's wrong, not confirm what's right.

The writer already believes their agent works. Your value comes from
challenging that assumption — the principle violation they didn't notice,
the ambiguity that will confuse the model, the scope creep that dilutes
focus.

Review prompt quality first. That is the main job.

## Good Findings

Each finding: what's wrong (reference the line), why it matters (the failure
mode), and what to do about it. Prioritize things that require understanding
principles and intent over surface issues.

## Severity

- **Blocking** — Must fix. Violates core principles, creates real failure modes.
- **Substantive** — Should fix. Weakens design, causes confusion, reduces reusability.
- **Minor** — Consider fixing. Polish, clarity, nice-to-haves.

Lead with blocking issues.

## What to Look For

How does this agent fail? What happens with ambiguous input, missing context,
conflicting skills? Which principles does it violate and what breaks?

Check for LLM writing patterns that weaken prompts: overcorrected guidance
encoding "stop doing X" as absolute prohibition, contrastive definitions
("not X — it's Y") that only make sense in a conversation, prescriptive
checklists where a principle would transfer better, labeled conclusions
that restate what the examples already showed.

After the prompt-quality pass, do a lighter mechanics pass when relevant. For
that second angle, load `resources/mechanics.md`.

## Report

1. Overall assessment
2. Findings by severity
3. Verdict: approve, approve with notes, or request changes
