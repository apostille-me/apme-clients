# Apostille Me client matrix

This repository publishes one Zed package with isolated language targets. Every
client shares versioned `apme-interfaces` contracts and reusable `apme-libs`
behavior.

Required slices are Gleam, Erlang, Elixir, Dart, Rust, Java, Go, Python 3, Ruby,
PHP, and TypeScript for Node.js, Deno, Bun, and edge runtimes. Kotlin and Swift
are intentionally not advertised until the organization has a mobile application
surface.

Run `python3 scripts/validate-client-matrix.py` before publishing.
