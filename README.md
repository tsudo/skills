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

## Install

Pick your runtime. One thing to know before you do: Claude Code installs each
skill as its own plugin, so you can take `reframe` and leave the rest. OpenAI
packages a repository as a single plugin, so installing it in Codex or ChatGPT
brings all four. If you only want one skill on an OpenAI runtime, copy the
directory instead. That path is at the bottom and it works everywhere.

### Codex

Add this repository as a marketplace, then install `tsudo-skills` from the
plugin picker:

```bash
codex plugin marketplace add tsudo/skills
```

Pin to a tag if you would rather not track `main`:

```bash
codex plugin marketplace add tsudo/skills --ref v1.4.0
```

For one skill rather than the set, copy it into a directory Codex reads:

```bash
mkdir -p "$HOME/.agents/skills"
cp -r skills/reframe "$HOME/.agents/skills/"
```

Codex picks up the change on its own. Use `$REPO_ROOT/.agents/skills` instead
to scope a skill to a single project.

### ChatGPT

Two different things travel under the word "skill" here, and they install
differently.

A **standalone skill** is one directory. Upload it in the desktop app and it
appears in the Skills sidebar. Take any directory under `skills/` and upload it
on its own.

A **plugin** is this whole repository, installed from the plugin directory, and
it works across Chat and Work surfaces rather than the desktop app alone.

Both depend on your account having the feature and, on a work account, on your
workspace policy allowing it. If you cannot see the Skills sidebar or the plugin
directory, that is an account or admin question rather than anything about this
repository.

### Claude Code

```text
/plugin marketplace add tsudo/skills
/plugin install reframe@tsudo-skills
```

Swap `reframe` for whichever skill you want. Each installs separately.

### Manual install

Copy the directory where your runtime looks for skills:

| Runtime | Destination |
| --- | --- |
| Codex, one user | `$HOME/.agents/skills` |
| Codex, one repository | `$REPO_ROOT/.agents/skills` |
| Claude Code | `~/.claude/skills` |

```bash
cp -r skills/reframe ~/.claude/skills/
```

There is also a cross-runtime registry, if you already use it:

```bash
npx skills add tsudo/skills --skill reframe
```

To load a skill through the OpenAI API instead, its create endpoint takes either
the directory or a single zip of it. Build the zips yourself:

```bash
python scripts/validate-openai-package.py --build-archives dist/
```

## Feedback

If you have questions, feel free to [contact me](https://keithcrawford.me/connect/).

If you would like to suggest an improvement or add a skill, see
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). Use and adapt these freely. Attribution is appreciated.
