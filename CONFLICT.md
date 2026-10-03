# apostille-me/apme-clients#14 — chore: nightly polyglot client hardening

head: automation/nightly-client-hardening  base: main  author: ORESoftware  updated: 2026-08-28T22:27:16Z
dir: /Users/maca5/codes/.claude-fleet/scratch/merge/apostille-me_apme-clients__14

## conflicted files
- clients/.api-surface.sha256
- clients/api-surface.json
- clients/c/.zed-api-surface.sha256
- clients/c/.zed-client-contract.json
- clients/client-api.schema.json
- clients/contract-manifest.json
- clients/cpp/.zed-api-surface.sha256
- clients/cpp/.zed-client-contract.json
- clients/dart/.zed-api-surface.sha256
- clients/dart/.zed-client-contract.json
- clients/elixir/.zed-api-surface.sha256
- clients/elixir/.zed-client-contract.json
- clients/erlang/.zed-api-surface.sha256
- clients/erlang/.zed-client-contract.json
- clients/gleam/.zed-api-surface.sha256
- clients/gleam/.zed-client-contract.json
- clients/golang/.zed-api-surface.sha256
- clients/golang/.zed-client-contract.json
- clients/java/.zed-api-surface.sha256
- clients/java/.zed-client-contract.json
- clients/kotlin/.zed-api-surface.sha256
- clients/kotlin/.zed-client-contract.json
- clients/php/.zed-api-surface.sha256
- clients/php/.zed-client-contract.json
- clients/python/.zed-api-surface.sha256
- clients/python/.zed-client-contract.json
- clients/ruby/.zed-api-surface.sha256
- clients/ruby/.zed-client-contract.json
- clients/rust/.zed-api-surface.sha256
- clients/rust/.zed-client-contract.json
- clients/swift/.zed-api-surface.sha256
- clients/swift/.zed-client-contract.json
- clients/typescript/.zed-contracts/nodejs/.zed-api-surface.sha256
- clients/typescript/.zed-contracts/nodejs/.zed-client-contract.json
- clients/typescript/bun/.zed-api-surface.sha256
- clients/typescript/bun/.zed-client-contract.json
- clients/typescript/deno/.zed-api-surface.sha256
- clients/typescript/deno/.zed-client-contract.json
- clients/typescript/edge/.zed-api-surface.sha256
- clients/typescript/edge/.zed-client-contract.json
- clients/wasm/.zed-api-surface.sha256
- clients/wasm/.zed-client-contract.json
- clients/zig/.zed-api-surface.sha256
- clients/zig/.zed-client-contract.json

## base (main) last 8 commits
9888e24 DEN-3573 Adopt the canonical JSON Schema client contract.
259b29a Merge branch 'agent-sync/20260823/main' into main
fa5fe0e ci: add pre-build JS and Rust source lint
7b7212a ci: add pre-build JS and Rust source lint
d585003 ci: add pre-build JS and Rust source lint
b30abfe chore: ignore tmp/temp worktree scratch directories
f956faf Merge remote:agent/full-polyglot-client-matrix into main with semantic hunk reconciliation
20442b0 Merge remote:agent/polyglot-client-matrix-20260805 into main with semantic hunk reconciliation

## head (automation/nightly-client-hardening) last 8 commits
34a1859 feat: harden canonical polyglot client contract
f956faf Merge remote:agent/full-polyglot-client-matrix into main with semantic hunk reconciliation
20442b0 Merge remote:agent/polyglot-client-matrix-20260805 into main with semantic hunk reconciliation
f6927d0 Merge remote:agent/zed-dependency-graph into main with canonical policy reconciliation
453762d Merge remote:agent/standardize-zed-client-matrix-20260805 into main
3a27a6c chore: ignore generated client build caches
d14fcb9 Prefer primary branches and avoid agent worktrees
56e7b17 fix: align package contract with native Zed targets

## merge-base: f956faf72985b88d1e443c35f86c9a8cb8d144f6

