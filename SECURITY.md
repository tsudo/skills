# Security Policy

## What counts as a security issue here

This repository ships instructions that an AI agent reads and acts on, so the
risk surface is the content itself:

- A `SKILL.md` whose instructions would lead an agent to exfiltrate data, damage
  files, or take an action a reader would not expect from its description.
- A bundled script that does something other than what the skill says it does.
- A reference or example that leaks a credential or personal data.
- Anything in this repository that misrepresents what a skill does.

## Reporting

Report privately to [keith@keithcrawford.me](mailto:keith@keithcrawford.me) rather than opening a public issue.
Include the affected file, what an agent would do as a result, and how you found
it. Do not include real secrets, credentials, or personal data in the report.

Expect an acknowledgement within a week. This is a personal project with no
on-call rotation, so that is a realistic commitment rather than an SLA.
