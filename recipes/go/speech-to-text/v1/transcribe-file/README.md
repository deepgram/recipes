# Transcribe Local Audio File (Speech-to-Text v1)

Transcribe audio from a local file using Deepgram's nova-3 model with temporary file handling.

## What it does

This example shows how to transcribe audio from a local file by first downloading a sample audio file, then using Deepgram's file-based transcription API. It includes proper temporary file management with automatic cleanup.

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