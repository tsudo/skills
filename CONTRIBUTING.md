# Contributing

## Before Opening a Change

One change per pull request, and say how you checked it. If the change touches
a skill, run the three commands under Skill Contributions and paste the results.

## Skill Contributions

Open an issue before adding a new skill. A publishable skill must:

- be useful in a project that has none of your local setup
- use a `skills/<name>/SKILL.md` directory with `name` matching the directory
- keep all required context inside its own skill directory
- contain no absolute paths, credentials, customer data, or anything private to the
  project it came from
- include `license: CC-BY-4.0` frontmatter and an attribution footer

Run these checks before opening a pull request:

```bash
agentskills validate ./skills/<name>
grep -rnE '/home/|/Users/|C:\\' skills/<name>
grep -rn '\.\./' skills/<name>
```

`agentskills` comes from the `skills-ref` package: `pip install skills-ref`.
The two `grep` commands should return no matches.

## Commit Statements

Write a short imperative statement describing the change:

- `Add repository scaffold`
- `Document publication workflow`
- `Fix license attribution`

This repository does not use Conventional Commits. With one skill per directory
and no released package, the `feat:`/`fix:` prefixes carry no version semantics
here and only add noise. Plain sentences are easier to scan in a short log.

## Pull Requests

Say what the change does, how you verified it, and anything you knowingly left undone.
