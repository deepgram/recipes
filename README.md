# recipes

Agent-maintained recipes showing how to use every Deepgram SDK feature across every supported language.

**All recipes are built and kept current by autonomous agents.** Humans can direct, override, and add recipes at any time.

[→ Contributing](CONTRIBUTING.md) · [→ Open PRs](../../pulls) · [→ Coverage matrix](COVERAGE.md) · [→ Request a recipe](../../issues/new/choose)

## How it works

1. **Discover** — Hourly: agents scan SDK repos for new releases and compare against `samples/` to find coverage gaps, creating queue issues for missing recipes
2. **Generate** — Agents pick up queue issues, fetch current SDK docs via Kapa, and write runnable `example.*` + `example_test.*` + `README.md` for each missing recipe, raising a PR
3. **Test** — Language-specific CI workflows run every example against the real Deepgram API
4. **Merge** — PRs merge once tests pass
5. **Update** — Coverage matrix rebuilds automatically on merge
6. **Review** — Weekly: agents check SDK release notes for new features and API changes, updating `features.json` and queuing fixes for stale recipes

## Recipe structure

```
samples/{language}/{product}/{version}/{recipe}/
  example.{ext}       # runnable, < 50 lines, reads DEEPGRAM_API_KEY from env
  example_test.{ext}  # runs the example as a subprocess, asserts output
  README.md           # what the feature does · params · sample output · how to run
```

## Languages

| Language | SDK | Install |
|----------|-----|---------|
| Python | [deepgram-python-sdk](https://github.com/deepgram/deepgram-python-sdk) | `pip install deepgram-sdk` |
| JavaScript | [deepgram-js-sdk](https://github.com/deepgram/deepgram-js-sdk) | `npm install @deepgram/sdk` |
| Go | [deepgram-go-sdk](https://github.com/deepgram/deepgram-go-sdk) | `go get github.com/deepgram/deepgram-go-sdk/v3` |
| .NET | [deepgram-dotnet-sdk](https://github.com/deepgram/deepgram-dotnet-sdk) | `dotnet add package Deepgram` |
| Java | [deepgram-java-sdk](https://github.com/deepgram/deepgram-java-sdk) | Maven: `com.deepgram.sdk` |
| Rust | [deepgram-rust-sdk](https://github.com/deepgram/deepgram-rust-sdk) | `deepgram = "0.6"` |
| CLI | [deepgram/cli](https://github.com/deepgram/cli) | `pip install deepctl` |

## Products

| Product | API versions | Example recipes |
|---------|-------------|-----------------|
| Speech-to-Text | v1 (nova-3, nova-2, nova, enhanced, base) · v2 (flux-general-en) | transcribe-url, transcribe-file, paragraphs, diarize, smart-format, utterances, summarize, sentiment, topics, intents, detect-entities, detect-language, redact, search, keywords, streaming, … |
| Text-to-Speech | v1 (aura-2 voices) | generate-audio, stream-audio, websocket-streaming, select-model, select-encoding |
| Audio Intelligence | v1 | summarize, sentiment, topics, intents, entities |
| Voice Agents | v1 | connect, custom-llm, custom-tts, function-calling |

## Agent schedules

| Workflow | Schedule | Purpose |
|----------|----------|---------|
| `discover-sdks` | Every hour at :07 | Find coverage gaps → create `queue:generate` issues |
| `process-queue` | Every hour at :27 | Pick up queue issues → generate recipes → open PRs |
| `review-sdk-changes` | Saturdays 08:17 UTC | Check SDK release notes for new features and API changes |
| `update-coverage` | On PR merge + every 6 h | Rebuild `COVERAGE.md` and per-language READMEs |
| `reconcile-index` | Daily 11:45 UTC | Verify README counts; flag incomplete recipe directories |

## Setup

1. Add `ANTHROPIC_API_KEY` as a repository secret
2. Add `DEEPGRAM_API_KEY` as a repository secret
3. Add `KAPA_API_KEY` as a repository secret (used by agents to query live Deepgram docs)
4. Set `KAPA_PROJECT_ID` as a repository variable: `1908afc6-c134-4c6f-a684-ed7d8ce91759`
5. Run **Actions → Setup Labels → Run workflow** once to create all issue labels
6. Enable **auto-merge**: Settings → General → Pull Requests → Allow auto-merge
7. Set **branch protection** on `main`: require status checks, add all 7 `test-*` workflows as required checks (GitHub only enforces a check when it actually runs, so PRs that touch only Python files will only gate on `test-python`)

`GITHUB_TOKEN` is provided automatically by GitHub Actions.

## Running agents locally

```bash
# Requires: ANTHROPIC_API_KEY set, DEEPGRAM_API_KEY set, gh auth login, git configured
claude --model claude-opus-4-6 -p "$(cat instructions/discover-sdks.md)"
claude --model claude-opus-4-6 -p "$(cat instructions/process-queue.md)"
```

See [instructions/README.md](instructions/README.md) for all available instructions.
