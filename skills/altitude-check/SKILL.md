---
name: altitude-check
description: Assess one body of work against its own stated goal and name the single next thing to do, reading the decisions taken since the plan was written so a choice that cut the spine of the plan gets caught while every task still looks healthy. Use this when someone asks to zoom out, where they stand, what to work on next, or whether this is still the right work. Not for ranking a whole board by priority or assessing two separate bodies of work at once.
license: MIT
compatibility: Works with or without an issue tracker. Given one - Linear, Jira, GitHub Issues - it reads a parent issue and its children; given none, it works from a plan, a task list, a pasted board export, or the session so far. Checks the tracker cannot answer are reported as not applicable rather than skipped. A read-only source is fine, since it proposes changes rather than making them. Writes a file only if you ask for one.
metadata:
  author: "Keith Crawford"
  version: "1.1.1"
  source-canon: "altitude-check"
  ported: "2026-08-29"
---

# altitude-check

Zoom out on one body of work and name the next thing to do.

## When To Use

- A long session has drilled into narrow sub-tasks and the goal has gone out of view.
- Work is being picked back up after a gap, with no confidence that what is in progress is still the right thing.
- A session is about to be committed to something and the next move has not been chosen deliberately.
- Someone asks whether the current work is still worth doing.

Do not use this to order a whole board by priority, to review a session backward for learnings, or to look at two separate bodies of work in one run.

## Definitions

**Workstream.** One body of work with a goal and a set of open pieces. Usually a parent issue and its children, because a tracker already gives you identity, states, and dependency links for free. Sometimes just the plan and the pile of work in front of you. Either is enough to run against; a tracker only makes more of the checks answerable.

## Core Idea

**The reconciliation is the input, not the output.** Finding out what is inconsistent does not tell you what to work on. Three phases, and the first two exist to earn the third.

| Phase | Question | Output |
| --- | --- | --- |
| A - Reconcile | What is actually true? | Findings, tagged and evidenced |
| B - Assess | Does the open work still serve the goal? | A verdict per check |
| C - Recommend | What should be worked on next? | One next thing, with its reason |

## What You Need

Three things, in descending order of how hard they are to substitute:

1. **A goal.** An observable end state for this body of work. Without it, Phase B has nothing to judge against and the run produces noise that reads like signal. If none exists in writing, elicit one before assessing.
2. **The open work.** Whatever form it takes: a tracker query, a task list, a plan, the session so far.
3. **The decisions made since the plan was written.** This is the one people skip, and it is where the expensive findings live.

Anything missing is worked around, not faked. Say which of the three you had.

## Procedure

### Step 1 - Resolve what you are assessing, and how this project writes things

Take the target from the invocation. If it is ambiguous, ask. Do not infer it from whatever the session happens to have been discussing most recently, because the wrong target produces a confident assessment of the wrong thing.

**Then go looking for the project's document conventions, before drafting anything.** Check `CLAUDE.md`, `AGENTS.md`, `STYLE.md`, `CONTRIBUTING.md`, and any `docs/style` file. Where a project states conventions, they outrank everything this skill says about shape: heading case, spelling, date format, filename, and whether tables are used at all. `## Output` below specifies which sections to produce, never how to format them.

Do this first rather than at the point of writing. Conventions change how the whole document gets drafted, and discovering them at the end means rewriting it.

If the project states nothing, write plainly: lead with the conclusion, no filler transitions, no marketing register, concrete over abstract.

### Step 2 - Establish the goal

In order of preference:

- **A prior altitude note, if one exists and the user points you at it.** Read the goal and the exclusions straight out of it, and note anything that has visibly changed since.
- **A written plan or design document**, where it states an end state rather than a list of tasks. Read the goal *and* the exclusions verbatim: a plan's out-of-scope section is often the only place the exclusions are written down, and it is what makes half the findings possible.
- **The parent issue or project description**, where one states an end state.
- **Ask.** Three questions, one at a time, answers recorded verbatim:
  1. Why does this body of work exist?
  2. What does winning look like? An observable end state, not a task list.
  3. What keeps getting pulled in that should stay out?

Verbatim matters on every path that has words to copy. A paraphrase at the source compounds through everything downstream.

**A vague goal is a stop condition, not an inconvenience.** If what you get back reads as an aspiration or a restatement of the task list, repair it with the user before going further. Six of the eight checks below compare open work against it.

**If there is nobody to ask** - a scheduled or single-shot run - you have two moves and they are not interchangeable:

- **Nothing states a goal, but the evidence implies a specific one.** Reconstruct it from what you can read: the title, recent comments, the decision log. Then label it unconfirmed in the output, say what you built it from, and make confirming it the first open question. An assessment against a labelled reconstruction is useful. The label is what makes it honest.
- **What you find is vague, and no evidence sharpens it.** Do not assess. Report that the goal is not specific enough to judge against, quote what you found, and say what a usable version would need.

