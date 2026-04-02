# Numerals (Speech-to-Text v1)

Converts spoken numbers to their numeric digit form in the transcript. When enabled, "twenty three" becomes "23" and "one hundred" becomes "100".

## What it does

The numerals feature formats spoken numbers as digits rather than words. This is particularly useful for financial transcriptions, medical records, technical documentation, or any content where numeric precision matters.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `numerals` | `true` | Convert spoken numbers to digit form |
| `model` | `nova-3` | High-accuracy speech recognition model |

## Example output

```
Transcript (with numerals): That's 1 small step for man, 1 giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
