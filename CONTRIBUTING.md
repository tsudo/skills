# Contributing

Fixes and corrections are welcome. A new skill needs a conversation first —
open an [issue](https://github.com/tsudo/skills/issues) and say what it does
before you write it.

Found a security problem? See [SECURITY.md](SECURITY.md) rather than
opening an issue.

## The bar for a skill

Everything here has to work in someone else's project on the first run.
So a skill:

- lives at `skills/<name>/SKILL.md`, with `name` matching the directory
- keeps everything it needs inside its own directory: no `../`, no sibling
  skills, nothing from the repository root
- carries no absolute paths, credentials, customer data, or anything private
  to the project it came from
- includes `license: CC-BY-4.0` frontmatter and an attribution footer, since
  a copied file leaves the LICENSE behind

Three commands check most of that:

```bash
agentskills validate ./skills/<name>
grep -rnE '/home/|/Users/|C:\\' skills/<name>
grep -rn '\.\./' skills/<name>
```

`agentskills` comes from the `skills-ref` package: `pip install skills-ref`.
Both greps should return nothing. CI runs all three on every pull request.

The real test is simpler than the commands: copy the folder into a project
that has none of your setup, and see whether it still works.

## What doesn't fit here

Skills that only make sense inside one workspace, need a custom installer, or
expect another skill to be installed alongside them. If it can't survive
`cp -r` into a stranger's project, it belongs somewhere else.
