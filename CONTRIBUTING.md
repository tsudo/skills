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
- includes `license: MIT` frontmatter and a footer carrying the author, the
  copyright line, an SPDX identifier, and an absolute link to the repository
  LICENSE, so a copied folder still names its terms
- credits any source it took method from in a `## Credits` section, naming the
  author, their repository, the licence, and the commit you read it at

Three commands check most of that:

```bash
agentskills validate ./skills/<name>
grep -rnE '/home/|/Users/|C:\\' skills/<name>
grep -rn '\.\./' skills/<name>
```

## Frontmatter that only one runtime reads

`name` and `description` are the two fields every runtime uses. The rest are
additive, and two of them are worth explaining because they look like promises
they do not make.

`allowed-tools` is Claude-compatible metadata. Claude Code reads it and scopes
the skill accordingly; OpenAI runtimes ignore it. It is a hint about what a
skill needs, not a permission grant anywhere, and it is not a security boundary
on any runtime. Keep it accurate, and do not write a skill that depends on it
being enforced.

`compatibility` is prose for a human deciding whether to install. Nothing parses
it. Say what the skill needs and what it writes, including what it does when the
runtime has no writable location, because ChatGPT often does not.

`agentskills` comes from the `skills-ref` package: `pip install skills-ref`.
Both greps should return nothing. CI runs all three on every pull request.

The real test is simpler than the commands: copy the folder into a project
that has none of your setup, and see whether it still works.

## What doesn't fit here

Skills that only make sense inside one workspace, need a custom installer, or
expect another skill to be installed alongside them. If it can't survive
`cp -r` into a stranger's project, it belongs somewhere else.
