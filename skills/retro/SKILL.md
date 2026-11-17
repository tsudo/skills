---
name: retro
description: Run a retrospective on the work just done and turn what it taught into changes a future session will actually see - a rule in the project's instruction file, a gotcha on the skill that tripped, a ticket for the follow-up. Quick mode drafts four answers for you to correct; full mode walks outcomes, root causes, decisions, and process. Use this when someone asks for a retro, a debrief, what went well or badly, or to capture lessons before closing out. Not for incident post-mortems, code review, or status reports.
license: MIT
compatibility: Standalone. Works best in a project with an agent instruction file such as CLAUDE.md or AGENTS.md, and uses the project's issue tracker when one is connected. Writes nothing until you approve the routing plan, and writes only inside the project unless you approve a destination outside it. Where no writable location exists, returns the plan and the proposed text in the conversation.
metadata:
  author: "Keith Crawford"
  version: "1.0.0"
  source-canon: "retro"
  ported: "2026-11-16"
---

# retro

Review the work just done, keep what deserves to last, and put each lesson where the next session will load it.

## When To Use

- A working session is ending and it produced corrections, surprises, or a pattern worth repeating.
- Someone asks for a retro, a debrief, an after-action review, or "what did we learn".
- A run went badly enough that the same mistake is likely to happen again unless something changes.

Do not use this for an incident post-mortem with a timeline and stakeholders, for reviewing code, or for a status update.

## Definitions

- **mode** - quick (four drafted answers) or full (a structured walkthrough).
- **routing plan** - the numbered list of proposed writes, each with its destination. Nothing is written until it is approved.
- **instruction file** - a file the agent runtime loads automatically: a project `CLAUDE.md` or `AGENTS.md`, a directory-scoped rules file, or a skill's own `SKILL.md`.

## Core Idea

A lesson written somewhere nothing reads changes nothing. A log of learnings feels like progress, but if no future session loads that log, the same mistake comes back. So this skill routes each lesson to the narrowest file that a future session loads at the moment the lesson applies, and drops the lessons that would not change what anyone does.

## What You Need

- The session being reviewed: the current conversation, or a log or transcript the user points to. This skill reviews work it can see; it does not reconstruct a session from memory.
- Optional: write access to the project, the project's issue tracker, a task list from the session.

## Procedure

### Step 1 - Gather before asking

Collect everything the questions will need, so no question asks the user to recall something already on the page.

**From the session:**

- Corrections the user gave, and approaches the user confirmed.
- Commands or invocations that failed, and what worked instead.
- Environment quirks and gotchas hit.
- Context that was missing and would have saved a step.
- Deferred work. Read the task list if there is one, and look for phrases such as "next session", "next time", "follow-up", "separate ticket", "later", "not today", "after this ships". Each item becomes a follow-up candidate, so deferred work does not end with the session.

**From the project:**

- Instruction files: `CLAUDE.md`, `AGENTS.md`, and any directory-scoped rules the runtime loads, such as `.claude/rules/`, `.cursor/rules/`, or nested `AGENTS.md` files.
- Skill directories, such as `.claude/skills/` or `.agents/skills/`, in case a lesson belongs on a skill that was used.
- An existing home for retro notes, such as `docs/retros/` or a `LESSONS.md`. Note its file naming and entry format.
- The project's issue tracker, if one is connected. A tracker counts only if it belongs to this project. A tool connected to some other workspace does not.
- The project's writing conventions, if it has any. Follow them for everything you write.

**Check the session against the project.** Where the session says a file was changed or created, look. Claims the disk cannot show, such as a deploy or a message sent, are listed as unverified rather than missing. Work the session claims but the disk does not show, in whole or in part, is the most important finding of the retro, because lessons drawn from work that does not exist mislead. State it at the top of whatever you show the user next, then carry on; each missing piece becomes a follow-up in the routing plan.

Note what exists. Create nothing yet.

**If nothing durable turned up,** say so in one line and offer to stop. A short clean session rarely earns a retro.

