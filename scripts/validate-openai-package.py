#!/usr/bin/env python3
# Copyright (c) 2026 Keith Crawford
# SPDX-License-Identifier: MIT
"""Validate the OpenAI plugin package and the versions it advertises.

The repository ships two manifests describing the same skills. Codex and
ChatGPT read `.codex-plugin/plugin.json`; Claude Code reads
`.claude-plugin/marketplace.json`. They drift silently, because nothing reads
both. This script does.

Checks:

  manifest   `.codex-plugin/plugin.json` parses, carries the four fields
             OpenAI documents as required, points `skills` at a real
             directory with a relative `./` path, and names no absolute path.
  skills     every directory under the referenced skills path holds a
             SKILL.md with `name` matching its directory.
  openai     any `agents/openai.yaml` parses and its referenced paths exist.
  versions   the plugin manifest, the Claude marketplace manifest, and the
             changelog agree on the release version, and every marketplace
             entry matches its skill's own frontmatter version.

Usage:
    python scripts/validate-openai-package.py
    python scripts/validate-openai-package.py --build-archives dist/
    python scripts/validate-openai-package.py --self-test

`--self-test` runs the control tests in both directions. Broken manifests built
in a temporary directory must be rejected, and a valid one must be accepted. A
check that has never been seen to fail is not known to work, and one that has
never been seen to pass may be rejecting everything.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

REQUIRED_MANIFEST_FIELDS = ("name", "version", "description", "skills")

# Windows drive letters, POSIX home directories, and the absolute roots a
# developer machine leaks most often. The lookbehind on the drive-letter branch
# is load-bearing: without it, the 's:/' inside 'https://' reads as a drive.
ABSOLUTE_PATH = re.compile(
    r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]"
    r"|(?:^|[\s\"'])(?:/home/|/Users/|/root/)"
)

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


class Findings:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def fail(self, message: str) -> None:
        self.errors.append(message)

    def ok(self) -> bool:
        return not self.errors


class UnreadableFile(Exception):
    """Raised instead of letting a decode or I/O error surface as a traceback."""


def read_text(path: Path) -> str:
    """Read a repository file as UTF-8, naming the file when that is not possible.

    Every file this script reads is committed Markdown or JSON, so a failure
    here means a genuinely broken file rather than an unsupported encoding. The
    point of catching it is that the CI log says which file.
    """
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise UnreadableFile(f"{path} is not valid UTF-8 ({exc.reason}).") from exc
    except OSError as exc:
        raise UnreadableFile(f"{path} could not be read: {exc}.") from exc


def read_frontmatter(skill_md: Path) -> dict[str, str]:
    """Pull the flat keys and metadata.version out of a SKILL.md.

    Deliberately small. A full YAML parse would pull in a dependency for four
    fields, and the frontmatter shape here is fixed by CONTRIBUTING.md.
    """
    match = FRONTMATTER.match(read_text(skill_md))
    if not match:
        return {}

    fields: dict[str, str] = {}
    in_metadata = False
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\S", line):
            in_metadata = line.startswith("metadata:")
            key, _, value = line.partition(":")
            if not in_metadata:
                fields[key.strip()] = value.strip().strip("\"'")
        elif in_metadata:
            key, _, value = line.strip().partition(":")
            fields[f"metadata.{key.strip()}"] = value.strip().strip("\"'")
    return fields


def changelog_version(root: Path) -> str | None:
    changelog = root / "CHANGELOG.md"
    if not changelog.exists():
        return None
    for line in read_text(changelog).splitlines():
        match = re.match(r"^##\s+v(\d+\.\d+\.\d+)", line.strip())
        if match:
            return match.group(1)
    return None


def check_manifest(root: Path, found: Findings) -> dict | None:
    manifest_path = root / ".codex-plugin" / "plugin.json"
    if not manifest_path.exists():
        found.fail(f"{manifest_path} does not exist.")
        return None

    raw = read_text(manifest_path)
    try:
        manifest = json.loads(raw)
    except json.JSONDecodeError as exc:
        found.fail(f"{manifest_path} is not valid JSON: {exc}")
        return None

    for field in REQUIRED_MANIFEST_FIELDS:
        if not manifest.get(field):
            found.fail(f"{manifest_path} is missing required field '{field}'.")

    skills_value = manifest.get("skills")
    if isinstance(skills_value, str):
        if not skills_value.startswith("./"):
            found.fail(
                f"manifest 'skills' is '{skills_value}'. It must be a relative "
                "path beginning './' so the package resolves wherever it is installed."
            )
        skills_dir = (root / skills_value.lstrip("./")).resolve()
        if not skills_dir.is_dir():
            found.fail(f"manifest 'skills' points at '{skills_value}', which is not a directory.")
    elif skills_value is not None:
        found.fail("manifest 'skills' must be a string path to the skills directory.")

    for key, value in manifest.items():
        if isinstance(value, str) and ABSOLUTE_PATH.search(value):
            found.fail(f"manifest field '{key}' contains an absolute path: {value}")

    return manifest


def check_skills(root: Path, manifest: dict, found: Findings) -> list[Path]:
    skills_value = manifest.get("skills")
    if not isinstance(skills_value, str):
        return []

    skills_dir = root / skills_value.lstrip("./")
    if not skills_dir.is_dir():
        return []

    directories = sorted(d for d in skills_dir.iterdir() if d.is_dir())
    if not directories:
        found.fail(f"No skill directories under {skills_dir}.")
        return []

    for directory in directories:
        skill_md = directory / "SKILL.md"
        if not skill_md.exists():
            found.fail(f"{directory} has no SKILL.md.")
            continue

        fields = read_frontmatter(skill_md)
        if not fields:
            found.fail(f"{skill_md} has no parseable frontmatter block.")
            continue
        if not fields.get("name"):
            found.fail(f"{skill_md} declares no 'name'.")
        elif fields["name"] != directory.name:
            found.fail(
                f"{skill_md} declares name '{fields['name']}' but sits in "
                f"directory '{directory.name}'. OpenAI resolves skills by directory."
            )
        if not fields.get("description"):
            found.fail(f"{skill_md} declares no 'description'. OpenAI requires it for discovery.")

        check_openai_yaml(directory, found)

    return directories


def check_openai_yaml(skill_dir: Path, found: Findings) -> None:
    """Parse an optional agents/openai.yaml and verify the paths it names."""
    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        return

    try:
        import yaml
    except ImportError:
        found.fail(
            f"{openai_yaml} exists but PyYAML is not installed. "
            "Install it (pip install pyyaml) so this file can be validated."
        )
        return

    try:
        data = yaml.safe_load(read_text(openai_yaml)) or {}
    except yaml.YAMLError as exc:
        found.fail(f"{openai_yaml} is not valid YAML: {exc}")
        return

    if not isinstance(data, dict):
        found.fail(f"{openai_yaml} must contain a mapping at the top level.")
        return

    interface = data.get("interface") or {}
    if isinstance(interface, dict):
        for key in ("icon", "icon_dark", "image"):
            asset = interface.get(key)
            if not isinstance(asset, str) or asset.startswith(("http://", "https://")):
                continue
            if asset.startswith("/") or ".." in asset:
                found.fail(
                    f"{openai_yaml} interface.{key} is '{asset}'. Assets must be "
                    "relative paths inside the skill directory."
                )
            elif not (skill_dir / asset).exists():
                found.fail(f"{openai_yaml} interface.{key} points at missing asset '{asset}'.")


def check_codex_marketplace(root: Path, manifest: dict, found: Findings) -> None:
    """Verify the Codex marketplace catalog, if the repo ships one.

    `codex plugin marketplace add owner/repo` reads
    .agents/plugins/marketplace.json, not the plugin manifest. A repo that
    advertises that command without this file sends users to a dead path.
    """
    catalog_path = root / ".agents" / "plugins" / "marketplace.json"
    if not catalog_path.exists():
        return

    try:
        catalog = json.loads(read_text(catalog_path))
    except json.JSONDecodeError as exc:
        found.fail(f"{catalog_path} is not valid JSON: {exc}")
        return

    if not catalog.get("name"):
        found.fail(f"{catalog_path} is missing required field 'name'.")
    if not ((catalog.get("interface") or {}).get("displayName")):
        found.fail(f"{catalog_path} is missing required field 'interface.displayName'.")

    entries = catalog.get("plugins")
    if not entries:
        found.fail(f"{catalog_path} lists no plugins.")
        return

    for entry in entries:
        name = entry.get("name")
        if not name:
            found.fail(f"{catalog_path} has a plugin entry with no 'name'.")
            continue
        policy = entry.get("policy") or {}
        if not policy.get("installation"):
            found.fail(f"{catalog_path} entry '{name}' declares no policy.installation.")

        source = entry.get("source") or {}
        kind = source.get("source")
        if kind == "local":
            target = source.get("path")
            if not target:
                found.fail(f"{catalog_path} entry '{name}' is a local source with no path.")
                continue
            plugin_manifest = (root / target / ".codex-plugin" / "plugin.json").resolve()
            if not plugin_manifest.exists():
                found.fail(
                    f"{catalog_path} entry '{name}' points at '{target}', which holds "
                    "no .codex-plugin/plugin.json."
                )
            elif name != manifest.get("name"):
                found.fail(
                    f"{catalog_path} entry is named '{name}' but the plugin manifest "
                    f"it points at is named '{manifest.get('name')}'."
                )
        elif kind is None:
            found.fail(f"{catalog_path} entry '{name}' declares no source.source.")


def check_versions(root: Path, manifest: dict, found: Findings) -> None:
    plugin_version = manifest.get("version")
    marketplace_path = root / ".claude-plugin" / "marketplace.json"

    changelog = changelog_version(root)
    if changelog and plugin_version and changelog != plugin_version:
        found.fail(
            f"CHANGELOG.md's newest release is v{changelog} but "
            f".codex-plugin/plugin.json says {plugin_version}. A pinned install "
            "resolves to a version the changelog does not describe."
        )

    if not marketplace_path.exists():
        return

    try:
        marketplace = json.loads(read_text(marketplace_path))
    except json.JSONDecodeError as exc:
        found.fail(f"{marketplace_path} is not valid JSON: {exc}")
        return

    marketplace_version = (marketplace.get("metadata") or {}).get("version")
    if plugin_version and marketplace_version and marketplace_version != plugin_version:
        found.fail(
            f".claude-plugin/marketplace.json metadata.version is "
            f"{marketplace_version} but .codex-plugin/plugin.json is "
            f"{plugin_version}. The two manifests describe one release."
        )

    for entry in marketplace.get("plugins") or []:
        name = entry.get("name")
        declared = entry.get("version")
        if not name or not declared:
            continue
        skill_md = root / "skills" / name / "SKILL.md"
        if not skill_md.exists():
            found.fail(f"marketplace.json lists '{name}' but skills/{name}/SKILL.md does not exist.")
            continue
        actual = read_frontmatter(skill_md).get("metadata.version")
        if actual and actual != declared:
            found.fail(
                f"marketplace.json gives '{name}' version {declared} but its "
                f"SKILL.md declares {actual}."
            )


def build_archives(root: Path, manifest: dict, skill_dirs: list[Path], out_dir: Path) -> None:
    """Write the plugin archive and one zip per skill for direct API upload."""
    out_dir.mkdir(parents=True, exist_ok=True)

    plugin_zip = out_dir / f"{manifest['name']}-{manifest['version']}.zip"
    with zipfile.ZipFile(plugin_zip, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.write(root / ".codex-plugin" / "plugin.json", ".codex-plugin/plugin.json")
        for directory in skill_dirs:
            for path in sorted(directory.rglob("*")):
                if path.is_file():
                    archive.write(path, str(path.relative_to(root)).replace("\\", "/"))
    print(f"  built {plugin_zip.relative_to(root)}")

    for directory in skill_dirs:
        skill_zip = out_dir / f"{directory.name}.zip"
        with zipfile.ZipFile(skill_zip, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(directory.rglob("*")):
                if path.is_file():
                    archive.write(path, str(path.relative_to(directory.parent)).replace("\\", "/"))
        print(f"  built {skill_zip.relative_to(root)}")


def validate(root: Path) -> Findings:
    found = Findings()
    try:
        manifest = check_manifest(root, found)
        if manifest is not None:
            check_skills(root, manifest, found)
            check_codex_marketplace(root, manifest, found)
            check_versions(root, manifest, found)
    except UnreadableFile as exc:
        found.fail(str(exc))
    return found


def self_test() -> int:
    """Control tests, both directions.

    Negative fixtures must fail, or a check is not working. The positive
    fixture must pass, or a check is over-matching -- which is how the
    drive-letter pattern once read the 's:/' in 'https://' as an absolute path
    and rejected every manifest carrying a homepage.
    """
    failures = 0

    positive = Path(tempfile.mkdtemp())
    try:
        scaffold(positive, extra={
            "homepage": "https://github.com/tsudo/skills",
            "repository": "https://github.com/tsudo/skills",
            "author": "Keith Crawford",
        })
        result = validate(positive)
        if result.ok():
            print("  ok: 'a valid package with URLs' correctly accepted")
        else:
            print("  SELF-TEST FAIL: 'a valid package with URLs' was rejected:")
            for error in result.errors:
                print(f"    {error}")
            failures += 1
    finally:
        shutil.rmtree(positive, ignore_errors=True)

    fixtures: list[tuple[str, object]] = []

    def fixture(name):
        def register(fn):
            fixtures.append((name, fn))
            return fn
        return register

    @fixture("manifest missing entirely")
    def _(root: Path) -> None:
        (root / ".codex-plugin").mkdir()

    @fixture("manifest is not valid JSON")
    def _(root: Path) -> None:
        scaffold(root)
        (root / ".codex-plugin" / "plugin.json").write_text("{ not json", encoding="utf-8")

    @fixture("skills path does not exist")
    def _(root: Path) -> None:
        scaffold(root, skills="./nonexistent/")

    @fixture("skills path is not relative")
    def _(root: Path) -> None:
        scaffold(root, skills="/absolute/skills/")

    @fixture("manifest carries an absolute path")
    def _(root: Path) -> None:
        scaffold(root, extra={"homepage": "/Users/someone/skills"})

    @fixture("required field missing")
    def _(root: Path) -> None:
        scaffold(root, drop="description")

    @fixture("skill name does not match its directory")
    def _(root: Path) -> None:
        scaffold(root, skill_name="something-else")

    @fixture("changelog version disagrees with the manifest")
    def _(root: Path) -> None:
        scaffold(root)
        (root / "CHANGELOG.md").write_text("# Changelog\n\n## v9.9.9 - 2026-01-01\n", encoding="utf-8")

    @fixture("codex marketplace entry points at a directory with no plugin manifest")
    def _(root: Path) -> None:
        scaffold(root)
        catalog = root / ".agents" / "plugins"
        catalog.mkdir(parents=True)
        (catalog / "marketplace.json").write_text(json.dumps({
            "name": "demo-package",
            "interface": {"displayName": "Demo"},
            "plugins": [{
                "name": "demo-package",
                "source": {"source": "local", "path": "./nowhere"},
                "policy": {"installation": "AVAILABLE"},
            }],
        }, indent=2), encoding="utf-8")

    @fixture("codex marketplace name disagrees with the plugin manifest")
    def _(root: Path) -> None:
        scaffold(root)
        catalog = root / ".agents" / "plugins"
        catalog.mkdir(parents=True)
        (catalog / "marketplace.json").write_text(json.dumps({
            "name": "demo-package",
            "interface": {"displayName": "Demo"},
            "plugins": [{
                "name": "a-different-name",
                "source": {"source": "local", "path": "."},
                "policy": {"installation": "AVAILABLE"},
            }],
        }, indent=2), encoding="utf-8")

    for name, build in fixtures:
        tmp = Path(tempfile.mkdtemp())
        try:
            build(tmp)
            result = validate(tmp)
            if result.ok():
                print(f"  SELF-TEST FAIL: '{name}' passed validation but must not.")
                failures += 1
            else:
                print(f"  ok: '{name}' correctly rejected")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        print(f"\n{failures} control(s) behaved wrongly. The checks are not proven.")
        return 1
    print(f"\n1 positive and {len(fixtures)} negative controls all behaved as intended.")
    return 0


def scaffold(root: Path, *, skills: str = "./skills/", skill_name: str = "demo",
             drop: str | None = None, extra: dict | None = None) -> None:
    """A minimally valid package, so each fixture breaks exactly one thing."""
    (root / ".codex-plugin").mkdir(parents=True, exist_ok=True)
    skill_dir = root / "skills" / "demo"
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {skill_name}\ndescription: A demo skill.\n---\n\nBody.\n",
        encoding="utf-8",
    )
    manifest = {
        "name": "demo-package",
        "version": "1.0.0",
        "description": "Demo.",
        "skills": skills,
    }
    if extra:
        manifest.update(extra)
    if drop:
        manifest.pop(drop, None)
    (root / ".codex-plugin" / "plugin.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root (default: current directory)")
    parser.add_argument("--build-archives", metavar="DIR",
                        help="Also write the plugin archive and per-skill zips to DIR")
    parser.add_argument("--self-test", action="store_true",
                        help="Run the negative control instead of validating the repository")
    args = parser.parse_args()

    if args.self_test:
        print("Control tests:")
        return self_test()

    root = Path(args.root).resolve()
    print(f"Validating OpenAI package in {root}")

    found = validate(root)
    if not found.ok():
        print()
        for error in found.errors:
            print(f"  FAIL: {error}")
        print(f"\n{len(found.errors)} problem(s) found.")
        return 1

    print("  manifest, skills, and versions all check out.")

    if args.build_archives:
        manifest = json.loads(read_text(root / ".codex-plugin" / "plugin.json"))
        skills_dir = root / manifest["skills"].lstrip("./")
        skill_dirs = sorted(d for d in skills_dir.iterdir() if d.is_dir())
        print("Building archives:")
        build_archives(root, manifest, skill_dirs, Path(args.build_archives).resolve())

    return 0


if __name__ == "__main__":
    sys.exit(main())
