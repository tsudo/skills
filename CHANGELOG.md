# Changelog

Notable changes to this repository. Skills carry their own `version` in
`SKILL.md` frontmatter; the versions below are repository releases.

## v1.0.1 — 2026-08-29

### Added

- `grill-me` — a relentless interview that sharpens a half-formed idea, plan, or
  decision until it is committable. Derived in method from two MIT-licensed
  sources, credited in the skill's own `## Credits` section.
- CI now validates every directory under `skills/` rather than a named one, and
  fails the build if any skill is missing its `license: MIT` frontmatter,
  copyright line, SPDX identifier, or link to the repository `LICENSE`.
- This changelog.

### Changed

- **Licence changed from CC-BY-4.0 to MIT.** MIT is a software licence and these
  skills are instructions an agent executes; Creative Commons recommends against
  CC licences for software. Each `SKILL.md` now carries a copyright line and an
  SPDX identifier pointing back to the repository `LICENSE`.
- README retitled and trimmed; `CONTRIBUTING.md` rewritten for a small repository.

### Note on v1.0.0

`v1.0.0` was published under CC-BY-4.0. That grant is perpetual and irrevocable
for anyone who obtained the repository at that tag, and it still applies to that
version. Everything from `v1.0.1` forward is MIT.

## v1.0.0 — 2026-08-29

- First public release.
- `reframe` — turns an analysis or long conversation into a standalone Markdown
  report, using the restructuring as a second pass over the reasoning.
- Claude Code plugin marketplace manifest, CI validation, and the repository
  scaffold.

Published under CC-BY-4.0. See the note above.
