# Entity Detection (Audio Intelligence v1)

Identifies named entities (people, places, organisations) from transcribed audio.

## What it does

This example demonstrates how to extract named entities from audio using Deepgram's Audio Intelligence API. The service automatically identifies and categorizes entities like person names, locations, and organizations found in the transcript.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `detect_entities` | `true` | Enables entity detection in the transcription |

## Example output

```
Transcript: ...
Entities: [{"label": "PER", "value": "Neil Armstrong", "confidence": 0.95, "start_word": 5, "end_word": 6}]
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```