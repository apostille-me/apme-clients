#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".zpkg.toml"
REQUIRED_DEPENDENCIES = {"apostille-me/apme-interfaces", "apostille-me/apme-libs"}
REQUIRED_TARGETS = {
    "gleam": "clients/gleam",
    "erlang": "clients/erlang",
    "elixir": "clients/elixir",
    "dart": "clients/dart",
    "rust": "clients/rust",
    "java": "clients/java",
    "golang": "clients/go",
    "python": "clients/python",
    "ruby": "clients/ruby",
    "php": "clients/php",
    "nodejs": "clients/typescript/nodejs",
    "deno": "clients/typescript/deno",
    "bun": "clients/typescript/bun",
    "edge": "clients/typescript/edge",
}
REQUIRED_PACKAGE_FIELDS = {"org", "name", "version", "description", "license"}


def fail(message: str) -> None:
    print(f"client-matrix: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    try:
        data = tomllib.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        fail(f"invalid .zpkg.toml: {exc}")
    package = data.get("package")
    if not isinstance(package, dict): fail("missing [package]")
    missing_fields = REQUIRED_PACKAGE_FIELDS - package.keys()
    if missing_fields: fail(f"[package] is missing: {', '.join(sorted(missing_fields))}")
    repository = package.get("repository")
    if not isinstance(repository, dict) or repository.get("vcs") != "git" or not repository.get("url"):
        fail("missing valid [package.repository] git metadata")
    install = data.get("install")
    if not isinstance(install, dict) or install.get("dir") != ".vendor/.zed": fail('[install].dir must be ".vendor/.zed"')
    dependencies = data.get("dependencies")
    if not isinstance(dependencies, dict): fail("missing [dependencies]")
    missing_dependencies = REQUIRED_DEPENDENCIES - dependencies.keys()
    if missing_dependencies: fail(f"missing Zed dependencies: {', '.join(sorted(missing_dependencies))}")
    targets = data.get("targets")
    if not isinstance(targets, dict): fail("missing [targets]")
    for name, expected_dir in REQUIRED_TARGETS.items():
        target = targets.get(name)
        if not isinstance(target, dict): fail(f"missing [targets.{name}]")
        if target.get("dir") != expected_dir: fail(f"[targets.{name}].dir must be {expected_dir!r}")
        target_dir = ROOT / expected_dir
        if not target_dir.is_dir(): fail(f"missing target directory: {expected_dir}")
        if not any(path.is_file() for path in target_dir.rglob("*")): fail(f"target directory is empty: {expected_dir}")
    print(f"client-matrix: OK ({len(REQUIRED_TARGETS)} required targets, {len(REQUIRED_DEPENDENCIES)} Zed dependencies)")


if __name__ == "__main__":
    main()
