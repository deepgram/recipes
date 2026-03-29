# Stream Audio Response (Text-to-Speech v1)

Stream text-to-speech audio for real-time playback.

## What it does

This example demonstrates how to stream audio directly from Deepgram's Text-to-Speech API rather than saving to a file. This approach allows for real-time audio playback and reduces latency by processing the audio stream as it's generated.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"aura-2-thalia-en"` | Specifies the voice model to use for speech generation |
| `encoding` | `"linear16"` | Sets the audio encoding format for streaming |

## Example output

```
Streamed audio: 12345 bytes
Content-Type: audio/wav
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```