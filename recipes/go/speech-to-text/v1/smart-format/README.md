# Smart Format (Speech-to-Text v1)

Automatically format numbers, dates, times, and currency in transcripts using Deepgram's smart formatting feature.

## What it does

Smart formatting converts spoken numbers, dates, times, and currency into their written forms automatically. Instead of "one hundred twenty three dollars", you get "$123". This feature improves transcript readability and reduces post-processing needs.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `smart_format` | `true` | Enables automatic formatting of numbers, dates, times, and currency |

## Example output

```
Smart Formatted Transcript: That's 1 small step for man, 1 giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```