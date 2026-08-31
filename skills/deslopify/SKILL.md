---
name: deslopify
description: Rewrite prose that reads as machine-generated into plain, direct writing, fixing structure first, then sentence constructions, then vocabulary, because fixing word choice over a default essay skeleton still reads as generated. Use this when someone asks to clean up the voice, make writing sound human, or cut the AI slop before it ships. Not for agent-facing instruction text - skill files, procedures, prompts - which use a flat imperative register on purpose.
license: MIT
compatibility: Standalone. Needs no repository, no MCP server, and no particular project layout. Reads the project's style guide if it has one. Returns the rewrite in the conversation and writes no files.
allowed-tools: "Read Grep Glob"
metadata:
  author: "Keith Crawford"
  version: "1.0.1"
  source-canon: "deslopify"
  ported: "2026-08-31"
---

# deslopify

Rewrite prose that reads as machine-generated into plain, direct writing.

Most writing guidance is passive. It shapes prose while the prose is being written, which means it does nothing for text that already exists. This is the opposite: one dedicated cleanup pass over a draft that is already on the page.

## When To Use

- Prose is about to ship and nobody has read it for generated tells.
- Someone says the writing sounds like a chatbot, or reads as filler.
- A draft is substantively right but reads wrong.

Do not use this on agent-facing instruction text - skill files, procedures, prompts, execution steps. Those use a flat imperative register deliberately, and rewriting them for warmth is a defect rather than a cleanup.

## What You Need

- The target text: supplied with the invocation, in a file the request points at, or already in the conversation.
- `references/tells.md`, which ships with this skill and carries the rule set.
- The project's own writing conventions, if it has any.

## Procedure

### Step 1 - Resolve the target

Resolve in this order, and take the first that matches:

1. Text supplied with the invocation.
2. A file the request names or points at. Read it. This is the common case, and the file is the target rather than the request that named it.
3. The previous response.

A request that points at a directory rather than a file resolves under case 2 only when the directory holds one candidate. Where it holds several, name them and ask which.

If none of the three resolves, ask what to rewrite and stop. Do not guess at the target.

### Step 2 - Find the project's conventions

Look for writing conventions the project already set, in this order: `CLAUDE.md`, `AGENTS.md`, `STYLE.md`, `CONTRIBUTING.md`, then any `docs/style` path.

If you find them, they win wherever they conflict with anything in this skill. The project's terminology, register, heading conventions, and house preferences are not yours to override. Where the project is silent on a point, this skill's guidance applies.

If you find none, apply the tells in `references/tells.md` as written.

State which conventions you found, or that you found none, before returning the rewrite.

Where a convention requires something `references/tells.md` lists as a tell, follow the convention and say so in that same line. Otherwise a reader cannot tell house style from slop you left in.

### Step 3 - Check the register

This step runs after Step 2 because the project's conventions usually settle it.

**Agent-facing instruction text is a hard stop.** A skill file, a procedure, a system prompt, or a list of execution steps is written flat and imperative on purpose. Making it read like an essay makes it worse at its job. Say so and stop.

Otherwise the target is human-facing prose and the rewrite proceeds. Documents like release notes, a README, or a changelog can be written for different readers - a customer, or an engineer integrating against the thing - and the choice changes what survives the rewrite.

Settle it in this order:

1. If the project's conventions name the register, use that.
2. If they do not, pick the register implied by the document's own content and by whatever else the project makes obvious - a package manifest, the surrounding directory, the audience the subject matter serves. State the assumption in one line and continue.
3. Ask only when the two readings would produce materially different text and nothing in the project or the document favors either.

Do not stop to ask a question the conventions already answered.

### Step 4 - Load the tells

Read `references/tells.md`.

### Step 5 - Rewrite, in layer order

Fix structure, then sentences, then vocabulary. The order is load-bearing. A vocabulary-only pass swaps out the obvious words and leaves prose that still reads as generated, because the skeleton is what gives it away.

Rewrite for a sharp reader who has no context on the project. Where the text makes an argument, lead with the conclusion and let the background and the mechanism follow it. This is an ordering principle, not a skeleton to impose: a flat list of parallel items has no such order, and forcing one on it is the uniform-skeleton tell arriving from the other direction. Standardize terminology and define any unfamiliar term where it first appears.

