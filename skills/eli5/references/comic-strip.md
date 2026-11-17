<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2026 Keith Crawford. Ships with the eli5 skill, github.com/tsudo/skills -->

# Building the Comic Strip

The picture is a column of small panels, read downward, each carrying a single beat. It is not a diagram. A reader should understand each panel at a glance and never have to trace a line to find out what happens next.

## Panels

**Stack them vertically.** One beat per panel, in story order. Do not compress the story into a single picture with a timeline, a loop, or numbered markers scattered around it. If the reader has to hunt for step three, rebuild it as separate panels.

**The titles carry the story.** Write each panel title as a short plain sentence with a subject and a verb. Someone reading the headings alone, first to last, should get the whole explanation:

> "You type an address."
> "Your browser asks for the number."
> "The answer comes back."
> "Now the page loads."

**One action per panel.** Three or four figures or objects and one movement, usually left to right. If a panel has two things happening, make it two panels. Richness comes from the sequence, not from what is packed into any one frame.

Arrows, labels, and small marks do not count toward the figures, and a row of identical small marks counts as one.

A decision is an action too. Draw the actor that decides with a single mark beside it showing the verdict, a tick or a cross, and no arrow. Name only the decision in the title; put what it weighs in the caption.

**Keep the cast consistent.** The same figures drawn the same way in every panel, so the reader recognizes them. Define each one once as an SVG `<symbol>` and reuse it with `<use>`. The template carries five - a person, a document, a server, a window, a robot. Add others the topic needs, such as a card or a phone, in the same line style.

When two actors would share one figure, such as two different banks, tell them apart with a short label and a small distinguishing mark, and keep each actor's mark the same in every panel.

**Number the panels, not the parts.** A "Step 1" label on each panel is fine. Numbers scattered inside one picture are a sign it is a diagram and should be split.

**One caption under each panel.** The caption adds the fact that makes the beat matter. It never restates the title. If the title is "Your browser asks for the number", a caption of "The browser looks up the number" is the same sentence twice; "Usually your internet provider answers this" adds something.

## Two checks before handing it over

1. Cover the pictures and read the headings alone. Is the explanation complete, and does it answer the question the reader asked? For "what is X", one title has to say what X does.
2. Look at each panel for two seconds. Is it clear without tracing anything?

If either fails, simplify or split.

## Copy

- The page heading is the topic, as a plain question or statement: "How a card tap gets approved". That is content, not framing.
- No visible framing text beyond it: no skill name, no "a simple guide", no footer explaining the format. The page holds the explanation and nothing around it.
- A key term gets the accent color in the caption where it first appears, matching the bold term in the walkthrough.
- Give every scene SVG an `aria-label` that says what the panel shows.

## Look

The template ships one restrained default: a serif for titles, a sans for captions, a pale ground, dark ink, and one accent color. The accent marks four things only: the step labels, the reader's own element, the arrow for the action the reader takes, and key terms. Everything else is ink. The page follows the system light or dark setting.

"The reader's own element" is the figure standing for the reader, plus anything that belongs to them in the story, such as their card, their phone, or their browser, and any mark drawn on those. "The action the reader takes" includes their device or app acting for them. Every other arrow is ink: use `class="move"`, not `class="move key"`.

Treat the look as a default, not a rule. Where the project has a design system, a brand palette, or a style the reader expects, use that instead. The panel rules above do not change with the look.

A brand palette usually has fewer colors than the template has tokens. Map it this way:

| Template token | Takes |
| --- | --- |
| `--ground` | The brand background |
| `--panel` | The brand's surface or card color if it has one, otherwise the background |
| `--ink` | The brand text color |
| `--line` | The brand text color, or its secondary text color if outlines look heavy |
| `--muted` | The brand's secondary text color, or the text color |
| `--scene` | The text color at about 5 to 8 percent over the background |
| `--accent` | The brand accent |

If the brand gives dark-theme values, map them the same way into the dark-mode block. If it gives only light values, delete the dark-mode block rather than inventing dark ones.

A brand font for headings replaces the serif; a font for body text replaces the sans. One brand font replaces both.

## Delivering the file

- Delete every instruction comment in the template, in the HTML and the CSS. Keep the two licence comment lines at the top; they are invisible on the page.
- Name the file `eli5-<slug>.html`, where the slug is the topic in two to four lowercase words joined by hyphens.

## Technique

- Hand-draw scenes as inline SVG.
- Self-contained only: inline CSS, inline SVG, system fonts. No CDN, no web fonts, no external images.
- The file is the deliverable. Never paste the HTML into the conversation as a substitute for handing over the file.
