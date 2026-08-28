# Repository Profile

Profile: content

This repository publishes content. The content profile treats CI as not applicable
unless a validation command is deliberately added.

This repository adds one. `.github/workflows/validate.yml` runs `agentskills validate`
and two path checks on every pull request and every push to `main`, because a skills
repository can ship a broken unit that looks fine in review. The deviation is
deliberate, not an oversight.
