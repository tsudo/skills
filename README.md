# Tsudo's AI Skills Library

![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## Welcome to Tsudo's Skills

These are skills I have authored or adapted. I hope you find them useful.

**Each skill is standalone**: install or copy a single skill directory and it works, with nothing else from this repo.

## Skills

- [`reframe`](skills/reframe/SKILL.md) - Turns a long analysis or conversation into a standalone report, using the restructuring as a second analytical pass.
- [`grill-me`](skills/grill-me/SKILL.md) - Interviews you about a half-formed plan until it is committable, then closes with a pre-mortem. Credits: [Pocock](https://github.com/mattpocock/skills), [Miessler](https://github.com/danielmiessler/LifeOS)
- [`altitude-check`](skills/altitude-check/SKILL.md) - Zooms out on one body of work, checks whether what is open still serves the goal, and names the single next thing to do. Works with a tracker or without one.
- [`deslopify`](skills/deslopify/SKILL.md) - Rewrites prose that reads as machine-generated into plain, direct writing, fixing structure before sentences before vocabulary. Credits: [Shankar](https://github.com/docwriter-org/plain-writing-skill)
- [`retro`](skills/retro/SKILL.md) - Runs a retrospective on the work you just finished and puts each lesson where the next session will load it, once you approve the plan.
- [`eli5`](skills/eli5/SKILL.md) - Explains an unfamiliar topic to a smart adult who is new to it: a short walkthrough, then a comic-strip page when the topic has steps. Inspired by [Clarke](https://x.com/graceclarke)
- [`council`](skills/council/SKILL.md) - Puts a real decision to a panel of independent advisor seats, then gives you the disagreement, what decides it, and a labelled recommendation. Inspired by decision-council (Fusion Software)

## Install

Claude Code installs each skill separately. Codex and ChatGPT install the whole
repository as one plugin.

### Codex

```bash
codex plugin marketplace add tsudo/skills
```

Then install `tsudo-skills` from the plugin picker. Add `--ref v1.5.1` to pin a
version instead of tracking `main`.

### ChatGPT

Upload a single skill directory in the desktop app and it appears in the Skills
sidebar. Or install the whole repository from the plugin directory, which also
works on web and mobile.

Both need the feature on your account, and your admin's permission on a work
account.

### Claude Code

```text
/plugin marketplace add tsudo/skills
/plugin install reframe@tsudo-skills
```

Swap `reframe` for any skill above.

### Manual install

```bash
cp -r skills/reframe ~/.claude/skills/
```

| Runtime | Destination |
| --- | --- |
| Claude Code | `~/.claude/skills` |
| Codex, all projects | `$HOME/.agents/skills` |
| Codex, one project | `$REPO_ROOT/.agents/skills` |

Or through a cross-runtime registry:

```bash
npx skills add tsudo/skills --skill reframe
```

The OpenAI Skills API takes either a skill directory or a zip of one.

## Feedback

If you have questions, feel free to [contact me](https://keithcrawford.me/connect/).

If you would like to suggest an improvement or add a skill, see
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). Use and adapt these freely. Attribution is appreciated.
