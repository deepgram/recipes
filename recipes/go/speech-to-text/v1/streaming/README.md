# Live Streaming Transcription (Speech-to-Text v1)

WebSocket-based real-time transcription of live audio streams.

## What it does

This example demonstrates how to transcribe live audio in real-time using Deepgram's Speech-to-Text WebSocket API. The connection allows you to stream audio data and receive immediate transcription results as the audio is being processed.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Uses the Nova-3 model for high-accuracy transcription |
| `smart_format` | `true` | Applies intelligent formatting to the transcript |

## Example output

```
Streaming transcription started...
[Transcript results]
Streaming complete
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```