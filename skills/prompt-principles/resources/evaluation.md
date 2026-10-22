# Evaluating Prompt Changes

Use `/prompt-principles`' Verify Proportionally guidance to choose whether
an experiment is warranted and obtain approval. This resource describes
how to gather evidence; it does not require a run for every edit.

## Observe Normal Work

For a small change, name the behavior to watch on the next relevant task.
Use that task's transcript when it becomes available; do not create extra
work solely to satisfy a testing step. Record which prompt version ran,
what the agent did, and whether the target behavior was exercised. Until
then, report the behavior as untested. A successful run shows what happened
on that task, not that the prompt caused it or will generalize.

## Design an Approved Experiment

Choose the smallest set of cases that can answer the approved question.
Include a near-miss or another task when it distinguishes plausible failure
modes; a wording change or new description does not trigger a fixed matrix.
Keep candidate runs, reruns, additional cases, and judge launches within
the approved scope. Obtain approval for a scope extension before proceeding.

## Start From What the Change Should Fix

State the observed failure or needed behavior and what result would settle the question. A fix drawn from one session may fit only that session; include another task when the experiment needs to establish generalization.

## Compare Against a Baseline

Run the same task with and without the change, on the model family the prompt targets. Without the baseline you can't tell the change's effect from what the model does by default. Record the model, harness, and date: behavior shifts between versions.

## Test Triggers and Routing

- **Skill descriptions:** write realistic requests that should load the skill and near-misses that shouldn't, and check which load it. A skill that loads and is then ignored failed too.
- **Agent descriptions:** give a cold caller representative tasks and the neighboring agents, and check that it picks the right one.

## Keep Candidates Blind

An agent that knows it's being tested behaves differently.

- Give candidates an organic task, what a user would type. Hide the evaluation itself from every prompt, file, and directory name a candidate sees: that it's a test, which variant it is, how it will be scored. Words and paths that belong to the real task stay, even when the task is about tests.
- Don't tell a candidate that other candidates exist, and don't ask it to list what it applied.
- Write a rubric of three to six concrete criteria for the judge, and keep it from the candidates.
- Run the judge on a model family other than the candidates'. It sees outputs under neutral labels, never model names, and scores every variant in one pass on one scale.

## Grade From Evidence

Grade what the agent did from its transcript and output: which files it opened, what it ran, what it produced. Its own account of what it followed is a claim, not evidence. Read every output yourself; when you disagree with the judge, suspect the rubric first.

## Edit Prompts in Their Own Change

Fix a misbehaving prompt in its own change, not in the middle of other work: an edit tangled into a feature can't be reviewed or evaluated.