A confident assessment against a vague or silently-invented goal is the worst thing this skill can produce, because it reads exactly like a good one.

**A reconstructed goal calls for more suspicion of your own findings, not less.** You wrote the thing the work is being measured against, so findings against it are partly findings against your own reading. Say so where it matters.

### Step 3 - Read the open work

Pull what is open, its states, any dependency links, and recent activity.

**Scope the query to this body of work.** A whole-board pull on an active tracker is large enough to blow a context or token limit, and it arrives as a stall rather than an error.

**Distinguish missing work from thin detail.** If some of the work is invisible to you - a query that only returned part of it, a board you have partial access to - say so and stop, because an assessment built on half the work looks exactly like a good one. If all of the work is visible but thinly recorded, which is the normal case for a plan or a task list, carry on: say up front what fidelity you had, and tag what you deduce as `Inferred`.

### Step 4 - Find and read the governing decisions

**Go looking. Do not wait to be handed a list.** Scan the documentation directories for anything recording decisions about this work: decision logs, design documents, architecture notes, RFCs, a project README, meeting notes, linked analysis. Read what is dated after the plan was made.

This is the step that gets skipped, and skipping it is what makes the whole run worthless. The failure is specific: a decision changed the shape of the plan, every open task still looks individually healthy, and an assessment that never opened the decision log reports everything fine. Directory listing is cheap. That outcome is not.

If the project genuinely records no decisions anywhere, say so explicitly. An unstated absence looks exactly like a check that passed.

### Step 5 - Reconcile in three directions

All three, every run. Where a direction has no input, report that rather than dropping the row.

| Direction | Looks for |
| --- | --- |
| Goal to open work | Intent that nothing on the list reflects. Scope with nothing behind it. Things declared out of scope that are being worked anyway |
| Open work to goal | Work nobody scoped. Items added since the plan. Finished work whose outcome changes what winning means |
| Both to decisions | Choices recorded since the plan that neither the goal nor the open work has absorbed |

The third catches the expensive failure. The first is what a person already does by eye, and is the least valuable of the three.

### Step 6 - Assess against the goal

Run every check. Each returns a finding or an explicit `clear`. A silent skip is indistinguishable from a pass.

| Check | Question |
| --- | --- |
| Goal service | Does each open item move toward what winning looks like? |
| Coverage gap | Is there anything winning requires that no item covers, open or finished? |
| Critical path | Which chain of dependent work is longest to winning? |
| Phantom blockers | Is anything waiting on something already finished or abandoned? |
| Stalls | What has been in progress with no movement and no comment for longer than this work's normal rhythm? |
| Work-in-progress load | How many things are in flight at once, against how many this team actually finishes? |
| Priority drift | Does each priority still match what waits on it? |
| Right work now | Is what is in progress the thing that should be in progress? |

**Where the source cannot answer a check** - no priority field, no dependency links, no timestamps - record `n/a, no X available`. That is a verdict. Reporting `clear` for a check you could not run is the failure this rule exists to prevent.

Phase A feeds this. A finding that a decision landed and nothing reflects it usually becomes a coverage gap here.

Judge against the goal, not against what is comfortable. **An assessment that never contradicts the plan is not an assessment.**

### Step 7 - Recommend

- **Next thing.** One item, with the single reason it beats the runner-up. A choice, not a ranked list. If the answer is "carry on with what is already in progress," say that outright rather than leaving the section off.
- **What comes after it.** Two to four items in dependency order.
- **Stop.** Anything in progress that should not be, with the reason.
- **Create.** Work the goal needs that nothing covers. On a writable tracker, file it with its dependency recorded. Otherwise write a complete specification per item - title, why the goal needs it, what blocks it, what it blocks, proposed priority - and say plainly that none of it is filed.
- **Re-rank.** Priority changes, each justified by what now waits on the item.

### Step 8 - Present, and write only if asked

Show the findings and the recommendation together. Tag each Phase A finding `Verified` if you read it in the source, or `Inferred` if you deduced it from titles, states, or dates. Every recommendation carries its reason.

**A hygiene fix is a tracker-only thing, and it is narrow:** clearing a dependency on something already finished, or correcting a state the tracker itself contradicts. `Verified` ones can be applied without asking, **in an interactive run only** - see the non-interactive rule two paragraphs down, which overrides this one entirely. Everything else - creating work, changing a priority, changing a state, anything judgement-shaped - stops for explicit approval.

**Never edit the user's own files on this authority.** Correcting a plan document, a README, or a design note is not hygiene however obviously right it looks, because those are the source you were reading rather than a tracker's bookkeeping. Propose the edit and let them make it. This skill never mutates a tracker, and never touches a document, on its own authority.

**In a non-interactive run** - a scheduled job, a single-shot invocation, anything with no turn to answer in - there is nobody to approve anything. Present the whole thing in one pass and change nothing at all, hygiene fixes included. List what you would have applied so a person can approve it later.

