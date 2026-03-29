# Stream File for Transcription (Speech-to-Text v1)

Stream an entire audio file over WebSocket connection for transcription. This approach combines the benefits of streaming (real-time results) with file-based processing (complete audio available upfront).

## What this demonstrates

File streaming allows you to process a complete audio file using the streaming WebSocket API instead of the REST API. This is useful when you want to receive transcription results progressively as the file is processed, rather than waiting for the entire file to be transcribed before getting results.

## Key parameters

- `Model = "nova-3"` — Deepgram's highest-accuracy speech model
- `SmartFormat = true` — Formats numbers, dates, currencies automatically
- `SampleRate = 16000` — Audio sample rate (16kHz)
- `Channels = 1` — Single-channel audio
- `Encoding = "linear16"` — 16-bit linear PCM encoding

## Example output

```
Transcript: Neil Armstrong became the first human
Transcript: Neil Armstrong became the first human to step foot on the moon
Transcript: Neil Armstrong became the first human to step foot on the moon on July twentieth nineteen sixty nine.
```

## Prerequisites

- .NET 8.0 or later
- `DEEPGRAM_API_KEY` environment variable set to your Deepgram API key

## Run the example

```bash
dotnet run
```

The example downloads the demo audio file, then streams it in chunks over the WebSocket connection. Unlike live streaming, this approach has the complete file available, so it can use larger chunks for faster processing while still providing progressive transcription results.