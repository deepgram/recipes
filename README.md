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
*152 recipes · last updated 2026-03-29 20:09 UTC*

| Recipe | Language | Product | Version | Files | Tests |
|--------|----------|---------|---------|-------|-------|
| [entities](recipes/dotnet/audio-intelligence/v1/entities/) | .NET | audio-intelligence | v1 | ✅ ✅ | — no run |
| [intents](recipes/dotnet/audio-intelligence/v1/intents/) | .NET | audio-intelligence | v1 | ✅ ✅ | — no run |
| [sentiment](recipes/dotnet/audio-intelligence/v1/sentiment/) | .NET | audio-intelligence | v1 | ✅ ✅ | — no run |
| [summarize](recipes/dotnet/audio-intelligence/v1/summarize/) | .NET | audio-intelligence | v1 | ✅ ✅ | — no run |
| [topics](recipes/dotnet/audio-intelligence/v1/topics/) | .NET | audio-intelligence | v1 | ✅ ✅ | — no run |
| [detect-entities](recipes/dotnet/speech-to-text/v1/detect-entities/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [detect-language](recipes/dotnet/speech-to-text/v1/detect-language/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [diarize](recipes/dotnet/speech-to-text/v1/diarize/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [intents](recipes/dotnet/speech-to-text/v1/intents/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [keywords](recipes/dotnet/speech-to-text/v1/keywords/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [multichannel](recipes/dotnet/speech-to-text/v1/multichannel/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [paragraphs](recipes/dotnet/speech-to-text/v1/paragraphs/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [punctuate](recipes/dotnet/speech-to-text/v1/punctuate/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [redact](recipes/dotnet/speech-to-text/v1/redact/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [search](recipes/dotnet/speech-to-text/v1/search/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [sentiment](recipes/dotnet/speech-to-text/v1/sentiment/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [smart-format](recipes/dotnet/speech-to-text/v1/smart-format/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [streaming](recipes/dotnet/speech-to-text/v1/streaming/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [streaming-file](recipes/dotnet/speech-to-text/v1/streaming-file/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [summarize](recipes/dotnet/speech-to-text/v1/summarize/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [topics](recipes/dotnet/speech-to-text/v1/topics/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [transcribe-file](recipes/dotnet/speech-to-text/v1/transcribe-file/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [transcribe-url](recipes/dotnet/speech-to-text/v1/transcribe-url/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [utterances](recipes/dotnet/speech-to-text/v1/utterances/) | .NET | speech-to-text | v1 | ✅ ✅ | — no run |
| [streaming](recipes/dotnet/speech-to-text/v2/streaming/) | .NET | speech-to-text | v2 | ✅ ✅ | — no run |
| [transcribe-url](recipes/dotnet/speech-to-text/v2/transcribe-url/) | .NET | speech-to-text | v2 | ✅ ✅ | — no run |
| [generate-audio](recipes/dotnet/text-to-speech/v1/generate-audio/) | .NET | text-to-speech | v1 | ✅ ✅ | — no run |
| [select-encoding](recipes/dotnet/text-to-speech/v1/select-encoding/) | .NET | text-to-speech | v1 | ✅ ✅ | — no run |
| [select-model](recipes/dotnet/text-to-speech/v1/select-model/) | .NET | text-to-speech | v1 | ✅ ✅ | — no run |
| [stream-audio](recipes/dotnet/text-to-speech/v1/stream-audio/) | .NET | text-to-speech | v1 | ✅ ✅ | — no run |
| [websocket-streaming](recipes/dotnet/text-to-speech/v1/websocket-streaming/) | .NET | text-to-speech | v1 | ✅ ✅ | — no run |
| [connect](recipes/dotnet/voice-agents/v1/connect/) | .NET | voice-agents | v1 | ✅ ✅ | — no run |
| [custom-llm](recipes/dotnet/voice-agents/v1/custom-llm/) | .NET | voice-agents | v1 | ✅ ✅ | — no run |
| [custom-tts](recipes/dotnet/voice-agents/v1/custom-tts/) | .NET | voice-agents | v1 | ✅ ✅ | — no run |
| [function-calling](recipes/dotnet/voice-agents/v1/function-calling/) | .NET | voice-agents | v1 | ✅ ✅ | — no run |
| [entities](recipes/go/audio-intelligence/v1/entities/) | Go | audio-intelligence | v1 | ✅ ✅ | — no run |
| [intents](recipes/go/audio-intelligence/v1/intents/) | Go | audio-intelligence | v1 | ✅ ✅ | — no run |
| [sentiment](recipes/go/audio-intelligence/v1/sentiment/) | Go | audio-intelligence | v1 | ✅ ✅ | — no run |
| [summarize](recipes/go/audio-intelligence/v1/summarize/) | Go | audio-intelligence | v1 | ✅ ✅ | — no run |
| [topics](recipes/go/audio-intelligence/v1/topics/) | Go | audio-intelligence | v1 | ✅ ✅ | — no run |
| [detect-entities](recipes/go/speech-to-text/v1/detect-entities/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [detect-language](recipes/go/speech-to-text/v1/detect-language/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [diarize](recipes/go/speech-to-text/v1/diarize/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [intents](recipes/go/speech-to-text/v1/intents/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [keywords](recipes/go/speech-to-text/v1/keywords/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [multichannel](recipes/go/speech-to-text/v1/multichannel/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [paragraphs](recipes/go/speech-to-text/v1/paragraphs/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [punctuate](recipes/go/speech-to-text/v1/punctuate/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [redact](recipes/go/speech-to-text/v1/redact/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [search](recipes/go/speech-to-text/v1/search/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [sentiment](recipes/go/speech-to-text/v1/sentiment/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [smart-format](recipes/go/speech-to-text/v1/smart-format/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [streaming](recipes/go/speech-to-text/v1/streaming/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [streaming-file](recipes/go/speech-to-text/v1/streaming-file/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [summarize](recipes/go/speech-to-text/v1/summarize/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [topics](recipes/go/speech-to-text/v1/topics/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [transcribe-file](recipes/go/speech-to-text/v1/transcribe-file/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [transcribe-url](recipes/go/speech-to-text/v1/transcribe-url/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [utterances](recipes/go/speech-to-text/v1/utterances/) | Go | speech-to-text | v1 | ✅ ✅ | — no run |
| [streaming](recipes/go/speech-to-text/v2/streaming/) | Go | speech-to-text | v2 | ✅ ✅ | — no run |
| [transcribe-url](recipes/go/speech-to-text/v2/transcribe-url/) | Go | speech-to-text | v2 | ✅ ✅ | — no run |
| [generate-audio](recipes/go/text-to-speech/v1/generate-audio/) | Go | text-to-speech | v1 | ✅ ✅ | — no run |
| [select-encoding](recipes/go/text-to-speech/v1/select-encoding/) | Go | text-to-speech | v1 | ✅ ✅ | — no run |
| [select-model](recipes/go/text-to-speech/v1/select-model/) | Go | text-to-speech | v1 | ✅ ✅ | — no run |
| [stream-audio](recipes/go/text-to-speech/v1/stream-audio/) | Go | text-to-speech | v1 | ✅ ✅ | — no run |
| [websocket-streaming](recipes/go/text-to-speech/v1/websocket-streaming/) | Go | text-to-speech | v1 | ✅ ✅ | — no run |
| [connect](recipes/go/voice-agents/v1/connect/) | Go | voice-agents | v1 | ✅ ✅ | — no run |
| [custom-llm](recipes/go/voice-agents/v1/custom-llm/) | Go | voice-agents | v1 | ✅ ✅ | — no run |
| [custom-tts](recipes/go/voice-agents/v1/custom-tts/) | Go | voice-agents | v1 | ✅ ✅ | — no run |
| [function-calling](recipes/go/voice-agents/v1/function-calling/) | Go | voice-agents | v1 | ✅ ✅ | — no run |
| [entities](recipes/java/audio-intelligence/v1/entities/) | Java | audio-intelligence | v1 | ❌ ✅ | — no run |
| [intents](recipes/java/audio-intelligence/v1/intents/) | Java | audio-intelligence | v1 | ❌ ✅ | — no run |
| [sentiment](recipes/java/audio-intelligence/v1/sentiment/) | Java | audio-intelligence | v1 | ❌ ✅ | — no run |
| [summarize](recipes/java/audio-intelligence/v1/summarize/) | Java | audio-intelligence | v1 | ❌ ✅ | — no run |
| [topics](recipes/java/audio-intelligence/v1/topics/) | Java | audio-intelligence | v1 | ❌ ✅ | — no run |
| [detect-entities](recipes/java/speech-to-text/v1/detect-entities/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [detect-language](recipes/java/speech-to-text/v1/detect-language/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [diarize](recipes/java/speech-to-text/v1/diarize/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [intents](recipes/java/speech-to-text/v1/intents/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [keywords](recipes/java/speech-to-text/v1/keywords/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [multichannel](recipes/java/speech-to-text/v1/multichannel/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [paragraphs](recipes/java/speech-to-text/v1/paragraphs/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [punctuate](recipes/java/speech-to-text/v1/punctuate/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [redact](recipes/java/speech-to-text/v1/redact/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [search](recipes/java/speech-to-text/v1/search/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [sentiment](recipes/java/speech-to-text/v1/sentiment/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [smart-format](recipes/java/speech-to-text/v1/smart-format/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [streaming](recipes/java/speech-to-text/v1/streaming/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [streaming-file](recipes/java/speech-to-text/v1/streaming-file/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [summarize](recipes/java/speech-to-text/v1/summarize/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [topics](recipes/java/speech-to-text/v1/topics/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [transcribe-file](recipes/java/speech-to-text/v1/transcribe-file/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [transcribe-url](recipes/java/speech-to-text/v1/transcribe-url/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [utterances](recipes/java/speech-to-text/v1/utterances/) | Java | speech-to-text | v1 | ❌ ✅ | — no run |
| [streaming](recipes/java/speech-to-text/v2/streaming/) | Java | speech-to-text | v2 | ❌ ✅ | — no run |
| [transcribe-url](recipes/java/speech-to-text/v2/transcribe-url/) | Java | speech-to-text | v2 | ❌ ✅ | — no run |
| [generate-audio](recipes/java/text-to-speech/v1/generate-audio/) | Java | text-to-speech | v1 | ❌ ✅ | — no run |
| [select-encoding](recipes/java/text-to-speech/v1/select-encoding/) | Java | text-to-speech | v1 | ❌ ✅ | — no run |
| [select-model](recipes/java/text-to-speech/v1/select-model/) | Java | text-to-speech | v1 | ❌ ✅ | — no run |
| [stream-audio](recipes/java/text-to-speech/v1/stream-audio/) | Java | text-to-speech | v1 | ❌ ✅ | — no run |
| [websocket-streaming](recipes/java/text-to-speech/v1/websocket-streaming/) | Java | text-to-speech | v1 | ❌ ✅ | — no run |
| [connect](recipes/java/voice-agents/v1/connect/) | Java | voice-agents | v1 | ❌ ✅ | — no run |
| [custom-llm](recipes/java/voice-agents/v1/custom-llm/) | Java | voice-agents | v1 | ❌ ✅ | — no run |
| [custom-tts](recipes/java/voice-agents/v1/custom-tts/) | Java | voice-agents | v1 | ❌ ✅ | — no run |
| [function-calling](recipes/java/voice-agents/v1/function-calling/) | Java | voice-agents | v1 | ❌ ✅ | — no run |
| [entities](recipes/javascript/audio-intelligence/v1/entities/) | JavaScript | audio-intelligence | v1 | ✅ ✅ | — no run |
| [intents](recipes/javascript/audio-intelligence/v1/intents/) | JavaScript | audio-intelligence | v1 | ✅ ✅ | — no run |
| [sentiment](recipes/javascript/audio-intelligence/v1/sentiment/) | JavaScript | audio-intelligence | v1 | ✅ ✅ | — no run |
| [summarize](recipes/javascript/audio-intelligence/v1/summarize/) | JavaScript | audio-intelligence | v1 | ✅ ✅ | — no run |
| [topics](recipes/javascript/audio-intelligence/v1/topics/) | JavaScript | audio-intelligence | v1 | ✅ ✅ | — no run |
| [detect-entities](recipes/javascript/speech-to-text/v1/detect-entities/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [detect-language](recipes/javascript/speech-to-text/v1/detect-language/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [diarize](recipes/javascript/speech-to-text/v1/diarize/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [intents](recipes/javascript/speech-to-text/v1/intents/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [keywords](recipes/javascript/speech-to-text/v1/keywords/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [multichannel](recipes/javascript/speech-to-text/v1/multichannel/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [paragraphs](recipes/javascript/speech-to-text/v1/paragraphs/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [punctuate](recipes/javascript/speech-to-text/v1/punctuate/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [redact](recipes/javascript/speech-to-text/v1/redact/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [search](recipes/javascript/speech-to-text/v1/search/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [sentiment](recipes/javascript/speech-to-text/v1/sentiment/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [smart-format](recipes/javascript/speech-to-text/v1/smart-format/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [streaming](recipes/javascript/speech-to-text/v1/streaming/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [streaming-file](recipes/javascript/speech-to-text/v1/streaming-file/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [summarize](recipes/javascript/speech-to-text/v1/summarize/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [topics](recipes/javascript/speech-to-text/v1/topics/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [transcribe-file](recipes/javascript/speech-to-text/v1/transcribe-file/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [transcribe-url](recipes/javascript/speech-to-text/v1/transcribe-url/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [utterances](recipes/javascript/speech-to-text/v1/utterances/) | JavaScript | speech-to-text | v1 | ✅ ✅ | — no run |
| [streaming](recipes/javascript/speech-to-text/v2/streaming/) | JavaScript | speech-to-text | v2 | ✅ ✅ | — no run |
| [transcribe-url](recipes/javascript/speech-to-text/v2/transcribe-url/) | JavaScript | speech-to-text | v2 | ✅ ✅ | — no run |
| [generate-audio](recipes/javascript/text-to-speech/v1/generate-audio/) | JavaScript | text-to-speech | v1 | ✅ ✅ | — no run |
| [select-encoding](recipes/javascript/text-to-speech/v1/select-encoding/) | JavaScript | text-to-speech | v1 | ✅ ✅ | — no run |
| [select-model](recipes/javascript/text-to-speech/v1/select-model/) | JavaScript | text-to-speech | v1 | ✅ ✅ | — no run |
| [stream-audio](recipes/javascript/text-to-speech/v1/stream-audio/) | JavaScript | text-to-speech | v1 | ✅ ✅ | — no run |
| [websocket-streaming](recipes/javascript/text-to-speech/v1/websocket-streaming/) | JavaScript | text-to-speech | v1 | ✅ ✅ | — no run |
| [connect](recipes/javascript/voice-agents/v1/connect/) | JavaScript | voice-agents | v1 | ✅ ✅ | — no run |
| [custom-llm](recipes/javascript/voice-agents/v1/custom-llm/) | JavaScript | voice-agents | v1 | ✅ ✅ | — no run |
| [custom-tts](recipes/javascript/voice-agents/v1/custom-tts/) | JavaScript | voice-agents | v1 | ✅ ✅ | — no run |
| [function-calling](recipes/javascript/voice-agents/v1/function-calling/) | JavaScript | voice-agents | v1 | ✅ ✅ | — no run |
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
