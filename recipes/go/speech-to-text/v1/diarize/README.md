# Speaker Diarization (Speech-to-Text v1)

Identify and separate different speakers in audio using Deepgram's speaker diarization feature.

## What it does

Speaker diarization automatically identifies when different people are speaking and labels each word with a speaker ID. This enables you to distinguish between multiple speakers in conversations, meetings, or interviews without manual intervention.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `diarize` | `true` | Enables automatic speaker identification and labeling |

## Example output

```
Speaker Diarization Results:
Speaker 0: That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```