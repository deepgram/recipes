# Live Streaming Transcription (Speech-to-Text v2)

v2 WebSocket streaming for real-time transcription.

## What it does

This example demonstrates how to use Deepgram's Speech-to-Text v2 WebSocket API for real-time audio transcription. The v2 API provides enhanced streaming capabilities with improved performance and accuracy for live audio processing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Uses the Nova-3 model for high-accuracy transcription |
| `smart_format` | `true` | Applies intelligent formatting to the transcript |

## Example output

```
[Transcript results]
v2 streaming complete
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```