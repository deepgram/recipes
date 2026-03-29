# Intent Recognition (Audio Intelligence v1)

Detects speaker intents from conversational context.

## What it does

This example demonstrates how to identify speaker intents from audio conversations using Deepgram's Audio Intelligence API. The service analyzes conversational patterns and context to determine what the speaker is trying to accomplish or communicate.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `intents` | `true` | Enables intent recognition in the transcription |

## Example output

```
Intent: inform
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