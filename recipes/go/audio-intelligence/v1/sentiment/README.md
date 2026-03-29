# Sentiment Analysis (Audio Intelligence v1)

Provides segment-level sentiment scoring for transcribed audio.

## What it does

This example demonstrates how to analyze sentiment from audio using Deepgram's Audio Intelligence API. The service provides sentiment scores (positive, negative, neutral) for different segments of the transcription with confidence ratings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `sentiment` | `true` | Enables sentiment analysis in the transcription |

## Example output

```
[positive] (0.85) The spacewalk...
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```