**Write a file only if the user wants one.** If they do, put it where they say; where nobody can be asked, put it beside the project's other documents and say where you put it. Follow the conventions found in Step 1, and never overwrite an earlier one - the difference between two of these is worth more than either alone. The section set is in `## Output` below.

## Output

In the session, always. In a file, on request. **These are sections, not a format** - render them however the project writes documents.

- **What this was judged against** - the goal and the exclusions, and where they came from. Mark a reconstructed goal as unconfirmed. Where they were elicited in-session rather than read, write them out in full, because otherwise they are gone when the session ends.
- **What you had to work with** - which of the three inputs were available and at what fidelity, in a line. A reader cannot weigh the assessment without it.
- **Where it stands** - one paragraph on where the work actually sits, in goal terms. Prose about position, not a list of what each item is doing.
- **Findings** - grouped by reconciliation direction, however many each produced. Each carries its evidence and its `Verified` or `Inferred` tag.
- **Assessment** - all eight checks, each with its verdict, including the `n/a` and split ones.
- **Recommendation** - the next thing and why it beats the runner-up, what comes after, what to stop, what to create, what to re-rank.
- **Open questions** - decisions not yet made that shape what comes next, each with its options.
- **Pickup line** - two or three lines someone can start the next session from, leading with the next thing and the one reason for it.

## What This Skill Does NOT Do

- **Order a whole board.** Ranking everything by priority, dependency, and size has no goal to judge against. This judges one body of work against its own stated end state, which is why it can conclude that real, well-formed work should stop. Ranking cannot reach that conclusion.
- **Look backward at a session for learnings.** This is about position and next action.
- **Decide the open questions.** It surfaces them with their options and leaves the choice with the user.
- **Change anything unattended.** Every create, re-rank, relation fix, and state change needs its own approval.
- **Assess two bodies of work at once.** Neither goal gets judged properly.
- **Maintain a filing system.** It reads a prior note if you have one and writes a new one if you ask. It does not own a directory, a naming scheme, or a chain.

## Gotchas

- **A vague goal makes the assessment impossible.** Goal service and coverage gap both compare open work against it. This is the single most likely reason a run produces nothing useful, and the fix is upstream in Step 2, not in working harder at Step 6.
- **Eight `clear` verdicts on months-old work is a signal, not a clean bill of health.** Two causes needing different fixes: either the goal is too loose to judge against, or the run coasted. Read the goal before assuming the first. On a sharp, observable goal, eight clears means somebody did not really look.
- **Findings on all eight is the other suspicious result, and it is the more dangerous one.** Especially on a first run against a goal you reconstructed yourself: you wrote the ruler, then found everything failed to measure up. Before reporting it, check that each finding traces to something you read rather than to how you phrased the goal. An over-call reads as thoroughness, which is why nobody catches it.

- **Write a file only when asked.** Most runs end in the session; that is the point of being able to run this in the middle of one. Someone asking where they stand has not asked for a document.
- **The recommendation is a choice, not a menu.** Handing back five ranked options returns the judgment to the user, which is the work this skill exists to do.
- **Step 7 creates, it does not describe.** "We should write that down later" has no trigger and nothing watching it. If the goal needs the work and the tracker is writable, it gets an item in this run. If it is not writable, a complete specification in the output is the deliverable.
- **No standing inventory, but always evidence.** Do not reproduce the task list, a status column, or a completion percentage - the source owns those and cannot go stale, while a copy is wrong at the next transition and gets trusted anyway. Do cite specific ids, dates, and counts against specific findings. "Five in flight, up from three" and "no movement since 02 June" are evidence for a verdict. A report with no ids and no dates in it cannot be checked, which is worse than one slightly out of date.
- **Scope the query.** A whole-board pull stalls the run rather than failing it, which is harder to diagnose than an error.

## Failure Handling

| Trigger | Impact | Recovery |
| --- | --- | --- |
| The target does not resolve to one body of work | No run | Ask. Do not guess, and do not fall back to something similarly named |
| A query returns everything | Context or token limit hit, run stalls | Re-query scoped to this work |
| Only part of the work is visible | An assessment that looks complete and is not | Say what is missing and stop |
| No goal exists, or the one that exists is too vague | Phase B returns noise that reads as signal | Repair it with the user first. This is a stop, not a caveat |
| Nothing records decisions | Direction three has no input | Say so explicitly and record it as `no decisions found`, never as `clear` |
| The tracker is read-only | Creates and re-ranks cannot be applied | Not an error. Write them as complete specifications and say they are unfiled |
| A check the source structurally cannot answer | A `clear` that means "could not look" | Record `n/a, no X available` |

*`altitude-check` by [Keith Crawford](https://keithcrawford.me), from [github.com/tsudo/skills](https://github.com/tsudo/skills). Copyright (c) 2026 Keith Crawford. `SPDX-License-Identifier: MIT` — full text in [LICENSE](https://github.com/tsudo/skills/blob/main/LICENSE).*
