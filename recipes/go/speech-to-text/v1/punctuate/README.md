# Punctuation (Speech-to-Text v1)

Automatically add punctuation to transcripts using Deepgram's punctuation feature for improved readability.

## What it does

This feature automatically adds punctuation marks like periods, commas, question marks, and exclamation points to transcripts based on speech patterns and pauses. This significantly improves transcript readability without manual post-processing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `punctuate` | `true` | Enables automatic punctuation insertion based on speech patterns |

## Example output

```
Punctuated Transcript: That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```