## PR diff stat (merge-base..head)
 clients/golang/.zed-api-surface.sha256             |   1 +
 clients/golang/.zed-client-contract.json           |  10 +
 clients/java/.zed-api-surface.sha256               |   1 +
 clients/java/.zed-client-contract.json             |  10 +
 clients/kotlin/.zed-api-surface.sha256             |   1 +
 clients/kotlin/.zed-client-contract.json           |  10 +
 clients/php/.zed-api-surface.sha256                |   1 +
 clients/php/.zed-client-contract.json              |  10 +
 clients/python/.zed-api-surface.sha256             |   1 +
 clients/python/.zed-client-contract.json           |  10 +
 clients/ruby/.zed-api-surface.sha256               |   1 +
 clients/ruby/.zed-client-contract.json             |  10 +
 clients/rust/.zed-api-surface.sha256               |   1 +
 clients/rust/.zed-client-contract.json             |  10 +
 clients/sdk-matrix.json                            | 109 ++++
 clients/swift/.zed-api-surface.sha256              |   1 +
 clients/swift/.zed-client-contract.json            |  10 +
 .../.zed-contracts/nodejs/.zed-api-surface.sha256  |   1 +
 .../nodejs/.zed-client-contract.json               |  10 +
 clients/typescript/bun/.zed-api-surface.sha256     |   1 +
 clients/typescript/bun/.zed-client-contract.json   |  10 +
 clients/typescript/deno/.zed-api-surface.sha256    |   1 +
 clients/typescript/deno/.zed-client-contract.json  |  10 +
 clients/typescript/edge/.zed-api-surface.sha256    |   1 +
 clients/typescript/edge/.zed-client-contract.json  |  10 +
 clients/wasm/.zed-api-surface.sha256               |   1 +
 clients/wasm/.zed-client-contract.json             |  10 +
 clients/zig/.zed-api-surface.sha256                |   1 +
 clients/zig/.zed-client-contract.json              |  10 +
 47 files changed, 1719 insertions(+), 30 deletions(-)

## base diff stat (merge-base..base)
 clients/php/.zed-api-surface.sha256                |    1 +
 clients/php/.zed-client-contract.json              |   10 +
 clients/python/.zed-api-surface.sha256             |    1 +
 clients/python/.zed-client-contract.json           |   10 +
 clients/python3/.zed-api-surface.sha256            |    1 +
 clients/python3/.zed-client-contract.json          |   10 +
 clients/ruby/.zed-api-surface.sha256               |    1 +
 clients/ruby/.zed-client-contract.json             |   10 +
 clients/rust/.zed-api-surface.sha256               |    1 +
 clients/rust/.zed-client-contract.json             |   10 +
 clients/swift/.zed-api-surface.sha256              |    1 +
 clients/swift/.zed-client-contract.json            |   10 +
 .../.zed-contracts/nodejs/.zed-api-surface.sha256  |    1 +
 .../nodejs/.zed-client-contract.json               |   10 +
 clients/typescript/bun/.zed-api-surface.sha256     |    1 +
 clients/typescript/bun/.zed-client-contract.json   |   10 +
 clients/typescript/deno/.zed-api-surface.sha256    |    1 +
 clients/typescript/deno/.zed-client-contract.json  |   10 +
 clients/typescript/edge/.zed-api-surface.sha256    |    1 +
 clients/typescript/edge/.zed-client-contract.json  |   10 +
 clients/wasm/.zed-api-surface.sha256               |    1 +
 clients/wasm/.zed-client-contract.json             |   10 +
 clients/zig/.zed-api-surface.sha256                |    1 +
 clients/zig/.zed-client-contract.json              |   10 +
 schemas/client-api.schema.json                     |  718 +++++++++
 scripts/client_contract_boundary.py                |  123 ++
 scripts/harden_client_contract.py                  | 1573 ++++++++++++++++++++
 scripts/verify_client_contract.py                  |  279 ++++
 tests/test_client_contract_boundary.py             |   50 +
 58 files changed, 4687 insertions(+)

