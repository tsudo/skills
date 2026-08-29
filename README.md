# Tsudo's AI skills library

![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## Welcome

Welcome to Tsudo's Skills.

These are skills I have authored or adapted. I hope you find them useful.

*Each skill is standalone*: install or copy a single skill directory and it works, with nothing else from this repo.

## Skills

| Skill | What it does | Credit |
| --- | --- | --- |
| [`reframe`](skills/reframe/SKILL.md) | Turns a long analysis or conversation into a standalone report, using the restructuring as a second analytical pass. | — |
| [`grill-me`](skills/grill-me/SKILL.md) | Interviews you about a half-formed plan until it is committable, then closes with a pre-mortem. | [Matt Pocock](https://github.com/mattpocock/skills), [Daniel Miessler](https://github.com/danielmiessler/LifeOS) |

Each skill names its full sources, their licences, and the commits they were read
at in its own `## Credits` section.

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

## Feedback

If you have questions, feel free to [contact me](https://keithcrawford.me/connect/).
If you would like to suggest an improvement or add a skill, see
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). Use and adapt these freely. Keep the copyright notice with any
copy, which is the one thing the licence asks.

Each `SKILL.md` carries a copyright line and an SPDX identifier pointing back to
this licence, so a copied folder still names its terms.
