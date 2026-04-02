# Filler Words (Speech-to-Text v1)

Captures filler words like "uh", "um", "mhm", and "uh huh" in the transcript output. By default, Deepgram omits these disfluencies to produce cleaner transcripts. Enabling filler words is useful for verbatim transcription, conversation analysis, or speaker coaching tools.

## What it does

When `filler_words` is enabled, the transcript includes spoken hesitations and fillers that would otherwise be silently removed. This gives a more accurate representation of exactly what was spoken.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `filler_words` | `true` | Include filler words (uh, um, etc.) in the transcript |
| `model` | `nova-3` | High-accuracy speech recognition model |

## Example output

```
Transcript (with filler words): That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
