# Skill-Level Principles

Skills exist to hold reusable knowledge without bloating every agent that needs it. The goal is not extraction for its own sake. The goal is to keep shared method stable, loadable, and easy to maintain.

## Extract for Reuse, Not for Tidiness

Move something into a skill when multiple agents need the same knowledge or method. If only one agent needs it, keeping it in the body is usually simpler because there is only one place to maintain. Extracting single-use content often feels cleaner, but in practice it creates a second surface without creating real reuse. The test is whether multiple agents would get lighter and clearer if the content moved out.

## Loading Is Part of the Design

`load`, `available`, and `model-invocable` are operating mechanics, not descriptive labels. `load` keeps a skill in the prompt every run, so it should be reserved for knowledge the agent genuinely needs all the time. `available` makes the skill visible for on-demand use. `model-invocable` determines whether that on-demand loading can actually happen. If these do not line up, the agent ends up seeing names it cannot use or competing against too much global skill noise. Good skill design includes designing how the agent will discover and load the skill, not just what the skill says.

## The Top Layer Should Route, Not Teach the Whole Domain

The skill body should carry the core guidance and point to deeper resources. Examples, variants, long procedures, and edge-case mechanics belong lower in the skill. This keeps the always-loaded layer compact while preserving depth when the task actually needs it. When too much lives in the top layer, every consumer pays for the full domain even when it only needs a narrow slice.

## Decompose So Agents Can Load Selectively

A skill should let an agent load only the part that matters. Split resources by real usage boundaries, not just by topic names. If two files are always loaded together, they probably want to be one file. If one file mixes several different use cases, agents will keep loading irrelevant context just to reach the one paragraph they needed. Good decomposition reduces noise without hiding the path to the right depth.

## Skills Teach; Agents Decide

Skills provide method, judgment criteria, vocabulary, and durable reference material. Agents apply that guidance to a concrete situation, make decisions, and produce outputs. Mixing those roles causes problems both ways. Agents become bloated when they carry all shared method inline, and skills become pseudo-agents when they start trying to own decisions that belong to the active worker.

## Separate Mechanism from Method

Keep tool operation separate from guidance about how to use the tool well. Mechanism tends to be reusable across many tasks, while method depends on what the worker is trying to accomplish. When those are fused together, neither part travels well. When they are separate, a tool skill can support many methodologies and a methodology skill can survive a tool change.
