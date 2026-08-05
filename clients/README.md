# Apostille Me client matrix

Every SDK exposes the same service surface: `health`, `ready`, `config`, `emitEvent`, `createLead`, `createAlert`, and a generic authenticated request primitive. Wire contracts and reusable domain behavior come from the sibling `apme-interfaces` and `apme-libs` Zed packages.

The TypeScript SDK uses a fetch-compatible core with explicit Node.js, Deno, Bun, and edge-runtime entry points. Kotlin and Swift are first-class because Apostille Me workflows include mobile document capture and status tracking.

`matrix.json` is the machine-readable source of truth. `scripts/verify-client-matrix.mjs` rejects missing package roots, missing TypeScript runtime exports, or missing Zed dependency edges.
