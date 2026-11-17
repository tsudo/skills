---
name: eli5
description: Explain an unfamiliar topic to an intelligent adult who has never worked with it - a short spoken-style walkthrough in chat, then a stacked comic-strip HTML page when the topic has steps or a flow. Plain, literal language, key terms taught where they happen, nothing talked down. Use this when someone says eli5, explain this like I'm new, break this down, catch me up on X, or how does X actually work. Not for a reader who already knows the field, for reference documentation, or for researching a topic from scratch.
license: MIT
compatibility: Standalone. The chat walkthrough works anywhere. The comic strip needs a place to write one HTML file and a way to hand it to the reader; where neither exists, the walkthrough stands alone and the skill says so in one line.
metadata:
  author: "Keith Crawford"
  version: "1.0.1"
  source-canon: "eli5"
  ported: "2026-11-16"
---

# eli5

Give a smart adult the point of an unfamiliar topic in one sentence, then walk them through how it works in under a minute of reading.

## When To Use

- Someone is new to a topic and wants the gist before the detail.
- Someone asks how a process, system, or mechanism actually works, in plain words.
- Someone has bounced off documentation written for people already inside the field.

Do not use this when the reader already knows the field and wants depth, when the job is reference documentation, or when the topic first needs research.

## Core Idea

**The reader is new to this subject and fully at home in ordinary adult life.** Calibrate to both halves at once.

- They have never touched the topic, so nothing inside it is assumed.
- They hold a job, pay bills, use a phone, and deal with banks, managers, and customers. Words from that world need no definition.
- Defining an everyday word is the sign the answer has slipped into talking down. Rewrite it.

The register is a knowledgeable friend explaining over coffee: direct, warm, and quick. It is not a lecture, and it is not a children's book.

## Procedure

### Step 1 - Say where you drew the line

Make the first sentence name what you are assuming the reader already knows, then carry straight on without pausing for a reply.

> "I'll assume you know what a website is but not how your browser finds one."

This gives the reader a one-line chance to recalibrate. Do not open with questions about their background.

### Step 2 - Walk it through in chat

Always deliver this part first, straight after the assumption line. Keep this order:

1. **Place it.** One line on where the topic lives and what it is for.
2. **The point, in one sentence.** If the reader stops here, they have it.
3. **How it works, in numbered steps.** About five steps, one or two sentences each, each written the way a person would say it aloud. Drop the small, telling facts in as asides, since they are what make the mechanism click.
4. **Teach terms where they happen.** Bold a key term the moment it appears in the story and define it in a few words there. Never front-load a glossary. Teach the terms the reader will meet next: the words they would need to search the topic or follow a conversation about it. Four new terms is a ceiling, not a target; needing more means the topic is too big for one answer. When the topic is itself a term, such as "what is an API", define it in the one-sentence point.
5. **One closing point.** A last line that makes the whole mechanism feel obvious in hindsight. It restates what the steps showed in one sentence; it does not add a claim the steps did not make.

Keep everything from the assumption line to the closing point under about 250 words. The hand-over line does not count.

A worked shape, for "how does my browser find a website":

> "I'll assume you know what a website is but not how your browser finds one. This is plumbing that runs every time you type an address - you never see it. The short version: your browser asks a directory for the website's number, then goes to that number.
>
> 1. You type an address. Computers can't route a name, so the browser needs the site's numeric address first.
> 2. It asks a **resolver** - a lookup service, usually run by your internet provider - for that number.
> 3. If the resolver hasn't looked the name up recently, it asks down a chain of directories until one answers.
> 4. The answer comes back and gets remembered for a while, which is why a second visit is faster.
> 5. Only now does the browser connect to the site.
>
> All of that happens before the page even starts loading."

Walk the main path only. Leave edge cases and exceptions for follow-up questions.

### Step 3 - Decide whether a picture helps

| The topic | Do this |
| --- | --- |
| Has several steps, a before and after, or one thing acting on another | Build the strip, one panel per walkthrough step |
| Has only a small flow, such as a request going out and an answer coming back | Build a short strip of three panels: the trigger, the work, the result. Merge walkthrough steps to fit |
| Is a static idea with no sequence, such as what a variable is | Skip the picture |

