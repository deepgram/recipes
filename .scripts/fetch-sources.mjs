#!/usr/bin/env node

/**
 * Zero-dependency Node v22 script to fetch sources defined in .deepgram/sources.json
 * - Clones repos into temp/
 * - Copies specified paths into sources/<name>/
 * - Uses only built-in modules
 */

import { spawn } from "node:child_process";
import { mkdirSync, readFileSync, rmSync, cpSync, existsSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

function log(msg) {
  process.stdout.write(`[fetch-sources] ${msg}\n`);
}

function run(cmd, args, opts = {}) {
  return new Promise((resolvePromise, reject) => {
    const child = spawn(cmd, args, { stdio: "inherit", ...opts });
    child.on("exit", (code) => {
      if (code === 0) return resolvePromise();
      reject(new Error(`${cmd} ${args.join(" ")} exited with code ${code}`));
    });
    child.on("error", reject);
  });
}

function sanitizeDirName(name) {
  return name.replace(/[^a-z0-9\-_. ]/gi, "-").replace(/\s+/g, "-");
}

async function ensureRepoCloned(tempDir, repoFull) {
  const [owner, repo] = repoFull.split("/");
  if (!owner || !repo) throw new Error(`Invalid repo format: ${repoFull}`);
  const repoDir = join(tempDir, `${owner}__${repo}`);
  if (!existsSync(repoDir)) {
    log(`Cloning ${repoFull}...`);
    await run("git", ["clone", `https://github.com/${repoFull}.git`, repoDir]);
  } else {
    log(`Pulling latest for ${repoFull}...`);
    await run("git", ["-C", repoDir, "pull", "--ff-only"]);
  }
  return repoDir;
}

function copyPath(srcPath, destPath) {
  // Remove destination if exists to ensure clean copy
  if (existsSync(destPath)) {
    rmSync(destPath, { recursive: true, force: true });
  }
  cpSync(srcPath, destPath, { recursive: true, force: true });
}

async function main() {
  const repoRoot = resolve(join(__dirname, ".."));
  const sourcesConfigPath = resolve(
    join(repoRoot, ".deepgram", "sources.json")
  );
  const tempDir = resolve(join(repoRoot, "temp"));
  const outDir = resolve(join(repoRoot, "sources"));

  // Ensure base dirs
  mkdirSync(tempDir, { recursive: true });
  mkdirSync(outDir, { recursive: true });

  let config;
  try {
    const json = readFileSync(sourcesConfigPath, "utf8");
    config = JSON.parse(json);
  } catch (err) {
    throw new Error(`Failed to read ${sourcesConfigPath}: ${err.message}`);
  }

  if (!config || !Array.isArray(config.sources)) {
    throw new Error('Invalid config: expected { "sources": [ ... ] }');
  }

  // Prepare distinct list of repos before any cloning
  const uniqueRepos = Array.from(
    new Set(
      config.sources
        .map((e) => e.repo?.trim())
        .filter((v) => typeof v === "string" && v.length > 0)
    )
  );

  log(`Discovered ${uniqueRepos.length} distinct repos.`);

  // Clone/pull each repo once
  const repoDirByRepo = new Map();
  for (const repo of uniqueRepos) {
    try {
      const dir = await ensureRepoCloned(tempDir, repo);
      repoDirByRepo.set(repo, dir);
    } catch (e) {
      process.stderr.write(
        `[fetch-sources] Failed to prepare repo '${repo}': ${e.message}\n`
      );
      // Intentionally continue; copy step will skip entries for missing repos
      continue;
    }
  }

  // Copy pass
  for (const entry of config.sources) {
    const name = entry.name?.trim();
    const repo = entry.repo?.trim();
    const pathInRepo = entry.path?.trim();
    if (!name || !repo || !pathInRepo) {
      log(`Skipping invalid entry: ${JSON.stringify(entry)}`);
      continue;
    }

    try {
      const repoDir = repoDirByRepo.get(repo);
      if (!repoDir) {
        process.stderr.write(
          `[fetch-sources] Skipping '${name}' because repo not prepared: ${repo}\n`
        );
        continue;
      }

      const safeName = sanitizeDirName(name);
      const destDir = join(outDir, safeName);
      mkdirSync(destDir, { recursive: true });

      const normalizedRepoPath = pathInRepo.replace(/^\/+/, "");
      const srcAbsolute = resolve(join(repoDir, normalizedRepoPath));
      const entryBaseName =
        normalizedRepoPath.split("/").filter(Boolean).pop() || "content";
      const destAbsolute = resolve(join(destDir, entryBaseName));

      if (!existsSync(srcAbsolute)) {
        log(`Path not found in repo ${repo}: ${pathInRepo}`);
        continue;
      }

      log(
        `Copying ${repo}:${pathInRepo} -> ${join(
          "sources",
          safeName,
          entryBaseName
        )}`
      );
      copyPath(srcAbsolute, destAbsolute);
    } catch (e) {
      process.stderr.write(
        `[fetch-sources] Skipping '${name}' due to error: ${e.message}\n`
      );
      continue;
    }
  }

  log("Done.");
}

main().catch((err) => {
  process.stderr.write(`[fetch-sources] Error: ${err.message}\n`);
  process.exit(1);
});
