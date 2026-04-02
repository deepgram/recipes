# Measurements (Speech-to-Text v1)

Converts spoken measurements to standard abbreviations in the transcript. When enabled, phrases like "five kilograms" become "5 kg" and "ten degrees Celsius" becomes "10°C".

## What it does

The measurements feature automatically formats measurement units mentioned in speech into their standard abbreviated forms. This is useful for transcribing technical content, medical dictation, scientific recordings, or any audio that references physical quantities.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `measurements` | `true` | Convert spoken measurements to standard abbreviations |
| `model` | `nova-3` | High-accuracy speech recognition model |

## Example output

```
Transcript (with measurements): That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
