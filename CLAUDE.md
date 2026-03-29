# dx-recipes: Claude Code Instructions

## What this repository is

A recipes collection of small, runnable code examples for Deepgram SDKs. Each recipe demonstrates one specific feature or operation with actual working code, a test, and a README.

## Sample directory structure

```
samples/{language}/{product}/{api-version}/{recipe-slug}/
  example.{ext}          # Runnable example (< 50 lines)
  example_test.{ext}     # Test that runs the example
  README.md              # Feature explanation with params and output
```

**Languages:** python, javascript, go, dotnet, java, rust, cli
**Products:** speech-to-text, text-to-speech, audio-intelligence, voice-agents
**Versions:** v1 (most products), v2 (STT only — flux-general-en English model)

## Recipe standards

Every example MUST:
- Read `DEEPGRAM_API_KEY` from environment (never hardcode)
- Print meaningful output (transcript, audio size, JSON field value — not just "done")
- Be < 50 lines
- Be fully runnable: `{run_command} example.{ext}`
- Use demo audio: `https://dpgr.am/spacewalk.wav`

Every test MUST:
- Actually run the example as a subprocess
- Verify exit code is 0
- Verify stdout is non-empty

Every README MUST:
- Explain what the feature does (not just "this example shows X")
- List the key parameters that enable the feature
- Show what the output looks like with the feature enabled
- Include prerequisites and run instructions

## Autonomous operation

This repository is managed by GitHub Actions workflows:
- `discover-sdks.yml`: Runs hourly, checks for coverage gaps, creates queue issues
- `process-queue.yml`: Runs hourly, picks up queue issues and generates examples
- `test-{language}.yml`: Runs on PR + daily, executes all examples against real API
- `update-coverage.yml`: Runs on PR merge, updates COVERAGE.md
- `reconcile-index.yml`: Runs daily, ensures README is accurate

All autonomous logic lives in `instructions/*.md` — read these before modifying behavior.

## Conventional commits

Follow conventional commits: `feat(python): add speech-to-text v1 paragraphs recipe`

Types: feat, fix, docs, style, refactor, test, chore

Never add Co-Authored-By lines for Claude Code.

## Workflow trigger design rule

GitHub blocks event propagation between workflows when using `GITHUB_TOKEN`:
a workflow-created issue does not fire `on: issues`, and a workflow-merged PR
does not fire `on: pull_request.closed`. This breaks any `workflow1 → workflow2`
event chain where workflow1 is autonomous.

**Rule:** every downstream workflow that should run after an agent action MUST have
a cron fallback. The cron is the safety net that picks up work the event trigger missed.

Current design:
- `process-queue` — cron at :27 catches issues created by `discover-sdks` (workflow-created
  issues don't fire `on: issues`)
- `update-coverage` — cron every 6h catches PRs merged by `process-queue` (workflow-merged
  PRs don't fire `on: pull_request.closed`)
- `reconcile-index` — cron-only by design; daily safety net for any drift

If you add a new downstream workflow, give it a cron. Never rely on event triggers alone
when the upstream action may be performed by an autonomous workflow.

## Never touch .github/workflows/

Agents running inside GitHub Actions CANNOT create or modify files in `.github/workflows/`:
- `GITHUB_TOKEN` does not have the `workflows` scope
- Even if bypassed, workflow file changes do not trigger CI until after they are merged
- New test workflows for new SDKs must be added manually by a human in a separate PR

When onboarding a new SDK, create the `samples/{language}/` directory and `sdks.json` entry,
then note in the queue issue that a human needs to add the test workflow.

## Never commit

- `.env` files or files containing API keys
- Audio files or binary outputs
- Files in `sources/` or `temp/` (these are transient)
