---
name: grill-me
description: Relentless interview that sharpens a half-formed idea, plan, or decision until it is committable. Models the problem as a design tree and works the frontier in rounds - questions asked in batches, each carrying a recommended answer, dependency-ordered so nothing is asked before its prerequisites are settled. Checkpoints every round to a markdown file so long sessions survive context loss, then closes with a pre-mortem that converts failure modes into binary pass/fail criteria. Use this when someone says help me think this through, poke holes in this, stress-test this plan, ask me the hard questions, or I am not sure what I am building yet. Use it too when a plan is about to be built and nobody has stated what would make it fail. Do not use it to review finished work, to write the plan itself, or when the decision is already made.
license: MIT
compatibility: Standalone. Needs no repository, no MCP server, and no particular project layout. Writes one checkpoint file to a location you choose.
allowed-tools: "Read Write Glob Grep"
metadata:
  author: "Keith Crawford"
  version: "1.0.0"
  source-canon: "grill-me"
  ported: "2026-08-29"
---

# grill-me

Interrogate a half-formed idea until its shape is clear enough to commit to.

## When To Use

- An idea, plan, or decision is real enough to discuss but too vague to build.
- A plan is about to be built and nobody has stated what would make it fail.
- Someone asks to have their thinking stress-tested rather than summarized.

Do not use this to review finished work, to write the plan itself, or where the decision is already made and only needs recording.

## Definitions

Use these terms exactly. Do not substitute synonyms.

- **design tree** - the decision structure for the topic. Every decision branches into the decisions that depend on it.
- **frontier** - every decision whose prerequisites are already settled. These are the questions answerable now without guessing at answers not yet heard.
- **round** - one batch of frontier questions, asked together, answered together.
- **checkpoint** - the markdown file recording settled decisions, the question log, and open flags.
- **pre-mortem** - the closing pass that imagines the idea shipped and failed.
- **criterion** - one binary pass/fail statement produced by the pre-mortem.

## Procedure

### Step 1 - Establish the topic

If the invocation includes a topic, use it. If the invocation is bare, ask what to grill, then continue.

### Step 2 - Create the checkpoint

Derive a slug from the topic. Lowercase, hyphen-separated, at most four words.

Ask where the checkpoint should go. If the user does not care, write `grill-{slug}.md` to the working directory. If the project has an obvious home for working notes - a `docs/`, `notes/`, or `scratch/` directory that already exists - offer that instead. State the chosen path before continuing.

Create the checkpoint with four headings: `## Shape & Settled Decisions`, `## Question Log`, `## Open Flags`, `## Criteria`.

### Step 3 - Run the shape check

If the category of the thing is ambiguous, propose two or three candidate shapes.

Ask discriminating questions until one shape survives.

If the category is already obvious, skip this step.

### Step 4 - Build the design tree

Identify the decisions the topic depends on.

Order the decisions by dependency. A decision whose answer depends on an unsettled decision is not on the frontier.

### Step 5 - Find facts before asking

Finding facts is your job, never the user's.

If a frontier question needs a fact from the codebase or the filesystem, use Grep, Glob, or Read to find it.

Ask the user only when the environment cannot answer the question, or when the answer is a preference rather than a fact.

Read the files directly rather than dispatching subagents. It is cheaper and it keeps the interview in one context.

### Step 6 - Ask the round

Compute the frontier. Ask every frontier question in one round.

Format each question this way:

```text
**Q1 - <question title>**

<question body, including the real alternatives>

**Recommended:** <the answer you would pick, and why in one line>
```

Lead with a recommendation on every question. Never ask a bare open question.

If a recommendation is low-confidence or the decision is high-stakes, add the single strongest objection to that recommendation on the line below it.

If exactly one question is blocking and its answer space is bounded, use your runtime's structured multiple-choice prompt if it has one, with the recommendation as the first option.

Wait for answers. Do not proceed to the next round unprompted.

### Step 7 - Checkpoint the round

Append each question and its answer to `## Question Log`.

Promote each settled decision to `## Shape & Settled Decisions`.

Record anything needing external input under `## Open Flags`.

Write the checkpoint before asking the next round.

### Step 8 - Recompute and repeat

Each answer settles a decision and pushes the frontier outward.

Recompute the frontier. Return to Step 6.

### Step 9 - Stop

Stop when any one of these is true:

- The frontier is empty. Every branch is visited and nothing is silently assumed.
- Twelve questions have been asked. Surface the checkpoint and ask whether to continue.
- Two consecutive answers are low-signal ("I don't know", "skip"). Record both under `## Open Flags` and stop.

### Step 10 - Run the pre-mortem

Ask: imagine this shipped and failed. What went wrong?

Convert each failure mode into one binary criterion. A criterion is testable, not aspirational.

Write the criteria to `## Criteria`.

### Step 11 - Hand off

Name what should happen next and stop. Do not do it.

| The grilled shape needs | Say so and stop |
| --- | --- |
| A written design or decision record | The shape and criteria are the input to it |
| Issue or ticket tracking | The settled decisions are the scope |
| Implementation | The criteria are the acceptance tests |
| More thinking, not more structure | The open flags are what is still missing |

Do not act on the grilled plan until the user confirms you have understood it the same way they do.

## Output

One checkpoint file at the path agreed in Step 2, containing the settled shape, the full question log, open flags, and the pre-mortem criteria.

No other file is created or modified.

## What This Skill Does NOT Do

- Does not write code, specifications, design documents, or tickets.
- Does not edit existing files. Only the checkpoint is written.
- Does not carry out the next step it names.
- Does not proceed past a round without an answer.
- Does not structure thinking you have already done. This finds out what the thinking is, which is the step before that.
- Does not look backward at finished work. It looks forward at work not yet started.

## Gotchas

- **A session with no disagreement means the skill was not needed.** If the user accepts every recommendation without pushback, the idea was already clear. Say so and stop early rather than manufacturing rounds.
- **Some questions cannot be grilled.** "How should this feel?" needs a prototype, not a discussion. When a question is only answerable by building a throwaway version, record it under `## Open Flags` and say so instead of asking it.
- **Batched rounds fail when the tree is shallow.** If the frontier holds one question for three rounds running, the topic is a single decision. Ask it directly and finish.

*`grill-me` by [Keith Crawford](https://keithcrawford.me), from [github.com/tsudo/skills](https://github.com/tsudo/skills). Copyright (c) 2026 Keith Crawford. `SPDX-License-Identifier: MIT` — full text in [LICENSE](https://github.com/tsudo/skills/blob/main/LICENSE).*
