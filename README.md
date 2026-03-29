# recipes

Agent-maintained recipes showing how to use every Deepgram SDK feature across every supported language.

**All recipes are built and kept current by autonomous agents.** Humans can direct, override, and add recipes at any time.

[→ Contributing](CONTRIBUTING.md) · [→ Open PRs](../../pulls) · [→ Coverage matrix](COVERAGE.md) · [→ Request a recipe](../../issues/new/choose)

## How it works

1. **Discover** — Hourly: agents scan SDK repos for new releases and compare against `recipes/` to find coverage gaps, creating queue issues for missing recipes
2. **Generate** — Agents pick up queue issues, fetch current SDK docs via Kapa, and write runnable `example.*` + `example_test.*` + `README.md` for each missing recipe, raising a PR
3. **Test** — Language-specific CI workflows run every example against the real Deepgram API
4. **Merge** — PRs merge once tests pass
5. **Update** — Coverage matrix rebuilds automatically on merge
6. **Review** — Weekly: agents check SDK release notes for new features and API changes, updating `features.json` and queuing fixes for stale recipes

## Recipe structure

```
recipes/{language}/{product}/{version}/{recipe}/
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

## Recipes

<!-- recipes-table-start -->
*82 recipes · last updated 2026-03-29 18:55 UTC*

| Recipe | Language | Product | Version | Files | Tests |
|--------|----------|---------|---------|-------|-------|
| [entities](recipes/javascript/audio-intelligence/v1/entities/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [entities](recipes/javascript/audio-intelligence/v1/entities/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [intents](recipes/javascript/audio-intelligence/v1/intents/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [intents](recipes/javascript/audio-intelligence/v1/intents/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [sentiment](recipes/javascript/audio-intelligence/v1/sentiment/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [sentiment](recipes/javascript/audio-intelligence/v1/sentiment/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [summarize](recipes/javascript/audio-intelligence/v1/summarize/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [summarize](recipes/javascript/audio-intelligence/v1/summarize/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [topics](recipes/javascript/audio-intelligence/v1/topics/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [topics](recipes/javascript/audio-intelligence/v1/topics/) | JavaScript | audio-intelligence | v1 | ❌ ✅ | — no run |
| [detect-entities](recipes/javascript/speech-to-text/v1/detect-entities/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [detect-entities](recipes/javascript/speech-to-text/v1/detect-entities/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [detect-language](recipes/javascript/speech-to-text/v1/detect-language/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [detect-language](recipes/javascript/speech-to-text/v1/detect-language/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [diarize](recipes/javascript/speech-to-text/v1/diarize/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [diarize](recipes/javascript/speech-to-text/v1/diarize/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [intents](recipes/javascript/speech-to-text/v1/intents/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [intents](recipes/javascript/speech-to-text/v1/intents/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [keywords](recipes/javascript/speech-to-text/v1/keywords/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [keywords](recipes/javascript/speech-to-text/v1/keywords/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [multichannel](recipes/javascript/speech-to-text/v1/multichannel/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [multichannel](recipes/javascript/speech-to-text/v1/multichannel/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [paragraphs](recipes/javascript/speech-to-text/v1/paragraphs/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [paragraphs](recipes/javascript/speech-to-text/v1/paragraphs/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [punctuate](recipes/javascript/speech-to-text/v1/punctuate/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [punctuate](recipes/javascript/speech-to-text/v1/punctuate/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [redact](recipes/javascript/speech-to-text/v1/redact/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [redact](recipes/javascript/speech-to-text/v1/redact/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [search](recipes/javascript/speech-to-text/v1/search/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [search](recipes/javascript/speech-to-text/v1/search/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [sentiment](recipes/javascript/speech-to-text/v1/sentiment/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [sentiment](recipes/javascript/speech-to-text/v1/sentiment/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [smart-format](recipes/javascript/speech-to-text/v1/smart-format/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [smart-format](recipes/javascript/speech-to-text/v1/smart-format/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [streaming-file](recipes/javascript/speech-to-text/v1/streaming-file/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [streaming-file](recipes/javascript/speech-to-text/v1/streaming-file/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [streaming](recipes/javascript/speech-to-text/v1/streaming/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [streaming](recipes/javascript/speech-to-text/v1/streaming/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [summarize](recipes/javascript/speech-to-text/v1/summarize/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [summarize](recipes/javascript/speech-to-text/v1/summarize/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [topics](recipes/javascript/speech-to-text/v1/topics/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [topics](recipes/javascript/speech-to-text/v1/topics/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [transcribe-file](recipes/javascript/speech-to-text/v1/transcribe-file/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [transcribe-file](recipes/javascript/speech-to-text/v1/transcribe-file/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [transcribe-url](recipes/javascript/speech-to-text/v1/transcribe-url/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [transcribe-url](recipes/javascript/speech-to-text/v1/transcribe-url/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [utterances](recipes/javascript/speech-to-text/v1/utterances/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [utterances](recipes/javascript/speech-to-text/v1/utterances/) | JavaScript | speech-to-text | v1 | ❌ ✅ | — no run |
| [streaming](recipes/javascript/speech-to-text/v2/streaming/) | JavaScript | speech-to-text | v2 | ❌ ✅ | — no run |
| [streaming](recipes/javascript/speech-to-text/v2/streaming/) | JavaScript | speech-to-text | v2 | ❌ ✅ | — no run |
| [transcribe-url](recipes/javascript/speech-to-text/v2/transcribe-url/) | JavaScript | speech-to-text | v2 | ❌ ✅ | — no run |
| [transcribe-url](recipes/javascript/speech-to-text/v2/transcribe-url/) | JavaScript | speech-to-text | v2 | ❌ ✅ | — no run |
| [generate-audio](recipes/javascript/text-to-speech/v1/generate-audio/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [generate-audio](recipes/javascript/text-to-speech/v1/generate-audio/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [select-encoding](recipes/javascript/text-to-speech/v1/select-encoding/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [select-encoding](recipes/javascript/text-to-speech/v1/select-encoding/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [select-model](recipes/javascript/text-to-speech/v1/select-model/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [select-model](recipes/javascript/text-to-speech/v1/select-model/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [stream-audio](recipes/javascript/text-to-speech/v1/stream-audio/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [stream-audio](recipes/javascript/text-to-speech/v1/stream-audio/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [websocket-streaming](recipes/javascript/text-to-speech/v1/websocket-streaming/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [websocket-streaming](recipes/javascript/text-to-speech/v1/websocket-streaming/) | JavaScript | text-to-speech | v1 | ❌ ✅ | — no run |
| [connect](recipes/javascript/voice-agents/v1/connect/) | JavaScript | voice-agents | v1 | ❌ ✅ | — no run |
| [connect](recipes/javascript/voice-agents/v1/connect/) | JavaScript | voice-agents | v1 | ❌ ✅ | — no run |
| [custom-llm](recipes/javascript/voice-agents/v1/custom-llm/) | JavaScript | voice-agents | v1 | ❌ ✅ | — no run |
| [custom-llm](recipes/javascript/voice-agents/v1/custom-llm/) | JavaScript | voice-agents | v1 | ❌ ✅ | — no run |
| [custom-tts](recipes/javascript/voice-agents/v1/custom-tts/) | JavaScript | voice-agents | v1 | ❌ ✅ | — no run |
| [custom-tts](recipes/javascript/voice-agents/v1/custom-tts/) | JavaScript | voice-agents | v1 | ❌ ✅ | — no run |
| [function-calling](recipes/javascript/voice-agents/v1/function-calling/) | JavaScript | voice-agents | v1 | ❌ ✅ | — no run |
| [function-calling](recipes/javascript/voice-agents/v1/function-calling/) | JavaScript | voice-agents | v1 | ❌ ✅ | — no run |
| [detect-language](recipes/python/speech-to-text/v1/detect-language/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [diarize](recipes/python/speech-to-text/v1/diarize/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [intents](recipes/python/speech-to-text/v1/intents/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [paragraphs](recipes/python/speech-to-text/v1/paragraphs/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [punctuate](recipes/python/speech-to-text/v1/punctuate/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [sentiment](recipes/python/speech-to-text/v1/sentiment/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [smart-format](recipes/python/speech-to-text/v1/smart-format/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [summarize](recipes/python/speech-to-text/v1/summarize/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [topics](recipes/python/speech-to-text/v1/topics/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [transcribe-url](recipes/python/speech-to-text/v1/transcribe-url/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [utterances](recipes/python/speech-to-text/v1/utterances/) | Python | speech-to-text | v1 | ✅ ✅ | — no run |
| [generate-audio](recipes/python/text-to-speech/v1/generate-audio/) | Python | text-to-speech | v1 | ✅ ✅ | — no run |

<!-- recipes-table-end -->

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
7. Set **branch protection** on `main`: require status checks → add **`E2E / test`** as the required check — this runs on every PR, makes real API calls, and is the gate for auto-merge. The per-language `test-*` workflows also run when their files change but are not required (they fail-fast and block human review if broken)

`GITHUB_TOKEN` is provided automatically by GitHub Actions.

## Running agents locally

```bash
# Requires: ANTHROPIC_API_KEY set, DEEPGRAM_API_KEY set, gh auth login, git configured
claude --model claude-opus-4-6 -p "$(cat instructions/discover-sdks.md)"
claude --model claude-opus-4-6 -p "$(cat instructions/process-queue.md)"
```

See [instructions/README.md](instructions/README.md) for all available instructions.
