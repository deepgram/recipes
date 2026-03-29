# Audio Summarization (Audio Intelligence v1)

Generates concise summary of transcribed audio content.

## What it does

This example demonstrates how to generate automated summaries from audio using Deepgram's Audio Intelligence API. The service analyzes the full transcript and creates a concise summary highlighting the key points and main topics discussed.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `summarize` | `"v2"` | Enables audio summarization using version 2 of the summarization model |

## Example output

```
Summary: A news report about...
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```