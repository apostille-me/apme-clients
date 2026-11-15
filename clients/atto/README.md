# Experimental AttoLang request-plan SDK

This `.atto` baseline mirrors the transport-neutral HTTP route/method contract
from `clients/rust/src/lib.rs`: health, config, events, and alerts.
It is **not** an HTTP transport, JWT store, or a published SDK.
Callers must provide their own authorized transport and keep credentials out of logs.

The `main()` function is a positive compiler/guest-runtime conformance fixture;
its expected exit code is 42. The Rust test
`cargo test --manifest-path clients/rust/Cargo.toml --all-targets` checks
source-level route parity, **not** actual Atto compilation or WebAssembly execution.
Only mark Atto runtime support verified after running this source against a
pinned AttoLang compiler and executing the emitted guest artifact.

The canonical wire contracts remain in `apostille-me/apme-interfaces`.
