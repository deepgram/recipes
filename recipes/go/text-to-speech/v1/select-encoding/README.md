# Select Audio Encoding (Text-to-Speech v1)

Choose specific audio encoding formats for text-to-speech output.

## What it does

This example demonstrates how to specify audio encoding formats when generating speech from text using Deepgram's Text-to-Speech API. You can select from various encoding formats like WAV, MP3, and others to match your application's requirements.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `encoding` | `"mp3"` | Specifies the output audio encoding format |

## Example output

```
Encoding: audio/mpeg
Audio saved: 5678 bytes
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```