### Step 2 - Choose the mode

If the user names a mode, in any wording ("quick retro", "do a full one"), use it and say which in one line. No confirmation is needed.

Otherwise recommend one. Count the strong signals, using only changes Step 1 confirmed on disk:

- Instruction, configuration, or build files were changed. Dependency manifests and lockfiles count; ordinary source files do not.
- New durable artifacts were created: docs, decision records, skills.
- The work spanned more than one area of the project.
- The user corrected course more than once.

Recommend quick for one strong signal or none, full for two or more. State the recommendation in one line and wait for the user to confirm or override.

### Step 3 - Quick mode

Show all four questions at once, each with a short draft answer from Step 1. Ask the user to correct, add to, or wave off any of them in one reply. Go one question at a time only if the user asks for that.

1. **What went well?** Wins worth repeating.
2. **What didn't go well?** Friction, surprises, failures.
3. **What did we learn?** Patterns confirmed, pitfalls found, preferences stated.
4. **What should change?** Specific adjustments for next time, including the deferred work found in Step 1.

Then go to Step 5.

### Step 4 - Full mode

Open with the inventory from Step 1:

```text
What this session shows:

Not on disk: [claimed work the project does not show, or "none"]
Wins:        [things that worked, approaches the user confirmed]
Decisions:   [choices made, with the reason given]
Corrections: [where the user redirected the work]
Failures:    [errors, retries, dead ends]
Open items:  [deferred or pending work]
```

Then cover these six sections in the same turn, each with a short draft from the inventory, and ask the user to correct or wave off any of them in one reply. Follow up only on the sections they answer with something new.

1. **Context.** What was the objective? What constraints applied?
2. **Outcomes.** Here is what went well and what did not, from the inventory. What would you add or correct?
3. **Causes.** Why did the successes happen, so they can be repeated? Why did the failures happen? What signal was missed?
4. **Decisions.** Which decisions mattered? Were the tradeoffs stated or implicit? With hindsight, were they reasonable?
5. **Process.** Where did the tools, workflow, or automation help, and where did they create friction?
6. **Takeaways.** The three to five that matter most. What to keep doing, and what to do differently.

### Step 5 - Filter for durability

Drop any insight that:

- only this session needed
- would not change what a future session does
- any competent session would do without being told

**Already recorded is not the same as already working.** If the lesson is already in a file a future session loads, and the session followed it, drop it. If it is recorded but the session broke it anyway, the record is too weak: propose strengthening it rather than dropping it. If it is recorded only somewhere sessions do not load, such as a package manifest, a wiki, or an earlier retro note, it still needs a home in an instruction file. Retro notes, this skill's own included, are not loaded.

If an earlier retro note lists a follow-up this session finished, propose marking it done.

List what you dropped in one line, so the user can pull an item back.

### Step 6 - Propose the routing plan

Give every surviving item one destination.

| Type | Destination | When |
| --- | --- | --- |
| Instruction | The narrowest instruction file that loads where the rule applies | A rule every future session should follow without being reminded. Add, strengthen, or remove a line |
| Follow-up | The project's issue tracker, named in the plan; with none, the retro notes under a follow-ups heading | A concrete next step that needs tracking |
| Record | The project's retro notes | Context worth keeping that is not a rule |
| Design question | Raised in the conversation only | A structural question for the user to decide |
| Memory | The runtime's persistent memory | A preference about working with this user that holds across projects, only where the runtime has one and the user approves |

When a lesson could be an instruction or a memory, ask whether it is about this project. If it is, it is an instruction: everyone working in the project should follow it, not only this user's sessions.

**For an instruction, choose the narrowest file in this order:**

1. The `## Gotchas` section of the skill the lesson concerns. Propose adding the section if the skill has none.
2. A directory-scoped rules file, when the rule applies to one part of the project. Use an existing one, or propose a new one only in a form the runtime loads, such as a nested `AGENTS.md`.
3. The project instruction file, when it applies to the whole project.
4. A user-level instruction file, only when the user asks for it, since it sits outside the project.

