# apme-clients

Polyglot client SDKs for **Apostille Me**. Generated and handwritten clients share the OpenAPI contract in `openapi/openapi.yaml`, while every language keeps idiomatic authentication, transport injection, retries, and error handling.

## Zed package graph

This repository is a Zed package installed under `.vendor/.zed`. It imports both canonical package layers:

- `apostille-me/apme-interfaces` — wire contracts and shared interfaces
- `apostille-me/apme-libs` — shared product behavior and helpers

Each supported Zed adapter is exposed as a target from the root `.zpkg.toml`. C, C++, and Zig remain buildable repository slices under `[targets.repository]` until Zed defines native adapters for those ecosystems. A `.zpkg.lock` is committed only when produced by a real resolver run.

## Client matrix

| Ecosystem | Path | Package metadata |
|---|---|---|
| C | `clients/c` | `CMakeLists.txt` |
| C++ | `clients/cpp` | `CMakeLists.txt` |
| Zig | `clients/zig` | `build.zig` |
| Gleam | `clients/gleam` | `gleam.toml` |
| Erlang | `clients/erlang` | `rebar.config` |
| Elixir | `clients/elixir` | `mix.exs` |
| Dart | `clients/dart` | `pubspec.yaml` |
| Rust | `clients/rust` | `Cargo.toml` |
| Rust/WASM | `clients/wasm` | `Cargo.toml` |
| Java | `clients/java` | `pom.xml` |
| Go | `clients/go` | `go.mod` |
| Python 3 | `clients/python` | `pyproject.toml` |
| Ruby | `clients/ruby` | `apme_client.gemspec` |
| PHP | `clients/php` | `composer.json` |
| TypeScript | `clients/typescript` | `package.json` |
| TypeScript / Node.js | `clients/typescript/nodejs` | package export |
| TypeScript / Deno | `clients/typescript/deno` | package export |
| TypeScript / Bun | `clients/typescript/bun` | package export |
| TypeScript / edge runtimes | `clients/typescript/edge` | package export |
| Kotlin | `clients/kotlin` | `build.gradle.kts` |
| Swift | `clients/swift` | `Package.swift` |

The SDK methods align with the shared edge contract: `health`, `getConfig`, `emitEvent`, and `emitAlert`. Every implementation accepts or prepares for an injectable transport so callers can supply platform networking, retries, telemetry, and deterministic tests without changing the public API.

## Validation

```bash
./scripts/validate-client-layout.sh
./scripts/test.sh
```

`test.sh` builds C and C++ with CMake, tests Zig when available, runs every other locally available toolchain, and reports explicit skips for unavailable ecosystems. CI can install the full matrix without changing the repository contract.
