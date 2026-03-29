# Live Streaming Transcription (Speech-to-Text v1)

Real-time speech transcription using WebSocket connection. This example demonstrates how to stream audio data and receive transcriptions in real-time as the audio is being processed.

## What this demonstrates

Live streaming transcription allows you to send audio data in real-time over a WebSocket connection and receive transcription results as they become available. This is ideal for applications that need immediate transcription feedback, such as live captioning, voice assistants, or real-time meeting transcription.

## Key parameters

- `Model = "nova-3"` — Deepgram's highest-accuracy speech model
- `Punctuate = true` — Adds punctuation to transcripts
- `SmartFormat = true` — Formats numbers, dates, currencies automatically
- `SampleRate = 16000` — Audio sample rate (16kHz)
- `Channels = 1` — Single-channel audio
- `Encoding = "linear16"` — 16-bit linear PCM encoding

## Example output

```
Transcript: Neil Armstrong
Transcript: That's one small step for man,
Transcript: That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- .NET 8.0 or later
- `DEEPGRAM_API_KEY` environment variable set to your Deepgram API key

## Run the example

```bash
dotnet run
```

The example downloads the demo audio file, then streams it in chunks to simulate real-time audio input, showing how transcription results arrive progressively as audio is processed.