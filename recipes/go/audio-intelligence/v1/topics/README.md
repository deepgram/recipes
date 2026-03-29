# Topic Detection (Audio Intelligence v1)

Identifies key topics discussed in transcribed audio.

## What it does

This example demonstrates how to detect and categorize topics from audio using Deepgram's Audio Intelligence API. The service analyzes the transcript content to identify the main subjects and themes being discussed throughout the audio.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `topics` | `true` | Enables topic detection in the transcription |

## Example output

```
Topic: space exploration
  Text: ...
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```