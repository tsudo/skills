<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2026 Keith Crawford. Ships with the deslopify skill, github.com/tsudo/skills -->

# Eval Fixtures

One slop input per rule in `tells.md`, paired with a checkable assertion about the clean output. These ship with the skill so the rewrite is tested rather than asserted.

**How to run.** For each fixture, rewrite the input through the `deslopify` procedure, then check the assertion against the output.

An assertion marked *(literal)* passes or fails without judgment: a string is present or it is absent. An assertion marked *(judgment)* needs a human read; treat it as a note rather than a hard gate.

A fixture passes when every literal assertion holds and no judgment note flags a regression.

**Structural rules are the ones worth watching.** Layer 1 is where a rewrite most often fails, and its assertions carry the most judgment, so a green board on Layers 2 and 3 alone proves the least interesting half. Read the Layer 1 outputs rather than scanning them.

## Layer 1 - Structure

| # | Rule | Slop input | Assertion on output |
|---|------|-----------|---------------------|
| 1 | Uniform skeleton | `This document covers three areas. First, performance improved because the cache was tuned, though results vary, so it is worth measuring. Second, reliability improved because retries were added, though failures persist, so it is worth monitoring. Third, cost improved because instances shrank, though usage varies, so it is worth tracking.` | *(judgment)* The three sections are no longer the same length running the same claim-explain-qualify-wrap arc. At least one is materially shorter. *(literal)* No `This document covers`. |
| 2 | Signposting | `In this section we'll look at the results. The tests passed. Furthermore, coverage rose. Moreover, the build time fell. As mentioned earlier, this matters.` | *(literal)* None of `In this section`, `Furthermore`, `Moreover`, `As mentioned earlier` appear. Output opens on the result. |
| 3 | Count-announcement opener | `Three things to note before we start: it reads, it rewrites, it reports.` | *(literal)* No `Three things to note`, and no other `N things` pre-announcement. Output states the first point directly or uses a plain list with no count preamble. |
| 4 | Zoom-out conclusion | `The migration finished Tuesday. As data infrastructure continues to evolve, we remain committed to improvements that serve our users.` | *(literal)* The closing sentence is gone, and no `continues to evolve` or `remain committed` survives. *(judgment)* The output ends on the migration, which is where the argument ends. |
| 5 | Bullets as default | `- **Performance.** The cache was tuned, so reads got faster.`<br>`- **Reasoning.** We chose write-through over write-back because the read path dominates and staleness costs more than write latency here.`<br>`- **Cost.** Instances shrank.` | *(judgment)* The reasoning item is developed as prose rather than compressed into a bullet; genuinely list-like items may stay bulleted. *(literal)* No bolded lead term followed by a gloss on the reasoning item. Skip this fixture where the project's own style guide mandates bullets - the convention wins, and that is the correct outcome, not a failure. |
| 6 | Generic examples | `The scheduler retries on failure. Organizations can use this to streamline their operational workflows.` | *(literal)* No `streamline` and no `Organizations can use this`. *(judgment)* The sentence is either cut or replaced with something true of this system specifically. |

## Layer 2 - Sentence

| # | Rule | Slop input | Assertion on output |
|---|------|-----------|---------------------|
| 7 | Negative parallelism | `It isn't just a linter, it's a mindset.` | *(literal)* The `isn't just ... it's ...` frame is absent. *(judgment)* Output states directly what the thing is. |
| 8 | Rhetorical Q&A | `So what is this tool? Well, it turns out it rewrites text.` | *(literal)* No `So what is` opener and no `Well,` pivot. Output leads with the answer. |
| 9 | Deferred reveal | `Reads were slow under load. This is where caching comes in.` | *(literal)* No `This is where` and no `comes in`. *(judgment)* Output names what caching does. |
| 10 | Marketing intensifier | `The real magic happens when the cache warms. The best part is, it scales automatically.` | *(literal)* Neither `The real magic happens` nor `The best part is` appears. *(judgment)* Output describes the mechanism and lets the reader judge the value. |
| 11 | Em-dash stacking | `The system — built for speed — scaled cleanly — mostly.` | *(literal)* At most one em-dash pair in the paragraph; the three-dash chain is gone. *(judgment)* Meaning preserved. Zero em-dashes is a pass - the rule is a ceiling, not a quota. |
| 12 | Staccato fragment-pairs | `Not bigger. Better. This isn't config. It's control.` | *(literal)* The clipped two-beat fragments are gone; the output uses complete sentences. *(judgment)* The point still carries. |
| 13 | Isocolon metaphor-pairs | `A garden needs tending; a mind needs feeding. A pipeline needs watching; a team needs trusting.` | *(literal)* No semicolon-joined matched-clause pair survives. *(judgment)* The literal claim is made without the manufactured symmetry. |
| 14 | Fake agency | `The logs become searchable records and the system decides to retry.` | *(literal)* No `become ... records` and no `decides to`. Actions get a real subject, such as `you can search the logs` and `the system retries on failure`. |
| 15 | Elegant variation, same referent | `Save the document. Open the file. Delete the record.` (all one referent) | *(literal)* One term is reused across all three sentences; the synonym swap is gone. |
| 16 | Elegant variation, referent unconfirmed | `The payload carries the merchant record, the settlement document, and the transaction file.` (three distinct qualifiers, referent identity not stated) | *(literal)* All three terms survive; nothing is collapsed onto a single noun. *(judgment)* The output says the referents could not be confirmed. This fixture fails if the rewrite standardizes the noun - that would edit the claim, not the prose. |

## Layer 3 - Vocabulary

| # | Rule | Slop input | Assertion on output |
|---|------|-----------|---------------------|
| 17 | Banned words | `We leverage a robust pipeline and delve into the results.` | *(literal)* None of `leverage`, `robust`, `delve` appear. `leverage` becomes `use` or another plain verb; `delve into` becomes `examine` or `look at`; `robust` is dropped or replaced with a concrete quality. |
| 18 | Banned phrases | `At the end of the day, we need to circle back on this and unpack the low-hanging fruit.` | *(literal)* None of `At the end of the day`, `circle back on`, `unpack`, `low-hanging fruit` appear. *(judgment)* Whatever the sentence actually meant survives, or the output says the sentence carried no recoverable claim. |
| 19 | Adjective test | `A robust, powerful, best-in-class framework handling significant traffic.` | *(literal)* None of `robust`, `powerful`, `best-in-class` appear. *(judgment)* Any surviving adjective carries concrete information - scale, performance, constraint, quantity. `significant traffic` is either given a figure or flagged as a missing detail, not left as mood. |

## Notes

- **Coverage is one fixture per rule in `tells.md`, checked against it.** Nineteen fixtures against eighteen rules; elegant variation carries two, because its do-not-collapse carve-out fails in the opposite direction from the rule itself and a single fixture cannot test both.
- Fixtures are literal and checkable wherever possible, so a run can pass or fail without a human in the loop. Rules that turn on rhythm or structure carry a *(judgment)* assertion by design: those are read-and-decide, not string-match.
- **A green Layer 2 and Layer 3 board proves little on its own.** Those are the string-matchable rules. The structural layer is the one the skill claims matters most, and it is the one whose assertions need reading.
- On adding a rule to `tells.md`, add a matching fixture here. One fixture per rule is the minimum.
- This is a plain input-and-assertion set. If you already run an eval harness, wire these inputs and assertions into it rather than running them by hand.
