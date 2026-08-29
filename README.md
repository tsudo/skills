# Tsudo's AI skills library

![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## Welcome

Welcome to Tsudo's Skills.

These are skills I have authored or adapted. I hope you find them useful.

*Each skill is standalone*: install or copy a single skill directory and it works, with nothing else from this repo.

## Install

### If you use Claude Code

```text
/plugin marketplace add tsudo/skills
/plugin install reframe@crawford-skills
```

### If you use a cross-runtime registry

```bash
npx skills add tsudo/skills --skill reframe
```

### If you just want the files

```bash
cp -r skills/reframe ~/.claude/skills/
```

## Skills

| Skill | What it does |
| --- | --- |
| [`reframe`](skills/reframe/SKILL.md) | Turns an analysis or long conversation into a standalone Markdown report, using the restructuring as a second pass over the reasoning. |
| [`grill-me`](skills/grill-me/SKILL.md) | Interviews you about a half-formed idea, plan, or decision until it is committable. Works in rounds, checkpoints to a file so long sessions survive, and closes with a pre-mortem that turns failure modes into pass/fail criteria. Credit: [Matt Pocock](https://github.com/mattpocock/skills) and [Daniel Miessler](https://github.com/danielmiessler/LifeOS) — see the skill's [Credits](skills/grill-me/SKILL.md#credits). |

Where a skill takes method from someone else's work, the credit sits in its own
`## Credits` section naming the source, its licence, and the commit it was read
at. Attribution is courtesy here, not a licence condition.

## Feedback

If you have questions, feel free to [contact me](https://keithcrawford.me/connect/).
If you would like to suggest an improvement or add a skill, see
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). Use and adapt these freely. Keep the copyright notice with any
copy, which is the one thing the licence asks.

Each `SKILL.md` carries a copyright line and an SPDX identifier pointing back to
this licence, so a copied folder still names its terms.
