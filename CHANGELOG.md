# Changelog

Notable changes to this repository. Skills carry their own `version` in
`SKILL.md` frontmatter; the versions below are repository releases.

## v1.3.0 — 2026-08-31

### Changed

- The marketplace is now named `tsudo-skills`, not `crawford-skills`. Install
  commands are `/plugin install <skill>@tsudo-skills`. The name matches the
  account and the repository, which is what people were already typing.

### Added

- `deslopify` 1.0.0. Rewrites prose that reads as machine-generated into plain,
  direct writing, fixing structure before sentences before vocabulary. Derived
  from [docwriter-org/plain-writing-skill](https://github.com/docwriter-org/plain-writing-skill)
  by Shreya Shankar (MIT), sharing no lines with it.
- First skill in this repository to ship bundled reference files. `tells.md`
  carries the rule set and `eval-fixtures.md` carries a self-test of one input
  per rule. Both were needed to make the SPDX-on-bundled-files CI step run
  against a real file for the first time; it had only ever seen an empty set.

## v1.2.0 — 2026-08-29

### Changed

- `altitude-check` 1.0.0 → 1.1.0, from two fresh-context test runs against the
  published file.
  - **A written plan is now a first-class source for the goal.** It was named
    as one in three places and missing from the step that actually establishes
    the goal, so the trackerless path could dead-end on a plan file sitting
    right there.
  - **Non-interactive runs have a path.** Where nobody can be asked, a goal
    implied by the evidence gets reconstructed and labelled unconfirmed; a goal
    that is merely vague still stops the run.
  - **Auto-applied fixes are scoped to trackers, and never to your files.**
    Correcting a plan or a README is not hygiene, however obviously right it
    looks. Previously a reader could take the auto-apply clause as licence to
    edit the documents it had just been reading.
  - Convention discovery moved into Step 1, ahead of drafting, instead of a
    clause at the point of writing.
  - Checks with an answerable half now split their verdict rather than
    collapsing to one; partial detail no longer aborts a run the way partial
    access does; and a run that returns findings on all eight checks is called
    out as suspicious in its own right, not just an all-clear one.

## v1.1.0 — 2026-08-29

### Added

- `altitude-check` — zooms out on one body of work, reads the decisions taken
  since the plan was written, judges what is open against the goal, and names one
  next thing to do. Useful mid-session when the work has drilled into sub-tasks
  and nobody has checked the goal in hours. Works with an issue tracker or
  without one; checks a source cannot answer are reported as not applicable
  rather than skipped.
- CI now asserts an SPDX identifier on every bundled file a skill ships
  alongside its `SKILL.md`. Nothing bundles anything today, so the check guards
  the next skill that does — a copied file leaves `LICENSE` behind.

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
