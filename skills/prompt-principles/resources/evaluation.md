# Evaluating Prompt Changes

A prompt change affects every future run, so test it like an experiment, at the scale of the change. A wording fix needs a careful read and one run. A new rule, a changed trigger, or a changed description needs the cases below.

## Start From What the Change Should Fix

Change a prompt for a failure seen in a real run (what ran, what the agent did, what you expected) or for a behavior the work now needs, and state it before editing: it's what the test checks. A fix written from one bad session tends to fit that session; run it on other tasks before keeping it, or over many edits the prompt drifts.

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
