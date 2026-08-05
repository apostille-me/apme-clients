# TypeScript runtimes

The TypeScript SDK is intentionally split by runtime so packaging and compatibility
claims remain honest:

- `nodejs`: Node.js 18+ and package-manager consumers.
- `deno`: native Deno module metadata.
- `bun`: Bun-native package metadata.
- `edge`: Web Fetch API only; no Node.js built-ins.

All four expose the same `ApostilleMeClient` surface.
