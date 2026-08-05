import assert from "node:assert/strict";
import {spawn} from "node:child_process";
import {fileURLToPath} from "node:url";

const port = 8793;
const root = new URL("../", import.meta.url);
const isWindows = process.platform === "win32";
const detached = !isWindows;
const wrangler = new URL(
  `clients/typescript/node_modules/.bin/wrangler${isWindows ? ".cmd" : ""}`,
  root,
);
const child = spawn(
  fileURLToPath(wrangler),
  ["dev", "--config", "test/wrangler.toml", "--port", String(port), "--log-level", "error"],
  {
    cwd: fileURLToPath(root),
    stdio: ["ignore", "pipe", "pipe"],
    detached,
  },
);

let logs = "";
let spawnFailure;
child.stdout.on("data", (chunk) => { logs += chunk; });
child.stderr.on("data", (chunk) => { logs += chunk; });
child.on("error", (error) => {
  spawnFailure = error;
  logs += `\nWrangler spawn failed: ${error.stack ?? error}`;
});

function signalChildGroup(signal) {
  if (child.exitCode !== null) return;
  try {
    if (detached && child.pid) process.kill(-child.pid, signal);
    else child.kill(signal);
  } catch (error) {
    if (error?.code !== "ESRCH") throw error;
  }
}

try {
  let response;
  for (let attempt = 0; attempt < 80; attempt += 1) {
    if (spawnFailure || child.exitCode !== null) break;
    try {
      response = await fetch(`http://127.0.0.1:${port}/`);
      if (response.ok) break;
    } catch {}
    await new Promise((resolve) => setTimeout(resolve, 250));
  }

  assert.equal(spawnFailure, undefined, logs);
  assert.ok(response, `Wrangler did not start\n${logs}`);
  assert.equal(response.status, 200, logs);
  const result = await response.json();
  assert.equal(result.ok, true, logs);
  assert.ok(Array.isArray(result.exports) && result.exports.length > 0, logs);
  console.log(`edge client import smoke passed with ${result.exports.length} exports`);
} finally {
  signalChildGroup("SIGTERM");
  await Promise.race([
    new Promise((resolve) => child.once("exit", resolve)),
    new Promise((resolve) => setTimeout(resolve, 3000)),
  ]);
  signalChildGroup("SIGKILL");
}
