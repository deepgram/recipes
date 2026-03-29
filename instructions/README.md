# Instructions

This directory contains self-contained agent prompts used by the autonomous recipe generation system.

Each file is a complete, standalone prompt that can be executed by an AI agent (Claude) either
automatically via a GitHub Actions workflow or manually from your local machine.

## Available Instructions

| File | Triggered By | What It Does |
|------|-------------|--------------|
| `discover-sdks.md` | Every hour at :07 | Scans `samples/` for coverage gaps and creates `queue:generate` issues for missing recipes. Also detects new Deepgram SDK repos not yet tracked. |
| `process-queue.md` | Every hour at :27, on issue events | Routes open `type:queue` issues. Executes `generate-examples.md` for `action:generate` issues; surfaces `action:new-sdk` issues for human review. |
| `generate-examples.md` | Triggered by queue issues | Generates runnable recipe files (`example.*`, `example_test.*`, `README.md`) for a language/product combination. Opens a PR and closes the queue issue. |
| `update-coverage.md` | On PR merge to main | Rebuilds `COVERAGE.md` and per-language/per-product README files to reflect the current state of `samples/`. |
| `reconcile-index.md` | Daily at 11:45 UTC | Verifies the root `README.md` count table is accurate. Creates `queue:fix` issues for sample directories missing required files. |

## How to Run Locally

Any instruction can be run locally using the Claude CLI:

```bash
claude --model claude-opus-4-6 -p "$(cat instructions/{name}.md)"
```

**Examples:**

```bash
# Check for coverage gaps and create queue issues
claude --model claude-opus-4-6 -p "$(cat instructions/discover-sdks.md)"

# Process the oldest pending queue issue
claude --model claude-opus-4-6 -p "$(cat instructions/process-queue.md)"

# Generate examples from a queue issue
claude --model claude-opus-4-6 -p "$(cat instructions/generate-examples.md)"

# Rebuild coverage documentation after merging samples
claude --model claude-opus-4-6 -p "$(cat instructions/update-coverage.md)"

# Reconcile the index and check for missing files
claude --model claude-opus-4-6 -p "$(cat instructions/reconcile-index.md)"
```

## Design Principles

- Instructions are idempotent — running the same instruction twice should not create duplicates.
- Instructions check existing state before taking action (no blind writes).
- Instructions never commit directly to `main`.
- Instructions skip failing items with a warning rather than aborting entirely.

## Cron-as-safety-net pattern

GitHub blocks event propagation between workflows when `GITHUB_TOKEN` is the actor.
A workflow-created issue does not fire `on: issues`. A workflow-merged PR does not
fire `on: pull_request.closed`. Any `autonomous-workflow → event → other-workflow`
chain is silently broken.

**Every downstream workflow has a cron fallback for this reason:**

```
discover-sdks (cron :07)
  └─ creates queue:generate issues
       └─ process-queue (cron :27) ← cron fires even when issues were created by a workflow
            └─ merges recipe PRs
                 └─ update-coverage (cron every 6h) ← cron fires even when PR was merged by workflow
```

`reconcile-index` (daily) is the final safety net — catches any drift the other workflows missed.

When adding new downstream workflows, always include a cron trigger.
