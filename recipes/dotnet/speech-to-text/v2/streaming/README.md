# v2 Model Streaming Transcription (Speech-to-Text v2)

Real-time speech transcription using Deepgram's v2 model (`flux-general-en`) over WebSocket connection. This combines the benefits of streaming with the enhanced accuracy of the v2 English-optimized model.

## What this demonstrates

Streaming with the v2 model provides real-time transcription using Deepgram's latest English-optimized speech recognition model. The `flux-general-en` model offers improved accuracy for conversational speech, better handling of background noise, and enhanced confidence scoring.

## Key parameters

- `Model = "flux-general-en"` — Deepgram's v2 English-optimized model
- `SmartFormat = true` — Formats numbers, dates, currencies automatically
- `Punctuate = true` — Adds punctuation to transcripts
- `SampleRate = 16000` — Audio sample rate (16kHz)
- `Channels = 1` — Single-channel audio
- `Encoding = "linear16"` — 16-bit linear PCM encoding

## v2 model advantages

- **Enhanced accuracy**: Specifically tuned for English conversational speech
- **Better noise handling**: Improved performance on audio with background noise
- **Higher confidence scores**: More accurate confidence metrics
- **Optimized for streaming**: Better real-time transcription performance

## Example output

```
Streaming audio with v2 model...
Transcript: Neil Armstrong (confidence: 0.98)
Transcript: Neil Armstrong became (confidence: 0.95)
Transcript: Neil Armstrong became the first human to step foot on the moon (confidence: 0.96)
Transcript: Neil Armstrong became the first human to step foot on the moon on July 20th, 1969. (confidence: 0.97)
Streaming completed.
```

## Prerequisites

- .NET 8.0 or later
- `DEEPGRAM_API_KEY` environment variable set to your Deepgram API key

## Run the example

```bash
dotnet run
```

The example downloads the demo audio file and streams it in real-time using the v2 model, showing progressive transcription results with confidence scores that are typically higher and more accurate than v1 models.