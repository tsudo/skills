<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2026 Keith Crawford. Ships with the deslopify skill, github.com/tsudo/skills -->

# Rewrite Tells

Three layers, applied in order. Structure first: fixing vocabulary while leaving a default skeleton intact still reads as generated.

Where the project has its own style guide, it wins over anything here.

## Layer 1 - Structure

| Tell | Fix |
|---|---|
| **Uniform skeleton.** Intro announces the topic, three roughly equal body sections, recap restates the headings. Every section the same length, every paragraph running the same claim-explain-qualify-wrap arc | Let the analysis set the shape. Sections can be unequal; some findings need one sentence. Not every document needs an intro or a conclusion |
| **Signposting**, also called meta-narration. "In this section we'll look at...", "As mentioned earlier...", an opening paragraph that restates the question before answering it, and stacked "Furthermore / Moreover / Additionally" | Delete it. If a transition needs a signpost, the section order is wrong. Answer first |
| **Count-announcement opener.** "Three things to note here...", "Two cautions before we start" | State the first point. If the items are genuinely distinct, list them without pre-announcing the quantity |
| **Zoom-out conclusion.** "As the technology continues to evolve...", or an "In conclusion" that adds nothing already said | End where the argument ends. Close on a specific next step, or cut the section |
| **Bullets as default.** Most of the content is short bullets, each opening with a bolded term and a gloss | Bullets for genuinely distinct items. Paragraphs for reasoning |
| **Generic examples.** "Organizations can use AI to streamline workflows" | Be specific. An example that could drop into a different document unchanged is filler |

## Layer 2 - Sentence

| Tell | Fix |
|---|---|
| **Negative parallelism**, in any wrapper. "It isn't just a tool, it's a paradigm shift" / "Security is more than just firewalls; it's a mindset" / "It wasn't the technology, it was the team" | State what it is. Cut the buildup |
| **Rhetorical Q&A.** "So what exactly is X? Well, it turns out..." Also headings phrased as the question the reader came to have answered | State the answer. The reader did not ask |
| **Deferred reveal.** "This is where automation comes in" | Name what it does |
| **Marketing intensifier.** "The real magic happens when...", "The best part is, it scales automatically" | Describe the mechanism. Let the reader judge the value |
| **Em-dash stacking.** "The system — designed for scale — handled the load — barely" | One em-dash pair per paragraph maximum; commas or separate sentences otherwise. The rule is one, not zero |
| **Staccato fragment-pairs.** "Not bigger. Better." / "This isn't config. It's control." | Write the full sentence. Let the point carry itself |
| **Isocolon metaphor-pairs.** "A garden needs tending; a mind needs feeding" | Make the literal claim without the matched-clause symmetry |
| **Fake agency.** "The logs become searchable records", "The system decides to retry" | Give the action a real subject: "you can search the logs", "the system retries on failure" |
| **Elegant variation.** One thing called "document", then "file", then "record" across three sentences | Pick one term and reuse it. Repeating the word is clearer than swapping synonyms to avoid repeating it. This applies only where the words name the same thing. Distinct qualifiers usually mean distinct things - "merchant record" and "settlement document" are two objects, not one word swapped; bare synonyms for one referent are the case to collapse. Where you cannot tell, keep them apart and say you could not confirm it |

## Layer 3 - Vocabulary

**Cut these words:** delve, crucial, robust, comprehensive, nuanced, leverage, synergy, holistic, paradigm, scalable, ecosystem, empower, seamlessly, innovative, disruptive, groundbreaking, revolutionize, game-changing, cutting-edge, best-in-class, utilize. In technical writing, also watch *ensure* and *implement* where a plainer verb works.

**Cut these phrases:** "in today's rapidly evolving landscape", "unlock the power of", "deep dive into", "at the end of the day", "moving the needle", "low-hanging fruit", "circle back on", "align on this", "double-click on that", "unpack this", "let me break this down", "here's the kicker", "it's worth noting that", "needless to say", "without further ado".

**Adjective test.** Strip every adjective from a paragraph, then restore only the ones carrying concrete information: scale, performance, constraint, quantity. Drop the ones carrying mood. "Robust system" becomes "service handling 10k req/s"; "powerful framework" becomes what the framework does.
