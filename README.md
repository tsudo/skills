# Tsudo's AI Skills Library

![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## Welcome to Tsudo's Skills

These are skills I have authored or adapted. I hope you find them useful.

**Each skill is standalone**: install or copy a single skill directory and it works, with nothing else from this repo.

## Skills

- [`reframe`](skills/reframe/SKILL.md) - Turns a long analysis or conversation into a standalone report, using the restructuring as a second analytical pass.
- [`grill-me`](skills/grill-me/SKILL.md) - Interviews you about a half-formed plan until it is committable, then closes with a pre-mortem. Credits: [Pocock](https://github.com/mattpocock/skills), [Miessler](https://github.com/danielmiessler/LifeOS)
- [`altitude-check`](skills/altitude-check/SKILL.md) - Zooms out on one body of work, checks whether what is open still serves the goal, and names the single next thing to do. Works with a tracker or without one.

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

[MIT](LICENSE). Use and adapt these freely. Attribution is appreciated.
