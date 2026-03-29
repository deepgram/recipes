# Language Detection (Speech-to-Text v1)

Automatically detect the language spoken in audio and get both the detected language code and transcript.

## What it does

Analyzes the audio to automatically identify the spoken language without requiring you to specify it beforehand. This is useful for multi-language content, international calls, or when the language is unknown.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `DetectLanguage` | `true` | Enables automatic language detection |

## Example output

```
Detected Language: en
Transcript: Yeah, as as much as it's worth celebrating, the first, spacewalk, with an all female team, I think many of us are looking forward to it just being normal and I think if it signifies anything, it is to honour the the women who came before us who were skilled and qualified, but didn't have the same opportunities that we have today.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```