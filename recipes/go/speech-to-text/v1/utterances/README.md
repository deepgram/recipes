# Utterances (Speech-to-Text v1)

Segment transcripts into speaker-based utterances with precise timing information using Deepgram's utterance detection.

## What it does

Utterances automatically group spoken content by speaker turns, providing structured segments with start/end timestamps and speaker identification. This is useful for conversation analysis, meeting transcription, and multi-speaker content processing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `utterances` | `true` | Enables speaker-based utterance segmentation with timing |

## Example output

```
Utterances:
Utterance 1 (Speaker 0): That's one small step for man, one giant leap for mankind.
  Start: 0.50s, End: 4.20s
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```