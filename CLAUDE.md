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

## Never commit

- `.env` files or files containing API keys
- Audio files or binary outputs
- Files in `sources/` or `temp/` (these are transient)