**What cutting is in scope.** Delete a sentence when removing it loses no information a reader could act on: a zoom-out closer, a line that would drop unchanged into any other document, a claim left empty once the banned words come out. That is the tell being fixed, not the text being shortened.

Keep anything that carries a fact, even a thin one. A fact often lives inside a construction the tell-set says to delete - a count-opener naming three changes, a marketing frame wrapped around a mechanism. Keep the fact and cut the frame; do not lose the payload with the wrapper. Where a sentence is vague because the underlying detail is missing rather than because it is padded, say what is missing instead of cutting or inventing it. Two words that mean the same thing collapse onto one term; two words that might name different things do not, because that is an edit to the claim rather than to the prose.

### Step 6 - Return the rewrite

Return the rewritten text in the conversation, and keep it clean enough to paste straight into the document it came from.

Anything you flagged as missing under Step 5 goes in a short list beneath the rewrite, never inline in it. A gap note pasted into a real document is a new defect.

This skill does not write files, and carries no tool that would let it. If the rewrite should be saved, that is a step you take with the text it hands back.

### Step 7 - Show the edits on request

If the invocation carried `--diff`, or the user asks what changed, follow the rewrite with a short list of the concrete edits: "cut two em-dash pairs", "replaced leverage with use", "removed the count-opener", "collapsed three synonyms for the same thing onto one term".

Name the edits actually made. Do not list rules that did not fire.

## Self-test

`references/eval-fixtures.md` holds one slop input per rule in `references/tells.md`, paired with a checkable assertion about the clean output. Rewrite each input through this procedure and confirm every assertion holds.

Assertions marked *(literal)* pass or fail on a string check. Assertions marked *(judgment)* need a human read and are notes rather than gates.

Run the fixtures after any change to this skill or to `references/tells.md`.

Read the Layer 1 results rather than scanning them. The structural fixtures carry the most judgment and the least string-matching, so a board that is green on Layers 2 and 3 alone has tested the vocabulary pass - which is the failure this skill exists to catch, not evidence against it.

## Output

- The rewritten text, in the conversation.
- A statement of which project conventions were found and applied, or that none were. One line where nothing conflicts; one line per conflict where a convention required something `references/tells.md` calls a tell.
- On `--diff` or on request, a bulleted list of the concrete edits.

Report `BLOCKED` if no target text resolves. Report the register mismatch and stop if the target is agent-facing instruction text.

## What This Skill Does NOT Do

- Does not write or modify files. The rewrite comes back in the conversation.
- Does not rewrite agent-facing instruction text.
- Does not override the project's own style guide. Where one exists, it wins.
- Does not invent new style rules. If the target exposes a tell that `references/tells.md` does not cover, name it for the user rather than adding it silently.
- Does not restructure the argument. It rewrites how the text reads, not what it claims. A conclusion that is wrong stays wrong, and saying so is a separate job.
- Does not shorten for its own sake. Plain writing usually comes out shorter, and a sentence emptied of information by the rewrite goes with it - but cutting text that still carries a fact is an edit the user asks for, not a side effect of this one. Step 5 draws the line.

## Gotchas

- **The agent-facing stop is a stop, not a warning.** Skill bodies, procedures, and prompts read flat because flat is correct for them. Rewriting one for humanity is the most common misuse of this skill and it silently degrades a working file. The register question among human readerships is a different thing and does not stop the run.
- **A vocabulary-only pass is the visible failure.** Swapping the banned words while leaving a standard essay skeleton produces text that still reads as generated and now also reads as edited. Structure is layer one for a reason.
- **The em-dash rule is one pair per paragraph, not zero.** Stripping every em-dash is over-correction. A single deliberate pair is fine.
- **Do not flatten a voice that is already someone's.** Where the target reads as a specific person rather than as a machine, the tells that fire may be that person's habits rather than generated filler. Judge it the way Step 3 judges register: if the project's conventions settle it, follow them; if the text carries no personal residue under the slop, rewrite and say you found none; ask only where a real voice is present and neutralizing it would change what the piece sounds like.

*`deslopify` by [Keith Crawford](https://keithcrawford.me), from [github.com/tsudo/skills](https://github.com/tsudo/skills). Copyright (c) 2026 Keith Crawford. `SPDX-License-Identifier: MIT` — full text in [LICENSE](https://github.com/tsudo/skills/blob/main/LICENSE).*
