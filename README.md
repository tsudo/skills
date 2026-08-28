# skills

![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg)

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

## Feedback

If you have questions, feel free to [contact me](https://keithcrawford.me/connect/).
If you would like to suggest an improvement or add a skill, see
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC-BY-4.0](LICENSE). Use and adapt these freely, with attribution.

Each `SKILL.md` carries its own attribution footer, because a copied file leaves the repository behind.
