# Profanity Filter (Speech-to-Text v1)

Masks profanity in the transcript output by replacing profane words with asterisks. This is useful for content moderation, broadcasting, and any application where clean language output is required.

## What it does

When `profanity_filter` is enabled, any recognized profanity in the audio is masked in the transcript output (e.g., profane words appear as "f***" or similar). The rest of the transcript remains unchanged.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `profanity_filter` | `true` | Mask profanity with asterisks in the transcript |
| `model` | `nova-3` | High-accuracy speech recognition model |

## Example output

```
Transcript (profanity filtered): That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
