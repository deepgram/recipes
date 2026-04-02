import { describe, it } from "node:test";
import { ok } from "node:assert";
import { execSync } from "node:child_process";
import { dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));

describe("profanity-filter", () => {
  it("runs without error and produces output", () => {
    const output = execSync("node example.js", {
      cwd: __dirname,
      timeout: 60000,
      env: process.env,
      encoding: "utf8",
    });
    ok(output.trim().length > 0, "Expected non-empty output");
  });
});
