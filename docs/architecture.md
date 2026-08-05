# Architecture

`apme-clients` contains generated and hand-written clients for apostille workflows, status checks, uploads, and typed errors.

## Canonical package fleet

- `apme-interfaces` owns wire formats and generated contract types.
- `apme-libs` owns reusable, runtime-light domain behavior.
- `apme-clients` consumes versioned interfaces and exposes language-specific SDKs.
- `apme-sync` owns offline-first reconciliation boundaries.
- `apme-api` and the web runtimes own deployment behavior.
- `apme-cli` composes clients, interfaces, and libraries for operator workflows.
- `apme-monorepo` coordinates pinned revisions without becoming a second package identity.

The long-name bootstrap repositories are historical aliases, not package sources. New dependencies must use the short `apostille-me/apme-*` coordinates.

## Zed and Git submodules

Prefer Zed for reusable dependency resolution. A repository retained as a Git submodule must have an explicit editable-workspace, inventory, embedded-source, experiment-reference, or legacy role. Do not represent the same repository as both a Zed dependency and a gitlink in one composition.

A root `.zpkg.toml` allows `zed overtake --git-submodules` to adopt an exact gitlink while preserving `.gitmodules`. Edge code is allowlisted and never a generic proxy.