A "what is X" topic still gets a strip when your walkthrough told it as something happening. Skip only when the walkthrough itself had no sequence. A picture forced onto a static idea is worse than none. When skipping, end the walkthrough with the closing point and stop.

### Step 4 - Build the comic strip

Diagram code in a chat block, such as Mermaid or ASCII art, reaches most readers as raw text. The picture is always a rendered file.

1. Read `references/comic-strip.md` for how panels are built.
2. Start from `assets/comic-strip.html`. Keep the cast symbols you need, delete the rest, and add new figures in the same style where the topic needs them.
3. If the project has its own design system, brand colors, or fonts, use them in place of the template's palette. Project conventions on spelling, wording, and output locations apply to the page and to the chat answer.
4. Save the file without asking, named `eli5-<slug>.html` as `references/comic-strip.md` describes. If the project's instruction files name a folder for generated pages, use it and create it if it is missing; otherwise use the project root. Asking would hold up the answer the reader came for.
5. Hand the file over in whatever way the runtime supports: attach it, open it in a preview, or give a full path the user can open.

If the runtime cannot write or hand over a file, skip the strip and say so in one line.

### Step 5 - Hand it over lightly

After the closing point, add one short line introducing the picture, and attach it in the same turn. Do not ask whether they want one first, and do not sell it.

End there. No recap, no menu of further topics.

### Step 6 - Stay calibrated through follow-ups

Keep the same rules for every follow-up in the conversation, with two changes. Skip the assumption line unless the reader's question shows the calibration was wrong; start directly on the new part. And use terms already taught without defining them again.

When a follow-up shows the reader already knows a part, skip that part and go deeper on the rest. Never re-explain ground already covered. Build a new strip only when the follow-up has a flow of its own.

## Language

- **Name the real thing.** A specific, literal term beats an analogy almost every time. Keep the field's jargon, defined once in a few words, because the reader needs it to search the topic or talk to someone in the field. When a plain description stands in for a term, give the term too: "a fingerprint of the contents, called a **hash**", not "a fingerprint" alone.
- **Ration analogies.** Use one only when no plain word exists, hold it to a single sentence drawn from adult life, such as a receptionist routing a call. Never toy boxes, magic helpers, or lemonade stands.
- **Use what the reader already owns.** "The bank approves the transfer" needs no explanation.

## Never

- Preamble: praising the question, announcing what you are about to do, or easing in.
- "Simply put", "it's easy", or any version of "imagine you're a child".
- Stacked or multi-paragraph analogies.
- Repeating back what the reader said they already understand.
- Defining everyday adult vocabulary.
- Long paragraphs. If it looks long, it is wrong.
- A fenced diagram presented as the picture.
- Framing copy inside the picture: skill names, "a simple explainer", or a footer about the format.

## Output

| Artifact | Where | When |
| --- | --- | --- |
| Walkthrough | The conversation | Always |
| Comic-strip HTML | The project's folder for generated pages, or the working directory | Only when the topic has a flow |

The HTML file is self-contained: inline CSS and SVG, system fonts, no network requests.

## What This Skill Does NOT Do

- Does not research. It explains what is already known or findable in the session.
- Does not write reference documentation or lasting notes. The output is an explanation for one reader.
- Does not draw architecture diagrams or technical review visuals. The strip tells a story to a newcomer; it is not a system map.
- Does not quiz the reader before answering.

## Gotchas

- **The calibration line can be skipped by accident.** Without it, a reader who knows more than assumed has no easy way to say so. Keep it even when the topic feels obvious.
- **Five steps is a target, not a container.** A topic that needs nine steps to make sense is too big for one answer. Explain the first part and offer the rest as a follow-up.
- **The strip drifts toward a diagram.** If any panel needs arrows crossing each other or numbers to follow, split it. See `references/comic-strip.md`.

*`eli5` by [Keith Crawford](https://keithcrawford.me), from [github.com/tsudo/skills](https://github.com/tsudo/skills). Copyright (c) 2026 Keith Crawford. `SPDX-License-Identifier: MIT` — full text in [LICENSE](https://github.com/tsudo/skills/blob/main/LICENSE).*
