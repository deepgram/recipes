# Transcribe Audio from URL (Speech-to-Text v2)

v2 API for transcribing English audio from URLs.

## What it does

This example demonstrates how to transcribe audio from a URL using Deepgram's Speech-to-Text v2 API. The v2 API is specifically designed for English audio transcription and provides enhanced accuracy and formatting capabilities for URL-based audio processing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Uses the Nova-3 model for high-accuracy transcription |
| `smart_format` | `true` | Applies intelligent formatting to the transcript |

## Example output

```
Yeah, as you mentioned...
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```