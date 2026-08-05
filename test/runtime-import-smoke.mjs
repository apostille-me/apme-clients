import assert from "node:assert/strict";

const runtime = globalThis.Deno ? "deno" : globalThis.Bun ? "bun" : "node";
const candidatesByRuntime = {
  node: [
    "../clients/typescript/dist/nodejs/index.js",
    "../clients/typescript/dist/src/index.js",
  ],
  deno: [
    "../clients/typescript/dist/deno/mod.js",
    "../clients/typescript/dist/src/index.js",
  ],
  bun: [
    "../clients/typescript/dist/bun/index.js",
    "../clients/typescript/dist/src/index.js",
  ],
};

let sdk;
let lastError;
for (const candidate of candidatesByRuntime[runtime]) {
  try {
    sdk = await import(new URL(candidate, import.meta.url));
    break;
  } catch (error) {
    lastError = error;
  }
}

assert.ok(sdk, `could not import the built TypeScript client in ${runtime}: ${lastError}`);
assert.ok(Object.keys(sdk).length > 0, "client module must export a public API");
for (const globalName of ["fetch", "Headers", "Request", "Response"]) {
  assert.equal(typeof globalThis[globalName], "function", `${runtime} must expose ${globalName}`);
}
console.log(`${runtime} client import smoke passed with ${Object.keys(sdk).length} exports`);
