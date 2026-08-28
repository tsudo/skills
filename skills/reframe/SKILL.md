---
name: reframe
description: Turn a substantial analysis, investigation, comparison, or exploratory conversation into a standalone Markdown report, using the restructuring as a second analytical pass that re-checks conclusions, assumptions, evidence, risks, and recommendations. Use this whenever someone asks to write this up, turn this into a report, document this decision, make this durable, or produce a findings document. Use it too when a discussion has accumulated real analysis that a reader who was not there would need reconstructed, even if nobody asks for a report by name. Do not use it for short factual answers, status updates, or transcripts.
license: CC-BY-4.0
metadata:
  author: "Keith Crawford"
  version: "1.0.0"
  source-canon: "reframe"
  ported: "2026-08-28"
allowed-tools: "Read Write Glob Grep"
---

# reframe

Use this skill when a substantial analysis, recommendation, investigation, comparison, or exploratory conversation should become a durable Markdown report.

The goal is not to summarize or prettify the source material. The goal is to use the change in structure as a second analytical pass: re-check the conclusion, test the assumptions, separate evidence from inference, and surface material gaps the original pass missed.

## When To Use

- A conversation contains enough analysis that a reader should not have to reconstruct it from chat order.
- A decision, recommendation, or assessment needs to stand alone.
- The user asks to make an analysis durable, turn it into a report, or write it up.
- A structured second pass may reveal a weak assumption, contradiction, missing risk, or better recommendation.

Do not use this for simple factual answers, short rewrites, status updates, transcripts, or cases where structure adds no value.

## Output

Produce one Markdown report. It should be readable by someone who did not see the original conversation.

Prefer this section set, then adapt it to the problem:

- `Objective`
- `Key Findings`
- `Analysis`
- `Risks and Gaps`
- `Recommendations`
- `Open Questions`
- `Structured Review Findings`

Only include `Structured Review Findings` when the second pass found something material: a changed conclusion, contradiction, missing evidence, weak assumption, or important omission. If the second pass changes nothing, leave that section out.

## Procedure

1. Confirm that the source material is substantial enough to justify a report. If the input is too thin, tell the user that a shorter answer is the better output.
2. Identify the actual objective. Name the decision, question, or problem the report serves. Do not use a topic label as the objective.
3. Extract the source material into claims, evidence, assumptions, risks, and recommendations. Preserve meaning, not chronology.
4. Choose the report shape. Start from the preferred section set above, then rename, merge, add, or drop sections when the material calls for it.
5. Load the adopter's project conventions before drafting. Look for `CLAUDE.md`, `AGENTS.md`, `STYLE.md`, or a `docs/style` file in the current project. If one exists, follow it. If none exists, use this fallback:
   - Lead with the conclusion.
   - Use concrete nouns and verbs.
   - Keep paragraphs short.
   - Avoid filler transitions and marketing language.
   - Use bullets only for distinct items.
   - Separate findings, analysis, risks, and recommendations.
   - Mark uncertainty plainly.
   - Make recommendations actionable and prioritized.
   - Prefer useful headings over clever headings.
   - Stop when the report has done its job.
6. Run the second analytical pass. Ask:
   - Does the original conclusion still follow from the evidence?
   - Which assumptions are doing real work?
   - What evidence is missing or weaker than it first looked?
   - Which risks were blended into recommendations instead of named?
   - Which recommendation should move up, move down, or be cut?
7. Draft the report. Do not narrate this procedure inside the report.
8. Confirm the destination before writing. Use the path the user supplied. If none was supplied, ask where the report should go, or return it in chat. If the user has explicitly delegated the choice, name the path you picked before writing to it. Ask before overwriting an existing file.
9. Verify the finished report against the quality gates below before returning it.

## Quality Gates

- The objective names a real decision, question, or problem.
- Findings, analysis, risks, and recommendations are separated.
- Recommendations are actionable and prioritized.
- The report is readable without the source conversation.
- The second pass is real. The report should not merely reorder the original text.
- Material uncertainties, assumptions, and missing evidence are visible.
- The report does not manufacture findings for symmetry.
- The destination was confirmed, or the chosen path was named, before writing.

## What This Skill Does Not Do

- It does not rewrite voice in place.
- It does not elicit new thinking interactively from scratch.
- It does not create a transcript.
- It does not invent findings to make the report look complete.
- It does not create issues, tasks, knowledge records, or follow-up artifacts unless the user explicitly asks for that separate action.
- It does not write outside the confirmed destination.
- It does not work from an isolated context. The conversation or the supplied analysis is the raw material; running this skill in a fresh agent that cannot see that material leaves it nothing to reframe.

## Failure Handling

- If the source material is missing, ask the user for the analysis or conversation to reframe.
- If the report destination is ambiguous, ask for the path or return the report in chat.
- If an output file already exists, ask before overwriting.
- If the second pass finds no material change, produce a shorter report and say that no separate structured-review finding was warranted.

---

*`reframe` by [Keith Crawford](https://keithcrawford.me). Licensed [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Source: [github.com/tsudo/skills](https://github.com/tsudo/skills).*