## merge output
Auto-merging clients/.api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/.api-surface.sha256
Auto-merging clients/api-surface.json
CONFLICT (add/add): Merge conflict in clients/api-surface.json
Auto-merging clients/c/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/c/.zed-api-surface.sha256
Auto-merging clients/c/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/c/.zed-client-contract.json
Auto-merging clients/client-api.schema.json
CONFLICT (add/add): Merge conflict in clients/client-api.schema.json
Auto-merging clients/contract-manifest.json
CONFLICT (add/add): Merge conflict in clients/contract-manifest.json
Auto-merging clients/cpp/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/cpp/.zed-api-surface.sha256
Auto-merging clients/cpp/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/cpp/.zed-client-contract.json
Auto-merging clients/dart/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/dart/.zed-api-surface.sha256
Auto-merging clients/dart/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/dart/.zed-client-contract.json
Auto-merging clients/elixir/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/elixir/.zed-api-surface.sha256
Auto-merging clients/elixir/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/elixir/.zed-client-contract.json
Auto-merging clients/erlang/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/erlang/.zed-api-surface.sha256
Auto-merging clients/erlang/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/erlang/.zed-client-contract.json
Auto-merging clients/gleam/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/gleam/.zed-api-surface.sha256
Auto-merging clients/gleam/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/gleam/.zed-client-contract.json
Auto-merging clients/golang/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/golang/.zed-api-surface.sha256
Auto-merging clients/golang/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/golang/.zed-client-contract.json
Auto-merging clients/java/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/java/.zed-api-surface.sha256
Auto-merging clients/java/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/java/.zed-client-contract.json
Auto-merging clients/kotlin/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/kotlin/.zed-api-surface.sha256
Auto-merging clients/kotlin/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/kotlin/.zed-client-contract.json
Auto-merging clients/php/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/php/.zed-api-surface.sha256
Auto-merging clients/php/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/php/.zed-client-contract.json
Auto-merging clients/python/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/python/.zed-api-surface.sha256
Auto-merging clients/python/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/python/.zed-client-contract.json
Auto-merging clients/ruby/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/ruby/.zed-api-surface.sha256
Auto-merging clients/ruby/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/ruby/.zed-client-contract.json
Auto-merging clients/rust/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/rust/.zed-api-surface.sha256
Auto-merging clients/rust/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/rust/.zed-client-contract.json
Auto-merging clients/swift/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/swift/.zed-api-surface.sha256
Auto-merging clients/swift/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/swift/.zed-client-contract.json
Auto-merging clients/typescript/.zed-contracts/nodejs/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/typescript/.zed-contracts/nodejs/.zed-api-surface.sha256
Auto-merging clients/typescript/.zed-contracts/nodejs/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/typescript/.zed-contracts/nodejs/.zed-client-contract.json
Auto-merging clients/typescript/bun/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/typescript/bun/.zed-api-surface.sha256
Auto-merging clients/typescript/bun/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/typescript/bun/.zed-client-contract.json
Auto-merging clients/typescript/deno/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/typescript/deno/.zed-api-surface.sha256
Auto-merging clients/typescript/deno/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/typescript/deno/.zed-client-contract.json
Auto-merging clients/typescript/edge/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/typescript/edge/.zed-api-surface.sha256
Auto-merging clients/typescript/edge/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/typescript/edge/.zed-client-contract.json
Auto-merging clients/wasm/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/wasm/.zed-api-surface.sha256
Auto-merging clients/wasm/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/wasm/.zed-client-contract.json
Auto-merging clients/zig/.zed-api-surface.sha256
CONFLICT (add/add): Merge conflict in clients/zig/.zed-api-surface.sha256
Auto-merging clients/zig/.zed-client-contract.json
CONFLICT (add/add): Merge conflict in clients/zig/.zed-client-contract.json
Automatic merge failed; fix conflicts and then commit the result.
