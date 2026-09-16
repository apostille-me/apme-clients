#!/usr/bin/env sh
# Fail-closed pre-publish gate for the canonical polyglot client contract.
#
# The contract authority is clients/api-surface.json validated by
# clients/client-api.schema.json and bound to apostille-me/apme-interfaces.
# This wrapper intentionally does not introduce a second surface declaration.
set -eu

root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$root"

python3 - <<'PY'
import importlib.util
import sys
if importlib.util.find_spec("jsonschema") is None:
    print("prepublish: pinned jsonschema dependency is required; run the repository contract bootstrap first", file=sys.stderr)
    raise SystemExit(2)
PY

exec python3 scripts/verify_client_contract.py