Prefer the instruction file the project already has. If the runtime in use may not load that file, say so in the plan.

If the project has no instruction file, propose creating one at the project root and mark it `(new file)` in the plan. Use the file the runtime in use loads: `CLAUDE.md` for Claude Code, `AGENTS.md` for most other agents. If unsure, ask. A new file opens with the project's name as its title, then one short heading per kind of rule, such as Commands or Conventions. Show the full proposed file in the plan.

Place each line under the existing heading it fits. Where none fits, propose a new heading in the file's existing style. Keep each rule to one line.

**For a record or a follow-up in notes,** use the project's existing retro location, and match its file naming and entry format. With no existing location, propose `retro-YYYY-MM-DD.md`, dated today, at the project root and let the user choose another place. A new notes file opens with a dated title and a one-line summary of the session; include that line in the plan so it is approved with the rest.

Present the plan in this shape:

```text
Dropped as not durable: <one line>

Proposed routing:
1. [INSTRUCTION +] AGENTS.md (new file)
   Why: <one line>
   + <the one-line rule>
2. [INSTRUCTION ~] CLAUDE.md, under "## Commands"
   Why: the session ran npm although the rule says pnpm
   - Tests: `pnpm test`
   + Tests: `pnpm test`. Never npm.
3. [FOLLOW-UP] "<action>" -> <tracker and project name>, or -> <notes file> (no tracker)
4. [RECORD] "<context>" -> <notes file>
5. [DESIGN] "<question>" -> for you to decide, nothing written

Approve, change, or remove any item. Nothing is written until you do.
```

Use `+` to add a line, `~` to strengthen one, and `-` to remove one the lesson replaces.

**Stop here.** Write nothing - no file, no ticket, no memory - until the user approves the plan. This stop holds even when the earlier work ran without pauses. The user may approve the plan, change items, or remove them.

### Step 7 - Write the approved items

For each approved item:

- Read the target file first. If the line is already there, say so and skip it.
- Make the change in place under the agreed heading. Do not reorganize the rest of the file.
- Create a tracker follow-up with a title, a short description, and a link to the retro notes if any were written.
- Write nothing the user did not approve, and nothing outside the project unless the user approved that destination.

Where there is no writable location, return each approved item in the conversation as text the user can paste, labeled with its destination.

### Step 8 - Report

```text
Retro complete (quick | full)
  Not on disk:         N (or none)
  Instruction changes: N
  Follow-ups:          N (tracker) + N (notes)
  Records written:     N
  Design questions:    N
  Dropped as not durable: N
```

## Output

The approved writes from the routing plan, and a completion summary in the conversation. Where nothing is writable, the same items are returned as labeled text.

## What This Skill Does NOT Do

- Does not write anything before the routing plan is approved.
- Does not run an incident post-mortem. For an incident with a timeline, impact, and stakeholders, use a post-mortem process built for that.
- Does not review code or audit the project. It checks only that the work the session describes is present.
- Does not reconstruct a session it cannot see.
- Does not reorganize or clean up instruction files beyond the approved lines.

## Gotchas

- **Momentum carries across the approval stop.** If the work before the retro ran without pauses, the retro tends to keep going straight into writing. Stop at the routing plan whatever the earlier pace was, and at mode confirmation when the user did not name a mode.
- **Instruction files grow until nobody reads them.** Prefer the narrowest file, keep each rule to one line, and remove a rule the lesson replaces.
- **A follow-up in notes is weaker than one in a tracker.** Nothing loads the notes at the moment the follow-up is due. When there is no tracker, say so in the report so the user knows where it went.

*`retro` by [Keith Crawford](https://keithcrawford.me), from [github.com/tsudo/skills](https://github.com/tsudo/skills). Copyright (c) 2026 Keith Crawford. `SPDX-License-Identifier: MIT` — full text in [LICENSE](https://github.com/tsudo/skills/blob/main/LICENSE).*
