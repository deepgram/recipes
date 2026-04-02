# Dictation Mode (Speech-to-Text v1)

Formats transcript using dictation-style spoken punctuation commands. When enabled, words like "period", "comma", or "new paragraph" spoken aloud are converted into their corresponding punctuation marks rather than being transcribed literally.

## What it does

Dictation mode is designed for scenarios where speakers dictate text and verbally indicate punctuation. For example, saying "Hello comma how are you period" would produce "Hello, how are you." instead of the literal words.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `dictation` | `true` | Converts spoken punctuation commands into punctuation marks |
| `model` | `nova-3` | High-accuracy speech recognition model |

## Example output

```
Transcript (dictation mode): That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
