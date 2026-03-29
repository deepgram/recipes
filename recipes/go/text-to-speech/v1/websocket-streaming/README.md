# WebSocket Streaming TTS (Text-to-Speech v1)

Low-latency text-to-speech via WebSocket connection.

## What it does

This example demonstrates how to use Deepgram's Text-to-Speech WebSocket API for low-latency speech generation. The WebSocket connection allows for faster audio generation and streaming compared to traditional HTTP requests, making it ideal for real-time applications.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"aura-2-thalia-en"` | Specifies the voice model to use for speech generation |
| `encoding` | `"linear16"` | Sets the audio encoding format for streaming |

## Example output

```
WebSocket TTS streaming complete
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```