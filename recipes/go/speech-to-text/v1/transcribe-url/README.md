# Transcribe Audio from URL (Speech-to-Text v1)

Transcribe audio directly from a URL using Deepgram's nova-3 model for high-accuracy speech recognition.

## What it does

This example demonstrates basic audio transcription by providing a URL to an audio file. The nova-3 model provides enhanced accuracy compared to the base model, making it ideal for production applications requiring high-quality transcription output.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | High-accuracy speech recognition model with improved performance |

## Example output

```
Transcript: That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```