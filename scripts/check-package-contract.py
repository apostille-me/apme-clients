#!/usr/bin/env python3
"""Validate the Apostille Me polyglot package, SDK targets, and runtime adapters."""

from __future__ import annotations

import json
import pathlib
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPECTED_DEPS = {"apostille-me/apme-interfaces", "apostille-me/apme-libs"}

CANONICAL_TARGETS = {
    "repository": ".",
    "c": "clients/c",
    "cpp": "clients/cpp",
    "zig": "clients/zig",
    "nodejs": "clients/typescript",
    "golang": "clients/go",
    "python": "clients/python",
    "ruby": "clients/ruby",
    "php": "clients/php",
    "rust": "clients/rust",
    "rust-wasm": "clients/wasm",
    "dart": "clients/dart",
    "gleam": "clients/gleam",
    "erlang": "clients/erlang",
    "elixir": "clients/elixir",
    "java": "clients/java",
    "kotlin": "clients/kotlin",
    "swift": "clients/swift",
}

TARGET_IMPLEMENTATIONS: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
    "c": (("CMakeLists.txt", "Makefile", "meson.build"), (".c", ".h")),
    "cpp": (("CMakeLists.txt", "Makefile", "meson.build"), (".cc", ".cpp", ".cxx", ".hpp", ".h")),
    "zig": (("build.zig", "build.zig.zon"), (".zig",)),
    "nodejs": (("package.json", "tsconfig.json"), (".ts", ".tsx", ".js", ".mjs")),
    "golang": (("go.mod",), (".go",)),
    "python": (("pyproject.toml", "setup.py", "setup.cfg"), (".py",)),
    "ruby": (("*.gemspec", "Gemfile"), (".rb",)),
    "php": (("composer.json",), (".php",)),
    "rust": (("Cargo.toml",), (".rs",)),
    "rust-wasm": (("Cargo.toml",), (".rs",)),
    "dart": (("pubspec.yaml",), (".dart",)),
    "gleam": (("gleam.toml",), (".gleam",)),
    "erlang": (("rebar.config", "erlang.mk"), (".erl", ".hrl")),
    "elixir": (("mix.exs",), (".ex", ".exs")),
    "java": (("pom.xml", "build.gradle", "build.gradle.kts"), (".java",)),
    "kotlin": (("build.gradle.kts", "build.gradle", "pom.xml"), (".kt",)),
    "swift": (("Package.swift",), (".swift",)),
}

RUNTIME_ADAPTERS = {
    "node": "clients/typescript/nodejs",
    "deno": "clients/typescript/deno",
    "bun": "clients/typescript/bun",
    "edge": "clients/typescript/edge",
}


def load(path: pathlib.Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def has_marker(base: pathlib.Path, patterns: tuple[str, ...]) -> bool:
    return any(any(base.glob(pattern)) for pattern in patterns)


def has_source(base: pathlib.Path, suffixes: tuple[str, ...]) -> bool:
    return any(path.is_file() and path.suffix.lower() in suffixes for path in base.rglob("*"))


def validate_surface(
    errors: list[str],
    label: str,
    directory: str,
    markers: tuple[str, ...],
    suffixes: tuple[str, ...],
) -> None:
    base = ROOT / directory
    if not base.is_dir():
        errors.append(f"{label}: missing {directory}")
        return
    if markers and not has_marker(base, markers):
        errors.append(f"{label}: missing build/package marker from {markers!r}")
    if not has_source(base, suffixes):
        errors.append(f"{label}: missing implementation source with suffixes {suffixes!r}")


def main() -> int:
    errors: list[str] = []
    manifest = load(ROOT / ".zpkg.toml")
    lock = load(ROOT / ".zpkg.lock")
    package = manifest.get("package", {})
    dependencies = manifest.get("dependencies", {})
    targets = manifest.get("targets", {})

    if package.get("org") != "apostille-me" or package.get("name") != "apme-clients":
        errors.append("package identity must be apostille-me/apme-clients")
    if package.get("repository", {}).get("url") != "https://github.com/apostille-me/apme-clients":
        errors.append("package.repository.url must match the canonical repository")
    if package.get("language") == "polyglot":
        errors.append("package.language must not use the noncanonical polyglot alias")

    if not isinstance(dependencies, dict) or not EXPECTED_DEPS.issubset(dependencies):
        errors.append("apme-clients must depend on apme-interfaces and apme-libs")
        dependencies = dependencies if isinstance(dependencies, dict) else {}
    for dependency in dependencies:
        if dependency.rsplit("/", 1)[-1].endswith(("-cli", "-infra")):
            errors.append(f"forbidden client dependency: {dependency}")

    if lock.get("version") != 1:
        errors.append(".zpkg.lock must use version = 1")
    if not isinstance(targets, dict):
        errors.append("[targets] must be a table")
        targets = {}

    declared_targets = set(targets)
    canonical_targets = set(CANONICAL_TARGETS)
    for target in sorted(canonical_targets - declared_targets):
        errors.append(f"missing canonical Zed target: {target}")
    for target in sorted(declared_targets - canonical_targets):
        errors.append(f"noncanonical Zed target must not be declared: {target}")

    for target, directory in CANONICAL_TARGETS.items():
        record = targets.get(target)
        if not isinstance(record, dict):
            continue
        if record.get("dir") != directory:
            errors.append(f"targets.{target}.dir must be {directory!r}")
        if target in TARGET_IMPLEMENTATIONS:
            markers, suffixes = TARGET_IMPLEMENTATIONS[target]
            validate_surface(errors, target, directory, markers, suffixes)

    for runtime, directory in RUNTIME_ADAPTERS.items():
        validate_surface(errors, f"typescript-{runtime}", directory, (), (".ts", ".js", ".mjs"))

    matrix_path = ROOT / "clients/typescript/runtime-matrix.json"
    try:
        matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid or missing TypeScript runtime matrix: {exc}")
    else:
        runtimes = matrix.get("runtimes", {})
        for runtime in RUNTIME_ADAPTERS:
            record = runtimes.get(runtime)
            if not isinstance(record, dict) or record.get("supported") is not True or not str(record.get("smoke", "")).strip():
                errors.append(f"TypeScript runtime {runtime!r} lacks support and a smoke command")

    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1
    print(
        f"validated {len(CANONICAL_TARGETS)} canonical Zed targets and "
        f"{len(RUNTIME_ADAPTERS)} TypeScript runtime adapters"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
